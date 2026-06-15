#!/usr/bin/env python3
"""
Sync Actas CD from ferrocarriloeste.org.ar into actas-cd/.

This mirrors the public WordPress category and downloads the file attachments
embedded in each acta post. The archive includes PDFs, DOCX files, and image
scans when the post does not expose a PDF.
"""

from __future__ import annotations

import argparse
import dataclasses
import html
import json
import re
import subprocess
import sys
import time
import urllib.parse
import unicodedata
import tempfile
import zipfile
from collections import defaultdict
from dataclasses import dataclass
from pathlib import Path


SITE_URL = "https://www.ferrocarriloeste.org.ar"
API_ROOT = f"{SITE_URL}/wp-json/wp/v2"
CATEGORY_ID = 62  # Actas CD
DEFAULT_OUTDIR = "actas-cd"
USER_AGENT = "CodexActasCDSync/1.0"
ALLOWED_HOST_SUFFIX = "ferrocarriloeste.org.ar"

TITLE_HINT_RE = re.compile(
    r"\b(acta|actas|cd|sesi[oó]n|periodo|per[ií]odo|balance)\b",
    re.IGNORECASE,
)
NUMERIC_DATE_RE = re.compile(r"\b(\d{1,2})[/-](\d{1,2})[/-](\d{2,4})\b")
NUMERIC_DATE_FULL_RE = re.compile(r"\b(\d{1,2})[/-](\d{1,2})[/-]((?:19|20)\d{2})\b")
NUMERIC_DATE_SHORT_RE = re.compile(r"\b(\d{1,2})[/-](\d{1,2})[/-](\d{2})\b")
SPANISH_DATE_RE = re.compile(
    r"\b(\d{1,2})\s+de\s+"
    r"(enero|febrero|marzo|abril|mayo|junio|julio|agosto|septiembre|setiembre|octubre|noviembre|diciembre)"
    r"\s+(?:de|del)\s+(\d{4})\b",
    re.IGNORECASE,
)
MONTH_YEAR_RE = re.compile(
    r"\b(enero|febrero|marzo|abril|mayo|junio|julio|agosto|septiembre|setiembre|octubre|noviembre|diciembre)\s+(\d{4})\b",
    re.IGNORECASE,
)
YEAR_RANGE_RE = re.compile(r"\b((?:19|20)\d{2})\s*[-/]\s*((?:19|20)\d{2})\b")
ACTA_NUM_RE = re.compile(r"\bacta\s+(\d+)\b", re.IGNORECASE)
PERIOD_NUM_RE = re.compile(r"\bper[ií]odo\s+(\d+)\b", re.IGNORECASE)
SESSION_NUM_RE = re.compile(
    r"\b(\d+)\s*(?:°|ra|ta|da|na|ma|va|a)?\s*(?:sesi[oó]n|ordinaria|ordinario)\b",
    re.IGNORECASE,
)
MONTH_CODES = {
    1: "ene",
    2: "feb",
    3: "mar",
    4: "abr",
    5: "may",
    6: "jun",
    7: "jul",
    8: "ago",
    9: "sep",
    10: "oct",
    11: "nov",
    12: "dic",
}
SPANISH_MONTHS = {
    "enero": 1,
    "febrero": 2,
    "marzo": 3,
    "abril": 4,
    "mayo": 5,
    "junio": 6,
    "julio": 7,
    "agosto": 8,
    "septiembre": 9,
    "setiembre": 9,
    "octubre": 10,
    "noviembre": 11,
    "diciembre": 12,
}
IMAGE_EXTENSIONS = {".jpg", ".jpeg", ".png", ".gif", ".webp"}
FILE_EXTENSIONS = {".pdf", ".doc", ".docx"} | IMAGE_EXTENSIONS
CODE_STOPWORDS = {
    "acta",
    "actas",
    "balance",
    "cd",
    "comision",
    "de",
    "del",
    "directiva",
    "el",
    "en",
    "general",
    "la",
    "las",
    "los",
    "ordinaria",
    "ordinario",
    "periodo",
    "período",
    "sesion",
    "sesiones",
    "y",
}


@dataclass
class AttachmentRecord:
    post_id: int
    post_date: str
    event_date: str
    title: str
    slug: str
    post_url: str
    source_url: str
    local_file: str
    kind: str
    reference: str
    note: str = ""


