<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "0c84b280e654e05ed658023021a6a975",
  "translation_date": "2025-09-23T10:00:37+00:00",
  "source_file": "lessons/1-Intro/README.md",
  "language_code": "fi"
}
-->
# Johdanto tekoälyyn

![Yhteenveto tekoälyn johdannosta doodlena](../../../../translated_images/ai-intro.bf28d1ac4235881c096f0ffdb320ba4102940eafcca4e9d7a55a03914361f8f3.fi.png)

> Sketchnote: [Tomomi Imura](https://twitter.com/girlie_mac)

## [Esiluennon kysely](https://ff-quizzes.netlify.app/en/ai/quiz/1)

**Tekoäly** on kiehtova tieteenala, joka tutkii, kuinka voimme saada tietokoneet osoittamaan älykästä käyttäytymistä, esimerkiksi tekemään asioita, joissa ihmiset ovat hyviä.

Alun perin tietokoneet kehitti [Charles Babbage](https://en.wikipedia.org/wiki/Charles_Babbage) suorittamaan laskutoimituksia ennalta määritellyn menettelytavan eli algoritmin mukaisesti. Vaikka modernit tietokoneet ovat huomattavasti kehittyneempiä kuin 1800-luvulla ehdotettu alkuperäinen malli, ne noudattavat yhä samaa hallittujen laskentojen periaatetta. Näin ollen tietokone voidaan ohjelmoida tekemään jotain, jos tiedämme tarkalleen, mitä vaiheita tavoitteen saavuttamiseksi tarvitaan.

![Kuva henkilöstä](../../../../translated_images/dsh_age.d212a30d4e54fb5f68b94a624aad64bc086124bcbbec9561ae5bd5da661e22d8.fi.png)

> Kuva: [Vickie Soshnikova](http://twitter.com/vickievalerie)

> ✅ Henkilön iän määrittäminen valokuvasta on tehtävä, jota ei voida ohjelmoida eksplisiittisesti, koska emme tiedä, miten päädymme päähämme tulevaan lukuun tehdessämme sen.

---

On kuitenkin tehtäviä, joiden ratkaisutapaa emme tiedä tarkasti. Mietitäänpä esimerkiksi henkilön iän määrittämistä valokuvasta. Opimme tekemään sen, koska olemme nähneet monia esimerkkejä eri-ikäisistä ihmisistä, mutta emme osaa selittää tarkasti, miten sen teemme, emmekä voi ohjelmoida tietokonetta tekemään sitä. Juuri tällaiset tehtävät kiinnostavat **tekoälyä** (AI, Artificial Intelligence).

✅ Mieti joitakin tehtäviä, jotka voisit siirtää tietokoneen tehtäväksi tekoälyn avulla. Pohdi esimerkiksi rahoituksen, lääketieteen ja taiteen aloja – miten nämä alat hyötyvät tekoälystä nykyään?

## Heikko tekoäly vs. vahva tekoäly

Heikko tekoäly | Vahva tekoäly
---------------------------------------|-------------------------------------
Heikko tekoäly viittaa tekoälyjärjestelmiin, jotka on suunniteltu ja koulutettu tiettyä tehtävää tai kapeaa tehtäväjoukkoa varten.|Vahva tekoäly eli yleinen tekoäly (AGI, Artificial General Intelligence) viittaa tekoälyjärjestelmiin, joilla on ihmisen tasoinen älykkyys ja ymmärrys.
Nämä tekoälyjärjestelmät eivät ole yleisesti älykkäitä; ne ovat erinomaisia suorittamaan ennalta määriteltyjä tehtäviä, mutta niiltä puuttuu todellinen ymmärrys tai tietoisuus.|Nämä tekoälyjärjestelmät pystyvät suorittamaan mitä tahansa älyllistä tehtävää, jonka ihminen voi tehdä, sopeutumaan eri aloille ja omaamaan tietoisuuden tai itsetietoisuuden.
Esimerkkejä heikosta tekoälystä ovat virtuaaliavustajat kuten Siri tai Alexa, suoratoistopalveluiden suositusalgoritmit ja asiakaspalveluun suunnitellut chatbotit.|Vahvan tekoälyn saavuttaminen on tekoälytutkimuksen pitkän aikavälin tavoite ja vaatisi tekoälyjärjestelmien kehittämistä, jotka pystyvät järkeilemään, oppimaan, ymmärtämään ja sopeutumaan laajasti erilaisiin tehtäviin ja konteksteihin.
Heikko tekoäly on erittäin erikoistunutta eikä omaa ihmisen kaltaisia kognitiivisia kykyjä tai yleisiä ongelmanratkaisutaitoja kapean alueensa ulkopuolella.|Vahva tekoäly on tällä hetkellä teoreettinen käsite, eikä mikään tekoälyjärjestelmä ole saavuttanut tätä yleisen älykkyyden tasoa.

Lisätietoja: **[Artificial General Intelligence](https://en.wikipedia.org/wiki/Artificial_general_intelligence)** (AGI).

## Älykkyyden määritelmä ja Turingin testi

Yksi ongelma käsiteltäessä termiä **[älykkyys](https://en.wikipedia.org/wiki/Intelligence)** on, ettei termille ole selkeää määritelmää. Voidaan väittää, että älykkyys liittyy **abstraktiin ajatteluun** tai **itsetietoisuuteen**, mutta emme pysty määrittelemään sitä kunnolla.

![Kuva kissasta](../../../../translated_images/photo-cat.8c8e8fb760ffe45725c5b9f6b0d954e9bf114475c01c55adf0303982851b7eae.fi.jpg)

> [Kuva](https://unsplash.com/photos/75715CVEJhI): [Amber Kipp](https://unsplash.com/@sadmax) Unsplashista

Termin *älykkyys* epäselvyyden havainnollistamiseksi yritä vastata kysymykseen: "Onko kissa älykäs?". Eri ihmiset antavat tähän kysymykseen erilaisia vastauksia, koska ei ole yleisesti hyväksyttyä testiä, joka todistaisi väitteen todeksi tai epätodeksi. Ja jos mielestäsi sellainen on – kokeilepa laittaa kissasi älykkyystestiin...

✅ Mieti hetki, miten määrittelet älykkyyden. Onko varis, joka osaa ratkaista labyrintin saadakseen ruokaa, älykäs? Onko lapsi älykäs?

---

Kun puhumme AGI:sta, tarvitsemme jonkin tavan määrittää, olemmeko luoneet aidosti älykkään järjestelmän. [Alan Turing](https://en.wikipedia.org/wiki/Alan_Turing) ehdotti menetelmää, jota kutsutaan **[Turingin testiksi](https://en.wikipedia.org/wiki/Turing_test)**, ja joka toimii myös älykkyyden määritelmänä. Testissä verrataan annettua järjestelmää johonkin luontaisesti älykkääseen – oikeaan ihmiseen. Koska mikä tahansa automaattinen vertailu voidaan ohittaa tietokoneohjelmalla, käytämme ihmistuomaria. Jos ihminen ei pysty erottamaan oikeaa henkilöä ja tietokonejärjestelmää tekstipohjaisessa vuoropuhelussa, järjestelmää pidetään älykkäänä.

> Pietarissa kehitetty chatbot [Eugene Goostman](https://en.wikipedia.org/wiki/Eugene_Goostman) pääsi lähelle Turingin testin läpäisemistä vuonna 2014 käyttämällä ovelaa persoonallisuustemppua. Se ilmoitti heti alussa olevansa 13-vuotias ukrainalainen poika, mikä selitti tiedon puutteet ja joitakin tekstin epäjohdonmukaisuuksia. Bottia pidettiin 30 % tuomareista ihmisenä viiden minuutin keskustelun jälkeen, mikä oli Turingin mukaan koneen saavutettavissa vuoteen 2000 mennessä. On kuitenkin ymmärrettävä, ettei tämä tarkoita, että olisimme luoneet älykkään järjestelmän tai että tietokonejärjestelmä olisi huijannut ihmistuomaria – botti ei huijannut ihmisiä, vaan bottia luoneet kehittäjät tekivät sen!

✅ Oletko koskaan tullut huijatuksi chatbotin toimesta luulemaan, että puhut ihmisen kanssa? Miten se onnistui vakuuttamaan sinut?

## Eri lähestymistavat tekoälyyn

Jos haluamme tietokoneen käyttäytyvän kuin ihminen, meidän on jollain tavalla mallinnettava tietokoneeseen oma ajattelutapamme. Siksi meidän on yritettävä ymmärtää, mikä tekee ihmisestä älykkään.

> Jotta voisimme ohjelmoida älykkyyden koneeseen, meidän on ymmärrettävä, miten omat päätöksentekoprosessimme toimivat. Jos pohdit itseäsi, huomaat, että jotkin prosessit tapahtuvat alitajuisesti – esimerkiksi erotamme kissan koirasta ajattelematta sitä – kun taas toiset vaativat järkeilyä.

Tähän ongelmaan on kaksi mahdollista lähestymistapaa:

Ylhäältä alas -lähestymistapa (symbolinen järkeily) | Alhaalta ylös -lähestymistapa (neuroverkot)
---------------------------------------|-------------------------------------
Ylhäältä alas -lähestymistapa mallintaa ihmisen järkeilytavan ongelman ratkaisemiseksi. Se sisältää **tiedon** keräämisen ihmiseltä ja sen esittämisen tietokoneen ymmärtämässä muodossa. Lisäksi meidän on kehitettävä tapa mallintaa **järkeily** tietokoneessa. | Alhaalta ylös -lähestymistapa mallintaa ihmisaivojen rakennetta, joka koostuu suuresta määrästä yksinkertaisia yksiköitä, joita kutsutaan **neuroneiksi**. Jokainen neuroni toimii painotettuna keskiarvona syötteistään, ja voimme kouluttaa neuroniverkkoa ratkaisemaan hyödyllisiä ongelmia tarjoamalla sille **koulutusdataa**.

On myös muita mahdollisia lähestymistapoja älykkyyteen:

* **Emergentti**, **synergeettinen** tai **moniagenttinen lähestymistapa** perustuu siihen, että monimutkainen älykäs käyttäytyminen voi syntyä suuren määrän yksinkertaisten agenttien vuorovaikutuksesta. [Evoluutiokybernetiikan](https://en.wikipedia.org/wiki/Global_brain#Evolutionary_cybernetics) mukaan älykkyys voi *syntyä* yksinkertaisemmasta, reaktiivisesta käyttäytymisestä *metasysteemitransition* prosessissa.

* **Evolutiivinen lähestymistapa** tai **geneettinen algoritmi** on optimointiprosessi, joka perustuu evoluution periaatteisiin.

Käsittelemme näitä lähestymistapoja myöhemmin kurssilla, mutta keskitymme nyt kahteen pääsuuntaan: ylhäältä alas ja alhaalta ylös.

### Ylhäältä alas -lähestymistapa

**Ylhäältä alas -lähestymistavassa** yritämme mallintaa järkeilyämme. Koska voimme seurata ajatuksiamme järkeillessämme, voimme yrittää formalisoida tämän prosessin ja ohjelmoida sen tietokoneeseen. Tätä kutsutaan **symboliseksi järkeilyksi**.

Ihmisillä on taipumus käyttää päässään sääntöjä, jotka ohjaavat heidän päätöksentekoprosessejaan. Esimerkiksi lääkäri diagnosoi potilasta ja saattaa huomata, että henkilöllä on kuumetta, mikä viittaa tulehdukseen kehossa. Soveltamalla laajaa sääntöjoukkoa tiettyyn ongelmaan lääkäri voi päätyä lopulliseen diagnoosiin.

Tämä lähestymistapa perustuu vahvasti **tiedon esittämiseen** ja **järkeilyyn**. Tiedon kerääminen ihmisen asiantuntijalta voi olla vaikein osa, sillä lääkäri ei monissa tapauksissa tiedä tarkalleen, miksi hän päätyy tiettyyn diagnoosiin. Joskus ratkaisu vain ilmestyy hänen mieleensä ilman tietoista ajattelua. Joitakin tehtäviä, kuten henkilön iän määrittämistä valokuvasta, ei voida lainkaan pelkistää tiedon käsittelyyn.

### Alhaalta ylös -lähestymistapa

Vaihtoehtoisesti voimme yrittää mallintaa aivojemme yksinkertaisimpia elementtejä – neuronia. Voimme rakentaa tietokoneeseen niin sanotun **keinotekoisen neuroverkon** ja yrittää opettaa sitä ratkaisemaan ongelmia antamalla sille esimerkkejä. Tämä prosessi on samanlainen kuin vastasyntyneen lapsen oppiminen ympäristöstään tekemällä havaintoja.

✅ Tee hieman tutkimusta siitä, miten vauvat oppivat. Mitkä ovat vauvan aivojen peruselementit?

> | Entä koneoppiminen?         |      |
> |--------------|-----------|
> | Tekoälyn osa-alue, jossa tietokone oppii ratkaisemaan ongelman datan perusteella, kutsutaan **koneoppimiseksi**. Emme käsittele perinteistä koneoppimista tässä kurssissa – suosittelemme erillistä [Machine Learning for Beginners](http://aka.ms/ml-beginners) -opetusohjelmaa. |   ![ML for Beginners](../../../../translated_images/ml-for-beginners.9e4fed176fd5817d7d1f7d358302515186579cbf09b2a6c5bd8092b345da7f22.fi.png)    |

## Lyhyt katsaus tekoälyn historiaan

Tekoäly aloitettiin tieteenalana 1900-luvun puolivälissä. Aluksi symbolinen järkeily oli hallitseva lähestymistapa, ja se johti useisiin merkittäviin saavutuksiin, kuten asiantuntijajärjestelmiin – tietokoneohjelmiin, jotka pystyivät toimimaan asiantuntijana tietyillä rajatuilla ongelma-alueilla. Pian kuitenkin huomattiin, että tällainen lähestymistapa ei skaalaudu hyvin. Tiedon kerääminen asiantuntijalta, sen esittäminen tietokoneessa ja tietokannan ajantasaisena pitäminen osoittautui erittäin monimutkaiseksi ja liian kalliiksi monissa tapauksissa. Tämä johti niin sanottuun [tekoälyn talveen](https://en.wikipedia.org/wiki/AI_winter) 1970-luvulla.

<img alt="Tekoälyn historian lyhyt katsaus" src="images/history-of-ai.png" width="70%"/>

> Kuva: [Dmitry Soshnikov](http://soshnikov.com)

Ajan myötä laskentateho halpeni ja dataa tuli enemmän saataville, joten neuroverkkoihin perustuvat lähestymistavat alkoivat osoittaa suurta suorituskykyä kilpaillessaan ihmisten kanssa monilla alueilla, kuten tietokonenäössä tai puheen ymmärtämisessä. Viime vuosikymmenen aikana termiä tekoäly on enimmäkseen käytetty synonyyminä neuroverkoille, koska suurin osa tekoälyn menestyksistä, joista kuulemme, perustuu niihin.

Voimme havaita, kuinka lähestymistavat ovat muuttuneet esimerkiksi shakkia pelaavan tietokoneohjelman luomisessa:

* Varhaiset shakkiohjelmat perustuivat hakuun – ohjelma yritti eksplisiittisesti arvioida mahdollisia vastustajan siirtoja tietyn määrän siirtoja eteenpäin ja valitsi optimaalisen siirron parhaan mahdollisen aseman perusteella. Tämä johti niin sanotun [alfa-beeta-karsinnan](https://en.wikipedia.org/wiki/Alpha%E2%80%93beta_pruning) hakualgoritmin kehittämiseen.
* Hakustrategiat toimivat hyvin pelin loppuvaiheessa, jossa hakutila on rajattu pieneen määrään mahdollisia siirtoja. Pelin alussa hakutila on kuitenkin valtava, ja algoritmia voidaan parantaa oppimalla olemassa olevista ihmispelaajien peleistä. Myöhemmät kokeilut hyödynsivät niin sanottua [tapauspohjaista järkeilyä](https://en.wikipedia.org/wiki/Case-based_reasoning), jossa ohjelma etsi tietokannasta tapauksia, jotka ovat hyvin samanlaisia kuin pelin nykyinen asema.
* Modernit ohjelmat, jotka voittavat ihmispelaajat, perustuvat neuroverkkoihin ja [vahvistusoppimiseen](https://en.wikipedia.org/wiki/Reinforcement_learning), jossa ohjelmat oppivat pelaamaan pelaamalla pitkään itseään vastaan ja oppimalla omista virheistään – aivan kuten ihmiset oppivat pelaamaan shakkia. Tietokoneohjelma voi kuitenkin pelata paljon enemmän pelejä paljon lyhyemmässä ajassa ja siten oppia paljon nopeammin.

✅ Tee hieman tutkimusta muista peleistä, joita tekoäly on pelannut.

Samoin voimme nähdä, kuinka lähestymistapa "puhuvien ohjelmien" (jotka voisivat läpäistä Turingin testin) luomiseen on muuttunut:

* Tämän tyyppiset varhaiset ohjelmat, kuten [Eliza](https://en.wikipedia.org/wiki/ELIZA), perustuivat hyvin yksinkertaisiin kielioppisääntöihin ja syötteen lauseen uudelleenmuotoiluun kysymykseksi.
* Modernit avustajat, kuten Cortana, Siri tai Google Assistant, ovat kaikki hybridijärjestelmiä, jotka käyttävät neuroverkkoja muuntamaan puheen tekstiksi ja tunnistamaan tarkoituksemme, ja sitten hyödyntävät järkeilyä tai eksplisiittisiä algoritmeja tarvittavien toimien suorittamiseen.
* Tulevaisuudessa voimme odottaa täysin neuroverkkoihin perustuvaa mallia, joka käsittelee vuoropuhelua itsenäisesti. Viimeaikaiset GPT- ja [Turing-NLG](https://turing.microsoft.com/)-neuroverkkojen perheet ovat osoittaneet suurta menestystä tässä.

<img alt="Turingin testin kehitys" src="images/turing-test-evol.png" width="70%"/>
> Kuva: Dmitry Soshnikov, [valokuva](https://unsplash.com/photos/r8LmVbUKgns) by [Marina Abrosimova](https://unsplash.com/@abrosimova_marina_foto), Unsplash

## Viimeaikainen tekoälytutkimus

Neuroverkkojen tutkimuksen valtava kasvu alkoi noin vuonna 2010, kun suuret julkiset tietoaineistot tulivat saataville. Suuri kokoelma kuvia nimeltä [ImageNet](https://en.wikipedia.org/wiki/ImageNet), joka sisältää noin 14 miljoonaa annotoitua kuvaa, synnytti [ImageNet Large Scale Visual Recognition Challenge](https://image-net.org/challenges/LSVRC/).

![ILSVRC Tarkkuus](../../../../lessons/1-Intro/images/ilsvrc.gif)

> Kuva: [Dmitry Soshnikov](http://soshnikov.com)

Vuonna 2012 [Konvoluutioneuroverkkoja](../4-ComputerVision/07-ConvNets/README.md) käytettiin ensimmäistä kertaa kuvien luokittelussa, mikä johti merkittävään virheiden vähenemiseen (lähes 30 %:sta 16,4 %:iin). Vuonna 2015 Microsoft Researchin ResNet-arkkitehtuuri [saavutti ihmistasoisen tarkkuuden](https://doi.org/10.1109/ICCV.2015.123).

Sen jälkeen neuroverkot ovat osoittaneet erittäin menestyksekästä toimintaa monissa tehtävissä:

---

Vuosi | Ihmistaso saavutettu
-----|--------
2015 | [Kuvien luokittelu](https://doi.org/10.1109/ICCV.2015.123)
2016 | [Puheentunnistus keskusteluissa](https://arxiv.org/abs/1610.05256)
2018 | [Automaattinen konekäännös](https://arxiv.org/abs/1803.05567) (kiinasta englantiin)
2020 | [Kuvatekstien luominen](https://arxiv.org/abs/2009.13682)

Viime vuosina olemme nähneet suuria edistysaskeleita suurten kielimallien, kuten BERT ja GPT-3, kanssa. Tämä on tapahtunut pääasiassa siksi, että saatavilla on paljon yleistä tekstidataa, joka mahdollistaa mallien kouluttamisen tekstien rakenteen ja merkityksen ymmärtämiseen, niiden esikouluttamisen yleisillä tekstikokoelmilla ja sitten erikoistamisen tarkempiin tehtäviin. Opimme lisää [luonnollisen kielen käsittelystä](../5-NLP/README.md) myöhemmin tässä kurssissa.

## 🚀 Haaste

Tee kierros internetissä ja selvitä, missä mielestäsi tekoälyä käytetään tehokkaimmin. Onko se karttasovelluksessa, puheesta tekstiksi -palvelussa vai videopelissä? Tutki, miten järjestelmä on rakennettu.

## [Luennon jälkeinen kysely](https://ff-quizzes.netlify.app/en/ai/quiz/2)

## Kertaus & Itseopiskelu

Kertaa tekoälyn ja koneoppimisen historiaa lukemalla [tämä oppitunti](https://github.com/microsoft/ML-For-Beginners/tree/main/1-Introduction/2-history-of-ML). Valitse jokin elementti tämän oppitunnin tai sen alussa olevan sketchnoten sisällöstä ja tutki sitä syvällisemmin ymmärtääksesi sen kehitystä ohjaavaa kulttuurista kontekstia.

**Tehtävä**: [Game Jam](assignment.md)

---

