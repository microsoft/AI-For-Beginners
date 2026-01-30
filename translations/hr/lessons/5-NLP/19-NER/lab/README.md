# NER

Laboratorijska vježba iz [AI for Beginners Curriculum](https://github.com/microsoft/ai-for-beginners).

## Zadatak

U ovom laboratoriju trebate trenirati model za prepoznavanje imenovanih entiteta (NER) za medicinske pojmove.

## Skup podataka

Za treniranje NER modela potreban nam je pravilno označen skup podataka s medicinskim entitetima. [BC5CDR skup podataka](https://biocreative.bioinformatics.udel.edu/tasks/biocreative-v/track-3-cdr/) sadrži označene entitete bolesti i kemikalija iz više od 1500 radova. Skup podataka možete preuzeti nakon registracije na njihovoj web stranici.

BC5CDR skup podataka izgleda ovako:

```
6794356|t|Tricuspid valve regurgitation and lithium carbonate toxicity in a newborn infant.
6794356|a|A newborn with massive tricuspid regurgitation, atrial flutter, congestive heart failure, and a high serum lithium level is described. This is the first patient to initially manifest tricuspid regurgitation and atrial flutter, and the 11th described patient with cardiac disease among infants exposed to lithium compounds in the first trimester of pregnancy. Sixty-three percent of these infants had tricuspid valve involvement. Lithium carbonate may be a factor in the increasing incidence of congenital heart disease when taken during early pregnancy. It also causes neurologic depression, cyanosis, and cardiac arrhythmia when consumed prior to delivery.
6794356	0	29	Tricuspid valve regurgitation	Disease	D014262
6794356	34	51	lithium carbonate	Chemical	D016651
6794356	52	60	toxicity	Disease	D064420
...
```

U ovom skupu podataka, naslov rada i sažetak nalaze se u prva dva retka, a zatim slijede pojedinačni entiteti s početnim i završnim pozicijama unutar bloka naslov+sažetak. Osim vrste entiteta, dobivate i ontološki ID tog entiteta unutar neke medicinske ontologije.

Trebat ćete napisati Python kod za pretvaranje ovog skupa podataka u BIO kodiranje.

## Mreža

Prvi pokušaj NER-a može se napraviti korištenjem LSTM mreže, kao što ste vidjeli u našem primjeru tijekom lekcije. Međutim, u NLP zadacima, [transformerska arhitektura](https://en.wikipedia.org/wiki/Transformer_(machine_learning_model)), a posebno [BERT jezični modeli](https://en.wikipedia.org/wiki/BERT_(language_model)) pokazuju znatno bolje rezultate. Prethodno trenirani BERT modeli razumiju opću strukturu jezika i mogu se dodatno prilagoditi za specifične zadatke s relativno malim skupovima podataka i računalnim troškovima.

Budući da planiramo primijeniti NER na medicinski scenarij, logično je koristiti BERT model treniran na medicinskim tekstovima. Microsoft Research objavio je prethodno trenirani model pod nazivom [PubMedBERT][PubMedBERT] ([publikacija][PubMedBERT-Pub]), koji je dodatno treniran koristeći tekstove iz [PubMed](https://pubmed.ncbi.nlm.nih.gov/) repozitorija.

*De facto* standard za treniranje transformerskih modela je biblioteka [Hugging Face Transformers](https://huggingface.co/). Također sadrži repozitorij unaprijed treniranih modela koje održava zajednica, uključujući PubMedBERT. Za učitavanje i korištenje ovog modela, potrebno je samo nekoliko linija koda:

```python
model_name = "microsoft/BiomedNLP-PubMedBERT-base-uncased-abstract"
classes = ... # number of classes: 2*entities+1
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = BertForTokenClassification.from_pretrained(model_name, classes)
```

Ovo nam daje sam `model`, izgrađen za zadatak klasifikacije tokena koristeći `classes` broj klasa, kao i `tokenizer` objekt koji može podijeliti ulazni tekst na tokene. Trebat ćete pretvoriti skup podataka u BIO format, uzimajući u obzir tokenizaciju PubMedBERT-a. Kao inspiraciju možete koristiti [ovaj Python kod](https://gist.github.com/shwars/580b55684be3328eb39ecf01b9cbbd88).

## Zaključak

Ovaj zadatak vrlo je sličan stvarnom zadatku koji biste mogli imati ako želite dobiti više uvida u velike količine tekstova na prirodnom jeziku. U našem slučaju, možemo primijeniti naš trenirani model na [skup podataka radova povezanih s COVID-om](https://www.kaggle.com/allen-institute-for-ai/CORD-19-research-challenge) i vidjeti koje uvide možemo dobiti. [Ovaj blog post](https://soshnikov.com/science/analyzing-medical-papers-with-azure-and-text-analytics-for-health/) i [ovaj rad](https://www.mdpi.com/2504-2289/6/1/4) opisuju istraživanja koja se mogu provesti na ovom korpusu radova koristeći NER.

**Odricanje od odgovornosti**:  
Ovaj dokument je preveden pomoću AI usluge za prevođenje [Co-op Translator](https://github.com/Azure/co-op-translator). Iako nastojimo osigurati točnost, imajte na umu da automatski prijevodi mogu sadržavati pogreške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati autoritativnim izvorom. Za kritične informacije preporučuje se profesionalni prijevod od strane čovjeka. Ne preuzimamo odgovornost za nesporazume ili pogrešna tumačenja koja mogu proizaći iz korištenja ovog prijevoda.