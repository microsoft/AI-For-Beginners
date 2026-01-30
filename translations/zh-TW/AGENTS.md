# AGENTS.md

## 專案概述

AI for Beginners 是一個為期 12 週、共 24 節課的全面課程，涵蓋人工智慧的基本概念。本教育資源庫包含使用 Jupyter Notebooks 的實作課程、測驗以及動手實驗。課程內容包括：

- 符號式 AI：知識表示與專家系統
- 使用 TensorFlow 和 PyTorch 的神經網路與深度學習
- 電腦視覺技術與架構
- 自然語言處理 (NLP)：包括 transformers 和 BERT
- 專門主題：基因演算法、強化學習、多代理系統
- AI 倫理與負責任 AI 原則

**主要技術：** Python 3、Jupyter Notebooks、TensorFlow、PyTorch、Keras、OpenCV、Vue.js（用於測驗應用程式）

**架構：** 教育內容資源庫，按主題區域組織 Jupyter Notebooks，並輔以基於 Vue.js 的測驗應用程式及廣泛的多語言支援。

## 設置指令

### 主要開發環境 (Python/Jupyter)

課程設計以 Python 和 Jupyter Notebooks 為基礎。推薦使用 miniconda：

```bash
# Clone the repository
git clone https://github.com/microsoft/ai-for-beginners
cd ai-for-beginners

# Create and activate conda environment
conda env create --name ai4beg --file environment.yml
conda activate ai4beg

# Start Jupyter Notebook
jupyter notebook
# OR
jupyter lab
```

### 替代方案：使用 devcontainer

```bash
# Open in VS Code and select "Reopen in Container" when prompted
# The devcontainer will automatically set up the environment
```

### 測驗應用程式設置

測驗應用程式是一個獨立的 Vue.js 應用程式，位於 `etc/quiz-app/`：

```bash
cd etc/quiz-app
npm install
npm run serve  # Development server
npm run build  # Production build
npm run lint   # Lint and fix files
```

## 開發工作流程

### 使用 Jupyter Notebooks

1. **本地開發：**
   - 啟動 conda 環境：`conda activate ai4beg`
   - 啟動 Jupyter：`jupyter notebook` 或 `jupyter lab`
   - 瀏覽至課程資料夾並打開 `.ipynb` 文件
   - 互動式執行單元以跟隨課程

2. **使用 VS Code 的 Python 擴展：**
   - 在 VS Code 中打開資源庫
   - 安裝 Python 擴展
   - VS Code 會自動檢測並使用 conda 環境
   - 直接在 VS Code 中打開 `.ipynb` 文件

3. **雲端開發：**
   - **GitHub Codespaces：** 點擊 "Code" → "Codespaces" → "Create codespace on main"
   - **Binder：** 使用 README 中的 Binder 徽章在瀏覽器中啟動
   - 注意：Binder 資源有限且有部分網路訪問限制

### 高級課程的 GPU 支援

後期課程顯著受益於 GPU 加速：

- **Azure Data Science VM：** 使用具備 GPU 支援的 NC 系列虛擬機
- **Azure Machine Learning：** 使用具 GPU 計算的 notebook 功能
- **Google Colab：** 單獨上傳 notebook（提供免費 GPU 支援）

### 測驗應用程式開發

```bash
cd etc/quiz-app
npm run serve  # Hot-reload development server at http://localhost:8080
```

## 測試指導

這是一個以學習內容為重點的教育資源庫，而非傳統的軟體測試。沒有傳統的測試套件。

### 驗證方法：

1. **Jupyter Notebooks：** 依序執行單元以驗證程式碼範例是否正常運行
2. **測驗應用程式測試：** 通過開發伺服器進行手動測試
3. **翻譯驗證：** 檢查 `translations/` 資料夾中的翻譯內容
4. **測驗應用程式語法檢查：** 在 `etc/quiz-app/` 中執行 `npm run lint`

### 執行程式碼範例：

```bash
# Activate environment first
conda activate ai4beg

# Run Python scripts directly
python lessons/4-ComputerVision/07-ConvNets/pytorchcv.py

# Or execute notebooks
jupyter notebook lessons/3-NeuralNetworks/03-Perceptron/Perceptron.ipynb
```

## 程式碼風格

### Python 程式碼風格

- 遵循標準 Python 規範，適用於教育性程式碼
- 清晰、易讀的程式碼，優先考慮學習而非最佳化
- 註解解釋關鍵概念
- 適合 Jupyter Notebook：單元應盡可能自成一體
- 對課程內容無嚴格語法檢查要求

### JavaScript/Vue.js (測驗應用程式)

- 在 `etc/quiz-app/package.json` 中配置 ESLint
- 執行 `npm run lint` 以檢查並自動修復問題
- 遵循 Vue 2.x 規範
- 基於元件的架構

### 文件組織

```
lessons/
  ├── 0-course-setup/          # Setup instructions
  ├── 1-Intro/                 # Introduction to AI
  ├── 2-Symbolic/              # Symbolic AI
  ├── 3-NeuralNetworks/        # Neural Networks basics
  ├── 4-ComputerVision/        # Computer Vision
  ├── 5-NLP/                   # Natural Language Processing
  ├── 6-Other/                 # Other AI techniques
  ├── 7-Ethics/                # AI Ethics
  └── X-Extras/                # Additional content

etc/
  ├── quiz-app/                # Vue.js quiz application
  └── quiz-src/                # Quiz source files

translations/                  # Multi-language translations
```

