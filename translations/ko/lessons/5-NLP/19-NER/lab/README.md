# NER

[초보자를 위한 AI 커리큘럼](https://github.com/microsoft/ai-for-beginners)에서의 실습 과제입니다.

## 작업

이 실습에서는 의료 용어를 위한 명명된 개체 인식(NER) 모델을 훈련해야 합니다.

## 데이터셋

NER 모델을 훈련하기 위해서는 의료 개체가 적절히 라벨링된 데이터셋이 필요합니다. [BC5CDR 데이터셋](https://biocreative.bioinformatics.udel.edu/tasks/biocreative-v/track-3-cdr/)은 1500편 이상의 논문에서 라벨링된 질병 및 화학 물질 개체를 포함하고 있습니다. 웹사이트에 등록한 후 데이터셋을 다운로드할 수 있습니다.

BC5CDR 데이터셋은 다음과 같은 형식을 가지고 있습니다:

```
6794356|t|Tricuspid valve regurgitation and lithium carbonate toxicity in a newborn infant.
6794356|a|A newborn with massive tricuspid regurgitation, atrial flutter, congestive heart failure, and a high serum lithium level is described. This is the first patient to initially manifest tricuspid regurgitation and atrial flutter, and the 11th described patient with cardiac disease among infants exposed to lithium compounds in the first trimester of pregnancy. Sixty-three percent of these infants had tricuspid valve involvement. Lithium carbonate may be a factor in the increasing incidence of congenital heart disease when taken during early pregnancy. It also causes neurologic depression, cyanosis, and cardiac arrhythmia when consumed prior to delivery.
6794356	0	29	Tricuspid valve regurgitation	Disease	D014262
6794356	34	51	lithium carbonate	Chemical	D016651
6794356	52	60	toxicity	Disease	D064420
...
```

이 데이터셋의 첫 두 줄에는 논문 제목과 초록이 있으며, 그 다음에는 제목+초록 블록 내에서 시작 및 끝 위치와 함께 개별 개체가 있습니다. 개체 유형 외에도, 이 개체가 특정 의료 온톨로지 내에서 가지는 온톨로지 ID도 제공합니다.

이 데이터를 BIO 인코딩으로 변환하기 위해 몇 가지 파이썬 코드를 작성해야 합니다.

## 네트워크

NER에 대한 첫 번째 시도는 수업 중에 보았던 LSTM 네트워크를 사용하여 수행할 수 있습니다. 그러나 NLP 작업에서는 [트랜스포머 아키텍처](https://en.wikipedia.org/wiki/Transformer_(machine_learning_model))와 특히 [BERT 언어 모델](https://en.wikipedia.org/wiki/BERT_(language_model))이 훨씬 더 좋은 결과를 보여줍니다. 사전 훈련된 BERT 모델은 언어의 일반적인 구조를 이해하고, 상대적으로 작은 데이터셋과 계산 비용으로 특정 작업에 맞게 미세 조정할 수 있습니다.

우리는 의료 시나리오에 NER을 적용할 계획이므로, 의료 텍스트로 훈련된 BERT 모델을 사용하는 것이 합리적입니다. Microsoft Research는 [PubMedBERT][PubMedBERT] ([발표][PubMedBERT-Pub])라는 사전 훈련된 모델을 발표하였으며, 이는 [PubMed](https://pubmed.ncbi.nlm.nih.gov/) 저장소의 텍스트를 사용하여 미세 조정되었습니다.

트랜스포머 모델 훈련의 *de facto* 표준은 [Hugging Face Transformers](https://huggingface.co/) 라이브러리입니다. 이 라이브러리에는 PubMedBERT를 포함한 커뮤니티에서 유지 관리하는 사전 훈련된 모델의 저장소도 포함되어 있습니다. 이 모델을 로드하고 사용하기 위해서는 몇 줄의 코드만 필요합니다:

```python
model_name = "microsoft/BiomedNLP-PubMedBERT-base-uncased-abstract"
classes = ... # number of classes: 2*entities+1
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = BertForTokenClassification.from_pretrained(model_name, classes)
```

이 코드는 입력 텍스트를 토큰으로 분할할 수 있는 `model` itself, built for token classification task using `classes` number of classes, as well as `tokenizer` 객체를 제공합니다. 데이터셋을 BIO 형식으로 변환할 때 PubMedBERT 토크나이제이션을 고려해야 합니다. [이 파이썬 코드 조각](https://gist.github.com/shwars/580b55684be3328eb39ecf01b9cbbd88)을 참고할 수 있습니다.

## 요약

이 작업은 자연어 텍스트의 대량에 대한 통찰력을 얻고자 할 때 실제로 수행하게 될 작업과 매우 유사합니다. 우리의 경우, 훈련된 모델을 [COVID 관련 논문 데이터셋](https://www.kaggle.com/allen-institute-for-ai/CORD-19-research-challenge)에 적용하여 어떤 통찰력을 얻을 수 있을지 살펴볼 수 있습니다. [이 블로그 포스트](https://soshnikov.com/science/analyzing-medical-papers-with-azure-and-text-analytics-for-health/)와 [이 논문](https://www.mdpi.com/2504-2289/6/1/4)은 NER을 사용하여 이 논문 집합에서 수행할 수 있는 연구를 설명합니다.

**면책 조항**:  
이 문서는 기계 기반 AI 번역 서비스를 사용하여 번역되었습니다. 정확성을 위해 노력하고 있지만, 자동 번역에는 오류나 부정확성이 포함될 수 있습니다. 원본 문서는 해당 언어로 작성된 권위 있는 출처로 간주되어야 합니다. 중요한 정보에 대해서는 전문적인 인간 번역을 권장합니다. 이 번역의 사용으로 인해 발생하는 오해나 잘못된 해석에 대해서는 저희가 책임지지 않습니다.