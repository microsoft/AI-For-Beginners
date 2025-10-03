# AGENTS.md

## Project Overview

AI for Beginners is a comprehensive 12-week, 24-lesson curriculum covering Artificial Intelligence fundamentals. This educational repository includes practical lessons using Jupyter Notebooks, quizzes, and hands-on labs. The curriculum covers:

- Symbolic AI with Knowledge Representation and Expert Systems
- Neural Networks and Deep Learning with TensorFlow and PyTorch
- Computer Vision techniques and architectures
- Natural Language Processing (NLP) including transformers and BERT
- Specialized topics: Genetic Algorithms, Reinforcement Learning, Multi-Agent Systems
- AI Ethics and Responsible AI principles

**Key Technologies:** Python 3, Jupyter Notebooks, TensorFlow, PyTorch, Keras, OpenCV, Vue.js (for quiz app)

**Architecture:** Educational content repository with Jupyter Notebooks organized by topic areas, supplemented by a Vue.js-based quiz application and extensive multi-language support.

## Setup Commands

### Primary Development Environment (Python/Jupyter)

The curriculum is designed to run with Python and Jupyter Notebooks. The recommended approach is using miniconda:

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

The quiz app is a separate Vue.js application located in `etc/quiz-app/`:

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
   - Navigate to lesson folders and open `.ipynb` files
   - Run cells interactively to follow lessons

2. **VS Code with Python Extension:**
   - Open repository in VS Code
   - Install Python extension
   - VS Code automatically detects and uses the conda environment
   - Open `.ipynb` files directly in VS Code

3. **Cloud Development:**
   - **GitHub Codespaces:** Click "Code" → "Codespaces" → "Create codespace on main"
   - **Binder:** Use the Binder badge on README to launch in browser
   - Note: Binder has limited resources and some web access restrictions

### GPU Support for Advanced Lessons

Later lessons benefit significantly from GPU acceleration:

- **Azure Data Science VM:** Use NC-series VMs with GPU support
- **Azure Machine Learning:** Use notebook features with GPU compute
- **Google Colab:** Upload notebooks individually (has free GPU support)

### Quiz App Development

```bash
cd etc/quiz-app
npm run serve  # Hot-reload development server at http://localhost:8080
```

## Testing Instructions

This is an educational repository focused on learning content rather than software testing. There is no traditional test suite.

### Validation Approaches:

1. **Jupyter Notebooks:** Execute cells sequentially to verify code examples work
2. **Quiz App Testing:** Manual testing via development server
3. **Translation Validation:** Check translated content in `translations/` folder
4. **Quiz App Linting:** `npm run lint` in `etc/quiz-app/`

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

- Standard Python conventions for educational code
- Clear, readable code prioritizing learning over optimization
- Comments explaining key concepts
- Jupyter Notebook-friendly: cells should be self-contained where possible
- No strict linting requirements for lesson content

### JavaScript/Vue.js (Quiz App)

- ESLint configuration in `etc/quiz-app/package.json`
- Run `npm run lint` to check and auto-fix issues
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

No build process required - Jupyter Notebooks are executed directly.

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

The repository uses Docsify for documentation:
- `index.html` serves as entry point
- No build required - served directly via GitHub Pages
- Access at: https://microsoft.github.io/AI-For-Beginners/

## Contributing Guidelines

### Pull Request Process

1. **Title Format:** Clear, descriptive titles describing the change
2. **CLA Requirement:** Microsoft CLA must be signed (automated check)
3. **Content Guidelines:**
   - Maintain educational focus and beginner-friendly approach
   - Test all code examples in notebooks
   - Ensure notebooks run end-to-end
   - Update translations if modifying English content
4. **Quiz App Changes:** Run `npm run lint` before committing

### Translation Contributions

- Translations are automated via GitHub Actions using co-op-translator
- Manual translations go in `translations/<language-code>/`
- Quiz translations in `etc/quiz-app/src/assets/translations/`
- Supported languages: 40+ languages (see README for full list)

### Active Contribution Areas

See `etc/CONTRIBUTING.md` for current needs:
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

No special environment variables required for basic usage.

For Azure deployments (quiz app):
- `AZURE_STATIC_WEB_APPS_API_TOKEN` (set automatically by Azure)

## Debugging and Troubleshooting

### Common Issues

**Issue:** Conda environment creation fails
- **Solution:** Update conda first: `conda update conda -y`
- Ensure sufficient disk space (50GB recommended)

**Issue:** Jupyter kernel not found
- **Solution:** 
  ```bash
  conda activate ai4beg
  python -m ipykernel install --user --name ai4beg
  ```

**Issue:** GPU not detected in notebooks
- **Solution:** 
  - Verify CUDA installation: `nvidia-smi`
  - Check PyTorch GPU: `python -c "import torch; print(torch.cuda.is_available())"`
  - Check TensorFlow GPU: `python -c "import tensorflow as tf; print(tf.config.list_physical_devices('GPU'))"`

**Issue:** Quiz app won't start
- **Solution:**
  ```bash
  cd etc/quiz-app
  rm -rf node_modules package-lock.json
  npm install
  npm run serve
  ```

**Issue:** Binder times out or blocks downloads
- **Solution:** Use GitHub Codespaces or local setup for better resource access

### Memory Issues

Some lessons require significant RAM (8GB+ recommended):
- Use cloud VMs for resource-intensive lessons
- Close other applications when training models
- Reduce batch sizes in notebooks if running out of memory

## Additional Notes

### For Course Instructors

- See `lessons/0-course-setup/for-teachers.md` for teaching guidance
- Lessons are self-contained and can be taught in sequence or selected individually
- Estimated time: 12 weeks at 2 lessons per week

### Cloud Resources

- **Azure for Students:** Free credits available for students
- **Microsoft Learn:** Supplementary learning paths linked throughout
- **Binder:** Free but limited resources and some network restrictions

### Code Execution Options

1. **Local (Recommended):** Full control, best performance, GPU support
2. **GitHub Codespaces:** Cloud-based VS Code, good for quick access
3. **Binder:** Browser-based Jupyter, free but limited
4. **Azure ML Notebooks:** Enterprise option with GPU support
5. **Google Colab:** Upload notebooks individually, free GPU tier available

### Working with Notebooks

- Notebooks are designed to be run cell-by-cell for learning
- Many notebooks download datasets on first run (may take time)
- Some models require GPU for reasonable training times
- Pre-trained models are used where possible to reduce compute requirements

### Performance Considerations

- Later computer vision lessons (CNNs, GANs) benefit from GPU
- NLP transformer lessons may require significant RAM
- Training from scratch is educational but time-consuming
- Transfer learning examples minimize training time
