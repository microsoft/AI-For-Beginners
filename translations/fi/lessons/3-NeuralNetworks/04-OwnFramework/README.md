<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "186bf7eeab776b36f557357ea56d4751",
  "translation_date": "2025-08-28T19:46:28+00:00",
  "source_file": "lessons/3-NeuralNetworks/04-OwnFramework/README.md",
  "language_code": "fi"
}
-->
# Johdanto neuroverkkoihin. Monikerroksinen perceptron

Edellisessä osiossa opit yksinkertaisimmasta neuroverkkonmallista - yhden kerroksen perceptronista, joka on lineaarinen kahden luokan luokittelumalli.

Tässä osiossa laajennamme tätä mallia joustavammaksi kehykseksi, joka mahdollistaa:

* suorittaa **moniluokkaluokittelua** kahden luokan luokittelun lisäksi
* ratkaista **regressio-ongelmia** luokittelun lisäksi
* erottaa luokkia, jotka eivät ole lineaarisesti erotettavissa

Kehitämme myös oman modulaarisen kehyksen Pythonissa, jonka avulla voimme rakentaa erilaisia neuroverkkorakenteita.

## [Ennakkokysely](https://ff-quizzes.netlify.app/en/ai/quiz/7)

## Koneoppimisen formalisointi

Aloitetaan koneoppimisen ongelman formalisoinnilla. Oletetaan, että meillä on harjoitusaineisto **X** ja sen luokat **Y**, ja meidän täytyy rakentaa malli *f*, joka tekee mahdollisimman tarkkoja ennusteita. Ennusteiden laatua mitataan **häviöfunktiolla** ℒ. Seuraavia häviöfunktioita käytetään usein:

* Regressio-ongelmassa, kun meidän täytyy ennustaa luku, voimme käyttää **absoluuttista virhettä** ∑<sub>i</sub>|f(x<sup>(i)</sup>)-y<sup>(i)</sup>| tai **neliöllistä virhettä** ∑<sub>i</sub>(f(x<sup>(i)</sup>)-y<sup>(i)</sup>)<sup>2</sup>
* Luokittelussa käytämme **0-1 häviötä** (joka on käytännössä sama kuin mallin **tarkkuus**) tai **logistista häviötä**.

Yhden kerroksen perceptronissa funktio *f* määriteltiin lineaarisena funktiona *f(x)=wx+b* (tässä *w* on painomatriisi, *x* on syöteominaisuuksien vektori ja *b* on bias-vektori). Eri neuroverkkorakenteissa tämä funktio voi olla monimutkaisempi.

> Luokittelussa on usein toivottavaa saada todennäköisyydet vastaaville luokille verkon ulostulona. Muuntaaksemme satunnaiset luvut todennäköisyyksiksi (esim. normalisoidaksemme ulostulon), käytämme usein **softmax**-funktiota σ, ja funktiosta *f* tulee *f(x)=σ(wx+b)*.

Yllä olevassa *f*:n määritelmässä *w* ja *b* kutsutaan **parametreiksi** θ=⟨*w,b*⟩. Kun aineisto ⟨**X**,**Y**⟩ on annettu, voimme laskea kokonaisvirheen koko aineistolle parametrien θ funktiona.

> ✅ **Neuroverkon koulutuksen tavoite on minimoida virhe muuttamalla parametreja θ**

## Gradienttimenetelmä optimointiin

On olemassa tunnettu menetelmä funktioiden optimointiin, nimeltään **gradienttimenetelmä**. Idea on, että voimme laskea derivaatan (moniulotteisessa tapauksessa **gradientin**) häviöfunktion suhteen parametreihin ja muuttaa parametreja siten, että virhe pienenee. Tämä voidaan formalisoida seuraavasti:

* Alusta parametrit satunnaisilla arvoilla w<sup>(0)</sup>, b<sup>(0)</sup>
* Toista seuraava vaihe monta kertaa:
    - w<sup>(i+1)</sup> = w<sup>(i)</sup>-η∂ℒ/∂w
    - b<sup>(i+1)</sup> = b<sup>(i)</sup>-η∂ℒ/∂b

