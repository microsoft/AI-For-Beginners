# AGENTS.md

## ਪ੍ਰੋਜੈਕਟ ਝਲਕ

AI for Beginners ਇੱਕ ਵਿਸਤ੍ਰਿਤ 12-ਹਫ਼ਤੇ, 24-ਪਾਠਾਂ ਵਾਲਾ ਕੋਰਸ ਹੈ ਜੋ Artificial Intelligence ਦੇ ਮੁੱਢਲੇ ਸਿਧਾਂਤਾਂ ਨੂੰ ਕਵਰ ਕਰਦਾ ਹੈ। ਇਹ ਸਿੱਖਿਆਵਾਂ ਲਈ ਬਣਾਇਆ ਗਿਆ ਰਿਪੋਜ਼ਟਰੀ Jupyter Notebooks, ਕਵਿਜ਼, ਅਤੇ ਹੱਥ-ਅਨੁਭਵ ਲੈਬਾਂ ਦੇ ਨਾਲ ਅਭਿਆਸਕ ਪਾਠਾਂ ਸ਼ਾਮਲ ਕਰਦਾ ਹੈ। ਕੋਰਸ ਵਿੱਚ ਇਹ ਸ਼ਾਮਲ ਹੈ:

- Symbolic AI ਨਾਲ Knowledge Representation ਅਤੇ Expert Systems
- Neural Networks ਅਤੇ Deep Learning (TensorFlow ਅਤੇ PyTorch ਦੇ ਨਾਲ)
- Computer Vision ਤਕਨੀਕਾਂ ਅਤੇ ਆਰਕੀਟੈਕਚਰ
- Natural Language Processing (NLP) ਜਿਸ ਵਿੱਚ transformers ਅਤੇ BERT ਸ਼ਾਮਲ ਹਨ
- ਵਿਸ਼ੇਸ਼ ਵਿਸ਼ੇ: Genetic Algorithms, Reinforcement Learning, Multi-Agent Systems
- AI Ethics ਅਤੇ Responsible AI ਦੇ ਸਿਧਾਂਤ

**ਮੁੱਖ ਤਕਨੀਕਾਂ:** Python 3, Jupyter Notebooks, TensorFlow, PyTorch, Keras, OpenCV, Vue.js (ਕਵਿਜ਼ ਐਪ ਲਈ)

**ਆਰਕੀਟੈਕਚਰ:** ਸਿੱਖਿਆਵਾਂ ਲਈ ਸਮੱਗਰੀ ਰਿਪੋਜ਼ਟਰੀ ਜੋ Jupyter Notebooks ਨੂੰ ਵਿਸ਼ੇਸ਼ ਖੇਤਰਾਂ ਵਿੱਚ ਵਿਵਸਥਿਤ ਕਰਦਾ ਹੈ, Vue.js-ਅਧਾਰਿਤ ਕਵਿਜ਼ ਐਪ ਅਤੇ ਬਹੁ-ਭਾਸ਼ਾ ਸਹਾਇਤਾ ਦੇ ਨਾਲ।

## ਸੈਟਅਪ ਕਮਾਂਡ

### ਮੁੱਖ ਵਿਕਾਸ ਵਾਤਾਵਰਣ (Python/Jupyter)

ਕੋਰਸ Python ਅਤੇ Jupyter Notebooks ਦੇ ਨਾਲ ਚਲਾਉਣ ਲਈ ਡਿਜ਼ਾਈਨ ਕੀਤਾ ਗਿਆ ਹੈ। ਸਿਫਾਰਸ਼ੀ ਤਰੀਕਾ ਹੈ miniconda ਦੀ ਵਰਤੋਂ:

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

### ਵਿਕਲਪ: devcontainer ਦੀ ਵਰਤੋਂ

```bash
# Open in VS Code and select "Reopen in Container" when prompted
# The devcontainer will automatically set up the environment
```

### ਕਵਿਜ਼ ਐਪ ਸੈਟਅਪ

ਕਵਿਜ਼ ਐਪ ਇੱਕ ਵੱਖਰਾ Vue.js ਐਪਲੀਕੇਸ਼ਨ ਹੈ ਜੋ `etc/quiz-app/` ਵਿੱਚ ਸਥਿਤ ਹੈ:

