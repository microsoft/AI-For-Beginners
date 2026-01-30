# AGENTS.md

## प्रकल्पाचा आढावा

AI for Beginners हा 12 आठवड्यांचा, 24 धड्यांचा अभ्यासक्रम आहे जो कृत्रिम बुद्धिमत्तेच्या मूलभूत गोष्टींचा समावेश करतो. या शैक्षणिक संग्रहात Jupyter Notebooks, क्विझ आणि प्रॅक्टिकल लॅब्ससह व्यावहारिक धडे समाविष्ट आहेत. अभ्यासक्रमामध्ये खालील गोष्टींचा समावेश आहे:

- प्रतीकात्मक AI: ज्ञानाचे प्रतिनिधित्व आणि तज्ज्ञ प्रणाली
- न्यूरल नेटवर्क्स आणि TensorFlow व PyTorch सह डीप लर्निंग
- संगणकीय दृष्टिकोन तंत्र आणि आर्किटेक्चर
- नैसर्गिक भाषा प्रक्रिया (NLP): ट्रान्सफॉर्मर्स आणि BERT
- विशेष विषय: जेनेटिक अल्गोरिदम, रिइन्फोर्समेंट लर्निंग, मल्टी-एजंट सिस्टम्स
- AI नैतिकता आणि जबाबदार AI तत्त्वे

**मुख्य तंत्रज्ञान:** Python 3, Jupyter Notebooks, TensorFlow, PyTorch, Keras, OpenCV, Vue.js (क्विझ अ‍ॅपसाठी)

**आर्किटेक्चर:** Jupyter Notebooks मध्ये विषयानुसार व्यवस्थित शैक्षणिक सामग्री संग्रह, Vue.js-आधारित क्विझ अ‍ॅप आणि विस्तृत बहुभाषिक समर्थनासह.

## सेटअप कमांड्स

### प्राथमिक विकास वातावरण (Python/Jupyter)

अभ्यासक्रम Python आणि Jupyter Notebooks सह चालविण्यासाठी डिझाइन केलेला आहे. शिफारस केलेला दृष्टिकोन म्हणजे मिनिकोंडा वापरणे:

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

### पर्याय: devcontainer वापरणे

```bash
# Open in VS Code and select "Reopen in Container" when prompted
# The devcontainer will automatically set up the environment
```

### क्विझ अ‍ॅप सेटअप

क्विझ अ‍ॅप हे `etc/quiz-app/` मध्ये स्थित Vue.js आधारित स्वतंत्र अ‍ॅप आहे:

```bash
cd etc/quiz-app
npm install
npm run serve  # Development server
npm run build  # Production build
npm run lint   # Lint and fix files
```

## विकास कार्यप्रवाह

### Jupyter Notebooks सह काम करणे

1. **स्थानिक विकास:**
   - Conda वातावरण सक्रिय करा: `conda activate ai4beg`
   - Jupyter सुरू करा: `jupyter notebook` किंवा `jupyter lab`
   - धड्यांच्या फोल्डर्समध्ये जा आणि `.ipynb` फाइल्स उघडा
   - धड्यांचे अनुसरण करण्यासाठी सेल्स परस्पर चालवा

2. **VS Code सह Python विस्तार:**
   - VS Code मध्ये संग्रह उघडा
   - Python विस्तार स्थापित करा
   - VS Code स्वयंचलितपणे Conda वातावरण शोधतो आणि वापरतो
   - `.ipynb` फाइल्स थेट VS Code मध्ये उघडा

3. **क्लाउड विकास:**
   - **GitHub Codespaces:** "Code" → "Codespaces" → "Create codespace on main" वर क्लिक करा
   - **Binder:** README वर Binder बॅज वापरून ब्राउझरमध्ये सुरू करा
   - टीप: Binder मध्ये मर्यादित संसाधने आणि काही वेब प्रवेश निर्बंध आहेत

### प्रगत धड्यांसाठी GPU समर्थन

नंतरचे धडे GPU प्रवेगक वापरल्याने लक्षणीय लाभ मिळवतात:

- **Azure Data Science VM:** GPU समर्थनासह NC-सीरीज VM वापरा
- **Azure Machine Learning:** GPU संगणकासह नोटबुक वैशिष्ट्ये वापरा
- **Google Colab:** नोटबुक्स स्वतंत्रपणे अपलोड करा (फ्री GPU समर्थन आहे)

### क्विझ अ‍ॅप विकास

```bash
cd etc/quiz-app
npm run serve  # Hot-reload development server at http://localhost:8080
```

## चाचणी सूचना

हा शैक्षणिक संग्रह आहे जो शिक्षण सामग्रीवर केंद्रित आहे, पारंपरिक सॉफ्टवेअर चाचणीवर नाही. पारंपरिक चाचणी संच नाही.

