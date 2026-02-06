# NER

[AI for Beginners Curriculum](https://github.com/microsoft/ai-for-beginners) ലെ ലാബ് അസൈൻമെന്റ്.

## ടാസ്‌ക്

ഈ ലാബിൽ, മെഡിക്കൽ പദങ്ങൾക്കായി നെയിംഡ് എന്റിറ്റി റെക്കഗ്നിഷൻ മോഡൽ ട്രെയിൻ ചെയ്യേണ്ടതാണ്.

## ഡാറ്റാസെറ്റ്

NER മോഡൽ ട്രെയിനിംഗിന്, മെഡിക്കൽ എന്റിറ്റികളോടുകൂടിയ ശരിയായ ലേബൽ ചെയ്ത ഡാറ്റാസെറ്റ് ആവശ്യമുണ്ട്. [BC5CDR dataset](https://biocreative.bioinformatics.udel.edu/tasks/biocreative-v/track-3-cdr/) 1500-ലധികം പേപ്പറുകളിൽ നിന്നുള്ള രോഗങ്ങളും രാസവസ്തുക്കളും ലേബൽ ചെയ്ത എന്റിറ്റികൾ ഉൾക്കൊള്ളുന്നു. അവരുടെ വെബ്സൈറ്റിൽ രജിസ്റ്റർ ചെയ്ത് ഡാറ്റാസെറ്റ് ഡൗൺലോഡ് ചെയ്യാം.

BC5CDR Dataset ഇങ്ങനെ കാണപ്പെടും:

```
6794356|t|Tricuspid valve regurgitation and lithium carbonate toxicity in a newborn infant.
6794356|a|A newborn with massive tricuspid regurgitation, atrial flutter, congestive heart failure, and a high serum lithium level is described. This is the first patient to initially manifest tricuspid regurgitation and atrial flutter, and the 11th described patient with cardiac disease among infants exposed to lithium compounds in the first trimester of pregnancy. Sixty-three percent of these infants had tricuspid valve involvement. Lithium carbonate may be a factor in the increasing incidence of congenital heart disease when taken during early pregnancy. It also causes neurologic depression, cyanosis, and cardiac arrhythmia when consumed prior to delivery.
6794356	0	29	Tricuspid valve regurgitation	Disease	D014262
6794356	34	51	lithium carbonate	Chemical	D016651
6794356	52	60	toxicity	Disease	D064420
...
```

ഈ ഡാറ്റാസെറ്റിൽ, ആദ്യ രണ്ട് വരികളിൽ പേപ്പർ തലക്കെട്ടും ആബ്സ്ട്രാക്റ്റും ഉണ്ട്, തുടർന്ന് ഓരോ എന്റിറ്റിയും, തലക്കെട്ടും ആബ്സ്ട്രാക്റ്റും ചേർന്ന ബ്ലോക്കിനുള്ളിൽ ആരംഭവും അവസാനവും സ്ഥിതിചെയ്യുന്ന സ്ഥാനങ്ങളോടുകൂടി കാണിക്കുന്നു. എന്റിറ്റി തരം കൂടാതെ, ചില മെഡിക്കൽ ഓന്റോളജികളിൽ ആ എന്റിറ്റിയുടെ ഓന്റോളജി ഐഡി ലഭിക്കും.

ഇത് BIO എൻകോഡിങ്ങിലേക്ക് മാറ്റാൻ Python കോഡ് എഴുതേണ്ടതുണ്ട്.

## നെറ്റ്‌വർക്ക്

NER-ന്റെ ആദ്യ ശ്രമം LSTM നെറ്റ്‌വർക്ക് ഉപയോഗിച്ച് ചെയ്യാം, പാഠത്തിൽ കാണിച്ച ഉദാഹരണത്തിൽപോലെ. എന്നാൽ NLP ടാസ്കുകളിൽ, [ട്രാൻസ്ഫോർമർ ആർക്കിടെക്ചർ](https://en.wikipedia.org/wiki/Transformer_(machine_learning_model)) പ്രത്യേകിച്ച് [BERT ഭാഷാ മോഡലുകൾ](https://en.wikipedia.org/wiki/BERT_(language_model)) വളരെ മികച്ച ഫലങ്ങൾ കാണിക്കുന്നു. പ്രീ-ട്രെയിൻ ചെയ്ത BERT മോഡലുകൾ ഒരു ഭാഷയുടെ പൊതുവായ ഘടന മനസിലാക്കുകയും, ചെറിയ ഡാറ്റാസെറ്റുകളും കംപ്യൂട്ടേഷണൽ ചെലവുകളും ഉപയോഗിച്ച് പ്രത്യേക ടാസ്കുകൾക്കായി ഫൈൻ-ട്യൂൺ ചെയ്യാൻ കഴിയും.

നാം NER മെഡിക്കൽ രംഗത്ത് പ്രയോഗിക്കാനാണ് ഉദ്ദേശിക്കുന്നത്, അതിനാൽ മെഡിക്കൽ ടെക്സ്റ്റുകളിൽ ട്രെയിൻ ചെയ്ത BERT മോഡൽ ഉപയോഗിക്കുന്നത് യുക്തിയുള്ളതാണ്. Microsoft Research [PubMedBERT][PubMedBERT] എന്ന പ്രീ-ട്രെയിൻ ചെയ്ത മോഡൽ പുറത്തിറക്കി, ഇത് [PubMed](https://pubmed.ncbi.nlm.nih.gov/) റിപോസിറ്ററിയിൽ നിന്നുള്ള ടെക്സ്റ്റുകൾ ഉപയോഗിച്ച് ഫൈൻ-ട്യൂൺ ചെയ്തതാണ് ([പ്രസിദ്ധീകരണം][PubMedBERT-Pub]).

ട്രാൻസ്ഫോർമർ മോഡലുകൾ ട്രെയിൻ ചെയ്യാനുള്ള *de facto* സ്റ്റാൻഡേർഡ് [Hugging Face Transformers](https://huggingface.co/) ലൈബ്രറിയാണ്. ഇതിൽ കമ്മ്യൂണിറ്റി പരിപാലിക്കുന്ന പ്രീ-ട്രെയിൻ ചെയ്ത മോഡലുകളുടെ റിപോസിറ്ററിയും ഉണ്ട്, അതിൽ PubMedBERT ഉൾപ്പെടുന്നു. ഈ മോഡൽ ലോഡ് ചെയ്ത് ഉപയോഗിക്കാൻ, കുറച്ച് കോഡ് വരികൾ മാത്രം ആവശ്യമാണ്:

```python
model_name = "microsoft/BiomedNLP-PubMedBERT-base-uncased-abstract"
classes = ... # ക്ലാസുകളുടെ എണ്ണം: 2*എൻറിറ്റികൾ+1
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = BertForTokenClassification.from_pretrained(model_name, classes)
```

ഇത് `classes` എണ്ണം ക്ലാസുകൾ ഉപയോഗിച്ച് ടോക്കൺ ക്ലാസിഫിക്കേഷൻ ടാസ്കിനായി നിർമ്മിച്ച `model`-ഉം, ഇൻപുട്ട് ടെക്സ്റ്റ് ടോക്കണുകളായി വിഭജിക്കാൻ കഴിയുന്ന `tokenizer` ഒബ്ജക്റ്റും നൽകുന്നു. ഡാറ്റാസെറ്റ് BIO ഫോർമാറ്റിലേക്ക് മാറ്റുമ്പോൾ PubMedBERT ടോക്കണൈസേഷൻ പരിഗണിക്കണം. [ഈ Python കോഡ്](https://gist.github.com/shwars/580b55684be3328eb39ecf01b9cbbd88) പ്രചോദനമായി ഉപയോഗിക്കാം.

## ടേക്ക്‌അവേ

നിങ്ങൾക്ക് വലിയ തോതിലുള്ള നാചുറൽ ലാംഗ്വേജ് ടെക്സ്റ്റുകളിൽ കൂടുതൽ洞察ങ്ങൾ നേടാൻ ആഗ്രഹമുണ്ടെങ്കിൽ, ഈ ടാസ്‌ക് വളരെ അടുത്തതാണ്. നമ്മുടെ ട്രെയിൻ ചെയ്ത മോഡൽ [COVID-സംബന്ധപ്പെട്ട പേപ്പറുകളുടെ ഡാറ്റാസെറ്റ്](https://www.kaggle.com/allen-institute-for-ai/CORD-19-research-challenge) പ്രയോഗിച്ച്, എന്ത്洞察ങ്ങൾ ലഭ്യമാകുമെന്ന് നോക്കാം. [ഈ ബ്ലോഗ് പോസ്റ്റ്](https://soshnikov.com/science/analyzing-medical-papers-with-azure-and-text-analytics-for-health/)യും [ഈ പേപ്പറും](https://www.mdpi.com/2504-2289/6/1/4) NER ഉപയോഗിച്ച് ഈ പേപ്പറുകളുടെ കോർപ്പസിൽ ചെയ്യാവുന്ന ഗവേഷണത്തെക്കുറിച്ച് വിവരിക്കുന്നു.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**അസൂയാ**:  
ഈ രേഖ AI വിവർത്തന സേവനം [Co-op Translator](https://github.com/Azure/co-op-translator) ഉപയോഗിച്ച് വിവർത്തനം ചെയ്തതാണ്. നാം കൃത്യതയ്ക്ക് ശ്രമിച്ചെങ്കിലും, സ്വയം പ്രവർത്തിക്കുന്ന വിവർത്തനങ്ങളിൽ പിശകുകൾ അല്ലെങ്കിൽ തെറ്റുകൾ ഉണ്ടാകാമെന്ന് ദയവായി ശ്രദ്ധിക്കുക. അതിന്റെ മാതൃഭാഷയിലുള്ള യഥാർത്ഥ രേഖ അധികാരപരമായ ഉറവിടമായി കണക്കാക്കണം. നിർണായക വിവരങ്ങൾക്ക്, പ്രൊഫഷണൽ മനുഷ്യ വിവർത്തനം ശുപാർശ ചെയ്യപ്പെടുന്നു. ഈ വിവർത്തനം ഉപയോഗിക്കുന്നതിൽ നിന്നുണ്ടാകുന്ന ഏതെങ്കിലും തെറ്റിദ്ധാരണകൾക്കോ തെറ്റായ വ്യാഖ്യാനങ്ങൾക്കോ ഞങ്ങൾ ഉത്തരവാദികളല്ല.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->