# AGENTS.md

## Projekto apžvalga

AI for Beginners yra išsamus 12 savaičių, 24 pamokų mokymo planas, apimantis dirbtinio intelekto pagrindus. Ši mokomoji saugykla apima praktines pamokas su Jupyter Notebooks, testus ir praktinius laboratorinius darbus. Mokymo planas apima:

- Simbolinį AI su žinių reprezentacija ir ekspertų sistemomis
- Neuroninius tinklus ir gilų mokymąsi naudojant TensorFlow ir PyTorch
- Kompiuterinės regos technikas ir architektūras
- Natūralios kalbos apdorojimą (NLP), įskaitant transformatorius ir BERT
- Specializuotas temas: genetinius algoritmus, stiprinamąjį mokymąsi, daugiaveiksnius sistemas
- AI etikos ir atsakingo AI principus

**Pagrindinės technologijos:** Python 3, Jupyter Notebooks, TensorFlow, PyTorch, Keras, OpenCV, Vue.js (testų aplikacijai)

**Architektūra:** Mokomoji turinio saugykla su Jupyter Notebooks, suskirstyta pagal temines sritis, papildyta Vue.js pagrindu veikiančia testų aplikacija ir plačia daugiakalbe palaikymo sistema.

## Nustatymo komandos

### Pagrindinė kūrimo aplinka (Python/Jupyter)

Mokymo planas sukurtas veikti su Python ir Jupyter Notebooks. Rekomenduojama naudoti miniconda:

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

### Alternatyva: naudojant devcontainer

```bash
# Open in VS Code and select "Reopen in Container" when prompted
# The devcontainer will automatically set up the environment
```

### Testų aplikacijos nustatymas

Testų aplikacija yra atskira Vue.js aplikacija, esanti `etc/quiz-app/`:

```bash
cd etc/quiz-app
npm install
npm run serve  # Development server
npm run build  # Production build
npm run lint   # Lint and fix files
```

## Kūrimo darbo eiga

### Darbas su Jupyter Notebooks

1. **Vietinis kūrimas:**
   - Aktyvuokite conda aplinką: `conda activate ai4beg`
   - Paleiskite Jupyter: `jupyter notebook` arba `jupyter lab`
   - Naršykite pamokų aplankus ir atidarykite `.ipynb` failus
   - Interaktyviai vykdykite langelius, kad sektumėte pamokas

2. **VS Code su Python plėtiniu:**
   - Atidarykite saugyklą VS Code
   - Įdiekite Python plėtinį
   - VS Code automatiškai aptinka ir naudoja conda aplinką
   - Atidarykite `.ipynb` failus tiesiogiai VS Code

3. **Debesų kūrimas:**
   - **GitHub Codespaces:** Spustelėkite "Code" → "Codespaces" → "Create codespace on main"
   - **Binder:** Naudokite Binder ženkliuką README, kad paleistumėte naršyklėje
   - Pastaba: Binder turi ribotus resursus ir tam tikrus interneto prieigos apribojimus

### GPU palaikymas pažengusioms pamokoms

Vėlesnės pamokos labai naudingos naudojant GPU:

- **Azure Data Science VM:** Naudokite NC serijos VM su GPU palaikymu
- **Azure Machine Learning:** Naudokite užrašų knygelių funkcijas su GPU skaičiavimais
- **Google Colab:** Įkelkite užrašų knygeles atskirai (yra nemokamas GPU palaikymas)

### Testų aplikacijos kūrimas

```bash
cd etc/quiz-app
npm run serve  # Hot-reload development server at http://localhost:8080
```

## Testavimo instrukcijos

Tai yra mokomoji saugykla, orientuota į mokymosi turinį, o ne programinės įrangos testavimą. Nėra tradicinio testų rinkinio.

### Validacijos metodai:

