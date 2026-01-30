# AGENTS.md

## Projectoverzicht

AI for Beginners is een uitgebreide 12-weekse, 24-lessen curriculum die de basisprincipes van Kunstmatige Intelligentie behandelt. Deze educatieve repository bevat praktische lessen met Jupyter Notebooks, quizzen en hands-on labs. Het curriculum omvat:

- Symbolische AI met kennisrepresentatie en expertsystemen
- Neurale netwerken en deep learning met TensorFlow en PyTorch
- Computer Vision-technieken en -architecturen
- Natural Language Processing (NLP), inclusief transformers en BERT
- Gespecialiseerde onderwerpen: genetische algoritmen, reinforcement learning, multi-agent systemen
- AI-ethiek en principes van verantwoorde AI

**Belangrijke technologieën:** Python 3, Jupyter Notebooks, TensorFlow, PyTorch, Keras, OpenCV, Vue.js (voor quiz-app)

**Architectuur:** Educatieve contentrepository met Jupyter Notebooks georganiseerd per onderwerp, aangevuld met een Vue.js-gebaseerde quizapplicatie en uitgebreide meertalige ondersteuning.

## Setupcommando's

### Primaire ontwikkelomgeving (Python/Jupyter)

Het curriculum is ontworpen om te werken met Python en Jupyter Notebooks. De aanbevolen aanpak is het gebruik van miniconda:

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

### Alternatief: Gebruik van devcontainer

```bash
# Open in VS Code and select "Reopen in Container" when prompted
# The devcontainer will automatically set up the environment
```

### Setup van de quizapplicatie

De quizapp is een aparte Vue.js-applicatie die zich bevindt in `etc/quiz-app/`:

```bash
cd etc/quiz-app
npm install
npm run serve  # Development server
npm run build  # Production build
npm run lint   # Lint and fix files
```

## Ontwikkelworkflow

### Werken met Jupyter Notebooks

1. **Lokale ontwikkeling:**
   - Activeer conda-omgeving: `conda activate ai4beg`
   - Start Jupyter: `jupyter notebook` of `jupyter lab`
   - Navigeer naar lesmappen en open `.ipynb`-bestanden
   - Voer cellen interactief uit om de lessen te volgen

2. **VS Code met Python-extensie:**
   - Open de repository in VS Code
   - Installeer de Python-extensie
   - VS Code detecteert en gebruikt automatisch de conda-omgeving
   - Open `.ipynb`-bestanden direct in VS Code

3. **Cloudontwikkeling:**
   - **GitHub Codespaces:** Klik op "Code" → "Codespaces" → "Create codespace on main"
   - **Binder:** Gebruik de Binder-badge in README om in de browser te starten
   - Opmerking: Binder heeft beperkte resources en enkele beperkingen voor webtoegang

### GPU-ondersteuning voor geavanceerde lessen

Latere lessen profiteren aanzienlijk van GPU-versnelling:

- **Azure Data Science VM:** Gebruik NC-serie VM's met GPU-ondersteuning
- **Azure Machine Learning:** Gebruik notebookfuncties met GPU-compute
- **Google Colab:** Upload notebooks afzonderlijk (gratis GPU-ondersteuning beschikbaar)

### Ontwikkeling van de quizapp

```bash
cd etc/quiz-app
npm run serve  # Hot-reload development server at http://localhost:8080
```

## Testinstructies

Dit is een educatieve repository gericht op leerinhoud in plaats van softwaretesten. Er is geen traditionele test-suite.

### Validatiebenaderingen:

1. **Jupyter Notebooks:** Voer cellen opeenvolgend uit om te verifiëren dat codevoorbeelden werken
2. **Quizapp testen:** Handmatig testen via ontwikkelserver
3. **Validatie van vertalingen:** Controleer vertaalde inhoud in de map `translations/`
4. **Linting van quizapp:** `npm run lint` in `etc/quiz-app/`

### Uitvoeren van codevoorbeelden:

```bash
# Activate environment first
conda activate ai4beg

# Run Python scripts directly
python lessons/4-ComputerVision/07-ConvNets/pytorchcv.py

# Or execute notebooks
jupyter notebook lessons/3-NeuralNetworks/03-Perceptron/Perceptron.ipynb
```

## Code stijl

### Python-code stijl

- Standaard Python-conventies voor educatieve code
- Duidelijke, leesbare code die leren boven optimalisatie stelt
- Commentaar dat belangrijke concepten uitlegt
- Jupyter Notebook-vriendelijk: cellen moeten waar mogelijk zelfstandig zijn
- Geen strikte lintingvereisten voor lesinhoud

### JavaScript/Vue.js (Quizapp)

- ESLint-configuratie in `etc/quiz-app/package.json`
- Voer `npm run lint` uit om problemen te controleren en automatisch op te lossen
- Vue 2.x-conventies
- Componentgebaseerde architectuur

### Bestandsorganisatie

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

## Build en deployment

### Jupyter-inhoud

Geen buildproces vereist - Jupyter Notebooks worden direct uitgevoerd.

### Quizapplicatie

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

### Documentatiesite

De repository gebruikt Docsify voor documentatie:
- `index.html` dient als toegangspunt
- Geen build vereist - direct geserveerd via GitHub Pages
- Toegang via: https://microsoft.github.io/AI-For-Beginners/

