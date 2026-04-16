# AGENTS.md

## پروجیکٹ کا جائزہ

AI for Beginners ایک جامع 12 ہفتوں، 24 اسباق پر مشتمل نصاب ہے جو مصنوعی ذہانت کے بنیادی اصولوں کا احاطہ کرتا ہے۔ یہ تعلیمی ذخیرہ عملی اسباق، Jupyter Notebooks، کوئزز، اور عملی تجربہ گاہوں پر مشتمل ہے۔ نصاب میں شامل ہیں:

- علامتی AI کے ساتھ علم کی نمائندگی اور ماہر نظام
- نیورل نیٹ ورکس اور ڈیپ لرننگ، TensorFlow اور PyTorch کے ساتھ
- کمپیوٹر وژن کی تکنیکیں اور ڈھانچے
- قدرتی زبان کی پروسیسنگ (NLP) بشمول ٹرانسفارمرز اور BERT
- خصوصی موضوعات: جینیٹک الگورتھمز، ری انفورسمنٹ لرننگ، ملٹی ایجنٹ سسٹمز
- AI اخلاقیات اور ذمہ دار AI اصول

**اہم ٹیکنالوجیز:** Python 3، Jupyter Notebooks، TensorFlow، PyTorch، Keras، OpenCV، Vue.js (کوئز ایپ کے لیے)

**آرکیٹیکچر:** تعلیمی مواد کا ذخیرہ، Jupyter Notebooks کے ذریعے موضوعاتی علاقوں میں منظم، Vue.js پر مبنی کوئز ایپلیکیشن اور وسیع ملٹی لینگویج سپورٹ کے ساتھ۔

## سیٹ اپ کمانڈز

### بنیادی ترقیاتی ماحول (Python/Jupyter)

یہ نصاب Python اور Jupyter Notebooks کے ساتھ چلانے کے لیے ڈیزائن کیا گیا ہے۔ تجویز کردہ طریقہ miniconda استعمال کرنا ہے:

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

### متبادل: devcontainer استعمال کرنا

```bash
# Open in VS Code and select "Reopen in Container" when prompted
# The devcontainer will automatically set up the environment
```

### کوئز ایپلیکیشن سیٹ اپ

کوئز ایپ ایک علیحدہ Vue.js ایپلیکیشن ہے جو `etc/quiz-app/` میں واقع ہے:

```bash
cd etc/quiz-app
npm install
npm run serve  # Development server
npm run build  # Production build
npm run lint   # Lint and fix files
```

## ترقیاتی ورک فلو

### Jupyter Notebooks کے ساتھ کام کرنا

1. **مقامی ترقی:**
   - conda ماحول کو فعال کریں: `conda activate ai4beg`
   - Jupyter شروع کریں: `jupyter notebook` یا `jupyter lab`
   - سبق کے فولڈرز پر جائیں اور `.ipynb` فائلیں کھولیں
   - اسباق کو فالو کرنے کے لیے سیلز کو انٹرایکٹیو طور پر چلائیں

2. **VS Code کے ساتھ Python ایکسٹینشن:**
   - ریپوزٹری کو VS Code میں کھولیں
   - Python ایکسٹینشن انسٹال کریں
   - VS Code خود بخود conda ماحول کا پتہ لگاتا ہے اور استعمال کرتا ہے
   - `.ipynb` فائلیں براہ راست VS Code میں کھولیں

3. **کلاؤڈ ترقی:**
   - **GitHub Codespaces:** "Code" پر کلک کریں → "Codespaces" → "Create codespace on main"
   - **Binder:** README پر موجود Binder بیج استعمال کریں تاکہ براؤزر میں لانچ کریں
   - نوٹ: Binder کے وسائل محدود ہیں اور کچھ ویب رسائی پابندیاں ہیں

### GPU سپورٹ برائے اعلیٰ اسباق

بعد کے اسباق GPU ایکسیلیریشن سے نمایاں فائدہ اٹھاتے ہیں:

- **Azure Data Science VM:** GPU سپورٹ کے ساتھ NC-series VMs استعمال کریں
- **Azure Machine Learning:** GPU کمپیوٹ کے ساتھ نوٹ بک فیچرز استعمال کریں
- **Google Colab:** نوٹ بکس کو انفرادی طور پر اپلوڈ کریں (مفت GPU سپورٹ ہے)

### کوئز ایپ ترقی

```bash
cd etc/quiz-app
npm run serve  # Hot-reload development server at http://localhost:8080
```

## ٹیسٹنگ ہدایات

یہ ایک تعلیمی ذخیرہ ہے جو سیکھنے کے مواد پر مرکوز ہے، نہ کہ سافٹ ویئر ٹیسٹنگ پر۔ یہاں کوئی روایتی ٹیسٹ سوئٹ نہیں ہے۔

### توثیق کے طریقے:

