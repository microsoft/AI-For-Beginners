<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "186bf7eeab776b36f557357ea56d4751",
  "translation_date": "2025-08-25T23:45:20+00:00",
  "source_file": "lessons/3-NeuralNetworks/04-OwnFramework/README.md",
  "language_code": "sk"
}
-->
# Úvod do neurónových sietí. Viacvrstvový perceptron

V predchádzajúcej časti ste sa oboznámili s najjednoduchším modelom neurónovej siete – jednovrstvovým perceptronom, lineárnym modelom pre dvojtriednu klasifikáciu.

V tejto časti rozšírime tento model na flexibilnejší rámec, ktorý nám umožní:

* vykonávať **viactriednu klasifikáciu** okrem dvojtriednej
* riešiť **regresné problémy** okrem klasifikácie
* oddeliť triedy, ktoré nie sú lineárne separovateľné

Taktiež si vyvinieme vlastný modulárny rámec v Pythone, ktorý nám umožní konštruovať rôzne architektúry neurónových sietí.

## [Kvíz pred prednáškou](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/104)

## Formalizácia strojového učenia

Začnime formalizáciou problému strojového učenia. Predpokladajme, že máme tréningovú množinu dát **X** s označeniami **Y**, a potrebujeme vytvoriť model *f*, ktorý bude robiť čo najpresnejšie predikcie. Kvalita predikcií sa meria pomocou **stratovej funkcie** ℒ. Často sa používajú nasledujúce stratové funkcie:

* Pre regresné problémy, keď potrebujeme predpovedať číslo, môžeme použiť **absolútnu chybu** ∑<sub>i</sub>|f(x<sup>(i)</sup>)-y<sup>(i)</sup>| alebo **kvadratickú chybu** ∑<sub>i</sub>(f(x<sup>(i)</sup>)-y<sup>(i)</sup>)<sup>2</sup>
* Pre klasifikáciu používame **0-1 stratu** (čo je v podstate to isté ako **presnosť** modelu) alebo **logistickú stratu**.

Pre jednovrstvový perceptron bola funkcia *f* definovaná ako lineárna funkcia *f(x)=wx+b* (kde *w* je matica váh, *x* je vektor vstupných vlastností a *b* je vektor biasu). Pre rôzne architektúry neurónových sietí môže mať táto funkcia zložitejšiu formu.

> V prípade klasifikácie je často žiaduce získať pravdepodobnosti príslušných tried ako výstup siete. Na konverziu ľubovoľných čísel na pravdepodobnosti (napr. na normalizáciu výstupu) často používame funkciu **softmax** σ, a funkcia *f* sa stáva *f(x)=σ(wx+b)*.

V definícii *f* vyššie sa *w* a *b* nazývajú **parametre** θ=⟨*w,b*⟩. Na základe množiny dát ⟨**X**,**Y**⟩ môžeme vypočítať celkovú chybu na celej množine dát ako funkciu parametrov θ.

> ✅ **Cieľom trénovania neurónovej siete je minimalizovať chybu zmenou parametrov θ**

## Optimalizácia pomocou gradientného zostupu

Existuje známa metóda optimalizácie funkcií nazývaná **gradientný zostup**. Myšlienka spočíva v tom, že môžeme vypočítať deriváciu (v multidimenzionálnom prípade nazývanú **gradient**) stratovej funkcie vzhľadom na parametre a meniť parametre tak, aby sa chyba znižovala. To môžeme formalizovať nasledovne:

* Inicializujte parametre náhodnými hodnotami w<sup>(0)</sup>, b<sup>(0)</sup>
* Opakujte nasledujúci krok mnohokrát:
    - w<sup>(i+1)</sup> = w<sup>(i)</sup>-η∂ℒ/∂w
    - b<sup>(i+1)</sup> = b<sup>(i)</sup>-η∂ℒ/∂b

