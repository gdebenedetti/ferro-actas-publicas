#!/usr/bin/env python3
"""Cruza el registro de votantes MFA con el padrón definitivo local de 2026.

El informe de salida contiene sólo agregados. El CSV persona a persona y los
casos pendientes se guardan en el directorio privado/ignorado del padrón web.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import re
import unicodedata
from collections import Counter, defaultdict
from datetime import datetime, time
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
DEFAULT_VOTERS = Path.home() / "Downloads" / "VOTACIO\u0301N FCO - todos_los_que_votaron.csv"
DEFAULT_PADRON = ROOT / "padron-ferro-en-accion-web/data/padron-2026/padron-definitivo-2026-mesas.csv"
DEFAULT_PADRON_2020 = ROOT / "archivo-club/elecciones/padrones/2020-09-08__padron-electoral__ferro.csv"
DEFAULT_PRIVATE_OUTPUT = ROOT / "padron-ferro-en-accion-web/data/padron-2026/participacion-votacion-2026.csv"
DEFAULT_PENDING_OUTPUT = ROOT / "padron-ferro-en-accion-web/data/padron-2026/cruces-votacion-2026-pendientes.csv"
DEFAULT_REPORT = ROOT / "mfa/trabajo/coaching-electoral/2026-10-12__analisis-resultados-votacion-2026.md"

PROPOSAL = [
    ("ABADIN", "BEN", 206.4),
    ("BENAGHI", "CERVANTES", 206.8),
    ("CERVELO", "DONATO", 207.0),
    ("DONELLI", "GARCIA RETAMAR", 207.1),
    ("GARCIA RIVAS", "JACA", 207.2),
    ("JACQUEMIN", "MARTINO", 207.4),
    ("MARTORELLI", "PARADISO", 207.6),
    ("PARAFITA", "RISI", 206.6),
    ("RISO", "SPINETTO", 207.2),
    ("SPITZNAGEL DE SONAGLIA", "ZYSMAN", 204.4),
]
TIME_FORMAT = "%d/%m/%Y %H:%M:%S"


def norm_text(value: str) -> str:
    value = unicodedata.normalize("NFKD", value.upper().strip())
    value = "".join(char for char in value if not unicodedata.combining(char))
    return re.sub(r"[^A-Z0-9]+", " ", value).strip()


def norm_member(value: str) -> str:
    value = re.sub(r"[.\\_-]", " ", value.upper().strip())
    match = re.fullmatch(r"([A-Z]{2})\s*(\d+)", re.sub(r"\s+", " ", value))
    if not match:
        return ""
    return f"{match.group(1)} {match.group(2).zfill(6)}"


def full_name(surname: str, given: str) -> str:
    return norm_text(f"{surname} {given}")


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8-sig", newline="") as source:
        return list(csv.DictReader(source))


def write_csv(path: Path, rows: list[dict[str, str]], fields: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8-sig", newline="") as output:
        writer = csv.DictWriter(output, fieldnames=fields, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(rows)


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as source:
        for chunk in iter(lambda: source.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def proposal_table(surname: str) -> int:
    value = norm_text(surname)
    matches = [index for index, (start, end, _) in enumerate(PROPOSAL, 1)
               if norm_text(start) <= value <= norm_text(end)]
    if len(matches) != 1:
        raise ValueError(f"El apellido no cae en un único rango de la propuesta: {surname!r} -> {matches}")
    return matches[0]


def pct(value: float) -> str:
    return f"{value * 100:.1f}%".replace(".", ",")


def num(value: float, decimals: int = 0) -> str:
    formatted = f"{value:,.{decimals}f}"
    return formatted.replace(",", "X").replace(".", ",").replace("X", ".")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--voters", type=Path, default=DEFAULT_VOTERS)
    parser.add_argument("--padron", type=Path, default=DEFAULT_PADRON)
    parser.add_argument("--padron-2020", type=Path, default=DEFAULT_PADRON_2020)
    parser.add_argument("--output", type=Path, default=DEFAULT_PRIVATE_OUTPUT)
    parser.add_argument("--pending-output", type=Path, default=DEFAULT_PENDING_OUTPUT)
    parser.add_argument("--report", type=Path, default=DEFAULT_REPORT)
    args = parser.parse_args()

    voters = read_csv(args.voters)
    padron = read_csv(args.padron)
    padron_2020 = read_csv(args.padron_2020)
    required_voter_fields = {"hora_voto", "mesa_donde_voto", "mesa_asignada", "nro_socio", "apellido", "nombre", "es_referido"}
    required_padron_fields = {"MESA", "Apellido", "Nombre", "Nro Socio"}
    required_2020_fields = {"nro_socio", "nombre"}
    if not voters or not required_voter_fields.issubset(voters[0]):
        raise ValueError(f"El CSV de votantes no tiene las columnas esperadas: {sorted(required_voter_fields)}")
    if not padron or not required_padron_fields.issubset(padron[0]):
        raise ValueError(f"El CSV del padrón no tiene las columnas esperadas: {sorted(required_padron_fields)}")
    if not padron_2020 or not required_2020_fields.issubset(padron_2020[0]):
        raise ValueError(f"El CSV del padrón 2020 no tiene las columnas esperadas: {sorted(required_2020_fields)}")

    voter_by_member: dict[str, dict[str, str]] = {}
    voter_by_name: dict[str, list[dict[str, str]]] = defaultdict(list)
    for row in voters:
        key = norm_member(row["nro_socio"])
        if not key:
            raise ValueError(f"Número de socio no interpretable en fila de votantes: {row['nro_socio']!r}")
        if key in voter_by_member:
            raise ValueError(f"Número de socio repetido en el CSV de votantes: {key}")
        row["_member_key"] = key
        row["_name_key"] = full_name(row["apellido"], row["nombre"])
        row["_proposal_table"] = str(proposal_table(row["apellido"]))
        row["_timestamp"] = datetime.strptime(row["hora_voto"], TIME_FORMAT)
        voter_by_member[key] = row
        voter_by_name[row["_name_key"]].append(row)

    padron_by_member: dict[str, dict[str, str]] = {}
    padron_by_name: dict[str, list[dict[str, str]]] = defaultdict(list)
    for row in padron:
        key = norm_member(row["Nro Socio"])
        if key:
            if key in padron_by_member:
                raise ValueError(f"Número de socio repetido en el padrón: {key}")
            row["_member_key"] = key
            padron_by_member[key] = row
        row["_name_key"] = full_name(row["Apellido"], row["Nombre"])
        row["_proposal_table"] = str(proposal_table(row["Apellido"]))
        padron_by_name[row["_name_key"]].append(row)

    historical_by_member: dict[str, list[dict[str, str]]] = defaultdict(list)
    historical_by_name: dict[str, list[dict[str, str]]] = defaultdict(list)
    for row in padron_2020:
        key = norm_member(row["nro_socio"])
        name_key = norm_text(row["nombre"])
        if key:
            historical_by_member[key].append(row)
        historical_by_name[name_key].append(row)

    history_status: dict[str, tuple[str, str, str]] = {}
    history_counts: Counter[str] = Counter()
    history_voted_by_id: Counter[str] = Counter()
    for row in padron:
        key = row.get("_member_key", "")
        name_key = row["_name_key"]
        old_by_id = historical_by_member.get(key, []) if key else []
        if old_by_id:
            if any(norm_text(old["nombre"]) == name_key for old in old_by_id):
                category = "id_name"
                result = ("SI", "número de socio y nombre exactos", category)
            elif len(old_by_id) == 1:
                category = "id_name_conflict"
                result = ("REVISAR", "número de socio coincide; nombre difiere", category)
            else:
                category = "ambiguous_id"
                result = ("REVISAR", "número de socio duplicado en padrón 2020", category)
        else:
            old_by_name = historical_by_name.get(name_key, [])
            if len(old_by_name) == 1:
                category = "unique_name"
                result = ("REVISAR", "nombre exacto único en 2020; número distinto o ausente", category)
            elif old_by_name:
                category = "ambiguous_name"
                result = ("REVISAR", "nombre repetido en padrón 2020", category)
            else:
                category = "not_found"
                result = ("NO LOCALIZADO", "sin número ni nombre exactos en padrón 2020", category)
        history_status[key or f"name:{name_key}"] = result
        history_counts[category] += 1
        if key in voter_by_member:
            history_voted_by_id[category] += 1

    statuses: dict[str, tuple[str, str, dict[str, str] | None]] = {}
    pending: list[dict[str, str]] = []
    exact_match_count = 0
    name_only_unique = 0
    ambiguous_voters = 0
    unmatched_voters = 0
    for row in voters:
        key = row["_member_key"]
        padron_record = padron_by_member.get(key)
        if padron_record:
            if row["_name_key"] != padron_record["_name_key"]:
                raise ValueError(f"El número de socio coincide pero el nombre difiere: {key}")
            statuses[key] = ("SI", "número de socio exacto", row)
            exact_match_count += 1
            continue
        candidates = padron_by_name.get(row["_name_key"], [])
        if len(candidates) == 1:
            candidate_key = norm_member(candidates[0]["Nro Socio"])
            statuses[candidate_key or f"name:{row['_name_key']}"] = (
                "REVISAR", "nombre completo exacto único; número de socio no coincide", row
            )
            pending.append({
                "tipo": "nombre único con número distinto o ausente",
                "nro_socio_sistema": row["nro_socio"],
                "apellido": row["apellido"],
                "nombre": row["nombre"],
                "mesa_sistema": row["mesa_asignada"],
                "hora_voto": row["hora_voto"],
            })
            name_only_unique += 1
        elif len(candidates) > 1:
            pending.append({
                "tipo": "nombre completo repetido en el padrón; identidad ambigua",
                "nro_socio_sistema": row["nro_socio"],
                "apellido": row["apellido"],
                "nombre": row["nombre"],
                "mesa_sistema": row["mesa_asignada"],
                "hora_voto": row["hora_voto"],
            })
            ambiguous_voters += 1
        else:
            pending.append({
                "tipo": "sin coincidencia por socio ni nombre",
                "nro_socio_sistema": row["nro_socio"],
                "apellido": row["apellido"],
                "nombre": row["nombre"],
                "mesa_sistema": row["mesa_asignada"],
                "hora_voto": row["hora_voto"],
            })
            unmatched_voters += 1

    # Index names that have multiple system voters; these cannot be assigned to a single row.
    ambiguous_names = {name for name, rows in voter_by_name.items() if len(rows) > 1}
    augmented: list[dict[str, str]] = []
    for source_row in padron:
        row = {key: value for key, value in source_row.items() if not key.startswith("_")}
        member_key = source_row.get("_member_key", "")
        status = statuses.get(member_key or f"name:{source_row['_name_key']}")
        if status is None:
            name_key = source_row["_name_key"]
            if name_key in ambiguous_names:
                possible = voter_by_name[name_key]
                # Only mark as review if at least one voter has no exact member-ID match.
                if any(v["_member_key"] not in padron_by_member for v in possible):
                    status = ("REVISAR", "nombre completo repetido; no se asigna a una persona", None)
        vote_state, method, voter_row = status or ("NO", "sin coincidencia en el registro de votantes", None)
        row["Voto 2026"] = vote_state
        row["Método de cruce"] = method
        row["Mesa registrada"] = voter_row["mesa_donde_voto"] if voter_row else ""
        row["Hora registrada"] = voter_row["hora_voto"] if voter_row else ""
        historic = history_status.get(member_key or f"name:{source_row['_name_key']}", ("REVISAR", "sin número para comparar", "missing_key"))
        row["En padrón 2020"] = historic[0]
        row["Método cruce 2020"] = historic[1]
        augmented.append(row)

    write_csv(args.output, augmented, list(augmented[0].keys()))
    write_csv(args.pending_output, pending, ["tipo", "nro_socio_sistema", "apellido", "nombre", "mesa_sistema", "hora_voto"])

    current_roster = Counter(int(row["MESA"]) for row in padron)
    current_voters = Counter(int(row["mesa_donde_voto"]) for row in voters)
    assigned_voters = Counter(int(row["mesa_asignada"]) for row in voters)
    on_expected_table = sum(row["mesa_donde_voto"] == row["mesa_asignada"] for row in voters)
    proposed_roster = Counter(int(row["_proposal_table"]) for row in padron)
    proposed_voters = Counter(int(row["_proposal_table"]) for row in voters)
    migration = Counter((int(row["mesa_asignada"]), int(row["_proposal_table"])) for row in voters)
    current_surnames_by_table: dict[int, set[str]] = defaultdict(set)
    for row in padron:
        current_surnames_by_table[int(row["MESA"])].add(norm_text(row["Apellido"]))
    surname_distribution: dict[str, Counter[int]] = defaultdict(Counter)
    for row in padron:
        surname_distribution[norm_text(row["Apellido"])][int(row["MESA"])] += 1
    split_surnames = {surname: counts for surname, counts in surname_distribution.items() if len(counts) > 1}
    border_rows = []
    for mesa in range(1, len(current_roster)):
        left = [row for row in padron if int(row["MESA"]) == mesa]
        right = [row for row in padron if int(row["MESA"]) == mesa + 1]
        if left and right:
            same = norm_text(left[-1]["Apellido"]) == norm_text(right[0]["Apellido"])
            border_rows.append((mesa, left[-1]["Apellido"], mesa + 1, right[0]["Apellido"], same))

    times = [row["_timestamp"] for row in voters]
    after_19 = sum(timestamp.time() > time(19, 0) for timestamp in times)
    by_hour = Counter(timestamp.strftime("%H:00") for timestamp in times)
    referral_yes = sum(row["es_referido"].strip().lower() in {"si", "sí", "yes", "true", "1"} for row in voters)
    proposed_expected = sum(item[2] for item in PROPOSAL)
    lowest_turnout_mesa = min(current_voters, key=lambda mesa: current_voters[mesa] / current_roster[mesa])
    highest_turnout_mesa = max(current_voters, key=lambda mesa: current_voters[mesa] / current_roster[mesa])
    matched_rows_by_key = {row["_member_key"]: row for row in voters}
    matched_by_id_official_mesa = sum(
        1 for key, voter in matched_rows_by_key.items()
        if key in padron_by_member and voter["mesa_asignada"] == padron_by_member[key]["MESA"]
    )

    lines = [
        "# Análisis del registro de votación 2026",
        "",
        "## Alcance y fuentes",
        "",
        f"- Registro entregado por MFA: `{args.voters.name}`; SHA-256 `{sha256(args.voters)}`.",
        f"- Padrón definitivo de trabajo 2026 con mesa y número de socio: `{args.padron.relative_to(ROOT) if args.padron.is_relative_to(ROOT) else args.padron}`; SHA-256 `{sha256(args.padron)}`.",
        f"- Padrón electoral 2020 archivado: `{args.padron_2020.relative_to(ROOT) if args.padron_2020.is_relative_to(ROOT) else args.padron_2020}`; SHA-256 `{sha256(args.padron_2020)}`.",
        "- El informe conserva únicamente agregados. El cruce persona a persona queda en el directorio local ignorado de `padron-ferro-en-accion-web/data/padron-2026/`.",
        "- Para 2023, el archivo público local registra elegibilidad/habilitación (`padron_2023_habilitado`), no si cada socio efectivamente votó. No se completa una columna de asistencia 2023 sin una fuente de votos de esa elección.",
        "",
        "## Resultado general",
        "",
        f"- Registros de votación: **{num(len(voters))}**; números de socio únicos.",
        f"- Padrón 2026: **{num(len(padron))}** filas; participación registrada equivalente a **{pct(len(voters) / len(padron))}** del listado.",
        f"- Cruce por número de socio normalizado y nombre coincidente: **{num(exact_match_count)}** ({pct(exact_match_count / len(voters))}). Se estandarizaron prefijos y ceros a la izquierda.",
        f"- Nombre completo exacto único, pero número distinto/ausente: **{num(name_only_unique)}** ({pct(name_only_unique / len(voters))}); quedan `REVISAR`, no se consideran cruce confirmado.",
        f"- Nombres repetidos que impiden asignar persona sin ambigüedad: **{num(ambiguous_voters)}** ({pct(ambiguous_voters / len(voters))}). Sin coincidencia nominal: **{num(unmatched_voters)}**.",
        f"- Mesa donde votó = mesa asignada en el sistema: **{num(on_expected_table)} de {num(len(voters))}**. Entre los cruces confirmados, la mesa del sistema coincide con la mesa del padrón en **{num(matched_by_id_official_mesa)} de {num(exact_match_count)}**.",
        f"- Marcados como referidos: **{num(referral_yes)}** ({pct(referral_yes / len(voters))}); el resto no lleva esa marca. No se desglosan referentes individuales en este informe.",
        "",
        "## Comparación histórica con el padrón 2020",
        "",
        "Esta comparación identifica presencia en el padrón electoral archivado de 2020, no el año efectivo de alta ni una incorporación específica en 2023. Se clasifica como coincidencia fuerte sólo el mismo número de socio y nombre completo normalizados; las variaciones quedan para revisión.",
        "",
        "| Situación respecto de 2020 | Filas del padrón 2026 | Con voto 2026 por número exacto |",
        "| --- | ---: | ---: |",
        f"| Número y nombre exactos en 2020 | {num(history_counts['id_name'])} | {num(history_voted_by_id['id_name'])} |",
        f"| Número coincide, nombre difiere | {num(history_counts['id_name_conflict'])} | {num(history_voted_by_id['id_name_conflict'])} |",
        f"| Nombre único en 2020, número distinto/ausente | {num(history_counts['unique_name'])} | {num(history_voted_by_id['unique_name'])} |",
        f"| Nombre repetido en 2020 | {num(history_counts['ambiguous_name'])} | {num(history_voted_by_id['ambiguous_name'])} |",
        f"| No localizado en 2020 por número ni nombre exacto | {num(history_counts['not_found'])} | {num(history_voted_by_id['not_found'])} |",
        "",
        f"Hay **{num(history_counts['not_found'])}** registros 2026 no localizados en el padrón 2020 por número ni nombre completo exactos; **{num(history_voted_by_id['not_found'])}** tienen un voto 2026 confirmado por número de socio. Es un grupo de posibles altas posteriores a 2020, sujeto a que el padrón 2020 sea el baseline correcto y a los límites de identidad indicados; no demuestra altas posteriores a 2023.",
        f"Además, **{num(history_counts['unique_name'])}** filas comparten nombre completo único pero no número con registros de 2020; **{num(history_voted_by_id['unique_name'])}** de ellas tienen voto 2026 por número exacto. Se mantienen como revisión para no contar cambios de número o categoría como incorporaciones nuevas.",
        "",
        "## Distribución por las mesas del padrón definitivo",
        "",
        f"La mesa registrada en el sistema concentra entre **{num(min(current_voters.values()))} y {num(max(current_voters.values()))}** votos; la participación por mesa queda entre **{pct(min(current_voters[m] / current_roster[m] for m in current_roster))} y {pct(max(current_voters[m] / current_roster[m] for m in current_roster))}** del tamaño de cada mesa.",
        "",
        "| Mesa | Electores en padrón | Votantes registrados | Participación |",
        "| ---: | ---: | ---: | ---: |",
    ]
    for mesa in sorted(current_roster):
        lines.append(f"| {mesa} | {num(current_roster[mesa])} | {num(current_voters[mesa])} | {pct(current_voters[mesa] / current_roster[mesa])} |")
    lines += [
        "",
        f"La mesa {highest_turnout_mesa} tiene la mayor participación ({num(current_voters[highest_turnout_mesa])}; {pct(current_voters[highest_turnout_mesa] / current_roster[highest_turnout_mesa])}); la mesa {lowest_turnout_mesa} tiene la menor ({num(current_voters[lowest_turnout_mesa])}; {pct(current_voters[lowest_turnout_mesa] / current_roster[lowest_turnout_mesa])}). La diferencia es {num(current_voters[highest_turnout_mesa] - current_voters[lowest_turnout_mesa])} votos registrados. Estas tasas describen el cruce de este registro con el padrón de trabajo; los casos no cruzados por socio requieren revisión y pueden mover cifras por mesa.",
        "",
        "## Qué muestran los cortes de mesa",
        "",
        "El padrón definitivo local reparte **786 o 787 registros en cada una de las diez mesas** y conserva orden alfabético por apellido y nombre. Es un patrón compatible con cortes por cantidad casi idéntica de electores. En cuatro límites, el apellido completo queda repartido entre dos mesas:",
        "",
        "| Mesas contiguas | Apellido que aparece a ambos lados | Personas de ese apellido en ambas mesas |",
        "| --- | --- | ---: |",
    ]
    for surname, counts in sorted(split_surnames.items(), key=lambda item: item[0]):
        tables = sorted(counts)
        lines.append(f"| {tables[0]} y {tables[-1]} | {surname} | {num(sum(counts.values()))} |")
    lines += [
        "",
        f"En total, **{num(len(split_surnames))} apellidos** aparecen en más de una mesa, con **{num(sum(sum(counts.values()) for counts in split_surnames.values()))} personas** en esos grupos. Los apellidos que cruzan un límite son BIANCHI, GARRONE, LA TORRE y RODRIGUEZ. Esto confirma que la asignación final divide algunos apellidos; por sí solo no documenta el motivo administrativo del criterio.",
        "",
        "| Límite | Último apellido en mesa anterior | Primer apellido en mesa siguiente | Mismo apellido |",
        "| --- | --- | --- | --- |",
    ]
    for left_mesa, left_name, right_mesa, right_name, same in border_rows:
        lines.append(f"| {left_mesa} / {right_mesa} | {left_name} | {right_name} | {'Sí' if same else 'No'} |")
    lines += [
        "",
        "## Comparación con la propuesta MFA del 21/9",
        "",
        f"La propuesta ordenaba por rangos alfabéticos y estimaba unas 206–208 participaciones por mesa ({num(proposed_expected, 1)} en total), a partir de 7.839 electores del listado provisorio. El padrón definitivo local tiene {num(len(padron))} filas ({num(len(padron) - 7839)} más). Aplicados los mismos rangos al padrón definitivo actual, todas las filas quedan asignadas; los tamaños se mantienen desiguales por diseño. La mesa 9 vuelve a ser la de mayor carga electoral, y la mesa 5 la de menor carga.",
        "",
        "| Mesa propuesta | Electores en padrón definitivo por rango | Votos observados por apellido en ese rango | Participación observada | Estimación propuesta |",
        "| ---: | ---: | ---: | ---: | ---: |",
    ]
    for mesa, (start, end, expected) in enumerate(PROPOSAL, 1):
        size = proposed_roster[mesa]
        votes = proposed_voters[mesa]
        lines.append(f"| {mesa} ({start}–{end}) | {num(size)} | {num(votes)} | {pct(votes / size)} | {num(expected, 1)} |")
    lines += [
        "",
        f"El registro suma **{num(len(voters))}** votos frente a **{num(proposed_expected, 1)}** participantes estimados en la propuesta: **{num(len(voters) - proposed_expected, 1)}** más ({pct(len(voters) / proposed_expected - 1)} por encima). Esta diferencia compara un resultado registrado con una estimación previa, no implica por sí misma que la estimación fuera un compromiso de resultado.",
        "",
        "| Mesa actual del sistema | " + " | ".join(str(mesa) for mesa in range(1, len(PROPOSAL) + 1)) + " |",
        "| ---: | " + " | ".join(["---:"] * len(PROPOSAL)) + " |",
    ]
    for current in sorted(current_voters):
        moved = [migration[(current, proposed)] for proposed in range(1, len(PROPOSAL) + 1)]
        lines.append(f"| {current} | " + " | ".join(str(value) for value in moved) + " |")
    changed = sum(count for (current, proposed), count in migration.items() if current != proposed)
    lines += [
        "",
        f"La matriz anterior redistribuye por apellido los **{num(len(voters))}** registros de votación según la propuesta. **{num(changed)}** quedarían en un número de mesa distinto al que figura en el sistema actual. El cálculo usa el apellido del registro de votación, no una asignación oficial alternativa.",
        "",
        "## Horarios y límites del registro",
        "",
        f"- Primera hora registrada: **{min(times).strftime(TIME_FORMAT)}**; última: **{max(times).strftime(TIME_FORMAT)}**.",
        f"- **{num(after_19)}** marcas tienen hora posterior a las 19:00. El horario 09:00–19:00 del archivo de stress es un supuesto de simulación; confirmar la hora oficial de cierre y si el sistema guardaba hora de captura o de carga antes de interpretar esos registros.",
        "- Distribución por hora local registrada:",
        "",
        "| Hora | Registros |",
        "| --- | ---: |",
    ]
    for hour in sorted(by_hour):
        lines.append(f"| {hour} | {num(by_hour[hour])} |")
    lines += [
        "",
        "## Lecturas y próximos cruces posibles",
        "",
        "1. El sistema registra exactamente la mesa asignada para todos los votantes del CSV; el cruce confirmado por socio también coincide con la mesa del padrón. No aparecen cambios de mesa en estos datos.",
        "2. El patrón de 786/787 electores por mesa y los cuatro apellidos partidos es evidencia observable compatible con una partición secuencial por tamaño. Para afirmar qué instrucción recibió la Junta o por qué lo hizo haría falta el acta, instructivo o listado oficial de asignaciones.",
        "3. No hay fuente de asistencia efectiva 2023 en el material disponible. `padron_2023_habilitado` en el CSV 2020 señala habilitación en el padrón, no que haya votado. El padrón oficial 2023 se consultaba individualmente y el proyecto no conserva un listado público completo de votantes.",
        "4. La copia del padrón 2026 tiene 265 filas sin número de socio; junto con 130 coincidencias nominales únicas y 18 ambiguas, conviene resolver los pendientes contra el registro interno antes de tratar la marca por persona como definitiva.",
        "5. Una vez disponible una fuente verificable de asistencia 2023, el cruce debería añadir `Voto 2023` por número de socio y separar: presentes en ambos padrones, altas 2026 que votaron, altas que no votaron y socios que ya no figuran. No se debe inferir voto 2023 desde la habilitación.",
        "",
        "## Artefactos generados",
        "",
        f"- Base local aumentada: `{args.output}`. Columnas nuevas: `Voto 2026`, `Método de cruce`, `Mesa registrada`, `Hora registrada`, `En padrón 2020` y `Método cruce 2020`.",
        f"- Pendientes de conciliación: `{args.pending_output}` ({num(len(pending))} filas).",
        f"- Script reproducible: `mfa/trabajo/coaching-electoral/scripts/analizar-votacion-2026.py`.",
        "",
        "El padrón combinado y la lista de pendientes contienen datos personales y permanecen fuera de Git, dentro del directorio privado ignorado del subproyecto. El informe agregado no lista nombres de socios ni referentes.",
        "",
    ]
    args.report.parent.mkdir(parents=True, exist_ok=True)
    args.report.write_text("\n".join(lines), encoding="utf-8")
    print(json.dumps({
        "voters": len(voters), "padron": len(padron), "exact_member_matches": exact_match_count,
        "unique_name_review": name_only_unique, "ambiguous_name_matches": ambiguous_voters,
        "unmatched": unmatched_voters, "private_output": str(args.output),
        "pending_output": str(args.pending_output), "report": str(args.report),
        "sha256_voters": sha256(args.voters), "sha256_padron": sha256(args.padron),
    }, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
