# AGENTS.md

## Projektöversikt

AI for Beginners är en omfattande 12-veckors, 24-lektions läroplan som täcker grunderna i artificiell intelligens. Detta utbildningsarkiv innehåller praktiska lektioner med Jupyter Notebooks, quiz och praktiska labbar. Läroplanen täcker:

- Symbolisk AI med kunskapsrepresentation och expertsystem
- Neurala nätverk och djupinlärning med TensorFlow och PyTorch
- Datorseendetekniker och arkitekturer
- Naturlig språkbehandling (NLP) inklusive transformers och BERT
- Specialiserade ämnen: genetiska algoritmer, förstärkningsinlärning, multi-agent-system
- AI-etik och principer för ansvarsfull AI

**Nyckelteknologier:** Python 3, Jupyter Notebooks, TensorFlow, PyTorch, Keras, OpenCV, Vue.js (för quiz-applikation)

**Arkitektur:** Utbildningsinnehållsarkiv med Jupyter Notebooks organiserade efter ämnesområden, kompletterat med en Vue.js-baserad quiz-applikation och omfattande flerspråkigt stöd.

## Installationskommandon

### Primär utvecklingsmiljö (Python/Jupyter)

Läroplanen är utformad för att köras med Python och Jupyter Notebooks. Den rekommenderade metoden är att använda miniconda:

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

### Alternativ: Använda devcontainer

```bash
# Open in VS Code and select "Reopen in Container" when prompted
# The devcontainer will automatically set up the environment
```

### Quiz-applikationens installation

Quiz-applikationen är en separat Vue.js-applikation som finns i `etc/quiz-app/`:

```bash
cd etc/quiz-app
npm install
npm run serve  # Development server
npm run build  # Production build
npm run lint   # Lint and fix files
```

## Utvecklingsarbetsflöde

### Arbeta med Jupyter Notebooks

1. **Lokal utveckling:**
   - Aktivera conda-miljön: `conda activate ai4beg`
   - Starta Jupyter: `jupyter notebook` eller `jupyter lab`
   - Navigera till lektionsmappar och öppna `.ipynb`-filer
   - Kör celler interaktivt för att följa lektionerna

2. **VS Code med Python-tillägg:**
   - Öppna arkivet i VS Code
   - Installera Python-tillägget
   - VS Code upptäcker och använder automatiskt conda-miljön
   - Öppna `.ipynb`-filer direkt i VS Code

3. **Molnutveckling:**
   - **GitHub Codespaces:** Klicka på "Code" → "Codespaces" → "Create codespace on main"
   - **Binder:** Använd Binder-märket på README för att starta i webbläsaren
   - Obs: Binder har begränsade resurser och vissa webbrestriktioner

### GPU-stöd för avancerade lektioner

Senare lektioner drar betydligt nytta av GPU-acceleration:

- **Azure Data Science VM:** Använd NC-seriens VM med GPU-stöd
- **Azure Machine Learning:** Använd notebook-funktioner med GPU-beräkning
- **Google Colab:** Ladda upp notebooks individuellt (har gratis GPU-stöd)

### Quiz-apputveckling

```bash
cd etc/quiz-app
npm run serve  # Hot-reload development server at http://localhost:8080
```

## Testinstruktioner

Detta är ett utbildningsarkiv som fokuserar på lärandeinnehåll snarare än mjukvarutestning. Det finns ingen traditionell testsvit.

### Valideringsmetoder:

1. **Jupyter Notebooks:** Kör celler sekventiellt för att verifiera att kodexemplen fungerar
2. **Quiz-apptestning:** Manuell testning via utvecklingsserver
3. **Validering av översättningar:** Kontrollera översatt innehåll i mappen `translations/`
4. **Quiz-applintning:** `npm run lint` i `etc/quiz-app/`

### Köra kodexempel:

```bash
# Activate environment first
conda activate ai4beg

# Run Python scripts directly
python lessons/4-ComputerVision/07-ConvNets/pytorchcv.py

# Or execute notebooks
jupyter notebook lessons/3-NeuralNetworks/03-Perceptron/Perceptron.ipynb
```

## Kodstil

### Python-kodstil

- Standard Python-konventioner för utbildningskod
- Tydlig, läsbar kod som prioriterar lärande framför optimering
- Kommentarer som förklarar nyckelkoncept
- Jupyter Notebook-vänlig: celler bör vara självständiga där det är möjligt
- Inga strikta lintningskrav för lektionsinnehåll

### JavaScript/Vue.js (Quiz-app)

- ESLint-konfiguration i `etc/quiz-app/package.json`
- Kör `npm run lint` för att kontrollera och automatiskt åtgärda problem
- Vue 2.x-konventioner
- Komponentbaserad arkitektur

### Filorganisation

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

## Bygg och distribution

### Jupyter-innehåll

Ingen byggprocess krävs - Jupyter Notebooks körs direkt.

### Quiz-applikation

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

### Dokumentationssida

Arkivet använder Docsify för dokumentation:
- `index.html` fungerar som ingångspunkt
- Ingen byggning krävs - serveras direkt via GitHub Pages
- Åtkomst på: https://microsoft.github.io/AI-For-Beginners/

