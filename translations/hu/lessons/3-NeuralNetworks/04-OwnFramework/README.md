<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "186bf7eeab776b36f557357ea56d4751",
  "translation_date": "2025-08-25T23:44:27+00:00",
  "source_file": "lessons/3-NeuralNetworks/04-OwnFramework/README.md",
  "language_code": "hu"
}
-->
# Bevezetés a neurális hálózatokba. Többrétegű perceptron

Az előző részben megismerkedtél a legegyszerűbb neurális hálózati modellel – az egyrétegű perceptronnal, amely egy lineáris kétosztályos osztályozási modell.

Ebben a részben kiterjesztjük ezt a modellt egy rugalmasabb keretrendszerré, amely lehetővé teszi számunkra, hogy:

* **többosztályos osztályozást** végezzünk a kétosztályos osztályozás mellett
* **regressziós problémákat** oldjunk meg az osztályozás mellett
* olyan osztályokat különítsünk el, amelyek nem lineárisan elválaszthatók

Ezenkívül kifejlesztünk egy saját moduláris keretrendszert Pythonban, amely lehetővé teszi számunkra különböző neurális hálózati architektúrák létrehozását.

## [Előadás előtti kvíz](https://ff-quizzes.netlify.app/en/ai/quiz/7)

## A gépi tanulás formalizálása

Kezdjük a gépi tanulási probléma formalizálásával. Tegyük fel, hogy van egy **X** edzési adathalmazunk címkékkel **Y**, és egy olyan modellt kell építenünk, *f*, amely a lehető legpontosabb előrejelzéseket adja. Az előrejelzések minőségét a **veszteségfüggvény** ℒ méri. Az alábbi veszteségfüggvényeket gyakran használják:

* Regressziós problémák esetén, amikor egy számot kell megjósolnunk, használhatjuk az **abszolút hibát** ∑<sub>i</sub>|f(x<sup>(i)</sup>)-y<sup>(i)</sup>|, vagy a **négyzetes hibát** ∑<sub>i</sub>(f(x<sup>(i)</sup>)-y<sup>(i)</sup>)<sup>2</sup>
* Osztályozás esetén használjuk a **0-1 veszteséget** (ami lényegében a modell **pontosságával** egyenértékű), vagy a **logisztikus veszteséget**.

Az egyszintű perceptron esetében az *f* függvényt lineáris függvényként definiáltuk: *f(x)=wx+b* (ahol *w* a súlymátrix, *x* a bemeneti jellemzők vektora, és *b* az eltolási vektor). Különböző neurális hálózati architektúrák esetén ez a függvény bonyolultabb formát ölthet.

> Osztályozás esetén gyakran kívánatos, hogy a hálózat kimenete az osztályok valószínűségeit adja meg. Az önkényes számok valószínűségekké alakításához (pl. a kimenet normalizálásához) gyakran használjuk a **softmax** függvényt σ, és az *f* függvény *f(x)=σ(wx+b)* formát ölt.

Az *f* fenti definíciójában *w* és *b* az úgynevezett **paraméterek**, θ=⟨*w,b*⟩. Az ⟨**X**,**Y**⟩ adathalmaz alapján kiszámíthatjuk az egész adathalmazra vonatkozó összesített hibát a paraméterek θ függvényében.

> ✅ **A neurális hálózat tanításának célja a hiba minimalizálása a paraméterek θ változtatásával**

## Gradiensalapú optimalizálás

Létezik egy jól ismert függvényoptimalizálási módszer, az úgynevezett **gradiensmódszer**. Az ötlet az, hogy kiszámíthatjuk a veszteségfüggvény deriváltját (többdimenziós esetben **gradiensnek** nevezzük) a paraméterekre vonatkozóan, és úgy változtathatjuk a paramétereket, hogy a hiba csökkenjen. Ez a következőképpen formalizálható:

* Inicializáljuk a paramétereket véletlenszerű értékekkel: w<sup>(0)</sup>, b<sup>(0)</sup>
* Ismételjük meg az alábbi lépést sokszor:
    - w<sup>(i+1)</sup> = w<sup>(i)</sup>-η∂ℒ/∂w
    - b<sup>(i+1)</sup> = b<sup>(i)</sup>-η∂ℒ/∂b

