<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "1ddf651d7681b4449f9d09ea3b17911e",
  "translation_date": "2025-08-28T19:15:04+00:00",
  "source_file": "lessons/6-Other/23-MultiagentSystems/README.md",
  "language_code": "fi"
}
-->
# Multi-Agent Systems

Yksi mahdollinen tapa saavuttaa älykkyyttä on niin sanottu **emergentti** (tai **synergeettinen**) lähestymistapa, joka perustuu siihen, että monien suhteellisen yksinkertaisten agenttien yhdistetty käyttäytyminen voi johtaa järjestelmän kokonaisvaltaisesti monimutkaisempaan (tai älykkäämpään) käyttäytymiseen. Teoreettisesti tämä perustuu [kollektiivisen älykkyyden](https://en.wikipedia.org/wiki/Collective_intelligence), [emergentismin](https://en.wikipedia.org/wiki/Global_brain) ja [evolutionaarisen kybernetiikan](https://en.wikipedia.org/wiki/Global_brain) periaatteisiin, jotka väittävät, että korkeamman tason järjestelmät saavat jonkinlaista lisäarvoa, kun ne yhdistetään asianmukaisesti alemman tason järjestelmistä (niin sanottu *metajärjestelmäsiirtymän periaate*).

## [Pre-lecture quiz](https://ff-quizzes.netlify.app/en/ai/quiz/45)

**Multi-Agent Systems** -suuntaus syntyi tekoälyssä 1990-luvulla vastauksena internetin ja hajautettujen järjestelmien kasvuun. Yksi klassisista tekoälyoppikirjoista, [Artificial Intelligence: A Modern Approach](https://en.wikipedia.org/wiki/Artificial_Intelligence:_A_Modern_Approach), tarkastelee klassista tekoälyä monen agentin järjestelmien näkökulmasta.

Monen agentin lähestymistavan keskiössä on **agentin** käsite - entiteetti, joka elää jossain **ympäristössä**, jota se voi havaita ja johon se voi vaikuttaa. Tämä on hyvin laaja määritelmä, ja agentteja voi olla monenlaisia ja eri luokitteluita:

* Kyvyn perusteella tehdä päätöksiä:
   - **Reaktiiviset** agentit toimivat yleensä yksinkertaisella pyyntö-vastaus-tyyppisellä käyttäytymisellä
   - **Pohdiskelevat** agentit käyttävät jonkinlaista loogista päättelyä ja/tai suunnittelukykyjä
* Paikan perusteella, jossa agentti suorittaa koodinsa:
   - **Staattiset** agentit toimivat omistetulla verkon solmulla
   - **Liikkuvat** agentit voivat siirtää koodinsa verkon solmujen välillä
* Käyttäytymisen perusteella:
   - **Passiiviset agentit** eivät omaa erityisiä tavoitteita. Tällaiset agentit voivat reagoida ulkoisiin ärsykkeisiin, mutta eivät aloita toimia itse.
   - **Aktiiviset agentit** omaavat tavoitteita, joita ne pyrkivät saavuttamaan
   - **Kognitiiviset agentit** sisältävät monimutkaista suunnittelua ja päättelyä

Monen agentin järjestelmiä käytetään nykyään monissa sovelluksissa:

* Peleissä monet ei-pelaajahahmot käyttävät jonkinlaista tekoälyä ja voidaan katsoa olevan älykkäitä agentteja
* Videotuotannossa monimutkaisten 3D-kohtausten renderöinti, jotka sisältävät väkijoukkoja, tehdään tyypillisesti monen agentin simulaatiolla
* Järjestelmien mallinnuksessa monen agentin lähestymistapaa käytetään simuloimaan monimutkaisen mallin käyttäytymistä. Esimerkiksi monen agentin lähestymistapaa on käytetty menestyksekkäästi ennustamaan COVID-19-taudin leviämistä maailmanlaajuisesti. Samanlaista lähestymistapaa voidaan käyttää mallintamaan kaupungin liikennettä ja tarkastelemaan, miten se reagoi liikennesääntöjen muutoksiin.
* Monimutkaisissa automaatiojärjestelmissä jokainen laite voi toimia itsenäisenä agenttina, mikä tekee koko järjestelmästä vähemmän monoliittisen ja kestävämmän.

Emme käytä paljon aikaa monen agentin järjestelmien syvälliseen tarkasteluun, mutta tarkastelemme yhtä esimerkkiä **monen agentin mallinnuksesta**.

## NetLogo

[NetLogo](https://ccl.northwestern.edu/netlogo/) on monen agentin mallinnusympäristö, joka perustuu muokattuun versioon [Logo](https://en.wikipedia.org/wiki/Logo_(programming_language))-ohjelmointikielestä. Tämä kieli kehitettiin ohjelmointikonseptien opettamiseen lapsille, ja sen avulla voit ohjata agenttia nimeltä **kilpikonna**, joka voi liikkua ja jättää jäljen taakseen. Tämä mahdollistaa monimutkaisten geometristen kuvioiden luomisen, mikä on hyvin visuaalinen tapa ymmärtää agentin käyttäytymistä.

NetLogossa voimme luoda useita kilpikonnia käyttämällä `create-turtles`-komentoa. Voimme sitten käskeä kaikkia kilpikonnia tekemään joitain toimintoja (alla olevassa esimerkissä - liikkumaan 10 pistettä eteenpäin):

```
create-turtles 10
ask turtles [
  forward 10
]
```

Tietenkin ei ole mielenkiintoista, jos kaikki kilpikonnat tekevät saman asian, joten voimme `ask`-komennolla pyytää tiettyjä kilpikonnaryhmiä, esimerkiksi niitä, jotka ovat tietyn pisteen läheisyydessä. Voimme myös luoda kilpikonnia eri *rotuihin* käyttämällä `breed [cats cat]`-komentoa. Tässä `cat` on rodun nimi, ja meidän täytyy määritellä sekä yksikkö- että monikkomuoto, koska eri komennot käyttävät eri muotoja selkeyden vuoksi.

> ✅ Emme mene NetLogo-kielen oppimiseen - voit vierailla erinomaisessa [Beginner's Interactive NetLogo Dictionary](https://ccl.northwestern.edu/netlogo/bind/)-resurssissa, jos olet kiinnostunut oppimaan lisää.

Voit [ladata](https://ccl.northwestern.edu/netlogo/download.shtml) ja asentaa NetLogon kokeillaksesi sitä.

### Mallikirjasto

NetLogon hienous on siinä, että se sisältää kirjaston toimivia malleja, joita voit kokeilla. Siirry **File → Models Library**, ja sinulla on monia mallikategorioita, joista valita.

<img alt="NetLogo Models Library" src="images/NetLogo-ModelLib.png" width="60%"/>

> Kuvakaappaus mallikirjastosta, Dmitry Soshnikov

Voit avata yhden malleista, esimerkiksi **Biology → Flocking**.

### Pääperiaatteet

Kun avaat mallin, sinut ohjataan NetLogon pääruutuun. Tässä on esimerkkimalli, joka kuvaa susien ja lampaiden populaatiota rajallisten resurssien (ruohon) avulla.

![NetLogo Main Screen](../../../../../translated_images/NetLogo-Main.32653711ec1a01b3cab22ec0b148e64193d0b979b055285bef329d5e3d6958c5.fi.png)

> Kuvakaappaus Dmitry Soshnikov

Tällä ruudulla näet:

* **Käyttöliittymä**-osion, joka sisältää:
  - Pääkentän, jossa kaikki agentit elävät
  - Erilaisia ohjaimia: painikkeita, liukusäätimiä jne.
  - Graafeja, joita voit käyttää simulaation parametrien näyttämiseen
* **Koodi**-välilehden, joka sisältää editorin, jossa voit kirjoittaa NetLogo-ohjelman

Useimmissa tapauksissa käyttöliittymässä on **Setup**-painike, joka alustaa simulaation tilan, ja **Go**-painike, joka käynnistää suorituksen. Näitä käsitellään vastaavilla käsittelijöillä koodissa, jotka näyttävät tältä:

```
to go [
...
]
```

NetLogon maailma koostuu seuraavista objekteista:

* **Agentit** (kilpikonnat), jotka voivat liikkua kentällä ja tehdä jotain. Voit käskeä agentteja käyttämällä `ask turtles [...]`-syntaksia, ja hakasulkeissa oleva koodi suoritetaan kaikilla agenteilla *kilpikonnatilassa*.
* **Ruudut** ovat kentän neliömäisiä alueita, joilla agentit elävät. Voit viitata kaikkiin agentteihin samalla ruudulla, tai voit muuttaa ruutujen värejä ja joitain muita ominaisuuksia. Voit myös `ask patches` tehdä jotain.
* **Tarkkailija** on ainutlaatuinen agentti, joka hallitsee maailmaa. Kaikki painikkeiden käsittelijät suoritetaan *tarkkailijatilassa*.

> ✅ Monen agentin ympäristön kauneus on siinä, että koodi, joka suoritetaan kilpikonnatilassa tai ruututilassa, suoritetaan samanaikaisesti kaikilla agenteilla rinnakkain. Näin ollen kirjoittamalla vähän koodia ja ohjelmoimalla yksittäisen agentin käyttäytymistä, voit luoda monimutkaisen simulaatiojärjestelmän käyttäytymisen kokonaisuutena.

### Flocking

Esimerkkinä monen agentin käyttäytymisestä tarkastellaan **[Flocking](https://en.wikipedia.org/wiki/Flocking_(behavior))**. Flocking on monimutkainen kuvio, joka muistuttaa hyvin lintujen parvien lentoa. Niiden lentoa katsellessa voi ajatella, että ne noudattavat jonkinlaista kollektiivista algoritmia tai että niillä on jonkinlainen *kollektiivinen älykkyys*. Tämä monimutkainen käyttäytyminen syntyy kuitenkin, kun jokainen yksittäinen agentti (tässä tapauksessa *lintu*) tarkkailee vain joitain muita agentteja lyhyen matkan päässä ja noudattaa kolmea yksinkertaista sääntöä:

* **Suuntautuminen** - se ohjautuu kohti naapureiden keskimääräistä suuntaa
* **Yhteensulautuminen** - se pyrkii ohjautumaan kohti naapureiden keskimääräistä sijaintia (*pitkän matkan vetovoima*)
* **Erottautuminen** - kun se pääsee liian lähelle muita lintuja, se pyrkii siirtymään pois (*lyhyen matkan hylkiminen*)

Voit suorittaa flocking-esimerkin ja tarkkailla käyttäytymistä. Voit myös säätää parametreja, kuten *erottelun astetta* tai *näköetäisyyttä*, joka määrittää, kuinka kauas kukin lintu voi nähdä. Huomaa, että jos vähennät näköetäisyyden nollaan, kaikki linnut muuttuvat sokeiksi, ja flocking loppuu. Jos vähennät erottelun nollaan, kaikki linnut kerääntyvät suoraan linjaan.

> ✅ Vaihda **Koodi**-välilehteen ja katso, missä flockingin kolme sääntöä (suuntautuminen, yhteensulautuminen ja erottautuminen) on toteutettu koodissa. Huomaa, kuinka viittaamme vain niihin agenteihin, jotka ovat näköetäisyydellä.

### Muita malleja kokeiltavaksi

On muutamia muita mielenkiintoisia malleja, joita voit kokeilla:

* **Art → Fireworks** näyttää, kuinka ilotulitus voidaan nähdä yksittäisten tulivirtojen kollektiivisena käyttäytymisenä
* **Social Science → Traffic Basic** ja **Social Science → Traffic Grid** näyttävät kaupungin liikenteen mallin 1D- ja 2D-ruudukossa liikennevaloilla tai ilman. Jokainen auto simulaatiossa noudattaa seuraavia sääntöjä:
   - Jos edessä oleva tila on tyhjä - kiihdytä (tiettyyn maksiminopeuteen asti)
   - Jos se näkee esteen edessä - jarruta (ja voit säätää, kuinka kauas kuljettaja voi nähdä)
* **Social Science → Party** näyttää, kuinka ihmiset ryhmittyvät cocktailkutsuilla. Voit löytää parametrien yhdistelmän, joka johtaa ryhmän onnellisuuden nopeimpaan kasvuun.

Kuten näistä esimerkeistä näet, monen agentin simulaatiot voivat olla varsin hyödyllinen tapa ymmärtää monimutkaisen järjestelmän käyttäytymistä, joka koostuu yksilöistä, jotka noudattavat samaa tai samanlaista logiikkaa. Sitä voidaan myös käyttää virtuaalisten agenttien, kuten [NPC:iden](https://en.wikipedia.org/wiki/NPC) ohjaamiseen tietokonepeleissä tai agenttien ohjaamiseen 3D-animoiduissa maailmoissa.

## Pohdiskelevat agentit

Edellä kuvatut agentit ovat hyvin yksinkertaisia, reagoivat ympäristön muutoksiin jonkinlaisen algoritmin avulla. Tällaiset agentit ovat **reaktiivisia agentteja**. Joskus agentit voivat kuitenkin tehdä päätöksiä ja suunnitella toimintaansa, jolloin niitä kutsutaan **pohdiskeleviksi**.

Tyypillinen esimerkki olisi henkilökohtainen agentti, joka saa ihmiseltä ohjeen varata lomamatkan. Oletetaan, että internetissä on monia agentteja, jotka voivat auttaa sitä. Sen pitäisi sitten ottaa yhteyttä muihin agentteihin nähdäkseen, mitkä lennot ovat saatavilla, mitkä ovat hotellien hinnat eri päivämäärille, ja yrittää neuvotella paras hinta. Kun lomasuunnitelma on valmis ja omistaja vahvistaa sen, se voi jatkaa varausta.

Tätä varten agenttien täytyy **kommunikoida**. Onnistuneeseen kommunikointiin tarvitaan:

* Jotain **standardikieliä tiedon vaihtoon**, kuten [Knowledge Interchange Format](https://en.wikipedia.org/wiki/Knowledge_Interchange_Format) (KIF) ja [Knowledge Query and Manipulation Language](https://en.wikipedia.org/wiki/Knowledge_Query_and_Manipulation_Language) (KQML). Nämä kielet on suunniteltu [puheaktiteorian](https://en.wikipedia.org/wiki/Speech_act) pohjalta.
* Näiden kielten tulisi sisältää myös **neuvotteluprotokollia**, jotka perustuvat erilaisiin **huutokauppatyyppeihin**.
* **Yhteinen ontologia**, jotta agentit viittaavat samoihin käsitteisiin ja ymmärtävät niiden semantiikan
* Tapa **löytää**, mitä eri agentit voivat tehdä, myös jonkinlaisen ontologian pohjalta

Pohdiskelevat agentit ovat paljon monimutkaisempia kuin reaktiiviset, koska ne eivät ainoastaan reagoi ympäristön muutoksiin, vaan niiden täytyy myös *aloittaa* toimia. Yksi ehdotetuista arkkitehtuureista pohdiskeleville agenteille on niin sanottu Belief-Desire-Intention (BDI) -agentti:

* **Uskomukset** muodostavat tietojoukon agentin ympäristöstä. Se voi olla rakenteeltaan tietokanta tai sääntöjoukko, jota agentti voi soveltaa tiettyyn tilanteeseen ympäristössä.
* **Toiveet** määrittelevät, mitä agentti haluaa tehdä, eli sen tavoitteet. Esimerkiksi yllä olevan henkilökohtaisen avustaja-agentin tavoite on varata matka, ja hotellin agentin tavoite on maksimoida voitto.
* **Aikomukset** ovat erityisiä toimia, joita agentti suunnittelee saavuttaakseen tavoitteensa. Toimet muuttavat tyypillisesti ympäristöä ja aiheuttavat kommunikointia muiden agenttien kanssa.

Saatavilla on joitakin alustoja monen agentin järjestelmien rakentamiseen, kuten [JADE](https://jade.tilab.com/). [Tämä artikkeli](https://arxiv.org/ftp/arxiv/papers/2007/2007.08961.pdf) sisältää katsauksen monen agentin alustoista sekä lyhyen historian monen agentin järjestelmistä ja niiden eri käyttötilanteista.

## Yhteenveto

Monen agentin järjestelmät voivat ottaa hyvin erilaisia muotoja ja niitä voidaan käyttää monissa eri sovelluksissa. 
Ne keskittyvät yleensä yksittäisen agentin yksinkertaisempaan käyttäytymiseen ja saavuttavat järjestelmän kokonaisvaltaisesti monimutkaisemman käyttäytymisen **synergeettisen vaikutuksen** ansiosta.

## 🚀 Haaste

Vie tämä oppitunti todelliseen maailmaan ja yritä hahmottaa monen agentin järjestelmä, joka voi ratkaista ongelman. Mitä esimerkiksi monen agentin järjestelmän pitäisi tehdä optimoidakseen koulubussireitin? Miten se voisi toimia leipomossa?

## [Post-lecture quiz](https://ff-quizzes.netlify.app/en/ai/quiz/46)

## Kertaus ja itseopiskelu

Tarkastele tämän tyyppisen järjestelmän käyttöä teollisuudessa. Valitse jokin ala, kuten valmistus tai videopeliteollisuus, ja selvitä, miten monen agentin järjestelmiä voidaan käyttää ainutlaatuisten ongelmien ratkaisemiseen.

## [NetLogo Assignment](assignment.md)

---

**Vastuuvapauslauseke**:  
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, huomioithan, että automaattiset käännökset voivat sisältää virheitä tai epätarkkuuksia. Alkuperäistä asiakirjaa sen alkuperäisellä kielellä tulisi pitää ensisijaisena lähteenä. Kriittisen tiedon osalta suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa väärinkäsityksistä tai virhetulkinnoista, jotka johtuvat tämän käännöksen käytöstä.