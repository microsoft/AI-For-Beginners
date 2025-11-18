<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "6b11a37115944252ab3ed04e358d830d",
  "translation_date": "2025-11-18T18:10:01+00:00",
  "source_file": "AGENTS.md",
  "language_code": "pcm"
}
-->
# AGENTS.md

## Project Overview

AI for Beginners na 12-week, 24-lesson curriculum wey dey teach Artificial Intelligence basics. Dis repository get practical lessons wey dey use Jupyter Notebooks, quizzes, and hands-on labs. Wetin e cover na:

- Symbolic AI wey include Knowledge Representation and Expert Systems
- Neural Networks and Deep Learning wey dey use TensorFlow and PyTorch
- Computer Vision techniques and architectures
- Natural Language Processing (NLP) wey include transformers and BERT
- Special topics: Genetic Algorithms, Reinforcement Learning, Multi-Agent Systems
- AI Ethics and Responsible AI principles

**Key Technologies:** Python 3, Jupyter Notebooks, TensorFlow, PyTorch, Keras, OpenCV, Vue.js (for quiz app)

**Architecture:** Educational content repository wey Jupyter Notebooks dey arrange by topic areas, plus Vue.js-based quiz app and multi-language support.

## Setup Commands

### Primary Development Environment (Python/Jupyter)

Dis curriculum dey work with Python and Jupyter Notebooks. E better make you use miniconda:

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

### Alternative: Using devcontainer

```bash
# Open in VS Code and select "Reopen in Container" when prompted
# The devcontainer will automatically set up the environment
```

### Quiz Application Setup

Quiz app na Vue.js application wey dey inside `etc/quiz-app/`:

```bash
cd etc/quiz-app
npm install
npm run serve  # Development server
npm run build  # Production build
npm run lint   # Lint and fix files
```

## Development Workflow

### Working with Jupyter Notebooks

1. **Local Development:**
   - Activate conda environment: `conda activate ai4beg`
   - Start Jupyter: `jupyter notebook` or `jupyter lab`
   - Go lesson folders and open `.ipynb` files
   - Run cells one by one to follow lessons

2. **VS Code with Python Extension:**
   - Open repository for VS Code
   - Install Python extension
   - VS Code go detect and use conda environment automatically
   - Open `.ipynb` files directly for VS Code

3. **Cloud Development:**
   - **GitHub Codespaces:** Click "Code" → "Codespaces" → "Create codespace on main"
   - **Binder:** Use Binder badge for README to launch for browser
   - Note: Binder get limited resources and some web access restrictions

### GPU Support for Advanced Lessons

Later lessons go benefit well from GPU acceleration:

- **Azure Data Science VM:** Use NC-series VMs wey get GPU support
- **Azure Machine Learning:** Use notebook features with GPU compute
- **Google Colab:** Upload notebooks one by one (e get free GPU support)

### Quiz App Development

```bash
cd etc/quiz-app
npm run serve  # Hot-reload development server at http://localhost:8080
```

## Testing Instructions

Dis repository na for learning content, e no be software testing. E no get traditional test suite.

### Validation Approaches:

1. **Jupyter Notebooks:** Run cells one by one to confirm say code examples dey work
2. **Quiz App Testing:** Test am manually with development server
3. **Translation Validation:** Check translated content for `translations/` folder
4. **Quiz App Linting:** `npm run lint` for `etc/quiz-app/`

### Running Code Examples:

```bash
# Activate environment first
conda activate ai4beg

# Run Python scripts directly
python lessons/4-ComputerVision/07-ConvNets/pytorchcv.py

# Or execute notebooks
jupyter notebook lessons/3-NeuralNetworks/03-Perceptron/Perceptron.ipynb
```

## Code Style

### Python Code Style

- Follow standard Python conventions for educational code
- Write code wey dey clear and easy to understand, no need for optimization
- Add comments wey dey explain key concepts
- Make Jupyter Notebook-friendly: cells suppose dey self-contained as much as possible
- No strict linting requirements for lesson content

### JavaScript/Vue.js (Quiz App)

- ESLint configuration dey for `etc/quiz-app/package.json`
- Run `npm run lint` to check and fix issues automatically
- Vue 2.x conventions
- Component-based architecture

### File Organization

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

## Build and Deployment

### Jupyter Content

No need build process - Jupyter Notebooks dey run directly.

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

