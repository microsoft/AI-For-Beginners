# AGENTS.md

## Przegląd projektu

AI for Beginners to kompleksowy 12-tygodniowy, 24-lekcyjny program nauczania obejmujący podstawy sztucznej inteligencji. Repozytorium edukacyjne zawiera praktyczne lekcje z użyciem Jupyter Notebooks, quizy oraz laboratoria praktyczne. Program nauczania obejmuje:

- Symboliczną AI z reprezentacją wiedzy i systemami ekspertowymi
- Sieci neuronowe i głębokie uczenie z TensorFlow i PyTorch
- Techniki i architektury widzenia komputerowego
- Przetwarzanie języka naturalnego (NLP), w tym transformery i BERT
- Tematy specjalistyczne: algorytmy genetyczne, uczenie ze wzmocnieniem, systemy wieloagentowe
- Etyka AI i zasady odpowiedzialnej sztucznej inteligencji

**Kluczowe technologie:** Python 3, Jupyter Notebooks, TensorFlow, PyTorch, Keras, OpenCV, Vue.js (dla aplikacji quizowej)

**Architektura:** Repozytorium treści edukacyjnych z Jupyter Notebooks zorganizowane według obszarów tematycznych, uzupełnione aplikacją quizową opartą na Vue.js oraz szerokim wsparciem wielojęzycznym.

## Polecenia konfiguracji

### Podstawowe środowisko programistyczne (Python/Jupyter)

Program nauczania jest zaprojektowany do uruchamiania z Pythonem i Jupyter Notebooks. Zalecanym podejściem jest użycie miniconda:

```bash
# Clone the repository
git clone https://github.com/microsoft/ai-for-beginners
cd ai-for-beginners

# Create and activate conda environment
conda env create --name ai4beg --file environment.yml
conda activate ai4beg

# Start Jupyter Notebook
jupyter notebook
# OR
jupyter lab
```

### Alternatywa: Użycie devcontainer

```bash
# Open in VS Code and select "Reopen in Container" when prompted
# The devcontainer will automatically set up the environment
```

### Konfiguracja aplikacji quizowej

Aplikacja quizowa to oddzielna aplikacja Vue.js znajdująca się w `etc/quiz-app/`:

```bash
cd etc/quiz-app
npm install
npm run serve  # Development server
npm run build  # Production build
npm run lint   # Lint and fix files
```

## Przepływ pracy programistycznej

### Praca z Jupyter Notebooks

1. **Rozwój lokalny:**
   - Aktywuj środowisko conda: `conda activate ai4beg`
   - Uruchom Jupyter: `jupyter notebook` lub `jupyter lab`
   - Przejdź do folderów lekcji i otwórz pliki `.ipynb`
   - Uruchamiaj komórki interaktywnie, aby śledzić lekcje

2. **VS Code z rozszerzeniem Python:**
   - Otwórz repozytorium w VS Code
   - Zainstaluj rozszerzenie Python
   - VS Code automatycznie wykrywa i używa środowiska conda
   - Otwórz pliki `.ipynb` bezpośrednio w VS Code

3. **Rozwój w chmurze:**
   - **GitHub Codespaces:** Kliknij "Code" → "Codespaces" → "Create codespace on main"
   - **Binder:** Użyj odznaki Binder na README, aby uruchomić w przeglądarce
   - Uwaga: Binder ma ograniczone zasoby i pewne ograniczenia dostępu do sieci

### Wsparcie GPU dla zaawansowanych lekcji

Późniejsze lekcje znacznie korzystają z przyspieszenia GPU:

- **Azure Data Science VM:** Użyj maszyn NC-series z obsługą GPU
- **Azure Machine Learning:** Użyj funkcji notebooków z obliczeniami GPU
- **Google Colab:** Prześlij notatniki indywidualnie (dostępne darmowe wsparcie GPU)

### Rozwój aplikacji quizowej

```bash
cd etc/quiz-app
npm run serve  # Hot-reload development server at http://localhost:8080
```

## Instrukcje testowania

To repozytorium edukacyjne skupia się na treściach edukacyjnych, a nie na testowaniu oprogramowania. Nie ma tradycyjnego zestawu testów.

### Podejścia do walidacji:

1. **Jupyter Notebooks:** Uruchamiaj komórki sekwencyjnie, aby zweryfikować działanie przykładów kodu
2. **Testowanie aplikacji quizowej:** Testowanie ręczne za pomocą serwera deweloperskiego
3. **Walidacja tłumaczeń:** Sprawdź przetłumaczone treści w folderze `translations/`
4. **Linting aplikacji quizowej:** `npm run lint` w `etc/quiz-app/`