## 建置與部署

### Jupyter 內容

不需要建置過程 - Jupyter Notebooks 可直接執行。

### 測驗應用程式

```bash
cd etc/quiz-app

# Development
npm run serve

# Production build
npm run build  # Outputs to etc/quiz-app/dist/

# Deploy to Azure Static Web Apps
# Azure automatically creates GitHub Actions workflow
# See etc/quiz-app/README.md for detailed deployment instructions
```

### 文件網站

資源庫使用 Docsify 作為文件系統：
- `index.html` 作為入口點
- 不需要建置 - 直接通過 GitHub Pages 提供服務
- 訪問地址：https://microsoft.github.io/AI-For-Beginners/

## 貢獻指南

### 拉取請求流程

1. **標題格式：** 清晰、描述性標題，說明更改內容
2. **CLA 要求：** 必須簽署 Microsoft CLA（自動檢查）
3. **內容指南：**
   - 保持教育重點和適合初學者的方式
   - 測試所有 notebook 中的程式碼範例
   - 確保 notebook 從頭到尾正常運行
   - 如果修改英文內容，請更新翻譯
4. **測驗應用程式更改：** 在提交前執行 `npm run lint`

### 翻譯貢獻

- 翻譯通過 GitHub Actions 使用 co-op-translator 自動完成
- 手動翻譯存放於 `translations/<language-code>/`
- 測驗翻譯存放於 `etc/quiz-app/src/assets/translations/`
- 支援語言：40+ 種語言（完整列表請參閱 README）

### 活躍貢獻領域

請參閱 `etc/CONTRIBUTING.md` 了解當前需求：
- 深度強化學習部分
- 物件檢測改進
- 命名實體識別範例
- 自定義嵌入訓練範例

## 環境配置

### 必需的依賴項

```bash
# Core Python packages (from requirements.txt)
tensorflow==2.17.0
torch (via conda)
torchvision (via conda)
keras==3.5.0
opencv (via conda)
scikit-learn
numpy==1.26
pandas==2.2.2
matplotlib==3.9
jupyter
```

### 環境變數

基本使用不需要特殊環境變數。

對於 Azure 部署（測驗應用程式）：
- `AZURE_STATIC_WEB_APPS_API_TOKEN`（由 Azure 自動設置）

## 除錯與故障排除

### 常見問題

**問題：** Conda 環境創建失敗  
- **解決方案：** 首先更新 conda：`conda update conda -y`  
- 確保磁碟空間充足（建議 50GB）

**問題：** 找不到 Jupyter 核心  
- **解決方案：**  
  ```bash
  conda activate ai4beg
  python -m ipykernel install --user --name ai4beg
  ```

**問題：** Notebook 中未檢測到 GPU  
- **解決方案：**  
  - 驗證 CUDA 安裝：`nvidia-smi`  
  - 檢查 PyTorch GPU：`python -c "import torch; print(torch.cuda.is_available())"`  
  - 檢查 TensorFlow GPU：`python -c "import tensorflow as tf; print(tf.config.list_physical_devices('GPU'))"`

**問題：** 測驗應用程式無法啟動  
- **解決方案：**  
  ```bash
  cd etc/quiz-app
  rm -rf node_modules package-lock.json
  npm install
  npm run serve
  ```

**問題：** Binder 超時或阻止下載  
- **解決方案：** 使用 GitHub Codespaces 或本地設置以獲得更好的資源訪問

### 記憶體問題

某些課程需要大量 RAM（建議 8GB+）：  
- 對於資源密集型課程，使用雲端虛擬機  
- 執行模型訓練時關閉其他應用程式  
- 如果記憶體不足，減少 notebook 中的批次大小

## 附加說明

### 對課程講師的建議

- 請參閱 `lessons/0-course-setup/for-teachers.md` 了解教學指導
- 課程是自成一體的，可以按順序教授或單獨選擇
- 預估時間：12 週，每週 2 節課

### 雲端資源

- **Azure for Students：** 學生可獲得免費額度
- **Microsoft Learn：** 課程中鏈接的補充學習路徑
- **Binder：** 免費但資源有限且有部分網路限制

### 程式碼執行選項

1. **本地（推薦）：** 完全控制，最佳效能，支援 GPU
2. **GitHub Codespaces：** 基於雲端的 VS Code，適合快速訪問
3. **Binder：** 基於瀏覽器的 Jupyter，免費但有限
4. **Azure ML Notebooks：** 企業選項，支援 GPU
5. **Google Colab：** 單獨上傳 notebook，提供免費 GPU 層

### 使用 Notebook

- Notebook 設計為逐單元執行以便學習
- 許多 notebook 在首次運行時下載數據集（可能需要一些時間）
- 某些模型需要 GPU 才能在合理時間內完成訓練
- 儘可能使用預訓練模型以減少計算需求

### 效能考量

- 後期電腦視覺課程（CNNs、GANs）受益於 GPU
- NLP transformer 課程可能需要大量 RAM
- 從零開始訓練具有教育意義但耗時
- 遷移學習範例可減少訓練時間

---

**免責聲明**：  
本文件使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。儘管我們努力確保翻譯的準確性，但請注意，自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應被視為權威來源。對於關鍵資訊，建議使用專業人工翻譯。我們對因使用此翻譯而引起的任何誤解或錯誤解釋不承擔責任。