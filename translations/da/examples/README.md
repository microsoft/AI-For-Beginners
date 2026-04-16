# Begynder-venlige AI-eksempler

Velkommen! Denne mappe indeholder enkle, selvstændige eksempler, der hjælper dig med at komme i gang med AI og maskinlæring. Hvert eksempel er designet til at være begyndervenligt med detaljerede kommentarer og trin-for-trin forklaringer.

## 📚 Oversigt over eksempler

| Eksempel | Beskrivelse | Sværhedsgrad | Forudsætninger |
|----------|-------------|--------------|----------------|
| [Hello AI World](../../../examples/01-hello-ai-world.py) | Dit første AI-program - simpel mønstergenkendelse | ⭐ Begynder | Grundlæggende Python |
| [Simple Neural Network](../../../examples/02-simple-neural-network.py) | Byg et neuralt netværk fra bunden | ⭐⭐ Begynder+ | Python, basal matematik |
| [Image Classifier](./03-image-classifier.ipynb) | Klassificér billeder med en forudtrænet model | ⭐⭐ Begynder+ | Python, numpy |
| [Text Sentiment](../../../examples/04-text-sentiment.py) | Analyser tekststemning (positiv/negativ) | ⭐⭐ Begynder+ | Python |

## 🚀 Kom godt i gang

### Forudsætninger

Sørg for, at du har Python installeret (3.8 eller nyere anbefales). Installer de nødvendige pakker:

```bash
# For Python scripts
pip install numpy

# For Jupyter notebooks (image classifier)
pip install jupyter numpy pillow tensorflow
```

Eller brug conda-miljøet fra hovedpensum:

```bash
conda env create --name ai4beg --file ../environment.yml
conda activate ai4beg
```

### Sådan kører du eksemplerne

**For Python-scripts (.py-filer):**
```bash
python 01-hello-ai-world.py
```

**For Jupyter-notebooks (.ipynb-filer):**
```bash
jupyter notebook 03-image-classifier.ipynb
```

## 📖 Læringssti

Vi anbefaler at følge eksemplerne i rækkefølge:

1. **Start med "Hello AI World"** - Lær det grundlæggende om mønstergenkendelse
2. **Byg et simpelt neuralt netværk** - Forstå, hvordan neurale netværk fungerer
3. **Prøv Image Classifier** - Se AI i aktion med rigtige billeder
4. **Analyser tekststemning** - Udforsk naturlig sprogbehandling

## 💡 Tips til begyndere

- **Læs kodekommentarerne grundigt** - De forklarer, hvad hver linje gør
- **Eksperimentér!** - Prøv at ændre værdier og se, hvad der sker
- **Vær ikke bekymret for at forstå alt** - Læring tager tid
- **Stil spørgsmål** - Brug [diskussionsforummet](https://github.com/microsoft/AI-For-Beginners/discussions)

## 🔗 Næste skridt

Efter at have gennemført disse eksempler, kan du udforske hele pensum:
- [Introduktion til AI](../lessons/1-Intro/README.md)
- [Neurale netværk](../lessons/3-NeuralNetworks/README.md)
- [Computer Vision](../lessons/4-ComputerVision/README.md)
- [Naturlig sprogbehandling](../lessons/5-NLP/README.md)

## 🤝 Bidrag

Fandt du disse eksempler nyttige? Hjælp os med at forbedre dem:
- Rapportér problemer eller foreslå forbedringer
- Tilføj flere eksempler for begyndere
- Forbedr dokumentation og kommentarer

---

*Husk: Hver ekspert har engang været en begynder. God læring! 🎓*

---

**Ansvarsfraskrivelse**:  
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på nøjagtighed, skal det bemærkes, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det originale dokument på dets oprindelige sprog bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi påtager os intet ansvar for misforståelser eller fejltolkninger, der måtte opstå som følge af brugen af denne oversættelse.