### Uruchamianie przykładów kodu:

```bash
# Activate environment first
conda activate ai4beg

# Run Python scripts directly
python lessons/4-ComputerVision/07-ConvNets/pytorchcv.py

# Or execute notebooks
jupyter notebook lessons/3-NeuralNetworks/03-Perceptron/Perceptron.ipynb
```

## Styl kodu

### Styl kodu Python

- Standardowe konwencje Pythona dla kodu edukacyjnego
- Jasny, czytelny kod, priorytetem jest nauka, a nie optymalizacja
- Komentarze wyjaśniające kluczowe koncepcje
- Przyjazne dla Jupyter Notebook: komórki powinny być możliwie samodzielne
- Brak rygorystycznych wymagań lintingu dla treści lekcji

### JavaScript/Vue.js (aplikacja quizowa)

- Konfiguracja ESLint w `etc/quiz-app/package.json`
- Uruchom `npm run lint`, aby sprawdzić i automatycznie naprawić problemy
- Konwencje Vue 2.x
- Architektura oparta na komponentach

### Organizacja plików

```
lessons/
  ├── 0-course-setup/          # Setup instructions
  ├── 1-Intro/                 # Introduction to AI
  ├── 2-Symbolic/              # Symbolic AI
  ├── 3-NeuralNetworks/        # Neural Networks basics
  ├── 4-ComputerVision/        # Computer Vision
  ├── 5-NLP/                   # Natural Language Processing
  ├── 6-Other/                 # Other AI techniques
  ├── 7-Ethics/                # AI Ethics
  └── X-Extras/                # Additional content

etc/
  ├── quiz-app/                # Vue.js quiz application
  └── quiz-src/                # Quiz source files

translations/                  # Multi-language translations
```

## Budowa i wdrożenie

### Treści Jupyter

Nie wymaga procesu budowy - Jupyter Notebooks są uruchamiane bezpośrednio.

### Aplikacja quizowa

```bash
cd etc/quiz-app

# Development
npm run serve

# Production build
npm run build  # Outputs to etc/quiz-app/dist/

# Deploy to Azure Static Web Apps
# Azure automatically creates GitHub Actions workflow
# See etc/quiz-app/README.md for detailed deployment instructions
```

### Strona dokumentacji

Repozytorium używa Docsify do dokumentacji:
- `index.html` służy jako punkt wejścia
- Nie wymaga budowy - serwowane bezpośrednio przez GitHub Pages
- Dostęp pod adresem: https://microsoft.github.io/AI-For-Beginners/

## Wytyczne dotyczące wkładu

### Proces Pull Request

1. **Format tytułu:** Jasne, opisowe tytuły opisujące zmiany
2. **Wymóg CLA:** Microsoft CLA musi być podpisany (automatyczna kontrola)
3. **Wytyczne dotyczące treści:**
   - Zachowaj edukacyjny charakter i podejście przyjazne dla początkujących
   - Przetestuj wszystkie przykłady kodu w notatnikach
   - Upewnij się, że notatniki działają od początku do końca
   - Zaktualizuj tłumaczenia, jeśli zmieniasz treści w języku angielskim
4. **Zmiany w aplikacji quizowej:** Uruchom `npm run lint` przed zatwierdzeniem

### Wkład w tłumaczenia

- Tłumaczenia są automatyzowane za pomocą GitHub Actions z użyciem co-op-translator
- Ręczne tłumaczenia trafiają do `translations/<language-code>/`
- Tłumaczenia quizów w `etc/quiz-app/src/assets/translations/`
- Obsługiwane języki: ponad 40 języków (zobacz README dla pełnej listy)

### Aktywne obszary wkładu

Zobacz `etc/CONTRIBUTING.md` dla aktualnych potrzeb:
- Sekcje dotyczące głębokiego uczenia ze wzmocnieniem
- Ulepszenia wykrywania obiektów
- Przykłady rozpoznawania nazwanych jednostek
- Próbki treningowe niestandardowych osadzeń

## Konfiguracja środowiska

### Wymagane zależności

```bash
# Core Python packages (from requirements.txt)
tensorflow==2.17.0
torch (via conda)
torchvision (via conda)
keras==3.5.0
opencv (via conda)
scikit-learn
numpy==1.26
pandas==2.2.2
matplotlib==3.9
jupyter
```

### Zmienne środowiskowe

Nie są wymagane specjalne zmienne środowiskowe dla podstawowego użytkowania.

