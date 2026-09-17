# Revisión de redes para actualización editorial de la web

**Movimiento Ferro en Acción — corte: 2026-08-28**  
**Alcance:** revisión editorial y de recursos para aprobación. No se modificó ferro-en-accion-web/, ni sus componentes, contenido de producción o configuración. No se hicieron commits, pushes ni deploys.

## Decisiones editoriales recibidas — 2026-08-28

- Se interpreta “subtrinidad de Comunidad” como “subprioridad de Comunidad”. Esta es una inferencia de redacción y debe corregirse antes de implementar si no refleja la intención exacta.
- Se autoriza publicar ingresos extraordinarios, alianzas estratégicas y horizonte a diez años con el mismo nivel de precisión que tienen las publicaciones, sin agregar cifras, mecanismos, responsables ni resultados no publicados.
- Novedades debe registrar resultados de reuniones y encuentros realizados, no convocatorias futuras. La invitación permanente autorizada es encontrarse en Av. Avellaneda & Pje. Paysandú, en la previa de los partidos en que Ferro juega de local, para intercambiar, comentar propuestas, escuchar las propuestas de Ferro y sumarse a colaborar.
- No se publicarán por ahora nombres de personas, equipos, profesionales, referentes ni nóminas; quedan fuera del alcance hasta un anuncio posterior.
- Se aprueba incorporar la formulación “Asociación Civil Sin Fines de Lucro” y la conducción del club por sus socios, tal como aparece en la comunicación revisada.
- Se autoriza reutilizar las imágenes y videos propios para esta actualización editorial. Cuando una publicación o hilo se lleve a Novedades, la redacción debe conservar casi literalmente el texto oficial, con ajustes mínimos de título y formato; no se incorporan comentarios de terceros.

## Resumen ejecutivo

Las siete publicaciones de X revisadas entre el 12 y el 27 de agosto de 2026, junto con las piezas recientes de Instagram de agosto y julio, consolidan cuatro líneas que la web ya anticipa, pero todavía no desarrolla con la misma especificidad: planificación económica, plan de infraestructura con horizonte de diez años, gestión profesional con rendición de cuentas y una política integral de salud mental.

La novedad más significativa es salud mental: aparece como tema de trabajo, prevención, escucha y acompañamiento para trabajadores, deportistas, socios y socias, pero no tiene una sección equivalente en la plataforma actual. Según la decisión recibida, se propone tratarla como subprioridad de Comunidad, no como una política operativa con detalles que todavía no fueron publicados. También se observa una actividad participativa reciente —reuniones y encuentros— que hoy queda dispersa en Novedades.

Recomendación de mayor impacto: actualizar Comunidad con una subprioridad de cuidado y salud mental, registrar resultados de reuniones en Novedades y sumar un archivo de encuentros realizados. Para infraestructura y economía conviene actualizar las prioridades existentes con el mismo nivel de detalle de las redes, sin convertir ese lenguaje en compromisos técnicos adicionales.

## Método, corte y límites

- Se revisaron en Chrome las siete URL de X indicadas y el perfil @ferroenaccion; se registraron los textos visibles, fechas, hilos, imágenes y video/portada cuando fueron accesibles.
- En Instagram se revisó la pestaña del perfil dejada abierta por el usuario (36 publicaciones, 1.232 seguidores, 9 seguidos, valores visibles al corte) y se abrieron directamente doce piezas recientes.
- Las métricas de X se anotan sólo cuando la interfaz mostró “Visualizaciones”. No se interpretan los números de botones sin etiqueta ni se comparan métricas entre plataformas.
- Las fechas de las publicaciones se tomaron de la fecha visible/metadatos de cada publicación, no de las solicitudes de medios.
- X permitió descargar 17 JPEG, incluida la portada del video del 25/08, mediante los recursos públicos visibles en Chrome. El video de X sólo quedó disponible como portada: el reproductor usó una URL blob: y no se obtuvo un MP4.
- Instagram permitió descargar 19 JPEG nuevos de trece publicaciones directas —las doce piezas principales y Dbd3poniaFo, abierta directamente por su relevancia— y recuperar fragmentos DASH de cinco Reels. El bundler devolvió `TypeError: Failed to fetch`, pero la reproducción visible permitió descargar los rangos de video/audio y ensamblar cinco MP4 completos verificados. No se reemplazó ningún recurso por otra fuente.

## Publicaciones de X relevadas