```bash
cd etc/quiz-app
npm install
npm run serve  # Development server
npm run build  # Production build
npm run lint   # Lint and fix files
```

## ਵਿਕਾਸ ਵਰਕਫਲੋ

### Jupyter Notebooks ਨਾਲ ਕੰਮ ਕਰਨਾ

1. **ਲੋਕਲ ਵਿਕਾਸ:**
   - conda environment ਨੂੰ ਐਕਟੀਵੇਟ ਕਰੋ: `conda activate ai4beg`
   - Jupyter ਸ਼ੁਰੂ ਕਰੋ: `jupyter notebook` ਜਾਂ `jupyter lab`
   - ਪਾਠਾਂ ਦੇ ਫੋਲਡਰਾਂ ਵਿੱਚ ਜਾਓ ਅਤੇ `.ipynb` ਫਾਈਲਾਂ ਖੋਲ੍ਹੋ
   - ਪਾਠਾਂ ਦੀ ਪਾਲਣਾ ਕਰਨ ਲਈ ਸੈਲਾਂ ਇੰਟਰੈਕਟਿਵ ਤਰੀਕੇ ਨਾਲ ਚਲਾਓ

2. **VS Code ਨਾਲ Python Extension:**
   - ਰਿਪੋਜ਼ਟਰੀ ਨੂੰ VS Code ਵਿੱਚ ਖੋਲ੍ਹੋ
   - Python extension ਇੰਸਟਾਲ ਕਰੋ
   - VS Code ਆਪਣੇ ਆਪ conda environment ਨੂੰ ਪਛਾਣਦਾ ਹੈ ਅਤੇ ਵਰਤਦਾ ਹੈ
   - `.ipynb` ਫਾਈਲਾਂ ਨੂੰ ਸਿੱਧੇ VS Code ਵਿੱਚ ਖੋਲ੍ਹੋ

3. **ਕਲਾਉਡ ਵਿਕਾਸ:**
   - **GitHub Codespaces:** "Code" → "Codespaces" → "Create codespace on main" 'ਤੇ ਕਲਿੱਕ ਕਰੋ
   - **Binder:** README 'ਤੇ Binder badge ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਬ੍ਰਾਊਜ਼ਰ ਵਿੱਚ ਲਾਂਚ ਕਰੋ
   - ਨੋਟ: Binder ਵਿੱਚ ਸੀਮਿਤ ਸਰੋਤ ਹਨ ਅਤੇ ਕੁਝ ਵੈੱਬ ਐਕਸੈਸ ਰੋਕਾਵਟਾਂ ਹਨ

### GPU ਸਹਾਇਤਾ ਉੱਚ ਪਾਠਾਂ ਲਈ

ਅਗਲੇ ਪਾਠ GPU acceleration ਤੋਂ ਕਾਫ਼ੀ ਲਾਭ ਪ੍ਰਾਪਤ ਕਰਦੇ ਹਨ:

- **Azure Data Science VM:** GPU ਸਹਾਇਤਾ ਵਾਲੇ NC-series VMs ਦੀ ਵਰਤੋਂ ਕਰੋ
- **Azure Machine Learning:** GPU compute ਦੇ ਨਾਲ notebook ਫੀਚਰਾਂ ਦੀ ਵਰਤੋਂ ਕਰੋ
- **Google Colab:** ਨੋਟਬੁੱਕਾਂ ਨੂੰ ਵੱਖ-ਵੱਖ ਅਪਲੋਡ ਕਰੋ (ਮੁਫ਼ਤ GPU ਸਹਾਇਤਾ ਹੈ)

### ਕਵਿਜ਼ ਐਪ ਵਿਕਾਸ

```bash
cd etc/quiz-app
npm run serve  # Hot-reload development server at http://localhost:8080
```

## ਟੈਸਟਿੰਗ ਹਦਾਇਤਾਂ

