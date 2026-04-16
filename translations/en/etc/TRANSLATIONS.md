<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "62b3e3ad5182edb905eec649a87eeeb4",
  "translation_date": "2025-08-31T18:04:23+00:00",
  "source_file": "etc/TRANSLATIONS.md",
  "language_code": "en"
}
-->
# Contribute by translating lessons

We welcome translations for the lessons in this curriculum!

## Guidelines

Each lesson folder and lesson introduction folder contains subfolders with the translated markdown files.

> Note, please do not translate any code in the code sample files; the only things to translate are README, assignments, and the quizzes. Thanks!

Translated files should follow this naming convention:

**README._[language]_.md**

where _[language]_ is a two-letter language abbreviation following the ISO 639-1 standard (e.g. `README.es.md` for Spanish and `README.nl.md` for Dutch).

**assignment._[language]_.md**

Similar to Readme files, please translate the assignments as well.

**Quizzes**

1. Add your translation to the quiz-app by adding a file here: https://github.com/microsoft/AI-For-Beginners/tree/main/etc/quiz-app/src/assets/translations, with the proper naming convention (en.json, fr.json). **Please don't localize the words 'true' or 'false' however. Thanks!**

2. Add your language code to the dropdown in the quiz-app's App.vue file.

3. Edit the quiz-app's [translations index.js file](https://github.com/microsoft/AI-For-Beginners/blob/main/etc/quiz-app/src/assets/translations/index.js) to add your language.

4. Finally, edit ALL the quiz links in your translated README.md files to point directly to your translated quiz: https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/1 becomes https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/1?loc=id

**THANK YOU**

We truly appreciate your efforts!

---

**Disclaimer**:  
This document has been translated using the AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). While we aim for accuracy, please note that automated translations may include errors or inaccuracies. The original document in its native language should be regarded as the authoritative source. For critical information, professional human translation is advised. We are not responsible for any misunderstandings or misinterpretations resulting from the use of this translation.