<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "0b306c04f5337b6e7430e5c0b16bb5c0",
  "translation_date": "2025-08-28T19:33:56+00:00",
  "source_file": "lessons/4-ComputerVision/09-Autoencoders/README.md",
  "language_code": "fi"
}
-->
# Autokooderit

Kun koulutamme CNN-verkkoja, yksi ongelmista on, että tarvitsemme paljon merkittyä dataa. Kuvien luokittelussa tämä tarkoittaa, että kuvat on jaoteltava eri luokkiin, mikä vaatii manuaalista työtä.

## [Ennakkokysely](https://ff-quizzes.netlify.app/en/ai/quiz/17)

Toisaalta voimme haluta käyttää raakadataa (ilman merkintöjä) CNN-ominaisuuksien oppimiseen, mitä kutsutaan **itseohjautuvaksi oppimiseksi**. Merkittyjen tietojen sijaan käytämme harjoituskuvia sekä verkon syötteenä että tulosteena. **Autokooderin** pääidea on, että meillä on **enkooderiverkko**, joka muuntaa syötekuvan johonkin **latenttitilaan** (yleensä pienemmän kokoiseen vektoriin), ja **dekooderiverkko**, jonka tehtävänä on rekonstruoida alkuperäinen kuva.

> ✅ [Autokooderi](https://wikipedia.org/wiki/Autoencoder) on "keinotekoisen neuroverkon tyyppi, jota käytetään oppimaan tehokkaita koodauksia merkitsemättömästä datasta."

Koska koulutamme autokooderia tallentamaan mahdollisimman paljon alkuperäisen kuvan tietoa tarkkaa rekonstruointia varten, verkko pyrkii löytämään parhaan **upotuksen** syötekuville niiden merkityksen tallentamiseksi.

![Autokooderin kaavio](../../../../../translated_images/autoencoder_schema.5e6fc9ad98a5eb6197f3513cf3baf4dfbe1389a6ae74daebda64de9f1c99f142.fi.jpg)

> Kuva [Keras-blogista](https://blog.keras.io/building-autoencoders-in-keras.html)

## Autokooderien käyttöskenaariot

Vaikka alkuperäisten kuvien rekonstruointi ei itsessään vaikuta kovin hyödylliseltä, on olemassa muutamia skenaarioita, joissa autokooderit ovat erityisen hyödyllisiä:

* **Kuvien ulottuvuuden pienentäminen visualisointia varten** tai **kuva-upotusten oppiminen**. Yleensä autokooderit antavat parempia tuloksia kuin PCA, koska ne ottavat huomioon kuvien spatiaalisen luonteen ja hierarkkiset piirteet.
* **Kohinanpoisto**, eli kohinan poistaminen kuvasta. Koska kohina sisältää paljon tarpeetonta tietoa, autokooderi ei pysty tallentamaan kaikkea suhteellisen pieneen latenttitilaan, ja näin se tallentaa vain kuvan tärkeät osat. Kohinanpoistajien koulutuksessa aloitamme alkuperäisistä kuvista ja käytämme kuvia, joihin on lisätty keinotekoista kohinaa, autokooderin syötteenä.
* **Superresoluutio**, eli kuvan resoluution parantaminen. Aloitamme korkearesoluutioisista kuvista ja käytämme matalamman resoluution kuvaa autokooderin syötteenä.
* **Generatiiviset mallit**. Kun autokooderi on koulutettu, dekooderiosaa voidaan käyttää uusien objektien luomiseen satunnaisista latenttivektoreista.

## Variatiiviset autokooderit (VAE)

Perinteiset autokooderit pienentävät syötteen ulottuvuutta jollain tavalla ja tunnistavat syötekuvien tärkeät piirteet. Latenttivektorit eivät kuitenkaan usein ole kovin merkityksellisiä. Esimerkiksi MNIST-datasetin tapauksessa ei ole helppoa selvittää, mitkä numerot vastaavat eri latenttivektoreita, koska läheiset latenttivektorit eivät välttämättä vastaa samoja numeroita.

Generatiivisten mallien kouluttamisessa on kuitenkin hyödyllistä ymmärtää latenttitilaa. Tämä ajatus johtaa meidät **variatiiviseen autokooderiin** (VAE).

VAE on autokooderi, joka oppii ennustamaan latenttiparametrien *tilastollisen jakauman*, niin sanotun **latenttijakauman**. Esimerkiksi voimme haluta, että latenttivektorit jakautuvat normaalisti keskiarvolla z<sub>mean</sub> ja keskihajonnalla z<sub>sigma</sub> (sekä keskiarvo että keskihajonta ovat jonkin ulottuvuuden d vektoreita). VAE:n enkooderi oppii ennustamaan nämä parametrit, ja dekooderi käyttää satunnaista vektoria tästä jakaumasta rekonstruoidakseen objektin.

Yhteenveto:

* Syötevektorista ennustamme `z_mean` ja `z_log_sigma` (keskihajonnan sijaan ennustamme sen logaritmin)
* Otamme vektorin `sample` jakaumasta N(z<sub>mean</sub>,exp(z<sub>log_sigma</sub>))
* Dekooderi yrittää dekoodata alkuperäisen kuvan käyttäen `sample`-vektoria syötteenä

<img src="images/vae.png" width="50%">

> Kuva [tästä blogikirjoituksesta](https://ijdykeman.github.io/ml/2016/12/21/cvae.html) kirjoittanut Isaak Dykeman

Variatiiviset autokooderit käyttävät monimutkaista häviöfunktiota, joka koostuu kahdesta osasta:

* **Rekonstruktiohäviö** on häviöfunktio, joka osoittaa, kuinka lähellä rekonstruoitu kuva on kohdetta (esimerkiksi keskineliövirhe, MSE). Se on sama häviöfunktio kuin tavallisissa autokoodereissa.
* **KL-häviö**, joka varmistaa, että latenttimuuttujien jakaumat pysyvät lähellä normaalia jakaumaa. Se perustuu [Kullback-Leiblerin divergenssiin](https://www.countbayesie.com/blog/2017/5/9/kullback-leibler-divergence-explained) - metriikkaan, jolla arvioidaan kahden tilastollisen jakauman samankaltaisuutta.

Yksi VAE:n tärkeistä eduista on, että niiden avulla voimme luoda uusia kuvia suhteellisen helposti, koska tiedämme, mistä jakaumasta voimme ottaa näytteitä latenttivektoreille. Esimerkiksi, jos koulutamme VAE:n 2D-latenttivektorilla MNIST-datasetilla, voimme muuttaa latenttivektorin komponentteja saadaksemme erilaisia numeroita:

<img alt="vaemnist" src="images/vaemnist.png" width="50%"/>

> Kuva [Dmitry Soshnikovilta](http://soshnikov.com)

Huomaa, kuinka kuvat sulautuvat toisiinsa, kun alamme ottaa latenttivektoreita eri osista latenttiparametritilaa. Voimme myös visualisoida tämän tilan 2D-muodossa:

<img alt="vaemnist cluster" src="images/vaemnist-diag.png" width="50%"/> 

> Kuva [Dmitry Soshnikovilta](http://soshnikov.com)

## ✍️ Harjoitukset: Autokooderit

Opi lisää autokoodereista näissä vastaavissa muistikirjoissa:

* [Autokooderit TensorFlow'ssa](AutoencodersTF.ipynb)
* [Autokooderit PyTorchissa](AutoEncodersPyTorch.ipynb)

## Autokooderien ominaisuudet

* **Dataan sidottu** - ne toimivat hyvin vain sellaisten kuvien kanssa, joilla ne on koulutettu. Esimerkiksi, jos koulutamme superresoluutioverkon kukilla, se ei toimi hyvin muotokuvilla. Tämä johtuu siitä, että verkko voi tuottaa korkeamman resoluution kuvan ottamalla yksityiskohtia koulutusdatan oppimista piirteistä.
* **Häviöllinen** - rekonstruoitu kuva ei ole sama kuin alkuperäinen kuva. Häviön luonne määräytyy koulutuksessa käytetyn *häviöfunktion* mukaan.
* Toimii **merkitsemättömällä datalla**

## [Jälkikysely](https://ff-quizzes.netlify.app/en/ai/quiz/18)

## Yhteenveto

Tässä oppitunnissa opit erilaisista autokooderityypeistä, joita tekoälytutkija voi käyttää. Opit, kuinka niitä rakennetaan ja kuinka niitä käytetään kuvien rekonstruointiin. Opit myös VAE:sta ja sen käytöstä uusien kuvien luomiseen.

## 🚀 Haaste

Tässä oppitunnissa opit käyttämään autokoodereita kuvien kanssa. Mutta niitä voidaan käyttää myös musiikkiin! Tutustu Magenta-projektin [MusicVAE](https://magenta.tensorflow.org/music-vae) -projektiin, joka käyttää autokoodereita musiikin rekonstruinnin oppimiseen. Tee [kokeiluja](https://colab.research.google.com/github/magenta/magenta-demos/blob/master/colab-notebooks/Multitrack_MusicVAE.ipynb) tämän kirjaston kanssa nähdäksesi, mitä voit luoda.

## [Jälkikysely](https://ff-quizzes.netlify.app/en/ai/quiz/16)

## Kertaus ja itseopiskelu

Lisätietoja autokoodereista löydät näistä resursseista:

* [Autokooderien rakentaminen Kerasilla](https://blog.keras.io/building-autoencoders-in-keras.html)
* [Blogikirjoitus NeuroHivessa](https://neurohive.io/ru/osnovy-data-science/variacionnyj-avtojenkoder-vae/)
* [Variatiiviset autokooderit selitettynä](https://kvfrans.com/variational-autoencoders-explained/)
* [Ehdolliset variatiiviset autokooderit](https://ijdykeman.github.io/ml/2016/12/21/cvae.html)

## Tehtävä

[TensorFlow-muistikirjan](AutoencodersTF.ipynb) lopussa on 'tehtävä' - käytä sitä tehtävänäsi.

---

**Vastuuvapauslauseke**:  
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, huomioithan, että automaattiset käännökset voivat sisältää virheitä tai epätarkkuuksia. Alkuperäinen asiakirja sen alkuperäisellä kielellä tulisi pitää ensisijaisena lähteenä. Kriittisen tiedon osalta suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa väärinkäsityksistä tai virhetulkinnoista, jotka johtuvat tämän käännöksen käytöstä.