ਇਹ ਸਿੱਖਿਆਵਾਂ ਲਈ ਬਣਾਇਆ ਗਿਆ ਰਿਪੋਜ਼ਟਰੀ ਹੈ ਜੋ ਸਿੱਖਣ ਦੀ ਸਮੱਗਰੀ 'ਤੇ ਧਿਆਨ ਕੇਂਦਰਿਤ ਕਰਦਾ ਹੈ, ਨਾ ਕਿ ਸਾਫਟਵੇਅਰ ਟੈਸਟਿੰਗ 'ਤੇ। ਇੱਥੇ ਕੋਈ ਰਵਾਇਤੀ ਟੈਸਟ ਸੂਟ ਨਹੀਂ ਹੈ।

### ਵੈਧਤਾ ਦੇ ਤਰੀਕੇ:

1. **Jupyter Notebooks:** ਕੋਡ ਉਦਾਹਰਣਾਂ ਨੂੰ ਚਲਾਉਣ ਲਈ ਸੈਲਾਂ ਨੂੰ ਲਗਾਤਾਰ ਚਲਾਓ
2. **ਕਵਿਜ਼ ਐਪ ਟੈਸਟਿੰਗ:** ਵਿਕਾਸ ਸਰਵਰ ਰਾਹੀਂ ਹੱਥ-ਅਨੁਭਵ ਟੈਸਟਿੰਗ
3. **ਅਨੁਵਾਦ ਵੈਧਤਾ:** `translations/` ਫੋਲਡਰ ਵਿੱਚ ਅਨੁਵਾਦ ਕੀਤੀ ਸਮੱਗਰੀ ਦੀ ਜਾਂਚ ਕਰੋ
4. **ਕਵਿਜ਼ ਐਪ ਲਿੰਟਿੰਗ:** `npm run lint` `etc/quiz-app/` ਵਿੱਚ ਚਲਾਓ

### ਕੋਡ ਉਦਾਹਰਣ ਚਲਾਉਣਾ:

```bash
# Activate environment first
conda activate ai4beg

# Run Python scripts directly
python lessons/4-ComputerVision/07-ConvNets/pytorchcv.py

# Or execute notebooks
jupyter notebook lessons/3-NeuralNetworks/03-Perceptron/Perceptron.ipynb
```

## ਕੋਡ ਸਟਾਈਲ

### Python ਕੋਡ ਸਟਾਈਲ

- ਸਿੱਖਿਆਵਾਂ ਲਈ ਸਟੈਂਡਰਡ Python ਰਵਾਇਤਾਂ
- ਸਿੱਖਣ ਨੂੰ ਤਰਜੀਹ ਦੇਣ ਵਾਲਾ ਸਪਸ਼ਟ ਅਤੇ ਪੜ੍ਹਨਯੋਗ ਕੋਡ
- ਮੁੱਖ ਧਾਰਨਾਵਾਂ ਨੂੰ ਸਮਝਾਉਣ ਵਾਲੇ ਟਿੱਪਣੀਆਂ
- Jupyter Notebook-ਅਨੁਕੂਲ: ਸੈਲਾਂ ਜਿੱਥੇ ਸੰਭਵ ਹੋਵੇ, ਸਵੈ-ਨਿਰਭਰ ਹੋਣੇ ਚਾਹੀਦੇ ਹਨ
- ਪਾਠ ਸਮੱਗਰੀ ਲਈ ਕੋਈ ਸਖ਼ਤ ਲਿੰਟਿੰਗ ਦੀ ਲੋੜ ਨਹੀਂ

### JavaScript/Vue.js (ਕਵਿਜ਼ ਐਪ)

- `etc/quiz-app/package.json` ਵਿੱਚ ESLint ਸੰਰਚਨਾ
- ਮੁੱਦਿਆਂ ਦੀ ਜਾਂਚ ਅਤੇ ਆਟੋ-ਫਿਕਸ ਕਰਨ ਲਈ `npm run lint` ਚਲਾਓ
- Vue 2.x ਰਵਾਇਤਾਂ
- ਕੰਪੋਨੈਂਟ-ਅਧਾਰਿਤ ਆਰਕੀਟੈਕਚਰ

### ਫਾਈਲ ਸੰਗਠਨ

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

## ਬਿਲਡ ਅਤੇ ਡਿਪਲੌਇਮੈਂਟ

### Jupyter ਸਮੱਗਰੀ

