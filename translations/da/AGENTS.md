# AGENTS.md

## Projektoversigt

AI for Beginners er et omfattende 12-ugers, 24-lektioners pensum, der dækker grundlæggende principper inden for kunstig intelligens. Dette uddannelsesrepository inkluderer praktiske lektioner med Jupyter Notebooks, quizzer og praktiske laboratorier. Pensum dækker:

- Symbolsk AI med vidensrepræsentation og ekspertsystemer
- Neurale netværk og dyb læring med TensorFlow og PyTorch
- Computer Vision-teknikker og arkitekturer
- Naturlig sprogbehandling (NLP) inklusive transformers og BERT
- Specialiserede emner: genetiske algoritmer, forstærkningslæring, multi-agent-systemer
- AI-etik og principper for ansvarlig AI

**Nøgleteknologier:** Python 3, Jupyter Notebooks, TensorFlow, PyTorch, Keras, OpenCV, Vue.js (til quiz-app)

**Arkitektur:** Uddannelsesindhold repository med Jupyter Notebooks organiseret efter emneområder, suppleret med en Vue.js-baseret quiz-applikation og omfattende flersproget support.

## Opsætningskommandoer

### Primært udviklingsmiljø (Python/Jupyter)

Pensum er designet til at køre med Python og Jupyter Notebooks. Den anbefalede tilgang er at bruge miniconda:

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

### Alternativ: Brug af devcontainer

```bash
# Open in VS Code and select "Reopen in Container" when prompted
# The devcontainer will automatically set up the environment
```

### Opsætning af quiz-applikation

Quiz-applikationen er en separat Vue.js-applikation placeret i `etc/quiz-app/`:

```bash
cd etc/quiz-app
npm install
npm run serve  # Development server
npm run build  # Production build
npm run lint   # Lint and fix files
```

## Udviklingsarbejdsgang

### Arbejde med Jupyter Notebooks

1. **Lokal udvikling:**
   - Aktivér conda-miljø: `conda activate ai4beg`
   - Start Jupyter: `jupyter notebook` eller `jupyter lab`
   - Naviger til lektionsmapper og åbn `.ipynb`-filer
   - Kør celler interaktivt for at følge lektionerne

2. **VS Code med Python-udvidelse:**
   - Åbn repository i VS Code
   - Installer Python-udvidelsen
   - VS Code registrerer og bruger automatisk conda-miljøet
   - Åbn `.ipynb`-filer direkte i VS Code

3. **Cloud-udvikling:**
   - **GitHub Codespaces:** Klik på "Code" → "Codespaces" → "Create codespace on main"
   - **Binder:** Brug Binder-badge på README til at starte i browseren
   - Bemærk: Binder har begrænsede ressourcer og nogle webadgangsrestriktioner

### GPU-support til avancerede lektioner

Senere lektioner drager betydeligt fordel af GPU-acceleration:

- **Azure Data Science VM:** Brug NC-serie VMs med GPU-support
- **Azure Machine Learning:** Brug notebook-funktioner med GPU-compute
- **Google Colab:** Upload notebooks individuelt (har gratis GPU-support)

### Udvikling af quiz-app

```bash
cd etc/quiz-app
npm run serve  # Hot-reload development server at http://localhost:8080
```

## Testinstruktioner

Dette er et uddannelsesrepository fokuseret på læringsindhold frem for softwaretest. Der er ingen traditionel test-suite.

### Valideringsmetoder:

1. **Jupyter Notebooks:** Udfør celler sekventielt for at verificere, at kodeeksempler fungerer
2. **Quiz-app-test:** Manuel test via udviklingsserver
3. **Validering af oversættelser:** Tjek oversat indhold i `translations/`-mappen
4. **Linting af quiz-app:** `npm run lint` i `etc/quiz-app/`

### Kørsel af kodeeksempler:

```bash
# Activate environment first
conda activate ai4beg

# Run Python scripts directly
python lessons/4-ComputerVision/07-ConvNets/pytorchcv.py

# Or execute notebooks
jupyter notebook lessons/3-NeuralNetworks/03-Perceptron/Perceptron.ipynb
```

## Kodestil

### Python-kodestil

- Standard Python-konventioner for uddannelseskode
- Klar, læsbar kode med fokus på læring frem for optimering
- Kommentarer, der forklarer nøglebegreber
- Jupyter Notebook-venlig: celler bør være selvstændige, hvor det er muligt
- Ingen strenge lintingkrav for lektionsindhold

### JavaScript/Vue.js (Quiz-app)

- ESLint-konfiguration i `etc/quiz-app/package.json`
- Kør `npm run lint` for at tjekke og automatisk rette problemer
- Vue 2.x-konventioner
- Komponentbaseret arkitektur

### Filorganisering

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

## Bygning og udrulning

### Jupyter-indhold

Ingen byggeproces krævet - Jupyter Notebooks køres direkte.

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

### Dokumentationsside

Repositoryet bruger Docsify til dokumentation:
- `index.html` fungerer som indgangspunkt
- Ingen bygning krævet - serveres direkte via GitHub Pages
- Adgang på: https://microsoft.github.io/AI-For-Beginners/

