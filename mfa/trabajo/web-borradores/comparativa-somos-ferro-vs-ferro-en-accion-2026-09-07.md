# Comparativa actualizada: Somos Ferro vs. Ferro en Acción

**Fecha de corte:** 7 de septiembre de 2026

**Sitios comparados:** [somosferro.com.ar](https://somosferro.com.ar/) y [ferroenaccion.ar](https://ferroenaccion.ar/)
**Alcance:** contenido, momento electoral, UX/UI, accesibilidad, SEO técnico, performance, analítica, mantenimiento y paridad entre producción y checkout local.

## Respuesta ejecutiva

Ferro en Acción mejoró de manera material desde la comparación del 5 de septiembre:

- La home productiva ahora tiene un bloque electoral visible con fecha, countdown, acceso al padrón y guía de elecciones.
- Se publicó la novedad del 3 de septiembre sobre la decisión de la Comisión Directiva: las próximas elecciones serán el domingo 27 de septiembre de 2026.
- Se agregó una guía electoral profunda en `/elecciones-ferro-2026/`, con horario, requisitos, padrón, proceso de votación, listas, preguntas frecuentes y fuentes.
- La mejora de performance ya es visible en producción: Lighthouse móvil dio **94 Performance**, **100 Accessibility**, **100 Best Practices** y **100 SEO** para la home.
- La home actual tuvo **FCP 1,2 s, LCP 2,7 s, TBT 150 ms y CLS 0**, frente a la referencia anterior de PSI de **68, FCP 4,6 s y LCP 5,5 s**. No es una comparación de laboratorio idéntica, por lo que debe leerse como señal fuerte de mejora y no como serie estadística homogénea.

La principal brecha que queda no es de calidad pública sino de control de fuentes: el `main` local del subrepositorio `ferro-en-accion-web` está en `3f4ffca` y contiene Participación y las novedades de agosto, pero todavía no contiene la ruta electoral, la novedad del 3/9 ni el countdown que sí están productivos. La producción y el checkout local vuelven a representar revisiones distintas.

## Qué cambió desde la comparación anterior

| Área | Antes | Ahora | Evaluación |
|---|---|---|---|
| Momento electoral | La fecha no tenía un hub propio en Ferro en Acción | Fecha visible en home, guía electoral, padrón, countdown y novedad del 3/9 | Mejora crítica |
| Paridad con producción | Faltaban localmente Participación y las novedades del 21 y 27/8 | Esos contenidos ya están en `main` local y en producción | Diferencia anterior resuelta |
| Paridad electoral | No había contenido electoral local ni registrado en el checkout inspeccionado | Producción tiene `/elecciones-ferro-2026/` y `/novedades/2026-09-03-elecciones-27-septiembre/`; `main` local todavía no | Nueva diferencia a resolver |
| Performance home | PSI anterior: 68; LCP 5,5 s | Lighthouse actual: 94; LCP 2,7 s | Mejora muy fuerte |
| Performance electoral | No existía ruta propia | La guía da 83; LCP 4,3 s | Buena base, todavía optimizable |
| SEO electoral | Sin página específica ni Event/FAQ/BreadcrumbList | Guía con canonical, Event, FAQPage y BreadcrumbList | Mejora de descubrimiento y utilidad |
| Countdown | Recomendado, no implementado en el corte anterior | Funciona, muestra tiempo restante y usa `America/Argentina/Buenos_Aires` | Implementación verificada |
| Accesibilidad | Home ya estaba en 100 | Home y guía electoral en 100 | Se mantuvo el nivel |

## Evidencia actual de Ferro en Acción

En la home productiva se observan:

- Navegación con `Elecciones 2026`, Plataforma, Quiénes somos, Prioridades, Novedades, Documentos, Participación, Propuestas y Contacto.
- Texto visible: “Las próximas elecciones de Ferro serán el domingo 27 de septiembre de 2026”.
- Link externo al padrón: `https://padron.ferroenaccion.ar/`.
- Link interno a la guía electoral.
- Countdown operativo: al momento de la comprobación mostraba días, horas, minutos y segundos restantes; no quedó congelado en cero.
- La novedad del 3 de septiembre aparece primera en la home y en `/novedades/`.
- El countdown tiene fallback textual, fecha objetivo y cierre explícitos: `2026-09-27T10:00:00-03:00` y `2026-09-27T19:00:00-03:00`.

Rutas productivas comprobadas con HTTP 200:

- `/`
- `/novedades/`
- `/participacion/`
- `/elecciones-ferro-2026/`
- `/novedades/2026-09-03-elecciones-27-septiembre/`
- `/sitemap.xml`
- `/robots.txt`
- `/llms.txt`
- `/.well-known/security.txt`

El sitemap productivo ya incluye la guía electoral, la novedad del 3/9, Participación y las novedades de agosto. `robots.txt` publica el sitemap y permite crawling general; también contempla explícitamente `OAI-SearchBot`.

## Contenido y arquitectura de información

### Ventajas actuales de Ferro en Acción

Ferro en Acción pasó de ser principalmente un sitio institucional/programático a tener una capa electoral completa sin abandonar el archivo permanente:

- Home institucional con propuesta, identidad, prioridades, actualidad y contacto.
- Plataforma HTML y páginas de propuestas enlazables.
- Archivo de novedades por fecha y slug.
- Documentos separados de las novedades.
- Participación como archivo de reuniones y encuentros.
- Guía electoral separada, compartible y actualizable.
- Padrón externo visible como acción primaria.
- FAQ electoral con datos estructurados.

Esto es más flexible para buscadores, compartir una información puntual y actualizar una fecha o requisito sin reescribir una única landing.

### Qué sigue haciendo mejor Somos Ferro

Somos Ferro mantiene ventajas de campaña:

- La promesa electoral aparece inmediatamente en el hero.
- Tiene una identidad más fotográfica y movilizadora.
- Expone cuatro agrupaciones aliadas, una lista amplia de integrantes y roles.
- Tiene una sección “Cómo votar” compacta y un formulario directo para sumarse.
- El mensaje “más de 100 socios y socias” y la grilla de personas producen una señal fuerte de volumen y capacidad.

### Qué todavía le falta a Ferro en Acción frente a Somos Ferro

- Una presentación pública del equipo/candidatura o, si no se quiere publicar una nómina, una explicación clara de quiénes integran los equipos y cómo se organiza la participación.
- Un CTA de campaña más directo para equipos de trabajo, fiscales, difusión y voluntariado.
- Un formulario de participación propio, si se decide asumir la carga de privacidad, seguridad y operación.
- Más prueba social visual: fotos de grupos, personas, equipos o encuentros, con nombres y roles sólo cuando estén confirmados.
- Una experiencia electoral más urgente en el primer viewport: la guía está muy completa, pero la home sigue iniciando desde un tono institucional más calmo.

### Qué no conviene copiar sin adaptación

El formulario de Somos Ferro pide nombre, email, WhatsApp y mensaje. Antes de replicarlo habría que definir finalidad, consentimiento, retención, responsable operativo, protección anti-spam y canal de baja. La conversión no debe comprarse a costa de una deuda de privacidad.

## Diseño visual y UX

### Ferro en Acción: mejoras comprobadas

- La fecha electoral ahora tiene jerarquía visual propia y no depende de que el visitante llegue a Novedades.
- La guía tiene breadcrumbs, tarjetas de resumen, pasos de votación, FAQ y fuentes.
- La navegación responsive se compacta antes de envolver enlaces en dos líneas.
- Las galerías dejaron de rotar automáticamente y usan controles explícitos; esto mejora control, accesibilidad y previsibilidad.
- El sitio conserva un sistema visual coherente: paleta crema/verde, Montserrat, tarjetas, bordes y componentes compartidos.
- El primer frame de las galerías tiene alt, dimensiones y fallback suficientes.

### Somos Ferro: ventajas de impacto

- Hero con fotografía de hinchada, logo blanco, CTA y countdown: comunica campaña en segundos.
- Fotografía y grilla de personas generan pertenencia y escala.
- La alternancia de bloques, imágenes, diagnóstico y propuestas tiene más carácter electoral.
- La barra de secciones es simple y orientada al recorrido de campaña.

### Riesgos o pendientes de Ferro en Acción

- La home mejoró su urgencia, pero todavía tiene menos presencia humana que Somos Ferro.
- La guía electoral es extensa; necesita mantener navegación interna, breadcrumbs y un resumen superior muy claro.
- El countdown debe desaparecer al terminar la jornada sin eliminar la fecha ni la información histórica de la elección.
- Hay que definir qué quedará después del 27/9: archivar el countdown, cambiar su estado a “elección realizada” o reemplazar el bloque por resultados/participación histórica.

## Performance y Core Web Vitals

Las mediciones se hicieron con Lighthouse 12.8.2, corrida de laboratorio móvil, sobre las dos home actuales y la guía electoral de Ferro. Los valores pueden variar entre corridas y no sustituyen CrUX/field data.

| Métrica | Ferro home | Ferro guía electoral | Somos Ferro home |
|---|---:|---:|---:|
| Performance | **94** | **83** | **66** |
| Accessibility | **100** | **100** | **96** |
| Best Practices | **100** | **100** | **79** |
| SEO | **100** | **100** | **100** |
| FCP | 1,2 s | 1,1 s | 3,2 s |
| LCP | 2,7 s | 4,3 s | 7,5 s |
| TBT | 150 ms | 90 ms | 110 ms |
| CLS | 0 | 0 | 0 |
| Solicitudes | 17 | — | 90 |
| Transferencia | 804 KB | — | 2,9 MB |
| Imágenes | 4 / 416 KB | — | 73 / 2,75 MB |

### Qué explica la mejora propia

La rama `codex/performance-seo-wcag` documenta y contiene cambios que explican el salto observado:

- variantes WebP/AVIF y `srcset`/`sizes`;
- dimensiones intrínsecas y carga diferida;
- menos dependencias de iconos y JavaScript;
- fuentes locales limitadas al subconjunto latino y pesos críticos precargados;
- CSS inline por ruta;
- galerías sin temporizador permanente;
- controles nativos para interacción y lightbox.

Producción ya exhibe parte de ese resultado: HTML más liviano, imágenes optimizadas, fuentes WOFF2 precargadas y cero hoja CSS externa bloqueante en la corrida.

### Oportunidad pendiente de LCP

La home ya queda cerca del umbral “bueno” de LCP, aunque 2,7 s todavía puede bajar de 2,5 s. La guía electoral tiene LCP de 4,3 s y debe ser el siguiente foco:

1. identificar exactamente el elemento LCP de la guía;
2. evitar que una imagen/estilo del hero electoral sea descubierto tarde;
3. revisar recursos de GTM/GA4, que en la home representan aproximadamente 300 KB y 49 ms de blocking time en esta corrida;
4. revalidar con Lighthouse y luego con datos de campo después del despliegue.

Somos Ferro queda claramente peor en peso, cantidad de imágenes, DOM y LCP. Su diseño fotográfico tiene valor político, pero hoy paga un costo técnico alto.

## Accesibilidad WCAG 2.2

### Ferro en Acción

La home y la guía electoral dieron 100 en Accessibility. Se observaron:

- skip link y landmarks;
- navegación principal etiquetada;
- headings coherentes;
- foco visible;
- botones nativos en galerías y acordeones;
- alt y dimensiones en imágenes;
- fallback textual para countdown;
- `prefers-reduced-motion`;
- nombres accesibles para padrón, guía y controles.

El countdown anuncia el estado mediante un texto accesible y usa `aria-live` sólo para mensajes de estado, evitando convertir cada segundo en ruido de lector de pantalla.

### Somos Ferro

La auditoría dio 96. El árbol accesible es bastante mejor que en el corte anterior en varios componentes: diagnóstico usa botones nativos y las fichas de integrantes aparecen como botones con nombres. Aun así, Lighthouse señala:

- roles ARIA incompatibles en algún elemento;
- problemas de contraste;
- 1.284 elementos en el DOM;
- 73 imágenes y aproximadamente 2,75 MB de imágenes transferidas.

En UX asistiva, la cantidad de integrantes es una fortaleza de prueba social pero también una superficie enorme de foco, lectura y mantenimiento.

## SEO, robots y datos estructurados

### Ventaja actual de Ferro en Acción

Ferro en Acción tiene ahora una arquitectura SEO más completa para el tema electoral:

- canonical y metadata por página;
- sitemap con `lastmod` editoriales;
- robots.txt con sitemap;
- llms.txt;
- security.txt;
- `Organization`, `WebSite`, `WebPage`;
- `NewsArticle` para novedades;
- `AboutPage`, `Event`, `FAQPage` y `BreadcrumbList` en la guía electoral;
- URLs individuales para la guía y la novedad del 3/9.

La guía electoral es más descubrible y reutilizable que un bloque anclado dentro de una landing única.

### Somos Ferro

La página tiene title, description, canonical, Open Graph, Twitter Card y contenido HTML visible. Lighthouse SEO dio 100, pero la revisión HTTP actual sigue encontrando:

- `/robots.txt`: 404;
- `/sitemap.xml`: 404;
- `/.well-known/security.txt`: 404;
- `/favicon.ico`: 404;
- duplicación de algunos metadatos en el DOM observado;
- no se observó JSON-LD en la página.

Esto no impide por sí solo que Google indexe la página, pero deja peor resuelta la gobernanza de crawling, descubrimiento, identidad institucional y fragmentos enriquecidos.

## Analítica, privacidad y seguridad

### Ferro en Acción

La arquitectura pública combina Google Tag Manager/GA4 con Vercel Analytics y Speed Insights, además del tracking semántico mediante `data-track-*`. La instrumentación cubre navegación, CTA, galerías, acordeones, mailto, descargas y enlaces externos.

En la corrida actual Lighthouse detectó que Google Tag Manager y GA4 representan la mayor parte del JavaScript de terceros de la home. Conviene mantener una revisión periódica para evitar pageviews duplicados o eventos con datos personales.

El enlace al padrón es un salto externo y debe seguir siendo claramente identificable como tal. La guía no debe afirmar datos del padrón que no estén confirmados por la fuente correspondiente.

### Somos Ferro

Somos Ferro tiene una ventaja clara de conversión por formulario, pero suma superficie de privacidad y operación. Lighthouse detectó cookies de terceros; además se observan Clarity, React desde CDN y un endpoint de formulario. Recomendaciones pendientes: política de privacidad visible, consentimiento explícito, minimización de datos, rate limit, CSRF, masking y documentación de Clarity.

## Paridad local/producción

### Estado actual

El checkout local `ferro-en-accion-web` está limpio en `main` y apunta a `3f4ffca`, con Participación y las novedades del 21/8 y 27/8. Su build genera esas rutas, pero no genera:

- `src/pages/elecciones-ferro-2026/`;
- la novedad `2026-09-03-elecciones-27-septiembre`;
- el componente de countdown;
- el enlace de navegación “Elecciones 2026”;
- la entrada electoral del sitemap.

El build local ejecutado el 7/9 fue correcto, pero no es evidencia de paridad con producción: genera sólo las rutas presentes en su checkout.

Producción, en cambio, publica el bloque electoral completo y está detrás de Vercel. El listado actual de Vercel muestra deployments productivos recientes, pero la respuesta pública no permite identificar por sí sola el commit exacto que originó el deployment que atiende el dominio. Esto debe resolverse dentro del hilo de actualización web, comparando el deployment, el branch y el checkout efectivo.

### Decisión recomendada

No conviene copiar a ciegas producción sobre `main`. Hay que:

1. identificar el commit/build que contiene la guía electoral publicada;
2. verificar qué cambios de la rama de performance ya llegaron a producción;
3. traer a la rama correcta sólo los commits/archivos validados;
4. ejecutar build, tests, verificación de rutas y Lighthouse;
5. dejar un único source of truth para el siguiente deploy.

## Scorecard actualizado

| Eje | Mejor hoy | Por qué |
|---|---|---|
| Urgencia electoral | Empate con matices | Somos Ferro tiene hero más movilizador; Ferro en Acción tiene guía y padrón más completos y enlazables. |
| Profundidad institucional | Ferro en Acción | Plataforma, propuestas, novedades, documentos y participación separadas. |
| Fecha y guía para votar | Ferro en Acción | Página dedicada, FAQ, Event, requisitos, proceso y fuentes. |
| Equipo visible | Somos Ferro | Más de 100 personas declaradas, roles y fichas. |
| Conversión de voluntariado | Somos Ferro | Formulario directo con tipos de colaboración. |
| Performance home | Ferro en Acción | 94 vs. 66; LCP 2,7 s vs. 7,5 s. |
| Peso y requests | Ferro en Acción | 804 KB/17 requests vs. 2,9 MB/90 requests en laboratorio. |
| Accesibilidad | Ferro en Acción | 100 vs. 96; menos DOM y controles más nativos. |
| SEO técnico | Ferro en Acción | Sitemap, robots, JSON-LD, security.txt y rutas individuales. |
| Impacto visual | Somos Ferro | Fotografía, hinchada, logos aliados y personas. |
| Archivo y mantenimiento editorial | Ferro en Acción | Colecciones, slugs, metadata, sitemap y páginas de detalle. |
| Source of truth | Pendiente | Producción ya incluye elecciones; `main` local no. |

## Prioridades recomendadas

### P0 — sincronización de fuente

Resolver inmediatamente la divergencia entre producción y `main` local. La elección está a pocos días: una modificación editorial posterior debe poder salir del mismo checkout que se audita y prueba.

### P1 — LCP de la guía electoral

Bajar el LCP de `/elecciones-ferro-2026/` de 4,3 s, especialmente si se comparte desde redes y recibe tráfico móvil concentrado.

### P1 — post-elección

Definir antes del 27/9 qué ocurre con countdown, guía, padrón, requisitos y CTA de fiscales. La fecha debe conservarse como archivo, pero la interfaz temporal no debe quedar mostrando una elección futura vencida.

### P2 — prueba social propia

Agregar fotos, equipos o testimonios sólo con fuentes y autorizaciones claras. No es necesario replicar la lista de Somos Ferro para ganar humanidad; alcanza con hacer visible el trabajo real ya documentado.

### P2 — participación

Decidir si se implementará un formulario propio. Si la respuesta es sí, hacerlo con política de privacidad, consentimiento, minimización de datos, anti-spam y tracking documentado.

## Fuentes y reproducibilidad

- [Ferro en Acción — home productiva](https://ferroenaccion.ar/)
- [Ferro en Acción — guía electoral 2026](https://ferroenaccion.ar/elecciones-ferro-2026/)
- [Ferro en Acción — novedades](https://ferroenaccion.ar/novedades/)
- [Ferro en Acción — novedad del 3 de septiembre](https://ferroenaccion.ar/novedades/2026-09-03-elecciones-27-septiembre/)
- [Ferro en Acción — sitemap](https://ferroenaccion.ar/sitemap.xml)
- [Ferro en Acción — robots.txt](https://ferroenaccion.ar/robots.txt)
- [Ferro en Acción — security.txt](https://ferroenaccion.ar/.well-known/security.txt)
- [Somos Ferro — home productiva](https://somosferro.com.ar/)
- Lighthouse 12.8.2, corrida local de laboratorio móvil, archivos temporales `/private/tmp/ferro-current-lighthouse.json`, `/private/tmp/ferro-current-election-lighthouse.json` y `/private/tmp/somos-current-lighthouse.json`.
- Checkout local: `ferro-en-accion-web`, `main` en `3f4ffca` al momento de la revisión.

## Limitaciones

- Lighthouse es una medición de laboratorio; no reemplaza datos de campo ni una serie histórica homogénea.
- La medición de Somos Ferro incluye muchas fichas e imágenes visibles en la home, por lo que el peso no es una comparación de idéntico contenido.
- No se pudo atribuir públicamente el dominio productivo a un commit exacto de Vercel sólo con la respuesta HTTP y el listado de deployments.
- La revisión editorial confirma la fecha comunicada en producción; horarios, requisitos y padrón deben seguir respaldados por las fuentes institucionales correspondientes.
