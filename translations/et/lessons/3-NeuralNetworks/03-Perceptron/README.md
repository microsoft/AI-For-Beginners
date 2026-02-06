# Sissejuhatus tehisnärvivõrkudesse: Perceptron

## [Eelloengu viktoriin](https://ff-quizzes.netlify.app/en/ai/quiz/5)

Üks esimesi katseid luua midagi tänapäevasele tehisnärvivõrgule sarnast tegi Frank Rosenblatt Cornelli Aeronautika Laboratooriumist 1957. aastal. See oli riistvaraline lahendus nimega "Mark-1", mis oli loodud primitiivsete geomeetriliste kujundite, nagu kolmnurgad, ruudud ja ringid, äratundmiseks.

|      |      |
|--------------|-----------|
|<img src='../../../../../translated_images/et/Rosenblatt-wikipedia.294821b285ac796d.webp' alt='Frank Rosenblatt'/> | <img src='../../../../../translated_images/et/Mark_I_perceptron_wikipedia.1f84eaa2d4b76ec9.webp' alt='Mark 1 Perceptron' />|

> Pildid [Wikipediast](https://en.wikipedia.org/wiki/Perceptron)

Sisendpilt esitati 20x20 fototundliku elemendi maatriksina, seega oli tehisnärvivõrgul 400 sisendit ja üks binaarne väljund. Lihtne võrk koosnes ühest neuronist, mida nimetatakse ka **läve loogika üksuseks**. Närvivõrgu kaaluparameetrid toimisid nagu potentsiomeetrid, mida tuli treeningfaasis käsitsi reguleerida.

> ✅ Potentsiomeeter on seade, mis võimaldab kasutajal reguleerida vooluringi takistust.

> The New York Times kirjutas tol ajal perceptroni kohta: *elektroonilise arvuti embrüo, mis [mereväe arvates] suudab kõndida, rääkida, näha, kirjutada, end paljundada ja olla teadlik oma olemasolust.*

## Perceptroni mudel

Oletame, et meie mudelil on N tunnust, sel juhul on sisendvektor suurusega N. Perceptron on **binaarne klassifitseerimismudel**, st see suudab eristada kahte sisendandmete klassi. Eeldame, et iga sisendvektori x korral on meie perceptroni väljund kas +1 või -1, sõltuvalt klassist. Väljund arvutatakse järgmise valemi abil:

y(x) = f(w<sup>T</sup>x)

kus f on astmelise aktiveerimise funktsioon

<!-- img src="http://www.sciweavers.org/tex2img.php?eq=f%28x%29%20%3D%20%5Cbegin%7Bcases%7D%0A%20%20%20%20%20%20%20%20%20%2B1%20%26%20x%20%5Cgeq%200%20%5C%5C%0A%20%20%20%20%20%20%20%20%20-1%20%26%20x%20%3C%200%0A%20%20%20%20%20%20%20%5Cend%7Bcases%7D%20%5C%5C%0A&bc=White&fc=Black&im=jpg&fs=12&ff=arev&edit=0" align="center" border="0" alt="f(x) = \begin{cases} +1 & x \geq 0 \\ -1 & x < 0 \end{cases} \\" width="154" height="50" / -->
<img src="../../../../../translated_images/et/activation-func.b4924007c7ce7764.webp"/>

## Perceptroni treenimine

Perceptroni treenimiseks peame leidma kaaluvektori w, mis klassifitseerib enamik väärtusi õigesti, st mille tulemuseks on kõige väiksem **viga**. See viga E on määratletud **perceptroni kriteeriumi** järgi järgmiselt:

E(w) = -&sum;w<sup>T</sup>x<sub>i</sub>t<sub>i</sub>

kus:

* summa arvutatakse nende treeningandmepunktide i pealt, mis on valesti klassifitseeritud
* x<sub>i</sub> on sisendandmed ja t<sub>i</sub> on kas -1 või +1 vastavalt negatiivsetele ja positiivsetele näidetele.

Seda kriteeriumi käsitletakse kaaluvektori w funktsioonina, mida tuleb minimeerida. Sageli kasutatakse meetodit nimega **gradientlangus**, kus alustatakse mõnest algkaalust w<sup>(0)</sup> ja seejärel igal sammul uuendatakse kaale järgmise valemi järgi:

w<sup>(t+1)</sup> = w<sup>(t)</sup> - &eta;&nabla;E(w)

Siin on &eta; nn **õppemäär** ja &nabla;E(w) tähistab E **gradienti**. Pärast gradiendi arvutamist saame tulemuseks:

w<sup>(t+1)</sup> = w<sup>(t)</sup> + &sum;&eta;x<sub>i</sub>t<sub>i</sub>

Pythonis näeb algoritm välja selline:

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

## Kokkuvõte

Selles õppetükis õppisite perceptroni kohta, mis on binaarne klassifitseerimismudel, ja kuidas seda treenida kaaluvektori abil.

## 🚀 Väljakutse

Kui soovite proovida ise perceptroni luua, proovige [seda laborit Microsoft Learnis](https://docs.microsoft.com/en-us/azure/machine-learning/component-reference/two-class-averaged-perceptron?WT.mc_id=academic-77998-cacaste), mis kasutab [Azure ML disainerit](https://docs.microsoft.com/en-us/azure/machine-learning/concept-designer?WT.mc_id=academic-77998-cacaste).

## [Järelloengu viktoriin](https://ff-quizzes.netlify.app/en/ai/quiz/6)

## Ülevaade ja iseseisev õppimine

Et näha, kuidas perceptronit saab kasutada nii mänguliste kui ka päriselu probleemide lahendamiseks, ja õppimist jätkata, minge [Perceptroni](Perceptron.ipynb) märkmikusse.

Siin on ka huvitav [artikkel perceptronite kohta](https://towardsdatascience.com/what-is-a-perceptron-basics-of-neural-networks-c4cfea20c590).

## [Ülesanne](lab/README.md)

Selles õppetükis rakendasime perceptroni binaarse klassifitseerimise ülesande jaoks ja kasutasime seda kahe käsitsi kirjutatud numbri eristamiseks. Selles laboris palutakse teil lahendada numbrite klassifitseerimise probleem täielikult, st määrata, millisele numbrile antud pilt kõige tõenäolisemalt vastab.

* [Juhised](lab/README.md)
* [Märkmik](lab/PerceptronMultiClass.ipynb)

---

**Lahtiütlus**:  
See dokument on tõlgitud AI tõlketeenuse [Co-op Translator](https://github.com/Azure/co-op-translator) abil. Kuigi püüame tagada täpsust, palume arvestada, et automaatsed tõlked võivad sisaldada vigu või ebatäpsusi. Algne dokument selle algses keeles tuleks pidada autoriteetseks allikaks. Olulise teabe puhul soovitame kasutada professionaalset inimtõlget. Me ei vastuta selle tõlke kasutamisest tulenevate arusaamatuste või valesti tõlgenduste eest.