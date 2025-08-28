<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f3d2cee9cb3c52160419e560c57a690e",
  "translation_date": "2025-08-28T02:30:12+00:00",
  "source_file": "lessons/4-ComputerVision/07-ConvNets/lab/README.md",
  "language_code": "tl"
}
-->
# Pag-uuri ng Mukha ng Alagang Hayop

Takdang-Aralin mula sa [AI for Beginners Curriculum](https://github.com/microsoft/ai-for-beginners).

## Gawain

Isipin na kailangan mong bumuo ng isang aplikasyon para sa nursery ng mga alagang hayop upang i-catalog ang lahat ng mga alaga. Isa sa mga magagandang tampok ng ganitong aplikasyon ay ang awtomatikong pagtukoy ng lahi mula sa isang litrato. Magagawa ito nang matagumpay gamit ang neural networks.

Kailangan mong sanayin ang isang convolutional neural network upang uriin ang iba't ibang lahi ng pusa at aso gamit ang **Pet Faces** dataset.

## Ang Dataset

Gagamitin natin ang **Pet Faces** dataset, na nagmula sa [Oxford-IIIT](https://www.robots.ox.ac.uk/~vgg/data/pets/) pets dataset. Naglalaman ito ng 35 iba't ibang lahi ng aso at pusa.

![Dataset na ating gagamitin](../../../../../../translated_images/data.50b2a9d5484bdbf0f52f5765b381cec9efe2bd296a98f007f90bedb6ac67f2a8.tl.png)

Upang i-download ang dataset, gamitin ang code snippet na ito:

```python
!wget https://mslearntensorflowlp.blob.core.windows.net/data/petfaces.tar.gz
!tar xfz petfaces.tar.gz
!rm petfaces.tar.gz
```

## Simula ng Notebook

Simulan ang lab sa pamamagitan ng pagbukas ng [PetFaces.ipynb](PetFaces.ipynb)

## Aral

Nalutas mo ang isang medyo komplikadong problema ng pag-uuri ng imahe mula sa simula! Maraming klase, ngunit nagawa mo pa ring makamit ang makatwirang katumpakan! Makatuwiran din na sukatin ang top-k accuracy, dahil madali itong malito sa ilang mga klase na hindi gaanong naiiba kahit para sa mga tao.

---

**Paunawa**:  
Ang dokumentong ito ay isinalin gamit ang AI translation service na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagama't sinisikap naming maging tumpak, pakitandaan na ang mga awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o hindi pagkakatugma. Ang orihinal na dokumento sa kanyang katutubong wika ang dapat ituring na opisyal na sanggunian. Para sa mahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang hindi pagkakaunawaan o maling interpretasyon na dulot ng paggamit ng pagsasaling ito.