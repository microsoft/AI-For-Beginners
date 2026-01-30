# AGENTS.md

## 프로젝트 개요

AI for Beginners는 인공지능 기초를 다루는 12주, 24강의 종합 커리큘럼입니다. 이 교육용 저장소는 Jupyter Notebooks, 퀴즈, 실습을 포함한 실질적인 학습 자료를 제공합니다. 커리큘럼은 다음을 포함합니다:

- 지식 표현 및 전문가 시스템을 활용한 기호 기반 AI
- TensorFlow와 PyTorch를 활용한 신경망 및 딥러닝
- 컴퓨터 비전 기술 및 아키텍처
- 변환기(transformers)와 BERT를 포함한 자연어 처리(NLP)
- 특화 주제: 유전 알고리즘, 강화 학습, 다중 에이전트 시스템
- AI 윤리 및 책임 있는 AI 원칙

**주요 기술:** Python 3, Jupyter Notebooks, TensorFlow, PyTorch, Keras, OpenCV, Vue.js (퀴즈 앱용)

**아키텍처:** 주제별로 구성된 Jupyter Notebooks와 Vue.js 기반 퀴즈 애플리케이션, 다국어 지원을 포함한 교육 콘텐츠 저장소

## 설정 명령어

### 주요 개발 환경 (Python/Jupyter)

이 커리큘럼은 Python과 Jupyter Notebooks에서 실행되도록 설계되었습니다. 권장 방법은 miniconda를 사용하는 것입니다:

```bash
# Clone the repository
git clone https://github.com/microsoft/ai-for-beginners
cd ai-for-beginners

# Create and activate conda environment
conda env create --name ai4beg --file environment.yml
conda activate ai4beg

# Start Jupyter Notebook
jupyter notebook
# OR
jupyter lab
```

### 대안: devcontainer 사용

```bash
# Open in VS Code and select "Reopen in Container" when prompted
# The devcontainer will automatically set up the environment
```

### 퀴즈 애플리케이션 설정

퀴즈 앱은 `etc/quiz-app/`에 위치한 별도의 Vue.js 애플리케이션입니다:

```bash
cd etc/quiz-app
npm install
npm run serve  # Development server
npm run build  # Production build
npm run lint   # Lint and fix files
```

## 개발 워크플로우

### Jupyter Notebooks 작업

1. **로컬 개발:**
   - conda 환경 활성화: `conda activate ai4beg`
   - Jupyter 시작: `jupyter notebook` 또는 `jupyter lab`
   - 강의 폴더로 이동하여 `.ipynb` 파일 열기
   - 셀을 인터랙티브하게 실행하며 강의 따라가기

2. **VS Code와 Python 확장 사용:**
   - VS Code에서 저장소 열기
   - Python 확장 설치
   - VS Code가 conda 환경을 자동으로 감지 및 사용
   - `.ipynb` 파일을 VS Code에서 직접 열기

3. **클라우드 개발:**
   - **GitHub Codespaces:** "Code" → "Codespaces" → "Create codespace on main" 클릭
   - **Binder:** README의 Binder 배지를 사용하여 브라우저에서 실행
   - 참고: Binder는 리소스가 제한적이며 일부 웹 액세스 제한이 있음

### 고급 강의를 위한 GPU 지원

후반부 강의는 GPU 가속의 이점을 크게 누릴 수 있습니다:

- **Azure Data Science VM:** GPU 지원이 있는 NC 시리즈 VM 사용
- **Azure Machine Learning:** GPU 컴퓨팅 기능이 있는 노트북 사용
- **Google Colab:** 개별 노트북 업로드 (무료 GPU 지원 제공)

### 퀴즈 앱 개발

```bash
cd etc/quiz-app
npm run serve  # Hot-reload development server at http://localhost:8080
```

## 테스트 지침

이 저장소는 학습 콘텐츠에 중점을 두고 있으며 소프트웨어 테스트를 위한 전통적인 테스트 스위트는 없습니다.

### 검증 방법:

1. **Jupyter Notebooks:** 셀을 순차적으로 실행하여 코드 예제가 작동하는지 확인
2. **퀴즈 앱 테스트:** 개발 서버를 통한 수동 테스트
3. **번역 검증:** `translations/` 폴더의 번역된 콘텐츠 확인
4. **퀴즈 앱 린팅:** `etc/quiz-app/`에서 `npm run lint` 실행

