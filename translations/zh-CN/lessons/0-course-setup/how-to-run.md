# 如何运行代码

本课程包含许多可执行的示例和实验，您可能希望运行这些内容。为此，您需要能够在本课程提供的 Jupyter 笔记本中执行 Python 代码。运行代码时，您有以下几种选择：

## 在您电脑上本地运行

要在本地电脑上运行代码，您需要安装 Python。推荐安装 **[miniconda](https://conda.io/en/latest/miniconda.html)** ——这是一种相对轻量级的安装方式，支持不同 Python **虚拟环境** 的 `conda` 包管理器。

安装 miniconda 后，克隆本仓库并创建一个虚拟环境来用于本课程：

```bash
git clone http://github.com/microsoft/ai-for-beginners
cd ai-for-beginners
conda env create --name ai4beg --file .devcontainer/environment.yml
conda activate ai4beg
```

### 使用带 Python 扩展的 Visual Studio Code

本课程建议使用带有 [Python 扩展](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-77998-cacaste) 的 [Visual Studio Code](http://code.visualstudio.com/?WT.mc_id=academic-77998-cacaste) 打开学习。

> **注意**：克隆并在 VS Code 中打开目录后，它会自动建议您安装 Python 扩展。同时您需要按照上述说明安装 miniconda。

> **注意**：如果 VS Code 建议您在容器中重新打开仓库，您应拒绝此操作以使用本地 Python 安装。

### 使用浏览器中的 Jupyter

您也可以在本地电脑的浏览器中使用 Jupyter 环境。无论是经典 Jupyter 还是 JupyterHub，都提供了自动补全、代码高亮等便利的开发环境。

要在本地启动 Jupyter，进入课程目录，然后执行：

```bash
jupyter notebook
```
或
```bash
jupyterhub
```
然后您可以导航到任何 `.ipynb` 文件，打开并开始操作。

### 在容器中运行

另一种替代 Python 安装的方法是运行容器。由于本仓库提供了专门的 `.devcontainer` 文件夹，指导如何为本仓库构建容器，VS Code 支持重新在容器中打开代码。这需要安装 Docker，并且稍微复杂些，因此建议更有经验的用户使用。

## 在云端运行

如果您不想在本地安装 Python，并且可以访问一些云资源，另一个不错的选择是云端运行代码。您可以通过以下几种方式实现：

* 使用 **[GitHub Codespaces](https://github.com/features/codespaces)**，这是 GitHub 为您创建的虚拟环境，可以通过 VS Code 浏览器界面访问。如果您有 Codespaces 权限，只需点击仓库中的 **Code** 按钮，启动 codespace，马上即可运行。
* 使用 **[Binder](https://mybinder.org/v2/gh/microsoft/ai-for-beginners/HEAD)**。[Binder](https://mybinder.org) 提供免费的云计算资源，方便用户在线测试 GitHub 上的代码。主页上有按钮可一键打开仓库到 Binder——您将进入 Binder 网站，它会构建基础容器，并无缝启动 Jupyter 网页界面。

> **注意**：为防止滥用，Binder 屏蔽了部分网络资源访问。这可能导致部分依赖于互联网获取模型和/或数据集的代码无法运行，您可能需要寻找变通方案。此外，Binder 提供的计算资源较为基础，因此训练速度较慢，特别是在后期较复杂的课程中。

## 在带 GPU 的云端运行

本课程后期一些课程如果支持 GPU 会大大加快速度。例如，模型训练在没有 GPU 的情况下会非常缓慢。您可以考虑以下几种方案，尤其是如果您通过 [Azure for Students](https://azure.microsoft.com/free/students/?WT.mc_id=academic-77998-cacaste) 或您的学校具备云资源访问权限：

* 创建 [数据科学虚拟机](https://docs.microsoft.com/learn/modules/intro-to-azure-data-science-virtual-machine/?WT.mc_id=academic-77998-cacaste)，并通过 Jupyter 连接。您可以直接在虚拟机上克隆仓库，开始学习。NC 系列虚拟机支持 GPU。

> **注意**：部分订阅，包括 Azure for Students，开箱即用并不支持 GPU，您可能需要通过技术支持请求申请额外 GPU 核心。

* 创建 [Azure 机器学习工作区](https://azure.microsoft.com/services/machine-learning/?WT.mc_id=academic-77998-cacaste)，并使用其中的 Notebook 功能。[此视频](https://azure-for-academics.github.io/quickstart/azureml-papers/) 展示了如何在 Azure ML Notebook 中克隆仓库并开始使用。

您还可以使用 Google Colab，其免费提供部分 GPU 支持，并上传 Jupyter 笔记本逐个执行。

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免责声明**：  
本文档使用 AI 翻译服务 [Co-op Translator](https://github.com/Azure/co-op-translator) 翻译而成。尽管我们力求准确，但请注意，自动翻译可能包含错误或不准确之处。原始文档的母语版本应被视为权威来源。对于重要信息，建议采用专业人工翻译。我们不对因使用此翻译所引起的任何误解或错误解读承担责任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->