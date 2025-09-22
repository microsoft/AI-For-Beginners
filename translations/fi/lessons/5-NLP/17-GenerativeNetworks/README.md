<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "d9de7847385eeeda67cfdcce1640ab72",
  "translation_date": "2025-08-28T19:58:30+00:00",
  "source_file": "lessons/5-NLP/17-GenerativeNetworks/README.md",
  "language_code": "fi"
}
-->
# Generatiiviset verkot

## [Esiluentakysely](https://ff-quizzes.netlify.app/en/ai/quiz/33)

Toistuvat neuroverkot (Recurrent Neural Networks, RNN) ja niiden porttimalliset solumuunnelmat, kuten Long Short Term Memory Cells (LSTM) ja Gated Recurrent Units (GRU), tarjoavat mekanismin kielen mallintamiseen, koska ne voivat oppia sanojen järjestyksen ja ennustaa seuraavan sanan sekvenssissä. Tämä mahdollistaa RNN:ien käytön **generatiivisissa tehtävissä**, kuten tavallisessa tekstin generoinnissa, konekäännöksessä ja jopa kuvatekstien luomisessa.

> ✅ Mieti kaikkia niitä kertoja, kun olet hyötynyt generatiivisista tehtävistä, kuten tekstin täydennyksestä kirjoittaessasi. Tutki suosikkisovelluksiasi ja selvitä, ovatko ne hyödyntäneet RNN:ejä.

Edellisessä yksikössä käsitellyssä RNN-arkkitehtuurissa jokainen RNN-yksikkö tuotti seuraavan piilotilan ulostulona. Voimme kuitenkin lisätä toisen ulostulon jokaiseen toistuvaan yksikköön, mikä mahdollistaa **sekvenssin** tuottamisen (joka on yhtä pitkä kuin alkuperäinen sekvenssi). Lisäksi voimme käyttää RNN-yksiköitä, jotka eivät ota syötettä jokaisessa vaiheessa, vaan ottavat vain alkuperäisen tilavektorin ja tuottavat sitten ulostulon sekvenssin.

Tämä mahdollistaa erilaiset neuroverkkoarkkitehtuurit, jotka on esitetty alla olevassa kuvassa:

![Kuva, joka näyttää yleisiä toistuvien neuroverkkojen malleja.](../../../../../translated_images/unreasonable-effectiveness-of-rnn.541ead816778f42dce6c42d8a56c184729aa2378d059b851be4ce12b993033df.fi.jpg)

