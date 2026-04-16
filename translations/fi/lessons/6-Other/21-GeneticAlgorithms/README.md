# Geneettiset algoritmit

## [Esiluentakysely](https://ff-quizzes.netlify.app/en/ai/quiz/41)

**Geneettiset algoritmit** (GA) perustuvat **evolutionääriseen lähestymistapaan** tekoälyssä, jossa populaation evoluutiomenetelmiä käytetään optimaalisen ratkaisun löytämiseksi tiettyyn ongelmaan. Ne esitti vuonna 1975 [John Henry Holland](https://wikipedia.org/wiki/John_Henry_Holland).

Geneettiset algoritmit perustuvat seuraaviin periaatteisiin:

* Ongelman kelvolliset ratkaisut voidaan esittää **geeneinä**
* **Risteytys** mahdollistaa kahden ratkaisun yhdistämisen uuden kelvollisen ratkaisun saamiseksi
* **Valinta** valitsee optimaalisempia ratkaisuja käyttäen jotain **soveltuvuusfunktiota**
* **Mutaatioita** lisätään optimoimisen epävakauttamiseksi ja paikallisesta minimistä pääsemiseksi

Jos haluat toteuttaa geneettisen algoritmin, tarvitset seuraavat asiat:

 * Menetelmän ongelman ratkaisujen koodaamiseen käyttäen **geenejä** g&in;&Gamma;
 * Geenijoukossa &Gamma; täytyy määritellä **soveltuvuusfunktio** fit: &Gamma;&rightarrow;**R**. Pienemmät funktion arvot vastaavat parempia ratkaisuja.
 * Määritellä **risteytysmekanismi**, joka yhdistää kaksi geeniä uuden kelvollisen ratkaisun saamiseksi crossover: &Gamma;<sup>2</sub>&rightarrow;&Gamma;.
 * Määritellä **mutaatiomekanismi** mutate: &Gamma;&rightarrow;&Gamma;.

Monissa tapauksissa risteytys ja mutaatio ovat melko yksinkertaisia algoritmeja, jotka manipuloivat geenejä numeerisina jonoina tai bittivektoreina.

Geneettisen algoritmin tarkka toteutus voi vaihdella tapauskohtaisesti, mutta yleinen rakenne on seuraava:

1. Valitse alkuperäinen populaatio G&subset;&Gamma;
2. Valitse satunnaisesti, mikä operaatio suoritetaan tässä vaiheessa: risteytys tai mutaatio
3. **Risteytys**:
  * Valitse satunnaisesti kaksi geeniä g<sub>1</sub>, g<sub>2</sub> &in; G
  * Laske risteytys g=crossover(g<sub>1</sub>,g<sub>2</sub>)
  * Jos fit(g)<fit(g<sub>1</sub>) tai fit(g)<fit(g<sub>2</sub>) - korvaa vastaava geeni populaatiossa g:llä.
4. **Mutaatio** - valitse satunnainen geeni g&in;G ja korvaa se mutate(g):llä
5. Toista vaiheesta 2, kunnes saavutetaan riittävän pieni fit-arvo tai kunnes askelten määrä saavuttaa rajan.

## Tyypilliset tehtävät

Geneettisillä algoritmeilla ratkaistaan tyypillisesti seuraavia tehtäviä:

1. Aikataulujen optimointi
1. Optimaalinen pakkaus
1. Optimaalinen leikkaus
1. Uuvuttavan haun nopeuttaminen

## ✍️ Harjoitukset: Geneettiset algoritmit

Jatka oppimista seuraavissa muistikirjoissa:

Siirry [tähän muistikirjaan](Genetic.ipynb) nähdäksesi kaksi esimerkkiä geneettisten algoritmien käytöstä:

1. Aarteiden reilu jakaminen
1. 8 kuningattaren ongelma

## Yhteenveto

Geneettisiä algoritmeja käytetään monien ongelmien ratkaisemiseen, mukaan lukien logistiikka- ja hakutehtävät. Ala on saanut inspiraationsa tutkimuksesta, joka yhdisti psykologian ja tietojenkäsittelytieteen aiheita.

## 🚀 Haaste

"Geneettiset algoritmit ovat yksinkertaisia toteuttaa, mutta niiden käyttäytymistä on vaikea ymmärtää." [lähde](https://wikipedia.org/wiki/Genetic_algorithm) Tee tutkimusta löytääksesi geneettisen algoritmin toteutuksen, kuten Sudoku-pulman ratkaisemisen, ja selitä, miten se toimii luonnoksena tai vuokaaviona.

## [Jälkiluentakysely](https://ff-quizzes.netlify.app/en/ai/quiz/42)

## Kertaus ja itseopiskelu

Katso [tämä loistava video](https://www.youtube.com/watch?v=qv6UVOQ0F44), jossa kerrotaan, miten tietokone voi oppia pelaamaan Super Mariota käyttäen geneettisillä algoritmeilla koulutettuja neuroverkkoja. Opimme lisää siitä, miten tietokone oppii pelaamaan tällaisia pelejä [seuraavassa osiossa](../22-DeepRL/README.md).

## [Tehtävä: Diofanttinen yhtälö](Diophantine.ipynb)

Tavoitteenasi on ratkaista niin sanottu **Diofanttinen yhtälö** - yhtälö, jolla on kokonaislukuratkaisuja. Esimerkiksi yhtälö a+2b+3c+4d=30. Sinun täytyy löytää kokonaislukuratkaisut, jotka täyttävät tämän yhtälön.

*Tämä tehtävä on saanut inspiraationsa [tästä artikkelista](https://habr.com/post/128704/).*

Vinkkejä:

1. Voit harkita ratkaisujen olevan välillä [0;30]
1. Geeninä voit käyttää juurten arvojen listaa

Käytä [Diophantine.ipynb](Diophantine.ipynb) aloituspisteenä.

---

