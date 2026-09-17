# Informe de auditoría del nuevo sitio oficial de Ferro

**Sitio analizado:** [ferrocarriloeste.org.ar](https://www.ferrocarriloeste.org.ar/)

**Fecha de corte:** 12 de septiembre de 2026

**Comparación histórica:** [captura de Wayback del 30/11/2024](https://web.archive.org/web/20241201000000/https://www.ferrocarriloeste.org.ar/)

## Resumen ejecutivo

El rediseño es un cambio importante y, en términos visuales, mejora mucho la percepción del sitio. La portada abandona el aspecto de portal institucional tradicional y pasa a una experiencia editorial, mobile-first y con una identidad verdolaga más consistente: verde profundo, verde eléctrico, tipografía display, tarjetas de noticias, módulos visuales, navegación compacta y llamados a la acción más visibles.

La mejora principal es de **jerarquía y presentación**. La portada actual permite entender rápidamente que el sitio reúne actualidad, fútbol, básquet, actividades, vida institucional, socios y contenidos audiovisuales. También integra mejor el ecosistema digital del club: portal de socios, resultados, YouTube, Instagram, sponsors y accesos institucionales.

El problema es que la renovación parece haber llegado antes que la limpieza integral del contenido y la navegación. El nuevo envoltorio convive con restos de la arquitectura anterior, enlaces que no llevan a ningún destino, URLs heredadas, datos potencialmente desactualizados, imágenes sin `alt` y una taxonomía poco consistente. En síntesis: **buen salto de diseño, pero todavía no es un salto equivalente de producto digital**.

### Veredicto general

| Área | Evaluación | Comentario |
|---|---:|---|
| Identidad visual | Alta | Mucho más reconocible, contemporánea y coherente con Ferro. |
| Portada y jerarquía | Alta | Mejor priorización de actualidad y accesos principales. |
| Mobile | Media-alta | La composición está claramente pensada para celular, aunque hay problemas de densidad y legibilidad. |
| Navegación | Media-baja | El menú es amplio pero conserva muchos placeholders y agrupaciones difíciles de interpretar. |
| Contenido | Media | Hay más variedad y módulos útiles, pero también etiquetas técnicas y posibles desactualizaciones. |
| SEO técnico | Media | Hay buenas bases, pero faltan controles de calidad y datos estructurados visibles. |
| Accesibilidad | Baja-media | Hay buenos nombres en algunos controles, pero varios riesgos claros en imágenes, enlaces y contraste. |
| Madurez de implementación | Media | Stack moderno sobre WordPress, con señales de migración todavía incompleta. |

## 1. Qué cambió respecto de la versión anterior

La versión de fines de 2024 tenía una estructura reconocible de WordPress: encabezado con logo, menú horizontal muy extenso, menús desplegables por área, un bloque de “Novedades”, una grilla de “Noticias”, bloques de fútbol/básquet/deportes/institucional, sponsors y footer. La propia captura archivada carga de forma incompleta, por lo que la comparación visual histórica debe tomarse con cautela; sin embargo, su árbol de contenido confirma la arquitectura anterior.

La versión actual presenta estos cambios visibles:

1. **Header compacto y mobile-first.** En escritorio combina logo, menú corto (“El Club”, “Fútbol”, “Básquet”, “Educación”, “Socios”), búsqueda, redes y botón “Asociate”. En celular se reduce a logo, menú, búsqueda y CTA.
2. **Nuevo lenguaje visual.** Fondo verde muy oscuro, acentos verde neón, tipografía `Bebas Neue` para títulos y `Inter` para texto, bordes redondeados y tarjetas grandes.
3. **Nueva portada editorial.** La sección “Actualidad Verdolaga” funciona como un gran carrusel/hero de noticias destacadas, con una pieza dominante y módulos laterales como Portal de Socios y Resultados Multideportes.
4. **Más módulos de comunidad.** Aparecen “Universo”, “Ferro Play”, “Nuestras figuras del mes”, Instagram y sponsors como bloques de primera clase, no sólo como enlaces secundarios.
5. **Mayor exposición de la conversión principal.** “Asociate” aparece arriba y también en módulos de socios, lo que sugiere una intención más clara de convertir visitas en socios/as.
6. **Reorganización del contenido deportivo.** La portada muestra actualidad general, últimas noticias y categorías como fútbol, básquet, handball, ajedrez, vóley y hockey sin obligar al visitante a entrar primero a un menú profundo.
7. **Reutilización del archivo existente.** Se conservan muchas URLs y contenidos históricos, pero se presentan dentro de un sistema visual nuevo. Esto reduce el costo de migración y preserva parte del posicionamiento acumulado.

## 2. Lo que está bien resuelto

### Identidad y percepción

- La identidad verdolaga se entiende inmediatamente.
- La combinación de verde oscuro y verde brillante da una firma visual fuerte.
- El uso de `Bebas Neue` en títulos transmite deporte, cartelera y cultura de club.
- El sistema tiene más personalidad que el WordPress institucional anterior.
- El rediseño parece alineado con la comunicación reciente del club: obras, crecimiento institucional, deportes y sentido de pertenencia.

### Portada

- “Actualidad Verdolaga” es un buen nombre para el centro de la experiencia.
- La noticia destacada, los accesos al portal de socios y los resultados aparecen arriba, donde tienen más valor.
- La portada no queda limitada al fútbol masculino: incluye básquet, deportes, educación, obras, socios y vida institucional.
- “Nuestras figuras del mes” es un módulo diferencial: reconoce atletas de distintas disciplinas y puede fortalecer la idea de club integral.
- “Ferro Play” e Instagram agregan movimiento y conectan la web con los canales donde la comunidad ya consume contenido.
- El footer tiene una estructura razonable: datos de contacto, El Club, Servicios e Institucional.

### Conversión y servicios

- El CTA “Asociate” es visible desde el primer pantallazo.
- El portal de socios está integrado varias veces, no escondido dentro de un menú.
- Hay accesos a aranceles, actividades, entradas y carga de currículum.
- La presencia de direcciones de sede, estadio y teléfono mejora la utilidad práctica.

### Contenido y transparencia

- El sitio conserva accesos a estatuto, comisión directiva, actas, protocolos, contrataciones y manual de marca.
- La inclusión de actas recientes en “Últimas noticias” vuelve visible una parte importante de la vida institucional.
- Las notas internas tienen fecha, categoría, título, imagen, compartir y noticias relacionadas.
- La página de nota incorpora “Más leídas”, “Relacionadas” y “Ver todas las noticias”, lo que ayuda a la navegación editorial.

## 3. Fallas y riesgos detectados

### Prioridad crítica o alta

#### A. Hay enlaces que no llevan a ningún lugar

En el DOM actual aparecen aproximadamente 20 enlaces con `href="#"`. Entre ellos están:

- Actividades
- Comisión Directiva
- Actas
- Instalaciones
- Protocolos
- Recursos Humanos
- Sitios Históricos
- Contrataciones
- Fútbol Femenino
- Cultura
- Filiales
- Tenis
- Beneficios
- Instituto Educativo
- Colonia
- tres piezas de Ferro Play

Algunos pueden ser encabezados visuales pensados para abrir submenús, pero otros aparecen como contenidos clickeables. El caso más problemático es Ferro Play: las tres tarjetas de video apuntan a `#`, mientras el botón “Ver Canal” sí apunta a YouTube. Para el usuario, una tarjeta con apariencia de contenido clickeable debería abrir el video o la nota correspondiente.

**Recomendación:** distinguir técnicamente entre encabezado de submenú y enlace real; usar botones para desplegables y URLs reales para contenidos. Eliminar `#` de las tarjetas que no tengan destino.

#### B. Hay enlaces inseguros o heredados en HTTP

Desde una página HTTPS todavía se observan enlaces `http://` a:

- Portal de Socios
- Instituto Educativo
- Zona Ferro
- varios sponsors
- el sitio de No Limits Design

Algunos dominios pueden redirigir correctamente, pero la mezcla HTTP/HTTPS es mala práctica, puede generar advertencias, pérdida de confianza y problemas de seguridad o analítica.

**Recomendación:** verificar cada dominio, actualizar a HTTPS cuando exista y, si no existe, evaluar si el enlace sigue siendo válido o debe retirarse.

#### C. Hay una URL evidentemente mal formada

El módulo de resultados expone `https://www.www.ferrocarriloeste.org.ar/resultados/`. El doble `www` es una señal clara de error de construcción de URL y probablemente rompe el acceso.

**Recomendación:** corregir a `https://www.ferrocarriloeste.org.ar/resultados/` y agregar una prueba automática para enlaces internos de la portada.

#### D. El dato de socios/as no es consistente entre piezas

El artículo de campaña indica que quienes quieran asociarse pueden hacerlo a través de `portal.fconline.com.ar`, mientras el header y el footer apuntan a `fconline.smartclubfan.com/ausiged/...`. Son destinos distintos. Puede tratarse de una URL nueva todavía no aplicada en todos los lugares, pero para una campaña de conversión es un problema importante.

**Recomendación:** definir un único destino canónico para asociarse, usarlo en header, footer, banners y notas, y redirigir las URLs antiguas.

### Prioridad media

#### E. La navegación nueva sigue siendo demasiado grande y heterogénea

El menú lateral conserva casi toda la amplitud del menú histórico: club, fútbol, deportes, subcomisiones, educación, prensa, marketing, protocolos, contrataciones y numerosos subniveles. El cambio visual lo hace menos intimidante, pero no resuelve del todo la arquitectura de información.

Hay además grupos con rótulos que funcionan como enlaces y otros que sólo funcionan como contenedores. “Club”, “Fútbol”, “Básquet”, “Subcomisiones” y “Deportes” no siguen exactamente el mismo patrón.

**Recomendación:** separar claramente:

- navegación principal;
- servicios de acción rápida;
- áreas deportivas;
- información institucional;
- recursos históricos/documentales.

También convendría agregar un buscador de actividades/deportes y una página índice de todas las disciplinas.

#### F. Aparecen etiquetas técnicas de administración en la interfaz

En el contenido accesible se leen etiquetas como `banners-home`, `Actas CD`, `Colegio Primario` y otras categorías que en algunos lugares pueden ser útiles, pero `banners-home` parece un nombre interno de clasificación. Si también se visualiza en pantalla, es un defecto de contenido; si sólo está en el árbol accesible o metadata, sigue siendo una señal de taxonomía poco limpia.

**Recomendación:** revisar nombres de categorías, slugs y etiquetas visibles. Nunca mostrar nombres internos de implementación a usuarios.

#### G. El carrusel concentra demasiada información y puede ser difícil de leer

La pieza principal usa una imagen con texto incorporado, overlay verde, etiqueta, título HTML y puntos de navegación. En mobile el título de la placa y el título HTML se superponen visualmente o compiten por atención.

El carrusel tiene muchos slides y cambia la prioridad automáticamente. Esto puede hacer que una convocatoria institucional importante desaparezca antes de que el visitante la procese.

**Recomendación:** limitar la cantidad de slides, detener el autoplay cuando el usuario interactúa y garantizar controles accesibles. Para convocatorias, usar también un bloque fijo de “Información importante”.

#### H. Muchos `alt` de módulos visuales están vacíos

En la portada se detectan imágenes sin texto alternativo en Portal de Socios, Resultados, Universo y varios sponsors. En cambio, las noticias principales sí tienen `alt` derivados del título.

**Recomendación:** agregar textos alternativos descriptivos a banners, sponsors y módulos funcionales. Si una imagen es puramente decorativa, marcarla explícitamente como tal y asegurar que el enlace tenga nombre accesible.

#### I. Hay enlaces sin nombre accesible

El árbol accesible muestra varios enlaces que sólo contienen una imagen sin `alt`, por ejemplo algunos bloques de Universo y banners. Esto dificulta la navegación con lector de pantalla y también complica pruebas automáticas.

**Recomendación:** cada enlace debe tener texto visible o un nombre accesible; cada banner funcional debe tener `alt` y un destino claro.

#### J. El buscador existe, pero su experiencia no quedó suficientemente comprobada

El header tiene botón “Buscar” y el formulario incluye el placeholder “Buscar en el club...”. La interacción abre el estado de búsqueda, pero no se verificó en este corte el envío completo de una consulta ni la calidad de los resultados.

**Recomendación:** probar consultas con títulos, apellidos, disciplinas y términos institucionales; agregar estado vacío, corrección de errores, paginación y filtros por sección.

### Prioridad baja o de mejora continua

#### K. URLs y taxonomías mezcladas

La versión histórica utilizaba rutas del tipo `/category/...`; la actual exhibe también `/categoria/...`, además de rutas especiales como `/basquet-basquet/`, `/noticias-basquet/` y rutas heredadas de artículos. Esto puede funcionar mediante reescrituras, pero hace menos previsible el sitio y aumenta la probabilidad de contenido duplicado o redirecciones.

**Recomendación:** definir una convención única, documentar redirecciones 301 y verificar canonical, sitemap y enlaces internos.

#### L. El artículo de campaña tiene tono institucional fuerte pero CTA débil

La nota explica bien el contexto y trabaja el sentido de pertenencia, pero el CTA final no se presenta como un botón destacado ni ofrece pasos concretos, requisitos, costos, beneficios o respuestas frecuentes. Para una campaña de socios, la nota funciona más como manifiesto que como landing de conversión.

**Recomendación:** sumar botón “Asociate ahora”, beneficios, modalidades, preguntas frecuentes, contacto y destino canónico.

#### M. Falta una capa visible de información útil para el día a día

En la portada aparecen resultados y entradas, pero no se ve un calendario general, horarios de actividades actualizado, próximos eventos, mapas diferenciados ni acceso inmediato a teléfonos/email de áreas. Para socios y familias, esos datos probablemente sean más útiles que una segunda grilla de noticias.

**Recomendación:** agregar “Próximos eventos”, “Horarios de actividades”, “Cómo llegar” con instrucciones claras y contactos por área.

## 4. SEO

### Fortalezas observadas

- `lang="es"` en el HTML.
- Título de portada: “Club Ferro Carril Oeste – Sitio web oficial”.
- Meta description presente.
- Open Graph y Twitter Cards presentes.
- `og:url` canónica para la portada.
- Las notas usan un único `h1` visible.
- Las secciones usan jerarquía de headings razonable.
- Las imágenes de noticias tienen `alt` basado en el título.
- La arquitectura conserva muchas URLs históricas, lo que puede ayudar a no perder todo el posicionamiento acumulado.

### Riesgos SEO

- La meta description de portada es genérica y no comunica actividades, noticias, socios ni ubicación.
- El `og:image` de portada apunta a una imagen de abril de 2026, mientras la portada actual muestra piezas de septiembre. Puede ser una imagen social desactualizada.
- Algunas piezas se generan desde Instagram o módulos dinámicos; si el contenido no queda en HTML rastreable, Google puede verlo peor que un bloque editorial normal.
- Los enlaces `#`, las URLs mal formadas y las rutas mezcladas pueden desperdiciar rastreo y generar mala experiencia.
- No se verificó en este corte la existencia y calidad de `robots.txt`, sitemap XML, canonical en todas las plantillas ni datos estructurados JSON-LD.
- No se observó evidencia suficiente de schema específico para `NewsArticle`, `SportsTeam`, `Organization`, `Event` o `SportsEvent`.
- Las placas con texto incrustado no sustituyen títulos HTML descriptivos. El título debe existir fuera de la imagen, como aparentemente ocurre en las noticias principales.
- Las notas tienen títulos muy largos y completamente en mayúsculas. Esto puede funcionar visualmente, pero conviene evaluar legibilidad en snippets y redes.

### Acciones SEO recomendadas

1. Auditar todas las respuestas 200, 301, 404 y 410 del cambio de arquitectura.
2. Generar sitemap limpio por entradas, categorías, páginas y PDFs relevantes.
3. Revisar canonical y Open Graph por plantilla.
4. Implementar JSON-LD para organización, artículos, eventos y partidos cuando corresponda.
5. Crear páginas índice optimizadas para cada deporte, actividad y servicio.
6. Mejorar títulos y descriptions de categorías, no sólo de artículos.
7. Agregar breadcrumbs visibles y en schema.
8. Corregir enlaces HTTP y placeholders.
9. Definir una política para noticias antiguas, campañas vencidas, aranceles y convocatorias.

## 5. Tecnología identificada

### Evidencia directa

- **CMS:** WordPress. El HTML expone `wp-theme-ferro-theme`, rutas `/wp-content/`, `/wp-includes/` y meta generator `WordPress 7.1`.
- **Tema:** `ferro-theme`.
- **Frontend compilado:** archivos `app-*.js` y `app-*.css` bajo `wp-content/themes/ferro-theme/public/build/assets/`, compatible con un proceso moderno de build.
- **Estilos:** clases utilitarias visibles en el `body`, incluyendo `bg-gray-50`, `text-gray-900`, `font-sans` y `antialiased`, lo que sugiere Tailwind CSS o una capa utilitaria equivalente.
- **Tipografías:** Google Fonts con `Bebas Neue` e `Inter`.
- **Analítica:** Google Tag/gtag con ID `G-57H2KDP8S4`, presumiblemente Google Analytics 4.
- **Instagram:** plugin Instagram Feed, versión expuesta `6.13.0`.
- **Formularios:** Contact Form 7, versión expuesta `6.1.7`.
- **Galerías/custom post types:** aparece un plugin `advanced-custom-post-type`.
- **Hosting/CDN:** no se puede confirmar con seguridad sólo desde la interfaz observada; debe verificarse con headers, DNS y una herramienta de fingerprinting independiente.
- **Desarrollo:** el footer atribuye el desarrollo a [No Limits Design](http://www.nolimitsdesign.com.ar/).

### Lectura técnica

La inferencia más razonable es que se mantiene WordPress como back office y se reemplaza buena parte del frontend del tema por una capa compilada moderna. Esto es una decisión sensata para un sitio editorial con muchos autores y categorías: conserva el flujo de publicación de WordPress y permite una experiencia visual más controlada.

El punto débil es el contrato entre contenido y frontend. Las etiquetas internas, URLs inconsistentes, enlaces `#` y alt vacíos sugieren que el nuevo tema todavía no valida suficientemente los datos que recibe desde WordPress.

## 6. Accesibilidad

### Aspectos positivos

- Hay nombres accesibles para “Abrir menú”, “Cerrar menú”, “Buscar”, “Slide anterior” y “Slide siguiente”.
- Se usan headings con jerarquía reconocible.
- Los artículos tienen fecha, categoría y título explícitos.
- El contenido principal parece estar renderizado en HTML, no sólo como imagen.

### Riesgos

- Imágenes funcionales sin `alt`.
- Enlaces con `#` que no expresan una acción real.
- Posible bajo contraste en texto verde o blanco sobre fotografía oscurecida; requiere medición WCAG, no sólo observación visual.
- Carrusel con muchos estados y posible autoplay.
- No se verificó foco visible, navegación completa por teclado, cierre del menú con Escape, `aria-expanded`, `aria-controls` ni gestión del foco en el overlay.
- La tipografía display condensada en tamaños grandes puede afectar lectura de títulos extensos.
- Los iconos de redes necesitan nombre accesible y diferenciación clara entre enlaces.

## 7. Contenido: fortalezas y faltantes

### Fortalezas

- La web presenta al club como una institución multideportiva, educativa y social.
- Hay un esfuerzo explícito por mostrar obras, infraestructura, sponsors, historia y disciplinas.
- La información institucional no desapareció con el rediseño.
- La portada se actualiza con noticias recientes y convive con documentación histórica.

### Faltantes o puntos a revisar

- No hay una ruta obvia y destacada para “todas las actividades” con filtros por edad, sede, género, nivel y disponibilidad.
- El contenido de socios mezcla portal, campaña, venta de entradas, abonos y servicios sin una landing unificada.
- No se ve una política editorial para contenidos vencidos: convocatorias, aranceles, abonos y horarios pueden quedar circulando como si fueran actuales.
- La web podría explicar mejor quién es responsable de cada área y cómo contactar a fútbol, básquet, actividades, educación, prensa y socios.
- Conviene revisar lenguaje inclusivo y consistencia: “socios/as”, “socias y socios”, “asociate”, mayúsculas y categorías no siempre siguen un mismo criterio.
- El módulo de “Más leídas” puede sobrerrepresentar actas o convocatorias si el criterio de popularidad no distingue entre interés editorial y necesidad institucional.

## 8. Qué priorizaría

### En la primera semana

1. Corregir el doble `www`, todos los `#` de contenidos clickeables y los enlaces HTTP.
2. Unificar el destino de asociación.
3. Completar `alt` y nombres accesibles de banners, sponsors y módulos.
4. Revisar Ferro Play para que cada tarjeta abra el contenido correcto.
5. Revisar links del menú en móvil y escritorio.

### En el primer mes

1. Hacer una auditoría completa de redirecciones y URLs heredadas.
2. Publicar un índice de actividades/deportes y un calendario de eventos.
3. Convertir campañas de socios en landing pages con CTA y datos concretos.
4. Revisar sitemap, canonical, robots, schema y Open Graph.
5. Medir Core Web Vitals en móvil y escritorio.
6. Probar el sitio con teclado, lector de pantalla y contraste WCAG.
7. Agregar tests automáticos de enlaces internos, imágenes sin alt y URLs HTTP.

### Como evolución de producto

- Crear un “Centro del socio” con asociación, pagos, actividades, entradas, abonos, horarios y contacto.
- Agregar una agenda unificada de partidos, actividades y eventos.
- Usar filtros y buscador por deporte, sede y público.
- Separar actualidad periodística de información operativa.
- Incorporar un sistema de alertas para convocatorias, cierres, cambios de horario y venta de entradas.
- Tratar documentación institucional —actas, balances, estatuto, contrataciones— como una biblioteca navegable, no sólo como noticias.

## 9. Evidencia y límites

- La web actual se inspeccionó visualmente en escritorio y en una ventana angosta tipo móvil, y mediante su árbol de accesibilidad y DOM.
- La versión histórica se contrastó con la captura de Wayback del 30/11/2024. La captura visual archivada quedó en estado de carga incompleta, por lo que la comparación histórica se apoya principalmente en la estructura y los contenidos que el snapshot conserva.
- No se hizo un test de rendimiento de laboratorio ni una medición formal de Core Web Vitals.
- No se verificó exhaustivamente cada URL del sitio, cada formulario, cada breakpoint ni cada estado del menú.
- No se puede confirmar desde la interfaz si existe CDN, WAF, hosting específico o una integración de despliegue determinada.
- Las observaciones de contenido son un corte temporal: noticias, fixtures, sponsors, aranceles y datos de contacto deben revisarse periódicamente.

## Fuentes consultadas

- [Sitio oficial actual](https://www.ferrocarriloeste.org.ar/)
- [Página interna de campaña de socios](https://www.ferrocarriloeste.org.ar/club/ferro-abre-una-nueva-campana-de-socios-y-socias-hoy-mas-que-nunca-volve-a-ferro/)
- [Manual de marca / imagen institucional](https://www.ferrocarriloeste.org.ar/escudo/)
- [FCONLINE, portal de socios](https://www.ferrocarriloeste.org.ar/institucional/fconline-el-nuevo-portal-de-socios-as/)
- [Captura histórica de Wayback, noviembre de 2024](https://web.archive.org/web/20241201000000/https://www.ferrocarriloeste.org.ar/)
- [Búsqueda indexada de Google sobre el sitio](https://www.google.com/search?q=site%3Aferrocarriloeste.org.ar+Club+Ferro+Carril+Oeste)