> Kuva blogikirjoituksesta [Unreasonable Effectiveness of Recurrent Neural Networks](http://karpathy.github.io/2015/05/21/rnn-effectiveness/) kirjoittanut [Andrej Karpaty](http://karpathy.github.io/)

* **Yksi-yhteen** on perinteinen neuroverkko, jossa on yksi syöte ja yksi ulostulo
* **Yksi-moneen** on generatiivinen arkkitehtuuri, joka ottaa yhden syötearvon ja tuottaa sekvenssin ulostuloarvoja. Esimerkiksi, jos haluamme kouluttaa **kuvatekstien luontiverkon**, joka tuottaa tekstikuvauksen kuvasta, voimme syöttää kuvan, käsitellä sen CNN:llä saadaksemme piilotilan ja käyttää sitten toistuvaa ketjua tuottamaan kuvatekstin sana sanalta
* **Moneen-yksi** vastaa edellisessä yksikössä kuvattuja RNN-arkkitehtuureja, kuten tekstiluokittelua
* **Moneen-moneen**, tai **sekvenssi-sekvenssi**, vastaa tehtäviä, kuten **konekäännös**, jossa ensimmäinen RNN kerää kaiken tiedon syötesekvenssistä piilotilaan, ja toinen RNN-ketju purkaa tämän tilan ulostulosekvenssiksi.

Tässä yksikössä keskitymme yksinkertaisiin generatiivisiin malleihin, jotka auttavat meitä tuottamaan tekstiä. Yksinkertaisuuden vuoksi käytämme merkkitason tokenisointia.

Koulutamme tämän RNN:n tuottamaan tekstiä askel askeleelta. Jokaisessa vaiheessa otamme merkkisekvenssin, jonka pituus on `nchars`, ja pyydämme verkkoa tuottamaan seuraavan ulostulomerkin jokaiselle syötemerkille:

![Kuva, joka näyttää esimerkin RNN:n sanan 'HELLO' generoinnista.](../../../../../translated_images/rnn-generate.56c54afb52f9781d63a7c16ea9c1b86cb70e6e1eae6a742b56b7b37468576b17.fi.png)

Kun tuotamme tekstiä (inference-vaiheessa), aloitamme jollakin **aloitussyötteellä**, joka syötetään RNN-soluihin tuottamaan niiden välimuisti, ja tästä tilasta alkaa generointi. Tuotamme yhden merkin kerrallaan ja syötämme tilan ja tuotetun merkin seuraavaan RNN-soluun tuottamaan seuraavan merkin, kunnes olemme tuottaneet tarpeeksi merkkejä.

<img src="images/rnn-generate-inf.png" width="60%"/>

> Kuva kirjoittajalta

## ✍️ Harjoitukset: Generatiiviset verkot

Jatka oppimista seuraavissa muistikirjoissa:

* [Generatiiviset verkot PyTorchilla](GenerativePyTorch.ipynb)
* [Generatiiviset verkot TensorFlow'lla](GenerativeTF.ipynb)

## Pehmeä tekstin generointi ja lämpötila

Jokaisen RNN-solun ulostulo on merkkien todennäköisyysjakauma. Jos aina valitsemme merkin, jolla on korkein todennäköisyys seuraavaksi merkiksi generoidussa tekstissä, teksti voi usein "jäädä kiertämään" samoja merkkisekvenssejä uudelleen ja uudelleen, kuten tässä esimerkissä:

```
today of the second the company and a second the company ...
```

Jos kuitenkin tarkastelemme seuraavan merkin todennäköisyysjakaumaa, voi olla, että muutaman korkeimman todennäköisyyden ero ei ole suuri, esimerkiksi yksi merkki voi saada todennäköisyyden 0,2 ja toinen 0,19. Esimerkiksi, kun etsitään seuraavaa merkkiä sekvenssissä '*play*', seuraava merkki voi yhtä hyvin olla joko välilyönti tai **e** (kuten sanassa *player*).

Tämä johtaa siihen johtopäätökseen, että ei ole aina "oikeudenmukaista" valita merkkiä, jolla on korkein todennäköisyys, koska toisen korkeimman valitseminen voi silti johtaa mielekkääseen tekstiin. On viisaampaa **näytteistää** merkkejä verkon ulostulon antamasta todennäköisyysjakaumasta. Voimme myös käyttää parametria, **lämpötila**, joka tasoittaa todennäköisyysjakaumaa, jos haluamme lisätä satunnaisuutta, tai tekee siitä jyrkemmän, jos haluamme pitäytyä enemmän korkeimman todennäköisyyden merkeissä.

Tutki, miten tämä pehmeä tekstin generointi on toteutettu yllä linkitetyissä muistikirjoissa.

## Yhteenveto

Vaikka tekstin generointi voi olla hyödyllistä itsessään, suurimmat hyödyt tulevat kyvystä tuottaa tekstiä RNN:ien avulla jostakin alkuperäisestä piirrevektorista. Esimerkiksi tekstin generointia käytetään osana konekäännöstä (sekvenssi-sekvenssi, tässä tapauksessa *enkooderin* tilavektoria käytetään tuottamaan tai *dekoodaamaan* käännetty viesti) tai kuvan tekstikuvauksen luomista (jolloin piirrevektori tulee CNN-uutteesta).

## 🚀 Haaste

Ota oppitunteja Microsoft Learn -alustalta tästä aiheesta

* Tekstin generointi [PyTorchilla](https://docs.microsoft.com/learn/modules/intro-natural-language-processing-pytorch/6-generative-networks/?WT.mc_id=academic-77998-cacaste)/[TensorFlow'lla](https://docs.microsoft.com/learn/modules/intro-natural-language-processing-tensorflow/5-generative-networks/?WT.mc_id=academic-77998-cacaste)

## [Jälkiluentakysely](https://ff-quizzes.netlify.app/en/ai/quiz/34)

## Kertaus ja itseopiskelu

Tässä on joitakin artikkeleita tietämyksesi laajentamiseksi

* Eri lähestymistapoja tekstin generointiin Markovin ketjuilla, LSTM:llä ja GPT-2:lla: [blogikirjoitus](https://towardsdatascience.com/text-generation-gpt-2-lstm-markov-chain-9ea371820e1e)
* Tekstin generoinnin esimerkki [Keras-dokumentaatiossa](https://keras.io/examples/generative/lstm_character_level_text_generation/)

## [Tehtävä](lab/README.md)

Olemme nähneet, kuinka tekstiä voidaan generoida merkki kerrallaan. Laboratoriossa tutkit sanatasoista tekstin generointia.

---

**Vastuuvapauslauseke**:  
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, huomioithan, että automaattiset käännökset voivat sisältää virheitä tai epätarkkuuksia. Alkuperäinen asiakirja sen alkuperäisellä kielellä tulisi pitää ensisijaisena lähteenä. Kriittisen tiedon osalta suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa väärinkäsityksistä tai virhetulkinnoista, jotka johtuvat tämän käännöksen käytöstä.