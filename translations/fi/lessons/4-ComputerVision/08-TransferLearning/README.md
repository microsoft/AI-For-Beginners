<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "717775c4050ccbffbe0c961ad8bf7bf7",
  "translation_date": "2025-08-28T19:26:17+00:00",
  "source_file": "lessons/4-ComputerVision/08-TransferLearning/README.md",
  "language_code": "fi"
}
-->
# Esikoulutetut verkot ja siirto-oppiminen

Konvoluutionaalisten neuroverkkojen (CNN) kouluttaminen voi viedä paljon aikaa, ja siihen tarvitaan runsaasti dataa. Suuri osa ajasta kuluu kuitenkin parhaiden matalan tason suodattimien oppimiseen, joita verkko voi käyttää kuvioiden tunnistamiseen kuvista. Herää luonnollinen kysymys – voimmeko käyttää yhdellä aineistolla koulutettua neuroverkkoa ja mukauttaa sen luokittelemaan erilaisia kuvia ilman, että koko koulutusprosessia tarvitaan?

## [Ennakkovisa](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/108)

Tätä lähestymistapaa kutsutaan **siirto-oppimiseksi**, koska siirrämme tietoa yhdestä neuroverkkon mallista toiseen. Siirto-oppimisessa aloitamme yleensä esikoulutetulla mallilla, joka on koulutettu suurella kuvadatasetillä, kuten **ImageNet**. Nämä mallit osaavat jo hyvin tunnistaa erilaisia piirteitä yleisistä kuvista, ja monissa tapauksissa pelkän luokittelijan rakentaminen näiden piirteiden päälle voi tuottaa hyviä tuloksia.

> ✅ Siirto-oppiminen on termi, joka esiintyy myös muilla tieteenaloilla, kuten kasvatustieteessä. Se viittaa prosessiin, jossa tietoa siirretään yhdeltä alalta toiselle.

## Esikoulutetut mallit piirteiden tunnistajina

Edellisessä osiossa käsitellyt konvoluutiokerrokset sisältävät useita kerroksia, joista jokainen on suunniteltu tunnistamaan tiettyjä piirteitä kuvasta. Tämä alkaa matalan tason pikseliyhdistelmistä (kuten vaakasuorat/pystysuorat viivat tai viivat) ja etenee korkeampien tasojen piirteisiin, kuten liekin silmään. Jos koulutamme CNN:n riittävän suurella ja monipuolisella kuvadatasetillä, verkon pitäisi oppia tunnistamaan nämä yleiset piirteet.

Sekä Keras että PyTorch sisältävät toimintoja, joilla voi helposti ladata esikoulutettujen neuroverkkojen painot joillekin yleisille arkkitehtuureille, joista suurin osa on koulutettu ImageNet-kuvilla. Useimmin käytetyt mallit on kuvattu [CNN-arkkitehtuurit](../07-ConvNets/CNN_Architectures.md) -sivulla edellisessä oppitunnissa. Erityisesti voit harkita seuraavia:

* **VGG-16/VGG-19**, jotka ovat suhteellisen yksinkertaisia malleja, mutta tarjoavat silti hyvän tarkkuuden. VGG:n käyttäminen ensimmäisenä kokeiluna on usein hyvä valinta siirto-oppimisen toimivuuden arvioimiseksi.
* **ResNet** on Microsoft Researchin vuonna 2015 ehdottama malliperhe. Niissä on enemmän kerroksia, joten ne vaativat enemmän resursseja.
* **MobileNet** on pienennettyjen mallien perhe, joka sopii mobiililaitteille. Käytä niitä, jos resurssit ovat rajalliset ja voit tinkiä hieman tarkkuudesta.

Tässä on esimerkki piirteistä, jotka VGG-16-verkko on tunnistanut kissan kuvasta:

![VGG-16:n tunnistamat piirteet](../../../../../translated_images/features.6291f9c7ba3a0b951af88fc9864632b9115365410765680680d30c927dd67354.fi.png)

## Kissojen ja koirien datasetti

