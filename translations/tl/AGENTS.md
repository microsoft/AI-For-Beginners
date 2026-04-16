# AGENTS.md

## Pangkalahatang-ideya ng Proyekto

Ang AI for Beginners ay isang komprehensibong 12-linggong, 24-leksyon na kurikulum na sumasaklaw sa mga pangunahing kaalaman ng Artificial Intelligence. Ang repositoryong pang-edukasyon na ito ay naglalaman ng mga praktikal na leksyon gamit ang Jupyter Notebooks, mga pagsusulit, at mga hands-on na lab. Ang kurikulum ay sumasaklaw sa:

- Symbolic AI gamit ang Knowledge Representation at Expert Systems
- Neural Networks at Deep Learning gamit ang TensorFlow at PyTorch
- Mga teknolohiya at arkitektura ng Computer Vision
- Natural Language Processing (NLP) kabilang ang transformers at BERT
- Mga espesyal na paksa: Genetic Algorithms, Reinforcement Learning, Multi-Agent Systems
- AI Ethics at mga prinsipyo ng Responsible AI

**Mga Pangunahing Teknolohiya:** Python 3, Jupyter Notebooks, TensorFlow, PyTorch, Keras, OpenCV, Vue.js (para sa quiz app)

**Arkitektura:** Repositoryo ng pang-edukasyong nilalaman na may Jupyter Notebooks na nakaayos ayon sa mga paksa, na sinusuportahan ng isang Vue.js-based na quiz application at malawak na suporta sa multi-language.

## Mga Command sa Setup

### Pangunahing Kapaligiran sa Pag-develop (Python/Jupyter)

Ang kurikulum ay idinisenyo upang tumakbo gamit ang Python at Jupyter Notebooks. Ang inirerekomendang paraan ay ang paggamit ng miniconda:

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

### Alternatibo: Paggamit ng devcontainer

```bash
# Open in VS Code and select "Reopen in Container" when prompted
# The devcontainer will automatically set up the environment
```

### Setup ng Quiz Application

Ang quiz app ay isang hiwalay na Vue.js application na matatagpuan sa `etc/quiz-app/`:

```bash
cd etc/quiz-app
npm install
npm run serve  # Development server
npm run build  # Production build
npm run lint   # Lint and fix files
```

## Workflow ng Pag-develop

### Paggamit ng Jupyter Notebooks

1. **Lokal na Pag-develop:**
   - I-activate ang conda environment: `conda activate ai4beg`
   - Simulan ang Jupyter: `jupyter notebook` o `jupyter lab`
   - Mag-navigate sa mga folder ng leksyon at buksan ang mga `.ipynb` file
   - Patakbuhin ang mga cell nang interaktibo upang sundan ang mga leksyon

2. **VS Code gamit ang Python Extension:**
   - Buksan ang repositoryo sa VS Code
   - I-install ang Python extension
   - Awtomatikong natutukoy ng VS Code ang conda environment
   - Buksan ang mga `.ipynb` file nang direkta sa VS Code

3. **Pag-develop sa Cloud:**
   - **GitHub Codespaces:** I-click ang "Code" → "Codespaces" → "Create codespace on main"
   - **Binder:** Gamitin ang Binder badge sa README upang mag-launch sa browser
   - Tandaan: Ang Binder ay may limitadong resources at ilang mga restriksyon sa web access

### Suporta sa GPU para sa Advanced na Mga Leksyon

Ang mga huling leksyon ay lubos na nakikinabang sa GPU acceleration:

- **Azure Data Science VM:** Gumamit ng NC-series VMs na may GPU support
- **Azure Machine Learning:** Gumamit ng mga notebook feature na may GPU compute
- **Google Colab:** I-upload ang mga notebook nang paisa-isa (may libreng GPU support)

### Pag-develop ng Quiz App

```bash
cd etc/quiz-app
npm run serve  # Hot-reload development server at http://localhost:8080
```

## Mga Tagubilin sa Pagsubok

Ito ay isang repositoryong pang-edukasyon na nakatuon sa nilalaman ng pag-aaral sa halip na software testing. Walang tradisyunal na test suite.

### Mga Paraan ng Pag-validate:

