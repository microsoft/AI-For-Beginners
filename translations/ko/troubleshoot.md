# AI-For-Beginners 문제 해결 가이드

이 가이드는 [AI-For-Beginners](https://github.com/microsoft/AI-For-Beginners) 저장소를 사용하거나 기여하는 동안 발생할 수 있는 일반적인 문제를 해결하는 데 도움을 줍니다. 각 문제는 배경, 증상, 설명, 단계별 해결 방법을 포함합니다.

---

## 목차

- [일반적인 문제](../..)
- [설치 문제](../..)
- [구성 문제](../..)
- [노트북 실행 문제](../..)
- [성능 문제](../..)
- [교재 웹사이트 문제](../..)
- [기여 관련 문제](../..)
- [FAQ](../..)
- [도움 받기](../..)

---

## 일반적인 문제

### 1. 저장소가 제대로 클론되지 않음

**배경:** 클론은 저장소를 로컬 머신으로 복사하는 과정입니다.

**증상:**
- 오류: `fatal: repository not found`
- 오류: `Permission denied (publickey)`

**가능한 원인:**
- 잘못된 저장소 URL
- 권한 부족
- SSH 키가 설정되지 않음

**해결 방법:**
1. **저장소 URL 확인하기**  
   HTTPS URL을 사용하세요:  
   ```
   git clone https://github.com/microsoft/AI-For-Beginners.git
   ```
2. **SSH가 실패하면 HTTPS로 전환하기**  
   `Permission denied (publickey)` 오류가 발생하면 SSH 대신 위의 HTTPS 링크를 사용하세요.
3. **SSH 키 설정하기 (선택 사항)**  
   SSH를 사용하려면 [GitHub의 SSH 가이드](https://docs.github.com/en/authentication/connecting-to-github-with-ssh)를 따르세요.

---

## 설치 문제

### 2. Python 환경 문제

**배경:** 이 저장소는 Python과 다양한 라이브러리에 의존합니다.

**증상:**
- 오류: `ModuleNotFoundError: No module named '<package>'`
- 스크립트나 노트북 실행 시 Import 오류

**가능한 원인:**
- 종속성이 설치되지 않음
- 잘못된 Python 버전

**해결 방법:**
1. **가상 환경 설정하기**  
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```
2. **종속성 설치하기**  
   ```bash
   pip install -r requirements.txt
   ```
3. **Python 버전 확인하기**  
   Python 3.7 이상을 사용하세요.  
   ```bash
   python --version
   ```

### 3. Jupyter가 설치되지 않음

**배경:** 노트북은 핵심 학습 자료입니다.

**증상:**
- 오류: `jupyter: command not found`
- 노트북 실행 실패

**가능한 원인:**
- Jupyter가 설치되지 않음

**해결 방법:**
1. **Jupyter Notebook 설치하기**  
   ```bash
   pip install notebook
   ```
   또는 Anaconda를 사용하는 경우:
   ```bash
   conda install notebook
   ```
2. **Jupyter Notebook 시작하기**  
   ```bash
   jupyter notebook
   ```

### 4. 종속성 버전 충돌

**배경:** 패키지 버전이 맞지 않으면 프로젝트가 중단될 수 있습니다.

**증상:**
- 호환되지 않는 버전에 대한 오류 또는 경고

**가능한 원인:**
- 오래된 또는 충돌하는 Python 패키지

**해결 방법:**
1. **깨끗한 환경에서 설치하기**  
   기존 venv/conda 환경을 삭제하고 새로 생성하세요.
2. **정확한 버전 사용하기**  
   항상 다음을 실행하세요:  
   ```bash
   pip install -r requirements.txt
   ```
   실패할 경우 README에 설명된 대로 누락된 패키지를 수동으로 설치하세요.

---

## 구성 문제

### 5. 환경 변수가 설정되지 않음

**배경:** 일부 모듈은 키, 토큰 또는 구성 설정이 필요합니다.

**증상:**
- 오류: `KeyError` 또는 누락된 구성에 대한 경고

**가능한 원인:**
- 필요한 환경 변수가 설정되지 않음

**해결 방법:**
1. **`.env.example` 또는 유사한 파일 확인하기**
2. **`.env` 파일 생성 후 필요한 값 채우기**
3. **환경 변수를 설정한 후 터미널 또는 IDE 다시 로드하기**

---

## 노트북 실행 문제

### 6. 노트북이 열리지 않거나 실행되지 않음

**배경:** Jupyter 노트북은 적절한 설정이 필요합니다.

**증상:**
- 노트북 실행 실패
- 브라우저가 자동으로 열리지 않음

**가능한 원인:**
- Jupyter가 설치되지 않음
- 브라우저 구성 문제

**해결 방법:**
1. **Jupyter 설치하기 (위 설치 문제 참조)**
2. **노트북을 수동으로 열기**  
   - 터미널에서 URL을 복사하여 브라우저에 붙여넣기 (예: `http://localhost:8888/?token=...`).

### 7. 커널이 충돌하거나 멈춤

**배경:** 노트북 커널은 리소스 제한 또는 코드 오류로 인해 충돌할 수 있습니다.

**증상:**
- 커널이 반복적으로 종료되거나 재시작됨
- 메모리 부족 오류

**가능한 원인:**
- 대규모 데이터셋
- 호환되지 않는 코드 또는 패키지

**해결 방법:**
1. **커널 재시작하기**  
   Jupyter에서 "Restart Kernel" 버튼을 사용하세요.
2. **메모리 사용량 확인하기**  
   사용하지 않는 애플리케이션 닫기.
3. **클라우드 플랫폼에서 노트북 실행하기**  
   [Google Colab](https://colab.research.google.com/) 또는 [Azure Notebooks](https://notebooks.azure.com/) 사용.

---

## 성능 문제

### 8. 노트북 실행 속도가 느림

**배경:** 일부 AI 작업은 많은 메모리와 CPU를 필요로 합니다.

**증상:**
- 실행 속도가 느림
- 노트북 팬 소음 증가

**가능한 원인:**
- 대규모 데이터셋 또는 모델
- 제한된 시스템 리소스

**해결 방법:**
1. **클라우드 플랫폼 사용하기**  
   - 노트북을 Colab 또는 Azure Notebooks에 업로드.
2. **데이터셋 크기 줄이기**  
   - 연습용 샘플 데이터를 사용하세요.
3. **불필요한 프로그램 닫기**  
   - 시스템 RAM 확보.

---

## 교재 웹사이트 문제

### 9. 챕터가 로드되지 않음

**배경:** 온라인 교재는 강의와 챕터를 표시합니다.

**증상:**
- 특정 챕터(예: Transformers/BERT)가 누락되거나 열리지 않음

**알려진 문제:**  
- [Issue #303](https://github.com/microsoft/AI-For-Beginners/issues/303): “18 Transformers. BERT. 교재 웹사이트에서 열리지 않음.” 파일 이름 오류(`READMEtransformers.md` 대신 `README.md`)로 인해 발생.

**해결 방법:**
1. **파일 이름 변경 오류 확인하기**  
   기여자인 경우 챕터 파일 이름이 `README.md`인지 확인하세요.
2. **누락된 파일 보고하기**  
   챕터 이름과 오류 세부 정보를 포함하여 GitHub 이슈를 열기.

---

## 기여 관련 문제

### 10. PR이 승인되지 않거나 빌드 실패

**배경:** 기여는 테스트를 통과하고 가이드라인을 따라야 합니다.

**증상:**
- Pull Request가 거부됨
- CI/CD 파이프라인 오류

**가능한 원인:**
- 테스트 실패
- 코딩 표준을 따르지 않음

**해결 방법:**
1. **기여 가이드라인 읽기**  
   - 저장소의 [CONTRIBUTING.md](https://github.com/microsoft/AI-For-Beginners/blob/main/CONTRIBUTING.md)를 따르세요.
2. **푸시 전에 로컬에서 테스트 실행하기**
3. **Linting 규칙 또는 포맷 요구사항 확인하기**

---

## FAQ

### 특정 모듈에 대한 도움은 어디서 찾을 수 있나요?
- 각 모듈은 일반적으로 자체 README를 가지고 있습니다. 설정 및 사용 팁은 거기서 시작하세요.

### 버그를 보고하거나 기능을 요청하려면 어떻게 해야 하나요?
- [GitHub Issue 열기](https://github.com/microsoft/AI-For-Beginners/issues/new)에서 명확한 설명과 재현 단계를 포함하세요.

### 여기에 나열되지 않은 문제에 대해 도움을 요청할 수 있나요?
- 가능합니다! 기존 이슈를 먼저 검색하고, 문제가 발견되지 않으면 새 이슈를 생성하세요.

---

## 도움 받기

- **이슈 확인:** [GitHub Issues](https://github.com/microsoft/AI-For-Beginners/issues)
- **질문하기:** GitHub Discussions를 사용하거나 이슈를 열기.
- **커뮤니티:** 채팅/포럼 옵션은 저장소 링크에서 확인하세요.

---

_최종 업데이트: 2025-09-20_

---

**면책 조항**:  
이 문서는 AI 번역 서비스 [Co-op Translator](https://github.com/Azure/co-op-translator)를 사용하여 번역되었습니다. 정확성을 위해 최선을 다하고 있으나, 자동 번역에는 오류나 부정확성이 포함될 수 있습니다. 원본 문서의 원어 버전을 신뢰할 수 있는 권위 있는 자료로 간주해야 합니다. 중요한 정보의 경우, 전문적인 인간 번역을 권장합니다. 이 번역 사용으로 인해 발생하는 오해나 잘못된 해석에 대해 당사는 책임을 지지 않습니다.