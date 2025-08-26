<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "0c37770bba4fff3c71dc00eb261ee61b",
  "translation_date": "2025-08-25T23:57:14+00:00",
  "source_file": "lessons/3-NeuralNetworks/03-Perceptron/README.md",
  "language_code": "sk"
}
-->
# Úvod do neurónových sietí: Perceptron

## [Kvíz pred prednáškou](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/103)

Jedným z prvých pokusov o implementáciu niečoho podobného moderným neurónovým sieťam bol projekt Franka Rosenblatta z Cornell Aeronautical Laboratory v roku 1957. Išlo o hardvérovú implementáciu nazvanú "Mark-1", ktorá bola navrhnutá na rozpoznávanie primitívnych geometrických tvarov, ako sú trojuholníky, štvorce a kruhy.

|      |      |
|--------------|-----------|
|<img src='images/Rosenblatt-wikipedia.jpg' alt='Frank Rosenblatt'/> | <img src='images/Mark_I_perceptron_wikipedia.jpg' alt='The Mark 1 Perceptron' />|

> Obrázky [z Wikipédie](https://en.wikipedia.org/wiki/Perceptron)

Vstupný obraz bol reprezentovaný maticou 20x20 fotobuniek, takže neurónová sieť mala 400 vstupov a jeden binárny výstup. Jednoduchá sieť obsahovala jeden neurón, nazývaný tiež **jednotka prahovej logiky**. Váhy neurónovej siete fungovali ako potenciometre, ktoré bolo potrebné manuálne nastaviť počas fázy učenia.

> ✅ Potenciometer je zariadenie, ktoré umožňuje používateľovi nastaviť odpor v obvode.

> New York Times v tom čase napísali o perceptrone: *embryo elektronického počítača, od ktorého [Námorníctvo] očakáva, že bude schopné chodiť, rozprávať, vidieť, písať, reprodukovať sa a byť si vedomé svojej existencie.*

## Model perceptronu

Predpokladajme, že máme N vlastností v našom modeli, v takom prípade by vstupný vektor bol vektor veľkosti N. Perceptron je model **binárnej klasifikácie**, t.j. dokáže rozlíšiť medzi dvoma triedami vstupných údajov. Predpokladáme, že pre každý vstupný vektor x bude výstup nášho perceptronu buď +1 alebo -1, v závislosti od triedy. Výstup sa vypočíta pomocou vzorca:

y(x) = f(w<sup>T</sup>x)

kde f je aktivačná funkcia typu krok.

<!-- img src="http://www.sciweavers.org/tex2img.php?eq=f%28x%29%20%3D%20%5Cbegin%7Bcases%7D%0A%20%20%20%20%20%20%20%20%20%2B1%20%26%20x%20%5Cgeq%200%20%5C%5C%0A%20%20%20%20%20%20%20%20%20-1%20%26%20x%20%3C%200%0A%20%20%20%20%20%20%20%5Cend%7Bcases%7D%20%5C%5C%0A&bc=White&fc=Black&im=jpg&fs=12&ff=arev&edit=0" align="center" border="0" alt="f(x) = \begin{cases} +1 & x \geq 0 \\ -1 & x < 0 \end{cases} \\" width="154" height="50" / -->
<img src="images/activation-func.png"/>

## Tréning perceptronu

Na tréning perceptronu potrebujeme nájsť vektor váh w, ktorý klasifikuje väčšinu hodnôt správne, t.j. vedie k najmenšej **chybe**. Táto chyba E je definovaná **kritériom perceptronu** nasledovne:

E(w) = -∑w<sup>T</sup>x<sub>i</sub>t<sub>i</sub>

kde:

* súčet sa berie na tých tréningových dátových bodoch i, ktoré vedú k nesprávnej klasifikácii
* x<sub>i</sub> je vstupný údaj a t<sub>i</sub> je buď -1 alebo +1 pre negatívne a pozitívne príklady.

Toto kritérium sa považuje za funkciu váh w, ktorú potrebujeme minimalizovať. Často sa používa metóda nazývaná **gradientný zostup**, pri ktorej začíname s nejakými počiatočnými váhami w<sup>(0)</sup>, a potom v každom kroku aktualizujeme váhy podľa vzorca:

w<sup>(t+1)</sup> = w<sup>(t)</sup> - η∇E(w)

Tu η je tzv. **rýchlosť učenia** a ∇E(w) označuje **gradient** E. Po výpočte gradientu dostaneme:

w<sup>(t+1)</sup> = w<sup>(t)</sup> + ∑ηx<sub>i</sub>t<sub>i</sub>

Algoritmus v Pythone vyzerá takto:

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

## Záver

V tejto lekcii ste sa naučili o perceptrone, ktorý je modelom binárnej klasifikácie, a ako ho trénovať pomocou vektora váh.

## 🚀 Výzva

Ak si chcete vyskúšať vytvoriť vlastný perceptron, skúste [tento lab na Microsoft Learn](https://docs.microsoft.com/en-us/azure/machine-learning/component-reference/two-class-averaged-perceptron?WT.mc_id=academic-77998-cacaste), ktorý používa [Azure ML designer](https://docs.microsoft.com/en-us/azure/machine-learning/concept-designer?WT.mc_id=academic-77998-cacaste).

## [Kvíz po prednáške](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/203)

## Prehľad a samostatné štúdium

Ak chcete vidieť, ako môžeme použiť perceptron na riešenie jednoduchého problému, ako aj reálnych problémov, a pokračovať v učení, prejdite na [Perceptron](../../../../../lessons/3-NeuralNetworks/03-Perceptron/Perceptron.ipynb) notebook.

Tu je zaujímavý [článok o perceptronoch](https://towardsdatascience.com/what-is-a-perceptron-basics-of-neural-networks-c4cfea20c590).

## [Úloha](lab/README.md)

V tejto lekcii sme implementovali perceptron pre úlohu binárnej klasifikácie a použili sme ho na klasifikáciu medzi dvoma ručne písanými číslicami. V tomto laboratóriu máte za úlohu vyriešiť problém klasifikácie číslic úplne, t.j. určiť, ktorá číslica najpravdepodobnejšie zodpovedá danému obrázku.

* [Pokyny](lab/README.md)
* [Notebook](../../../../../lessons/3-NeuralNetworks/03-Perceptron/lab/PerceptronMultiClass.ipynb)

**Upozornenie**:  
Tento dokument bol preložený pomocou služby AI prekladu [Co-op Translator](https://github.com/Azure/co-op-translator). Aj keď sa snažíme o presnosť, prosím, berte na vedomie, že automatizované preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho rodnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nie sme zodpovední za akékoľvek nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.