# AGENTS.md

## ပရောဂျက်အကျဉ်းချုပ်

AI for Beginners သည် Artificial Intelligence အခြေခံများကို လေ့လာရန် ၁၂ ပတ်၊ ၂၄ သင်ခန်းစာပါဝင်သော အပြည့်အစုံသင်ရိုးဖြစ်သည်။ ဤပညာရေးဆိုင်ရာ repository တွင် Jupyter Notebooks အသုံးပြုသင်ခန်းစာများ၊ မေးခွန်းများနှင့် လက်တွေ့လုပ်ငန်းများပါဝင်သည်။ သင်ရိုးတွင် အောက်ပါအကြောင်းအရာများကို ဖုံးကွယ်ထားသည် -

- Knowledge Representation နှင့် Expert Systems ဖြင့် Symbolic AI
- TensorFlow နှင့် PyTorch အသုံးပြု Neural Networks နှင့် Deep Learning
- Computer Vision နည်းလမ်းများနှင့် architecture များ
- Natural Language Processing (NLP) အပါအဝင် transformers နှင့် BERT
- အထူးအကြောင်းအရာများ - Genetic Algorithms, Reinforcement Learning, Multi-Agent Systems
- AI Ethics နှင့် တာဝန်ရှိသော AI အခြေခံများ

**အဓိကနည်းပညာများ:** Python 3, Jupyter Notebooks, TensorFlow, PyTorch, Keras, OpenCV, Vue.js (မေးခွန်းအက်ပ်အတွက်)

**Architecture:** Jupyter Notebooks ကို အကြောင်းအရာအလိုက် စီစဉ်ထားသော ပညာရေးဆိုင်ရာ repository၊ Vue.js အခြေခံမေးခွန်းအက်ပ်နှင့် ဘာသာစကားများစွာအတွက် အကျယ်အပြန့်ပံ့ပိုးမှုဖြင့် ဖြည့်စွက်ထားသည်။

## Setup Commands

### အဓိကဖွံ့ဖြိုးရေးပတ်ဝန်းကျင် (Python/Jupyter)

သင်ရိုးသည် Python နှင့် Jupyter Notebooks ဖြင့် အလုပ်လုပ်ရန် ရည်ရွယ်ထားသည်။ အကြံပြုထားသောနည်းလမ်းမှာ miniconda ကို အသုံးပြုခြင်းဖြစ်သည် -

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

### အခြားနည်းလမ်း: devcontainer အသုံးပြုခြင်း

```bash
# Open in VS Code and select "Reopen in Container" when prompted
# The devcontainer will automatically set up the environment
```

### မေးခွန်းအက်ပ် Setup

မေးခွန်းအက်ပ်သည် `etc/quiz-app/` တွင် တည်ရှိသော Vue.js အက်ပ်တစ်ခုဖြစ်သည် -

```bash
cd etc/quiz-app
npm install
npm run serve  # Development server
npm run build  # Production build
npm run lint   # Lint and fix files
```

## ဖွံ့ဖြိုးရေးလုပ်ငန်းစဉ်

### Jupyter Notebooks နှင့် အလုပ်လုပ်ခြင်း

1. **Local Development:**
   - conda environment ကို activate လုပ်ပါ: `conda activate ai4beg`
   - Jupyter ကို စတင်ပါ: `jupyter notebook` သို့မဟုတ် `jupyter lab`
   - သင်ခန်းစာ folder များသို့ သွားပြီး `.ipynb` ဖိုင်များကို ဖွင့်ပါ
   - သင်ခန်းစာများကို လိုက်နာရန် cell များကို လုပ်ဆောင်ပါ

2. **VS Code နှင့် Python Extension:**
   - Repository ကို VS Code တွင် ဖွင့်ပါ
   - Python extension ကို install လုပ်ပါ
   - VS Code သည် conda environment ကို အလိုအလျောက် ရှာဖွေပြီး အသုံးပြုသည်
   - `.ipynb` ဖိုင်များကို VS Code တွင် တိုက်ရိုက်ဖွင့်ပါ