ਕੋਈ ਬਿਲਡ ਪ੍ਰਕਿਰਿਆ ਦੀ ਲੋੜ ਨਹੀਂ - Jupyter Notebooks ਨੂੰ ਸਿੱਧੇ ਚਲਾਇਆ ਜਾਂਦਾ ਹੈ।

### ਕਵਿਜ਼ ਐਪਲੀਕੇਸ਼ਨ

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

### ਦਸਤਾਵੇਜ਼ ਸਾਈਟ

ਰਿਪੋਜ਼ਟਰੀ Docsify ਦੀ ਵਰਤੋਂ ਕਰਦਾ ਹੈ ਦਸਤਾਵੇਜ਼ ਲਈ:
- `index.html` ਪ੍ਰਵੇਸ਼ ਬਿੰਦੂ ਵਜੋਂ ਕੰਮ ਕਰਦਾ ਹੈ
- ਕੋਈ ਬਿਲਡ ਦੀ ਲੋੜ ਨਹੀਂ - ਸਿੱਧੇ GitHub Pages ਰਾਹੀਂ ਸਰਵ ਕੀਤਾ ਜਾਂਦਾ ਹੈ
- ਪਹੁੰਚ ਕਰੋ: https://microsoft.github.io/AI-For-Beginners/

## ਯੋਗਦਾਨ ਦੇ ਨਿਯਮ

### ਪੁਲ ਰਿਕਵੇਸਟ ਪ੍ਰਕਿਰਿਆ

1. **ਸਿਰਲੇਖ ਫਾਰਮੈਟ:** ਸਪਸ਼ਟ, ਵਰਣਨਾਤਮਕ ਸਿਰਲੇਖ ਜੋ ਬਦਲਾਅ ਨੂੰ ਦਰਸਾਉਂਦੇ ਹਨ
2. **CLA ਲੋੜ:** Microsoft CLA ਸਾਈਨ ਹੋਣਾ ਚਾਹੀਦਾ ਹੈ (ਆਟੋਮੈਟਿਕ ਜਾਂਚ)
3. **ਸਮੱਗਰੀ ਨਿਯਮ:**
   - ਸਿੱਖਿਆਵਾਂ 'ਤੇ ਧਿਆਨ ਕੇਂਦਰਿਤ ਅਤੇ ਸ਼ੁਰੂਆਤੀ-ਅਨੁਕੂਲ ਦ੍ਰਿਸ਼ਟੀਕੋਣ
   - ਨੋਟਬੁੱਕਾਂ ਵਿੱਚ ਸਾਰੇ ਕੋਡ ਉਦਾਹਰਣਾਂ ਦੀ ਜਾਂਚ ਕਰੋ
   - ਯਕੀਨੀ ਬਣਾਓ ਕਿ ਨੋਟਬੁੱਕਾਂ ਅੰਤ-ਤੱਕ ਚਲਦੀਆਂ ਹਨ
   - ਜੇਕਰ ਅੰਗਰੇਜ਼ੀ ਸਮੱਗਰੀ ਨੂੰ ਬਦਲਦੇ ਹੋ, ਤਾਂ ਅਨੁਵਾਦਾਂ ਨੂੰ ਅਪਡੇਟ ਕਰੋ
4. **ਕਵਿਜ਼ ਐਪ ਬਦਲਾਅ:** ਕਮਿਟ ਕਰਨ ਤੋਂ ਪਹਿਲਾਂ `npm run lint` ਚਲਾਓ

### ਅਨੁਵਾਦ ਯੋਗਦਾਨ

- ਅਨੁਵਾਦ GitHub Actions ਰਾਹੀਂ co-op-translator ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਆਟੋਮੈਟਿਕ ਹਨ
- ਹੱਥ-ਅਨੁਵਾਦ `translations/<language-code>/` ਵਿੱਚ ਜਾਂਦੇ ਹਨ
- ਕਵਿਜ਼ ਅਨੁਵਾਦ `etc/quiz-app/src/assets/translations/` ਵਿੱਚ
- ਸਹਾਇਤਾਪ੍ਰਾਪਤ ਭਾਸ਼ਾਵਾਂ: 40+ ਭਾਸ਼ਾਵਾਂ (ਪੂਰੀ ਸੂਚੀ ਲਈ README ਵੇਖੋ)

