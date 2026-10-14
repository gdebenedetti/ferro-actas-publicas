# Resumen de la notebook

NotebookLM `Ferro Actas Publicas` reúne documentos públicos de Ferrocarril Oeste para consultar y contrastar actas de Comisión Directiva, actas de asambleas, balances, convocatorias, el estatuto y materiales de referencia.

## Cómo está organizado

- `Comisión Directiva - Actas`: actas de CD; algunas sesiones incluyen balances o anexos financieros, pero siguen siendo actas ordinarias.
- `Asamblea - Actas`: actas de asambleas ordinarias y extraordinarias.
- `Asamblea - Balances`: memorias y balances, identificados también por ejercicio.
- `Estatuto`: estatuto del club.
- `Soporte - Indices y notas`: inventarios cronológicos, resumen y mapa de consolidaciones.

Estas son las cinco etiquetas que devuelve el CLI al 13/10/2026. No aparecen actualmente etiquetas `Asamblea - Convocatorias` ni `Documentación General`; no se recrean como parte de esta actualización.

## Criterio de nombres y fechas

Las fuentes documentales usan primero la fecha del evento o cierre que el documento acredita, con el patrón `AAAA-MM-DD__tipo__referencia`. La fecha de publicación o escaneo puede ser posterior y se conserva como dato distinto cuando es relevante. Las referencias de ejercicios se expresan como `E### (AAAA/AAAA)`, por ejemplo `E119 (2022/2023)`. Las fuentes sin una fecha documental pertinente, como el estatuto, mantienen un título descriptivo.

## Fuentes consolidadas

Algunas fuentes multipartes o históricas se agruparon en PDFs para ahorrar capacidad sin perder las páginas originales. Cada PDF consolidado comienza con una guía de contenido y rangos de páginas. El archivo `source-map.md` identifica cada fuente reemplazada, su orden y sus páginas; los índices, en cambio, describen el inventario local de originales. Los bundles preservan imágenes y texto embebido; no se aplicó OCR nuevo. Las fusiones no implican validar cifras contables: para números, nombres o citas literales, contrastar las páginas originales.

## Consultas posibles

- ¿Qué fecha de sesión aparece dentro del acta P101-S019 y cuándo se publicó?
- ¿Qué temas trata una sesión de Comisión Directiva que también incluye un balance mensual?
- ¿Qué documentos corresponden a E119 (2022/2023) y en qué orden aparecen en el consolidado?
- ¿Qué resolvió una asamblea y qué balance o ejercicio se presentó?
- ¿Qué personas aparecen y con qué cargos o condición de socio, indicando página y fuente?
- ¿Qué diferencias hay entre el inventario de originales y las fuentes consolidadas de la notebook?

## Capacidad al corte

Al 13/10/2026 hay 76 fuentes activas de un máximo de 100 en el plan Plus: 24 lugares disponibles. Entre ellas hay 16 PDFs consolidados (siete agrupaciones históricas y nueve fusiones multipartes). El conteo puede cambiar si se agregan o eliminan fuentes.

## Límites de lectura

NotebookLM sirve para localizar y relacionar información. En documentos escaneados, la extracción de texto puede ser incompleta; no tomar transcripciones o cifras recuperadas automáticamente como verificación contable. Pedir citas y páginas y comprobar los valores directamente en el PDF cuando su exactitud importe.