Koulutuksen aikana optimointivaiheet lasketaan oletettavasti koko aineistoa käyttäen (muista, että häviö lasketaan summana kaikkien harjoitusnäytteiden läpi). Todellisuudessa otamme kuitenkin pieniä osia aineistosta, joita kutsutaan **minibatcheiksi**, ja laskemme gradientit osajoukon perusteella. Koska osajoukko valitaan satunnaisesti joka kerta, tätä menetelmää kutsutaan **stokastiseksi gradienttimenetelmäksi** (SGD).

## Monikerroksiset perceptronit ja takaisinkuljetus

Yhden kerroksen verkko, kuten yllä nähtiin, pystyy luokittelemaan lineaarisesti erotettavia luokkia. Rikkaamman mallin rakentamiseksi voimme yhdistää useita verkon kerroksia. Matemaattisesti tämä tarkoittaisi, että funktio *f* olisi monimutkaisempi ja laskettaisiin useassa vaiheessa:
* z<sub>1</sub>=w<sub>1</sub>x+b<sub>1</sub>
* z<sub>2</sub>=w<sub>2</sub>α(z<sub>1</sub>)+b<sub>2</sub>
* f = σ(z<sub>2</sub>)

Tässä α on **epälineaarinen aktivointifunktio**, σ on softmax-funktio, ja parametrit θ=<*w<sub>1</sub>,b<sub>1</sub>,w<sub>2</sub>,b<sub>2</sub>*>.

Gradienttimenetelmä pysyy samana, mutta gradienttien laskeminen on vaikeampaa. Ketjulaskusäännön avulla voimme laskea derivaatat seuraavasti:

* ∂ℒ/∂w<sub>2</sub> = (∂ℒ/∂σ)(∂σ/∂z<sub>2</sub>)(∂z<sub>2</sub>/∂w<sub>2</sub>)
* ∂ℒ/∂w<sub>1</sub> = (∂ℒ/∂σ)(∂σ/∂z<sub>2</sub>)(∂z<sub>2</sub>/∂α)(∂α/∂z<sub>1</sub>)(∂z<sub>1</sub>/∂w<sub>1</sub>)

> ✅ Ketjulaskusääntöä käytetään laskemaan häviöfunktion derivaatat parametrien suhteen.

Huomaa, että kaikkien näiden lausekkeiden vasemmanpuoleinen osa on sama, ja näin voimme tehokkaasti laskea derivaatat aloittaen häviöfunktiosta ja kulkemalla "taaksepäin" laskentakaavion läpi. Näin monikerroksisen perceptronin koulutusmenetelmää kutsutaan **takaisinkuljetukseksi** tai 'backpropiksi'.

<img alt="laskentakaavio" src="images/ComputeGraphGrad.png"/>

> TODO: kuvan lähde

> ✅ Käymme takaisinkuljetusta paljon yksityiskohtaisemmin läpi esimerkkivihkossamme.  

## Yhteenveto

Tässä oppitunnissa rakensimme oman neuroverkkokirjaston ja käytimme sitä yksinkertaiseen kaksiulotteiseen luokittelutehtävään.

## 🚀 Haaste

Liitetyssä vihkossa toteutat oman kehyksen monikerroksisten perceptronien rakentamiseen ja kouluttamiseen. Näet yksityiskohtaisesti, miten modernit neuroverkot toimivat.

Siirry [OwnFramework](OwnFramework.ipynb) -vihkoon ja käy se läpi.

## [Jälkikysely](https://ff-quizzes.netlify.app/en/ai/quiz/8)

## Kertaus ja itseopiskelu

Takaisinkuljetus on yleinen algoritmi, jota käytetään tekoälyssä ja koneoppimisessa. Se kannattaa [tutkia tarkemmin](https://wikipedia.org/wiki/Backpropagation).

## [Tehtävä](lab/README.md)

Tässä laboratoriossa sinua pyydetään käyttämään tässä oppitunnissa rakentamaasi kehystä MNIST-käsinkirjoitettujen numeroiden luokitteluun.

* [Ohjeet](lab/README.md)
* [Vihko](lab/MyFW_MNIST.ipynb)

---

**Vastuuvapauslauseke**:  
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, huomioithan, että automaattiset käännökset voivat sisältää virheitä tai epätarkkuuksia. Alkuperäinen asiakirja sen alkuperäisellä kielellä tulisi pitää ensisijaisena lähteenä. Kriittisen tiedon osalta suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa väärinkäsityksistä tai virhetulkinnoista, jotka johtuvat tämän käännöksen käytöstä.