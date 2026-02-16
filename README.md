# Introducción a la Programación con Python (Py101)

[![Python](https://img.shields.io/badge/Python-3.11+-blue?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Codespaces](https://img.shields.io/badge/GitHub-Codespaces-brightgreen?style=for-the-badge&logo=github&logoColor=white)](https://github.com/features/codespaces)
[![License](https://img.shields.io/badge/License-CC--BY%204.0-blue.svg?style=for-the-badge)](LICENSE)

> **Estado:** ✅ Curso Activo | **Nivel:** Principiante

Este repositorio contiene el material oficial del curso **Py101**, el punto de partida fundamental para cualquier ruta de desarrollo en Python. Cubre desde la sintaxis básica y los tipos de datos hasta la modularización y el uso de entornos virtuales.

---

## 🗺️ Ruta de Aprendizaje

### Prerrequisitos

Este es el curso introductorio. No se requieren conocimientos previos de programación, aunque es útil tener familiaridad básica con el uso de una terminal.

### Continuación de la ruta

Py101 es el primer paso de una formación completa:

| Curso | Título | Estado |
| :--- | :--- | :--- |
| **Py101** | **Introducción a la Programación con Python** | ✅ **Este curso** |
| Py111 | Programación Orientada a Objetos | Siguiente paso |
| Py311 | Fundamentos de Ingeniería de Datos | Avanzado |
---

## 🚀 Acerca del Curso

Un programa diseñado para construir una base sólida en el lenguaje Python 3. Al completarlo serás capaz de:

*   **Comprender la sintaxis de Python:** Variables, expresiones, comentarios y palabras reservadas.
*   **Dominar los tipos de datos:** Desde básicos (int, float, str) hasta colecciones complejas (list, diet, set).
*   **Controlar el flujo del programa:** Condicionales, ciclos iterativos y manejo de excepciones.
*   **Estructurar código reutilizable:** Funciones, generadores y comprensión de listas.
*   **Organizar proyectos:** Uso de módulos, paquetes y creación de entornos virtuales.
*   **Interactuar con el sistema:** Lectura/escritura de archivos y entrada/salida estándar.

Todo el entorno se ejecuta en la nube mediante **GitHub Codespaces**, sin necesidad de instalación local compleja.

---

## 📅 Temario y Estructura

El contenido está dividido en cuadernos (notebooks) progresivos:

### 📚 Contenidos

#### 🔹 Módulo 1: Primeros Pasos
*   `01` - [Introducción](01_introduccion.ipynb)
*   `02` - [IPython y Jupyter](02_ipython_y_jupyter.ipynb)
*   `03` - [Palabras reservadas y nombres](03_palabras_reservadas_y_nombres.ipynb)
*   `04` - [Introspección y ayuda](04_introspeccion_y_ayuda.ipynb)

#### 🔹 Módulo 2: Datos y Operaciones Básicas
*   `05` - [Expresiones y comentarios](05_expresiones_y_comentarios.ipynb)
*   `06` - [Tipos de datos en Python](06_tipos_de_datos_en_python.ipynb)
*   `07` - [Conversión de tipos básicos](07_conversion_de_tipos_basicos.ipynb)
*   `08` - [Colecciones en Python](08_colecciones_en_python.ipynb)
*   `09` - [Expresiones con operadores](09_expresiones_con_operadores.ipynb)

#### 🔹 Módulo 3: Control de Flujo
*   `10` - [Entrada y salida estándar](10_entrada_y_salida_estandar.ipynb)
*   `11` - [Declaraciones y bloques de código](11_declaraciones_y_bloques_de_codigo.ipynb)
*   `12` - [Condicionales](12_condicionales.ipynb)
*   `13` - [Ciclos e interrupciones de flujo](13_ciclos_e_interrupciones_de_flujo.ipynb)
*   `14` - [Iteraciones](14_iteraciones.ipynb)

#### 🔹 Módulo 4: Funciones y Tipos Estructurados
*   `15` - [Funciones](15_funciones.ipynb)
*   `16` - [Tipos list y tuple](16_tipos_list_y_tuple.ipynb)
*   `17` - [Tipo str](17_tipo_str.ipynb)
*   `18` - [f-strings](18_f-strings.ipynb)
*   `19` - [Tipos bytes y bytearray](19_tipos_bytes_y_bytearray.ipynb)
*   `20` - [Tipo dict](20_tipo_dict.ipynb)
*   `21` - [Tipos set y frozenset](21_tipos_set_y_frozenset.ipynb)

#### 🔹 Módulo 5: Programación Avanzada
*   `22` - [Bases de programación funcional](22_bases_de_programacion_funcional.ipynb)
*   `23` - [Gestión de excepciones](23_gestion_de_excepciones.ipynb)
*   `24` - [Iteradores y generadores](24_iteradores_y_generadores.ipynb)
*   `25` - [Completado de elementos (Comprehensions)](25_completado_de_elementos.ipynb)

#### 🔹 Módulo 6: I/O y Modularización
*   `26` - [Lectura y escritura de archivos](26_lectura_y_escritura_de_archivos.ipynb)
*   `27` - [Módulos y paquetes](27_modulos_paquetes.ipynb)
*   `28` - [Distribución de código](28_distribucion_de_codigo.ipynb)
*   `29` - [Gestión de paquetes](29_gestion_de_paquetes.ipynb)
*   `30` - [Entornos virtuales](30_entornos_virtuales.ipynb)

---

## 🛠️ Instalación y Uso

¡Olvídate de configurar entornos locales complejos! Este repositorio está configurado para **GitHub Codespaces**.

1.  Haz clic en el botón **"Code"** (verde) arriba a la derecha.
2.  Ve a la pestaña **"Codespaces"**.
3.  Haz clic en **"Create codespace on main"**.

El entorno se iniciará automáticamente con Python 3 y todas las extensiones necesarias listas para usar.

### Ejecución Local (Opcional)

Si prefieres trabajar en tu máquina:

```bash
# 1. Clonar el repositorio
git clone https://github.com/PythonistaMX/py101.git
cd py101

# 2. Crear entorno virtual (Recomendado)
python3 -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate

# 3. Iniciar Jupyter
# (Asegúrate de tener jupyter instalado o instálalo con pip install jupyter)
jupyter lab
```

---

## 📝 Licencia

Este material es desarrollado y mantenido por José Luis Chiquete Valdivieso (2017-2026).

Este proyecto está bajo la licencia **Creative Commons Atribución 4.0 Internacional (CC-BY 4.0)**.

**Eres libre de:**
- ✅ Compartir el material en cualquier medio o formato
- ✅ Adaptar, remezclar y crear contenido derivado
- ✅ Usar con fines comerciales

**Con la condición de:**
- 📌 **Atribución:** Debes dar crédito apropiado, proporcionar un enlace a la licencia e indicar si se han realizado cambios.

Para más información, visita: [https://creativecommons.org/licenses/by/4.0/](https://creativecommons.org/licenses/by/4.0/)

Véase el archivo [LICENSE](LICENSE) para los términos completos.