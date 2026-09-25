# Versionado del research electoral

## Versión vigente

**v0.13.0 — 2026-09-25**

Versión trazable del paquete de coaching electoral de Movimiento Ferro en Acción, con el análisis del debate presidencial de FerroWeb y la actualización del corte electoral de las tres agrupaciones.

La versión incorpora la transcripción automática original del debate presidencial de FerroWeb del 24/9, publicada el 25/9, junto con una línea de tiempo de voces, candidatos, moderación, video explicativo, publicidad y cortes técnicos. Incluye dos lecturas separadas: una comparación imparcial del desempeño y otra centrada en la actuación de MFA.

La transcripción se conserva como VTT bruto y permanece en estado `transcript-localizado`: los nombres se normalizan en el análisis contra la nómina oficial, pero las cifras, acusaciones y negaciones requieren contraste con audio y documentos.

La versión incorpora el bloque electoral del PGM 216 de FerroWeb, con Santiago Alfis como apoderado de MFA, además de las intervenciones de Somos Ferro e Identidad Verdolaga. Los subtítulos automáticos permiten localizar pasajes, pero las cifras y afirmaciones jurídicas siguen requiriendo validación documental. También mantiene las actualizaciones operativa, comparativa y de la entrevista a Pedro Masó.

También registra la composición oficial de Junta Electoral comunicada al equipo, sin exponer detalles internos de la negociación.

Se agrega la nota de FerroWeb sobre la presentación de Somos Ferro, con la fórmula consignada, el anuncio del debate del 24/9 y la limitación documentada de la transcripción del video.

Se incorpora la transcripción aportada por el equipo, con estado `transcript-localizado`, discrepancias nominales señaladas y una matriz de afirmaciones financieras y de auditoría que requiere contraste con audio y documentos.

Se incorpora la fórmula comunicada por Identidad Verdolaga y su mensaje de continuidad, con separación entre texto de campaña, promesas y afirmaciones que requieren respaldo documental.

Se incorpora la entrevista extensa de Hablemos de Ferro a Patricio Baigorrotegui, con clasificación de tono facilitador, bloques temáticos, cifras sensibles y preguntas hostiles derivadas.

Se actualiza el marco operativo tras la confirmación oficial de que las elecciones se realizarán el 27/9: la IGJ pasa a ser antecedente y el padrón provisorio publicado el 16/9 pasa a ser el foco documental inmediato. Se agrega el corte público de X e Instagram del 20/9 para MFA, Somos Ferro e Identidad Verdolaga, con el desplazamiento del coaching hacia comparación de propuestas, fórmulas, primeros 90 días y preparación del debate.

## Alcance de v0.12.0

- Confirmación institucional actualizada: el pedido de suspensión ante la IGJ no prosperó y la elección del 27/9 sigue vigente.
- Incorporación del listado provisorio 2026 publicado el 16/9: 7.855 filas, reclamos hasta el 23/9 y padrón definitivo todavía pendiente.
- Corte de X e Instagram consultado el 20/9 para MFA, Somos Ferro e Identidad Verdolaga.
- Nuevo argumentario comparativo sobre elección confirmada, padrón, continuidad, propuestas y debate.

## Alcance de v0.11.0

- Registro del bloque electoral del PGM 216 de Hablemos de Ferro, publicado el 14/9/2026, con timestamps de Somos Ferro, MFA e Identidad Verdolaga.
- Subtítulos automáticos localizados y advertencias sobre errores nominales, cifras y afirmaciones jurídicas.
- Incorporación del contraste con el listado provisorio 2026 de 7.855 filas y el reclamo de más de 8.000 habilitados en el programa.

## Alcance de v0.9.0

- Entrevista a Pedro Masó en Splendid AM 990 / Solo x Deporte, fechada el 23/7/2026.
- Ejes localizados de MFA: participación de socios, prioridad del fútbol sin descuidar disciplinas, renovación de la conducción, director deportivo, plan integral de fútbol, obras a diez años y unidad posterior a la elección.
- Correcciones y límites de subtítulos automáticos, con cifras de socios y votantes en estado pendiente.
- Preguntas hostiles derivadas para transformar mensajes generales en mecanismos, responsables, plazos y controles.

## Alcance de v0.8.0

- Comparación de la plataforma de Somos Ferro por propuesta, ejecución, responsables, recursos, plazos e indicadores.
- Módulo de padrón y elegibilidad que distingue coberturas históricas de un padrón oficial 2026 todavía pendiente.
- Clasificación operativa de medios y entrevistas por conductas observables, sin convertir inferencias editoriales en hechos.
- Checklist previo al debate del 24/9 y priorización de fichas, validación audiovisual y simulaciones.

## Alcance de v0.1.0

- Repaso documental inicial del proyecto y repositorios.
- Actualización pública de agrupaciones al 6/9/2026.
- Plataforma PDF y web de Somos Ferro.
- Cronología reciente de Identidad Verdolaga.
- Novedades de MFA y posiciones públicas sobre Junta Electoral.
- Corpus de nueve entrevistas, debates y asambleas históricas aportadas en el hilo.
- Banco inicial de preguntas hostiles y reglas para validar transcripciones.
- Matriz comparativa por temas y base de simulación hostil para una futura sesión de voz.
- Composición oficial de la Junta Electoral: cuatro lugares de Identidad Verdolaga y uno de Somos Ferro.

## Estados de evidencia

- `observado`: leído directamente en fuente pública.
- `transcript-localizado`: transcript automático exportado, aún sujeto a control de audio.
- `original-contrastado`: cotejado con documento, imagen o publicación primaria.
- `declaración`: lo afirma una agrupación, medio o dirigente; no implica que el hecho esté probado.
- `pendiente`: falta documento, audio, fecha, resolución o decisión de MFA.

## Regla de actualización

Cada corte nuevo debe:

1. conservar el documento anterior;
2. agregar fecha de consulta y fuentes originales;
3. distinguir cambio factual de interpretación;
4. registrar correcciones de nombres, cifras y transcripciones;
5. actualizar el changelog y subir la versión menor (`v0.2.0`, `v0.3.0`) cuando agregue investigación nueva;
6. reservar versiones de parche (`v0.2.1`) para correcciones editoriales sin nuevo research.

## Fuentes y límites de esta versión

La captura no es un monitoreo permanente ni prueba intención de voto. Los conteos de redes son fotografías públicas. Los subtítulos automáticos y OCR sirven para localizar pasajes; las citas sensibles requieren audio, imagen o documento original. El debate del 24/9 ya tiene video y transcripción automática archivados, pero los pasajes sensibles siguen requiriendo contraste con audio, documentos y fuentes originales.
