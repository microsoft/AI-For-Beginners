# AGENTS.md

## Muhtasari wa Mradi

AI for Beginners ni mtaala wa kina wa wiki 12, masomo 24 unaofundisha misingi ya Akili Bandia. Hifadhi hii ya kielimu inajumuisha masomo ya vitendo kwa kutumia Jupyter Notebooks, majaribio, na maabara ya vitendo. Mtaala unashughulikia:

- AI ya Kisimboli kwa kutumia Uwakilishi wa Maarifa na Mifumo ya Wataalamu
- Mitandao ya Neva na Kujifunza kwa Kina kwa kutumia TensorFlow na PyTorch
- Mbinu na miundo ya Maono ya Kompyuta
- Usindikaji wa Lugha Asilia (NLP) ikijumuisha transformers na BERT
- Mada Maalum: Algorithimu za Kijenetiki, Kujifunza kwa Kuimarisha, Mifumo ya Wakala Wengi
- Maadili ya AI na kanuni za AI Inayowajibika

**Teknolojia Muhimu:** Python 3, Jupyter Notebooks, TensorFlow, PyTorch, Keras, OpenCV, Vue.js (kwa programu ya majaribio)

**Miundombinu:** Hifadhi ya maudhui ya kielimu yenye Jupyter Notebooks zilizopangwa kwa maeneo ya mada, ikisaidiwa na programu ya majaribio inayotumia Vue.js na msaada wa lugha nyingi.

## Amri za Usanidi

### Mazingira ya Kimsingi ya Maendeleo (Python/Jupyter)

Mtaala umeundwa kuendeshwa kwa Python na Jupyter Notebooks. Njia inayopendekezwa ni kutumia miniconda:

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

### Njia Mbadala: Kutumia devcontainer

```bash
# Open in VS Code and select "Reopen in Container" when prompted
# The devcontainer will automatically set up the environment
```

### Usanidi wa Programu ya Majaribio

Programu ya majaribio ni programu tofauti ya Vue.js iliyoko kwenye `etc/quiz-app/`:

```bash
cd etc/quiz-app
npm install
npm run serve  # Development server
npm run build  # Production build
npm run lint   # Lint and fix files
```

## Mtiririko wa Maendeleo

### Kufanya Kazi na Jupyter Notebooks

1. **Maendeleo ya Ndani:**
   - Washa mazingira ya conda: `conda activate ai4beg`
   - Anzisha Jupyter: `jupyter notebook` au `jupyter lab`
   - Nenda kwenye folda za masomo na fungua faili za `.ipynb`
   - Endesha seli moja baada ya nyingine kufuata masomo

2. **VS Code na Kiendelezi cha Python:**
   - Fungua hifadhi kwenye VS Code
   - Sakinisha kiendelezi cha Python
   - VS Code hugundua na kutumia mazingira ya conda moja kwa moja
   - Fungua faili za `.ipynb` moja kwa moja kwenye VS Code

3. **Maendeleo ya Wingu:**
   - **GitHub Codespaces:** Bonyeza "Code" → "Codespaces" → "Create codespace on main"
   - **Binder:** Tumia beji ya Binder kwenye README kufungua kwenye kivinjari
   - Kumbuka: Binder ina rasilimali chache na vizuizi vya ufikiaji wa wavuti

### Msaada wa GPU kwa Masomo ya Juu

Masomo ya baadaye yanapata manufaa makubwa kutoka kwa kasi ya GPU:

- **Azure Data Science VM:** Tumia NC-series VMs zenye msaada wa GPU
- **Azure Machine Learning:** Tumia vipengele vya daftari na hesabu ya GPU
- **Google Colab:** Pakia daftari moja moja (ina msaada wa GPU bila malipo)

### Maendeleo ya Programu ya Majaribio

```bash
cd etc/quiz-app
npm run serve  # Hot-reload development server at http://localhost:8080
```

## Maelekezo ya Kupima

Hii ni hifadhi ya kielimu inayolenga maudhui ya kujifunza badala ya kupima programu. Hakuna seti ya majaribio ya jadi.

### Njia za Uthibitishaji:

