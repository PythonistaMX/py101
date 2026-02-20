# Introducción a la Programación con Python 3 (Py101)

[![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![Jupyter](https://img.shields.io/badge/Made%20with-Jupyter-orange?logo=jupyter&logoColor=white)](https://jupyter.org/try)
[![Dev Containers](https://img.shields.io/badge/Dev%20Containers-blue?logo=visualstudiocode&logoColor=white)](https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/PythonistaMX/py101)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Open in Codespaces](https://github.com/codespaces/badge.svg)](https://github.com/codespaces/new?hide_repo_select=true&ref=main&repo=152273296)

> Estado: ✅ Curso Activo | Nivel: Básico

Este repositorio contiene el material oficial del curso **Py101**, enfocado en los fundamentos del lenguaje de programación Python 3. Es el punto de partida perfecto para iniciarse en el mundo de la programación con Python.

## 🗺️ Ruta de Aprendizaje

Este curso forma parte de la serie **Fundamentos de Python (py1xx)**:

| Curso | Título | Estado |
| :---: | :--- | :--- |
| **py101** | **Introducción a Python 3** | **✅ Este curso** |
| **py111** | POO con Python 3 | Siguiente paso |
| **py121** | Biblioteca estándar de Python | Futuro |
| **py131** | Estructuras de Datos y Algoritmia | Especialización |
| **py141** | Automatización y Extracción de Datos | Aplicación práctica |

## 🚀 Acerca del Curso

Un programa diseñado para aprender las bases de la programación utilizando Python. Al completarlo serás capaz de:

*   Comprender la sintaxis y semántica básica de **Python 3**.
*   Utilizar **Jupyter Notebooks** como herramienta de desarrollo.
*   Dominar los **tipos de datos** básicos y colecciones (listas, tuplas, diccionarios).
*   Controlar el flujo del programa con **condicionales y ciclos**.
*   Modularizar código utilizando **funciones y módulos**.
*   Gestionar errores mediante **excepciones**.
*   Trabajar con **archivos** y estructura de paquetes.

## 📅 Temario y Estructura

El contenido está dividido en cuadernos (notebooks) progresivos:

### 📚 Contenidos

*   `01` - [Introducción a Python](01_introduccion.ipynb)
*   `02` - [IPython y Jupyter](02_ipython_y_jupyter.ipynb)
*   `03` - [Palabras reservadas y nombres](03_palabras_reservadas_y_nombres.ipynb)
*   `04` - [Introspección y ayuda](04_introspeccion_y_ayuda.ipynb)
*   `05` - [Expresiones y comentarios](05_expresiones_y_comentarios.ipynb)
*   `06` - [Tipos de datos](06_tipos_de_datos_en_python.ipynb)
*   `07` - [Conversión de tipos básicos](07_conversion_de_tipos_basicos.ipynb)
*   `08` - [Colecciones](08_colecciones_en_python.ipynb)
*   `09` - [Expresiones con operadores](09_expresiones_con_operadores.ipynb)
*   `10` - [Entrada y salida estándar](10_entrada_y_salida_estandar.ipynb)
*   `11` - [Declaraciones y bloques de código](11_declaraciones_y_bloques_de_codigo.ipynb)
*   `12` - [Condicionales](12_condicionales.ipynb)
*   `13` - [Ciclos e interrupciones de flujo](13_ciclos_e_interrupciones_de_flujo.ipynb)
*   `14` - [Iteraciones](14_iteraciones.ipynb)
*   `15` - [Funciones](15_funciones.ipynb)
*   `16` - [Tipos list y tuple](16_tipos_list_y_tuple.ipynb)
*   `17` - [Tipo str](17_tipo_str.ipynb)
*   `18` - [F-strings](18_f-strings.ipynb)
*   `19` - [Tipos bytes y bytearray](19_tipos_bytes_y_bytearray.ipynb)
*   `20` - [Tipo dict](20_tipo_dict.ipynb)
*   `21` - [Tipos set y frozenset](21_tipos_set_y_frozenset.ipynb)
*   `22` - [Bases de programación funcional](22_bases_de_programacion_funcional.ipynb)
*   `23` - [Coincidencia de patrones (match/case)](23_coincidencia_de_patrones.ipynb)
*   `24` - [Gestión de excepciones](24_gestion_de_excepciones.ipynb)
*   `25` - [Iteradores y generadores](25_iteradores_y_generadores.ipynb)
*   `26` - [Completado de elementos](26_completado_de_elementos.ipynb)
*   `27` - [Lectura y escritura de archivos](27_lectura_y_escritura_de_archivos.ipynb)
*   `28` - [Módulos y paquetes](28_modulos_paquetes.ipynb)
*   `29` - [Distribución de código](29_distribucion_de_codigo.ipynb)
*   `30` - [Gestión de paquetes](30_gestion_de_paquetes.ipynb)
*   `31` - [Entornos virtuales](31_entornos_virtuales.ipynb)

## 🛠️ Instalación y Uso

¡Olvídate de configurar entornos locales complejos! Este repositorio está configurado para **GitHub Codespaces**.

1.  Haz clic en el botón **"Code"** (verde) arriba a la derecha.
2.  Ve a la pestaña **"Codespaces"**.
3.  Haz clic en **"Create codespace on main"**.

El entorno se iniciará automáticamente con Python 3 y todas las extensiones necesarias listas para usar.

### Ejecución Local (Opcional)

Si prefieres trabajar en tu máquina:

1.  **Clonar el repositorio**
    ```bash
    git clone https://github.com/PythonistaMX/py101.git
    cd py101
    ```

2.  **Crear entorno virtual (Recomendado)**
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # En Windows: venv\Scripts\activate
    ```

3.  **Iniciar Jupyter**
    ```bash
    # (Asegúrate de tener jupyter instalado o instálalo con pip install jupyter)
    jupyter lab
    ```

## 📝 Licencia

Este material es desarrollado y mantenido por José Luis Chiquete Valdivieso.

Este proyecto está bajo la licencia **Creative Commons Atribución 4.0 Internacional (CC-BY 4.0)**.

Eres libre de:

*   ✅ Compartir el material en cualquier medio o formato
*   ✅ Adaptar, remezclar y crear contenido derivado
*   ✅ Usar con fines comerciales

Con la condición de:

*   Reconocer la autoría original

Para más detalles, consulta el archivo [LICENSE](LICENSE).
