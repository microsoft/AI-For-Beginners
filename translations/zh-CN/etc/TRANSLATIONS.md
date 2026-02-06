# 通过翻译课程内容贡献

我们欢迎对本课程内容进行翻译！

## 指南

每个课程文件夹和课程介绍文件夹中都有包含翻译后的 Markdown 文件的子文件夹。

> 注意，请不要翻译代码示例文件中的任何代码；唯一需要翻译的内容是 README、作业和测验。谢谢！

翻译后的文件应遵循以下命名规范：

**README._[language]_.md**

其中 _[language]_ 是遵循 ISO 639-1 标准的两位语言缩写（例如，西班牙语为 `README.es.md`，荷兰语为 `README.nl.md`）。

**assignment._[language]_.md**

与 README 文件类似，请翻译作业文件。

**测验**

1. 将您的翻译添加到测验应用中，通过在以下位置添加文件：https://github.com/microsoft/AI-For-Beginners/tree/main/etc/quiz-app/src/assets/translations，并遵循正确的命名规范（例如 en.json, fr.json）。**请不要翻译 'true' 或 'false' 这两个词，谢谢！**

2. 在测验应用的 App.vue 文件中添加您的语言代码到下拉菜单中。

3. 编辑测验应用的 [translations index.js 文件](https://github.com/microsoft/AI-For-Beginners/blob/main/etc/quiz-app/src/assets/translations/index.js)，以添加您的语言。

4. 最后，编辑您翻译后的 README.md 文件中的所有测验链接，使其直接指向您的翻译版测验：https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/1 改为 https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/1?loc=id

**感谢您！**

我们真诚地感谢您的努力！

**免责声明**：  
本文档使用AI翻译服务 [Co-op Translator](https://github.com/Azure/co-op-translator) 进行翻译。尽管我们努力确保翻译的准确性，但请注意，自动翻译可能包含错误或不准确之处。应以原始语言的文档作为权威来源。对于关键信息，建议使用专业人工翻译。我们对于因使用本翻译而引起的任何误解或误读不承担责任。