### 코드 예제 실행:

```bash
# Activate environment first
conda activate ai4beg

# Run Python scripts directly
python lessons/4-ComputerVision/07-ConvNets/pytorchcv.py

# Or execute notebooks
jupyter notebook lessons/3-NeuralNetworks/03-Perceptron/Perceptron.ipynb
```

## 코드 스타일

### Python 코드 스타일

- 교육용 코드에 적합한 표준 Python 규칙
- 최적화보다는 학습에 중점을 둔 명확하고 읽기 쉬운 코드
- 주요 개념을 설명하는 주석
- Jupyter Notebook 친화적: 가능한 한 셀이 독립적이어야 함
- 강의 콘텐츠에 대해 엄격한 린팅 요구 사항 없음

### JavaScript/Vue.js (퀴즈 앱)

- `etc/quiz-app/package.json`에 ESLint 구성
- `npm run lint` 실행하여 문제 확인 및 자동 수정
- Vue 2.x 규칙 준수
- 컴포넌트 기반 아키텍처

### 파일 구성

```
lessons/
  ├── 0-course-setup/          # Setup instructions
  ├── 1-Intro/                 # Introduction to AI
  ├── 2-Symbolic/              # Symbolic AI
  ├── 3-NeuralNetworks/        # Neural Networks basics
  ├── 4-ComputerVision/        # Computer Vision
  ├── 5-NLP/                   # Natural Language Processing
  ├── 6-Other/                 # Other AI techniques
  ├── 7-Ethics/                # AI Ethics
  └── X-Extras/                # Additional content

etc/
  ├── quiz-app/                # Vue.js quiz application
  └── quiz-src/                # Quiz source files

translations/                  # Multi-language translations
```

## 빌드 및 배포

### Jupyter 콘텐츠

빌드 프로세스가 필요하지 않음 - Jupyter Notebooks는 직접 실행됩니다.

### 퀴즈 애플리케이션

```bash
cd etc/quiz-app

# Development
npm run serve

# Production build
npm run build  # Outputs to etc/quiz-app/dist/

# Deploy to Azure Static Web Apps
# Azure automatically creates GitHub Actions workflow
# See etc/quiz-app/README.md for detailed deployment instructions
```

### 문서 사이트

이 저장소는 Docsify를 사용하여 문서를 제공합니다:
- `index.html`이 진입점으로 사용됨
- 빌드가 필요하지 않음 - GitHub Pages를 통해 직접 제공됨
- 액세스: https://microsoft.github.io/AI-For-Beginners/

## 기여 가이드라인

### Pull Request 프로세스

1. **제목 형식:** 변경 사항을 명확히 설명하는 제목
2. **CLA 요구 사항:** Microsoft CLA 서명 필요 (자동 확인)
3. **콘텐츠 가이드라인:**
   - 교육적 초점과 초보자 친화적 접근 유지
   - 노트북의 모든 코드 예제 테스트
   - 노트북이 처음부터 끝까지 실행되도록 보장
   - 영어 콘텐츠를 수정할 경우 번역 업데이트
4. **퀴즈 앱 변경 사항:** 커밋 전에 `npm run lint` 실행

### 번역 기여

- 번역은 GitHub Actions를 통해 자동화됨 (co-op-translator 사용)
- 수동 번역은 `translations/<language-code>/`에 저장
- 퀴즈 번역은 `etc/quiz-app/src/assets/translations/`에 저장
- 지원 언어: 40개 이상 (전체 목록은 README 참조)

### 활성 기여 영역

현재 필요 사항은 `etc/CONTRIBUTING.md`를 참조:
- 심층 강화 학습 섹션
- 객체 탐지 개선
- 개체명 인식 예제
- 사용자 정의 임베딩 학습 샘플

## 환경 구성

### 필수 종속성

```bash
# Core Python packages (from requirements.txt)
tensorflow==2.17.0
torch (via conda)
torchvision (via conda)
keras==3.5.0
opencv (via conda)
scikit-learn
numpy==1.26
pandas==2.2.2
matplotlib==3.9
jupyter
```

