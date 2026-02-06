# AGENTS.md

## Prosjektoversikt

AI for Beginners er et omfattende 12-ukers, 24-leksjons pensum som dekker grunnleggende prinsipper innen kunstig intelligens. Dette utdanningslageret inkluderer praktiske leksjoner med Jupyter Notebooks, quizzer og praktiske laboratorier. Pensumet dekker:

- Symbolsk AI med kunnskapsrepresentasjon og ekspertssystemer
- Nevrale nettverk og dyp læring med TensorFlow og PyTorch
- Datamaskinsynsteknikker og arkitekturer
- Naturlig språkbehandling (NLP) inkludert transformatorer og BERT
- Spesialiserte emner: genetiske algoritmer, forsterkende læring, multi-agent systemer
- AI-etikk og prinsipper for ansvarlig AI

**Nøkkelteknologier:** Python 3, Jupyter Notebooks, TensorFlow, PyTorch, Keras, OpenCV, Vue.js (for quiz-app)

**Arkitektur:** Utdanningsinnholdslager med Jupyter Notebooks organisert etter emneområder, supplert med en Vue.js-basert quiz-applikasjon og omfattende flerspråklig støtte.

## Oppsettskommandoer

### Primært utviklingsmiljø (Python/Jupyter)

Pensumet er designet for å kjøre med Python og Jupyter Notebooks. Den anbefalte tilnærmingen er å bruke miniconda:

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

### Alternativ: Bruke devcontainer

```bash
# Open in VS Code and select "Reopen in Container" when prompted
# The devcontainer will automatically set up the environment
```

### Oppsett av quiz-applikasjon

Quiz-appen er en separat Vue.js-applikasjon som ligger i `etc/quiz-app/`:

```bash
cd etc/quiz-app
npm install
npm run serve  # Development server
npm run build  # Production build
npm run lint   # Lint and fix files
```

## Utviklingsarbeidsflyt

### Arbeide med Jupyter Notebooks

1. **Lokal utvikling:**
   - Aktiver conda-miljø: `conda activate ai4beg`
   - Start Jupyter: `jupyter notebook` eller `jupyter lab`
   - Naviger til leksjonsmapper og åpne `.ipynb`-filer
   - Kjør celler interaktivt for å følge leksjonene

2. **VS Code med Python-utvidelse:**
   - Åpne lageret i VS Code
   - Installer Python-utvidelsen
   - VS Code oppdager og bruker automatisk conda-miljøet
   - Åpne `.ipynb`-filer direkte i VS Code

3. **Skyutvikling:**
   - **GitHub Codespaces:** Klikk "Code" → "Codespaces" → "Create codespace on main"
   - **Binder:** Bruk Binder-merket på README for å starte i nettleseren
   - Merk: Binder har begrensede ressurser og noen begrensninger for nettverkstilgang

### GPU-støtte for avanserte leksjoner

Senere leksjoner drar betydelig nytte av GPU-akselerasjon:

- **Azure Data Science VM:** Bruk NC-serie VM-er med GPU-støtte
- **Azure Machine Learning:** Bruk notatbokfunksjoner med GPU-beregning
- **Google Colab:** Last opp notatbøker individuelt (har gratis GPU-støtte)

### Utvikling av quiz-app

```bash
cd etc/quiz-app
npm run serve  # Hot-reload development server at http://localhost:8080
```

## Testinstruksjoner

Dette er et utdanningslager fokusert på læringsinnhold snarere enn programvaretesting. Det finnes ingen tradisjonell testpakke.

### Valideringsmetoder:

1. **Jupyter Notebooks:** Kjør celler sekvensielt for å bekrefte at kodeeksempler fungerer
2. **Quiz-app testing:** Manuell testing via utviklingsserver
3. **Validering av oversettelser:** Sjekk oversatt innhold i `translations/`-mappen
4. **Linting av quiz-app:** `npm run lint` i `etc/quiz-app/`

### Kjøre kodeeksempler:

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

- Standard Python-konvensjoner for utdanningskode
- Klar, lesbar kode som prioriterer læring fremfor optimalisering
- Kommentarer som forklarer viktige konsepter
- Jupyter Notebook-vennlig: celler bør være selvstendige der det er mulig
- Ingen strenge lintingkrav for leksjonsinnhold

### JavaScript/Vue.js (Quiz-app)

- ESLint-konfigurasjon i `etc/quiz-app/package.json`
- Kjør `npm run lint` for å sjekke og automatisk fikse problemer
- Vue 2.x-konvensjoner
- Komponentbasert arkitektur

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

## Bygging og distribusjon

### Jupyter-innhold

Ingen byggeprosess kreves - Jupyter Notebooks kjøres direkte.

### Quiz-applikasjon

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

### Dokumentasjonsnettsted

Lageret bruker Docsify for dokumentasjon:
- `index.html` fungerer som inngangspunkt
- Ingen bygging kreves - serveres direkte via GitHub Pages
- Tilgang på: https://microsoft.github.io/AI-For-Beginners/

