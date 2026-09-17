# Padrones electorales y de socios de Ferro Carril Oeste

Relevamiento de padrones públicos vinculados a elecciones y asambleas del Club Ferro Carril Oeste. La búsqueda se inició el 18 de agosto y se actualizó el 16 de septiembre de 2026.

## Resultado principal

Se encontró y descargó un padrón electoral completo y abierto:

- **Padrón electoral 2020**: PDF oficial de 94 páginas, publicado en septiembre de 2020. El listado incluye número de socio, nombre, edad, categoría y antigüedad. La copia servida por el sitio conserva como título interno `Padron publicar - con perspectiva de género.xlsx`, pero el archivo público descargable es un PDF.
- **Listado provisorio 2026**: PDF oficial de 168 páginas, publicado el 16 de septiembre de 2026. Incluye número de socio y nombre, agrupados en PA, PV, SA y SV. El Club advierte que todavía no es el padrón definitivo y recibe reclamos hasta el 23 de septiembre.
- **Conversión estructurada**: el PDF fue transformado en un CSV de 5.964 registros y 22 columnas. Incluye el año estimado de alta (`2020 - antiguedad_2020`) y campos vacíos para completar el cruce con 2023. La extracción fue verificada considerando que el encabezado aparece sólo en la primera página.

## Control de integridad de la conversión

- Las 5.964 filas detectables del PDF coinciden con las 5.964 filas del CSV, página por página, en las 94 páginas.
- No hay números de socio ordinarios duplicados.
- No hay registros completos duplicados.
- `SD 30000` aparece 16 veces de manera intencional, como código simbólico de los registros de socios/as ausentes por desaparición forzada.
- Hay 13 nombres repetidos con números de socio diferentes. Pueden corresponder a homónimos o a más de un registro de una misma persona; por eso el cruce futuro debe priorizar `nro_socio` y no sólo `nombre`.

Este control confirma que no se perdieron filas durante la extracción del PDF, pero no puede demostrar que el padrón original no tuviera omisiones, altas duplicadas o errores de identidad. Esa validación sólo será posible al compararlo con otro padrón, legajos o el sistema oficial de socios.

Para 2023, el club publicó un **portal de consulta individual por DNI**, no un PDF/XLSX con el listado completo. La captura histórica del portal confirma que se trataba del “PADRÓN ELECTORAL FERRO CARRIL OESTE 2023”, con consulta de habilitación, mesa y orden. No se encontró una respuesta individual ni una copia pública del listado completo archivada por Internet Archive.

El 16 de septiembre de 2026 el Club publicó el **listado provisorio de socios y socias aptos para votar** para las elecciones de 2026. La publicación aclara que no constituye el padrón definitivo, informa un plazo de reclamos hasta el 23 de septiembre y adjunta un PDF de 168 páginas con 7.855 filas numeradas. El archivo conserva cuatro categorías de socio (PA, PV, SA y SV) y 16 registros simbólicos `SD 30000`, que se excluyen de la consulta. La fuente no incluye DNI.

## Archivos locales

