# Syväoppimisen koulutusvinkit

Kun neuroverkot syvenevät, niiden koulutusprosessi muuttuu yhä haastavammaksi. Yksi merkittävä ongelma on niin sanottu [häviävät gradientit](https://en.wikipedia.org/wiki/Vanishing_gradient_problem) tai [räjähtävät gradientit](https://deepai.org/machine-learning-glossary-and-terms/exploding-gradient-problem#:~:text=Exploding%20gradients%20are%20a%20problem,updates%20are%20small%20and%20controlled.). [Tämä artikkeli](https://towardsdatascience.com/the-vanishing-exploding-gradient-problem-in-deep-neural-networks-191358470c11) tarjoaa hyvän johdannon näihin ongelmiin.

Jotta syvien verkkojen koulutus olisi tehokkaampaa, voidaan käyttää muutamia tekniikoita.

## Arvojen pitäminen kohtuullisella välillä

Numeristen laskelmien vakauden varmistamiseksi haluamme varmistaa, että kaikki neuroverkon arvot ovat kohtuullisessa mittakaavassa, tyypillisesti [-1..1] tai [0..1]. Tämä ei ole kovin tiukka vaatimus, mutta liukulukulaskennan luonne on sellainen, että erimagnitudisia arvoja ei voida käsitellä tarkasti yhdessä. Esimerkiksi, jos lisäämme 10<sup>-10</sup> ja 10<sup>10</sup>, tuloksena on todennäköisesti 10<sup>10</sup>, koska pienempi arvo "muutetaan" samalle suuruusluokalle kuin suurempi, ja näin mantissa menetetään.

Useimmilla aktivointifunktioilla on epälineaarisuuksia alueella [-1..1], ja siksi on järkevää skaalata kaikki syöttödata [-1..1] tai [0..1] välille.

## Alkuarvojen alustaminen

Ihanteellisesti haluamme, että arvot pysyvät samassa mittakaavassa verkon kerrosten läpi kulkiessaan. Siksi on tärkeää alustaa painot siten, että arvojen jakauma säilyy.

Normaalijakauma **N(0,1)** ei ole hyvä idea, koska jos meillä on *n* syötettä, ulostulon keskihajonta olisi *n*, ja arvot todennäköisesti hyppäisivät ulos [0..1] välistä.

Seuraavia alustuksia käytetään usein:

- Uniform-jakauma -- `uniform`
- **N(0,1/n)** -- `gaussian`
- **N(0,1/√n_in)** takaa, että syötteillä, joiden keskiarvo on nolla ja keskihajonta 1, sama keskiarvo/keskihajonta säilyy
- **N(0,√2/(n_in+n_out))** -- niin sanottu **Xavier-alustus** (`glorot`), joka auttaa pitämään signaalit oikealla alueella sekä eteen- että taaksepäin kulkiessa

## Eränormalisointi

Vaikka painot alustettaisiin oikein, ne voivat koulutuksen aikana kasvaa tai pienentyä mielivaltaisesti, mikä vie signaalit pois oikealta alueelta. Voimme palauttaa signaalit oikealle alueelle käyttämällä yhtä **normalisointitekniikoista**. Vaikka niitä on useita (painonormalisointi, kerrosnormalisointi), yleisimmin käytetty on eränormalisointi.

**Eränormalisoinnin** idea on ottaa huomioon kaikki arvot minibatchin sisällä ja suorittaa normalisointi (eli vähentää keskiarvo ja jakaa keskihajonnalla) näiden arvojen perusteella. Se toteutetaan verkkokerroksena, joka suorittaa tämän normalisoinnin painojen soveltamisen jälkeen, mutta ennen aktivointifunktiota. Tämän seurauksena saavutetaan yleensä korkeampi lopullinen tarkkuus ja nopeampi koulutus.

Tässä on [alkuperäinen tutkimus](https://arxiv.org/pdf/1502.03167.pdf) eränormalisoinnista, [selitys Wikipediassa](https://en.wikipedia.org/wiki/Batch_normalization) ja [hyvä johdantoblogi](https://towardsdatascience.com/batch-normalization-in-3-levels-of-understanding-14c2da90a338) (sekä yksi [venäjäksi](https://habrahabr.ru/post/309302/)).

## Dropout

**Dropout** on mielenkiintoinen tekniikka, joka poistaa tietyn prosenttiosuuden satunnaisia neuroneja koulutuksen aikana. Se toteutetaan kerroksena, jossa on yksi parametri (poistettavien neuronien prosenttiosuus, tyypillisesti 10%-50%), ja koulutuksen aikana se nollaa syöttövektorin satunnaiset elementit ennen niiden siirtämistä seuraavaan kerrokseen.

Vaikka tämä saattaa kuulostaa oudolta idealta, voit nähdä dropoutin vaikutuksen MNIST-numeroiden luokittelijan koulutuksessa [`Dropout.ipynb`](Dropout.ipynb) -muistikirjassa. Se nopeuttaa koulutusta ja mahdollistaa korkeamman tarkkuuden saavuttamisen vähemmillä koulutusepookeilla.

Tätä vaikutusta voidaan selittää useilla tavoilla:

- Sitä voidaan pitää satunnaisena shokkitekijänä mallille, joka vie optimoinnin pois paikallisesta minimistä
- Sitä voidaan pitää *implisiittisenä mallin keskiarvona*, koska dropoutin aikana voidaan sanoa, että koulutamme hieman erilaista mallia

> *Jotkut sanovat, että kun humalainen henkilö yrittää oppia jotain, hän muistaa sen paremmin seuraavana aamuna verrattuna selväpäiseen henkilöön, koska aivot, joissa jotkut neuronit eivät toimi kunnolla, yrittävät sopeutua paremmin ymmärtämään merkityksen. Emme ole koskaan testanneet itse, onko tämä totta vai ei.*

## Yliläräämisen estäminen

Yksi syväoppimisen tärkeistä näkökohdista on kyky estää [ylilärääminen](../../3-NeuralNetworks/05-Frameworks/Overfitting.md). Vaikka voi olla houkuttelevaa käyttää erittäin tehokasta neuroverkkopohjaista mallia, meidän tulisi aina tasapainottaa mallin parametrien määrä koulutusnäytteiden määrän kanssa.

> Varmista, että ymmärrät [yliläräämisen](../../3-NeuralNetworks/05-Frameworks/Overfitting.md) käsitteen, jonka olemme aiemmin esitelleet!

Yliläräämisen estämiseen on useita tapoja:

- Aikainen pysäytys -- seurataan jatkuvasti virhettä validointijoukossa ja lopetetaan koulutus, kun validointivirhe alkaa kasvaa.
- Eksplisiittinen painojen heikkeneminen / regularisointi -- lisätään ylimääräinen rangaistus häviöfunktioon suurista painoarvoista, mikä estää mallia saamasta erittäin epävakaita tuloksia
- Mallin keskiarvoistus -- koulutetaan useita malleja ja keskiarvoistetaan tulos. Tämä auttaa minimoimaan varianssia.
- Dropout (implisiittinen mallin keskiarvoistus)

## Optimointimenetelmät / koulutusalgoritmit

Toinen tärkeä koulutuksen näkökohta on valita hyvä koulutusalgoritmi. Vaikka klassinen **gradient descent** on järkevä valinta, se voi joskus olla liian hidas tai aiheuttaa muita ongelmia.

Syväoppimisessa käytämme **Stokastista Gradienttilaskua** (SGD), joka on gradienttilasku, joka sovelletaan satunnaisesti valittuihin minibatcheihin koulutusjoukosta. Painot säädetään seuraavalla kaavalla:

w<sup>t+1</sup> = w<sup>t</sup> - η∇ℒ

### Momentum

**Momentum SGD**:ssä pidämme osan aiempien vaiheiden gradientista. Se on samanlainen kuin jos liikumme jonnekin inertiaa käyttäen, ja saamme iskun eri suuntaan, liikeratamme ei muutu välittömästi, vaan säilyttää osan alkuperäisestä liikkeestä. Tässä otamme käyttöön toisen vektorin v, joka edustaa *nopeutta*:

- v<sup>t+1</sup> = γ v<sup>t</sup> - η∇ℒ
- w<sup>t+1</sup> = w<sup>t</sup>+v<sup>t+1</sup>

Tässä parametri γ osoittaa, kuinka paljon otamme inertiaa huomioon: γ=0 vastaa klassista SGD:tä; γ=1 on puhdas liikeyhtälö.

### Adam, Adagrad, jne.

Koska jokaisessa kerroksessa kerromme signaalit matriisilla W<sub>i</sub>, riippuen ||W<sub>i</sub>||:stä, gradientti voi joko hävitä ja olla lähellä 0:aa tai kasvaa rajattomasti. Tämä on räjähtävien/häviävien gradienttien ongelman ydin.

Yksi ratkaisu tähän ongelmaan on käyttää vain gradientin suuntaa yhtälössä ja jättää absoluuttinen arvo huomiotta, eli

w<sup>t+1</sup> = w<sup>t</sup> - η(∇ℒ/||∇ℒ||), missä ||∇ℒ|| = √∑(∇ℒ)<sup>2</sup>

Tätä algoritmia kutsutaan **Adagrad**iksi. Muita algoritmeja, jotka käyttävät samaa ideaa: **RMSProp**, **Adam**

> **Adam**ia pidetään erittäin tehokkaana algoritmina moniin sovelluksiin, joten jos et ole varma, mitä käyttää - käytä Adamia.

### Gradientin leikkaaminen

Gradientin leikkaaminen on laajennus yllä olevalle idealle. Kun ||∇ℒ|| ≤ θ, otamme alkuperäisen gradientin huomioon painojen optimoinnissa, ja kun ||∇ℒ|| > θ - jaamme gradientin sen normilla. Tässä θ on parametri, useimmissa tapauksissa voimme ottaa θ=1 tai θ=10.

### Oppimisnopeuden heikkeneminen

Koulutuksen onnistuminen riippuu usein oppimisnopeusparametrista η. On loogista olettaa, että suuremmat η-arvot johtavat nopeampaan koulutukseen, mikä on yleensä toivottavaa koulutuksen alussa, ja sitten pienemmät η-arvot mahdollistavat verkon hienosäädön. Siksi useimmissa tapauksissa haluamme pienentää η:ta koulutuksen aikana.

Tämä voidaan tehdä kertomalla η jollain luvulla (esim. 0.98) jokaisen koulutusepookin jälkeen tai käyttämällä monimutkaisempaa **oppimisnopeuden aikataulua**.

## Eri verkkoarkkitehtuurit

Oikean verkkoarkkitehtuurin valitseminen ongelmallesi voi olla haastavaa. Normaalisti valitsemme arkkitehtuurin, joka on osoittautunut toimivaksi kyseisessä tehtävässä (tai vastaavassa). Tässä on [hyvä yleiskatsaus](https://www.topbots.com/a-brief-history-of-neural-network-architectures/) neuroverkkoarkkitehtuureista tietokonenäköön.

> On tärkeää valita arkkitehtuuri, joka on riittävän tehokas koulutusnäytteiden määrälle, joka meillä on. Liian tehokkaan mallin valitseminen voi johtaa [yliläräämiseen](../../3-NeuralNetworks/05-Frameworks/Overfitting.md).

Toinen hyvä tapa olisi käyttää arkkitehtuuria, joka mukautuu automaattisesti vaadittuun monimutkaisuuteen. Jossain määrin **ResNet**-arkkitehtuuri ja **Inception** ovat itseään mukautuvia. [Lisää tietokonenäköarkkitehtuureista](../07-ConvNets/CNN_Architectures.md)

---

**Vastuuvapauslauseke**:  
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, huomioithan, että automaattiset käännökset voivat sisältää virheitä tai epätarkkuuksia. Alkuperäistä asiakirjaa sen alkuperäisellä kielellä tulisi pitää ensisijaisena lähteenä. Kriittisen tiedon osalta suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa väärinkäsityksistä tai virhetulkinnoista, jotka johtuvat tämän käännöksen käytöstä.