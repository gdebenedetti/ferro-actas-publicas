# Ferro en Acción

Repositorio curado de documentación pública vinculada a Ferrocarril Oeste y a Movimiento Ferro en Acción (MFA). Reúne actas, balances y convocatorias del club en un archivo ordenado, y material de comunicación pública de la agrupación.

## Dos ejes de trabajo

| Eje | Qué es | Dónde vive |
| --- | --- | --- |
| **Club** | Espejo de documentos publicados en [ferrocarriloeste.org.ar](https://www.ferrocarriloeste.org.ar) | `archivo-club/actas-cd/`, `archivo-club/actas-asamblea/`, `archivo-club/scripts/` |
| **MFA** | Comunicación e identidad de Movimiento Ferro en Acción | `mfa/comunicacion/redes-sociales/`, `mfa/identidad/manual-marca/`, `mfa/trabajo/web-borradores/`, [`ferro-en-accion-web/`](./ferro-en-accion-web/), [`MFA-agente-WhatsApp/`](./MFA-agente-WhatsApp/) |

El club y la agrupación son cosas distintas: acá conviven porque comparten contexto institucional, pero cada eje tiene su propósito y su forma de mantenerse al día.

## Estructura del repositorio

```
.
├── mfa/comunicacion/redes-sociales/   # Corpus e informes de Instagram y X (MFA)
├── mfa/identidad/manual-marca/       # Espejo del manual de marca
├── mfa/trabajo/web-borradores/       # Borradores de documentación para web
├── archivo-club/
│   ├── actas-cd/
│   ├── actas-asamblea/
│   ├── scripts/
│   └── notebooklm/        # Estado de la notebook NotebookLM (opcional)
├── ferro-en-accion-web/   # Sitio institucional MFA (Astro, repo aparte)
├── MFA-agente-WhatsApp/   # Investigación para un posible canal institucional por WhatsApp
└── AGENTS.md              # Reglas de trabajo para agentes y colaboradores
```

## Qué hay en cada carpeta documental

### `archivo-club/actas-cd/`

Actas y balances públicos de la Comisión Directiva, desde ~2018 hasta la fecha. Período actual: **P101** (sesiones `P101-S001` … `P101-S029`).

Los faltantes conocidos están anotados en [`archivo-club/actas-cd/index.md`](./archivo-club/actas-cd/index.md) — por ejemplo, sesiones 17 y 28 del período 100.

### `archivo-club/actas-asamblea/`

Actas, balances, convocatorias y materiales de apoyo de asambleas generales. Cubre desde ~2018; no hay acta independiente de 2021 en esta copia pública (sí el balance del ejercicio 2020–2021).

Detalle completo en [`archivo-club/actas-asamblea/index.md`](./archivo-club/actas-asamblea/index.md).

## Convenciones de nombres

Los archivos siguen el patrón `AAAA-MM-DD__tipo__referencia.ext`:

| Parte | Ejemplo | Significado |
| --- | --- | --- |
| Fecha | `2025-09-28` | Fecha del evento (sesión o asamblea), no la de publicación |
| Tipo | `cd-acta`, `asamblea-balance` | Clase de documento |
| Referencia | `p101-s024`, `ej121` | Período/sesión o ejercicio contable |

**Ejercicios contables:** cuando un documento menciona `Ejercicio N`, se interpreta como un ciclo de dos años: `E119 (2022/2023)`.

**Comisión Directiva:** esquema `P###-S###` (período + sesión) o `P###-A###` en gestiones anteriores.

**Documentos en partes:** cada parte es un archivo separado con sufijo `__part-01`, `__part-02`, etc.

Los formatos originales se conservan: PDF, DOCX e imágenes (cuando el club publicó scans de WhatsApp o CamScanner).

## Sincronización desde el sitio oficial

Los scripts descargan adjuntos desde la API REST de WordPress del club:

```bash
cd archivo-club
python3 scripts/sync_actas_cd.py
python3 scripts/sync_actas_asamblea.py
```

Si pasás `--outdir`, los caminos relativos se resuelven bajo `archivo-club/`, no según el directorio actual.

| Script | Categoría WP | Salida |
| --- | --- | --- |
| `sync_actas_cd.py` | ID 62 (Actas CD) | `archivo-club/actas-cd/` |
| `sync_actas_asamblea.py` | ID 71 (Asamblea) | `archivo-club/actas-asamblea/` |

Cada corrida regenera `index.md` y `manifest.json`. No editar esos archivos a mano salvo para corregir algo puntual que el script no capture; conviene anotar la excepción en el índice o en el manifest.

## NotebookLM

Notebook de trabajo: **`Ferro Actas Publicas`**.

- [`archivo-club/notebooklm/notebooklm-context.md`](./archivo-club/notebooklm/notebooklm-context.md) — metadata, etiquetas y criterio de clasificación.
- [`archivo-club/notebooklm/notebooklm-annotations.md`](./archivo-club/notebooklm/notebooklm-annotations.md) — fichas de lectura parcial (3 documentos verificados).

Etiquetas activas: `Asamblea - Actas`, `Asamblea - Balances`, `Asamblea - Convocatorias`, `Asamblea - Tutoriales`, `CD - Actas`, `Soporte - Indices y notas`, `Documentación General`.

Sirve para consultar con contexto y citas: última acta disponible, documentos en partes, diferencias entre fecha del archivo y fecha visible en el PDF, relaciones entre acta/balance/convocatoria del mismo período.

## Redes sociales y agrupaciones

Corpus relevado al 2026-06-25 en [`mfa/comunicacion/redes-sociales/`](./mfa/comunicacion/redes-sociales/):

- **Movimiento Ferro en Acción:** corpus de Instagram y X con foco en gestión, participación y CIARF.
- **Comparativa electoral:** análisis de `Somos Ferro`, `Primero Ferro`, `Juventud Verdolaga`, `Unidos por Oeste`, `Identidad Verdolaga` y `Todo Verde`.

Índice y análisis en [`mfa/comunicacion/redes-sociales/index.md`](./mfa/comunicacion/redes-sociales/index.md) y [`mfa/comunicacion/redes-sociales/analisis/comparativa-agrupaciones.md`](./mfa/comunicacion/redes-sociales/analisis/comparativa-agrupaciones.md).

## Identidad (manual de marca)

[`mfa/identidad/manual-marca/`](./mfa/identidad/manual-marca/) espejo del manual de marca y recursos asociados para Movimiento Ferro en Acción.

## Trabajo (borradores web)

[`mfa/trabajo/web-borradores/`](./mfa/trabajo/web-borradores/) borradores Word y artefactos de trabajo para la web (no producción).

## Sitio web MFA

[`ferro-en-accion-web/`](./ferro-en-accion-web/) es un subproyecto aparte (Astro 5, TypeScript) pensado para Cloudflare Pages. Contenido editable en Markdown (`novedades/`, `documentos/`) y textos institucionales en `src/data/site.ts`.

```bash
cd ferro-en-accion-web
npm install
npm run dev
```

Ver [`ferro-en-accion-web/README.md`](./ferro-en-accion-web/README.md) para build y deploy.

### Guía local del subproyecto

- El subproyecto tiene sus propias reglas de edición en [`ferro-en-accion-web/AGENTS.md`](./ferro-en-accion-web/AGENTS.md).
- Usar ese archivo cuando la tarea toque contenido, SEO, navegación, build o despliegue del sitio.

## Investigación: MFA Agente WhatsApp

[`MFA-agente-WhatsApp/`](./MFA-agente-WhatsApp/) reúne el research para evaluar un posible canal institucional de MFA por WhatsApp. La etapa actual es exclusivamente documental: alcance, políticas del canal, alternativas de arquitectura, necesidades de operación y decisiones pendientes. No contiene implementación ni credenciales.

## Para qué sirve este repo

- Consultar documentos históricos del club de forma ordenada.
- Seguir la secuencia de actas y balances con continuidad explícita.
- Detectar huecos, duplicados o inconsistencias entre nombre de archivo y contenido.
- Alimentar NotebookLM u otras herramientas de consulta con fuentes verificables.
- Documentar la comunicación pública de MFA junto al archivo institucional del club.

## Reglas de trabajo

Ver [`AGENTS.md`](./AGENTS.md): usar siempre la fuente pública original, no inventar fechas ni sesiones, registrar ausencias en los índices y preferir nombres legibles.
