<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "0c37770bba4fff3c71dc00eb261ee61b",
  "translation_date": "2025-08-31T17:50:26+00:00",
  "source_file": "lessons/3-NeuralNetworks/03-Perceptron/README.md",
  "language_code": "lt"
}
-->
# Įvadas į neuroninius tinklus: Perceptronas

## [Prieš paskaitos testas](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/103)

Vienas iš pirmųjų bandymų sukurti kažką panašaus į šiuolaikinį neuroninį tinklą buvo atliktas Franko Rosenblatto iš Kornelio aeronautikos laboratorijos 1957 metais. Tai buvo aparatinės įrangos įgyvendinimas, pavadintas „Mark-1“, sukurtas atpažinti primityvias geometrines figūras, tokias kaip trikampiai, kvadratai ir apskritimai.

|      |      |
|--------------|-----------|
|<img src='images/Rosenblatt-wikipedia.jpg' alt='Frank Rosenblatt'/> | <img src='images/Mark_I_perceptron_wikipedia.jpg' alt='The Mark 1 Perceptron' />|

> Vaizdai [iš Vikipedijos](https://en.wikipedia.org/wiki/Perceptron)

Įvesties vaizdas buvo pateikiamas kaip 20x20 fotoląstelių masyvas, todėl neuroninis tinklas turėjo 400 įėjimų ir vieną dvejetainį išėjimą. Paprastas tinklas turėjo vieną neuroną, dar vadinamą **slenksčio logikos vienetu**. Neuroninio tinklo svoriai veikė kaip potenciometrai, kuriuos reikėjo rankiniu būdu reguliuoti mokymo metu.

> ✅ Potenciometras yra prietaisas, leidžiantis vartotojui reguliuoti grandinės varžą.

> Tuo metu „The New York Times“ rašė apie perceptroną: *elektroninio kompiuterio embrionas, kurį [karinis jūrų laivynas] tikisi, kad galės vaikščioti, kalbėti, matyti, rašyti, daugintis ir būti sąmoningas savo egzistencijos.*

## Perceptrono modelis

Tarkime, kad mūsų modelyje yra N savybių, tokiu atveju įvesties vektorius būtų N dydžio vektorius. Perceptronas yra **dvejetainės klasifikacijos** modelis, t. y. jis gali atskirti dviejų klasių įvesties duomenis. Mes prisiimsime, kad kiekvienam įvesties vektoriui x mūsų perceptrono išėjimas bus arba +1, arba -1, priklausomai nuo klasės. Išėjimas bus apskaičiuojamas pagal formulę:

y(x) = f(w<sup>T</sup>x)

kur f yra slenksčio aktyvavimo funkcija

<!-- img src="http://www.sciweavers.org/tex2img.php?eq=f%28x%29%20%3D%20%5Cbegin%7Bcases%7D%0A%20%20%20%20%20%20%20%20%20%2B1%20%26%20x%20%5Cgeq%200%20%5C%5C%0A%20%20%20%20%20%20%20%20%20-1%20%26%20x%20%3C%200%0A%20%20%20%20%20%20%20%5Cend%7Bcases%7D%20%5C%5C%0A&bc=White&fc=Black&im=jpg&fs=12&ff=arev&edit=0" align="center" border="0" alt="f(x) = \begin{cases} +1 & x \geq 0 \\ -1 & x < 0 \end{cases} \\" width="154" height="50" / -->
<img src="images/activation-func.png"/>

## Perceptrono mokymas

Norint išmokyti perceptroną, reikia rasti svorių vektorių w, kuris teisingai klasifikuotų daugumą reikšmių, t. y. duotų mažiausią **klaidą**. Ši klaida E apibrėžiama pagal **perceptrono kriterijų** taip:

E(w) = -∑w<sup>T</sup>x<sub>i</sub>t<sub>i</sub>

kur:

* suma imama iš tų mokymo duomenų taškų i, kurie duoda neteisingą klasifikaciją
* x<sub>i</sub> yra įvesties duomenys, o t<sub>i</sub> yra -1 arba +1 atitinkamai neigiamiems ir teigiamiems pavyzdžiams.

Šis kriterijus laikomas svorių w funkcija, ir mes turime ją minimizuoti. Dažnai naudojamas metodas, vadinamas **gradientiniu nusileidimu**, kuriame pradedame nuo pradinio svorio w<sup>(0)</sup>, o kiekviename žingsnyje atnaujiname svorius pagal formulę:

w<sup>(t+1)</sup> = w<sup>(t)</sup> - η∇E(w)

Čia η yra vadinamas **mokymosi greitis**, o ∇E(w) reiškia **gradientą** E. Po gradiento apskaičiavimo gauname:

w<sup>(t+1)</sup> = w<sup>(t)</sup> + ∑ηx<sub>i</sub>t<sub>i</sub>

Algoritmas Python kalba atrodo taip:

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

## Išvada

Šioje pamokoje sužinojote apie perceptroną, kuris yra dvejetainės klasifikacijos modelis, ir kaip jį išmokyti naudojant svorių vektorių.

## 🚀 Iššūkis

Jei norite pabandyti sukurti savo perceptroną, išbandykite [šį laboratorinį darbą Microsoft Learn platformoje](https://docs.microsoft.com/en-us/azure/machine-learning/component-reference/two-class-averaged-perceptron?WT.mc_id=academic-77998-cacaste), kuris naudoja [Azure ML dizainerį](https://docs.microsoft.com/en-us/azure/machine-learning/concept-designer?WT.mc_id=academic-77998-cacaste).

## [Po paskaitos testas](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/203)

## Apžvalga ir savarankiškas mokymasis

Norėdami pamatyti, kaip perceptronas gali būti naudojamas sprendžiant žaislinius ir realaus gyvenimo problemas, ir tęsti mokymąsi - eikite į [Perceptron](Perceptron.ipynb) užrašų knygelę.

Štai įdomus [straipsnis apie perceptronus](https://towardsdatascience.com/what-is-a-perceptron-basics-of-neural-networks-c4cfea20c590).

## [Užduotis](lab/README.md)

Šioje pamokoje mes įgyvendinome perceptroną dvejetainės klasifikacijos užduočiai ir panaudojome jį dviejų ranka rašytų skaitmenų klasifikavimui. Šiame laboratoriniame darbe jūsų prašoma visiškai išspręsti skaitmenų klasifikavimo problemą, t. y. nustatyti, kuris skaitmuo greičiausiai atitinka pateiktą vaizdą.

* [Instrukcijos](lab/README.md)
* [Užrašų knygelė](lab/PerceptronMultiClass.ipynb)

---

**Atsakomybės apribojimas**:  
Šis dokumentas buvo išverstas naudojant AI vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba turėtų būti laikomas autoritetingu šaltiniu. Kritinei informacijai rekomenduojama naudoti profesionalų žmogaus vertimą. Mes neprisiimame atsakomybės už nesusipratimus ar klaidingus interpretavimus, atsiradusius dėl šio vertimo naudojimo.