# AGENTS.md

## Projekti ülevaade

AI for Beginners on põhjalik 12-nädalane, 24-õppetunniga õppekava, mis hõlmab tehisintellekti põhialuseid. See hariduslik repositoorium sisaldab praktilisi õppetunde Jupyter Notebookides, teste ja praktilisi laboreid. Õppekava hõlmab:

- Sümboolne AI koos teadmiste esitluse ja ekspertsüsteemidega
- Neuraalvõrgud ja süvaõpe TensorFlow ja PyTorch abil
- Arvutinägemise tehnikad ja arhitektuurid
- Loodusliku keele töötlemine (NLP), sealhulgas transformerid ja BERT
- Spetsialiseeritud teemad: geneetilised algoritmid, tugevdusõpe, multiagent-süsteemid
- AI eetika ja vastutustundliku AI põhimõtted

**Peamised tehnoloogiad:** Python 3, Jupyter Notebookid, TensorFlow, PyTorch, Keras, OpenCV, Vue.js (testirakenduse jaoks)

**Arhitektuur:** Haridusliku sisu repositoorium, kus Jupyter Notebookid on organiseeritud teemade kaupa, täiendatud Vue.js-põhise testirakenduse ja ulatusliku mitmekeelse toega.

## Seadistamise käsud

### Peamine arenduskeskkond (Python/Jupyter)

Õppekava on loodud töötama Pythoniga ja Jupyter Notebookidega. Soovitatav lähenemine on kasutada minicondat:

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

### Alternatiiv: devcontaineri kasutamine

```bash
# Open in VS Code and select "Reopen in Container" when prompted
# The devcontainer will automatically set up the environment
```

### Testirakenduse seadistamine

Testirakendus on eraldi Vue.js rakendus, mis asub kaustas `etc/quiz-app/`:

```bash
cd etc/quiz-app
npm install
npm run serve  # Development server
npm run build  # Production build
npm run lint   # Lint and fix files
```

## Arenduse töövoog

### Töötamine Jupyter Notebookidega

1. **Kohalik arendus:**
   - Aktiveeri conda keskkond: `conda activate ai4beg`
   - Käivita Jupyter: `jupyter notebook` või `jupyter lab`
   - Liigu õppetundide kaustadesse ja ava `.ipynb` failid
   - Käivita lahtrid interaktiivselt, et õppetundidega kaasa minna

2. **VS Code Python laiendiga:**
   - Ava repositoorium VS Code'is
   - Paigalda Python laiendus
   - VS Code tuvastab ja kasutab automaatselt conda keskkonda
   - Ava `.ipynb` failid otse VS Code'is

3. **Pilvearendus:**
   - **GitHub Codespaces:** Klõpsa "Code" → "Codespaces" → "Create codespace on main"
   - **Binder:** Kasuta README-s olevat Binderi märki, et käivitada brauseris
   - Märkus: Binderil on piiratud ressursid ja mõned veebipääsu piirangud

### GPU tugi edasijõudnud õppetundide jaoks

Hilisemad õppetunnid saavad GPU kiirendusest märkimisväärset kasu:

- **Azure Data Science VM:** Kasuta NC-seeria VM-e GPU toega
- **Azure Machine Learning:** Kasuta GPU arvutusvõimalustega märkmikufunktsioone
- **Google Colab:** Laadi märkmikud individuaalselt üles (pakub tasuta GPU tuge)

### Testirakenduse arendus

```bash
cd etc/quiz-app
npm run serve  # Hot-reload development server at http://localhost:8080
```

## Testimisjuhised

See on hariduslik repositoorium, mis keskendub õppesisule, mitte tarkvara testimisele. Traditsioonilist testikomplekti ei ole.

### Valideerimise lähenemised:

