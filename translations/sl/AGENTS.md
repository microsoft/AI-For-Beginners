# AGENTS.md

## Pregled projekta

AI for Beginners je obsežen 12-tedenski, 24-lekcijski učni načrt, ki pokriva osnove umetne inteligence. Ta izobraževalni repozitorij vključuje praktične lekcije z uporabo Jupyter Notebooks, kvize in praktične laboratorijske vaje. Učni načrt zajema:

- Simbolno AI z reprezentacijo znanja in ekspertnih sistemov
- Nevronske mreže in globoko učenje z TensorFlow in PyTorch
- Tehnike in arhitekture računalniškega vida
- Obdelavo naravnega jezika (NLP), vključno s transformatorji in BERT
- Specializirane teme: genetski algoritmi, okrepljeno učenje, sistemi z več agenti
- Etika AI in načela odgovorne umetne inteligence

**Ključne tehnologije:** Python 3, Jupyter Notebooks, TensorFlow, PyTorch, Keras, OpenCV, Vue.js (za aplikacijo kvizov)

**Arhitektura:** Izobraževalni repozitorij z vsebinami, organiziranimi po tematskih področjih, dopolnjen z aplikacijo za kvize, ki temelji na Vue.js, ter obsežno podporo za več jezikov.

## Ukazi za nastavitev

### Primarno razvojno okolje (Python/Jupyter)

Učni načrt je zasnovan za uporabo s Pythonom in Jupyter Notebooks. Priporočena metoda je uporaba miniconda:

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

### Alternativa: Uporaba devcontainer

```bash
# Open in VS Code and select "Reopen in Container" when prompted
# The devcontainer will automatically set up the environment
```

### Nastavitev aplikacije za kvize

Aplikacija za kvize je ločena aplikacija Vue.js, ki se nahaja v `etc/quiz-app/`:

```bash
cd etc/quiz-app
npm install
npm run serve  # Development server
npm run build  # Production build
npm run lint   # Lint and fix files
```

## Razvojni potek dela

### Delo z Jupyter Notebooks

1. **Lokalni razvoj:**
   - Aktivirajte conda okolje: `conda activate ai4beg`
   - Zaženite Jupyter: `jupyter notebook` ali `jupyter lab`
   - Pomaknite se do map z lekcijami in odprite `.ipynb` datoteke
   - Interaktivno izvajajte celice za sledenje lekcijam

2. **VS Code z razširitvijo za Python:**
   - Odprite repozitorij v VS Code
   - Namestite razširitev za Python
   - VS Code samodejno zazna in uporabi conda okolje
   - Neposredno odprite `.ipynb` datoteke v VS Code

3. **Razvoj v oblaku:**
   - **GitHub Codespaces:** Kliknite "Code" → "Codespaces" → "Create codespace on main"
   - **Binder:** Uporabite značko Binder v README za zagon v brskalniku
   - Opomba: Binder ima omejene vire in nekatere omejitve dostopa do spleta

### Podpora za GPU pri naprednih lekcijah

Kasnejše lekcije močno koristijo pospeševanje z GPU:

- **Azure Data Science VM:** Uporabite NC-serijo VM-jev z GPU podporo
- **Azure Machine Learning:** Uporabite funkcije zvezkov z GPU računalništvom
- **Google Colab:** Posamezno naložite zvezke (ima brezplačno GPU podporo)

### Razvoj aplikacije za kvize

```bash
cd etc/quiz-app
npm run serve  # Hot-reload development server at http://localhost:8080
```

## Navodila za testiranje

To je izobraževalni repozitorij, osredotočen na učne vsebine, ne na testiranje programske opreme. Tradicionalni testni paket ni na voljo.

### Pristopi za validacijo:

1. **Jupyter Notebooks:** Zaporedno izvajajte celice, da preverite delovanje primerov kode
2. **Testiranje aplikacije za kvize:** Ročno testiranje prek razvojnega strežnika
3. **Validacija prevodov:** Preverite prevedene vsebine v mapi `translations/`
4. **Linting aplikacije za kvize:** `npm run lint` v `etc/quiz-app/`

### Izvajanje primerov kode:

```bash
# Activate environment first
conda activate ai4beg

# Run Python scripts directly
python lessons/4-ComputerVision/07-ConvNets/pytorchcv.py

# Or execute notebooks
jupyter notebook lessons/3-NeuralNetworks/03-Perceptron/Perceptron.ipynb
```

## Slog kode

### Slog Python kode

- Standardne Python konvencije za izobraževalno kodo
- Jasna, berljiva koda, ki daje prednost učenju pred optimizacijo
- Komentarji, ki pojasnjujejo ključne koncepte
- Prijazno za Jupyter Notebook: celice naj bodo čim bolj samostojne
- Brez strogih zahtev za linting pri vsebinah lekcij

### JavaScript/Vue.js (aplikacija za kvize)

- ESLint konfiguracija v `etc/quiz-app/package.json`
- Zaženite `npm run lint` za preverjanje in samodejno odpravljanje težav
- Konvencije Vue 2.x
- Arhitektura, ki temelji na komponentah

### Organizacija datotek

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

## Gradnja in uvajanje

### Vsebina Jupyter

Gradnja ni potrebna - Jupyter Notebooks se izvajajo neposredno.

### Aplikacija za kvize

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

### Spletno mesto dokumentacije

Repozitorij uporablja Docsify za dokumentacijo:
- `index.html` služi kot vstopna točka
- Gradnja ni potrebna - neposredno dostopno prek GitHub Pages
- Dostop na: https://microsoft.github.io/AI-For-Beginners/

## Smernice za prispevanje

