# Mga Teknik sa Pagsasanay ng Deep Learning

Habang lumalalim ang mga neural network, nagiging mas mahirap ang proseso ng kanilang pagsasanay. Isa sa mga pangunahing problema ay ang tinatawag na [vanishing gradients](https://en.wikipedia.org/wiki/Vanishing_gradient_problem) o [exploding gradients](https://deepai.org/machine-learning-glossary-and-terms/exploding-gradient-problem#:~:text=Exploding%20gradients%20are%20a%20problem,updates%20are%20small%20and%20controlled.). [Ang post na ito](https://towardsdatascience.com/the-vanishing-exploding-gradient-problem-in-deep-neural-networks-191358470c11) ay nagbibigay ng magandang pagpapakilala sa mga problemang ito.

Upang gawing mas epektibo ang pagsasanay ng malalalim na network, may ilang mga teknik na maaaring gamitin.

## Panatilihin ang mga Halaga sa Katanggap-tanggap na Saklaw

Upang gawing mas matatag ang mga numerikal na kalkulasyon, nais nating tiyakin na ang lahat ng halaga sa loob ng ating neural network ay nasa katanggap-tanggap na saklaw, karaniwang [-1..1] o [0..1]. Hindi ito isang mahigpit na kinakailangan, ngunit ang kalikasan ng floating point computations ay tulad na ang mga halaga ng magkaibang magnitude ay hindi maaaring ma-manipula nang tumpak nang magkasama. Halimbawa, kung magdadagdag tayo ng 10<sup>-10</sup> at 10<sup>10</sup>, malamang na makuha natin ang 10<sup>10</sup>, dahil ang mas maliit na halaga ay "maiko-convert" sa parehong order ng mas malaking halaga, at mawawala ang mantissa.

Karamihan sa mga activation function ay may non-linearities sa paligid ng [-1..1], kaya’t makatuwirang i-scale ang lahat ng input data sa saklaw na [-1..1] o [0..1].

## Paunang Pag-inisyalisa ng Timbang

Sa ideal na sitwasyon, nais nating ang mga halaga ay nasa parehong saklaw pagkatapos dumaan sa mga layer ng network. Kaya’t mahalagang i-inisyalisa ang mga timbang sa paraang mapapanatili ang distribusyon ng mga halaga.

Ang normal na distribusyon **N(0,1)** ay hindi magandang ideya, dahil kung mayroon tayong *n* na input, ang standard deviation ng output ay magiging *n*, at malamang na lumabas ang mga halaga sa saklaw na [0..1].

Ang mga sumusunod na inisyalisa ay madalas gamitin:

- Uniform distribution -- `uniform`
- **N(0,1/n)** -- `gaussian`
- **N(0,1/√n_in)** na nagsisiguro na para sa mga input na may zero mean at standard deviation na 1, mananatili ang parehong mean/standard deviation
- **N(0,√2/(n_in+n_out))** -- tinatawag na **Xavier initialization** (`glorot`), na tumutulong upang mapanatili ang mga signal sa saklaw sa parehong forward at backward propagation

## Batch Normalization

Kahit na may tamang inisyalisa ng timbang, maaaring maging napakalaki o napakaliit ng mga timbang sa panahon ng pagsasanay, na magdadala sa mga signal sa labas ng tamang saklaw. Maaari nating ibalik ang mga signal sa tamang saklaw gamit ang isa sa mga teknik ng **normalization**. Habang may ilang mga teknik (Weight normalization, Layer Normalization), ang pinakakaraniwang ginagamit ay ang Batch Normalization.

Ang ideya ng **batch normalization** ay isaalang-alang ang lahat ng halaga sa minibatch, at magsagawa ng normalization (hal., ibawas ang mean at hatiin sa standard deviation) batay sa mga halagang iyon. Ito ay ipinatutupad bilang isang network layer na gumagawa ng normalization pagkatapos ilapat ang mga timbang, ngunit bago ang activation function. Bilang resulta, mas mataas ang posibilidad na makamit ang mas mataas na panghuling accuracy at mas mabilis na pagsasanay.

Narito ang [orihinal na papel](https://arxiv.org/pdf/1502.03167.pdf) tungkol sa batch normalization, ang [paliwanag sa Wikipedia](https://en.wikipedia.org/wiki/Batch_normalization), at [isang magandang introductory blog post](https://towardsdatascience.com/batch-normalization-in-3-levels-of-understanding-14c2da90a338) (at ang isa [sa Russian](https://habrahabr.ru/post/309302/)).

## Dropout

Ang **Dropout** ay isang kawili-wiling teknik na nag-aalis ng isang tiyak na porsyento ng mga random na neuron sa panahon ng pagsasanay. Ito ay ipinatutupad din bilang isang layer na may isang parameter (porsyento ng mga neuron na aalisin, karaniwang 10%-50%), at sa panahon ng pagsasanay, ito ay nagze-zero ng mga random na elemento ng input vector bago ito ipasa sa susunod na layer.

Bagama’t maaaring mukhang kakaiba ang ideyang ito, makikita mo ang epekto ng dropout sa pagsasanay ng MNIST digit classifier sa [`Dropout.ipynb`](Dropout.ipynb) notebook. Pinapabilis nito ang pagsasanay at nagbibigay-daan sa atin na makamit ang mas mataas na accuracy sa mas kaunting training epochs.

Ang epekto na ito ay maaaring ipaliwanag sa ilang paraan:

- Maaari itong ituring bilang isang random na "shock" factor sa modelo, na nag-aalis sa optimization mula sa local minimum
- Maaari itong ituring bilang *implicit model averaging*, dahil maaari nating sabihin na sa panahon ng dropout, sinasanay natin ang bahagyang magkaibang modelo

> *May ilang nagsasabi na kapag ang isang lasing na tao ay nag-aaral ng isang bagay, mas maaalala niya ito kinabukasan kumpara sa isang taong hindi lasing, dahil ang utak na may ilang hindi gumaganang neuron ay mas nag-a-adjust upang maunawaan ang kahulugan. Hindi pa namin nasubukan kung totoo ito o hindi.*

## Pag-iwas sa Overfitting

Isa sa mga napakahalagang aspeto ng deep learning ay ang maiwasan ang [overfitting](../../3-NeuralNetworks/05-Frameworks/Overfitting.md). Bagama’t maaaring nakakaakit na gumamit ng napakalakas na modelo ng neural network, dapat nating palaging balansehin ang bilang ng mga parameter ng modelo sa bilang ng mga training samples.

> Siguraduhing nauunawaan mo ang konsepto ng [overfitting](../../3-NeuralNetworks/05-Frameworks/Overfitting.md) na naipakilala na natin!

May ilang paraan upang maiwasan ang overfitting:

- Early stopping -- patuloy na subaybayan ang error sa validation set at itigil ang pagsasanay kapag nagsimulang tumaas ang validation error.
- Explicit Weight Decay / Regularization -- magdagdag ng karagdagang parusa sa loss function para sa mataas na absolute values ng weights, na pumipigil sa modelo na magbigay ng napaka-unstable na resulta
- Model Averaging -- pagsasanay ng ilang mga modelo at pagkatapos ay pag-average ng resulta. Nakakatulong ito upang mabawasan ang variance.
- Dropout (Implicit Model Averaging)

## Mga Optimizer / Algorithm sa Pagsasanay

Isa pang mahalagang aspeto ng pagsasanay ay ang pumili ng magandang algorithm sa pagsasanay. Bagama’t ang klasikong **gradient descent** ay isang makatwirang pagpipilian, maaari itong minsan ay masyadong mabagal, o magresulta sa iba pang mga problema.

Sa deep learning, ginagamit natin ang **Stochastic Gradient Descent** (SGD), na isang gradient descent na inilalapat sa minibatches, na random na pinili mula sa training set. Ina-adjust ang mga timbang gamit ang pormulang ito:

w<sup>t+1</sup> = w<sup>t</sup> - η∇ℒ

### Momentum

Sa **momentum SGD**, pinapanatili natin ang bahagi ng gradient mula sa mga nakaraang hakbang. Katulad ito ng kapag tayo ay gumagalaw na may inertia, at nakatanggap tayo ng tulak sa ibang direksyon, ang ating trajectory ay hindi agad nagbabago, ngunit pinapanatili ang bahagi ng orihinal na galaw. Narito ang isa pang vector v upang kumatawan sa *bilis*:

- v<sup>t+1</sup> = γ v<sup>t</sup> - η∇ℒ
- w<sup>t+1</sup> = w<sup>t</sup>+v<sup>t+1</sup>

Ang parameter na γ ay nagpapahiwatig kung gaano kalaki ang isinasaalang-alang natin ang inertia: γ=0 ay tumutugma sa klasikong SGD; γ=1 ay isang purong equation ng galaw.

### Adam, Adagrad, atbp.

Dahil sa bawat layer ay pinararami natin ang mga signal ng ilang matrix W<sub>i</sub>, depende sa ||W<sub>i</sub>||, ang gradient ay maaaring lumiit at maging malapit sa 0, o tumaas nang walang hanggan. Ito ang esensya ng Exploding/Vanishing Gradients problem.

Isa sa mga solusyon sa problemang ito ay gamitin lamang ang direksyon ng gradient sa equation, at huwag pansinin ang absolute value, hal.,

w<sup>t+1</sup> = w<sup>t</sup> - η(∇ℒ/||∇ℒ||), kung saan ||∇ℒ|| = √∑(∇ℒ)<sup>2</sup>

Ang algorithm na ito ay tinatawag na **Adagrad**. Ang iba pang mga algorithm na gumagamit ng parehong ideya: **RMSProp**, **Adam**

> **Adam** ay itinuturing na isang napaka-epektibong algorithm para sa maraming aplikasyon, kaya kung hindi ka sigurado kung alin ang gagamitin - gamitin ang Adam.

### Gradient Clipping

Ang gradient clipping ay isang extension ng ideya sa itaas. Kapag ang ||∇ℒ|| ≤ θ, isinasaalang-alang natin ang orihinal na gradient sa weight optimization, at kapag ||∇ℒ|| > θ - hinahati natin ang gradient sa norm nito. Ang θ ay isang parameter, sa karamihan ng mga kaso maaari nating kunin ang θ=1 o θ=10.

### Learning Rate Decay

Ang tagumpay ng pagsasanay ay madalas na nakadepende sa learning rate parameter na η. Makatuwirang isipin na ang mas malalaking halaga ng η ay nagreresulta sa mas mabilis na pagsasanay, na karaniwang nais natin sa simula ng pagsasanay, at pagkatapos ay mas maliit na halaga ng η ang nagpapahintulot sa atin na i-fine-tune ang network. Kaya, sa karamihan ng mga kaso nais nating bawasan ang η sa proseso ng pagsasanay.

Magagawa ito sa pamamagitan ng pag-multiply ng η sa ilang numero (hal., 0.98) pagkatapos ng bawat epoch ng pagsasanay, o sa pamamagitan ng paggamit ng mas komplikadong **learning rate schedule**.

## Iba't Ibang Arkitektura ng Network

Ang pagpili ng tamang arkitektura ng network para sa iyong problema ay maaaring maging mahirap. Karaniwan, pipili tayo ng arkitektura na napatunayang gumagana para sa ating partikular na gawain (o katulad nito). Narito ang isang [magandang overview](https://www.topbots.com/a-brief-history-of-neural-network-architectures/) ng mga neural network architectures para sa computer vision.

> Mahalagang pumili ng arkitektura na sapat na makapangyarihan para sa bilang ng mga training samples na mayroon tayo. Ang pagpili ng sobrang makapangyarihang modelo ay maaaring magresulta sa [overfitting](../../3-NeuralNetworks/05-Frameworks/Overfitting.md).

Isa pang magandang paraan ay ang paggamit ng arkitektura na awtomatikong nag-a-adjust sa kinakailangang kumplikado. Sa ilang antas, ang **ResNet** na arkitektura at **Inception** ay self-adjusting. [Higit pa sa mga arkitektura ng computer vision](../07-ConvNets/CNN_Architectures.md)

---

**Paunawa**:  
Ang dokumentong ito ay isinalin gamit ang AI translation service na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagama't sinisikap naming maging tumpak, tandaan na ang mga awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o hindi pagkakatugma. Ang orihinal na dokumento sa kanyang katutubong wika ang dapat ituring na opisyal na sanggunian. Para sa mahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang hindi pagkakaunawaan o maling interpretasyon na dulot ng paggamit ng pagsasaling ito.