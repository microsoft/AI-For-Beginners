# NER

Laboratorinis darbas iš [AI for Beginners Curriculum](https://github.com/microsoft/ai-for-beginners).

## Užduotis

Šiame laboratoriniame darbe turite apmokyti modelį, atpažįstantį pavadintas medicinines sąvokas.

## Duomenų rinkinys

Norint apmokyti NER modelį, reikia tinkamai pažymėto duomenų rinkinio su medicininėmis sąvokomis. [BC5CDR duomenų rinkinys](https://biocreative.bioinformatics.udel.edu/tasks/biocreative-v/track-3-cdr/) apima pažymėtas ligų ir cheminių medžiagų sąvokas iš daugiau nei 1500 straipsnių. Duomenų rinkinį galite atsisiųsti užsiregistravę jų svetainėje.

BC5CDR duomenų rinkinys atrodo taip:

```
6794356|t|Tricuspid valve regurgitation and lithium carbonate toxicity in a newborn infant.
6794356|a|A newborn with massive tricuspid regurgitation, atrial flutter, congestive heart failure, and a high serum lithium level is described. This is the first patient to initially manifest tricuspid regurgitation and atrial flutter, and the 11th described patient with cardiac disease among infants exposed to lithium compounds in the first trimester of pregnancy. Sixty-three percent of these infants had tricuspid valve involvement. Lithium carbonate may be a factor in the increasing incidence of congenital heart disease when taken during early pregnancy. It also causes neurologic depression, cyanosis, and cardiac arrhythmia when consumed prior to delivery.
6794356	0	29	Tricuspid valve regurgitation	Disease	D014262
6794356	34	51	lithium carbonate	Chemical	D016651
6794356	52	60	toxicity	Disease	D064420
...
```

Šiame duomenų rinkinyje pirmos dvi eilutės yra straipsnio pavadinimas ir santrauka, o po to pateikiamos atskiros sąvokos su pradžios ir pabaigos pozicijomis pavadinimo + santraukos bloke. Be sąvokos tipo, pateikiamas ir šios sąvokos ontologijos ID tam tikroje medicininėje ontologijoje.

Jums reikės parašyti Python kodą, kad šiuos duomenis konvertuotumėte į BIO kodavimą.

## Tinklas

Pirmąjį NER bandymą galima atlikti naudojant LSTM tinklą, kaip pavyzdyje, kurį matėte pamokoje. Tačiau NLP užduotyse [transformerių architektūra](https://en.wikipedia.org/wiki/Transformer_(machine_learning_model)), o ypač [BERT kalbos modeliai](https://en.wikipedia.org/wiki/BERT_(language_model)) duoda daug geresnius rezultatus. Iš anksto apmokyti BERT modeliai supranta bendrą kalbos struktūrą ir gali būti pritaikyti specifinėms užduotims naudojant palyginti mažus duomenų rinkinius ir nedideles skaičiavimo sąnaudas.

Kadangi planuojame taikyti NER medicininiame kontekste, logiška naudoti BERT modelį, apmokytą medicininių tekstų pagrindu. Microsoft Research išleido iš anksto apmokytą modelį, vadinamą [PubMedBERT][PubMedBERT] ([publikacija][PubMedBERT-Pub]), kuris buvo pritaikytas naudojant tekstus iš [PubMed](https://pubmed.ncbi.nlm.nih.gov/) saugyklos.

Standartas transformerių modelių apmokymui yra [Hugging Face Transformers](https://huggingface.co/) biblioteka. Ji taip pat turi bendruomenės palaikomų iš anksto apmokytų modelių saugyklą, įskaitant PubMedBERT. Norint įkelti ir naudoti šį modelį, tereikia kelių kodo eilučių:

```python
model_name = "microsoft/BiomedNLP-PubMedBERT-base-uncased-abstract"
classes = ... # number of classes: 2*entities+1
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = BertForTokenClassification.from_pretrained(model_name, classes)
```

Tai suteikia mums `modelį`, sukurtą žetonų klasifikavimo užduočiai naudojant `classes` klasių skaičių, taip pat `tokenizer` objektą, kuris gali suskaidyti įvesties tekstą į žetonus. Jums reikės konvertuoti duomenų rinkinį į BIO formatą, atsižvelgiant į PubMedBERT žetonizaciją. Galite pasinaudoti [šiuo Python kodo fragmentu](https://gist.github.com/shwars/580b55684be3328eb39ecf01b9cbbd88) kaip įkvėpimu.

## Išvada

Ši užduotis yra labai artima realioms užduotims, kurias greičiausiai turėsite atlikti, jei norėsite gauti daugiau įžvalgų iš didelių natūralios kalbos tekstų apimčių. Mūsų atveju, galime pritaikyti apmokytą modelį [COVID susijusių straipsnių duomenų rinkiniui](https://www.kaggle.com/allen-institute-for-ai/CORD-19-research-challenge) ir pamatyti, kokias įžvalgas galime gauti. [Šis tinklaraščio įrašas](https://soshnikov.com/science/analyzing-medical-papers-with-azure-and-text-analytics-for-health/) ir [šis straipsnis](https://www.mdpi.com/2504-2289/6/1/4) aprašo tyrimus, kurie gali būti atlikti su šiuo straipsnių korpusu naudojant NER.

---

**Atsakomybės apribojimas**:  
Šis dokumentas buvo išverstas naudojant AI vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba turėtų būti laikomas autoritetingu šaltiniu. Kritinei informacijai rekomenduojama naudoti profesionalų žmogaus vertimą. Mes neprisiimame atsakomybės už nesusipratimus ar klaidingus interpretavimus, atsiradusius dėl šio vertimo naudojimo.