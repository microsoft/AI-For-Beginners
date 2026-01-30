# AGENTS.md

## Prehľad projektu

AI for Beginners je komplexný 12-týždňový, 24-lekciový kurz pokrývajúci základy umelej inteligencie. Tento vzdelávací repozitár obsahuje praktické lekcie využívajúce Jupyter Notebooks, kvízy a praktické laboratóriá. Kurz zahŕňa:

- Symbolickú AI s reprezentáciou znalostí a expertnými systémami
- Neurónové siete a hlboké učenie s TensorFlow a PyTorch
- Techniky a architektúry počítačového videnia
- Spracovanie prirodzeného jazyka (NLP) vrátane transformerov a BERT
- Špecializované témy: genetické algoritmy, posilňovacie učenie, systémy s viacerými agentmi
- Etika AI a princípy zodpovednej AI

**Kľúčové technológie:** Python 3, Jupyter Notebooks, TensorFlow, PyTorch, Keras, OpenCV, Vue.js (pre aplikáciu kvízov)

**Architektúra:** Vzdelávací obsah organizovaný v repozitári s Jupyter Notebooks podľa tematických oblastí, doplnený o aplikáciu kvízov založenú na Vue.js a rozsiahlu podporu viacerých jazykov.

## Príkazy na nastavenie

### Primárne vývojové prostredie (Python/Jupyter)

Kurz je navrhnutý na spustenie s Pythonom a Jupyter Notebooks. Odporúčaný prístup je použitie miniconda:

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

### Alternatíva: Použitie devcontainer

```bash
# Open in VS Code and select "Reopen in Container" when prompted
# The devcontainer will automatically set up the environment
```

### Nastavenie aplikácie kvízov

Aplikácia kvízov je samostatná Vue.js aplikácia umiestnená v `etc/quiz-app/`:

```bash
cd etc/quiz-app
npm install
npm run serve  # Development server
npm run build  # Production build
npm run lint   # Lint and fix files
```

## Vývojový pracovný postup

### Práca s Jupyter Notebooks

1. **Lokálny vývoj:**
   - Aktivujte conda prostredie: `conda activate ai4beg`
   - Spustite Jupyter: `jupyter notebook` alebo `jupyter lab`
   - Prejdite do priečinkov s lekciami a otvorte súbory `.ipynb`
   - Spúšťajte bunky interaktívne podľa lekcií

2. **VS Code s rozšírením Python:**
   - Otvorte repozitár vo VS Code
   - Nainštalujte rozšírenie Python
   - VS Code automaticky detekuje a používa conda prostredie
   - Otvorte súbory `.ipynb` priamo vo VS Code

3. **Cloudový vývoj:**
   - **GitHub Codespaces:** Kliknite na "Code" → "Codespaces" → "Create codespace on main"
   - **Binder:** Použite odznak Binder v README na spustenie v prehliadači
   - Poznámka: Binder má obmedzené zdroje a niektoré obmedzenia prístupu na web

### Podpora GPU pre pokročilé lekcie

Neskoršie lekcie výrazne profitujú z akcelerácie GPU:

- **Azure Data Science VM:** Použite NC-series VM s podporou GPU
- **Azure Machine Learning:** Použite funkcie notebookov s GPU výpočtami
- **Google Colab:** Nahrajte notebooky jednotlivo (má bezplatnú podporu GPU)

### Vývoj aplikácie kvízov

```bash
cd etc/quiz-app
npm run serve  # Hot-reload development server at http://localhost:8080
```

## Pokyny na testovanie

Toto je vzdelávací repozitár zameraný na obsah učenia, nie na testovanie softvéru. Neexistuje tradičný testovací balík.

### Prístupy k validácii:

1. **Jupyter Notebooks:** Spúšťajte bunky postupne na overenie funkčnosti príkladov kódu
2. **Testovanie aplikácie kvízov:** Manuálne testovanie cez vývojový server
3. **Validácia prekladov:** Skontrolujte preložený obsah v priečinku `translations/`
4. **Linting aplikácie kvízov:** `npm run lint` v `etc/quiz-app/`

### Spúšťanie príkladov kódu:

```bash
# Activate environment first
conda activate ai4beg

# Run Python scripts directly
python lessons/4-ComputerVision/07-ConvNets/pytorchcv.py

# Or execute notebooks
jupyter notebook lessons/3-NeuralNetworks/03-Perceptron/Perceptron.ipynb
```

## Štýl kódu

### Štýl Python kódu

- Štandardné Python konvencie pre vzdelávací kód
- Jasný, čitateľný kód s prioritou učenia pred optimalizáciou
- Komentáre vysvetľujúce kľúčové koncepty
- Notebooky priateľské k Jupyter: bunky by mali byť čo najviac samostatné
- Žiadne prísne požiadavky na linting pre obsah lekcií

### JavaScript/Vue.js (aplikácia kvízov)

- Konfigurácia ESLint v `etc/quiz-app/package.json`
- Spustite `npm run lint` na kontrolu a automatické opravy problémov
- Konvencie Vue 2.x
- Architektúra založená na komponentoch

### Organizácia súborov

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

## Build a nasadenie

### Obsah Jupyter

Nie je potrebný žiadny build proces - Jupyter Notebooks sa spúšťajú priamo.

### Aplikácia kvízov

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

### Dokumentačná stránka

Repozitár používa Docsify na dokumentáciu:
- `index.html` slúži ako vstupný bod
- Nie je potrebný žiadny build - slúži priamo cez GitHub Pages
- Prístup na: https://microsoft.github.io/AI-For-Beginners/