A tanítás során az optimalizálási lépéseket az egész adathalmaz figyelembevételével kellene kiszámítani (emlékezzünk, hogy a veszteséget az összes edzési minta összegzéseként számítjuk ki). Azonban a valóságban az adathalmaz kis részeit, úgynevezett **minibatch-eket** vesszük, és a gradienseket az adatok egy részhalmazán alapulva számítjuk ki. Mivel a részhalmazt minden alkalommal véletlenszerűen választjuk ki, ezt a módszert **sztochasztikus gradiensmódszernek** (SGD) nevezzük.

## Többrétegű perceptronok és visszaterjesztés

Az egyrétegű hálózat, ahogy fentebb láttuk, képes lineárisan elválasztható osztályokat osztályozni. Gazdagabb modell létrehozásához több réteget kombinálhatunk a hálózatban. Matematikailag ez azt jelenti, hogy az *f* függvény bonyolultabb formát ölt, és több lépésben számítódik ki:
* z<sub>1</sub>=w<sub>1</sub>x+b<sub>1</sub>
* z<sub>2</sub>=w<sub>2</sub>α(z<sub>1</sub>)+b<sub>2</sub>
* f = σ(z<sub>2</sub>)

Itt α egy **nemlineáris aktivációs függvény**, σ egy softmax függvény, és a paraméterek θ=<*w<sub>1</sub>,b<sub>1</sub>,w<sub>2</sub>,b<sub>2</sub>*>.

A gradiensmódszer algoritmusa változatlan marad, de a gradiens kiszámítása bonyolultabbá válik. A láncszabály alapján a deriváltak a következőképpen számíthatók:

* ∂ℒ/∂w<sub>2</sub> = (∂ℒ/∂σ)(∂σ/∂z<sub>2</sub>)(∂z<sub>2</sub>/∂w<sub>2</sub>)
* ∂ℒ/∂w<sub>1</sub> = (∂ℒ/∂σ)(∂σ/∂z<sub>2</sub>)(∂z<sub>2</sub>/∂α)(∂α/∂z<sub>1</sub>)(∂z<sub>1</sub>/∂w<sub>1</sub>)

> ✅ A láncszabályt használjuk a veszteségfüggvény paraméterekre vonatkozó deriváltjainak kiszámításához.

Figyeljük meg, hogy ezeknek a kifejezéseknek a bal szélső része ugyanaz, így hatékonyan kiszámíthatjuk a deriváltakat a veszteségfüggvénytől kiindulva, és "visszafelé" haladva a számítási gráfon. Ezért a többrétegű perceptron tanításának módszerét **visszaterjesztésnek** (backpropagation), vagy röviden 'backprop'-nak nevezzük.

<img alt="számítási gráf" src="images/ComputeGraphGrad.png"/>

> TODO: kép forrásmegjelölés

> ✅ A visszaterjesztést sokkal részletesebben tárgyaljuk a notebook példánkban.  

## Összegzés

Ebben a leckében létrehoztuk saját neurális hálózati könyvtárunkat, és egy egyszerű kétdimenziós osztályozási feladatra használtuk.

## 🚀 Kihívás

A mellékelt notebookban megvalósítod saját keretrendszeredet többrétegű perceptronok építésére és tanítására. Részletesen megismerheted, hogyan működnek a modern neurális hálózatok.

Haladj tovább az [OwnFramework](../../../../../lessons/3-NeuralNetworks/04-OwnFramework/OwnFramework.ipynb) notebookhoz, és dolgozd át.

## [Előadás utáni kvíz](https://ff-quizzes.netlify.app/en/ai/quiz/8)

## Áttekintés és önálló tanulás

A visszaterjesztés egy gyakori algoritmus az AI és ML területén, érdemes [részletesebben tanulmányozni](https://wikipedia.org/wiki/Backpropagation).

## [Feladat](lab/README.md)

Ebben a laborban arra kérünk, hogy használd a leckében létrehozott keretrendszert az MNIST kézzel írt számjegyek osztályozásának megoldására.

* [Útmutató](lab/README.md)
* [Notebook](../../../../../lessons/3-NeuralNetworks/04-OwnFramework/lab/MyFW_MNIST.ipynb)

**Felelősség kizárása**:  
Ez a dokumentum az AI fordítási szolgáltatás [Co-op Translator](https://github.com/Azure/co-op-translator) segítségével lett lefordítva. Bár törekszünk a pontosságra, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az eredeti nyelvén tekintendő hiteles forrásnak. Kritikus információk esetén javasolt professzionális emberi fordítást igénybe venni. Nem vállalunk felelősséget semmilyen félreértésért vagy téves értelmezésért, amely a fordítás használatából eredhet.