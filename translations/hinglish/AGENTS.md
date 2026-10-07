# AGENTS.md

## Project Overview

AI for Beginners ek comprehensive 12-week, 24-lesson ka curriculum hai jo Artificial Intelligence ke fundamentals cover karta hai. Yeh educational repository Jupyter Notebooks, quizzes aur hands-on labs ke saath practical lessons deti hai. Curriculum mein yeh sab shamil hai:

- Symbolic AI, Knowledge Representation aur Expert Systems
- TensorFlow aur PyTorch ke saath Neural Networks aur Deep Learning
- Computer Vision techniques aur architectures
- Natural Language Processing (NLP), jisme transformers aur BERT bhi shamil hain
- Special topics: Genetic Algorithms, Reinforcement Learning, Multi-Agent Systems
- AI Ethics aur Responsible AI ke principles

**Main Technologies:** Python 3, Jupyter Notebooks, TensorFlow, PyTorch, Keras, OpenCV, Vue.js (quiz app ke liye)

**Architecture:** Educational content repository jisme Jupyter Notebooks topic areas ke hisaab se organize kiye gaye hain, saath mein ek Vue.js-based quiz application aur extensive multi-language support hai.

## Setup Commands

### Primary Development Environment (Python/Jupyter)

Curriculum ko Python aur Jupyter Notebooks ke saath chalane ke liye design kiya gaya hai. Recommended tareeka miniconda use karna hai:

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

### Alternative: devcontainer use karna

```bash
# Open in VS Code and select "Reopen in Container" when prompted
# The devcontainer will automatically set up the environment
```

### Quiz Application Setup

Quiz app ek alag Vue.js application hai jo `etc/quiz-app/` mein hai:

```bash
cd etc/quiz-app
npm install
npm run serve  # Development server
npm run build  # Production build
npm run lint   # Lint and fix files
```

## Development Workflow

### Jupyter Notebooks ke saath kaam karna

1. **Local Development:**
   - conda environment activate karein: `conda activate ai4beg`
   - Jupyter start karein: `jupyter notebook` ya `jupyter lab`
   - Lesson folders mein jaayein aur `.ipynb` files kholein
   - Lessons ko follow karne ke liye cells ko interactively run karein

2. **VS Code with Python Extension:**
   - Repository ko VS Code mein kholein
   - Python extension install karein
   - VS Code automatically conda environment ko detect karke use kar leta hai
   - `.ipynb` files ko seedhe VS Code mein kholein

3. **Cloud Development:**
   - **GitHub Codespaces:** "Code" → "Codespaces" → "Create codespace on main" par click karein
   - **Binder:** README par diye gaye Binder badge se browser mein launch karein
   - Note: Binder mein limited resources hain aur kuch web access restrictions bhi hain

### Advanced Lessons ke liye GPU Support

Baad ke lessons mein GPU acceleration se kaafi faayda hota hai:

- **Azure Data Science VM:** GPU support ke saath NC-series VMs use karein
- **Azure Machine Learning:** GPU compute ke saath notebook features use karein
- **Google Colab:** Notebooks ko ek-ek karke upload karein (free GPU support milta hai)

### Quiz App Development

```bash
cd etc/quiz-app
npm run serve  # Hot-reload development server at http://localhost:8080
```

## Testing Instructions

Yeh ek educational repository hai jo software testing ke bajay learning content par focused hai. Isme koi traditional test suite nahi hai.

### Validation Approaches:

1. **Jupyter Notebooks:** Cells ko ek ke baad ek run karein taaki code examples sahi chal rahe hon
2. **Quiz App Testing:** Development server ke through manual testing
3. **Translation Validation:** `translations/` folder mein translated content check karein
4. **Quiz App Linting:** `etc/quiz-app/` mein `npm run lint` chalayein

### Code Examples run karna:

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

- Educational code ke liye standard Python conventions
- Clear, readable code jo learning ko priority deta hai, optimization ko nahi
- Key concepts samjhane wale comments
- Jupyter Notebook-friendly: cells jahan tak ho sake self-contained hone chahiye
- Lesson content ke liye koi strict linting requirements nahi hain

### JavaScript/Vue.js (Quiz App)

- ESLint configuration `etc/quiz-app/package.json` mein hai
- Issues check karne aur auto-fix karne ke liye `npm run lint` chalayein
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

Koi build process zaroori nahi hai - Jupyter Notebooks seedhe execute hote hain.

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

Repository documentation ke liye Docsify use karti hai:
- `index.html` entry point ka kaam karta hai
- Koi build zaroori nahi - seedhe GitHub Pages ke through serve hota hai
- Yahan access karein: https://microsoft.github.io/AI-For-Beginners/

## Contributing Guidelines

### Pull Request Process

