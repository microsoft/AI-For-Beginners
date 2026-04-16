# AGENTS.md

## Přehled projektu

AI for Beginners je komplexní 12týdenní, 24lekční kurikulum pokrývající základy umělé inteligence. Tento vzdělávací repozitář obsahuje praktické lekce využívající Jupyter Notebooks, kvízy a praktické laboratoře. Kurikulum zahrnuje:

- Symbolickou AI s reprezentací znalostí a expertními systémy
- Neuronové sítě a hluboké učení s TensorFlow a PyTorch
- Techniky a architektury počítačového vidění
- Zpracování přirozeného jazyka (NLP) včetně transformerů a BERT
- Specializovaná témata: genetické algoritmy, posilované učení, systémy s více agenty
- Etiku AI a principy odpovědné AI

**Klíčové technologie:** Python 3, Jupyter Notebooks, TensorFlow, PyTorch, Keras, OpenCV, Vue.js (pro aplikaci kvízů)

**Architektura:** Vzdělávací obsahový repozitář s Jupyter Notebooks organizovanými podle tematických oblastí, doplněný aplikací kvízů založenou na Vue.js a rozsáhlou podporou více jazyků.

## Příkazy pro nastavení

### Primární vývojové prostředí (Python/Jupyter)

Kurikulum je navrženo pro běh s Pythonem a Jupyter Notebooks. Doporučený přístup je použití miniconda:

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

### Alternativa: Použití devcontaineru

```bash
# Open in VS Code and select "Reopen in Container" when prompted
# The devcontainer will automatically set up the environment
```

### Nastavení aplikace kvízů

Aplikace kvízů je samostatná aplikace Vue.js umístěná v `etc/quiz-app/`:

```bash
cd etc/quiz-app
npm install
npm run serve  # Development server
npm run build  # Production build
npm run lint   # Lint and fix files
```

## Vývojový postup

### Práce s Jupyter Notebooks

1. **Lokální vývoj:**
   - Aktivujte conda prostředí: `conda activate ai4beg`
   - Spusťte Jupyter: `jupyter notebook` nebo `jupyter lab`
   - Přejděte do složek s lekcemi a otevřete soubory `.ipynb`
   - Interaktivně spouštějte buňky pro sledování lekcí

2. **VS Code s rozšířením Python:**
   - Otevřete repozitář ve VS Code
   - Nainstalujte rozšíření Python
   - VS Code automaticky detekuje a používá conda prostředí
   - Otevřete soubory `.ipynb` přímo ve VS Code

3. **Cloudový vývoj:**
   - **GitHub Codespaces:** Klikněte na "Code" → "Codespaces" → "Create codespace on main"
   - **Binder:** Použijte odznak Binder v README pro spuštění v prohlížeči
   - Poznámka: Binder má omezené zdroje a některá omezení přístupu na web

### Podpora GPU pro pokročilé lekce

Pozdější lekce výrazně těží z akcelerace GPU:

- **Azure Data Science VM:** Použijte NC-series VM s podporou GPU
- **Azure Machine Learning:** Použijte funkce notebooků s GPU výpočetními prostředky
- **Google Colab:** Nahrajte jednotlivé notebooky (má bezplatnou podporu GPU)

### Vývoj aplikace kvízů

```bash
cd etc/quiz-app
npm run serve  # Hot-reload development server at http://localhost:8080
```

## Pokyny k testování

Toto je vzdělávací repozitář zaměřený na výukový obsah, nikoli na testování softwaru. Neexistuje žádná tradiční testovací sada.

### Přístupy k validaci:

1. **Jupyter Notebooks:** Postupně spouštějte buňky pro ověření funkčnosti příkladů kódu
2. **Testování aplikace kvízů:** Manuální testování přes vývojový server
3. **Validace překladů:** Zkontrolujte přeložený obsah ve složce `translations/`
4. **Lintování aplikace kvízů:** `npm run lint` v `etc/quiz-app/`

### Spouštění příkladů kódu:

```bash
# Activate environment first
conda activate ai4beg

# Run Python scripts directly
python lessons/4-ComputerVision/07-ConvNets/pytorchcv.py

# Or execute notebooks
jupyter notebook lessons/3-NeuralNetworks/03-Perceptron/Perceptron.ipynb
```

## Styl kódu

### Styl kódu Python

- Standardní konvence Pythonu pro vzdělávací kód
- Jasný, čitelný kód upřednostňující učení před optimalizací
- Komentáře vysvětlující klíčové koncepty
- Přátelské pro Jupyter Notebook: buňky by měly být co nejvíce samostatné
- Žádné přísné požadavky na lintování pro obsah lekcí

### JavaScript/Vue.js (aplikace kvízů)

- Konfigurace ESLint v `etc/quiz-app/package.json`
- Spusťte `npm run lint` pro kontrolu a automatické opravy problémů
- Konvence Vue 2.x
- Architektura založená na komponentách

### Organizace souborů

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

## Sestavení a nasazení

### Obsah Jupyter

Není vyžadován žádný proces sestavení - Jupyter Notebooks se spouštějí přímo.

### Aplikace kvízů

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

### Dokumentační web

Repozitář používá Docsify pro dokumentaci:
- `index.html` slouží jako vstupní bod
- Není vyžadováno sestavení - slouží přímo přes GitHub Pages
- Přístup na: https://microsoft.github.io/AI-For-Beginners/

## Pokyny pro přispívání

