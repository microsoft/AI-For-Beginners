# Giluminio mokymosi triukai

Kadangi neuroniniai tinklai tampa vis gilesni, jų mokymosi procesas tampa vis sudėtingesnis. Viena pagrindinių problemų yra vadinamieji [nykstantys gradientai](https://en.wikipedia.org/wiki/Vanishing_gradient_problem) arba [eksploduojantys gradientai](https://deepai.org/machine-learning-glossary-and-terms/exploding-gradient-problem#:~:text=Exploding%20gradients%20are%20a%20problem,updates%20are%20small%20and%20controlled.). [Šis įrašas](https://towardsdatascience.com/the-vanishing-exploding-gradient-problem-in-deep-neural-networks-191358470c11) gerai pristato šias problemas.

Norint efektyviau mokyti gilius tinklus, galima naudoti keletą metodų.

## Vertybių laikymas tinkamame intervale

Norint, kad skaičiavimai būtų stabilesni, turime užtikrinti, kad visos neuroninio tinklo vertės būtų tinkamo mastelio, paprastai intervale [-1..1] arba [0..1]. Tai nėra labai griežta taisyklė, tačiau plaukiojančių kablelių skaičiavimų esmė tokia, kad skirtingo dydžio reikšmės negali būti tiksliai apdorojamos kartu. Pavyzdžiui, jei sudėsime 10<sup>-10</sup> ir 10<sup>10</sup>, greičiausiai gausime 10<sup>10</sup>, nes mažesnė reikšmė bus "paversta" į tokį patį mastelį kaip ir didesnė, todėl mantisa pranyks.

Dauguma aktyvacijos funkcijų yra netiesinės apie intervalą [-1..1], todėl prasminga visus įvesties duomenis paversti į intervalą [-1..1] arba [0..1].

## Pradinė svorių inicializacija

Idealiu atveju, norime, kad vertės būtų tame pačiame diapazone praėjus per tinklo sluoksnius. Todėl svarbu inicializuoti svorius taip, kad būtų išsaugota vertybių pasiskirstymo forma.

Normalusis pasiskirstymas **N(0,1)** nėra gera idėja, nes turint *n* įėjimų, išėjimo standartinis nuokrypis bus *&radic;n*, ir vertės gali išeiti už intervalą [0..1].

Dažnai naudojamos šios inicializacijos:

 * Vienodas pasiskirstymas -- `uniform`
 * **N(0,1/n)** -- `gaussian`
 * **N(0,1/&radic;n_in)** garantuoja, kad įėjimams su nuliu vidurkiu ir standartiniu nuokrypiu 1 išlieka tas pats vidurkis/standartinis nuokrypis
 * **N(0,&radic;2/(n_in+n_out))** -- vadinamoji **Xavier inicializacija** (`glorot`), kuri padeda signalus išlaikyti diapazone tiek tiesioginiame, tiek atvirkštiniame sklidimo metu

## Paketų normalizavimas

Net ir su tinkama svorių inicializacija, svoriai gali tapti labai dideli arba maži mokymosi metu, ir tai išves signalus iš tinkamo diapazono. Signalus galima sugrąžinti naudojant vieną iš **normalizavimo** metodų. Nors jų yra keli (svorių normalizavimas, sluoksnio normalizavimas), dažniausiai naudojamas yra paketų normalizavimas.

Idėja, esanti **paketų normalizavime**, yra įvertinti visas reikšmes per mini paketą ir vykdyti normalizavimą (t. y. atimti vidurkį ir padalyti iš standartinio nuokrypio) remiantis šiomis reikšmėmis. Tai įgyvendinama kaip tinklo sluoksnis, kuris atlieka normalizavimą po svorių taikymo, bet prieš aktyvacijos funkciją. Dėl to dažniausiai matomas aukštesnis galutinis tikslumas ir greitesnis mokymasis.

Čia yra [originalus straipsnis](https://arxiv.org/pdf/1502.03167.pdf) apie paketų normalizavimą, [paaiškinimas Wikipedijoje](https://en.wikipedia.org/wiki/Batch_normalization) bei [geras pradedančiųjų tinklaraščio įrašas](https://towardsdatascience.com/batch-normalization-in-3-levels-of-understanding-14c2da90a338) (ir vienas [rusų kalba](https://habrahabr.ru/post/309302/)).

## Droupautas

**Droupautas** yra įdomi technika, kuri mokymo metu pašalina tam tikrą procentą atsitiktinių neuronų. Tai taip pat įgyvendinama kaip sluoksnis su vienu parametru (pašalinamų neuronų procentas, dažniausiai 10%-50%), ir mokymo metu atsitiktiniai įvesties vektoriaus elementai yra nuliniai prieš perduodant kitam sluoksniui.

Nors tai gali skambėti keistai, galite pamatyti droupauto poveikį MNIST skaitmenų klasifikatoriui [`Dropout.ipynb`](Dropout.ipynb) užrašų knygoje. Tai pagreitina mokymą ir leidžia pasiekti didesnį tikslumą per mažiau mokymosi epochų.

Šį efektą galima paaiškinti keliais būdais:

 * Jį galima laikyti kaip atsitiktinį smūgį modeliui, kuris išveda optimizaciją iš lokalaus minimumo
 * Jį galima laikyti kaip *implicit model averaging* (netiesioginį modelių vidurkinimą), nes droupauto metu tarsi treniruojamas kiek kitoks modelis

> *Kai kurie žmonės sako, kad kai girtautas žmogus bando ko nors išmokti, kitą rytą jis tai geriau prisimena nei blaivus žmogus, nes smegenys su kai kurių neuronų sutrikimais bando geriau prisitaikyti suvokti prasmę. Mes niekada nebandėme, ar tai tiesa.*

## Perpanaudojimo prevencija

Vienas iš labai svarbių giluminio mokymosi aspektų yra sugebėjimas užkirsti kelią [perpanaudojimui](../../3-NeuralNetworks/05-Frameworks/Overfitting.md). Nors gali būti pagunda naudoti labai galingą neuroninio tinklo modelį, visada turime subalansuoti modelio parametrų skaičių su mokymosi pavyzdžių skaičiumi.

> Įsitikinkite, kad suprantate [perpanaudojimo](../../3-NeuralNetworks/05-Frameworks/Overfitting.md) koncepciją, kurią pristatėme anksčiau!

Yra keletas būdų užkirsti kelią perpanaudojimui:

 * Ankstyvas sustabdymas -- nuolat stebėti klaidą validacijos rinkinyje ir sustabdyti mokymą, kai validacijos klaida pradeda didėti.
 * Aiškus svorių mažinimas / reguliavimas -- pridedant papildomą bausmę nuostolių funkcijai už dideles absoliučias svorių reikšmes, kas padeda išvengti modelio labai nestabilių rezultatų
 * Modelių vidurkinimas -- treniruojant kelis modelius ir vidurkinant rezultatus. Tai padeda sumažinti variaciją.
 * Droupautas (netiesioginis modelių vidurkinimas)

## Optimizatoriai / Mokymosi algoritmai

Kitas svarbus mokymosi aspektas yra pasirinkti tinkamą mokymo algoritmą. Nors klasikinis **gradiento nuolydis** yra racionalus pasirinkimas, jis kartais gali būti per lėtas arba sukelti kitų problemų.

Giluminiame mokyme mes naudojame **stokastinį gradiento nuolydį** (SGD), kuris taikomas minibachams, atsitiktinai atrinktiems iš mokymo duomenų rinkinio. Svoriai koreguojami pagal šią formulę:

w<sup>t+1</sup> = w<sup>t</sup> - &eta;&nabla;&lagran;

### Momentumas

**momentumo SGD** metu išlaikome dalį gradientų iš ankstesnių žingsnių. Tai panašu į situaciją, kai judame inercija, ir gauname smūgį į kitą pusę, trajektorija nesikeičia iš karto, bet saugo dalį pradinių judesių. Čia įvedame kitą vektorių v, kuris atspindi *greitį*:

* v<sup>t+1</sup> = &gamma; v<sup>t</sup> - &eta;&nabla;&lagran;
* w<sup>t+1</sup> = w<sup>t</sup>+v<sup>t+1</sup>

Čia parametras &gamma; nurodo, kiek atsižvelgiame į inertiją: &gamma;=0 atitinka klasikinį SGD; &gamma;=1 yra grynoji judėjimo lygtis.

### Adam, Adagrad ir kt.

Kadangi kiekviename sluoksnyje dauginame signalus iš matricos W<sub>i</sub>, priklausomai nuo ||W<sub>i</sub>||, gradientas gali arba išnykti ir priartėti prie 0, arba nevaldomai augti. Tai yra Exploding/Vanishing Gradients problemos esmė.

Vienas iš šios problemos sprendimų yra naudoti tik gradiento kryptį lygties formulėje ir ignoruoti absoliučią vertę, t. y.

w<sup>t+1</sup> = w<sup>t</sup> - &eta;(&nabla;&lagran;/||&nabla;&lagran;||), kur ||&nabla;&lagran;|| = &radic;&sum;(&nabla;&lagran;)<sup>2</sup>

Šis algoritmas vadinamas **Adagrad**. Kiti su tokia pačia idėja paremti algoritmai: **RMSProp**, **Adam**

> **Adam** laikomas labai efektyviu algoritmu daugeliui pritaikymų, todėl jei nesate tikri, kurį naudoti – rinkitės Adam.

### Gradientų „apkarpymas“ (clipping)

Gradientų apkarpymas yra minėtos idėjos plėtinys. Kai ||&nabla;&lagran;|| &le; &theta;, laikome originalų gradientą svorio optimizavimui, o kai ||&nabla;&lagran;|| > &theta;, dalijame gradientą iš jo normos. Čia &theta; yra parametras, daugeliu atvejų galime imti &theta;=1 arba &theta;=10.

### Mokymosi greičio mažinimas

Mokymosi sėkmė dažnai priklauso nuo mokymosi parametro &eta;. Logiška manyti, kad didesnės &eta; reikšmės leidžia greičiau mokytis, kas dažnai pageidaujama mokymosi pradžioje, o mažesnės &eta; leidžia geriau tikslinti tinklą vėliau. Todėl daugeliu atvejų norime mažinti &eta; mokymosi metu.

Tai galima padaryti dauginant &eta; iš tam tikro skaičiaus (pvz., 0.98) po kiekvienos mokymosi epchos arba naudojant sudėtingesnį **mokymosi greičio tvarkaraštį**.

## Skirtingos tinklų architektūros

Teisingos tinklo architektūros pasirinkimas jūsų problemai gali būti sudėtingas. Paprastai pasirenkama architektūra, kuri įrodė savo veiksmingumą mūsų specifinei užduočiai (ar panašiai). Štai [geras apžvalginis straipsnis](https://www.topbots.com/a-brief-history-of-neural-network-architectures/) apie neuroninių tinklų architektūras kompiuterinei vizijai.

> Svarbu pasirinkti tokį modelį, kuris būtų pakankamai galingas turimam mokymosi pavyzdžių kiekiui. Per galingas modelis gali sukelti [perpanaudojimą](../../3-NeuralNetworks/05-Frameworks/Overfitting.md)

Kitas geras būdas būtų naudoti architektūrą, kuri automatiškai prisitaiko prie reikiamo sudėtingumo. Tam tikra prasme, tokie architektūros kaip **ResNet** ir **Inception** yra savaime pritaikomos. [Daugiau apie kompiuterinės vizijos architektūras](../07-ConvNets/CNN_Architectures.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Atsakomybės apribojimas**:
Šis dokumentas buvo išverstas naudojant dirbtinio intelekto vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba laikomas autoritetingu šaltiniu. Svarbiai informacijai rekomenduojama naudoti profesionalų žmogiškąjį vertimą. Mes neatsakome už jokius nesusipratimus ar neteisingą interpretaciją, kilusią naudojantis šiuo vertimu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->