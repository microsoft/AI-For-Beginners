# Aloittelijaystävällisiä AI-esimerkkejä

Tervetuloa! Tämä hakemisto sisältää yksinkertaisia, itsenäisiä esimerkkejä, jotka auttavat sinua pääsemään alkuun tekoälyn ja koneoppimisen parissa. Jokainen esimerkki on suunniteltu aloitteleville käyttäjille, ja niissä on yksityiskohtaiset kommentit sekä vaiheittaiset selitykset.

## 📚 Esimerkkien yleiskatsaus

| Esimerkki | Kuvaus | Vaikeustaso | Esitiedot |
|-----------|--------|-------------|-----------|
| [Hello AI World](../../../examples/01-hello-ai-world.py) | Ensimmäinen AI-ohjelmasi - yksinkertainen kuvioiden tunnistus | ⭐ Aloittelija | Pythonin perusteet |
| [Simple Neural Network](../../../examples/02-simple-neural-network.py) | Rakenna neuroverkko alusta alkaen | ⭐⭐ Aloittelija+ | Python, perusmatematiikka |
| [Image Classifier](./03-image-classifier.ipynb) | Luokittele kuvia valmiiksi koulutetulla mallilla | ⭐⭐ Aloittelija+ | Python, numpy |
| [Text Sentiment](../../../examples/04-text-sentiment.py) | Analysoi tekstin sentimenttiä (positiivinen/negatiivinen) | ⭐⭐ Aloittelija+ | Python |

## 🚀 Aloittaminen

### Esitiedot

Varmista, että sinulla on Python asennettuna (suositeltu versio 3.8 tai uudempi). Asenna tarvittavat paketit:

```bash
# For Python scripts
pip install numpy

# For Jupyter notebooks (image classifier)
pip install jupyter numpy pillow tensorflow
```

Tai käytä pääopetussuunnitelman conda-ympäristöä:

```bash
conda env create --name ai4beg --file ../environment.yml
conda activate ai4beg
```

### Esimerkkien suorittaminen

**Python-skripteille (.py-tiedostot):**
```bash
python 01-hello-ai-world.py
```

**Jupyter-notebookeille (.ipynb-tiedostot):**
```bash
jupyter notebook 03-image-classifier.ipynb
```

## 📖 Oppimispolku

Suosittelemme seuraamaan esimerkkejä järjestyksessä:

1. **Aloita "Hello AI World" -esimerkillä** - Opettele kuvioiden tunnistuksen perusteet
2. **Rakenna yksinkertainen neuroverkko** - Ymmärrä, miten neuroverkot toimivat
3. **Kokeile kuvaluokittelijaa** - Näe tekoäly toiminnassa oikeiden kuvien kanssa
4. **Analysoi tekstin sentimenttiä** - Tutustu luonnollisen kielen käsittelyyn

## 💡 Vinkkejä aloittelijoille

- **Lue koodikommentit huolellisesti** - Ne selittävät, mitä kukin rivi tekee
- **Kokeile!** - Muuta arvoja ja katso, mitä tapahtuu
- **Älä huolehdi, jos et ymmärrä kaikkea** - Oppiminen vie aikaa
- **Kysy kysymyksiä** - Käytä [Keskustelupalstaa](https://github.com/microsoft/AI-For-Beginners/discussions)

## 🔗 Seuraavat askeleet

Kun olet käynyt läpi nämä esimerkit, tutustu koko opetussuunnitelmaan:
- [Johdatus tekoälyyn](../lessons/1-Intro/README.md)
- [Neuroverkot](../lessons/3-NeuralNetworks/README.md)
- [Tietokonenäkö](../lessons/4-ComputerVision/README.md)
- [Luonnollisen kielen käsittely](../lessons/5-NLP/README.md)

## 🤝 Osallistuminen

Ovatko nämä esimerkit hyödyllisiä? Auta meitä parantamaan niitä:
- Ilmoita ongelmista tai ehdota parannuksia
- Lisää lisää esimerkkejä aloittelijoille
- Paranna dokumentaatiota ja kommentteja

---

*Muista: Jokainen asiantuntija on joskus ollut aloittelija. Mukavia oppimishetkiä! 🎓*

---

**Vastuuvapauslauseke**:  
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, huomioithan, että automaattiset käännökset voivat sisältää virheitä tai epätarkkuuksia. Alkuperäistä asiakirjaa sen alkuperäisellä kielellä tulisi pitää ensisijaisena lähteenä. Kriittisen tiedon osalta suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa väärinkäsityksistä tai virhetulkinnoista, jotka johtuvat tämän käännöksen käytöstä.