<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4522e22e150be0845e03aa41209a39d5",
  "translation_date": "2025-08-28T02:45:13+00:00",
  "source_file": "lessons/5-NLP/13-TextRep/README.md",
  "language_code": "tl"
}
-->
# Pagsasakatawan ng Teksto bilang Tensors

## [Pre-lecture quiz](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/113)

## Pag-uuri ng Teksto

Sa unang bahagi ng seksyong ito, magtutuon tayo sa gawain ng **pag-uuri ng teksto**. Gagamitin natin ang [AG News](https://www.kaggle.com/amananandrai/ag-news-classification-dataset) Dataset, na naglalaman ng mga artikulo ng balita tulad ng sumusunod:

* Kategorya: Sci/Tech  
* Pamagat: Ky. Company Wins Grant to Study Peptides (AP)  
* Nilalaman: AP - Isang kumpanya na itinatag ng isang chemistry researcher sa University of Louisville ang nanalo ng grant para mag-develop...

Ang layunin natin ay uriin ang balita sa isa sa mga kategorya base sa teksto.

## Pagsasakatawan ng Teksto

Kung nais nating lutasin ang mga gawain sa Natural Language Processing (NLP) gamit ang neural networks, kailangan natin ng paraan upang isakatawan ang teksto bilang tensors. Ang mga computer ay kumakatawan na sa mga tekstwal na karakter bilang mga numero na tumutugma sa mga font sa iyong screen gamit ang mga encoding tulad ng ASCII o UTF-8.

<img alt="Larawan na nagpapakita ng diagram na nagmamapa ng isang karakter sa ASCII at binary na representasyon" src="images/ascii-character-map.png" width="50%"/>

> [Pinagmulan ng Larawan](https://www.seobility.net/en/wiki/ASCII)

Bilang mga tao, nauunawaan natin kung ano ang **kinakatawan** ng bawat letra, at kung paano nagsasama-sama ang mga karakter upang mabuo ang mga salita sa isang pangungusap. Gayunpaman, ang mga computer mismo ay walang ganitong pag-unawa, at kailangang matutunan ng neural network ang kahulugan nito sa panahon ng training.

Dahil dito, maaari tayong gumamit ng iba't ibang paraan sa pagsasakatawan ng teksto:

* **Character-level representation**, kung saan isinasakatawan natin ang teksto sa pamamagitan ng pagtrato sa bawat karakter bilang isang numero. Kung mayroon tayong *C* na iba't ibang karakter sa ating text corpus, ang salitang *Hello* ay isasakatawan bilang 5x*C* tensor. Ang bawat letra ay tumutugma sa isang column ng tensor sa one-hot encoding.  
* **Word-level representation**, kung saan gumagawa tayo ng **bokabularyo** ng lahat ng salita sa ating teksto, at pagkatapos ay isinasakatawan ang mga salita gamit ang one-hot encoding. Ang paraang ito ay mas mainam, dahil ang bawat letra mismo ay walang masyadong kahulugan, kaya sa pamamagitan ng paggamit ng mas mataas na antas ng semantikong konsepto - mga salita - pinapasimple natin ang gawain para sa neural network. Gayunpaman, dahil sa laki ng diksyunaryo, kailangan nating harapin ang mataas na dimensional na sparse tensors.

Anuman ang representasyon, kailangan muna nating i-convert ang teksto sa isang sequence ng **tokens**, kung saan ang isang token ay maaaring isang karakter, isang salita, o minsan kahit bahagi ng isang salita. Pagkatapos, iko-convert natin ang token sa isang numero, karaniwang gamit ang **bokabularyo**, at ang numerong ito ay maaaring ipasok sa neural network gamit ang one-hot encoding.

## N-Grams

Sa natural na wika, ang tiyak na kahulugan ng mga salita ay matutukoy lamang sa konteksto. Halimbawa, ang mga kahulugan ng *neural network* at *fishing network* ay ganap na magkaiba. Isa sa mga paraan upang isaalang-alang ito ay ang pagbuo ng ating modelo sa mga pares ng salita, at ituring ang mga pares ng salita bilang magkakahiwalay na token sa bokabularyo. Sa ganitong paraan, ang pangungusap na *I like to go fishing* ay isasakatawan ng sumusunod na sequence ng mga token: *I like*, *like to*, *to go*, *go fishing*. Ang problema sa paraang ito ay ang laki ng diksyunaryo ay lumalaki nang malaki, at ang mga kombinasyon tulad ng *go fishing* at *go shopping* ay kinakatawan ng magkaibang token, na walang anumang semantikong pagkakatulad sa kabila ng parehong pandiwa.

Sa ilang mga kaso, maaari nating isaalang-alang ang paggamit ng tri-grams -- mga kombinasyon ng tatlong salita -- din. Kaya ang paraang ito ay madalas na tinatawag na **n-grams**. Gayundin, may kabuluhan ang paggamit ng n-grams sa character-level representation, kung saan ang n-grams ay halos tumutugma sa iba't ibang pantig.

## Bag-of-Words at TF/IDF

Kapag nilulutas ang mga gawain tulad ng pag-uuri ng teksto, kailangan nating magawang isakatawan ang teksto sa isang fixed-size na vector, na gagamitin natin bilang input sa final dense classifier. Isa sa mga pinakasimpleng paraan upang gawin ito ay pagsamahin ang lahat ng indibidwal na representasyon ng salita, halimbawa sa pamamagitan ng pagdaragdag ng mga ito. Kung idaragdag natin ang one-hot encodings ng bawat salita, magkakaroon tayo ng vector ng frequencies, na nagpapakita kung ilang beses lumitaw ang bawat salita sa loob ng teksto. Ang ganitong representasyon ng teksto ay tinatawag na **bag of words** (BoW).

<img src="images/bow.png" width="90%"/>

> Larawan ng may-akda

Ang BoW ay mahalagang kumakatawan kung aling mga salita ang lumitaw sa teksto at sa anong dami, na maaaring maging isang magandang indikasyon kung tungkol saan ang teksto. Halimbawa, ang artikulo ng balita tungkol sa pulitika ay malamang na naglalaman ng mga salitang tulad ng *president* at *country*, habang ang publikasyong pang-agham ay magkakaroon ng mga salitang tulad ng *collider*, *discovered*, atbp. Kaya, ang mga frequency ng salita ay sa maraming kaso ay maaaring maging magandang indikasyon ng nilalaman ng teksto.

Ang problema sa BoW ay ang ilang karaniwang salita, tulad ng *and*, *is*, atbp. ay lumilitaw sa karamihan ng mga teksto, at sila ang may pinakamataas na frequency, na tinatabunan ang mga salitang talagang mahalaga. Maaari nating bawasan ang kahalagahan ng mga salitang ito sa pamamagitan ng pagsasaalang-alang sa frequency kung saan lumilitaw ang mga salita sa buong koleksyon ng dokumento. Ito ang pangunahing ideya sa likod ng TF/IDF approach, na tinalakay nang mas detalyado sa mga notebook na nakalakip sa araling ito.

Gayunpaman, wala sa mga paraang ito ang ganap na makakukuha ng **semantika** ng teksto. Kailangan natin ng mas makapangyarihang neural network models upang magawa ito, na tatalakayin natin sa susunod na bahagi ng seksyon.

## ✍️ Mga Ehersisyo: Pagsasakatawan ng Teksto

Ipagpatuloy ang iyong pag-aaral sa mga sumusunod na notebook:

* [Text Representation with PyTorch](TextRepresentationPyTorch.ipynb)  
* [Text Representation with TensorFlow](TextRepresentationTF.ipynb)  

## Konklusyon

Sa ngayon, pinag-aralan natin ang mga teknik na maaaring magdagdag ng frequency weight sa iba't ibang salita. Gayunpaman, hindi nila kayang isakatawan ang kahulugan o pagkakasunod-sunod. Tulad ng sinabi ng sikat na lingguwista na si J. R. Firth noong 1935, "Ang kumpletong kahulugan ng isang salita ay palaging nakabatay sa konteksto, at walang pag-aaral ng kahulugan na hiwalay sa konteksto ang maaaring ituring na seryoso." Matututuhan natin sa susunod na kurso kung paano makuha ang impormasyong kontekstwal mula sa teksto gamit ang language modeling.

## 🚀 Hamon

Subukan ang iba pang mga ehersisyo gamit ang bag-of-words at iba't ibang data models. Maaaring ma-inspire ka ng [kompetisyon na ito sa Kaggle](https://www.kaggle.com/competitions/word2vec-nlp-tutorial/overview/part-1-for-beginners-bag-of-words).

## [Post-lecture quiz](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/213)

## Review at Pag-aaral sa Sarili

Sanayin ang iyong kakayahan sa text embeddings at bag-of-words techniques sa [Microsoft Learn](https://docs.microsoft.com/learn/modules/intro-natural-language-processing-pytorch/?WT.mc_id=academic-77998-cacaste)

## [Assignment: Notebooks](assignment.md)

---

**Paunawa**:  
Ang dokumentong ito ay isinalin gamit ang AI translation service na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagama't sinisikap naming maging tumpak, pakitandaan na ang mga awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o hindi pagkakatugma. Ang orihinal na dokumento sa kanyang katutubong wika ang dapat ituring na opisyal na sanggunian. Para sa mahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang hindi pagkakaunawaan o maling interpretasyon na maaaring magmula sa paggamit ng pagsasaling ito.