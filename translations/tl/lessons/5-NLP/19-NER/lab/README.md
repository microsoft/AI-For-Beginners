# NER

Gawain mula sa [AI for Beginners Curriculum](https://github.com/microsoft/ai-for-beginners).

## Gawain

Sa lab na ito, kailangan mong sanayin ang named entity recognition model para sa mga terminong medikal.

## Ang Dataset

Para masanay ang NER model, kailangan natin ng maayos na labeled dataset na may mga medikal na entidad. Ang [BC5CDR dataset](https://biocreative.bioinformatics.udel.edu/tasks/biocreative-v/track-3-cdr/) ay naglalaman ng mga labeled na sakit at kemikal na entidad mula sa mahigit 1500 na papel. Maaari mong i-download ang dataset pagkatapos magparehistro sa kanilang website.

Ganito ang hitsura ng BC5CDR Dataset:

```
6794356|t|Tricuspid valve regurgitation and lithium carbonate toxicity in a newborn infant.
6794356|a|A newborn with massive tricuspid regurgitation, atrial flutter, congestive heart failure, and a high serum lithium level is described. This is the first patient to initially manifest tricuspid regurgitation and atrial flutter, and the 11th described patient with cardiac disease among infants exposed to lithium compounds in the first trimester of pregnancy. Sixty-three percent of these infants had tricuspid valve involvement. Lithium carbonate may be a factor in the increasing incidence of congenital heart disease when taken during early pregnancy. It also causes neurologic depression, cyanosis, and cardiac arrhythmia when consumed prior to delivery.
6794356	0	29	Tricuspid valve regurgitation	Disease	D014262
6794356	34	51	lithium carbonate	Chemical	D016651
6794356	52	60	toxicity	Disease	D064420
...
```

Sa dataset na ito, may pamagat ng papel at abstrak sa unang dalawang linya, at pagkatapos ay may mga indibidwal na entidad, kasama ang simula at dulo ng posisyon sa loob ng title+abstract block. Bukod sa uri ng entidad, makakakuha ka rin ng ontology ID ng entidad na ito sa loob ng ilang medikal na ontology.

Kailangan mong magsulat ng Python code upang i-convert ito sa BIO encoding.

## Ang Network

Ang unang pagsubok sa NER ay maaaring gawin gamit ang LSTM network, tulad ng halimbawa na nakita mo sa aralin. Gayunpaman, sa mga NLP na gawain, ang [transformer architecture](https://en.wikipedia.org/wiki/Transformer_(machine_learning_model)), at partikular ang [BERT language models](https://en.wikipedia.org/wiki/BERT_(language_model)) ay nagpapakita ng mas magagandang resulta. Ang mga pre-trained BERT models ay nauunawaan ang pangkalahatang istruktura ng isang wika, at maaaring i-fine-tune para sa mga partikular na gawain gamit ang medyo maliit na datasets at computational costs.

Dahil balak nating gamitin ang NER sa medikal na senaryo, makatuwiran na gumamit ng BERT model na sinanay sa mga medikal na teksto. Ang Microsoft Research ay naglabas ng pre-trained model na tinatawag na [PubMedBERT][PubMedBERT] ([publication][PubMedBERT-Pub]), na na-fine-tune gamit ang mga teksto mula sa [PubMed](https://pubmed.ncbi.nlm.nih.gov/) repository.

Ang *de facto* na pamantayan para sa pagsasanay ng transformer models ay ang [Hugging Face Transformers](https://huggingface.co/) library. Naglalaman din ito ng repository ng mga pre-trained models na pinapanatili ng komunidad, kabilang ang PubMedBERT. Para ma-load at magamit ang model na ito, kailangan lang natin ng ilang linya ng code:

```python
model_name = "microsoft/BiomedNLP-PubMedBERT-base-uncased-abstract"
classes = ... # number of classes: 2*entities+1
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = BertForTokenClassification.from_pretrained(model_name, classes)
```

Ito ay nagbibigay sa atin ng `model` mismo, na itinayo para sa token classification task gamit ang `classes` na bilang ng mga klase, pati na rin ang `tokenizer` object na maaaring maghiwalay ng input text sa mga token. Kailangan mong i-convert ang dataset sa BIO format, isinasaalang-alang ang tokenization ng PubMedBERT. Maaari mong gamitin ang [bahaging ito ng Python code](https://gist.github.com/shwars/580b55684be3328eb39ecf01b9cbbd88) bilang inspirasyon.

## Mga Aral

Ang gawain na ito ay malapit sa aktwal na gawain na malamang na makaharap mo kung nais mong makakuha ng mas maraming kaalaman mula sa malalaking dami ng natural language texts. Sa ating kaso, maaari nating gamitin ang ating sinanay na model sa [dataset ng mga papel na may kaugnayan sa COVID](https://www.kaggle.com/allen-institute-for-ai/CORD-19-research-challenge) at tingnan kung anong mga kaalaman ang makukuha natin. Ang [blog post na ito](https://soshnikov.com/science/analyzing-medical-papers-with-azure-and-text-analytics-for-health/) at [papel na ito](https://www.mdpi.com/2504-2289/6/1/4) ay naglalarawan ng pananaliksik na maaaring gawin sa corpus ng mga papel gamit ang NER.

---

**Paunawa**:  
Ang dokumentong ito ay isinalin gamit ang AI translation service na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagama't sinisikap naming maging tumpak, tandaan na ang mga awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o hindi pagkakatugma. Ang orihinal na dokumento sa kanyang katutubong wika ang dapat ituring na opisyal na pinagmulan. Para sa mahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang hindi pagkakaunawaan o maling interpretasyon na maaaring magmula sa paggamit ng pagsasaling ito.