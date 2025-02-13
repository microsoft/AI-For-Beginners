# 通过翻译课程贡献

我们欢迎对本课程中课程的翻译！

## 指南

每个课程文件夹和课程介绍文件夹中都有包含翻译后的markdown文件的文件夹。

> 请注意，请勿翻译代码示例文件中的任何代码；唯一需要翻译的内容是README、作业和测验。谢谢！

翻译后的文件应遵循以下命名约定：

**README._[language]_.md**

其中 _[language]_ 是遵循ISO 639-1标准的两字母语言缩写（例如，`README.es.md`表示西班牙语，`README.nl.md`表示荷兰语）。

**assignment._[language]_.md**

与README类似，请翻译作业。

**测验**

1. 通过在此处添加文件，将您的翻译添加到quiz-app中：https://github.com/microsoft/AI-For-Beginners/tree/main/etc/quiz-app/src/assets/translations，并遵循适当的命名约定（en.json，fr.json）。**不过，请不要本地化“true”或“false”这两个词。谢谢！**

2. 将您的语言代码添加到quiz-app的App.vue文件中的下拉菜单中。

3. 编辑quiz-app的[translations index.js文件](https://github.com/microsoft/AI-For-Beginners/blob/main/etc/quiz-app/src/assets/translations/index.js)以添加您的语言。

4. 最后，编辑您翻译后的README.md文件中的所有测验链接，使其直接指向您的翻译测验：https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/1 变为 https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/1?loc=id

**谢谢**

我们非常感谢您的努力！

**免责声明**：  
本文件使用机器翻译服务进行翻译。虽然我们努力确保准确性，但请注意，自动翻译可能包含错误或不准确之处。原始文件的母语版本应被视为权威来源。对于关键信息，建议进行专业人工翻译。我们对因使用本翻译而产生的任何误解或错误解释不承担责任。