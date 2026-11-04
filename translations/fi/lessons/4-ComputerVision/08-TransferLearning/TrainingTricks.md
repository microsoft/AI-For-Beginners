# Syväoppimisen koulutusvinkit

Kun neuroverkot muuttuvat syvemmiksi, niiden kouluttamisesta tulee yhä haastavampaa. Yksi merkittävä ongelma ovat niin sanotut [häviävät gradientit](https://en.wikipedia.org/wiki/Vanishing_gradient_problem) tai [räjähtävät gradientit](https://deepai.org/machine-learning-glossary-and-terms/exploding-gradient-problem#:~:text=Exploding%20gradients%20are%20a%20problem,updates%20are%20small%20and%20controlled.). [Tämä kirjoitus](https://towardsdatascience.com/the-vanishing-exploding-gradient-problem-in-deep-neural-networks-191358470c11) tarjoaa hyvän johdannon näihin ongelmiin.

Syvien verkkojen koulutuksen tehostamiseksi on olemassa muutamia tekniikoita, joita voidaan käyttää.

## Arvojen pitäminen järkevällä välillä

Numeraalisten laskelmien vakauttamiseksi haluamme varmistaa, että kaikki arvot neuroverkossa ovat järkevällä skaalalla, tyypillisesti [-1..1] tai [0..1]. Tämä ei ole kovin tiukka vaatimus, mutta liukulukulaskennan luonne on sellainen, että eri suuruusluokan arvoja ei voi tarkasti käsitellä yhdessä. Esimerkiksi, jos lisäämme 10<sup>-10</sup> ja 10<sup>10</sup>, saamme todennäköisesti 10<sup>10</sup>, koska pienempi arvo ”muutetaan” saman suuruusluokan arvoon kuin suurempi, jolloin tarkkuus häviää.

Suurin osa aktivointifunktioista on ei-lineaarisia välillä [-1..1], joten on järkevää skaalata kaikki syöteaineisto välille [-1..1] tai [0..1].

## Alkupainojen alustaminen

Ihanteellisesti haluamme, että arvot pysyvät samassa haarukassa kerrosten läpi kuljettaessa. Siksi on tärkeää alustaa painot siten, että arvon jakauma säilyy.

Normaali jakauma **N(0,1)** ei ole hyvä idea, sillä jos meillä on *n* syötettä, lähtöarvojen keskihajonta olisi *&radic;n* ja arvot todennäköisesti hyppäisivät pois [0..1] -väliltä.

Seuraavia alustustapoja käytetään usein:

 * Yhtenäinen jakauma -- `uniform`
 * **N(0,1/n)** -- `gaussian`
 * **N(0,1/&radic;n_in)** takaa, että jos syötteillä on keskiarvo nolla ja keskihajonta 1, sama keskiarvo/keskihajonta säilyy
 * **N(0,&radic;2/(n_in+n_out))** -- niin kutsuttu **Xavier-alustus** (`glorot`), joka auttaa pitämään signaalit oikealla alueella sekä eteen- että taaksepäin kuljetuksessa

## Ryhmänormalisointi

Vaikka painojen alustus olisi kunnossa, painot voivat tulla mielivaltaisen suuriksi tai pieniksi koulutuksen aikana, jolloin signaalit eivät pysy oikealla alueella. Voimme palauttaa signaalit oikealle alueelle käyttämällä yhtä **normalisointitekniikoista**. Vaikka niitä on useita (Painon normalisointi, Kerroksen normalisointi), yleisimmin käytetty on ryhmänormalisointi.

Ryhmänormalisoinnin idea on ottaa huomioon kaikki arvot miniryhmässä ja suorittaa normalisointi (eli vähentää keskiarvo ja jakaa keskihajonnalla) näiden arvojen perusteella. Se toteutetaan verkon osana, joka suorittaa tämän normalisoinnin painojen soveltamisen jälkeen ja ennen aktivointifunktiota. Tämän seurauksena näemme todennäköisesti paremman lopputarkkuuden ja nopeamman koulutuksen.

Tässä on [alkuperäinen artikkeli](https://arxiv.org/pdf/1502.03167.pdf) ryhmänormalisoinnista, [selitys Wikipediassa](https://en.wikipedia.org/wiki/Batch_normalization) ja [hyvä johdantoblogikirjoitus](https://towardsdatascience.com/batch-normalization-in-3-levels-of-understanding-14c2da90a338) (sekä myös [venäjäksi](https://habrahabr.ru/post/309302/)).

## Pudotuskerros (Dropout)

**Dropout** on kiinnostava tekniikka, joka poistaa satunnaisesti tietyn prosenttiosuuden neuroneista koulutuksen aikana. Se toteutetaan myös kerroksena, jolla on yksi parametri (poistettavien neuronien prosenttiosuus, tyypillisesti 10%-50%), ja koulutuksen aikana se nollaa satunnaisesti syötteen vektorin elementtejä ennen seuraavaan kerrokseen siirtymistä.

Vaikka tämä saattaa kuulostaa oudolta idealta, voit nähdä dropoutin vaikutuksen MNIST-käsinkirjoitettujen numeroiden luokittelijan koulutukseen [`Dropout.ipynb`](Dropout.ipynb) -muistikirjassa. Se nopeuttaa koulutusta ja mahdollistaa korkeamman tarkkuuden vähemmissä koulutuskierroissa.

Tämän ilmiön voi selittää monella tavalla:

 * Sitä voidaan pitää satunnaisena shokkitekijänä mallille, joka vie optimoinnin pois paikallisesta minimistä
 * Sitä voidaan pitää *implisiittisenä malli-averagingina*, koska dropoutin aikana koulutamme hieman eri mallia

> *Jotkut sanovat, että kun humalainen henkilö yrittää oppia jotain, hän muistaa sen paremmin seuraavana aamuna verrattuna raittiiseen, koska aivot, joissa on viallisia neuroneja, yrittävät mukautua paremmin ymmärtääkseen asian. Emme ole itse testanneet, onko tämä totta.*

## Ylitäytön ehkäisy

Yksi hyvin tärkeä syväoppimisen osa-alue on kyky estää [ylitäyttöä](../../3-NeuralNetworks/05-Frameworks/Overfitting.md). Vaikka voi olla houkuttelevaa käyttää erittäin tehokasta neuroverkkopohjaista mallia, meidän pitäisi aina tasapainottaa mallin parametrien määrä koulutusnäytteiden määrän kanssa.

> Varmista, että ymmärrät aiemmin esitetyn [ylitäyttö](../../3-NeuralNetworks/05-Frameworks/Overfitting.md) -käsitteen!

Ylitäytön estämiseen on useita menetelmiä:

 * Varhainen pysäytys – valvotaan jatkuvasti validointidatan virhettä ja lopetetaan koulutus, kun validoinnin virhe alkaa kasvaa.
 * Selkeä painojen pienennys / regularisointi – lisätään tappiofunktioon ylimääräinen rangaistus vähentämään painojen suuria arvoja, mikä estää mallia saamasta epävakaita tuloksia
 * Mallin yhteenlasku – useiden mallien kouluttaminen ja tulosten yhdistäminen auttaa vähentämään varianssia.
 * Dropout (implisiittinen mallin yhteenlasku)

## Optimointimenetelmät / Koulutusalgoritmit

Toinen tärkeä asia koulutuksessa on valita hyvä algoritmi. Vaikka klassinen **gradienttimenetys** on kohtuullinen valinta, se voi olla joskus liian hidas tai aiheuttaa muita ongelmia.

Syväoppimisessa käytämme **stokastista gradienttimenetystä** (SGD), joka on gradienttimenetys, jota sovelletaan satunnaisesti valittuihin miniryhmiin koulutusdatasta. Painoja säädetään kaavalla:

w<sup>t+1</sup> = w<sup>t</sup> - &eta;&nabla;&lagran;

### Momentum

**momentaalisessa SGD:ssä** pidämme osan edellisten vaiheiden gradientista. Se on samanlaista kuin liikkuminen hitaudella: jos liikumme johonkin suuntaan ja saamme iskun eri suuntaan, reittimme ei muutu heti, vaan jatkaa osin alkuperäistä liikettä. Tänne otamme mukaan toisen vektorin v, joka kuvaa *nopeutta*:

* v<sup>t+1</sup> = &gamma; v<sup>t</sup> - &eta;&nabla;&lagran;
* w<sup>t+1</sup> = w<sup>t</sup>+v<sup>t+1</sup>

Parametri &gamma; kertoo, kuinka paljon hitaan liikkeen vaikutus otetaan huomioon: &gamma;=0 vastaa klassista SGD:tä; &gamma;=1 on siirtymisen laki.

### Adam, Adagrad jne.

Koska jokaisessa kerroksessa kerrotaan signaalit jollakin matriisilla W<sub>i</sub>, gradientti voi joko pienentyä lähelle nollaa tai kasvaa rajatta riippuen ||W<sub>i</sub>||:stä. Tämä on räjähtävien/häviävien gradienttien ongelman ydin.

Yksi ratkaisu tähän ongelmaan on käyttää vain gradientin suuntaa kaavassa ja jättää pois itse arvo, eli:

w<sup>t+1</sup> = w<sup>t</sup> - &eta;(&nabla;&lagran;/||&nabla;&lagran;||), missä ||&nabla;&lagran;|| = &radic;&sum;(&nabla;&lagran;)<sup>2</sup>

Tätä algoritmia kutsutaan **Adagradiksi**. Samalla idealla toimivia algoritmeja ovat: **RMSProp**, **Adam**

> **Adamia** pidetään erittäin tehokkaana algoritmina moniin käyttötarkoituksiin, joten jos et ole varma, kumpaa käyttää, valitse Adam.

### Gradientin rajaaminen

Gradientin rajaaminen on yllä kuvatun idean laajennus. Kun ||&nabla;&lagran;|| &le; &theta;, käytämme alkuperäistä gradienttia painojen optimoinnissa, ja kun ||&nabla;&lagran;|| > &theta;, jaamme gradientin sen normilla. Tässä &theta; on parametri, useimmiten voidaan valita &theta;=1 tai &theta;=10.

### Oppimisnopeuden vähennys

Koulutuksen onnistuminen riippuu usein oppimisnopeusparametrista &eta;. On loogista olettaa, että suuremmat &eta;-arvot johtavat nopeampaan koulutukseen, mikä on tyypillisesti hyvä alkuvaiheessa, ja pienempi &eta; mahdollistaa verkon hienosäädön. Siksi useimmissa tapauksissa haluamme pienentää &eta; koulutuksen aikana.

Tämä voidaan tehdä kertomalla &eta; jollakin luvulla (esim. 0.98) jokaisen epookin jälkeen tai käyttämällä monimutkaisempaa **oppimisnopeuden aikataulua**.

## Erilaiset verkkoarkkitehtuurit

Oikean verkkoarkkitehtuurin valinta ongelmaasi voi olla hankalaa. Tavallisesti valitsemme arkkitehtuurin, joka on todettu toimivaksi kyseiseen tehtävään (tai vastaavaan). Tässä on [hyvä yleiskatsaus](https://www.topbots.com/a-brief-history-of-neural-network-architectures/) tietokonenäköarkkitehtuureista.

> On tärkeää valita arkkitehtuuri, joka on riittävän tehokas suhteessa käytettävissä oleviin koulutusnäytteisiin. Liian tehokas malli voi johtaa [ylitäyttöön](../../3-NeuralNetworks/05-Frameworks/Overfitting.md)

Toinen hyvä tapa on käyttää arkkitehtuuria, joka automaattisesti mukautuu vaadittuun monimutkaisuuteen. Jonkin verran itseään sääteviä ovat **ResNet-**- ja **Inception**-arkkitehtuurit. [Lisää tietokonenäköarkkitehtuureista](../07-ConvNets/CNN_Architectures.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vastuuvapauslauseke**:
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, otathan huomioon, että automaattiset käännökset saattavat sisältää virheitä tai epätarkkuuksia. Alkuperäinen asiakirja sen alkuperäiskielellä on virallinen lähde. Tärkeissä asioissa suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa tämän käännöksen käytöstä aiheutuvista väärinymmärryksistä tai tulkinnoista.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->