Počas trénovania by sa optimalizačné kroky mali počítať s ohľadom na celú množinu dát (pamätajte, že strata sa počíta ako súčet cez všetky tréningové vzorky). V praxi však berieme malé časti množiny dát nazývané **minibatch-e** a počítame gradienty na základe podmnožiny dát. Pretože podmnožina sa zakaždým vyberá náhodne, takáto metóda sa nazýva **stochastický gradientný zostup** (SGD).

## Viacvrstvové perceptrony a spätná propagácia

Jednovrstvová sieť, ako sme videli vyššie, je schopná klasifikovať lineárne separovateľné triedy. Na vytvorenie bohatšieho modelu môžeme kombinovať niekoľko vrstiev siete. Matematicky to znamená, že funkcia *f* bude mať zložitejšiu formu a bude sa počítať v niekoľkých krokoch:
* z<sub>1</sub>=w<sub>1</sub>x+b<sub>1</sub>
* z<sub>2</sub>=w<sub>2</sub>α(z<sub>1</sub>)+b<sub>2</sub>
* f = σ(z<sub>2</sub>)

Tu je α **nelineárna aktivačná funkcia**, σ je softmax funkcia a parametre θ=<*w<sub>1</sub>,b<sub>1</sub>,w<sub>2</sub>,b<sub>2</sub>*>.

Algoritmus gradientného zostupu zostáva rovnaký, ale výpočet gradientov je zložitejší. Na základe pravidla reťazovej derivácie môžeme vypočítať derivácie nasledovne:

* ∂ℒ/∂w<sub>2</sub> = (∂ℒ/∂σ)(∂σ/∂z<sub>2</sub>)(∂z<sub>2</sub>/∂w<sub>2</sub>)
* ∂ℒ/∂w<sub>1</sub> = (∂ℒ/∂σ)(∂σ/∂z<sub>2</sub>)(∂z<sub>2</sub>/∂α)(∂α/∂z<sub>1</sub>)(∂z<sub>1</sub>/∂w<sub>1</sub>)

> ✅ Pravidlo reťazovej derivácie sa používa na výpočet derivácií stratovej funkcie vzhľadom na parametre.

Všimnite si, že ľavá časť všetkých týchto výrazov je rovnaká, a preto môžeme efektívne počítať derivácie začínajúc stratovou funkciou a postupujúc "späť" cez výpočtový graf. Preto sa metóda trénovania viacvrstvového perceptronu nazýva **spätná propagácia** alebo 'backprop'.

<img alt="výpočtový graf" src="images/ComputeGraphGrad.png"/>

> TODO: citácia obrázku

> ✅ Spätnú propagáciu si podrobnejšie preberieme v našom príklade v notebooku.  

## Záver

V tejto lekcii sme si vytvorili vlastnú knižnicu neurónových sietí a použili sme ju na jednoduchú dvojrozmernú klasifikačnú úlohu.

## 🚀 Výzva

V priloženom notebooku implementujete vlastný rámec na vytváranie a trénovanie viacvrstvových perceptronov. Budete môcť detailne vidieť, ako moderné neurónové siete fungujú.

Pokračujte do notebooku [OwnFramework](../../../../../lessons/3-NeuralNetworks/04-OwnFramework/OwnFramework.ipynb) a prejdite si ho.

## [Kvíz po prednáške](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/204)

## Prehľad a samoštúdium

Spätná propagácia je bežný algoritmus používaný v AI a ML, stojí za to ju [študovať podrobnejšie](https://wikipedia.org/wiki/Backpropagation).

## [Zadanie](lab/README.md)

V tomto laboratóriu máte za úlohu použiť rámec, ktorý ste vytvorili v tejto lekcii, na riešenie klasifikácie ručne písaných číslic MNIST.

* [Inštrukcie](lab/README.md)
* [Notebook](../../../../../lessons/3-NeuralNetworks/04-OwnFramework/lab/MyFW_MNIST.ipynb)

**Zrieknutie sa zodpovednosti**:  
Tento dokument bol preložený pomocou služby AI prekladu [Co-op Translator](https://github.com/Azure/co-op-translator). Aj keď sa snažíme o presnosť, prosím, berte na vedomie, že automatizované preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho rodnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nie sme zodpovední za žiadne nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.