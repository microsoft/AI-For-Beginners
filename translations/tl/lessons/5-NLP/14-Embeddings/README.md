# Embeddings

## [Pre-lecture quiz](https://ff-quizzes.netlify.app/en/ai/quiz/27)

Kapag nagsasanay ng mga classifier gamit ang BoW o TF/IDF, gumagamit tayo ng high-dimensional bag-of-words vectors na may habang `vocab_size`, at tahasang kino-convert ang low-dimensional positional representation vectors sa sparse one-hot representation. Gayunpaman, ang one-hot representation na ito ay hindi memory-efficient. Bukod dito, ang bawat salita ay itinuturing na hiwalay sa isa't isa, ibig sabihin, ang one-hot encoded vectors ay hindi nagpapakita ng anumang semantikong pagkakatulad sa pagitan ng mga salita.

Ang ideya ng **embedding** ay ang pagrepresenta ng mga salita gamit ang mas mababang dimensional na dense vectors, na sa isang paraan ay sumasalamin sa semantikong kahulugan ng isang salita. Tatalakayin natin sa susunod kung paano bumuo ng makabuluhang word embeddings, ngunit sa ngayon, isipin muna natin ang embeddings bilang isang paraan upang bawasan ang dimensionality ng word vector.

Ang embedding layer ay kukuha ng isang salita bilang input, at magbibigay ng output vector na may tinukoy na `embedding_size`. Sa isang banda, ito ay halos katulad ng isang `Linear` layer, ngunit sa halip na kumuha ng one-hot encoded vector, maaari itong kumuha ng word number bilang input, na nagpapahintulot sa atin na maiwasan ang paggawa ng malalaking one-hot-encoded vectors.

Sa paggamit ng embedding layer bilang unang layer sa ating classifier network, maaari tayong lumipat mula sa bag-of-words patungo sa **embedding bag** model, kung saan una nating kino-convert ang bawat salita sa ating teksto sa kaukulang embedding, at pagkatapos ay kinakalkula ang ilang aggregate function sa lahat ng mga embedding na iyon, tulad ng `sum`, `average`, o `max`.

![Larawan na nagpapakita ng isang embedding classifier para sa limang sequence words.](../../../../../translated_images/tl/embedding-classifier-example.b77f021a7ee67eee.webp)

> Larawan mula sa may-akda

## ✍️ Mga Ehersisyo: Embeddings

Ipagpatuloy ang iyong pag-aaral sa mga sumusunod na notebooks:
* [Embeddings with PyTorch](EmbeddingsPyTorch.ipynb)
* [Embeddings TensorFlow](EmbeddingsTF.ipynb)

## Semantic Embeddings: Word2Vec

Habang ang embedding layer ay natututo kung paano i-map ang mga salita sa vector representation, ang representation na ito ay hindi kinakailangang may malalim na semantikong kahulugan. Magiging maganda kung makakabuo tayo ng vector representation kung saan ang magkatulad na salita o mga kasingkahulugan ay tumutugma sa mga vectors na malapit sa isa't isa batay sa ilang vector distance (hal. Euclidean distance).