1. **Jupyter Notebooks:** Patakbuhin ang mga cell nang sunud-sunod upang tiyakin na gumagana ang mga halimbawa ng code
2. **Pagsubok ng Quiz App:** Manu-manong pagsubok gamit ang development server
3. **Pag-validate ng Translation:** Suriin ang nilalaman ng pagsasalin sa folder na `translations/`
4. **Linting ng Quiz App:** `npm run lint` sa `etc/quiz-app/`

### Pagpapatakbo ng Mga Halimbawa ng Code:

```bash
# Activate environment first
conda activate ai4beg

# Run Python scripts directly
python lessons/4-ComputerVision/07-ConvNets/pytorchcv.py

# Or execute notebooks
jupyter notebook lessons/3-NeuralNetworks/03-Perceptron/Perceptron.ipynb
```

## Estilo ng Code

### Estilo ng Python Code

- Karaniwang mga convention ng Python para sa educational code
- Malinaw, nababasang code na inuuna ang pag-aaral kaysa sa optimization
- Mga komento na nagpapaliwanag ng mga pangunahing konsepto
- Jupyter Notebook-friendly: ang mga cell ay dapat na self-contained hangga't maaari
- Walang mahigpit na linting requirements para sa nilalaman ng leksyon

### JavaScript/Vue.js (Quiz App)

- ESLint configuration sa `etc/quiz-app/package.json`
- Patakbuhin ang `npm run lint` upang suriin at awtomatikong ayusin ang mga isyu
- Mga convention ng Vue 2.x
- Arkitektura na nakabatay sa component

### Organisasyon ng File

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

## Build at Deployment

### Nilalaman ng Jupyter

Walang kinakailangang proseso ng build - ang Jupyter Notebooks ay direktang pinapatakbo.

### Quiz Application

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

### Site ng Dokumentasyon

Ang repositoryo ay gumagamit ng Docsify para sa dokumentasyon:
- Ang `index.html` ang nagsisilbing entry point
- Walang kinakailangang build - direktang isinasagawa sa pamamagitan ng GitHub Pages
- Ma-access sa: https://microsoft.github.io/AI-For-Beginners/

## Mga Alituntunin sa Pag-contribute

### Proseso ng Pull Request

1. **Format ng Pamagat:** Malinaw, deskriptibong pamagat na naglalarawan ng pagbabago
2. **Kailangan ng CLA:** Kailangang pumirma ng Microsoft CLA (automated na pagsusuri)
3. **Mga Alituntunin sa Nilalaman:**
   - Panatilihin ang pokus sa edukasyon at beginner-friendly na approach
   - Subukan ang lahat ng halimbawa ng code sa notebooks
   - Tiyakin na ang mga notebook ay tumatakbo mula simula hanggang dulo
   - I-update ang mga pagsasalin kung binabago ang nilalaman sa Ingles
4. **Mga Pagbabago sa Quiz App:** Patakbuhin ang `npm run lint` bago mag-commit

### Mga Kontribusyon sa Pagsasalin

- Ang mga pagsasalin ay awtomatikong ginagawa sa pamamagitan ng GitHub Actions gamit ang co-op-translator
- Ang mga manu-manong pagsasalin ay inilalagay sa `translations/<language-code>/`
- Ang mga pagsasalin ng quiz ay nasa `etc/quiz-app/src/assets/translations/`
- Mga suportadong wika: 40+ na wika (tingnan ang README para sa buong listahan)

### Aktibong Mga Lugar ng Kontribusyon

Tingnan ang `etc/CONTRIBUTING.md` para sa kasalukuyang pangangailangan:
- Mga seksyon ng Deep Reinforcement Learning
- Mga pagpapabuti sa Object Detection
- Mga halimbawa ng Named Entity Recognition
- Mga sample ng custom embedding training

## Konfigurasyon ng Kapaligiran

### Mga Kinakailangang Dependency

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

### Mga Variable ng Kapaligiran

Walang espesyal na mga variable ng kapaligiran na kinakailangan para sa pangunahing paggamit.

Para sa mga deployment sa Azure (quiz app):
- `AZURE_STATIC_WEB_APPS_API_TOKEN` (awtomatikong itinakda ng Azure)

## Debugging at Pag-troubleshoot

### Karaniwang Mga Isyu

