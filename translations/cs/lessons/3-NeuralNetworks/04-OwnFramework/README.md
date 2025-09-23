<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "186bf7eeab776b36f557357ea56d4751",
  "translation_date": "2025-08-25T23:44:56+00:00",
  "source_file": "lessons/3-NeuralNetworks/04-OwnFramework/README.md",
  "language_code": "cs"
}
-->
# Úvod do neuronových sítí. Vícevrstvý perceptron

V předchozí části jste se seznámili s nejjednodušším modelem neuronové sítě – jednovrstvým perceptronem, což je lineární model pro dvoutřídovou klasifikaci.

V této části rozšíříme tento model na flexibilnější rámec, který nám umožní:

* provádět **vícetřídovou klasifikaci** kromě dvoutřídové
* řešit **regresní úlohy** kromě klasifikace
* oddělovat třídy, které nejsou lineárně separovatelné

Také vyvineme vlastní modulární rámec v Pythonu, který nám umožní vytvářet různé architektury neuronových sítí.

## [Kvíz před přednáškou](https://ff-quizzes.netlify.app/en/ai/quiz/7)

## Formalizace strojového učení

Začněme formalizací problému strojového učení. Předpokládejme, že máme trénovací dataset **X** s příslušnými štítky **Y**, a potřebujeme vytvořit model *f*, který bude poskytovat co nejpřesnější predikce. Kvalita predikcí se měří pomocí **ztrátové funkce** ℒ. Často se používají následující ztrátové funkce:

* Pro regresní úlohy, kdy potřebujeme předpovědět číslo, můžeme použít **absolutní chybu** ∑<sub>i</sub>|f(x<sup>(i)</sup>)-y<sup>(i)</sup>| nebo **kvadratickou chybu** ∑<sub>i</sub>(f(x<sup>(i)</sup>)-y<sup>(i)</sup>)<sup>2</sup>
* Pro klasifikaci používáme **0-1 ztrátu** (což je v podstatě totéž jako **přesnost** modelu) nebo **logistickou ztrátu**.

Pro jednovrstvý perceptron byla funkce *f* definována jako lineární funkce *f(x)=wx+b* (kde *w* je matice vah, *x* je vektor vstupních vlastností a *b* je vektor biasu). U různých architektur neuronových sítí může mít tato funkce složitější formu.

> V případě klasifikace je často žádoucí získat pravděpodobnosti odpovídajících tříd jako výstup sítě. K převodu libovolných čísel na pravděpodobnosti (např. k normalizaci výstupu) často používáme funkci **softmax** σ, a funkce *f* se stává *f(x)=σ(wx+b)*.

V definici *f* výše se *w* a *b* nazývají **parametry** θ=⟨*w,b*⟩. Na základě datasetu ⟨**X**,**Y**⟩ můžeme vypočítat celkovou chybu na celém datasetu jako funkci parametrů θ.

> ✅ **Cílem trénování neuronové sítě je minimalizovat chybu změnou parametrů θ**

## Optimalizace pomocí gradientního sestupu

Existuje známá metoda optimalizace funkcí nazvaná **gradientní sestup**. Myšlenka spočívá v tom, že můžeme vypočítat derivaci (v multidimenzionálním případě nazývanou **gradient**) ztrátové funkce vzhledem k parametrům a měnit parametry tak, aby se chyba snižovala. To lze formalizovat následovně:

* Inicializujte parametry náhodnými hodnotami w<sup>(0)</sup>, b<sup>(0)</sup>
* Opakujte následující krok mnohokrát:
    - w<sup>(i+1)</sup> = w<sup>(i)</sup>-η∂ℒ/∂w
    - b<sup>(i+1)</sup> = b<sup>(i)</sup>-η∂ℒ/∂b

Během trénování by měly být optimalizační kroky vypočítávány s ohledem na celý dataset (pamatujte, že ztráta se počítá jako součet přes všechny trénovací vzorky). V praxi však bereme malé části datasetu nazývané **minibatch** a počítáme gradienty na základě podmnožiny dat. Protože podmnožina je pokaždé vybírána náhodně, tato metoda se nazývá **stochastický gradientní sestup** (SGD).

