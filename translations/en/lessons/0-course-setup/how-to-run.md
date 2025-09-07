<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "7df19702b8d2d3f7c4238c51bec2c8fc",
  "translation_date": "2025-08-31T17:33:44+00:00",
  "source_file": "lessons/0-course-setup/how-to-run.md",
  "language_code": "en"
}
-->
# How to Run the Code

This curriculum includes many executable examples and labs that you may want to run. To do this, you need the ability to execute Python code in Jupyter Notebooks provided as part of this curriculum. Here are several options for running the code:

## Run locally on your computer

To run the code locally on your computer, you need to have some version of Python installed. I personally recommend installing **[miniconda](https://conda.io/en/latest/miniconda.html)**—a lightweight installation that supports the `conda` package manager for different Python **virtual environments**.

After installing miniconda, you need to clone the repository and create a virtual environment for this course:

```bash
git clone http://github.com/microsoft/ai-for-beginners
cd ai-for-beginners
conda env create --name ai4beg --file .devcontainer/environment.yml
conda activate ai4beg
```

### Using Visual Studio Code with Python Extension

One of the best ways to use the curriculum is to open it in [Visual Studio Code](http://code.visualstudio.com/?WT.mc_id=academic-77998-cacaste) with the [Python Extension](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-77998-cacaste).

> **Note**: Once you clone and open the directory in VS Code, it will automatically suggest installing Python extensions. You will also need to install miniconda as described above.

> **Note**: If VS Code suggests reopening the repository in a container, decline this to use the local Python installation.

### Using Jupyter in the Browser

You can also use the Jupyter environment directly from your browser on your own computer. Both classical Jupyter and Jupyter Hub provide a convenient development environment with features like auto-completion and code highlighting.

To start Jupyter locally, navigate to the course directory and execute:

```bash
jupyter notebook
```  
or  
```bash
jupyterhub
```  

You can then navigate to any of the `.ipynb` files, open them, and start working.

### Running in a container

Another option for running the code is to use a container. Since our repository includes a special `.devcontainer` folder that specifies how to build a container for this repo, VS Code will offer to reopen the code in a container. This requires Docker installation and is more complex, so we recommend it for more experienced users.

## Running in the Cloud

If you prefer not to install Python locally and have access to cloud resources, running the code in the cloud is a good alternative. Here are a few options:

* Use **[GitHub Codespaces](https://github.com/features/codespaces)**, a virtual environment created for you on GitHub, accessible through the VS Code browser interface. If you have access to Codespaces, simply click the **Code** button in the repo, start a codespace, and get started quickly.
* Use **[Binder](https://mybinder.org/v2/gh/microsoft/ai-for-beginners/HEAD)**. [Binder](https://mybinder.org) provides free cloud computing resources for testing code on GitHub. There’s a button on the repository’s front page to open it in Binder. This will take you to the Binder site, which will build the underlying container and seamlessly start the Jupyter web interface.

> **Note**: To prevent misuse, Binder blocks access to some web resources. This may cause issues with code that fetches models or datasets from the public Internet. You may need to find workarounds. Additionally, Binder’s compute resources are basic, so training will be slow, especially in later, more complex lessons.

## Running in the Cloud with GPU

Some of the later lessons in this curriculum will benefit greatly from GPU support, as training without it can be very slow. Here are a few options, especially if you have access to the cloud through [Azure for Students](https://azure.microsoft.com/free/students/?WT.mc_id=academic-77998-cacaste) or your institution:

* Create a [Data Science Virtual Machine](https://docs.microsoft.com/learn/modules/intro-to-azure-data-science-virtual-machine/?WT.mc_id=academic-77998-cacaste) and connect to it via Jupyter. You can clone the repository directly onto the machine and start learning. NC-series VMs include GPU support.

> **Note**: Some subscriptions, including Azure for Students, do not provide GPU support by default. You may need to request additional GPU cores through a technical support request.

* Create an [Azure Machine Learning Workspace](https://azure.microsoft.com/services/machine-learning/?WT.mc_id=academic-77998-cacaste) and use the Notebook feature there. [This video](https://azure-for-academics.github.io/quickstart/azureml-papers/) demonstrates how to clone a repository into an Azure ML notebook and start using it.

You can also use Google Colab, which offers some free GPU support. Simply upload the Jupyter Notebooks there and execute them one by one.

---

**Disclaimer**:  
This document has been translated using the AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). While we aim for accuracy, please note that automated translations may include errors or inaccuracies. The original document in its native language should be regarded as the authoritative source. For critical information, professional human translation is advised. We are not responsible for any misunderstandings or misinterpretations resulting from the use of this translation.