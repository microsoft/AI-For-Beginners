# AGENTS.md

## نمای کلی پروژه

AI for Beginners یک برنامه آموزشی جامع ۱۲ هفته‌ای و ۲۴ درس است که اصول هوش مصنوعی را پوشش می‌دهد. این مخزن آموزشی شامل درس‌های عملی با استفاده از Jupyter Notebooks، آزمون‌ها و آزمایش‌های عملی است. این برنامه آموزشی موارد زیر را شامل می‌شود:

- هوش مصنوعی نمادین با نمایش دانش و سیستم‌های خبره
- شبکه‌های عصبی و یادگیری عمیق با TensorFlow و PyTorch
- تکنیک‌ها و معماری‌های بینایی کامپیوتری
- پردازش زبان طبیعی (NLP) شامل ترانسفورمرها و BERT
- موضوعات تخصصی: الگوریتم‌های ژنتیک، یادگیری تقویتی، سیستم‌های چندعاملی
- اصول اخلاق هوش مصنوعی و هوش مصنوعی مسئولانه

**فناوری‌های کلیدی:** Python 3، Jupyter Notebooks، TensorFlow، PyTorch، Keras، OpenCV، Vue.js (برای اپلیکیشن آزمون)

**معماری:** مخزن محتوای آموزشی با Jupyter Notebooks که بر اساس موضوعات سازماندهی شده است، همراه با یک اپلیکیشن آزمون مبتنی بر Vue.js و پشتیبانی گسترده چندزبانه.

## دستورات راه‌اندازی

### محیط توسعه اصلی (Python/Jupyter)

برنامه آموزشی برای اجرا با Python و Jupyter Notebooks طراحی شده است. روش پیشنهادی استفاده از miniconda است:

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

### جایگزین: استفاده از devcontainer

```bash
# Open in VS Code and select "Reopen in Container" when prompted
# The devcontainer will automatically set up the environment
```

### راه‌اندازی اپلیکیشن آزمون

اپلیکیشن آزمون یک اپلیکیشن جداگانه Vue.js است که در مسیر `etc/quiz-app/` قرار دارد:

```bash
cd etc/quiz-app
npm install
npm run serve  # Development server
npm run build  # Production build
npm run lint   # Lint and fix files
```

## جریان کاری توسعه

### کار با Jupyter Notebooks

1. **توسعه محلی:**
   - فعال کردن محیط conda: `conda activate ai4beg`
   - شروع Jupyter: `jupyter notebook` یا `jupyter lab`
   - به پوشه‌های درس بروید و فایل‌های `.ipynb` را باز کنید
   - سلول‌ها را به صورت تعاملی اجرا کنید تا درس‌ها را دنبال کنید

2. **VS Code با افزونه Python:**
   - مخزن را در VS Code باز کنید
   - افزونه Python را نصب کنید
   - VS Code به طور خودکار محیط conda را شناسایی و استفاده می‌کند
   - فایل‌های `.ipynb` را مستقیماً در VS Code باز کنید

3. **توسعه ابری:**
   - **GitHub Codespaces:** روی "Code" → "Codespaces" → "Create codespace on main" کلیک کنید
   - **Binder:** از نشان Binder در README برای اجرا در مرورگر استفاده کنید
   - توجه: Binder منابع محدودی دارد و برخی محدودیت‌های دسترسی به وب اعمال می‌شود

### پشتیبانی GPU برای درس‌های پیشرفته

درس‌های بعدی به طور قابل توجهی از شتاب GPU بهره‌مند می‌شوند:

- **Azure Data Science VM:** از VMهای سری NC با پشتیبانی GPU استفاده کنید
- **Azure Machine Learning:** از ویژگی‌های نوت‌بوک با محاسبات GPU استفاده کنید
- **Google Colab:** نوت‌بوک‌ها را به صورت جداگانه آپلود کنید (پشتیبانی رایگان GPU دارد)

### توسعه اپلیکیشن آزمون

```bash
cd etc/quiz-app
npm run serve  # Hot-reload development server at http://localhost:8080
```

## دستورالعمل‌های تست

این مخزن آموزشی بر محتوای یادگیری تمرکز دارد و نه تست نرم‌افزار. هیچ مجموعه تست سنتی وجود ندارد.

### روش‌های اعتبارسنجی:

1. **Jupyter Notebooks:** سلول‌ها را به ترتیب اجرا کنید تا مطمئن شوید مثال‌های کد کار می‌کنند
2. **تست اپلیکیشن آزمون:** تست دستی از طریق سرور توسعه
3. **اعتبارسنجی ترجمه:** محتوای ترجمه شده در پوشه `translations/` را بررسی کنید
4. **Linting اپلیکیشن آزمون:** `npm run lint` در `etc/quiz-app/` اجرا کنید