1. **Jupyter Notebookid:** Käivita lahtrid järjestikku, et kontrollida koodinäidete toimimist
2. **Testirakenduse testimine:** Käsitsi testimine arendusserveri kaudu
3. **Tõlgete valideerimine:** Kontrolli tõlgitud sisu kaustas `translations/`
4. **Testirakenduse lintimine:** `npm run lint` kaustas `etc/quiz-app/`

### Koodinäidete käivitamine:

```bash
# Activate environment first
conda activate ai4beg

# Run Python scripts directly
python lessons/4-ComputerVision/07-ConvNets/pytorchcv.py

# Or execute notebooks
jupyter notebook lessons/3-NeuralNetworks/03-Perceptron/Perceptron.ipynb
```

## Koodistiil

### Pythoni koodistiil

- Standardne Pythoni konventsioon haridusliku koodi jaoks
- Selge ja loetav kood, mis eelistab õppimist optimeerimise asemel
- Kommentaarid, mis selgitavad põhikontseptsioone
- Jupyter Notebooki-sõbralik: lahtrid peaksid olema võimalikult iseseisvad
- Õppetundide sisule ei kehti ranged lintimisnõuded

### JavaScript/Vue.js (testirakendus)

- ESLinti konfiguratsioon kaustas `etc/quiz-app/package.json`
- Käivita `npm run lint`, et kontrollida ja automaatselt parandada probleeme
- Vue 2.x konventsioonid
- Komponentidel põhinev arhitektuur

### Failide organiseerimine

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

## Ehitamine ja juurutamine

### Jupyteri sisu

Ehitamisprotsessi ei ole vaja - Jupyter Notebookid käivitatakse otse.

### Testirakendus

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

### Dokumentatsiooni sait

Repositoorium kasutab dokumentatsiooni jaoks Docsifyt:
- `index.html` toimib sissepääsupunktina
- Ehitamist ei ole vaja - teenindatakse otse GitHub Pages kaudu
- Juurdepääs: https://microsoft.github.io/AI-For-Beginners/

## Kaastöö juhised

### Pull Request protsess

1. **Pealkirja formaat:** Selged ja kirjeldavad pealkirjad, mis kirjeldavad muudatust
2. **CLA nõue:** Microsofti CLA peab olema allkirjastatud (automaatne kontroll)
3. **Sisu juhised:**
   - Säilita hariduslik fookus ja algajasõbralik lähenemine
   - Testi kõiki koodinäiteid märkmikes
   - Veendu, et märkmikud töötavad algusest lõpuni
   - Uuenda tõlkeid, kui muudate ingliskeelset sisu
4. **Testirakenduse muudatused:** Käivita `npm run lint` enne commitimist

### Tõlgete kaastöö

- Tõlked tehakse automaatselt GitHub Actionsi kaudu, kasutades co-op-translatorit
- Käsitsi tõlked lähevad kausta `translations/<language-code>/`
- Testide tõlked kausta `etc/quiz-app/src/assets/translations/`
- Toetatud keeled: üle 40 keele (vt README täieliku loendi jaoks)

### Aktiivsed kaastöövaldkonnad

Vaata `etc/CONTRIBUTING.md` praeguste vajaduste jaoks:
- Süva tugevdusõppe sektsioonid
- Objektituvastuse täiustused
- Näidete lisamine nimeüksuste tuvastamiseks
- Kohandatud embeddingu treeningnäidised

## Keskkonna konfiguratsioon

### Nõutavad sõltuvused

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

### Keskkonnamuutujad

Põhikasutuseks ei ole vaja spetsiaalseid keskkonnamuutujaid.

Azure'i juurutuste jaoks (testirakendus):
- `AZURE_STATIC_WEB_APPS_API_TOKEN` (Azure määrab automaatselt)

## Silumine ja tõrkeotsing

### Levinud probleemid

**Probleem:** Conda keskkonna loomine ebaõnnestub
- **Lahendus:** Uuenda esmalt condat: `conda update conda -y`
- Veendu, et kettaruumi oleks piisavalt (soovitatav 50GB)

