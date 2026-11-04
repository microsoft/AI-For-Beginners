# Tipy pro trénink hlubokého učení

Jak se neuronové sítě stávají hlubšími, proces jejich tréninku se stává čím dál náročnějším. Jedním z hlavních problémů jsou takzvané [mizící gradienty](https://en.wikipedia.org/wiki/Vanishing_gradient_problem) nebo [explodující gradienty](https://deepai.org/machine-learning-glossary-and-terms/exploding-gradient-problem#:~:text=Exploding%20gradients%20are%20a%20problem,updates%20are%20small%20and%20controlled.). [Tento příspěvek](https://towardsdatascience.com/the-vanishing-exploding-gradient-problem-in-deep-neural-networks-191358470c11) nabízí dobrý úvod do těchto problémů.

Pro efektivnější trénink hlubokých sítí existuje několik technik, které lze použít.

## Udržování hodnot v rozumném rozsahu

Abychom zajistili stabilnější číselné výpočty, chceme mít všechny hodnoty v naší neuronové síti v rozumném měřítku, obvykle [-1..1] nebo [0..1]. Není to velmi přísný požadavek, ale povaha výpočtů s plovoucí desetinnou čárkou je taková, že hodnoty různých velikostí nelze přesně manipulovat společně. Například pokud sečteme 10<sup>-10</sup> a 10<sup>10</sup>, pravděpodobně dostaneme 10<sup>10</sup>, protože menší hodnota bude „převedena“ na stejný řád jako ta větší, a ztrácí se tedy mantisa.

Většina aktivačních funkcí má nelinearity kolem [-1..1], a proto dává smysl škálovat všechna vstupní data do intervalu [-1..1] nebo [0..1].

## Počáteční inicializace vah

Ideálně chceme mít hodnoty ve stejném rozsahu i po průchodu vrstvami sítě. Je proto důležité inicializovat váhy tak, aby byla zachována distribuce hodnot.

Normální rozdělení **N(0,1)** není dobrý nápad, protože pokud máme *n* vstupů, směrodatná odchylka výstupu by byla *&radic;n*, a hodnoty by pravděpodobně vybočily z intervalu [0..1].

Často používané inicializace jsou:

 * Rovnoměrné rozdělení -- `uniform`
 * **N(0,1/n)** -- `gaussian`
 * **N(0,1/&radic;n_in)** zaručuje, že pro vstupy s nulovým průměrem a směrodatnou odchylkou 1 zůstane stejný průměr/směrodatná odchylka
 * **N(0,&radic;2/(n_in+n_out))** -- tzv. **Xavier inicializace** (`glorot`), pomáhá udržovat signály v rozsahu během jak průchodu dopředu, tak zpětnou propagací

## Normalizace batchů (Batch Normalization)

I při správné inicializaci vah mohou být váhy během tréninku libovolně velké nebo malé, což může vyvést signály mimo správný rozsah. Signály můžeme vrátit zpět pomocí jedné z technik **normalizace**. Existuje jich několik (normalizace vah, normalizace vrstev), ale nejčastěji používaná je Batch Normalization.

Myšlenka **batch normalization** je vzít v úvahu všechny hodnoty v mini-batche a provést normalizaci (tj. odečíst průměr a vydělit směrodatnou odchylkou) na základě těchto hodnot. Je implementována jako vrstva v síti, která normalizuje po aplikaci vah, ale před aktivační funkcí. Výsledkem je pravděpodobně vyšší konečná přesnost a rychlejší trénink.

Zde je [originální článek](https://arxiv.org/pdf/1502.03167.pdf) o batch normalization, [vysvětlení na Wikipedii](https://en.wikipedia.org/wiki/Batch_normalization) a [dobrý úvodní blogový příspěvek](https://towardsdatascience.com/batch-normalization-in-3-levels-of-understanding-14c2da90a338) (a jeden [v ruštině](https://habrahabr.ru/post/309302/)).

## Dropout

**Dropout** je zajímavá technika, která během tréninku náhodně odstraní určité procento neuronů. Je také implementována jako vrstva s jedním parametrem (procento neuronů k odstranění, obvykle 10%-50%), a během tréninku nuluje náhodné prvky vstupního vektoru před tím, než ho předá další vrstvě.

Ačkoliv to může znít jako zvláštní nápad, efekt dropoutu při tréninku klasifikátoru číslic MNIST můžete vidět v poznámkovém bloku [`Dropout.ipynb`](Dropout.ipynb). Zrychluje trénink a umožňuje dosáhnout vyšší přesnosti s menším počtem epoch.

Tento efekt lze vysvětlit různými způsoby:

 * Lze ho považovat za náhodný šokující faktor pro model, který ho vytahuje z lokálního minima optimalizace
 * Lze ho považovat za *implicitní průměrování modelu*, protože lze říci, že během dropoutu trénujeme mírně odlišný model

> *Někteří lidé říkají, že když se opilý člověk snaží něco naučit, ráno si to lépe zapamatuje než střízlivý člověk, protože mozek s chybujícím neuronem se lépe snaží přizpůsobit a pochopit význam. Sami jsme to nikdy neověřili, zda je to pravda nebo ne.*

## Prevence přeučení

Jedním z velmi důležitých aspektů hlubokého učení je schopnost zabránit [přeučení](../../3-NeuralNetworks/05-Frameworks/Overfitting.md). I když by mohlo být lákavé použít vysoce výkonný model neuronové sítě, vždy bychom měli vyvážit počet parametrů modelu s počtem tréninkových vzorků.

> Ujistěte se, že rozumíte konceptu [přeučení](../../3-NeuralNetworks/05-Frameworks/Overfitting.md), který jsme dříve uvedli!

Existuje několik způsobů, jak zabránit přeučení:

 * Předčasné zastavení -- neustále sledovat chybu na validační sadě a zastavit trénink, když se validační chyba začne zvyšovat.
 * Explicitní úbytek vah / regularizace -- přidání další penalizace do ztrátové funkce za vysoké absolutní hodnoty vah, což zabraňuje příliš nestabilním výsledkům modelu
 * Průměrování modelů -- trénování více modelů a průměrování výsledků. Pomáhá to minimalizovat rozptyl.
 * Dropout (implicitní průměrování modelů)

## Optimalizátory / tréninkové algoritmy

Dalším důležitým aspektem tréninku je výběr vhodného tréninkového algoritmu. Zatímco klasický **gradientní sestup** je rozumnou volbou, může být někdy příliš pomalý nebo způsobovat jiné problémy.

V hlubokém učení používáme **stochastický gradientní sestup** (SGD), což je gradientní sestup aplikovaný na minibatche náhodně vybraných z tréninkové sady. Váhy se upravují podle tohoto vzorce:

w<sup>t+1</sup> = w<sup>t</sup> - &eta;&nabla;&lagran;

### Momentum

V **momentum SGD** si uchováváme část gradientu z předchozích kroků. Je to podobné jako když se pohybujeme s setrvačností a dostaneme ránu do jiného směru; naše trajektorie se okamžitě nezmění, ale drží si část původního pohybu. Zde zavádíme další vektor v, který představuje *rychlost*:

* v<sup>t+1</sup> = &gamma; v<sup>t</sup> - &eta;&nabla;&lagran;
* w<sup>t+1</sup> = w<sup>t</sup>+v<sup>t+1</sup>

Parametr &gamma; zde určuje, do jaké míry bereme setrvačnost v úvahu: &gamma;=0 odpovídá klasickému SGD; &gamma;=1 je čistá rovnice pohybu.

### Adam, Adagrad atd.

Také protože v každé vrstvě násobíme signály nějakou maticí W<sub>i</sub>, v závislosti na ||W<sub>i</sub>|| může gradient buď klesat a být blízký nule, nebo růst do nekonečna. To je podstata problému explodujících/mizících gradientů.

Jedním z řešení tohoto problému je použít pouze směr gradientu ve vzorci a ignorovat jeho absolutní hodnotu, tj.

w<sup>t+1</sup> = w<sup>t</sup> - &eta;(&nabla;&lagran;/||&nabla;&lagran;||), kde ||&nabla;&lagran;|| = &radic;&sum;(&nabla;&lagran;)<sup>2</sup>

Tento algoritmus se nazývá **Adagrad**. Další algoritmy používající stejný princip jsou: **RMSProp**, **Adam**

> **Adam** je považován za velmi efektivní algoritmus pro mnoho aplikací, takže pokud si nejste jisti, který použít - použijte Adam.

### Ořezávání gradientu (Gradient clipping)

Ořezávání gradientu je rozšíření výše uvedené myšlenky. Když ||&nabla;&lagran;|| &le; &theta;, považujeme gradient za původní při optimalizaci vah, a když ||&nabla;&lagran;|| > &theta;, gradient dělíme jeho normou. Zde je &theta; parametr, většinou lze brát &theta;=1 nebo &theta;=10.

### Snižování rychlosti učení

Úspěšnost tréninku často závisí na parametru rychlosti učení &eta;. Je logické předpokládat, že větší hodnoty &eta; vedou k rychlejšímu tréninku, což obvykle chceme na začátku tréninku, a pak menší hodnoty &eta; nám umožní síť lépe doladit. Proto v většině případů chceme během tréninku hodnotu &eta; snižovat.

To lze udělat násobením &eta; nějakým číslem (např. 0,98) po každé epoše tréninku nebo použitím složitějšího **plánu snižování rychlosti učení**.

## Různé architektury sítí

Výběr správné architektury sítě pro váš problém může být složitý. Obvykle zvolíme architekturu, která se osvědčila pro náš konkrétní úkol (nebo podobný). Zde je [dobrý přehled](https://www.topbots.com/a-brief-history-of-neural-network-architectures/) architektur neuronových sítí pro počítačové vidění.

> Je důležité vybrat architekturu, která bude dostatečně výkonná vzhledem k počtu tréninkových vzorků, které máme. Výběr příliš výkonného modelu může vést k [přeučení](../../3-NeuralNetworks/05-Frameworks/Overfitting.md)

Jinou dobrou cestou je použít architekturu, která se automaticky přizpůsobí požadované složitosti. Do jisté míry jsou **ResNet** a **Inception** architektury, které se samy přizpůsobují. [Více o architekturách pro počítačové vidění](../07-ConvNets/CNN_Architectures.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Prohlášení o omezení odpovědnosti**:
Tento dokument byl přeložen pomocí AI překladatelské služby [Co-op Translator](https://github.com/Azure/co-op-translator). Přestože usilujeme o co největší přesnost, mějte prosím na paměti, že automatizované překlady mohou obsahovat chyby nebo nepřesnosti. Originální dokument v jeho mateřském jazyce by měl být považován za autoritativní zdroj. Pro kritické informace se doporučuje profesionální lidský překlad. Nejsme odpovědní za jakékoli nedorozumění nebo nesprávné interpretace vzniklé použitím tohoto překladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->