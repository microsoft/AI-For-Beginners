<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "7df19702b8d2d3f7c4238c51bec2c8fc",
  "translation_date": "2025-08-24T20:42:01+00:00",
  "source_file": "lessons/0-course-setup/how-to-run.md",
  "language_code": "zh"
}
-->
# 如何运行代码

本课程包含许多可执行的示例和实验室，您可能希望运行这些代码。为此，您需要能够在本课程提供的 Jupyter Notebooks 中执行 Python 代码。以下是几种运行代码的方式：

## 在本地计算机上运行

要在本地计算机上运行代码，您需要安装某个版本的 Python。我个人推荐安装 **[miniconda](https://conda.io/en/latest/miniconda.html)**——这是一种轻量级的安装方式，支持用于不同 Python **虚拟环境**的 `conda` 包管理器。

安装 miniconda 后，您需要克隆代码库并创建一个用于本课程的虚拟环境：

```bash
git clone http://github.com/microsoft/ai-for-beginners
cd ai-for-beginners
conda env create --name ai4beg --file .devcontainer/environment.yml
conda activate ai4beg
```

### 使用带有 Python 扩展的 Visual Studio Code

使用本课程的最佳方式可能是通过 [Visual Studio Code](http://code.visualstudio.com/?WT.mc_id=academic-77998-cacaste) 和 [Python 扩展](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-77998-cacaste) 打开它。

> **注意**：克隆并在 VS Code 中打开目录后，系统会自动建议您安装 Python 扩展。您还需要按照上述说明安装 miniconda。

> **注意**：如果 VS Code 建议您在容器中重新打开代码库，请拒绝此操作以使用本地 Python 安装。

### 在浏览器中使用 Jupyter

您还可以直接在自己的计算机浏览器中使用 Jupyter 环境。实际上，经典 Jupyter 和 Jupyter Hub 都提供了非常方便的开发环境，包括自动补全、代码高亮等功能。

要在本地启动 Jupyter，请进入课程目录并执行以下命令：

```bash
jupyter notebook
```  
或  
```bash
jupyterhub
```  
然后，您可以导航到任意 `.ipynb` 文件，打开并开始工作。

### 在容器中运行

Python 安装的一个替代方案是使用容器运行代码。由于我们的代码库包含一个特殊的 `.devcontainer` 文件夹，指示如何为此代码库构建容器，VS Code 会提示您在容器中重新打开代码。这需要安装 Docker，并且操作会更复杂，因此我们建议更有经验的用户使用此方法。

## 在云端运行

如果您不想在本地安装 Python，并且可以访问一些云资源，那么在云端运行代码是一个不错的选择。以下是几种方法：

* 使用 **[GitHub Codespaces](https://github.com/features/codespaces)**，这是 GitHub 为您创建的虚拟环境，可通过 VS Code 的浏览器界面访问。如果您有 Codespaces 的访问权限，只需点击代码库中的 **Code** 按钮，启动一个 codespace，即可快速开始运行。
* 使用 **[Binder](https://mybinder.org/v2/gh/microsoft/ai-for-beginners/HEAD)**。 [Binder](https://mybinder.org) 是为像您这样的用户提供的免费云计算资源，用于测试 GitHub 上的代码。在代码库首页有一个按钮可以在 Binder 中打开代码库——这会快速将您带到 Binder 网站，自动构建底层容器并无缝启动 Jupyter 网页界面。

> **注意**：为防止滥用，Binder 对某些网络资源的访问进行了限制。这可能会导致某些代码无法运行，例如从公共互联网获取模型或数据集的代码。您可能需要找到一些替代方法。此外，Binder 提供的计算资源相对基础，因此在后续更复杂的课程中，训练速度会很慢。

## 在云端使用 GPU 运行

本课程的一些后续课程如果有 GPU 支持会受益匪浅，否则训练速度会非常慢。如果您可以通过 [Azure for Students](https://azure.microsoft.com/free/students/?WT.mc_id=academic-77998-cacaste) 或您的机构访问云资源，可以选择以下几种方式：

* 创建 [Data Science Virtual Machine](https://docs.microsoft.com/learn/modules/intro-to-azure-data-science-virtual-machine/?WT.mc_id=academic-77998-cacaste)，并通过 Jupyter 连接到它。然后，您可以直接将代码库克隆到虚拟机上并开始学习。NC 系列虚拟机支持 GPU。

> **注意**：某些订阅（包括 Azure for Students）默认不提供 GPU 支持。您可能需要通过技术支持请求额外的 GPU 核心。

* 创建 [Azure Machine Learning Workspace](https://azure.microsoft.com/services/machine-learning/?WT.mc_id=academic-77998-cacaste)，然后使用其中的 Notebook 功能。[此视频](https://azure-for-academics.github.io/quickstart/azureml-papers/) 展示了如何将代码库克隆到 Azure ML Notebook 并开始使用。

您还可以使用 Google Colab，它提供一些免费的 GPU 支持，并将 Jupyter Notebooks 上传到其中逐一执行。

**免责声明**：  
本文档使用AI翻译服务 [Co-op Translator](https://github.com/Azure/co-op-translator) 进行翻译。尽管我们努力确保翻译的准确性，但请注意，自动翻译可能包含错误或不准确之处。应以原始语言的文档为权威来源。对于关键信息，建议使用专业人工翻译。因使用本翻译而引起的任何误解或误读，我们概不负责。