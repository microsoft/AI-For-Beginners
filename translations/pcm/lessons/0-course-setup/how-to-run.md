# How to Run the Code

Dis curriculum get plenti executable examples and labs wey you go like run. To fit do dis, you need beta skill to execute Python code for Jupyter Notebooks wey dem provide as part of dis curriculum. You get plenty ways to run the code:

## Run locally on your computer

To run the code for your computer, you need to get Python installation. One wey we fit recommend na to install **[miniconda](https://conda.io/en/latest/miniconda.html)** - e light well well and e support `conda` package manager for different Python **virtual environments**.

After you don install miniconda, clone the repository and create one virtual environment to use for dis course:

```bash
git clone http://github.com/microsoft/ai-for-beginners
cd ai-for-beginners
conda env create --name ai4beg --file .devcontainer/environment.yml
conda activate ai4beg
```

### Using Visual Studio Code with Python Extension

Dis curriculum better pass if you use am inside [Visual Studio Code](http://code.visualstudio.com/?WT.mc_id=academic-77998-cacaste) with [Python Extension](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-77998-cacaste).

> **Note**: Once you clone and open the directory for VS Code, e go automatically remind you to install Python extensions. You go still need to install miniconda as we describe for top.

> **Note**: If VS Code tell you make you re-open the repository for inside container, you suppose no do am, make you fit use local Python installation.

### Using Jupyter in the Browser

You fit still use Jupyter environment from your browser for your own computer. Both classical Jupyter and JupyterHub dey provide correct development environment with auto-completion, code highlighting, etc.

To start Jupyter locally, waka go the directory wey hold the course, then run:

```bash
jupyter notebook
```
or
```bash
jupyterhub
```
You fit then waka go anybody `.ipynb` files, open dem and start to work.

### Running in container

One other way to still run the code no be to install Python, na to run the code inside container. Because our repository get special `.devcontainer` folder wey talk how to build container for dis repo, VS Code go fit help you re-open the code inside container. Dis one require say you get Docker installed, and e still dey complex pass, so we recommend am only to people wey sabi well well.

## Running in the Cloud

If you no want install Python for your own computer, and you get access to cloud resources - one better way na to run the code for cloud. You get plenty ways to do am:

* Use **[GitHub Codespaces](https://github.com/features/codespaces)**, wey be virtual environment wey dem create for you on top GitHub, and you fit use VS Code browser interface take access am. If you fit use Codespaces, you fit just click **Code** button for the repo, start codespace, and run am sharp sharp.
* Use **[Binder](https://mybinder.org/v2/gh/microsoft/ai-for-beginners/HEAD)**. [Binder](https://mybinder.org) dey offer free computer resources for cloud so people like you fit try run code from GitHub. For the front page, dem get button wey make you fit open the repo for Binder - dis one go take you go the binder site quick, wey go build container and start Jupyter web interface for you without wahala.

> **Note**: To stop misuse, Binder block some web resources. Dis one fit make some code no work, especially if the code dey fetch models and/or datasets from public Internet. You fit need find way workaround. Also, the compute resources wey Binder get, simple, so training go slow, especially for the later, more complex lessons.

## Running in the Cloud with GPU

Some of the later lessons for dis curriculum go beta if dem get GPU support. Model training fit slow no GPU. You fit follow some options if you get cloud access through [Azure for Students](https://azure.microsoft.com/free/students/?WT.mc_id=academic-77998-cacaste), or from your school:

* Create [Data Science Virtual Machine](https://docs.microsoft.com/learn/modules/intro-to-azure-data-science-virtual-machine/?WT.mc_id=academic-77998-cacaste) and connect to am through Jupyter. You fit then clone the repo enter inside the machine, and start to learn. NC-series VMs get GPU support.

> **Note**: Some subscriptions, including Azure for Students, no dey come with GPU support straight. You go need check to add GPU cores with technical support request.

* Create [Azure Machine Learning Workspace](https://azure.microsoft.com/services/machine-learning/?WT.mc_id=academic-77998-cacaste), then use Notebook feature for there. [Dis video](https://azure-for-academics.github.io/quickstart/azureml-papers/) show how to clone repository enter Azure ML notebook and start to use am.

You fit still use Google Colab, wey get some free GPU support, and upload Jupyter Notebooks there take run dem one by one.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Warning**:  
Dis document na translation wey AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator) do. Even though we try make am correct, make you sabi say automated translation fit get some mistakes or wahala. Di original document wey dey dia own language na di correct one. For important matter, e better make professional human person translate am. We no go responsible for any wrong understand or mix-up wey fit happen because of dis translation.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->