1. **Jupyter Notebooks:** Endesha seli mfululizo ili kuthibitisha mifano ya msimbo inafanya kazi
2. **Kupima Programu ya Majaribio:** Kupima kwa mikono kupitia seva ya maendeleo
3. **Uthibitishaji wa Tafsiri:** Angalia maudhui yaliyotafsiriwa kwenye folda ya `translations/`
4. **Linting ya Programu ya Majaribio:** `npm run lint` kwenye `etc/quiz-app/`

### Kuendesha Mifano ya Msimbo:

```bash
# Activate environment first
conda activate ai4beg

# Run Python scripts directly
python lessons/4-ComputerVision/07-ConvNets/pytorchcv.py

# Or execute notebooks
jupyter notebook lessons/3-NeuralNetworks/03-Perceptron/Perceptron.ipynb
```

## Mtindo wa Msimbo

### Mtindo wa Msimbo wa Python

- Miongozo ya kawaida ya Python kwa msimbo wa kielimu
- Msimbo ulio wazi na rahisi kueleweka, ukipa kipaumbele kujifunza badala ya ufanisi
- Maelezo ya maoni yanayoelezea dhana muhimu
- Rafiki wa Jupyter Notebook: seli zinapaswa kuwa huru kadri inavyowezekana
- Hakuna mahitaji madhubuti ya linting kwa maudhui ya masomo

### JavaScript/Vue.js (Programu ya Majaribio)

- Usanidi wa ESLint kwenye `etc/quiz-app/package.json`
- Endesha `npm run lint` ili kuangalia na kurekebisha masuala moja kwa moja
- Miongozo ya Vue 2.x
- Miundombinu inayotegemea vipengele

### Mpangilio wa Faili

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

## Ujenzi na Upelekaji

### Maudhui ya Jupyter

Hakuna mchakato wa ujenzi unaohitajika - Jupyter Notebooks zinaendeshwa moja kwa moja.

### Programu ya Majaribio

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

### Tovuti ya Nyaraka

Hifadhi inatumia Docsify kwa nyaraka:
- `index.html` hutumika kama sehemu ya kuanzia
- Hakuna ujenzi unaohitajika - hutolewa moja kwa moja kupitia GitHub Pages
- Fikia kwenye: https://microsoft.github.io/AI-For-Beginners/

## Miongozo ya Kuchangia

### Mchakato wa Ombi la Kuvuta

1. **Muundo wa Kichwa:** Vichwa wazi, vinavyoelezea mabadiliko
2. **Mahitaji ya CLA:** CLA ya Microsoft lazima isainiwe (ukaguzi wa kiotomatiki)
3. **Miongozo ya Maudhui:**
   - Dumisha mtazamo wa kielimu na urahisi wa wanaoanza
   - Jaribu mifano yote ya msimbo kwenye daftari
   - Hakikisha daftari zinaendeshwa mwanzo hadi mwisho
   - Sasisha tafsiri ikiwa unarekebisha maudhui ya Kiingereza
4. **Mabadiliko ya Programu ya Majaribio:** Endesha `npm run lint` kabla ya kujitolea

### Michango ya Tafsiri

- Tafsiri zinafanywa kiotomatiki kupitia GitHub Actions kwa kutumia co-op-translator
- Tafsiri za mikono huenda kwenye `translations/<language-code>/`
- Tafsiri za majaribio kwenye `etc/quiz-app/src/assets/translations/`
- Lugha zinazoungwa mkono: Lugha 40+ (angalia README kwa orodha kamili)

### Maeneo ya Michango Hai

Angalia `etc/CONTRIBUTING.md` kwa mahitaji ya sasa:
- Sehemu za Kujifunza kwa Kuimarisha kwa Kina
- Maboresho ya Utambuzi wa Vitu
- Mifano ya Utambuzi wa Viumbe kwa Majina
- Sampuli za mafunzo ya embeddings maalum

## Usanidi wa Mazingira

### Vitegemezi Vinavyohitajika

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

### Vigezo vya Mazingira

Hakuna vigezo maalum vya mazingira vinavyohitajika kwa matumizi ya msingi.

Kwa upelekaji wa Azure (programu ya majaribio):
- `AZURE_STATIC_WEB_APPS_API_TOKEN` (imewekwa kiotomatiki na Azure)

## Utatuzi wa Hitilafu

### Masuala ya Kawaida

**Tatizo:** Uundaji wa mazingira ya conda unashindwa
- **Suluhisho:** Sasisha conda kwanza: `conda update conda -y`
- Hakikisha nafasi ya diski inatosha (50GB inapendekezwa)