| Fecha y publicación | Texto principal observado | Tema, CTA o evento | Multimedia y dato visible |
| --- | --- | --- | --- |
| 2026-08-27 — [2093086096309563664](https://x.com/ferroenaccion/status/2093086096309563664) | “Nos juntamos a trabajar pensando en el Ferro que soñamos y queremos. El presente económico y financiero nos exige responsabilidad, y obliga a pensar una planificación y tener la capacidad de generar ingresos extraordinarios que nos permitan llevar a cabo todo lo que se necesita”. | Reunión de trabajo; planificación económica y financiera; ingresos extraordinarios. No anuncia lugar, fecha ni resultado concreto. | 4 imágenes visibles; 829 visualizaciones. El hilo agrega club moderno, socios protagonistas, vínculos/aliados estratégicos y herramientas para crecer. |
| 2026-08-26 — [2092768168984895969](https://x.com/ferroenaccion/status/2092768168984895969) | “Ferro necesita obras, lo sabemos. Necesita tener una planificación y un orden de prioridad de esas obras. Por eso proponemos poner en valor las instalaciones del club, llevar a cabo un programa de mantenimiento, un plan integral de infraestructura.” | Propuesta de obras priorizadas, mantenimiento y plan integral. El hilo precisa corto, mediano y largo plazo, etapas, plazos, presupuestos y un plan institucional a diez años. | 2 imágenes visibles; 450 visualizaciones. |
| 2026-08-25 — [2092349463553532017](https://x.com/ferroenaccion/status/2092349463553532017) | “La prevención, la escucha y el acompañamiento debe ser uno de los pilares del Ferro que se viene. Creemos imprescindible construir una política integral de salud mental, que forme parte de la formación y acompañamiento de cada trabajador, deportista, socio y socia del Club.” | Salud mental como política integral; prevención, escucha, acompañamiento y formación. No se detallan protocolo, equipo, alcance ni implementación. | Video visible de 0:50 y portada; 758 visualizaciones. La portada quedó descargada en `x/`; el MP4 no se obtuvo por la URL `blob:` del reproductor. |
| 2026-08-21 — [2090875531512205662](https://x.com/ferroenaccion/status/2090875531512205662) | “Nos encontramos con socios y socias de Ferro, profesionales de la salud, profesores, docentes; para conversar sobre un pilar fundamental de nuestro proyecto de Club: hacer del cuidado de la salud mental una prioridad y trabajo diario.” | Encuentro realizado sobre salud mental; participan, según el texto, socios/as, profesionales de la salud, profesores y docentes. El hilo habla de una política integral para trabajadores, deportistas y socios. | 4 imágenes visibles; 1.858 visualizaciones. |
| 2026-08-20 — [2090463619511099423](https://x.com/ferroenaccion/status/2090463619511099423) | “Queremos un Ferro gestionado con profesionalismo, planificación y responsabilidad. Con dirigentes presentes, que conozcan el club, acompañen a sus trabajadores y entiendan que cada decisión tiene que estar al servicio de Ferro.” | Gestión profesional y dirigencia presente. El hilo suma planificar, evaluar, rendir cuentas, escuchar y participar. | 1 imagen visible; 913 visualizaciones. Se observó además un comentario público que pregunta por una eventual participación previa en el gerenciamiento del fútbol de Bragarnik; no se toma como hecho y requiere respuesta humana si se decide abordarlo. |
| 2026-08-18 — [2089847175991681325](https://x.com/ferroenaccion/status/2089847175991681325) | “El Ferro que soñamos, necesita una nueva en generación en la conducción del Club. Con socios y socias presentes en el día a día, comprometidos con la historia de Ferro. Una nueva etapa sin personalismos. Con trabajo en equipo y con visión de futuro.” | Nueva generación, socios presentes, trabajo en equipo, visión de futuro y ausencia de personalismos. El hilo cierra con “Es con todos”. | 4 imágenes visibles; 819 visualizaciones. Se conserva la redacción original, incluida la errata “nueva en generación”. |
| 2026-08-12 — [2087682797049712790](https://x.com/ferroenaccion/status/2087682797049712790) | “Seguimos sumando miradas y construyendo propuestas para Ferro. Este jueves nos encontramos para trabajar sobre salud mental y deporte, desde una mirada comunitaria y preventiva. Nos cuidamos en equipo.” | Convocatoria a encuentro de salud mental y deporte. Al corte, el evento ya pasó; no se informa lugar ni hora en el post. | 1 imagen visible; 447 visualizaciones. |

### Lectura de los hilos de X

Los hilos no agregan cifras, nombres de equipos ni responsables de ejecución, pero sí amplían el mensaje: club moderno y sólido; socios como protagonistas; alianzas estratégicas; planificación a diez años; presupuestos; club lindo, visible y seguro; y una asociación civil sin fines de lucro conducida por sus socios. Son insumos editoriales, no documentación técnica ni prueba suficiente para publicar compromisos cerrados.

## Instagram: publicaciones y contenidos efectivamente revisados

Se revisaron directamente las doce piezas siguientes, con fecha y caption visibles en Instagram:

| Fecha | Publicación | Contenido observado y lectura editorial |
| --- | --- | --- |
| 2026-08-27 | [DcjuvdVEaFM](https://www.instagram.com/ferroenaccion/p/DcjuvdVEaFM/) | Caption completo sobre una reunión de trabajo, situación económica/financiera, planificación, ingresos extraordinarios, aliados estratégicos y socios protagonistas. Es la versión más desarrollada del X del 27/08. La interfaz mostró 132 likes y 8 comentarios al corte. |
| 2026-08-26 | [DchevLPkldJ](https://www.instagram.com/ferroenaccion/p/DchevLPkldJ/) | Obras, prioridades, mantenimiento, plan integral y plan a corto, mediano y largo plazo, con etapas, plazos y presupuestos; horizonte institucional de diez años. |
| 2026-08-25 | [DcefpGPyQw4](https://www.instagram.com/ferroenaccion/reel/DcefpGPyQw4/) | Reel sobre prevención, escucha, acompañamiento y política integral de salud mental con abordaje profesional y responsable. La presencia de una cuenta personal en la interfaz no se usa para atribuir cargos o integrar equipos. |
| 2026-08-23 | [DcZPieYipCf](https://www.instagram.com/ferroenaccion/reel/DcZPieYipCf/) | Convocatoria a una previa antes de un partido, “mañana desde las 18:00”. Es una actividad puntual ya pasada, no un evento próximo. |
| 2026-08-21 | [DcUBtriEad3](https://www.instagram.com/ferroenaccion/p/DcUBtriEad3/) | Encuentro con socios/as, profesionales de la salud, profesores y docentes para trabajar cuidado, prevención, escucha y acompañamiento en salud mental. |
| 2026-08-20 | [DcRGck6FOen](https://www.instagram.com/ferroenaccion/p/DcRGck6FOen/) | Gestión con profesionalismo, planificación, responsabilidad, evaluación y rendición de cuentas; afirma que Ferro es una Asociación Civil Sin Fines de Lucro conducida por y para sus socios. El usuario aprobó incorporar esta formulación jurídica y política en la web. |
| 2026-08-12 | [Db9WCJzEssN](https://www.instagram.com/ferroenaccion/p/Db9WCJzEssN/) | Convocatoria a trabajar salud mental y deporte desde una mirada comunitaria y preventiva. Los comentarios visibles incluyen preguntas, pero no se toman como declaraciones de Ferro. |
| 2026-07-29 | [DbZTE0zjseE](https://www.instagram.com/ferroenaccion/reel/DbZTE0zjseE/) | Festejo del 122.º aniversario; club de socios, para toda la familia; deseo de ascender; construcción “con todos”. El ascenso aparece como deseo político/deportivo, no como dato o promesa verificable. |
| 2026-07-29 | [DbZG6x6khzt](https://www.instagram.com/ferroenaccion/p/DbZG6x6khzt/) | Celebración familiar y comunitaria del aniversario; alternativa seria, trabajo cotidiano y Ferro como construcción colectiva. |
| 2026-07-22 | [DbHR7c1D4hS](https://www.instagram.com/ferroenaccion/reel/DbHR7c1D4hS/) | Equipo preparado y profesional, trabajo integral, saber qué hacer y cómo hacerlo; CTA “Acompañanos”. Los comentarios preguntan por nombres, pero no hay nómina pública que permita responderlos. |
| 2026-07-21 | [DbEeotTksjH](https://www.instagram.com/ferroenaccion/p/DbEeotTksjH/) | Presentación de ejes, nueva etapa, transparencia, planificación, gestión profesional y participación. Los comentarios visibles sugieren preguntas FAQ sobre CIARF, “nueva etapa” e integrantes; son oportunidades de contenido, no fuentes para contestar. |
| 2026-07-21 | [DbDvDN_lJdt](https://www.instagram.com/ferroenaccion/reel/DbDvDN_lJdt/) | CTA “Sumate a Ferro en Acción”; asociación entre acción, construcción de un club mejor y Ferro como tarea de todos. |

Además, en la grilla visible del perfil se revisaron piezas recientes sobre escuchar a socios/as y sus ideas (DbwPCjEjJ_m), junto con reuniones abiertas y convocatorias previas. La pieza Dbd3poniaFo queda excluida del tratamiento editorial por validación humana posterior: no se la considera evidencia para publicar un encuentro, acompañamiento o referentes. El recurso descargado se conserva sólo como material técnico de trazabilidad y no se usa en la web.

## Eventos, reuniones y actividades detectados

| Fecha de publicación | Estado y actividad | Qué puede afirmarse | Qué falta confirmar |
| --- | --- | --- | --- |
| 2026-08-27 | Reunión de trabajo | Se trabajó sobre el Ferro deseado y sobre planificación económica/financiera. | Fecha y lugar del encuentro, participantes, resultados, herramientas concretas y alcance de “ingresos extraordinarios”. |
| 2026-08-12 / 2026-08-21 | Convocatoria y posterior encuentro sobre salud mental y deporte | Hubo una convocatoria comunitaria/preventiva y luego un encuentro con socios/as, profesionales de la salud, profesores y docentes. | Lugar, fecha/hora exacta del encuentro, síntesis de conclusiones, equipo/protocolo y próximos pasos. |
| 2026-08-23 | Previa antes de un partido | Se convocó al “pueblo verdolaga” para una actividad al día siguiente desde las 18:00. | Partido, lugar exacto, asistencia y resultado; no corresponde presentarlo como próximo. |
| 2026-07-29 | Festejo del 122.º aniversario | Se observan celebraciones familiares y entre amigos. | Datos logísticos y autorización para usar imágenes de terceros si se incorpora material. |

No aparece en estas publicaciones un evento futuro con fecha confirmada para cargar ahora. Por decisión editorial, Novedades debe registrar resultados de reuniones y encuentros realizados, no convocatorias futuras. La única invitación abierta a proponer es permanente: acercarse a Av. Avellaneda & Pje. Paysandú en la previa de los partidos en que Ferro juegue de local, para intercambiar, comentar propuestas, escuchar las propuestas de Ferro y sumarse a colaborar.

## Cruce con el sitio y el corpus local

El baseline local fue cortado el 2026-06-25 y ya registraba reuniones abiertas, plenarias, CIARF, gestión profesional, secretaría técnica, reinversión y rechazo a las SAD. La web vigente agrega la plataforma del 2026-07-02 y la Reunión Abierta del 2026-07-16. La estructura actual tiene Novedades, Documentos y FAQ dentro de Plataforma, pero no un listado dedicado de eventos.

| Tema | Presencia actual | Novedad observada | Gap u oportunidad editorial |
| --- | --- | --- | --- |
| Gestión, planificación y participación | Fuerte: hero, About, plataforma, documento de gestión y FAQ. | Nueva generación, dirigentes presentes, trabajo en equipo, no personalismos, evaluar y rendir cuentas. | Actualizar el texto de principios de conducción sin publicar nombres o cargos no confirmados. |
| Infraestructura y patrimonio | Presente en la prioridad “Cuidar y poner en valor nuestro patrimonio”, CIARF y piezas “Sabemos”. | Programa de mantenimiento, prioridades, etapas, plazos, presupuestos y horizonte de diez años; club lindo, visible y seguro. | Se puede actualizar con el mismo nivel de precisión que las redes, sin agregar cifras, responsables ni compromisos técnicos no publicados. |
| Economía y sostenibilidad | Presente de forma general como “base económica sólida”. | Ingresos extraordinarios, vínculos y aliados estratégicos como herramientas de crecimiento. | Se puede incorporar la formulación pública con igual precisión, sin sumar mecanismos, cifras ni resultados ausentes. |
| Salud mental | No hay sección específica en la plataforma ni en Novedades revisadas. CIARF menciona área médica/kinesiología, pero no salud mental. | Tema repetido en convocatoria, encuentro y propuesta de política integral. | Incorporar como subprioridad de Comunidad, conservando el alcance público de prevención, escucha y acompañamiento; no publicar protocolo, nómina ni roles no informados. |
| Eventos y reuniones | Novedades contiene piezas fechadas; existe una página para la reunión del 16/07 con PDF y fotos. | Actividad recurrente en agosto y encuentros comunicados en redes. | Crear archivo/listado de resultados de encuentros realizados, sin sección de convocatorias futuras ni feed automático. |
| Identidad y comunidad | Muy presente: “Ferro somos todos”, club como un todo, socios protagonistas. | Familia, aniversario, historia, “en manos de los socios”; deseo de ascender. | Mantener identidad como tono; separar deseos de resultados y verificar toda afirmación legal. |
| Contacto y canales | Email, Instagram y X; no se observa otro canal oficial en src/data/site.ts. | CTA “Acompañanos” y “Sumate” en Instagram; invitación permanente en Av. Avellaneda & Pje. Paysandú antes de los partidos de local. | Hacer visible esa invitación y el camino institucional para participar, sin inventar un formulario o canal que no exista. |

**Documentos:** la web ya tiene documentos de gestión profesional, CIARF y reorganización institucional. Ninguna de las publicaciones nuevas trae un PDF, plan técnico o material descargable equivalente. Si se aprueban detalles sobre infraestructura, economía o salud mental, conviene publicar primero una ficha institucional fechada y versionada, enlazada desde la novedad, en lugar de presentar un caption como documento.

## Discrepancias y datos a confirmar

- El baseline local registra 175 seguidores y 34 posts declarados en X al corte del 25/06; la revisión actual mostró 205 seguidores y 84 posts en el perfil. Son métricas volátiles y no deben mezclarse como una serie sin fecha.
- La publicación de X del 18/08 contiene la frase “nueva en generación”; se preserva como cita, pero no debe pasar sin edición a la web.
- “Plan a diez años”, etapas, plazos y presupuestos aparecen en el hilo de infraestructura, pero no se publicó ningún documento que permita verificarlos como plan técnico aprobado; se autorizó reutilizar sólo ese nivel de detalle público.
- “Ingresos extraordinarios” y “aliados estratégicos” son formulaciones públicas sin detalles operativos; se autorizó incorporarlas sin ampliar su precisión. La formulación jurídica y la conducción por socios fueron aprobadas por el usuario para la actualización web.
- Comentarios de terceros sobre antecedentes de gestión, nombres o salarios no se convierten en hechos ni respuestas institucionales. Requieren validación y definición política antes de entrar en FAQ o contacto. Tampoco se publican por ahora nombres de personas, equipos, profesionales o referentes.

### Archivos locales consultados

- mfa/comunicacion/redes-sociales/analisis/anexos/ferro-en-accion.md
- mfa/comunicacion/redes-sociales/analisis/analisis.md
- mfa/comunicacion/redes-sociales/analisis/instagram.md
- mfa/comunicacion/redes-sociales/analisis/x.md y x-corpus.md
- ferro-en-accion-web/src/data/site.ts
- ferro-en-accion-web/src/content/plataforma/2026-07-02-plataforma-ferro-en-accion.md
- ferro-en-accion-web/src/content/novedades/*.md y documentos/*.md

## Hechos, interpretación y recomendaciones

### Hechos observados

Se publicaron siete piezas de X entre el 12 y el 27/08 sobre economía, infraestructura, salud mental, gestión y conducción. Instagram repitió y amplió esas líneas, sumando celebraciones, una previa y contenidos de participación. No se observaron presupuestos, cronogramas de implementación, responsables, protocolo de salud mental, lista completa de integrantes ni resultados cuantificados.

### Interpretación editorial

La comunicación se desplaza desde la presentación de ejes hacia una demostración de método: reunirse, escuchar, ordenar prioridades, profesionalizar, cuidar y planificar. Salud mental funciona como expansión del concepto de club integral y comunidad, no todavía como política operativa documentada. Economía e infraestructura agregan vocabulario de ejecución, pero aún requieren respaldo técnico para no sobreprometer.

### Recomendación de tratamiento

Transformar las publicaciones en piezas institucionales fieles: conservar el texto de los posts e hilos casi literalmente, ordenar su lectura con título y formato web, y usar enlaces a redes como fuente y canal de seguimiento. Evitar incrustar X/Instagram como feed o presentar comentarios de terceros como posiciones de Ferro.

## Recursos descargados y no descargados

Los archivos están en [recursos/revision-redes-2026-08-28/](./recursos/revision-redes-2026-08-28/) y tienen un índice de trazabilidad en su [README.md](./recursos/revision-redes-2026-08-28/README.md). Son recursos de trabajo, fuera de producción.

### Inventario consolidado

| Tipo de recurso | Cantidad | Ubicación | Estado verificable |
| --- | ---: | --- | --- |
| Imágenes JPEG de X | 17 | [`recursos/.../x/`](./recursos/revision-redes-2026-08-28/x/) | Descargadas: cuatro, dos, una portada, cuatro, una, cuatro y una, en ese orden para las siete publicaciones solicitadas. |
| Imágenes JPEG nuevas de Instagram | 19 | [`recursos/.../instagram/`](./recursos/revision-redes-2026-08-28/instagram/) | Descargadas para las trece publicaciones directas revisadas; el mapeo exacto está en el README de recursos. |
| Imágenes JPEG preexistentes | 7 | Raíz de [`recursos/.../`](./recursos/revision-redes-2026-08-28/) | Conservadas sin reemplazar; no se usan para completar atribuciones nuevas. |
| Fragmentos DASH de Instagram | 141 | [`recursos/.../instagram/`](./recursos/revision-redes-2026-08-28/instagram/) | Video/audio MP4 por rangos de bytes; se conservan como trazabilidad técnica. |
| MP4 completos de Instagram | 5 nuevos | [`instagram/ensamblados/`](./recursos/revision-redes-2026-08-28/instagram/ensamblados/) | Verificados con `ffprobe`: VP9/AAC, audio presente y duración coincidente con la reproducción visible. |

### MP4 completos verificados

| Publicación | Archivo | Duración / dimensiones |
| --- | --- | --- |
| [DcefpGPyQw4](https://www.instagram.com/ferroenaccion/reel/DcefpGPyQw4/) | [`instagram-2026-08-25-salud-mental-politica-completo.mp4`](./recursos/revision-redes-2026-08-28/instagram/ensamblados/instagram-2026-08-25-salud-mental-politica-completo.mp4) | 84,01 s; 1080×1920 |
| [DcZPieYipCf](https://www.instagram.com/ferroenaccion/reel/DcZPieYipCf/) | [`instagram-2026-08-23-previa-local-completo.mp4`](./recursos/revision-redes-2026-08-28/instagram/ensamblados/instagram-2026-08-23-previa-local-completo.mp4) | 13,89 s; 720×1280 |
| [DbZTE0zjseE](https://www.instagram.com/ferroenaccion/reel/DbZTE0zjseE/) | [`instagram-2026-07-29-aniversario-reel-completo.mp4`](./recursos/revision-redes-2026-08-28/instagram/ensamblados/instagram-2026-07-29-aniversario-reel-completo.mp4) | 62,90 s; 1080×1920 |
| [DbHR7c1D4hS](https://www.instagram.com/ferroenaccion/reel/DbHR7c1D4hS/) | [`instagram-2026-07-22-equipo-profesional-completo.mp4`](./recursos/revision-redes-2026-08-28/instagram/ensamblados/instagram-2026-07-22-equipo-profesional-completo.mp4) | 101,15 s; 720×1280 |
| [DbDvDN_lJdt](https://www.instagram.com/ferroenaccion/reel/DbDvDN_lJdt/) | [`instagram-2026-07-21-documento-historico-completo.mp4`](./recursos/revision-redes-2026-08-28/instagram/ensamblados/instagram-2026-07-21-documento-historico-completo.mp4) | 92,53 s; 720×1280 |

Los cinco MP4 sin el sufijo `-completo` son ensamblados parciales anteriores, conservados sin reemplazar y no aptos para implementación.

### JPEG preexistentes retenidos

| Archivo | Fuente | Dimensiones | SHA-256 abreviado |
| --- | --- | ---: | --- |
| [instagram-2026-08-27-planificacion-economia.jpg](./recursos/revision-redes-2026-08-28/instagram-2026-08-27-planificacion-economia.jpg) | [DcjuvdVEaFM](https://www.instagram.com/ferroenaccion/p/DcjuvdVEaFM/) | 960×720 | fed9d7ebb3c2…0174bd7 |
| [instagram-2026-08-26-infraestructura.jpg](./recursos/revision-redes-2026-08-28/instagram-2026-08-26-infraestructura.jpg) | [DchevLPkldJ](https://www.instagram.com/ferroenaccion/p/DchevLPkldJ/) | 1080×1349 | d05b116675fc…f3ef57 |
| [instagram-2026-08-21-salud-mental-encuentro.jpg](./recursos/revision-redes-2026-08-21-salud-mental-encuentro.jpg) | [DcUBtriEad3](https://www.instagram.com/ferroenaccion/p/DcUBtriEad3/) | 900×506 | 028aed2dc9fe…63a8b4 |
| [instagram-2026-08-20-gestion-profesional.jpg](./recursos/revision-redes-2026-08-20-gestion-profesional.jpg) | [DcRGck6FOen](https://www.instagram.com/ferroenaccion/p/DcRGck6FOen/) | 1080×1350 | 4c6d176b2960…67a798 |
| [instagram-2026-08-12-salud-mental-deporte.jpg](./recursos/revision-redes-2026-08-28/instagram-2026-08-12-salud-mental-deporte.jpg) | [Db9WCJzEssN](https://www.instagram.com/ferroenaccion/p/Db9WCJzEssN/) | 1122×1402 | 2c2a53725f83…950952 |
| [instagram-2026-07-29-aniversario-familia.jpg](./recursos/revision-redes-2026-08-28/instagram-2026-07-29-aniversario-familia.jpg) | [DbZG6x6khzt](https://www.instagram.com/ferroenaccion/p/DbZG6x6khzt/) | 1152×1440 | f3caa1bfb7e7…3b6b6 |
| [instagram-2026-07-21-ejes.jpg](./recursos/revision-redes-2026-08-28/instagram-2026-07-21-ejes.jpg) | [DbEeotTksjH](https://www.instagram.com/ferroenaccion/p/DbEeotTksjH/) | 1080×1349 | 4bf698900c80…559a49 |

**No descargados o pendientes:** el MP4 de X del 25/08, porque el reproductor sólo expuso una URL `blob:`; y recursos de piezas que sólo quedaron visibles en la grilla. La imagen de [Dbd3poniaFo](https://www.instagram.com/ferroenaccion/p/Dbd3poniaFo/) sí quedó descargada. El bundler de recursos de Instagram devolvió exactamente `TypeError: Failed to fetch`, pero la reproducción permitió recuperar los fragmentos y completar los cinco Reels indicados. No se sustituyó ningún recurso por otra fuente ni se sobreescribieron archivos existentes.

## Propuestas priorizadas para la web

| Prioridad / esfuerzo | Propuesta | Página o sección afectada | Fuente | ¿Multimedia? |
| --- | --- | --- | --- | --- |
| P0 / medio | Incorporar “Cuidado y salud mental” como subprioridad de Comunidad, con prevención, escucha y acompañamiento, sin convertir el texto en una política operativa con protocolo o nómina. | /plataforma/, Comunidad y una novedad asociada. | X 12/08, 21/08 y 25/08; IG Db9WCJzEssN, DcUBtriEad3, DcefpGPyQw4. | Sí: hay imágenes y un MP4 completo de trabajo en `recursos/`; requiere validación humana del lenguaje profesional y accesible. |
| P0 / medio | Incorporar un archivo de resultados de encuentros y reuniones realizados, sin listado de convocatorias futuras. | Nueva ruta sugerida /participacion/ o sección de Novedades. | Encuentro 21/08, reunión del 16/07 ya publicada y otras reuniones observadas. | No es indispensable; se puede sumar imagen por resultado con alt y fuente. |
| P1 / medio | Ampliar la prioridad de patrimonio con mantenimiento permanente, orden de prioridades y horizonte de corto/mediano/largo plazo, conservando el nivel de detalle público. | Plataforma, prioridad “Cuidar y poner en valor nuestro patrimonio”; eventualmente Novedades. | X/IG 26/08; imágenes descargadas en `recursos/.../instagram/`. | Sí, una imagen. No agregar cifras, responsables ni compromisos técnicos no publicados. |
| P1 / medio | Reforzar economía y conducción con planificación financiera, ingresos extraordinarios, evaluación, rendición y alianzas, usando exactamente la precisión de las redes. | Prioridad “Construir una base económica sólida”, Quiénes somos y FAQ. | X/IG 20/08 y 27/08; imágenes descargadas en `recursos/.../instagram/`. | Opcional: una imagen de trabajo. No publicar cifras, mecanismos ni resultados ausentes. |
| P1 / bajo | Ajustar el relato de “nueva etapa”: socios presentes, trabajo en equipo, profesionalismo sin personalismos y club como un todo. | Hero, Quiénes somos y cierre de Plataforma. | X 18/08 y 20/08; IG DcRGck6FOen, DbEeotTksjH, DbHR7c1D4hS. | No indispensable. |
| P2 / bajo | Añadir una novedad de comunidad e identidad por el 122.º aniversario, sólo como registro editorial fechado, sin convertir el deseo de ascenso en promesa. | Novedades. | IG DbZG6x6khzt y DbZTE0zjseE; imágenes y MP4 descargados. | Sí, autorización de reutilización confirmada por el usuario; resolver alt text y encuadre. |
| P2 / bajo | Ampliar FAQ con “¿Qué es CIARF?”, “¿Qué significa nueva etapa?”, “¿Cómo se participa?” y “¿Qué alcance tendría la política de salud mental?”. | FAQ de /plataforma/#faq. | Preguntas visibles en comentarios y captions del 21/07; CIARF existente en la web. | No. Las respuestas requieren aprobación humana; los comentarios sólo justifican las preguntas. |
| P2 / bajo | Hacer visible un CTA institucional de participación y contacto, con la invitación permanente en Av. Avellaneda & Pje. Paysandú antes de los partidos de local. | Home, Contacto y Comunidad/Participación. | CTAs “Acompañanos”/“Sumate” en IG; instrucción editorial del 28/08; email y redes actuales en src/data/site.ts. | No. Si se implementa, etiquetar links/descargas con data-track-* y preservar la analítica existente. |

## Propuesta de estructura editorial para eventos y reuniones

Si se aprueba una sección dedicada, cada tarjeta mobile-first debería mostrar, en este orden: estado (Realizado o Archivo; “Próximo” sólo cuando el usuario confirme fecha), fecha confirmada, título, resultado o síntesis en una frase, lugar sólo si está verificado, enlace opcional a la publicación fuente y relación con la propuesta. La ficha completa puede sumar materiales, fotos con alt, transcript/captions si hay video y fecha de actualización.

La sección no debería comportarse como un feed ni funcionar como agenda de convocatorias. Debe conservar los encuentros pasados como archivo y permitir llegar a la propuesta relacionada. Para la actividad del 12/08 y el encuentro del 21/08, el texto aprobado puede registrar que hubo convocatoria y encuentro de trabajo; sólo debe afirmar resultados concretos si están en la publicación o los confirma el equipo. La invitación permanente de Av. Avellaneda & Pje. Paysandú debe vivir como CTA estable de participación, separada del archivo de reuniones.

## SEO y LLM como impacto secundario

Sólo después de aprobar el contenido:

- actualizar title, description, canonical, Open Graph y fecha/categoría de cada nueva novedad o ruta;
- comprobar src/pages/sitemap.xml.ts si se crea una colección o ruta de participación nueva y revisar lastmod;
- actualizar el FAQ y su JSON-LD en src/pages/plataforma/index.astro sólo con respuestas aprobadas;
- actualizar src/pages/llms.txt.ts con la nueva sección, sus enlaces y una síntesis que no confunda publicaciones sociales con documentación institucional;
- usar datos Event sólo para eventos próximos con fecha, lugar y horario confirmados; para encuentros pasados conviene una página de artículo/archivo;
- validar enlaces sociales y metadatos sin convertir la web en un agregador de publicaciones.

## Checklist de implementación posterior

- [x] Tratar salud mental como subprioridad de Comunidad; confirmar sólo si “subtrinidad” tenía otro significado.
- [ ] Validar con referentes competentes alcance, lenguaje, protocolo y límites de cualquier propuesta de salud mental.
- [ ] Confirmar fechas, lugares y resultados concretos de cada reunión antes de redactar Novedades; no incorporar convocatorias futuras como contenido editorial.
- [x] Incorporar, con la precisión autorizada, la formulación “Asociación Civil Sin Fines de Lucro” y la conducción por socios.
- [x] Registrar autorización de reutilización de imágenes y videos propios; antes de producción resolver alt text, créditos, encuadre y subtítulos/transcripción si correspondiera.
- [x] Mantener fuera de publicación nombres, equipos, profesionales, referentes y nóminas hasta un anuncio posterior.
- [x] Usar la precisión de los textos oficiales para ingresos extraordinarios, alianzas estratégicas y horizonte de diez años, sin ampliar detalles.
- [x] Separar el CTA permanente de Av. Avellaneda & Pje. Paysandú del archivo de reuniones y resultados.
- [ ] Transponer los posts e hilos aprobados casi literalmente, ajustando sólo título, formato y datos expresamente autorizados; no incorporar comentarios de terceros.
- [ ] Incorporar alt text descriptivo, foco visible, jerarquía de encabezados y lectura cómoda desde celular.
- [ ] Etiquetar CTA, enlaces sociales y descargas con data-track-*; preservar src/components/Analytics.astro, functions/api/track.ts, wrangler.toml y el endpoint de interacciones.
- [ ] Actualizar metadatos, JSON-LD, sitemap y llms.txt según las rutas aprobadas.
- [ ] Ejecutar build y verificaciones de accesibilidad/enlaces en una rama de implementación, sin publicar hasta nueva aprobación.

## Fuentes públicas

- [Perfil de Ferro en Acción en X](https://x.com/ferroenaccion) y las siete publicaciones enlazadas en la tabla de X.
- [Perfil de Ferro en Acción en Instagram](https://www.instagram.com/ferroenaccion/) y las publicaciones directas enlazadas en la tabla de Instagram.
- Corpus local de comunicación: mfa/comunicacion/redes-sociales/.
- Sitio inspeccionado: ferro-en-accion-web/, especialmente src/data/site.ts, src/content/plataforma/ y src/content/novedades/ y documentos/.

## Decisiones incorporadas y validaciones pendientes

Decisiones ya recibidas y aplicadas a este informe:

- Salud mental se trata como subprioridad de Comunidad, con el alcance público de prevención, escucha y acompañamiento.
- Se pueden publicar ingresos extraordinarios, alianzas estratégicas y horizonte a diez años con la precisión de las redes, sin agregar detalles.
- Novedades debe contar resultados de reuniones y encuentros realizados; no se proponen convocatorias futuras. El CTA permanente autorizado es Av. Avellaneda & Pje. Paysandú antes de los partidos de local.
- No se publican nombres, equipos, profesionales, referentes ni nóminas por ahora.
- Se aprueba la formulación jurídica “Asociación Civil Sin Fines de Lucro” y la conducción por socios.
- Se autoriza reutilizar las imágenes y videos propios descargados, con revisión posterior de accesibilidad, créditos y encuadre.
- La comunicación institucional debe conservar casi literalmente los textos oficiales y sus hilos cuando se los lleve a Novedades; sólo se ajustan título, formato y datos expresamente autorizados. Los comentarios de terceros quedan fuera.

Validaciones humanas que siguen siendo necesarias antes de implementar:

- Confirmar el significado de “subtrinidad” si no era un error por “subprioridad”.
- Confirmar fechas, lugares y resultados concretos de cada reunión antes de publicar Novedades; el relevamiento no puede completar esos datos.
- Revisar con referentes competentes el lenguaje de salud mental para no presentar como protocolo, equipo o servicio algo que las redes no detallan.
- Definir alt text, créditos, encuadres, subtítulos/transcripciones y selección final de medios.
- Aprobar las respuestas de FAQ sobre CIARF, “nueva etapa” y antecedentes de gestión. Las preguntas visibles justifican el contenido, pero no autorizan respuestas inventadas.

## Estado de archivos y git

- Sitio ferro-en-accion-web/: se inspeccionó; no se modificaron archivos.
- Estado git del sitio al cierre: limpio; git -C ferro-en-accion-web status --short no devolvió archivos.
- Proyecto padre: el informe y la carpeta de recursos son nuevos artefactos de trabajo; se preservaron cambios previos no relacionados del usuario.
- Estado git del proyecto padre al cierre: sucio por cambios previos del usuario y por los nuevos artefactos de este relevamiento en mfa/trabajo/web-borradores/.
- No se creó commit, no se hizo push y no se ejecutó deploy. El estado final se verificó al cerrar el relevamiento y se informa también en la entrega.
