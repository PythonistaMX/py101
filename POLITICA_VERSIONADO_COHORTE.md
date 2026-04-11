# Politica de Versionado por Cohorte (Py101)

Esta politica define como congelar y operar el entorno del curso Py101 por generacion cuando se imparte con GitHub Codespaces.

## Objetivo

- Garantizar que todos los estudiantes de una cohorte trabajen con el mismo entorno.
- Evitar diferencias de comportamiento entre sesiones por cambios en dependencias.
- Mantener trazabilidad tecnica para soporte y auditoria academica.

## Alcance

- Aplica a todas las cohortes activas de Py101.
- Aplica a clases en vivo, material asincronico y evaluaciones por bloque.

## Regla de Cohorte

Cada cohorte debe tener una version academica fija del curso con este formato:

- `py101-cYYYY-MM`

Ejemplos:

- `py101-c2026-04`
- `py101-c2026-08`

## Congelamiento Tecnico (Baseline)

Antes de iniciar una cohorte, el instructor responsable debe congelar:

1. Referencia de contenido (tag o commit).
2. Configuracion de contenedor en `.devcontainer/`.
3. Version de Python del entorno.
4. Dependencias efectivas del kernel (lista exportada).

## Evidencia Minima por Cohorte

Guardar en `cohortes/py101-cYYYY-MM/`:

1. `README_COHORTE.md` (fechas, instructor, objetivos y alcance).
2. `ENV_BASELINE.txt` con:
   - hash de commit
   - version de Python
   - lista de paquetes del kernel
3. `NOTAS_CAMBIOS.md` con ajustes aplicados durante la imparticion.

## Politica de Cambios Durante Imparticion

- Cambios permitidos: correcciones de erratas, ajustes de redaccion y ejemplos menores.
- Cambios no permitidos sin aprobacion academica: alterar alcance de evaluacion, prerrequisitos o secuencia de temas.
- Todo cambio debe registrarse en `NOTAS_CAMBIOS.md` con fecha y motivo.

## Evaluaciones por Bloque

- Las evaluaciones se deben ejecutar con la misma baseline de la cohorte.
- Si se actualiza entorno por causa mayor, se debe publicar una fe de erratas y revalidar instrucciones.

## Cierre de Cohorte

Al finalizar:

1. Etiquetar estado final de la cohorte.
2. Archivar evidencias y retroalimentacion recurrente.
3. Proponer mejoras para la siguiente cohorte sin modificar retrospectivamente la cerrada.

## Checklist Operativo Rapido

Antes de la sesion 1:

- [ ] Cohorte etiquetada (`py101-cYYYY-MM`).
- [ ] Codespace de prueba ejecutado correctamente.
- [ ] Notebooks troncales abiertos y celdas clave verificadas.
- [ ] Evidencia `ENV_BASELINE.txt` creada.

Antes de cada evaluacion de bloque:

- [ ] Confirmar que no hubo drift del entorno.
- [ ] Validar notebook y datos de la evaluacion.
- [ ] Publicar instrucciones consistentes con la baseline.