### ਸਰਗਰਮ ਯੋਗਦਾਨ ਖੇਤਰ

ਮੌਜੂਦਾ ਲੋੜਾਂ ਲਈ `etc/CONTRIBUTING.md` ਵੇਖੋ:
- Deep Reinforcement Learning ਸੈਕਸ਼ਨ
- Object Detection ਸੁਧਾਰ
- Named Entity Recognition ਉਦਾਹਰਣ
- Custom embedding training samples

## ਵਾਤਾਵਰਣ ਸੰਰਚਨਾ

### ਲੋੜੀਂਦੇ Dependencies

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

### ਵਾਤਾਵਰਣ ਵੈਰੀਏਬਲ

ਮੁੱਢਲੇ ਵਰਤੋਂ ਲਈ ਕੋਈ ਖਾਸ ਵਾਤਾਵਰਣ ਵੈਰੀਏਬਲ ਦੀ ਲੋੜ ਨਹੀਂ।

Azure ਡਿਪਲੌਇਮੈਂਟ ਲਈ (ਕਵਿਜ਼ ਐਪ):
- `AZURE_STATIC_WEB_APPS_API_TOKEN` (Azure ਦੁਆਰਾ ਆਪਣੇ ਆਪ ਸੈਟ ਕੀਤਾ ਜਾਂਦਾ ਹੈ)

## ਡਿਬੱਗਿੰਗ ਅਤੇ ਸਮੱਸਿਆ ਹੱਲ

### ਆਮ ਸਮੱਸਿਆਵਾਂ

**ਸਮੱਸਿਆ:** Conda environment ਬਣਾਉਣਾ ਫੇਲ੍ਹ ਹੋ ਜਾਂਦਾ ਹੈ
- **ਹੱਲ:** ਪਹਿਲਾਂ conda ਨੂੰ ਅਪਡੇਟ ਕਰੋ: `conda update conda -y`
- ਯਕੀਨੀ ਬਣਾਓ ਕਿ ਕਾਫ਼ੀ ਡਿਸਕ ਸਪੇਸ ਹੈ (50GB ਸਿਫਾਰਸ਼ੀ)

**ਸਮੱਸਿਆ:** Jupyter kernel ਨਹੀਂ ਮਿਲਦਾ
- **ਹੱਲ:** 
  ```bash
  conda activate ai4beg
  python -m ipykernel install --user --name ai4beg
  ```

**ਸਮੱਸਿਆ:** ਨੋਟਬੁੱਕਾਂ ਵਿੱਚ GPU ਨਹੀਂ ਮਿਲਦਾ
- **ਹੱਲ:** 
  - CUDA ਇੰਸਟਾਲੇਸ਼ਨ ਦੀ ਜਾਂਚ ਕਰੋ: `nvidia-smi`
  - PyTorch GPU ਦੀ ਜਾਂਚ ਕਰੋ: `python -c "import torch; print(torch.cuda.is_available())"`
  - TensorFlow GPU ਦੀ ਜਾਂਚ ਕਰੋ: `python -c "import tensorflow as tf; print(tf.config.list_physical_devices('GPU'))"`

**ਸਮੱਸਿਆ:** ਕਵਿਜ਼ ਐਪ ਸ਼ੁਰੂ ਨਹੀਂ ਹੁੰਦੀ
- **ਹੱਲ:**
  ```bash
  cd etc/quiz-app
  rm -rf node_modules package-lock.json
  npm install
  npm run serve
  ```

**ਸਮੱਸਿਆ:** Binder ਟਾਈਮ ਆਉਟ ਜਾਂ ਡਾਊਨਲੋਡ ਰੋਕਦਾ ਹੈ
- **ਹੱਲ:** ਵਧੀਆ ਸਰੋਤ ਪਹੁੰਚ ਲਈ GitHub Codespaces ਜਾਂ ਲੋਕਲ ਸੈਟਅਪ ਦੀ ਵਰਤੋਂ ਕਰੋ

### ਮੈਮੋਰੀ ਸਮੱਸਿਆਵਾਂ

