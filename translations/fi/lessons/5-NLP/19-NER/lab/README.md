# NER

Lab-tehtävä [AI for Beginners Curriculum](https://github.com/microsoft/ai-for-beginners) -materiaalista.

## Tehtävä

Tässä laboratoriossa sinun tulee kouluttaa nimettyjen entiteettien tunnistusmalli (NER) lääketieteellisiä termejä varten.

## Datasetti

NER-mallin kouluttamiseen tarvitaan asianmukaisesti merkitty datasetti, joka sisältää lääketieteellisiä entiteettejä. [BC5CDR datasetti](https://biocreative.bioinformatics.udel.edu/tasks/biocreative-v/track-3-cdr/) sisältää merkittyjä sairauksia ja kemiallisia entiteettejä yli 1500 julkaisusta. Voit ladata datasetin rekisteröitymällä heidän verkkosivustollaan.

BC5CDR datasetti näyttää tältä:

```
6794356|t|Tricuspid valve regurgitation and lithium carbonate toxicity in a newborn infant.
6794356|a|A newborn with massive tricuspid regurgitation, atrial flutter, congestive heart failure, and a high serum lithium level is described. This is the first patient to initially manifest tricuspid regurgitation and atrial flutter, and the 11th described patient with cardiac disease among infants exposed to lithium compounds in the first trimester of pregnancy. Sixty-three percent of these infants had tricuspid valve involvement. Lithium carbonate may be a factor in the increasing incidence of congenital heart disease when taken during early pregnancy. It also causes neurologic depression, cyanosis, and cardiac arrhythmia when consumed prior to delivery.
6794356	0	29	Tricuspid valve regurgitation	Disease	D014262
6794356	34	51	lithium carbonate	Chemical	D016651
6794356	52	60	toxicity	Disease	D064420
...
```

Tässä datasetissä ensimmäiset kaksi riviä sisältävät julkaisun otsikon ja tiivistelmän, ja sen jälkeen yksittäiset entiteetit, joissa on alku- ja loppusijainnit otsikko+tiivistelmä -osiossa. Entiteettityypin lisäksi saat tämän entiteetin ontologia-ID:n jossain lääketieteellisessä ontologiassa.

Sinun tulee kirjoittaa Python-koodia muuntaaksesi tämän BIO-koodaukseen.

## Verkko

Ensimmäinen yritys NER-mallin luomisessa voidaan tehdä käyttämällä LSTM-verkkoa, kuten esimerkissä, jonka näit oppitunnin aikana. Kuitenkin NLP-tehtävissä [transformer-arkkitehtuuri](https://en.wikipedia.org/wiki/Transformer_(machine_learning_model)) ja erityisesti [BERT-kielimallit](https://en.wikipedia.org/wiki/BERT_(language_model)) tuottavat paljon parempia tuloksia. Esikoulutetut BERT-mallit ymmärtävät kielen yleisen rakenteen ja niitä voidaan hienosäätää erityisiin tehtäviin suhteellisen pienillä dataseteillä ja laskentakustannuksilla.

Koska suunnittelemme NER-mallin soveltamista lääketieteelliseen skenaarioon, on järkevää käyttää BERT-mallia, joka on koulutettu lääketieteellisillä teksteillä. Microsoft Research on julkaissut esikoulutetun mallin nimeltä [PubMedBERT][PubMedBERT] ([julkaisu][PubMedBERT-Pub]), joka on hienosäädetty [PubMed](https://pubmed.ncbi.nlm.nih.gov/) -arkiston teksteillä.

Transformer-mallien koulutuksen *de facto* standardi on [Hugging Face Transformers](https://huggingface.co/) -kirjasto. Se sisältää myös yhteisön ylläpitämän esikoulutettujen mallien arkiston, mukaan lukien PubMedBERT. Tämän mallin lataamiseen ja käyttämiseen tarvitaan vain muutama rivi koodia:

```python
model_name = "microsoft/BiomedNLP-PubMedBERT-base-uncased-abstract"
classes = ... # number of classes: 2*entities+1
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = BertForTokenClassification.from_pretrained(model_name, classes)
```

Tämä antaa meille `model`-objektin, joka on rakennettu token-luokittelutehtävää varten käyttäen `classes`-luokkien määrää, sekä `tokenizer`-objektin, joka voi jakaa syötetyn tekstin tokeneiksi. Sinun tulee muuntaa datasetti BIO-muotoon ottaen huomioon PubMedBERT-tokenisointi. Voit käyttää [tätä Python-koodinpätkää](https://gist.github.com/shwars/580b55684be3328eb39ecf01b9cbbd88) inspiraationa.

## Yhteenveto

Tämä tehtävä on hyvin lähellä todellista tehtävää, jonka saatat kohdata, jos haluat saada enemmän tietoa suurista luonnollisen kielen tekstimääristä. Meidän tapauksessamme voimme soveltaa koulutettua malliamme [COVID-aiheisten julkaisujen datasettiin](https://www.kaggle.com/allen-institute-for-ai/CORD-19-research-challenge) ja nähdä, mitä oivalluksia voimme saada. [Tämä blogikirjoitus](https://soshnikov.com/science/analyzing-medical-papers-with-azure-and-text-analytics-for-health/) ja [tämä julkaisu](https://www.mdpi.com/2504-2289/6/1/4) kuvaavat tutkimusta, jota voidaan tehdä tämän julkaisukorpuksen avulla käyttäen NER-mallia.

---

**Vastuuvapauslauseke**:  
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, huomioithan, että automaattiset käännökset voivat sisältää virheitä tai epätarkkuuksia. Alkuperäinen asiakirja sen alkuperäisellä kielellä tulisi pitää ensisijaisena lähteenä. Kriittisen tiedon osalta suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa väärinkäsityksistä tai virhetulkinnoista, jotka johtuvat tämän käännöksen käytöstä.