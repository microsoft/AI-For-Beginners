<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "bd10f434e444bce61b7f97eeb1ff6a55",
  "translation_date": "2025-08-28T20:03:50+00:00",
  "source_file": "lessons/5-NLP/19-NER/README.md",
  "language_code": "fi"
}
-->
# Nimettyjen Entiteettien Tunnistus

Tähän asti olemme keskittyneet pääasiassa yhteen NLP-tehtävään - luokitteluun. On kuitenkin olemassa myös muita NLP-tehtäviä, joita voidaan toteuttaa neuroverkoilla. Yksi näistä tehtävistä on **[nimettyjen entiteettien tunnistus](https://wikipedia.org/wiki/Named-entity_recognition)** (NER), joka keskittyy tunnistamaan tekstistä tiettyjä entiteettejä, kuten paikkoja, henkilön nimiä, päivämäärä- ja aikavälejä, kemiallisia kaavoja ja niin edelleen.

## [Ennakkokysely](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/119)

## Esimerkki NER:n käytöstä

Oletetaan, että haluat kehittää luonnollisen kielen chatbotin, joka on samanlainen kuin Amazon Alexa tai Google Assistant. Älykkäät chatbotit toimivat *ymmärtämällä* käyttäjän tarpeet tekemällä tekstiluokittelua syötteenä annettuun lauseeseen. Tämän luokittelun tuloksena saadaan niin sanottu **intentio**, joka määrittää, mitä chatbotin tulisi tehdä.

<img alt="Bot NER" src="images/bot-ner.png" width="50%"/>

> Kuva tekijältä

Käyttäjä voi kuitenkin antaa joitakin parametreja osana lausetta. Esimerkiksi säätä kysyessään hän voi määrittää sijainnin tai ajankohdan. Botin tulisi pystyä ymmärtämään nämä entiteetit ja täyttämään parametripaikat vastaavasti ennen toiminnon suorittamista. Juuri tässä NER astuu kuvaan.

> ✅ Toinen esimerkki voisi olla [tieteellisten lääketieteellisten artikkeleiden analysointi](https://soshnikov.com/science/analyzing-medical-papers-with-azure-and-text-analytics-for-health/). Yksi tärkeimmistä asioista, joita meidän täytyy etsiä, ovat tietyt lääketieteelliset termit, kuten sairaudet ja lääkeaineet. Vaikka pieni määrä sairauksia voidaan todennäköisesti tunnistaa merkkijonohakua käyttämällä, monimutkaisemmat entiteetit, kuten kemialliset yhdisteet ja lääkkeiden nimet, vaativat monimutkaisempaa lähestymistapaa.

## NER tokeniluokitteluna

NER-mallit ovat pohjimmiltaan **tokeniluokittelumalleja**, koska jokaiselle syötteen tokenille meidän täytyy päättää, kuuluuko se johonkin entiteettiin vai ei, ja jos kuuluu - mihin entiteettiluokkaan.

Tarkastellaan seuraavaa artikkelin otsikkoa:

**Kolmipurjeläpän vuoto** ja **litiumkarbonaatin** **toksisuus** vastasyntyneellä lapsella.

Entiteetit tässä ovat:

* Kolmipurjeläpän vuoto on sairaus (`DIS`)
* Litiumkarbonaatti on kemiallinen aine (`CHEM`)
* Toksisuus on myös sairaus (`DIS`)

Huomaa, että yksi entiteetti voi ulottua usean tokenin yli. Ja kuten tässä tapauksessa, meidän täytyy erottaa kaksi peräkkäistä entiteettiä toisistaan. Siksi on yleistä käyttää kahta luokkaa kullekin entiteetille - yksi määrittämään entiteetin ensimmäinen token (usein käytetään etuliitettä `B-`, joka tarkoittaa **b**eginning eli alkua), ja toinen entiteetin jatkumoa varten (`I-`, joka tarkoittaa **i**nner token eli sisäistä tokenia). Käytämme myös `O`-luokkaa edustamaan kaikkia **m**uita tokeneita. Tällainen tokenien tagitus tunnetaan nimellä [BIO-tagitus](https://en.wikipedia.org/wiki/Inside%E2%80%93outside%E2%80%93beginning_(tagging)) (tai IOB). Kun otsikko on tagitettu, se näyttää tältä:

Token | Tag
------|-----
Kolmipurjeläpän | B-DIS
vuoto | I-DIS
ja | O
litium | B-CHEM
karbonaatti | I-CHEM
toksisuus | B-DIS
vastasyntyneellä | O
lapsella | O
. | O

Koska meidän täytyy rakentaa yksi-yhteen vastaavuus tokenien ja luokkien välillä, voimme kouluttaa oikeanpuoleisen **moni-moniin** neuroverkkopohjaisen mallin tästä kuvasta:

![Kuva, joka esittää yleisiä toistuvien neuroverkkojen malleja.](../../../../../translated_images/unreasonable-effectiveness-of-rnn.541ead816778f42dce6c42d8a56c184729aa2378d059b851be4ce12b993033df.fi.jpg)

> *Kuva [tästä blogikirjoituksesta](http://karpathy.github.io/2015/05/21/rnn-effectiveness/) kirjoittajalta [Andrej Karpathy](http://karpathy.github.io/). NER-tokeniluokittelumallit vastaavat oikeanpuoleista verkkoarkkitehtuuria tässä kuvassa.*

## NER-mallien kouluttaminen

Koska NER-malli on pohjimmiltaan tokeniluokittelumalli, voimme käyttää RNN:itä, joihin olemme jo tutustuneet, tähän tehtävään. Tässä tapauksessa jokainen toistuvan verkon lohko palauttaa tokenin ID:n. Seuraava esimerkkimuistikirja näyttää, kuinka LSTM voidaan kouluttaa tokeniluokittelua varten.

## ✍️ Esimerkkimuistikirjat: NER

Jatka oppimista seuraavassa muistikirjassa:

* [NER TensorFlow'lla](NER-TF.ipynb)

## Yhteenveto

NER-malli on **tokeniluokittelumalli**, mikä tarkoittaa, että sitä voidaan käyttää tokeniluokittelun suorittamiseen. Tämä on erittäin yleinen tehtävä NLP:ssä, ja se auttaa tunnistamaan tekstistä tiettyjä entiteettejä, kuten paikkoja, nimiä, päivämääriä ja paljon muuta.

## 🚀 Haaste

Suorita alla linkitetty tehtävä, jossa koulutat nimettyjen entiteettien tunnistusmallin lääketieteellisiä termejä varten, ja kokeile sitä sitten eri datasetillä.

## [Jälkikysely](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/219)

## Kertaus ja itseopiskelu

Lue blogikirjoitus [The Unreasonable Effectiveness of Recurrent Neural Networks](http://karpathy.github.io/2015/05/21/rnn-effectiveness/) ja seuraa artikkelin lisälukemisosioita syventääksesi tietämystäsi.

## [Tehtävä](lab/README.md)

Tämän oppitunnin tehtävässä sinun tulee kouluttaa lääketieteellisten entiteettien tunnistusmalli. Voit aloittaa LSTM-mallin kouluttamisella, kuten tässä oppitunnissa on kuvattu, ja jatkaa BERT-transformerimallin käyttämiseen. Lue [ohjeet](lab/README.md) saadaksesi kaikki yksityiskohdat.

---

**Vastuuvapauslauseke**:  
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, huomioithan, että automaattiset käännökset voivat sisältää virheitä tai epätarkkuuksia. Alkuperäinen asiakirja sen alkuperäisellä kielellä tulisi pitää ensisijaisena lähteenä. Kriittisen tiedon osalta suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa väärinkäsityksistä tai virhetulkinnoista, jotka johtuvat tämän käännöksen käytöstä.