1. **Jupyter Notebooks:** Vykdykite langelius iš eilės, kad patikrintumėte, ar kodų pavyzdžiai veikia
2. **Testų aplikacijos testavimas:** Rankinis testavimas per kūrimo serverį
3. **Vertimo validacija:** Patikrinkite išverstą turinį aplanke `translations/`
4. **Testų aplikacijos lintingas:** `npm run lint` aplanke `etc/quiz-app/`

### Kodų pavyzdžių vykdymas:

```bash
# Activate environment first
conda activate ai4beg

# Run Python scripts directly
python lessons/4-ComputerVision/07-ConvNets/pytorchcv.py

# Or execute notebooks
jupyter notebook lessons/3-NeuralNetworks/03-Perceptron/Perceptron.ipynb
```

## Kodų stilius

### Python kodų stilius

- Standartinės Python konvencijos mokomajam kodui
- Aiškus, lengvai suprantamas kodas, prioritetas mokymuisi, o ne optimizavimui
- Komentarai, paaiškinantys pagrindines sąvokas
- Draugiškas Jupyter Notebook: langeliai turėtų būti kuo labiau savarankiški
- Pamokų turiniui nėra griežtų linting reikalavimų

### JavaScript/Vue.js (Testų aplikacija)

- ESLint konfigūracija `etc/quiz-app/package.json`
- Paleiskite `npm run lint`, kad patikrintumėte ir automatiškai ištaisytumėte problemas
- Vue 2.x konvencijos
- Komponentų pagrindu sukurta architektūra

### Failų organizavimas

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

## Kūrimas ir diegimas

### Jupyter turinys

Nereikia kūrimo proceso - Jupyter Notebooks vykdomi tiesiogiai.

### Testų aplikacija

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

### Dokumentacijos svetainė

Saugykla naudoja Docsify dokumentacijai:
- `index.html` yra įėjimo taškas
- Nereikia kūrimo - tiesiogiai aptarnaujama per GitHub Pages
- Prieiga: https://microsoft.github.io/AI-For-Beginners/

## Prisidėjimo gairės

### Pull Request procesas

1. **Pavadinimo formatas:** Aiškūs, aprašomieji pavadinimai, apibūdinantys pakeitimą
2. **CLA reikalavimas:** Microsoft CLA turi būti pasirašytas (automatinis patikrinimas)
3. **Turinio gairės:**
   - Išlaikykite mokomąjį fokusą ir draugišką pradedantiesiems požiūrį
   - Testuokite visus kodų pavyzdžius užrašų knygelėse
   - Užtikrinkite, kad užrašų knygelės veiktų nuo pradžios iki pabaigos
   - Atnaujinkite vertimus, jei keičiate anglišką turinį
4. **Testų aplikacijos pakeitimai:** Paleiskite `npm run lint` prieš įsipareigojant

### Vertimo indėlis

- Vertimai yra automatizuoti per GitHub Actions naudojant co-op-translator
- Rankiniai vertimai dedami į `translations/<language-code>/`
- Testų vertimai į `etc/quiz-app/src/assets/translations/`
- Palaikomos kalbos: 40+ kalbų (žr. README visą sąrašą)

### Aktyvios prisidėjimo sritys

Žr. `etc/CONTRIBUTING.md` dėl dabartinių poreikių:
- Gilaus stiprinamojo mokymosi skyriai
- Objektų aptikimo patobulinimai
- Pavyzdžiai su pavadintų objektų atpažinimu
- Pavyzdžiai su individualizuotu įterpimų mokymu

## Aplinkos konfigūracija

### Reikalingos priklausomybės

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

### Aplinkos kintamieji

Nereikia specialių aplinkos kintamųjų pagrindiniam naudojimui.

Azure diegimams (testų aplikacija):
- `AZURE_STATIC_WEB_APPS_API_TOKEN` (automatiškai nustatomas Azure)

## Derinimas ir trikčių šalinimas

### Dažnos problemos

