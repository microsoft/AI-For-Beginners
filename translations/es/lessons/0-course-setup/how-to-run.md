# Cómo Ejecutar el Código

Este plan de estudios contiene muchos ejemplos y laboratorios ejecutables que querrás correr. Para hacer esto, necesitas la capacidad de ejecutar código Python en los Jupyter Notebooks proporcionados como parte de este plan de estudios. Tienes varias opciones para ejecutar el código:

## Ejecutar localmente en tu computadora

Para ejecutar el código localmente en tu computadora, necesitas tener alguna versión de Python instalada. Personalmente, recomiendo instalar **[miniconda](https://conda.io/en/latest/miniconda.html)**; es una instalación bastante ligera que soporta el gestor de paquetes `conda` para diferentes **entornos virtuales** de Python.

Después de instalar miniconda, necesitas clonar el repositorio y crear un entorno virtual que se utilizará para este curso:

```bash
git clone http://github.com/microsoft/ai-for-beginners
cd ai-for-beginners
conda env create --name ai4beg --file .devcontainer/environment.yml
conda activate ai4beg
```

### Usando Visual Studio Code con la Extensión de Python

Probablemente, la mejor manera de utilizar el plan de estudios es abrirlo en [Visual Studio Code](http://code.visualstudio.com/?WT.mc_id=academic-77998-cacaste) con la [Extensión de Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-77998-cacaste).

> **Nota**: Una vez que clones y abras el directorio en VS Code, te sugerirá automáticamente instalar las extensiones de Python. También tendrás que instalar miniconda como se describió anteriormente.

> **Nota**: Si VS Code te sugiere reabrir el repositorio en un contenedor, debes rechazar esto para usar la instalación local de Python.

### Usando Jupyter en el Navegador

También puedes usar el entorno de Jupyter directamente desde el navegador en tu propia computadora. De hecho, tanto Jupyter clásico como Jupyter Hub proporcionan un entorno de desarrollo bastante conveniente con autocompletado, resaltado de código, etc.

Para iniciar Jupyter localmente, ve al directorio del curso y ejecuta:

```bash
jupyter notebook
```
o
```bash
jupyterhub
```
Luego puedes navegar a cualquiera de las carpetas `.ipynb` files, open them and start working.

### Running in container

One alternative to Python installation would be to run the code in container. Since our repository contains special `.devcontainer` que indican cómo construir un contenedor para este repositorio; VS Code te ofrecerá reabrir el código en un contenedor. Esto requerirá la instalación de Docker y también será más complejo, por lo que recomendamos esto a usuarios más experimentados.

## Ejecutando en la Nube

Si no deseas instalar Python localmente y tienes acceso a algunos recursos en la nube, una buena alternativa sería ejecutar el código en la nube. Hay varias formas de hacerlo:

* Usando **[GitHub Codespaces](https://github.com/features/codespaces)**, que es un entorno virtual creado para ti en GitHub, accesible a través de la interfaz del navegador de VS Code. Si tienes acceso a Codespaces, solo necesitas hacer clic en el botón **Code** en el repositorio, iniciar un codespace y comenzar a trabajar en poco tiempo.
* Usando **[Binder](https://mybinder.org/v2/gh/microsoft/ai-for-beginners/HEAD)**. [Binder](https://mybinder.org) es un recurso de computación gratuito proporcionado en la nube para que personas como tú prueben algún código en GitHub. Hay un botón en la página principal para abrir el repositorio en Binder; esto te llevará rápidamente al sitio de Binder, que construirá el contenedor subyacente y comenzará la interfaz web de Jupyter sin problemas.

> **Nota**: Para prevenir el uso indebido, Binder tiene acceso bloqueado a algunos recursos web. Esto puede impedir que parte del código funcione, especialmente el que obtiene modelos y/o conjuntos de datos de Internet público. Es posible que necesites encontrar algunas soluciones alternativas. Además, los recursos de computación proporcionados por Binder son bastante básicos, por lo que el entrenamiento será lento, especialmente en lecciones más complejas más adelante.

## Ejecutando en la Nube con GPU

Algunas de las lecciones posteriores en este plan de estudios se beneficiarían enormemente del soporte de GPU, porque de lo contrario el entrenamiento será dolorosamente lento. Hay algunas opciones que puedes seguir, especialmente si tienes acceso a la nube ya sea a través de [Azure for Students](https://azure.microsoft.com/free/students/?WT.mc_id=academic-77998-cacaste) o a través de tu institución:

* Crea una [Máquina Virtual de Ciencia de Datos](https://docs.microsoft.com/learn/modules/intro-to-azure-data-science-virtual-machine/?WT.mc_id=academic-77998-cacaste) y conéctate a ella a través de Jupyter. Luego puedes clonar el repositorio directamente en la máquina y comenzar a aprender. Las máquinas virtuales de la serie NC tienen soporte para GPU.

> **Nota**: Algunas suscripciones, incluyendo Azure for Students, no proporcionan soporte de GPU por defecto. Es posible que necesites solicitar núcleos de GPU adicionales a través de una solicitud de soporte técnico.

* Crea un [Espacio de Trabajo de Azure Machine Learning](https://azure.microsoft.com/services/machine-learning/?WT.mc_id=academic-77998-cacaste) y luego utiliza la función de Notebook allí. [Este video](https://azure-for-academics.github.io/quickstart/azureml-papers/) muestra cómo clonar un repositorio en un notebook de Azure ML y comenzar a usarlo.

También puedes utilizar Google Colab, que viene con algo de soporte gratuito de GPU, y subir Jupyter Notebooks allí para ejecutarlos uno por uno.

**Descargo de responsabilidad**:  
Este documento ha sido traducido utilizando servicios de traducción automática basados en IA. Aunque nos esforzamos por lograr la precisión, tenga en cuenta que las traducciones automáticas pueden contener errores o inexactitudes. El documento original en su idioma nativo debe considerarse la fuente autorizada. Para información crítica, se recomienda una traducción profesional realizada por humanos. No nos hacemos responsables de malentendidos o interpretaciones erróneas que surjan del uso de esta traducción.