**Isyu:** Nabigo ang paglikha ng conda environment
- **Solusyon:** I-update muna ang conda: `conda update conda -y`
- Tiyakin ang sapat na disk space (inirerekomenda ang 50GB)

**Isyu:** Hindi natagpuan ang Jupyter kernel
- **Solusyon:** 
  ```bash
  conda activate ai4beg
  python -m ipykernel install --user --name ai4beg
  ```

**Isyu:** Hindi natukoy ang GPU sa mga notebook
- **Solusyon:** 
  - I-verify ang CUDA installation: `nvidia-smi`
  - Suriin ang PyTorch GPU: `python -c "import torch; print(torch.cuda.is_available())"`
  - Suriin ang TensorFlow GPU: `python -c "import tensorflow as tf; print(tf.config.list_physical_devices('GPU'))"`

**Isyu:** Hindi magsimula ang quiz app
- **Solusyon:**
  ```bash
  cd etc/quiz-app
  rm -rf node_modules package-lock.json
  npm install
  npm run serve
  ```

**Isyu:** Nag-timeout ang Binder o hinaharangan ang mga pag-download
- **Solusyon:** Gumamit ng GitHub Codespaces o lokal na setup para sa mas mahusay na access sa resources

### Mga Isyu sa Memorya

Ang ilang mga leksyon ay nangangailangan ng malaking RAM (inirerekomenda ang 8GB+):
- Gumamit ng cloud VMs para sa mga leksyon na nangangailangan ng maraming resources
- Isara ang ibang mga application kapag nagte-train ng mga modelo
- Bawasan ang batch sizes sa mga notebook kung nauubusan ng memorya

## Karagdagang Tala

### Para sa mga Instruktor ng Kurso

- Tingnan ang `lessons/0-course-setup/for-teachers.md` para sa gabay sa pagtuturo
- Ang mga leksyon ay self-contained at maaaring ituro nang sunud-sunod o piliin nang paisa-isa
- Tinatayang oras: 12 linggo sa 2 leksyon bawat linggo

### Mga Resource sa Cloud

- **Azure for Students:** Libreng credits na magagamit para sa mga estudyante
- **Microsoft Learn:** Mga supplementary learning path na naka-link sa buong kurso
- **Binder:** Libre ngunit may limitadong resources at ilang restriksyon sa network

### Mga Opsyon sa Pagpapatakbo ng Code

1. **Lokal (Inirerekomenda):** Buong kontrol, pinakamahusay na performance, suporta sa GPU
2. **GitHub Codespaces:** Cloud-based na VS Code, maganda para sa mabilisang access
3. **Binder:** Jupyter na nakabase sa browser, libre ngunit limitado
4. **Azure ML Notebooks:** Enterprise na opsyon na may suporta sa GPU
5. **Google Colab:** I-upload ang mga notebook nang paisa-isa, may libreng GPU tier na magagamit

### Paggamit ng Notebooks

- Ang mga notebook ay idinisenyo upang patakbuhin nang cell-by-cell para sa pag-aaral
- Maraming notebook ang nagda-download ng datasets sa unang run (maaaring tumagal ng oras)
- Ang ilang mga modelo ay nangangailangan ng GPU para sa makatwirang oras ng training
- Ang mga pre-trained na modelo ay ginagamit hangga't maaari upang mabawasan ang compute requirements

### Mga Pagsasaalang-alang sa Performance

- Ang mga huling leksyon sa computer vision (CNNs, GANs) ay nakikinabang sa GPU
- Ang mga leksyon sa NLP transformer ay maaaring mangailangan ng malaking RAM
- Ang pagte-train mula sa simula ay pang-edukasyon ngunit matagal
- Ang mga halimbawa ng transfer learning ay nagpapababa ng oras ng training

---

**Paunawa**:  
Ang dokumentong ito ay isinalin gamit ang AI translation service na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagama't sinisikap naming maging tumpak, pakitandaan na ang mga awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o hindi pagkakatugma. Ang orihinal na dokumento sa orihinal nitong wika ang dapat ituring na opisyal na sanggunian. Para sa mahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot para sa anumang hindi pagkakaunawaan o maling interpretasyon na maaaring magmula sa paggamit ng pagsasaling ito.