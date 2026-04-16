# Úvod do neurónových sietí

![Zhrnutie obsahu Úvodu do neurónových sietí v kresbe](../../../../translated_images/sk/ai-neuralnetworks.1c687ae40bc86e83.webp)

Ako sme si povedali v úvode, jedným zo spôsobov, ako dosiahnuť inteligenciu, je trénovať **počítačový model** alebo **umelý mozog**. Od polovice 20. storočia vedci skúšali rôzne matematické modely, až kým sa v posledných rokoch tento smer neukázal ako mimoriadne úspešný. Takéto matematické modely mozgu sa nazývajú **neurónové siete**.

> Niekedy sa neurónové siete nazývajú *Umelé neurónové siete* (Artificial Neural Networks, ANNs), aby sa zdôraznilo, že hovoríme o modeloch, nie o skutočných sieťach neurónov.

## Strojové učenie

Neurónové siete sú súčasťou širšej disciplíny nazývanej **Strojové učenie**, ktorej cieľom je využívať dáta na trénovanie počítačových modelov schopných riešiť problémy. Strojové učenie tvorí veľkú časť umelej inteligencie, avšak v tomto kurze sa klasickému strojovému učeniu nevenujeme.

> Navštívte náš samostatný kurz **[Strojové učenie pre začiatočníkov](http://github.com/microsoft/ml-for-beginners)**, aby ste sa dozvedeli viac o klasickom strojovom učení.

V strojovom učení predpokladáme, že máme nejakú množinu príkladov **X** a zodpovedajúce výstupné hodnoty **Y**. Príklady sú často N-rozmerné vektory, ktoré pozostávajú z **príznakov**, a výstupy sa nazývajú **štítky**.

Budeme sa zaoberať dvoma najbežnejšími problémami strojového učenia:

* **Klasifikácia**, kde je potrebné zaradiť vstupný objekt do dvoch alebo viacerých tried.
* **Regresia**, kde je potrebné predpovedať číselnú hodnotu pre každý zo vstupných vzoriek.

> Pri reprezentácii vstupov a výstupov ako tenzorov je vstupná množina dát matica veľkosti M&times;N, kde M je počet vzoriek a N je počet príznakov. Výstupné štítky Y sú vektorom veľkosti M.

V tomto kurze sa zameriame iba na modely neurónových sietí.

## Model neurónu

Z biológie vieme, že náš mozog pozostáva z neurónových buniek (neurónov), pričom každý z nich má viacero "vstupov" (dendritov) a jeden "výstup" (axon). Dendrity aj axóny môžu viesť elektrické signály a spojenia medzi nimi — známe ako synapsie — môžu vykazovať rôzne stupne vodivosti, ktoré sú regulované neurotransmitermi.

![Model neurónu](../../../../translated_images/sk/synapse-wikipedia.ed20a9e4726ea1c6.webp) | ![Model neurónu](../../../../translated_images/sk/artneuron.1a5daa88d20ebe6f.webp)
----|----
Skutočný neurón *([Obrázok](https://en.wikipedia.org/wiki/Synapse#/media/File:SynapseSchematic_lines.svg) z Wikipédie)* | Umelý neurón *(Obrázok od autora)*

Najjednoduchší matematický model neurónu teda obsahuje niekoľko vstupov X<sub>1</sub>, ..., X<sub>N</sub> a jeden výstup Y, a sériu váh W<sub>1</sub>, ..., W<sub>N</sub>. Výstup sa vypočíta ako:

<img src="../../../../translated_images/sk/netout.1eb15eb76fd76731.webp" alt="Y = f\left(\sum_{i=1}^N X_iW_i\right)" width="131" height="53" align="center"/>

kde f je nejaká nelineárna **aktivačná funkcia**.

> Prvé modely neurónov boli opísané v klasickom článku [A logical calculus of the ideas immanent in nervous activity](https://www.cs.cmu.edu/~./epxing/Class/10715/reading/McCulloch.and.Pitts.pdf) od Warrena McCullocka a Waltera Pittsa v roku 1943. Donald Hebb vo svojej knihe "[The Organization of Behavior: A Neuropsychological Theory](https://books.google.com/books?id=VNetYrB8EBoC)" navrhol spôsob, akým by sa tieto siete mohli trénovať.

## V tejto sekcii

V tejto sekcii sa naučíme:
* [Perceptron](03-Perceptron/README.md), jeden z najstarších modelov neurónových sietí pre dvojtriednu klasifikáciu
* [Viacvrstvové siete](04-OwnFramework/README.md) s priloženým notebookom [ako si vytvoriť vlastný framework](04-OwnFramework/OwnFramework.ipynb)
* [Frameworky neurónových sietí](05-Frameworks/README.md), s týmito notebookmi: [PyTorch](05-Frameworks/IntroPyTorch.ipynb) a [Keras/Tensorflow](05-Frameworks/IntroKerasTF.ipynb)
* [Overfitting](../../../../lessons/3-NeuralNetworks/05-Frameworks)

---

**Upozornenie**:  
Tento dokument bol preložený pomocou služby AI prekladu [Co-op Translator](https://github.com/Azure/co-op-translator). Hoci sa snažíme o presnosť, prosím, berte na vedomie, že automatizované preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho rodnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nenesieme zodpovednosť za akékoľvek nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.