<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "186bf7eeab776b36f557357ea56d4751",
  "translation_date": "2025-08-28T02:37:47+00:00",
  "source_file": "lessons/3-NeuralNetworks/04-OwnFramework/README.md",
  "language_code": "tl"
}
-->
# Panimula sa Neural Networks. Multi-Layered Perceptron

Sa nakaraang seksyon, natutunan mo ang tungkol sa pinakasimpleng modelo ng neural network - ang one-layered perceptron, isang linear na modelo para sa two-class classification.

Sa seksyong ito, palalawakin natin ang modelong ito sa isang mas flexible na framework, na magpapahintulot sa atin na:

* magsagawa ng **multi-class classification** bukod sa two-class
* lutasin ang **regression problems** bukod sa classification
* paghiwalayin ang mga klase na hindi linear na nahihiwalay

Bubuo rin tayo ng sarili nating modular framework sa Python na magpapahintulot sa atin na magdisenyo ng iba't ibang neural network architectures.

## [Pre-lecture quiz](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/104)

## Pormalisasyon ng Machine Learning

Magsimula tayo sa pormalisasyon ng problema sa Machine Learning. Ipagpalagay natin na mayroon tayong training dataset na **X** na may mga label na **Y**, at kailangan nating bumuo ng modelong *f* na gagawa ng pinakatumpak na prediksyon. Ang kalidad ng prediksyon ay sinusukat gamit ang **Loss function** ℒ. Ang mga sumusunod na loss functions ay madalas gamitin:

* Para sa regression problem, kung saan kailangan nating magpredik ng numero, maaari nating gamitin ang **absolute error** ∑<sub>i</sub>|f(x<sup>(i)</sup>)-y<sup>(i)</sup>|, o **squared error** ∑<sub>i</sub>(f(x<sup>(i)</sup>)-y<sup>(i)</sup>)<sup>2</sup>
* Para sa classification, ginagamit natin ang **0-1 loss** (na mahalagang kapareho ng **accuracy** ng modelo), o **logistic loss**.

Para sa one-level perceptron, ang function na *f* ay naidefine bilang isang linear function *f(x)=wx+b* (kung saan ang *w* ay ang weight matrix, *x* ay ang vector ng input features, at *b* ay bias vector). Para sa iba't ibang neural network architectures, ang function na ito ay maaaring magkaroon ng mas kumplikadong anyo.

> Sa kaso ng classification, madalas na mas kanais-nais na makuha ang mga probabilidad ng mga kaukulang klase bilang output ng network. Upang i-convert ang arbitraryong mga numero sa probabilidad (hal. upang i-normalize ang output), madalas nating ginagamit ang **softmax** function σ, at ang function na *f* ay nagiging *f(x)=σ(wx+b)*

Sa depinisyon ng *f* sa itaas, ang *w* at *b* ay tinatawag na **parameters** θ=⟨*w,b*⟩. Sa ibinigay na dataset ⟨**X**,**Y**⟩, maaari nating kalkulahin ang kabuuang error sa buong dataset bilang isang function ng parameters θ.

> ✅ **Ang layunin ng neural network training ay bawasan ang error sa pamamagitan ng pagbabago ng parameters θ**

## Gradient Descent Optimization

Mayroong isang kilalang paraan ng pag-optimize ng function na tinatawag na **gradient descent**. Ang ideya ay maaari nating kalkulahin ang derivative (sa multi-dimensional na kaso tinatawag na **gradient**) ng loss function kaugnay ng parameters, at baguhin ang parameters sa paraang mababawasan ang error. Maaari itong ipormalisa sa ganitong paraan:

* I-initialize ang parameters gamit ang ilang random na halaga w<sup>(0)</sup>, b<sup>(0)</sup>
* Ulitin ang sumusunod na hakbang nang maraming beses:
    - w<sup>(i+1)</sup> = w<sup>(i)</sup>-η∂ℒ/∂w
    - b<sup>(i+1)</sup> = b<sup>(i)</sup>-η∂ℒ/∂b