### اجرای مثال‌های کد:

```bash
# Activate environment first
conda activate ai4beg

# Run Python scripts directly
python lessons/4-ComputerVision/07-ConvNets/pytorchcv.py

# Or execute notebooks
jupyter notebook lessons/3-NeuralNetworks/03-Perceptron/Perceptron.ipynb
```

## سبک کدنویسی

### سبک کدنویسی Python

- کنوانسیون‌های استاندارد Python برای کد آموزشی
- کد واضح و خوانا که یادگیری را بر بهینه‌سازی اولویت می‌دهد
- توضیحات در کامنت‌ها برای مفاهیم کلیدی
- مناسب برای Jupyter Notebook: سلول‌ها باید تا حد امکان مستقل باشند
- هیچ الزامی برای linting سختگیرانه برای محتوای درس وجود ندارد

### JavaScript/Vue.js (اپلیکیشن آزمون)

- پیکربندی ESLint در `etc/quiz-app/package.json`
- اجرای `npm run lint` برای بررسی و رفع خودکار مشکلات
- کنوانسیون‌های Vue 2.x
- معماری مبتنی بر کامپوننت

### سازماندهی فایل‌ها

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

## ساخت و استقرار

### محتوای Jupyter

فرآیند ساخت لازم نیست - Jupyter Notebooks مستقیماً اجرا می‌شوند.

### اپلیکیشن آزمون

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

### سایت مستندات

این مخزن از Docsify برای مستندات استفاده می‌کند:
- `index.html` به عنوان نقطه ورود عمل می‌کند
- هیچ ساختی لازم نیست - مستقیماً از طریق GitHub Pages ارائه می‌شود
- دسترسی در: https://microsoft.github.io/AI-For-Beginners/

## دستورالعمل‌های مشارکت

### فرآیند Pull Request

1. **فرمت عنوان:** عناوین واضح و توصیفی که تغییر را توضیح می‌دهند
2. **الزام CLA:** باید توافق‌نامه Microsoft CLA امضا شود (بررسی خودکار)
3. **دستورالعمل‌های محتوا:**
   - تمرکز آموزشی و رویکرد مناسب برای مبتدیان را حفظ کنید
   - تمام مثال‌های کد در نوت‌بوک‌ها را تست کنید
   - اطمینان حاصل کنید که نوت‌بوک‌ها به صورت کامل اجرا می‌شوند
   - در صورت تغییر محتوای انگلیسی، ترجمه‌ها را به‌روزرسانی کنید
4. **تغییرات اپلیکیشن آزمون:** قبل از کامیت `npm run lint` را اجرا کنید

### مشارکت در ترجمه‌ها

- ترجمه‌ها به صورت خودکار از طریق GitHub Actions با استفاده از co-op-translator انجام می‌شوند
- ترجمه‌های دستی در `translations/<language-code>/` قرار می‌گیرند
- ترجمه‌های آزمون در `etc/quiz-app/src/assets/translations/` قرار دارند
- زبان‌های پشتیبانی شده: بیش از ۴۰ زبان (لیست کامل در README)

### حوزه‌های فعال مشارکت

به `etc/CONTRIBUTING.md` برای نیازهای فعلی مراجعه کنید:
- بخش‌های یادگیری تقویتی عمیق
- بهبودهای تشخیص اشیا
- مثال‌های شناسایی موجودیت‌های نام‌دار
- نمونه‌های آموزش جاسازی‌های سفارشی

## پیکربندی محیط

### وابستگی‌های مورد نیاز

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

### متغیرهای محیطی

برای استفاده پایه هیچ متغیر محیطی خاصی لازم نیست.

برای استقرارهای Azure (اپلیکیشن آزمون):
- `AZURE_STATIC_WEB_APPS_API_TOKEN` (به طور خودکار توسط Azure تنظیم می‌شود)

## اشکال‌زدایی و رفع مشکلات

### مشکلات رایج

**مشکل:** ایجاد محیط Conda شکست می‌خورد
- **راه‌حل:** ابتدا Conda را به‌روزرسانی کنید: `conda update conda -y`
- اطمینان حاصل کنید که فضای دیسک کافی دارید (۵۰ گیگابایت توصیه می‌شود)

