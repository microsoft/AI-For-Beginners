# 초보자를 위한 AI 예제

환영합니다! 이 디렉토리에는 AI와 머신러닝을 시작하는 데 도움을 주기 위한 간단하고 독립적인 예제가 포함되어 있습니다. 각 예제는 초보자가 쉽게 이해할 수 있도록 상세한 주석과 단계별 설명을 제공합니다.

## 📚 예제 개요

| 예제 | 설명 | 난이도 | 선행 조건 |
|------|------|--------|-----------|
| [Hello AI World](../../../examples/01-hello-ai-world.py) | 첫 번째 AI 프로그램 - 간단한 패턴 인식 | ⭐ 초보자 | Python 기본 |
| [Simple Neural Network](../../../examples/02-simple-neural-network.py) | 신경망을 처음부터 직접 구축하기 | ⭐⭐ 초보자+ | Python, 기본 수학 |
| [Image Classifier](./03-image-classifier.ipynb) | 사전 학습된 모델로 이미지 분류하기 | ⭐⭐ 초보자+ | Python, numpy |
| [Text Sentiment](../../../examples/04-text-sentiment.py) | 텍스트 감정 분석 (긍정/부정) | ⭐⭐ 초보자+ | Python |

## 🚀 시작하기

### 선행 조건

Python이 설치되어 있는지 확인하세요 (권장 버전: 3.8 이상). 필요한 패키지를 설치하세요:

```bash
# For Python scripts
pip install numpy

# For Jupyter notebooks (image classifier)
pip install jupyter numpy pillow tensorflow
```

또는 메인 커리큘럼의 conda 환경을 사용하세요:

```bash
conda env create --name ai4beg --file ../environment.yml
conda activate ai4beg
```

### 예제 실행 방법

**Python 스크립트 (.py 파일):**
```bash
python 01-hello-ai-world.py
```

**Jupyter 노트북 (.ipynb 파일):**
```bash
jupyter notebook 03-image-classifier.ipynb
```

## 📖 학습 경로

예제를 순서대로 따라가는 것을 추천합니다:

1. **"Hello AI World"부터 시작하세요** - 패턴 인식의 기본을 배워보세요
2. **간단한 신경망 구축하기** - 신경망의 작동 원리를 이해하세요
3. **이미지 분류기 시도하기** - 실제 이미지를 활용한 AI를 경험하세요
4. **텍스트 감정 분석하기** - 자연어 처리 탐구하기

## 💡 초보자를 위한 팁

- **코드 주석을 꼼꼼히 읽으세요** - 각 줄이 무엇을 하는지 설명합니다
- **실험해보세요!** - 값을 변경해보고 결과를 확인하세요
- **모든 것을 이해하려고 걱정하지 마세요** - 학습은 시간이 걸립니다
- **질문하세요** - [토론 게시판](https://github.com/microsoft/AI-For-Beginners/discussions)을 활용하세요

## 🔗 다음 단계

이 예제를 완료한 후, 전체 커리큘럼을 탐색해보세요:
- [AI 소개](../lessons/1-Intro/README.md)
- [신경망](../lessons/3-NeuralNetworks/README.md)
- [컴퓨터 비전](../lessons/4-ComputerVision/README.md)
- [자연어 처리](../lessons/5-NLP/README.md)

## 🤝 기여하기

이 예제가 도움이 되었나요? 개선에 참여하세요:
- 문제를 보고하거나 개선 사항을 제안하세요
- 초보자를 위한 더 많은 예제를 추가하세요
- 문서와 주석을 개선하세요

---

*기억하세요: 모든 전문가도 한때는 초보자였습니다. 즐거운 학습 되세요! 🎓*

---

**면책 조항**:  
이 문서는 AI 번역 서비스 [Co-op Translator](https://github.com/Azure/co-op-translator)를 사용하여 번역되었습니다. 정확성을 위해 최선을 다하고 있으나, 자동 번역에는 오류나 부정확성이 포함될 수 있습니다. 원본 문서(원어로 작성된 문서)를 권위 있는 자료로 간주해야 합니다. 중요한 정보의 경우, 전문 번역가에 의한 번역을 권장합니다. 이 번역 사용으로 인해 발생하는 오해나 잘못된 해석에 대해 당사는 책임을 지지 않습니다.