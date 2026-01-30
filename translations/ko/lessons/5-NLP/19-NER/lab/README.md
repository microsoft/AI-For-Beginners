# NER

[AI for Beginners Curriculum](https://github.com/microsoft/ai-for-beginners)에서 제공하는 실습 과제입니다.

## 과제

이 실습에서는 의료 용어를 위한 개체명 인식(NER) 모델을 학습시켜야 합니다.

## 데이터셋

NER 모델을 학습시키기 위해서는 의료 개체가 적절히 라벨링된 데이터셋이 필요합니다. [BC5CDR 데이터셋](https://biocreative.bioinformatics.udel.edu/tasks/biocreative-v/track-3-cdr/)은 1500개 이상의 논문에서 질병과 화학 물질 개체가 라벨링된 데이터를 제공합니다. 해당 웹사이트에서 회원가입 후 데이터를 다운로드할 수 있습니다.

BC5CDR 데이터셋은 다음과 같은 형식을 가지고 있습니다:

```
6794356|t|Tricuspid valve regurgitation and lithium carbonate toxicity in a newborn infant.
6794356|a|A newborn with massive tricuspid regurgitation, atrial flutter, congestive heart failure, and a high serum lithium level is described. This is the first patient to initially manifest tricuspid regurgitation and atrial flutter, and the 11th described patient with cardiac disease among infants exposed to lithium compounds in the first trimester of pregnancy. Sixty-three percent of these infants had tricuspid valve involvement. Lithium carbonate may be a factor in the increasing incidence of congenital heart disease when taken during early pregnancy. It also causes neurologic depression, cyanosis, and cardiac arrhythmia when consumed prior to delivery.
6794356	0	29	Tricuspid valve regurgitation	Disease	D014262
6794356	34	51	lithium carbonate	Chemical	D016651
6794356	52	60	toxicity	Disease	D064420
...
```

이 데이터셋에는 첫 두 줄에 논문의 제목과 초록이 포함되어 있으며, 이후에는 개별 개체와 제목+초록 블록 내에서의 시작 및 끝 위치가 나옵니다. 개체 유형 외에도, 해당 개체가 속한 의료 온톨로지의 ID를 제공합니다.

이 데이터를 BIO 인코딩 형식으로 변환하기 위해 Python 코드를 작성해야 합니다.

## 네트워크

NER의 첫 번째 시도는 LSTM 네트워크를 사용하는 것으로 시작할 수 있습니다. 이는 수업 중에 본 예제와 유사합니다. 하지만 NLP 작업에서는 [트랜스포머 아키텍처](https://en.wikipedia.org/wiki/Transformer_(machine_learning_model))와 특히 [BERT 언어 모델](https://en.wikipedia.org/wiki/BERT_(language_model))이 훨씬 더 나은 결과를 보여줍니다. 사전 학습된 BERT 모델은 언어의 일반적인 구조를 이해하며, 비교적 작은 데이터셋과 낮은 계산 비용으로 특정 작업에 맞게 미세 조정할 수 있습니다.

의료 시나리오에 NER을 적용할 계획이므로, 의료 텍스트로 학습된 BERT 모델을 사용하는 것이 합리적입니다. Microsoft Research는 [PubMed](https://pubmed.ncbi.nlm.nih.gov/) 저장소의 텍스트를 사용해 미세 조정된 [PubMedBERT][PubMedBERT] ([논문][PubMedBERT-Pub])이라는 사전 학습 모델을 공개했습니다.

트랜스포머 모델을 학습시키는 *사실상 표준*은 [Hugging Face Transformers](https://huggingface.co/) 라이브러리입니다. 이 라이브러리는 PubMedBERT를 포함한 커뮤니티에서 관리하는 사전 학습 모델 저장소도 제공합니다. 이 모델을 로드하고 사용하는 데 필요한 코드는 몇 줄이면 충분합니다:

```python
model_name = "microsoft/BiomedNLP-PubMedBERT-base-uncased-abstract"
classes = ... # number of classes: 2*entities+1
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = BertForTokenClassification.from_pretrained(model_name, classes)
```

이 코드는 `classes` 개의 클래스를 사용하는 토큰 분류 작업을 위한 `model`과 입력 텍스트를 토큰으로 분할할 수 있는 `tokenizer` 객체를 제공합니다. PubMedBERT 토크나이제이션을 고려하여 데이터셋을 BIO 형식으로 변환해야 합니다. [이 Python 코드](https://gist.github.com/shwars/580b55684be3328eb39ecf01b9cbbd88)를 참고 자료로 사용할 수 있습니다.

## 요점

이 과제는 대량의 자연어 텍스트에서 더 많은 통찰을 얻고자 할 때 실제로 직면할 가능성이 높은 작업과 매우 유사합니다. 우리의 경우, 학습된 모델을 [COVID 관련 논문 데이터셋](https://www.kaggle.com/allen-institute-for-ai/CORD-19-research-challenge)에 적용하여 어떤 통찰을 얻을 수 있을지 확인할 수 있습니다. [이 블로그 글](https://soshnikov.com/science/analyzing-medical-papers-with-azure-and-text-analytics-for-health/)과 [이 논문](https://www.mdpi.com/2504-2289/6/1/4)은 NER을 사용하여 이 논문 집합에서 수행할 수 있는 연구를 설명합니다.

**면책 조항**:  
이 문서는 AI 번역 서비스 [Co-op Translator](https://github.com/Azure/co-op-translator)를 사용하여 번역되었습니다. 정확성을 위해 최선을 다하고 있지만, 자동 번역에는 오류나 부정확성이 포함될 수 있습니다. 원본 문서를 해당 언어로 작성된 상태에서 권위 있는 자료로 간주해야 합니다. 중요한 정보의 경우, 전문적인 인간 번역을 권장합니다. 이 번역 사용으로 인해 발생하는 오해나 잘못된 해석에 대해 당사는 책임을 지지 않습니다.