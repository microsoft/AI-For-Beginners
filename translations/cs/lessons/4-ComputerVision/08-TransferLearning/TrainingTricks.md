# Triky pro trénování hlubokého učení

Jak se neuronové sítě stávají hlubšími, proces jejich trénování se stává stále náročnějším. Jedním z hlavních problémů jsou tzv. [mizící gradienty](https://en.wikipedia.org/wiki/Vanishing_gradient_problem) nebo [explodující gradienty](https://deepai.org/machine-learning-glossary-and-terms/exploding-gradient-problem#:~:text=Exploding%20gradients%20are%20a%20problem,updates%20are%20small%20and%20controlled.). [Tento článek](https://towardsdatascience.com/the-vanishing-exploding-gradient-problem-in-deep-neural-networks-191358470c11) poskytuje dobrý úvod do těchto problémů.

Aby bylo trénování hlubokých sítí efektivnější, existuje několik technik, které lze použít.

## Udržování hodnot v rozumném intervalu

Aby byly numerické výpočty stabilnější, chceme zajistit, že všechny hodnoty v naší neuronové síti budou v rozumném měřítku, obvykle [-1..1] nebo [0..1]. Není to příliš přísný požadavek, ale povaha výpočtů s plovoucí desetinnou čárkou je taková, že hodnoty různých velikostí nelze přesně manipulovat společně. Například pokud sečteme 10<sup>-10</sup> a 10<sup>10</sup>, pravděpodobně dostaneme 10<sup>10</sup>, protože menší hodnota bude „převedena“ na stejný řád jako větší, a tím se ztratí mantisa.

Většina aktivačních funkcí má nelinearity kolem [-1..1], a proto má smysl škálovat všechna vstupní data do intervalu [-1..1] nebo [0..1].

## Inicializace počátečních vah

Ideálně chceme, aby hodnoty zůstaly ve stejném rozsahu po průchodu vrstvami sítě. Proto je důležité inicializovat váhy tak, aby zachovaly rozložení hodnot.

Normální rozložení **N(0,1)** není dobrý nápad, protože pokud máme *n* vstupů, standardní odchylka výstupu bude *n*, a hodnoty pravděpodobně vyskočí z intervalu [0..1].

Často se používají následující inicializace:

 * Rovnoměrné rozložení -- `uniform`
 * **N(0,1/n)** -- `gaussian`
 * **N(0,1/√n_in)** zaručuje, že pro vstupy s nulovou střední hodnotou a standardní odchylkou 1 zůstane stejná střední hodnota/standardní odchylka
 * **N(0,√2/(n_in+n_out))** -- tzv. **Xavierova inicializace** (`glorot`), která pomáhá udržet signály v rozsahu během předního i zpětného šíření

## Normalizace batchů

I při správné inicializaci vah se mohou váhy během trénování stát libovolně velkými nebo malými, což vyvede signály z požadovaného rozsahu. Signály můžeme vrátit zpět pomocí jedné z technik **normalizace**. Zatímco existuje několik z nich (normalizace vah, normalizace vrstev), nejčastěji používaná je normalizace batchů.

Myšlenka **normalizace batchů** spočívá v tom, že vezmeme v úvahu všechny hodnoty napříč minibatchem a provedeme normalizaci (tj. odečteme střední hodnotu a vydělíme standardní odchylkou) na základě těchto hodnot. Je implementována jako vrstva sítě, která provádí tuto normalizaci po aplikaci vah, ale před aktivační funkcí. Výsledkem je pravděpodobně vyšší konečná přesnost a rychlejší trénování.

Zde je [původní článek](https://arxiv.org/pdf/1502.03167.pdf) o normalizaci batchů, [vysvětlení na Wikipedii](https://en.wikipedia.org/wiki/Batch_normalization) a [dobrý úvodní blogový příspěvek](https://towardsdatascience.com/batch-normalization-in-3-levels-of-understanding-14c2da90a338) (a jeden [v ruštině](https://habrahabr.ru/post/309302/)).

## Dropout

**Dropout** je zajímavá technika, která během trénování odstraňuje určité procento náhodných neuronů. Je také implementována jako vrstva s jedním parametrem (procento neuronů k odstranění, obvykle 10%-50%), a během trénování nuluje náhodné prvky vstupního vektoru, než je předá do další vrstvy.

I když to může znít jako zvláštní nápad, můžete vidět efekt dropout na trénování klasifikátoru číslic MNIST v notebooku [`Dropout.ipynb`](../../../../../lessons/4-ComputerVision/08-TransferLearning/Dropout.ipynb). Zrychluje trénování a umožňuje dosáhnout vyšší přesnosti v méně epochách.

Tento efekt lze vysvětlit několika způsoby:

 * Může být považován za náhodný šokový faktor pro model, který vyvede optimalizaci z lokálního minima
 * Může být považován za *implicitní průměrování modelu*, protože můžeme říci, že během dropout trénujeme mírně odlišný model

> *Někteří lidé říkají, že když se opilý člověk snaží něco naučit, zapamatuje si to lépe následující ráno ve srovnání se střízlivým člověkem, protože mozek s některými nefunkčními neurony se snaží lépe přizpůsobit a pochopit význam. Nikdy jsme sami netestovali, zda je to pravda.*

## Prevence přeučení

Jedním z velmi důležitých aspektů hlubokého učení je schopnost zabránit [přeučení](../../3-NeuralNetworks/05-Frameworks/Overfitting.md). I když může být lákavé použít velmi výkonný model neuronové sítě, měli bychom vždy vyvážit počet parametrů modelu s počtem trénovacích vzorků.

> Ujistěte se, že rozumíte konceptu [přeučení](../../3-NeuralNetworks/05-Frameworks/Overfitting.md), který jsme představili dříve!

Existuje několik způsobů, jak zabránit přeučení:

 * Předčasné zastavení -- průběžné sledování chyby na validační sadě a zastavení trénování, když validační chyba začne růst.
 * Explicitní úbytek vah / Regularizace -- přidání dodatečné penalizace do ztrátové funkce za vysoké absolutní hodnoty vah, což zabraňuje modelu dosáhnout velmi nestabilních výsledků
 * Průměrování modelu -- trénování několika modelů a následné průměrování výsledků. To pomáhá minimalizovat rozptyl.
 * Dropout (Implicitní průměrování modelu)

## Optimalizátory / Trénovací algoritmy

Dalším důležitým aspektem trénování je výběr dobrého trénovacího algoritmu. Zatímco klasický **gradientní sestup** je rozumnou volbou, může být někdy příliš pomalý nebo způsobovat jiné problémy.

V hlubokém učení používáme **Stochastický gradientní sestup** (SGD), což je gradientní sestup aplikovaný na minibatche, náhodně vybrané z trénovací sady. Váhy se upravují podle tohoto vzorce:

w<sup>t+1</sup> = w<sup>t</sup> - η∇ℒ

### Momentum

V **momentum SGD** uchováváme část gradientu z předchozích kroků. Je to podobné jako když se pohybujeme někam s setrvačností, a dostaneme ránu jiným směrem, naše trajektorie se nezmění okamžitě, ale zachová část původního pohybu. Zde zavádíme další vektor v, který reprezentuje *rychlost*:

* v<sup>t+1</sup> = γ v<sup>t</sup> - η∇ℒ
* w<sup>t+1</sup> = w<sup>t</sup>+v<sup>t+1</sup>

Parametr γ zde určuje, do jaké míry bereme setrvačnost v úvahu: γ=0 odpovídá klasickému SGD; γ=1 je čistá pohybová rovnice.

### Adam, Adagrad, atd.

Protože v každé vrstvě násobíme signály nějakou maticí W<sub>i</sub>, v závislosti na ||W<sub>i</sub>|| může gradient buď mizet a být blízko 0, nebo růst neomezeně. To je podstata problému Explodujících/Mizících Gradientů.

Jedním z řešení tohoto problému je použít pouze směr gradientu ve vzorci a ignorovat absolutní hodnotu, tj.

w<sup>t+1</sup> = w<sup>t</sup> - η(∇ℒ/||∇ℒ||), kde ||∇ℒ|| = √∑(∇ℒ)<sup>2</sup>

Tento algoritmus se nazývá **Adagrad**. Další algoritmy, které používají stejnou myšlenku: **RMSProp**, **Adam**

> **Adam** je považován za velmi efektivní algoritmus pro mnoho aplikací, takže pokud si nejste jisti, který použít - použijte Adam.

### Ořezávání gradientu

Ořezávání gradientu je rozšíření výše uvedené myšlenky. Když ||∇ℒ|| ≤ θ, uvažujeme původní gradient při optimalizaci vah, a když ||∇ℒ|| > θ - dělíme gradient jeho normou. Zde je θ parametr, ve většině případů můžeme vzít θ=1 nebo θ=10.

### Úbytek rychlosti učení

Úspěch trénování často závisí na parametru rychlosti učení η. Je logické předpokládat, že větší hodnoty η vedou k rychlejšímu trénování, což je něco, co obvykle chceme na začátku trénování, a poté menší hodnoty η umožňují jemné doladění sítě. Proto ve většině případů chceme během trénování snižovat η.

To lze provést násobením η nějakým číslem (např. 0,98) po každé epoše trénování, nebo použitím složitějšího **plánu rychlosti učení**.

## Různé architektury sítí

Výběr správné architektury sítě pro váš problém může být složitý. Obvykle bychom zvolili architekturu, která se osvědčila pro náš konkrétní úkol (nebo podobný). Zde je [dobrý přehled](https://www.topbots.com/a-brief-history-of-neural-network-architectures/) architektur neuronových sítí pro počítačové vidění.

> Je důležité zvolit architekturu, která bude dostatečně výkonná pro počet trénovacích vzorků, které máme. Výběr příliš výkonného modelu může vést k [přeučení](../../3-NeuralNetworks/05-Frameworks/Overfitting.md).

Dalším dobrým způsobem by bylo použít architekturu, která se automaticky přizpůsobí požadované složitosti. Do určité míry jsou architektury **ResNet** a **Inception** samopřizpůsobivé. [Více o architekturách pro počítačové vidění](../07-ConvNets/CNN_Architectures.md).

**Prohlášení:**  
Tento dokument byl přeložen pomocí služby pro automatický překlad [Co-op Translator](https://github.com/Azure/co-op-translator). Ačkoli se snažíme o přesnost, mějte prosím na paměti, že automatické překlady mohou obsahovat chyby nebo nepřesnosti. Původní dokument v jeho původním jazyce by měl být považován za autoritativní zdroj. Pro důležité informace se doporučuje profesionální lidský překlad. Neodpovídáme za žádná nedorozumění nebo nesprávné interpretace vyplývající z použití tohoto překladu.