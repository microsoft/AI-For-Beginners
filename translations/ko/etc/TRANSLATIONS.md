# 수업 번역에 기여하기

이 커리큘럼의 수업에 대한 번역을 환영합니다!

## 가이드라인

각 수업 폴더와 수업 소개 폴더에는 번역된 마크다운 파일이 포함된 폴더가 있습니다.

> 주의: 코드 샘플 파일의 코드는 번역하지 마세요. 번역해야 할 항목은 README, 과제 및 퀴즈뿐입니다. 감사합니다!

번역된 파일은 다음과 같은 명명 규칙을 따라야 합니다:

**README._[language]_.md**

여기서 _[language]_는 ISO 639-1 표준에 따른 두 글자의 언어 약어입니다 (예: `README.es.md`는 스페인어, `README.nl.md`는 네덜란드어에 해당).

**assignment._[language]_.md**

README와 유사하게, 과제도 번역해 주세요.

**퀴즈**

1. 번역을 퀴즈 앱에 추가하려면 여기에서 파일을 추가하세요: https://github.com/microsoft/AI-For-Beginners/tree/main/etc/quiz-app/src/assets/translations, 적절한 명명 규칙(en.json, fr.json)을 따르세요. **'true' 또는 'false'라는 단어는 현지화하지 마세요. 감사합니다!**

2. 퀴즈 앱의 App.vue 파일에서 드롭다운에 언어 코드를 추가하세요.

3. 퀴즈 앱의 [translations index.js 파일](https://github.com/microsoft/AI-For-Beginners/blob/main/etc/quiz-app/src/assets/translations/index.js)을 편집하여 언어를 추가하세요.

4. 마지막으로, 번역된 README.md 파일의 모든 퀴즈 링크를 직접 번역된 퀴즈로 연결되도록 수정하세요: https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/1에서 https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/1?loc=id로 변경합니다.

**감사합니다**

여러분의 노고에 진심으로 감사드립니다!

**면책 조항**:  
이 문서는 기계 기반 AI 번역 서비스를 사용하여 번역되었습니다. 정확성을 위해 노력하고 있지만, 자동 번역에는 오류나 부정확성이 있을 수 있음을 유의하시기 바랍니다. 원본 문서는 해당 언어로 작성된 권위 있는 출처로 간주되어야 합니다. 중요한 정보에 대해서는 전문적인 인간 번역을 권장합니다. 이 번역의 사용으로 인해 발생하는 오해나 잘못된 해석에 대해 우리는 책임을 지지 않습니다.