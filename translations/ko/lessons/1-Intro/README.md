<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "5d1cbc67a9690adb5b33adf297794087",
  "translation_date": "2025-08-24T21:27:23+00:00",
  "source_file": "lessons/1-Intro/README.md",
  "language_code": "ko"
}
-->
> 이미지 제공: [Dmitry Soshnikov](http://soshnikov.com)

시간이 지나면서 컴퓨팅 자원이 저렴해지고 더 많은 데이터가 이용 가능해지면서, 신경망 접근법이 컴퓨터 비전이나 음성 이해와 같은 여러 분야에서 인간과 경쟁하며 뛰어난 성과를 보여주기 시작했습니다. 지난 10년 동안, 인공지능이라는 용어는 대부분 신경망의 동의어로 사용되었는데, 우리가 듣는 대부분의 AI 성공 사례가 신경망을 기반으로 하고 있기 때문입니다.

체스 프로그램 개발에서 접근 방식이 어떻게 변화했는지 살펴볼 수 있습니다:

* 초기 체스 프로그램은 검색 기반으로 작동했습니다. 프로그램은 주어진 몇 번의 다음 수에서 상대방의 가능한 움직임을 명시적으로 추정하고, 몇 번의 움직임 후에 달성할 수 있는 최적의 위치를 기반으로 최적의 움직임을 선택했습니다. 이는 [알파-베타 가지치기](https://en.wikipedia.org/wiki/Alpha%E2%80%93beta_pruning) 검색 알고리즘 개발로 이어졌습니다.
* 검색 전략은 가능한 움직임의 수가 제한된 게임 후반부에서는 잘 작동하지만, 게임 초반부에서는 검색 공간이 방대하여 알고리즘을 인간 플레이어 간의 기존 경기에서 학습하도록 개선할 수 있습니다. 이후 실험에서는 [사례 기반 추론](https://en.wikipedia.org/wiki/Case-based_reasoning)을 사용하여 프로그램이 게임의 현재 위치와 매우 유사한 사례를 지식 기반에서 찾도록 했습니다.
* 인간 플레이어를 능가하는 현대 프로그램은 신경망과 [강화 학습](https://en.wikipedia.org/wiki/Reinforcement_learning)을 기반으로 하며, 프로그램이 오랜 시간 동안 스스로 경기를 하며 자신의 실수로부터 학습하는 방식으로 작동합니다. 이는 인간이 체스를 배우는 방식과 매우 유사하지만, 컴퓨터 프로그램은 훨씬 더 많은 경기를 훨씬 짧은 시간 안에 플레이할 수 있어 훨씬 빠르게 학습할 수 있습니다.

✅ AI가 플레이한 다른 게임에 대해 조사해 보세요.

마찬가지로 "대화형 프로그램"(튜링 테스트를 통과할 가능성이 있는 프로그램)을 만드는 접근 방식이 어떻게 변화했는지 볼 수 있습니다:

* [Eliza](https://en.wikipedia.org/wiki/ELIZA)와 같은 초기 프로그램은 매우 간단한 문법 규칙과 입력 문장을 질문으로 재구성하는 방식에 기반했습니다.
* Cortana, Siri, Google Assistant와 같은 현대적인 비서들은 음성을 텍스트로 변환하고 사용자의 의도를 인식하기 위해 신경망을 사용하는 하이브리드 시스템이며, 이후 필요한 작업을 수행하기 위해 일부 추론 또는 명시적 알고리즘을 사용합니다.
* 미래에는 대화 자체를 처리할 수 있는 완전한 신경망 기반 모델을 기대할 수 있습니다. 최근 GPT 및 [Turing-NLG](https://turing.microsoft.com/) 계열의 신경망은 이 분야에서 큰 성공을 보여주고 있습니다.

> 이미지 제공: Dmitry Soshnikov, [사진](https://unsplash.com/photos/r8LmVbUKgns) 제공: [Marina Abrosimova](https://unsplash.com/@abrosimova_marina_foto), Unsplash

## 최근 AI 연구

신경망 연구의 최근 급격한 성장은 2010년경 대규모 공개 데이터셋이 이용 가능해지면서 시작되었습니다. 약 1,400만 개의 주석이 달린 이미지를 포함한 방대한 이미지 컬렉션인 [ImageNet](https://en.wikipedia.org/wiki/ImageNet)은 [ImageNet 대규모 시각 인식 챌린지](https://image-net.org/challenges/LSVRC/)의 탄생을 이끌었습니다.

![ILSVRC 정확도](../../../../lessons/1-Intro/images/ilsvrc.gif)

> 이미지 제공: [Dmitry Soshnikov](http://soshnikov.com)

2012년, [합성곱 신경망(Convolutional Neural Networks)](../4-ComputerVision/07-ConvNets/README.md)이 처음으로 이미지 분류에 사용되었고, 이로 인해 분류 오류율이 크게 감소했습니다(약 30%에서 16.4%로). 2015년에는 Microsoft Research의 ResNet 아키텍처가 [인간 수준의 정확도](https://doi.org/10.1109/ICCV.2015.123)를 달성했습니다.

그 이후로 신경망은 다양한 작업에서 매우 성공적인 성과를 보여주었습니다:

---

연도 | 인간 수준 성과 달성
-----|-------------------
2015 | [이미지 분류](https://doi.org/10.1109/ICCV.2015.123)
2016 | [대화형 음성 인식](https://arxiv.org/abs/1610.05256)
2018 | [자동 기계 번역](https://arxiv.org/abs/1803.05567) (중국어-영어)
2020 | [이미지 캡셔닝](https://arxiv.org/abs/2009.13682)

최근 몇 년 동안 BERT와 GPT-3와 같은 대규모 언어 모델의 엄청난 성공을 목격했습니다. 이는 주로 일반 텍스트 데이터가 풍부하게 존재하여 모델이 텍스트의 구조와 의미를 학습할 수 있도록 하고, 일반 텍스트 컬렉션에서 사전 학습한 후 특정 작업에 맞게 모델을 전문화할 수 있었기 때문입니다. 이 과정에서 [자연어 처리(Natural Language Processing)](../5-NLP/README.md)에 대해 더 자세히 배울 것입니다.

## 🚀 도전 과제

인터넷을 탐색하며 AI가 가장 효과적으로 사용되고 있다고 생각되는 분야를 찾아보세요. 지도 앱, 음성-텍스트 변환 서비스, 비디오 게임 중 어디일까요? 해당 시스템이 어떻게 구축되었는지 조사해보세요.

## [강의 후 퀴즈](https://ff-quizzes.netlify.app/en/ai/quiz/2)

## 복습 및 자기 학습

[이 강의](https://github.com/microsoft/ML-For-Beginners/tree/main/1-Introduction/2-history-of-ML)를 읽으며 AI와 ML의 역사를 복습하세요. 해당 강의나 이 강의 상단의 스케치노트에서 하나의 요소를 선택하여, 그것의 진화에 영향을 미친 문화적 맥락을 더 깊이 이해하기 위해 연구해보세요.

**과제**: [게임 잼](assignment.md)

**면책 조항**:  
이 문서는 AI 번역 서비스 [Co-op Translator](https://github.com/Azure/co-op-translator)를 사용하여 번역되었습니다. 정확성을 위해 최선을 다하고 있지만, 자동 번역에는 오류나 부정확성이 포함될 수 있습니다. 원본 문서의 원어 버전을 권위 있는 출처로 간주해야 합니다. 중요한 정보의 경우, 전문적인 인간 번역을 권장합니다. 이 번역 사용으로 인해 발생하는 오해나 잘못된 해석에 대해 책임을 지지 않습니다.