3. **Cloud Development:**
   - **GitHub Codespaces:** "Code" → "Codespaces" → "Create codespace on main" ကို နှိပ်ပါ
   - **Binder:** README တွင် Binder badge ကို အသုံးပြု၍ browser တွင် စတင်ပါ
   - မှတ်ချက်: Binder တွင် အရင်းအမြစ်ကန့်သတ်မှုများနှင့် web access ကန့်သတ်မှုများရှိသည်

### GPU Support for Advanced Lessons

နောက်ဆုံးသင်ခန်းစာများသည် GPU acceleration ကို အလွန်အကျွံအကျိုးရှိစေသည် -

- **Azure Data Science VM:** GPU support ပါရှိသော NC-series VMs ကို အသုံးပြုပါ
- **Azure Machine Learning:** GPU compute ပါရှိသော notebook features ကို အသုံးပြုပါ
- **Google Colab:** Notebook များကို တစ်ခုချင်း upload လုပ်ပါ (အခမဲ့ GPU support ရရှိနိုင်သည်)

### မေးခွန်းအက်ပ် ဖွံ့ဖြိုးရေး

```bash
cd etc/quiz-app
npm run serve  # Hot-reload development server at http://localhost:8080
```

## စမ်းသပ်ခြင်းအညွှန်းများ

ဤသည်သည် ပညာရေးဆိုင်ရာ repository ဖြစ်ပြီး software testing အတွက် မရည်ရွယ်ပါ။ အခြား test suite မပါဝင်ပါ။

### အတည်ပြုနည်းလမ်းများ:

1. **Jupyter Notebooks:** Code examples အလုပ်လုပ်မှုကို အတည်ပြုရန် cell များကို အစဉ်လိုက်လုပ်ဆောင်ပါ
2. **မေးခွန်းအက်ပ် စမ်းသပ်ခြင်း:** Development server မှတစ်ဆင့် လက်တွေ့စမ်းသပ်ပါ
3. **ဘာသာပြန်အတည်ပြုခြင်း:** `translations/` folder တွင် ဘာသာပြန်ထားသော အကြောင်းအရာကို စစ်ဆေးပါ
4. **မေးခွန်းအက်ပ် Linting:** `npm run lint` ကို `etc/quiz-app/` တွင် run လုပ်ပါ

### Code Examples ကို အလုပ်လုပ်စေခြင်း:

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

- ပညာရေး code အတွက် စံပြ Python အခြေခံများ
- သင်ယူမှုကို ဦးစားပေးသော ရှင်းလင်းသော code
- အဓိကအကြောင်းအရာများကို ရှင်းပြသော comment များ
- Jupyter Notebook-friendly: cell များကို self-contained ဖြစ်စေရန် ကြိုးစားပါ
- သင်ခန်းစာအကြောင်းအရာအတွက် strict linting မလိုအပ်ပါ

### JavaScript/Vue.js (မေးခွန်းအက်ပ်)

- `etc/quiz-app/package.json` တွင် ESLint configuration
- `npm run lint` ကို run လုပ်၍ ပြဿနာများကို auto-fix လုပ်ပါ
- Vue 2.x conventions
- Component-based architecture

### ဖိုင်စီစဉ်မှု

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

## Build နှင့် Deployment

### Jupyter Content

Build လုပ်စရာမလိုအပ်ပါ - Jupyter Notebooks ကို တိုက်ရိုက် run လုပ်ပါ။

### မေးခွန်းအက်ပ်

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

Repository သည် Docsify ကို အသုံးပြု၍ documentation ကို ဖော်ပြသည်:
- `index.html` သည် entry point အဖြစ် တည်ရှိသည်
- Build လုပ်စရာမလိုအပ်ပါ - GitHub Pages မှတစ်ဆင့် တိုက်ရိုက် serve လုပ်သည်
- Access: https://microsoft.github.io/AI-For-Beginners/

## Contributing Guidelines

### Pull Request Process

1. **Title Format:** ပြောင်းလဲမှုကို ဖော်ပြသော ရှင်းလင်းသော ခေါင်းစဉ်များ
2. **CLA Requirement:** Microsoft CLA ကို လက်မှတ်ရေးထိုးရမည် (automated check)
3. **Content Guidelines:**
   - ပညာရေးအာရုံစိုက်မှုနှင့် beginner-friendly ဖြစ်စေရန် ထိန်းသိမ်းပါ
   - Notebook များတွင် code examples အားလုံးကို စမ်းသပ်ပါ
   - Notebook များကို အဆုံးအထိ run လုပ်နိုင်ရမည်
   - English content ကို ပြောင်းလဲပါက ဘာသာပြန်များကို update လုပ်ပါ
