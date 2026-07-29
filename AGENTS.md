# AGENTS.md

Este repositorio es un archivo curado de documentación pública vinculada a Ferrocarril Oeste y a Movimiento Ferro en Acción (MFA).

## Alcance

- `archivo-club/actas-cd/` y `archivo-club/actas-asamblea/`: espejo documental del club.
- `mfa/comunicacion/redes-sociales/`: corpus, análisis y comparativas de la comunicación pública de MFA y de otras agrupaciones.
- `mfa/identidad/manual-marca/`: manual de marca y recursos asociados.
- `mfa/trabajo/web-borradores/`: borradores Word y artefactos de trabajo para web (no producción).
- `ferro-en-accion-web/`: sitio institucional de MFA, con contenido editable en Markdown y textos de soporte.

## Objetivo

- Buscar, identificar, descargar y ordenar actas, balances, convocatorias y materiales públicos de apoyo.
- Mantener la información agrupada por tipo, fecha y referencia de asamblea, sesión o campaña.
- Priorizar la continuidad documental y registrar faltantes, dudas o ausencias en los `index.md`.
- Conservar separado lo que es archivo institucional del club, comunicación de MFA y análisis comparativo de agrupaciones.

## Regla de trabajo

- Usar siempre la fuente pública original como referencia.
- No inventar fechas, sesiones, nombres de archivo, métricas o integrantes.
- Si un documento parece duplicado, partido en varias partes o mal nombrado, anotarlo y normalizarlo.
- Si hay una ausencia, dejarla explícita en el índice o anexo correspondiente.
- Preferir nombres de archivo consistentes y legibles antes que nombres técnicos.
- Cuando un texto sea inferencia o lectura política, marcarlo como tal y separar evidencia de interpretación.

## Criterio de búsqueda

- Buscar primero por fecha, tipo de documento, usuario/cuenta y patrón del sitio o red.
- Confirmar la fecha visible del documento o publicación antes de registrar un archivo.
- Cuando haya duda, conservar el dato en el índice con una nota breve.
- En redes sociales, registrar métricas sólo si son visibles públicamente al momento del corte.
- En TikTok y otras plataformas bloqueadas, dejar constancia del bloqueo o de la falta de acceso sin completar con suposiciones.

## Criterios por subproyecto

### Archivo institucional

- No editar a mano `index.md` o `manifest.json` generados por scripts salvo correcciones puntuales.
- Mantener la nomenclatura consistente por fecha, tipo y referencia.
- Registrar en los índices los faltantes conocidos, documentos en partes y diferencias entre fecha de archivo y fecha visible.

### Redes sociales

- Mantener el corpus, el análisis y la comparativa enlazados entre sí.
- Cuando haya mucho volumen, priorizar el detalle completo en las piezas relevantes y dejar trazabilidad hacia el corpus.
- Distinguir con claridad entre baseline, comparativa y anexos por agrupación.
- Si una agrupación no tiene sitio, Instagram o TikTok público detectado, dejarlo asentado como ausencia, no como omisión.

### Sitio web MFA

- Tratar `ferro-en-accion-web/` como subproyecto editable pero separado del archivo documental.
- Mantener el contenido institucional coherente con el corpus público de redes y con el sitio original de MFA.
- No mezclar materiales del sitio con el archivo histórico del club salvo en índices o textos de navegación.
- Conservar la base de analítica del sitio al editar la web: no borrar `src/components/Analytics.astro`, `functions/api/track.ts`, `wrangler.toml`, ni el patrón `data-track-*` sin revisar el impacto.
- Cuando se agreguen o modifiquen CTAs, chips, pastillas, acordeones, links internos, mailto, descargas o redes, etiquetarlos con `data-track-*` para mantener el seguimiento fino.
- Mantener la separación de responsabilidades: Cloudflare Web Analytics para pageviews/performance y el endpoint propio para interacciones UI.
