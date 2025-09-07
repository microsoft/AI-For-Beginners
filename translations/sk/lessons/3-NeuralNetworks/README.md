<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "1c6b8c7c1778a35fc1139b7f2aecb7b3",
  "translation_date": "2025-08-25T23:42:06+00:00",
  "source_file": "lessons/3-NeuralNetworks/README.md",
  "language_code": "sk"
}
-->
# Úvod do neurónových sietí

![Zhrnutie obsahu Úvodu do neurónových sietí v kresbe](../../../../translated_images/ai-neuralnetworks.1c687ae40bc86e834f497844866a26d3e0886650a67a4bbe29442e2f157d3b18.sk.png)

Ako sme diskutovali v úvode, jedným zo spôsobov, ako dosiahnuť inteligenciu, je trénovať **počítačový model** alebo **umelý mozog**. Od polovice 20. storočia sa výskumníci pokúšali o rôzne matematické modely, až kým sa v posledných rokoch tento smer neukázal ako mimoriadne úspešný. Takéto matematické modely mozgu sa nazývajú **neurónové siete**.

> Neurónové siete sa niekedy nazývajú *Umelé neurónové siete*, ANNs, aby sa zdôraznilo, že hovoríme o modeloch, nie o skutočných sieťach neurónov.

## Strojové učenie

Neurónové siete sú súčasťou širšej disciplíny nazývanej **Strojové učenie**, ktorej cieľom je využívať dáta na trénovanie počítačových modelov schopných riešiť problémy. Strojové učenie tvorí veľkú časť umelej inteligencie, avšak v tomto učebnom pláne sa klasickým strojovým učením nezaoberáme.

> Navštívte náš samostatný **[Strojové učenie pre začiatočníkov](http://github.com/microsoft/ml-for-beginners)** učebný plán, aby ste sa dozvedeli viac o klasickom strojovom učení.

V strojovom učení predpokladáme, že máme nejakú množinu dát príkladov **X** a zodpovedajúce výstupné hodnoty **Y**. Príklady sú často N-rozmerné vektory, ktoré pozostávajú z **príznakov**, a výstupy sa nazývajú **označenia**.

Budeme sa zaoberať dvoma najbežnejšími problémami strojového učenia:

* **Klasifikácia**, kde je potrebné klasifikovať vstupný objekt do dvoch alebo viacerých tried.
* **Regresia**, kde je potrebné predpovedať číselnú hodnotu pre každý zo vstupných vzoriek.

> Pri reprezentácii vstupov a výstupov ako tenzorov je vstupná množina dát matica veľkosti M×N, kde M je počet vzoriek a N je počet príznakov. Výstupné označenia Y sú vektor veľkosti M.

V tomto učebnom pláne sa budeme zameriavať iba na modely neurónových sietí.

## Model neurónu

Z biológie vieme, že náš mozog pozostáva z neurónových buniek, z ktorých každá má viacero "vstupov" (axónov) a jeden výstup (dendrit). Axóny a dendrity môžu prenášať elektrické signály a spojenia medzi axónmi a dendritmi môžu vykazovať rôzne stupne vodivosti (riadené neuromediátormi).

![Model neurónu](../../../../translated_images/synapse-wikipedia.ed20a9e4726ea1c6a3ce8fec51c0b9bec6181946dca0fe4e829bc12fa3bacf01.sk.jpg) | ![Model neurónu](../../../../translated_images/artneuron.1a5daa88d20ebe6f5824ddb89fba0bdaaf49f67e8230c1afbec42909df1fc17e.sk.png)
----|----
Skutočný neurón *([Obrázok](https://en.wikipedia.org/wiki/Synapse#/media/File:SynapseSchematic_lines.svg) z Wikipédie)* | Umelý neurón *(Obrázok od autora)*

Najjednoduchší matematický model neurónu teda obsahuje niekoľko vstupov X<sub>1</sub>, ..., X<sub>N</sub> a jeden výstup Y, a sériu váh W<sub>1</sub>, ..., W<sub>N</sub>. Výstup sa vypočíta ako:

<img src="images/netout.png" alt="Y = f\left(\sum_{i=1}^N X_iW_i\right)" width="131" height="53" align="center"/>

kde f je nejaká nelineárna **aktivačná funkcia**.

> Prvé modely neurónov boli opísané v klasickom článku [A logical calculus of the ideas immanent in nervous activity](https://www.cs.cmu.edu/~./epxing/Class/10715/reading/McCulloch.and.Pitts.pdf) od Warrena McCullocka a Waltera Pittsa v roku 1943. Donald Hebb vo svojej knihe "[The Organization of Behavior: A Neuropsychological Theory](https://books.google.com/books?id=VNetYrB8EBoC)" navrhol spôsob, akým môžu byť tieto siete trénované.

## V tejto sekcii

V tejto sekcii sa naučíme:
* [Perceptron](03-Perceptron/README.md), jeden z najstarších modelov neurónových sietí pre dvojtriednu klasifikáciu
* [Viacvrstvové siete](04-OwnFramework/README.md) s priloženým notebookom [ako vytvoriť vlastný framework](../../../../lessons/3-NeuralNetworks/04-OwnFramework/OwnFramework.ipynb)
* [Frameworky neurónových sietí](05-Frameworks/README.md), s týmito notebookmi: [PyTorch](../../../../lessons/3-NeuralNetworks/05-Frameworks/IntroPyTorch.ipynb) a [Keras/Tensorflow](../../../../lessons/3-NeuralNetworks/05-Frameworks/IntroKerasTF.ipynb)
* [Overfitting](../../../../lessons/3-NeuralNetworks/05-Frameworks)

**Upozornenie**:  
Tento dokument bol preložený pomocou služby na automatický preklad [Co-op Translator](https://github.com/Azure/co-op-translator). Hoci sa snažíme o presnosť, upozorňujeme, že automatické preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho pôvodnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nenesieme zodpovednosť za akékoľvek nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.