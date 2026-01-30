# AGENTS.md

## প্রকল্পের সংক্ষিপ্ত বিবরণ

AI for Beginners একটি ১২-সপ্তাহের, ২৪-লেসনের পাঠক্রম যা কৃত্রিম বুদ্ধিমত্তার মৌলিক বিষয়গুলি কভার করে। এই শিক্ষামূলক রিপোজিটরিতে রয়েছে Jupyter Notebooks ব্যবহার করে ব্যবহারিক পাঠ, কুইজ এবং হাতে-কলমে ল্যাব। পাঠক্রমটি নিম্নলিখিত বিষয়গুলি অন্তর্ভুক্ত করে:

- প্রতীকী AI: জ্ঞান উপস্থাপনা এবং বিশেষজ্ঞ সিস্টেম
- নিউরাল নেটওয়ার্ক এবং TensorFlow ও PyTorch ব্যবহার করে ডিপ লার্নিং
- কম্পিউটার ভিশন কৌশল এবং আর্কিটেকচার
- প্রাকৃতিক ভাষা প্রক্রিয়াকরণ (NLP), ট্রান্সফর্মার এবং BERT সহ
- বিশেষায়িত বিষয়: জেনেটিক অ্যালগরিদম, রিইনফোর্সমেন্ট লার্নিং, মাল্টি-এজেন্ট সিস্টেম
- AI নৈতিকতা এবং দায়িত্বশীল AI নীতিমালা

**মূল প্রযুক্তি:** Python 3, Jupyter Notebooks, TensorFlow, PyTorch, Keras, OpenCV, Vue.js (কুইজ অ্যাপের জন্য)

**আর্কিটেকচার:** Jupyter Notebooks দ্বারা বিষয়ভিত্তিকভাবে সংগঠিত শিক্ষামূলক কন্টেন্ট রিপোজিটরি, Vue.js-ভিত্তিক কুইজ অ্যাপ এবং ব্যাপক বহুভাষিক সমর্থন দ্বারা সম্পূরক।

## সেটআপ কমান্ড

### প্রাথমিক ডেভেলপমেন্ট পরিবেশ (Python/Jupyter)

এই পাঠক্রমটি Python এবং Jupyter Notebooks দিয়ে চালানোর জন্য ডিজাইন করা হয়েছে। প্রস্তাবিত পদ্ধতি হলো miniconda ব্যবহার করা:

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

### বিকল্প: devcontainer ব্যবহার করা

```bash
# Open in VS Code and select "Reopen in Container" when prompted
# The devcontainer will automatically set up the environment
```

### কুইজ অ্যাপ সেটআপ

কুইজ অ্যাপটি একটি পৃথক Vue.js অ্যাপ্লিকেশন যা `etc/quiz-app/`-এ অবস্থিত:

```bash
cd etc/quiz-app
npm install
npm run serve  # Development server
npm run build  # Production build
npm run lint   # Lint and fix files
```

## ডেভেলপমেন্ট ওয়ার্কফ্লো

### Jupyter Notebooks নিয়ে কাজ করা

1. **লোকাল ডেভেলপমেন্ট:**
   - conda পরিবেশ সক্রিয় করুন: `conda activate ai4beg`
   - Jupyter শুরু করুন: `jupyter notebook` বা `jupyter lab`
   - লেসন ফোল্ডারে যান এবং `.ipynb` ফাইল খুলুন
   - ইন্টারেক্টিভভাবে সেল চালান এবং পাঠ অনুসরণ করুন

2. **VS Code এবং Python এক্সটেনশন:**
   - রিপোজিটরি VS Code-এ খুলুন
   - Python এক্সটেনশন ইনস্টল করুন
   - VS Code স্বয়ংক্রিয়ভাবে conda পরিবেশ সনাক্ত করে এবং ব্যবহার করে
   - `.ipynb` ফাইল সরাসরি VS Code-এ খুলুন

3. **ক্লাউড ডেভেলপমেন্ট:**
   - **GitHub Codespaces:** "Code" → "Codespaces" → "Create codespace on main" ক্লিক করুন
   - **Binder:** README-তে Binder ব্যাজ ব্যবহার করে ব্রাউজারে চালু করুন
   - নোট: Binder-এ সীমিত রিসোর্স এবং কিছু ওয়েব অ্যাক্সেস সীমাবদ্ধতা রয়েছে

