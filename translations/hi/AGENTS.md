# AGENTS.md

## परियोजना का अवलोकन

AI for Beginners एक व्यापक 12-सप्ताह, 24-पाठ का पाठ्यक्रम है जो कृत्रिम बुद्धिमत्ता के मूलभूत सिद्धांतों को कवर करता है। यह शैक्षिक रिपॉजिटरी Jupyter Notebooks, क्विज़ और प्रायोगिक लैब्स के साथ व्यावहारिक पाठ प्रदान करता है। पाठ्यक्रम में शामिल हैं:

- प्रतीकात्मक AI, ज्ञान प्रतिनिधित्व और विशेषज्ञ प्रणालियाँ
- TensorFlow और PyTorch के साथ न्यूरल नेटवर्क और डीप लर्निंग
- कंप्यूटर विज़न तकनीक और आर्किटेक्चर
- प्राकृतिक भाषा प्रसंस्करण (NLP), जिसमें ट्रांसफॉर्मर्स और BERT शामिल हैं
- विशेष विषय: जेनेटिक एल्गोरिदम, रिइंफोर्समेंट लर्निंग, मल्टी-एजेंट सिस्टम
- AI नैतिकता और जिम्मेदार AI सिद्धांत

**मुख्य तकनीकें:** Python 3, Jupyter Notebooks, TensorFlow, PyTorch, Keras, OpenCV, Vue.js (क्विज़ ऐप के लिए)

**आर्किटेक्चर:** Jupyter Notebooks द्वारा विषय क्षेत्रों में व्यवस्थित शैक्षिक सामग्री रिपॉजिटरी, Vue.js-आधारित क्विज़ एप्लिकेशन और व्यापक बहुभाषी समर्थन के साथ।

## सेटअप कमांड्स

### प्राथमिक विकास वातावरण (Python/Jupyter)

पाठ्यक्रम Python और Jupyter Notebooks के साथ चलाने के लिए डिज़ाइन किया गया है। अनुशंसित तरीका है miniconda का उपयोग:

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

### विकल्प: devcontainer का उपयोग करना

```bash
# Open in VS Code and select "Reopen in Container" when prompted
# The devcontainer will automatically set up the environment
```

### क्विज़ एप्लिकेशन सेटअप

क्विज़ ऐप एक अलग Vue.js एप्लिकेशन है जो `etc/quiz-app/` में स्थित है:

```bash
cd etc/quiz-app
npm install
npm run serve  # Development server
npm run build  # Production build
npm run lint   # Lint and fix files
```

## विकास कार्यप्रवाह

### Jupyter Notebooks के साथ काम करना

1. **स्थानीय विकास:**
   - conda वातावरण सक्रिय करें: `conda activate ai4beg`
   - Jupyter शुरू करें: `jupyter notebook` या `jupyter lab`
   - पाठ फ़ोल्डरों पर जाएं और `.ipynb` फ़ाइलें खोलें
   - पाठों का अनुसरण करने के लिए कोशिकाओं को इंटरैक्टिव रूप से चलाएं

2. **VS Code के साथ Python एक्सटेंशन:**
   - रिपॉजिटरी को VS Code में खोलें
   - Python एक्सटेंशन इंस्टॉल करें
   - VS Code स्वचालित रूप से conda वातावरण का पता लगाता है और उपयोग करता है
   - `.ipynb` फ़ाइलें सीधे VS Code में खोलें

3. **क्लाउड विकास:**
   - **GitHub Codespaces:** "Code" → "Codespaces" → "Create codespace on main" पर क्लिक करें
   - **Binder:** README पर Binder बैज का उपयोग करके ब्राउज़र में लॉन्च करें
   - नोट: Binder में सीमित संसाधन और कुछ वेब एक्सेस प्रतिबंध हैं

### उन्नत पाठों के लिए GPU समर्थन

बाद के पाठ GPU त्वरण से काफी लाभान्वित होते हैं:

- **Azure Data Science VM:** GPU समर्थन के साथ NC-सीरीज़ VMs का उपयोग करें
- **Azure Machine Learning:** GPU कंप्यूट के साथ नोटबुक सुविधाओं का उपयोग करें
- **Google Colab:** नोटबुक्स को व्यक्तिगत रूप से अपलोड करें (मुफ्त GPU समर्थन है)

### क्विज़ ऐप विकास

```bash
cd etc/quiz-app
npm run serve  # Hot-reload development server at http://localhost:8080
```

## परीक्षण निर्देश

यह एक शैक्षिक रिपॉजिटरी है जो सॉफ़्टवेयर परीक्षण के बजाय सीखने की सामग्री पर केंद्रित है। कोई पारंपरिक परीक्षण सूट नहीं है।

### सत्यापन दृष्टिकोण:

