# 測驗

這些測驗是 AI 課程（https://aka.ms/ai-beginners）的課前和課後測驗。

## 新增翻譯測驗集

透過在 `assets/translations` 資料夾中建立相應的測驗結構來新增測驗翻譯。原始測驗位於 `assets/translations/en`。測驗依據課程分為多個組別。請確保編號與正確的測驗部分對齊。整個課程共有 40 個測驗，編號從 0 開始。

編輯翻譯後，請編輯翻譯資料夾中的 `index.js` 檔案，按照 `en` 的慣例匯入所有檔案。

接著，編輯 `assets/translations` 中的 `index.js` 檔案，匯入新的翻譯檔案。

然後，編輯此應用程式中的 `App.vue` 下拉選單，新增您的語言。將本地化縮寫與您的語言資料夾名稱匹配。

最後，編輯翻譯課程中的所有測驗連結（如果存在），以包含此本地化作為查詢參數，例如：`?loc=fr`。

## 專案設定

```
npm install
```

### 編譯並熱重載以進行開發

```
npm run serve
```

### 編譯並壓縮以進行生產環境

```
npm run build
```

### 檢查並修復檔案

```
npm run lint
```

### 自訂配置

請參閱 [配置參考](https://cli.vuejs.org/config/)。

致謝：感謝此測驗應用程式的原始版本：https://github.com/arpan45/simple-quiz-vue

## 部署到 Azure

以下是幫助您開始的逐步指南：

1. Fork GitHub 儲存庫  
確保您的靜態網站應用程式程式碼位於您的 GitHub 儲存庫中。Fork 此儲存庫。

2. 建立 Azure 靜態網站應用程式  
- 建立 [Azure 帳戶](http://azure.microsoft.com)  
- 前往 [Azure 入口網站](https://portal.azure.com)  
- 點擊「建立資源」，然後搜尋「靜態網站應用程式」。  
- 點擊「建立」。  

3. 配置靜態網站應用程式  
- 基本設定：  
  - 訂閱：選擇您的 Azure 訂閱。  
  - 資源群組：建立新的資源群組或使用現有的資源群組。  
  - 名稱：為您的靜態網站應用程式提供一個名稱。  
  - 區域：選擇最接近您使用者的區域。  

- #### 部署詳細資訊：  
  - 原始碼：選擇「GitHub」。  
  - GitHub 帳戶：授權 Azure 存取您的 GitHub 帳戶。  
  - 組織：選擇您的 GitHub 組織。  
  - 儲存庫：選擇包含靜態網站應用程式的儲存庫。  
  - 分支：選擇您要部署的分支。  

- #### 建置詳細資訊：  
  - 建置預設值：選擇您的應用程式所使用的框架（例如 React、Angular、Vue 等）。  
  - 應用程式位置：指定包含應用程式程式碼的資料夾（例如，如果在根目錄，則為 /）。  
  - API 位置：如果有 API，請指定其位置（可選）。  
  - 輸出位置：指定生成輸出的資料夾（例如 build 或 dist）。  

4. 檢查並建立  
檢查您的設定，然後點擊「建立」。Azure 將設置必要的資源，並在您的儲存庫中建立 GitHub Actions 工作流程。

5. GitHub Actions 工作流程  
Azure 會自動在您的儲存庫中建立一個 GitHub Actions 工作流程檔案（.github/workflows/azure-static-web-apps-<name>.yml）。此工作流程將處理建置和部署過程。

6. 監控部署  
前往您的 GitHub 儲存庫中的「Actions」標籤。  
您應該會看到一個正在運行的工作流程。此工作流程將建置並部署您的靜態網站應用程式到 Azure。  
一旦工作流程完成，您的應用程式將在提供的 Azure URL 上線。

### 範例工作流程檔案

以下是 GitHub Actions 工作流程檔案的範例：  
name: Azure Static Web Apps CI/CD  
```
on:
  push:
    branches:
      - main
  pull_request:
    types: [opened, synchronize, reopened, closed]
    branches:
      - main

jobs:
  build_and_deploy_job:
    runs-on: ubuntu-latest
    name: Build and Deploy Job
    steps:
      - uses: actions/checkout@v2
      - name: Build And Deploy
        id: builddeploy
        uses: Azure/static-web-apps-deploy@v1
        with:
          azure_static_web_apps_api_token: ${{ secrets.AZURE_STATIC_WEB_APPS_API_TOKEN }}
          repo_token: ${{ secrets.GITHUB_TOKEN }}
          action: "upload"
          app_location: "etc/quiz-app # App source code path"
          api_location: ""API source code path optional
          output_location: "dist" #Built app content directory - optional
```

### 其他資源
- [Azure 靜態網站應用程式文件](https://learn.microsoft.com/azure/static-web-apps/getting-started)  
- [GitHub Actions 文件](https://docs.github.com/actions/use-cases-and-examples/deploying/deploying-to-azure-static-web-app)  

**免責聲明**：  
本文件已使用人工智能翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。我們致力於提供準確的翻譯，但請注意，自動翻譯可能包含錯誤或不準確之處。應以原文文件作為權威來源。對於關鍵資訊，建議尋求專業人工翻譯。我們對因使用此翻譯而引起的任何誤解或錯誤解釋概不負責。