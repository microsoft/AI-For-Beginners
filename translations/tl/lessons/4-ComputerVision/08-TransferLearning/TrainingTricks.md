# Mga Tip sa Pagsasanay sa Deep Learning

Habang lumalalim ang mga neural network, nagiging mas mahirap ang kanilang proseso ng pagsasanay. Isang malaking problema dito ay ang tinatawag na [vanishing gradients](https://en.wikipedia.org/wiki/Vanishing_gradient_problem) o [exploding gradients](https://deepai.org/machine-learning-glossary-and-terms/exploding-gradient-problem#:~:text=Exploding%20gradients%20are%20a%20problem,updates%20are%20small%20and%20controlled.). [Ang post na ito](https://towardsdatascience.com/the-vanishing-exploding-gradient-problem-in-deep-neural-networks-191358470c11) ay nagbibigay ng magandang pagpapakilala tungkol sa mga problemang ito.

Upang maging mas mahusay ang pagsasanay ng malalalim na network, may ilang teknik na maaaring gamitin.

## Pagpapanatili ng mga halaga sa makatwirang pagitan

Upang gawing mas matatag ang mga numerikal na kalkulasyon, nais nating masiguro na ang lahat ng mga halaga sa loob ng ating neural network ay nasa makatwirang saklaw, karaniwan ay [-1..1] o [0..1]. Hindi ito isang mahigpit na kinakailangan, ngunit ang kalikasan ng floating point na mga kalkulasyon ay hindi nagpapahintulot na eksaktong maproseso nang sabay-sabay ang mga halagang may magkaibang magnitude. Halimbawa, kung pagsasamahin natin ang 10<sup>-10</sup> at 10<sup>10</sup>, malamang makakakuha tayo ng 10<sup>10</sup>, dahil ang mas maliit na halaga ay maaaring "ma-convert" sa parehong order ng mas malaking halaga, kaya mawawala ang mantissa.

Karamihan sa mga activation function ay may non-linearidad sa paligid ng [-1..1], kaya't makatuwiran na i-scale ang lahat ng input data sa pagitan ng [-1..1] o [0..1].

## Paunang Pag-inisyal ng Timbang

Sa ideal, nais nating ang mga halaga ay manatili sa parehong saklaw pagkatapos dumaan sa mga layer ng network. Kaya mahalaga ang pag-inisyal ng mga timbang sa paraang mapanatili ang distribusyon ng mga halaga.

Ang normal na distribusyon na **N(0,1)** ay hindi magandang ideya dahil kung mayroon tayong *n* inputs, ang standard deviation ng output ay magiging *&radic;n*, at malamang na lumalabas ang mga halaga mula sa interval na [0..1].

Kadalasang ginagamit ang mga sumusunod na pag-inisyal:

 * Uniform distribution -- `uniform`
 * **N(0,1/n)** -- `gaussian`
 * **N(0,1/&radic;n_in)** na garantisadong para sa mga input na may zero mean at standard deviation na 1, ang parehong mean/standard deviation ay mananatili
 * **N(0,&radic;2/(n_in+n_out))** -- tinatawag na **Xavier initialization** (`glorot`), nakatutulong ito upang mapanatili ang mga signals sa saklaw kapwa sa forward at backward propagation

## Batch Normalization

Kahit na may tamang weight initialization, ang mga timbang ay maaaring maging sobrang laki o sobrang liit habang nagsasanay, at magdadala sila ng mga signals sa labas ng tamang saklaw. Maaari nating ibalik ang mga signals sa tamang lugar sa pamamagitan ng paggamit ng isa sa mga teknik ng **normalization**. Bagamat may ilang uri nito (Weight normalization, Layer Normalization), ang pinaka-karaniwang ginagamit ay Batch Normalization.

Ang ideya ng **batch normalization** ay isaalang-alang ang lahat ng mga halaga sa buong minibatch, at isagawa ang normalisasyon (ibig sabihin ay ibawas ang mean at hatiin sa standard deviation) batay sa mga halagang iyon. Isinasagawa ito bilang isang layer ng network na gumagawa ng normalisasyon pagkatapos ilapat ang mga timbang, ngunit bago ang activation function. Bilang resulta, mas mataas ang posibilidad na makakita tayo ng mas mataas na final accuracy at mas mabilis na pagsasanay.

Narito ang [orihinal na papel](https://arxiv.org/pdf/1502.03167.pdf) tungkol sa batch normalization, ang [paliwanag sa Wikipedia](https://en.wikipedia.org/wiki/Batch_normalization), at [isang magandang blog post na pang-panimula](https://towardsdatascience.com/batch-normalization-in-3-levels-of-understanding-14c2da90a338) (at ang isa [sa wikang Russian](https://habrahabr.ru/post/309302/)).

## Dropout

Ang **Dropout** ay isang kawili-wiling teknik na nagtatanggal ng isang porsyento ng mga random na neuron habang nagsasanay. Isinasagawa rin ito bilang isang layer na may isang parametro (porsyento ng mga neuron na tatanggalin, karaniwang 10%-50%), at habang nagsasanay ay pinapalitan nito ng zero ang mga random na elemento ng input vector bago ito ipasa sa susunod na layer.

Bagamat parang kakaibang ideya ito, makikita mo ang epekto ng dropout sa pagsasanay ng MNIST digit classifier sa [`Dropout.ipynb`](Dropout.ipynb) notebook. Pinapabilis nito ang pagsasanay at pinapayagan tayong makamit ang mas mataas na accuracy sa mas kaunting mga epoch ng pagsasanay.

Ang epekto na ito ay maaaring ipaliwanag sa ilang paraan:

 * Maaari itong ituring bilang isang random na factor ng pagkagulat sa modelo, na nag-aalis ng optimisasyon mula sa lokal na minimum
 * Maaari itong ituring bilang *implicit model averaging*, dahil masasabi natin na habang may dropout ay nagsasanay tayo ng bahagyang magkakaibang modelo

> *Sinasabi ng ilan na kapag ang isang lasing na tao ay sumusubok matuto ng isang bagay, mas matatatandaan niya ito kinabukasan ng umaga kaysa sa isang matino, dahil ang utak na may ilang malfunctioning neurons ay sinusubukang umangkop nang mas mahusay upang maunawaan ang ibig sabihin. Hindi pa namin nasubukan ito kung totoo o hindi*

## Pag-iwas sa overfitting

Isang napakahalagang aspeto ng deep learning ay ang kakayahang maiwasan ang [overfitting](../../3-NeuralNetworks/05-Frameworks/Overfitting.md). Bagamat kaakit-akit gumamit ng napakapowerful na neural network model, dapat nating balansehin palagi ang bilang ng mga parameter ng modelo sa bilang ng mga training sample.

> Siguraduhing naiintindihan mo ang konsepto ng [overfitting](../../3-NeuralNetworks/05-Frameworks/Overfitting.md) na naipaliwanag namin kanina!

May ilang paraan upang maiwasan ang overfitting:

 * Early stopping -- patuloy na imonitor ang error sa validation set at ihinto ang pagsasanay kapag nagsimula itong tumaas.
 * Explicit Weight Decay / Regularization -- pagdaragdag ng dagdag na penalty sa loss function para sa mataas na absolute values ng mga timbang, na pumipigil sa modelo na magkaroon ng napakalaking hindi matatag na resulta
 * Model Averaging -- pagsasanay ng ilang mga modelo at pagkatapos ay pag-average ng resulta. Nakakatulong ito upang mabawasan ang variance.
 * Dropout (Implicit Model Averaging)

## Mga Optimizer / Algoritmo ng Pagsasanay

Isa pang mahalagang aspeto ng pagsasanay ay ang pagpili ng magandang training algorithm. Bagamat ang klasikong **gradient descent** ay makatwirang pagpipilian, minsan ito ay masyadong mabagal o nagdudulot ng iba pang problema.

Sa deep learning, ginagamit natin ang **Stochastic Gradient Descent** (SGD), na gradient descent na inilapat sa mga minibatch na random na pinili mula sa training set. Ina-adjust ang mga timbang gamit ang pormulang ito:

w<sup>t+1</sup> = w<sup>t</sup> - &eta;&nabla;&lagran;

### Momentum

Sa **momentum SGD**, iniingatan natin ang bahagi ng gradient mula sa mga naunang hakbang. Katulad ito ng paggalaw natin na may inertia, at kung makakatanggap tayo ng suntok sa ibang direksyon, hindi agad nagbabago ang ating trajectory, kundi pinananatili ang bahagi ng orihinal na galaw. Dito ipinakilala ang isa pang vector na v upang ipakita ang *bilis*:

* v<sup>t+1</sup> = &gamma; v<sup>t</sup> - &eta;&nabla;&lagran;
* w<sup>t+1</sup> = w<sup>t</sup>+v<sup>t+1</sup>

Ang parametro na &gamma; ay nagpapakita kung gaano kalaki ang epekto ng inertia: &gamma;=0 ay katumbas ng klasikong SGD; &gamma;=1 ay isang purong ekwasyon ng galaw.

### Adam, Adagrad, at iba pa

Dahil sa bawat layer, minumultiply natin ang mga signals ng isang matrix W<sub>i</sub>, depende sa ||W<sub>i</sub>||, ang gradient ay maaaring lumiit at maging malapit sa 0, o lumaki nang walang hanggan. Ito ang pinakapuso ng problema ng Exploding/Vanishing Gradients.

Isa sa mga solusyon sa problemang ito ay gamitin lamang ang direksyon ng gradient sa ekwasyon, at hindi pansinin ang absolute value, ibig sabihin:

w<sup>t+1</sup> = w<sup>t</sup> - &eta;(&nabla;&lagran;/||&nabla;&lagran;||), kung saan ||&nabla;&lagran;|| = &radic;&sum;(&nabla;&lagran;)<sup>2</sup>

Ang algoritmong ito ay tinatawag na **Adagrad**. Ang iba pang mga algoritmong gumagamit ng parehong ideya ay ang **RMSProp**, **Adam**.

> **Adam** ay itinuturing na isang napaka-epektibong algorithm para sa maraming aplikasyon, kaya kung hindi ka sigurado kung alin ang gagamitin - gamitin ang Adam.

### Gradient clipping

Ang gradient clipping ay isang pagpapalawig sa ideya sa itaas. Kapag ang ||&nabla;&lagran;|| &le; &theta;, isasaalang-alang ang orihinal na gradient sa optimization ng timbang, at kapag ||&nabla;&lagran;|| > &theta; - hinahati natin ang gradient sa kanyang norma. Dito, ang &theta; ay isang parametro, sa karamihan ng mga kaso maaari itong kunin na &theta;=1 o &theta;=10.

### Pagbaba ng learning rate

Madalas na nakadepende ang tagumpay ng pagsasanay sa parametrong learning rate na &eta;. May lohika na mas mataas na halaga ng &eta; ay nagreresulta sa mas mabilis na pagsasanay, na karaniwang gusto natin sa simula ng pagsasanay, at pagkatapos ay mas maliit na halaga ng &eta; ang nagpapahintulot sa atin na maayos na i-fine-tune ang network. Kaya sa karamihan ng kaso nais nating babaan ang &eta; habang nagpapatuloy ang pagsasanay.

Magagawa ito sa pamamagitan ng pag-multiply ng &eta; ng isang numero (hal. 0.98) pagkatapos ng bawat epoch ng pagsasanay, o sa paggamit ng mas kumplikadong **learning rate schedule**.

## Iba't ibang Arkitektura ng Network

Ang pagpili ng tamang arkitektura ng network para sa iyong problema ay maaaring maging mahirap. Karaniwan, pipili tayo ng arkitekturang napatunayang gumagana para sa ating partikular na gawain (o katulad nito). Narito ang isang [magandang kabuuang pagtingin](https://www.topbots.com/a-brief-history-of-neural-network-architectures/) sa mga arkitektura ng neural network para sa computer vision.

> Mahalaga na pumili ng arkitekturang sapat ang kapangyarihan para sa dami ng mga training sample na meron tayo. Ang pagpili ng napakamakapangyarihang modelo ay maaaring magresulta sa [overfitting](../../3-NeuralNetworks/05-Frameworks/Overfitting.md)

Isa pang magandang paraan ay ang paggamit ng arkitekturang kusang iaangkop ang kinakailangang komplikasyon. Sa ilang antas, ang **ResNet** na arkitektura at **Inception** ay self-adjusting. [Higit pa tungkol sa arkitektura sa computer vision](../07-ConvNets/CNN_Architectures.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Pagtatanggi**:
Ang dokumentong ito ay isinalin gamit ang serbisyo ng AI translation na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagama't nagsusumikap kami para sa katumpakan, pakatandaan na ang awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o hindi pagkakatugma. Ang orihinal na dokumento sa orihinal nitong wika ang dapat ituring na pangunahing sanggunian. Para sa mahahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang maling pagkakaintindi o maling interpretasyon na nagmula sa paggamit ng pagsasaling ito.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->