Tässä esimerkissä käytämme [Kissat ja koirat](https://www.microsoft.com/download/details.aspx?id=54765&WT.mc_id=academic-77998-cacaste) -datasettiä, joka on hyvin lähellä todellista kuvaluokitteluskenaariota.

## ✍️ Harjoitus: Siirto-oppiminen

Katsotaan siirto-oppimista käytännössä vastaavissa muistikirjoissa:

* [Siirto-oppiminen - PyTorch](TransferLearningPyTorch.ipynb)
* [Siirto-oppiminen - TensorFlow](TransferLearningTF.ipynb)

## Adversaarisen kissan visualisointi

Esikoulutettu neuroverkko sisältää erilaisia kuvioita "aivoissaan", mukaan lukien käsityksiä **ihanteellisesta kissasta** (samoin kuin ihanteellisesta koirasta, seeprasta jne.). Olisi mielenkiintoista jotenkin **visualisoida tämä kuva**. Tämä ei kuitenkaan ole yksinkertaista, koska kuviot ovat hajallaan verkon painoissa ja järjestetty hierarkkiseen rakenteeseen.

Yksi lähestymistapa on aloittaa satunnaisesta kuvasta ja yrittää käyttää **gradienttilaskeutumisoptimointia** säätämään kuvaa siten, että verkko alkaa ajatella sen olevan kissa.

![Kuvan optimointisilmukka](../../../../../translated_images/ideal-cat-loop.999fbb8ff306e044f997032f4eef9152b453e6a990e449bbfb107de2493cc37e.fi.png)

Jos teemme näin, saamme kuitenkin jotain, joka muistuttaa satunnaista kohinaa. Tämä johtuu siitä, että *on monia tapoja saada verkko ajattelemaan, että syötekuva on kissa*, mukaan lukien sellaiset, jotka eivät visuaalisesti ole järkeviä. Vaikka nämä kuvat sisältävät paljon kissalle tyypillisiä kuvioita, mikään ei rajoita niitä olemaan visuaalisesti erottuvia.

Tuloksen parantamiseksi voimme lisätä toisen termin häviöfunktioon, jota kutsutaan **variaatiohäviöksi**. Se on mittari, joka osoittaa, kuinka samanlaisia kuvan vierekkäiset pikselit ovat. Variaatiohäviön minimointi tekee kuvasta tasaisemman ja poistaa kohinaa – paljastaen näin visuaalisesti miellyttävämpiä kuvioita. Tässä on esimerkki tällaisista "ihanteellisista" kuvista, jotka luokitellaan suurella todennäköisyydellä kissaksi ja seepraksi:

![Ihanteellinen kissa](../../../../../translated_images/ideal-cat.203dd4597643d6b0bd73038b87f9c0464322725e3a06ab145d25d4a861c70592.fi.png) | ![Ihanteellinen seepra](../../../../../translated_images/ideal-zebra.7f70e8b54ee15a7a314000bb5df38a6cfe086ea04d60df4d3ef313d046b98a2b.fi.png)
-----|-----
 *Ihanteellinen kissa* | *Ihanteellinen seepra*

Samaa lähestymistapaa voidaan käyttää niin sanottujen **adversaaristen hyökkäysten** suorittamiseen neuroverkkoa vastaan. Oletetaan, että haluamme huijata neuroverkkoa ja saada koiran näyttämään kissalta. Jos otamme koiran kuvan, jonka verkko tunnistaa koiraksi, voimme säätää sitä hieman gradienttilaskeutumisoptimoinnin avulla, kunnes verkko alkaa luokitella sen kissaksi:

![Kuva koirasta](../../../../../translated_images/original-dog.8f68a67d2fe0911f33041c0f7fce8aa4ea919f9d3917ec4b468298522aeb6356.fi.png) | ![Kuva koirasta, joka luokitellaan kissaksi](../../../../../translated_images/adversarial-dog.d9fc7773b0142b89752539bfbf884118de845b3851c5162146ea0b8809fc820f.fi.png)
-----|-----
*Alkuperäinen kuva koirasta* | *Kuva koirasta, joka luokitellaan kissaksi*

Katso koodi yllä olevien tulosten toistamiseen seuraavasta muistikirjasta:

* [Ihanteellinen ja adversaarinen kissa - TensorFlow](AdversarialCat_TF.ipynb)

## Yhteenveto

Siirto-oppimisen avulla voit nopeasti rakentaa luokittelijan mukautettuun objektien luokittelutehtävään ja saavuttaa korkean tarkkuuden. Voit huomata, että monimutkaisemmat tehtävät, joita nyt ratkaisemme, vaativat suurempaa laskentatehoa, eikä niitä voida helposti ratkaista CPU:lla. Seuraavassa osiossa yritämme käyttää kevyempää toteutusta saman mallin kouluttamiseen pienemmillä laskentaresursseilla, mikä johtaa vain hieman alhaisempaan tarkkuuteen.

## 🚀 Haaste

Mukana olevissa muistikirjoissa on huomioita siitä, kuinka siirto-oppiminen toimii parhaiten jossain määrin samankaltaisen koulutusdatan kanssa (esimerkiksi uusi eläinlaji). Tee kokeiluja täysin uusilla kuvatyypeillä nähdäksesi, kuinka hyvin tai huonosti siirto-oppimismallisi toimivat.

## [Jälkivisa](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/208)

## Kertaus ja itseopiskelu

Lue [TrainingTricks.md](TrainingTricks.md) syventääksesi tietämystäsi muista tavoista kouluttaa mallejasi.

## [Tehtävä](lab/README.md)

Tässä laboratoriossa käytämme todellista [Oxford-IIIT](https://www.robots.ox.ac.uk/~vgg/data/pets/) lemmikkieläindatasettiä, joka sisältää 35 kissan- ja koirarotua, ja rakennamme siirto-oppimiseen perustuvan luokittelijan.

---

**Vastuuvapauslauseke**:  
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, huomioithan, että automaattiset käännökset voivat sisältää virheitä tai epätarkkuuksia. Alkuperäistä asiakirjaa sen alkuperäisellä kielellä tulisi pitää ensisijaisena lähteenä. Kriittisen tiedon osalta suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa väärinkäsityksistä tai virhetulkinnoista, jotka johtuvat tämän käännöksen käytöstä.