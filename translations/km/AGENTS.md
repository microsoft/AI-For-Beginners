# AGENTS.md

## Project Overview

AI សម្រាប់អ្នកចាប់ផ្តើមគឺជាកម្មវិធីសិក្សា 12 សប្ដាហ៍ មានមេរៀន 24 ដែលគ្របដណ្តប់មូលដ្ឋានអំពីបញ្ញាសិប្បនិម្មិត។ ឃ្លាំងសិក្សានេះរួមបញ្ចូលមេរៀនអនុវត្តដោយប្រើ Jupyter Notebooks ការប្រលង និងហLaboratories ដៃគូ។ អំពីវគ្គសិក្សាដូចជា៖

- បញ្ញាសិប្បនិម្មិតសញ្ញា ជាមួយការបង្ហាញចំណេះដឹង និងប្រព័ន្ធអ្នកជំនាញ
- បណ្តាញប្រសាទ និង ការរៀនជម្រៅ ជាមួយ TensorFlow និង PyTorch
- បច្ចេកទេស និងសំណុំរចនាសម្ព័ន្ធមើលឃើញកុំព្យូទ័រ
- ការកែសម្រួលភាសាធម្មជាតិ (NLP) រួមទាំង transformers និង BERT
- ប្រធានបទពិសេស៖ អាល់ហ្គូលិចមហេតុវិជ្ជា, ការរៀនបន្ធុងជំរុញ, ប្រព័ន្ធភ្នាក់ងារច្រើន
- នីតិវិធីផ្នែកបញ្ញាសិប្បនិម្មិត និងគោលការណ៍បញ្ញាសិប្បនិម្មិតយកចិត្តទុកដាក់

**បច្ចេកវិជ្ជាសំខាន់ៗ៖** Python 3, Jupyter Notebooks, TensorFlow, PyTorch, Keras, OpenCV, Vue.js (សម្រាប់កម្មវិធីប្រលង)

**រចនាសម្ព័ន្ធ៖** ឃ្លាំងមាតិកាសិក្សាដែលមាន Jupyter Notebooks ដាក់លំដាប់តាមប្រធានបទ ជាមួយកម្មវិធីប្រលងសម្រាប់ Vue.js និងការគាំទ្រភាសាច្រើន។

## Setup Commands

### Primary Development Environment (Python/Jupyter)

វគ្គសិក្សាត្រូវបានរចនាឡើងសម្រាប់រត់ជាមួយ Python និង Jupyter Notebooks។ វិធីសាស្ត្រដែលបានអនុញ្ញាតគឺប្រើ miniconda៖

```bash
# បែនការផ្ទុកទិន្នន័យ
git clone https://github.com/microsoft/ai-for-beginners
cd ai-for-beginners

# បង្កើត និងដំណើរការ​បរិយាកាស conda
conda env create --name ai4beg --file environment.yml
conda activate ai4beg

# ចាប់ផ្ដើម Jupyter Notebook
jupyter notebook
# ឬ
jupyter lab
```

### Alternative: Using devcontainer

```bash
# បើកនៅក្នុង VS Code ហើយជ្រើស "Reopen in Container" ពេលដែលមានការផ្តល់សំណូមពរ
# devcontainer នឹងរៀបចំបរិយាកាសដោយស្វ័យប្រវត្តិ
```

### Quiz Application Setup

កម្មវិធីប្រលងគឺជា Vue.js app ផ្សេងដែលស្ថិតនៅ `etc/quiz-app/`៖

```bash
cd etc/quiz-app
npm install
npm run serve  # សេវាកម្មអភិវឌ្ឍន៍
npm run build  # ការបង្កើតផលិតកម្ម
npm run lint   # ពិនិត្យ និងជួសជុលកម្មវិធីឯកសារ
```

## Development Workflow

### Working with Jupyter Notebooks

1. **Local Development:**
   - បើកបរិស្ថាន conda៖ `conda activate ai4beg`
   - ចាប់ផ្តើម Jupyter៖ `jupyter notebook` ឬ `jupyter lab`
   - ទៅកាន់ថតមេរៀន និងបើកឯកសារ `.ipynb`
   - រត់កូដក្នុងកោសិកាវីដេអូដើម្បីតាមដានមេរៀន

2. **VS Code with Python Extension:**
   - បើកឃ្លាំងមាតិកានៅក្នុង VS Code
   - ដំឡើងផ្នែកបន្ថែម Python
   - VS Code ស្វ័យប្រវត្តិអាចរកឃើញនិងប្រើបរិស្ថាន conda
   - បើកឯកសារ `.ipynb` ដោយផ្ទាល់ក្នុង VS Code

