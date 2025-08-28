<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "7336583e4630220c835335da640016db",
  "translation_date": "2025-08-28T02:38:38+00:00",
  "source_file": "lessons/3-NeuralNetworks/03-Perceptron/lab/README.md",
  "language_code": "tl"
}
-->
# Multi-Class Classification gamit ang Perceptron

Takdang-Aralin mula sa [AI for Beginners Curriculum](https://github.com/microsoft/ai-for-beginners).

## Gawain

Gamit ang code na ating ginawa sa araling ito para sa binary classification ng MNIST handwritten digits, gumawa ng isang multi-class classifier na makakakilala ng anumang digit. Kalkulahin ang classification accuracy sa train at test dataset, at ipakita ang confusion matrix.

## Mga Pahiwatig

1. Para sa bawat digit, gumawa ng dataset para sa binary classifier ng "ang digit na ito vs. lahat ng iba pang digit"
1. Mag-train ng 10 iba't ibang perceptrons para sa binary classification (isa para sa bawat digit)
1. Mag-define ng function na magka-classify sa input digit

> **Pahiwatig**: Kung pagsasamahin natin ang weights ng lahat ng 10 perceptrons sa isang matrix, magagamit natin ang lahat ng 10 perceptrons sa input digits sa pamamagitan ng isang matrix multiplication. Ang pinaka-probable na digit ay maaaring mahanap gamit lamang ang `argmax` operation sa output.

## Panimulang Notebook

Simulan ang lab sa pamamagitan ng pagbukas ng [PerceptronMultiClass.ipynb](PerceptronMultiClass.ipynb)

---

**Paunawa**:  
Ang dokumentong ito ay isinalin gamit ang AI translation service na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagama't sinisikap naming maging tumpak, pakitandaan na ang mga awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o hindi pagkakatugma. Ang orihinal na dokumento sa kanyang katutubong wika ang dapat ituring na opisyal na sanggunian. Para sa mahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang hindi pagkakaunawaan o maling interpretasyon na dulot ng paggamit ng pagsasaling ito.