### উন্নত পাঠের জন্য GPU সমর্থন

পরবর্তী পাঠগুলি GPU অ্যাক্সিলারেশন থেকে উল্লেখযোগ্যভাবে উপকৃত হয়:

- **Azure Data Science VM:** GPU সমর্থন সহ NC-সিরিজ VM ব্যবহার করুন
- **Azure Machine Learning:** GPU কম্পিউট সহ নোটবুক বৈশিষ্ট্য ব্যবহার করুন
- **Google Colab:** পৃথকভাবে নোটবুক আপলোড করুন (বিনামূল্যে GPU সমর্থন রয়েছে)

### কুইজ অ্যাপ ডেভেলপমেন্ট

```bash
cd etc/quiz-app
npm run serve  # Hot-reload development server at http://localhost:8080
```

## টেস্টিং নির্দেশনা

এটি একটি শিক্ষামূলক রিপোজিটরি যা সফটওয়্যার টেস্টিংয়ের চেয়ে শেখার কন্টেন্টে বেশি মনোযোগ দেয়। এখানে প্রচলিত টেস্ট স্যুট নেই।

### যাচাইকরণ পদ্ধতি:

1. **Jupyter Notebooks:** কোড উদাহরণগুলি কাজ করছে কিনা তা নিশ্চিত করতে সেলগুলি ক্রমান্বয়ে চালান
2. **কুইজ অ্যাপ টেস্টিং:** ডেভেলপমেন্ট সার্ভারের মাধ্যমে ম্যানুয়াল টেস্টিং
3. **অনুবাদ যাচাইকরণ:** `translations/` ফোল্ডারে অনুবাদকৃত কন্টেন্ট পরীক্ষা করুন
4. **কুইজ অ্যাপ লিন্টিং:** `npm run lint` চালান `etc/quiz-app/`-এ

### কোড উদাহরণ চালানো:

```bash
# Activate environment first
conda activate ai4beg

# Run Python scripts directly
python lessons/4-ComputerVision/07-ConvNets/pytorchcv.py

# Or execute notebooks
jupyter notebook lessons/3-NeuralNetworks/03-Perceptron/Perceptron.ipynb
```

## কোড স্টাইল

### Python কোড স্টাইল

- শিক্ষামূলক কোডের জন্য স্ট্যান্ডার্ড Python কনভেনশন
- পরিষ্কার, পাঠযোগ্য কোড যা অপ্টিমাইজেশনের চেয়ে শেখাকে অগ্রাধিকার দেয়
- মূল ধারণাগুলি ব্যাখ্যা করার জন্য মন্তব্য
- Jupyter Notebook-সুলভ: সেলগুলি সম্ভব হলে স্বয়ংসম্পূর্ণ হওয়া উচিত
- পাঠ কন্টেন্টের জন্য কঠোর লিন্টিং প্রয়োজনীয়তা নেই

### JavaScript/Vue.js (কুইজ অ্যাপ)

- `etc/quiz-app/package.json`-এ ESLint কনফিগারেশন
- সমস্যা পরীক্ষা এবং স্বয়ংক্রিয়ভাবে ঠিক করার জন্য `npm run lint` চালান
- Vue 2.x কনভেনশন
- কম্পোনেন্ট-ভিত্তিক আর্কিটেকচার

### ফাইল সংগঠন

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

## বিল্ড এবং ডিপ্লয়মেন্ট

### Jupyter কন্টেন্ট

কোনো বিল্ড প্রক্রিয়া প্রয়োজন নেই - Jupyter Notebooks সরাসরি চালানো হয়।

### কুইজ অ্যাপ্লিকেশন

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

### ডকুমেন্টেশন সাইট

রিপোজিটরি Docsify ব্যবহার করে ডকুমেন্টেশন তৈরি করে:
- `index.html` এন্ট্রি পয়েন্ট হিসেবে কাজ করে
- কোনো বিল্ড প্রয়োজন নেই - সরাসরি GitHub Pages দ্বারা পরিবেশিত
- অ্যাক্সেস করুন: https://microsoft.github.io/AI-For-Beginners/

## কন্ট্রিবিউশন নির্দেশিকা

### পুল রিকোয়েস্ট প্রক্রিয়া

