# NER

[AI for Beginners Curriculum](https://github.com/microsoft/ai-for-beginners) ನಿಂದ ಪ್ರಯೋಗಾಲಯ ಕಾರ್ಯ.

## ಕಾರ್ಯ

ಈ ಪ್ರಯೋಗಾಲಯದಲ್ಲಿ, ನೀವು ವೈದ್ಯಕೀಯ ಪದಗಳಿಗಾಗಿ ನಾಮಿತ ಘಟಕ ಗುರುತಿಸುವ ಮಾದರಿಯನ್ನು ತರಬೇತುಗೊಳಿಸಬೇಕಾಗಿದೆ.

## ಡೇಟಾಸೆಟ್

NER ಮಾದರಿಯನ್ನು ತರಬೇತುಗೊಳಿಸಲು, ವೈದ್ಯಕೀಯ ಘಟಕಗಳೊಂದಿಗೆ ಸರಿಯಾಗಿ ಲೇಬಲ್ ಮಾಡಲಾದ ಡೇಟಾಸೆಟ್ ಅಗತ್ಯವಿದೆ. [BC5CDR ಡೇಟಾಸೆಟ್](https://biocreative.bioinformatics.udel.edu/tasks/biocreative-v/track-3-cdr/) 1500 ಕ್ಕೂ ಹೆಚ್ಚು ಪೇಪರ್‌ಗಳಿಂದ ರೋಗಗಳು ಮತ್ತು ರಾಸಾಯನಿಕ ಘಟಕಗಳನ್ನು ಲೇಬಲ್ ಮಾಡಿದೆ. ನೀವು ಅವರ ವೆಬ್‌ಸೈಟ್‌ನಲ್ಲಿ ನೋಂದಾಯಿಸಿಕೊಂಡ ನಂತರ ಡೇಟಾಸೆಟ್ ಅನ್ನು ಡೌನ್‌ಲೋಡ್ ಮಾಡಬಹುದು.

BC5CDR ಡೇಟಾಸೆಟ್ ಹೀಗೆ ಕಾಣುತ್ತದೆ:

```
6794356|t|Tricuspid valve regurgitation and lithium carbonate toxicity in a newborn infant.
6794356|a|A newborn with massive tricuspid regurgitation, atrial flutter, congestive heart failure, and a high serum lithium level is described. This is the first patient to initially manifest tricuspid regurgitation and atrial flutter, and the 11th described patient with cardiac disease among infants exposed to lithium compounds in the first trimester of pregnancy. Sixty-three percent of these infants had tricuspid valve involvement. Lithium carbonate may be a factor in the increasing incidence of congenital heart disease when taken during early pregnancy. It also causes neurologic depression, cyanosis, and cardiac arrhythmia when consumed prior to delivery.
6794356	0	29	Tricuspid valve regurgitation	Disease	D014262
6794356	34	51	lithium carbonate	Chemical	D016651
6794356	52	60	toxicity	Disease	D064420
...
```

ಈ ಡೇಟಾಸೆಟ್‌ನಲ್ಲಿ, ಮೊದಲ ಎರಡು ಸಾಲುಗಳಲ್ಲಿ ಪೇಪರ್ ಶೀರ್ಷಿಕೆ ಮತ್ತು ಸಾರಾಂಶ ಇರುತ್ತದೆ, ನಂತರ ಪ್ರತ್ಯೇಕ ಘಟಕಗಳು ಇರುತ್ತವೆ, ಶೀರ್ಷಿಕೆ+ಸಾರಾಂಶ ಬ್ಲಾಕ್‌ನೊಳಗಿನ ಪ್ರಾರಂಭ ಮತ್ತು ಅಂತ್ಯ ಸ್ಥಾನಗಳೊಂದಿಗೆ. ಘಟಕದ ಪ್ರಕಾರದ ಜೊತೆಗೆ, ನೀವು ಕೆಲವು ವೈದ್ಯಕೀಯ ಆಂಟಾಲಜಿ ಒಳಗಿನ ಆಂಟಾಲಜಿ ID ಅನ್ನು ಪಡೆಯುತ್ತೀರಿ.

ನೀವು ಇದನ್ನು BIO ಎನ್‌ಕೋಡಿಂಗ್‌ಗೆ ಪರಿವರ್ತಿಸಲು ಕೆಲವು Python ಕೋಡ್ ಬರೆಯಬೇಕಾಗುತ್ತದೆ.

## ನೆಟ್‌ವರ್ಕ್

NER ಗೆ ಮೊದಲ ಪ್ರಯತ್ನವನ್ನು LSTM ನೆಟ್‌ವರ್ಕ್ ಬಳಸಿ ಮಾಡಬಹುದು, ನಮ್ಮ ಉದಾಹರಣೆಯಲ್ಲಿ ನೀವು ಪಾಠದ ವೇಳೆ ನೋಡಿದ್ದೀರಿ. ಆದರೆ, NLP ಕಾರ್ಯಗಳಲ್ಲಿ, [ಟ್ರಾನ್ಸ್‌ಫಾರ್ಮರ್ ವಾಸ್ತುಶಿಲ್ಪ](https://en.wikipedia.org/wiki/Transformer_(machine_learning_model)) ಮತ್ತು ವಿಶೇಷವಾಗಿ [BERT ಭಾಷಾ ಮಾದರಿಗಳು](https://en.wikipedia.org/wiki/BERT_(language_model)) ಬಹುಮಟ್ಟಿಗೆ ಉತ್ತಮ ಫಲಿತಾಂಶಗಳನ್ನು ತೋರಿಸುತ್ತವೆ. ಪೂರ್ವ-ತರಬೇತುಗೊಂಡ BERT ಮಾದರಿಗಳು ಭಾಷೆಯ ಸಾಮಾನ್ಯ ರಚನೆಯನ್ನು ಅರ್ಥಮಾಡಿಕೊಳ್ಳುತ್ತವೆ ಮತ್ತು ಸಾಪೇಕ್ಷವಾಗಿ ಸಣ್ಣ ಡೇಟಾಸೆಟ್‌ಗಳು ಮತ್ತು ಗಣನೀಯ ವೆಚ್ಚಗಳೊಂದಿಗೆ ನಿರ್ದಿಷ್ಟ ಕಾರ್ಯಗಳಿಗೆ ಸೂಕ್ಷ್ಮ-ತರಬೇತುಗೊಳಿಸಬಹುದು.

ನಾವು NER ಅನ್ನು ವೈದ್ಯಕೀಯ ಸಂದರ್ಭಕ್ಕೆ ಅನ್ವಯಿಸಲು ಯೋಜಿಸುತ್ತಿರುವುದರಿಂದ, ವೈದ್ಯಕೀಯ ಪಠ್ಯಗಳ ಮೇಲೆ ತರಬೇತುಗೊಂಡ BERT ಮಾದರಿಯನ್ನು ಬಳಸುವುದು ಸೂಕ್ತ. Microsoft Research [PubMedBERT][PubMedBERT] ಎಂಬ ಪೂರ್ವ-ತರಬೇತುಗೊಂಡ ಮಾದರಿಯನ್ನು ಬಿಡುಗಡೆ ಮಾಡಿದೆ ([ಪ್ರಕಟನೆ][PubMedBERT-Pub]), ಇದು [PubMed](https://pubmed.ncbi.nlm.nih.gov/) ಸಂಗ್ರಹದಿಂದ ಪಠ್ಯಗಳನ್ನು ಬಳಸಿ ಸೂಕ್ಷ್ಮ-ತರಬೇತುಗೊಂಡಿದೆ.

ಟ್ರಾನ್ಸ್‌ಫಾರ್ಮರ್ ಮಾದರಿಗಳನ್ನು ತರಬೇತುಗೊಳಿಸಲು *de facto* ಮಾನದಂಡ [Hugging Face Transformers](https://huggingface.co/) ಗ್ರಂಥಾಲಯ. ಇದರಲ್ಲಿ ಸಮುದಾಯ ನಿರ್ವಹಿಸುವ ಪೂರ್ವ-ತರಬೇತುಗೊಂಡ ಮಾದರಿಗಳ ಸಂಗ್ರಹವಿದೆ, ಇದರಲ್ಲಿ PubMedBERT ಕೂಡ ಸೇರಿದೆ. ಈ ಮಾದರಿಯನ್ನು ಲೋಡ್ ಮಾಡಿ ಬಳಸಲು, ನಮಗೆ ಕೆಲವು ಸಾಲುಗಳ ಕೋಡ್ ಬೇಕಾಗುತ್ತದೆ:

```python
model_name = "microsoft/BiomedNLP-PubMedBERT-base-uncased-abstract"
classes = ... # ವರ್ಗಗಳ ಸಂಖ್ಯೆ: 2*ಘಟಕಗಳು+1
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = BertForTokenClassification.from_pretrained(model_name, classes)
```

ಇದು ನಮಗೆ `model` ಅನ್ನು ನೀಡುತ್ತದೆ, ಇದು `classes` ಸಂಖ್ಯೆಯ ವರ್ಗಗಳನ್ನು ಬಳಸಿ ಟೋಕನ್ ವರ್ಗೀಕರಣ ಕಾರ್ಯಕ್ಕಾಗಿ ನಿರ್ಮಿಸಲಾಗಿದೆ, ಜೊತೆಗೆ `tokenizer` ವಸ್ತುವನ್ನು ನೀಡುತ್ತದೆ, ಇದು ಇನ್‌ಪುಟ್ ಪಠ್ಯವನ್ನು ಟೋಕನ್‌ಗಳಾಗಿ ವಿಭಜಿಸಬಹುದು. ನೀವು ಡೇಟಾಸೆಟ್ ಅನ್ನು BIO ಫಾರ್ಮ್ಯಾಟ್‌ಗೆ ಪರಿವರ್ತಿಸಬೇಕಾಗುತ್ತದೆ, PubMedBERT ಟೋಕನೈಜೇಶನ್ ಅನ್ನು ಗಮನದಲ್ಲಿಟ್ಟುಕೊಂಡು. ಪ್ರೇರಣೆಗೆ ನೀವು [ಈ Python ಕೋಡ್](https://gist.github.com/shwars/580b55684be3328eb39ecf01b9cbbd88) ಬಳಸಬಹುದು.

## ಸಾರಾಂಶ

ಈ ಕಾರ್ಯವು ನೀವು ಬಹುಮಾನ್ಯ ಪ್ರಮಾಣದ ನೈಸರ್ಗಿಕ ಭಾಷಾ ಪಠ್ಯಗಳಲ್ಲಿ ಹೆಚ್ಚಿನ ಅರ್ಥಗಳನ್ನು ಪಡೆಯಲು ಬಯಸಿದರೆ ಎದುರಿಸಬಹುದಾದ ನಿಜವಾದ ಕಾರ್ಯಕ್ಕೆ ಬಹಳ ಹತ್ತಿರವಾಗಿದೆ. ನಮ್ಮ ಪ್ರಕರಣದಲ್ಲಿ, ನಾವು ತರಬೇತುಗೊಂಡ ಮಾದರಿಯನ್ನು [COVID-ಸಂಬಂಧಿತ ಪೇಪರ್‌ಗಳ ಡೇಟಾಸೆಟ್](https://www.kaggle.com/allen-institute-for-ai/CORD-19-research-challenge) ಗೆ ಅನ್ವಯಿಸಿ, ನಾವು ಯಾವ ಅರ್ಥಗಳನ್ನು ಪಡೆಯಬಹುದು ಎಂದು ನೋಡಬಹುದು. [ಈ ಬ್ಲಾಗ್ ಪೋಸ್ಟ್](https://soshnikov.com/science/analyzing-medical-papers-with-azure-and-text-analytics-for-health/) ಮತ್ತು [ಈ ಪೇಪರ್](https://www.mdpi.com/2504-2289/6/1/4) NER ಬಳಸಿ ಈ ಪೇಪರ್‌ಗಳ ಸಂಗ್ರಹದ ಮೇಲೆ ಮಾಡಬಹುದಾದ ಸಂಶೋಧನೆಯನ್ನು ವಿವರಿಸುತ್ತವೆ.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ಅಸ್ವೀಕರಣ**:  
ಈ ದಸ್ತಾವೇಜು AI ಅನುವಾದ ಸೇವೆ [Co-op Translator](https://github.com/Azure/co-op-translator) ಬಳಸಿ ಅನುವಾದಿಸಲಾಗಿದೆ. ನಾವು ನಿಖರತೆಯಿಗಾಗಿ ಪ್ರಯತ್ನಿಸುತ್ತಿದ್ದರೂ, ಸ್ವಯಂಚಾಲಿತ ಅನುವಾದಗಳಲ್ಲಿ ದೋಷಗಳು ಅಥವಾ ಅಸತ್ಯತೆಗಳು ಇರಬಹುದು ಎಂದು ದಯವಿಟ್ಟು ಗಮನಿಸಿ. ಮೂಲ ಭಾಷೆಯಲ್ಲಿರುವ ಮೂಲ ದಸ್ತಾವೇಜನ್ನು ಅಧಿಕೃತ ಮೂಲವೆಂದು ಪರಿಗಣಿಸಬೇಕು. ಮಹತ್ವದ ಮಾಹಿತಿಗಾಗಿ, ವೃತ್ತಿಪರ ಮಾನವ ಅನುವಾದವನ್ನು ಶಿಫಾರಸು ಮಾಡಲಾಗುತ್ತದೆ. ಈ ಅನುವಾದ ಬಳಕೆಯಿಂದ ಉಂಟಾಗುವ ಯಾವುದೇ ತಪ್ಪು ಅರ್ಥಮಾಡಿಕೊಳ್ಳುವಿಕೆ ಅಥವಾ ತಪ್ಪು ವಿವರಣೆಗಳಿಗೆ ನಾವು ಹೊಣೆಗಾರರಾಗುವುದಿಲ್ಲ.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->