## Pokyny na prispievanie

### Proces Pull Request

1. **Formát názvu:** Jasné, popisné názvy opisujúce zmenu
2. **Požiadavka CLA:** Microsoft CLA musí byť podpísané (automatická kontrola)
3. **Pokyny k obsahu:**
   - Zachovajte vzdelávací zameranie a prístup pre začiatočníkov
   - Testujte všetky príklady kódu v notebookoch
   - Uistite sa, že notebooky fungujú od začiatku do konca
   - Aktualizujte preklady, ak upravujete anglický obsah
4. **Zmeny aplikácie kvízov:** Spustite `npm run lint` pred commitom

### Príspevky k prekladom

- Preklady sú automatizované cez GitHub Actions pomocou co-op-translator
- Manuálne preklady idú do `translations/<language-code>/`
- Preklady kvízov v `etc/quiz-app/src/assets/translations/`
- Podporované jazyky: 40+ jazykov (pozrite README pre úplný zoznam)

### Aktívne oblasti prispievania

Pozrite `etc/CONTRIBUTING.md` pre aktuálne potreby:
- Sekcie hlbokého posilňovacieho učenia
- Vylepšenia detekcie objektov
- Príklady rozpoznávania pomenovaných entít
- Ukážky vlastného tréningu embeddingov

## Konfigurácia prostredia

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

### Premenné prostredia

Nie sú potrebné žiadne špeciálne premenné prostredia pre základné použitie.

Pre nasadenia na Azure (aplikácia kvízov):
- `AZURE_STATIC_WEB_APPS_API_TOKEN` (nastavené automaticky Azure)

## Ladenie a riešenie problémov

### Bežné problémy

**Problém:** Vytvorenie conda prostredia zlyhá
- **Riešenie:** Najskôr aktualizujte conda: `conda update conda -y`
- Uistite sa, že máte dostatok miesta na disku (odporúča sa 50GB)

**Problém:** Jupyter kernel nebol nájdený
- **Riešenie:** 
  ```bash
  conda activate ai4beg
  python -m ipykernel install --user --name ai4beg
  ```

**Problém:** GPU nie je detekované v notebookoch
- **Riešenie:** 
  - Overte inštaláciu CUDA: `nvidia-smi`
  - Skontrolujte GPU v PyTorch: `python -c "import torch; print(torch.cuda.is_available())"`
  - Skontrolujte GPU v TensorFlow: `python -c "import tensorflow as tf; print(tf.config.list_physical_devices('GPU'))"`

**Problém:** Aplikácia kvízov sa nespustí
- **Riešenie:**
  ```bash
  cd etc/quiz-app
  rm -rf node_modules package-lock.json
  npm install
  npm run serve
  ```

**Problém:** Binder vyprší čas alebo blokuje sťahovanie
- **Riešenie:** Použite GitHub Codespaces alebo lokálne nastavenie pre lepší prístup k zdrojom

### Problémy s pamäťou

Niektoré lekcie vyžadujú značné množstvo RAM (odporúča sa 8GB+):
- Použite cloudové VM pre lekcie náročné na zdroje
- Zatvorte ostatné aplikácie pri tréningu modelov
- Znížte veľkosti dávok v notebookoch, ak dochádza pamäť

## Dodatočné poznámky

### Pre učiteľov kurzu

- Pozrite `lessons/0-course-setup/for-teachers.md` pre pokyny na výučbu
- Lekcie sú samostatné a môžu byť vyučované postupne alebo vybrané individuálne
- Odhadovaný čas: 12 týždňov pri 2 lekciách týždenne

### Cloudové zdroje

- **Azure for Students:** Bezplatné kredity dostupné pre študentov
- **Microsoft Learn:** Doplnkové vzdelávacie cesty prepojené v celom kurze
- **Binder:** Bezplatné, ale obmedzené zdroje a niektoré obmedzenia siete

### Možnosti spúšťania kódu

1. **Lokálne (odporúčané):** Plná kontrola, najlepší výkon, podpora GPU
2. **GitHub Codespaces:** Cloudový VS Code, vhodný na rýchly prístup
3. **Binder:** Jupyter v prehliadači, bezplatný, ale obmedzený
4. **Azure ML Notebooks:** Podnikové riešenie s podporou GPU
5. **Google Colab:** Nahrajte notebooky jednotlivo, dostupná bezplatná GPU vrstva

### Práca s notebookmi

- Notebooky sú navrhnuté na spúšťanie bunky po bunke pre učenie
- Mnohé notebooky sťahujú datasety pri prvom spustení (môže to chvíľu trvať)
- Niektoré modely vyžadujú GPU pre rozumné časy tréningu
- Predtrénované modely sa používajú tam, kde je to možné, na zníženie požiadaviek na výpočty

### Výkonnostné úvahy

- Neskoršie lekcie počítačového videnia (CNN, GAN) profitujú z GPU
- Lekcie NLP s transformermi môžu vyžadovať značné množstvo RAM
- Tréning od začiatku je vzdelávací, ale časovo náročný
- Príklady transferového učenia minimalizujú čas tréningu

---

**Upozornenie**:  
Tento dokument bol preložený pomocou služby AI prekladu [Co-op Translator](https://github.com/Azure/co-op-translator). Hoci sa snažíme o presnosť, prosím, berte na vedomie, že automatizované preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho rodnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nenesieme zodpovednosť za akékoľvek nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.