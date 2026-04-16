# レッスンの翻訳で貢献する

このカリキュラムのレッスンの翻訳を歓迎します！

## ガイドライン

各レッスンフォルダーおよびレッスン紹介フォルダーには、翻訳されたMarkdownファイルが含まれています。

> 注意: コードサンプルファイル内のコードは翻訳しないでください。翻訳するのはREADME、課題、クイズのみです。よろしくお願いします！

翻訳されたファイルは以下の命名規則に従ってください：

**README._[language]_.md**

_[language]_はISO 639-1標準に従った2文字の言語略称です（例: スペイン語の場合は`README.es.md`、オランダ語の場合は`README.nl.md`）。

**assignment._[language]_.md**

READMEと同様に、課題も翻訳してください。

**クイズ**

1. クイズアプリに翻訳を追加するには、以下の場所にファイルを追加してください: https://github.com/microsoft/AI-For-Beginners/tree/main/etc/quiz-app/src/assets/translations。適切な命名規則（例: en.json, fr.json）を守ってください。**ただし、「true」や「false」という単語はローカライズしないでください。よろしくお願いします！**

2. クイズアプリのApp.vueファイルでドロップダウンに言語コードを追加してください。

3. クイズアプリの[translations index.jsファイル](https://github.com/microsoft/AI-For-Beginners/blob/main/etc/quiz-app/src/assets/translations/index.js)を編集して言語を追加してください。

4. 最後に、翻訳されたREADME.mdファイル内のすべてのクイズリンクを、翻訳されたクイズに直接リンクするよう編集してください: https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/1 を https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/1?loc=id に変更してください。

**ありがとうございます**

皆さんの努力に心から感謝します！

**免責事項**:  
この文書は、AI翻訳サービス [Co-op Translator](https://github.com/Azure/co-op-translator) を使用して翻訳されています。正確性を追求しておりますが、自動翻訳には誤りや不正確な部分が含まれる可能性があることをご承知おきください。元の言語で記載された文書が公式な情報源とみなされるべきです。重要な情報については、専門の人間による翻訳を推奨します。この翻訳の使用に起因する誤解や誤認について、当方は一切の責任を負いません。