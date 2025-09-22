<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f07c85bbf05a1f67505da98f4ecc124c",
  "translation_date": "2025-08-28T19:36:50+00:00",
  "source_file": "lessons/4-ComputerVision/10-GANs/README.md",
  "language_code": "fi"
}
-->
# Generatiiviset vastakkaisasettelumallit

Edellisessä osiossa opimme **generatiivisista malleista**: malleista, jotka voivat luoda uusia kuvia, jotka muistuttavat harjoitusaineistossa olevia kuvia. VAE oli hyvä esimerkki generatiivisesta mallista.

## [Pre-lecture quiz](https://ff-quizzes.netlify.app/en/ai/quiz/19)

Jos kuitenkin yritämme luoda jotain todella merkityksellistä, kuten maalauksen kohtuullisella resoluutiolla, VAE:lla huomaamme, että koulutus ei konvergoi hyvin. Tätä käyttötapausta varten meidän tulisi oppia toinen arkkitehtuuri, joka on erityisesti suunnattu generatiivisille malleille - **Generatiiviset vastakkaisasettelumallit**, eli GANit.

GANin pääidea on käyttää kahta neuroverkkoa, jotka koulutetaan toisiaan vastaan:

<img src="images/gan_architecture.png" width="70%"/>

> Kuva: [Dmitry Soshnikov](http://soshnikov.com)

> ✅ Pieni sanasto:
> * **Generaattori** on verkko, joka ottaa satunnaisen vektorin ja tuottaa kuvan tuloksena.
> * **Diskriminaattori** on verkko, joka ottaa kuvan ja yrittää määrittää, onko se oikea kuva (harjoitusaineistosta) vai generaattorin luoma. Se on käytännössä kuvaluokitin.

### Diskriminaattori

Diskriminaattorin arkkitehtuuri ei eroa tavallisesta kuvaluokitusverkosta. Yksinkertaisimmillaan se voi olla täysin yhdistetty luokitin, mutta todennäköisesti se on [konvoluutioneuroverkko](../07-ConvNets/README.md).

> ✅ GAN, joka perustuu konvoluutioneuroverkkoihin, tunnetaan nimellä [DCGAN](https://arxiv.org/pdf/1511.06434.pdf)

CNN-diskriminaattori koostuu seuraavista kerroksista: useita konvoluutioita ja poolauksia (joilla pienennetään spatiaalista kokoa) sekä yksi tai useampi täysin yhdistetty kerros, joilla saadaan "piirrevektori", ja lopuksi binääriluokitin.

> ✅ 'Poolaus' tässä yhteydessä on tekniikka, joka pienentää kuvan kokoa. "Poolauskerrokset pienentävät datan ulottuvuuksia yhdistämällä yhden kerroksen neuroniryhmien tulokset yhdeksi neuroniksi seuraavassa kerroksessa." - [lähde](https://wikipedia.org/wiki/Convolutional_neural_network#Pooling_layers)

### Generaattori

Generaattori on hieman monimutkaisempi. Voit ajatella sen olevan käänteinen diskriminaattori. Se alkaa latenttivektorista (piirrevektorin sijaan), sisältää täysin yhdistetyn kerroksen, joka muuntaa sen vaadittuun kokoon/muotoon, ja sitä seuraavat dekonstruktiot ja skaalaus ylöspäin. Tämä on samanlainen kuin [autokooderin](../09-Autoencoders/README.md) *dekooderi*-osa.

> ✅ Koska konvoluutiokerros toteutetaan lineaarisena suodattimena, joka kulkee kuvan läpi, dekonstruktio on pohjimmiltaan samanlainen kuin konvoluutio ja voidaan toteuttaa samalla kerroslogiikalla.

<img src="images/gan_arch_detail.png" width="70%"/>

> Kuva: [Dmitry Soshnikov](http://soshnikov.com)

### GANin kouluttaminen

GANit ovat **vastakkaisasettelullisia**, koska generaattorin ja diskriminaattorin välillä on jatkuva kilpailu. Tämän kilpailun aikana sekä generaattori että diskriminaattori parantavat suoritustaan, jolloin verkko oppii tuottamaan yhä parempia kuvia.

Koulutus tapahtuu kahdessa vaiheessa:

* **Diskriminaattorin kouluttaminen**. Tämä tehtävä on melko suoraviivainen: luomme generaattorin avulla erän kuvia, jotka merkitään 0:ksi (väärennetty kuva), ja otamme erän kuvia syötedatasta (merkittynä 1:ksi, oikea kuva). Saamme jonkin *diskriminaattorihäviön* ja suoritamme takapropagaation.
* **Generaattorin kouluttaminen**. Tämä on hieman monimutkaisempaa, koska emme tiedä generaattorin odotettua tulosta suoraan. Otamme koko GAN-verkon, joka koostuu generaattorista ja diskriminaattorista, syötämme siihen satunnaisia vektoreita ja odotamme tuloksen olevan 1 (vastaa oikeita kuvia). Jäädytämme sitten diskriminaattorin parametrit (emme halua sen kouluttuvan tässä vaiheessa) ja suoritamme takapropagaation.

Tämän prosessin aikana sekä generaattorin että diskriminaattorin häviöt eivät laske merkittävästi. Ihannetilanteessa niiden tulisi vaihdella, mikä vastaa molempien verkkojen suorituskyvyn paranemista.

## ✍️ Harjoitukset: GANit

* [GAN-muistikirja TensorFlow/Kerasilla](GANTF.ipynb)
* [GAN-muistikirja PyTorchilla](GANPyTorch.ipynb)

### GANin koulutuksen ongelmat

GANit ovat tunnetusti erityisen vaikeita kouluttaa. Tässä muutamia ongelmia:

* **Mode Collapse**. Tämä tarkoittaa, että generaattori oppii tuottamaan yhden onnistuneen kuvan, joka huijaa diskriminaattoria, mutta ei monenlaisia erilaisia kuvia.
* **Herkkä hyperparametreille**. Usein GAN ei konvergoi lainkaan, mutta oppimisnopeuden äkillinen lasku voi johtaa konvergenssiin.
* **Tasapainon ylläpitäminen** generaattorin ja diskriminaattorin välillä. Monissa tapauksissa diskriminaattorin häviö voi pudota nollaan suhteellisen nopeasti, mikä estää generaattoria kouluttautumasta edelleen. Tämän voittamiseksi voimme yrittää asettaa eri oppimisnopeudet generaattorille ja diskriminaattorille tai ohittaa diskriminaattorin koulutuksen, jos häviö on jo liian alhainen.
* **Korkean resoluution kouluttaminen**. Tämä ongelma liittyy samaan kuin autokoodereissa: liian monen konvoluutiokerroksen rekonstruointi johtaa artefakteihin. Tämä ongelma ratkaistaan tyypillisesti niin sanotulla **progressiivisella kasvulla**, jossa ensin muutama kerros koulutetaan matalaresoluutioisilla kuvilla, ja sitten kerroksia "avataan" tai lisätään. Toinen ratkaisu on lisätä ylimääräisiä yhteyksiä kerrosten välille ja kouluttaa useita resoluutioita samanaikaisesti - katso lisätietoja tästä [Multi-Scale Gradient GANs -paperista](https://arxiv.org/abs/1903.06048).

## Tyylinsiirto

GANit ovat loistava tapa luoda taiteellisia kuvia. Toinen mielenkiintoinen tekniikka on niin sanottu **tyylinsiirto**, jossa otetaan yksi **sisältökuva** ja piirretään se uudelleen eri tyylillä, soveltaen **tyylikuvan** suodattimia.

Näin se toimii:
* Aloitamme satunnaisesta kohinakuvaasta (tai sisältökuvasta, mutta ymmärtämisen kannalta on helpompi aloittaa satunnaisesta kohinasta).
* Tavoitteenamme on luoda sellainen kuva, joka olisi lähellä sekä sisältökuvaa että tyylikuvaa. Tämä määritetään kahdella häviöfunktiolla:
   - **Sisältöhäviö** lasketaan CNN:n tietyissä kerroksissa nykyisestä kuvasta ja sisältökuvasta saatujen piirteiden perusteella.
   - **Tyylihävikkö** lasketaan nykyisen kuvan ja tyylikuvan välillä älykkäällä tavalla käyttämällä Gram-matriiseja (lisätietoja [esimerkkimuistikirjassa](StyleTransfer.ipynb)).
* Kuvan tasoittamiseksi ja kohinan poistamiseksi otamme käyttöön myös **Variation loss** -häviön, joka laskee keskimääräisen etäisyyden vierekkäisten pikselien välillä.
* Pääoptimointisilmukka säätää nykyistä kuvaa gradienttilaskennan (tai jonkin muun optimointialgoritmin) avulla minimoidakseen kokonaismenetyksen, joka on kaikkien kolmen häviön painotettu summa.

## ✍️ Esimerkki: [Tyylinsiirto](StyleTransfer.ipynb)

## [Post-lecture quiz](https://ff-quizzes.netlify.app/en/ai/quiz/20)

## Yhteenveto

Tässä oppitunnissa opit GANeista ja niiden kouluttamisesta. Opit myös erityisistä haasteista, joita tämä neuroverkkojen tyyppi voi kohdata, sekä strategioista niiden voittamiseksi.

## 🚀 Haaste

Käy läpi [tyylinsiirto-muistikirja](StyleTransfer.ipynb) käyttäen omia kuviasi.

## Kertaus ja itseopiskelu

Lisätietoja GANeista löydät näistä lähteistä:

* Marco Pasini, [10 Lessons I Learned Training GANs for one Year](https://towardsdatascience.com/10-lessons-i-learned-training-generative-adversarial-networks-gans-for-a-year-c9071159628)
* [StyleGAN](https://en.wikipedia.org/wiki/StyleGAN), GAN-arkkitehtuuri, jota kannattaa harkita
* [Creating Generative Art using GANs on Azure ML](https://soshnikov.com/scienceart/creating-generative-art-using-gan-on-azureml/)

## Tehtävä

Palaa johonkin tämän oppitunnin kahdesta muistikirjasta ja kouluta GAN omilla kuvillasi. Mitä voit luoda?

---

**Vastuuvapauslauseke**:  
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Pyrimme tarkkuuteen, mutta huomioithan, että automaattiset käännökset voivat sisältää virheitä tai epätarkkuuksia. Alkuperäistä asiakirjaa sen alkuperäisellä kielellä tulee pitää ensisijaisena lähteenä. Kriittisen tiedon osalta suositellaan ammattimaista ihmiskääntämistä. Emme ole vastuussa tämän käännöksen käytöstä aiheutuvista väärinkäsityksistä tai virhetulkinnoista.