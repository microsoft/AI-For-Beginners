# AGENTS.md

## نظرة عامة على المشروع

"الذكاء الاصطناعي للمبتدئين" هو منهج شامل لمدة 12 أسبوعًا يتضمن 24 درسًا يغطي أساسيات الذكاء الاصطناعي. يحتوي هذا المستودع التعليمي على دروس عملية باستخدام Jupyter Notebooks، اختبارات قصيرة، ومختبرات تطبيقية. يغطي المنهج:

- الذكاء الاصطناعي الرمزي مع تمثيل المعرفة وأنظمة الخبراء
- الشبكات العصبية والتعلم العميق باستخدام TensorFlow وPyTorch
- تقنيات وهياكل الرؤية الحاسوبية
- معالجة اللغة الطبيعية (NLP) بما في ذلك المحولات وBERT
- مواضيع متخصصة: الخوارزميات الجينية، التعلم المعزز، أنظمة متعددة الوكلاء
- أخلاقيات الذكاء الاصطناعي ومبادئ الذكاء الاصطناعي المسؤول

**التقنيات الرئيسية:** Python 3، Jupyter Notebooks، TensorFlow، PyTorch، Keras، OpenCV، Vue.js (لتطبيق الاختبارات)

**الهيكلية:** مستودع محتوى تعليمي يحتوي على Jupyter Notebooks منظمة حسب مجالات الموضوعات، مدعومة بتطبيق اختبارات يعتمد على Vue.js ودعم متعدد اللغات بشكل واسع.

## أوامر الإعداد

### بيئة التطوير الأساسية (Python/Jupyter)

تم تصميم المنهج للعمل باستخدام Python وJupyter Notebooks. الطريقة الموصى بها هي استخدام miniconda:

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

### البديل: استخدام devcontainer

```bash
# Open in VS Code and select "Reopen in Container" when prompted
# The devcontainer will automatically set up the environment
```

### إعداد تطبيق الاختبارات

تطبيق الاختبارات هو تطبيق Vue.js منفصل موجود في `etc/quiz-app/`:

```bash
cd etc/quiz-app
npm install
npm run serve  # Development server
npm run build  # Production build
npm run lint   # Lint and fix files
```

## سير العمل التطويري

### العمل مع Jupyter Notebooks

1. **التطوير المحلي:**
   - تفعيل بيئة conda: `conda activate ai4beg`
   - بدء Jupyter: `jupyter notebook` أو `jupyter lab`
   - الانتقال إلى مجلدات الدروس وفتح ملفات `.ipynb`
   - تشغيل الخلايا بشكل تفاعلي لمتابعة الدروس

2. **VS Code مع إضافة Python:**
   - فتح المستودع في VS Code
   - تثبيت إضافة Python
   - يقوم VS Code بالكشف تلقائيًا واستخدام بيئة conda
   - فتح ملفات `.ipynb` مباشرة في VS Code

3. **التطوير السحابي:**
   - **GitHub Codespaces:** انقر على "Code" → "Codespaces" → "Create codespace on main"
   - **Binder:** استخدم شارة Binder في README لتشغيله في المتصفح
   - ملاحظة: Binder لديه موارد محدودة وبعض قيود الوصول إلى الويب

### دعم GPU للدروس المتقدمة

تستفيد الدروس المتأخرة بشكل كبير من تسريع GPU:

- **Azure Data Science VM:** استخدم VMs من سلسلة NC مع دعم GPU
- **Azure Machine Learning:** استخدم ميزات الدفاتر مع حساب GPU
- **Google Colab:** قم بتحميل الدفاتر بشكل فردي (يدعم GPU مجانًا)

### تطوير تطبيق الاختبارات

```bash
cd etc/quiz-app
npm run serve  # Hot-reload development server at http://localhost:8080
```

## تعليمات الاختبار

هذا مستودع تعليمي يركز على محتوى التعلم بدلاً من اختبار البرمجيات. لا توجد مجموعة اختبارات تقليدية.

### طرق التحقق:

