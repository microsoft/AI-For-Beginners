# Giliojo mokymosi treniravimo gudrybės

Kai neuroniniai tinklai tampa gilesni, jų treniravimo procesas tampa vis sudėtingesnis. Viena iš pagrindinių problemų yra vadinamosios [nykstančios gradientės](https://en.wikipedia.org/wiki/Vanishing_gradient_problem) arba [sprogstančios gradientės](https://deepai.org/machine-learning-glossary-and-terms/exploding-gradient-problem#:~:text=Exploding%20gradients%20are%20a%20problem,updates%20are%20small%20and%20controlled.). [Šis straipsnis](https://towardsdatascience.com/the-vanishing-exploding-gradient-problem-in-deep-neural-networks-191358470c11) pateikia gerą įvadą į šias problemas.

Norint efektyviau treniruoti gilius tinklus, galima naudoti keletą technikų.

## Vertybių išlaikymas pagrįstame intervale

Norint užtikrinti skaičiavimų stabilumą, svarbu, kad visos neuroninio tinklo vertės būtų pagrįsto masto, paprastai [-1..1] arba [0..1]. Tai nėra labai griežtas reikalavimas, tačiau plaukiojančio kablelio skaičiavimų prigimtis yra tokia, kad skirtingų dydžių vertės negali būti tiksliai apdorojamos kartu. Pavyzdžiui, jei sudėsime 10<sup>-10</sup> ir 10<sup>10</sup>, greičiausiai gausime 10<sup>10</sup>, nes mažesnė vertė bus „konvertuota“ į tą patį dydį kaip didesnė, ir mantisa bus prarasta.

Dauguma aktyvavimo funkcijų turi nelinijines savybes aplink [-1..1], todėl prasminga visus įvesties duomenis skalėti į [-1..1] arba [0..1] intervalą.

## Pradinis svorių inicializavimas

Idealiu atveju norime, kad vertės išliktų tame pačiame intervale, kai jos pereina per tinklo sluoksnius. Todėl svarbu inicializuoti svorius taip, kad būtų išsaugotas vertybių pasiskirstymas.

Normalusis pasiskirstymas **N(0,1)** nėra gera idėja, nes jei turime *n* įėjimų, išėjimo standartinis nuokrypis bus *n*, ir vertės greičiausiai išeis už [0..1] intervalo ribų.

Dažnai naudojami šie inicializavimo būdai:

- Vienodas pasiskirstymas – `uniform`
- **N(0,1/n)** – `gaussian`
- **N(0,1/√n_in)** užtikrina, kad įėjimams su nuliu vidurkiu ir standartiniu nuokrypiu 1 išliks tas pats vidurkis ir standartinis nuokrypis
- **N(0,√2/(n_in+n_out))** – vadinamasis **Xavier inicializavimas** (`glorot`), kuris padeda išlaikyti signalus tinkamame intervale tiek pirmyn, tiek atgal skaičiuojant gradientus

## Partijos normalizavimas

Net ir tinkamai inicializavus svorius, treniravimo metu jie gali tapti labai dideli arba labai maži, o tai išves signalus iš tinkamo intervalo. Signalus galime grąžinti į tinkamą intervalą naudodami vieną iš **normalizavimo** technikų. Nors jų yra keletas (svorių normalizavimas, sluoksnio normalizavimas), dažniausiai naudojama yra partijos normalizavimas.

**Partijos normalizavimo** idėja yra atsižvelgti į visas vertes mini partijoje ir atlikti normalizavimą (t. y. atimti vidurkį ir padalinti iš standartinio nuokrypio) remiantis tomis vertėmis. Tai įgyvendinama kaip tinklo sluoksnis, kuris atlieka šį normalizavimą po svorių pritaikymo, bet prieš aktyvavimo funkciją. Dėl to greičiau treniruojama ir pasiekiamas didesnis galutinis tikslumas.

Čia yra [originalus straipsnis](https://arxiv.org/pdf/1502.03167.pdf) apie partijos normalizavimą, [paaiškinimas Vikipedijoje](https://en.wikipedia.org/wiki/Batch_normalization) ir [geras įvadinis tinklaraščio įrašas](https://towardsdatascience.com/batch-normalization-in-3-levels-of-understanding-14c2da90a338) (ir vienas [rusiškai](https://habrahabr.ru/post/309302/)).

## Dropout

**Dropout** yra įdomi technika, kuri treniravimo metu pašalina tam tikrą procentą atsitiktinių neuronų. Tai taip pat įgyvendinama kaip sluoksnis su vienu parametru (pašalinamų neuronų procentas, paprastai 10%-50%), o treniravimo metu atsitiktiniai įvesties vektoriaus elementai yra nustatomi į nulį prieš perduodant juos kitam sluoksniui.

Nors tai gali atrodyti kaip keista idėja, galite pamatyti dropout poveikį treniruojant MNIST skaitmenų klasifikatorių [`Dropout.ipynb`](Dropout.ipynb) užrašų knygelėje. Tai pagreitina treniravimą ir leidžia pasiekti didesnį tikslumą per mažiau treniravimo epochų.

Šį efektą galima paaiškinti keliais būdais:

- Tai galima laikyti atsitiktiniu šoku modeliui, kuris padeda išvengti optimizacijos įstrigimo lokaliame minimume
- Tai galima laikyti *netiesioginiu modelio vidurkinimu*, nes dropout metu treniruojame šiek tiek kitokį modelį

> *Kai kurie žmonės sako, kad kai girtas žmogus bando kažko išmokti, jis tai geriau prisimins kitą rytą, palyginti su blaiviu žmogumi, nes smegenys su kai kuriais neveikiančiais neuronais geriau prisitaiko suprasti prasmę. Mes niekada netikrinome, ar tai tiesa.*

## Perteklinio pritaikymo prevencija

Vienas iš labai svarbių giluminio mokymosi aspektų yra gebėjimas išvengti [perteklinio pritaikymo](../../3-NeuralNetworks/05-Frameworks/Overfitting.md). Nors gali būti viliojanti idėja naudoti labai galingą neuroninio tinklo modelį, visada turėtume subalansuoti modelio parametrų skaičių su treniravimo pavyzdžių skaičiumi.

> Įsitikinkite, kad suprantate [perteklinio pritaikymo](../../3-NeuralNetworks/05-Frameworks/Overfitting.md) sąvoką, kurią aptarėme anksčiau!

Yra keletas būdų išvengti perteklinio pritaikymo:

- Ankstyvas sustabdymas – nuolat stebėti klaidą validacijos rinkinyje ir sustabdyti treniravimą, kai validacijos klaida pradeda didėti.
- Aiškus svorių mažinimas / reguliavimas – pridėti papildomą baudos terminą prie nuostolių funkcijos už dideles svorių absoliučias vertes, kad modelis negautų labai nestabilių rezultatų
- Modelio vidurkinimas – treniruoti kelis modelius ir tada vidurkinti rezultatus. Tai padeda sumažinti dispersiją.
- Dropout (netiesioginis modelio vidurkinimas)

## Optimizatoriai / Treniravimo algoritmai

Kitas svarbus treniravimo aspektas yra pasirinkti gerą treniravimo algoritmą. Nors klasikinis **gradientinis nusileidimas** yra pagrįstas pasirinkimas, jis kartais gali būti per lėtas arba sukelti kitų problemų.

Giliojo mokymosi srityje naudojame **stochastinį gradientinį nusileidimą** (SGD), kuris yra gradientinis nusileidimas, taikomas mini partijoms, atsitiktinai parinktoms iš treniravimo rinkinio. Svoriai koreguojami pagal šią formulę:

w<sup>t+1</sup> = w<sup>t</sup> - η∇ℒ

### Inercija

**Inercijos SGD** metu išlaikome dalį ankstesnių žingsnių gradiento. Tai panašu į tai, kai judame su inercija, ir gavę smūgį kita kryptimi, mūsų trajektorija nepasikeičia iš karto, bet išlaiko dalį pradinio judėjimo. Čia įvedame kitą vektorių v, kuris atspindi *greitį*:

- v<sup>t+1</sup> = γ v<sup>t</sup> - η∇ℒ
- w<sup>t+1</sup> = w<sup>t</sup> + v<sup>t+1</sup>

Čia parametras γ nurodo, kiek atsižvelgiame į inerciją: γ=0 atitinka klasikinį SGD; γ=1 yra grynas judėjimo lygtis.

### Adam, Adagrad ir kt.

Kadangi kiekviename sluoksnyje signalus dauginame iš tam tikros matricos W<sub>i</sub>, priklausomai nuo ||W<sub>i</sub>||, gradientas gali arba sumažėti iki beveik 0, arba augti neribotai. Tai yra sprogstančių/nykstančių gradientų problemos esmė.

Vienas iš šios problemos sprendimų yra naudoti tik gradiento kryptį lygties skaičiavime ir ignoruoti absoliučią vertę, t. y.

w<sup>t+1</sup> = w<sup>t</sup> - η(∇ℒ/||∇ℒ||), kur ||∇ℒ|| = √∑(∇ℒ)<sup>2</sup>

Šis algoritmas vadinamas **Adagrad**. Kiti algoritmai, naudojantys tą pačią idėją: **RMSProp**, **Adam**

> **Adam** laikomas labai efektyviu algoritmu daugeliui užduočių, todėl, jei nesate tikri, kurį naudoti – rinkitės Adam.

### Gradientų ribojimas

Gradientų ribojimas yra aukščiau pateiktos idėjos išplėtimas. Kai ||∇ℒ|| ≤ θ, svorių optimizavimui naudojame originalų gradientą, o kai ||∇ℒ|| > θ – gradientą dalijame iš jo normos. Čia θ yra parametras, daugeliu atvejų galime imti θ=1 arba θ=10.

### Mokymosi greičio mažinimas

Treniravimo sėkmė dažnai priklauso nuo mokymosi greičio parametro η. Logiška manyti, kad didesnės η vertės lemia greitesnį treniravimą, ko paprastai norime treniravimo pradžioje, o mažesnės η vertės leidžia tinklą tiksliau sureguliuoti. Todėl daugeliu atvejų norime mažinti η treniravimo proceso metu.

Tai galima padaryti dauginant η iš tam tikro skaičiaus (pvz., 0.98) po kiekvienos treniravimo epochos arba naudojant sudėtingesnį **mokymosi greičio grafiką**.

## Skirtingos tinklo architektūros

Pasirinkti tinkamą tinklo architektūrą savo problemai gali būti sudėtinga. Paprastai pasirenkame architektūrą, kuri jau pasiteisino atliekant mūsų specifinę užduotį (arba panašią). Čia yra [geras apžvalga](https://www.topbots.com/a-brief-history-of-neural-network-architectures/) apie neuroninių tinklų architektūras kompiuterinei regai.

> Svarbu pasirinkti architektūrą, kuri bus pakankamai galinga turimam treniravimo pavyzdžių skaičiui. Per galingo modelio pasirinkimas gali sukelti [perteklinį pritaikymą](../../3-NeuralNetworks/05-Frameworks/Overfitting.md).

Kitas geras būdas yra naudoti architektūrą, kuri automatiškai prisitaikys prie reikiamo sudėtingumo. Tam tikru mastu **ResNet** architektūra ir **Inception** yra savireguliuojančios. [Daugiau apie kompiuterinės regos architektūras](../07-ConvNets/CNN_Architectures.md).

---

**Atsakomybės apribojimas**:  
Šis dokumentas buvo išverstas naudojant AI vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba turėtų būti laikomas autoritetingu šaltiniu. Kritinei informacijai rekomenduojama profesionali žmogaus vertimo paslauga. Mes neprisiimame atsakomybės už nesusipratimus ar klaidingus interpretavimus, atsiradusius dėl šio vertimo naudojimo.