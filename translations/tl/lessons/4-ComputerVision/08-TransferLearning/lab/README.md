# Pag-uuri ng Oxford Pets gamit ang Transfer Learning

Takdang-Aralin mula sa [AI for Beginners Curriculum](https://github.com/microsoft/ai-for-beginners).

## Gawain

Isipin na kailangan mong gumawa ng isang aplikasyon para sa pet nursery upang i-catalog ang lahat ng alagang hayop. Isa sa mga magagandang tampok ng ganitong aplikasyon ay ang awtomatikong pagtukoy ng lahi mula sa isang litrato. Sa takdang-araling ito, gagamit tayo ng transfer learning upang uriin ang mga totoong larawan ng alagang hayop mula sa [Oxford-IIIT](https://www.robots.ox.ac.uk/~vgg/data/pets/) pets dataset.

## Ang Dataset

Gagamitin natin ang orihinal na [Oxford-IIIT](https://www.robots.ox.ac.uk/~vgg/data/pets/) pets dataset, na naglalaman ng 35 iba't ibang lahi ng aso at pusa.

Upang i-download ang dataset, gamitin ang code snippet na ito:

```python
!wget https://www.robots.ox.ac.uk/~vgg/data/pets/data/images.tar.gz
!tar xfz images.tar.gz
!rm images.tar.gz
```

## Simula ng Notebook

Simulan ang lab sa pamamagitan ng pagbubukas ng [OxfordPets.ipynb](OxfordPets.ipynb)

## Mahalagang Aral

Ang transfer learning at pre-trained networks ay nagbibigay-daan sa atin na lutasin ang mga totoong problema sa pag-uuri ng imahe nang medyo madali. Gayunpaman, ang mga pre-trained networks ay mahusay lamang sa mga imahe na may parehong uri, at kung magsisimula tayong mag-uri ng napakaibang mga imahe (hal. mga medikal na imahe), malamang na makakakuha tayo ng mas masamang resulta.

---

**Paunawa**:  
Ang dokumentong ito ay isinalin gamit ang AI translation service na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagama't sinisikap naming maging tumpak, pakitandaan na ang mga awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o hindi pagkakatugma. Ang orihinal na dokumento sa orihinal nitong wika ang dapat ituring na opisyal na sanggunian. Para sa mahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang hindi pagkakaunawaan o maling interpretasyon na maaaring magmula sa paggamit ng pagsasaling ito.