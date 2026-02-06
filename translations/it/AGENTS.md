# AGENTS.md

## Panoramica del Progetto

AI for Beginners è un curriculum completo di 12 settimane e 24 lezioni che copre i fondamenti dell'Intelligenza Artificiale. Questo repository educativo include lezioni pratiche con Jupyter Notebooks, quiz e laboratori pratici. Il curriculum tratta:

- AI simbolica con rappresentazione della conoscenza e sistemi esperti
- Reti neurali e Deep Learning con TensorFlow e PyTorch
- Tecniche e architetture di Computer Vision
- Elaborazione del linguaggio naturale (NLP) inclusi transformers e BERT
- Argomenti specializzati: algoritmi genetici, apprendimento per rinforzo, sistemi multi-agente
- Etica dell'AI e principi di AI responsabile

**Tecnologie chiave:** Python 3, Jupyter Notebooks, TensorFlow, PyTorch, Keras, OpenCV, Vue.js (per l'app dei quiz)

**Architettura:** Repository di contenuti educativi con Jupyter Notebooks organizzati per aree tematiche, integrati da un'app per quiz basata su Vue.js e supporto multilingue esteso.

## Comandi di Configurazione

### Ambiente di Sviluppo Primario (Python/Jupyter)

Il curriculum è progettato per funzionare con Python e Jupyter Notebooks. L'approccio consigliato è utilizzare miniconda:

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

### Alternativa: Utilizzo di devcontainer

```bash
# Open in VS Code and select "Reopen in Container" when prompted
# The devcontainer will automatically set up the environment
```

### Configurazione dell'App per Quiz

L'app per quiz è un'applicazione Vue.js separata situata in `etc/quiz-app/`:

```bash
cd etc/quiz-app
npm install
npm run serve  # Development server
npm run build  # Production build
npm run lint   # Lint and fix files
```

## Flusso di Sviluppo

### Lavorare con Jupyter Notebooks

1. **Sviluppo Locale:**
   - Attivare l'ambiente conda: `conda activate ai4beg`
   - Avviare Jupyter: `jupyter notebook` o `jupyter lab`
   - Navigare nelle cartelle delle lezioni e aprire i file `.ipynb`
   - Eseguire le celle interattivamente per seguire le lezioni

2. **VS Code con Estensione Python:**
   - Aprire il repository in VS Code
   - Installare l'estensione Python
   - VS Code rileva automaticamente e utilizza l'ambiente conda
   - Aprire direttamente i file `.ipynb` in VS Code

3. **Sviluppo Cloud:**
   - **GitHub Codespaces:** Cliccare su "Code" → "Codespaces" → "Create codespace on main"
   - **Binder:** Utilizzare il badge Binder nel README per avviare nel browser
   - Nota: Binder ha risorse limitate e alcune restrizioni di accesso web

### Supporto GPU per Lezioni Avanzate

Le lezioni successive beneficiano significativamente dell'accelerazione GPU:

- **Azure Data Science VM:** Utilizzare VM della serie NC con supporto GPU
- **Azure Machine Learning:** Utilizzare le funzionalità notebook con calcolo GPU
- **Google Colab:** Caricare i notebook singolarmente (supporto GPU gratuito disponibile)

### Sviluppo dell'App per Quiz

```bash
cd etc/quiz-app
npm run serve  # Hot-reload development server at http://localhost:8080
```

## Istruzioni per il Testing

Questo è un repository educativo focalizzato sui contenuti di apprendimento piuttosto che sul testing software. Non esiste una suite di test tradizionale.

### Approcci di Validazione:

1. **Jupyter Notebooks:** Eseguire le celle in sequenza per verificare che gli esempi di codice funzionino
2. **Testing dell'App per Quiz:** Test manuale tramite server di sviluppo
3. **Validazione delle Traduzioni:** Controllare i contenuti tradotti nella cartella `translations/`
4. **Linting dell'App per Quiz:** `npm run lint` in `etc/quiz-app/`

### Esecuzione degli Esempi di Codice:

```bash
# Activate environment first
conda activate ai4beg

# Run Python scripts directly
python lessons/4-ComputerVision/07-ConvNets/pytorchcv.py

# Or execute notebooks
jupyter notebook lessons/3-NeuralNetworks/03-Perceptron/Perceptron.ipynb
```

## Stile del Codice

### Stile del Codice Python

- Convenzioni standard Python per codice educativo
- Codice chiaro e leggibile che privilegia l'apprendimento rispetto all'ottimizzazione
- Commenti che spiegano i concetti chiave
- Compatibile con Jupyter Notebook: le celle dovrebbero essere il più possibile autonome
- Nessun requisito di linting rigoroso per i contenuti delle lezioni

### JavaScript/Vue.js (App per Quiz)

- Configurazione ESLint in `etc/quiz-app/package.json`
- Eseguire `npm run lint` per controllare e correggere automaticamente i problemi
- Convenzioni Vue 2.x
- Architettura basata su componenti

### Organizzazione dei File

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

## Build e Deployment

### Contenuti Jupyter

Non è richiesto alcun processo di build - i Jupyter Notebooks vengono eseguiti direttamente.

### Applicazione per Quiz

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

### Sito di Documentazione

Il repository utilizza Docsify per la documentazione:
- `index.html` funge da punto di ingresso
- Non è richiesto alcun build - servito direttamente tramite GitHub Pages
- Accesso: https://microsoft.github.io/AI-For-Beginners/

## Linee Guida per i Contributi

### Processo di Pull Request

1. **Formato del Titolo:** Titoli chiari e descrittivi che descrivono la modifica
2. **Requisito CLA:** Deve essere firmato il Microsoft CLA (controllo automatico)
3. **Linee Guida sui Contenuti:**
   - Mantenere il focus educativo e l'approccio adatto ai principianti
   - Testare tutti gli esempi di codice nei notebook
   - Assicurarsi che i notebook funzionino dall'inizio alla fine
   - Aggiornare le traduzioni se si modifica il contenuto in inglese
4. **Modifiche all'App per Quiz:** Eseguire `npm run lint` prima di effettuare il commit

### Contributi alle Traduzioni

- Le traduzioni sono automatizzate tramite GitHub Actions utilizzando co-op-translator
- Le traduzioni manuali vanno in `translations/<language-code>/`
- Traduzioni dei quiz in `etc/quiz-app/src/assets/translations/`
- Lingue supportate: oltre 40 lingue (vedere README per l'elenco completo)

### Aree di Contributo Attive

Vedere `etc/CONTRIBUTING.md` per le necessità attuali:
- Sezioni di Deep Reinforcement Learning
- Miglioramenti al rilevamento degli oggetti
- Esempi di riconoscimento di entità nominate
- Campioni di addestramento di embedding personalizzati

## Configurazione dell'Ambiente

### Dipendenze Necessarie

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

### Variabili d'Ambiente

Non sono richieste variabili d'ambiente speciali per l'uso di base.

Per i deployment su Azure (app per quiz):
- `AZURE_STATIC_WEB_APPS_API_TOKEN` (impostato automaticamente da Azure)

## Debugging e Risoluzione dei Problemi

### Problemi Comuni

**Problema:** Creazione dell'ambiente conda fallita
- **Soluzione:** Aggiornare conda prima: `conda update conda -y`
- Assicurarsi di avere spazio su disco sufficiente (50GB consigliati)

**Problema:** Kernel Jupyter non trovato
- **Soluzione:** 
  ```bash
  conda activate ai4beg
  python -m ipykernel install --user --name ai4beg
  ```

**Problema:** GPU non rilevata nei notebook
- **Soluzione:** 
  - Verificare l'installazione di CUDA: `nvidia-smi`
  - Controllare GPU con PyTorch: `python -c "import torch; print(torch.cuda.is_available())"`
  - Controllare GPU con TensorFlow: `python -c "import tensorflow as tf; print(tf.config.list_physical_devices('GPU'))"`

**Problema:** L'app per quiz non si avvia
- **Soluzione:**
  ```bash
  cd etc/quiz-app
  rm -rf node_modules package-lock.json
  npm install
  npm run serve
  ```

**Problema:** Binder si blocca o non scarica
- **Soluzione:** Utilizzare GitHub Codespaces o configurazione locale per un migliore accesso alle risorse

### Problemi di Memoria

Alcune lezioni richiedono una quantità significativa di RAM (consigliati 8GB+):
- Utilizzare VM cloud per lezioni che richiedono molte risorse
- Chiudere altre applicazioni durante l'addestramento dei modelli
- Ridurre le dimensioni dei batch nei notebook se la memoria è insufficiente

## Note Aggiuntive

### Per gli Istruttori del Corso

- Vedere `lessons/0-course-setup/for-teachers.md` per le indicazioni didattiche
- Le lezioni sono autonome e possono essere insegnate in sequenza o selezionate singolarmente
- Tempo stimato: 12 settimane con 2 lezioni a settimana

### Risorse Cloud

- **Azure for Students:** Crediti gratuiti disponibili per gli studenti
- **Microsoft Learn:** Percorsi di apprendimento supplementari collegati
- **Binder:** Gratuito ma con risorse limitate e alcune restrizioni di rete

### Opzioni di Esecuzione del Codice

1. **Locale (Consigliato):** Controllo completo, migliori prestazioni, supporto GPU
2. **GitHub Codespaces:** VS Code basato su cloud, buono per accesso rapido
3. **Binder:** Jupyter basato su browser, gratuito ma limitato
4. **Azure ML Notebooks:** Opzione aziendale con supporto GPU
5. **Google Colab:** Caricare i notebook singolarmente, livello GPU gratuito disponibile

### Lavorare con i Notebook

- I notebook sono progettati per essere eseguiti cella per cella per l'apprendimento
- Molti notebook scaricano dataset al primo avvio (potrebbe richiedere tempo)
- Alcuni modelli richiedono GPU per tempi di addestramento ragionevoli
- Dove possibile, vengono utilizzati modelli pre-addestrati per ridurre i requisiti di calcolo

### Considerazioni sulle Prestazioni

- Le lezioni successive di visione artificiale (CNN, GAN) beneficiano della GPU
- Le lezioni sui transformers NLP possono richiedere molta RAM
- L'addestramento da zero è educativo ma richiede tempo
- Gli esempi di apprendimento trasferito riducono i tempi di addestramento

---

**Clausola di esclusione della responsabilità**:  
Questo documento è stato tradotto utilizzando il servizio di traduzione automatica [Co-op Translator](https://github.com/Azure/co-op-translator). Sebbene ci impegniamo per garantire l'accuratezza, si prega di notare che le traduzioni automatiche possono contenere errori o imprecisioni. Il documento originale nella sua lingua nativa dovrebbe essere considerato la fonte autorevole. Per informazioni critiche, si raccomanda una traduzione professionale effettuata da un traduttore umano. Non siamo responsabili per eventuali incomprensioni o interpretazioni errate derivanti dall'uso di questa traduzione.