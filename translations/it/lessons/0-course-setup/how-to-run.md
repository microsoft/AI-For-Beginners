# Cómo Ejecutar el Código

Este currículo contiene muchos ejemplos ejecutables y laboratorios que querrás ejecutar. Para hacer esto, necesitas la capacidad de ejecutar código Python en Jupyter Notebooks que se proporcionan como parte de este currículo. Tienes varias opciones para ejecutar el código:

## Ejecutar localmente en tu computadora

Para ejecutar el código localmente en tu computadora, necesitarás tener instalada alguna versión de Python. Personalmente, recomiendo instalar **[miniconda](https://conda.io/en/latest/miniconda.html)**, ya que es una instalación bastante ligera que soporta el administrador de paquetes `conda` para diferentes **entornos virtuales** de Python.

Después de instalar miniconda, necesitarás clonar el repositorio y crear un entorno virtual que se utilizará para este curso:

```bash
git clone http://github.com/microsoft/ai-for-beginners
cd ai-for-beginners
conda env create --name ai4beg --file .devcontainer/environment.yml
conda activate ai4beg
```

### Usando Visual Studio Code con la Extensión de Python

Probablemente la mejor manera de utilizar el currículo es abrirlo en [Visual Studio Code](http://code.visualstudio.com/?WT.mc_id=academic-77998-cacaste) con la [Extensión de Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-77998-cacaste).

> **Nota**: Una vez que clones y abras el directorio en VS Code, te sugerirá automáticamente que instales las extensiones de Python. También tendrás que instalar miniconda como se describió anteriormente.

> **Nota**: Si VS Code te sugiere reabrir el repositorio en un contenedor, debes rechazar esto para usar la instalación local de Python.

### Usando Jupyter en el Navegador

También puedes utilizar el entorno Jupyter directamente desde el navegador en tu propia computadora. De hecho, tanto Jupyter clásico como Jupyter Hub ofrecen un entorno de desarrollo bastante conveniente con autocompletado, resaltado de código, etc.

Para iniciar Jupyter localmente, ve al directorio del curso y ejecuta:

```bash
jupyter notebook
```
o
```bash
jupyterhub
```
Luego podrás navegar a cualquiera de las carpetas `.ipynb` files, open them and start working.

### Running in container

One alternative to Python installation would be to run the code in container. Since our repository contains special `.devcontainer` que indican cómo construir un contenedor para este repositorio; VS Code te ofrecerá reabrir el código en el contenedor. Esto requerirá la instalación de Docker y será más complejo, por lo que lo recomendamos para usuarios más experimentados.

## Ejecución en la Nube

Si no deseas instalar Python localmente y tienes acceso a algunos recursos en la nube, una buena alternativa sería ejecutar el código en la nube. Hay varias maneras de hacerlo:

* Usando **[GitHub Codespaces](https://github.com/features/codespaces)**, que es un entorno virtual creado para ti en GitHub, accesible a través de la interfaz del navegador de VS Code. Si tienes acceso a Codespaces, solo tienes que hacer clic en el botón **Code** en el repositorio, iniciar un codespace y comenzar a trabajar en poco tiempo.
* Usando **[Binder](https://mybinder.org/v2/gh/microsoft/ai-for-beginners/HEAD)**. [Binder](https://mybinder.org) es un recurso de computación gratuito proporcionado en la nube para personas como tú que desean probar algún código en GitHub. Hay un botón en la página principal para abrir el repositorio en Binder; esto debería llevarte rápidamente al sitio de binder, que construirá el contenedor subyacente y comenzará la interfaz web de Jupyter para ti sin problemas.

> **Nota**: Para prevenir el uso indebido, Binder tiene bloqueado el acceso a algunos recursos web. Esto puede impedir que parte del código funcione, especialmente si intenta obtener modelos y/o conjuntos de datos de Internet público. Puede que necesites encontrar algunas soluciones alternativas. Además, los recursos de computación proporcionados por Binder son bastante básicos, por lo que el entrenamiento será lento, especialmente en lecciones más complejas más adelante.

## Ejecución en la Nube con GPU

Algunas de las lecciones posteriores en este currículo se beneficiarán enormemente del soporte de GPU, ya que de lo contrario el entrenamiento será dolorosamente lento. Hay algunas opciones que puedes seguir, especialmente si tienes acceso a la nube ya sea a través de [Azure for Students](https://azure.microsoft.com/free/students/?WT.mc_id=academic-77998-cacaste) o a través de tu institución:

* Crea una [Máquina Virtual de Ciencia de Datos](https://docs.microsoft.com/learn/modules/intro-to-azure-data-science-virtual-machine/?WT.mc_id=academic-77998-cacaste) y conéctate a ella a través de Jupyter. Luego puedes clonar el repositorio directamente en la máquina y comenzar a aprender. Las máquinas virtuales de la serie NC tienen soporte para GPU.

> **Nota**: Algunas suscripciones, incluyendo Azure for Students, no proporcionan soporte de GPU de manera predeterminada. Puede que necesites solicitar núcleos de GPU adicionales a través de una solicitud de soporte técnico.

* Crea un [Espacio de Trabajo de Azure Machine Learning](https://azure.microsoft.com/services/machine-learning/?WT.mc_id=academic-77998-cacaste) y luego utiliza la función de Notebook allí. [Este video](https://azure-for-academics.github.io/quickstart/azureml-papers/) muestra cómo clonar un repositorio en un notebook de Azure ML y comenzar a utilizarlo.

También puedes usar Google Colab, que viene con algo de soporte gratuito para GPU, y subir Jupyter Notebooks allí para ejecutarlos uno por uno.

**Disclaimer**:  
Este documento ha sido traducido utilizando servicios de traducción automática basados en inteligencia artificial. Aunque nos esforzamos por la precisión, tenga en cuenta que las traducciones automáticas pueden contener errores o inexactitudes. El documento original en su idioma nativo debe considerarse la fuente autoritativa. Para información crítica, se recomienda la traducción profesional humana. No somos responsables de malentendidos o malas interpretaciones que surjan del uso de esta traducción.