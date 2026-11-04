# كيفية تشغيل الكود

يحتوي هذا المنهج على الكثير من الأمثلة المختبرة والمختبرات التي قد ترغب في تشغيلها. لتنفيذ ذلك، تحتاج إلى القدرة على تشغيل كود بايثون في دفاتر Jupyter المقدمة كجزء من هذا المنهج. لديك عدة خيارات لتشغيل الكود:

## التشغيل محليًا على جهاز الكمبيوتر الخاص بك

لتشغيل الكود محليًا على جهاز الكمبيوتر الخاص بك، يلزم وجود تثبيت لبايثون. أحد التوصيات هو تثبيت **[miniconda](https://conda.io/en/latest/miniconda.html)** - فهي تثبيت خفيف يدعم مدير الحزم `conda` لبيئات بايثون **الافتراضية** المختلفة.

بعد تثبيت miniconda، قم باستنساخ المستودع وأنشئ بيئة افتراضية لاستخدامها في هذه الدورة:

```bash
git clone http://github.com/microsoft/ai-for-beginners
cd ai-for-beginners
conda env create --name ai4beg --file .devcontainer/environment.yml
conda activate ai4beg
```

> **ملاحظة لنظام ويندوز**: إذا فشل إنشاء البيئة أثناء تثبيت `gdk-pixbuf` مع ظهور خطأ `UnicodeDecodeError` يشير إلى ترميز `gbk`، فعّل وضع UTF-8 في بايثون في الطرفية وحاول مرة أخرى. استخدم الصيغة المناسبة للطرفية التي تستخدمها:
>
> **PowerShell:**
>
> ```powershell
> $env:PYTHONUTF8 = "1"
> conda env create --name ai4beg --file .devcontainer/environment.yml
> ```
>
> **موجه الأوامر (`cmd.exe`) أو موجه Anaconda:**
>
> ```cmd
> set PYTHONUTF8=1
> conda env create --name ai4beg --file .devcontainer/environment.yml
> ```
>
> **Bash، بما في ذلك Git Bash:**
>
> ```bash
> export PYTHONUTF8=1
> conda env create --name ai4beg --file .devcontainer/environment.yml
> ```
>
> إذا تركت محاولة فاشلة البيئة `ai4beg` خلفها، قم بإلغائها وحذف تلك البيئة قبل المحاولة مرة أخرى. استخدم `conda deactivate` أولًا عندما تكون البيئة نشطة:
>
> ```text
> conda deactivate
> conda env remove --name ai4beg
> ```

### استخدام Visual Studio Code مع امتداد بايثون

يُفضل استخدام هذا المنهج عند فتحه في [Visual Studio Code](http://code.visualstudio.com/?WT.mc_id=academic-77998-cacaste) مع [امتداد بايثون](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-77998-cacaste).

> **ملاحظة**: بمجرد استنساخ وفتح الدليل في VS Code، سيقترح تلقائيًا تثبيت امتدادات بايثون. كما يجب عليك تثبيت miniconda كما هو موضح أعلاه.

> **ملاحظة**: إذا اقترح VS Code إعادة فتح المستودع داخل حاوية، يجب عليك رفض ذلك لاستخدام تثبيت بايثون المحلي.

### استخدام Jupyter في المتصفح

يمكنك أيضًا استخدام بيئة Jupyter من المتصفح على جهازك الخاص. كل من Jupyter التقليدي وJupyterHub يوفران بيئة تطوير ملائمة مع الإكمال التلقائي، تمييز الكود، وغيرها.

لبدء Jupyter محليًا، انتقل إلى دليل الدورة ونفّذ:

```bash
jupyter notebook
```
أو
```bash
jupyterhub
```
 ثم يمكنك التنقل إلى أي من ملفات `.ipynb`، فتحها والبدء بالعمل.

### التشغيل داخل الحاوية

أحد البدائل لتثبيت بايثون هو تشغيل الكود داخل حاوية. حيث يوفر مستودعنا مجلد `.devcontainer` خاص يشرح كيفية بناء حاوية لهذا المستودع، ويقدم VS Code فرصة لإعادة فتح الكود داخل حاوية. هذا يتطلب تثبيت Docker، كما أنه أكثر تعقيدًا، لذلك نوصي به للمستخدمين ذوي الخبرة.

## التشغيل في السحابة

إذا كنت لا ترغب في تثبيت بايثون محليًا، ولديك إمكانية الوصول لبعض موارد السحابة - فبديل جيد هو تشغيل الكود في السحابة. هناك عدة طرق للقيام بذلك:

* استخدام **[GitHub Codespaces](https://github.com/features/codespaces)**، وهي بيئة افتراضية تم إنشاؤها لك على GitHub، يمكن الوصول إليها عبر واجهة متصفح VS Code. إذا كان لديك حق الوصول إلى Codespaces، يمكنك النقر على زر **Code** في المستودع، بدء مساحة أكواد، والبدء فورًا.
* استخدام **[Binder](https://mybinder.org/v2/gh/microsoft/ai-for-beginners/HEAD)**. يوفر [Binder](https://mybinder.org) موارد حوسبة مجانية في السحابة للأشخاص مثلك لتجربة الأكواد على GitHub. هناك زر في الصفحة الرئيسية لفتح المستودع في Binder - هذا سيوصلك بسرعة إلى موقع Binder، الذي سينشئ حاوية أساسية ويبدأ واجهة Jupyter ويب بسلاسة.

> **ملاحظة**: لمنع سوء الاستخدام، الوصول إلى بعض الموارد عبر الويب محظور في Binder. قد يمنع هذا بعض أجزاء الكود التي تجلب نماذج و/أو مجموعات بيانات من الإنترنت. قد تحتاج إلى إيجاد حلول بديلة. كما أن الموارد الحسابية التي يوفرها Binder أساسية، لذا سيكون التدريب بطيئًا، خاصة في الدروس المتقدمة والأكثر تعقيدًا.

## التشغيل في السحابة مع دعم GPU

بعض الدروس اللاحقة في هذا المنهج ستستفيد كثيرًا من دعم GPU. تدريب النماذج، على سبيل المثال، يمكن أن يكون بطيئًا للغاية بخلاف ذلك. هناك بعض الخيارات التي يمكنك اتباعها، خاصة إذا كان لديك وصول للسحابة عبر [Azure for Students](https://azure.microsoft.com/free/students/?WT.mc_id=academic-77998-cacaste)، أو عبر مؤسستك:

* إنشاء [آلة افتراضية لعلوم البيانات](https://docs.microsoft.com/learn/modules/intro-to-azure-data-science-virtual-machine/?WT.mc_id=academic-77998-cacaste) والاتصال بها عبر Jupyter. يمكنك بعدها استنساخ المستودع مباشرة على الجهاز، والبدء بالتعلم. آلات NC-series الافتراضية تدعم GPU.

> **ملاحظة**: بعض الاشتراكات، بما في ذلك Azure for Students، لا توفر دعم GPU بشكل افتراضي. قد تحتاج إلى طلب أنوية GPU إضافية عبر طلب دعم تقني.

* إنشاء [مساحة عمل تعلم الآلة على Azure](https://azure.microsoft.com/services/machine-learning/?WT.mc_id=academic-77998-cacaste) ثم استخدام ميزة المفكرة هناك. يوضح [هذا الفيديو](https://azure-for-academics.github.io/quickstart/azureml-papers/) كيفية استنساخ مستودع إلى مفكرة Azure ML والبدء باستخدامه.

يمكنك أيضًا استخدام Google Colab، الذي يأتي بدعم GPU مجاني محدود، ورفع دفاتر Jupyter هناك لتشغيلها واحدًا تلو الآخر.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**تنويه**:
تمت ترجمة هذا المستند باستخدام خدمة الترجمة بالذكاء الاصطناعي [Co-op Translator](https://github.com/Azure/co-op-translator). بينما نسعى للدقة، يرجى العلم أن الترجمات الآلية قد تحتوي على أخطاء أو عدم دقة. يجب اعتبار المستند الأصلي بلغته الأصلية المصدر الرسمي والمعتمد. للمعلومات الهامة، يُنصح بالاستعانة بترجمة بشرية محترفة. نحن غير مسؤولين عن أي سوء فهم أو تفسير ناتج عن استخدام هذه الترجمة.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->