### Proces pull requestů

1. **Formát názvu:** Jasné, popisné názvy popisující změnu
2. **Požadavek CLA:** Musí být podepsán Microsoft CLA (automatická kontrola)
3. **Pokyny k obsahu:**
   - Zachovejte vzdělávací zaměření a přístup pro začátečníky
   - Otestujte všechny příklady kódu v noteboocích
   - Ujistěte se, že notebooky běží od začátku do konce
   - Aktualizujte překlady, pokud upravujete anglický obsah
4. **Změny aplikace kvízů:** Spusťte `npm run lint` před odesláním

### Přispívání překladů

- Překlady jsou automatizovány pomocí GitHub Actions s co-op-translator
- Manuální překlady jdou do `translations/<language-code>/`
- Překlady kvízů do `etc/quiz-app/src/assets/translations/`
- Podporované jazyky: 40+ jazyků (viz README pro úplný seznam)

### Aktivní oblasti přispívání

Viz `etc/CONTRIBUTING.md` pro aktuální potřeby:
- Sekce hlubokého posilovaného učení
- Vylepšení detekce objektů
- Příklady rozpoznávání pojmenovaných entit
- Ukázky trénování vlastních embeddingů

## Konfigurace prostředí

### Požadované závislosti

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

### Proměnné prostředí

Pro základní použití nejsou vyžadovány žádné speciální proměnné prostředí.

Pro nasazení na Azure (aplikace kvízů):
- `AZURE_STATIC_WEB_APPS_API_TOKEN` (nastaveno automaticky Azure)

## Ladění a řešení problémů

### Běžné problémy

**Problém:** Selhání vytvoření conda prostředí
- **Řešení:** Nejprve aktualizujte conda: `conda update conda -y`
- Zajistěte dostatek místa na disku (doporučeno 50 GB)

**Problém:** Jupyter kernel nebyl nalezen
- **Řešení:** 
  ```bash
  conda activate ai4beg
  python -m ipykernel install --user --name ai4beg
  ```

**Problém:** GPU není detekováno v noteboocích
- **Řešení:** 
  - Ověřte instalaci CUDA: `nvidia-smi`
  - Zkontrolujte GPU v PyTorch: `python -c "import torch; print(torch.cuda.is_available())"`
  - Zkontrolujte GPU v TensorFlow: `python -c "import tensorflow as tf; print(tf.config.list_physical_devices('GPU'))"`

**Problém:** Aplikace kvízů se nespustí
- **Řešení:**
  ```bash
  cd etc/quiz-app
  rm -rf node_modules package-lock.json
  npm install
  npm run serve
  ```

**Problém:** Binder vyprší nebo blokuje stahování
- **Řešení:** Použijte GitHub Codespaces nebo lokální nastavení pro lepší přístup ke zdrojům

### Problémy s pamětí

Některé lekce vyžadují značné množství RAM (doporučeno 8 GB+):
- Použijte cloudové VM pro lekce náročné na zdroje
- Zavřete ostatní aplikace při trénování modelů
- Snižte velikost batchů v noteboocích, pokud dochází paměť

## Další poznámky

### Pro instruktory kurzu

- Viz `lessons/0-course-setup/for-teachers.md` pro pokyny k výuce
- Lekce jsou samostatné a mohou být vyučovány v pořadí nebo vybírány jednotlivě
- Odhadovaný čas: 12 týdnů při 2 lekcích týdně

### Cloudové zdroje

- **Azure pro studenty:** Bezplatné kredity dostupné pro studenty
- **Microsoft Learn:** Doplňkové vzdělávací cesty propojené v průběhu
- **Binder:** Bezplatné, ale omezené zdroje a některá síťová omezení

### Možnosti spouštění kódu

1. **Lokálně (doporučeno):** Plná kontrola, nejlepší výkon, podpora GPU
2. **GitHub Codespaces:** Cloudové VS Code, dobré pro rychlý přístup
3. **Binder:** Jupyter v prohlížeči, bezplatný, ale omezený
4. **Azure ML Notebooks:** Podnikové řešení s podporou GPU
5. **Google Colab:** Nahrajte jednotlivé notebooky, dostupná bezplatná GPU vrstva

### Práce s notebooky

- Notebooky jsou navrženy tak, aby byly spouštěny buňku po buňce pro učení
- Mnoho notebooků stahuje datové sady při prvním spuštění (může trvat déle)
- Některé modely vyžadují GPU pro rozumné časy trénování
- Předtrénované modely jsou používány, kde je to možné, pro snížení výpočetních požadavků

### Výkonnostní úvahy

- Pozdější lekce počítačového vidění (CNN, GAN) těží z GPU
- Lekce NLP s transformery mohou vyžadovat značné množství RAM
- Trénování od začátku je vzdělávací, ale časově náročné
- Příklady transferového učení minimalizují čas trénování

---

**Upozornění**:  
Tento dokument byl přeložen pomocí služby pro automatický překlad [Co-op Translator](https://github.com/Azure/co-op-translator). I když se snažíme o co největší přesnost, mějte prosím na paměti, že automatické překlady mohou obsahovat chyby nebo nepřesnosti. Za autoritativní zdroj by měl být považován původní dokument v jeho původním jazyce. Pro důležité informace doporučujeme profesionální lidský překlad. Neodpovídáme za žádná nedorozumění nebo nesprávné výklady vyplývající z použití tohoto překladu.