| Año / fecha | Archivo | Qué es | Fuente original |
| --- | --- | --- | --- |
| 2018-07 | `2018-07__estatuto-club-ferro.pdf` | Estatuto con reglas sobre electores y supervisión del padrón. | [Estatuto oficial](https://ferrocarriloeste.org.ar/wp-content/uploads/2018/07/Estatuto.pdf) |
| 2020-09-08 | `2020-09-08__padron-electoral__ferro.pdf` | **Padrón electoral completo**, 94 páginas. | [PADRON.pdf oficial](https://www.ferrocarriloeste.org.ar/wp-content/uploads/2020/09/PADRON.pdf) |
| 2020-09-08 | `2020-09-08__padron-electoral__ferro.csv` | Conversión tabular: 5.964 registros, 22 columnas, campos de cruce 2023 y año de alta estimado. | Derivado del PDF oficial, conservando la fuente arriba enlazada. |
| 2020-09-08 | `2020-09-08__padron-electoral__ferro.xlsx` | Planilla complementaria con fórmulas, filtros visuales, validaciones y hoja de notas. | Derivada del CSV/PDF oficial. |
| 2023-08-24 | `2023-08-24__recomendaciones-junta-electoral.pdf` | Reglas y fechas de publicación/reclamo del padrón electoral 2023. | [Recomendaciones de la Junta Electoral](https://www.ferrocarriloeste.org.ar/wp-content/uploads/2023/08/Elecciones-FCO-2023-Junta-Electoral-documento-final.pdf) |
| 2023-09 | `2023-09__resolucion-impugnacion-padron.pdf` | Resolución sobre cuestionamientos al padrón 2023; compara los padrones 2020 y 2023. | [Resolución oficial](https://www.ferrocarriloeste.org.ar/wp-content/uploads/2023/09/Resolucion-sobre-la-impugnacion-efectuada-por-la-agrupacion-Primero-Ferro.pdf) |
| 2023-12-06 | `2023-12-06__captura-wayback__portal-padron.html` | Captura pública del portal: confirma que el sistema era el padrón electoral 2023 y consultaba por DNI. | [Internet Archive](https://web.archive.org/web/20231206134022id_/https://padron.ferrocarriloeste.org.ar/) |
| 2026-08-18 | `2026-08-18__portal-padron__actual.html` | Copia del portal actualmente accesible; muestra el padrón de asamblea 2025, no un listado electoral 2026. | [Portal público](https://padron.ferrocarriloeste.org.ar/index.php) |
| 2026-09-16 | `2026-09-16__listado-provisorio-potenciales-votantes.pdf` | **Listado provisorio 2026**, 168 páginas, 7.855 filas numeradas; 7.839 registros ordinarios consultables y 16 códigos simbólicos `SD 30000` excluidos. | [Publicación oficial del listado provisorio](https://www.ferrocarriloeste.org.ar/junta-electoral/listado-provisorio-de-socios-y-socias-aptos-para-votar/) |
| — | `wayback__capturas-portal-padron.json` | Índice de capturas públicas del portal; no registra respuestas individuales del endpoint de consulta. | [Índice CDX de Internet Archive](https://web.archive.org/cdx/search/cdx?url=padron.ferrocarriloeste.org.ar/*&from=2023&to=2026&output=json&filter=statuscode:200&collapse=digest) |

## Fuentes web y contexto

- [Comunicado de la Junta Electoral 2020](https://www.ferrocarriloeste.org.ar/institucional/comunicado-de-la-junta-electoral/): anuncia que el padrón se publicaría el 7 de septiembre de 2020 y que incluiría número de asociado, nombre, fecha de nacimiento y antigüedad.
- [Padrón electoral 2023](https://www.ferrocarriloeste.org.ar/club/padron-electoral/): remite al portal de consulta individual para la elección del 17 de septiembre de 2023.
- [Condiciones generales de las elecciones 2023](https://www.ferrocarriloeste.org.ar/comision-directiva/elecciones-en-ferro-condiciones-generales/): informa fechas, acreditación y vínculo al portal de consulta.
- [Comunicado institucional posterior a las elecciones 2023](https://ferrocarriloeste.com.ar/m_index1.php?noti=23726): resume objeciones sobre diferencias entre los padrones 2020 y 2023 y la respuesta de la Junta Electoral.
- [Nota de Doble Amarilla sobre el padrón 2023](https://www.dobleamarilla.com.ar/rosca/elecciones-en-ferro--la-oposicion-denuncia--serias-irregularidades--en-el-padron--pero-el-oficialismo-lo-desmiente_a64f3c72938458bd4bb9aa60b): fuente periodística que describe el acceso por DNI y el plazo de reclamos; se conserva como contexto, no como fuente primaria.
- [Mención periodística a elecciones 2026](https://www.dobleamarilla.com.ar/rosca/comicios-en-el-futbol-argentino--las-elecciones-internas-que-marcan-el-2026-en-los-clubes-de-primera-y-el-ascenso_a69d980a11d2d404fa6ebe77b): menciona septiembre de 2026 como fecha prevista, todavía sin padrón electoral público encontrado en la web oficial al momento del corte.

También se revisó la [API pública de búsqueda del sitio oficial](https://www.ferrocarriloeste.org.ar/wp-json/wp/v2/search?search=padron&per_page=100): el resultado relevante sigue siendo la publicación de 2023; no apareció una publicación 2026 específica de padrón.

## Qué se impugnó en 2023 y qué respondió la Junta Electoral

La resolución oficial de septiembre de 2023 trató cuatro planteos principales:

1. **199 personas que figuraban en el padrón 2023 y no en el de 2020.** La Junta explicó que 124 eran socios/as vitalicios dados de baja en 2016 por no completar el reempadronamiento iniciado en 2014 y luego reincorporados al sistema cuando volvieron a contactarse con el club. Para otros casos mencionó recupero de antigüedad mediante cánones, licencias que conservaban la antigüedad y personas que cumplían los requisitos. Rechazó que fueran inclusiones irregulares.
2. **120 diferencias de antigüedad entre 2020 y 2023.** La Junta focalizó la revisión en 60 casos: 43 altas de septiembre de 2019 y 17 altas del 8 de septiembre de 2020. Revisó historiales de cuotas, recibos y documentación exhibida por el club, y no encontró elementos suficientes para excluirlos.
3. **241 altas durante el ASPO de marzo a septiembre de 2020.** El grupo estaba compuesto por 153 plenos activos, 80 semiplenos activos y 8 plenos jubilados. El club informó que la oficina de socios siguió trabajando de forma remota y parcialmente presencial, incluyendo cobro y recupero de socios. La Junta hizo verificaciones aleatorias y comprobó el requisito de antigüedad, con atención especial a las altas del 8 de septiembre.
4. **Altas posteriores al 28 de agosto de 2020 y hasta la elección.** La impugnación sostenía que el 28 de agosto debía ser la fecha de corte. La Junta interpretó que la edad y la antigüedad debían cumplirse al momento de la elección, el 17 de septiembre de 2023, y que el padrón publicado era provisional. Por ese motivo también rechazó este planteo.

Además, una comunicación anónima sobre supuestas “alteraciones del padrón” fue considerada extemporánea y no fue tratada, porque había sido remitida después del plazo de reclamos del 4 de septiembre. La resolución terminó rechazando los planteos y mantuvo la validez del padrón 2023 para la elección.

## Límites y faltantes

- El padrón 2020 contiene datos personales publicados por el club; se conserva como copia documental sin reproducir el listado en este índice.
- `padron_2020_ok = SI` significa que la fila fue extraída del PDF 2020 y pasó los controles de estructura; no significa que se haya validado todavía contra el padrón 2023.
- `anio_alta_estimado_2020` se calcula como `2020 - antiguedad_2020`. Es una estimación por año, no una fecha exacta de alta.
- Hay 16 registros `SD 30000`, con la categoría oficial “Elector/a ausente por desaparición forzada (Art. 9 Dec. 935/2010)”. Se conservan como registros simbólicos diferenciados mediante `tipo_registro_2020`; no se les asigna antigüedad ni año de alta estimado.
- El portal 2023 y el portal actual requieren ingresar un DNI para devolver el resultado. No se intentó enumerar personas ni reconstruir la base de datos mediante consultas masivas.
- La resolución 2023 menciona anexos documentales compartidos por WeTransfer, pero esos anexos no aparecen como archivos permanentes en el sitio oficial y el enlace temporal no se tomó como una descarga estable.
- El listado 2026 disponible es provisorio y no equivale al padrón electoral definitivo. No incluye DNI, mesa ni orden; esos datos sólo podrán agregarse cuando el Club publique una fuente oficial que los contenga.
