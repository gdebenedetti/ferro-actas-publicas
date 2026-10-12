# Análisis del registro de votación 2026

## Alcance y fuentes

- Registro entregado por MFA: `VOTACIÓN FCO - todos_los_que_votaron.csv`; SHA-256 `ae96c66a71cd5c08acd4f88395028a79c4f8460df446918d19a3093297ffb806`.
- Padrón definitivo de trabajo 2026 con mesa y número de socio: `padron-ferro-en-accion-web/data/padron-2026/padron-definitivo-2026-mesas.csv`; SHA-256 `8321f948bcc97a5dbcffa113582e04f5bf6b0ae4ae962fc4edad33ebd77a1c0c`.
- Padrón electoral 2020 archivado: `archivo-club/elecciones/padrones/2020-09-08__padron-electoral__ferro.csv`; SHA-256 `96ea4c3a31ebc9dd5077826acf54d187c1de2b3c992e433a8a3e260acf8c4c0e`.
- El informe conserva únicamente agregados. El cruce persona a persona queda en el directorio local ignorado de `padron-ferro-en-accion-web/data/padron-2026/`.
- Para 2023, el archivo público local registra elegibilidad/habilitación (`padron_2023_habilitado`), no si cada socio efectivamente votó. No se completa una columna de asistencia 2023 sin una fuente de votos de esa elección.

## Resultado general

- Registros de votación: **3.392**; números de socio únicos.
- Padrón 2026: **7.868** filas; participación registrada equivalente a **43,1%** del listado.
- Cruce por número de socio normalizado y nombre coincidente: **3.244** (95,6%). Se estandarizaron prefijos y ceros a la izquierda.
- Nombre completo exacto único, pero número distinto/ausente: **130** (3,8%); quedan `REVISAR`, no se consideran cruce confirmado.
- Nombres repetidos que impiden asignar persona sin ambigüedad: **18** (0,5%). Sin coincidencia nominal: **0**.
- Mesa donde votó = mesa asignada en el sistema: **3.392 de 3.392**. Entre los cruces confirmados, la mesa del sistema coincide con la mesa del padrón en **3.244 de 3.244**.
- Marcados como referidos: **317** (9,3%); el resto no lleva esa marca. No se desglosan referentes individuales en este informe.

## Comparación histórica con el padrón 2020

Esta comparación identifica presencia en el padrón electoral archivado de 2020, no el año efectivo de alta ni una incorporación específica en 2023. Se clasifica como coincidencia fuerte sólo el mismo número de socio y nombre completo normalizados; las variaciones quedan para revisión.

| Situación respecto de 2020 | Filas del padrón 2026 | Con voto 2026 por número exacto |
| --- | ---: | ---: |
| Número y nombre exactos en 2020 | 4.063 | 1.679 |
| Número coincide, nombre difiere | 141 | 28 |
| Nombre único en 2020, número distinto/ausente | 354 | 156 |
| Nombre repetido en 2020 | 20 | 1 |
| No localizado en 2020 por número ni nombre exacto | 3.290 | 1.380 |

Hay **3.290** registros 2026 no localizados en el padrón 2020 por número ni nombre completo exactos; **1.380** tienen un voto 2026 confirmado por número de socio. Es un grupo de posibles altas posteriores a 2020, sujeto a que el padrón 2020 sea el baseline correcto y a los límites de identidad indicados; no demuestra altas posteriores a 2023.
Además, **354** filas comparten nombre completo único pero no número con registros de 2020; **156** de ellas tienen voto 2026 por número exacto. Se mantienen como revisión para no contar cambios de número o categoría como incorporaciones nuevas.

## Distribución por las mesas del padrón definitivo

La mesa registrada en el sistema concentra entre **324 y 372** votos; la participación por mesa queda entre **41,2% y 47,3%** del tamaño de cada mesa.

| Mesa | Electores en padrón | Votantes registrados | Participación |
| ---: | ---: | ---: | ---: |
| 1 | 786 | 334 | 42,5% |
| 2 | 787 | 343 | 43,6% |
| 3 | 787 | 340 | 43,2% |
| 4 | 787 | 336 | 42,7% |
| 5 | 787 | 324 | 41,2% |
| 6 | 786 | 342 | 43,5% |
| 7 | 787 | 347 | 44,1% |
| 8 | 787 | 329 | 41,8% |
| 9 | 787 | 325 | 41,3% |
| 10 | 787 | 372 | 47,3% |

