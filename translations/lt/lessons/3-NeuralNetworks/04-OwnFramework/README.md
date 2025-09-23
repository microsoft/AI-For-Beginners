<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "186bf7eeab776b36f557357ea56d4751",
  "translation_date": "2025-08-31T17:49:36+00:00",
  "source_file": "lessons/3-NeuralNetworks/04-OwnFramework/README.md",
  "language_code": "lt"
}
-->
# Įvadas į neuroninius tinklus. Daugiasluoksnis perceptronas

Ankstesniame skyriuje sužinojote apie paprasčiausią neuroninio tinklo modelį – vieno sluoksnio perceptroną, kuris yra linijinis dviejų klasių klasifikavimo modelis.

Šiame skyriuje išplėsime šį modelį į lankstesnę sistemą, leidžiančią:

* atlikti **daugiaklasę klasifikaciją** be dviejų klasių
* spręsti **regresijos problemas** be klasifikavimo
* atskirti klases, kurios nėra linijiškai atskiriamos

Taip pat sukursime savo modulinę sistemą Python kalboje, kuri leis mums konstruoti įvairias neuroninių tinklų architektūras.

## [Prieš paskaitą vykdomas testas](https://ff-quizzes.netlify.app/en/ai/quiz/7)

## Mašininio mokymosi formalizavimas

Pradėkime nuo mašininio mokymosi problemos formalizavimo. Tarkime, turime mokymo duomenų rinkinį **X** su žymėmis **Y**, ir mums reikia sukurti modelį *f*, kuris pateiktų kuo tikslesnes prognozes. Prognozių kokybė matuojama **nuostolių funkcija** ℒ. Dažnai naudojamos šios nuostolių funkcijos:

* Regresijos problemoms, kai reikia prognozuoti skaičių, galime naudoti **absoliutinę paklaidą** ∑<sub>i</sub>|f(x<sup>(i)</sup>)-y<sup>(i)</sup>| arba **kvadratinę paklaidą** ∑<sub>i</sub>(f(x<sup>(i)</sup>)-y<sup>(i)</sup>)<sup>2</sup>
* Klasifikavimui naudojame **0-1 nuostolį** (kuris iš esmės yra tas pats kaip modelio **tikslumas**) arba **logistinį nuostolį**.

Vieno sluoksnio perceptrono funkcija *f* buvo apibrėžta kaip linijinė funkcija *f(x)=wx+b* (čia *w* yra svorių matrica, *x* yra įvesties požymių vektorius, o *b* yra poslinkio vektorius). Skirtingoms neuroninių tinklų architektūroms ši funkcija gali būti sudėtingesnė.

> Klasifikavimo atveju dažnai pageidaujama, kad tinklo išvestis būtų klasių tikimybės. Norint paversti bet kokius skaičius į tikimybes (pvz., normalizuoti išvestį), dažnai naudojame **softmax** funkciją σ, ir funkcija *f* tampa *f(x)=σ(wx+b)*

Aukščiau pateiktoje *f* apibrėžtyje *w* ir *b* vadinami **parametrais** θ=⟨*w,b*⟩. Turėdami duomenų rinkinį ⟨**X**,**Y**⟩, galime apskaičiuoti bendrą klaidą visame duomenų rinkinyje kaip funkciją nuo parametrų θ.

> ✅ **Neuroninio tinklo mokymo tikslas yra sumažinti klaidą keičiant parametrus θ**

## Gradientinio nusileidimo optimizavimas

Yra gerai žinomas funkcijų optimizavimo metodas, vadinamas **gradientiniu nusileidimu**. Jo idėja yra ta, kad galime apskaičiuoti nuostolių funkcijos išvestinę (daugiamatėje erdvėje vadinamą **gradientu**) pagal parametrus ir keisti parametrus taip, kad klaida sumažėtų. Tai galima formalizuoti taip:

* Inicializuokite parametrus atsitiktinėmis reikšmėmis w<sup>(0)</sup>, b<sup>(0)</sup>
* Kartokite šį žingsnį daug kartų:
    - w<sup>(i+1)</sup> = w<sup>(i)</sup>-η∂ℒ/∂w
    - b<sup>(i+1)</sup> = b<sup>(i)</sup>-η∂ℒ/∂b