### सत्यापन दृष्टिकोन:

1. **Jupyter Notebooks:** कोड उदाहरणे कार्य करतात याची खात्री करण्यासाठी सेल्स क्रमाने चालवा
2. **क्विझ अ‍ॅप चाचणी:** विकास सर्व्हरद्वारे मॅन्युअल चाचणी
3. **अनुवाद सत्यापन:** `translations/` फोल्डरमधील अनुवादित सामग्री तपासा
4. **क्विझ अ‍ॅप लिंटिंग:** `npm run lint` `etc/quiz-app/` मध्ये चालवा

### कोड उदाहरणे चालवणे:

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

- शैक्षणिक कोडसाठी मानक Python परंपरा
- शिक्षणाला प्राधान्य देणारा स्पष्ट, वाचनीय कोड
- मुख्य संकल्पना स्पष्ट करणारे टिप्पण्या
- Jupyter Notebook-अनुकूल: सेल्स शक्यतो स्वतंत्र असावेत
- धड्यांच्या सामग्रीसाठी कठोर लिंटिंग आवश्यकता नाही

### JavaScript/Vue.js (क्विझ अ‍ॅप)

- `etc/quiz-app/package.json` मध्ये ESLint कॉन्फिगरेशन
- समस्या तपासण्यासाठी आणि स्वयंचलितपणे दुरुस्त करण्यासाठी `npm run lint` चालवा
- Vue 2.x परंपरा
- घटक-आधारित आर्किटेक्चर

### फाइल्सचे आयोजन

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

## बिल्ड आणि वितरण

### Jupyter सामग्री

बिल्ड प्रक्रिया आवश्यक नाही - Jupyter Notebooks थेट चालवले जातात.

### क्विझ अ‍ॅप

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

### दस्तऐवजीकरण साइट

संग्रह Docsify वापरतो:
- `index.html` प्रवेश बिंदू म्हणून कार्य करते
- बिल्ड आवश्यक नाही - GitHub Pages द्वारे थेट सेवा दिली जाते
- प्रवेश येथे: https://microsoft.github.io/AI-For-Beginners/

## योगदान मार्गदर्शक तत्त्वे

### पुल विनंती प्रक्रिया

1. **शीर्षक स्वरूप:** बदलाचे स्पष्ट, वर्णनात्मक शीर्षक
2. **CLA आवश्यकता:** Microsoft CLA साइन केलेले असणे आवश्यक आहे (स्वयंचलित तपासणी)
3. **सामग्री मार्गदर्शक तत्त्वे:**
   - शैक्षणिक फोकस आणि नवशिक्यांसाठी अनुकूल दृष्टिकोन राखा
   - नोटबुक्समधील सर्व कोड उदाहरणे चाचणी करा
   - नोटबुक्स एंड-टू-एंड चालवण्याची खात्री करा
   - इंग्रजी सामग्री बदलल्यास अनुवाद अद्यतनित करा
4. **क्विझ अ‍ॅप बदल:** कमिट करण्यापूर्वी `npm run lint` चालवा

### अनुवाद योगदान

- GitHub Actions द्वारे co-op-translator वापरून अनुवाद स्वयंचलित आहेत
- मॅन्युअल अनुवाद `translations/<language-code>/` मध्ये जातात
- क्विझ अनुवाद `etc/quiz-app/src/assets/translations/` मध्ये
- समर्थित भाषा: 40+ भाषा (पूर्ण यादीसाठी README पहा)

### सक्रिय योगदान क्षेत्रे

`etc/CONTRIBUTING.md` मध्ये वर्तमान गरजा पहा:
- डीप रिइन्फोर्समेंट लर्निंग विभाग
- ऑब्जेक्ट डिटेक्शन सुधारणा
- नेम्ड एंटिटी रिकग्निशन उदाहरणे
- कस्टम एम्बेडिंग प्रशिक्षण नमुने

## वातावरण कॉन्फिगरेशन

### आवश्यक अवलंबित्व

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

### वातावरणीय चल

मूलभूत वापरासाठी कोणतेही विशेष वातावरणीय चल आवश्यक नाही.

Azure वितरणासाठी (क्विझ अ‍ॅप):
- `AZURE_STATIC_WEB_APPS_API_TOKEN` (Azure द्वारे स्वयंचलितपणे सेट केले जाते)

## डीबगिंग आणि समस्या निवारण

### सामान्य समस्या

**समस्या:** Conda वातावरण तयार करण्यात अयशस्वी
- **उपाय:** Conda प्रथम अद्यतनित करा: `conda update conda -y`
- पुरेशी डिस्क जागा सुनिश्चित करा (50GB शिफारस केलेली)

**समस्या:** Jupyter कर्नल सापडत नाही
- **उपाय:** 
  ```bash
  conda activate ai4beg
  python -m ipykernel install --user --name ai4beg
  ```