1. **Jupyter Notebooks:** قم بتنفيذ الخلايا بشكل متسلسل للتحقق من عمل أمثلة الكود
2. **اختبار تطبيق الاختبارات:** اختبار يدوي عبر خادم التطوير
3. **التحقق من الترجمة:** تحقق من المحتوى المترجم في مجلد `translations/`
4. **Linting لتطبيق الاختبارات:** `npm run lint` في `etc/quiz-app/`

### تشغيل أمثلة الكود:

```bash
# Activate environment first
conda activate ai4beg

# Run Python scripts directly
python lessons/4-ComputerVision/07-ConvNets/pytorchcv.py

# Or execute notebooks
jupyter notebook lessons/3-NeuralNetworks/03-Perceptron/Perceptron.ipynb
```

## أسلوب كتابة الكود

### أسلوب كتابة كود Python

- اتفاقيات Python القياسية للكود التعليمي
- كود واضح وقابل للقراءة يركز على التعلم بدلاً من التحسين
- تعليقات تشرح المفاهيم الرئيسية
- مناسب لـ Jupyter Notebook: يجب أن تكون الخلايا مكتفية ذاتيًا قدر الإمكان
- لا توجد متطلبات صارمة لـ linting لمحتوى الدروس

### JavaScript/Vue.js (تطبيق الاختبارات)

- تكوين ESLint في `etc/quiz-app/package.json`
- تشغيل `npm run lint` للتحقق من المشكلات وإصلاحها تلقائيًا
- اتفاقيات Vue 2.x
- هيكلية تعتمد على المكونات

### تنظيم الملفات

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

## البناء والنشر

### محتوى Jupyter

لا توجد عملية بناء مطلوبة - يتم تنفيذ Jupyter Notebooks مباشرة.

### تطبيق الاختبارات

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

### موقع التوثيق

يستخدم المستودع Docsify للتوثيق:
- `index.html` يعمل كنقطة دخول
- لا توجد عملية بناء مطلوبة - يتم تقديمه مباشرة عبر GitHub Pages
- الوصول عبر: https://microsoft.github.io/AI-For-Beginners/

## إرشادات المساهمة

### عملية طلب السحب

1. **تنسيق العنوان:** عناوين واضحة وواصفة تصف التغيير
2. **متطلب CLA:** يجب توقيع CLA الخاص بـ Microsoft (فحص تلقائي)
3. **إرشادات المحتوى:**
   - الحفاظ على التركيز التعليمي ونهج مناسب للمبتدئين
   - اختبار جميع أمثلة الكود في الدفاتر
   - التأكد من تشغيل الدفاتر من البداية إلى النهاية
   - تحديث الترجمات إذا تم تعديل المحتوى الإنجليزي
4. **تغييرات تطبيق الاختبارات:** تشغيل `npm run lint` قبل الالتزام

### مساهمات الترجمة

- تتم الترجمات تلقائيًا عبر GitHub Actions باستخدام co-op-translator
- الترجمات اليدوية توضع في `translations/<language-code>/`
- ترجمات الاختبارات في `etc/quiz-app/src/assets/translations/`
- اللغات المدعومة: أكثر من 40 لغة (راجع README للحصول على القائمة الكاملة)

### مجالات المساهمة النشطة

راجع `etc/CONTRIBUTING.md` للاحتياجات الحالية:
- أقسام التعلم المعزز العميق
- تحسينات الكشف عن الكائنات
- أمثلة التعرف على الكيانات المسماة
- عينات تدريب التضمين المخصص

## تكوين البيئة

### التبعيات المطلوبة

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

### متغيرات البيئة

لا توجد متغيرات بيئة خاصة مطلوبة للاستخدام الأساسي.

لعمليات نشر Azure (تطبيق الاختبارات):
- `AZURE_STATIC_WEB_APPS_API_TOKEN` (يتم تعيينه تلقائيًا بواسطة Azure)

## التصحيح واستكشاف الأخطاء

### المشكلات الشائعة

**المشكلة:** فشل إنشاء بيئة Conda
- **الحل:** تحديث conda أولاً: `conda update conda -y`
- التأكد من وجود مساحة كافية على القرص (يوصى بـ 50GB)

