# NER

Laboratorijska naloga iz [učnega načrta AI za začetnike](https://github.com/microsoft/ai-for-beginners).

## Naloga

V tej nalogi morate trenirati model za prepoznavanje imenovanih entitet (NER) za medicinske izraze.

## Podatkovni nabor

Za treniranje modela NER potrebujemo ustrezno označen podatkovni nabor z medicinskimi entitetami. [Podatkovni nabor BC5CDR](https://biocreative.bioinformatics.udel.edu/tasks/biocreative-v/track-3-cdr/) vsebuje označene entitete bolezni in kemikalij iz več kot 1500 člankov. Podatkovni nabor lahko prenesete po registraciji na njihovi spletni strani.

Podatkovni nabor BC5CDR je videti takole:

```
6794356|t|Tricuspid valve regurgitation and lithium carbonate toxicity in a newborn infant.
6794356|a|A newborn with massive tricuspid regurgitation, atrial flutter, congestive heart failure, and a high serum lithium level is described. This is the first patient to initially manifest tricuspid regurgitation and atrial flutter, and the 11th described patient with cardiac disease among infants exposed to lithium compounds in the first trimester of pregnancy. Sixty-three percent of these infants had tricuspid valve involvement. Lithium carbonate may be a factor in the increasing incidence of congenital heart disease when taken during early pregnancy. It also causes neurologic depression, cyanosis, and cardiac arrhythmia when consumed prior to delivery.
6794356	0	29	Tricuspid valve regurgitation	Disease	D014262
6794356	34	51	lithium carbonate	Chemical	D016651
6794356	52	60	toxicity	Disease	D064420
...
```

V tem podatkovnem naboru sta naslov članka in povzetek navedena v prvih dveh vrsticah, nato pa sledijo posamezne entitete z začetnimi in končnimi položaji znotraj bloka naslov+povzetek. Poleg vrste entitete dobite tudi ontološki ID te entitete znotraj določene medicinske ontologije.

Potrebno bo napisati nekaj kode v Pythonu, da podatke pretvorite v BIO kodiranje.

## Mreža

Prvi poskus pri NER lahko izvedete z uporabo LSTM mreže, kot ste videli v našem primeru med lekcijo. Vendar pa pri nalogah obdelave naravnega jezika (NLP) [transformerska arhitektura](https://en.wikipedia.org/wiki/Transformer_(machine_learning_model)) in posebej [BERT-jevi jezikovni modeli](https://en.wikipedia.org/wiki/BERT_(language_model)) dosegajo veliko boljše rezultate. Predtrenirani BERT modeli razumejo splošno strukturo jezika in jih je mogoče prilagoditi za specifične naloge z razmeroma majhnimi podatkovnimi nabori in nizkimi računalniškimi stroški.

Ker načrtujemo uporabo NER v medicinskem scenariju, je smiselno uporabiti BERT model, treniran na medicinskih besedilih. Microsoft Research je izdal predtreniran model z imenom [PubMedBERT][PubMedBERT] ([objava][PubMedBERT-Pub]), ki je bil prilagojen z uporabo besedil iz repozitorija [PubMed](https://pubmed.ncbi.nlm.nih.gov/).

*De facto* standard za treniranje transformerskih modelov je knjižnica [Hugging Face Transformers](https://huggingface.co/). Vsebuje tudi repozitorij modelov, ki jih vzdržuje skupnost, vključno s PubMedBERT. Za nalaganje in uporabo tega modela potrebujemo le nekaj vrstic kode:

```python
model_name = "microsoft/BiomedNLP-PubMedBERT-base-uncased-abstract"
classes = ... # number of classes: 2*entities+1
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = BertForTokenClassification.from_pretrained(model_name, classes)
```

To nam zagotovi sam `model`, zgrajen za nalogo klasifikacije tokenov z uporabo `classes` števila razredov, ter objekt `tokenizer`, ki lahko razdeli vhodno besedilo na tokene. Podatkovni nabor boste morali pretvoriti v BIO format, pri čemer upoštevajte tokenizacijo PubMedBERT. Kot navdih lahko uporabite [ta del kode v Pythonu](https://gist.github.com/shwars/580b55684be3328eb39ecf01b9cbbd88).

## Ključne ugotovitve

Ta naloga je zelo podobna dejanski nalogi, s katero se boste verjetno srečali, če želite pridobiti več vpogleda v velike količine besedil v naravnem jeziku. V našem primeru lahko naš trenirani model uporabimo na [podatkovnem naboru člankov, povezanih s COVID-om](https://www.kaggle.com/allen-institute-for-ai/CORD-19-research-challenge) in preverimo, katere vpoglede lahko pridobimo. [Ta objava na blogu](https://soshnikov.com/science/analyzing-medical-papers-with-azure-and-text-analytics-for-health/) in [ta članek](https://www.mdpi.com/2504-2289/6/1/4) opisujeta raziskave, ki jih je mogoče opraviti na tem korpusu člankov z uporabo NER.

**Omejitev odgovornosti**:  
Ta dokument je bil preveden z uporabo storitve AI za prevajanje [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas prosimo, da upoštevate, da lahko avtomatizirani prevodi vsebujejo napake ali netočnosti. Izvirni dokument v njegovem maternem jeziku je treba obravnavati kot avtoritativni vir. Za ključne informacije priporočamo profesionalni človeški prevod. Ne prevzemamo odgovornosti za morebitne nesporazume ali napačne razlage, ki bi nastale zaradi uporabe tega prevoda.