3. **Cloud Development:**
   - **GitHub Codespaces:** ចុច "Code" → "Codespaces" → "Create codespace on main"
   - **Binder:** ប្រើប៊ាដសម្រាប់ Binder នៅក្នុង README ដើម្បីបើកក្នុងកម្មវិធីទំព័រមេ
   - កំណត់សម្គាល់៖ Binder មានធនធានកំណត់ និងមានការកំណត់ចូលប្រើវេបសាយខ្លះៗ

### GPU Support for Advanced Lessons

មេរៀនក្រោយៗមានអត្ថប្រយោជន៍យ៉ាងច្រើនពីការបើកបរជាមួយ GPU៖

- **Azure Data Science VM:** ប្រើ NC-series VM ដោយមាន GPU
- **Azure Machine Learning:** ប្រើមុខងារសៀវភៅកំណត់ត្រាជាមួយ GPU
- **Google Colab:** ផ្ទុកឡើងសៀវភៅកំណត់ត្រាដោយផ្ទាល់ (ផ្តល់ជាមួយ GPU ដោយឥតគិតថ្លៃ)

### Quiz App Development

```bash
cd etc/quiz-app
npm run serve  # ម៉ាស៊ីនមេអភិវឌ្ឍន៍ដែលផ្ទុកឡើងឡើងវិញយ៉ាងឆាប់រហ័ស​នៅ http://localhost:8080
```

## Testing Instructions

នេះគឺជាឃ្លាំងសិក្សាដែលផ្ដោតលើមាតិកាដល់ការរៀន យ៉ាងហោចណាស់មិនមែនសម្រាប់ការពិនិត្យកម្មវិធីតាមបែបផ្លូវការ។ មិនមានស៊ុមតេស្តបែបបុរាណឡើយ។

### Validation Approaches:

1. **Jupyter Notebooks:** រត់កូដនៅក្នុងកោសិកាតាមលំដាប់ដើម្បីបញ្ជាក់កំហុស
2. **Quiz App Testing:** ពិនិត្យដោយដៃតាមម៉ាស៊ីនបម្រើអភិវឌ្ឍ
3. **Translation Validation:** ពិនិត្យមាតិកាប្រែសម្រួលនៅថត `translations/`
4. **Quiz App Linting:** `npm run lint` នៅក្នុង `etc/quiz-app/`

### Running Code Examples:

```bash
# បើកបរិបទស៊ើបអង្កេតជាលើកដំបូង
conda activate ai4beg

# រត់ស្គ្រីប Python បន្ដផ្ទាល់
python lessons/4-ComputerVision/07-ConvNets/pytorchcv.py

# ឬអនុវត្តបា្រិយកន្តភ្ជាប់នួស
jupyter notebook lessons/3-NeuralNetworks/03-Perceptron/Perceptron.ipynb
```

## Code Style

### Python Code Style

- លំដាប់ Python វិជ្ជាជីវៈសម្រាប់កូដសិក្សា
- កូដច្បាស់លាស់ អាចអានបាន គោរពលើការរៀនជាងការបង្កើតប្រសើរឡើង
- ពណ៌នាច្បាស់លាស់ សម្រាប់មេរៀនដែលមានគោលបំណងបង្រៀន
- សម្របខ្លួនសម្រាប់ Jupyter Notebook៖ កោសិកាគួរតែមានជ្រៅទាំងលក្ខណៈយកខ្លួនឯង
- មិនមានតម្រូវការតឹងរឹងក្នុងការត្រួតពិនិត្យលីនឌីងសម្រាប់មេរៀននេះឡើយ

### JavaScript/Vue.js (Quiz App)

- កំណត់ ESLint នៅ `etc/quiz-app/package.json`
- ដំណើរការ `npm run lint` ដើម្បីពិនិត្យ និងជួសជុលបញ្ហា
- ប្រើ Vue 2.x
- សំណុំរចនាសម្ព័ន្ធផ្អែកលើគ្រឿងបន្លាស់

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

មិនចាំបាច់មានដំណើរការបង្កើត - Jupyter Notebooks រត់ដោយផ្ទាល់។

### Quiz Application

```bash
cd etc/quiz-app

# ការអភិវឌ្ឍ
npm run serve

# ការសាងសង់ផលិតកម្ម
npm run build  # ផលបត់ចេញទៅ etc/quiz-app/dist/

# ដាក់បញ្ចូលទៅ Azure Static Web Apps
# Azure បង្កើត workflow GitHub Actions ដោយស្វ័យប្រវត្តិ
# សូមមើល etc/quiz-app/README.md សម្រាប់ការណែនាំលំអិតអំពីការដាក់បញ្ចូល
```

### Documentation Site