### 환경 변수

기본 사용을 위한 특별한 환경 변수가 필요하지 않음.

Azure 배포(퀴즈 앱)의 경우:
- `AZURE_STATIC_WEB_APPS_API_TOKEN` (Azure에서 자동 설정)

## 디버깅 및 문제 해결

### 일반적인 문제

**문제:** Conda 환경 생성 실패
- **해결 방법:** 먼저 conda 업데이트: `conda update conda -y`
- 충분한 디스크 공간 확보 (50GB 권장)

**문제:** Jupyter 커널을 찾을 수 없음
- **해결 방법:** 
  ```bash
  conda activate ai4beg
  python -m ipykernel install --user --name ai4beg
  ```

**문제:** 노트북에서 GPU가 감지되지 않음
- **해결 방법:** 
  - CUDA 설치 확인: `nvidia-smi`
  - PyTorch GPU 확인: `python -c "import torch; print(torch.cuda.is_available())"`
  - TensorFlow GPU 확인: `python -c "import tensorflow as tf; print(tf.config.list_physical_devices('GPU'))"`

**문제:** 퀴즈 앱이 시작되지 않음
- **해결 방법:**
  ```bash
  cd etc/quiz-app
  rm -rf node_modules package-lock.json
  npm install
  npm run serve
  ```

**문제:** Binder가 시간 초과되거나 다운로드를 차단함
- **해결 방법:** 더 나은 리소스 액세스를 위해 GitHub Codespaces 또는 로컬 설정 사용

### 메모리 문제

일부 강의는 상당한 RAM(8GB 이상 권장)을 요구합니다:
- 리소스 집약적인 강의를 위해 클라우드 VM 사용
- 모델 학습 시 다른 애플리케이션 닫기
- 메모리가 부족할 경우 노트북에서 배치 크기 줄이기

## 추가 참고 사항

### 강사용

- 강의 지침은 `lessons/0-course-setup/for-teachers.md` 참조
- 강의는 독립적으로 구성되어 있으며 순서대로 또는 개별적으로 진행 가능
- 예상 소요 시간: 주당 2강 기준 12주

### 클라우드 리소스

- **Azure for Students:** 학생을 위한 무료 크레딧 제공
- **Microsoft Learn:** 학습 경로가 강의 전반에 걸쳐 연결됨
- **Binder:** 무료이지만 리소스 제한 및 일부 네트워크 제한 존재

### 코드 실행 옵션

1. **로컬 (권장):** 완전한 제어, 최고의 성능, GPU 지원
2. **GitHub Codespaces:** 클라우드 기반 VS Code, 빠른 액세스에 적합
3. **Binder:** 브라우저 기반 Jupyter, 무료이지만 제한적
4. **Azure ML Notebooks:** GPU 지원이 포함된 엔터프라이즈 옵션
5. **Google Colab:** 개별 노트북 업로드, 무료 GPU 계층 제공

### 노트북 작업

- 노트북은 학습을 위해 셀 단위로 실행되도록 설계됨
- 많은 노트북이 첫 실행 시 데이터셋을 다운로드함 (시간 소요 가능)
- 일부 모델은 합리적인 학습 시간을 위해 GPU가 필요함
- 사전 학습된 모델을 사용하여 컴퓨팅 요구 사항 감소

### 성능 고려 사항

- 후반부 컴퓨터 비전 강의(CNN, GAN)는 GPU의 이점을 누림
- NLP 변환기 강의는 상당한 RAM이 필요할 수 있음
- 처음부터 학습은 교육적이지만 시간이 많이 소요됨
- 전이 학습 예제는 학습 시간을 최소화함

---

**면책 조항**:  
이 문서는 AI 번역 서비스 [Co-op Translator](https://github.com/Azure/co-op-translator)를 사용하여 번역되었습니다. 정확성을 위해 최선을 다하고 있으나, 자동 번역에는 오류나 부정확성이 포함될 수 있습니다. 원본 문서의 원어 버전이 권위 있는 출처로 간주되어야 합니다. 중요한 정보의 경우, 전문적인 인간 번역을 권장합니다. 이 번역 사용으로 인해 발생하는 오해나 잘못된 해석에 대해 당사는 책임을 지지 않습니다.