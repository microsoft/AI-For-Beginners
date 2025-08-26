<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "0c37770bba4fff3c71dc00eb261ee61b",
  "translation_date": "2025-08-25T23:59:03+00:00",
  "source_file": "lessons/3-NeuralNetworks/03-Perceptron/README.md",
  "language_code": "sl"
}
-->
# Uvod v nevronske mreže: Perceptron

## [Predavanje kviz](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/103)

Eden prvih poskusov implementacije nečesa podobnega sodobni nevronski mreži je izvedel Frank Rosenblatt iz Cornell Aeronautical Laboratory leta 1957. Šlo je za strojno implementacijo, imenovano "Mark-1", zasnovano za prepoznavanje osnovnih geometrijskih oblik, kot so trikotniki, kvadrati in krogi.

|      |      |
|--------------|-----------|
|<img src='images/Rosenblatt-wikipedia.jpg' alt='Frank Rosenblatt'/> | <img src='images/Mark_I_perceptron_wikipedia.jpg' alt='The Mark 1 Perceptron' />|

> Slike [iz Wikipedije](https://en.wikipedia.org/wiki/Perceptron)

Vhodna slika je bila predstavljena z matriko fotocelic velikosti 20x20, zato je imela nevronska mreža 400 vhodov in en binarni izhod. Preprosta mreža je vsebovala en nevron, imenovan tudi **enota logičnega praga**. Teže nevronske mreže so delovale kot potenciometri, ki so zahtevali ročno prilagoditev med fazo učenja.

> ✅ Potenciometer je naprava, ki omogoča uporabniku prilagajanje upornosti v vezju.

> New York Times je takrat o perceptronu zapisal: *zarodek elektronskega računalnika, za katerega [mornarica] pričakuje, da bo lahko hodil, govoril, videl, pisal, se razmnoževal in bil zaveden svojega obstoja.*

## Model perceptrona

Predpostavimo, da imamo v našem modelu N značilnosti, v tem primeru bi bil vhodni vektor velikosti N. Perceptron je model za **binarno klasifikacijo**, kar pomeni, da lahko razlikuje med dvema razredoma vhodnih podatkov. Predpostavljamo, da bo za vsak vhodni vektor x izhod našega perceptrona bodisi +1 ali -1, odvisno od razreda. Izhod se izračuna po formuli:

y(x) = f(w<sup>T</sup>x)

kjer je f funkcija aktivacije s pragom.

<!-- img src="http://www.sciweavers.org/tex2img.php?eq=f%28x%29%20%3D%20%5Cbegin%7Bcases%7D%0A%20%20%20%20%20%20%20%20%20%2B1%20%26%20x%20%5Cgeq%200%20%5C%5C%0A%20%20%20%20%20%20%20%20%20-1%20%26%20x%20%3C%200%0A%20%20%20%20%20%20%20%5Cend%7Bcases%7D%20%5C%5C%0A&bc=White&fc=Black&im=jpg&fs=12&ff=arev&edit=0" align="center" border="0" alt="f(x) = \begin{cases} +1 & x \geq 0 \\ -1 & x < 0 \end{cases} \\" width="154" height="50" / -->
<img src="images/activation-func.png"/>

## Učenje perceptrona

Za učenje perceptrona moramo najti vektor tež w, ki pravilno razvrsti večino vrednosti, tj. povzroči najmanjšo **napako**. Ta napaka E je definirana z **merilom perceptrona** na naslednji način:

E(w) = -∑w<sup>T</sup>x<sub>i</sub>t<sub>i</sub>

kjer:

* je vsota vzeta za tiste točke učnih podatkov i, ki so napačno razvrščene,
* x<sub>i</sub> so vhodni podatki, t<sub>i</sub> pa je bodisi -1 ali +1 za negativne oziroma pozitivne primere.

To merilo obravnavamo kot funkcijo tež w, ki jo moramo minimizirati. Pogosto se uporablja metoda, imenovana **gradientni spust**, pri kateri začnemo z začetnimi težami w<sup>(0)</sup>, nato pa pri vsakem koraku posodobimo teže po formuli:

w<sup>(t+1)</sup> = w<sup>(t)</sup> - η∇E(w)

Tukaj je η tako imenovana **hitrost učenja**, ∇E(w) pa označuje **gradient** E. Po izračunu gradienta dobimo:

w<sup>(t+1)</sup> = w<sup>(t)</sup> + ∑ηx<sub>i</sub>t<sub>i</sub>

Algoritem v Pythonu izgleda takole:

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

## Zaključek

V tej lekciji ste spoznali perceptron, ki je model za binarno klasifikacijo, in kako ga naučiti z uporabo vektorja tež.

## 🚀 Izziv

Če želite poskusiti zgraditi svoj perceptron, poskusite [to delavnico na Microsoft Learn](https://docs.microsoft.com/en-us/azure/machine-learning/component-reference/two-class-averaged-perceptron?WT.mc_id=academic-77998-cacaste), ki uporablja [Azure ML designer](https://docs.microsoft.com/en-us/azure/machine-learning/concept-designer?WT.mc_id=academic-77998-cacaste).

## [Kviz po predavanju](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/203)

## Pregled in samostojno učenje

Če želite videti, kako lahko uporabimo perceptron za reševanje preprostih problemov in resničnih problemov, ter nadaljevati z učenjem, obiščite zvezek [Perceptron](../../../../../lessons/3-NeuralNetworks/03-Perceptron/Perceptron.ipynb).

Tukaj je zanimiv [članek o perceptronih](https://towardsdatascience.com/what-is-a-perceptron-basics-of-neural-networks-c4cfea20c590).

## [Naloga](lab/README.md)

V tej lekciji smo implementirali perceptron za nalogo binarne klasifikacije in ga uporabili za razvrščanje med dvema ročno napisanima številkama. V tej delavnici morate rešiti problem popolne klasifikacije številk, tj. določiti, katera številka najverjetneje ustreza določeni sliki.

* [Navodila](lab/README.md)
* [Zvezek](../../../../../lessons/3-NeuralNetworks/03-Perceptron/lab/PerceptronMultiClass.ipynb)

**Omejitev odgovornosti**:  
Ta dokument je bil preveden z uporabo storitve AI za prevajanje [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas prosimo, da upoštevate, da lahko avtomatizirani prevodi vsebujejo napake ali netočnosti. Izvirni dokument v njegovem izvirnem jeziku je treba obravnavati kot avtoritativni vir. Za ključne informacije priporočamo profesionalni človeški prevod. Ne odgovarjamo za morebitne nesporazume ali napačne razlage, ki izhajajo iz uporabe tega prevoda.