1. **শিরোনাম ফরম্যাট:** পরিবর্তনটি বর্ণনা করে পরিষ্কার, বর্ণনামূলক শিরোনাম
2. **CLA প্রয়োজনীয়তা:** Microsoft CLA স্বাক্ষরিত হতে হবে (স্বয়ংক্রিয় চেক)
3. **কন্টেন্ট নির্দেশিকা:**
   - শিক্ষামূলক ফোকাস এবং শিক্ষানবিশ-বান্ধব পদ্ধতি বজায় রাখুন
   - নোটবুকগুলিতে সমস্ত কোড উদাহরণ পরীক্ষা করুন
   - নিশ্চিত করুন যে নোটবুকগুলি শুরু থেকে শেষ পর্যন্ত চালানো যায়
   - ইংরেজি কন্টেন্ট পরিবর্তন করলে অনুবাদ আপডেট করুন
4. **কুইজ অ্যাপ পরিবর্তন:** কমিট করার আগে `npm run lint` চালান

### অনুবাদ কন্ট্রিবিউশন

- অনুবাদগুলি GitHub Actions দ্বারা স্বয়ংক্রিয়ভাবে সম্পন্ন হয় co-op-translator ব্যবহার করে
- ম্যানুয়াল অনুবাদ `translations/<language-code>/`-এ যায়
- কুইজ অনুবাদ `etc/quiz-app/src/assets/translations/`-এ
- সমর্থিত ভাষা: ৪০+ ভাষা (সম্পূর্ণ তালিকার জন্য README দেখুন)

### সক্রিয় কন্ট্রিবিউশন ক্ষেত্র

বর্তমান প্রয়োজনের জন্য `etc/CONTRIBUTING.md` দেখুন:
- ডিপ রিইনফোর্সমেন্ট লার্নিং বিভাগ
- অবজেক্ট ডিটেকশন উন্নতি
- নামযুক্ত সত্তা সনাক্তকরণ উদাহরণ
- কাস্টম এমবেডিং প্রশিক্ষণের নমুনা

## পরিবেশ কনফিগারেশন

### প্রয়োজনীয় ডিপেনডেন্সি

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

### পরিবেশ ভেরিয়েবল

মৌলিক ব্যবহারের জন্য কোনো বিশেষ পরিবেশ ভেরিয়েবল প্রয়োজন নেই।

Azure ডিপ্লয়মেন্টের জন্য (কুইজ অ্যাপ):
- `AZURE_STATIC_WEB_APPS_API_TOKEN` (Azure দ্বারা স্বয়ংক্রিয়ভাবে সেট করা)

## ডিবাগিং এবং সমস্যা সমাধান

### সাধারণ সমস্যা

**সমস্যা:** Conda পরিবেশ তৈরি ব্যর্থ
- **সমাধান:** প্রথমে conda আপডেট করুন: `conda update conda -y`
- পর্যাপ্ত ডিস্ক স্পেস নিশ্চিত করুন (৫০GB প্রস্তাবিত)

**সমস্যা:** Jupyter কের্নেল পাওয়া যায় না
- **সমাধান:** 
  ```bash
  conda activate ai4beg
  python -m ipykernel install --user --name ai4beg
  ```

**সমস্যা:** নোটবুকে GPU সনাক্ত হয় না
- **সমাধান:** 
  - CUDA ইনস্টলেশন যাচাই করুন: `nvidia-smi`
  - PyTorch GPU পরীক্ষা করুন: `python -c "import torch; print(torch.cuda.is_available())"`
  - TensorFlow GPU পরীক্ষা করুন: `python -c "import tensorflow as tf; print(tf.config.list_physical_devices('GPU'))"`

**সমস্যা:** কুইজ অ্যাপ শুরু হয় না
- **সমাধান:**
  ```bash
  cd etc/quiz-app
  rm -rf node_modules package-lock.json
  npm install
  npm run serve
  ```

**সমস্যা:** Binder টাইম আউট বা ডাউনলোড ব্লক করে
- **সমাধান:** ভালো রিসোর্স অ্যাক্সেসের জন্য GitHub Codespaces বা লোকাল সেটআপ ব্যবহার করুন

### মেমোরি সমস্যা