ਕੁਝ ਪਾਠਾਂ ਲਈ ਕਾਫ਼ੀ RAM ਦੀ ਲੋੜ ਹੁੰਦੀ ਹੈ (8GB+ ਸਿਫਾਰਸ਼ੀ):
- ਸਰੋਤ-ਗਹਿਰੇ ਪਾਠਾਂ ਲਈ ਕਲਾਉਡ VMs ਦੀ ਵਰਤੋਂ ਕਰੋ
- ਮਾਡਲ ਟ੍ਰੇਨਿੰਗ ਦੌਰਾਨ ਹੋਰ ਐਪਲੀਕੇਸ਼ਨ ਬੰਦ ਕਰੋ
- ਜੇਕਰ ਮੈਮੋਰੀ ਖਤਮ ਹੋ ਰਹੀ ਹੈ, ਤਾਂ ਨੋਟਬੁੱਕਾਂ ਵਿੱਚ batch sizes ਘਟਾਓ

## ਵਾਧੂ ਨੋਟਸ

### ਕੋਰਸ ਅਧਿਆਪਕਾਂ ਲਈ

- ਸਿੱਖਾਉਣ ਲਈ ਹਦਾਇਤਾਂ ਲਈ `lessons/0-course-setup/for-teachers.md` ਵੇਖੋ
- ਪਾਠ ਸਵੈ-ਨਿਰਭਰ ਹਨ ਅਤੇ ਲਗਾਤਾਰ ਜਾਂ ਵੱਖ-ਵੱਖ ਚੁਣੇ ਜਾ ਸਕਦੇ ਹਨ
- ਅਨੁਮਾਨਿਤ ਸਮਾਂ: 12 ਹਫ਼ਤੇ ਵਿੱਚ 2 ਪਾਠ ਪ੍ਰਤੀ ਹਫ਼ਤਾ

### ਕਲਾਉਡ ਸਰੋਤ

- **Azure for Students:** ਵਿਦਿਆਰਥੀਆਂ ਲਈ ਮੁਫ਼ਤ ਕ੍ਰੈਡਿਟ ਉਪਲਬਧ
- **Microsoft Learn:** ਸਹਾਇਕ ਸਿੱਖਣ ਪਾਠਾਂ ਦੇ ਲਿੰਕ
- **Binder:** ਮੁਫ਼ਤ ਪਰ ਸੀਮਿਤ ਸਰੋਤ ਅਤੇ ਕੁਝ ਨੈੱਟਵਰਕ ਰੋਕਾਵਟਾਂ

### ਕੋਡ ਚਲਾਉਣ ਦੇ ਵਿਕਲਪ

1. **ਲੋਕਲ (ਸਿਫਾਰਸ਼ੀ):** ਪੂਰੀ ਨਿਯੰਤਰਣ, ਵਧੀਆ ਪ੍ਰਦਰਸ਼ਨ, GPU ਸਹਾਇਤਾ
2. **GitHub Codespaces:** ਕਲਾਉਡ-ਅਧਾਰਿਤ VS Code, ਤੇਜ਼ ਪਹੁੰਚ ਲਈ ਵਧੀਆ
3. **Binder:** ਬ੍ਰਾਊਜ਼ਰ-ਅਧਾਰਿਤ Jupyter, ਮੁਫ਼ਤ ਪਰ ਸੀਮਿਤ
4. **Azure ML Notebooks:** GPU ਸਹਾਇਤਾ ਵਾਲਾ ਇੰਟਰਪ੍ਰਾਈਜ਼ ਵਿਕਲਪ
5. **Google Colab:** ਨੋਟਬੁੱਕਾਂ ਨੂੰ ਵੱਖ-ਵੱਖ ਅਪਲੋਡ ਕਰੋ, ਮੁਫ਼ਤ GPU ਟੀਅਰ ਉਪਲਬਧ

### ਨੋਟਬੁੱਕਾਂ ਨਾਲ ਕੰਮ ਕਰਨਾ