**Tatizo:** Kernel ya Jupyter haipatikani
- **Suluhisho:** 
  ```bash
  conda activate ai4beg
  python -m ipykernel install --user --name ai4beg
  ```

**Tatizo:** GPU haijatambuliwa kwenye daftari
- **Suluhisho:** 
  - Thibitisha usakinishaji wa CUDA: `nvidia-smi`
  - Angalia GPU ya PyTorch: `python -c "import torch; print(torch.cuda.is_available())"`
  - Angalia GPU ya TensorFlow: `python -c "import tensorflow as tf; print(tf.config.list_physical_devices('GPU'))"`

**Tatizo:** Programu ya majaribio haianzi
- **Suluhisho:**
  ```bash
  cd etc/quiz-app
  rm -rf node_modules package-lock.json
  npm install
  npm run serve
  ```

**Tatizo:** Binder inachukua muda mrefu au inazuia upakuaji
- **Suluhisho:** Tumia GitHub Codespaces au usanidi wa ndani kwa ufikiaji bora wa rasilimali

### Masuala ya Kumbukumbu

Baadhi ya masomo yanahitaji RAM kubwa (8GB+ inapendekezwa):
- Tumia VMs za wingu kwa masomo yanayohitaji rasilimali nyingi
- Funga programu nyingine wakati wa kufundisha mifano
- Punguza ukubwa wa kundi kwenye daftari ikiwa kumbukumbu inakosekana

## Vidokezo vya Ziada

### Kwa Walimu wa Kozi

- Angalia `lessons/0-course-setup/for-teachers.md` kwa mwongozo wa kufundisha
- Masomo ni huru na yanaweza kufundishwa kwa mfuatano au kuchaguliwa moja moja
- Muda unaokadiriwa: Wiki 12 kwa masomo 2 kwa wiki

### Rasilimali za Wingu

- **Azure kwa Wanafunzi:** Mikopo ya bure inapatikana kwa wanafunzi
- **Microsoft Learn:** Njia za kujifunza za ziada zimeunganishwa kote
- **Binder:** Bila malipo lakini ina rasilimali chache na vizuizi vya mtandao

### Chaguo za Utekelezaji wa Msimbo

1. **Ndani (Inapendekezwa):** Udhibiti kamili, utendaji bora, msaada wa GPU
2. **GitHub Codespaces:** VS Code inayotegemea wingu, nzuri kwa ufikiaji wa haraka
3. **Binder:** Jupyter inayotegemea kivinjari, bila malipo lakini na vizuizi
4. **Azure ML Notebooks:** Chaguo la biashara lenye msaada wa GPU
5. **Google Colab:** Pakia daftari moja moja, kiwango cha bure cha GPU kinapatikana

### Kufanya Kazi na Daftari

- Daftari zimeundwa kuendeshwa seli kwa seli kwa kujifunza
- Daftari nyingi hupakua seti za data mara ya kwanza zinapoendeshwa (inaweza kuchukua muda)
- Baadhi ya mifano inahitaji GPU kwa nyakati za mafunzo zinazokubalika
- Mifano iliyofunzwa tayari inatumiwa inapowezekana kupunguza mahitaji ya hesabu

### Mazingatio ya Utendaji

- Masomo ya baadaye ya maono ya kompyuta (CNNs, GANs) yanapata manufaa kutoka kwa GPU
- Masomo ya NLP ya transformer yanaweza kuhitaji RAM kubwa
- Mafunzo kutoka mwanzo ni ya kielimu lakini yanachukua muda
- Mifano ya kujifunza kwa uhamisho hupunguza muda wa mafunzo

---

**Kanusho**:  
Hati hii imetafsiriwa kwa kutumia huduma ya tafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kwa usahihi, tafadhali fahamu kuwa tafsiri za kiotomatiki zinaweza kuwa na makosa au kutokuwa sahihi. Hati ya asili katika lugha yake ya awali inapaswa kuchukuliwa kama chanzo cha mamlaka. Kwa taarifa muhimu, inashauriwa kutumia huduma ya tafsiri ya binadamu ya kitaalamu. Hatutawajibika kwa maelewano mabaya au tafsiri zisizo sahihi zinazotokana na matumizi ya tafsiri hii.