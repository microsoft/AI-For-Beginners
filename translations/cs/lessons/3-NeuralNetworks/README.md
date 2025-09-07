<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "5abc5f7978919be90cd313f0c20e8228",
  "translation_date": "2025-09-07T14:35:52+00:00",
  "source_file": "lessons/3-NeuralNetworks/README.md",
  "language_code": "cs"
}
-->
# Úvod do neuronových sítí

![Shrnutí obsahu Úvodu do neuronových sítí ve sketchnotu](../../../../translated_images/ai-neuralnetworks.1c687ae40bc86e834f497844866a26d3e0886650a67a4bbe29442e2f157d3b18.cs.png)

Jak jsme si řekli v úvodu, jedním ze způsobů, jak dosáhnout inteligence, je trénovat **počítačový model** nebo **umělý mozek**. Od poloviny 20. století vědci zkoušeli různé matematické modely, až se v posledních letech tento směr ukázal jako velmi úspěšný. Tyto matematické modely mozku se nazývají **neuronové sítě**.

> Někdy se neuronové sítě označují jako *umělé neuronové sítě* (Artificial Neural Networks, ANNs), aby bylo jasné, že mluvíme o modelech, nikoli o skutečných sítích neuronů.

## Strojové učení

Neuronové sítě jsou součástí širší disciplíny nazývané **strojové učení**, jejímž cílem je využívat data k trénování počítačových modelů, které dokážou řešit problémy. Strojové učení tvoří velkou část umělé inteligence, avšak v tomto kurikulu se klasickým strojovým učením nezabýváme.

> Navštivte náš samostatný **[kurikulum Strojové učení pro začátečníky](http://github.com/microsoft/ml-for-beginners)**, kde se dozvíte více o klasickém strojovém učení.

Ve strojovém učení předpokládáme, že máme nějakou datovou sadu příkladů **X** a odpovídající výstupní hodnoty **Y**. Příklady jsou často N-rozměrné vektory, které se skládají z **příznaků**, a výstupy se nazývají **štítky**.

Budeme se zabývat dvěma nejběžnějšími problémy strojového učení:

* **Klasifikace**, kde je třeba zařadit vstupní objekt do dvou nebo více tříd.
* **Regrese**, kde je třeba předpovědět číselnou hodnotu pro každý ze vstupních vzorků.

> Při reprezentaci vstupů a výstupů jako tenzorů je vstupní datová sada maticí o velikosti M×N, kde M je počet vzorků a N je počet příznaků. Výstupní štítky Y jsou vektorem o velikosti M.

V tomto kurikulu se zaměříme pouze na modely neuronových sítí.

## Model neuronu

Z biologie víme, že náš mozek se skládá z nervových buněk, z nichž každá má více "vstupů" (axonů) a jeden výstup (dendrit). Axony a dendrity mohou vést elektrické signály a spojení mezi axony a dendrity mohou vykazovat různé stupně vodivosti (řízené neuromediátory).

![Model neuronu](../../../../translated_images/synapse-wikipedia.ed20a9e4726ea1c6a3ce8fec51c0b9bec6181946dca0fe4e829bc12fa3bacf01.cs.jpg) | ![Model neuronu](../../../../translated_images/artneuron.1a5daa88d20ebe6f5824ddb89fba0bdaaf49f67e8230c1afbec42909df1fc17e.cs.png)
----|----
Skutečný neuron *([Obrázek](https://en.wikipedia.org/wiki/Synapse#/media/File:SynapseSchematic_lines.svg) z Wikipedie)* | Umělý neuron *(Obrázek od autora)*

Nejjednodušší matematický model neuronu tedy obsahuje několik vstupů X<sub>1</sub>, ..., X<sub>N</sub> a jeden výstup Y a řadu vah W<sub>1</sub>, ..., W<sub>N</sub>. Výstup se vypočítá jako:

<img src="images/netout.png" alt="Y = f\left(\sum_{i=1}^N X_iW_i\right)" width="131" height="53" align="center"/>

kde f je nějaká nelineární **aktivační funkce**.

> První modely neuronu byly popsány v klasickém článku [Logický kalkulus idejí imanentních nervové aktivitě](https://www.cs.cmu.edu/~./epxing/Class/10715/reading/McCulloch.and.Pitts.pdf) od Warrena McCullocha a Waltera Pittse v roce 1943. Donald Hebb ve své knize "[Organizace chování: Neuropsychologická teorie](https://books.google.com/books?id=VNetYrB8EBoC)" navrhl způsob, jak lze tyto sítě trénovat.

## V této sekci

V této sekci se naučíme:
* [Perceptron](03-Perceptron/README.md), jeden z nejstarších modelů neuronových sítí pro klasifikaci do dvou tříd
* [Vícevrstvé sítě](04-OwnFramework/README.md) s doprovodným notebookem [jak vytvořit vlastní framework](04-OwnFramework/OwnFramework.ipynb)
* [Frameworky neuronových sítí](05-Frameworks/README.md), s těmito notebooky: [PyTorch](05-Frameworks/IntroPyTorch.ipynb) a [Keras/Tensorflow](05-Frameworks/IntroKerasTF.ipynb)
* [Přeučení](../../../../lessons/3-NeuralNetworks/05-Frameworks)

---

**Prohlášení**:  
Tento dokument byl přeložen pomocí služby pro automatický překlad [Co-op Translator](https://github.com/Azure/co-op-translator). I když se snažíme o přesnost, mějte prosím na paměti, že automatické překlady mohou obsahovat chyby nebo nepřesnosti. Původní dokument v jeho původním jazyce by měl být považován za autoritativní zdroj. Pro důležité informace doporučujeme profesionální lidský překlad. Neodpovídáme za žádné nedorozumění nebo nesprávné interpretace vyplývající z použití tohoto překladu.