La mesa 10 tiene la mayor participación (372; 47,3%); la mesa 5 tiene la menor (324; 41,2%). La diferencia es 48 votos registrados. Estas tasas describen el cruce de este registro con el padrón de trabajo; los casos no cruzados por socio requieren revisión y pueden mover cifras por mesa.

## Qué muestran los cortes de mesa

El padrón definitivo local reparte **786 o 787 registros en cada una de las diez mesas** y conserva orden alfabético por apellido y nombre. Es un patrón compatible con cortes por cantidad casi idéntica de electores. En cuatro límites, el apellido completo queda repartido entre dos mesas:

| Mesas contiguas | Apellido que aparece a ambos lados | Personas de ese apellido en ambas mesas |
| --- | --- | ---: |
| 1 y 2 | BIANCHI | 8 |
| 4 y 5 | GARRONE | 3 |
| 5 y 6 | LA TORRE | 2 |
| 8 y 9 | RODRIGUEZ | 56 |

En total, **4 apellidos** aparecen en más de una mesa, con **69 personas** en esos grupos. Los apellidos que cruzan un límite son BIANCHI, GARRONE, LA TORRE y RODRIGUEZ. Esto confirma que la asignación final divide algunos apellidos; por sí solo no documenta el motivo administrativo del criterio.

| Límite | Último apellido en mesa anterior | Primer apellido en mesa siguiente | Mismo apellido |
| --- | --- | --- | --- |
| 1 / 2 | BIANCHI | BIANCHI | Sí |
| 2 / 3 | CHAVEZ SANABRIA | CHAZANAVICIUS DE CANONICO | No |
| 3 / 4 | DRINCOVICH | DRIZZA | No |
| 4 / 5 | GARRONE | GARRONE | Sí |
| 5 / 6 | LA TORRE | LA TORRE | Sí |
| 6 / 7 | MELIAN | MELIDONI | No |
| 7 / 8 | PELLEGRINO DE BULLEJOS | PELLERANO CARDUS | No |
| 8 / 9 | RODRIGUEZ | RODRIGUEZ | Sí |
| 9 / 10 | SOSA ROJAS | SOSE | No |

## Comparación con la propuesta MFA del 21/9

La propuesta ordenaba por rangos alfabéticos y estimaba unas 206–208 participaciones por mesa (2.067,7 en total), a partir de 7.839 electores del listado provisorio. El padrón definitivo local tiene 7.868 filas (29 más). Aplicados los mismos rangos al padrón definitivo actual, todas las filas quedan asignadas; los tamaños se mantienen desiguales por diseño. La mesa 9 vuelve a ser la de mayor carga electoral, y la mesa 5 la de menor carga.

| Mesa propuesta | Electores en padrón definitivo por rango | Votos observados por apellido en ese rango | Participación observada | Estimación propuesta |
| ---: | ---: | ---: | ---: | ---: |
| 1 (ABADIN–BEN) | 706 | 305 | 43,2% | 206,4 |
| 2 (BENAGHI–CERVANTES) | 826 | 360 | 43,6% | 206,8 |
| 3 (CERVELO–DONATO) | 809 | 345 | 42,6% | 207,0 |
| 4 (DONELLI–GARCIA RETAMAR) | 770 | 325 | 42,2% | 207,1 |
| 5 (GARCIA RIVAS–JACA) | 692 | 298 | 43,1% | 207,2 |
| 6 (JACQUEMIN–MARTINO) | 826 | 342 | 41,4% | 207,4 |
| 7 (MARTORELLI–PARADISO) | 790 | 351 | 44,4% | 207,6 |
| 8 (PARAFITA–RISI) | 784 | 343 | 43,8% | 206,6 |
| 9 (RISO–SPINETTO) | 918 | 369 | 40,2% | 207,2 |
| 10 (SPITZNAGEL DE SONAGLIA–ZYSMAN) | 747 | 354 | 47,4% | 204,4 |

