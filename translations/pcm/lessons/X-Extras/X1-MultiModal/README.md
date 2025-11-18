<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "9c592c26aca16ca085d268c732284187",
  "translation_date": "2025-11-18T18:30:26+00:00",
  "source_file": "lessons/X-Extras/X1-MultiModal/README.md",
  "language_code": "pcm"
}
-->
# Multi-Modal Networks

Afta transformer models don show say dem fit solve NLP tasks well, people don dey use di same or similar architecture for computer vision tasks. Pipo dey show interest for how dem go fit build models wey go *combine* vision and natural language sabi. One of di try wey OpenAI do na CLIP and DALL.E.

## Contrastive Image Pre-Training (CLIP)

Di main idea for CLIP na to fit compare text prompts wit image and check how di image match di prompt.

![CLIP Architecture](../../../../../translated_images/clip-arch.b3dbf20b4e8ed8be1c38e2bc6100fd3cc257c33cda4692b301be91f791b13ea7.pcm.png)

> *Picture from [this blog post](https://openai.com/blog/clip/)*

Di model dey train wit images wey dem collect from Internet and di captions wey follow di images. For each batch, we go take N pairs of (image, text), and turn dem to vector representations I<sub>1</sub>,..., I<sub>N</sub> / T<sub>1</sub>, ..., T<sub>N</sub>. Di representations go then dey match together. Di loss function dey set to make di cosine similarity between vectors wey match one pair (e.g. I<sub>i</sub> and T<sub>i</sub>) high, and make di cosine similarity between di other pairs low. Na why dem dey call dis approach **contrastive**.

CLIP model/library dey available for [OpenAI GitHub](https://github.com/openai/CLIP). Di approach dey explain for [this blog post](https://openai.com/blog/clip/), and dem explain am well well for [this paper](https://arxiv.org/pdf/2103.00020.pdf).

Once dem don pre-train di model, we fit give am batch of images and batch of text prompts, and wetin e go return na tensor wit probabilities. CLIP fit dey use for plenty tasks:

**Image Classification**

Suppose we wan classify images between, say, cats, dogs and humans. For dis case, we fit give di model one image, and series of text prompts: "*a picture of a cat*", "*a picture of a dog*", "*a picture of a human*". For di vector wey get 3 probabilities we go just pick di index wey get di highest value.

![CLIP for Image Classification](../../../../../translated_images/clip-class.3af42ef0b2b19369a633df5f20ddf4f5a01d6c8ffa181e9d3a0572c19f919f72.pcm.png)

> *Picture from [this blog post](https://openai.com/blog/clip/)*

**Text-Based Image Search**

We fit also do di opposite. If we get collection of images, we fit pass di collection to di model, and one text prompt - e go give us di image wey match di prompt pass.

## ✍️ Example: [Using CLIP for Image Classification and Image Search](Clip.ipynb)

Open di [Clip.ipynb](Clip.ipynb) notebook to see how CLIP dey work.

## Image Generation wit VQGAN+ CLIP

CLIP fit also dey use for **image generation** from text prompt. To do dis, we need **generator model** wey fit generate images based on vector input. One of di models wey fit do dis na [VQGAN](https://compvis.github.io/taming-transformers/) (Vector-Quantized GAN).

Di main ideas wey make VQGAN different from ordinary [GAN](../../4-ComputerVision/10-GANs/README.md) na:
* E dey use autoregressive transformer architecture to generate sequence of visual parts wey dey rich wit context wey go form di image. Di visual parts na [CNN](../../4-ComputerVision/07-ConvNets/README.md) dey learn am.
* E dey use sub-image discriminator wey dey check whether di parts of di image na "real" or "fake" (unlike di "all-or-nothing" approach for traditional GAN).

Learn more about VQGAN for di [Taming Transformers](https://compvis.github.io/taming-transformers/) website.

One big difference between VQGAN and traditional GAN na say di traditional GAN fit produce better image from any input vector, but VQGAN fit produce image wey no go make sense. So, we need to guide di image creation process well, and CLIP fit help us do dis.

![VQGAN+CLIP Architecture](../../../../../translated_images/vqgan.5027fe05051dfa3101950cfa930303f66e6478b9bd273e83766731796e462d9b.pcm.png)

To generate image wey match text prompt, we go start wit random encoding vector wey go pass through VQGAN to produce image. Then CLIP go dey use to produce loss function wey go show how di image match di text prompt. Di goal na to reduce dis loss, using back propagation to adjust di input vector parameters.

One better library wey dey implement VQGAN+CLIP na [Pixray](http://github.com/pixray/pixray)

![Picture produced by Pixray](../../../../../translated_images/a_closeup_watercolor_portrait_of_young_male_teacher_of_literature_with_a_book.2384968e9db8a0d09dc96de938b9f95bde8a7e1c721f48f286a7795bf16d56c7.pcm.png) |  ![Picture produced by pixray](../../../../../translated_images/a_closeup_oil_portrait_of_young_female_teacher_of_computer_science_with_a_computer.e0b6495f210a439077e1c32cc8afdf714e634fe24dc78dc5aa45fd2f560b0ed5.pcm.png) | ![Picture produced by Pixray](../../../../../translated_images/a_closeup_oil_portrait_of_old_male_teacher_of_math.5362e67aa7fc2683b9d36a613b364deb7454760cd39205623fc1e3938fa133c0.pcm.png)
----|----|----
Picture wey dem generate from prompt *a closeup watercolor portrait of young male teacher of literature with a book* | Picture wey dem generate from prompt *a closeup oil portrait of young female teacher of computer science with a computer* | Picture wey dem generate from prompt *a closeup oil portrait of old male teacher of mathematics in front of blackboard*

> Pictures from **Artificial Teachers** collection by [Dmitry Soshnikov](http://soshnikov.com)

## DALL-E
### [DALL-E 1](https://openai.com/research/dall-e)
DALL-E na version of GPT-3 wey dem train to generate images from prompts. E don train wit 12-billion parameters.

Unlike CLIP, DALL-E dey take both text and image as one stream of tokens for both images and text. So, from plenty prompts, you fit generate images based on di text.

### [DALL-E 2](https://openai.com/dall-e-2)
Di main difference between DALL.E 1 and 2 na say e dey generate more realistic images and art.

Examples of image generation wit DALL-E:
![Picture produced by Pixray](../../../../../translated_images/DALL·E%202023-06-20%2015.56.56%20-%20a%20closeup%20watercolor%20portrait%20of%20young%20male%20teacher%20of%20literature%20with%20a%20book.6c235e8271d9ed10ce985d86aeb241a58518958647973af136912116b9518fce.pcm.png) |  ![Picture produced by pixray](../../../../../translated_images/DALL·E%202023-06-20%2015.57.43%20-%20a%20closeup%20oil%20portrait%20of%20young%20female%20teacher%20of%20computer%20science%20with%20a%20computer.f21dc4166340b6c8b4d1cb57efd1e22127407f9b28c9ac7afe11344065369e64.pcm.png) | ![Picture produced by Pixray](../../../../../translated_images/DALL·E%202023-06-20%2015.58.42%20-%20%20a%20closeup%20oil%20portrait%20of%20old%20male%20teacher%20of%20mathematics%20in%20front%20of%20blackboard.d331c2dfbdc3f7c46aa65c0809066f5e7ed4b49609cd259852e760df21051e4a.pcm.png)
----|----|----
Picture wey dem generate from prompt *a closeup watercolor portrait of young male teacher of literature with a book* | Picture wey dem generate from prompt *a closeup oil portrait of young female teacher of computer science with a computer* | Picture wey dem generate from prompt *a closeup oil portrait of old male teacher of mathematics in front of blackboard*

## References

* VQGAN Paper: [Taming Transformers for High-Resolution Image Synthesis](https://compvis.github.io/taming-transformers/paper/paper.pdf)
* CLIP Paper: [Learning Transferable Visual Models From Natural Language Supervision](https://arxiv.org/pdf/2103.00020.pdf)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:  
Dis docu wey you dey see don use AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator) take translate am. Even though we dey try make sure say e correct, make you sabi say translation wey machine do fit get mistake or no too accurate. Di original docu for di language wey dem first write am na di main correct one. If na important information, e go better make professional human translator check am. We no go fit take blame for any misunderstanding or wrong interpretation wey fit happen because you use dis translation.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->