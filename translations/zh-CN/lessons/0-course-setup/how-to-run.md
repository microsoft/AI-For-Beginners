# 如何运行代码

本课程包含了许多可执行的示例和实验，您可能想运行它们。为此，您需要能够在本课程提供的 Jupyter 笔记本中执行 Python 代码。您有几种运行代码的选择：

## 在本地计算机上运行

要在本地计算机上运行代码，需要安装 Python。推荐安装 **[miniconda](https://conda.io/en/latest/miniconda.html)** —— 这是一个相当轻量的安装，支持 `conda` 包管理器，用于管理不同的 Python <strong>虚拟环境</strong>。

安装 miniconda 后，克隆仓库并创建一个虚拟环境，用于本课程：

```bash
git clone http://github.com/microsoft/ai-for-beginners
cd ai-for-beginners
conda env create --name ai4beg --file .devcontainer/environment.yml
conda activate ai4beg
```

> **Windows 注意事项**：如果在通过 `gdk-pixbuf` 安装 `UnicodeDecodeError` 时，环境创建失败并出现提到 `gbk` 编解码器的错误，请在终端启用 Python 的 UTF-8 模式后重试。请根据所用终端使用相应的语法：
>
> **PowerShell:**
>
> ```powershell
> $env:PYTHONUTF8 = "1"
> conda env create --name ai4beg --file .devcontainer/environment.yml
> ```
>
> **命令提示符 (`cmd.exe`) 或 Anaconda 提示符:**
>
> ```cmd
> set PYTHONUTF8=1
> conda env create --name ai4beg --file .devcontainer/environment.yml
> ```
>
> **Bash，包括 Git Bash:**
>
> ```bash
> export PYTHONUTF8=1
> conda env create --name ai4beg --file .devcontainer/environment.yml
> ```
>
> 如果之前尝试失败导致留下了 `ai4beg` 环境，请先停用该环境并将其删除后再重试。当有环境处于激活状态时，先使用 `conda deactivate`：
>
> ```text
> conda deactivate
> conda env remove --name ai4beg
> ```

### 使用带 Python 扩展的 Visual Studio Code

最佳的使用方式是在 [Visual Studio Code](http://code.visualstudio.com/?WT.mc_id=academic-77998-cacaste) 中打开本课程，并安装 [Python 扩展](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-77998-cacaste)。

> <strong>注意</strong>：一旦克隆并在 VS Code 中打开目录，它会自动建议你安装 Python 扩展。你也需要按照上述说明安装 miniconda。

> <strong>注意</strong>：如果 VS Code 提示你在容器中重新打开仓库，你应当拒绝以使用本地的 Python 安装。

### 在浏览器中使用 Jupyter

你也可以在自己电脑的浏览器中使用 Jupyter 环境。无论是经典 Jupyter 还是 JupyterHub，都提供了便利的开发环境，具有自动补全、代码高亮等功能。

要在本地启动 Jupyter，请进入课程目录，执行：

```bash
jupyter notebook
```
或
```bash
jupyterhub
```
然后你可以导航到任何 `.ipynb` 文件，打开它们并开始工作。

### 容器中运行

Python 安装的另一种选择是将代码运行在容器中。由于我们的仓库包含一个特殊的 `.devcontainer` 文件夹，指导如何为该仓库构建容器，VS Code 提供了在容器中重新打开代码的选项。这将需要安装 Docker，操作也更复杂，因此我们推荐给有经验的用户。

## 云端运行

如果你不想在本地安装 Python，并且拥有一些云资源访问权限，运行代码到云端是一个不错的替代方案。有几种方式可以实现：

* 使用 **[GitHub Codespaces](https://github.com/features/codespaces)**，这是 GitHub 为你创建的一个虚拟环境，可以通过 VS Code 浏览器界面访问。如果你能使用 Codespaces，只需点击仓库中的 **Code** 按钮，启动 Codespace，即可迅速开始。
* 使用 **[Binder](https://mybinder.org/v2/gh/microsoft/ai-for-beginners/HEAD)**。[Binder](https://mybinder.org) 提供免费云计算资源，让像你一样的人可以测试 GitHub 上的代码。首页有一个按钮可用来在 Binder 中打开仓库 —— 这会快速带你进入 Binder 网站，自动构建底层容器并无缝启动 Jupyter 网页界面。

> <strong>注意</strong>：为防止滥用，Binder 屏蔽了部分 Web 资源的访问。这可能导致某些代码无法正常运行，比如从公共网络获取模型和/或数据集。你可能需要寻找解决方法。此外，Binder 提供的计算资源相对基本，特别是在后期复杂课程中训练会很慢。

## 使用 GPU 的云端运行

本课程的后期部分非常需要 GPU 支持。比如模型训练，否则速度会非常慢。如果你能够通过 [Azure for Students](https://azure.microsoft.com/free/students/?WT.mc_id=academic-77998-cacaste) 或你的机构访问云端资源，下面有几种选择：

* 创建 [数据科学虚拟机](https://docs.microsoft.com/learn/modules/intro-to-azure-data-science-virtual-machine/?WT.mc_id=academic-77998-cacaste) 并通过 Jupyter 连接。你可以直接在机器上克隆仓库并开始学习。NC 系列虚拟机支持 GPU。

> <strong>注意</strong>：某些订阅，包括 Azure for Students，默认不提供 GPU 支持。你可能需要通过技术支持请求额外申请 GPU 核心。

* 创建 [Azure 机器学习工作区](https://azure.microsoft.com/services/machine-learning/?WT.mc_id=academic-77998-cacaste)，并使用其中的 Notebook 功能。[此视频](https://azure-for-academics.github.io/quickstart/azureml-papers/) 展示了如何将仓库克隆到 Azure ML notebook 并开始使用。

你还可以使用 Google Colab，它提供一定的免费 GPU 支持，并上传 Jupyter 笔记本逐个执行。

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免责声明**：
本文件由 AI 翻译服务 [Co-op Translator](https://github.com/Azure/co-op-translator) 翻译完成。尽管我们力求准确，但请注意，自动翻译可能包含错误或不准确之处。原始语言版文件应视为权威来源。对于重要信息，建议使用专业人工翻译。我们对因使用本翻译而产生的任何误解或误释不承担责任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->