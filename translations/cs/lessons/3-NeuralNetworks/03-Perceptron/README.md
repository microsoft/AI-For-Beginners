# Úvod do neuronových sítí: Perceptron

## [Kvíz před lekcí](https://ff-quizzes.netlify.app/en/ai/quiz/5)

Jedním z prvních pokusů o implementaci něčeho podobného moderní neuronové síti byl projekt Franka Rosenblatta z Cornell Aeronautical Laboratory v roce 1957. Šlo o hardwarovou implementaci nazvanou "Mark-1", která byla navržena k rozpoznávání primitivních geometrických tvarů, jako jsou trojúhelníky, čtverce a kruhy.

|      |      |
|--------------|-----------|
|<img src='../../../../../translated_images/cs/Rosenblatt-wikipedia.294821b285ac796d.webp' alt='Frank Rosenblatt'/> | <img src='../../../../../translated_images/cs/Mark_I_perceptron_wikipedia.1f84eaa2d4b76ec9.webp' alt='The Mark 1 Perceptron' />|

> Obrázky [z Wikipedie](https://en.wikipedia.org/wiki/Perceptron)

Vstupní obraz byl reprezentován maticí 20x20 fotobuněk, takže neuronová síť měla 400 vstupů a jeden binární výstup. Jednoduchá síť obsahovala jeden neuron, který se také nazývá **jednotka logického prahu**. Váhy neuronové sítě fungovaly jako potenciometry, které bylo nutné manuálně upravovat během fáze učení.

> ✅ Potenciometr je zařízení, které umožňuje uživateli upravit odpor v obvodu.

> New York Times tehdy o perceptronu napsaly: *embryo elektronického počítače, od kterého [námořnictvo] očekává, že bude schopné chodit, mluvit, vidět, psát, reprodukovat se a být si vědomo své existence.*

## Model perceptronu

Předpokládejme, že máme N vlastností v našem modelu, v takovém případě by vstupní vektor měl velikost N. Perceptron je model **binární klasifikace**, tj. dokáže rozlišit mezi dvěma třídami vstupních dat. Předpokládáme, že pro každý vstupní vektor x bude výstup našeho perceptronu buď +1, nebo -1, v závislosti na třídě. Výstup se vypočítá podle vzorce:

y(x) = f(w<sup>T</sup>x)

kde f je aktivační funkce typu schod.

<!-- img src="http://www.sciweavers.org/tex2img.php?eq=f%28x%29%20%3D%20%5Cbegin%7Bcases%7D%0A%20%20%20%20%20%20%20%20%20%2B1%20%26%20x%20%5Cgeq%200%20%5C%5C%0A%20%20%20%20%20%20%20%20%20-1%20%26%20x%20%3C%200%0A%20%20%20%20%20%20%20%5Cend%7Bcases%7D%20%5C%5C%0A&bc=White&fc=Black&im=jpg&fs=12&ff=arev&edit=0" align="center" border="0" alt="f(x) = \begin{cases} +1 & x \geq 0 \\ -1 & x < 0 \end{cases} \\" width="154" height="50" / -->
<img src="../../../../../translated_images/cs/activation-func.b4924007c7ce7764.webp"/>

## Trénování perceptronu

Abychom perceptron natrénovali, musíme najít vektor vah w, který klasifikuje většinu hodnot správně, tj. vede k nejmenší **chybě**. Tato chyba E je definována pomocí **kritéria perceptronu** následujícím způsobem:

E(w) = -&sum;w<sup>T</sup>x<sub>i</sub>t<sub>i</sub>

kde:

* součet se bere přes ty tréninkové datové body i, které vedou k nesprávné klasifikaci
* x<sub>i</sub> je vstupní data a t<sub>i</sub> je buď -1 nebo +1 pro negativní a pozitivní příklady.

Toto kritérium je považováno za funkci vah w, kterou je třeba minimalizovat. Často se používá metoda **gradientního sestupu**, při které začneme s počátečními váhami w<sup>(0)</sup> a v každém kroku aktualizujeme váhy podle vzorce:

w<sup>(t+1)</sup> = w<sup>(t)</sup> - &eta;&nabla;E(w)

Zde &eta; je tzv. **rychlost učení** a &nabla;E(w) označuje **gradient** E. Po výpočtu gradientu získáme:

w<sup>(t+1)</sup> = w<sup>(t)</sup> + &sum;&eta;x<sub>i</sub>t<sub>i</sub>

Algoritmus v Pythonu vypadá takto:

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

## Závěr

V této lekci jste se naučili o perceptronu, což je model binární klasifikace, a jak jej natrénovat pomocí vektoru vah.

## 🚀 Výzva

Pokud si chcete zkusit vytvořit vlastní perceptron, zkuste [tento lab na Microsoft Learn](https://docs.microsoft.com/en-us/azure/machine-learning/component-reference/two-class-averaged-perceptron?WT.mc_id=academic-77998-cacaste), který využívá [Azure ML designer](https://docs.microsoft.com/en-us/azure/machine-learning/concept-designer?WT.mc_id=academic-77998-cacaste).

## [Kvíz po lekci](https://ff-quizzes.netlify.app/en/ai/quiz/6)

## Přehled & Samostudium

Chcete-li vidět, jak lze perceptron použít k řešení jednoduchého problému i reálných problémů, a pokračovat v učení, podívejte se na notebook [Perceptron](Perceptron.ipynb).

Zajímavý [článek o perceptronech](https://towardsdatascience.com/what-is-a-perceptron-basics-of-neural-networks-c4cfea20c590) také stojí za přečtení.

## [Úkol](lab/README.md)

V této lekci jsme implementovali perceptron pro úlohu binární klasifikace a použili jsme jej k rozlišení mezi dvěma ručně psanými číslicemi. V tomto labu máte za úkol vyřešit problém klasifikace číslic kompletně, tj. určit, která číslice nejpravděpodobněji odpovídá danému obrázku.

* [Instrukce](lab/README.md)
* [Notebook](lab/PerceptronMultiClass.ipynb)

---