## Retningslinjer for bidrag

### Pull Request-proces

1. **Titelformat:** Klare, beskrivende titler, der beskriver ændringen
2. **CLA-krav:** Microsoft CLA skal være underskrevet (automatisk kontrol)
3. **Indholdsretningslinjer:**
   - Bevar uddannelsesfokus og begyndervenlig tilgang
   - Test alle kodeeksempler i notebooks
   - Sørg for, at notebooks kører fra start til slut
   - Opdater oversættelser, hvis du ændrer engelsk indhold
4. **Ændringer i quiz-app:** Kør `npm run lint` før commit

### Oversættelsesbidrag

- Oversættelser er automatiserede via GitHub Actions ved hjælp af co-op-translator
- Manuelle oversættelser placeres i `translations/<language-code>/`
- Quiz-oversættelser i `etc/quiz-app/src/assets/translations/`
- Understøttede sprog: 40+ sprog (se README for fuld liste)

### Aktive bidragsområder

Se `etc/CONTRIBUTING.md` for aktuelle behov:
- Sektioner om dyb forstærkningslæring
- Forbedringer af objektdetektion
- Eksempler på navngiven enhedsgenkendelse
- Prøver på træning af brugerdefinerede embeddings

## Miljøkonfiguration

### Krævede afhængigheder

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

### Miljøvariabler

Ingen specielle miljøvariabler krævet for grundlæggende brug.

For Azure-udrulninger (quiz-app):
- `AZURE_STATIC_WEB_APPS_API_TOKEN` (indstillet automatisk af Azure)

## Fejlfinding og problemløsning

### Almindelige problemer

**Problem:** Oprettelse af conda-miljø mislykkes
- **Løsning:** Opdater først conda: `conda update conda -y`
- Sørg for tilstrækkelig diskplads (50GB anbefalet)

**Problem:** Jupyter-kernel ikke fundet
- **Løsning:** 
  ```bash
  conda activate ai4beg
  python -m ipykernel install --user --name ai4beg
  ```

**Problem:** GPU ikke registreret i notebooks
- **Løsning:** 
  - Bekræft CUDA-installation: `nvidia-smi`
  - Tjek PyTorch GPU: `python -c "import torch; print(torch.cuda.is_available())"`
  - Tjek TensorFlow GPU: `python -c "import tensorflow as tf; print(tf.config.list_physical_devices('GPU'))"`

**Problem:** Quiz-app starter ikke
- **Løsning:**
  ```bash
  cd etc/quiz-app
  rm -rf node_modules package-lock.json
  npm install
  npm run serve
  ```

**Problem:** Binder timeout eller blokerer downloads
- **Løsning:** Brug GitHub Codespaces eller lokal opsætning for bedre ressourceadgang

### Hukommelsesproblemer

Nogle lektioner kræver betydelig RAM (8GB+ anbefalet):
- Brug cloud-VM'er til ressourcetunge lektioner
- Luk andre applikationer, når du træner modeller
- Reducer batchstørrelser i notebooks, hvis du løber tør for hukommelse

## Yderligere noter

### For kursusinstruktører

- Se `lessons/0-course-setup/for-teachers.md` for undervisningsvejledning
- Lektionerne er selvstændige og kan undervises i rækkefølge eller vælges individuelt
- Estimeret tid: 12 uger med 2 lektioner om ugen

### Cloud-ressourcer

- **Azure for Students:** Gratis kreditter tilgængelige for studerende
- **Microsoft Learn:** Supplerende læringsforløb linket gennem hele pensum
- **Binder:** Gratis, men begrænsede ressourcer og nogle netværksrestriktioner

### Muligheder for kodekørsel

1. **Lokal (anbefalet):** Fuld kontrol, bedste ydeevne, GPU-support
2. **GitHub Codespaces:** Cloud-baseret VS Code, godt til hurtig adgang
3. **Binder:** Browser-baseret Jupyter, gratis men begrænset
4. **Azure ML Notebooks:** Enterprise-mulighed med GPU-support
5. **Google Colab:** Upload notebooks individuelt, gratis GPU-niveau tilgængeligt

### Arbejde med notebooks

- Notebooks er designet til at blive kørt celle for celle for læring
- Mange notebooks downloader datasæt ved første kørsel (kan tage tid)
- Nogle modeller kræver GPU for rimelige træningstider
- Forudtrænede modeller bruges, hvor det er muligt, for at reducere beregningskrav

### Ydeevneovervejelser

- Senere computer vision-lektioner (CNNs, GANs) drager fordel af GPU
- NLP-transformer-lektioner kan kræve betydelig RAM
- Træning fra bunden er lærerigt, men tidskrævende
- Eksempler på transfer learning minimerer træningstid

---

**Ansvarsfraskrivelse**:  
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på nøjagtighed, skal det bemærkes, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det originale dokument på dets oprindelige sprog bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi påtager os intet ansvar for misforståelser eller fejltolkninger, der måtte opstå som følge af brugen af denne oversættelse.