4. **မေးခွန်းအက်ပ် ပြောင်းလဲမှုများ:** Commit မလုပ်မီ `npm run lint` ကို run လုပ်ပါ

### Translation Contributions

- GitHub Actions မှတစ်ဆင့် co-op-translator ကို အသုံးပြု၍ ဘာသာပြန်များကို အလိုအလျောက်လုပ်ဆောင်သည်
- Manual ဘာသာပြန်များကို `translations/<language-code>/` တွင် ထည့်ပါ
- မေးခွန်းဘာသာပြန်များကို `etc/quiz-app/src/assets/translations/` တွင် ထည့်ပါ
- ပံ့ပိုးထားသော ဘာသာစကားများ: ၄၀+ ဘာသာစကားများ (README တွင် အပြည့်အစုံကြည့်ပါ)

### Active Contribution Areas

`etc/CONTRIBUTING.md` တွင် လက်ရှိလိုအပ်ချက်များကို ကြည့်ပါ:
- Deep Reinforcement Learning အပိုင်းများ
- Object Detection အဆင့်မြှင့်တင်မှုများ
- Named Entity Recognition ဥပမာများ
- Custom embedding training samples

## Environment Configuration

### လိုအပ်သော Dependencies

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

အခြေခံအသုံးပြုမှုအတွက် အထူး environment variables မလိုအပ်ပါ။

Azure deployment များအတွက် (မေးခွန်းအက်ပ်):
- `AZURE_STATIC_WEB_APPS_API_TOKEN` (Azure မှ အလိုအလျောက် set လုပ်သည်)

## Debugging နှင့် Troubleshooting

### အများဆုံးတွေ့ရသော ပြဿနာများ

**ပြဿနာ:** Conda environment creation မအောင်မြင်ပါ
- **ဖြေရှင်းနည်း:** conda ကို update လုပ်ပါ: `conda update conda -y`
- Disk space လုံလောက်မှုရှိကြောင်း သေချာပါ (50GB အကြံပြုထားသည်)

**ပြဿနာ:** Jupyter kernel မတွေ့ပါ
- **ဖြေရှင်းနည်း:** 
  ```bash
  conda activate ai4beg
  python -m ipykernel install --user --name ai4beg
  ```

**ပြဿနာ:** Notebook များတွင် GPU မတွေ့ပါ
- **ဖြေရှင်းနည်း:** 
  - CUDA installation ကို စစ်ဆေးပါ: `nvidia-smi`
  - PyTorch GPU ကို စစ်ဆေးပါ: `python -c "import torch; print(torch.cuda.is_available())"`
  - TensorFlow GPU ကို စစ်ဆေးပါ: `python -c "import tensorflow as tf; print(tf.config.list_physical_devices('GPU'))"`

**ပြဿနာ:** မေးခွန်းအက်ပ် မစတင်နိုင်ပါ
- **ဖြေရှင်းနည်း:**
  ```bash
  cd etc/quiz-app
  rm -rf node_modules package-lock.json
  npm install
  npm run serve
  ```

**ပြဿနာ:** Binder timeout ဖြစ်သည် သို့မဟုတ် downloads ကို block လုပ်သည်
- **ဖြေရှင်းနည်း:** GitHub Codespaces သို့မဟုတ် local setup ကို အသုံးပြုပါ

### Memory ပြဿနာများ

သင်ခန်းစာအချို့တွင် RAM အလွန်များ (8GB+ အကြံပြုထားသည်) လိုအပ်သည်:
- အရင်းအမြစ်များအလွန်များသော သင်ခန်းစာများအတွက် cloud VMs ကို အသုံးပြုပါ
- Model များကို training လုပ်နေစဉ် အခြား application များကို ပိတ်ပါ
- Memory မလုံလောက်ပါက notebook များတွင် batch size ကို လျှော့ချပါ

## အပိုမှတ်ချက်များ

### သင်ခန်းစာဆရာများအတွက်

