# Usposabljanje modela Skip-Gram

Laboratorijska naloga iz [učnega načrta AI za začetnike](https://github.com/microsoft/ai-for-beginners).

## Naloga

V tej laboratorijski nalogi vas izzivamo, da usposobite model Word2Vec z uporabo tehnike Skip-Gram. Usposobite mrežo z vgrajevanjem za napovedovanje sosednjih besed v $N$-tokenov širokem oknu Skip-Gram. Uporabite lahko [kodo iz te lekcije](../../../../../../lessons/5-NLP/15-LanguageModeling/CBoW-TF.ipynb) in jo nekoliko prilagodite.

## Podatkovni niz

Uporabite lahko katerokoli knjigo. Na voljo je veliko brezplačnih besedil na [Project Gutenberg](https://www.gutenberg.org/), na primer, tukaj je neposredna povezava do [Alice's Adventures in Wonderland](https://www.gutenberg.org/files/11/11-0.txt)) avtorja Lewisa Carrolla. Lahko pa uporabite tudi Shakespearove igre, ki jih lahko pridobite z naslednjo kodo:

```python
path_to_file = tf.keras.utils.get_file(
   'shakespeare.txt', 
   'https://storage.googleapis.com/download.tensorflow.org/data/shakespeare.txt')
text = open(path_to_file, 'rb').read().decode(encoding='utf-8')
```

## Raziskujte!

Če imate čas in želite poglobiti svoje znanje, poskusite raziskati več stvari:

* Kako velikost vgrajevanja vpliva na rezultate?
* Kako različni slogi besedila vplivajo na rezultat?
* Vzemite več zelo različnih vrst besed in njihovih sopomenk, pridobite njihove vektorske predstavitve, uporabite PCA za zmanjšanje dimenzij na 2 in jih narišite v 2D prostoru. Ali opazite kakšne vzorce?

**Omejitev odgovornosti**:  
Ta dokument je bil preveden z uporabo storitve za prevajanje z umetno inteligenco [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas prosimo, da upoštevate, da lahko avtomatizirani prevodi vsebujejo napake ali netočnosti. Izvirni dokument v njegovem maternem jeziku je treba obravnavati kot avtoritativni vir. Za ključne informacije priporočamo profesionalni človeški prevod. Ne odgovarjamo za morebitna nesporazumevanja ali napačne razlage, ki izhajajo iz uporabe tega prevoda.