def main() -> int:
    parser = argparse.ArgumentParser(description="Sync Ferro Actas CD")
    parser.add_argument(
        "--outdir",
        default=DEFAULT_OUTDIR,
        help="Directory that will receive the files and generated index",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Collect metadata without downloading files or writing indexes",
    )
    args = parser.parse_args()

    posts = fetch_posts(CATEGORY_ID)
    records = collect_records(posts)

    if args.dry_run:
        for record in records:
            print(format_record_line(record))
        return 0

    outdir = Path(args.outdir)
    outdir.mkdir(parents=True, exist_ok=True)
    rename_existing_files(records, outdir)
    download_missing_files(records, outdir)
    write_manifest(records, outdir)
    write_index(records, outdir)

    print(f"downloaded_or_present={len(records)}")
    print(f"index={outdir / 'index.md'}")
    print(f"manifest={outdir / 'manifest.json'}")
    return 0


def fetch_posts(category_id: int) -> list[dict]:
    posts: list[dict] = []
    page = 1
    while True:
        query = {
            "categories": category_id,
            "status": "publish",
            "per_page": 100,
            "page": page,
            "_fields": "id,date,slug,title,link,content,categories",
        }
        payload = fetch_json("posts", query)
        if not isinstance(payload, list):
            break
        posts.extend(payload)
        if len(payload) < 100:
            break
        page += 1
    posts.sort(key=lambda p: (p.get("date", ""), p.get("id", 0)), reverse=True)
    return posts


def collect_records(posts: list[dict]) -> list[AttachmentRecord]:
    seen_urls: set[str] = set()
    records: list[AttachmentRecord] = []

    for post in posts:
        title = clean_text(post["title"]["rendered"])
        content = post["content"]["rendered"]
        attachments = extract_attachment_urls(content)
        if not attachments:
            continue

        if not TITLE_HINT_RE.search(title) and not TITLE_HINT_RE.search(clean_text(content)):
            continue

        post_date = post.get("date", "")[:10]
        slug = post.get("slug", "")
        post_url = post.get("link", "")
        reference = infer_reference(title, slug, post_date, attachments)
        kind = classify_kind(title)
        event_date = infer_event_date(title, slug, reference, attachments, post_date)

        if kind == "cd-acta" and event_date == "2025-09-18" and "septiembre 2025" in normalize_text(title):
            reference = "Período 101 - Sesión 22"

        note = build_note(title, attachments)

        for idx, source_url in enumerate(attachments, start=1):
            canonical_url = normalize_source_url(source_url)
            if not is_local_url(canonical_url):
                continue
            if canonical_url in seen_urls:
                continue
            seen_urls.add(canonical_url)

            document_code = build_document_code(title, slug, reference, canonical_url)
            if kind == "cd-acta" and event_date == "2025-09-18" and "septiembre 2025" in normalize_text(title):
                document_code = "p101-s022"

            local_file = build_local_filename(event_date, kind, document_code, canonical_url, len(attachments), idx)
            records.append(
                AttachmentRecord(
                    post_id=int(post["id"]),
                    post_date=post_date,
                    event_date=event_date,
                    title=title,
                    slug=slug,
                    post_url=post_url,
                    source_url=canonical_url,
                    local_file=local_file,
                    kind=kind,
                    reference=reference,
                    note=note,
                )
            )

    records.sort(key=lambda r: (r.event_date, r.post_date, r.kind, r.title, r.local_file), reverse=True)
    return records


def classify_kind(title: str) -> str:
    lowered = title.lower()
    if "balance" in lowered or "memoria y balance" in lowered:
        return "cd-balance"
    return "cd-acta"


def infer_reference(title: str, slug: str, post_date: str, attachments: list[str]) -> str:
    for candidate in [title, slug, *[Path(urllib.parse.urlparse(u).path).name for u in attachments]]:
        ref = extract_reference(candidate)
        if ref:
            return ref
    return post_date or "unknown"


