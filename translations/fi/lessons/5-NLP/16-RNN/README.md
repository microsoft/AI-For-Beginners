<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "58bf4adb210aab53e8f78c8082040e7c",
  "translation_date": "2025-08-28T20:05:37+00:00",
  "source_file": "lessons/5-NLP/16-RNN/README.md",
  "language_code": "fi"
}
-->
# Toistuvat neuroverkot

## [Ennakkokysely](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/116)

Aiemmissa osioissa olemme käyttäneet tekstin semanttisia esityksiä ja yksinkertaista lineaarista luokitinta upotusten päällä. Tämä arkkitehtuuri pyrkii vangitsemaan sanojen yhdistetyn merkityksen lauseessa, mutta se ei ota huomioon sanojen **järjestystä**, koska upotusten päälle tehty yhdistämisoperaatio poistaa tämän tiedon alkuperäisestä tekstistä. Koska nämä mallit eivät pysty mallintamaan sanojen järjestystä, ne eivät voi ratkaista monimutkaisempia tai epäselvempiä tehtäviä, kuten tekstin generointia tai kysymysten vastaamista.

Jotta voimme ymmärtää tekstin sekvenssin merkityksen, meidän täytyy käyttää toista neuroverkkoarkkitehtuuria, jota kutsutaan **toistuvaksi neuroverkoksi** eli RNN:ksi. RNN:ssä syötämme lauseen verkon läpi yksi symboli kerrallaan, ja verkko tuottaa jonkin **tilan**, jonka syötämme verkkoon uudelleen seuraavan symbolin kanssa.

![RNN](../../../../../translated_images/rnn.27f5c29c53d727b546ad3961637a267f0fe9ec5ab01f2a26a853c92fcefbb574.fi.png)

> Kuva: kirjoittaja

Kun syötteenä on tokenien sekvenssi X<sub>0</sub>,...,X<sub>n</sub>, RNN luo neuroverkkolohkojen sekvenssin ja kouluttaa tämän sekvenssin päästä päähän takaisinlevityksen avulla. Jokainen verkkolohko ottaa syötteenä parin (X<sub>i</sub>,S<sub>i</sub>) ja tuottaa tuloksena S<sub>i+1</sub>. Lopullinen tila S<sub>n</sub> (tai tulos Y<sub>n</sub>) syötetään lineaariseen luokittimeen tuloksen tuottamiseksi. Kaikilla verkkolohkoilla on samat painot, ja ne koulutetaan päästä päähän yhden takaisinlevityskierroksen avulla.

Koska tilavektorit S<sub>0</sub>,...,S<sub>n</sub> kulkevat verkon läpi, se pystyy oppimaan sanojen välisiä sekventiaalisia riippuvuuksia. Esimerkiksi, kun sana *not* esiintyy jossain kohtaa sekvenssiä, verkko voi oppia kumoamaan tiettyjä elementtejä tilavektorissa, mikä johtaa negaatioon.

> ✅ Koska kaikkien RNN-lohkojen painot yllä olevassa kuvassa ovat jaettuja, sama kuva voidaan esittää yhtenä lohkona (oikealla) toistuvalla palautesilmukalla, joka syöttää verkon ulostulotilan takaisin syötteeksi.

## RNN-solun anatomia

Katsotaan, miten yksinkertainen RNN-solu on järjestetty. Se ottaa syötteenä edellisen tilan S<sub>i-1</sub> ja nykyisen symbolin X<sub>i</sub>, ja sen täytyy tuottaa ulostulotila S<sub>i</sub> (ja joskus olemme kiinnostuneita myös jostain muusta ulostulosta Y<sub>i</sub>, kuten generatiivisissa verkoissa).

Yksinkertaisessa RNN-solussa on kaksi painomatriisia: yksi muuntaa syötesymbolin (kutsutaan sitä W:ksi) ja toinen muuntaa syötetilan (H). Tässä tapauksessa verkon ulostulo lasketaan kaavalla σ(W×X<sub>i</sub>+H×S<sub>i-1</sub>+b), missä σ on aktivointifunktio ja b on lisäbias.

<img alt="RNN-solun anatomia" src="images/rnn-anatomy.png" width="50%"/>

> Kuva: kirjoittaja

Monissa tapauksissa syötetokenit kulkevat upotuskerroksen läpi ennen RNN:ään syöttämistä, jotta dimensioita voidaan pienentää. Tässä tapauksessa, jos syötevektorien dimensio on *emb_size* ja tilavektorin dimensio on *hid_size*, W:n koko on *emb_size*×*hid_size* ja H:n koko on *hid_size*×*hid_size*.

## Pitkät lyhytaikaiset muistiverkot (LSTM)

Yksi klassisten RNN:ien suurimmista ongelmista on niin sanottu **häviävien gradienttien** ongelma. Koska RNN:t koulutetaan päästä päähän yhdessä takaisinlevityskierroksessa, niillä on vaikeuksia virheen propagoinnissa verkon ensimmäisiin kerroksiin, eikä verkko näin ollen pysty oppimaan kaukaisten tokenien välisiä suhteita. Yksi tapa välttää tämä ongelma on ottaa käyttöön **eksplisiittinen tilanhallinta** käyttämällä niin sanottuja **portteja**. Tällaisia arkkitehtuureja on kaksi tunnettua: **Pitkät lyhytaikaiset muistiverkot** (LSTM) ja **Gated Relay Unit** (GRU).

![Kuva esimerkki pitkän lyhytaikaisen muistisolun rakenteesta](../../../../../lessons/5-NLP/16-RNN/images/long-short-term-memory-cell.svg)

> Kuvalähde TBD