## Riktlinjer för bidrag

### Pull Request-process

1. **Titelformat:** Tydliga, beskrivande titlar som beskriver ändringen
2. **CLA-krav:** Microsoft CLA måste vara signerad (automatisk kontroll)
3. **Innehållsriktlinjer:**
   - Bibehåll utbildningsfokus och nybörjarvänlig approach
   - Testa alla kodexempel i notebooks
   - Säkerställ att notebooks körs från början till slut
   - Uppdatera översättningar om engelskt innehåll ändras
4. **Ändringar i quiz-appen:** Kör `npm run lint` innan du begår ändringar

### Översättningsbidrag

- Översättningar automatiseras via GitHub Actions med co-op-translator
- Manuella översättningar placeras i `translations/<language-code>/`
- Quiz-översättningar i `etc/quiz-app/src/assets/translations/`
- Stödda språk: 40+ språk (se README för fullständig lista)

### Aktiva bidragsområden

Se `etc/CONTRIBUTING.md` för aktuella behov:
- Sektioner om djup förstärkningsinlärning
- Förbättringar av objektdetektion
- Exempel på namngiven entity-igenkänning
- Anpassade inbäddningsträningsprover

## Miljökonfiguration

### Nödvändiga beroenden

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

### Miljövariabler

Inga speciella miljövariabler krävs för grundläggande användning.

För Azure-distributioner (quiz-app):
- `AZURE_STATIC_WEB_APPS_API_TOKEN` (ställs in automatiskt av Azure)

## Felsökning och problemlösning

### Vanliga problem

**Problem:** Skapande av conda-miljö misslyckas
- **Lösning:** Uppdatera först conda: `conda update conda -y`
- Säkerställ tillräckligt med diskutrymme (50GB rekommenderas)

**Problem:** Jupyter-kärna hittas inte
- **Lösning:** 
  ```bash
  conda activate ai4beg
  python -m ipykernel install --user --name ai4beg
  ```

**Problem:** GPU upptäcks inte i notebooks
- **Lösning:** 
  - Verifiera CUDA-installation: `nvidia-smi`
  - Kontrollera PyTorch GPU: `python -c "import torch; print(torch.cuda.is_available())"`
  - Kontrollera TensorFlow GPU: `python -c "import tensorflow as tf; print(tf.config.list_physical_devices('GPU'))"`

**Problem:** Quiz-appen startar inte
- **Lösning:**
  ```bash
  cd etc/quiz-app
  rm -rf node_modules package-lock.json
  npm install
  npm run serve
  ```

**Problem:** Binder timeout eller blockerar nedladdningar
- **Lösning:** Använd GitHub Codespaces eller lokal installation för bättre resursåtkomst

### Minnesproblem

Vissa lektioner kräver betydande RAM (8GB+ rekommenderas):
- Använd moln-VMs för resursintensiva lektioner
- Stäng andra applikationer när du tränar modeller
- Minska batchstorlekar i notebooks om minnet tar slut

## Ytterligare anteckningar

### För kursinstruktörer

- Se `lessons/0-course-setup/for-teachers.md` för undervisningsvägledning
- Lektionerna är självständiga och kan läras i sekvens eller väljas individuellt
- Beräknad tid: 12 veckor med 2 lektioner per vecka

### Molnresurser

- **Azure för studenter:** Gratis krediter tillgängliga för studenter
- **Microsoft Learn:** Kompletterande lärvägar länkade genomgående
- **Binder:** Gratis men begränsade resurser och vissa nätverksrestriktioner

### Alternativ för kodkörning

1. **Lokal (Rekommenderas):** Full kontroll, bästa prestanda, GPU-stöd
2. **GitHub Codespaces:** Molnbaserad VS Code, bra för snabb åtkomst
3. **Binder:** Webbläsarbaserad Jupyter, gratis men begränsad
4. **Azure ML Notebooks:** Företagsalternativ med GPU-stöd
5. **Google Colab:** Ladda upp notebooks individuellt, gratis GPU-nivå tillgänglig

### Arbeta med notebooks

- Notebooks är utformade för att köras cell-för-cell för lärande
- Många notebooks laddar ner dataset vid första körningen (kan ta tid)
- Vissa modeller kräver GPU för rimliga träningstider
- Förtränade modeller används där det är möjligt för att minska beräkningskraven

### Prestandaöverväganden

- Senare lektioner om datorseende (CNNs, GANs) drar nytta av GPU
- NLP-transformerlektioner kan kräva betydande RAM
- Träning från grunden är utbildande men tidskrävande
- Exempel på transferinlärning minimerar träningstiden

---

**Ansvarsfriskrivning**:  
Detta dokument har översatts med hjälp av AI-översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Även om vi strävar efter noggrannhet, bör det noteras att automatiska översättningar kan innehålla fel eller felaktigheter. Det ursprungliga dokumentet på dess originalspråk bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för eventuella missförstånd eller feltolkningar som uppstår vid användning av denna översättning.