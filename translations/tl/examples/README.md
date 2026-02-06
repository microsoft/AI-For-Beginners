# Mga Halimbawa ng AI para sa Baguhan

Maligayang pagdating! Ang direktoryong ito ay naglalaman ng mga simpleng halimbawa na standalone upang matulungan kang magsimula sa AI at machine learning. Ang bawat halimbawa ay idinisenyo para sa mga baguhan na may detalyadong mga komento at hakbang-hakbang na paliwanag.

## 📚 Pangkalahatang-ideya ng mga Halimbawa

| Halimbawa | Paglalarawan | Antas ng Hirap | Mga Kinakailangan |
|-----------|--------------|----------------|-------------------|
| [Hello AI World](../../../examples/01-hello-ai-world.py) | Ang iyong unang AI program - simpleng pagkilala ng pattern | ⭐ Baguhan | Mga batayan ng Python |
| [Simple Neural Network](../../../examples/02-simple-neural-network.py) | Gumawa ng neural network mula sa simula | ⭐⭐ Baguhan+ | Python, batayang matematika |
| [Image Classifier](./03-image-classifier.ipynb) | Mag-uri ng mga larawan gamit ang pre-trained na modelo | ⭐⭐ Baguhan+ | Python, numpy |
| [Text Sentiment](../../../examples/04-text-sentiment.py) | Suriin ang damdamin ng teksto (positibo/negatibo) | ⭐⭐ Baguhan+ | Python |

## 🚀 Pagsisimula

### Mga Kinakailangan

Siguraduhing naka-install ang Python (inirerekomenda ang bersyong 3.8 o mas bago). I-install ang mga kinakailangang package:

```bash
# For Python scripts
pip install numpy

# For Jupyter notebooks (image classifier)
pip install jupyter numpy pillow tensorflow
```

O gamitin ang conda environment mula sa pangunahing kurikulum:

```bash
conda env create --name ai4beg --file ../environment.yml
conda activate ai4beg
```

### Pagpapatakbo ng mga Halimbawa

**Para sa mga Python script (.py files):**
```bash
python 01-hello-ai-world.py
```

**Para sa mga Jupyter notebook (.ipynb files):**
```bash
jupyter notebook 03-image-classifier.ipynb
```

## 📖 Landas ng Pagkatuto

Inirerekomenda naming sundin ang mga halimbawa ayon sa pagkakasunod-sunod:

1. **Simulan sa "Hello AI World"** - Alamin ang mga batayan ng pagkilala ng pattern
2. **Gumawa ng Simple Neural Network** - Unawain kung paano gumagana ang mga neural network
3. **Subukan ang Image Classifier** - Tingnan ang AI sa aksyon gamit ang mga totoong larawan
4. **Suriin ang Damdamin ng Teksto** - Tuklasin ang natural language processing

## 💡 Mga Tip para sa mga Baguhan

- **Basahing mabuti ang mga komento sa code** - Ipinaliwanag nito kung ano ang ginagawa ng bawat linya
- **Mag-eksperimento!** - Subukang baguhin ang mga halaga at tingnan ang resulta
- **Huwag mag-alala kung hindi mo agad maiintindihan ang lahat** - Ang pagkatuto ay nangangailangan ng oras
- **Magtanong** - Gamitin ang [Discussion board](https://github.com/microsoft/AI-For-Beginners/discussions)

## 🔗 Mga Susunod na Hakbang

Pagkatapos makumpleto ang mga halimbawang ito, tuklasin ang buong kurikulum:
- [Panimula sa AI](../lessons/1-Intro/README.md)
- [Neural Networks](../lessons/3-NeuralNetworks/README.md)
- [Computer Vision](../lessons/4-ComputerVision/README.md)
- [Natural Language Processing](../lessons/5-NLP/README.md)

## 🤝 Pag-aambag

Nakita mo bang kapaki-pakinabang ang mga halimbawang ito? Tulungan kaming pagandahin pa ang mga ito:
- Mag-ulat ng mga isyu o magmungkahi ng mga pagpapabuti
- Magdagdag ng higit pang mga halimbawa para sa mga baguhan
- Pagandahin ang dokumentasyon at mga komento

---

*Tandaan: Ang bawat eksperto ay minsang naging baguhan. Maligayang pag-aaral! 🎓*

---

**Paunawa**:  
Ang dokumentong ito ay isinalin gamit ang AI translation service na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagama't sinisikap naming maging tumpak, mangyaring tandaan na ang mga awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o hindi pagkakatugma. Ang orihinal na dokumento sa kanyang katutubong wika ang dapat ituring na opisyal na sanggunian. Para sa mahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang hindi pagkakaunawaan o maling interpretasyon na dulot ng paggamit ng pagsasaling ito.