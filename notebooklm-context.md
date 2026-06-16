# Resumen de la notebook

NotebookLM: `Ferro Actas Publicas` (`a44c97a9-d538-4de7-8915-c728b2f7774b`).

Esta notebook reúne fuentes publicas de Ferrocarril Oeste de los ultimos años para consultar, comparar y verificar actas, balances, convocatorias y materiales vinculados.

La idea es que funcione como un punto de acceso a la informacion historica: se suben los documentos originales y los indices para poder responder preguntas con contexto y citas.

## Metadata actual

- Etiquetas activas:
  - `Asamblea - Actas`
  - `Asamblea - Balances`
  - `Asamblea - Convocatorias`
  - `Asamblea - Tutoriales`
  - `CD - Actas`
  - `CD - Balances`
  - `Soporte - Indices y notas`
  - `Documentación General`
- Criterio aplicado:
  - En Asamblea, usar `ej###` cuando el acta nombra el ejercicio; si no lo nombra de forma explicita, conservar una referencia por fecha.
  - En Comision Directiva, conservar el esquema `p###/s###` propio del archivo.
  - Los indices y notas viven fuera de las etiquetas de actas.
- Estado del proceso:
  - `Asamblea - Actas` y `CD - Actas` quedaron normalizadas en NotebookLM.
  - `CD - Balances` quedo separado correctamente.
  - La notebook ya es util para consultas generales, pero la metadata ampliada por documento sigue siendo parcial.

## Convencion de ejercicios

- Cuando un documento menciona un `Ejercicio`, se interpreta como un periodo de dos anos y se normaliza como `E### (AAAA/AAAA)`.
- Ejemplo: `Ejercicio 119` = `E119 (2022/2023)`.
- Para balances y memorias, conviene buscar siempre tambien por la fecha de cierre visible en el documento.

## Que permite consultar

- la ultima acta o balance disponible;
- una sesion, asamblea o convocatoria concreta;
- documentos que estan divididos en partes;
- diferencias entre la fecha del archivo, la fecha visible dentro del documento y la fecha de publicacion;
- si un nombre de archivo coincide o no con lo que muestra el PDF o DOCX;
- relaciones entre actas, balances y convocatorias del mismo periodo.

## Como usarla

- preguntando por fecha, sesion, periodo o tipo de documento;
- pidiendo comparaciones entre archivos;
- pidiendo que confirme datos visibles dentro del documento;
- usando los indices como guia para ubicar la fuente correcta antes de leer el original.

## Ejemplos de preguntas

- "Cual es la ultima acta de Comision Directiva y que dice la primera pagina?"
- "Que balance corresponde a la asamblea de septiembre de 2025?"
- "Este archivo parece escaneado: la fecha del nombre coincide con la fecha visible?"
- "Que documentos estan vinculados a la sesion 26 del periodo 101?"
- "Hay algun documento dividido en varias partes o con nombre inconsistente?"

## Regla practica

Si el documento original, el nombre del archivo y el indice no coinciden del todo, conviene conservar la diferencia como observacion en vez de forzar una sola fecha.
