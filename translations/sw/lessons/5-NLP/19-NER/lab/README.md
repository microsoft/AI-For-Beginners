# NER

Kazi ya Maabara kutoka [Mtaala wa AI kwa Kompyuta](https://github.com/microsoft/ai-for-beginners).

## Kazi

Katika maabara hii, unahitaji kufundisha mfano wa utambuzi wa vyombo vilivyopewa majina (NER) kwa maneno ya kitabibu.

## Seti ya Data

Ili kufundisha mfano wa NER, tunahitaji seti ya data iliyowekwa alama ipasavyo yenye vyombo vya kitabibu. [Seti ya data ya BC5CDR](https://biocreative.bioinformatics.udel.edu/tasks/biocreative-v/track-3-cdr/) ina vyombo vya magonjwa na kemikali vilivyowekwa alama kutoka kwa zaidi ya makala 1500. Unaweza kupakua seti ya data baada ya kujisajili kwenye tovuti yao.

Seti ya data ya BC5CDR inaonekana kama ifuatavyo:

```
6794356|t|Tricuspid valve regurgitation and lithium carbonate toxicity in a newborn infant.
6794356|a|A newborn with massive tricuspid regurgitation, atrial flutter, congestive heart failure, and a high serum lithium level is described. This is the first patient to initially manifest tricuspid regurgitation and atrial flutter, and the 11th described patient with cardiac disease among infants exposed to lithium compounds in the first trimester of pregnancy. Sixty-three percent of these infants had tricuspid valve involvement. Lithium carbonate may be a factor in the increasing incidence of congenital heart disease when taken during early pregnancy. It also causes neurologic depression, cyanosis, and cardiac arrhythmia when consumed prior to delivery.
6794356	0	29	Tricuspid valve regurgitation	Disease	D014262
6794356	34	51	lithium carbonate	Chemical	D016651
6794356	52	60	toxicity	Disease	D064420
...
```

Katika seti hii ya data, kuna kichwa cha makala na muhtasari kwenye mistari miwili ya kwanza, na kisha kuna vyombo vya mtu binafsi, na nafasi za mwanzo na mwisho ndani ya sehemu ya kichwa+muhtasari. Mbali na aina ya chombo, unapata kitambulisho cha ontolojia cha chombo hiki ndani ya ontolojia fulani ya kitabibu.

Utahitaji kuandika msimbo wa Python ili kubadilisha hii kuwa usimbaji wa BIO.

## Mtandao

Jaribio la kwanza la NER linaweza kufanywa kwa kutumia mtandao wa LSTM, kama katika mfano wetu ulioona wakati wa somo. Hata hivyo, katika kazi za NLP, [usanifu wa transformer](https://en.wikipedia.org/wiki/Transformer_(machine_learning_model)), na hasa [mifano ya lugha ya BERT](https://en.wikipedia.org/wiki/BERT_(language_model)) huonyesha matokeo bora zaidi. Mifano ya BERT iliyofundishwa awali inaelewa muundo wa jumla wa lugha, na inaweza kufundishwa zaidi kwa kazi maalum kwa kutumia seti ndogo za data na gharama ndogo za kihesabu.

Kwa kuwa tunapanga kutumia NER katika hali ya kitabibu, ina maana kutumia mfano wa BERT uliofundishwa kwenye maandishi ya kitabibu. Microsoft Research imetoa mfano uliofundishwa awali unaoitwa [PubMedBERT][PubMedBERT] ([uchapishaji][PubMedBERT-Pub]), ambao ulifundishwa zaidi kwa kutumia maandishi kutoka hifadhidata ya [PubMed](https://pubmed.ncbi.nlm.nih.gov/).

Kiwango cha *de facto* cha kufundisha mifano ya transformer ni maktaba ya [Hugging Face Transformers](https://huggingface.co/). Pia ina hifadhidata ya mifano iliyofundishwa awali inayosimamiwa na jamii, ikijumuisha PubMedBERT. Ili kupakia na kutumia mfano huu, tunahitaji mistari michache tu ya msimbo:

```python
model_name = "microsoft/BiomedNLP-PubMedBERT-base-uncased-abstract"
classes = ... # number of classes: 2*entities+1
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = BertForTokenClassification.from_pretrained(model_name, classes)
```

Hii inatupa `model` yenyewe, iliyojengwa kwa kazi ya uainishaji wa tokeni kwa kutumia idadi ya `classes`, pamoja na kitu cha `tokenizer` ambacho kinaweza kugawanya maandishi ya pembejeo kuwa tokeni. Utahitaji kubadilisha seti ya data kuwa muundo wa BIO, ukizingatia usimbaji wa tokeni wa PubMedBERT. Unaweza kutumia [kipande hiki cha msimbo wa Python](https://gist.github.com/shwars/580b55684be3328eb39ecf01b9cbbd88) kama msukumo.

## Hitimisho

Kazi hii iko karibu sana na kazi halisi unayoweza kuwa nayo ikiwa unataka kupata maarifa zaidi kutoka kwa idadi kubwa ya maandishi ya lugha asilia. Katika hali yetu, tunaweza kutumia mfano wetu uliofundishwa kwenye [seti ya data ya makala zinazohusiana na COVID](https://www.kaggle.com/allen-institute-for-ai/CORD-19-research-challenge) na kuona ni maarifa gani tutakayoweza kupata. [Chapisho hili la blogu](https://soshnikov.com/science/analyzing-medical-papers-with-azure-and-text-analytics-for-health/) na [karatasi hii](https://www.mdpi.com/2504-2289/6/1/4) vinaelezea utafiti unaoweza kufanywa kwenye mkusanyiko huu wa makala kwa kutumia NER.

**Kanusho**:  
Hati hii imetafsiriwa kwa kutumia huduma ya kutafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kuhakikisha usahihi, tafadhali fahamu kuwa tafsiri za kiotomatiki zinaweza kuwa na makosa au kutokuwa sahihi. Hati asilia katika lugha yake ya awali inapaswa kuchukuliwa kama chanzo cha mamlaka. Kwa taarifa muhimu, tafsiri ya kitaalamu ya binadamu inapendekezwa. Hatutawajibika kwa kutoelewana au tafsiri zisizo sahihi zinazotokana na matumizi ya tafsiri hii.