LSTM-verkko on järjestetty samalla tavalla kuin RNN, mutta kerrosten välillä kulkee kaksi tilaa: varsinainen tila C ja piilotettu vektori H. Jokaisessa yksikössä piilotettu vektori H<sub>i</sub> yhdistetään syötteeseen X<sub>i</sub>, ja ne ohjaavat, mitä tilassa C tapahtuu **porttien** avulla. Jokainen portti on neuroverkko, jossa on sigmoid-aktivointi (ulostulo välillä [0,1]), ja sitä voidaan ajatella bittimaskina, kun se kerrotaan tilavektorilla. Kuvassa vasemmalta oikealle on seuraavat portit:

* **Unohtamisportti** ottaa piilotetun vektorin ja määrittää, mitkä komponentit vektorista C täytyy unohtaa ja mitkä välittää eteenpäin.
* **Syöttöportti** ottaa tietoa syötteestä ja piilotetuista vektoreista ja lisää sen tilaan.
* **Ulostuloportti** muuntaa tilan lineaarisen kerroksen kautta, jossa on *tanh*-aktivointi, ja valitsee sen komponentteja piilotetun vektorin H<sub>i</sub> avulla tuottaakseen uuden tilan C<sub>i+1</sub>.

Tilan C komponentteja voidaan ajatella lippuina, jotka voidaan kytkeä päälle ja pois. Esimerkiksi, kun kohtaamme nimen *Alice* sekvenssissä, voimme olettaa, että se viittaa naispuoliseen hahmoon, ja nostaa tilassa lipun, joka kertoo, että lauseessa on naispuolinen substantiivi. Kun myöhemmin kohtaamme fraasin *and Tom*, nostamme lipun, joka kertoo, että lauseessa on monikollinen substantiivi. Näin manipuloimalla tilaa voimme mahdollisesti seurata lauseen osien kieliopillisia ominaisuuksia.

> ✅ Erinomainen resurssi LSTM:n sisäisen toiminnan ymmärtämiseen on tämä loistava artikkeli [Understanding LSTM Networks](https://colah.github.io/posts/2015-08-Understanding-LSTMs/) kirjoittanut Christopher Olah.

## Kaksisuuntaiset ja monikerroksiset RNN:t

Olemme käsitelleet toistuvia verkkoja, jotka toimivat yhteen suuntaan, sekvenssin alusta loppuun. Tämä vaikuttaa luonnolliselta, koska se muistuttaa tapaa, jolla luemme ja kuuntelemme puhetta. Kuitenkin, koska monissa käytännön tapauksissa meillä on satunnainen pääsy syötteen sekvenssiin, voi olla järkevää suorittaa toistuva laskenta molempiin suuntiin. Tällaisia verkkoja kutsutaan **kaksisuuntaisiksi** RNN:iksi. Kaksisuuntaisessa verkossa tarvitsemme kaksi piilotettua tilavektoria, yhden kumpaankin suuntaan.

Toistuva verkko, joko yksisuuntainen tai kaksisuuntainen, vangitsee tiettyjä kuvioita sekvenssissä ja voi tallentaa ne tilavektoriin tai välittää ulostuloon. Kuten konvoluutioverkoissa, voimme rakentaa toisen toistuvan kerroksen ensimmäisen päälle vangitaksemme korkeamman tason kuvioita ja rakentaa matalan tason kuvioista, jotka ensimmäinen kerros on poiminut. Tämä johtaa käsitteeseen **monikerroksinen RNN**, joka koostuu kahdesta tai useammasta toistuvasta verkosta, joissa edellisen kerroksen ulostulo syötetään seuraavaan kerrokseen.

![Kuva monikerroksisesta pitkän lyhytaikaisen muistiverkosta](../../../../../translated_images/multi-layer-lstm.dd975e29bb2a59fe58b429db833932d734c81f211cad2783797a9608984acb8c.fi.jpg)

*Kuva [tästä upeasta postauksesta](https://towardsdatascience.com/from-a-lstm-cell-to-a-multilayer-lstm-network-with-pytorch-2899eb5696f3) kirjoittanut Fernando López*

## ✍️ Harjoitukset: Upotukset

Jatka oppimista seuraavissa muistikirjoissa:

* [RNN:t PyTorchilla](RNNPyTorch.ipynb)
* [RNN:t TensorFlow'lla](RNNTF.ipynb)

## Yhteenveto

Tässä osiossa olemme nähneet, että RNN:itä voidaan käyttää sekvenssiluokitteluun, mutta itse asiassa ne voivat käsitellä monia muita tehtäviä, kuten tekstin generointia, konekäännöstä ja paljon muuta. Tarkastelemme näitä tehtäviä seuraavassa osiossa.

## 🚀 Haaste

Lue kirjallisuutta LSTM:istä ja pohdi niiden sovelluksia:

- [Grid Long Short-Term Memory](https://arxiv.org/pdf/1507.01526v1.pdf)
- [Show, Attend and Tell: Neural Image Caption
Generation with Visual Attention](https://arxiv.org/pdf/1502.03044v2.pdf)

## [Jälkikysely](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/216)

## Kertaus ja itseopiskelu

- [Understanding LSTM Networks](https://colah.github.io/posts/2015-08-Understanding-LSTMs/) kirjoittanut Christopher Olah.

## [Tehtävä: Muistikirjat](assignment.md)

---

**Vastuuvapauslauseke**:  
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, huomioithan, että automaattiset käännökset voivat sisältää virheitä tai epätarkkuuksia. Alkuperäistä asiakirjaa sen alkuperäisellä kielellä tulisi pitää ensisijaisena lähteenä. Kriittisen tiedon osalta suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa väärinkäsityksistä tai virhetulkinnoista, jotka johtuvat tämän käännöksen käytöstä.