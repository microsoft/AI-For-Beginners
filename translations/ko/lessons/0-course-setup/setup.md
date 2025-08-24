<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "c4c545eb30765a49469ced84cfb4379f",
  "translation_date": "2025-08-24T21:38:09+00:00",
  "source_file": "lessons/0-course-setup/setup.md",
  "language_code": "ko"
}
-->
# 이 커리큘럼 시작하기

## 학생이신가요?

다음 리소스를 통해 시작해보세요:

* [Student Hub 페이지](https://docs.microsoft.com/learn/student-hub?WT.mc_id=academic-77998-cacaste) 이 페이지에서는 초보자를 위한 리소스, 학생 팩, 그리고 무료 인증서 바우처를 받을 수 있는 방법을 찾을 수 있습니다. 이 페이지는 즐겨찾기에 추가하고 정기적으로 확인하세요. 콘텐츠는 최소 월 단위로 변경됩니다.
* [Microsoft Student Learn Ambassadors](https://studentambassadors.microsoft.com?WT.mc_id=academic-77998-cacaste) 글로벌 학생 대사 커뮤니티에 참여하세요. 이것이 Microsoft로 들어가는 길이 될 수 있습니다.

**학생 여러분**, 커리큘럼을 사용하는 몇 가지 방법이 있습니다. 먼저, GitHub에서 텍스트를 읽고 코드를 직접 살펴볼 수 있습니다. 노트북에서 코드를 실행하고 싶다면 [실행 방법에 대한 지침](./etc/how-to-run.md)을 읽고, [이 블로그 게시물](https://soshnikov.com/education/how-to-execute-notebooks-from-github/)에서 추가적인 조언을 찾아보세요.

> **Note**: [이 커리큘럼의 코드 실행 방법에 대한 지침](./how-to-run.md)

## 자기주도 학습

만약 이 과정을 자기주도 학습 프로젝트로 진행하고 싶다면, 전체 저장소를 자신의 GitHub 계정으로 포크하고 혼자 또는 그룹과 함께 연습 문제를 완료하는 것을 추천합니다:

* 강의 전 퀴즈로 시작하세요.
* 강의 소개 텍스트를 읽으세요.
* 강의에 추가 노트북이 있다면, 코드를 읽고 실행하며 진행하세요. TensorFlow와 PyTorch 노트북이 모두 제공된다면, 선호하는 프레임워크를 선택해 집중하세요.
* 노트북에는 종종 코드를 약간 수정하여 실험해야 하는 도전 과제가 포함되어 있습니다.
* 강의 후 퀴즈를 진행하세요.
* 모듈에 실습이 포함되어 있다면 과제를 완료하세요.
* [토론 게시판](https://github.com/microsoft/AI-For-Beginners/discussions)을 방문하여 "소리 내어 배우기"를 실천하세요.

> 추가 학습을 위해, [Microsoft Learn](https://docs.microsoft.com/en-us/users/dmitrysoshnikov-9132/collections/31zgizg2p418yo/?WT.mc_id=academic-77998-cacaste) 모듈과 학습 경로를 따라가는 것을 추천합니다.

**교사 여러분**, 이 커리큘럼을 활용하는 방법에 대한 [몇 가지 제안](/for-teachers.md)을 포함시켰습니다.

---

## 교육학

이 커리큘럼을 개발하면서 두 가지 교육학 원칙을 선택했습니다: **프로젝트 기반**으로 실습을 보장하고 **빈번한 퀴즈**를 포함하는 것입니다.

프로젝트와 콘텐츠를 연계함으로써 학생들에게 더 흥미로운 학습 경험을 제공하고 개념의 이해와 기억력을 강화할 수 있습니다. 또한, 수업 전 낮은 부담의 퀴즈는 학생들이 주제를 학습할 의도를 설정하게 하고, 수업 후 두 번째 퀴즈는 추가적인 기억력을 보장합니다. 이 커리큘럼은 유연하고 재미있게 설계되었으며 전체 또는 일부로 진행할 수 있습니다. 프로젝트는 작게 시작하여 12주 과정이 끝날 때 점점 복잡해집니다.

> **퀴즈에 대한 참고 사항**: 모든 퀴즈는 [이 앱](https://red-field-0a6ddfd03.1.azurestaticapps.net/)에 포함되어 있으며, 총 50개의 퀴즈가 각 3문제로 구성되어 있습니다. 퀴즈는 강의 내에서 링크되어 있지만, 퀴즈 앱은 로컬에서 실행할 수 있습니다. `etc/quiz-app` 폴더의 지침을 따르세요.

## 오프라인 접근

[Docsify](https://docsify.js.org/#/)를 사용하여 이 문서를 오프라인에서 실행할 수 있습니다. 이 저장소를 포크하고, [Docsify 설치](https://docsify.js.org/#/quickstart)를 로컬 머신에 진행한 후, 이 저장소의 루트 폴더에서 `docsify serve`를 입력하세요. 웹사이트는 localhost의 포트 3000에서 제공됩니다: `localhost:3000`. 커리큘럼의 PDF는 [이 링크](../../../../../../../../../etc/pdf/readme.pdf)에서 이용 가능합니다.

**면책 조항**:  
이 문서는 AI 번역 서비스 [Co-op Translator](https://github.com/Azure/co-op-translator)를 사용하여 번역되었습니다. 정확성을 위해 최선을 다하고 있지만, 자동 번역에는 오류나 부정확성이 포함될 수 있습니다. 원본 문서의 원어 버전을 권위 있는 출처로 간주해야 합니다. 중요한 정보의 경우, 전문적인 인간 번역을 권장합니다. 이 번역 사용으로 인해 발생하는 오해나 잘못된 해석에 대해 책임을 지지 않습니다.