def infer_event_date(title: str, slug: str, reference: str, attachments: list[str], post_date: str) -> str:
    candidates = [title, slug, reference, *[Path(urllib.parse.urlparse(u).path).name for u in attachments]]
    for candidate in candidates:
        event_date = extract_exact_date(candidate)
        if event_date:
            return event_date

    for attachment in attachments:
        if Path(urllib.parse.urlparse(attachment).path).suffix.lower() != ".docx":
            continue
        docx_date = extract_docx_event_date(attachment)
        if docx_date:
            return docx_date

    return post_date


def extract_exact_date(text: str) -> str | None:
    if not text:
        return None

    compact = clean_text(text)
    compact = re.sub(r"\s*([/-])\s*", r"\1", compact)

    for pattern in (NUMERIC_DATE_FULL_RE, NUMERIC_DATE_SHORT_RE):
        for match in pattern.finditer(compact):
            event_date = normalize_iso_date(match.group(1), match.group(2), match.group(3))
            if event_date:
                return event_date

    normalized = normalize_text(text)
    match = SPANISH_DATE_RE.search(normalized)
    if match:
        day, month_name, year = match.groups()
        return normalize_iso_date(day, str(SPANISH_MONTHS[month_name.lower()]), year)

    return None


def extract_docx_event_date(docx_url: str) -> str | None:
    with tempfile.TemporaryDirectory() as tmpdir:
        docx_path = Path(tmpdir) / "attachment.docx"
        try:
            subprocess.run(
                [
                    "curl",
                    "-fsSL",
                    "--max-time",
                    "60",
                    docx_url,
                    "-o",
                    str(docx_path),
                ],
                check=True,
                capture_output=True,
                text=True,
            )
        except subprocess.CalledProcessError:
            return None

        try:
            with zipfile.ZipFile(docx_path) as archive:
                xml = archive.read("word/document.xml").decode("utf-8", errors="ignore")
        except (FileNotFoundError, KeyError, OSError, zipfile.BadZipFile):
            return None

    text = re.sub(r"<w:tab/>", "\t", xml)
    text = re.sub(r"</w:p>", "\n", text)
    text = re.sub(r"<[^>]+>", "", text)
    text = html.unescape(text)
    return extract_exact_date(text)


def normalize_iso_date(day: str, month: str, year: str) -> str | None:
    day_int = int(day)
    month_int = int(month)
    year_int = int(year)
    if year_int < 100:
        year_int += 2000
    if not (1 <= day_int <= 31 and 1 <= month_int <= 12):
        return None
    return f"{year_int:04d}-{month_int:02d}-{day_int:02d}"


def build_note(title: str, attachments: list[str]) -> str:
    if "cd" in title.lower() and any(Path(urllib.parse.urlparse(u).path).suffix.lower() == ".docx" for u in attachments):
        return "Fuente original en Word."
    if any(Path(urllib.parse.urlparse(u).path).suffix.lower() in IMAGE_EXTENSIONS for u in attachments):
        return "Acta publicada como imágenes."
    return ""


def extract_reference(text: str) -> str | None:
    if not text:
        return None

    normalized = normalize_text(text)

    match = NUMERIC_DATE_RE.search(text)
    if match:
        return normalize_numeric_date(match.group(1), match.group(2), match.group(3))

    match = SPANISH_DATE_RE.search(normalized)
    if match:
        day, month_name, year = match.groups()
        return normalize_numeric_date(day, str(SPANISH_MONTHS[month_name.lower()]), year)

    match = MONTH_YEAR_RE.search(normalized)
    if match:
        month_name, year = match.groups()
        return f"{month_name.lower()} {year}"

    match = ACTA_NUM_RE.search(normalized)
    if match:
        return f"Acta {match.group(1)}"

    match = SESSION_NUM_RE.search(normalized)
    if match:
        return f"Sesion {match.group(1)}"

    return None