- ਨੋਟਬੁੱਕ ਸਿੱਖਣ ਲਈ ਸੈਲ-ਦਰ-ਸੈਲ ਚਲਾਉਣ ਲਈ ਡਿਜ਼ਾਈਨ ਕੀਤੇ ਗਏ ਹਨ
- ਕਈ ਨੋਟਬੁੱਕ ਪਹਿਲੀ ਵਾਰ ਚਲਾਉਣ 'ਤੇ ਡਾਟਾਸੈਟ ਡਾਊਨਲੋਡ ਕਰਦੇ ਹਨ (ਸਮਾਂ ਲੱਗ ਸਕਦਾ ਹੈ)
- ਕੁਝ ਮਾਡਲ ਵਾਜਬ ਟ੍ਰੇਨਿੰਗ ਸਮਾਂ ਲਈ GPU ਦੀ ਲੋੜ ਕਰਦੇ ਹਨ
- ਪ੍ਰੀ-ਟ੍ਰੇਨਡ ਮਾਡਲ ਵਰਤੇ ਜਾਂਦੇ ਹਨ ਜਿੱਥੇ ਸੰਭਵ ਹੋਵੇ, ਗਣਨਾ ਦੀ ਲੋੜ ਘਟਾਉਣ ਲਈ

### ਪ੍ਰਦਰਸ਼ਨ ਦੇ ਵਿਚਾਰ

- ਅਗਲੇ computer vision ਪਾਠ (CNNs, GANs) GPU ਤੋਂ ਲਾਭ ਪ੍ਰਾਪਤ ਕਰਦੇ ਹਨ
- NLP transformer ਪਾਠ ਕਾਫ਼ੀ RAM ਦੀ ਲੋੜ ਕਰ ਸਕਦੇ ਹਨ
- ਸ਼ੁਰੂ ਤੋਂ ਟ੍ਰੇਨਿੰਗ ਸਿੱਖਣ ਲਈ ਲਾਭਦਾਇਕ ਹੈ ਪਰ ਸਮਾਂ-ਖਪਤ ਵਾਲੀ ਹੈ
- Transfer learning ਉਦਾਹਰਣ ਟ੍ਰੇਨਿੰਗ ਸਮਾਂ ਘਟਾਉਂਦੇ ਹਨ

---

**ਅਸਵੀਕਰਤੀ**:  
ਇਹ ਦਸਤਾਵੇਜ਼ AI ਅਨੁਵਾਦ ਸੇਵਾ [Co-op Translator](https://github.com/Azure/co-op-translator) ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਅਨੁਵਾਦ ਕੀਤਾ ਗਿਆ ਹੈ। ਜਦੋਂ ਕਿ ਅਸੀਂ ਸਹੀ ਹੋਣ ਦੀ ਕੋਸ਼ਿਸ਼ ਕਰਦੇ ਹਾਂ, ਕਿਰਪਾ ਕਰਕੇ ਧਿਆਨ ਦਿਓ ਕਿ ਸਵੈਚਾਲਿਤ ਅਨੁਵਾਦਾਂ ਵਿੱਚ ਗਲਤੀਆਂ ਜਾਂ ਅਸੁਚੀਤਤਾਵਾਂ ਹੋ ਸਕਦੀਆਂ ਹਨ। ਇਸ ਦੀ ਮੂਲ ਭਾਸ਼ਾ ਵਿੱਚ ਮੌਜੂਦ ਦਸਤਾਵੇਜ਼ ਨੂੰ ਅਧਿਕਾਰਤ ਸਰੋਤ ਮੰਨਿਆ ਜਾਣਾ ਚਾਹੀਦਾ ਹੈ। ਮਹੱਤਵਪੂਰਨ ਜਾਣਕਾਰੀ ਲਈ, ਪੇਸ਼ੇਵਰ ਮਨੁੱਖੀ ਅਨੁਵਾਦ ਦੀ ਸਿਫਾਰਸ਼ ਕੀਤੀ ਜਾਂਦੀ ਹੈ। ਇਸ ਅਨੁਵਾਦ ਦੀ ਵਰਤੋਂ ਤੋਂ ਪੈਦਾ ਹੋਣ ਵਾਲੇ ਕਿਸੇ ਵੀ ਗਲਤਫਹਿਮੀ ਜਾਂ ਗਲਤ ਵਿਆਖਿਆ ਲਈ ਅਸੀਂ ਜ਼ਿੰਮੇਵਾਰ ਨਹੀਂ ਹਾਂ।