**समस्या:** नोटबुक्समध्ये GPU आढळत नाही
- **उपाय:** 
  - CUDA स्थापना सत्यापित करा: `nvidia-smi`
  - PyTorch GPU तपासा: `python -c "import torch; print(torch.cuda.is_available())"`
  - TensorFlow GPU तपासा: `python -c "import tensorflow as tf; print(tf.config.list_physical_devices('GPU'))"`

**समस्या:** क्विझ अ‍ॅप सुरू होत नाही
- **उपाय:**
  ```bash
  cd etc/quiz-app
  rm -rf node_modules package-lock.json
  npm install
  npm run serve
  ```

**समस्या:** Binder वेळ संपतो किंवा डाउनलोड्स ब्लॉक करतो
- **उपाय:** चांगल्या संसाधन प्रवेशासाठी GitHub Codespaces किंवा स्थानिक सेटअप वापरा

### मेमरी समस्या

काही धड्यांना लक्षणीय RAM आवश्यक आहे (8GB+ शिफारस केलेली):
- संसाधन-गहन धड्यांसाठी क्लाउड VM वापरा
- मॉडेल्स प्रशिक्षण करताना इतर अ‍ॅप्स बंद करा
- मेमरी कमी झाल्यास नोटबुक्समध्ये बॅच साइज कमी करा

## अतिरिक्त टीप

### अभ्यासक्रम प्रशिक्षकांसाठी

- शिक्षण मार्गदर्शनासाठी `lessons/0-course-setup/for-teachers.md` पहा
- धडे स्वतंत्र आहेत आणि क्रमाने शिकवले जाऊ शकतात किंवा स्वतंत्रपणे निवडले जाऊ शकतात
- अंदाजे वेळ: 12 आठवडे, दर आठवड्याला 2 धडे

### क्लाउड संसाधने

- **Azure for Students:** विद्यार्थ्यांसाठी मोफत क्रेडिट्स उपलब्ध
- **Microsoft Learn:** पूरक शिक्षण मार्ग लिंक केलेले
- **Binder:** मोफत पण मर्यादित संसाधने आणि काही नेटवर्क निर्बंध

### कोड कार्यान्वयन पर्याय

1. **स्थानिक (शिफारस केलेले):** पूर्ण नियंत्रण, सर्वोत्तम कार्यक्षमता, GPU समर्थन
2. **GitHub Codespaces:** क्लाउड-आधारित VS Code, जलद प्रवेशासाठी चांगले
3. **Binder:** ब्राउझर-आधारित Jupyter, मोफत पण मर्यादित
4. **Azure ML Notebooks:** GPU समर्थनासह एंटरप्राइझ पर्याय
5. **Google Colab:** नोटबुक्स स्वतंत्रपणे अपलोड करा, फ्री GPU स्तर उपलब्ध

### नोटबुक्ससह काम करणे

- नोटबुक्स शिकण्यासाठी सेल-बाय-सेल चालवण्यासाठी डिझाइन केलेले आहेत
- अनेक नोटबुक्स पहिल्या रनवर डेटासेट डाउनलोड करतात (वेळ लागू शकतो)
- काही मॉडेल्ससाठी GPU आवश्यक आहे जेणेकरून प्रशिक्षण वेळ वाजवी असेल
- प्री-ट्रेन केलेले मॉडेल्स शक्यतो वापरले जातात जेणेकरून संगणकीय आवश्यकता कमी होईल

### कार्यक्षमता विचार

- संगणकीय दृष्टिकोन धडे (CNNs, GANs) GPU वापरल्याने लाभ मिळतो
- NLP ट्रान्सफॉर्मर धड्यांना लक्षणीय RAM आवश्यक असू शकते
- स्क्रॅचपासून प्रशिक्षण शैक्षणिक आहे पण वेळखाऊ आहे
- ट्रान्सफर लर्निंग उदाहरणे प्रशिक्षण वेळ कमी करतात

---

**अस्वीकरण**:  
हा दस्तऐवज AI भाषांतर सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) वापरून भाषांतरित करण्यात आला आहे. आम्ही अचूकतेसाठी प्रयत्नशील असलो तरी कृपया लक्षात ठेवा की स्वयंचलित भाषांतरांमध्ये त्रुटी किंवा अचूकतेचा अभाव असू शकतो. मूळ भाषेतील दस्तऐवज हा अधिकृत स्रोत मानला जावा. महत्त्वाच्या माहितीसाठी व्यावसायिक मानवी भाषांतराची शिफारस केली जाते. या भाषांतराचा वापर करून उद्भवलेल्या कोणत्याही गैरसमज किंवा चुकीच्या अर्थासाठी आम्ही जबाबदार राहणार नाही.