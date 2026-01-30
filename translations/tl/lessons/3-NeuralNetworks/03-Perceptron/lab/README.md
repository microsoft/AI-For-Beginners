# Multi-Class Classification gamit ang Perceptron

Gawain mula sa [AI for Beginners Curriculum](https://github.com/microsoft/ai-for-beginners).

## Gawain

Gamit ang code na ating binuo sa araling ito para sa binary classification ng MNIST handwritten digits, gumawa ng isang multi-class classifier na kayang makilala ang anumang digit. Kalkulahin ang classification accuracy sa train at test dataset, at ipakita ang confusion matrix.

## Mga Pahiwatig

1. Para sa bawat digit, gumawa ng dataset para sa binary classifier ng "ang digit na ito laban sa lahat ng iba pang mga digit"
1. Mag-train ng 10 iba't ibang perceptrons para sa binary classification (isa para sa bawat digit)
1. Magtakda ng isang function na magka-classify sa input digit

> **Pahiwatig**: Kung pagsasamahin natin ang mga weights ng lahat ng 10 perceptrons sa isang matrix, magagamit natin ang lahat ng 10 perceptrons sa input digits sa pamamagitan ng isang matrix multiplication. Ang pinaka-malamang na digit ay maaaring mahanap sa pamamagitan lamang ng paggamit ng `argmax` operation sa output.

## Simulang Notebook

Simulan ang gawain sa pamamagitan ng pagbubukas ng [PerceptronMultiClass.ipynb](PerceptronMultiClass.ipynb)

---

**Paunawa**:  
Ang dokumentong ito ay isinalin gamit ang AI translation service na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagama't sinisikap naming maging tumpak, pakitandaan na ang mga awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o hindi pagkakatugma. Ang orihinal na dokumento sa orihinal nitong wika ang dapat ituring na opisyal na sanggunian. Para sa mahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang hindi pagkakaunawaan o maling interpretasyon na maaaring magmula sa paggamit ng pagsasaling ito.