Dla wdrożeń Azure (aplikacja quizowa):
- `AZURE_STATIC_WEB_APPS_API_TOKEN` (ustawiane automatycznie przez Azure)

## Debugowanie i rozwiązywanie problemów

### Typowe problemy

**Problem:** Tworzenie środowiska conda nie powiodło się
- **Rozwiązanie:** Najpierw zaktualizuj conda: `conda update conda -y`
- Upewnij się, że masz wystarczającą ilość miejsca na dysku (zalecane 50GB)

**Problem:** Nie znaleziono jądra Jupyter
- **Rozwiązanie:** 
  ```bash
  conda activate ai4beg
  python -m ipykernel install --user --name ai4beg
  ```

**Problem:** GPU nie jest wykrywane w notatnikach
- **Rozwiązanie:** 
  - Zweryfikuj instalację CUDA: `nvidia-smi`
  - Sprawdź GPU w PyTorch: `python -c "import torch; print(torch.cuda.is_available())"`
  - Sprawdź GPU w TensorFlow: `python -c "import tensorflow as tf; print(tf.config.list_physical_devices('GPU'))"`

**Problem:** Aplikacja quizowa nie uruchamia się
- **Rozwiązanie:**
  ```bash
  cd etc/quiz-app
  rm -rf node_modules package-lock.json
  npm install
  npm run serve
  ```

**Problem:** Binder przekracza limit czasu lub blokuje pobieranie
- **Rozwiązanie:** Użyj GitHub Codespaces lub lokalnej konfiguracji dla lepszego dostępu do zasobów

### Problemy z pamięcią

Niektóre lekcje wymagają znacznej ilości RAM (zalecane 8GB+):
- Użyj maszyn w chmurze dla lekcji wymagających dużych zasobów
- Zamknij inne aplikacje podczas trenowania modeli
- Zmniejsz rozmiary partii w notatnikach, jeśli brakuje pamięci

## Dodatkowe uwagi

### Dla instruktorów kursu

- Zobacz `lessons/0-course-setup/for-teachers.md` dla wskazówek dotyczących nauczania
- Lekcje są samodzielne i mogą być prowadzone w kolejności lub wybierane indywidualnie
- Szacowany czas: 12 tygodni przy 2 lekcjach tygodniowo

### Zasoby w chmurze

- **Azure dla studentów:** Dostępne darmowe kredyty dla studentów
- **Microsoft Learn:** Dodatkowe ścieżki edukacyjne powiązane w całym kursie
- **Binder:** Darmowe, ale ograniczone zasoby i pewne ograniczenia sieciowe

### Opcje uruchamiania kodu

1. **Lokalnie (zalecane):** Pełna kontrola, najlepsza wydajność, wsparcie GPU
2. **GitHub Codespaces:** Chmurowe VS Code, dobre do szybkiego dostępu
3. **Binder:** Jupyter w przeglądarce, darmowe, ale ograniczone
4. **Azure ML Notebooks:** Opcja korporacyjna z obsługą GPU
5. **Google Colab:** Prześlij notatniki indywidualnie, dostępny darmowy poziom GPU

### Praca z notatnikami

- Notatniki są zaprojektowane do uruchamiania komórka po komórce w celu nauki
- Wiele notatników pobiera zestawy danych przy pierwszym uruchomieniu (może to zająć trochę czasu)
- Niektóre modele wymagają GPU dla rozsądnych czasów treningu
- Modele wstępnie wytrenowane są używane tam, gdzie to możliwe, aby zmniejszyć wymagania obliczeniowe

### Rozważania dotyczące wydajności

- Późniejsze lekcje dotyczące widzenia komputerowego (CNN, GAN) korzystają z GPU
- Lekcje dotyczące transformatorów NLP mogą wymagać znacznej ilości RAM
- Trenowanie od podstaw jest edukacyjne, ale czasochłonne
- Przykłady transfer learningu minimalizują czas treningu

---

**Zastrzeżenie**:  
Ten dokument został przetłumaczony za pomocą usługi tłumaczenia AI [Co-op Translator](https://github.com/Azure/co-op-translator). Chociaż dokładamy wszelkich starań, aby tłumaczenie było precyzyjne, prosimy pamiętać, że automatyczne tłumaczenia mogą zawierać błędy lub nieścisłości. Oryginalny dokument w jego języku źródłowym powinien być uznawany za autorytatywne źródło. W przypadku informacji o kluczowym znaczeniu zaleca się skorzystanie z profesjonalnego tłumaczenia przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z użycia tego tłumaczenia.