1. **Jupyter Notebooks:** कोशिकाओं को क्रमिक रूप से चलाएं ताकि कोड उदाहरण काम कर रहे हों
2. **क्विज़ ऐप परीक्षण:** विकास सर्वर के माध्यम से मैन्युअल परीक्षण
3. **अनुवाद सत्यापन:** `translations/` फ़ोल्डर में अनुवादित सामग्री की जांच करें
4. **क्विज़ ऐप लिंटिंग:** `npm run lint` को `etc/quiz-app/` में चलाएं

### कोड उदाहरण चलाना:

```bash
# Activate environment first
conda activate ai4beg

# Run Python scripts directly
python lessons/4-ComputerVision/07-ConvNets/pytorchcv.py

# Or execute notebooks
jupyter notebook lessons/3-NeuralNetworks/03-Perceptron/Perceptron.ipynb
```

## कोड शैली

### Python कोड शैली

- शैक्षिक कोड के लिए मानक Python परंपराएँ
- स्पष्ट, पठनीय कोड जो सीखने को प्राथमिकता देता है, अनुकूलन को नहीं
- प्रमुख अवधारणाओं को समझाने वाले टिप्पणियाँ
- Jupyter Notebook-अनुकूल: कोशिकाएँ जहाँ तक संभव हो आत्म-निहित होनी चाहिए
- पाठ सामग्री के लिए कोई सख्त लिंटिंग आवश्यकताएँ नहीं

### JavaScript/Vue.js (क्विज़ ऐप)

- `etc/quiz-app/package.json` में ESLint कॉन्फ़िगरेशन
- मुद्दों की जांच और स्वचालित सुधार के लिए `npm run lint` चलाएँ
- Vue 2.x परंपराएँ
- घटक-आधारित आर्किटेक्चर

### फ़ाइल संगठन

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

## निर्माण और परिनियोजन

### Jupyter सामग्री

कोई निर्माण प्रक्रिया आवश्यक नहीं है - Jupyter Notebooks सीधे निष्पादित किए जाते हैं।

### क्विज़ एप्लिकेशन

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

### दस्तावेज़ीकरण साइट

रिपॉजिटरी Docsify का उपयोग करती है दस्तावेज़ीकरण के लिए:
- `index.html` प्रवेश बिंदु के रूप में कार्य करता है
- कोई निर्माण आवश्यक नहीं - सीधे GitHub Pages के माध्यम से परोसा जाता है
- एक्सेस करें: https://microsoft.github.io/AI-For-Beginners/

## योगदान दिशानिर्देश

### पुल अनुरोध प्रक्रिया

1. **शीर्षक प्रारूप:** परिवर्तन का वर्णन करने वाले स्पष्ट, वर्णनात्मक शीर्षक
2. **CLA आवश्यकता:** Microsoft CLA हस्ताक्षरित होना चाहिए (स्वचालित जांच)
3. **सामग्री दिशानिर्देश:**
   - शैक्षिक फोकस और शुरुआती-अनुकूल दृष्टिकोण बनाए रखें
   - नोटबुक्स में सभी कोड उदाहरणों का परीक्षण करें
   - सुनिश्चित करें कि नोटबुक्स एंड-टू-एंड चलें
   - यदि अंग्रेजी सामग्री को संशोधित कर रहे हैं तो अनुवाद अपडेट करें
4. **क्विज़ ऐप परिवर्तन:** कमिट करने से पहले `npm run lint` चलाएँ

### अनुवाद योगदान

- अनुवाद GitHub Actions के माध्यम से स्वचालित हैं co-op-translator का उपयोग करके
- मैन्युअल अनुवाद `translations/<language-code>/` में जाते हैं
- क्विज़ अनुवाद `etc/quiz-app/src/assets/translations/` में
- समर्थित भाषाएँ: 40+ भाषाएँ (पूरी सूची के लिए README देखें)

### सक्रिय योगदान क्षेत्र

वर्तमान आवश्यकताओं के लिए `etc/CONTRIBUTING.md` देखें:
- डीप रिइंफोर्समेंट लर्निंग अनुभाग
- ऑब्जेक्ट डिटेक्शन सुधार
- नामित इकाई पहचान उदाहरण
- कस्टम एम्बेडिंग प्रशिक्षण नमूने

## पर्यावरण कॉन्फ़िगरेशन

### आवश्यक निर्भरताएँ

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

### पर्यावरण चर

मूल उपयोग के लिए कोई विशेष पर्यावरण चर आवश्यक नहीं है।

Azure परिनियोजन (क्विज़ ऐप) के लिए:
- `AZURE_STATIC_WEB_APPS_API_TOKEN` (Azure द्वारा स्वचालित रूप से सेट)

## डिबगिंग और समस्या निवारण

### सामान्य समस्याएँ

**समस्या:** Conda वातावरण निर्माण विफल
- **समाधान:** पहले conda अपडेट करें: `conda update conda -y`
- पर्याप्त डिस्क स्थान सुनिश्चित करें (50GB अनुशंसित)

