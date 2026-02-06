# Pagsasanay sa Skip-Gram Model

Takdang-Aralin mula sa [AI for Beginners Curriculum](https://github.com/microsoft/ai-for-beginners).

## Gawain

Sa lab na ito, hinahamon ka naming sanayin ang Word2Vec model gamit ang Skip-Gram na teknika. Sanayin ang isang network na may embedding upang mahulaan ang mga kalapit na salita sa $N$-tokens-wide Skip-Gram window. Maaari mong gamitin ang [code mula sa araling ito](../CBoW-TF.ipynb), at bahagyang baguhin ito.

## Ang Dataset

Malugod kang gumamit ng anumang libro. Makakahanap ka ng maraming libreng teksto sa [Project Gutenberg](https://www.gutenberg.org/), halimbawa, narito ang direktang link sa [Alice's Adventures in Wonderland](https://www.gutenberg.org/files/11/11-0.txt)) ni Lewis Carroll. O, maaari mong gamitin ang mga dula ni Shakespeare, na maaari mong makuha gamit ang sumusunod na code:

```python
path_to_file = tf.keras.utils.get_file(
   'shakespeare.txt', 
   'https://storage.googleapis.com/download.tensorflow.org/data/shakespeare.txt')
text = open(path_to_file, 'rb').read().decode(encoding='utf-8')
```

## Mag-eksperimento!

Kung may oras ka at nais mong mas lumalim sa paksa, subukang tuklasin ang ilang bagay:

* Paano naaapektuhan ng laki ng embedding ang mga resulta?
* Paano naaapektuhan ng iba't ibang estilo ng teksto ang resulta?
* Kumuha ng ilang napaka-ibang uri ng mga salita at kanilang mga kasingkahulugan, kunin ang kanilang mga vector representations, mag-apply ng PCA upang mabawasan ang dimensyon sa 2, at i-plot ang mga ito sa 2D space. May nakikita ka bang mga pattern?

---

**Paunawa**:  
Ang dokumentong ito ay isinalin gamit ang AI translation service na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagama't sinisikap naming maging tumpak, tandaan na ang mga awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o hindi pagkakatugma. Ang orihinal na dokumento sa kanyang katutubong wika ang dapat ituring na opisyal na sanggunian. Para sa mahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang hindi pagkakaunawaan o maling interpretasyon na dulot ng paggamit ng pagsasaling ito.