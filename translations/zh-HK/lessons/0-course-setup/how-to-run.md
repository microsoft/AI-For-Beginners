# 如何執行程式碼

本課程包含了很多可執行的範例和實驗室，你會想要運行它們。為此，你需要能在本課程提供的 Jupyter 筆記本中執行 Python 程式碼。你有幾種選擇來執行程式碼：

## 在你的電腦本地執行

要在你的電腦本地執行程式碼，需要安裝 Python。推薦安裝 **[miniconda](https://conda.io/en/latest/miniconda.html)** —— 它是個相當輕量的安裝，支援 `conda` 套件管理器來處理不同的 Python **虛擬環境**。

安裝 miniconda 後，請複製這個資料庫並建立一個虛擬環境，用於本課程：

```bash
git clone http://github.com/microsoft/ai-for-beginners
cd ai-for-beginners
conda env create --name ai4beg --file .devcontainer/environment.yml
conda activate ai4beg
```


### 使用含 Python 擴充功能的 Visual Studio Code

本課程最適合在 [Visual Studio Code](http://code.visualstudio.com/?WT.mc_id=academic-77998-cacaste) 中開啟，並搭配 [Python 擴充功能](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-77998-cacaste) 使用。

> **注意**：當你複製並在 VS Code 中開啟目錄後，它會自動建議你安裝 Python 擴充功能。你也需要照上述說明安裝 miniconda。

> **注意**：如果 VS Code 建議你在容器中重新開啟倉庫，請拒絕此建議以使用本地 Python 安裝。

### 在瀏覽器中使用 Jupyter

你也可以在自己的電腦瀏覽器中使用 Jupyter 環境。傳統 Jupyter 和 JupyterHub 都提供方便的開發環境，包括自動補全、程式碼高亮等功能。

要在本地啟動 Jupyter，前往課程目錄並執行：

```bash
jupyter notebook
```
 或
```bash
jupyterhub
```


之後，你可以導航到任意 `.ipynb` 檔案，開啟它們並開始工作。

### 在容器中運行

另一種選擇是不安裝 Python，而是在容器中運行程式碼。由於我們的資料庫包含一個特殊的 `.devcontainer` 資料夾，說明如何為此倉庫建置容器，VS Code 提供在容器中重新開啟程式碼的選項。這需要安裝 Docker，且過程較複雜，因此建議有經驗的使用者使用。

## 在雲端執行

如果你不想在本地安裝 Python，且能存取一些雲端資源，另一個好選擇是在雲端運行程式碼。你有幾種方式可以做到：

* 使用 **[GitHub Codespaces](https://github.com/features/codespaces)**，這是在 GitHub 上為你建立的虛擬環境，通過 VS Code 瀏覽器介面存取。如果你有 Codespaces 權限，只需點選倉庫內的 **Code** 按鈕，啟動 codespace，即可快速開始。

* 使用 **[Binder](https://mybinder.org/v2/gh/microsoft/ai-for-beginners/HEAD)**。 [Binder](https://mybinder.org) 為用戶提供免費的雲端運算資源，方便你測試 GitHub 上的程式碼。首頁有個按鈕可在 Binder 中開啟該倉庫——它會快速帶你進入 Binder 網站，建立底層容器並無縫啟動 Jupyter 網頁介面。

> **注意**：為防止濫用，Binder 有些網路資源的訪問被阻擋，這可能會導致部分從公共網際網路抓取模型和/或資料集的程式碼無法運作。你可能需要尋找替代方案。此外，Binder 提供的運算資源相當基礎，訓練速度會慢，尤其是在後面較複雜的課程中。

## 在雲端使用 GPU 執行

本課程後期的某些課程會從 GPU 支援中大幅獲益。例如模型訓練否則會非常緩慢。若你透過 [Azure for Students](https://azure.microsoft.com/free/students/?WT.mc_id=academic-77998-cacaste) 或你的學校取得雲端資源，可參考以下選項：

* 建立 [Data Science 虛擬機](https://docs.microsoft.com/learn/modules/intro-to-azure-data-science-virtual-machine/?WT.mc_id=academic-77998-cacaste) 並透過 Jupyter 連接它。你可直接將倉庫複製到該機器，然後開始學習。NC 系列虛擬機支援 GPU。

> **注意**：部分訂閱方案（包括 Azure for Students）預設不提供 GPU 支援，你可能需透過技術支援請求額外核配 GPU 核心。

* 建立 [Azure 機器學習工作區](https://azure.microsoft.com/services/machine-learning/?WT.mc_id=academic-77998-cacaste)，並使用該處的筆記本功能。[這段影片](https://azure-for-academics.github.io/quickstart/azureml-papers/) 介紹如何將倉庫克隆到 Azure ML 筆記本並開始使用。

你也可以使用 Google Colab，它提供一些免費的 GPU 支援，並可將 Jupyter 筆記本逐一上傳執行。

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：  
本文件由 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。儘管我們盡力確保準確性，但請注意，自動翻譯可能存在錯誤或不準確之處。原始文件的母語版本應視為權威來源。對於重要資訊，建議採用專業人工翻譯。我們不對因使用本翻譯所引起的任何誤解或誤釋承擔責任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->