# 퀴즈

이 퀴즈는 https://aka.ms/ai-beginners의 AI 커리큘럼을 위한 강의 전후 퀴즈입니다.

## 번역된 퀴즈 세트 추가하기

`assets/translations` 폴더에 맞는 퀴즈 구조를 생성하여 퀴즈 번역을 추가하세요. 표준 퀴즈는 `assets/translations/en`에 있습니다. 퀴즈는 수업별로 여러 그룹으로 나뉘어 있습니다. 적절한 퀴즈 섹션에 맞춰 번호를 정렬하세요. 이 커리큘럼에는 총 40개의 퀴즈가 있으며, 카운트는 0부터 시작합니다.

번역을 편집한 후, 번역 폴더의 index.js 파일을 수정하여 `en`의 규칙에 따라 모든 파일을 가져오세요.

`index.js` 파일을 `assets/translations`에서 수정하여 새로 번역된 파일을 가져옵니다.

그런 다음, 이 앱의 `App.vue`에서 드롭다운을 수정하여 귀하의 언어를 추가하세요. 지역화된 약어를 귀하의 언어 폴더 이름과 일치시킵니다.

마지막으로, 번역된 수업에서 퀴즈 링크가 존재하는 경우, 이 지역화를 쿼리 매개변수로 포함하도록 모든 퀴즈 링크를 수정하세요: 예를 들어 `?loc=fr`.

## 프로젝트 설정

```
npm install
```

### 개발을 위한 컴파일 및 핫 리로드

```
npm run serve
```

### 프로덕션을 위한 컴파일 및 최소화

```
npm run build
```

### 파일 린트 및 수정

```
npm run lint
```

### 구성 사용자화

[구성 참조](https://cli.vuejs.org/config/)를 참조하세요.

크레딧: 이 퀴즈 앱의 원본 버전 덕분입니다: https://github.com/arpan45/simple-quiz-vue

## Azure에 배포하기

시작하는 데 도움이 되는 단계별 가이드입니다:

1. GitHub 저장소 포크하기
정적 웹 앱 코드가 GitHub 저장소에 있는지 확인하세요. 이 저장소를 포크합니다.

2. Azure 정적 웹 앱 만들기
- [Azure 계정](http://azure.microsoft.com) 만들기
- [Azure 포털](https://portal.azure.com)로 이동
- "리소스 만들기"를 클릭하고 "정적 웹 앱"을 검색합니다.
- "만들기"를 클릭합니다.

3. 정적 웹 앱 구성
- 기본: 구독: 귀하의 Azure 구독을 선택합니다.
- 리소스 그룹: 새 리소스 그룹을 만들거나 기존 리소스를 사용합니다.
- 이름: 정적 웹 앱의 이름을 제공합니다.
- 지역: 사용자와 가장 가까운 지역을 선택합니다.

- #### 배포 세부정보:
- 소스: "GitHub"를 선택합니다.
- GitHub 계정: Azure가 귀하의 GitHub 계정에 접근할 수 있도록 권한을 부여합니다.
- 조직: 귀하의 GitHub 조직을 선택합니다.
- 저장소: 정적 웹 앱이 포함된 저장소를 선택합니다.
- 브랜치: 배포할 브랜치를 선택합니다.

- #### 빌드 세부정보:
- 빌드 프리셋: 앱이 구축된 프레임워크를 선택합니다 (예: React, Angular, Vue 등).
- 앱 위치: 앱 코드가 포함된 폴더를 지정합니다 (예: 루트에 있는 경우 /).
- API 위치: API가 있는 경우 위치를 지정합니다 (선택 사항).
- 출력 위치: 빌드 출력이 생성되는 폴더를 지정합니다 (예: build 또는 dist).

4. 검토 및 생성
설정을 검토하고 "생성"을 클릭합니다. Azure는 필요한 리소스를 설정하고 귀하의 저장소에 GitHub Actions 워크플로를 생성합니다.

5. GitHub Actions 워크플로
Azure는 귀하의 저장소에 GitHub Actions 워크플로 파일을 자동으로 생성합니다 (.github/workflows/azure-static-web-apps-<name>.yml). 이 워크플로는 빌드 및 배포 프로세스를 처리합니다.

6. 배포 모니터링
GitHub 저장소의 "작업" 탭으로 이동합니다.
워크플로가 실행되고 있어야 합니다. 이 워크플로는 귀하의 정적 웹 앱을 Azure에 빌드하고 배포합니다.
워크플로가 완료되면, 귀하의 앱은 제공된 Azure URL에서 실시간으로 사용할 수 있습니다.

### 예시 워크플로 파일

다음은 GitHub Actions 워크플로 파일의 예시입니다:
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

### 추가 자료
- [Azure Static Web Apps 문서](https://learn.microsoft.com/azure/static-web-apps/getting-started)
- [GitHub Actions 문서](https://docs.github.com/actions/use-cases-and-examples/deploying/deploying-to-azure-static-web-app)

**면책 조항**:  
이 문서는 기계 기반 AI 번역 서비스를 사용하여 번역되었습니다. 정확성을 위해 노력하고 있지만, 자동 번역에는 오류나 부정확성이 포함될 수 있음을 유의하시기 바랍니다. 원본 문서는 해당 언어로 된 권위 있는 출처로 간주되어야 합니다. 중요한 정보에 대해서는 전문적인 인간 번역을 권장합니다. 이 번역의 사용으로 인해 발생하는 오해나 잘못된 해석에 대해서는 저희가 책임지지 않습니다.