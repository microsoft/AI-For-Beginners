# AGENTS.md

## Prezentare generală a proiectului

AI for Beginners este un curriculum cuprinzător de 12 săptămâni și 24 de lecții, care acoperă fundamentele Inteligenței Artificiale. Acest depozit educațional include lecții practice folosind Jupyter Notebooks, teste și laboratoare interactive. Curriculumul acoperă:

- AI simbolic cu reprezentarea cunoștințelor și sisteme expert
- Rețele neuronale și învățare profundă cu TensorFlow și PyTorch
- Tehnici și arhitecturi de viziune computerizată
- Procesarea limbajului natural (NLP), inclusiv transformatori și BERT
- Subiecte specializate: Algoritmi genetici, Învățare prin întărire, Sisteme multi-agent
- Etica AI și principii de AI responsabil

**Tehnologii cheie:** Python 3, Jupyter Notebooks, TensorFlow, PyTorch, Keras, OpenCV, Vue.js (pentru aplicația de teste)

**Arhitectură:** Depozit de conținut educațional cu Jupyter Notebooks organizate pe domenii tematice, completat de o aplicație de teste bazată pe Vue.js și suport extins pentru mai multe limbi.

## Comenzi de configurare

### Mediu principal de dezvoltare (Python/Jupyter)

Curriculumul este conceput să ruleze cu Python și Jupyter Notebooks. Abordarea recomandată este utilizarea miniconda:

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

### Alternativă: Utilizarea devcontainer

```bash
# Open in VS Code and select "Reopen in Container" when prompted
# The devcontainer will automatically set up the environment
```

### Configurarea aplicației de teste

Aplicația de teste este o aplicație separată Vue.js situată în `etc/quiz-app/`:

```bash
cd etc/quiz-app
npm install
npm run serve  # Development server
npm run build  # Production build
npm run lint   # Lint and fix files
```

## Flux de lucru pentru dezvoltare

### Lucrul cu Jupyter Notebooks

1. **Dezvoltare locală:**
   - Activează mediul conda: `conda activate ai4beg`
   - Pornește Jupyter: `jupyter notebook` sau `jupyter lab`
   - Navighează la folderele lecțiilor și deschide fișierele `.ipynb`
   - Rulează celulele interactiv pentru a urma lecțiile

2. **VS Code cu extensia Python:**
   - Deschide depozitul în VS Code
   - Instalează extensia Python
   - VS Code detectează automat și utilizează mediul conda
   - Deschide fișierele `.ipynb` direct în VS Code

3. **Dezvoltare în cloud:**
   - **GitHub Codespaces:** Click pe "Code" → "Codespaces" → "Create codespace on main"
   - **Binder:** Folosește insigna Binder din README pentru a lansa în browser
   - Notă: Binder are resurse limitate și unele restricții de acces web

### Suport GPU pentru lecții avansate

Lecțiile ulterioare beneficiază semnificativ de accelerarea GPU:

- **Azure Data Science VM:** Utilizează VM-uri din seria NC cu suport GPU
- **Azure Machine Learning:** Utilizează funcțiile notebook cu calcul GPU
- **Google Colab:** Încarcă notebook-urile individual (are suport GPU gratuit)

### Dezvoltarea aplicației de teste

```bash
cd etc/quiz-app
npm run serve  # Hot-reload development server at http://localhost:8080
```

## Instrucțiuni de testare

Acesta este un depozit educațional axat pe conținut de învățare, nu pe testarea software. Nu există un set tradițional de teste.

### Metode de validare:

1. **Jupyter Notebooks:** Rulează celulele secvențial pentru a verifica dacă exemplele de cod funcționează
2. **Testarea aplicației de teste:** Testare manuală prin serverul de dezvoltare
3. **Validarea traducerilor:** Verifică conținutul tradus în folderul `translations/`
4. **Linting pentru aplicația de teste:** `npm run lint` în `etc/quiz-app/`

### Executarea exemplelor de cod:

```bash
# Activate environment first
conda activate ai4beg

# Run Python scripts directly
python lessons/4-ComputerVision/07-ConvNets/pytorchcv.py

# Or execute notebooks
jupyter notebook lessons/3-NeuralNetworks/03-Perceptron/Perceptron.ipynb
```

## Stilul codului

### Stilul codului Python

- Convenții standard Python pentru cod educațional
- Cod clar și ușor de citit, prioritizând învățarea în detrimentul optimizării
- Comentarii care explică conceptele cheie
- Prietenos cu Jupyter Notebook: celulele ar trebui să fie cât mai autonome
- Fără cerințe stricte de linting pentru conținutul lecțiilor

### JavaScript/Vue.js (Aplicația de teste)

- Configurație ESLint în `etc/quiz-app/package.json`
- Rulează `npm run lint` pentru a verifica și a corecta automat problemele
- Convenții Vue 2.x
- Arhitectură bazată pe componente

### Organizarea fișierelor

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

## Construire și implementare

### Conținut Jupyter

Nu este necesar un proces de construire - Jupyter Notebooks sunt executate direct.

### Aplicația de teste

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

### Site-ul de documentație

Depozitul folosește Docsify pentru documentație:
- `index.html` servește ca punct de intrare
- Nu este necesară construirea - servit direct prin GitHub Pages
- Acces la: https://microsoft.github.io/AI-For-Beginners/

