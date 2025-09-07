<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "7df19702b8d2d3f7c4238c51bec2c8fc",
  "translation_date": "2025-08-26T11:08:29+00:00",
  "source_file": "lessons/0-course-setup/how-to-run.md",
  "language_code": "mo"
}
-->
# 如何執行程式碼

這份課程包含許多可執行的範例和實驗室，您可能會想要執行它們。為了做到這一點，您需要能夠在這份課程提供的 Jupyter Notebooks 中執行 Python 程式碼。以下是幾種執行程式碼的選項：

## 在本地電腦上執行

若要在本地電腦上執行程式碼，您需要安裝某個版本的 Python。我個人推薦安裝 **[miniconda](https://conda.io/en/latest/miniconda.html)**，這是一個輕量級的安裝包，支援使用 `conda` 套件管理器來建立不同的 Python **虛擬環境**。

安裝 miniconda 後，您需要克隆這個儲存庫並建立一個虛擬環境來用於這門課程：

```bash
git clone http://github.com/microsoft/ai-for-beginners
cd ai-for-beginners
conda env create --name ai4beg --file .devcontainer/environment.yml
conda activate ai4beg
```

### 使用 Visual Studio Code 和 Python 擴展

最好的方式可能是使用 [Visual Studio Code](http://code.visualstudio.com/?WT.mc_id=academic-77998-cacaste) 搭配 [Python 擴展](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-77998-cacaste)來開啟這份課程。

> **注意**：當您克隆並在 VS Code 中開啟目錄時，系統會自動建議您安裝 Python 擴展。您還需要按照上述步驟安裝 miniconda。

> **注意**：如果 VS Code 建議您在容器中重新開啟儲存庫，請拒絕此建議，改用本地的 Python 安裝。

### 在瀏覽器中使用 Jupyter

您也可以直接在自己的電腦瀏覽器中使用 Jupyter 環境。事實上，無論是傳統的 Jupyter 還是 Jupyter Hub，都提供了相當方便的開發環境，包括自動補全、程式碼高亮等功能。

若要在本地啟動 Jupyter，請進入課程的目錄，然後執行以下指令：

```bash
jupyter notebook
```
或
```bash
jupyterhub
```
接著，您可以瀏覽任何 `.ipynb` 檔案，開啟並開始工作。

### 在容器中執行

另一種替代安裝 Python 的方式是使用容器來執行程式碼。由於我們的儲存庫包含一個特殊的 `.devcontainer` 資料夾，指示如何為此儲存庫建立容器，VS Code 會提示您在容器中重新開啟程式碼。這需要安裝 Docker，並且操作會更為複雜，因此我們建議有經驗的使用者採用此方法。

## 在雲端執行

如果您不想在本地安裝 Python，並且有一些雲端資源可用，那麼在雲端執行程式碼是一個不錯的選擇。以下是幾種方法：

* 使用 **[GitHub Codespaces](https://github.com/features/codespaces)**，這是一個在 GitHub 上為您建立的虛擬環境，可透過 VS Code 的瀏覽器介面訪問。如果您有 Codespaces 的存取權，只需點擊儲存庫中的 **Code** 按鈕，啟動一個 Codespace，即可快速開始。

* 使用 **[Binder](https://mybinder.org/v2/gh/microsoft/ai-for-beginners/HEAD)**。[Binder](https://mybinder.org) 是一個免費的雲端計算資源，供像您這樣的使用者在 GitHub 上測試一些程式碼。首頁上有一個按鈕可以將儲存庫開啟於 Binder，這會快速將您帶到 Binder 網站，該網站會建立底層容器並無縫啟動 Jupyter 網頁介面。

> **注意**：為了防止濫用，Binder 對某些網路資源的存取是受限的。這可能會導致某些需要從公共網路下載模型或數據集的程式碼無法正常運行，您可能需要尋找替代方案。此外，Binder 提供的計算資源相對基礎，因此在後續更複雜的課程中，訓練速度可能會較慢。

## 在雲端使用 GPU 執行

課程中的某些後續章節會因為需要大量計算而非常適合使用 GPU，否則訓練過程可能會非常緩慢。如果您有雲端資源的存取權，例如透過 [Azure for Students](https://azure.microsoft.com/free/students/?WT.mc_id=academic-77998-cacaste) 或您的機構，以下是幾個選項：

* 建立 [Data Science Virtual Machine](https://docs.microsoft.com/learn/modules/intro-to-azure-data-science-virtual-machine/?WT.mc_id=academic-77998-cacaste)，並透過 Jupyter 連接到它。您可以直接將儲存庫克隆到該機器上，然後開始學習。NC 系列的虛擬機器支援 GPU。

> **注意**：某些訂閱（包括 Azure for Students）並未預設提供 GPU 支援。您可能需要透過技術支援請求額外的 GPU 核心。

* 建立 [Azure Machine Learning Workspace](https://azure.microsoft.com/services/machine-learning/?WT.mc_id=academic-77998-cacaste)，然後使用其中的 Notebook 功能。[這段影片](https://azure-for-academics.github.io/quickstart/azureml-papers/)展示了如何將儲存庫克隆到 Azure ML Notebook 並開始使用。

您也可以使用 Google Colab，它提供一些免費的 GPU 支援，並將 Jupyter Notebooks 上傳到那裡，逐一執行。

**免責聲明**：  
本文件已使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。我們致力於提供準確的翻譯，但請注意，自動翻譯可能包含錯誤或不準確之處。應以原始語言的文件作為權威來源。對於關鍵資訊，建議尋求專業人工翻譯。我們對因使用此翻譯而產生的任何誤解或錯誤解讀概不負責。