কিছু পাঠ উল্লেখযোগ্য RAM প্রয়োজন (৮GB+ প্রস্তাবিত):
- রিসোর্স-ইনটেনসিভ পাঠের জন্য ক্লাউড VM ব্যবহার করুন
- মডেল প্রশিক্ষণের সময় অন্যান্য অ্যাপ্লিকেশন বন্ধ করুন
- মেমোরি শেষ হয়ে গেলে নোটবুকে ব্যাচ সাইজ কমান

## অতিরিক্ত নোট

### কোর্স ইনস্ট্রাক্টরদের জন্য

- শিক্ষাদানের নির্দেশনার জন্য `lessons/0-course-setup/for-teachers.md` দেখুন
- পাঠগুলি স্বয়ংসম্পূর্ণ এবং ক্রমানুসারে বা পৃথকভাবে শেখানো যেতে পারে
- আনুমানিক সময়: প্রতি সপ্তাহে ২টি পাঠ ধরে ১২ সপ্তাহ

### ক্লাউড রিসোর্স

- **Azure for Students:** শিক্ষার্থীদের জন্য বিনামূল্যে ক্রেডিট উপলব্ধ
- **Microsoft Learn:** সম্পূরক শেখার পথগুলি লিঙ্ক করা হয়েছে
- **Binder:** বিনামূল্যে তবে সীমিত রিসোর্স এবং কিছু নেটওয়ার্ক সীমাবদ্ধতা

### কোড চালানোর বিকল্প

1. **লোকাল (প্রস্তাবিত):** পূর্ণ নিয়ন্ত্রণ, সেরা পারফরম্যান্স, GPU সমর্থন
2. **GitHub Codespaces:** ক্লাউড-ভিত্তিক VS Code, দ্রুত অ্যাক্সেসের জন্য ভালো
3. **Binder:** ব্রাউজার-ভিত্তিক Jupyter, বিনামূল্যে তবে সীমিত
4. **Azure ML Notebooks:** GPU সমর্থন সহ এন্টারপ্রাইজ বিকল্প
5. **Google Colab:** পৃথকভাবে নোটবুক আপলোড করুন, বিনামূল্যে GPU টিয়ার উপলব্ধ

### নোটবুক নিয়ে কাজ করা

- নোটবুকগুলি শেখার জন্য সেল-বাই-সেল চালানোর জন্য ডিজাইন করা হয়েছে
- অনেক নোটবুক প্রথমবার চালানোর সময় ডেটাসেট ডাউনলোড করে (সময় লাগতে পারে)
- কিছু মডেল যুক্তিসঙ্গত প্রশিক্ষণের সময়ের জন্য GPU প্রয়োজন
- প্রি-ট্রেইন্ড মডেল ব্যবহার করা হয় যেখানে সম্ভব, কম্পিউট প্রয়োজনীয়তা কমাতে

### পারফরম্যান্স বিবেচনা

- পরবর্তী কম্পিউটার ভিশন পাঠ (CNNs, GANs) GPU থেকে উপকৃত হয়
- NLP ট্রান্সফর্মার পাঠ উল্লেখযোগ্য RAM প্রয়োজন
- স্ক্র্যাচ থেকে প্রশিক্ষণ শিক্ষামূলক তবে সময়সাপেক্ষ
- ট্রান্সফার লার্নিং উদাহরণ প্রশিক্ষণের সময় কমিয়ে দেয়

---

**অস্বীকৃতি**:  
এই নথিটি AI অনুবাদ পরিষেবা [Co-op Translator](https://github.com/Azure/co-op-translator) ব্যবহার করে অনুবাদ করা হয়েছে। আমরা যথাসম্ভব সঠিক অনুবাদের চেষ্টা করি, তবে অনুগ্রহ করে মনে রাখবেন যে স্বয়ংক্রিয় অনুবাদে ত্রুটি বা অসঙ্গতি থাকতে পারে। নথিটির মূল ভাষায় রচিত সংস্করণটিকেই প্রামাণিক উৎস হিসেবে বিবেচনা করা উচিত। গুরুত্বপূর্ণ তথ্যের জন্য পেশাদার মানব অনুবাদ সুপারিশ করা হয়। এই অনুবাদ ব্যবহারের ফলে সৃষ্ট কোনো ভুল বোঝাবুঝি বা ভুল ব্যাখ্যার জন্য আমরা দায়ী নই।