1. **Title Format:** Change ko describe karne wale clear, descriptive titles
2. **CLA Requirement:** Microsoft CLA signed hona chahiye (automated check)
3. **Content Guidelines:**
   - Educational focus aur beginner-friendly approach banaye rakhein
   - Notebooks ke saare code examples ko test karein
   - Dhyan rakhein ki notebooks end-to-end chalein
   - Agar English content modify kar rahe hain toh translations bhi update karein
4. **Quiz App Changes:** Commit karne se pehle `npm run lint` chalayein

### Translation Contributions

- Translations GitHub Actions ke through automated hain, co-op-translator use karke
- Manual translations `translations/<language-code>/` mein jaate hain
- Quiz translations `etc/quiz-app/src/assets/translations/` mein hain
- Supported languages: 40+ languages (poori list ke liye README dekhein)

### Active Contribution Areas

Current needs ke liye `etc/CONTRIBUTING.md` dekhein:
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

Basic usage ke liye koi special environment variable zaroori nahi hai.

Azure deployments (quiz app) ke liye:
- `AZURE_STATIC_WEB_APPS_API_TOKEN` (Azure ke dwara automatically set hota hai)

## Debugging and Troubleshooting

### Common Issues

**Issue:** Conda environment creation fail ho jaata hai
- **Solution:** Pehle conda update karein: `conda update conda -y`
- Paryaapt disk space ensure karein (50GB recommended)

**Issue:** Jupyter kernel nahi mil raha
- **Solution:** 
  ```bash
  conda activate ai4beg
  python -m ipykernel install --user --name ai4beg
  ```

**Issue:** Notebooks mein GPU detect nahi ho raha
- **Solution:** 
  - CUDA installation verify karein: `nvidia-smi`
  - PyTorch GPU check karein: `python -c "import torch; print(torch.cuda.is_available())"`
  - TensorFlow GPU check karein: `python -c "import tensorflow as tf; print(tf.config.list_physical_devices('GPU'))"`

**Issue:** Quiz app start nahi hota
- **Solution:**
  ```bash
  cd etc/quiz-app
  rm -rf node_modules package-lock.json
  npm install
  npm run serve
  ```

**Issue:** Binder time out ho jaata hai ya downloads ko block karta hai
- **Solution:** Behtar resource access ke liye GitHub Codespaces ya local setup use karein

### Memory Issues

Kuch lessons ko kaafi RAM (8GB+ recommended) ki zaroorat hoti hai:
- Resource-intensive lessons ke liye cloud VMs use karein
- Model training karte waqt doosri applications band rakhein
- Agar memory khatam ho rahi hai toh notebooks mein batch size kam karein

## Additional Notes

### Course Instructors ke liye

- Teaching guidance ke liye `lessons/0-course-setup/for-teachers.md` dekhein
- Lessons self-contained hain aur inhe order mein ya individually chuna ja sakta hai
- Estimated time: 12 weeks, har week 2 lessons

### Cloud Resources

- **Azure for Students:** Students ke liye free credits available hain
- **Microsoft Learn:** Supplementary learning paths poore curriculum mein link kiye gaye hain
- **Binder:** Free hai, lekin limited resources aur kuch network restrictions ke saath

### Code Execution Options

1. **Local (Recommended):** Poora control, best performance, GPU support
2. **GitHub Codespaces:** Cloud-based VS Code, quick access ke liye accha
3. **Binder:** Browser-based Jupyter, free lekin limited
4. **Azure ML Notebooks:** GPU support ke saath enterprise option
5. **Google Colab:** Notebooks ko ek-ek karke upload karein, free GPU tier available hai

### Notebooks ke saath kaam karna

- Notebooks ko learning ke liye cell-by-cell run karne ke liye design kiya gaya hai
- Kai notebooks pehli baar run hone par datasets download karti hain (time lag sakta hai)
- Kuch models ko reasonable training time ke liye GPU ki zaroorat hoti hai
- Jahan possible ho, pre-trained models use kiye gaye hain taaki compute requirements kam rahein

### Performance Considerations

- Baad ke Computer Vision lessons (CNNs, GANs) GPU se faayda uthate hain
- NLP transformer lessons ko kaafi RAM ki zaroorat ho sakti hai
- Scratch se training educational hai lekin time-consuming hai
- Transfer learning examples training time ko kam karte hain

---

<!-- HINGLISH NOTE START -->
**Note**:
Yeh document Hindi translation ko Hinglish (Roman script) mein convert karke banaya gaya hai, taaki padhna aur samajhna aasaan ho.
Isme kuch galtiyan ya anuvaad ki kamiyan ho sakti hain. Sabse sahi jaankari ke liye original English document ko hi authoritative source maanein.
<!-- HINGLISH NOTE END -->
