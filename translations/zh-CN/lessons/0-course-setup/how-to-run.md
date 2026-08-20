# 如何运行代码

本课程包含许多可执行示例和实验，您可能想运行它们。为此，您需要能够在本课程提供的 Jupyter Notebook 中执行 Python 代码。您有几种运行代码的选择：

## 在您的计算机上本地运行

若要在您的计算机上本地运行代码，需要安装 Python。推荐安装 **[miniconda](https://conda.io/en/latest/miniconda.html)** —— 它是较轻量的安装，支持使用 `conda` 包管理器管理不同的 Python <strong>虚拟环境</strong>。

安装 miniconda 后，克隆仓库并创建一个本课程用的虚拟环境：

```bash
git clone http://github.com/microsoft/ai-for-beginners
cd ai-for-beginners
conda env create --name ai4beg --file .devcontainer/environment.yml
conda activate ai4beg
```

> **Windows 注意事项**：如果创建环境时在安装 `gdk-pixbuf` 阶段失败，并出现提及 `gbk` 编码的 `UnicodeDecodeError`，请在您使用的终端中启用 Python UTF-8 模式，然后重试。请根据终端类型使用相应的语法：
>
> **PowerShell：**
>
> ```powershell
> $env:PYTHONUTF8 = "1"
> conda env create --name ai4beg --file .devcontainer/environment.yml
> ```
>
> **命令提示符（`cmd.exe`）或 Anaconda Prompt：**
>
> ```cmd
> set PYTHONUTF8=1
> conda env create --name ai4beg --file .devcontainer/environment.yml
> ```
>
> **Bash（包括 Git Bash）：**
>
> ```bash
> export PYTHONUTF8=1
> conda env create --name ai4beg --file .devcontainer/environment.yml
> ```
>
> 如果失败的尝试留下了 `ai4beg` 环境，请先停用并删除该课程环境，然后再重试。如果当前已激活某个环境，请先运行 `conda deactivate`：
>
> ```text
> conda deactivate
> conda env remove --name ai4beg
> ```

### 使用带 Python 扩展的 Visual Studio Code

在 [Visual Studio Code](http://code.visualstudio.com/?WT.mc_id=academic-77998-cacaste) 中打开本课程并安装 [Python 扩展](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-77998-cacaste)，是使用本课程的最佳方式。

> <strong>注意</strong>：克隆并在 VS Code 中打开目录后，它会自动提示您安装 Python 扩展。同时，您还需按照上面描述安装 miniconda。

> <strong>注意</strong>：如果 VS Code 提示您重新在容器中打开仓库，您应拒绝该请求，以便使用本地 Python 安装。

### 在浏览器中使用 Jupyter

您也可以在自己计算机上的浏览器中使用 Jupyter 环境。无论是经典 Jupyter 还是 JupyterHub，都提供自动补全、代码高亮等便捷的开发环境。

要在本地启动 Jupyter，请进入课程目录，执行以下命令：

```bash
jupyter notebook
```
或
```bash
jupyterhub
```
然后，您可以导航到任何 `.ipynb` 文件，打开它们并开始工作。

### 容器中运行

安装 Python 的另一种方式是通过容器运行代码。由于我们的仓库提供了一个专门的 `.devcontainer` 文件夹，指导如何为此仓库构建容器，VS Code 提供重新在容器中打开代码的选项。这需要安装 Docker，且更复杂，因此我们建议经验丰富的用户使用。

## 云端运行

如果您不想本地安装 Python，且拥有某些云资源，另一种选择是云端运行代码。您可以通过几种方式实现这一点：

* 使用 **[GitHub Codespaces](https://github.com/features/codespaces)**，这是 GitHub 为您创建的虚拟环境，可通过 VS Code 浏览器界面访问。如果您能使用 Codespaces，只需点击仓库中的 **Code** 按钮，启动 codespace，马上就能运行。
* 使用 **[Binder](https://mybinder.org/v2/gh/microsoft/ai-for-beginners/HEAD)**。[Binder](https://mybinder.org) 为像您这样的用户提供免费的云端计算资源，可以用来测试 GitHub 上的代码。主页上有一个按钮可以在 Binder 中打开仓库，这会迅速带您到 Binder 网站，它会构建底层容器，并无缝启动 Jupyter 网页界面。

> <strong>注意</strong>：为防止滥用，Binder 对某些网络资源有限制。这可能导致部分代码无法运行（尤其是那些从公共互联网获取模型和/或数据集的代码）。您可能需要找到一些解决方法。另外，Binder 提供的计算资源相当基础，训练过程会很慢，尤其是在后面更复杂的课程中。

## 云端 GPU 运行

本课程后期的部分课程非常依赖 GPU 支持。例如模型训练，若无 GPU 会非常缓慢。如果您拥有云端账号，尤其是通过 [Azure for Students](https://azure.microsoft.com/free/students/?WT.mc_id=academic-77998-cacaste) 或您所在机构的云服务，可以采用以下几种方式：

* 创建 [数据科学虚拟机（Data Science Virtual Machine）](https://docs.microsoft.com/learn/modules/intro-to-azure-data-science-virtual-machine/?WT.mc_id=academic-77998-cacaste)，通过 Jupyter 连接。然后您可以直接在虚拟机上克隆仓库，开始学习。NC 系列虚拟机支持 GPU。

> <strong>注意</strong>：某些订阅（包括 Azure for Students）默认不提供 GPU 支持。您可能需要通过技术支持请求额外申请 GPU 核心。

* 创建 [Azure 机器学习工作区](https://azure.microsoft.com/services/machine-learning/?WT.mc_id=academic-77998-cacaste)，使用其中的 Notebook 功能。[此视频](https://azure-for-academics.github.io/quickstart/azureml-papers/)展示了如何将仓库克隆到 Azure ML Notebook 并开始使用。

您也可以使用 Google Colab，它提供部分免费 GPU 支持，您可以上传 Jupyter Notebook 并逐个执行。

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免责声明**：
本文件由 AI 翻译服务 [Co-op Translator](https://github.com/Azure/co-op-translator) 翻译完成。尽管我们力求准确，但请注意，自动翻译可能包含错误或不准确之处。原始语言版文件应视为权威来源。对于重要信息，建议使用专业人工翻译。我们对因使用本翻译而产生的任何误解或误释不承担责任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
