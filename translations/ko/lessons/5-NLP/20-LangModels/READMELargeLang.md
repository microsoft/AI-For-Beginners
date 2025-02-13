# 사전 훈련된 대규모 언어 모델

이전의 모든 작업에서 우리는 레이블이 붙은 데이터 세트를 사용하여 특정 작업을 수행하도록 신경망을 훈련시켰습니다. BERT와 같은 대규모 변환기 모델을 사용하여 우리는 자가 지도 방식으로 언어 모델을 구축하고, 이후 특정 도메인에 맞춘 추가 훈련을 통해 특정 다운스트림 작업에 특화시킵니다. 그러나 대규모 언어 모델이 도메인 특정 훈련 없이도 많은 작업을 해결할 수 있다는 것이 입증되었습니다. 이를 수행할 수 있는 모델의 집합을 **GPT**(Generative Pre-Trained Transformer)라고 합니다.

## [강의 전 퀴즈](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/120)

## 텍스트 생성 및 당혹감

신경망이 다운스트림 훈련 없이 일반 작업을 수행할 수 있다는 아이디어는 [Language Models are Unsupervised Multitask Learners](https://cdn.openai.com/better-language-models/language_models_are_unsupervised_multitask_learners.pdf) 논문에 제시되었습니다. 주요 아이디어는 많은 다른 작업이 **텍스트 생성**을 사용하여 모델링될 수 있다는 것입니다. 텍스트를 이해한다는 것은 본질적으로 그것을 생성할 수 있다는 것을 의미합니다. 모델은 인간 지식을 포함하는 방대한 양의 텍스트에서 훈련되기 때문에 다양한 주제에 대한 지식을 갖추게 됩니다.

> 텍스트를 이해하고 생성할 수 있다는 것은 우리 주변 세계에 대한 지식을 갖추는 것을 의미합니다. 사람들도 대체로 독서를 통해 배웁니다. GPT 네트워크는 이 점에서 유사합니다.

텍스트 생성 네트워크는 다음 단어 $$P(w_N)$$의 확률을 예측하는 방식으로 작동합니다. 그러나 다음 단어의 무조건적 확률은 이 단어가 텍스트 말뭉치에서 나타나는 빈도와 같습니다. GPT는 이전 단어들을 고려하여 다음 단어의 **조건부 확률**을 제공할 수 있습니다: $$P(w_N | w_{n-1}, ..., w_0)$$

> 확률에 대한 자세한 내용은 [Data Science for Beginners Curriculum](https://github.com/microsoft/Data-Science-For-Beginners/tree/main/1-Introduction/04-stats-and-probability)에서 확인할 수 있습니다.

언어 생성 모델의 품질은 **당혹감**(perplexity)으로 정의할 수 있습니다. 이는 작업 특정 데이터 세트 없이 모델 품질을 측정할 수 있는 내재적 메트릭입니다. 이는 *문장의 확률* 개념에 기반하여 모델이 실제일 가능성이 높은 문장에 높은 확률을 부여하고(즉, 모델이 그것에 대해 **당혹스럽지 않음**), 덜 의미 있는 문장에는 낮은 확률을 부여합니다(예: *Can it does what?*). 모델에 실제 텍스트 말뭉치에서 문장을 제공할 때 우리는 그들이 높은 확률과 낮은 **당혹감**을 가질 것이라고 기대합니다. 수학적으로 이는 테스트 세트의 정규화된 역확률로 정의됩니다:
$$
\mathrm{Perplexity}(W) = \sqrt[N]{1\over P(W_1,...,W_N)}
$$ 

**[Hugging Face의 GPT 기반 텍스트 편집기를 사용하여 텍스트 생성을 실험해 보세요](https://transformer.huggingface.co/doc/gpt2-large)**. 이 편집기에서 텍스트 작성을 시작하고 **[TAB]**를 누르면 여러 완성 옵션이 제공됩니다. 옵션이 너무 짧거나 만족스럽지 않다면 다시 [TAB]를 눌러 더 많은 옵션, 긴 텍스트 조각 등을 받을 수 있습니다.

## GPT는 하나의 가족입니다

GPT는 단일 모델이 아니라 [OpenAI](https://openai.com)에서 개발하고 훈련한 모델의 모음입니다.

GPT 모델에는 다음이 포함됩니다:

| [GPT-2](https://huggingface.co/docs/transformers/model_doc/gpt2#openai-gpt2) | [GPT 3](https://openai.com/research/language-models-are-few-shot-learners) | [GPT-4](https://openai.com/gpt-4) |
| -- | -- | -- |
| 최대 15억 개의 매개변수를 가진 언어 모델. | 최대 1750억 개의 매개변수를 가진 언어 모델 | 100조 개의 매개변수를 가지며 이미지 및 텍스트 입력을 받아 텍스트를 출력합니다. |

GPT-3 및 GPT-4 모델은 [Microsoft Azure의 인지 서비스로 제공됩니다](https://azure.microsoft.com/en-us/services/cognitive-services/openai-service/#overview?WT.mc_id=academic-77998-cacaste) 및 [OpenAI API](https://openai.com/api/)로도 이용할 수 있습니다.

## 프롬프트 엔지니어링

GPT는 언어와 코드를 이해하기 위해 방대한 양의 데이터로 훈련되었기 때문에 입력(프롬프트)에 대한 응답으로 출력을 제공합니다. 프롬프트는 모델에 다음 작업을 수행하도록 지시하는 입력 또는 쿼리입니다. 원하는 결과를 얻으려면 가장 효과적인 프롬프트가 필요하며, 이는 적절한 단어, 형식, 구문 또는 기호를 선택하는 것을 포함합니다. 이러한 접근 방식은 [프롬프트 엔지니어링](https://learn.microsoft.com/en-us/shows/ai-show/the-basics-of-prompt-engineering-with-azure-openai-service?WT.mc_id=academic-77998-bethanycheum)이라고 합니다.

[이 문서](https://learn.microsoft.com/en-us/semantic-kernel/prompt-engineering/?WT.mc_id=academic-77998-bethanycheum)는 프롬프트 엔지니어링에 대한 더 많은 정보를 제공합니다.

## ✍️ 예제 노트북: [OpenAI-GPT와 함께 놀기](../../../../../lessons/5-NLP/20-LangModels/GPT-PyTorch.ipynb)

다음 노트북에서 학습을 계속하세요:

* [OpenAI-GPT 및 Hugging Face Transformers로 텍스트 생성하기](../../../../../lessons/5-NLP/20-LangModels/GPT-PyTorch.ipynb)

## 결론

새로운 일반 사전 훈련된 언어 모델은 언어 구조를 모델링할 뿐만 아니라 방대한 양의 자연어를 포함하고 있습니다. 따라서 이들은 제로 샷 또는 몇 샷 설정에서 일부 NLP 작업을 효과적으로 해결하는 데 사용할 수 있습니다.

## [강의 후 퀴즈](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/220)

**면책 조항**:  
이 문서는 기계 기반 AI 번역 서비스를 사용하여 번역되었습니다. 정확성을 위해 노력하고 있지만, 자동 번역에는 오류나 부정확성이 있을 수 있습니다. 원본 문서는 해당 언어로 된 권위 있는 출처로 간주되어야 합니다. 중요한 정보에 대해서는 전문적인 인간 번역을 권장합니다. 이 번역을 사용하여 발생하는 오해나 잘못 해석에 대해 우리는 책임을 지지 않습니다.