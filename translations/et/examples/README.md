# Algajatele sobivad tehisintellekti näited

Tere tulemast! See kataloog sisaldab lihtsaid ja iseseisvaid näiteid, mis aitavad sul alustada tehisintellekti ja masinõppega. Iga näide on loodud algajasõbralikuks, sisaldades üksikasjalikke kommentaare ja samm-sammulisi selgitusi.

## 📚 Näidete ülevaade

| Näide | Kirjeldus | Raskusaste | Eelteadmised |
|-------|-----------|------------|--------------|
| [Tere, AI maailm](../../../examples/01-hello-ai-world.py) | Sinu esimene tehisintellekti programm - lihtne mustrituvastus | ⭐ Algaja | Pythoni algteadmised |
| [Lihtne närvivõrk](../../../examples/02-simple-neural-network.py) | Loo närvivõrk nullist | ⭐⭐ Algaja+ | Python, põhiteadmised matemaatikast |
| [Pildiklassifitseerija](./03-image-classifier.ipynb) | Klassifitseeri pilte eelnevalt treenitud mudeliga | ⭐⭐ Algaja+ | Python, numpy |
| [Teksti sentiment](../../../examples/04-text-sentiment.py) | Analüüsi teksti sentimenti (positiivne/negatiivne) | ⭐⭐ Algaja+ | Python |

## 🚀 Alustamine

### Eeltingimused

Veendu, et sul on Python installitud (soovitatav versioon 3.8 või uuem). Paigalda vajalikud paketid:

```bash
# For Python scripts
pip install numpy

# For Jupyter notebooks (image classifier)
pip install jupyter numpy pillow tensorflow
```

Või kasuta põhikursuse conda keskkonda:

```bash
conda env create --name ai4beg --file ../environment.yml
conda activate ai4beg
```

### Näidete käivitamine

**Python skriptide (.py failid) jaoks:**
```bash
python 01-hello-ai-world.py
```

**Jupyteri märkmike (.ipynb failid) jaoks:**
```bash
jupyter notebook 03-image-classifier.ipynb
```

## 📖 Õppimise teekond

Soovitame järgida näiteid järjekorras:

1. **Alusta "Tere, AI maailm" näitest** - Õpi mustrituvastuse põhitõdesid
2. **Ehita lihtne närvivõrk** - Mõista, kuidas närvivõrgud töötavad
3. **Proovi pildiklassifitseerijat** - Näe tehisintellekti töös päris piltidega
4. **Analüüsi teksti sentimenti** - Uuri loomuliku keele töötlemist

## 💡 Näpunäiteid algajatele

- **Loe hoolikalt koodikommentaare** - Need selgitavad, mida iga rida teeb
- **Katseta!** - Proovi muuta väärtusi ja vaata, mis juhtub
- **Ära muretse, kui kõike kohe ei mõista** - Õppimine võtab aega
- **Küsi küsimusi** - Kasuta [arutelufoorumit](https://github.com/microsoft/AI-For-Beginners/discussions)

## 🔗 Järgmised sammud

Pärast nende näidete läbimist avasta kogu õppekava:
- [Sissejuhatus tehisintellekti](../lessons/1-Intro/README.md)
- [Närvivõrgud](../lessons/3-NeuralNetworks/README.md)
- [Arvutinägemine](../lessons/4-ComputerVision/README.md)
- [Loomuliku keele töötlemine](../lessons/5-NLP/README.md)

## 🤝 Kaasaaitamine

Leidsid need näited kasulikud? Aita meil neid paremaks muuta:
- Teata probleemidest või tee parandusettepanekuid
- Lisa rohkem algajatele mõeldud näiteid
- Paranda dokumentatsiooni ja kommentaare

---

*Pea meeles: Iga ekspert on kunagi olnud algaja. Head õppimist! 🎓*

---

**Lahtiütlus**:  
See dokument on tõlgitud, kasutades AI tõlketeenust [Co-op Translator](https://github.com/Azure/co-op-translator). Kuigi püüame tagada täpsust, palun arvestage, et automaatsed tõlked võivad sisaldada vigu või ebatäpsusi. Algne dokument selle algses keeles tuleks lugeda autoriteetseks allikaks. Olulise teabe puhul on soovitatav kasutada professionaalset inimtõlget. Me ei vastuta selle tõlke kasutamisest tulenevate arusaamatuste või valede tõlgenduste eest.