ឃ្លាំងនេះប្រើ Docsify សម្រាប់ឯកសារដឹកនាំ៖
- `index.html` ជាកន្លែងចូល
- មិនចាំបាច់បង្កើត - ផ្តល់ជូនដោយផ្ទាល់តាម GitHub Pages
- ចូលប្រើបានតាម: https://microsoft.github.io/AI-For-Beginners/

## Contributing Guidelines

### Pull Request Process

1. **Title Format:** ចំណងជើងច្បាស់លាស់ ពណ៌នាប្រែប្រួល
2. **CLA Requirement:** ត្រូវចុះហត្ថលេខា Microsoft CLA (ពិនិត្យដោយស្វ័យប្រវត្តិ)
3. **Content Guidelines:**
   - ការបង្កើតមាតិកាផ្ដោតលើការសិក្សា និងងាយស្រួលសម្រាប់អ្នកចាប់ផ្តើម
   - សាកល្បងគ្រប់ឧទាហរណ៍កូដក្នុងសៀវភៅកំណត់ត្រា
   - ប្រាកដថាសៀវភៅកំណត់ត្រារត់បានពេញលេញ
   - បច្ចប្បន្នភាពការប្រែប្រួលបើមានការផ្លាស់ប្តូរមាតិកាអង់គ្លេស
4. **Quiz App Changes:** ប្រតិបត្តិ `npm run lint` មុនធ្វើការប្តូរ

### Translation Contributions

- ការប្រែសម្រួលធ្វើដោយស្វ័យប្រវត្តិផ្ដល់ដោយ GitHub Actions ប្រែសម្រួលជា co-op-translator
- ប្រែសម្រួលដោយដៃនៅក្នុងថត `translations/<language-code>/`
- ប្រែសម្រួលប្រកាន់ប្រលងនៅ `etc/quiz-app/src/assets/translations/`
- គាំទ្រភាសា 40+ ភាសា (មើល README សម្រាប់បញ្ជីពេញលេញ)

### Active Contribution Areas

មើល `etc/CONTRIBUTING.md` សម្រាប់តម្រូវការចុងក្រោយ៖
- ផ្នែក Deep Reinforcement Learning
- ការកែលម្អស្វែងរកវត្ថុ
- ឧទាហរណ៍ Named Entity Recognition
- គំរូហ្វឹកហាត់ embedding តាមបំណង

## Environment Configuration

### Required Dependencies

