# How to Run di Code

Dis curriculum get plenti executable examples and labs wey you go wan run. To fit do dis, you need di ability to run Python code for Jupyter Notebooks wey dem provide as part of dis curriculum. You get plenti ways to run di code:

## Run am for your computer

To run di code for your computer, you need Python installation. One recommendation na to install **[miniconda](https://conda.io/en/latest/miniconda.html)** - e be lightweight installation wey support di `conda` package manager for different Python **virtual environments**.

After you install miniconda, clone di repository and create virtual environment wey you go use for dis course:

```bash
git clone http://github.com/microsoft/ai-for-beginners
cd ai-for-beginners
conda env create --name ai4beg --file .devcontainer/environment.yml
conda activate ai4beg
```

> **Windows note**: If environment creation no work well while you dey install `gdk-pixbuf` and you see `UnicodeDecodeError` wey talk about `gbk` codec, make you enable Python UTF-8 mode for your terminal and try again. Use di syntax for your terminal:
>
> **PowerShell:**
>
> ```powershell
> $env:PYTHONUTF8 = "1"
> conda env create --name ai4beg --file .devcontainer/environment.yml
> ```
>
> **Command Prompt (`cmd.exe`) or Anaconda Prompt:**
>
> ```cmd
> set PYTHONUTF8=1
> conda env create --name ai4beg --file .devcontainer/environment.yml
> ```
>
> **Bash, including Git Bash:**
>
> ```bash
> export PYTHONUTF8=1
> conda env create --name ai4beg --file .devcontainer/environment.yml
> ```
>
> If your first try fail and `ai4beg` environment still dey, deactivate am and remove before you try again. Use `conda deactivate` first if environment dey active:
>
> ```text
> conda deactivate
> conda env remove --name ai4beg
> ```

### How to use Visual Studio Code with Python Extension

Dis curriculum best if you open am for [Visual Studio Code](http://code.visualstudio.com/?WT.mc_id=academic-77998-cacaste) with [Python Extension](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-77998-cacaste).

> **Note**: Once you clone and open di directory for VS Code, e go suggest make you install Python extensions. You go still need install miniconda like we talk before.

> **Note**: If VS Code suggest say make you re-open di repo inside container, you suppose say no for dat and use the local Python installation. 

### How to use Jupyter for Browser

You fit still use Jupyter environment from your browser for your own PC. Both classical Jupyter and JupyterHub dey give better development environment with auto-completion, code highlight, and more.

To start Jupyter locally, waka go di course directory, then run:

```bash
jupyter notebook
```
or
```bash
jupyterhub
```
Then you fit waka enter any `.ipynb` files, open dem and start work.

### Run am for container

One other way to run code instead of Python install na to run am for container. Since our repo get special `.devcontainer` folder wey talk how to build container for dis repo, VS Code get option for you to re-open di code inside container. Dis one need Docker installation, e go complex small, so na for those wey sabi well.

## Run for Cloud

If you no wan install Python for your computer and you get some cloud resources, one better way na to run di code for cloud. You fit do am for plenti ways:

* Use **[GitHub Codespaces](https://github.com/features/codespaces)**, na virtual environment dem create for you on GitHub, wey you fit access through VS Code browser. If you get Codespaces, you fit just click **Code** button for repo, start codespace, and begin run quick quick.
* Use **[Binder](https://mybinder.org/v2/gh/microsoft/ai-for-beginners/HEAD)**. [Binder](https://mybinder.org) dey provide free cloud computing resources for people like you to test code wey dey GitHub. Dem get button for front page to open repo for Binder - e go quick take you go binder site wey go build the container underneath and start Jupyter web interface smoothly.

> **Note**: To prevent misuse, Binder block some web resources. Dis fit stop some code wey dey fetch models or datasets from public Internet from working. You fit need find workarounds. Also, di compute resources wey Binder provide basic bare, so training go slow, especially for later complex lessons.

## Run for Cloud with GPU

Some later lessons for dis curriculum go benefit well well from GPU support. Model training fit slow die if no GPU. You fit follow some options if you get cloud access through [Azure for Students](https://azure.microsoft.com/free/students/?WT.mc_id=academic-77998-cacaste), or through your institution:

* Create [Data Science Virtual Machine](https://docs.microsoft.com/learn/modules/intro-to-azure-data-science-virtual-machine/?WT.mc_id=academic-77998-cacaste) and connect through Jupyter. You fit clone di repo right for di machine and start to learn. NC-series VMs get GPU support.

> **Note**: Some subscriptions, like Azure for Students, no carry GPU support automatically. You fit need request extra GPU cores wit technical support.

* Create [Azure Machine Learning Workspace](https://azure.microsoft.com/services/machine-learning/?WT.mc_id=academic-77998-cacaste) and use Notebook feature. [Dis video](https://azure-for-academics.github.io/quickstart/azureml-papers/) show how to clone repo into Azure ML notebook and start to use am.

You fit also use Google Colab, wey get some free GPU support, and upload Jupyter Notebooks there to run dem one by one.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Dis document don translate wit AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). Even tho we dey try make am correct, abeg make you know say automated translation fit get errors or mistakes. Di original document for dia own language na im be di correct source. For important info, make person wey sabi human translation do am. We no go responsible for any misunderstanding or wrong understanding wey fit happen because of dis translation.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->