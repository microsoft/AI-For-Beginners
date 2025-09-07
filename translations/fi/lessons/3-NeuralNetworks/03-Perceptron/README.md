<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "0c37770bba4fff3c71dc00eb261ee61b",
  "translation_date": "2025-08-28T19:47:58+00:00",
  "source_file": "lessons/3-NeuralNetworks/03-Perceptron/README.md",
  "language_code": "fi"
}
-->
# Johdanto neuroverkkoihin: Perceptron

## [Ennakkovisa](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/103)

Yksi ensimmäisistä yrityksistä toteuttaa jotain modernin neuroverkon kaltaista tehtiin Frank Rosenblattin toimesta Cornellin ilmailulaboratoriossa vuonna 1957. Se oli laitteistototeutus nimeltä "Mark-1", joka oli suunniteltu tunnistamaan yksinkertaisia geometrisia kuvioita, kuten kolmioita, neliöitä ja ympyröitä.

|      |      |
|--------------|-----------|
|<img src='images/Rosenblatt-wikipedia.jpg' alt='Frank Rosenblatt'/> | <img src='images/Mark_I_perceptron_wikipedia.jpg' alt='The Mark 1 Perceptron' />|

> Kuvat [Wikipediasta](https://en.wikipedia.org/wiki/Perceptron)

Syötekuva esitettiin 20x20 valokennoruudukolla, joten neuroverkossa oli 400 syötettä ja yksi binäärinen ulostulo. Yksinkertainen verkko sisälsi yhden neuronin, jota kutsuttiin myös **kynnyksen logiikkayksiköksi**. Neuroverkon painot toimivat potentiometreinä, joita piti säätää manuaalisesti koulutusvaiheen aikana.

> ✅ Potentiometri on laite, jonka avulla käyttäjä voi säätää piirin vastusta.

> The New York Times kirjoitti tuolloin perceptronista: *sähköisen tietokoneen alkio, jonka [laivasto] odottaa pystyvän kävelemään, puhumaan, näkemään, kirjoittamaan, lisääntymään ja olemaan tietoinen olemassaolostaan.*

## Perceptron-malli

Oletetaan, että mallissamme on N ominaisuutta, jolloin syötevektori olisi kooltaan N. Perceptron on **binääriluokittelumalli**, eli se pystyy erottamaan kahdenlaiset syötedatat toisistaan. Oletamme, että jokaiselle syötevektorille x perceptronimme ulostulo on joko +1 tai -1 riippuen luokasta. Ulostulo lasketaan kaavalla:

y(x) = f(w<sup>T</sup>x)

missä f on askelaktivointifunktio

<!-- img src="http://www.sciweavers.org/tex2img.php?eq=f%28x%29%20%3D%20%5Cbegin%7Bcases%7D%0A%20%20%20%20%20%20%20%20%20%2B1%20%26%20x%20%5Cgeq%200%20%5C%5C%0A%20%20%20%20%20%20%20%20%20-1%20%26%20x%20%3C%200%0A%20%20%20%20%20%20%20%5Cend%7Bcases%7D%20%5C%5C%0A&bc=White&fc=Black&im=jpg&fs=12&ff=arev&edit=0" align="center" border="0" alt="f(x) = \begin{cases} +1 & x \geq 0 \\ -1 & x < 0 \end{cases} \\" width="154" height="50" / -->
<img src="images/activation-func.png"/>

## Perceptronin kouluttaminen

Perceptronin kouluttamiseksi meidän täytyy löytää painovektori w, joka luokittelee suurimman osan arvoista oikein, eli tuottaa pienimmän **virheen**. Tämä virhe E määritellään **perceptron-kriteerin** avulla seuraavasti:

E(w) = -∑w<sup>T</sup>x<sub>i</sub>t<sub>i</sub>

missä:

* summa otetaan niistä koulutusdatan pisteistä i, jotka luokitellaan väärin
* x<sub>i</sub> on syötedata ja t<sub>i</sub> on joko -1 tai +1 negatiivisille ja positiivisille esimerkeille vastaavasti.

Tätä kriteeriä pidetään painojen w funktiona, ja meidän täytyy minimoida se. Usein käytetään menetelmää nimeltä **gradienttimenetelmä**, jossa aloitetaan jollain alkuarvolla w<sup>(0)</sup> ja sitten jokaisessa vaiheessa päivitetään painot kaavan mukaan:

w<sup>(t+1)</sup> = w<sup>(t)</sup> - η∇E(w)

Tässä η on niin sanottu **oppimisnopeus**, ja ∇E(w) tarkoittaa E:n **gradienttia**. Kun gradientti on laskettu, päädytään seuraavaan:

w<sup>(t+1)</sup> = w<sup>(t)</sup> + ∑ηx<sub>i</sub>t<sub>i</sub>

Algoritmi Pythonilla näyttää tältä:

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

## Yhteenveto

Tässä oppitunnissa opit perceptronista, joka on binääriluokittelumalli, ja kuinka sitä koulutetaan käyttämällä painovektoria.

## 🚀 Haaste

Jos haluat kokeilla rakentaa oman perceptronin, kokeile [tätä Microsoft Learn -laboratoriota](https://docs.microsoft.com/en-us/azure/machine-learning/component-reference/two-class-averaged-perceptron?WT.mc_id=academic-77998-cacaste), joka käyttää [Azure ML -suunnittelijaa](https://docs.microsoft.com/en-us/azure/machine-learning/concept-designer?WT.mc_id=academic-77998-cacaste).

## [Jälkivisa](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/203)

## Kertaus ja itseopiskelu

Jos haluat nähdä, kuinka perceptronia voidaan käyttää sekä yksinkertaisten että todellisten ongelmien ratkaisemiseen, ja jatkaa oppimista, siirry [Perceptron](Perceptron.ipynb) -muistikirjaan.

Tässä on myös mielenkiintoinen [artikkeli perceptroneista](https://towardsdatascience.com/what-is-a-perceptron-basics-of-neural-networks-c4cfea20c590).

## [Tehtävä](lab/README.md)

Tässä oppitunnissa toteutimme perceptronin binääriluokittelutehtävää varten ja käytimme sitä kahden käsinkirjoitetun numeron luokitteluun. Tässä laboratoriossa sinun tehtäväsi on ratkaista numeroiden luokittelu kokonaisuudessaan, eli määrittää, mikä numero todennäköisimmin vastaa annettua kuvaa.

* [Ohjeet](lab/README.md)
* [Muistikirja](lab/PerceptronMultiClass.ipynb)

---

**Vastuuvapauslauseke**:  
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, huomioithan, että automaattiset käännökset voivat sisältää virheitä tai epätarkkuuksia. Alkuperäinen asiakirja sen alkuperäisellä kielellä tulisi pitää ensisijaisena lähteenä. Kriittisen tiedon osalta suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa väärinkäsityksistä tai virhetulkinnoista, jotka johtuvat tämän käännöksen käytöstä.