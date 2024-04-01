[![GitHub license](https://img.shields.io/github/license/microsoft/AI-For-Beginners.svg)](https://github.com/microsoft/AI-For-Beginners/blob/main/LICENSE)
[![GitHub contributors](https://img.shields.io/github/contributors/microsoft/AI-For-Beginners.svg)](https://GitHub.com/microsoft/AI-For-Beginners/graphs/contributors/)
[![GitHub issues](https://img.shields.io/github/issues/microsoft/AI-For-Beginners.svg)](https://GitHub.com/microsoft/AI-For-Beginners/issues/)
[![GitHub pull-requests](https://img.shields.io/github/issues-pr/microsoft/AI-For-Beginners.svg)](https://GitHub.com/microsoft/AI-For-Beginners/pulls/)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com)

[![GitHub watchers](https://img.shields.io/github/watchers/microsoft/AI-For-Beginners.svg?style=social&label=Watch)](https://GitHub.com/microsoft/AI-For-Beginners/watchers/)
[![GitHub forks](https://img.shields.io/github/forks/microsoft/AI-For-Beginners.svg?style=social&label=Fork)](https://GitHub.com/microsoft/AI-For-Beginners/network/)
[![GitHub stars](https://img.shields.io/github/stars/microsoft/AI-For-Beginners.svg?style=social&label=Star)](https://GitHub.com/microsoft/AI-For-Beginners/stargazers/)
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/microsoft/ai-for-beginners/HEAD)
[![Gitter](https://badges.gitter.im/Microsoft/ai-for-beginners.svg)](https://gitter.im/Microsoft/ai-for-beginners?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge)

# الذكاء الصناعي للمبتدئين - منهج
# الذكاء الاصطناعي للمبتدئين

| ![رسم توضيحي بواسطة [(@girlie_mac)](https://twitter.com/girlie_mac) ](./lessons/sketchnotes/ai-overview.png)|
|:---:| |
| الذكاء الاصطناعي للمبتدئين - _رسم توضيحي بواسطة [@girlie_mac](https://twitter.com/girlie_mac)_ |
استكشف عالم **الذكاء الاصطناعي** (AI) مع المنهاج الدراسي البالغ 12 أسبوعًا و 24 درسًا من مايكروسوفت! اغمر نفسك في الذكاء الاصطناعي الرمزي، والشبكات العصبونية، ورؤية الحاسوب، ومعالجة اللغة الطبيعية، وأكثر من ذلك. الدروس التطبيقية والاختبارات والمختبرات تعزز تعلمك. مثالي للمبتدئين، هذا الدليل الشامل، الذي صممه خبراء، يغطي TensorFlow و PyTorch ومبادئ الذكاء الاصطناعي الأخلاقي. ابدأ رحلتك في الذكاء الاصطناعي اليوم!

في هذا المنهج الدراسي، ستتعلم:

- مختلف النهج في الذكاء الاصطناعي، بما في ذلك النهج الرمزي "القديم الجيد" مع **تمثيل المعرفة** والاستدلال ([GOFAI](https://en.wikipedia.org/wiki/Symbolic_artificial_intelligence)).
- **الشبكات العصبونية** و**التعلم العميق**، التي تشكل نواة الذكاء الاصطناعي الحديث. سنوضح المفاهيم وراء هذه المواضيع المهمة باستخدام الشفرة في اثنين من الإطارات الأكثر شهرة - [TensorFlow](http://Tensorflow.org) و [PyTorch](http://pytorch.org).
- **هندسة الشبكات العصبونية** للعمل مع الصور والنصوص. سنغطي النماذج الحديثة ولكن قد نفتقر قليلاً إلى أحدث التطورات.
- النهج الأقل شيوعًا في الذكاء الاصطناعي، مثل **الخوارزميات الوراثية** و**أنظمة الوكلاء المتعددة**.

ما لن نغطيه في هذا المنهج الدراسي:

* حالات الأعمال لاستخدام **الذكاء الاصطناعي في الأعمال**. انظر إلى مسار التعلم [مقدمة في الذكاء الاصطناعي لمستخدمي الأعمال](https://docs.microsoft.com/learn/paths/introduction-ai-for-business-users/?WT.mc_id=academic-77998-cacaste) على Microsoft Learn، أو [مدرسة الأعمال الذكية](https://www.microsoft.com/ai/ai-business-school/?WT.mc_id=academic-77998-cacaste)، التي تم تطويرها بالتعاون مع [INSEAD](https://www.insead.edu/).
* **التعلم الآلي الكلاسيكي**، الذي يُوصَف بشكل جيد في منهجنا [منهج التعلم الآلي للمبتدئين](http://github.com/Microsoft/ML-for-Beginners).
* التطبيقات العملية للذكاء الاصطناعي التي تم بناؤها باستخدام **[الخدمات العقلية](https://azure.microsoft.com/services/cognitive-services/?WT.mc_id=academic-77998-cacaste)**. لهذا، نوصي بالبدء مع موديلات Microsoft Learn للرؤية ومعالجة اللغة الطبيعية، **[الذكاء التوليدي مع خدمة Azure OpenAI](https://learn.microsoft.com/en-us/training/paths/develop-ai-solutions-azure-openai/?WT.mc_id=academic-77998-bethanycheum)** وغيرها.
* إطارات ML **السحابية** المحددة، مثل [Azure Machine Learning](https://azure.microsoft.com/services/machine-learning/?WT.mc_id=academic-77998-cacaste)، [Microsoft Fabric](https://learn.microsoft.com/en-us/training/paths/get-started-fabric/?WT.mc_id=academic-77998-bethanycheum)، أو [Azure Databricks](https://docs.microsoft.com/learn/paths/data-engineer-azure-databricks?WT.mc_id=academic-77998-cacaste). يمكنك النظر في استخدام مسارات التعلم [بناء وتشغيل حلول التعلم الآلي باستخدام خدمة Azure Machine Learning](https://docs.microsoft.com/learn/paths/build-ai-solutions-with-azure-ml-service/?WT.mc_id=academic-77998-cacaste) و [بناء وتشغيل حلول التعلم الآلي باستخدام Azure Databricks](https://docs.microsoft.com/learn/paths/build-operate-machine-learning-solutions-azure-databricks/?WT.mc_id=academic-77998-cacaste).
* **الذكاء الاصطناعي المحادثاتي** و**الروبوتات الدردشة**. هناك مسار تعلم منفصل [إنشاء حلول الذكاء الاصطناعي المحادثاتية](https://docs.microsoft.com/learn/paths/create-conversational-ai-solutions/?WT.mc_id=academic-77998-cacaste)، ويمكنك أيضًا الرجوع إلى [هذه المدونة](https://soshnikov.com/azure/hello-bot-conversational-ai-on-microsoft-platform/) لمزيد من التفاصيل.
* **الرياضيات العميقة** وراء التعلم العميق. لهذا، نوصي بقراءة [Deep Learning](https://www.amazon.com/Deep-Learning-Adaptive-Computation-Machine/dp/0262035618) من تأليف Ian Goodfellow وYoshua Bengio وAaron Courville، والذي يتوفر أيضًا على الإنترنت على [https://www.deeplearningbook.org/](https://www.deeplearningbook.org/).

لمقدمة لطيفة حول مواضيع **الذكاء الاصطناعي في السحابة** يمكنك النظر في مسار التعلم [البدء في الذكاء الاصطناعي على Azure](https://docs.microsoft.com/learn/paths/get-started-with-artificial-intelligence-on-azure/?WT.mc_id=academic-77998-cacaste).


## إعلان - تم إصدار منهج جديد حول الذكاء الاصطناعي التوليدي!

لقد قمنا للتو بإصدار منهج يتكون من 12 درسًا حول الذكاء الاصطناعي التوليدي. تعال وتعلم أشياء مثل:

- توجيه وهندسة التوجيه
- إنشاء تطبيقات النصوص والصور
- تطبيقات البحث

كالعادة، يتضمن الدرس مهامًا لإكمالها، واختبارات لفحص المعرفة، وتحديات.

تفقَّد ذلك:

> https://aka.ms/genai-beginners
---
# المحتوى
| الرقم | الدرس                                              | المقدمة                                     | بايتورش                                                  | كيراس/تنسورفلو                                                               | المختبر                                         |
|------|----------------------------------------------------|-------------------------------------------|---------------------------------------------------------|-------------------------------------------------------------------------------|------------------------------------------------|
| I    | مقدمة في الذكاء الاصطناعي                         |                                           |                                                         |                                                                               |                                                |
| 1    | المقدمة وتاريخ الذكاء الاصطناعي                   | [نص](lessons/1-Intro/README.md)           |                                                         |                                                                               |                                                |
| II   | الذكاء الاصطناعي الرمزي                           |                                           |                                                         |                                                                               |                                                |
| 2    | تمثيل المعرفة والنظم الخبيرة                    | [نص](lessons/2-Symbolic/README.md)       | [نظام خبير](https://github.com/microsoft/AI-For-Beginners/blob/main/lessons/2-Symbolic/Animals.ipynb), [أونتولوجيا](https://github.com/microsoft/AI-For-Beginners/blob/main/lessons/2-Symbolic/FamilyOntology.ipynb), [مخطط المفاهيم](https://github.com/microsoft/AI-For-Beginners/blob/main/lessons/2-Symbolic/MSConceptGraph.ipynb) |                                                                               |                                                |
| III  | مقدمة في الشبكات العصبية                         |                                           |                                                         |                                                                               |                                                |
| 3    | البيرسيبترون                                      | [نص](lessons/3-NeuralNetworks/03-Perceptron/README.md) | [دفتر](https://github.com/microsoft/AI-For-Beginners/blob/main/lessons/3-NeuralNetworks/03-Perceptron/Perceptron.ipynb) |                                                                               | [مختبر](lessons/3-NeuralNetworks/03-Perceptron/lab/README.md) |
| 4    | البيرسيبترون ذو الطبقات المتعددة وإنشاء إطار العمل الخاص بنا | [نص](lessons/3-NeuralNetworks/04-OwnFramework/README.md) | [دفتر](https://github.com/microsoft/AI-For-Beginners/blob/main/lessons/3-NeuralNetworks/04-OwnFramework/OwnFramework.ipynb) |                                                                               | [مختبر](lessons/3-NeuralNetworks/04-OwnFramework/lab/README.md) |
| 5    | مقدمة في الأطر العمل (بايتورش/تنسورفلو) ومشكلة التكيف الزائد | [نص](lessons/3-NeuralNetworks/05-Frameworks/README.md) | [بايتورش](https://github.com/microsoft/AI-For-Beginners/blob/main/lessons/3-NeuralNetworks/05-Frameworks/IntroPyTorch.ipynb) | [كيراس/تنسورفلو](https://github.com/microsoft/AI-For-Beginners/blob/main/lessons/3-NeuralNetworks/05-Frameworks/IntroKeras.ipynb)/[تنسورفلو](https://github.com/microsoft/AI-For-Beginners/blob/main/lessons/3-NeuralNetworks/05-Frameworks/IntroKerasTF.ipynb) | [مختبر](lessons/3-NeuralNetworks/05-Frameworks/lab/README.md) |
| IV   | الرؤية الحاسوبية                                  | [استكشاف الرؤية الحاسوبية باستخدام Microsoft Azure AI Fundamentals](https://docs.microsoft.com/learn/paths/explore-computer-vision-microsoft-azure/?WT.mc_id=academic-77998-cacaste) | [Microsoft Learn Module عن الرؤية الحاسوبية](https://docs.microsoft.com/learn/modules/intro-computer-vision-pytorch/?WT.mc_id=academic-77998-cacaste) | [بايتورش](https://docs.microsoft.com/learn/modules/intro-computer-vision-pytorch/?WT.mc_id=academic-77998-cacaste) | [تنسورفلو](https://docs.microsoft.com/learn/modules/intro-computer-vision-TensorFlow/?WT.mc_id=academic-77998-cacaste) |                                                |
| 6    | مقدمة في الرؤية الحاسوبية. OpenCV                | [نص](lessons/4-ComputerVision/06-IntroCV/README.md) |                                                         | [دفتر](https://github.com/microsoft/AI-For-Beginners/blob/main/lessons/4-ComputerVision/06-IntroCV/OpenCV.ipynb) | [مختبر](lessons/4-ComputerVision/06-IntroCV/lab/README.md) |
| 7    | الشبكات العصبية التكرارية المتعددة الطبقات والهندسة المعمارية لشبكة CNN | [نص](lessons/4-ComputerVision/07-ConvNets/README.md) | [بايتورش](https://github.com/microsoft/AI-For-Beginners/blob/main/lessons/4-ComputerVision/07-ConvNets/ConvNetsPyTorch.ipynb) | [تنسورفلو](lessons/4-ComputerVision/07-ConvNets/ConvNetsTF.ipynb) | [مختبر](lessons/4-ComputerVision/07-ConvNets/lab/README.md) |
| 8    | الشبكات العصبية التكرارية المتعددة الطبقات والهندسة المعمارية لشبكة CNN | [نص](lessons/4-ComputerVision/07-ConvNets/README.md) | [بايتورش](https://github.com/microsoft/AI-For-Beginners/blob/main/lessons/4-ComputerVision/07-ConvNets/ConvNetsPyTorch.ipynb) | [تنسورفلو](lessons/4-ComputerVision/07-ConvNets/ConvNetsTF.ipynb) | [مختبر](lessons/4-ComputerVision/07-ConvNets/lab/README.md) |
| 9    | استراتيجيات التدريب وإلغاء العينات                | [نص](lessons/4-ComputerVision/08-TransferLearning/README.md) | [بايتورش](https://github.com/microsoft/AI-For-Beginners/blob/main/lessons/4-ComputerVision/08-TransferLearning/TransferLearningPyTorch.ipynb) | [تنسورفلو](https://github.com/microsoft/AI-For-Beginners/blob/main/lessons/4-ComputerVision/08-TransferLearning/TransferLearningTF.ipynb) | [مختبر](lessons/4-ComputerVision/08-TransferLearning/lab/README.md) |
| 10   | الشبكات العصبية التكرارية المتعددة الطبقات والهندسة المعمارية لشبكة CNN | [نص](lessons/4-ComputerVision/07-ConvNets/README.md) | [بايتورش](https://github.com/microsoft/AI-For-Beginners/blob/main/lessons/4-ComputerVision/07-ConvNets/ConvNetsPyTorch.ipynb) | [تنسورفلو](lessons/4-ComputerVision/07-ConvNets/ConvNetsTF.ipynb) | [مختبر](lessons/4-ComputerVision/07-ConvNets/lab/README.md) |
| 11   | الشبكات العصبية التكرارية المتعددة الطبقات والهندسة المعمارية لشبكة CNN | [نص](lessons/4-ComputerVision/07-ConvNets/README.md) | [بايتورش](https://github.com/microsoft/AI-For-Beginners/blob/main/lessons/4-ComputerVision/07-ConvNets/ConvNetsPyTorch.ipynb) | [تنسورفلو](lessons/4-ComputerVision/07-ConvNets/ConvNetsTF.ipynb) | [مختبر](lessons/4-ComputerVision/07-ConvNets/lab/README.md) |
| 12   | الشبكات العصبية التكرارية المتعددة الطبقات والهندسة المعمارية لشبكة CNN | [نص](lessons/4-ComputerVision/07-ConvNets/README.md) | [بايتورش](https://github.com/microsoft/AI-For-Beginners/blob/main/lessons/4-ComputerVision/07-ConvNets/ConvNetsPyTorch.ipynb) | [تنسورفلو](lessons/4-ComputerVision/07-ConvNets/ConvNetsTF.ipynb) | [مختبر](lessons/4-ComputerVision/07-ConvNets/lab/README.md) |
| 13   | الشبكات العصبية التكرارية المتعددة الطبقات والهندسة المعمارية لشبكة CNN | [نص](lessons/4-ComputerVision/07-ConvNets/README.md) | [بايتورش](https://github.com/microsoft/AI-For-Beginners/blob/main/lessons/4-ComputerVision/07-ConvNets/ConvNetsPyTorch.ipynb) | [تنسورفلو](lessons/4-ComputerVision/07-ConvNets/ConvNetsTF.ipynb) | [مختبر](lessons/4-ComputerVision/07-ConvNets/lab/README.md) |
| 14   | الشبكات العصبية التكرارية المتعددة الطبقات والهندسة المعمارية لشبكة CNN | [نص](lessons/4-ComputerVision/07-ConvNets/README.md) | [بايتورش](https://github.com/microsoft/AI-For-Beginners/blob/main/lessons/4-ComputerVision/07-ConvNets/ConvNetsPyTorch.ipynb) | [تنسورفلو](lessons/4-ComputerVision/07-ConvNets/ConvNetsTF.ipynb) | [مختبر](lessons/4-ComputerVision/07-ConvNets/lab/README.md) |
| 15   | الشبكات العصبية التكرارية المتعددة الطبقات والهندسة المعمارية لشبكة CNN | [نص](lessons/4-ComputerVision/07-ConvNets/README.md) | [بايتورش](https://github.com/microsoft/AI-For-Beginners/blob/main/lessons/4-ComputerVision/07-ConvNets/ConvNetsPyTorch.ipynb) | [تنسورفلو](lessons/4-ComputerVision/07-ConvNets/ConvNetsTF.ipynb) | [مختبر](lessons/4-ComputerVision/07-ConvNets/lab/README.md) |
| 16   | الشبكات العصبية التكرارية المتعددة الطبقات والهندسة المعمارية لشبكة CNN | [نص](lessons/4-ComputerVision/07-ConvNets/README.md) | [بايتورش](https://github.com/microsoft/AI-For-Beginners/blob/main/lessons/4-ComputerVision/07-ConvNets/ConvNetsPyTorch.ipynb) | [تنسورفلو](lessons/4-ComputerVision/07-ConvNets/ConvNetsTF.ipynb) | [مختبر](lessons/4-ComputerVision/07-ConvNets/lab/README.md) |
| 17   | الشبكات العصبية التكرارية المتعددة الطبقات والهندسة المعمارية لشبكة CNN | [نص](lessons/4-ComputerVision/07-ConvNets/README.md) | [بايتورش](https://github.com/microsoft/AI-For-Beginners/blob/main/lessons/4-ComputerVision/07-ConvNets/ConvNetsPyTorch.ipynb) | [تنسورفلو](lessons/4-ComputerVision/07-ConvNets/ConvNetsTF.ipynb) | [مختبر](lessons/4-ComputerVision/07-ConvNets/lab/README.md) |
| 18   | الشبكات العصبية التكرارية المتعددة الطبقات والهندسة المعمارية لشبكة CNN | [نص](lessons/4-ComputerVision/07-ConvNets/README.md) | [بايتورش](https://github.com/microsoft/AI-For-Beginners/blob/main/lessons/4-ComputerVision/07-ConvNets/ConvNetsPyTorch.ipynb) | [تنسورفلو](lessons/4-ComputerVision/07-ConvNets/ConvNetsTF.ipynb) | [مختبر](lessons/4-ComputerVision/07-ConvNets/lab/README.md) |
| 19   | الشبكات العصبية التكرارية المتعددة الطبقات والهندسة المعمارية لشبكة CNN | [نص](lessons/4-ComputerVision/07-ConvNets/README.md) | [بايتورش](https://github.com/microsoft/AI-For-Beginners/blob/main/lessons/4-ComputerVision/07-ConvNets/ConvNetsPyTorch.ipynb) | [تنسورفلو](lessons/4-ComputerVision/07-ConvNets/ConvNetsTF.ipynb) | [مختبر](lessons/4-ComputerVision/07-ConvNets/lab/README.md) |
| 20   | الشبكات العصبية التكرارية المتعددة الطبقات والهندسة المعمارية لشبكة CNN | [نص](lessons/4-ComputerVision/07-ConvNets/README.md) | [بايتورش](https://github.com/microsoft/AI-For-Beginners/blob/main/lessons/4-ComputerVision/07-ConvNets/ConvNetsPyTorch.ipynb) | [تنسورفلو](lessons/4-ComputerVision/07-ConvNets/ConvNetsTF.ipynb) | [مختبر](lessons/4-ComputerVision/07-ConvNets/lab/README.md) |
| VI   | تقنيات الذكاء الاصطناعي الأخرى                    |                                           |                                                         |                                                                               |                                                |
| 21   | الخوارزميات الجينية                               | [نص](lessons/6-OtherAITechniques/21-GeneticAlgorithms/README.md) | [دفتر](https://github.com/microsoft/AI-For-Beginners/blob/main/lessons/6)

**[خريطة ذهنية للدورة](http://soshnikov.com/courses/ai-for-beginners/mindmap.html)**

كل درس يحتوي على بعض المواد التمهيدية (مرتبطة كـ **نص** أعلاه)، وبعض دفاتر Jupyter التنفيذية، التي غالبًا ما تكون محددة للإطار (**بايتورش** أو **تنسورفلو**). الدفتر التنفيذي يحتوي أيضًا على الكثير من المواد النظرية، لذا يجب عليك فهم الموضوع عبر الأقل إحدى الإصدارات من الدفاتر (إما بايتورش أو تنسورفلو). هناك أيضًا **مختبرات** متاحة لبعض المواضيع، تتيح لك الفرصة لتطبيق المواد التي تعلمتها على مشكلة محددة.

تحتوي بعض الأقسام أيضًا على روابط إلى وحدات **MS Learn** تغطي مواضيع ذات صلة. يوفر Microsoft Learn بيئة تعلم مريحة مع دعم GPU، على الرغم من أنه من الناحية الخاصة بالمحتوى، يمكنك توقع أن يعمق هذه المنهجية قليلاً.

# هل أنت طالب؟

ابدأ مع الموارد التالية:

- [صفحة محور الطلاب](https://docs.microsoft.com/learn/student-hub?WT.mc_id=academic-77998-cacaste) في هذه الصفحة، ستجد موارد للمبتدئين، باقات طلابية وحتى طرق للحصول على قسيمة شهادة مجانية. هذه الصفحة هي واحدة ترغب في حفظها والتحقق منها بين الحين والآخر حيث نقوم بتبديل المحتوى على الأقل شهريًا.
- [سفراء Microsoft Student Learn](https://studentambassadors.microsoft.com?WT.mc_id=academic-77998-cacaste) انضم إلى مجتمع عالمي من سفراء الطلاب، يمكن أن يكون هذا طريقك إلى Microsoft.

- # البدء

**أيها الطلاب**، هناك طريقتان للاستفادة من المنهج. أولًا وقبل كل شيء، يمكنك ببساطة قراءة النص وتصفح الشفرة مباشرةً على GitHub. إذا كنت ترغب في تشغيل الشفرة في أي من الدفاتر - [اقرأ تعليماتنا](./etc/how-to-run.md)، وابحث عن المزيد من النصائح حول كيفية القيام بذلك [في هذه المقالة في البلوج](https://soshnikov.com/education/how-to-execute-notebooks-from-github/).

> **ملاحظة**: [تعليمات حول كيفية تشغيل الشفرة في هذه المنهجية](./etc/how-to-run.md)

ومع ذلك، إذا كنت ترغب في أن تأخذ الدورة كمشروع دراسي ذاتي، فإننا نقترح عليك أن تقوم بنسخ المستودع بأكمله إلى حساب GitHub الخاص بك وتكمل التمارين بمفردك أو مع مجموعة:

- ابدأ بإجراء اختبار قبل المحاضرة.
- اقرأ نص المقدمة للمحاضرة.
- إذا كانت المحاضرة تحتوي على دفاتر ملاحظات إضافية، انتقل إليها وقم بقراءة وتنفيذ الشفرة. إذا كانت هناك دفاتر ملاحظات لـ TensorFlow و PyTorch، يمكنك التركيز على أحدهما - اختر الإطار المفضل لديك.
- تحتوي دفاتر الملاحظات في كثير من الأحيان على بعض التحديات التي تتطلب منك ضبط الشفرة قليلاً لتجربتها.
- اجتاز اختباراً بعد المحاضرة.
- إذا كان هناك مختبر مرفق بالوحدة - قم بإكمال المهمة.
- زر [لوحة النقاش](https://github.com/microsoft/AI-For-Beginners/discussions) لـ "تعلم بصوت عال".

> للمزيد من الدراسة، نوصي بمتابعة هذه [وحدات Microsoft Learn](https://docs.microsoft.com/en-us/users/dmitrysoshnikov-9132/collections/31zgizg2p418yo/?WT.mc_id=academic-77998-cacaste) ومسارات التعلم.

**أيها المعلمون**، لقد [قمنا بتضمين بعض الاقتراحات](/etc/for-teachers.md) حول كيفية استخدام هذه المنهجية.

---

## الاعتمادات

**✍️ المؤلف الرئيسي:** [دميتري سوشنيكوف](http://soshnikov.com)، دكتوراه <br/>
**🔥 المحرر:** [جين لوبر](https://twitter.com/jenlooper)، دكتوراه <br/>
**🎨 رسام السكتشات:** [تومومي إمورا](https://twitter.com/girlie_mac) <br/>
**✅ منشئ الاختبارات:** [لطيفة بيلو](https://github.com/CinnamonXI)، [MLSA](https://studentambassadors.microsoft.com/)  <br/>
**🙏 المساهمون الرئيسيون:** [يفجيني بيشتشيك](https://github.com/Pe4enIks) 

## تعرف على الفريق

[![Promo video](/lessons/sketchnotes/ai-for-beginners.png)](https://youtu.be/m2KrAk0cC1c "Promo video")

> 🎥 انقر فوق الصورة أعلاه لمشاهدة فيديو حول المشروع والأشخاص الذين قاموا بإنشائه!

---

## منهجية التدريس

لقد اخترنا مبدأين تربويين أثناء بناء هذه المنهجية: التأكيد على أنها مشروعية ومبنية على **المشاريع العملية** وتضم **اختبارات متكررة**.

من خلال ضمان أن المحتوى يتماشى مع المشاريع، يتم جعل العملية أكثر جاذبية للطلاب وستتم زيادة استبقاء المفاهيم. بالإضافة إلى ذلك، يضع اختبار منخفض الأهمية قبل الفصل الدراسي النية للطالب نحو تعلم موضوع معين، بينما يضمن اختبار آخر بعد الفصل استبقاءًا أكبر. تم تصميم هذه المنهجية لتكون مرنة وممتعة ويمكن أخذها بالكامل أو جزئيًا. تبدأ المشاريع صغيرة وتصبح أكثر تعقيدًا تدريجيًا بنهاية الدورة الدراسية المدتها 12 أسبوعًا.

> اعثر على [كود السلوك](etc/CODE_OF_CONDUCT.md) لدينا، و[المساهمة](etc/CONTRIBUTING.md)، و[الإرشادات للترجمة](etc/TRANSLATIONS.md). اعثر على [وثائق الدعم هنا](etc/SUPPORT.md) و[معلومات الأمان هنا](etc/SECURITY.md). نحن نرحب بتعليقاتكم البناءة!

> **ملاحظة حول الاختبارات**: تحتوي جميع الاختبارات على [تطبيق](https://red-field-0a6ddfd03.1.azurestaticapps.net/)، لإجمالي 50 اختبارًا يتكون كل منها من ثلاثة أسئلة. يتم ربطها من داخل الدروس ولكن يمكن تشغيل تطبيق الاختبارات محليًا. اتبع التعليمات في المجلد `etc/quiz-app`. 

## الوصول دون اتصال

يمكنك تشغيل هذا الوثائق دون اتصال عن طريق استخدام [Docsify](https://docsify.js.org/#/). قم بنسخ هذا المستودع، [ثبت Docsify](https://docsify.js.org/#/quickstart) على جهاز الكمبيوتر الخاص بك، ثم في مجلد `etc/docsify` من هذا المستودع، اكتب `docsify serve`. سيتم تقديم الموقع على منفذ 3000 على جهاز localhost الخاص بك: `localhost:3000`. يتوفر ملف pdf للمنهجية [في هذا الرابط](/etc/pdf/read)

me.pdf).

## مطلوب مساعدة!

هل ترغب في المساهمة في الترجمة؟ يرجى قراءة [إرشادات الترجمة](etc/TRANSLATIONS.md) الخاصة بنا.

## مناهج دراسية أخرى

تنتج فرقنا مناهج دراسية أخرى! تحقق من:

- [الذكاء الاصطناعي للمبتدئين](https://aka.ms/ai-beginners)
- [علوم البيانات للمبتدئين](https://aka.ms/datascie)
- - [الذكاء الاصطناعي التوليدية للمبتدئين](https://aka.ms/genai-beginners)
- [**جديد** أمن المعلومات للمبتدئين](https://github.com/microsoft/Security-101??WT.mc_id=academic-96948-sayoung)
- [تطوير الويب للمبتدئين](https://aka.ms/webdev-beginners)
- [الإنترنت الأشياء (IoT) للمبتدئين](https://aka.ms/iot-beginners)
- [تعلم الآلة للمبتدئين](https://aka.ms/ml-beginners)
- [تطوير XR للمبتدئين](https://aka.ms/xr-dev-for-beginners)
- [احتراف GitHub Copilot للبرمجة التشاركية في الذكاء الاصطناعي](https://aka.ms/GitHubCopilotAI)
