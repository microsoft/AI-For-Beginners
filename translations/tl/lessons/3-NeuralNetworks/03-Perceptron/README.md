<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "0c37770bba4fff3c71dc00eb261ee61b",
  "translation_date": "2025-08-28T02:38:20+00:00",
  "source_file": "lessons/3-NeuralNetworks/03-Perceptron/README.md",
  "language_code": "tl"
}
-->
# Panimula sa Neural Networks: Perceptron

## [Pre-lecture quiz](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/103)

Isa sa mga unang pagsubok na magpatupad ng isang bagay na katulad ng modernong neural network ay ginawa ni Frank Rosenblatt mula sa Cornell Aeronautical Laboratory noong 1957. Ito ay isang hardware implementation na tinawag na "Mark-1", na idinisenyo upang makilala ang mga simpleng geometric na hugis, tulad ng mga tatsulok, parisukat, at bilog.

|      |      |
|--------------|-----------|
|<img src='images/Rosenblatt-wikipedia.jpg' alt='Frank Rosenblatt'/> | <img src='images/Mark_I_perceptron_wikipedia.jpg' alt='The Mark 1 Perceptron' />|

> Mga larawan [mula sa Wikipedia](https://en.wikipedia.org/wiki/Perceptron)

Ang input na imahe ay kinakatawan ng 20x20 photocell array, kaya't ang neural network ay mayroong 400 inputs at isang binary output. Ang simpleng network ay naglalaman ng isang neuron, na tinatawag ding **threshold logic unit**. Ang mga weights ng neural network ay kumilos tulad ng mga potentiometer na kailangang manu-manong ayusin sa panahon ng training phase.

> ✅ Ang potentiometer ay isang aparato na nagpapahintulot sa gumagamit na ayusin ang resistance ng isang circuit.

> Sinulat ng New York Times tungkol sa perceptron noong panahong iyon: *ang embryo ng isang electronic computer na [ang Navy] inaasahan na makakalakad, makakapagsalita, makakakita, makakasulat, makakapagparami ng sarili, at magiging mulat sa kanyang pag-iral.*

## Modelo ng Perceptron

Ipagpalagay natin na mayroon tayong N features sa ating modelo, kung saan ang input vector ay magiging isang vector na may sukat na N. Ang perceptron ay isang modelo ng **binary classification**, ibig sabihin, kaya nitong makilala ang dalawang klase ng input na data. Ipagpalagay natin na para sa bawat input vector x, ang output ng ating perceptron ay magiging +1 o -1, depende sa klase. Ang output ay kakalkulahin gamit ang formula:

y(x) = f(w<sup>T</sup>x)

kung saan ang f ay isang step activation function

<!-- img src="http://www.sciweavers.org/tex2img.php?eq=f%28x%29%20%3D%20%5Cbegin%7Bcases%7D%0A%20%20%20%20%20%20%20%20%20%2B1%20%26%20x%20%5Cgeq%200%20%5C%5C%0A%20%20%20%20%20%20%20%20%20-1%20%26%20x%20%3C%200%0A%20%20%20%20%20%20%20%5Cend%7Bcases%7D%20%5C%5C%0A&bc=White&fc=Black&im=jpg&fs=12&ff=arev&edit=0" align="center" border="0" alt="f(x) = \begin{cases} +1 & x \geq 0 \\ -1 & x < 0 \end{cases} \\" width="154" height="50" / -->
<img src="images/activation-func.png"/>

## Pagsasanay ng Perceptron

Upang sanayin ang isang perceptron, kailangan nating hanapin ang weights vector w na nag-uuri ng karamihan sa mga halaga nang tama, ibig sabihin, nagreresulta sa pinakamaliit na **error**. Ang error na E ay tinutukoy ng **perceptron criterion** sa sumusunod na paraan:

E(w) = -∑w<sup>T</sup>x<sub>i</sub>t<sub>i</sub>

kung saan:

* ang kabuuan ay kinukuha sa mga training data points i na nagreresulta sa maling classification
* x<sub>i</sub> ay ang input na data, at t<sub>i</sub> ay alinman sa -1 o +1 para sa negatibo at positibong halimbawa ayon sa pagkakabanggit.

Ang criterion na ito ay itinuturing bilang isang function ng weights w, at kailangan nating i-minimize ito. Madalas, ginagamit ang isang paraan na tinatawag na **gradient descent**, kung saan nagsisimula tayo sa ilang initial weights w<sup>(0)</sup>, at pagkatapos sa bawat hakbang ay ina-update ang weights ayon sa formula:

w<sup>(t+1)</sup> = w<sup>(t)</sup> - η∇E(w)

Dito, ang η ay tinatawag na **learning rate**, at ang ∇E(w) ay tumutukoy sa **gradient** ng E. Pagkatapos kalkulahin ang gradient, makakakuha tayo ng:

w<sup>(t+1)</sup> = w<sup>(t)</sup> + ∑ηx<sub>i</sub>t<sub>i</sub>

Ang algorithm sa Python ay ganito:

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

## Konklusyon

Sa araling ito, natutunan mo ang tungkol sa perceptron, na isang binary classification model, at kung paano ito sanayin gamit ang weights vector.

## 🚀 Hamon

Kung nais mong subukang gumawa ng sarili mong perceptron, subukan ang [lab na ito sa Microsoft Learn](https://docs.microsoft.com/en-us/azure/machine-learning/component-reference/two-class-averaged-perceptron?WT.mc_id=academic-77998-cacaste) na gumagamit ng [Azure ML designer](https://docs.microsoft.com/en-us/azure/machine-learning/concept-designer?WT.mc_id=academic-77998-cacaste).

## [Post-lecture quiz](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/203)

## Review at Pag-aaral ng Sarili

Upang makita kung paano natin magagamit ang perceptron upang lutasin ang isang simpleng problema pati na rin ang mga totoong problema, at upang ipagpatuloy ang pag-aaral - pumunta sa [Perceptron](Perceptron.ipynb) notebook.

Narito ang isang kawili-wiling [artikulo tungkol sa perceptrons](https://towardsdatascience.com/what-is-a-perceptron-basics-of-neural-networks-c4cfea20c590).

## [Takdang Aralin](lab/README.md)

Sa araling ito, nagpatupad tayo ng perceptron para sa binary classification task, at ginamit natin ito upang uriin ang pagitan ng dalawang handwritten digits. Sa lab na ito, hinihiling sa iyo na lutasin ang problema ng digit classification nang buo, ibig sabihin, tukuyin kung aling digit ang pinaka-malamang na tumutugma sa isang ibinigay na imahe.

* [Mga Instruksyon](lab/README.md)
* [Notebook](lab/PerceptronMultiClass.ipynb)

---

**Paunawa**:  
Ang dokumentong ito ay isinalin gamit ang AI translation service na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagama't sinisikap naming maging tumpak, tandaan na ang mga awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o hindi pagkakatugma. Ang orihinal na dokumento sa kanyang katutubong wika ang dapat ituring na opisyal na sanggunian. Para sa mahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang hindi pagkakaunawaan o maling interpretasyon na maaaring magmula sa paggamit ng pagsasaling ito.