## Vícevrstvé perceptrony a zpětné šíření

Jednovrstvá síť, jak jsme viděli výše, je schopna klasifikovat lineárně separovatelné třídy. Pro vytvoření bohatšího modelu můžeme kombinovat několik vrstev sítě. Matematicky by to znamenalo, že funkce *f* bude mít složitější formu a bude vypočítávána v několika krocích:
* z<sub>1</sub>=w<sub>1</sub>x+b<sub>1</sub>
* z<sub>2</sub>=w<sub>2</sub>α(z<sub>1</sub>)+b<sub>2</sub>
* f = σ(z<sub>2</sub>)

Zde je α **nelineární aktivační funkce**, σ je funkce softmax a parametry jsou θ=<*w<sub>1</sub>,b<sub>1</sub>,w<sub>2</sub>,b<sub>2</sub>*>.

Algoritmus gradientního sestupu zůstane stejný, ale výpočet gradientů bude složitější. Na základě pravidla řetězové derivace můžeme vypočítat derivace jako:

* ∂ℒ/∂w<sub>2</sub> = (∂ℒ/∂σ)(∂σ/∂z<sub>2</sub>)(∂z<sub>2</sub>/∂w<sub>2</sub>)
* ∂ℒ/∂w<sub>1</sub> = (∂ℒ/∂σ)(∂σ/∂z<sub>2</sub>)(∂z<sub>2</sub>/∂α)(∂α/∂z<sub>1</sub>)(∂z<sub>1</sub>/∂w<sub>1</sub>)

> ✅ Pravidlo řetězové derivace se používá k výpočtu derivací ztrátové funkce vzhledem k parametrům.

Všimněte si, že levá část všech těchto výrazů je stejná, a proto můžeme efektivně vypočítat derivace počínaje ztrátovou funkcí a postupovat "zpětně" skrz výpočetní graf. Proto se metoda trénování vícevrstvého perceptronu nazývá **zpětné šíření** nebo 'backprop'.

<img alt="výpočetní graf" src="images/ComputeGraphGrad.png"/>

> TODO: citace obrázku

> ✅ Zpětné šíření probereme mnohem podrobněji v našem příkladovém notebooku.  

## Závěr

V této lekci jsme vytvořili vlastní knihovnu neuronových sítí a použili ji pro jednoduchý dvourozměrný klasifikační úkol.

## 🚀 Výzva

V přiloženém notebooku implementujete vlastní rámec pro vytváření a trénování vícevrstvých perceptronů. Budete moci podrobně vidět, jak moderní neuronové sítě fungují.

Pokračujte do notebooku [OwnFramework](../../../../../lessons/3-NeuralNetworks/04-OwnFramework/OwnFramework.ipynb) a projděte si ho.

## [Kvíz po přednášce](https://ff-quizzes.netlify.app/en/ai/quiz/8)

## Přehled & Samostudium

Zpětné šíření je běžný algoritmus používaný v AI a ML, stojí za to ho [studovat podrobněji](https://wikipedia.org/wiki/Backpropagation).

## [Úkol](lab/README.md)

V tomto laboratorním cvičení máte za úkol použít rámec, který jste vytvořili v této lekci, k řešení klasifikace ručně psaných číslic MNIST.

* [Instrukce](lab/README.md)
* [Notebook](../../../../../lessons/3-NeuralNetworks/04-OwnFramework/lab/MyFW_MNIST.ipynb)

**Upozornění**:  
Tento dokument byl přeložen pomocí služby pro automatický překlad [Co-op Translator](https://github.com/Azure/co-op-translator). I když se snažíme o přesnost, mějte prosím na paměti, že automatické překlady mohou obsahovat chyby nebo nepřesnosti. Původní dokument v jeho původním jazyce by měl být považován za závazný zdroj. Pro důležité informace se doporučuje profesionální lidský překlad. Nezodpovídáme za jakékoli nedorozumění nebo nesprávné interpretace vyplývající z použití tohoto překladu.