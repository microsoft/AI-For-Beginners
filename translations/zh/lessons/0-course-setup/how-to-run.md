# 如何运行代码

本课程包含许多可执行的示例和实验室，您可能希望运行这些示例。为了做到这一点，您需要能够在本课程提供的 Jupyter Notebooks 中执行 Python 代码。您有几种运行代码的选项：

## 在本地计算机上运行

要在本地计算机上运行代码，您需要安装某个版本的 Python。我个人推荐安装 **[miniconda](https://conda.io/en/latest/miniconda.html)** - 这是一个相对轻量的安装，它支持 `conda` 包管理器，用于不同的 Python **虚拟环境**。

安装完 miniconda 后，您需要克隆该代码库并创建一个用于本课程的虚拟环境：

```bash
git clone http://github.com/microsoft/ai-for-beginners
cd ai-for-beginners
conda env create --name ai4beg --file .devcontainer/environment.yml
conda activate ai4beg
```

### 使用带有 Python 扩展的 Visual Studio Code

使用本课程的最佳方式可能是通过带有 [Python Extension](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-77998-cacaste) 的 [Visual Studio Code](http://code.visualstudio.com/?WT.mc_id=academic-77998-cacaste) 打开它。

> **注意**：一旦您克隆并在 VS Code 中打开目录，它会自动建议您安装 Python 扩展。您还需要按照上述说明安装 miniconda。

> **注意**：如果 VS Code 建议您在容器中重新打开代码库，您需要拒绝此请求，以使用本地 Python 安装。

### 在浏览器中使用 Jupyter

您还可以直接在自己计算机的浏览器中使用 Jupyter 环境。实际上，经典 Jupyter 和 Jupyter Hub 都提供了相当方便的开发环境，具有自动补全、代码高亮等功能。

要在本地启动 Jupyter，请进入课程目录，并执行：

```bash
jupyter notebook
```
或
```bash
jupyterhub
```
然后您可以导航到任何 `.ipynb` files, open them and start working.

### Running in container

One alternative to Python installation would be to run the code in container. Since our repository contains special `.devcontainer` 文件夹，该文件夹指示如何为该代码库构建容器，VS Code 会建议您在容器中重新打开代码。这将需要 Docker 安装，并且会更复杂，因此我们建议更有经验的用户使用此选项。

## 在云中运行

如果您不想在本地安装 Python，并且可以访问一些云资源 - 一个不错的替代方案是通过云运行代码。您可以通过几种方式做到这一点：

* 使用 **[GitHub Codespaces](https://github.com/features/codespaces)**，这是在 GitHub 上为您创建的虚拟环境，可以通过 VS Code 浏览器界面访问。如果您可以访问 Codespaces，您只需点击代码库中的 **Code** 按钮，启动一个代码空间，几乎可以立即开始运行。
* 使用 **[Binder](https://mybinder.org/v2/gh/microsoft/ai-for-beginners/HEAD)**。 [Binder](https://mybinder.org) 是为像您这样的人在云中提供的免费计算资源，以测试 GitHub 上的一些代码。主页上有一个按钮可以在 Binder 中打开代码库 - 这应该会快速将您带到 Binder 网站，Binder 会构建底层容器并无缝启动 Jupyter Web 界面。

> **注意**：为了防止滥用，Binder 阻止访问某些网络资源。这可能会导致某些代码无法正常工作，特别是那些从公共互联网获取模型和/或数据集的代码。您可能需要寻找一些解决方法。此外，Binder 提供的计算资源相当基础，因此训练将会很慢，尤其是在后面的更复杂的课程中。

## 在云中使用 GPU 运行

本课程中的一些后续课程将极大受益于 GPU 支持，否则训练将会非常缓慢。您可以遵循以下几种选择，特别是如果您可以通过 [Azure for Students](https://azure.microsoft.com/free/students/?WT.mc_id=academic-77998-cacaste) 或通过您的机构访问云：

* 创建 [Data Science Virtual Machine](https://docs.microsoft.com/learn/modules/intro-to-azure-data-science-virtual-machine/?WT.mc_id=academic-77998-cacaste) 并通过 Jupyter 连接到它。然后，您可以直接将代码库克隆到该机器上，开始学习。NC 系列虚拟机支持 GPU。

> **注意**：某些订阅，包括 Azure for Students，并不默认提供 GPU 支持。您可能需要通过技术支持请求额外的 GPU 核心。

* 创建 [Azure Machine Learning Workspace](https://azure.microsoft.com/services/machine-learning/?WT.mc_id=academic-77998-cacaste)，然后在其中使用 Notebook 功能。 [此视频](https://azure-for-academics.github.io/quickstart/azureml-papers/) 展示了如何将代码库克隆到 Azure ML notebook 中并开始使用。

您还可以使用 Google Colab，它提供了一些免费的 GPU 支持，并可以在其中上传 Jupyter Notebooks，逐个执行它们。

**免责声明**：  
本文件是使用机器翻译的人工智能翻译服务进行翻译的。虽然我们努力追求准确性，但请注意，自动翻译可能包含错误或不准确之处。原始文件的母语版本应被视为权威来源。对于重要信息，建议进行专业人工翻译。我们对因使用本翻译而产生的任何误解或误读不承担责任。