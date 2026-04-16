# 수업 번역으로 기여하기

이 커리큘럼의 수업 번역을 환영합니다!

## 지침

각 수업 폴더와 수업 소개 폴더에는 번역된 마크다운 파일이 포함되어 있습니다.

> 참고: 코드 샘플 파일의 코드는 번역하지 마세요. 번역해야 할 부분은 README, 과제, 퀴즈입니다. 감사합니다!

번역된 파일은 다음 명명 규칙을 따라야 합니다:

**README._[language]_.md**

여기서 _[language]_는 ISO 639-1 표준을 따르는 두 글자 언어 약어입니다 (예: 스페인어는 `README.es.md`, 네덜란드어는 `README.nl.md`).

**assignment._[language]_.md**

README와 마찬가지로 과제도 번역해주세요.

**퀴즈**

1. 번역을 퀴즈 앱에 추가하려면 여기에 파일을 추가하세요: https://github.com/microsoft/AI-For-Beginners/tree/main/etc/quiz-app/src/assets/translations, 올바른 명명 규칙을 따르세요 (en.json, fr.json). **단, 'true'와 'false'는 현지화하지 마세요. 감사합니다!**

2. 퀴즈 앱의 App.vue 파일에서 드롭다운에 언어 코드를 추가하세요.

3. 퀴즈 앱의 [translations index.js 파일](https://github.com/microsoft/AI-For-Beginners/blob/main/etc/quiz-app/src/assets/translations/index.js)을 편집하여 언어를 추가하세요.

4. 마지막으로, 번역된 README.md 파일의 모든 퀴즈 링크를 번역된 퀴즈로 직접 연결되도록 수정하세요: https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/1은 https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/1?loc=id로 변경됩니다.

**감사합니다**

여러분의 노력에 진심으로 감사드립니다!

**면책 조항**:  
이 문서는 AI 번역 서비스 [Co-op Translator](https://github.com/Azure/co-op-translator)를 사용하여 번역되었습니다. 정확성을 위해 최선을 다하고 있지만, 자동 번역에는 오류나 부정확성이 포함될 수 있습니다. 원본 문서를 해당 언어로 작성된 상태에서 권위 있는 자료로 간주해야 합니다. 중요한 정보의 경우, 전문적인 인간 번역을 권장합니다. 이 번역 사용으로 인해 발생하는 오해나 잘못된 해석에 대해 당사는 책임을 지지 않습니다.