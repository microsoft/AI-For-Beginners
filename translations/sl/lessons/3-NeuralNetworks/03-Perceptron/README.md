# Uvod v nevronske mreže: Perceptron

## [Predhodni kviz](https://ff-quizzes.netlify.app/en/ai/quiz/5)

Eden prvih poskusov implementacije nečesa podobnega sodobni nevronski mreži je izvedel Frank Rosenblatt iz Cornell Aeronautical Laboratory leta 1957. Šlo je za strojno implementacijo, imenovano "Mark-1", zasnovano za prepoznavanje primitivnih geometrijskih oblik, kot so trikotniki, kvadrati in krogi.

|      |      |
|--------------|-----------|
|<img src='../../../../../translated_images/sl/Rosenblatt-wikipedia.294821b285ac796d.webp' alt='Frank Rosenblatt'/> | <img src='../../../../../translated_images/sl/Mark_I_perceptron_wikipedia.1f84eaa2d4b76ec9.webp' alt='The Mark 1 Perceptron' />|

> Slike [iz Wikipedije](https://en.wikipedia.org/wiki/Perceptron)

Vhodna slika je bila predstavljena z matriko fotocelic velikosti 20x20, kar pomeni, da je imela nevronska mreža 400 vhodov in en binarni izhod. Preprosta mreža je vsebovala en nevron, imenovan tudi **enota logičnega praga**. Teže nevronske mreže so delovale kot potenciometri, ki so jih morali ročno nastaviti med fazo učenja.

> ✅ Potenciometer je naprava, ki omogoča uporabniku prilagajanje upornosti v vezju.

> New York Times je takrat o perceptronu zapisal: *zarodek elektronskega računalnika, za katerega [mornarica] pričakuje, da bo lahko hodil, govoril, videl, pisal, se razmnoževal in bil zavesten svoje eksistence.*

## Model perceptrona

Predpostavimo, da imamo v našem modelu N značilnosti, v tem primeru bi bil vhodni vektor velikosti N. Perceptron je model za **binarno klasifikacijo**, kar pomeni, da lahko razlikuje med dvema razredoma vhodnih podatkov. Predpostavljamo, da bo za vsak vhodni vektor x izhod našega perceptrona bodisi +1 ali -1, odvisno od razreda. Izhod se izračuna po formuli:

y(x) = f(w<sup>T</sup>x)

kjer je f funkcija aktivacije s korakom.

<!-- img src="http://www.sciweavers.org/tex2img.php?eq=f%28x%29%20%3D%20%5Cbegin%7Bcases%7D%0A%20%20%20%20%20%20%20%20%20%2B1%20%26%20x%20%5Cgeq%200%20%5C%5C%0A%20%20%20%20%20%20%20%20%20-1%20%26%20x%20%3C%200%0A%20%20%20%20%20%20%20%5Cend%7Bcases%7D%20%5C%5C%0A&bc=White&fc=Black&im=jpg&fs=12&ff=arev&edit=0" align="center" border="0" alt="f(x) = \begin{cases} +1 & x \geq 0 \\ -1 & x < 0 \end{cases} \\" width="154" height="50" / -->
<img src="../../../../../translated_images/sl/activation-func.b4924007c7ce7764.webp"/>

## Učenje perceptrona

Za učenje perceptrona moramo najti vektorsko težo w, ki pravilno klasificira večino vrednosti, tj. povzroči najmanjšo **napako**. Ta napaka E je definirana z **merilom perceptrona** na naslednji način:

E(w) = -&sum;w<sup>T</sup>x<sub>i</sub>t<sub>i</sub>

kjer:

* vsota zajema tiste točke učnih podatkov i, ki povzročijo napačno klasifikacijo,
* x<sub>i</sub> so vhodni podatki, t<sub>i</sub> pa je bodisi -1 ali +1 za negativne oziroma pozitivne primere.

To merilo obravnavamo kot funkcijo tež w, ki jo moramo minimizirati. Pogosto se uporablja metoda **gradientnega spusta**, pri kateri začnemo z začetnimi težami w<sup>(0)</sup>, nato pa pri vsakem koraku posodobimo teže po formuli:

w<sup>(t+1)</sup> = w<sup>(t)</sup> - &eta;&nabla;E(w)

Tu je &eta; tako imenovana **stopnja učenja**, &nabla;E(w) pa označuje **gradient** E. Ko izračunamo gradient, dobimo:

w<sup>(t+1)</sup> = w<sup>(t)</sup> + &sum;&eta;x<sub>i</sub>t<sub>i</sub>

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

V tej lekciji ste spoznali perceptron, ki je model za binarno klasifikacijo, in kako ga naučiti z uporabo vektorske teže.

## 🚀 Izziv

Če želite poskusiti zgraditi svoj perceptron, preizkusite [to delavnico na Microsoft Learn](https://docs.microsoft.com/en-us/azure/machine-learning/component-reference/two-class-averaged-perceptron?WT.mc_id=academic-77998-cacaste), ki uporablja [Azure ML designer](https://docs.microsoft.com/en-us/azure/machine-learning/concept-designer?WT.mc_id=academic-77998-cacaste).

## [Kviz po predavanju](https://ff-quizzes.netlify.app/en/ai/quiz/6)

## Pregled in samostojno učenje

Če želite videti, kako lahko perceptron uporabimo za reševanje preprostih problemov in resničnih težav ter nadaljevati z učenjem, obiščite zvezek [Perceptron](Perceptron.ipynb).

Tukaj je zanimiv [članek o perceptronih](https://towardsdatascience.com/what-is-a-perceptron-basics-of-neural-networks-c4cfea20c590).

## [Naloga](lab/README.md)

V tej lekciji smo implementirali perceptron za nalogo binarne klasifikacije in ga uporabili za razlikovanje med dvema ročno napisanima številkama. V tej delavnici morate rešiti problem popolne klasifikacije številk, tj. določiti, katera številka najbolj verjetno ustreza dani sliki.

* [Navodila](lab/README.md)
* [Zvezek](lab/PerceptronMultiClass.ipynb)

---

