# Politica Editorial de Contenido (Py101)

Esta politica define los criterios editoriales minimos para mantener consistencia terminologica y tipografica en el material del curso Py101.

## Objetivo

- Mantener uniformidad en el lenguaje del curso.
- Reducir ambiguedades entre texto explicativo, codigo e instrucciones operativas.
- Facilitar revisiones editoriales futuras sobre notebooks y documentos de apoyo.

## Alcance

- Aplica a todas las notebooks del curso.
- Aplica a documentos markdown de apoyo cuando usen los mismos terminos tecnicos del curso.
- No sustituye criterios pedagogicos o tecnicos del contenido; solo establece reglas de redaccion y formato editorial.

## Regla General

En texto explicativo escrito en markdown, los anglicismos tecnicos y nombres de sistemas operativos definidos por esta politica deben representarse de forma consistente, privilegiando claridad y diferenciacion respecto de codigo, comandos y literales.

## Anglicismos Tecnicos

- Usar cursivas para terminos como `Python`, `script`, `notebook`, `kernel` y otros anglicismos tecnicos equivalentes cuando formen parte de la prosa explicativa.
- Aplicar el mismo criterio a terminos como `Jupyter`, `IPython`, `shell`, `prompt` y otros prestamos linguisticos cuando se usen como conceptos dentro de la explicacion.
- Mantener consistencia dentro de una misma notebook y entre notebooks del curso.

## Sistemas Operativos y Plataformas

- Escribir `macOS` exactamente de esa forma.
- No usar `MacOS` ni `MacOS X` en texto editorial actualizado.
- Cuando se mencione la plataforma general, preferir `GNU/Linux` en lugar de `Linux`.
- Escribir en cursivas los nombres de sistemas operativos en prosa: `GNU/Linux`, `macOS`, `Windows` y `UNIX`.

## Exclusiones

No aplicar estas reglas de cursivas dentro de:

- bloques de codigo cercados
- fragmentos de codigo inline
- comandos, rutas, nombres de archivo o literales tecnicos cuando deban conservar sintaxis exacta
- salidas de ejecucion, metadatos o contenido serializado de notebooks, salvo correccion justificada

## Criterio de Edicion

- Limitar los cambios editoriales a celdas markdown, salvo necesidad tecnica explicita.
- No modificar codigo de ejemplo solo para forzar consistencia tipografica en prosa.
- Evitar cambios de redaccion no relacionados con el objetivo editorial de la revision.
- Preservar el sentido pedagogico original del material.

## Validacion Recomendada

En revisiones masivas:

1. Buscar terminos objetivo solo en contenido markdown.
2. Excluir bloques de codigo para evitar falsos positivos.
3. Confirmar que no se alteraron comandos, ejemplos ejecutables ni salidas.
4. Revisar diff final para verificar que los cambios queden acotados a redaccion y formato.

## Actualizacion de la Politica

- Toda excepcion recurrente debe documentarse aqui.
- Si se agregan nuevos terminos tecnicos al curso, deben incorporarse de manera explicita a esta politica.
- Las actualizaciones deben mantener compatibilidad con el estilo general del repositorio.