**समस्या:** Jupyter कर्नेल नहीं मिला
- **समाधान:** 
  ```bash
  conda activate ai4beg
  python -m ipykernel install --user --name ai4beg
  ```

**समस्या:** नोटबुक्स में GPU का पता नहीं चला
- **समाधान:** 
  - CUDA स्थापना सत्यापित करें: `nvidia-smi`
  - PyTorch GPU जांचें: `python -c "import torch; print(torch.cuda.is_available())"`
  - TensorFlow GPU जांचें: `python -c "import tensorflow as tf; print(tf.config.list_physical_devices('GPU'))"`

**समस्या:** क्विज़ ऐप शुरू नहीं होता
- **समाधान:**
  ```bash
  cd etc/quiz-app
  rm -rf node_modules package-lock.json
  npm install
  npm run serve
  ```

**समस्या:** Binder टाइम आउट या डाउनलोड को ब्लॉक करता है
- **समाधान:** बेहतर संसाधन एक्सेस के लिए GitHub Codespaces या स्थानीय सेटअप का उपयोग करें

### मेमोरी समस्याएँ

कुछ पाठों को महत्वपूर्ण RAM (8GB+ अनुशंसित) की आवश्यकता होती है:
- संसाधन-गहन पाठों के लिए क्लाउड VMs का उपयोग करें
- मॉडल प्रशिक्षण करते समय अन्य एप्लिकेशन बंद करें
- यदि मेमोरी समाप्त हो रही है तो नोटबुक्स में बैच आकार कम करें

## अतिरिक्त नोट्स

### पाठ्यक्रम प्रशिक्षकों के लिए

- शिक्षण मार्गदर्शन के लिए `lessons/0-course-setup/for-teachers.md` देखें
- पाठ आत्म-निहित हैं और क्रम में या व्यक्तिगत रूप से चुने जा सकते हैं
- अनुमानित समय: प्रति सप्ताह 2 पाठ पर 12 सप्ताह

### क्लाउड संसाधन

- **Azure for Students:** छात्रों के लिए मुफ्त क्रेडिट उपलब्ध
- **Microsoft Learn:** पूरक शिक्षण पथ पूरे पाठ्यक्रम में लिंक किए गए
- **Binder:** मुफ्त लेकिन सीमित संसाधन और कुछ नेटवर्क प्रतिबंध

### कोड निष्पादन विकल्प

1. **स्थानीय (अनुशंसित):** पूर्ण नियंत्रण, सर्वोत्तम प्रदर्शन, GPU समर्थन
2. **GitHub Codespaces:** क्लाउड-आधारित VS Code, त्वरित एक्सेस के लिए अच्छा
3. **Binder:** ब्राउज़र-आधारित Jupyter, मुफ्त लेकिन सीमित
4. **Azure ML Notebooks:** GPU समर्थन के साथ एंटरप्राइज़ विकल्प
5. **Google Colab:** नोटबुक्स को व्यक्तिगत रूप से अपलोड करें, मुफ्त GPU टियर उपलब्ध

### नोटबुक्स के साथ काम करना

- नोटबुक्स को सीखने के लिए कोशिका-दर-कोशिका चलाने के लिए डिज़ाइन किया गया है
- कई नोटबुक्स पहली बार चलने पर डेटासेट डाउनलोड करती हैं (समय लग सकता है)
- कुछ मॉडलों को उचित प्रशिक्षण समय के लिए GPU की आवश्यकता होती है
- प्री-ट्रेंड मॉडल का उपयोग जहाँ संभव हो, कंप्यूट आवश्यकताओं को कम करने के लिए

### प्रदर्शन विचार

- बाद के कंप्यूटर विज़न पाठ (CNNs, GANs) GPU से लाभान्वित होते हैं
- NLP ट्रांसफॉर्मर पाठों को महत्वपूर्ण RAM की आवश्यकता हो सकती है
- स्क्रैच से प्रशिक्षण शैक्षिक है लेकिन समय लेने वाला है
- ट्रांसफर लर्निंग उदाहरण प्रशिक्षण समय को कम करते हैं

---

**अस्वीकरण**:  
यह दस्तावेज़ AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) का उपयोग करके अनुवादित किया गया है। जबकि हम सटीकता सुनिश्चित करने का प्रयास करते हैं, कृपया ध्यान दें कि स्वचालित अनुवाद में त्रुटियां या अशुद्धियां हो सकती हैं। मूल भाषा में उपलब्ध मूल दस्तावेज़ को प्रामाणिक स्रोत माना जाना चाहिए। महत्वपूर्ण जानकारी के लिए, पेशेवर मानव अनुवाद की सिफारिश की जाती है। इस अनुवाद के उपयोग से उत्पन्न किसी भी गलतफहमी या गलत व्याख्या के लिए हम उत्तरदायी नहीं हैं।