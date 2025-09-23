<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "0c37770bba4fff3c71dc00eb261ee61b",
  "translation_date": "2025-08-25T23:56:55+00:00",
  "source_file": "lessons/3-NeuralNetworks/03-Perceptron/README.md",
  "language_code": "cs"
}
-->
# Úvod do neuronových sítí: Perceptron

## [Kvíz před přednáškou](https://ff-quizzes.netlify.app/en/ai/quiz/5)

Jedním z prvních pokusů o implementaci něčeho podobného moderní neuronové síti provedl Frank Rosenblatt z Cornell Aeronautical Laboratory v roce 1957. Jednalo se o hardwarovou implementaci nazvanou "Mark-1", která byla navržena k rozpoznávání primitivních geometrických tvarů, jako jsou trojúhelníky, čtverce a kruhy.

|      |      |
|--------------|-----------|
|<img src='images/Rosenblatt-wikipedia.jpg' alt='Frank Rosenblatt'/> | <img src='images/Mark_I_perceptron_wikipedia.jpg' alt='The Mark 1 Perceptron' />|

> Obrázky [z Wikipedie](https://en.wikipedia.org/wiki/Perceptron)

Vstupní obraz byl reprezentován maticí 20x20 fotobuněk, takže neuronová síť měla 400 vstupů a jeden binární výstup. Jednoduchá síť obsahovala jeden neuron, který se také nazývá **jednotka logického prahu**. Váhy neuronové sítě fungovaly jako potenciometry, které bylo nutné manuálně upravit během fáze učení.

> ✅ Potenciometr je zařízení, které umožňuje uživateli upravit odpor v obvodu.

> The New York Times tehdy o perceptronu napsal: *zárodek elektronického počítače, od kterého [námořnictvo] očekává, že bude schopen chodit, mluvit, vidět, psát, reprodukovat se a být si vědom své existence.*

## Model perceptronu

Předpokládejme, že máme N vlastností v našem modelu, v takovém případě by vstupní vektor byl vektor o velikosti N. Perceptron je model **binární klasifikace**, tj. dokáže rozlišit mezi dvěma třídami vstupních dat. Předpokládáme, že pro každý vstupní vektor x bude výstup našeho perceptronu buď +1, nebo -1, v závislosti na třídě. Výstup bude vypočítán podle vzorce:

y(x) = f(w<sup>T</sup>x)

kde f je aktivační funkce typu schod.

<!-- img src="http://www.sciweavers.org/tex2img.php?eq=f%28x%29%20%3D%20%5Cbegin%7Bcases%7D%0A%20%20%20%20%20%20%20%20%20%2B1%20%26%20x%20%5Cgeq%200%20%5C%5C%0A%20%20%20%20%20%20%20%20%20-1%20%26%20x%20%3C%200%0A%20%20%20%20%20%20%20%5Cend%7Bcases%7D%20%5C%5C%0A&bc=White&fc=Black&im=jpg&fs=12&ff=arev&edit=0" align="center" border="0" alt="f(x) = \begin{cases} +1 & x \geq 0 \\ -1 & x < 0 \end{cases} \\" width="154" height="50" / -->
<img src="images/activation-func.png"/>

## Trénování perceptronu

Abychom perceptron natrénovali, musíme najít vektor vah w, který klasifikuje většinu hodnot správně, tj. vede k nejmenší **chybě**. Tato chyba E je definována pomocí **kritéria perceptronu** následujícím způsobem:

E(w) = -∑w<sup>T</sup>x<sub>i</sub>t<sub>i</sub>

kde:

* součet se bere přes ty body trénovacích dat i, které vedou k nesprávné klasifikaci
* x<sub>i</sub> je vstupní data a t<sub>i</sub> je buď -1 nebo +1 pro negativní a pozitivní příklady.

Toto kritérium je považováno za funkci vah w, kterou musíme minimalizovat. Často se používá metoda nazvaná **gradientní sestup**, při které začneme s nějakými počátečními váhami w<sup>(0)</sup> a poté v každém kroku aktualizujeme váhy podle vzorce:

w<sup>(t+1)</sup> = w<sup>(t)</sup> - η∇E(w)

Zde η je tzv. **rychlost učení** a ∇E(w) označuje **gradient** E. Po výpočtu gradientu získáme:

w<sup>(t+1)</sup> = w<sup>(t)</sup> + ∑ηx<sub>i</sub>t<sub>i</sub>

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

## [Kvíz po přednášce](https://ff-quizzes.netlify.app/en/ai/quiz/6)

## Přehled & Samostudium

Chcete-li vidět, jak můžeme použít perceptron k řešení jednoduchého problému i reálných problémů, a pokračovat v učení, podívejte se na notebook [Perceptron](../../../../../lessons/3-NeuralNetworks/03-Perceptron/Perceptron.ipynb).

Zde je zajímavý [článek o perceptronech](https://towardsdatascience.com/what-is-a-perceptron-basics-of-neural-networks-c4cfea20c590).

## [Úkol](lab/README.md)

V této lekci jsme implementovali perceptron pro úlohu binární klasifikace a použili jsme jej k rozlišení mezi dvěma ručně psanými číslicemi. V tomto labu máte za úkol vyřešit problém klasifikace číslic kompletně, tj. určit, která číslice nejpravděpodobněji odpovídá danému obrázku.

* [Instrukce](lab/README.md)
* [Notebook](../../../../../lessons/3-NeuralNetworks/03-Perceptron/lab/PerceptronMultiClass.ipynb)

**Prohlášení:**  
Tento dokument byl přeložen pomocí služby pro automatický překlad [Co-op Translator](https://github.com/Azure/co-op-translator). Ačkoli se snažíme o přesnost, mějte prosím na paměti, že automatické překlady mohou obsahovat chyby nebo nepřesnosti. Původní dokument v jeho původním jazyce by měl být považován za autoritativní zdroj. Pro důležité informace se doporučuje profesionální lidský překlad. Neodpovídáme za žádná nedorozumění nebo nesprávné interpretace vyplývající z použití tohoto překladu.