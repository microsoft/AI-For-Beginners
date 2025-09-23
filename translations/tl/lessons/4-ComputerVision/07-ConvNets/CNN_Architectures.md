<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "2f7b97b375358cb51a1e098df306bf73",
  "translation_date": "2025-08-28T02:29:54+00:00",
  "source_file": "lessons/4-ComputerVision/07-ConvNets/CNN_Architectures.md",
  "language_code": "tl"
}
-->
# Mga Kilalang Arkitektura ng CNN

### VGG-16

Ang VGG-16 ay isang network na nakamit ang 92.7% na katumpakan sa ImageNet top-5 classification noong 2014. Ito ay may sumusunod na istruktura ng layer:

![ImageNet Layers](../../../../../translated_images/vgg-16-arch1.d901a5583b3a51baeaab3e768567d921e5d54befa46e1e642616c5458c934028.tl.jpg)

Tulad ng nakikita mo, sinusunod ng VGG ang tradisyunal na pyramid architecture, na isang sunod-sunod na convolution-pooling layers.

![ImageNet Pyramid](../../../../../translated_images/vgg-16-arch.64ff2137f50dd49fdaa786e3f3a975b3f22615efd13efb19c5d22f12e01451a1.tl.jpg)

> Larawan mula sa [Researchgate](https://www.researchgate.net/figure/Vgg16-model-structure-To-get-the-VGG-NIN-model-we-replace-the-2-nd-4-th-6-th-7-th_fig2_335194493)

### ResNet

Ang ResNet ay isang pamilya ng mga modelo na iminungkahi ng Microsoft Research noong 2015. Ang pangunahing ideya ng ResNet ay ang paggamit ng **residual blocks**:

<img src="images/resnet-block.png" width="300"/>

> Larawan mula sa [papel na ito](https://arxiv.org/pdf/1512.03385.pdf)

Ang dahilan ng paggamit ng identity pass-through ay upang ang layer ay mag-predict ng **pagkakaiba** sa pagitan ng resulta ng nakaraang layer at ng output ng residual block - kaya tinawag itong *residual*. Ang mga blocks na ito ay mas madaling i-train, at maaaring bumuo ng mga network na may daan-daang ganitong blocks (ang mga karaniwang variant ay ResNet-52, ResNet-101, at ResNet-152).

Maaari mo ring isipin ang network na ito bilang may kakayahang i-adjust ang complexity nito sa dataset. Sa simula, kapag sinisimulan mong i-train ang network, ang mga weight values ay maliit, at karamihan ng signal ay dumadaan sa identity layers. Habang umuusad ang training at lumalaki ang mga weights, tumataas ang kahalagahan ng network parameters, at ina-adjust ng network ang sarili upang ma-accommodate ang kinakailangang expressive power para sa tamang pag-classify ng training images.

### Google Inception

Ang Google Inception architecture ay nagdadala ng ideyang ito sa mas mataas na antas, at binubuo ang bawat network layer bilang kombinasyon ng iba't ibang paths:

<img src="images/inception.png" width="400"/>

> Larawan mula sa [Researchgate](https://www.researchgate.net/figure/Inception-module-with-dimension-reductions-left-and-schema-for-Inception-ResNet-v1_fig2_355547454)

Dito, kailangan nating bigyang-diin ang papel ng 1x1 convolutions, dahil sa una ay tila walang saysay ang mga ito. Bakit natin kailangang gumamit ng 1x1 filter sa imahe? Gayunpaman, kailangan mong tandaan na ang convolution filters ay gumagana rin sa iba't ibang depth channels (orihinal - RGB colors, sa mga susunod na layers - channels para sa iba't ibang filters), at ang 1x1 convolution ay ginagamit upang pagsamahin ang mga input channels gamit ang iba't ibang trainable weights. Maaari rin itong ituring bilang downsampling (pooling) sa channel dimension.

Narito ang [isang magandang blog post](https://medium.com/analytics-vidhya/talented-mr-1x1-comprehensive-look-at-1x1-convolution-in-deep-learning-f6b355825578) tungkol sa paksa, at [ang orihinal na papel](https://arxiv.org/pdf/1312.4400.pdf).

### MobileNet

Ang MobileNet ay isang pamilya ng mga modelo na may mas maliit na sukat, na angkop para sa mga mobile devices. Gamitin ang mga ito kung kulang ka sa resources at handang magsakripisyo ng kaunting katumpakan. Ang pangunahing ideya sa likod nito ay ang tinatawag na **depthwise separable convolution**, na nagpapahintulot na i-represent ang convolution filters sa pamamagitan ng komposisyon ng spatial convolutions at 1x1 convolution sa depth channels. Malaki ang nabawas sa bilang ng mga parameters, kaya mas maliit ang network sa sukat, at mas madaling i-train kahit kaunti ang data.

Narito ang [isang magandang blog post tungkol sa MobileNet](https://medium.com/analytics-vidhya/image-classification-with-mobilenet-cc6fbb2cd470).

## Konklusyon

Sa unit na ito, natutunan mo ang pangunahing konsepto sa likod ng computer vision neural networks - convolutional networks. Ang mga arkitektura sa totoong buhay na nagpapagana sa image classification, object detection, at maging sa image generation networks ay lahat nakabatay sa CNNs, ngunit may mas maraming layers at ilang karagdagang training tricks.

## 🚀 Hamon

Sa mga kasamang notebooks, may mga tala sa ibaba tungkol sa kung paano makakamit ang mas mataas na katumpakan. Subukan ang ilang eksperimento upang makita kung kaya mong makamit ang mas mataas na katumpakan.

## [Post-lecture quiz](https://ff-quizzes.netlify.app/en/ai/quiz/14)

## Review at Pag-aaral ng Sarili

Bagamat ang CNNs ay kadalasang ginagamit para sa mga Computer Vision tasks, maganda rin ang mga ito para sa pagkuha ng fixed-sized patterns. Halimbawa, kung ang ating pinag-aaralan ay tunog, maaari rin nating gamitin ang CNNs upang maghanap ng ilang partikular na patterns sa audio signal - kung saan ang filters ay magiging 1-dimensional (at tatawagin itong 1D-CNN). Gayundin, minsan ginagamit ang 3D-CNN upang kumuha ng features sa multi-dimensional space, tulad ng ilang mga pangyayari sa video - maaaring makuha ng CNN ang ilang patterns ng pagbabago ng features sa paglipas ng panahon. Mag-review at mag-aral ng sarili tungkol sa iba pang tasks na maaaring gawin gamit ang CNNs.

## [Assignment](lab/README.md)

Sa lab na ito, ang iyong gawain ay i-classify ang iba't ibang breed ng pusa at aso. Ang mga imaheng ito ay mas kumplikado kaysa sa MNIST dataset, mas mataas ang dimensyon, at higit sa 10 klase ang mayroon.

---

**Paunawa**:  
Ang dokumentong ito ay isinalin gamit ang AI translation service na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagama't sinisikap naming maging tumpak, tandaan na ang mga awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o hindi pagkakatugma. Ang orihinal na dokumento sa kanyang katutubong wika ang dapat ituring na opisyal na sanggunian. Para sa mahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang hindi pagkakaunawaan o maling interpretasyon na maaaring magmula sa paggamit ng pagsasaling ito.