**Problema:** Conda aplinkos kūrimas nepavyksta
- **Sprendimas:** Pirmiausia atnaujinkite conda: `conda update conda -y`
- Užtikrinkite pakankamą disko vietą (rekomenduojama 50GB)

**Problema:** Jupyter branduolys nerastas
- **Sprendimas:** 
  ```bash
  conda activate ai4beg
  python -m ipykernel install --user --name ai4beg
  ```

**Problema:** GPU neužfiksuotas užrašų knygelėse
- **Sprendimas:** 
  - Patikrinkite CUDA diegimą: `nvidia-smi`
  - Patikrinkite PyTorch GPU: `python -c "import torch; print(torch.cuda.is_available())"`
  - Patikrinkite TensorFlow GPU: `python -c "import tensorflow as tf; print(tf.config.list_physical_devices('GPU'))"`

**Problema:** Testų aplikacija nepasileidžia
- **Sprendimas:**
  ```bash
  cd etc/quiz-app
  rm -rf node_modules package-lock.json
  npm install
  npm run serve
  ```

**Problema:** Binder laikas baigiasi arba blokuoja atsisiuntimus
- **Sprendimas:** Naudokite GitHub Codespaces arba vietinį nustatymą geresniam resursų prieinamumui

### Atminties problemos

Kai kurios pamokos reikalauja daug RAM (rekomenduojama 8GB+):
- Naudokite debesų VM resursams reikalaujančioms pamokoms
- Uždarykite kitas programas, kai mokote modelius
- Sumažinkite partijų dydžius užrašų knygelėse, jei trūksta atminties

## Papildomos pastabos

### Kursų instruktoriams

- Žr. `lessons/0-course-setup/for-teachers.md` dėl mokymo gairių
- Pamokos yra savarankiškos ir gali būti mokomos iš eilės arba pasirinktos atskirai
- Numatomas laikas: 12 savaičių po 2 pamokas per savaitę

### Debesų resursai

- **Azure for Students:** Nemokami kreditai studentams
- **Microsoft Learn:** Papildomi mokymosi keliai, susieti visame kurse
- **Binder:** Nemokamas, bet riboti resursai ir tam tikri tinklo apribojimai

### Kodų vykdymo parinktys

1. **Vietinis (rekomenduojama):** Pilna kontrolė, geriausias našumas, GPU palaikymas
2. **GitHub Codespaces:** Debesų pagrindu veikiantis VS Code, geras greitam pasiekiamumui
3. **Binder:** Naršyklės pagrindu veikiantis Jupyter, nemokamas, bet ribotas
4. **Azure ML Notebooks:** Įmonės pasirinkimas su GPU palaikymu
5. **Google Colab:** Įkelkite užrašų knygeles atskirai, yra nemokamas GPU lygis

### Darbas su užrašų knygelėmis

- Užrašų knygelės sukurtos taip, kad būtų vykdomos langelis po langelio mokymuisi
- Daugelis užrašų knygelių pirmą kartą paleidžiant atsisiunčia duomenų rinkinius (gali užtrukti)
- Kai kurie modeliai reikalauja GPU, kad mokymas būtų greitas
- Naudojami iš anksto apmokyti modeliai, kad sumažėtų skaičiavimo reikalavimai

### Našumo svarstymai

- Vėlesnės kompiuterinės regos pamokos (CNN, GAN) naudingos naudojant GPU
- NLP transformatorių pamokos gali reikalauti daug RAM
- Mokymas nuo nulio yra mokomasis, bet užima daug laiko
- Perkėlimo mokymosi pavyzdžiai sumažina mokymo laiką

---

**Atsakomybės atsisakymas**:  
Šis dokumentas buvo išverstas naudojant AI vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba turėtų būti laikomas autoritetingu šaltiniu. Dėl svarbios informacijos rekomenduojama profesionali žmogaus vertimo paslauga. Mes neprisiimame atsakomybės už nesusipratimus ar neteisingus aiškinimus, atsiradusius naudojant šį vertimą.