## Richtlijnen voor bijdragen

### Pull request-proces

1. **Titel formaat:** Duidelijke, beschrijvende titels die de wijziging beschrijven
2. **CLA-vereiste:** Microsoft CLA moet worden ondertekend (automatische controle)
3. **Inhoud richtlijnen:**
   - Behoud educatieve focus en beginnersvriendelijke aanpak
   - Test alle codevoorbeelden in notebooks
   - Zorg ervoor dat notebooks van begin tot eind werken
   - Werk vertalingen bij als Engelse inhoud wordt gewijzigd
4. **Wijzigingen in quizapp:** Voer `npm run lint` uit voordat je commit

### Bijdragen aan vertalingen

- Vertalingen worden geautomatiseerd via GitHub Actions met co-op-translator
- Handmatige vertalingen gaan in `translations/<language-code>/`
- Quizvertalingen in `etc/quiz-app/src/assets/translations/`
- Ondersteunde talen: 40+ talen (zie README voor volledige lijst)

### Actieve bijdragegebieden

Zie `etc/CONTRIBUTING.md` voor huidige behoeften:
- Secties over deep reinforcement learning
- Verbeteringen in objectdetectie
- Voorbeelden van named entity recognition
- Voorbeelden van training van aangepaste embeddings

## Omgevingsconfiguratie

### Vereiste afhankelijkheden

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

### Omgevingsvariabelen

Geen speciale omgevingsvariabelen vereist voor basisgebruik.

Voor Azure-deployments (quizapp):
- `AZURE_STATIC_WEB_APPS_API_TOKEN` (automatisch ingesteld door Azure)

## Debugging en probleemoplossing

### Veelvoorkomende problemen

**Probleem:** Aanmaken van conda-omgeving mislukt
- **Oplossing:** Update eerst conda: `conda update conda -y`
- Zorg voor voldoende schijfruimte (50GB aanbevolen)

**Probleem:** Jupyter-kernel niet gevonden
- **Oplossing:** 
  ```bash
  conda activate ai4beg
  python -m ipykernel install --user --name ai4beg
  ```

**Probleem:** GPU niet gedetecteerd in notebooks
- **Oplossing:** 
  - Controleer CUDA-installatie: `nvidia-smi`
  - Controleer PyTorch GPU: `python -c "import torch; print(torch.cuda.is_available())"`
  - Controleer TensorFlow GPU: `python -c "import tensorflow as tf; print(tf.config.list_physical_devices('GPU'))"`

**Probleem:** Quizapp start niet
- **Oplossing:**
  ```bash
  cd etc/quiz-app
  rm -rf node_modules package-lock.json
  npm install
  npm run serve
  ```

**Probleem:** Binder loopt vast of blokkeert downloads
- **Oplossing:** Gebruik GitHub Codespaces of lokale setup voor betere toegang tot resources

### Geheugenproblemen

Sommige lessen vereisen veel RAM (8GB+ aanbevolen):
- Gebruik cloud-VM's voor resource-intensieve lessen
- Sluit andere applicaties tijdens het trainen van modellen
- Verminder batchgroottes in notebooks als het geheugen opraakt

## Aanvullende opmerkingen

### Voor cursusinstructeurs

- Zie `lessons/0-course-setup/for-teachers.md` voor lesinstructies
- Lessen zijn zelfstandig en kunnen in volgorde of afzonderlijk worden gegeven
- Geschatte tijd: 12 weken met 2 lessen per week

### Cloudresources

- **Azure for Students:** Gratis tegoeden beschikbaar voor studenten
- **Microsoft Learn:** Aanvullende leerpaden gekoppeld door de hele cursus
- **Binder:** Gratis maar beperkte resources en enkele netwerkbeperkingen

### Opties voor code-uitvoering

1. **Lokaal (Aanbevolen):** Volledige controle, beste prestaties, GPU-ondersteuning
2. **GitHub Codespaces:** Cloudgebaseerde VS Code, goed voor snelle toegang
3. **Binder:** Browsergebaseerde Jupyter, gratis maar beperkt
4. **Azure ML Notebooks:** Enterprise-optie met GPU-ondersteuning
5. **Google Colab:** Upload notebooks afzonderlijk, gratis GPU-laag beschikbaar

### Werken met notebooks

- Notebooks zijn ontworpen om cel-voor-cel te worden uitgevoerd voor leerdoeleinden
- Veel notebooks downloaden datasets bij de eerste uitvoering (kan tijd kosten)
- Sommige modellen vereisen GPU voor redelijke trainingstijden
- Voorgetrainde modellen worden waar mogelijk gebruikt om rekenvereisten te verminderen

### Prestatieoverwegingen

- Latere lessen over computer vision (CNN's, GAN's) profiteren van GPU
- NLP-transformerlessen kunnen veel RAM vereisen
- Training vanaf nul is educatief maar tijdrovend
- Voorbeelden van transfer learning minimaliseren trainingstijd

---

**Disclaimer**:  
Dit document is vertaald met behulp van de AI-vertalingsservice [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we streven naar nauwkeurigheid, dient u zich ervan bewust te zijn dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het originele document in de oorspronkelijke taal moet worden beschouwd als de gezaghebbende bron. Voor kritieke informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor eventuele misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.