## Ghid pentru contribuții

### Procesul de Pull Request

1. **Formatul titlului:** Titluri clare și descriptive care descriu schimbarea
2. **Cerința CLA:** CLA Microsoft trebuie semnat (verificare automată)
3. **Ghiduri de conținut:**
   - Menține accentul educațional și abordarea prietenoasă pentru începători
   - Testează toate exemplele de cod din notebook-uri
   - Asigură-te că notebook-urile rulează cap-coadă
   - Actualizează traducerile dacă modifici conținutul în limba engleză
4. **Modificări ale aplicației de teste:** Rulează `npm run lint` înainte de a face commit

### Contribuții la traduceri

- Traducerile sunt automatizate prin GitHub Actions folosind co-op-translator
- Traducerile manuale se află în `translations/<language-code>/`
- Traducerile pentru teste în `etc/quiz-app/src/assets/translations/`
- Limbi suportate: peste 40 de limbi (vezi README pentru lista completă)

### Domenii active de contribuție

Vezi `etc/CONTRIBUTING.md` pentru nevoile actuale:
- Secțiuni de învățare profundă prin întărire
- Îmbunătățiri ale detectării obiectelor
- Exemple de recunoaștere a entităților numite
- Mostre de antrenament pentru încorporări personalizate

## Configurarea mediului

### Dependențe necesare

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

### Variabile de mediu

Nu sunt necesare variabile de mediu speciale pentru utilizarea de bază.

Pentru implementările Azure (aplicația de teste):
- `AZURE_STATIC_WEB_APPS_API_TOKEN` (setat automat de Azure)

## Depanare și rezolvarea problemelor

### Probleme comune

**Problemă:** Crearea mediului conda eșuează
- **Soluție:** Actualizează conda mai întâi: `conda update conda -y`
- Asigură-te că ai suficient spațiu pe disc (recomandat 50GB)

**Problemă:** Kernel-ul Jupyter nu este găsit
- **Soluție:** 
  ```bash
  conda activate ai4beg
  python -m ipykernel install --user --name ai4beg
  ```

**Problemă:** GPU-ul nu este detectat în notebook-uri
- **Soluție:** 
  - Verifică instalarea CUDA: `nvidia-smi`
  - Verifică GPU-ul PyTorch: `python -c "import torch; print(torch.cuda.is_available())"`
  - Verifică GPU-ul TensorFlow: `python -c "import tensorflow as tf; print(tf.config.list_physical_devices('GPU'))"`

**Problemă:** Aplicația de teste nu pornește
- **Soluție:**
  ```bash
  cd etc/quiz-app
  rm -rf node_modules package-lock.json
  npm install
  npm run serve
  ```

**Problemă:** Binder expiră sau blochează descărcările
- **Soluție:** Utilizează GitHub Codespaces sau configurarea locală pentru acces mai bun la resurse

### Probleme de memorie

Unele lecții necesită RAM semnificativ (recomandat 8GB+):
- Utilizează VM-uri cloud pentru lecțiile care necesită multe resurse
- Închide alte aplicații când antrenezi modele
- Redu dimensiunile batch-urilor în notebook-uri dacă rămâi fără memorie

## Note suplimentare

### Pentru instructorii cursului

- Vezi `lessons/0-course-setup/for-teachers.md` pentru ghid de predare
- Lecțiile sunt autonome și pot fi predate în ordine sau selectate individual
- Timp estimat: 12 săptămâni cu 2 lecții pe săptămână

### Resurse cloud

- **Azure for Students:** Credite gratuite disponibile pentru studenți
- **Microsoft Learn:** Cursuri suplimentare legate pe parcurs
- **Binder:** Gratuit, dar cu resurse limitate și unele restricții de rețea

### Opțiuni de execuție a codului

1. **Local (Recomandat):** Control complet, performanță optimă, suport GPU
2. **GitHub Codespaces:** VS Code bazat pe cloud, bun pentru acces rapid
3. **Binder:** Jupyter bazat pe browser, gratuit dar limitat
4. **Azure ML Notebooks:** Opțiune enterprise cu suport GPU
5. **Google Colab:** Încarcă notebook-urile individual, disponibil nivel GPU gratuit

### Lucrul cu notebook-uri

- Notebook-urile sunt concepute să fie rulate celulă cu celulă pentru învățare
- Multe notebook-uri descarcă seturi de date la prima rulare (poate dura)
- Unele modele necesită GPU pentru timpi rezonabili de antrenament
- Modelele pre-antrenate sunt utilizate acolo unde este posibil pentru a reduce cerințele de calcul

### Considerații de performanță

- Lecțiile ulterioare de viziune computerizată (CNN-uri, GAN-uri) beneficiază de GPU
- Lecțiile NLP cu transformatori pot necesita RAM semnificativ
- Antrenamentul de la zero este educativ, dar consumă mult timp
- Exemplele de învățare transferabilă minimizează timpul de antrenament

---

**Declinare de responsabilitate**:  
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). Deși ne străduim să asigurăm acuratețea, vă rugăm să fiți conștienți că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa natală ar trebui considerat sursa autoritară. Pentru informații critice, se recomandă traducerea profesională realizată de oameni. Nu ne asumăm responsabilitatea pentru neînțelegerile sau interpretările greșite care pot apărea din utilizarea acestei traduceri.