**المشكلة:** لم يتم العثور على نواة Jupyter
- **الحل:** 
  ```bash
  conda activate ai4beg
  python -m ipykernel install --user --name ai4beg
  ```

**المشكلة:** لم يتم اكتشاف GPU في الدفاتر
- **الحل:** 
  - التحقق من تثبيت CUDA: `nvidia-smi`
  - التحقق من GPU في PyTorch: `python -c "import torch; print(torch.cuda.is_available())"`
  - التحقق من GPU في TensorFlow: `python -c "import tensorflow as tf; print(tf.config.list_physical_devices('GPU'))"`

**المشكلة:** تطبيق الاختبارات لا يبدأ
- **الحل:**
  ```bash
  cd etc/quiz-app
  rm -rf node_modules package-lock.json
  npm install
  npm run serve
  ```

**المشكلة:** Binder ينتهي أو يحظر التنزيلات
- **الحل:** استخدم GitHub Codespaces أو الإعداد المحلي للحصول على موارد أفضل

### مشكلات الذاكرة

تتطلب بعض الدروس ذاكرة كبيرة (يوصى بـ 8GB+):
- استخدم VMs السحابية للدروس التي تتطلب موارد مكثفة
- أغلق التطبيقات الأخرى عند تدريب النماذج
- قلل أحجام الدفعات في الدفاتر إذا نفدت الذاكرة

## ملاحظات إضافية

### للمدربين

- راجع `lessons/0-course-setup/for-teachers.md` للحصول على إرشادات التدريس
- الدروس مكتفية ذاتيًا ويمكن تدريسها بالتسلسل أو اختيارها بشكل فردي
- الوقت المقدر: 12 أسبوعًا بمعدل درسين في الأسبوع

### الموارد السحابية

- **Azure للطلاب:** اعتمادات مجانية متاحة للطلاب
- **Microsoft Learn:** مسارات تعلم إضافية مرتبطة طوال الدورة
- **Binder:** مجاني ولكن بموارد محدودة وبعض قيود الشبكة

### خيارات تنفيذ الكود

1. **محلي (موصى به):** تحكم كامل، أفضل أداء، دعم GPU
2. **GitHub Codespaces:** VS Code قائم على السحابة، جيد للوصول السريع
3. **Binder:** Jupyter قائم على المتصفح، مجاني ولكن محدود
4. **دفاتر Azure ML:** خيار مؤسسي مع دعم GPU
5. **Google Colab:** تحميل الدفاتر بشكل فردي، طبقة GPU مجانية متاحة

### العمل مع الدفاتر

- تم تصميم الدفاتر ليتم تشغيلها خلية بخلايا للتعلم
- العديد من الدفاتر تقوم بتنزيل مجموعات البيانات عند التشغيل الأول (قد يستغرق وقتًا)
- تتطلب بعض النماذج GPU لأوقات تدريب معقولة
- يتم استخدام النماذج المدربة مسبقًا حيثما أمكن لتقليل متطلبات الحوسبة

### اعتبارات الأداء

- تستفيد دروس الرؤية الحاسوبية المتأخرة (CNNs، GANs) من GPU
- دروس محولات NLP قد تتطلب ذاكرة كبيرة
- التدريب من الصفر تعليمي ولكنه يستغرق وقتًا طويلاً
- أمثلة التعلم بالنقل تقلل من وقت التدريب

---

**إخلاء المسؤولية**:  
تم ترجمة هذا المستند باستخدام خدمة الترجمة بالذكاء الاصطناعي [Co-op Translator](https://github.com/Azure/co-op-translator). بينما نسعى لتحقيق الدقة، يرجى العلم أن الترجمات الآلية قد تحتوي على أخطاء أو معلومات غير دقيقة. يجب اعتبار المستند الأصلي بلغته الأصلية المصدر الرسمي. للحصول على معلومات حاسمة، يُوصى بالاستعانة بترجمة بشرية احترافية. نحن غير مسؤولين عن أي سوء فهم أو تفسيرات خاطئة ناتجة عن استخدام هذه الترجمة.