**مشکل:** هسته Jupyter پیدا نمی‌شود
- **راه‌حل:** 
  ```bash
  conda activate ai4beg
  python -m ipykernel install --user --name ai4beg
  ```

**مشکل:** GPU در نوت‌بوک‌ها شناسایی نمی‌شود
- **راه‌حل:** 
  - نصب CUDA را بررسی کنید: `nvidia-smi`
  - GPU در PyTorch را بررسی کنید: `python -c "import torch; print(torch.cuda.is_available())"`
  - GPU در TensorFlow را بررسی کنید: `python -c "import tensorflow as tf; print(tf.config.list_physical_devices('GPU'))"`

**مشکل:** اپلیکیشن آزمون شروع نمی‌شود
- **راه‌حل:**
  ```bash
  cd etc/quiz-app
  rm -rf node_modules package-lock.json
  npm install
  npm run serve
  ```

**مشکل:** Binder زمان‌سنجی می‌شود یا دانلودها را مسدود می‌کند
- **راه‌حل:** از GitHub Codespaces یا تنظیمات محلی برای دسترسی بهتر به منابع استفاده کنید

### مشکلات حافظه

برخی درس‌ها به RAM قابل توجهی نیاز دارند (۸ گیگابایت یا بیشتر توصیه می‌شود):
- از VMهای ابری برای درس‌های پرمصرف منابع استفاده کنید
- برنامه‌های دیگر را هنگام آموزش مدل‌ها ببندید
- اندازه دسته‌ها را در نوت‌بوک‌ها کاهش دهید اگر حافظه کافی ندارید

## یادداشت‌های اضافی

### برای مربیان دوره

- به `lessons/0-course-setup/for-teachers.md` برای راهنمایی تدریس مراجعه کنید
- درس‌ها مستقل هستند و می‌توانند به ترتیب یا به صورت انتخابی تدریس شوند
- زمان تخمینی: ۱۲ هفته با ۲ درس در هفته

### منابع ابری

- **Azure for Students:** اعتبار رایگان برای دانشجویان در دسترس است
- **Microsoft Learn:** مسیرهای یادگیری مکمل در طول دوره لینک شده‌اند
- **Binder:** رایگان اما منابع محدود و برخی محدودیت‌های شبکه دارد

### گزینه‌های اجرای کد

1. **محلی (توصیه‌شده):** کنترل کامل، بهترین عملکرد، پشتیبانی GPU
2. **GitHub Codespaces:** VS Code مبتنی بر ابر، مناسب برای دسترسی سریع
3. **Binder:** Jupyter مبتنی بر مرورگر، رایگان اما محدود
4. **Azure ML Notebooks:** گزینه سازمانی با پشتیبانی GPU
5. **Google Colab:** نوت‌بوک‌ها را به صورت جداگانه آپلود کنید، سطح GPU رایگان در دسترس است

### کار با نوت‌بوک‌ها

- نوت‌بوک‌ها برای اجرا سلول به سلول طراحی شده‌اند تا یادگیری را تسهیل کنند
- بسیاری از نوت‌بوک‌ها در اولین اجرا مجموعه داده‌ها را دانلود می‌کنند (ممکن است زمان‌بر باشد)
- برخی مدل‌ها برای زمان‌های آموزش معقول به GPU نیاز دارند
- مدل‌های از پیش آموزش‌دیده در صورت امکان استفاده می‌شوند تا نیاز به محاسبات کاهش یابد

### ملاحظات عملکرد

- درس‌های بینایی کامپیوتری بعدی (CNNها، GANها) از GPU بهره‌مند می‌شوند
- درس‌های ترانسفورمر NLP ممکن است به RAM قابل توجهی نیاز داشته باشند
- آموزش از ابتدا آموزشی است اما زمان‌بر است
- مثال‌های یادگیری انتقالی زمان آموزش را به حداقل می‌رسانند

---

**سلب مسئولیت**:  
این سند با استفاده از سرویس ترجمه هوش مصنوعی [Co-op Translator](https://github.com/Azure/co-op-translator) ترجمه شده است. در حالی که ما تلاش می‌کنیم دقت را حفظ کنیم، لطفاً توجه داشته باشید که ترجمه‌های خودکار ممکن است شامل خطاها یا نادرستی‌ها باشند. سند اصلی به زبان اصلی آن باید به عنوان منبع معتبر در نظر گرفته شود. برای اطلاعات حساس، ترجمه حرفه‌ای انسانی توصیه می‌شود. ما مسئولیتی در قبال سوء تفاهم‌ها یا تفسیرهای نادرست ناشی از استفاده از این ترجمه نداریم.