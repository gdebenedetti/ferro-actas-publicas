# Versionado del research electoral

## Versión vigente

**v0.10.0 — 2026-09-17**

Versión trazable del paquete de coaching electoral de Movimiento Ferro en Acción, con el primer marco comparativo y de simulación.

La versión incorpora la entrevista pública a Pedro Masó, jefe de campaña de Ferro en Acción, y registra un nuevo programa de FerroWeb localizado sin transcripción pública. También mantiene la actualización operativa y comparativa de la versión anterior. Las posiciones específicas de MFA, las cifras electorales y el contenido hablado del nuevo video siguen requiriendo definición o validación documental.

También registra la composición oficial de Junta Electoral comunicada al equipo, sin exponer detalles internos de la negociación.

Se agrega la nota de FerroWeb sobre la presentación de Somos Ferro, con la fórmula consignada, el anuncio del debate del 24/9 y la limitación documentada de la transcripción del video.

Se incorpora la transcripción aportada por el equipo, con estado `transcript-localizado`, discrepancias nominales señaladas y una matriz de afirmaciones financieras y de auditoría que requiere contraste con audio y documentos.

Se incorpora la fórmula comunicada por Identidad Verdolaga y su mensaje de continuidad, con separación entre texto de campaña, promesas y afirmaciones que requieren respaldo documental.

Se incorpora la entrevista extensa de Hablemos de Ferro a Patricio Baigorrotegui, con clasificación de tono facilitador, bloques temáticos, cifras sensibles y preguntas hostiles derivadas.

## Alcance de v0.10.0

- Registro del PGM 216 de Hablemos de Ferro, publicado el 14/9/2026, con descripción pública y estado `localizado-sin-transcript`.
- Separación explícita entre contexto deportivo del medio y evidencia electoral no observada.

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

La captura no es un monitoreo permanente ni prueba intención de voto. Los conteos de redes son fotografías públicas. Los subtítulos automáticos y OCR sirven para localizar pasajes; las citas sensibles requieren audio, imagen o documento original. El debate del 24/9 sigue sin confirmación pública.
