# Mélytanulási Trükkök

Ahogy a neurális hálók egyre mélyebbé válnak, az edzésük folyamata egyre nehezebbé válik. Az egyik fő probléma az úgynevezett [eltűnő gradiens](https://en.wikipedia.org/wiki/Vanishing_gradient_problem) vagy [robbanó gradiens](https://deepai.org/machine-learning-glossary-and-terms/exploding-gradient-problem#:~:text=Exploding%20gradients%20are%20a%20problem,updates%20are%20small%20and%20controlled.). [Ez a bejegyzés](https://towardsdatascience.com/the-vanishing-exploding-gradient-problem-in-deep-neural-networks-191358470c11) jó bevezetést nyújt ezekhez a problémákhoz.

A mély hálók edzésének hatékonyabbá tétele érdekében néhány technikát alkalmazhatunk.

## Értékek ésszerű tartományban tartása

A numerikus számítások stabilabbá tétele érdekében biztosítani szeretnénk, hogy a neurális hálón belüli összes érték ésszerű skálán belül legyen, általában [-1..1] vagy [0..1]. Ez nem egy nagyon szigorú követelmény, de a lebegőpontos számítások természete olyan, hogy különböző nagyságrendű értékeket nem lehet pontosan együtt kezelni. Például, ha összeadjuk 10<sup>-10</sup>-et és 10<sup>10</sup>-et, valószínűleg 10<sup>10</sup>-et kapunk, mert a kisebb érték "átalakul" a nagyobb nagyságrendjére, és így a mantissza elveszik.

A legtöbb aktivációs függvény nemlinearitása [-1..1] körül van, ezért érdemes az összes bemeneti adatot [-1..1] vagy [0..1] tartományra skálázni.

## Kezdeti Súlyok Inicializálása

Ideális esetben azt szeretnénk, hogy az értékek ugyanabban a tartományban maradjanak, miután áthaladnak a háló rétegein. Ezért fontos a súlyokat úgy inicializálni, hogy megőrizzék az értékek eloszlását.

A normál eloszlás **N(0,1)** nem jó ötlet, mert ha *n* bemenetünk van, a kimenet szórása *n* lesz, és az értékek valószínűleg kiesnek a [0..1] tartományból.

Gyakran használt inicializálások:

 * Egyenletes eloszlás -- `uniform`
 * **N(0,1/n)** -- `gaussian`
 * **N(0,1/√n_in)** garantálja, hogy nullás középértékű és 1-es szórású bemenetek esetén ugyanaz a középérték/szórás maradjon
 * **N(0,√2/(n_in+n_out))** -- az úgynevezett **Xavier inicializálás** (`glorot`), amely segít az értékeket tartományban tartani mind előre-, mind visszafelé terjedés során

## Batch Normalizáció

Még megfelelő súlyinicializálás mellett is előfordulhat, hogy az edzés során a súlyok túl nagyok vagy túl kicsik lesznek, és ezáltal az értékek kikerülnek a megfelelő tartományból. Az értékeket vissza lehet hozni a megfelelő tartományba **normalizációs** technikák alkalmazásával. Bár több ilyen technika létezik (Súly normalizáció, Réteg normalizáció), a leggyakrabban használt a Batch Normalizáció.

A **batch normalizáció** ötlete az, hogy figyelembe vesszük az összes értéket a minibatch-ben, és normalizálást végzünk (azaz kivonjuk az átlagot és osztjuk a szórással) ezek alapján. Ez egy hálórétegként van implementálva, amely ezt a normalizálást végzi a súlyok alkalmazása után, de az aktivációs függvény előtt. Ennek eredményeként valószínűleg magasabb végső pontosságot és gyorsabb edzést érhetünk el.

Itt található az [eredeti tanulmány](https://arxiv.org/pdf/1502.03167.pdf) a batch normalizációról, a [magyarázat a Wikipédián](https://en.wikipedia.org/wiki/Batch_normalization), és [egy jó bevezető blogbejegyzés](https://towardsdatascience.com/batch-normalization-in-3-levels-of-understanding-14c2da90a338) (valamint egy [orosz nyelvű](https://habrahabr.ru/post/309302/)).

## Dropout

A **Dropout** egy érdekes technika, amely az edzés során véletlenszerűen eltávolítja a neuronok bizonyos százalékát. Ez egy rétegként van implementálva, amelynek egy paramétere van (az eltávolítandó neuronok százaléka, általában 10%-50%), és az edzés során véletlenszerűen nullázza a bemeneti vektor elemeit, mielőtt továbbadná a következő rétegnek.

Bár ez furcsának tűnhet, a dropout hatását láthatjuk az MNIST számjegyosztályozó edzésén a [`Dropout.ipynb`](../../../../../lessons/4-ComputerVision/08-TransferLearning/Dropout.ipynb) jegyzetfüzetben. Gyorsítja az edzést, és lehetővé teszi, hogy kevesebb edzési epoch alatt magasabb pontosságot érjünk el.

Ez a hatás többféleképpen magyarázható:

 * Tekinthetjük úgy, mint egy véletlenszerű sokkoló tényezőt a modell számára, amely kimozdítja az optimalizációt a lokális minimumból
 * Tekinthetjük úgy, mint *implicit modellátlagolást*, mert mondhatjuk, hogy a dropout során kissé eltérő modellt edzünk

> *Egyesek azt mondják, hogy amikor egy részeg ember próbál valamit megtanulni, másnap reggel jobban emlékszik rá, mint egy józan ember, mert az agy, amelyben néhány neuron nem működik megfelelően, jobban alkalmazkodik a jelentés megragadásához. Mi soha nem teszteltük, hogy ez igaz-e vagy sem.*

## Túltanulás Megelőzése

A mélytanulás egyik nagyon fontos aspektusa, hogy képesek legyünk megelőzni a [túltanulást](../../3-NeuralNetworks/05-Frameworks/Overfitting.md). Bár csábító lehet nagyon erős neurális háló modellt használni, mindig egyensúlyban kell tartanunk a modell paramétereinek számát a tanító minták számával.

> Győződj meg róla, hogy megérted a [túltanulás](../../3-NeuralNetworks/05-Frameworks/Overfitting.md) fogalmát, amelyet korábban bemutattunk!

Több módszer létezik a túltanulás megelőzésére:

 * Korai leállítás -- folyamatosan figyeljük a validációs halmaz hibáját, és leállítjuk az edzést, amikor a validációs hiba növekedni kezd.
 * Explicit Súlycsökkenés / Regularizáció -- extra büntetést adunk a veszteségfüggvényhez a súlyok magas abszolút értékeiért, ami megakadályozza, hogy a modell nagyon instabil eredményeket adjon
 * Modellátlagolás -- több modellt edzünk, majd átlagoljuk az eredményt. Ez segít minimalizálni a varianciát.
 * Dropout (Implicit Modellátlagolás)

## Optimalizálók / Edzési Algoritmusok

Az edzés másik fontos aspektusa a megfelelő edzési algoritmus kiválasztása. Bár a klasszikus **gradiens csökkenés** ésszerű választás, néha túl lassú lehet, vagy más problémákhoz vezethet.

A mélytanulásban **Stochasztikus Gradiens Csökkenést** (SGD) használunk, amely a gradiens csökkenést alkalmazza a tanító halmazból véletlenszerűen kiválasztott minibatch-ekre. A súlyokat az alábbi képlet szerint állítjuk be:

w<sup>t+1</sup> = w<sup>t</sup> - η∇ℒ

### Momentum

A **momentum SGD**-ben megtartunk egy részt az előző lépések gradienséből. Ez hasonló ahhoz, amikor valahová tehetetlenséggel mozgunk, és kapunk egy ütést egy másik irányba, a pályánk nem változik meg azonnal, hanem megtartja az eredeti mozgás egy részét. Itt bevezetünk egy másik vektort, v-t, amely a *sebességet* képviseli:

* v<sup>t+1</sup> = γ v<sup>t</sup> - η∇ℒ
* w<sup>t+1</sup> = w<sup>t</sup>+v<sup>t+1</sup>

Itt a γ paraméter jelzi, hogy mennyire vesszük figyelembe a tehetetlenséget: γ=0 megfelel a klasszikus SGD-nek; γ=1 egy tiszta mozgásegyenlet.

### Adam, Adagrad, stb.

Mivel minden rétegben szignálokat szorzunk egy W<sub>i</sub> mátrixszal, a ||W<sub>i</sub>|| függvényében a gradiens vagy csökkenhet és közel 0 lehet, vagy végtelenül növekedhet. Ez a Robbanó/Eltűnő Gradiens probléma lényege.

Az egyik megoldás erre a problémára az, hogy csak a gradiens irányát használjuk az egyenletben, és figyelmen kívül hagyjuk az abszolút értéket, azaz:

w<sup>t+1</sup> = w<sup>t</sup> - η(∇ℒ/||∇ℒ||), ahol ||∇ℒ|| = √∑(∇ℒ)<sup>2</sup>

Ezt az algoritmust **Adagrad**-nak hívják. Más algoritmusok, amelyek ugyanazt az ötletet használják: **RMSProp**, **Adam**

> **Adam**-ot sok alkalmazásban nagyon hatékony algoritmusnak tartják, így ha nem vagy biztos benne, melyiket használd - válaszd az Adam-et.

### Gradiens vágás

A gradiens vágás az előző ötlet kiterjesztése. Amikor ||∇ℒ|| ≤ θ, az eredeti gradiens-t vesszük figyelembe a súlyoptimalizálásban, és amikor ||∇ℒ|| > θ - osztjuk a gradiens-t a normájával. Itt θ egy paraméter, a legtöbb esetben θ=1 vagy θ=10 értéket vehetünk.

### Tanulási ráta csökkentése

Az edzés sikere gyakran a tanulási ráta paraméter η-tól függ. Logikus feltételezni, hogy a nagyobb η értékek gyorsabb edzést eredményeznek, amit általában az edzés elején szeretnénk, majd kisebb η értékek lehetővé teszik a háló finomhangolását. Ezért a legtöbb esetben szeretnénk csökkenteni η-t az edzés folyamata során.

Ez úgy történhet, hogy η-t megszorozzuk egy számmal (pl. 0.98) minden edzési epoch után, vagy bonyolultabb **tanulási ráta ütemezést** használunk.

## Különböző Hálózati Architektúrák

A megfelelő hálózati architektúra kiválasztása a problémádhoz trükkös lehet. Általában olyan architektúrát választunk, amely bizonyítottan működik a konkrét feladatunkhoz (vagy hasonlóhoz). Itt van egy [jó áttekintés](https://www.topbots.com/a-brief-history-of-neural-network-architectures/) a számítógépes látás neurális hálózati architektúráiról.

> Fontos olyan architektúrát választani, amely elég erős lesz a rendelkezésre álló tanító minták számához. Túl erős modell kiválasztása [túltanuláshoz](../../3-NeuralNetworks/05-Frameworks/Overfitting.md) vezethet.

Egy másik jó megoldás olyan architektúra használata, amely automatikusan alkalmazkodik a szükséges komplexitáshoz. Bizonyos mértékig a **ResNet** architektúra és az **Inception** önállóan alkalmazkodó. [További információ a számítógépes látás architektúrákról](../07-ConvNets/CNN_Architectures.md).

**Felelősség kizárása**:  
Ez a dokumentum az AI fordítási szolgáltatás [Co-op Translator](https://github.com/Azure/co-op-translator) segítségével lett lefordítva. Bár igyekszünk pontosságra törekedni, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az eredeti nyelvén tekintendő hiteles forrásnak. Kritikus információk esetén javasolt professzionális emberi fordítást igénybe venni. Nem vállalunk felelősséget semmilyen félreértésért vagy téves értelmezésért, amely a fordítás használatából eredhet.