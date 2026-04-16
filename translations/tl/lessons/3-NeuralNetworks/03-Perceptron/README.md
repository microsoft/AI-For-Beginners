# Panimula sa Neural Networks: Perceptron

## [Pre-lecture quiz](https://ff-quizzes.netlify.app/en/ai/quiz/5)

Isa sa mga unang pagsubok na lumikha ng isang bagay na katulad ng modernong neural network ay ginawa ni Frank Rosenblatt mula sa Cornell Aeronautical Laboratory noong 1957. Ito ay isang hardware implementation na tinawag na "Mark-1", na idinisenyo upang makilala ang mga simpleng geometric na hugis tulad ng tatsulok, parisukat, at bilog.

|      |      |
|--------------|-----------|
|<img src='../../../../../translated_images/tl/Rosenblatt-wikipedia.294821b285ac796d.webp' alt='Frank Rosenblatt'/> | <img src='../../../../../translated_images/tl/Mark_I_perceptron_wikipedia.1f84eaa2d4b76ec9.webp' alt='The Mark 1 Perceptron' />|

> Mga larawan [mula sa Wikipedia](https://en.wikipedia.org/wiki/Perceptron)

Ang input na imahe ay kinakatawan ng 20x20 photocell array, kaya't ang neural network ay mayroong 400 inputs at isang binary output. Ang simpleng network ay naglalaman ng isang neuron, na tinatawag ding **threshold logic unit**. Ang mga weights ng neural network ay kumilos tulad ng mga potentiometer na kailangang manu-manong ayusin sa panahon ng training phase.

> ✅ Ang potentiometer ay isang device na nagbibigay-daan sa user na ayusin ang resistance ng isang circuit.

> Sinulat ng New York Times tungkol sa perceptron noong panahong iyon: *ang embryo ng isang electronic computer na [ang Navy] inaasahan na makakalakad, makakapagsalita, makakakita, makakasulat, makakapagparami ng sarili, at magiging malay sa kanyang pag-iral.*

## Modelo ng Perceptron

Ipagpalagay natin na mayroon tayong N features sa ating modelo, kung saan ang input vector ay magiging isang vector na may sukat na N. Ang perceptron ay isang modelo ng **binary classification**, ibig sabihin, kaya nitong makilala ang dalawang klase ng input data. Ipagpalagay natin na para sa bawat input vector x, ang output ng ating perceptron ay magiging +1 o -1, depende sa klase. Ang output ay kakalkulahin gamit ang formula:

y(x) = f(w<sup>T</sup>x)

kung saan ang f ay isang step activation function

<img src="../../../../../translated_images/tl/activation-func.b4924007c7ce7764.webp"/>

## Pagsasanay ng Perceptron

Upang sanayin ang isang perceptron, kailangan nating hanapin ang weights vector w na nagkaklasipika ng karamihan sa mga values nang tama, ibig sabihin, nagreresulta sa pinakamaliit na **error**. Ang error na E ay tinutukoy ng **perceptron criterion** sa ganitong paraan:

E(w) = -&sum;w<sup>T</sup>x<sub>i</sub>t<sub>i</sub>

kung saan:

* ang sum ay kinukuha sa mga training data points i na nagreresulta sa maling classification
* x<sub>i</sub> ay ang input data, at t<sub>i</sub> ay alinman sa -1 o +1 para sa negative at positive examples ayon sa pagkakabanggit.

Ang criterion na ito ay itinuturing bilang isang function ng weights w, at kailangan natin itong i-minimize. Madalas, ginagamit ang isang method na tinatawag na **gradient descent**, kung saan nagsisimula tayo sa ilang initial weights w<sup>(0)</sup>, at pagkatapos sa bawat hakbang ay ina-update ang weights ayon sa formula:

w<sup>(t+1)</sup> = w<sup>(t)</sup> - &eta;&nabla;E(w)

Dito, ang &eta; ay tinatawag na **learning rate**, at ang &nabla;E(w) ay tumutukoy sa **gradient** ng E. Pagkatapos kalkulahin ang gradient, makakakuha tayo ng:

w<sup>(t+1)</sup> = w<sup>(t)</sup> + &sum;&eta;x<sub>i</sub>t<sub>i</sub>

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

## [Post-lecture quiz](https://ff-quizzes.netlify.app/en/ai/quiz/6)

## Review at Pag-aaral sa Sarili

Upang makita kung paano natin magagamit ang perceptron upang lutasin ang isang simpleng problema pati na rin ang mga totoong problema, at upang ipagpatuloy ang pag-aaral - pumunta sa [Perceptron](Perceptron.ipynb) notebook.

Narito ang isang kawili-wiling [artikulo tungkol sa perceptrons](https://towardsdatascience.com/what-is-a-perceptron-basics-of-neural-networks-c4cfea20c590).

## [Takdang Aralin](lab/README.md)

Sa araling ito, nag-implement tayo ng perceptron para sa binary classification task, at ginamit natin ito upang magklasipika sa pagitan ng dalawang handwritten digits. Sa lab na ito, hinihiling sa iyo na lutasin ang problema ng digit classification nang buo, ibig sabihin, tukuyin kung aling digit ang pinaka-malamang na tumutugma sa isang ibinigay na imahe.

* [Mga Instruksyon](lab/README.md)
* [Notebook](lab/PerceptronMultiClass.ipynb)

---

