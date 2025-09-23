<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "d7f8a25ff13cfe9f4cd671cc23351fad",
  "translation_date": "2025-08-28T19:35:27+00:00",
  "source_file": "lessons/4-ComputerVision/12-Segmentation/README.md",
  "language_code": "fi"
}
-->
# Segmentointi

Olemme aiemmin oppineet objektien tunnistamisesta, jonka avulla voimme paikantaa objektit kuvasta ennustamalla niiden *rajauslaatikot*. Joissakin tehtävissä emme kuitenkaan tarvitse pelkästään rajauslaatikoita, vaan myös tarkempaa objektien paikannusta. Tätä tehtävää kutsutaan **segmentoinniksi**.

## [Pre-lecture quiz](https://ff-quizzes.netlify.app/en/ai/quiz/23)

Segmentointia voidaan pitää **pikseliluokitteluna**, jossa jokaiselle kuvan **pikselille** täytyy ennustaa sen luokka (*tausta* on yksi luokista). Segmentointialgoritmeja on kaksi päätyyppiä:

* **Semanttinen segmentointi** kertoo vain pikselin luokan, mutta ei erottele saman luokan eri objekteja.
* **Instanssisegmentointi** jakaa luokat eri instansseihin.

Esimerkiksi instanssisegmentoinnissa nämä lampaat ovat eri objekteja, mutta semanttisessa segmentoinnissa kaikki lampaat kuuluvat yhteen luokkaan.

<img src="images/instance_vs_semantic.jpeg" width="50%">

> Kuva [tästä blogikirjoituksesta](https://nirmalamurali.medium.com/image-classification-vs-semantic-segmentation-vs-instance-segmentation-625c33a08d50)

Segmentointiin on olemassa erilaisia neuroverkkoarkkitehtuureja, mutta niillä kaikilla on sama rakenne. Tavallaan se muistuttaa aiemmin oppimaasi autoenkooderia, mutta alkuperäisen kuvan purkamisen sijaan tavoitteemme on purkaa **maski**. Segmentointiverkolla on seuraavat osat:

* **Kooderi**, joka poimii piirteitä syötekuvasta.
* **Dekooderi**, joka muuntaa nämä piirteet **maskikuvaksi**, jonka koko ja kanavien määrä vastaavat luokkien määrää.

<img src="images/segm.png" width="80%">

> Kuva [tästä julkaisusta](https://arxiv.org/pdf/2001.05566.pdf)

Erityisesti on mainittava segmentoinnissa käytettävä häviöfunktio. Klassisia autoenkoodereita käytettäessä meidän täytyy mitata kahden kuvan samankaltaisuutta, ja tähän voidaan käyttää keskineliövirhettä (MSE). Segmentoinnissa kohdemaskikuvan jokainen pikseli edustaa luokkanumeroa (yksi-kuuma-koodattuna kolmannessa ulottuvuudessa), joten meidän täytyy käyttää luokitteluun tarkoitettuja häviöfunktioita - ristiinentroopiahäviötä, joka on keskiarvoistettu kaikille pikseleille. Jos maski on binäärinen, käytetään **binääristä ristiinentroopiahäviötä** (BCE).

> ✅ Yksi-kuuma-koodaus on tapa koodata luokkamerkki vektoriksi, jonka pituus vastaa luokkien määrää. Tutustu [tähän artikkeliin](https://datagy.io/sklearn-one-hot-encode/) saadaksesi lisätietoja tästä tekniikasta.

## Segmentointi lääketieteellisissä kuvissa

Tässä oppitunnissa näemme segmentoinnin toiminnassa kouluttamalla verkon tunnistamaan ihmisen luomia (tunnetaan myös nimellä "moolit") lääketieteellisistä kuvista. Käytämme <a href="https://www.fc.up.pt/addi/ph2%20database.html">PH<sup>2</sup>-tietokantaa</a>, joka sisältää dermoskopiakuvia. Tämä tietokanta sisältää 200 kuvaa kolmesta luokasta: tyypillinen luomi, epätyypillinen luomi ja melanooma. Kaikilla kuvilla on myös vastaava **maski**, joka rajaa luomen.

> ✅ Tämä tekniikka sopii erityisen hyvin tämän tyyppisiin lääketieteellisiin kuviin, mutta mitä muita tosielämän sovelluksia voisit kuvitella?

<img alt="navi" src="images/navi.png"/>

> Kuva PH<sup>2</sup>-tietokannasta

Koulutamme mallin segmentoimaan minkä tahansa luomen taustastaan.

## ✍️ Harjoitukset: Semanttinen segmentointi

Avaa alla olevat muistikirjat oppiaksesi lisää erilaisista semanttisen segmentoinnin arkkitehtuureista, harjoitellaksesi niiden käyttöä ja nähdäksesi ne toiminnassa.

* [Semantic Segmentation Pytorch](SemanticSegmentationPytorch.ipynb)
* [Semantic Segmentation TensorFlow](SemanticSegmentationTF.ipynb)

## [Post-lecture quiz](https://ff-quizzes.netlify.app/en/ai/quiz/24)

## Yhteenveto

Segmentointi on erittäin tehokas tekniikka kuvien luokittelussa, joka menee rajausbokseja pidemmälle pikselitason luokitteluun. Sitä käytetään lääketieteellisissä kuvissa ja monissa muissa sovelluksissa.

## 🚀 Haaste

Kehon segmentointi on vain yksi yleisistä tehtävistä, joita voimme tehdä ihmisten kuvilla. Muita tärkeitä tehtäviä ovat **luurangon tunnistus** ja **asennon tunnistus**. Kokeile [OpenPose](https://github.com/CMU-Perceptual-Computing-Lab/openpose)-kirjastoa nähdäksesi, miten asennon tunnistusta voidaan käyttää.

## Kertaus ja itseopiskelu

Tämä [Wikipedia-artikkeli](https://wikipedia.org/wiki/Image_segmentation) tarjoaa hyvän yleiskatsauksen tämän tekniikan eri sovelluksista. Opi lisää itsenäisesti instanssisegmentoinnin ja panoptisen segmentoinnin alalajeista tässä tutkimuskentässä.

## [Tehtävä](lab/README.md)

Tässä laboratoriossa kokeile **ihmiskehon segmentointia** käyttäen [Segmentation Full Body MADS Dataset](https://www.kaggle.com/datasets/tapakah68/segmentation-full-body-mads-dataset)-tietokantaa Kagglesta.

---

**Vastuuvapauslauseke**:  
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, huomioithan, että automaattiset käännökset voivat sisältää virheitä tai epätarkkuuksia. Alkuperäinen asiakirja sen alkuperäisellä kielellä tulisi pitää ensisijaisena lähteenä. Kriittisen tiedon osalta suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa väärinkäsityksistä tai virhetulkinnoista, jotka johtuvat tämän käännöksen käytöstä.