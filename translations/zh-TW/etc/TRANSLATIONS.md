# 透過翻譯課程來貢獻

我們歡迎您為本課程的課程內容進行翻譯！

## 指南

每個課程資料夾和課程介紹資料夾中都有包含翻譯後的 Markdown 文件的資料夾。

> 注意，請不要翻譯任何程式碼範例文件中的程式碼；唯一需要翻譯的是 README、作業和測驗。謝謝！

翻譯後的文件應遵循以下命名規範：

**README._[language]_.md**

其中 _[language]_ 是遵循 ISO 639-1 標準的兩位字母語言縮寫（例如，西班牙文為 `README.es.md`，荷蘭文為 `README.nl.md`）。

**assignment._[language]_.md**

與 README 類似，請同樣翻譯作業文件。

**測驗**

1. 將您的翻譯新增到測驗應用程式中，方法是將文件新增到此處：https://github.com/microsoft/AI-For-Beginners/tree/main/etc/quiz-app/src/assets/translations，並遵循正確的命名規範（如 en.json、fr.json）。**請不要翻譯 'true' 或 'false' 這些詞語，謝謝！**

2. 將您的語言代碼新增到測驗應用程式的 App.vue 文件中的下拉選單中。

3. 編輯測驗應用程式的 [translations index.js 文件](https://github.com/microsoft/AI-For-Beginners/blob/main/etc/quiz-app/src/assets/translations/index.js)，以新增您的語言。

4. 最後，編輯您翻譯後的 README.md 文件中的所有測驗連結，直接指向您的翻譯測驗，例如：https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/1 變更為 https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/1?loc=id

**感謝您**

我們由衷感謝您的努力！

**免責聲明**：  
本文件使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們致力於提供準確的翻譯，但請注意，自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應被視為權威來源。對於關鍵資訊，建議使用專業人工翻譯。我們對因使用此翻譯而引起的任何誤解或錯誤解釋不承擔責任。