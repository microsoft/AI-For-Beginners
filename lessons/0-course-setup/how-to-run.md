# How to Run the Code

This curriculum contains a lot of executable examples and labs that you would want to run. In order to do this, you need the ability to execute Python code in Jupyter Notebooks provided as part of this curriculum. You have several options for running the code:

## Run locally on your computer

To run the code locally on your computer, a Python installation is needed. One recommendation is to install **[miniconda](https://conda.io/en/latest/miniconda.html)** - it is a rather lightweight installation that supports the `conda` package manager for different Python **virtual environments**.

After you install miniconda, clone the repository and create a virtual environment to be used for this course:

```bash
git clone http://github.com/microsoft/ai-for-beginners
cd ai-for-beginners
conda env create --name ai4beg --file .devcontainer/environment.yml
conda activate ai4beg
```

### Using Visual Studio Code with Python Extension

This curriculum is best used when opening it in [Visual Studio Code](http://code.visualstudio.com/?WT.mc_id=academic-77998-cacaste) with [Python Extension](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-77998-cacaste).

> **Note**: Once you clone and open the directory in VS Code, it will automatically suggest you to install Python extensions. You would also have to install miniconda as described above.

> **Note**: If VS Code suggests to you to re-open the repository in a container, you should decline this to use the local Python installation. 

### Using Jupyter in the Browser

You can also use a Jupyter environment from the browser on your own computer. Both classical Jupyter and JupyerHub provides a convenient development environment with auto-completion, code highlighting, etc.

To start Jupyter locally, go to the directory of the course, and execute:

```bash
jupyter notebook
```
or
```bash
jupyterhub
```
You then can navigate to any of the `.ipynb` files, open them and start working.

### Running in container

One alternative to Python installation would be to run the code in a container. Since our repository supplies a special `.devcontainer` folder that instructs how to build a container for this repo, VS Code offers the opportunity to re-open the code in a container. This will require Docker installation, and also would be more complex, so we recommend this to more experienced users.

## Running in the Cloud

If you do not want to install Python locally, and have access to some cloud resources - a good alternative would be to run the code in the cloud. There are several ways you can do this:

* Using **[GitHub Codespaces](https://github.com/features/codespaces)**, which is a virtual environment created for you on GitHub, accessible through a VS Code browser interface. If you have access to Codespaces, you can just click the **Code** button in the repo, start a codespace, and get running in no time.
* Using **[Binder](https://mybinder.org/v2/gh/microsoft/ai-for-beginners/HEAD)**. [Binder](https://mybinder.org) offers free computing resources provided in the cloud for people like you to test out some code on GitHub. There is a button at the front page to open the repository in Binder - this should quickly take you to the binder site, which will build an underlying container and start a Jupyter web interface for you seamlessly.

> **Note**: To prevent misuse, Binder has access to some web resources blocked. This may prevent some of the code from working, which fetches models and/or datasets from the public Internet. You may need to find some workarounds. Also, compute resources provided by Binder are pretty basic, so training will be slow, especially in later, more complex lessons.

## Running in the Cloud with GPU

Some of the later lessons in this curriculum would greatly benefit from GPU support. Model training, for instance, can be painfully slow otherwise. There are a few options you can follow, especially if you have access to the cloud either through [Azure for Students](https://azure.microsoft.com/free/students/?WT.mc_id=academic-77998-cacaste), or through your institution:

* Create [Data Science Virtual Machine](https://docs.microsoft.com/learn/modules/intro-to-azure-data-science-virtual-machine/?WT.mc_id=academic-77998-cacaste) and connect to it through Jupyter. You can then clone the repo right onto the machine, and start learning. NC-series VMs have GPU support.

> **Note**: Some subscriptions, including Azure for Students, do not provide GPU support out of the box. You may need to request additional GPU cores with a technical support request.

* Create [Azure Machine Learning Workspace](https://azure.microsoft.com/services/machine-learning/?WT.mc_id=academic-77998-cacaste) and then use the Notebook feature there. [This video](https://azure-for-academics.github.io/quickstart/azureml-papers/) shows how to clone a repository into Azure ML notebook and start using it.

You can also use Google Colab, which comes with some free GPU support, and upload Jupyter Notebooks there to execute them one-by-one.