def extract_attachment_urls(content: str) -> list[str]:
    content = html.unescape(content)
    urls: list[str] = []

    # Standard links to PDFs, DOCX files, or images.
    for match in re.finditer(
        r'https?://[^\s"\'<>«»]+?(?:pdf|docx?|jpe?g|png|gif|webp)(?:[^\s"\'<>«»]*)?',
        content,
        re.IGNORECASE,
    ):
        urls.append(match.group(0))

    # Links or shortcodes that point to an attachment.
    for match in re.finditer(r'(?:href|file|data-src|data-lazy-src)=["\']([^"\']+)["\']', content, re.IGNORECASE):
        candidate = match.group(1)
        if looks_like_attachment(candidate):
            urls.append(candidate)

    # Images: prefer the largest source from srcset, otherwise src.
    for tag in re.finditer(r'<img\b[^>]*>', content, re.IGNORECASE):
        tag_html = tag.group(0)
        srcset = re.search(r'srcset=["\']([^"\']+)["\']', tag_html, re.IGNORECASE)
        if srcset:
            selected = choose_best_srcset_url(srcset.group(1))
            if selected:
                urls.append(selected)
                continue
        src = re.search(r'src=["\']([^"\']+)["\']', tag_html, re.IGNORECASE)
        if src:
            urls.append(src.group(1))

    deduped: list[str] = []
    seen: set[str] = set()
    for url in urls:
        normalized = normalize_source_url(url)
        if not normalized:
            continue
        if not is_attachment_url(normalized):
            continue
        if normalized not in seen:
            seen.add(normalized)
            deduped.append(normalized)
    return deduped


def choose_best_srcset_url(srcset: str) -> str | None:
    best_url = None
    best_width = -1
    for item in srcset.split(","):
        candidate = item.strip()
        if not candidate:
            continue
        parts = candidate.rsplit(" ", 1)
        url = parts[0].strip()
        width = 0
        if len(parts) == 2 and parts[1].endswith("w"):
            try:
                width = int(parts[1][:-1])
            except ValueError:
                width = 0
        if width >= best_width:
            best_width = width
            best_url = url
    return best_url


def looks_like_attachment(url: str) -> bool:
    path = urllib.parse.urlparse(url).path.lower()
    return any(path.endswith(ext) for ext in FILE_EXTENSIONS)


def is_attachment_url(url: str) -> bool:
    path = urllib.parse.urlparse(url).path.lower()
    return any(path.endswith(ext) for ext in FILE_EXTENSIONS)


def normalize_source_url(url: str) -> str:
    url = html.unescape(url).strip()
    url = re.split(r'[<>"\'«»]', url)[0]
    url = url.rstrip("])>,")

    parsed = urllib.parse.urlparse(url)
    path = parsed.path
    path = re.sub(r"-\d+x\d+(?=\.[A-Za-z0-9]+$)", "", path)
    normalized = urllib.parse.urlunparse(
        (
            parsed.scheme,
            parsed.netloc,
            path,
            parsed.params,
            parsed.query,
            parsed.fragment,
        )
    )
    return normalized


def is_local_url(url: str) -> bool:
    parsed = urllib.parse.urlparse(url)
    return parsed.netloc.lower().endswith(ALLOWED_HOST_SUFFIX)


def build_document_code(title: str, slug: str, reference: str, source_url: str) -> str:
    candidate_texts = [reference, title, slug, Path(urllib.parse.urlparse(source_url).path).name]

    period = extract_first_match(PERIOD_NUM_RE, candidate_texts)
    session = extract_first_match(SESSION_NUM_RE, candidate_texts)
    acta = extract_first_match(ACTA_NUM_RE, candidate_texts)
    if period and session:
        return f"p{int(period):03d}-s{int(session):03d}"
    if period and acta:
        return f"p{int(period):03d}-a{int(acta):03d}"
    if period:
        return f"p{int(period):03d}"
    if session:
        return f"s{int(session):03d}"
    if acta:
        return f"a{int(acta):03d}"

    month_year = extract_month_year_code(candidate_texts)
    if month_year:
        return month_year

    year_range = extract_year_range(candidate_texts)
    if year_range:
        return year_range

    year = extract_year(candidate_texts)
    if year:
        return year

    compact = compact_code_from_text(
        title,
        reference,
        slug,
        prefix=None,
        max_tokens=4,
        drop_words=CODE_STOPWORDS,
    )
    return compact or "document"


def build_local_filename(
    event_date: str,
    kind: str,
    document_code: str,
    source_url: str,
    total_parts: int,
    part_index: int,
) -> str:
    basename = Path(urllib.parse.urlparse(source_url).path).name
    parts = [event_date or "undated", slugify(kind) or "document", slugify(document_code) or "item"]
    if total_parts > 1:
        parts.append(f"part-{part_index:02d}")
    ext = normalize_local_extension(Path(basename).suffix.lower() or ".bin")
    filename = "__".join(parts) + ext
    return str(Path("balances") / filename) if kind == "cd-balance" else filename


