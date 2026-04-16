# 사전 학습된 대형 언어 모델

이전의 모든 작업에서는 레이블이 지정된 데이터셋을 사용하여 특정 작업을 수행하도록 신경망을 훈련했습니다. BERT와 같은 대형 트랜스포머 모델에서는 자기 지도 학습 방식으로 언어 모델링을 사용하여 언어 모델을 구축한 후, 추가적인 도메인 특화 훈련을 통해 특정 다운스트림 작업에 맞게 전문화합니다. 하지만 대형 언어 모델이 도메인 특화 훈련 없이도 많은 작업을 해결할 수 있다는 것이 입증되었습니다. 이러한 작업을 수행할 수 있는 모델군을 **GPT**(Generative Pre-Trained Transformer)라고 합니다.

## [강의 전 퀴즈](https://ff-quizzes.netlify.app/en/ai/quiz/39)

## 텍스트 생성과 Perplexity

다운스트림 훈련 없이 일반적인 작업을 수행할 수 있는 신경망의 아이디어는 [Language Models are Unsupervised Multitask Learners](https://cdn.openai.com/better-language-models/language_models_are_unsupervised_multitask_learners.pdf) 논문에서 제시되었습니다. 주요 아이디어는 많은 다른 작업이 **텍스트 생성**을 사용하여 모델링될 수 있다는 것입니다. 텍스트를 이해한다는 것은 본질적으로 텍스트를 생성할 수 있다는 것을 의미하기 때문입니다. 모델이 방대한 양의 인간 지식을 포함하는 텍스트로 훈련되었기 때문에 다양한 주제에 대한 지식을 갖추게 됩니다.

> 텍스트를 이해하고 생성할 수 있다는 것은 주변 세계에 대한 지식을 갖추고 있다는 것을 의미합니다. 사람들도 독서를 통해 많은 것을 배우며, GPT 네트워크도 이와 유사한 방식으로 학습합니다.

텍스트 생성 네트워크는 다음 단어의 확률 $$P(w_N)$$을 예측함으로써 작동합니다. 그러나 다음 단어의 무조건적 확률은 텍스트 코퍼스에서 해당 단어의 빈도와 같습니다. GPT는 이전 단어를 기반으로 한 다음 단어의 **조건부 확률**을 제공합니다: $$P(w_N | w_{n-1}, ..., w_0)$$

> 확률에 대해 더 알고 싶다면 [Data Science for Beginners Curriculum](https://github.com/microsoft/Data-Science-For-Beginners/tree/main/1-Introduction/04-stats-and-probability)을 참고하세요.

언어 생성 모델의 품질은 **perplexity**를 사용하여 정의할 수 있습니다. 이는 특정 작업 데이터셋 없이 모델 품질을 측정할 수 있는 내재적 지표입니다. *문장의 확률* 개념에 기반하며, 모델은 현실적일 가능성이 높은 문장에 높은 확률을 부여하고, 덜 의미 있는 문장(예: *Can it does what?*)에는 낮은 확률을 부여합니다. 모델에 실제 텍스트 코퍼스의 문장을 제공하면 높은 확률과 낮은 **perplexity**를 기대할 수 있습니다. 수학적으로는 테스트 세트의 정규화된 역확률로 정의됩니다:
$$
\mathrm{Perplexity}(W) = \sqrt[N]{1\over P(W_1,...,W_N)}
$$ 

**[Hugging Face의 GPT 기반 텍스트 편집기](https://transformer.huggingface.co/doc/gpt2-large)**를 사용하여 텍스트 생성을 실험해볼 수 있습니다. 이 편집기에서 텍스트를 작성한 후 **[TAB]** 키를 누르면 여러 완성 옵션이 제공됩니다. 옵션이 너무 짧거나 만족스럽지 않다면 [TAB]을 다시 눌러 더 긴 텍스트를 포함한 추가 옵션을 확인할 수 있습니다.

## GPT는 하나의 모델이 아닌 가족

GPT는 단일 모델이 아니라 [OpenAI](https://openai.com)가 개발하고 훈련한 모델들의 집합입니다.

GPT 모델에는 다음이 포함됩니다:

| [GPT-2](https://huggingface.co/docs/transformers/model_doc/gpt2#openai-gpt2) | [GPT-3](https://openai.com/research/language-models-are-few-shot-learners) | [GPT-4](https://openai.com/gpt-4) |
| -- | -- | -- |
|최대 15억 개의 파라미터를 가진 언어 모델 | 최대 1750억 개의 파라미터를 가진 언어 모델 | 100조 개의 파라미터를 가지며 이미지와 텍스트 입력을 받아 텍스트를 출력 |


GPT-3와 GPT-4 모델은 [Microsoft Azure의 인지 서비스](https://azure.microsoft.com/en-us/services/cognitive-services/openai-service/#overview?WT.mc_id=academic-77998-cacaste)와 [OpenAI API](https://openai.com/api)를 통해 사용할 수 있습니다.

## 프롬프트 엔지니어링

GPT는 방대한 데이터로 언어와 코드를 이해하도록 훈련되었기 때문에 입력(프롬프트)에 대한 응답으로 출력을 제공합니다. 프롬프트는 GPT에 제공하는 입력 또는 쿼리로, 모델에게 다음에 수행할 작업에 대한 지침을 제공합니다. 원하는 결과를 얻으려면 가장 효과적인 프롬프트가 필요하며, 이는 적절한 단어, 형식, 구문 또는 심지어 기호를 선택하는 것을 포함합니다. 이러한 접근법을 [프롬프트 엔지니어링](https://learn.microsoft.com/en-us/shows/ai-show/the-basics-of-prompt-engineering-with-azure-openai-service?WT.mc_id=academic-77998-bethanycheum)이라고 합니다.

[이 문서](https://learn.microsoft.com/en-us/semantic-kernel/prompt-engineering/?WT.mc_id=academic-77998-bethanycheum)는 프롬프트 엔지니어링에 대한 추가 정보를 제공합니다.

## ✍️ 예제 노트북: [OpenAI-GPT 활용하기](GPT-PyTorch.ipynb)

다음 노트북에서 학습을 이어가세요:

* [OpenAI-GPT와 Hugging Face Transformers를 사용한 텍스트 생성](GPT-PyTorch.ipynb)

## 결론

새로운 일반 사전 학습 언어 모델은 단순히 언어 구조를 모델링하는 것뿐만 아니라 방대한 자연 언어를 포함하고 있습니다. 따라서 이러한 모델은 일부 NLP 작업을 제로샷 또는 퓨샷 설정에서 효과적으로 해결할 수 있습니다.

## [강의 후 퀴즈](https://ff-quizzes.netlify.app/en/ai/quiz/40)

---