Mokymo metu optimizavimo žingsniai turėtų būti skaičiuojami atsižvelgiant į visą duomenų rinkinį (prisiminkite, kad nuostoliai skaičiuojami kaip suma per visus mokymo pavyzdžius). Tačiau realiame gyvenime mes imame mažas duomenų rinkinio dalis, vadinamas **minipartijomis**, ir skaičiuojame gradientus remdamiesi duomenų pogrupiu. Kadangi kiekvieną kartą pogrupis imamas atsitiktinai, toks metodas vadinamas **stochastiniu gradientiniu nusileidimu** (SGD).

## Daugiasluoksniai perceptronai ir atgalinio sklidimo algoritmas

Vieno sluoksnio tinklas, kaip matėme aukščiau, gali klasifikuoti linijiškai atskiriamas klases. Norėdami sukurti turtingesnį modelį, galime sujungti kelis tinklo sluoksnius. Matematiškai tai reikštų, kad funkcija *f* turėtų sudėtingesnę formą ir būtų skaičiuojama keliais etapais:
* z<sub>1</sub>=w<sub>1</sub>x+b<sub>1</sub>
* z<sub>2</sub>=w<sub>2</sub>α(z<sub>1</sub>)+b<sub>2</sub>
* f = σ(z<sub>2</sub>)

Čia α yra **nelinijinė aktyvavimo funkcija**, σ yra softmax funkcija, o parametrai θ=<*w<sub>1</sub>,b<sub>1</sub>,w<sub>2</sub>,b<sub>2</sub>*>.

Gradientinio nusileidimo algoritmas išliktų toks pat, tačiau gradientų skaičiavimas būtų sudėtingesnis. Remiantis grandinės diferencijavimo taisykle, galime apskaičiuoti išvestines taip:

* ∂ℒ/∂w<sub>2</sub> = (∂ℒ/∂σ)(∂σ/∂z<sub>2</sub>)(∂z<sub>2</sub>/∂w<sub>2</sub>)
* ∂ℒ/∂w<sub>1</sub> = (∂ℒ/∂σ)(∂σ/∂z<sub>2</sub>)(∂z<sub>2</sub>/∂α)(∂α/∂z<sub>1</sub>)(∂z<sub>1</sub>/∂w<sub>1</sub>)

> ✅ Grandinės diferencijavimo taisyklė naudojama nuostolių funkcijos išvestinėms pagal parametrus apskaičiuoti.

Atkreipkite dėmesį, kad kairiausia visų šių išraiškų dalis yra ta pati, todėl galime efektyviai apskaičiuoti išvestines, pradedant nuo nuostolių funkcijos ir einant "atgal" per skaičiavimo grafiką. Todėl daugiasluoksnio perceptrono mokymo metodas vadinamas **atgaliniu sklidimu** arba 'backprop'.

<img alt="skaičiavimo grafikas" src="images/ComputeGraphGrad.png"/>

> TODO: paveikslėlio citata

> ✅ Atgalinį sklidimą aptarsime daug išsamiau mūsų užrašų knygelės pavyzdyje.  

## Išvada

Šioje pamokoje sukūrėme savo neuroninio tinklo biblioteką ir panaudojome ją paprastai dviejų dimensijų klasifikavimo užduočiai.

## 🚀 Iššūkis

Pridedamoje užrašų knygelėje įgyvendinsite savo sistemą daugiasluoksnių perceptronų kūrimui ir mokymui. Galėsite išsamiai pamatyti, kaip veikia šiuolaikiniai neuroniniai tinklai.

Pereikite prie [OwnFramework](OwnFramework.ipynb) užrašų knygelės ir dirbkite su ja.

## [Po paskaitos vykdomas testas](https://ff-quizzes.netlify.app/en/ai/quiz/8)

## Apžvalga ir savarankiškas mokymasis

Atgalinis sklidimas yra dažnai naudojamas algoritmas dirbtinio intelekto ir mašininio mokymosi srityse, verta jį [išsamiau išnagrinėti](https://wikipedia.org/wiki/Backpropagation)

## [Užduotis](lab/README.md)

Šioje laboratorijoje jūsų prašoma panaudoti sistemą, kurią sukūrėte šioje pamokoje, MNIST ranka rašytų skaitmenų klasifikavimo užduočiai spręsti.

* [Instrukcijos](lab/README.md)
* [Užrašų knygelė](lab/MyFW_MNIST.ipynb)

---

**Atsakomybės apribojimas**:  
Šis dokumentas buvo išverstas naudojant AI vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba turėtų būti laikomas autoritetingu šaltiniu. Kritinei informacijai rekomenduojama naudoti profesionalų žmogaus vertimą. Mes neprisiimame atsakomybės už nesusipratimus ar klaidingus interpretavimus, atsiradusius dėl šio vertimo naudojimo.