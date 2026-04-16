# Przykłady AI dla Początkujących

Witaj! Ten katalog zawiera proste, samodzielne przykłady, które pomogą Ci rozpocząć przygodę z AI i uczeniem maszynowym. Każdy przykład został zaprojektowany z myślą o początkujących, z dokładnymi komentarzami i wyjaśnieniami krok po kroku.

## 📚 Przegląd Przykładów

| Przykład | Opis | Poziom trudności | Wymagania wstępne |
|----------|------|------------------|-------------------|
| [Hello AI World](../../../examples/01-hello-ai-world.py) | Twój pierwszy program AI - proste rozpoznawanie wzorców | ⭐ Początkujący | Podstawy Pythona |
| [Prosta Sieć Neuronowa](../../../examples/02-simple-neural-network.py) | Zbuduj sieć neuronową od podstaw | ⭐⭐ Początkujący+ | Python, podstawowa matematyka |
| [Klasyfikator Obrazów](./03-image-classifier.ipynb) | Klasyfikuj obrazy za pomocą wstępnie wytrenowanego modelu | ⭐⭐ Początkujący+ | Python, numpy |
| [Analiza Sentimentów Tekstu](../../../examples/04-text-sentiment.py) | Analizuj sentyment tekstu (pozytywny/negatywny) | ⭐⭐ Początkujący+ | Python |

## 🚀 Rozpoczęcie Pracy

### Wymagania wstępne

Upewnij się, że masz zainstalowany Python (zalecana wersja 3.8 lub wyższa). Zainstaluj wymagane pakiety:

```bash
# For Python scripts
pip install numpy

# For Jupyter notebooks (image classifier)
pip install jupyter numpy pillow tensorflow
```

Lub skorzystaj z środowiska conda z głównego programu nauczania:

```bash
conda env create --name ai4beg --file ../environment.yml
conda activate ai4beg
```

### Uruchamianie Przykładów

**Dla skryptów Python (.py):**
```bash
python 01-hello-ai-world.py
```

**Dla notebooków Jupyter (.ipynb):**
```bash
jupyter notebook 03-image-classifier.ipynb
```

## 📖 Ścieżka Nauki

Zalecamy realizowanie przykładów w następującej kolejności:

1. **Rozpocznij od "Hello AI World"** - Poznaj podstawy rozpoznawania wzorców
2. **Zbuduj Prostą Sieć Neuronową** - Zrozum, jak działają sieci neuronowe
3. **Wypróbuj Klasyfikator Obrazów** - Zobacz AI w akcji na prawdziwych obrazach
4. **Analizuj Sentiment Tekstu** - Odkryj przetwarzanie języka naturalnego

## 💡 Wskazówki dla Początkujących

- **Dokładnie czytaj komentarze w kodzie** - Wyjaśniają, co robi każda linia
- **Eksperymentuj!** - Spróbuj zmieniać wartości i zobacz, co się stanie
- **Nie martw się, jeśli nie zrozumiesz wszystkiego od razu** - Nauka wymaga czasu
- **Zadawaj pytania** - Skorzystaj z [Forum dyskusyjnego](https://github.com/microsoft/AI-For-Beginners/discussions)

## 🔗 Kolejne Kroki

Po ukończeniu tych przykładów, zapoznaj się z pełnym programem nauczania:
- [Wprowadzenie do AI](../lessons/1-Intro/README.md)
- [Sieci Neuronowe](../lessons/3-NeuralNetworks/README.md)
- [Wizja Komputerowa](../lessons/4-ComputerVision/README.md)
- [Przetwarzanie Języka Naturalnego](../lessons/5-NLP/README.md)

## 🤝 Współtworzenie

Uważasz, że te przykłady są pomocne? Pomóż nam je ulepszyć:
- Zgłaszaj problemy lub proponuj ulepszenia
- Dodawaj więcej przykładów dla początkujących
- Poprawiaj dokumentację i komentarze

---

*Pamiętaj: Każdy ekspert kiedyś był początkującym. Miłej nauki! 🎓*

---

**Zastrzeżenie**:  
Ten dokument został przetłumaczony za pomocą usługi tłumaczenia AI [Co-op Translator](https://github.com/Azure/co-op-translator). Chociaż dokładamy wszelkich starań, aby tłumaczenie było precyzyjne, prosimy pamiętać, że automatyczne tłumaczenia mogą zawierać błędy lub nieścisłości. Oryginalny dokument w jego języku źródłowym powinien być uznawany za autorytatywne źródło. W przypadku informacji o kluczowym znaczeniu zaleca się skorzystanie z profesjonalnego tłumaczenia przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z użycia tego tłumaczenia.