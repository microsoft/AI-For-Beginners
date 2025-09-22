<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "0b306c04f5337b6e7430e5c0b16bb5c0",
  "translation_date": "2025-08-31T17:41:55+00:00",
  "source_file": "lessons/4-ComputerVision/09-Autoencoders/README.md",
  "language_code": "lt"
}
-->
# Autoenkoderiai

Mokant CNN, viena iš problemų yra ta, kad reikia daug pažymėtų duomenų. Vaizdų klasifikavimo atveju reikia rankiniu būdu suskirstyti vaizdus į skirtingas klases.

## [Prieš paskaitą vykdomas testas](https://ff-quizzes.netlify.app/en/ai/quiz/17)

Tačiau galime norėti naudoti neapdorotus (nepažymėtus) duomenis CNN funkcijų ištraukėjų mokymui, vadinamą **savaiminio mokymosi** metodu. Vietoj etikečių naudosime mokymo vaizdus tiek kaip tinklo įvestį, tiek kaip išvestį. Pagrindinė **autoenkoderio** idėja yra turėti **enkoderio tinklą**, kuris paverčia įvesties vaizdą į tam tikrą **latentę erdvę** (paprastai tai yra mažesnio dydžio vektorius), ir **dekoderio tinklą**, kurio tikslas yra atkurti originalų vaizdą.

