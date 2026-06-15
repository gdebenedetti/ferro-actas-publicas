#!/usr/bin/env python3
"""
Sync assembly-related PDFs from ferrocarriloeste.org.ar.

Default behavior:
- query the WordPress API for the public "Actas Asamblea" category
- query posts that mention "asamblea"
- query posts whose titles mention "memoria y balance"
- extract embedded PDF URLs from post content and gview shortcodes
- download missing PDFs into actas-asamblea/
- regenerate actas-asamblea/index.md and actas-asamblea/manifest.json

The script is intentionally conservative. It avoids broad generic keywords like
"acta" or "balance" because those pull in a lot of unrelated commission-directive
material. When the site changes, this is the script to extend.
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
from collections import OrderedDict
from dataclasses import dataclass, field
from pathlib import Path
from typing import Iterable


SITE_URL = "https://www.ferrocarriloeste.org.ar"
API_ROOT = f"{SITE_URL}/wp-json/wp/v2"
DEFAULT_CATEGORY_ID = 71  # Actas Asamblea
DEFAULT_TERMS = ("asamblea", "memoria y balance")
DEFAULT_MEDIA_TERMS = ("asamblea", "memoria y balance")
USER_AGENT = "CodexActasSync/1.0"

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
PERIOD_RE = re.compile(r"\bper[ií]odo\s+(\d+)\b", re.IGNORECASE)
ACTA_NUM_RE = re.compile(r"\bacta\s+(\d+)\b", re.IGNORECASE)
EXERCISE_RE = re.compile(r"\bejercicio\s+(\d+)\b", re.IGNORECASE)
BOARD_ACTA_RE = re.compile(r"^acta\s+\d+\s*/\s*per[ií]odo", re.IGNORECASE)
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
COMMON_CODE_STOPWORDS = {
    "acta",
    "actas",
    "asamblea",
    "balance",
    "cd",
    "comision",
    "convocatoria",
    "del",
    "directiva",
    "el",
    "en",
    "general",
    "la",
    "las",
    "llamado",
    "los",
    "memoria",
    "o",
    "ordinaria",
    "ordinario",
    "para",
    "periodo",
    "por",
    "sesion",
    "sesiones",
    "socios",
    "sobre",
    "un",
    "una",
    "y",
}


@dataclass
class PdfRecord:
    post_id: int
    post_date: str
    event_date: str
    title: str
    slug: str
    post_url: str
    pdf_url: str
    local_file: str
    kind: str
    reference: str
    note: str = ""


def main() -> int:
    parser = argparse.ArgumentParser(description="Sync Ferro assembly PDFs")
    parser.add_argument(
        "--outdir",
        default="actas-asamblea",
        help="Directory that will receive the PDFs and generated index",
    )
    parser.add_argument(
        "--category-id",
        type=int,
        default=DEFAULT_CATEGORY_ID,
        help="WordPress category id for Actas Asamblea",
    )
    parser.add_argument(
        "--terms",
        nargs="*",
        default=list(DEFAULT_TERMS),
        help="Search terms to query in WordPress",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Collect metadata without downloading files or writing indexes",
    )
    args = parser.parse_args()

    outdir = Path(args.outdir)
    posts = collect_posts(args.category_id, args.terms)
    media = collect_media(args.terms)
    records = collect_pdf_records(posts, media, outdir)

    if args.dry_run:
        for record in records:
            print(format_record_line(record))
        return 0

    outdir.mkdir(parents=True, exist_ok=True)
    rename_existing_files(records, outdir)
    download_missing_pdfs(records, outdir)
    write_manifest(records, outdir)
    write_index(records, outdir)

    print(f"downloaded_or_present={len(records)}")
    print(f"index={outdir / 'index.md'}")
    print(f"manifest={outdir / 'manifest.json'}")
    return 0


def collect_posts(category_id: int, terms: Iterable[str]) -> list[dict]:
    sources: list[tuple[str, dict]] = [
        (f"category:{category_id}", {"categories": category_id}),
    ]
    for term in terms:
        sources.append((f"search:{term}", {"search": term}))

    collected: dict[int, dict] = {}
    for source_name, params in sources:
        for post in fetch_collection(
            "posts",
            {
                **params,
                "status": "publish",
                "per_page": 100,
                "_fields": "id,date,slug,title,link,content,categories",
            },
        ):
            if not should_include_post(post, source_name):
                continue

            post_id = int(post["id"])
            entry = collected.get(post_id)
            if entry is None:
                collected[post_id] = {
                    "post": post,
                    "sources": {source_name},
                }
            else:
                entry["sources"].add(source_name)

    posts = [entry["post"] for entry in collected.values()]
    posts.sort(key=lambda p: (p.get("date", ""), p.get("id", 0)), reverse=True)
    return posts


def collect_media(terms: Iterable[str]) -> list[dict]:
    sources: list[tuple[str, dict]] = []
    for term in terms:
        sources.append((f"media:{term}", {"search": term}))

    collected: dict[int, dict] = {}
    for source_name, params in sources:
        for media in fetch_collection(
            "media",
            {
                **params,
                "status": "inherit",
                "per_page": 100,
                "_fields": "id,date,slug,title,link,source_url,mime_type",
            },
        ):
            if not should_include_media(media, source_name):
                continue
            media_id = int(media["id"])
            entry = collected.get(media_id)
            if entry is None:
                collected[media_id] = {
                    "media": media,
                    "sources": {source_name},
                }
            else:
                entry["sources"].add(source_name)

    media_items = [entry["media"] for entry in collected.values()]
    media_items.sort(key=lambda m: (m.get("date", ""), m.get("id", 0)), reverse=True)
    return media_items


def should_include_post(post: dict, source_name: str) -> bool:
    title = strip_html(post["title"]["rendered"])
    content = strip_html(post["content"]["rendered"])
    title_lower = title.lower()
    content_lower = content.lower()
    categories = {int(c) for c in post.get("categories", [])}

    if is_cd_act_post(title, content):
        return False

    if source_name.startswith("category:"):
        return True

    if source_name == "search:asamblea":
        if "asamblea" not in title_lower and "asamblea" not in content_lower:
            return False
        if BOARD_ACTA_RE.search(title_lower):
            return False
        return extract_pdf_urls(post["content"]["rendered"]) != []

    if source_name == "search:memoria y balance":
        if "memoria y balance" not in title_lower:
            return False
        return extract_pdf_urls(post["content"]["rendered"]) != []

    return bool(categories & {71}) or "asamblea" in title_lower


def should_include_media(media: dict, source_name: str) -> bool:
    title = strip_html(media["title"]["rendered"])
    title_lower = title.lower()
    if media.get("mime_type") != "application/pdf":
        return False

    if source_name == "media:asamblea":
        return "asamblea" in title_lower or "asamblea" in media.get("source_url", "").lower()

    if source_name == "media:memoria y balance":
        return "memoria y balance" in title_lower

    return False


def is_cd_act_post(title: str, content: str) -> bool:
    normalized = normalize_text(f"{title} {content}")
    return "comision directiva" in normalized or "reunion de cd" in normalized


def collect_pdf_records(posts: list[dict], media_items: list[dict], outdir: Path) -> list[PdfRecord]:
    records_by_pdf: "OrderedDict[str, PdfRecord]" = OrderedDict()

    for post in posts:
        title = strip_html(post["title"]["rendered"])
        slug = post.get("slug", "")
        post_url = post.get("link", "")
        post_date = post.get("date", "")[:10]
        categories = {int(c) for c in post.get("categories", [])}
        kind = classify_kind(title, categories)
        pdf_urls = extract_pdf_urls(post["content"]["rendered"])

        for idx, pdf_url in enumerate(pdf_urls, start=1):
            if not is_local_pdf_url(pdf_url):
                continue
            reference = infer_reference(title, slug, pdf_url, kind, post_date)
            event_date = infer_event_date(title, slug, reference, pdf_url, post_date)
            document_code = build_document_code(kind, title, slug, reference, pdf_url, event_date)
            local_file = build_local_filename(event_date, kind, document_code, len(pdf_urls), idx)
            note = build_note(title, slug, kind)

            if pdf_url not in records_by_pdf:
                records_by_pdf[pdf_url] = PdfRecord(
                    post_id=int(post["id"]),
                    post_date=post_date,
                    event_date=event_date,
                    title=title,
                    slug=slug,
                    post_url=post_url,
                    pdf_url=pdf_url,
                    local_file=local_file,
                    kind=kind,
                    reference=reference,
                    note=note,
                )

    for media in media_items:
        title = strip_html(media["title"]["rendered"])
        slug = media.get("slug", "")
        media_url = media.get("source_url", "")
        if not is_local_pdf_url(media_url):
            continue

        post_date = media.get("date", "")[:10]
        kind = classify_kind(title, set())
        reference = infer_reference(title, slug, media_url, kind, post_date)
        event_date = infer_event_date(title, slug, reference, media_url, post_date)
        document_code = build_document_code(kind, title, slug, reference, media_url, event_date)
        local_file = build_local_filename(event_date, kind, document_code, 1, 1)
        note = build_note(title, slug, kind)

        if media_url not in records_by_pdf:
            records_by_pdf[media_url] = PdfRecord(
                post_id=int(media["id"]),
                post_date=post_date,
                event_date=event_date,
                title=title,
                slug=slug,
                post_url=media.get("link", media_url),
                pdf_url=media_url,
                local_file=local_file,
                kind=kind,
                reference=reference,
                note=note,
            )

    # Sort newest first by inferred event date, then title, then file name.
    records = list(records_by_pdf.values())
    records.sort(key=lambda r: (r.event_date, r.post_date, r.title, r.local_file), reverse=True)
    return records


def classify_kind(title: str, categories: set[int]) -> str:
    lowered = title.lower()
    if "memoria y balance" in lowered:
        return "asamblea-balance"
    if "convocatoria" in lowered or "llamado a asamblea" in lowered:
        return "asamblea-convocatoria"
    if "tutorial" in lowered:
        return "asamblea-tutorial"
    if BOARD_ACTA_RE.search(lowered):
        return "cd-acta"
    if "asamblea" in lowered or 71 in categories:
        return "asamblea-acta"
    return "asamblea-related"


def build_note(title: str, slug: str, kind: str) -> str:
    if kind == "asamblea-acta" and "25-09-2022" in title and "26-09-2021" in slug:
        return "El título visible y el enlace no coinciden; conviene revisar el PDF."
    if kind == "asamblea-balance":
        return "Balance asociado a la asamblea."
    if kind == "asamblea-convocatoria":
        return "Aviso o convocatoria vinculada a la asamblea."
    if kind == "asamblea-tutorial":
        return "Material de apoyo vinculado a la asamblea."
    if kind == "cd-acta":
        return "Documento de Comisión Directiva detectado dentro de la búsqueda de asamblea."
    return ""


def infer_reference(title: str, slug: str, pdf_url: str, kind: str, post_date: str) -> str:
    candidates = [title, slug, Path(urllib.parse.urlparse(pdf_url).path).name]
    for candidate in candidates:
        ref = extract_reference(candidate)
        if ref:
            return ref

    if kind == "asamblea-balance":
        exercise = EXERCISE_RE.search(title)
        if exercise:
            return f"Ejercicio {exercise.group(1)}"

    if post_date:
        return post_date
    return "unknown"


def infer_event_date(title: str, slug: str, reference: str, pdf_url: str, post_date: str) -> str:
    candidates = [title, slug, reference, Path(urllib.parse.urlparse(pdf_url).path).name]
    for candidate in candidates:
        event_date = extract_exact_date(candidate)
        if event_date:
            return event_date
    return post_date


def extract_exact_date(text: str) -> str | None:
    if not text:
        return None

    compact = strip_html(text)
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


def normalize_iso_date(day: str, month: str, year: str) -> str | None:
    day_int = int(day)
    month_int = int(month)
    year_int = int(year)
    if year_int < 100:
        year_int += 2000
    if not (1 <= day_int <= 31 and 1 <= month_int <= 12):
        return None
    return f"{year_int:04d}-{month_int:02d}-{day_int:02d}"


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

    match = EXERCISE_RE.search(normalized)
    if match:
        return f"Ejercicio {match.group(1)}"

    return None


def normalize_numeric_date(day: str, month: str, year: str) -> str:
    day_int = int(day)
    month_int = int(month)
    year_int = int(year)
    if year_int < 100:
        year_int += 2000
    return f"{day_int:02d}/{month_int:02d}/{year_int:04d}"


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
    text = re.sub(r"\s+", " ", text)
    return text.strip().lower()


def strip_html(text: str) -> str:
    text = html.unescape(text)
    text = re.sub(r"<[^>]+>", "", text)
    return text.strip()


def clean_text(text: str) -> str:
    return re.sub(r"\s+", " ", strip_html(text)).strip()


def extract_pdf_urls(html_text: str) -> list[str]:
    urls: list[str] = []

    for match in re.finditer(r'https?://[^\s"\'<>«»]+?\.pdf[^\s"\'<>«»]*', html_text, re.IGNORECASE):
        urls.append(sanitize_pdf_url(match.group(0)))

    # WordPress gview shortcode style: [gview file=»https://...pdf»]
    for match in re.finditer(r'file=.?([^\s"\'<>«»]+?\.pdf[^\s"\'<>«»]*)', html_text, re.IGNORECASE):
        url = sanitize_pdf_url(match.group(1))
        if url.startswith("http"):
            urls.append(url)

    deduped: list[str] = []
    seen: set[str] = set()
    for url in urls:
        if url and url not in seen:
            seen.add(url)
            deduped.append(url)
    return deduped


def sanitize_pdf_url(url: str) -> str:
    url = html.unescape(url).strip()
    url = re.split(r'[<>"\'«»]', url)[0]
    url = url.rstrip("])>,")
    return url


def build_document_code(
    kind: str,
    title: str,
    slug: str,
    reference: str,
    pdf_url: str,
    event_date: str,
) -> str:
    candidate_texts = [reference, title, slug, Path(urllib.parse.urlparse(pdf_url).path).name, event_date]

    if kind == "asamblea-balance":
        exercise = extract_first_match(EXERCISE_RE, candidate_texts)
        if exercise:
            return f"ej{int(exercise):03d}"
        year_range = extract_year_range(candidate_texts)
        if year_range:
            return year_range
        month_year = extract_month_year_code(candidate_texts)
        if month_year:
            return month_year
        if event_date:
            event_month = month_code_from_iso(event_date)
            if event_month:
                return event_month
        year = extract_year(candidate_texts) or event_date[:4]
        if year:
            return year
        return compact_code_from_text(title, reference, slug, prefix="balance", max_tokens=3)

    if kind == "asamblea-convocatoria":
        year = extract_year(candidate_texts) or event_date[:4]
        if year:
            return f"conv-{year}"
        month_year = extract_month_year_code(candidate_texts)
        if month_year:
            return f"conv-{month_year}"
        return compact_code_from_text(title, reference, slug, prefix="conv", max_tokens=3)

    if kind == "asamblea-tutorial":
        return compact_code_from_text(
            title,
            reference,
            slug,
            prefix="tutorial",
            max_tokens=4,
            drop_words=COMMON_CODE_STOPWORDS | {"tutorial"},
        )

    if kind == "asamblea-acta":
        period = extract_first_match(PERIOD_RE, candidate_texts)
        if period:
            return f"p{int(period):03d}"
        year_range = extract_year_range(candidate_texts)
        if year_range:
            return year_range
        month_year = extract_month_year_code(candidate_texts)
        if month_year:
            return month_year
        if event_date:
            event_month = month_code_from_iso(event_date)
            if event_month:
                return event_month
        return compact_code_from_text(
            title,
            reference,
            slug,
            prefix="acta",
            max_tokens=4,
            drop_words=COMMON_CODE_STOPWORDS,
        )

    if kind == "cd-acta":
        period = extract_first_match(PERIOD_RE, candidate_texts)
        acta = extract_first_match(ACTA_NUM_RE, candidate_texts)
        if period and acta:
            return f"p{int(period):03d}-a{int(acta):03d}"
        if period:
            return f"p{int(period):03d}"
        if acta:
            return f"a{int(acta):03d}"
        return compact_code_from_text(
            title,
            reference,
            slug,
            prefix="cd",
            max_tokens=4,
            drop_words=COMMON_CODE_STOPWORDS | {"acta"},
        )

    return compact_code_from_text(title, reference, slug, prefix=kind or "document", max_tokens=4)


def build_local_filename(
    event_date: str,
    kind: str,
    document_code: str,
    total_parts: int,
    part_index: int,
) -> str:
    parts = [event_date or "undated", slugify(kind) or "document", slugify(document_code) or "item"]
    if total_parts > 1:
        parts.append(f"part-{part_index:02d}")
    filename = "__".join(parts) + ".pdf"
    return str(Path("balances") / filename) if kind == "asamblea-balance" else filename


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


def month_code_from_iso(date_text: str) -> str | None:
    if not date_text or len(date_text) < 7:
        return None
    match = re.match(r"^(\d{4})-(\d{2})(?:-\d{2})?$", date_text)
    if not match:
        return None
    _, month = match.groups()
    month_int = int(month)
    month_code = MONTH_CODES.get(month_int)
    if not month_code:
        return None
    return f"{month_code}-{date_text[:4]}"


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
    text = html.unescape(text)
    text = text.lower()
    text = re.sub(r"[^a-z0-9]+", "-", text)
    text = re.sub(r"-+", "-", text).strip("-")
    return text


def download_missing_pdfs(records: list[PdfRecord], outdir: Path) -> None:
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
                    record.pdf_url,
                    "-o",
                    str(local_path),
                ]
            )
        except subprocess.CalledProcessError as exc:
            print(f"skip {record.pdf_url} ({exc})", file=sys.stderr)


def rename_existing_files(records: list[PdfRecord], outdir: Path) -> None:
    manifest_path = outdir / "manifest.json"
    if not manifest_path.exists():
        return

    try:
        existing = json.loads(manifest_path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return

    old_by_pdf: dict[str, str] = {}
    for item in existing.get("records", []):
        pdf_url = item.get("pdf_url")
        local_file = item.get("local_file")
        if isinstance(pdf_url, str) and isinstance(local_file, str):
            old_by_pdf[pdf_url] = local_file

    for record in records:
        old_local_file = old_by_pdf.get(record.pdf_url)
        if not old_local_file or old_local_file == record.local_file:
            continue

        old_path = outdir / old_local_file
        new_path = outdir / record.local_file
        new_path.parent.mkdir(parents=True, exist_ok=True)
        if old_path.exists() and not new_path.exists():
            old_path.rename(new_path)


def write_manifest(records: list[PdfRecord], outdir: Path) -> None:
    payload = {
        "site": SITE_URL,
        "category_id": DEFAULT_CATEGORY_ID,
        "terms": list(DEFAULT_TERMS),
        "count": len(records),
        "records": [dataclasses.asdict(record) for record in records],
    }
    (outdir / "manifest.json").write_text(
        json.dumps(payload, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )


def write_index(records: list[PdfRecord], outdir: Path) -> None:
    lines = [
        "# Documentos de Asamblea",
        "",
        f"Documentos reunidos: {len(records)}",
        "",
        "Esta carpeta reúne actas, balances, convocatorias y materiales de apoyo vinculados con las asambleas. Los documentos están ordenados del más reciente al más antiguo.",
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
            f"| {record.event_date} | {record.post_date} | {friendly_kind_label(record.kind)} | {format_reference(record)} | "
            f"{record.title} | `{record.local_file}` | {record.pdf_url} | {note} |"
        )

    (outdir / "index.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def format_record_line(record: PdfRecord) -> str:
    return (
        f"{record.event_date} | {record.post_date} | {friendly_kind_label(record.kind)} | {format_reference(record)} | "
        f"{record.title} | {record.local_file} | {record.pdf_url}"
    )


def format_reference(record: PdfRecord) -> str:
    code = extract_local_code(record.local_file)
    if not code:
        return record.reference

    match = re.fullmatch(r"p(\d{3})-a(\d{3})", code, re.IGNORECASE)
    if match:
        return f"Período {int(match.group(1))} · Acta {int(match.group(2))}"

    match = re.fullmatch(r"p(\d{3})", code, re.IGNORECASE)
    if match:
        return f"Período {int(match.group(1))}"

    match = re.fullmatch(r"ej(\d{3})", code, re.IGNORECASE)
    if match:
        return f"Ejercicio {int(match.group(1))}"

    match = re.fullmatch(r"(ene|feb|mar|abr|may|jun|jul|ago|sep|oct|nov|dic)-(\d{4})", code, re.IGNORECASE)
    if match:
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
        }.get(match.group(1).lower(), match.group(1).upper())
        return f"{month_name} {match.group(2)}"

    match = re.fullmatch(r"conv-(\d{4})", code, re.IGNORECASE)
    if match:
        return f"Convocatoria {match.group(1)}"

    match = re.fullmatch(r"(\d{4}-\d{4})", code)
    if match:
        return f"Ejercicio {match.group(1)}"

    if code.lower().startswith("tutorial"):
        return "Material de apoyo"

    return record.reference or code.replace("-", " ").title()


def friendly_kind_label(kind: str) -> str:
    return {
        "asamblea-acta": "Acta de asamblea",
        "asamblea-balance": "Balance de asamblea",
        "asamblea-convocatoria": "Convocatoria",
        "asamblea-tutorial": "Material de apoyo",
        "asamblea-related": "Documento vinculado",
        "cd-acta": "Acta de Comisión Directiva",
        "cd-balance": "Balance de Comisión Directiva",
    }.get(kind, kind.replace("-", " ").title())


def build_summary_lines(records: list[PdfRecord]) -> list[str]:
    lines: list[str] = ["## Continuidad"]
    if not any(record.kind == "asamblea-acta" and record.event_date.startswith("2021-") for record in records):
        lines.append("- No aparece una acta de asamblea independiente fechada en 2021 dentro de esta copia pública.")
    else:
        lines.append("- La secuencia incluye documentos de asamblea fechados en 2021.")
    if any(record.kind == "asamblea-balance" and record.event_date == "2021-09-20" for record in records):
        lines.append("- Sí está incluido el balance del ejercicio 2020-2021, separado del acta.")
    return lines


def extract_local_code(local_file: str) -> str:
    stem = Path(local_file).stem
    parts = stem.split("__")
    if len(parts) >= 3:
        return parts[2]
    return ""


def fetch_collection(endpoint: str, params: dict) -> list[dict]:
    results: list[dict] = []
    page = 1
    per_page = int(params.get("per_page", 100))

    while True:
        query = dict(params)
        query["page"] = page
        query["per_page"] = per_page
        url = f"{API_ROOT}/{endpoint}?" + urllib.parse.urlencode(query)
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
        payload = json.loads(body)

        if not isinstance(payload, list):
            break

        results.extend(payload)
        if len(payload) < per_page:
            break
        page += 1

    return results


def is_local_pdf_url(url: str) -> bool:
    parsed = urllib.parse.urlparse(url)
    host = parsed.netloc.lower()
    return host.endswith("ferrocarriloeste.org.ar")


def run_curl(cmd: list[str], retries: int = 3, delay_seconds: float = 1.5) -> str:
    last_exc: subprocess.CalledProcessError | None = None
    for attempt in range(1, retries + 1):
        try:
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
            else:
                effective_cmd = cmd
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
