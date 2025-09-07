<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "e40b47ac3fd48f71304ede1474e66293",
  "translation_date": "2025-08-28T20:07:22+00:00",
  "source_file": "lessons/5-NLP/14-Embeddings/README.md",
  "language_code": "fi"
}
-->
# Upotukset

## [Ennakkokysely](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/114)

Kun koulutimme luokittimia BoW:n tai TF/IDF:n perusteella, käytimme korkean ulottuvuuden bag-of-words-vektoreita, joiden pituus oli `vocab_size`, ja muunsimme eksplisiittisesti matalan ulottuvuuden paikkavektoreista harvoiksi yksiulotteisiksi vektoreiksi. Tämä yksiulotteinen esitys ei kuitenkaan ole muistin kannalta tehokas. Lisäksi jokaista sanaa käsitellään toisistaan riippumattomana, eli yksiulotteiset vektorit eivät ilmaise mitään semanttista samankaltaisuutta sanojen välillä.

**Upotuksen** idea on edustaa sanoja matalamman ulottuvuuden tiheillä vektoreilla, jotka jollain tavalla heijastavat sanan semanttista merkitystä. Myöhemmin keskustelemme siitä, miten rakentaa merkityksellisiä sanaupotuksia, mutta toistaiseksi voimme ajatella upotuksia tapana pienentää sanavektorin ulottuvuutta.

Upotuskerros ottaa sanan syötteenä ja tuottaa ulostulovektorin, jonka pituus on määritelty `embedding_size`. Tietyssä mielessä se on hyvin samanlainen kuin `Linear`-kerros, mutta sen sijaan, että se ottaisi yksiulotteisen vektorin, se voi ottaa sanan numeron syötteenä, jolloin voimme välttää suurten yksiulotteisten vektorien luomisen.

Käyttämällä upotuskerrosta luokittajaverkkomme ensimmäisenä kerroksena voimme siirtyä bag-of-words-mallista **embedding bag** -malliin, jossa ensin muutamme tekstimme jokaisen sanan vastaavaksi upotukseksi ja laskemme sitten jonkin aggregaattifunktion näiden upotusten yli, kuten `sum`, `average` tai `max`.  

![Kuva, joka näyttää upotusluokittimen viidelle sanalle sekvenssissä.](../../../../../translated_images/embedding-classifier-example.b77f021a7ee67eeec8e68bfe11636c5b97d6eaa067515a129bfb1d0034b1ac5b.fi.png)

> Kuva kirjoittajalta

## ✍️ Harjoitukset: Upotukset

Jatka oppimista seuraavissa muistikirjoissa:
* [Upotukset PyTorchilla](EmbeddingsPyTorch.ipynb)
* [Upotukset TensorFlowlla](EmbeddingsTF.ipynb)

## Semanttiset upotukset: Word2Vec

Vaikka upotuskerros oppi kartoittamaan sanat vektoriedustukseen, tämä edustus ei välttämättä sisältänyt paljon semanttista merkitystä. Olisi hyödyllistä oppia vektoriedustus, jossa samankaltaiset sanat tai synonyymit vastaavat vektoreita, jotka ovat lähellä toisiaan jonkin vektorietäisyyden (esim. euklidisen etäisyyden) suhteen.

