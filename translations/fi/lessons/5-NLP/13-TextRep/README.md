<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4522e22e150be0845e03aa41209a39d5",
  "translation_date": "2025-08-28T20:08:38+00:00",
  "source_file": "lessons/5-NLP/13-TextRep/README.md",
  "language_code": "fi"
}
-->
# Tekstin esittäminen tensoreina

## [Ennakkovisa](https://ff-quizzes.netlify.app/en/ai/quiz/25)

## Tekstin luokittelu

Tämän osion ensimmäisessä osassa keskitymme **tekstin luokitteluun**. Käytämme [AG News](https://www.kaggle.com/amananandrai/ag-news-classification-dataset) -aineistoa, joka sisältää uutisartikkeleita, kuten seuraavan:

* Kategoria: Tiede/Teknologia
* Otsikko: Ky. Yhtiö saa apurahan peptidien tutkimiseen (AP)
* Sisältö: AP - Kemian tutkijan perustama yritys Louisvillen yliopistosta sai apurahan kehittääkseen...

Tavoitteenamme on luokitella uutinen tekstin perusteella yhteen kategorioista.

## Tekstin esittäminen

Jos haluamme ratkaista luonnollisen kielen käsittelyn (NLP) tehtäviä neuroverkoilla, meidän on löydettävä tapa esittää teksti tensoreina. Tietokoneet esittävät tekstimerkit jo numeroina, jotka vastaavat näytöllä näkyviä fontteja, käyttäen esimerkiksi ASCII- tai UTF-8-koodauksia.

<img alt="Kuva, joka näyttää kaavion, jossa merkki muunnetaan ASCII- ja binaariesitykseksi" src="images/ascii-character-map.png" width="50%"/>

> [Kuvan lähde](https://www.seobility.net/en/wiki/ASCII)

Ihmisinä ymmärrämme, mitä kukin kirjain **tarkoittaa**, ja miten kaikki merkit muodostavat yhdessä lauseen sanat. Tietokoneet eivät kuitenkaan itsessään ymmärrä tätä, ja neuroverkon on opittava merkitys koulutuksen aikana.

Siksi voimme käyttää erilaisia lähestymistapoja tekstin esittämiseen:

* **Merkkitason esitys**, jossa teksti esitetään käsittelemällä jokaista merkkiä numerona. Jos tekstikorpuksessamme on *C* erilaista merkkiä, sana *Hello* esitetään 5x*C*-tensorina. Jokainen kirjain vastaa tensorin saraketta one-hot-koodauksessa.
* **Sanatason esitys**, jossa luomme tekstimme kaikista sanoista **sanaston** ja esittelemme sanat one-hot-koodauksella. Tämä lähestymistapa on jossain määrin parempi, koska yksittäisillä kirjaimilla ei ole paljon merkitystä, ja käyttämällä korkeampia semanttisia käsitteitä - sanoja - yksinkertaistamme tehtävää neuroverkolle. Kuitenkin suuren sanaston koon vuoksi joudumme käsittelemään korkean ulottuvuuden harvoja tensoreita.

Riippumatta esitystavasta, meidän on ensin muunnettava teksti **tokeneiden** jaksoksi, joissa yksi token voi olla merkki, sana tai joskus jopa osa sanaa. Sitten muunnetaan token numeroksi, tyypillisesti käyttämällä **sanastoa**, ja tämä numero voidaan syöttää neuroverkkoon one-hot-koodauksen avulla.

## N-grammit

Luonnollisessa kielessä sanojen tarkka merkitys voidaan määrittää vain kontekstissa. Esimerkiksi *neuroverkko* ja *kalastusverkko* tarkoittavat täysin eri asioita. Yksi tapa ottaa tämä huomioon on rakentaa mallimme sanapareille ja käsitellä sanapareja erillisinä sanaston tokeneina. Näin lause *I like to go fishing* esitetään seuraavalla tokeneiden jaksolla: *I like*, *like to*, *to go*, *go fishing*. Tämän lähestymistavan ongelmana on, että sanaston koko kasvaa merkittävästi, ja yhdistelmät kuten *go fishing* ja *go shopping* esitetään eri tokeneina, joilla ei ole mitään semanttista yhteyttä, vaikka niissä on sama verbi.

Joissakin tapauksissa voimme harkita myös tri-grammien - kolmen sanan yhdistelmien - käyttöä. Tämän vuoksi lähestymistapaa kutsutaan usein **n-grammeiksi**. Lisäksi on järkevää käyttää n-grammeja merkkitason esityksessä, jolloin n-grammit vastaavat suunnilleen eri tavujen yhdistelmiä.

## Bag-of-Words ja TF/IDF

Kun ratkaistaan tehtäviä, kuten tekstin luokittelua, meidän on pystyttävä esittämään teksti yhdellä kiinteän kokoisella vektorilla, jota käytämme syötteenä lopulliselle tiheälle luokittelijalle. Yksi yksinkertaisimmista tavoista tehdä tämä on yhdistää kaikki yksittäiset sanan esitykset, esimerkiksi lisäämällä ne yhteen. Jos lisäämme jokaisen sanan one-hot-koodaukset, saamme vektorin, joka näyttää, kuinka monta kertaa kukin sana esiintyy tekstissä. Tällainen tekstin esitys tunnetaan nimellä **bag of words** (BoW).

<img src="images/bow.png" width="90%"/>

> Kuva kirjoittajan tekemä

BoW esittää käytännössä, mitkä sanat esiintyvät tekstissä ja missä määrin, mikä voi olla hyvä osoitus tekstin sisällöstä. Esimerkiksi poliittinen uutisartikkeli sisältää todennäköisesti sanoja kuten *presidentti* ja *maa*, kun taas tieteellinen julkaisu saattaa sisältää sanoja kuten *kiihdytin*, *löydetty* jne. Näin ollen sanan esiintymistiheydet voivat monissa tapauksissa olla hyvä osoitus tekstin sisällöstä.

BoW:n ongelmana on, että tietyt yleiset sanat, kuten *ja*, *on* jne., esiintyvät useimmissa teksteissä ja niillä on korkeimmat esiintymistiheydet, mikä peittää alleen sanat, jotka ovat todella tärkeitä. Voimme vähentää näiden sanojen merkitystä ottamalla huomioon, kuinka usein sanat esiintyvät koko dokumenttikokoelmassa. Tämä on TF/IDF-lähestymistavan perusidea, jota käsitellään tarkemmin tämän oppitunnin liitteenä olevissa muistikirjoissa.

Mikään näistä lähestymistavoista ei kuitenkaan pysty täysin huomioimaan tekstin **semantiikkaa**. Tarvitsemme tehokkaampia neuroverkkopohjaisia malleja tämän saavuttamiseksi, ja näitä käsitellään myöhemmin tässä osiossa.

## ✍️ Harjoitukset: Tekstin esittäminen

Jatka oppimista seuraavissa muistikirjoissa:

* [Tekstin esittäminen PyTorchilla](TextRepresentationPyTorch.ipynb)
* [Tekstin esittäminen TensorFlow'lla](TextRepresentationTF.ipynb)

## Yhteenveto

Tähän mennessä olemme tutkineet tekniikoita, jotka voivat lisätä painotusta eri sanojen esiintymistiheyksille. Ne eivät kuitenkaan pysty esittämään merkitystä tai järjestystä. Kuten kuuluisa kielitieteilijä J. R. Firth sanoi vuonna 1935: "Sanan täydellinen merkitys on aina kontekstuaalinen, eikä merkityksen tutkimista ilman kontekstia voida ottaa vakavasti." Kurssin myöhemmissä osissa opimme, kuinka tekstistä voidaan vangita kontekstuaalista tietoa kielimallinnuksen avulla.

## 🚀 Haaste

Kokeile muita harjoituksia käyttäen bag-of-words-menetelmää ja erilaisia datamalleja. Voit saada inspiraatiota tästä [Kaggle-kilpailusta](https://www.kaggle.com/competitions/word2vec-nlp-tutorial/overview/part-1-for-beginners-bag-of-words)

## [Jälkivisa](https://ff-quizzes.netlify.app/en/ai/quiz/26)

## Kertaus ja itseopiskelu

Harjoittele taitojasi tekstin upotusten ja bag-of-words-tekniikoiden parissa [Microsoft Learnissa](https://docs.microsoft.com/learn/modules/intro-natural-language-processing-pytorch/?WT.mc_id=academic-77998-cacaste)

## [Tehtävä: Muistikirjat](assignment.md)

---

**Vastuuvapauslauseke**:  
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, huomioithan, että automaattiset käännökset voivat sisältää virheitä tai epätarkkuuksia. Alkuperäinen asiakirja sen alkuperäisellä kielellä tulisi pitää ensisijaisena lähteenä. Kriittisen tiedon osalta suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa väärinkäsityksistä tai virhetulkinnoista, jotka johtuvat tämän käännöksen käytöstä.