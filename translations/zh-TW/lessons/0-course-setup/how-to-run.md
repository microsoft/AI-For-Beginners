# 如何執行程式碼

本課程包含許多可執行的範例和實驗，你會想要運行這些範例。為此，你需要具備在本課程所提供的 Jupyter 筆記本中執行 Python 程式碼的能力。你有幾種選擇可以執行程式碼：

## 在你的電腦上本地執行

若要在你的電腦本地運行程式碼，需要安裝 Python。一個建議是安裝 **[miniconda](https://conda.io/en/latest/miniconda.html)** — 它是一個相當輕量的安裝，支援 `conda` 套件管理工具來管理不同的 Python **虛擬環境**。

安裝 miniconda 之後，複製本儲存庫並建立一個虛擬環境來使用這門課程：

```bash
git clone http://github.com/microsoft/ai-for-beginners
cd ai-for-beginners
conda env create --name ai4beg --file .devcontainer/environment.yml
conda activate ai4beg
```

### 使用帶有 Python 擴充功能的 Visual Studio Code

本課程在使用 [Visual Studio Code](http://code.visualstudio.com/?WT.mc_id=academic-77998-cacaste) 並安裝 [Python 擴充功能](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-77998-cacaste) 時效果最佳。

> **注意**：一旦你複製儲存庫並在 VS Code 中打開目錄，它會自動建議你安裝 Python 擴充功能。你還需要按上述說明安裝 miniconda。

> **注意**：如果 VS Code 建議你在容器中重新打開儲存庫，你應該拒絕此建議以使用本地的 Python 安裝。

### 在瀏覽器中使用 Jupyter

你也可以在自己的電腦瀏覽器中使用 Jupyter 環境。傳統的 Jupyter 和 JupyterHub 都提供方便的開發環境，具備自動完成、程式碼高亮等功能。

要在本地啟動 Jupyter，請前往課程目錄，並執行：

```bash
jupyter notebook
```
或
```bash
jupyterhub
```
然後你可以瀏覽任何 `.ipynb` 檔案，打開它們並開始工作。

### 在容器中執行

另一個替代 Python 安裝的選項是直接在容器中執行程式碼。由於我們的儲存庫提供了一個特殊的 `.devcontainer` 資料夾，指示如何為本儲存庫建構容器，VS Code 提供重新在容器中打開程式碼的功能。這需要安裝 Docker，流程也會較複雜，因此建議較有經驗的使用者採用此方案。

## 在雲端運行

如果你不想在本地安裝 Python，並且有雲端資源可用，另一個好選擇是直接在雲端執行程式碼。有幾種方式可以做到：

* 使用 **[GitHub Codespaces](https://github.com/features/codespaces)**，這是在 GitHub 上為你建立的虛擬環境，可經由 VS Code 瀏覽器介面存取。如果你有 Codespaces 的權限，只需點擊儲存庫中的 **Code** 按鈕，啟動 codespace，馬上即可開始執行。
* 使用 **[Binder](https://mybinder.org/v2/gh/microsoft/ai-for-beginners/HEAD)**。[Binder](https://mybinder.org) 提供免費的雲端運算資源，讓你可以測試 GitHub 上的程式碼。首頁有一個按鈕可直接開啟儲存庫於 Binder — 這會快速引導你到 Binder 網站，自動建構底層容器並啟動 Jupyter 網頁介面。

> **注意**：為防止濫用，Binder 對部分網路資源進行封鎖，這可能導致部分從公共網路下載模型和/或資料集的程式碼無法正常運作，你可能需找尋替代方案。此外，Binder 提供的運算資源相當基礎，訓練過程會較慢，尤其是後期更複雜的課程。

## 使用 GPU 雲端運行

在本課程後期，有些課程會非常受惠於 GPU 支援。例如，模型訓練否則會非常緩慢。以下是一些選項，特別是如果你透過 [Azure for Students](https://azure.microsoft.com/free/students/?WT.mc_id=academic-77998-cacaste) 或機構有雲端存取權：

* 建立 [資料科學虛擬機](https://docs.microsoft.com/learn/modules/intro-to-azure-data-science-virtual-machine/?WT.mc_id=academic-77998-cacaste) 並透過 Jupyter 連線。你可以直接在機器上複製儲存庫並開始學習。NC 系列虛擬機支援 GPU。

> **注意**：部分訂閱，包括 Azure for Students，預設不包含 GPU 支援。你可能需要透過技術支援申請額外的 GPU 核心。

* 建立 [Azure 機器學習工作區](https://azure.microsoft.com/services/machine-learning/?WT.mc_id=academic-77998-cacaste)，然後使用其中的 Notebook 功能。[此影片](https://azure-for-academics.github.io/quickstart/azureml-papers/) 示範如何將儲存庫克隆到 Azure ML 筆記本並開始使用。

你也可以使用 Google Colab，該服務附帶部分免費的 GPU 支援，並上傳 Jupyter 筆記本，一筆一筆地執行。

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：  
本文件係使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們努力追求準確性，但請注意，自動翻譯可能包含錯誤或不精確之處。原始文件的母語版本應視為權威資料來源。對於重要資訊，建議採用專業人工翻譯。我們對因使用本翻譯所引起的任何誤解或誤譯不承擔任何責任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->