1. **Jupyter Notebooks:** کوڈ مثالوں کو کام کرنے کی تصدیق کے لیے سیلز کو ترتیب وار چلائیں
2. **کوئز ایپ ٹیسٹنگ:** ترقیاتی سرور کے ذریعے دستی ٹیسٹنگ
3. **ترجمہ کی توثیق:** `translations/` فولڈر میں ترجمہ شدہ مواد چیک کریں
4. **کوئز ایپ لنٹنگ:** `npm run lint` `etc/quiz-app/` میں چلائیں

### کوڈ مثالیں چلانا:

```bash
# Activate environment first
conda activate ai4beg

# Run Python scripts directly
python lessons/4-ComputerVision/07-ConvNets/pytorchcv.py

# Or execute notebooks
jupyter notebook lessons/3-NeuralNetworks/03-Perceptron/Perceptron.ipynb
```

## کوڈ اسٹائل

### Python کوڈ اسٹائل

- تعلیمی کوڈ کے لیے معیاری Python کنونشنز
- واضح، پڑھنے کے قابل کوڈ جو سیکھنے کو ترجیح دیتا ہے
- کلیدی تصورات کی وضاحت کرنے والے تبصرے
- Jupyter Notebook کے لیے دوستانہ: سیلز کو جہاں ممکن ہو خود مختار ہونا چاہیے
- سبق کے مواد کے لیے سخت لنٹنگ کی ضروریات نہیں

### JavaScript/Vue.js (کوئز ایپ)

- `etc/quiz-app/package.json` میں ESLint کنفیگریشن
- مسائل چیک کرنے اور خودکار طور پر ٹھیک کرنے کے لیے `npm run lint` چلائیں
- Vue 2.x کنونشنز
- جزو پر مبنی آرکیٹیکچر

### فائل تنظیم

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

## بلڈ اور ڈیپلائمنٹ

### Jupyter مواد

کوئی بلڈ پروسیس درکار نہیں - Jupyter Notebooks براہ راست چلائی جاتی ہیں۔

### کوئز ایپلیکیشن

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

### دستاویزات سائٹ

ریپوزٹری Docsify کو دستاویزات کے لیے استعمال کرتی ہے:
- `index.html` انٹری پوائنٹ کے طور پر کام کرتا ہے
- کوئی بلڈ درکار نہیں - براہ راست GitHub Pages کے ذریعے پیش کیا جاتا ہے
- رسائی: https://microsoft.github.io/AI-For-Beginners/

## تعاون کے رہنما اصول

### پل ریکویسٹ پروسیس

1. **عنوان کی شکل:** تبدیلی کی وضاحت کرنے والے واضح، وضاحتی عنوانات
2. **CLA ضرورت:** Microsoft CLA دستخط شدہ ہونا چاہیے (خودکار چیک)
3. **مواد کے رہنما اصول:**
   - تعلیمی توجہ اور ابتدائی دوستانہ انداز برقرار رکھیں
   - نوٹ بکس میں تمام کوڈ مثالوں کی جانچ کریں
   - یقینی بنائیں کہ نوٹ بکس شروع سے آخر تک چلیں
   - اگر انگریزی مواد میں ترمیم کریں تو ترجمے کو اپ ڈیٹ کریں
4. **کوئز ایپ تبدیلیاں:** کمیٹ کرنے سے پہلے `npm run lint` چلائیں

### ترجمہ تعاون

- ترجمے GitHub Actions کے ذریعے خودکار طور پر کیے جاتے ہیں، co-op-translator استعمال کرتے ہوئے
- دستی ترجمے `translations/<language-code>/` میں جاتے ہیں
- کوئز ترجمے `etc/quiz-app/src/assets/translations/` میں
- معاون زبانیں: 40+ زبانیں (مکمل فہرست کے لیے README دیکھیں)

### فعال تعاون کے علاقے

موجودہ ضروریات کے لیے `etc/CONTRIBUTING.md` دیکھیں:
- ڈیپ ری انفورسمنٹ لرننگ سیکشنز
- آبجیکٹ ڈیٹیکشن میں بہتری
- نامزد ادارہ کی شناخت کی مثالیں
- کسٹم ایمبیڈنگ ٹریننگ کے نمونے

## ماحول کی تشکیل

### مطلوبہ انحصار

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

### ماحول کے متغیرات

بنیادی استعمال کے لیے کوئی خاص ماحول کے متغیرات درکار نہیں۔

Azure ڈیپلائمنٹس کے لیے (کوئز ایپ):
- `AZURE_STATIC_WEB_APPS_API_TOKEN` (Azure کے ذریعے خودکار طور پر سیٹ کیا جاتا ہے)

## ڈیبگنگ اور مسئلہ حل کرنا

### عام مسائل

**مسئلہ:** Conda ماحول کی تخلیق ناکام ہو جاتی ہے
- **حل:** پہلے conda کو اپ ڈیٹ کریں: `conda update conda -y`
- کافی ڈسک اسپیس یقینی بنائیں (50GB تجویز کردہ)