Tämän saavuttamiseksi meidän täytyy esikouluttaa upotusmallimme suurella tekstikokoelmalla erityisellä tavalla. Yksi tapa kouluttaa semanttisia upotuksia on nimeltään [Word2Vec](https://en.wikipedia.org/wiki/Word2vec). Se perustuu kahteen pääarkkitehtuuriin, joita käytetään sanojen hajautetun edustuksen tuottamiseen:

 - **Jatkuva bag-of-words** (CBoW) — tässä arkkitehtuurissa koulutamme mallin ennustamaan sanan ympäröivästä kontekstista. Annetulla ngrammilla $(W_{-2},W_{-1},W_0,W_1,W_2)$ mallin tavoitteena on ennustaa $W_0$ käyttäen $(W_{-2},W_{-1},W_1,W_2)$.
 - **Jatkuva skip-gram** on CBoW:n vastakohta. Malli käyttää ympäröivää kontekstisanan ikkunaa ennustaakseen nykyisen sanan.

CBoW on nopeampi, kun taas skip-gram on hitaampi, mutta se edustaa harvinaisia sanoja paremmin.

![Kuva, joka näyttää sekä CBoW- että Skip-Gram-algoritmit sanojen muuntamiseksi vektoreiksi.](../../../../../translated_images/example-algorithms-for-converting-words-to-vectors.fbe9207a726922f6f0f5de66427e8a6eda63809356114e28fb1fa5f4a83ebda7.fi.png)

> Kuva [tästä artikkelista](https://arxiv.org/pdf/1301.3781.pdf)

Word2Vec-esikoulutetut upotukset (samoin kuin muut vastaavat mallit, kuten GloVe) voidaan myös käyttää upotuskerroksen sijasta neuroverkoissa. Meidän täytyy kuitenkin käsitellä sanastoja, koska Word2Vec/GloVe:n esikoulutuksessa käytetty sanasto eroaa todennäköisesti tekstikorpuksemme sanastosta. Tutustu yllä oleviin muistikirjoihin nähdäksesi, miten tämä ongelma voidaan ratkaista.

## Kontekstuaaliset upotukset

Yksi perinteisten esikoulutettujen upotusten, kuten Word2Vecin, keskeisistä rajoituksista on sanan merkityksen erottelun ongelma. Vaikka esikoulutetut upotukset voivat vangita osan sanojen merkityksestä kontekstissa, jokainen mahdollinen sanan merkitys koodataan samaan upotukseen. Tämä voi aiheuttaa ongelmia jatkomalleissa, koska monet sanat, kuten sana 'play', voivat tarkoittaa eri asioita riippuen kontekstista, jossa niitä käytetään.

Esimerkiksi sana 'play' näissä kahdessa eri lauseessa tarkoittaa hyvin eri asioita:

- Kävin teatterissa katsomassa **näytelmää**.
- John haluaa **leikkiä** ystäviensä kanssa.

Yllä olevat esikoulutetut upotukset edustavat molempia näytelmän merkityksiä samassa upotuksessa. Tämän rajoituksen voittamiseksi meidän täytyy rakentaa upotuksia **kielimallin** perusteella, joka on koulutettu suurella tekstikorpuksella ja *tietää*, miten sanoja voidaan yhdistää eri konteksteissa. Kontekstuaalisten upotusten käsittely on tämän oppitunnin ulkopuolella, mutta palaamme niihin myöhemmin kurssilla, kun puhumme kielimalleista.

## Yhteenveto

Tässä oppitunnissa opit rakentamaan ja käyttämään upotuskerroksia TensorFlowssa ja Pytorchissa, jotta sanojen semanttiset merkitykset heijastuisivat paremmin.

## 🚀 Haaste

Word2Veciä on käytetty joissakin mielenkiintoisissa sovelluksissa, kuten laululyriikan ja runouden luomisessa. Tutustu [tähän artikkeliin](https://www.politetype.com/blog/word2vec-color-poems), jossa kirjoittaja käy läpi, miten hän käytti Word2Veciä runojen luomiseen. Katso myös [tämä Dan Shiffmannin video](https://www.youtube.com/watch?v=LSS_bos_TPI&ab_channel=TheCodingTrain), jossa selitetään tätä tekniikkaa eri tavalla. Kokeile sitten soveltaa näitä tekniikoita omaan tekstikorpukseesi, ehkä Kagglesta hankittuun.

## [Jälkikysely](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/214)

## Kertaus ja itseopiskelu

Lue tämä Word2Vec-artikkeli: [Efficient Estimation of Word Representations in Vector Space](https://arxiv.org/pdf/1301.3781.pdf)

## [Tehtävä: Muistikirjat](assignment.md)

---

**Vastuuvapauslauseke**:  
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, huomioithan, että automaattiset käännökset voivat sisältää virheitä tai epätarkkuuksia. Alkuperäinen asiakirja sen alkuperäisellä kielellä tulisi pitää ensisijaisena lähteenä. Kriittisen tiedon osalta suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa väärinkäsityksistä tai virhetulkinnoista, jotka johtuvat tämän käännöksen käytöstä.