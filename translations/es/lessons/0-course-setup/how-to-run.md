# Cómo Ejecutar el Código

Este plan de estudios contiene muchos ejemplos ejecutables y laboratorios que querrás ejecutar. Para ello, necesitas la capacidad de ejecutar código Python en Jupyter Notebooks proporcionados como parte de este plan de estudios. Tienes varias opciones para ejecutar el código:

## Ejecutar localmente en tu computadora

Para ejecutar el código localmente en tu computadora, es necesaria una instalación de Python. Una recomendación es instalar **[miniconda](https://conda.io/en/latest/miniconda.html)**, que es una instalación relativamente ligera que soporta el gestor de paquetes `conda` para diferentes **entornos virtuales** de Python.

Después de instalar miniconda, clona el repositorio y crea un entorno virtual para usar en este curso:

```bash
git clone http://github.com/microsoft/ai-for-beginners
cd ai-for-beginners
conda env create --name ai4beg --file .devcontainer/environment.yml
conda activate ai4beg
```

> **Nota para Windows**: Si la creación del entorno falla mientras instalas `gdk-pixbuf` con un `UnicodeDecodeError` que menciona el códec `gbk`, habilita el modo UTF-8 de Python en tu terminal y reintenta. Usa la sintaxis correspondiente para la terminal que estés usando:
>
> **PowerShell:**
>
> ```powershell
> $env:PYTHONUTF8 = "1"
> conda env create --name ai4beg --file .devcontainer/environment.yml
> ```
>
> **Command Prompt (`cmd.exe`) o Anaconda Prompt:**
>
> ```cmd
> set PYTHONUTF8=1
> conda env create --name ai4beg --file .devcontainer/environment.yml
> ```
>
> **Bash, incluido Git Bash:**
>
> ```bash
> export PYTHONUTF8=1
> conda env create --name ai4beg --file .devcontainer/environment.yml
> ```
>
> Si un intento fallido dejó el entorno `ai4beg` activo, desactívalo y elimina ese entorno antes de reintentar. Usa `conda deactivate` primero cuando un entorno esté activo:
>
> ```text
> conda deactivate
> conda env remove --name ai4beg
> ```

### Uso de Visual Studio Code con la Extensión de Python

Este plan de estudios se usa mejor abriéndolo en [Visual Studio Code](http://code.visualstudio.com/?WT.mc_id=academic-77998-cacaste) con la [Extensión de Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-77998-cacaste).

> **Nota**: Una vez que clones y abras el directorio en VS Code, automáticamente te sugerirá instalar las extensiones de Python. También tendrás que instalar miniconda como se describió arriba.

> **Nota**: Si VS Code te sugiere reabrir el repositorio en un contenedor, debes rechazar esta opción para usar la instalación local de Python.

### Uso de Jupyter en el Navegador

También puedes usar un entorno Jupyter desde el navegador en tu propia computadora. Tanto Jupyter clásico como JupyterHub ofrecen un entorno de desarrollo conveniente con autocompletado, resaltado de código, etc.

Para iniciar Jupyter localmente, ve al directorio del curso y ejecuta:

```bash
jupyter notebook
```
o
```bash
jupyterhub
```
Luego puedes navegar a cualquiera de los archivos `.ipynb`, abrirlos y empezar a trabajar.

### Ejecutar en un contenedor

Una alternativa a la instalación de Python es ejecutar el código en un contenedor. Dado que nuestro repositorio incluye una carpeta especial `.devcontainer` que indica cómo construir un contenedor para este repositorio, VS Code ofrece la posibilidad de reabrir el código en un contenedor. Esto requerirá la instalación de Docker y será más complejo, por lo que recomendamos esta opción para usuarios con más experiencia.

## Ejecutar en la Nube

Si no quieres instalar Python localmente y tienes acceso a algunos recursos en la nube, una buena alternativa es ejecutar el código en la nube. Hay varias formas de hacer esto:

* Usando **[GitHub Codespaces](https://github.com/features/codespaces)**, que es un entorno virtual creado para ti en GitHub, accesible a través de una interfaz de navegador de VS Code. Si tienes acceso a Codespaces, solo tienes que hacer clic en el botón **Code** en el repositorio, iniciar un codespace y ponerte en marcha rápidamente.
* Usando **[Binder](https://mybinder.org/v2/gh/microsoft/ai-for-beginners/HEAD)**. [Binder](https://mybinder.org) ofrece recursos informáticos gratuitos en la nube para que personas como tú prueben código en GitHub. Hay un botón en la página principal para abrir el repositorio en Binder; esto debería llevarte rápidamente al sitio de Binder, que construirá un contenedor subyacente e iniciará una interfaz web de Jupyter para ti sin problemas.

> **Nota**: Para evitar abusos, Binder bloquea el acceso a algunos recursos web. Esto puede impedir que parte del código funcione, especialmente el que descarga modelos y/o conjuntos de datos desde Internet público. Quizás necesites encontrar algunas soluciones alternativas. Además, los recursos de cómputo proporcionados por Binder son bastante básicos, por lo que el entrenamiento será lento, especialmente en lecciones posteriores más complejas.

## Ejecutar en la Nube con GPU

Algunas de las lecciones más avanzadas en este plan de estudios se beneficiarían enormemente del soporte GPU. El entrenamiento de modelos, por ejemplo, puede ser muy lento sin GPU. Hay algunas opciones que puedes seguir, especialmente si tienes acceso a la nube a través de [Azure para Estudiantes](https://azure.microsoft.com/free/students/?WT.mc_id=academic-77998-cacaste) o mediante tu institución:

* Crear una [Máquina Virtual de Ciencia de Datos](https://docs.microsoft.com/learn/modules/intro-to-azure-data-science-virtual-machine/?WT.mc_id=academic-77998-cacaste) y conectarte a ella mediante Jupyter. Puedes entonces clonar el repositorio directamente en la máquina y comenzar a aprender. Las máquinas virtuales de la serie NC tienen soporte GPU.

> **Nota**: Algunas suscripciones, incluyendo Azure para Estudiantes, no proporcionan soporte GPU por defecto. Es posible que necesites solicitar núcleos GPU adicionales mediante una petición de soporte técnico.

* Crear un [Espacio de Trabajo de Azure Machine Learning](https://azure.microsoft.com/services/machine-learning/?WT.mc_id=academic-77998-cacaste) y luego usar la función Notebook allí. [Este video](https://azure-for-academics.github.io/quickstart/azureml-papers/) muestra cómo clonar un repositorio en un notebook de Azure ML y empezar a usarlo.

También puedes usar Google Colab, que incluye algo de soporte GPU gratuito, y subir los Jupyter Notebooks para ejecutarlos uno por uno.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Descargo de responsabilidad**:
Este documento ha sido traducido utilizando el servicio de traducción automática [Co-op Translator](https://github.com/Azure/co-op-translator). Aunque nos esforzamos por la precisión, tenga en cuenta que las traducciones automatizadas pueden contener errores o inexactitudes. El documento original en su idioma nativo debe considerarse la fuente autorizada. Para información crítica, se recomienda una traducción profesional humana. No somos responsables de cualquier malentendido o interpretación errónea que surja del uso de esta traducción.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->