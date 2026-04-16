# 如何執行程式碼

本課程包含許多可執行的範例和實驗室，您會想要執行它們。為此，您需要能夠在本課程所提供的 Jupyter 筆記本中執行 Python 程式碼。您有幾種選擇可以執行程式碼：

## 在您電腦本地執行

要在您電腦本地執行程式碼，需要安裝 Python。建議安裝 **[miniconda](https://conda.io/en/latest/miniconda.html)** — 這是一個相對輕量的安裝，支援使用 `conda` 套件管理器管理不同的 Python **虛擬環境**。

安裝 miniconda 後，克隆此倉庫並建立一個虛擬環境供本課程使用：

```bash
git clone http://github.com/microsoft/ai-for-beginners
cd ai-for-beginners
conda env create --name ai4beg --file .devcontainer/environment.yml
conda activate ai4beg
```

### 使用安裝了 Python 擴充功能的 Visual Studio Code

本課程最適合在安裝了 [Python 擴充功能](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-77998-cacaste) 的 [Visual Studio Code](http://code.visualstudio.com/?WT.mc_id=academic-77998-cacaste) 中開啟進行使用。

> **注意**：當您克隆並在 VS Code 中開啟目錄時，它會自動建議您安裝 Python 擴充功能。您同時也需要依前述安裝 miniconda。

> **注意**：如果 VS Code 建議您在容器中重新開啟倉庫，您應該拒絕，以使用本地的 Python 安裝。

### 在瀏覽器中使用 Jupyter

您也可以在自己電腦的瀏覽器中使用 Jupyter 環境。傳統的 Jupyter 與 JupyterHub 都提供了方便的開發環境，包括自動補完、程式碼高亮等功能。

要在本地啟動 Jupyter，請前往課程目錄並執行：

```bash
jupyter notebook
```
或
```bash
jupyterhub
```
然後您可以導航到任何 `.ipynb` 檔案，開啟並開始操作。

### 在容器中執行

另一種替代安裝 Python 的方法是使用容器來執行程式碼。由於我們的倉庫提供了一個特殊的 `.devcontainer` 資料夾，說明了如何為此倉庫建置容器，VS Code 提供機會讓您在容器中重新打開程式碼。這需要安裝 Docker，且流程較複雜，因此我們建議較有經驗的使用者採用此方式。

## 在雲端執行

如果您不想在本地安裝 Python，且能使用某些雲端資源，一個不錯的選擇是直接在雲端執行程式碼。您可以用以下幾種方法：

* 使用 **[GitHub Codespaces](https://github.com/features/codespaces)**，這是在 GitHub 上為您建立的虛擬環境，可透過 VS Code 瀏覽器介面存取。如果您有 Codespaces 的使用權，您只需點選倉庫中的 **Code** 按鈕，啟動 codespace，即可迅速開始。
* 使用 **[Binder](https://mybinder.org/v2/gh/microsoft/ai-for-beginners/HEAD)**。[Binder](https://mybinder.org) 免費提供雲端計算資源，方便您測試 GitHub 上的程式碼。在首頁有個按鈕可在 Binder 中開啟此倉庫 — 這會快速導向 Binder 網站，並自動建構一個底層容器，順暢啟動 Jupyter 網頁介面。

> **注意**：為防止濫用，Binder 對部分網絡資源有限制，有時會阻擋某些從公共網際網路下載模型或資料集的程式碼，可能導致部分程式無法正常運行，您可能需要尋找替代方案。此外，Binder 提供的計算資源較基本，訓練過程會比較慢，尤其在後續較複雜課程中。

## 在雲端使用 GPU 執行

本課程後面的一些章節會大大受益於 GPU 支援。例如模型訓練，否則會非常緩慢。您可以選擇以下幾種方法，特別是您有透過 [Azure for Students](https://azure.microsoft.com/free/students/?WT.mc_id=academic-77998-cacaste) 或您的機構取得雲端資源：

* 建立 [Data Science Virtual Machine](https://docs.microsoft.com/learn/modules/intro-to-azure-data-science-virtual-machine/?WT.mc_id=academic-77998-cacaste) 並透過 Jupyter 連線。您可以直接將倉庫克隆到此虛擬機，開始學習。NC 系列虛擬機支援 GPU。

> **注意**：部分訂閱服務，包括 Azure for Students 預設不提供 GPU 支援，您可能需要透過技術支援申請額外 GPU 核心。

* 建立 [Azure Machine Learning Workspace](https://azure.microsoft.com/services/machine-learning/?WT.mc_id=academic-77998-cacaste) 並使用其 Notebook 功能。[此影片](https://azure-for-academics.github.io/quickstart/azureml-papers/) 示範如何將倉庫克隆到 Azure ML Notebook 並開始使用。

您亦可使用 Google Colab，它提供部分免費 GPU 支援，並能上傳 Jupyter 筆記本，一個一個地執行。

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：  
本文件經由 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。儘管我們力求準確，請注意自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應被視為權威來源。對於重要資訊，建議使用專業人工翻譯。本公司不對使用本翻譯所引致的任何誤解或誤釋承擔責任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->