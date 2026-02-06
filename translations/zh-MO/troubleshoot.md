# AI-For-Beginners 疑難排解指南

本指南旨在幫助您解決使用或貢獻 [AI-For-Beginners](https://github.com/microsoft/AI-For-Beginners) 儲存庫時常見的問題。每個問題都包含背景、症狀、解釋以及逐步解決方案。

---

## 目錄

- [一般問題](../..)
- [安裝問題](../..)
- [配置問題](../..)
- [執行筆記本](../..)
- [性能問題](../..)
- [教科書網站問題](../..)
- [貢獻問題](../..)
- [常見問題](../..)
- [尋求幫助](../..)

---

## 一般問題

### 1. 儲存庫無法正確複製

**背景：** 複製儲存庫可以將其拷貝到您的機器上。

**症狀：**
- 錯誤：`fatal: repository not found`
- 錯誤：`Permission denied (publickey)`

**可能原因：**
- 儲存庫 URL 錯誤
- 權限不足
- SSH 金鑰未配置

**解決方案：**
1. **檢查儲存庫 URL。**  
   使用 HTTPS URL：  
   ```
   git clone https://github.com/microsoft/AI-For-Beginners.git
   ```
2. **如果 SSH 失敗，切換到 HTTPS。**  
   如果看到 `Permission denied (publickey)`，請使用上述 HTTPS 連結代替 SSH。
3. **配置 SSH 金鑰（可選）。**  
   如果您希望使用 SSH，請參考 [GitHub 的 SSH 指南](https://docs.github.com/en/authentication/connecting-to-github-with-ssh)。

---

## 安裝問題

### 2. Python 環境問題

**背景：** 儲存庫依賴 Python 和各種庫。

**症狀：**
- 錯誤：`ModuleNotFoundError: No module named '<package>'`
- 執行腳本或筆記本時出現導入錯誤

**可能原因：**
- 未安裝依賴項
- Python 版本錯誤

**解決方案：**
1. **設置虛擬環境。**  
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```
2. **安裝依賴項。**  
   ```bash
   pip install -r requirements.txt
   ```
3. **檢查 Python 版本。**  
   使用 Python 3.7 或更新版本。  
   ```bash
   python --version
   ```

### 3. 未安裝 Jupyter

**背景：** 筆記本是核心學習資源。

**症狀：**
- 錯誤：`jupyter: command not found`
- 筆記本無法啟動

**可能原因：**
- 未安裝 Jupyter

**解決方案：**
1. **安裝 Jupyter Notebook。**  
   ```bash
   pip install notebook
   ```
   或者，如果使用 Anaconda：
   ```bash
   conda install notebook
   ```
2. **啟動 Jupyter Notebook。**  
   ```bash
   jupyter notebook
   ```

### 4. 依賴版本衝突

**背景：** 如果包版本不匹配，項目可能會出現問題。

**症狀：**
- 關於不兼容版本的錯誤或警告

**可能原因：**
- 舊的或衝突的 Python 包

**解決方案：**
1. **在乾淨的環境中安裝。**  
   刪除舊的 venv/conda 環境並創建新的。
2. **使用精確版本。**  
   始終執行：
   ```bash
   pip install -r requirements.txt
   ```
   如果失敗，請按照 README 中的說明手動安裝缺失的包。

---

## 配置問題

### 5. 環境變數未設置

**背景：** 某些模組可能需要金鑰、令牌或配置設置。

**症狀：**
- 錯誤：`KeyError` 或缺少配置的警告

**可能原因：**
- 必需的環境變數未設置

**解決方案：**
1. **檢查 `.env.example` 或類似文件。**
2. **創建 `.env` 文件並填寫所需值。**
3. **設置環境變數後重新加載終端或 IDE。**

---

## 執行筆記本

### 6. 筆記本無法打開或運行

**背景：** Jupyter 筆記本需要正確的設置。

**症狀：**
- 筆記本無法啟動
- 瀏覽器未自動打開

**可能原因：**
- 未安裝 Jupyter
- 瀏覽器配置問題

**解決方案：**
1. **安裝 Jupyter（參見上方的安裝問題）。**
2. **手動打開筆記本。**
   - 從終端複製 URL（例如，`http://localhost:8888/?token=...`）並將其粘貼到瀏覽器中。

### 7. 核心崩潰或凍結

**背景：** 筆記本核心可能因資源限制或代碼錯誤而崩潰。

**症狀：**
- 核心反覆死機或重啟
- 記憶體不足錯誤

**可能原因：**
- 大型數據集
- 不兼容的代碼或包

**解決方案：**
1. **重啟核心。**  
   使用 Jupyter 中的“重啟核心”按鈕。
2. **檢查記憶體使用情況。**  
   關閉未使用的應用程序。
3. **在雲平台上運行筆記本。**  
   使用 [Google Colab](https://colab.research.google.com/) 或 [Azure Notebooks](https://notebooks.azure.com/)。

---

## 性能問題

### 8. 筆記本運行緩慢

**背景：** 某些 AI 任務需要大量記憶體和 CPU。

**症狀：**
- 執行速度慢
- 筆記本電腦風扇聲音很大

**可能原因：**
- 大型數據集或模型
- 系統資源有限

**解決方案：**
1. **使用雲平台。**
   - 將筆記本上傳到 Colab 或 Azure Notebooks。
2. **減少數據集大小。**
   - 使用樣本數據進行練習。
3. **關閉不必要的程序。**
   - 釋放系統 RAM。

---

## 教科書網站問題

### 9. 章節無法加載

**背景：** 在線教科書顯示課程和章節。

**症狀：**
- 某章節（例如 Transformers/BERT）丟失或無法打開

**已知問題：**  
- [問題 #303](https://github.com/microsoft/AI-For-Beginners/issues/303)：“18 Transformers. BERT. 無法在教科書網站上打開。” 由於文件名錯誤（`READMEtransformers.md` 而非 `README.md`）引起。

**解決方案：**
1. **檢查文件重命名錯誤。**  
   如果您是貢獻者，請確保章節文件命名為 `README.md`。
2. **報告丟失的文件。**  
   在 GitHub 上開啟問題，提供章節名稱和錯誤詳情。

---

## 貢獻問題

### 10. PR 未被接受或構建失敗

**背景：** 貢獻必須通過測試並遵循指南。

**症狀：**
- 拉取請求被拒絕
- CI/CD 管道錯誤

**可能原因：**
- 測試失敗
- 未遵循編碼標準

**解決方案：**
1. **閱讀貢獻指南。**
   - 遵循儲存庫的 [CONTRIBUTING.md](https://github.com/microsoft/AI-For-Beginners/blob/main/CONTRIBUTING.md)。
2. **在推送之前本地運行測試。**
3. **檢查格式要求或 linting 規則。**

---

## 常見問題

### 我在哪裡可以找到特定模組的幫助？
- 每個模組通常都有自己的 README。從那裡開始了解設置和使用提示。

### 如何報告錯誤或請求功能？
- [開啟 GitHub 問題](https://github.com/microsoft/AI-For-Beginners/issues/new)，提供清晰的描述和重現步驟。

### 如果我的問題未列出，我可以尋求幫助嗎？
- 可以！先搜索現有問題，如果找不到您的問題，請創建新問題。

---

## 尋求幫助

- **檢查問題：** [GitHub 問題](https://github.com/microsoft/AI-For-Beginners/issues)
- **提出問題：** 使用 GitHub 討論或開啟問題。
- **社群：** 查看儲存庫連結以獲取聊天/論壇選項。

---

_最後更新日期：2025-09-20_

---

**免責聲明**：  
本文件已使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。儘管我們努力確保翻譯的準確性，但請注意，自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應被視為權威來源。對於關鍵資訊，建議使用專業人工翻譯。我們對因使用此翻譯而產生的任何誤解或錯誤解釋不承擔責任。