Upang magawa ito, kailangan nating i-pre-train ang ating embedding model sa isang malaking koleksyon ng teksto sa isang partikular na paraan. Ang isang paraan upang magsanay ng semantic embeddings ay tinatawag na [Word2Vec](https://en.wikipedia.org/wiki/Word2vec). Ito ay batay sa dalawang pangunahing arkitektura na ginagamit upang makabuo ng distributed representation ng mga salita:

 - **Continuous bag-of-words** (CBoW) — sa arkitekturang ito, sinasanay natin ang modelo upang hulaan ang isang salita mula sa nakapaligid na konteksto. Ibinigay ang ngram $(W_{-2},W_{-1},W_0,W_1,W_2)$, ang layunin ng modelo ay hulaan ang $W_0$ mula sa $(W_{-2},W_{-1},W_1,W_2)$.
 - **Continuous skip-gram** — kabaligtaran ng CBoW. Ang modelo ay gumagamit ng nakapaligid na window ng mga context words upang hulaan ang kasalukuyang salita.

Mas mabilis ang CBoW, habang ang skip-gram ay mas mabagal, ngunit mas mahusay sa pagrepresenta ng mga bihirang salita.

![Larawan na nagpapakita ng parehong CBoW at Skip-Gram algorithms upang i-convert ang mga salita sa vectors.](../../../../../translated_images/tl/example-algorithms-for-converting-words-to-vectors.fbe9207a726922f6.webp)

> Larawan mula sa [papel na ito](https://arxiv.org/pdf/1301.3781.pdf)

Ang Word2Vec pre-trained embeddings (pati na rin ang iba pang katulad na mga modelo, tulad ng GloVe) ay maaari ring gamitin bilang kapalit ng embedding layer sa mga neural networks. Gayunpaman, kailangan nating harapin ang mga bokabularyo, dahil ang bokabularyo na ginamit upang i-pre-train ang Word2Vec/GloVe ay malamang na naiiba sa bokabularyo sa ating text corpus. Tingnan ang mga Notebook sa itaas upang makita kung paano malulutas ang problemang ito.

## Contextual Embeddings

Ang isang pangunahing limitasyon ng tradisyunal na pretrained embedding representations tulad ng Word2Vec ay ang problema ng word sense disambiguation. Habang ang pretrained embeddings ay maaaring makuha ang ilang kahulugan ng mga salita sa konteksto, ang bawat posibleng kahulugan ng isang salita ay naka-encode sa parehong embedding. Maaari itong magdulot ng mga problema sa downstream models, dahil maraming salita tulad ng salitang 'play' ay may iba't ibang kahulugan depende sa konteksto kung saan ito ginagamit.

Halimbawa, ang salitang 'play' sa dalawang magkaibang pangungusap na ito ay may magkaibang kahulugan:

- Pumunta ako sa isang **play** sa teatro.
- Gusto ni John na **maglaro** kasama ang kanyang mga kaibigan.

Ang pretrained embeddings sa itaas ay kumakatawan sa parehong mga kahulugan ng salitang 'play' sa parehong embedding. Upang malampasan ang limitasyong ito, kailangan nating bumuo ng embeddings batay sa **language model**, na sinanay sa isang malaking corpus ng teksto, at *alam* kung paano maaaring pagsama-samahin ang mga salita sa iba't ibang konteksto. Ang pagtalakay sa contextual embeddings ay labas sa saklaw ng tutorial na ito, ngunit babalikan natin ito kapag pinag-usapan na ang mga language models sa susunod na bahagi ng kurso.

## Konklusyon

Sa araling ito, natutunan mo kung paano bumuo at gumamit ng embedding layers sa TensorFlow at Pytorch upang mas mahusay na maipakita ang semantikong kahulugan ng mga salita.

## 🚀 Hamon

Ang Word2Vec ay ginamit sa ilang mga kawili-wiling aplikasyon, kabilang ang paggawa ng mga liriko ng kanta at tula. Tingnan ang [artikulong ito](https://www.politetype.com/blog/word2vec-color-poems) na nagpapaliwanag kung paano ginamit ng may-akda ang Word2Vec upang makabuo ng tula. Panoorin din ang [video na ito ni Dan Shiffmann](https://www.youtube.com/watch?v=LSS_bos_TPI&ab_channel=TheCodingTrain) upang matuklasan ang ibang paliwanag ng teknik na ito. Pagkatapos, subukang ilapat ang mga teknik na ito sa sarili mong text corpus, marahil mula sa Kaggle.

## [Post-lecture quiz](https://ff-quizzes.netlify.app/en/ai/quiz/28)

## Review at Pag-aaral sa Sarili

Basahin ang papel na ito tungkol sa Word2Vec: [Efficient Estimation of Word Representations in Vector Space](https://arxiv.org/pdf/1301.3781.pdf)

## [Takdang-Aralin: Notebooks](assignment.md)

---