El registro suma **3.392** votos frente a **2.067,7** participantes estimados en la propuesta: **1.324,3** más (64,0% por encima). Esta diferencia compara un resultado registrado con una estimación previa, no implica por sí misma que la estimación fuera un compromiso de resultado.

| Mesa actual del sistema | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 1 | 305 | 29 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| 2 | 0 | 331 | 12 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| 3 | 0 | 0 | 333 | 7 | 0 | 0 | 0 | 0 | 0 | 0 |
| 4 | 0 | 0 | 0 | 318 | 18 | 0 | 0 | 0 | 0 | 0 |
| 5 | 0 | 0 | 0 | 0 | 280 | 44 | 0 | 0 | 0 | 0 |
| 6 | 0 | 0 | 0 | 0 | 0 | 298 | 44 | 0 | 0 | 0 |
| 7 | 0 | 0 | 0 | 0 | 0 | 0 | 307 | 40 | 0 | 0 |
| 8 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 303 | 26 | 0 |
| 9 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 325 | 0 |
| 10 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 18 | 354 |

La matriz anterior redistribuye por apellido los **3.392** registros de votación según la propuesta. **238** quedarían en un número de mesa distinto al que figura en el sistema actual. El cálculo usa el apellido del registro de votación, no una asignación oficial alternativa.

## Horarios y límites del registro

- Primera hora registrada: **27/09/2026 10:04:15**; última: **27/09/2026 19:30:12**.
- **21** marcas tienen hora posterior a las 19:00. El horario 09:00–19:00 del archivo de stress es un supuesto de simulación; confirmar la hora oficial de cierre y si el sistema guardaba hora de captura o de carga antes de interpretar esos registros.
- Distribución por hora local registrada:

| Hora | Registros |
| --- | ---: |
| 10:00 | 354 |
| 11:00 | 487 |
| 12:00 | 508 |
| 13:00 | 474 |
| 14:00 | 384 |
| 15:00 | 440 |
| 16:00 | 268 |
| 17:00 | 231 |
| 18:00 | 225 |
| 19:00 | 21 |

## Lecturas y próximos cruces posibles

1. El sistema registra exactamente la mesa asignada para todos los votantes del CSV; el cruce confirmado por socio también coincide con la mesa del padrón. No aparecen cambios de mesa en estos datos.
2. El patrón de 786/787 electores por mesa y los cuatro apellidos partidos es evidencia observable compatible con una partición secuencial por tamaño. Para afirmar qué instrucción recibió la Junta o por qué lo hizo haría falta el acta, instructivo o listado oficial de asignaciones.
3. No hay fuente de asistencia efectiva 2023 en el material disponible. `padron_2023_habilitado` en el CSV 2020 señala habilitación en el padrón, no que haya votado. El padrón oficial 2023 se consultaba individualmente y el proyecto no conserva un listado público completo de votantes.
4. La copia del padrón 2026 tiene 265 filas sin número de socio; junto con 130 coincidencias nominales únicas y 18 ambiguas, conviene resolver los pendientes contra el registro interno antes de tratar la marca por persona como definitiva.
5. Una vez disponible una fuente verificable de asistencia 2023, el cruce debería añadir `Voto 2023` por número de socio y separar: presentes en ambos padrones, altas 2026 que votaron, altas que no votaron y socios que ya no figuran. No se debe inferir voto 2023 desde la habilitación.

## Artefactos generados

- Base local aumentada: `/Users/guidodebenedetti/Documents/Ferro en Acción/padron-ferro-en-accion-web/data/padron-2026/participacion-votacion-2026.csv`. Columnas nuevas: `Voto 2026`, `Método de cruce`, `Mesa registrada`, `Hora registrada`, `En padrón 2020` y `Método cruce 2020`.
- Pendientes de conciliación: `/Users/guidodebenedetti/Documents/Ferro en Acción/padron-ferro-en-accion-web/data/padron-2026/cruces-votacion-2026-pendientes.csv` (148 filas).
- Script reproducible: `mfa/trabajo/coaching-electoral/scripts/analizar-votacion-2026.py`.

El padrón combinado y la lista de pendientes contienen datos personales y permanecen fuera de Git, dentro del directorio privado ignorado del subproyecto. El informe agregado no lista nombres de socios ni referentes.
