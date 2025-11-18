<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "7df19702b8d2d3f7c4238c51bec2c8fc",
  "translation_date": "2025-11-18T18:32:29+00:00",
  "source_file": "lessons/0-course-setup/how-to-run.md",
  "language_code": "pcm"
}
-->
# How to Run di Code

Dis curriculum get plenty examples wey you fit run and labs wey you go wan try. To fit do am, you need di ability to run Python code inside Jupyter Notebooks wey dem provide as part of dis curriculum. You get different ways wey you fit take run di code:

## Run am for your computer

To run di code for your computer, you go need make Python dey installed. I go recommend make you install **[miniconda](https://conda.io/en/latest/miniconda.html)** - e no heavy and e dey support `conda` package manager for different Python **virtual environments**.

After you don install miniconda, you go need clone di repository and create virtual environment wey you go use for dis course:

```bash
git clone http://github.com/microsoft/ai-for-beginners
cd ai-for-beginners
conda env create --name ai4beg --file .devcontainer/environment.yml
conda activate ai4beg
```

### Use Visual Studio Code with Python Extension

Di best way to use dis curriculum na to open am for [Visual Studio Code](http://code.visualstudio.com/?WT.mc_id=academic-77998-cacaste) with [Python Extension](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-77998-cacaste).

> **Note**: Once you don clone and open di directory for VS Code, e go suggest make you install Python extensions. You go also need install miniconda as I don talk before.

> **Note**: If VS Code suggest make you re-open di repository inside container, no gree. Use di local Python installation instead.

### Use Jupyter for Browser

You fit also use Jupyter environment directly from your browser for your computer. Di classical Jupyter and Jupyter Hub dey provide better development environment wey get auto-completion, code highlighting, and di rest.

To start Jupyter locally, go di directory of di course, then run:

```bash
jupyter notebook
```
or
```bash
jupyterhub
```
You fit then navigate go any `.ipynb` file, open am and start work.

### Run am inside container

Another way wey you fit run di code na to use container. Since di repository get special `.devcontainer` folder wey dey show how to build container for di repo, VS Code go suggest make you re-open di code inside container. Dis one go need Docker installation, and e dey more complex, so we dey recommend am for people wey don sabi well.

## Run am for Cloud

If you no wan install Python for your computer, and you get access to cloud resources - one better option na to run di code for cloud. You get different ways wey you fit do am:

* Use **[GitHub Codespaces](https://github.com/features/codespaces)**, wey be virtual environment wey GitHub go create for you, wey you fit access through VS Code browser interface. If you get access to Codespaces, just click **Code** button for di repo, start codespace, and begin dey run am sharp sharp.
* Use **[Binder](https://mybinder.org/v2/gh/microsoft/ai-for-beginners/HEAD)**. [Binder](https://mybinder.org) na free computing resources wey dey cloud for people wey wan test code for GitHub. You go see button for di front page to open di repository for Binder - e go carry you go di Binder site, wey go build di container and start Jupyter web interface for you without wahala.

> **Note**: To stop misuse, Binder dey block access to some web resources. Dis fit make some code wey dey fetch models and/or datasets from public Internet no work. You go need find workaround. Also, di compute resources wey Binder dey provide no too strong, so training go slow, especially for di later lessons wey dey more complex.

## Run am for Cloud with GPU

Some of di later lessons for dis curriculum go need GPU support, because if GPU no dey, training go slow well well. You get some options wey you fit follow, especially if you get access to cloud through [Azure for Students](https://azure.microsoft.com/free/students/?WT.mc_id=academic-77998-cacaste), or through your institution:

* Create [Data Science Virtual Machine](https://docs.microsoft.com/learn/modules/intro-to-azure-data-science-virtual-machine/?WT.mc_id=academic-77998-cacaste) and connect am through Jupyter. You fit then clone di repo directly for di machine, and start dey learn. NC-series VMs get GPU support.

> **Note**: Some subscriptions, including Azure for Students, no dey provide GPU support straight. You fit need request extra GPU cores through technical support.

* Create [Azure Machine Learning Workspace](https://azure.microsoft.com/services/machine-learning/?WT.mc_id=academic-77998-cacaste) and use di Notebook feature wey dey there. [Dis video](https://azure-for-academics.github.io/quickstart/azureml-papers/) dey show how to clone repository into Azure ML notebook and start dey use am.

You fit also use Google Colab, wey dey come with free GPU support, and upload Jupyter Notebooks there to run dem one by one.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:  
Dis dokyument don use AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator) do di translation. Even as we dey try make am accurate, abeg sabi say automated translations fit get mistake or no dey correct well. Di original dokyument for im native language na di main source wey you go fit trust. For important information, e good make professional human translation dey use. We no go fit take blame for any misunderstanding or wrong interpretation wey fit happen because you use dis translation.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->