# Cómo Ejecutar el Código

Este plan de estudios contiene muchos ejemplos ejecutables y laboratorios que querrás ejecutar. Para hacerlo, necesitas la capacidad de ejecutar código Python en los Jupyter Notebooks proporcionados como parte de este plan de estudios. Tienes varias opciones para ejecutar el código:

## Ejecutar localmente en tu computadora

Para ejecutar el código localmente en tu computadora, se necesita una instalación de Python. Una recomendación es instalar **[miniconda](https://conda.io/en/latest/miniconda.html)**: es una instalación bastante ligera que soporta el gestor de paquetes `conda` para diferentes **entornos virtuales** de Python.

Después de instalar miniconda, clona el repositorio y crea un entorno virtual que será usado para este curso:

```bash
git clone http://github.com/microsoft/ai-for-beginners
cd ai-for-beginners
conda env create --name ai4beg --file .devcontainer/environment.yml
conda activate ai4beg
```

### Usando Visual Studio Code con la Extensión de Python

Este plan de estudios se usa mejor cuando se abre en [Visual Studio Code](http://code.visualstudio.com/?WT.mc_id=academic-77998-cacaste) con la [Extensión de Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-77998-cacaste).

> **Nota**: Una vez que clones y abras el directorio en VS Code, automáticamente te sugerirá instalar las extensiones de Python. También tendrás que instalar miniconda como se describió arriba.

> **Nota**: Si VS Code te sugiere volver a abrir el repositorio en un contenedor, deberías rechazar esto para usar la instalación local de Python.

### Usando Jupyter en el Navegador

También puedes usar un entorno Jupyter desde el navegador en tu propia computadora. Tanto Jupyter clásico como JupyterHub proveen un entorno de desarrollo conveniente con autocompletado, resaltado de código, etc.

Para iniciar Jupyter localmente, ve al directorio del curso, y ejecuta:

```bash
jupyter notebook
```
o
```bash
jupyterhub
```
Luego puedes navegar a cualquiera de los archivos `.ipynb`, abrirlos y comenzar a trabajar.

### Ejecutando en un contenedor

Una alternativa a la instalación de Python sería ejecutar el código en un contenedor. Debido a que nuestro repositorio proporciona una carpeta especial `.devcontainer` que indica cómo construir un contenedor para este repositorio, VS Code ofrece la opción de volver a abrir el código en un contenedor. Esto requerirá la instalación de Docker y además sería más complejo, por lo que recomendamos esto a usuarios con más experiencia.

## Ejecutar en la Nube

Si no quieres instalar Python localmente y tienes acceso a algunos recursos en la nube, una buena alternativa sería ejecutar el código en la nube. Hay varias maneras de hacerlo:

* Usando **[GitHub Codespaces](https://github.com/features/codespaces)**, que es un entorno virtual creado para ti en GitHub, accesible a través de una interfaz de navegador de VS Code. Si tienes acceso a Codespaces, solo tienes que hacer clic en el botón **Code** en el repositorio, iniciar un codespace y comenzar a trabajar en muy poco tiempo.
* Usando **[Binder](https://mybinder.org/v2/gh/microsoft/ai-for-beginners/HEAD)**. [Binder](https://mybinder.org) ofrece recursos de cómputo gratuitos proporcionados en la nube para personas como tú que quieren probar código en GitHub. Hay un botón en la página principal para abrir el repositorio en Binder; esto debería llevarte rápidamente al sitio de Binder, que construirá un contenedor subyacente e iniciará una interfaz web de Jupyter para ti sin inconvenientes.

> **Nota**: Para prevenir uso indebido, Binder tiene acceso bloqueado a algunos recursos web. Esto puede prevenir que parte del código funcione si descarga modelos y/o conjuntos de datos de Internet público. Puede que necesites encontrar algunas soluciones alternativas. Además, los recursos de cómputo proporcionados por Binder son bastante básicos, por lo que el entrenamiento será lento, especialmente en lecciones posteriores y más complejas.

## Ejecutar en la Nube con GPU

Algunas de las lecciones posteriores en este plan de estudios se beneficiarían mucho del soporte de GPU. El entrenamiento de modelos, por ejemplo, puede ser dolorosamente lento de otra forma. Hay algunas opciones que puedes seguir, especialmente si tienes acceso a la nube ya sea mediante [Azure para Estudiantes](https://azure.microsoft.com/free/students/?WT.mc_id=academic-77998-cacaste) o a través de tu institución:

* Crear una [Máquina Virtual para Ciencia de Datos](https://docs.microsoft.com/learn/modules/intro-to-azure-data-science-virtual-machine/?WT.mc_id=academic-77998-cacaste) y conectarte a ella mediante Jupyter. Luego puedes clonar el repositorio directamente en la máquina y comenzar a aprender. Las máquinas virtuales de la serie NC tienen soporte para GPU.

> **Nota**: Algunas suscripciones, incluidas Azure para Estudiantes, no proporcionan soporte para GPU por defecto. Puede que necesites solicitar núcleos GPU adicionales mediante una solicitud de soporte técnico.

* Crear un [Espacio de Trabajo Azure Machine Learning](https://azure.microsoft.com/services/machine-learning/?WT.mc_id=academic-77998-cacaste) y luego usar la función de Notebook allí. [Este video](https://azure-for-academics.github.io/quickstart/azureml-papers/) muestra cómo clonar un repositorio en un notebook de Azure ML y comenzar a usarlo.

También puedes usar Google Colab, que viene con soporte gratuito de GPU y subir allí Jupyter Notebooks para ejecutarlos uno por uno.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Aviso legal**:  
Este documento ha sido traducido utilizando el servicio de traducción automática [Co-op Translator](https://github.com/Azure/co-op-translator). Aunque nos esforzamos por la precisión, tenga en cuenta que las traducciones automatizadas pueden contener errores o inexactitudes. El documento original en su idioma nativo debe considerarse la fuente autorizada. Para información crítica, se recomienda una traducción profesional humana. No nos hacemos responsables por malentendidos o interpretaciones erróneas derivadas del uso de esta traducción.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->