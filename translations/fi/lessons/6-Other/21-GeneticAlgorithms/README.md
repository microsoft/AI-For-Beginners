<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "893aa368cb485da704b466a0f3775587",
  "translation_date": "2025-08-28T19:14:11+00:00",
  "source_file": "lessons/6-Other/21-GeneticAlgorithms/README.md",
  "language_code": "fi"
}
-->
# Geneettiset algoritmit

## [Ennakkovisa](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/121)

**Geneettiset algoritmit** (GA) perustuvat **evolutionääriseen lähestymistapaan** tekoälyssä, jossa populaation evoluutiomenetelmiä käytetään optimaalisen ratkaisun löytämiseksi tiettyyn ongelmaan. Ne esiteltiin vuonna 1975 [John Henry Hollandin](https://wikipedia.org/wiki/John_Henry_Holland) toimesta.

Geneettiset algoritmit perustuvat seuraaviin periaatteisiin:

* Ongelman kelvolliset ratkaisut voidaan esittää **geeneinä**
* **Risteytys** mahdollistaa kahden ratkaisun yhdistämisen uuden kelvollisen ratkaisun saamiseksi
* **Valinta** valitsee optimaalisempia ratkaisuja käyttäen jotain **soveltuvuusfunktiota**
* **Mutaatioita** lisätään optimoimisen epävakauttamiseksi ja paikallisesta minimistä pääsemiseksi

Jos haluat toteuttaa geneettisen algoritmin, tarvitset seuraavat asiat:

* Menetelmän ongelman ratkaisujen koodaamiseen käyttäen **geenejä** g∈Γ
* Geenijoukossa Γ tulee määritellä **soveltuvuusfunktio** fit: Γ→**R**. Pienemmät funktion arvot vastaavat parempia ratkaisuja.
* Määritellä **risteytysmekanismi**, joka yhdistää kaksi geeniä uuden kelvollisen ratkaisun saamiseksi crossover: Γ<sup>2</sup>→Γ.
* Määritellä **mutaatiomekanismi** mutate: Γ→Γ.

Monissa tapauksissa risteytys ja mutaatio ovat melko yksinkertaisia algoritmeja, jotka manipuloivat geenejä numeerisina jonoina tai bittivektoreina.

Geneettisen algoritmin tarkka toteutus voi vaihdella tapauskohtaisesti, mutta yleinen rakenne on seuraava:

1. Valitse alkuperäinen populaatio G⊂Γ
2. Valitse satunnaisesti, suoritetaanko tässä vaiheessa risteytys vai mutaatio
3. **Risteytys**:
   * Valitse satunnaisesti kaksi geeniä g<sub>1</sub>, g<sub>2</sub> ∈ G
   * Laske risteytys g=crossover(g<sub>1</sub>,g<sub>2</sub>)
   * Jos fit(g)<fit(g<sub>1</sub>) tai fit(g)<fit(g<sub>2</sub>), korvaa vastaava geeni populaatiossa geenillä g.
4. **Mutaatio** - valitse satunnainen geeni g∈G ja korvaa se mutate(g):llä
5. Toista vaiheesta 2, kunnes saavutetaan riittävän pieni fit-arvo tai kunnes askelten enimmäismäärä saavutetaan.

## Tyypilliset tehtävät

Geneettisillä algoritmeilla ratkaistavia tehtäviä ovat esimerkiksi:

1. Aikataulujen optimointi
1. Optimaalinen pakkaaminen
1. Optimaalinen leikkaus
1. Uuvuttavan haun nopeuttaminen

## ✍️ Harjoitukset: Geneettiset algoritmit

Jatka oppimista seuraavissa muistikirjoissa:

Siirry [tähän muistikirjaan](Genetic.ipynb) nähdäksesi kaksi esimerkkiä geneettisten algoritmien käytöstä:

1. Aarteiden oikeudenmukainen jako
1. 8 kuningattaren ongelma

## Yhteenveto

Geneettisiä algoritmeja käytetään monien ongelmien ratkaisemiseen, mukaan lukien logistiikka- ja hakutehtävät. Ala on saanut inspiraationsa tutkimuksesta, joka yhdisti psykologian ja tietojenkäsittelytieteen aiheita.

## 🚀 Haaste

"Geneettiset algoritmit ovat yksinkertaisia toteuttaa, mutta niiden käyttäytymistä on vaikea ymmärtää." [lähde](https://wikipedia.org/wiki/Genetic_algorithm) Tee tutkimusta löytääksesi geneettisen algoritmin toteutuksen, kuten Sudoku-pulman ratkaisemisen, ja selitä, miten se toimii luonnoksena tai vuokaaviona.

## [Jälkivisa](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/221)

## Kertaus ja itseopiskelu

Katso [tämä loistava video](https://www.youtube.com/watch?v=qv6UVOQ0F44), jossa kerrotaan, kuinka tietokone voi oppia pelaamaan Super Mariota käyttäen geneettisillä algoritmeilla koulutettuja neuroverkkoja. Opimme lisää siitä, kuinka tietokone oppii pelaamaan tällaisia pelejä [seuraavassa osiossa](../22-DeepRL/README.md).

## [Tehtävä: Diofantoksen yhtälö](Diophantine.ipynb)

Tavoitteenasi on ratkaista niin sanottu **Diofantoksen yhtälö** - yhtälö, jolla on kokonaislukuratkaisuja. Esimerkiksi yhtälö a+2b+3c+4d=30. Sinun tulee löytää kokonaislukuratkaisut, jotka täyttävät tämän yhtälön.

*Tämä tehtävä on saanut inspiraationsa [tästä artikkelista](https://habr.com/post/128704/).*

Vinkkejä:

1. Voit olettaa, että ratkaisut ovat välillä [0;30]
1. Geeninä voit käyttää juurten arvojen listaa

Käytä [Diophantine.ipynb](Diophantine.ipynb) lähtökohtana.

---

**Vastuuvapauslauseke**:  
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, huomioithan, että automaattiset käännökset voivat sisältää virheitä tai epätarkkuuksia. Alkuperäistä asiakirjaa sen alkuperäisellä kielellä tulisi pitää ensisijaisena lähteenä. Kriittisen tiedon osalta suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa väärinkäsityksistä tai virhetulkinnoista, jotka johtuvat tämän käännöksen käytöstä.