- `lessons/0-course-setup/for-teachers.md` တွင် သင်ကြားမှုအညွှန်းကို ကြည့်ပါ
- သင်ခန်းစာများသည် self-contained ဖြစ်ပြီး အစဉ်လိုက် သို့မဟုတ် တစ်ခုချင်းရွေး၍ သင်ကြားနိုင်သည်
- ခန့်မှန်းထားသောအချိန်: ၁၂ ပတ်၊ တစ်ပတ်လျှင် သင်ခန်းစာ ၂ ခု

### Cloud Resources

- **Azure for Students:** ကျောင်းသားများအတွက် အခမဲ့ credits ရရှိနိုင်သည်
- **Microsoft Learn:** သင်ခန်းစာများတွင် ဆက်စပ် learning paths များ link လုပ်ထားသည်
- **Binder:** အခမဲ့ဖြစ်သော်လည်း အရင်းအမြစ်ကန့်သတ်မှုများနှင့် network ကန့်သတ်မှုများရှိသည်

### Code Execution Options

1. **Local (အကြံပြုထားသည်):** အပြည့်အဝထိန်းချုပ်မှု၊ အကောင်းဆုံး performance၊ GPU support
2. **GitHub Codespaces:** Cloud-based VS Code, အလွယ်တကူ access ရရှိနိုင်သည်
3. **Binder:** Browser-based Jupyter, အခမဲ့ဖြစ်သော်လည်း ကန့်သတ်မှုများရှိသည်
4. **Azure ML Notebooks:** GPU support ပါရှိသော Enterprise option
5. **Google Colab:** Notebook များကို တစ်ခုချင်း upload လုပ်ပါ၊ အခမဲ့ GPU tier ရရှိနိုင်သည်

### Notebook များနှင့် အလုပ်လုပ်ခြင်း

- Notebook များကို သင်ယူမှုအတွက် cell-by-cell run လုပ်ရန် ရည်ရွယ်ထားသည်
- Notebook များသည် ပထမဆုံး run လုပ်စဉ် dataset များကို download လုပ်သည် (အချိန်ယူနိုင်သည်)
- Model အချို့သည် reasonable training time ရရှိရန် GPU လိုအပ်သည်
- Compute လိုအပ်ချက်များကို လျှော့ချရန် pre-trained models ကို အသုံးပြုသည်

### Performance အတွေးအခေါ်များ

- နောက်ဆုံး computer vision သင်ခန်းစာများ (CNNs, GANs) တွင် GPU အကျိုးရှိသည်
- NLP transformer သင်ခန်းစာများတွင် RAM အလွန်များလိုအပ်နိုင်သည်
- Scratch မှ training လုပ်ခြင်းသည် ပညာရေးအတွက် အကျိုးရှိသော်လည်း အချိန်ယူနိုင်သည်
- Transfer learning ဥပမာများသည် training အချိန်ကို လျှော့ချသည်

---

**အကြောင်းကြားချက်**:  
ဤစာရွက်စာတမ်းကို AI ဘာသာပြန်ဝန်ဆောင်မှု [Co-op Translator](https://github.com/Azure/co-op-translator) ကို အသုံးပြု၍ ဘာသာပြန်ထားပါသည်။ ကျွန်ုပ်တို့သည် တိကျမှန်ကန်မှုအတွက် ကြိုးစားနေသော်လည်း၊ အလိုအလျောက် ဘာသာပြန်ခြင်းတွင် အမှားများ သို့မဟုတ် မမှန်ကန်မှုများ ပါဝင်နိုင်သည်ကို သတိပြုပါ။ မူရင်းဘာသာစကားဖြင့် ရေးသားထားသော စာရွက်စာတမ်းကို အာဏာတရားရှိသော ရင်းမြစ်အဖြစ် သတ်မှတ်သင့်ပါသည်။ အရေးကြီးသော အချက်အလက်များအတွက် လူ့ဘာသာပြန်ပညာရှင်များမှ ပရော်ဖက်ရှင်နယ် ဘာသာပြန်ခြင်းကို အကြံပြုပါသည်။ ဤဘာသာပြန်ကို အသုံးပြုခြင်းမှ ဖြစ်ပေါ်လာသော အလွဲအလွတ်များ သို့မဟုတ် အနားလွဲမှုများအတွက် ကျွန်ုပ်တို့သည် တာဝန်မယူပါ။