def normalize_local_extension(ext: str) -> str:
    if ext == ".jpeg":
        return ".jpg"
    return ext


def extract_first_match(pattern: re.Pattern[str], texts: list[str]) -> str | None:
    for text in texts:
        if not text:
            continue
        match = pattern.search(normalize_text(text))
        if match:
            return match.group(1)
    return None


def extract_year_range(texts: list[str]) -> str | None:
    for text in texts:
        if not text:
            continue
        match = YEAR_RANGE_RE.search(clean_text(text))
        if not match:
            continue
        start = int(match.group(1))
        end = int(match.group(2))
        if start > end:
            start, end = end, start
        return f"{start:04d}-{end:04d}"
    return None


def extract_year(texts: list[str]) -> str | None:
    for text in texts:
        if not text:
            continue
        match = re.search(r"\b((?:19|20)\d{2})\b", clean_text(text))
        if match:
            return match.group(1)
    return None


def extract_month_year_code(texts: list[str]) -> str | None:
    for text in texts:
        if not text:
            continue
        normalized = normalize_text(text)
        match = MONTH_YEAR_RE.search(normalized)
        if match:
            month_name, year = match.groups()
            month_number = SPANISH_MONTHS[month_name.lower()]
            return f"{MONTH_CODES[month_number]}-{year}"
    return None


def compact_code_from_text(
    *texts: str,
    prefix: str | None = None,
    max_tokens: int = 4,
    drop_words: set[str] | None = None,
) -> str:
    drop = {word.lower() for word in (drop_words or set())}
    tokens: list[str] = []

    for text in texts:
        if not text:
            continue
        normalized = normalize_text(text)
        normalized = re.sub(r"(?<=\d)(?=[a-z])", " ", normalized)
        normalized = re.sub(r"(?<=[a-z])(?=\d)", " ", normalized)
        for raw_token in re.findall(r"[a-z0-9]+", normalized):
            token = raw_token
            if token in drop:
                continue
            if token.isdigit() and len(token) == 4 and token.startswith(("19", "20")):
                continue
            if token in SPANISH_MONTHS:
                token = MONTH_CODES[SPANISH_MONTHS[token]]
            tokens.append(token)
            if len(tokens) >= max_tokens:
                break
        if len(tokens) >= max_tokens:
            break

    code = "-".join(tokens[:max_tokens])
    if not code:
        return prefix or ""
    if prefix:
        return f"{prefix}-{code}"
    return code


def slugify(text: str) -> str:
    text = clean_text(text).lower()
    text = re.sub(r"[^a-z0-9]+", "-", text)
    return re.sub(r"-+", "-", text).strip("-")