```bash
# បណ្ណាល័យ Python មូលដ្ឋាន (ពី requirements.txt)
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

មិនមានអថេរបរិស្ថានពិសេសណាមួយទេ សម្រាប់ការប្រើប្រាស់មូលដ្ឋាន។

សម្រាប់ការដាក់ទុកលើ Azure (កម្មវិធីប្រលង):
- `AZURE_STATIC_WEB_APPS_API_TOKEN` (កំណត់ដោយស្វ័យប្រវត្តិដោយ Azure)

## Debugging and Troubleshooting

### Common Issues

**Issue:** បង្កើតបរិស្ថាន conda បរាជ័យ
- **Solution:** បន្ទាន់សម័យ conda ជាមុន៖ `conda update conda -y`
- ប្រាកដថាមានថាសគ្រប់គ្រាន់ (ផ្ដល់អនុសាសន៍ 50GB)

**Issue:** មិនឃើញកឺណែល Jupyter
- **Solution:** 
  ```bash
  conda activate ai4beg
  python -m ipykernel install --user --name ai4beg
  ```

**Issue:** មិនមានការរកឃើញ GPU នៅក្នុងសៀវភៅកំណត់ត្រា
- **Solution:** 
  - ពិនិត្យការដំឡើង CUDA៖ `nvidia-smi`
  - ពិនិត្យ PyTorch GPU៖ `python -c "import torch; print(torch.cuda.is_available())"`
  - ពិនិត្យ TensorFlow GPU៖ `python -c "import tensorflow as tf; print(tf.config.list_physical_devices('GPU'))"`

**Issue:** កម្មវិធីប្រលងមិនចាប់ផ្តើម
- **Solution:**
  ```bash
  cd etc/quiz-app
  rm -rf node_modules package-lock.json
  npm install
  npm run serve
  ```

**Issue:** Binder ពុំចូលរយៈពេលឬហាមឃាត់ការទាញយក
- **Solution:** ប្រើ GitHub Codespaces ឬដំណើរការក្នុងតំបន់ស្រុកសម្រាប់ចូលប្រើធនធានកាន់តែប្រសើរ

### Memory Issues

មេរៀនខ្លះៗត្រូវការមេម៉ូរី RAM ធំ (ផ្ដល់អនុសាសន៍ 8GB+)៖
- ប្រើ VM គ្រប់គ្រាន់នៅពពកសម្រាប់មេរៀនដែលតម្រូវធនធានច្រើន
- បិទកម្មវិធីផ្សេងទៀតពេលហ្វឹកហាត់ម៉ូឌែល
- បន្ថយទំហំដុំក្នុងសៀវភៅកំណត់ត្រាបើផុតមេម៉ូរី

## Additional Notes

### For Course Instructors

- មើល `lessons/0-course-setup/for-teachers.md` សម្រាប់ការណែនាំបង្រៀន
- មេរៀនត្រូវបានរចនាឡើងដោយឯករាជ្យ និងអាចបង្រៀនតាមលំដាប់ ឬជ្រើសរើសជាបុគ្គល
- ពេលវេលាប៉ាន់ប្រមាណ៖ 12 សប្ដាហ៍ ជាមួយមេរៀន 2 មេរៀនក្នុងមួយសប្ដាហ៍

### Cloud Resources

- **Azure សម្រាប់សិស្ស:** មានកម្រៃឥតគិតថ្លៃសម្រាប់សិស្ស
- **Microsoft Learn:** ផ្លូវចេះសិក្សាជាប់គ្នាទាំងនេះ
- **Binder:** ឥតគិតថ្លៃ ប៉ុន្តែកំណត់ធនធាន និងមានការកំណត់បណ្តាញខ្លះៗ

### Code Execution Options

1. **Local (Recommended):** គ្រប់គ្រងពេញលេញ ប្រសិទ្ធភាពខ្ពស់ មានចំណុច GPU
2. **GitHub Codespaces:** VS Code នៅពពក ល្អសម្រាប់ចូលរហ័ស
3. **Binder:** ប្រើ Jupyter នៅម៉ាស៊ីនមេឥតគិតថ្លៃ ប៉ុន្តែកំណត់
4. **Azure ML Notebooks:** ជម្រើសសហគ្រាសមានសមត្ថភាព GPU
5. **Google Colab:** ផ្ទុកឯកសារចូលម៉ត់ដោយផ្ទាល់ មានជាន់ GPU ឥតគិតថ្លៃ

### Working with Notebooks

- សៀវភៅកំណត់ត្រាត្រូវដំណើរការដោយការ​រត់កោសិកា​តាមលំដាប់​សម្រាប់ការរៀន
- សៀវភៅកំណត់ត្រាភាគច្រើនទាញយកទិន្នន័យពេលដំណើរការដំបូង (អាចចំណាយពេល)
- ម៉ូឌែលខ្លះត្រូវការប្រើ GPU សម្រាប់ពេលហ្វឹកហាត់សមរម្យ
- ប្រើម៉ូឌែលដែលហ្វឹកហាត់រួចជាចម្បងដើម្បីកាត់បន្ថយការប្រើកំណត់គណនាបន្ថែម

### Performance Considerations

- មេរៀនមើលឃើញកុំព្យូទ័របន្ទាប់ៗ (CNNs, GANs) មានអត្ថប្រយោជន៍ពី GPU
- មេរៀន NLP ប្រើ transformer អាចតម្រូវ RAM ច្រើន
- ការហ្វឹកហាត់ពីដើមគឺការសិក្សា ប៉ុន្តែចំណាយពេល
- ឧទាហរណ៍រៀនប្រែបន្លាស់ជួយកាត់បន្ថយពេលហ្វឹកហាត់

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ការបដិសេធ**៖  
ឯកសារនេះត្រូវបានបកប្រែដោយប្រើសេវាកម្មបកប្រែ AI [Co-op Translator](https://github.com/Azure/co-op-translator)។ ខណៈដែលយើងខិតខំប្រឹងប្រែងឱ្យបានដូចត្រឹមត្រូវ សូមយកចិត្តទុកដាក់ថាការបកប្រែដោយស្វ័យប្រវត្តិអាចមានកំហុស ឬ ការ​ខុស​ឆ្គង។ ឯកសារដើមក្នុងភាសាតំណក់នឹងត្រូវបានចាត់ទុកជាផ្លូវការជាចម្បង។ សម្រាប់ព័ត៌មានសំខាន់ៗ សូមណែនាំឱ្យប្រើការបកប្រែដោយមនុស្សដែលមានជំនាញ។ យើងមិនទទួលខុសត្រូវចំពោះការយល់ច្រឡំ ឬ ការបកស្រាយខុសឆ្គងណាមួយដែលកើតឡើងពីការប្រើប្រាស់ការបកប្រែនេះ។
<!-- CO-OP TRANSLATOR DISCLAIMER END -->