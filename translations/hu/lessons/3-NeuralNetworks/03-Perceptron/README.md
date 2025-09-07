<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "0c37770bba4fff3c71dc00eb261ee61b",
  "translation_date": "2025-08-25T23:56:31+00:00",
  "source_file": "lessons/3-NeuralNetworks/03-Perceptron/README.md",
  "language_code": "hu"
}
-->
# Bevezetés a neurális hálózatokba: Perceptron

## [Előadás előtti kvíz](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/103)

Az egyik első próbálkozás egy modern neurális hálózathoz hasonló rendszer megvalósítására Frank Rosenblatt nevéhez fűződik, aki 1957-ben a Cornell Aeronautical Laboratory-nál dolgozott. Ez egy hardveres megvalósítás volt, amelyet "Mark-1"-nek neveztek, és amelyet egyszerű geometriai alakzatok, például háromszögek, négyzetek és körök felismerésére terveztek.

|      |      |
|--------------|-----------|
|<img src='images/Rosenblatt-wikipedia.jpg' alt='Frank Rosenblatt'/> | <img src='images/Mark_I_perceptron_wikipedia.jpg' alt='A Mark 1 Perceptron' />|

> Képek [a Wikipédiáról](https://en.wikipedia.org/wiki/Perceptron)

A bemeneti képet egy 20x20-as fotocella mátrix reprezentálta, így a neurális hálózatnak 400 bemenete és egy bináris kimenete volt. Egy egyszerű hálózat egyetlen neuront tartalmazott, amelyet **küszöblogikai egységnek** is neveztek. A neurális hálózat súlyai potenciométerekként működtek, amelyeket a tanítási fázis során manuálisan kellett beállítani.

> ✅ A potenciométer egy olyan eszköz, amely lehetővé teszi az áramkör ellenállásának beállítását.

> A New York Times akkoriban így írt a perceptronról: *az elektronikus számítógép embriója, amelyről [a haditengerészet] azt várja, hogy képes lesz járni, beszélni, látni, írni, önmagát reprodukálni és tudatában lenni saját létezésének.*

## Perceptron modell

Tegyük fel, hogy a modellünkben N jellemző van, ebben az esetben a bemeneti vektor egy N méretű vektor lesz. A perceptron egy **bináris osztályozási** modell, azaz két osztály közötti különbségtételre képes. Feltételezzük, hogy minden bemeneti vektor x esetén a perceptron kimenete +1 vagy -1 lesz, az osztálytól függően. A kimenetet a következő képlettel számítjuk ki:

y(x) = f(w<sup>T</sup>x)

ahol f egy lépés aktivációs függvény

<!-- img src="http://www.sciweavers.org/tex2img.php?eq=f%28x%29%20%3D%20%5Cbegin%7Bcases%7D%0A%20%20%20%20%20%20%20%20%20%2B1%20%26%20x%20%5Cgeq%200%20%5C%5C%0A%20%20%20%20%20%20%20%20%20-1%20%26%20x%20%3C%200%0A%20%20%20%20%20%20%20%5Cend%7Bcases%7D%20%5C%5C%0A&bc=White&fc=Black&im=jpg&fs=12&ff=arev&edit=0" align="center" border="0" alt="f(x) = \begin{cases} +1 & x \geq 0 \\ -1 & x < 0 \end{cases} \\" width="154" height="50" / -->
<img src="images/activation-func.png"/>

## A perceptron tanítása

A perceptron tanításához meg kell találnunk egy w súlyvektort, amely a legtöbb értéket helyesen osztályozza, azaz a legkisebb **hibát** eredményezi. Ezt a hibát E a **perceptron kritérium** határozza meg a következő módon:

E(w) = -∑w<sup>T</sup>x<sub>i</sub>t<sub>i</sub>

ahol:

* az összegzés azon tanítási adatok i pontjaira vonatkozik, amelyek helytelen osztályozást eredményeznek
* x<sub>i</sub> a bemeneti adat, és t<sub>i</sub> -1 vagy +1 a negatív és pozitív példák esetén.

Ezt a kritériumot a w súlyok függvényeként tekintjük, és minimalizálnunk kell. Gyakran egy **gradiens csökkenés** nevű módszert alkalmaznak, amelyben kezdeti w<sup>(0)</sup> súlyokkal indulunk, majd minden lépésben a következő képlet szerint frissítjük a súlyokat:

w<sup>(t+1)</sup> = w<sup>(t)</sup> - η∇E(w)

Itt η az úgynevezett **tanulási ráta**, és ∇E(w) az E **gradiensét** jelöli. A gradiens kiszámítása után a következőképpen alakul:

w<sup>(t+1)</sup> = w<sup>(t)</sup> + ∑ηx<sub>i</sub>t<sub>i</sub>

Az algoritmus Pythonban így néz ki:

```python
def train(positive_examples, negative_examples, num_iterations = 100, eta = 1):

    weights = [0,0,0] # Initialize weights (almost randomly :)
        
    for i in range(num_iterations):
        pos = random.choice(positive_examples)
        neg = random.choice(negative_examples)

        z = np.dot(pos, weights) # compute perceptron output
        if z < 0: # positive example classified as negative
            weights = weights + eta*weights.shape

        z  = np.dot(neg, weights)
        if z >= 0: # negative example classified as positive
            weights = weights - eta*weights.shape

    return weights
```

## Összegzés

Ebben a leckében megismerkedtél a perceptronnal, amely egy bináris osztályozási modell, és megtanultad, hogyan lehet azt egy súlyvektor segítségével tanítani.

## 🚀 Kihívás

Ha szeretnéd kipróbálni egy saját perceptron létrehozását, próbáld ki [ezt a labort a Microsoft Learn oldalon](https://docs.microsoft.com/en-us/azure/machine-learning/component-reference/two-class-averaged-perceptron?WT.mc_id=academic-77998-cacaste), amely az [Azure ML designer](https://docs.microsoft.com/en-us/azure/machine-learning/concept-designer?WT.mc_id=academic-77998-cacaste) használatát mutatja be.

## [Előadás utáni kvíz](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/203)

## Áttekintés és önálló tanulás

Ha szeretnéd látni, hogyan használhatjuk a perceptront egy egyszerű probléma, valamint valós problémák megoldására, és folytatnád a tanulást, látogass el a [Perceptron](../../../../../lessons/3-NeuralNetworks/03-Perceptron/Perceptron.ipynb) jegyzetfüzetbe.

Itt van egy érdekes [cikk a perceptronokról](https://towardsdatascience.com/what-is-a-perceptron-basics-of-neural-networks-c4cfea20c590).

## [Feladat](lab/README.md)

Ebben a leckében egy perceptront valósítottunk meg bináris osztályozási feladathoz, és azt használtuk két kézzel írt számjegy megkülönböztetésére. Ebben a laborban az a feladatod, hogy teljes egészében oldd meg a számjegyosztályozás problémáját, azaz határozd meg, hogy egy adott kép melyik számjegyhez tartozik legvalószínűbben.

* [Útmutató](lab/README.md)
* [Jegyzetfüzet](../../../../../lessons/3-NeuralNetworks/03-Perceptron/lab/PerceptronMultiClass.ipynb)

**Felelősség kizárása**:  
Ez a dokumentum az AI fordítási szolgáltatás [Co-op Translator](https://github.com/Azure/co-op-translator) segítségével lett lefordítva. Bár törekszünk a pontosságra, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az eredeti nyelvén tekintendő hiteles forrásnak. Fontos információk esetén javasolt professzionális emberi fordítást igénybe venni. Nem vállalunk felelősséget semmilyen félreértésért vagy téves értelmezésért, amely a fordítás használatából eredhet.