**Probleem:** Jupyteri kernelit ei leitud
- **Lahendus:** 
  ```bash
  conda activate ai4beg
  python -m ipykernel install --user --name ai4beg
  ```

**Probleem:** GPU ei tuvastatud märkmikes
- **Lahendus:** 
  - Kontrolli CUDA paigaldust: `nvidia-smi`
  - Kontrolli PyTorchi GPU-d: `python -c "import torch; print(torch.cuda.is_available())"`
  - Kontrolli TensorFlow GPU-d: `python -c "import tensorflow as tf; print(tf.config.list_physical_devices('GPU'))"`

**Probleem:** Testirakendus ei käivitu
- **Lahendus:**
  ```bash
  cd etc/quiz-app
  rm -rf node_modules package-lock.json
  npm install
  npm run serve
  ```

**Probleem:** Binder aegub või blokeerib allalaadimised
- **Lahendus:** Kasuta GitHub Codespacesi või kohalikku seadistust parema ressursikasutuse jaoks

### Mälu probleemid

Mõned õppetunnid nõuavad märkimisväärset RAM-i (soovitatav 8GB+):
- Kasuta pilve VM-e ressursimahukate õppetundide jaoks
- Sulge muud rakendused mudelite treenimise ajal
- Vähenda märkmikes batch-suurusi, kui mälu otsa saab

## Täiendavad märkused

### Kursuse juhendajatele

- Vaata `lessons/0-course-setup/for-teachers.md` õpetamisjuhiste jaoks
- Õppetunnid on iseseisvad ja neid saab õpetada järjestikku või individuaalselt valida
- Hinnanguline kestus: 12 nädalat, 2 õppetundi nädalas

### Pilveressursid

- **Azure for Students:** Tasuta krediidid saadaval tudengitele
- **Microsoft Learn:** Täiendavad õpiteed, mis on lingitud kogu kursuse jooksul
- **Binder:** Tasuta, kuid piiratud ressursid ja mõned võrgupiirangud

### Koodi käivitamise valikud

1. **Kohalik (soovitatav):** Täielik kontroll, parim jõudlus, GPU tugi
2. **GitHub Codespaces:** Pilvepõhine VS Code, hea kiireks juurdepääsuks
3. **Binder:** Brauseripõhine Jupyter, tasuta, kuid piiratud
4. **Azure ML märkmikud:** Ettevõtte valik GPU toega
5. **Google Colab:** Laadi märkmikud individuaalselt üles, saadaval tasuta GPU tase

### Töötamine märkmikega

- Märkmikud on loodud lahtrite kaupa käivitamiseks õppimise eesmärgil
- Paljud märkmikud laadivad esmakordsel käivitamisel andmekogumeid (võib võtta aega)
- Mõned mudelid vajavad GPU-d mõistliku treeninguaja saavutamiseks
- Eeltreenitud mudeleid kasutatakse võimalusel, et vähendada arvutusnõudeid

### Jõudluse kaalutlused

- Hilisemad arvutinägemise õppetunnid (CNN-id, GAN-id) saavad kasu GPU-st
- NLP transformeri õppetunnid võivad vajada märkimisväärset RAM-i
- Nullist treenimine on hariduslik, kuid aeganõudev
- Ülekandeõppe näited vähendavad treeninguaega

---

**Lahtiütlus**:  
See dokument on tõlgitud AI tõlketeenuse [Co-op Translator](https://github.com/Azure/co-op-translator) abil. Kuigi püüame tagada täpsust, palume arvestada, et automaatsed tõlked võivad sisaldada vigu või ebatäpsusi. Algne dokument selle algses keeles tuleks pidada autoriteetseks allikaks. Olulise teabe puhul soovitame kasutada professionaalset inimtõlget. Me ei vastuta selle tõlke kasutamisest tulenevate arusaamatuste või valesti tõlgenduste eest.