def rename_existing_files(records: list[AttachmentRecord], outdir: Path) -> None:
    manifest_path = outdir / "manifest.json"
    if not manifest_path.exists():
        return

    try:
        existing = json.loads(manifest_path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return

    old_by_source: dict[str, str] = {}
    for item in existing.get("records", []):
        source_url = item.get("source_url")
        local_file = item.get("local_file")
        if isinstance(source_url, str) and isinstance(local_file, str):
            old_by_source[source_url] = local_file

    for record in records:
        old_local_file = old_by_source.get(record.source_url)
        if not old_local_file or old_local_file == record.local_file:
            continue

        old_path = outdir / old_local_file
        new_path = outdir / record.local_file
        new_path.parent.mkdir(parents=True, exist_ok=True)
        if old_path.exists() and not new_path.exists():
            old_path.rename(new_path)


def clean_text(text: str) -> str:
    text = html.unescape(text)
    text = re.sub(r"<[^>]+>", "", text)
    return re.sub(r"\s+", " ", text).strip()


def normalize_text(text: str) -> str:
    text = html.unescape(text)
    text = unicodedata.normalize("NFKD", text)
    text = "".join(ch for ch in text if not unicodedata.combining(ch))
    text = text.replace("_", " ")
    text = text.replace("-", " ")
    text = text.replace("/", " ")
    text = re.sub(
        r"(\d+(?:ra|ta|da|na|ma))(?=(?:ordinaria|ordinario|sesion|sesi[oó]n)\b)",
        r"\1 ",
        text,
        flags=re.IGNORECASE,
    )
    return re.sub(r"\s+", " ", text).strip().lower()


def normalize_numeric_date(day: str, month: str, year: str) -> str:
    day_int = int(day)
    month_int = int(month)
    year_int = int(year)
    if year_int < 100:
        year_int += 2000
    return f"{day_int:02d}/{month_int:02d}/{year_int:04d}"


def download_missing_files(records: list[AttachmentRecord], outdir: Path) -> None:
    for record in records:
        local_path = outdir / record.local_file
        local_path.parent.mkdir(parents=True, exist_ok=True)
        if local_path.exists():
            continue
        try:
            run_curl(
                [
                    "curl",
                    "-fsSL",
                    "--max-time",
                    "60",
                    record.source_url,
                    "-o",
                    str(local_path),
                ]
            )
        except subprocess.CalledProcessError as exc:
            print(f"skip {record.source_url} ({exc})", file=sys.stderr)


def write_manifest(records: list[AttachmentRecord], outdir: Path) -> None:
    extensions = {}
    for record in records:
        ext = Path(urllib.parse.urlparse(record.source_url).path).suffix.lower() or ".bin"
        extensions[ext] = extensions.get(ext, 0) + 1

    payload = {
        "site": SITE_URL,
        "category_id": CATEGORY_ID,
        "count": len(records),
        "extensions": dict(sorted(extensions.items())),
        "records": [dataclasses.asdict(record) for record in records],
    }
    (outdir / "manifest.json").write_text(
        json.dumps(payload, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )


def write_index(records: list[AttachmentRecord], outdir: Path) -> None:
    lines = [
        "# Documentos de Comisión Directiva",
        "",
        f"Documentos reunidos: {len(records)}",
        "",
        "Esta carpeta reúne actas y balances públicos de la Comisión Directiva. Los documentos están ordenados del más reciente al más antiguo.",
        "",
        "## Qué conviene saber",
        "- Cuando una publicación tiene varias partes, cada archivo aparece por separado.",
    ]
    summary_lines = build_summary_lines(records)
    if summary_lines:
        lines.extend([""] + summary_lines)

    lines.extend([
        "",
        "## Listado",
        "",
        "| Fecha | Publicación | Tipo | Referencia | Título | Archivo | Enlace | Observaciones |",
        "| --- | --- | --- | --- | --- | --- | --- | --- |",
    ])
    for record in records:
        note = record.note.replace("|", "\\|")
        lines.append(
            f"| {record.event_date} | {record.post_date} | {friendly_kind_label(record.kind)} | {format_reference(record)} | {record.title} | "
            f"`{record.local_file}` | {record.source_url} | {note} |"
        )
    (outdir / "index.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def format_record_line(record: AttachmentRecord) -> str:
    return (
        f"{record.event_date} | {record.post_date} | {friendly_kind_label(record.kind)} | {format_reference(record)} | {record.title} | "
        f"{record.local_file} | {record.source_url}"
    )


def format_reference(record: AttachmentRecord) -> str:
    code = extract_local_code(record.local_file)
    if not code:
        if record.kind == "cd-acta" and record.reference.lower().startswith("período 101 - sesión 22"):
            return "P101-S022"
        return record.reference

    if code.lower() == "p101-s022":
        return "P101-S022"

    match = re.fullmatch(r"p(\d{3})-s(\d{3})", code, re.IGNORECASE)
    if match:
        return f"P{int(match.group(1)):03d}-S{int(match.group(2)):03d}"

    match = re.fullmatch(r"p(\d{3})-a(\d{3})", code, re.IGNORECASE)
    if match:
        return f"P{int(match.group(1)):03d}-A{int(match.group(2)):03d}"

    match = re.fullmatch(r"p(\d{3})", code, re.IGNORECASE)
    if match:
        return f"P{int(match.group(1)):03d}"

    match = re.fullmatch(r"ej(\d{3})", code, re.IGNORECASE)
    if match:
        return f"EJ{int(match.group(1)):03d}"

    match = re.fullmatch(r"conv-(\d{4})", code, re.IGNORECASE)
    if match:
        return f"CONV-{match.group(1)}"

    match = re.fullmatch(r"([a-z]{3})-(\d{4})", code, re.IGNORECASE)
    if match:
        month_code = match.group(1).lower()
        month_name = {
            "ene": "Enero",
            "feb": "Febrero",
            "mar": "Marzo",
            "abr": "Abril",
            "may": "Mayo",
            "jun": "Junio",
            "jul": "Julio",
            "ago": "Agosto",
            "sep": "Septiembre",
            "oct": "Octubre",
            "nov": "Noviembre",
            "dic": "Diciembre",
        }.get(month_code, month_code.upper())
        return f"{month_name} {match.group(2)}"

    if code.lower().startswith("tutorial"):
        return "Material de apoyo"

    return code.upper()


def friendly_kind_label(kind: str) -> str:
    return {
        "cd-acta": "Acta de Comisión Directiva",
        "cd-balance": "Balance de Comisión Directiva",
    }.get(kind, kind.replace("-", " ").title())


def build_summary_lines(records: list[AttachmentRecord]) -> list[str]:
    lines: list[str] = ["## Continuidad"]
    gaps = summarize_period_gaps(records)
    if gaps:
        lines.append("En la secuencia hay estos faltantes:")
        for period, missing in gaps:
            lines.append(f"- Período {period}: faltan las sesiones {format_number_list(missing)}.")
    else:
        lines.append("No se ven faltantes de numeración en la secuencia publicada.")

    if any(extract_local_code(record.local_file).lower() == "p101-s022" for record in records):
        lines.append("- La publicación de septiembre de 2025 quedó identificada como P101-S022.")

    return lines


def summarize_period_gaps(records: list[AttachmentRecord]) -> list[tuple[int, list[int]]]:
    by_period: dict[int, set[int]] = defaultdict(set)
    for record in records:
        code = extract_local_code(record.local_file).lower()
        match = re.fullmatch(r"p(\d{3})-(?:s|a)(\d{3})", code)
        if not match:
            continue
        period = int(match.group(1))
        number = int(match.group(2))
        by_period[period].add(number)

    gaps: list[tuple[int, list[int]]] = []
    for period in sorted(by_period):
        numbers = sorted(by_period[period])
        if not numbers:
            continue
        missing = [n for n in range(numbers[0], numbers[-1] + 1) if n not in by_period[period]]
        if missing:
            gaps.append((period, missing))
    return gaps


def format_number_list(numbers: list[int]) -> str:
    if not numbers:
        return ""
    if len(numbers) == 1:
        return str(numbers[0])
    if len(numbers) == 2:
        return f"{numbers[0]} y {numbers[1]}"
    return ", ".join(str(number) for number in numbers[:-1]) + f" y {numbers[-1]}"


def extract_local_code(local_file: str) -> str:
    stem = Path(local_file).stem
    parts = stem.split("__")
    if len(parts) >= 3:
        return parts[2]
    return ""


def fetch_json(endpoint: str, params: dict) -> object:
    url = f"{API_ROOT}/{endpoint}?" + urllib.parse.urlencode(params)
    body = run_curl(
        [
            "curl",
            "-fsSL",
            "-L",
            "--max-time",
            "60",
            url,
        ]
    )
    return json.loads(body)


def run_curl(cmd: list[str], retries: int = 3, delay_seconds: float = 1.5) -> str:
    last_exc: subprocess.CalledProcessError | None = None
    for attempt in range(1, retries + 1):
        try:
            effective_cmd = cmd
            if cmd and cmd[0] == "curl":
                effective_cmd = [
                    "curl",
                    "-4",
                    "--retry",
                    "5",
                    "--retry-all-errors",
                    "--retry-delay",
                    "2",
                ] + cmd[1:]
            proc = subprocess.run(effective_cmd, check=True, capture_output=True, text=True)
            return proc.stdout
        except subprocess.CalledProcessError as exc:
            last_exc = exc
            if exc.stderr:
                print(exc.stderr.strip(), file=sys.stderr)
            if attempt < retries:
                time.sleep(delay_seconds * attempt)
    assert last_exc is not None
    raise last_exc


if __name__ == "__main__":
    raise SystemExit(main())