Sa panahon ng training, ang mga optimization steps ay dapat kalkulahin gamit ang buong dataset (tandaan na ang loss ay kinakalkula bilang kabuuan sa lahat ng training samples). Gayunpaman, sa totoong buhay, kumukuha tayo ng maliliit na bahagi ng dataset na tinatawag na **minibatches**, at kinakalkula ang gradients batay sa subset ng data. Dahil ang subset ay kinukuha nang random sa bawat pagkakataon, ang pamamaraang ito ay tinatawag na **stochastic gradient descent** (SGD).

## Multi-Layered Perceptrons at Backpropagation

Ang one-layer network, tulad ng nakita natin sa itaas, ay may kakayahang mag-classify ng mga klase na linear na nahihiwalay. Upang makabuo ng mas mayamang modelo, maaari nating pagsamahin ang ilang layer ng network. Sa matematika, nangangahulugan ito na ang function na *f* ay magkakaroon ng mas kumplikadong anyo, at kakalkulahin sa ilang hakbang:
* z<sub>1</sub>=w<sub>1</sub>x+b<sub>1</sub>
* z<sub>2</sub>=w<sub>2</sub>α(z<sub>1</sub>)+b<sub>2</sub>
* f = σ(z<sub>2</sub>)

Dito, ang α ay isang **non-linear activation function**, ang σ ay isang softmax function, at ang parameters θ=<*w<sub>1</sub>,b<sub>1</sub>,w<sub>2</sub>,b<sub>2</sub>*>.

Mananatili ang gradient descent algorithm, ngunit magiging mas mahirap ang pagkalkula ng gradients. Gamit ang chain differentiation rule, maaari nating kalkulahin ang derivatives bilang:

* ∂ℒ/∂w<sub>2</sub> = (∂ℒ/∂σ)(∂σ/∂z<sub>2</sub>)(∂z<sub>2</sub>/∂w<sub>2</sub>)
* ∂ℒ/∂w<sub>1</sub> = (∂ℒ/∂σ)(∂σ/∂z<sub>2</sub>)(∂z<sub>2</sub>/∂α)(∂α/∂z<sub>1</sub>)(∂z<sub>1</sub>/∂w<sub>1</sub>)

> ✅ Ang chain differentiation rule ay ginagamit upang kalkulahin ang derivatives ng loss function kaugnay ng parameters.

Pansinin na ang pinakakaliwang bahagi ng lahat ng mga ekspresyon na ito ay pareho, kaya't maaari nating epektibong kalkulahin ang derivatives simula sa loss function at bumalik "pabalik" sa computational graph. Kaya't ang paraan ng pag-train ng multi-layered perceptron ay tinatawag na **backpropagation**, o 'backprop'.

<img alt="compute graph" src="images/ComputeGraphGrad.png"/>

> TODO: banggitin ang pinagmulan ng larawan

> ✅ Tatalakayin natin ang backprop nang mas detalyado sa ating notebook na halimbawa.  

## Konklusyon

Sa araling ito, bumuo tayo ng sarili nating neural network library, at ginamit natin ito para sa isang simpleng two-dimensional classification task.

## 🚀 Hamon

Sa kalakip na notebook, ipapatupad mo ang sarili mong framework para sa pagbuo at pag-train ng multi-layered perceptrons. Makikita mo nang detalyado kung paano gumagana ang mga modernong neural networks.

Magpatuloy sa [OwnFramework](OwnFramework.ipynb) notebook at gawin ito.

## [Post-lecture quiz](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/204)

## Review at Pag-aaral sa Sarili

Ang backpropagation ay isang karaniwang algorithm na ginagamit sa AI at ML, na mainam pag-aralan [nang mas detalyado](https://wikipedia.org/wiki/Backpropagation)

## [Gawain](lab/README.md)

Sa lab na ito, hinihiling kang gamitin ang framework na binuo mo sa araling ito upang lutasin ang MNIST handwritten digit classification.

* [Mga Instruksyon](lab/README.md)
* [Notebook](lab/MyFW_MNIST.ipynb)

---

**Paunawa**:  
Ang dokumentong ito ay isinalin gamit ang AI translation service na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagama't sinisikap naming maging tumpak, tandaan na ang mga awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o hindi pagkakatugma. Ang orihinal na dokumento sa kanyang katutubong wika ang dapat ituring na opisyal na sanggunian. Para sa mahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang hindi pagkakaunawaan o maling interpretasyon na dulot ng paggamit ng pagsasaling ito.