**مسئلہ:** Jupyter کرنل نہیں ملا
- **حل:** 
  ```bash
  conda activate ai4beg
  python -m ipykernel install --user --name ai4beg
  ```

**مسئلہ:** نوٹ بکس میں GPU کا پتہ نہیں چلتا
- **حل:** 
  - CUDA انسٹالیشن کی تصدیق کریں: `nvidia-smi`
  - PyTorch GPU چیک کریں: `python -c "import torch; print(torch.cuda.is_available())"`
  - TensorFlow GPU چیک کریں: `python -c "import tensorflow as tf; print(tf.config.list_physical_devices('GPU'))"`

**مسئلہ:** کوئز ایپ شروع نہیں ہوتی
- **حل:**
  ```bash
  cd etc/quiz-app
  rm -rf node_modules package-lock.json
  npm install
  npm run serve
  ```

**مسئلہ:** Binder ٹائم آؤٹ یا ڈاؤن لوڈز کو بلاک کرتا ہے
- **حل:** بہتر وسائل کی رسائی کے لیے GitHub Codespaces یا مقامی سیٹ اپ استعمال کریں

### میموری کے مسائل

کچھ اسباق کو کافی RAM کی ضرورت ہوتی ہے (8GB+ تجویز کردہ):
- وسائل کے لیے کلاؤڈ VMs استعمال کریں
- ماڈلز کی تربیت کے دوران دیگر ایپلیکیشنز بند کریں
- اگر میموری ختم ہو رہی ہو تو نوٹ بکس میں بیچ سائزز کم کریں

## اضافی نوٹس

### کورس انسٹرکٹرز کے لیے

- تدریسی رہنمائی کے لیے `lessons/0-course-setup/for-teachers.md` دیکھیں
- اسباق خود مختار ہیں اور ترتیب وار یا انفرادی طور پر منتخب کیے جا سکتے ہیں
- تخمینی وقت: 12 ہفتے، ہر ہفتے 2 اسباق

### کلاؤڈ وسائل

- **Azure for Students:** طلباء کے لیے مفت کریڈٹس دستیاب ہیں
- **Microsoft Learn:** اضافی سیکھنے کے راستے پورے نصاب میں لنک کیے گئے ہیں
- **Binder:** مفت لیکن محدود وسائل اور کچھ نیٹ ورک پابندیاں

### کوڈ چلانے کے اختیارات

1. **مقامی (تجویز کردہ):** مکمل کنٹرول، بہترین کارکردگی، GPU سپورٹ
2. **GitHub Codespaces:** کلاؤڈ پر مبنی VS Code، فوری رسائی کے لیے اچھا
3. **Binder:** براؤزر پر مبنی Jupyter، مفت لیکن محدود
4. **Azure ML Notebooks:** GPU سپورٹ کے ساتھ انٹرپرائز آپشن
5. **Google Colab:** نوٹ بکس کو انفرادی طور پر اپلوڈ کریں، مفت GPU ٹائر دستیاب ہے

### نوٹ بکس کے ساتھ کام کرنا

- نوٹ بکس سیکھنے کے لیے سیل بہ سیل چلانے کے لیے ڈیزائن کیے گئے ہیں
- بہت سے نوٹ بکس پہلی بار چلانے پر ڈیٹا سیٹس ڈاؤن لوڈ کرتے ہیں (وقت لگ سکتا ہے)
- کچھ ماڈلز کو معقول تربیتی وقت کے لیے GPU کی ضرورت ہوتی ہے
- جہاں ممکن ہو، پری ٹرینڈ ماڈلز استعمال کیے جاتے ہیں تاکہ کمپیوٹ کی ضروریات کم ہوں

### کارکردگی کے تحفظات

- بعد کے کمپیوٹر وژن اسباق (CNNs، GANs) GPU سے فائدہ اٹھاتے ہیں
- NLP ٹرانسفارمر اسباق کو کافی RAM کی ضرورت ہو سکتی ہے
- شروع سے تربیت تعلیمی ہے لیکن وقت طلب
- ٹرانسفر لرننگ کی مثالیں تربیتی وقت کو کم کرتی ہیں

---

**ڈسکلیمر**:  
یہ دستاویز AI ترجمہ سروس [Co-op Translator](https://github.com/Azure/co-op-translator) کا استعمال کرتے ہوئے ترجمہ کی گئی ہے۔ ہم درستگی کی بھرپور کوشش کرتے ہیں، لیکن براہ کرم آگاہ رہیں کہ خودکار ترجمے میں غلطیاں یا غیر درستیاں ہو سکتی ہیں۔ اصل دستاویز کو اس کی اصل زبان میں مستند ذریعہ سمجھا جانا چاہیے۔ اہم معلومات کے لیے، پیشہ ور انسانی ترجمہ کی سفارش کی جاتی ہے۔ ہم اس ترجمے کے استعمال سے پیدا ہونے والی کسی بھی غلط فہمی یا غلط تشریح کے ذمہ دار نہیں ہیں۔