### Postopek za Pull Request

1. **Oblika naslova:** Jasni, opisni naslovi, ki opisujejo spremembo
2. **Zahteva CLA:** Microsoft CLA mora biti podpisan (samodejna preverba)
3. **Smernice za vsebino:**
   - Ohranjajte izobraževalni fokus in pristop, prijazen začetnikom
   - Testirajte vse primere kode v zvezkih
   - Zagotovite, da zvezki delujejo od začetka do konca
   - Posodobite prevode, če spreminjate vsebine v angleščini
4. **Spremembe aplikacije za kvize:** Zaženite `npm run lint` pred potrditvijo

### Prispevki k prevodom

- Prevajanja so avtomatizirana prek GitHub Actions z uporabo co-op-translator
- Ročni prevodi gredo v `translations/<language-code>/`
- Prevodi kvizov v `etc/quiz-app/src/assets/translations/`
- Podprti jeziki: več kot 40 jezikov (glejte README za celoten seznam)

### Aktivna področja prispevkov

Glejte `etc/CONTRIBUTING.md` za trenutne potrebe:
- Sekcije globokega okrepljenega učenja
- Izboljšave pri zaznavanju objektov
- Primeri prepoznavanja imenovanih entitet
- Vzorci za usposabljanje prilagojenih vdelav

## Konfiguracija okolja

### Zahtevane odvisnosti

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

### Spremenljivke okolja

Za osnovno uporabo niso potrebne posebne spremenljivke okolja.

Za uvajanje na Azure (aplikacija za kvize):
- `AZURE_STATIC_WEB_APPS_API_TOKEN` (samodejno nastavljeno prek Azure)

## Odpravljanje napak in težav

### Pogoste težave

**Težava:** Ustvarjanje conda okolja ne uspe
- **Rešitev:** Najprej posodobite conda: `conda update conda -y`
- Prepričajte se, da imate dovolj prostora na disku (priporočeno 50GB)

**Težava:** Jupyter jedro ni najdeno
- **Rešitev:** 
  ```bash
  conda activate ai4beg
  python -m ipykernel install --user --name ai4beg
  ```

**Težava:** GPU ni zaznan v zvezkih
- **Rešitev:** 
  - Preverite namestitev CUDA: `nvidia-smi`
  - Preverite GPU v PyTorch: `python -c "import torch; print(torch.cuda.is_available())"`
  - Preverite GPU v TensorFlow: `python -c "import tensorflow as tf; print(tf.config.list_physical_devices('GPU'))"`

**Težava:** Aplikacija za kvize se ne zažene
- **Rešitev:**
  ```bash
  cd etc/quiz-app
  rm -rf node_modules package-lock.json
  npm install
  npm run serve
  ```

**Težava:** Binder se izteče ali blokira prenose
- **Rešitev:** Uporabite GitHub Codespaces ali lokalno nastavitev za boljši dostop do virov

### Težave z pomnilnikom

Nekatere lekcije zahtevajo veliko RAM-a (priporočeno 8GB+):
- Uporabite VM-je v oblaku za lekcije, ki zahtevajo veliko virov
- Zaprite druge aplikacije med usposabljanjem modelov
- Zmanjšajte velikosti serij v zvezkih, če zmanjkuje pomnilnika

## Dodatne opombe

### Za učitelje tečaja

- Glejte `lessons/0-course-setup/for-teachers.md` za smernice poučevanja
- Lekcije so samostojne in jih je mogoče učiti zaporedno ali izbrati posamezno
- Ocenjen čas: 12 tednov, 2 lekciji na teden

### Viri v oblaku

- **Azure za študente:** Brezplačni krediti na voljo za študente
- **Microsoft Learn:** Dodatne učne poti, povezane skozi celoten tečaj
- **Binder:** Brezplačno, vendar omejeni viri in nekatere omejitve omrežja

### Možnosti izvajanja kode

1. **Lokalno (priporočeno):** Popoln nadzor, najboljša zmogljivost, podpora za GPU
2. **GitHub Codespaces:** Oblak, ki temelji na VS Code, dobro za hiter dostop
3. **Binder:** Jupyter v brskalniku, brezplačno, vendar omejeno
4. **Azure ML Notebooks:** Možnost za podjetja z GPU podporo
5. **Google Colab:** Posamezno naložite zvezke, na voljo brezplačna GPU raven

### Delo z zvezki

- Zvezki so zasnovani za izvajanje celice po celici za učenje
- Veliko zvezkov ob prvem zagonu prenese podatkovne nabore (lahko traja nekaj časa)
- Nekateri modeli zahtevajo GPU za razumno časovno usposabljanje
- Predhodno usposobljeni modeli se uporabljajo, kjer je mogoče, za zmanjšanje zahtev po računalniški moči

### Premisleki o zmogljivosti

- Kasnejše lekcije računalniškega vida (CNN, GAN) koristijo GPU
- Lekcije NLP transformatorjev lahko zahtevajo veliko RAM-a
- Usposabljanje od začetka je poučno, vendar zamudno
- Primeri prenosa učenja zmanjšujejo čas usposabljanja

---

**Omejitev odgovornosti**:  
Ta dokument je bil preveden z uporabo storitve AI za prevajanje [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas prosimo, da upoštevate, da lahko avtomatizirani prevodi vsebujejo napake ali netočnosti. Izvirni dokument v njegovem maternem jeziku je treba obravnavati kot avtoritativni vir. Za ključne informacije priporočamo profesionalni človeški prevod. Ne prevzemamo odgovornosti za morebitne nesporazume ali napačne razlage, ki bi nastale zaradi uporabe tega prevoda.