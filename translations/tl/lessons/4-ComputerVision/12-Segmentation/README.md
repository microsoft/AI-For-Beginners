<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "d7f8a25ff13cfe9f4cd671cc23351fad",
  "translation_date": "2025-08-28T02:33:16+00:00",
  "source_file": "lessons/4-ComputerVision/12-Segmentation/README.md",
  "language_code": "tl"
}
-->
# Segmentasyon

Natutuhan na natin ang tungkol sa Object Detection, na nagbibigay-daan sa atin upang mahanap ang mga bagay sa isang imahe sa pamamagitan ng paghula ng kanilang *bounding boxes*. Gayunpaman, para sa ilang mga gawain, hindi lamang bounding boxes ang kailangan natin, kundi mas eksaktong lokasyon ng mga bagay. Ang gawaing ito ay tinatawag na **segmentasyon**.

## [Pre-lecture quiz](https://ff-quizzes.netlify.app/en/ai/quiz/23)

Ang segmentasyon ay maaaring tingnan bilang **pixel classification**, kung saan para sa **bawat** pixel ng imahe, kailangan nating hulaan ang klase nito (*background* bilang isa sa mga klase). Mayroong dalawang pangunahing algorithm para sa segmentasyon:

* **Semantic segmentation** ay nagsasabi lamang ng klase ng pixel, at hindi gumagawa ng pagkakaiba sa pagitan ng iba't ibang bagay na nasa parehong klase.
* **Instance segmentation** ay naghahati ng mga klase sa iba't ibang mga instance.

Halimbawa, sa instance segmentation, ang mga tupa ay itinuturing na magkakaibang mga bagay, ngunit sa semantic segmentation, ang lahat ng tupa ay kinakatawan ng iisang klase.

<img src="images/instance_vs_semantic.jpeg" width="50%">

> Larawan mula sa [blog post na ito](https://nirmalamurali.medium.com/image-classification-vs-semantic-segmentation-vs-instance-segmentation-625c33a08d50)

May iba't ibang neural architectures para sa segmentasyon, ngunit lahat sila ay may parehong istruktura. Sa isang paraan, ito ay kahalintulad sa autoencoder na natutunan mo na dati, ngunit sa halip na i-deconstruct ang orihinal na imahe, ang layunin natin ay i-deconstruct ang isang **mask**. Kaya, ang isang segmentation network ay may mga sumusunod na bahagi:

* **Encoder** na kumukuha ng mga feature mula sa input na imahe.
* **Decoder** na nagta-transform ng mga feature na iyon sa **mask image**, na may parehong laki at bilang ng mga channel na tumutugma sa bilang ng mga klase.

<img src="images/segm.png" width="80%">

> Larawan mula sa [publikasyong ito](https://arxiv.org/pdf/2001.05566.pdf)

Dapat nating bigyang-diin ang loss function na ginagamit para sa segmentasyon. Kapag gumagamit ng klasikong autoencoders, kailangan nating sukatin ang pagkakapareho sa pagitan ng dalawang imahe, at maaari nating gamitin ang mean square error (MSE) para dito. Sa segmentasyon, ang bawat pixel sa target mask image ay kumakatawan sa numero ng klase (one-hot-encoded sa ikatlong dimensyon), kaya kailangan nating gumamit ng loss functions na partikular para sa classification - cross-entropy loss, na ina-average sa lahat ng pixel. Kung ang mask ay binary - ginagamit ang **binary cross-entropy loss** (BCE).

> ✅ Ang one-hot encoding ay isang paraan upang i-encode ang class label sa isang vector na ang haba ay katumbas ng bilang ng mga klase. Tingnan ang [artikulong ito](https://datagy.io/sklearn-one-hot-encode/) tungkol sa teknik na ito.

## Segmentasyon para sa Medical Imaging

Sa araling ito, makikita natin ang segmentasyon sa aksyon sa pamamagitan ng pagsasanay ng network upang makilala ang human nevi (kilala rin bilang moles) sa mga medical images. Gagamitin natin ang <a href="https://www.fc.up.pt/addi/ph2%20database.html">PH<sup>2</sup> Database</a> ng mga dermoscopy images bilang pinagmulan ng imahe. Ang dataset na ito ay naglalaman ng 200 imahe ng tatlong klase: typical nevus, atypical nevus, at melanoma. Ang lahat ng mga imahe ay mayroon ding kaukulang **mask** na nagbabalangkas sa nevus.

> ✅ Ang teknik na ito ay partikular na angkop para sa ganitong uri ng medical imaging, ngunit ano pa kayang mga totoong aplikasyon ang naiisip mo?

<img alt="navi" src="images/navi.png"/>

> Larawan mula sa PH<sup>2</sup> Database

Magsasanay tayo ng isang modelo upang i-segment ang anumang nevus mula sa background nito.

## ✍️ Mga Ehersisyo: Semantic Segmentation

Buksan ang mga notebook sa ibaba upang matuto pa tungkol sa iba't ibang semantic segmentation architectures, magsanay sa paggamit ng mga ito, at makita ang mga ito sa aksyon.

* [Semantic Segmentation Pytorch](SemanticSegmentationPytorch.ipynb)
* [Semantic Segmentation TensorFlow](SemanticSegmentationTF.ipynb)

## [Post-lecture quiz](https://ff-quizzes.netlify.app/en/ai/quiz/24)

## Konklusyon

Ang segmentasyon ay isang napakalakas na teknik para sa image classification, na lumalampas sa bounding boxes patungo sa pixel-level classification. Ito ay isang teknik na ginagamit sa medical imaging, bukod sa iba pang mga aplikasyon.

## 🚀 Hamon

Ang body segmentation ay isa lamang sa mga karaniwang gawain na maaari nating gawin gamit ang mga imahe ng tao. Ang iba pang mahahalagang gawain ay kinabibilangan ng **skeleton detection** at **pose detection**. Subukan ang [OpenPose](https://github.com/CMU-Perceptual-Computing-Lab/openpose) library upang makita kung paano magagamit ang pose detection.

## Review at Pag-aaral sa Sarili

Ang [artikulong ito sa Wikipedia](https://wikipedia.org/wiki/Image_segmentation) ay nagbibigay ng magandang pangkalahatang-ideya ng iba't ibang aplikasyon ng teknik na ito. Alamin pa ang tungkol sa mga subdomain ng Instance segmentation at Panoptic segmentation sa larangang ito.

## [Takdang Aralin](lab/README.md)

Sa lab na ito, subukan ang **human body segmentation** gamit ang [Segmentation Full Body MADS Dataset](https://www.kaggle.com/datasets/tapakah68/segmentation-full-body-mads-dataset) mula sa Kaggle.

---

**Paunawa**:  
Ang dokumentong ito ay isinalin gamit ang AI translation service na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagama't sinisikap naming maging tumpak, tandaan na ang mga awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o hindi pagkakatugma. Ang orihinal na dokumento sa kanyang katutubong wika ang dapat ituring na opisyal na sanggunian. Para sa mahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang hindi pagkakaunawaan o maling interpretasyon na dulot ng paggamit ng pagsasaling ito.