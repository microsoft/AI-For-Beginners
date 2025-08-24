<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "7df19702b8d2d3f7c4238c51bec2c8fc",
  "translation_date": "2025-08-24T09:26:09+00:00",
  "source_file": "lessons/0-course-setup/how-to-run.md",
  "language_code": "es"
}
-->
# Cómo Ejecutar el Código

Este curso contiene muchos ejemplos ejecutables y laboratorios que querrás ejecutar. Para hacerlo, necesitas la capacidad de ejecutar código Python en Jupyter Notebooks proporcionados como parte de este curso. Tienes varias opciones para ejecutar el código:

## Ejecutar localmente en tu computadora

Para ejecutar el código localmente en tu computadora, necesitas tener alguna versión de Python instalada. Personalmente, recomiendo instalar **[miniconda](https://conda.io/en/latest/miniconda.html)**: es una instalación bastante ligera que soporta el gestor de paquetes `conda` para diferentes **entornos virtuales** de Python.

Después de instalar miniconda, necesitas clonar el repositorio y crear un entorno virtual para usar en este curso:

```bash
git clone http://github.com/microsoft/ai-for-beginners
cd ai-for-beginners
conda env create --name ai4beg --file .devcontainer/environment.yml
conda activate ai4beg
```

### Usar Visual Studio Code con la Extensión de Python

Probablemente la mejor manera de usar el curso es abrirlo en [Visual Studio Code](http://code.visualstudio.com/?WT.mc_id=academic-77998-cacaste) con la [Extensión de Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-77998-cacaste).

> **Nota**: Una vez que clones y abras el directorio en VS Code, automáticamente te sugerirá instalar las extensiones de Python. También tendrás que instalar miniconda como se describió anteriormente.

> **Nota**: Si VS Code te sugiere reabrir el repositorio en un contenedor, necesitas rechazar esta opción para usar la instalación local de Python.

### Usar Jupyter en el Navegador

También puedes usar el entorno de Jupyter directamente desde el navegador en tu propia computadora. De hecho, tanto Jupyter clásico como Jupyter Hub ofrecen un entorno de desarrollo bastante conveniente con autocompletado, resaltado de código, etc.

Para iniciar Jupyter localmente, ve al directorio del curso y ejecuta:

```bash
jupyter notebook
```
o
```bash
jupyterhub
```
Luego puedes navegar a cualquiera de los archivos `.ipynb`, abrirlos y comenzar a trabajar.

### Ejecutar en un contenedor

Una alternativa a la instalación de Python sería ejecutar el código en un contenedor. Dado que nuestro repositorio contiene una carpeta especial `.devcontainer` que indica cómo construir un contenedor para este repositorio, VS Code te ofrecerá reabrir el código en un contenedor. Esto requerirá la instalación de Docker y será más complejo, por lo que recomendamos esta opción para usuarios más experimentados.

## Ejecutar en la Nube

Si no deseas instalar Python localmente y tienes acceso a algunos recursos en la nube, una buena alternativa sería ejecutar el código en la nube. Hay varias maneras de hacerlo:

* Usar **[GitHub Codespaces](https://github.com/features/codespaces)**, que es un entorno virtual creado para ti en GitHub, accesible a través de la interfaz del navegador de VS Code. Si tienes acceso a Codespaces, simplemente puedes hacer clic en el botón **Code** en el repositorio, iniciar un codespace y comenzar a trabajar rápidamente.
* Usar **[Binder](https://mybinder.org/v2/gh/microsoft/ai-for-beginners/HEAD)**. [Binder](https://mybinder.org) proporciona recursos de computación gratuitos en la nube para personas como tú que quieren probar código en GitHub. Hay un botón en la página principal para abrir el repositorio en Binder, lo que debería llevarte rápidamente al sitio de Binder, que construirá el contenedor subyacente y comenzará la interfaz web de Jupyter de manera fluida.

> **Nota**: Para prevenir el mal uso, Binder tiene acceso bloqueado a algunos recursos web. Esto puede impedir que funcione parte del código que descarga modelos y/o conjuntos de datos desde Internet público. Es posible que necesites buscar algunas soluciones alternativas. Además, los recursos de computación proporcionados por Binder son bastante básicos, por lo que el entrenamiento será lento, especialmente en lecciones más complejas.

## Ejecutar en la Nube con GPU

Algunas de las lecciones más avanzadas de este curso se beneficiarían enormemente del soporte de GPU, ya que de lo contrario el entrenamiento será extremadamente lento. Hay algunas opciones que puedes seguir, especialmente si tienes acceso a la nube, ya sea a través de [Azure para Estudiantes](https://azure.microsoft.com/free/students/?WT.mc_id=academic-77998-cacaste) o a través de tu institución:

* Crear una [Máquina Virtual de Ciencia de Datos](https://docs.microsoft.com/learn/modules/intro-to-azure-data-science-virtual-machine/?WT.mc_id=academic-77998-cacaste) y conectarte a ella a través de Jupyter. Luego puedes clonar el repositorio directamente en la máquina y comenzar a aprender. Las máquinas virtuales de la serie NC tienen soporte para GPU.

> **Nota**: Algunas suscripciones, incluyendo Azure para Estudiantes, no proporcionan soporte para GPU de manera predeterminada. Es posible que necesites solicitar núcleos de GPU adicionales a través de una solicitud de soporte técnico.

* Crear un [Espacio de Trabajo de Azure Machine Learning](https://azure.microsoft.com/services/machine-learning/?WT.mc_id=academic-77998-cacaste) y luego usar la función de Notebook allí. [Este video](https://azure-for-academics.github.io/quickstart/azureml-papers/) muestra cómo clonar un repositorio en el notebook de Azure ML y comenzar a usarlo.

También puedes usar Google Colab, que incluye soporte gratuito para GPU, y subir los Jupyter Notebooks allí para ejecutarlos uno por uno.

**Descargo de responsabilidad**:  
Este documento ha sido traducido utilizando el servicio de traducción automática [Co-op Translator](https://github.com/Azure/co-op-translator). Aunque nos esforzamos por garantizar la precisión, tenga en cuenta que las traducciones automatizadas pueden contener errores o imprecisiones. El documento original en su idioma nativo debe considerarse la fuente autorizada. Para información crítica, se recomienda una traducción profesional realizada por humanos. No nos hacemos responsables de malentendidos o interpretaciones erróneas que puedan surgir del uso de esta traducción.