## Retningslinjer for bidrag

### Prosess for pull requests

1. **Tittelformat:** Klare, beskrivende titler som beskriver endringen
2. **CLA-krav:** Microsoft CLA må signeres (automatisk sjekk)
3. **Innholdsretningslinjer:**
   - Oppretthold fokus på utdanning og nybegynnervennlig tilnærming
   - Test alle kodeeksempler i notatbøker
   - Sørg for at notatbøker kjører fra start til slutt
   - Oppdater oversettelser hvis du endrer innhold på engelsk
4. **Endringer i quiz-app:** Kjør `npm run lint` før du sender inn

### Oversettelsesbidrag

- Oversettelser er automatisert via GitHub Actions ved bruk av co-op-translator
- Manuelle oversettelser legges i `translations/<language-code>/`
- Quiz-oversettelser i `etc/quiz-app/src/assets/translations/`
- Støttede språk: 40+ språk (se README for full liste)

### Aktive bidragsområder

Se `etc/CONTRIBUTING.md` for nåværende behov:
- Seksjoner om dyp forsterkende læring
- Forbedringer i objektdeteksjon
- Eksempler på navngitt enhetsgjenkjenning
- Eksempler på tilpasset embedding-trening

## Miljøkonfigurasjon

### Nødvendige avhengigheter

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

Ingen spesielle miljøvariabler kreves for grunnleggende bruk.

For Azure-distribusjoner (quiz-app):
- `AZURE_STATIC_WEB_APPS_API_TOKEN` (settes automatisk av Azure)

## Feilsøking og problemløsning

### Vanlige problemer

**Problem:** Oppretting av conda-miljø mislykkes
- **Løsning:** Oppdater først conda: `conda update conda -y`
- Sørg for tilstrekkelig diskplass (50GB anbefalt)

**Problem:** Jupyter-kjerne ikke funnet
- **Løsning:** 
  ```bash
  conda activate ai4beg
  python -m ipykernel install --user --name ai4beg
  ```

**Problem:** GPU ikke oppdaget i notatbøker
- **Løsning:** 
  - Verifiser CUDA-installasjon: `nvidia-smi`
  - Sjekk PyTorch GPU: `python -c "import torch; print(torch.cuda.is_available())"`
  - Sjekk TensorFlow GPU: `python -c "import tensorflow as tf; print(tf.config.list_physical_devices('GPU'))"`

**Problem:** Quiz-app starter ikke
- **Løsning:**
  ```bash
  cd etc/quiz-app
  rm -rf node_modules package-lock.json
  npm install
  npm run serve
  ```

**Problem:** Binder tidsavbryter eller blokkerer nedlastinger
- **Løsning:** Bruk GitHub Codespaces eller lokal oppsett for bedre ressursbruk

### Minneproblemer

Noen leksjoner krever betydelig RAM (8GB+ anbefalt):
- Bruk sky-VM-er for ressurskrevende leksjoner
- Lukk andre applikasjoner når du trener modeller
- Reduser batch-størrelser i notatbøker hvis du går tom for minne

## Tilleggsnotater

### For kursinstruktører

- Se `lessons/0-course-setup/for-teachers.md` for undervisningsveiledning
- Leksjonene er selvstendige og kan undervises i rekkefølge eller velges individuelt
- Estimert tid: 12 uker med 2 leksjoner per uke

### Skyressurser

- **Azure for Students:** Gratis kreditter tilgjengelig for studenter
- **Microsoft Learn:** Supplerende læringsstier lenket gjennom hele kurset
- **Binder:** Gratis, men begrensede ressurser og noen nettverksrestriksjoner

### Alternativer for kodekjøring

1. **Lokal (anbefalt):** Full kontroll, best ytelse, GPU-støtte
2. **GitHub Codespaces:** Skybasert VS Code, bra for rask tilgang
3. **Binder:** Nettleserbasert Jupyter, gratis men begrenset
4. **Azure ML Notebooks:** Bedriftsalternativ med GPU-støtte
5. **Google Colab:** Last opp notatbøker individuelt, gratis GPU-nivå tilgjengelig

### Arbeide med notatbøker

- Notatbøker er designet for å kjøres celle-for-celle for læring
- Mange notatbøker laster ned datasett ved første kjøring (kan ta tid)
- Noen modeller krever GPU for rimelige treningstider
- Forhåndstrente modeller brukes der det er mulig for å redusere beregningskrav

### Ytelseshensyn

- Senere leksjoner om datamaskinsyn (CNNs, GANs) drar nytte av GPU
- NLP-transformatorleksjoner kan kreve betydelig RAM
- Trening fra bunnen av er lærerikt, men tidkrevende
- Eksempler på overføringslæring minimerer treningstid

---

**Ansvarsfraskrivelse**:  
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi tilstreber nøyaktighet, vær oppmerksom på at automatiserte oversettelser kan inneholde feil eller unøyaktigheter. Det originale dokumentet på sitt opprinnelige språk bør anses som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for eventuelle misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.