> ✅ [Autoenkoderis](https://wikipedia.org/wiki/Autoencoder) yra "dirbtinio neuroninio tinklo tipas, naudojamas efektyviam nepažymėtų duomenų kodavimui išmokti."

Kadangi mokome autoenkoderį užfiksuoti kuo daugiau informacijos iš originalaus vaizdo, kad būtų galima tiksliai jį atkurti, tinklas stengiasi rasti geriausią **įterpimą** įvesties vaizdams, kad užfiksuotų jų prasmę.

![Autoenkoderio schema](../../../../../translated_images/autoencoder_schema.5e6fc9ad98a5eb6197f3513cf3baf4dfbe1389a6ae74daebda64de9f1c99f142.lt.jpg)

> Vaizdas iš [Keras tinklaraščio](https://blog.keras.io/building-autoencoders-in-keras.html)

## Autoenkoderių naudojimo scenarijai

Nors originalių vaizdų atkūrimas pats savaime gali atrodyti ne itin naudingas, yra keletas scenarijų, kur autoenkoderiai yra ypač naudingi:

* **Vaizdų dimensijos mažinimas vizualizacijai** arba **vaizdų įterpimų mokymui**. Paprastai autoenkoderiai duoda geresnius rezultatus nei PCA, nes jie atsižvelgia į vaizdų erdvinę prigimtį ir hierarchines savybes.
* **Triukšmo šalinimas**, t. y. triukšmo pašalinimas iš vaizdo. Kadangi triukšmas perduoda daug nereikalingos informacijos, autoenkoderis negali viso to sutalpinti į palyginti mažą latentę erdvę, todėl jis užfiksuoja tik svarbią vaizdo dalį. Mokant triukšmo šalinimo tinklus, pradedame nuo originalių vaizdų ir naudojame vaizdus su dirbtinai pridėtu triukšmu kaip autoenkoderio įvestį.
* **Superrezoliucija**, vaizdo raiškos didinimas. Pradedame nuo aukštos raiškos vaizdų ir naudojame mažesnės raiškos vaizdą kaip autoenkoderio įvestį.
* **Generatyviniai modeliai**. Kai autoenkoderis yra išmokytas, dekoderio dalis gali būti naudojama naujų objektų kūrimui, pradedant nuo atsitiktinių latentės vektorių.

## Variaciniai autoenkoderiai (VAE)

Tradiciniai autoenkoderiai kažkaip sumažina įvesties duomenų dimensiją, nustatydami svarbias įvesties vaizdų savybes. Tačiau latentės vektoriai dažnai neturi aiškios prasmės. Kitaip tariant, naudojant MNIST duomenų rinkinį kaip pavyzdį, nustatyti, kurie skaitmenys atitinka skirtingus latentės vektorius, nėra lengva užduotis, nes artimi latentės vektoriai nebūtinai atitinka tuos pačius skaitmenis.

Kita vertus, norint mokyti *generatyvinius* modelius, geriau turėti tam tikrą supratimą apie latentę erdvę. Ši idėja veda mus prie **variacinio autoenkoderio** (VAE).

VAE yra autoenkoderis, kuris mokosi prognozuoti *statistinį pasiskirstymą* latentės parametrų, vadinamą **latentės pasiskirstymu**. Pavyzdžiui, galime norėti, kad latentės vektoriai būtų normaliai pasiskirstę su tam tikru vidurkiu z<sub>mean</sub> ir standartiniu nuokrypiu z<sub>sigma</sub> (tiek vidurkis, tiek standartinis nuokrypis yra tam tikro dimensijos vektoriai). VAE enkoderis mokosi prognozuoti šiuos parametrus, o dekoderis paima atsitiktinį vektorių iš šio pasiskirstymo, kad atkurtų objektą.

Apibendrinant:

* Iš įvesties vektoriaus prognozuojame `z_mean` ir `z_log_sigma` (vietoj standartinio nuokrypio prognozuojame jo logaritmą)
* Iš pasiskirstymo N(z<sub>mean</sub>,exp(z<sub>log\_sigma</sub>)) imame vektorių `sample`
* Dekoderis bando atkurti originalų vaizdą, naudodamas `sample` kaip įvesties vektorių

<img src="images/vae.png" width="50%">

> Vaizdas iš [šio tinklaraščio įrašo](https://ijdykeman.github.io/ml/2016/12/21/cvae.html) autoriaus Isaak Dykeman

Variaciniai autoenkoderiai naudoja sudėtingą nuostolių funkciją, kurią sudaro dvi dalys:

* **Atkūrimo nuostolis** – nuostolių funkcija, rodanti, kaip arti atkurtas vaizdas yra tikslui (tai gali būti vidutinė kvadratinė paklaida arba MSE). Tai ta pati nuostolių funkcija kaip ir įprastuose autoenkoderiuose.
* **KL nuostolis**, kuris užtikrina, kad latentės kintamųjų pasiskirstymas išliktų artimas normaliam pasiskirstymui. Jis pagrįstas [Kullback-Leibler divergencijos](https://www.countbayesie.com/blog/2017/5/9/kullback-leibler-divergence-explained) sąvoka – metrika, skirta įvertinti, kaip panašūs yra du statistiniai pasiskirstymai.

Vienas svarbus VAE privalumas yra tas, kad jie leidžia gana lengvai generuoti naujus vaizdus, nes žinome, iš kurio pasiskirstymo imti latentės vektorius. Pavyzdžiui, jei mokome VAE su 2D latentės vektoriumi MNIST duomenų rinkinyje, galime keisti latentės vektoriaus komponentus, kad gautume skirtingus skaitmenis:

<img alt="vaemnist" src="images/vaemnist.png" width="50%"/>

> Vaizdas autoriaus [Dmitry Soshnikov](http://soshnikov.com)

Stebėkite, kaip vaizdai susilieja vienas su kitu, kai pradedame gauti latentės vektorius iš skirtingų latentės parametrų erdvės dalių. Taip pat galime vizualizuoti šią erdvę 2D:

<img alt="vaemnist cluster" src="images/vaemnist-diag.png" width="50%"/> 

> Vaizdas autoriaus [Dmitry Soshnikov](http://soshnikov.com)

## ✍️ Pratimai: Autoenkoderiai

Sužinokite daugiau apie autoenkoderius šiuose atitinkamuose užrašų knygelėse:

* [Autoenkoderiai TensorFlow](AutoencodersTF.ipynb)
* [Autoenkoderiai PyTorch](AutoEncodersPyTorch.ipynb)

## Autoenkoderių savybės

* **Duomenų specifika** – jie gerai veikia tik su tokio tipo vaizdais, su kuriais buvo mokomi. Pavyzdžiui, jei mokome superrezoliucijos tinklą su gėlėmis, jis neveiks gerai su portretais. Taip yra todėl, kad tinklas gali sukurti aukštesnės raiškos vaizdą, naudodamas smulkias detales iš mokymo duomenų rinkinio.
* **Nuostolingumas** – atkurtas vaizdas nėra toks pat kaip originalus vaizdas. Nuostolių pobūdis apibrėžiamas *nuostolių funkcija*, naudojama mokymo metu.
* Veikia su **nepažymėtais duomenimis**

## [Po paskaitos vykdomas testas](https://ff-quizzes.netlify.app/en/ai/quiz/18)

## Išvada

Šioje pamokoje sužinojote apie įvairius autoenkoderių tipus, prieinamus AI mokslininkui. Sužinojote, kaip juos kurti ir kaip naudoti vaizdų atkūrimui. Taip pat sužinojote apie VAE ir kaip jį naudoti naujų vaizdų generavimui.

## 🚀 Iššūkis

Šioje pamokoje sužinojote apie autoenkoderių naudojimą vaizdams. Tačiau jie gali būti naudojami ir muzikai! Peržiūrėkite Magenta projekto [MusicVAE](https://magenta.tensorflow.org/music-vae) projektą, kuris naudoja autoenkoderius muzikos atkūrimui išmokti. Atlikite keletą [eksperimentų](https://colab.research.google.com/github/magenta/magenta-demos/blob/master/colab-notebooks/Multitrack_MusicVAE.ipynb) su šia biblioteka ir pažiūrėkite, ką galite sukurti.

## [Po paskaitos vykdomas testas](https://ff-quizzes.netlify.app/en/ai/quiz/16)

## Apžvalga ir savarankiškas mokymasis

Daugiau informacijos apie autoenkoderius rasite šiuose šaltiniuose:

* [Autoenkoderių kūrimas Keras](https://blog.keras.io/building-autoencoders-in-keras.html)
* [Tinklaraščio įrašas NeuroHive](https://neurohive.io/ru/osnovy-data-science/variacionnyj-avtojenkoder-vae/)
* [Variaciniai autoenkoderiai paaiškinti](https://kvfrans.com/variational-autoencoders-explained/)
* [Sąlyginiai variaciniai autoenkoderiai](https://ijdykeman.github.io/ml/2016/12/21/cvae.html)

## Užduotis

Šios [užrašų knygelės su TensorFlow](AutoencodersTF.ipynb) pabaigoje rasite „užduotį“ – naudokite ją kaip savo užduotį.

---

**Atsakomybės apribojimas**:  
Šis dokumentas buvo išverstas naudojant AI vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors stengiamės užtikrinti tikslumą, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba turėtų būti laikomas autoritetingu šaltiniu. Kritinei informacijai rekomenduojama naudoti profesionalų žmogaus vertimą. Mes neprisiimame atsakomybės už nesusipratimus ar klaidingus interpretavimus, atsiradusius dėl šio vertimo naudojimo.