### Documentation Site

Dis repository dey use Docsify for documentation:
- `index.html` na entry point
- No need build - e dey serve directly via GitHub Pages
- Access am for: https://microsoft.github.io/AI-For-Beginners/

## Contributing Guidelines

### Pull Request Process

1. **Title Format:** Use clear, descriptive titles wey explain wetin you change
2. **CLA Requirement:** Microsoft CLA must dey signed (automated check)
3. **Content Guidelines:**
   - Keep am educational and beginner-friendly
   - Test all code examples for notebooks
   - Make sure notebooks dey run from start to finish
   - Update translations if you change English content
4. **Quiz App Changes:** Run `npm run lint` before you commit

### Translation Contributions

- Translations dey automated via GitHub Actions wey dey use co-op-translator
- Manual translations dey go `translations/<language-code>/`
- Quiz translations dey for `etc/quiz-app/src/assets/translations/`
- Supported languages: 40+ languages (check README for full list)

### Active Contribution Areas

Check `etc/CONTRIBUTING.md` for current needs:
- Deep Reinforcement Learning sections
- Object Detection improvements
- Named Entity Recognition examples
- Custom embedding training samples

## Environment Configuration

### Required Dependencies

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

### Environment Variables

No special environment variables dey required for basic usage.

For Azure deployments (quiz app):
- `AZURE_STATIC_WEB_APPS_API_TOKEN` (Azure go set am automatically)

## Debugging and Troubleshooting

### Common Issues

**Issue:** Conda environment creation no work
- **Solution:** Update conda first: `conda update conda -y`
- Make sure say you get enough disk space (50GB recommended)

**Issue:** Jupyter kernel no dey
- **Solution:** 
  ```bash
  conda activate ai4beg
  python -m ipykernel install --user --name ai4beg
  ```

**Issue:** GPU no dey show for notebooks
- **Solution:** 
  - Check CUDA installation: `nvidia-smi`
  - Check PyTorch GPU: `python -c "import torch; print(torch.cuda.is_available())"`
  - Check TensorFlow GPU: `python -c "import tensorflow as tf; print(tf.config.list_physical_devices('GPU'))"`

**Issue:** Quiz app no dey start
- **Solution:**
  ```bash
  cd etc/quiz-app
  rm -rf node_modules package-lock.json
  npm install
  npm run serve
  ```

**Issue:** Binder dey timeout or block downloads
- **Solution:** Use GitHub Codespaces or local setup for better resources

### Memory Issues

Some lessons dey need plenty RAM (8GB+ recommended):
- Use cloud VMs for lessons wey dey need plenty resources
- Close other apps when you dey train models
- Reduce batch sizes for notebooks if memory dey finish

## Additional Notes

### For Course Instructors

- Check `lessons/0-course-setup/for-teachers.md` for teaching guidance
- Lessons dey self-contained and you fit teach am one by one or follow sequence
- Estimated time: 12 weeks at 2 lessons per week

### Cloud Resources

- **Azure for Students:** Free credits dey available for students
- **Microsoft Learn:** Supplementary learning paths dey linked throughout
- **Binder:** Free but e get limited resources and some network restrictions

### Code Execution Options

1. **Local (Recommended):** Full control, best performance, GPU support
2. **GitHub Codespaces:** Cloud-based VS Code, good for quick access
3. **Binder:** Browser-based Jupyter, free but limited
4. **Azure ML Notebooks:** Enterprise option with GPU support
5. **Google Colab:** Upload notebooks one by one, free GPU tier dey available

### Working with Notebooks

- Notebooks dey designed to run cell-by-cell for learning
- Many notebooks dey download datasets for first run (e fit take time)
- Some models dey need GPU for better training time
- Pre-trained models dey use where e dey possible to reduce compute requirements

### Performance Considerations

- Later computer vision lessons (CNNs, GANs) go benefit from GPU
- NLP transformer lessons fit need plenty RAM
- Training from scratch dey educational but e dey take time
- Transfer learning examples dey reduce training time

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:  
Dis docu don dey translate wit AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). Even though we dey try make am accurate, abeg sabi say automatic translation fit get mistake or no correct well. Di original docu for di native language na di main correct source. For important information, e better make una use professional human translation. We no go fit take blame for any misunderstanding or wrong interpretation wey fit happen because of dis translation.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->