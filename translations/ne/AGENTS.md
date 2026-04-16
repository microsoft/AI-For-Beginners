# AGENTS.md

## परियोजना अवलोकन

AI for Beginners एक व्यापक १२ हप्ताको, २४ पाठको पाठ्यक्रम हो जसले कृत्रिम बुद्धिमत्ताको आधारभूत कुराहरू समेट्छ। यो शैक्षिक रिपोजिटरीले Jupyter Notebooks, क्विजहरू, र प्रयोगात्मक प्रयोगशालाहरू प्रयोग गरेर व्यावहारिक पाठहरू समावेश गर्दछ। पाठ्यक्रमले निम्न विषयहरू समेट्छ:

- प्रतीकात्मक AI: ज्ञान प्रतिनिधित्व र विशेषज्ञ प्रणालीहरू
- न्युरल नेटवर्क र TensorFlow तथा PyTorch प्रयोग गरेर गहिरो शिक्षण
- कम्प्युटर भिजन प्रविधिहरू र आर्किटेक्चरहरू
- प्राकृतिक भाषा प्रशोधन (NLP): ट्रान्सफर्मरहरू र BERT समावेश
- विशेष विषयहरू: जेनेटिक एल्गोरिदम, सुदृढीकरण शिक्षण, बहु-एजेन्ट प्रणालीहरू
- AI नैतिकता र जिम्मेवार AI सिद्धान्तहरू

**मुख्य प्रविधिहरू:** Python 3, Jupyter Notebooks, TensorFlow, PyTorch, Keras, OpenCV, Vue.js (क्विज एपका लागि)

**आर्किटेक्चर:** शैक्षिक सामग्री रिपोजिटरी, Jupyter Notebooks विषय क्षेत्रहरूद्वारा व्यवस्थित, Vue.js आधारित क्विज एप र बहु-भाषा समर्थनको साथ।

## सेटअप कमाण्डहरू

### प्राथमिक विकास वातावरण (Python/Jupyter)

पाठ्यक्रम Python र Jupyter Notebooks प्रयोग गरेर चलाउन डिजाइन गरिएको छ। सिफारिस गरिएको विधि मिनिकन्डा प्रयोग गर्नु हो:

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

### वैकल्पिक: devcontainer प्रयोग गर्दै

```bash
# Open in VS Code and select "Reopen in Container" when prompted
# The devcontainer will automatically set up the environment
```

### क्विज एप सेटअप

क्विज एप `etc/quiz-app/` मा रहेको अलग Vue.js एप हो:

```bash
cd etc/quiz-app
npm install
npm run serve  # Development server
npm run build  # Production build
npm run lint   # Lint and fix files
```

## विकास कार्यप्रवाह

### Jupyter Notebooks सँग काम गर्दै

1. **स्थानीय विकास:**
   - कन्डा वातावरण सक्रिय गर्नुहोस्: `conda activate ai4beg`
   - Jupyter सुरु गर्नुहोस्: `jupyter notebook` वा `jupyter lab`
   - पाठ फोल्डरहरूमा नेभिगेट गर्नुहोस् र `.ipynb` फाइलहरू खोल्नुहोस्
   - पाठहरू अनुसरण गर्न अन्तरक्रियात्मक रूपमा सेलहरू चलाउनुहोस्

2. **VS Code सँग Python विस्तार:**
   - रिपोजिटरी VS Code मा खोल्नुहोस्
   - Python विस्तार स्थापना गर्नुहोस्
   - VS Code ले स्वतः कन्डा वातावरण पत्ता लगाउँछ र प्रयोग गर्दछ
   - `.ipynb` फाइलहरू सीधा VS Code मा खोल्नुहोस्

3. **क्लाउड विकास:**
   - **GitHub Codespaces:** "Code" → "Codespaces" → "Create codespace on main" क्लिक गर्नुहोस्
   - **Binder:** README मा Binder ब्याज प्रयोग गरेर ब्राउजरमा सुरु गर्नुहोस्
   - नोट: Binder मा सीमित स्रोतहरू र केही वेब पहुँच प्रतिबन्धहरू छन्

### GPU समर्थन उन्नत पाठहरूको लागि

पछिल्ला पाठहरूले GPU एक्सेलेरेशनबाट धेरै फाइदा लिन्छन्:

- **Azure Data Science VM:** GPU समर्थनसहित NC-शृंखला VM प्रयोग गर्नुहोस्
- **Azure Machine Learning:** GPU कम्प्युटसहित नोटबुक सुविधाहरू प्रयोग गर्नुहोस्
- **Google Colab:** व्यक्तिगत रूपमा नोटबुकहरू अपलोड गर्नुहोस् (निःशुल्क GPU समर्थन छ)

### क्विज एप विकास

```bash
cd etc/quiz-app
npm run serve  # Hot-reload development server at http://localhost:8080
```

## परीक्षण निर्देशनहरू

यो शैक्षिक रिपोजिटरी शिक्षण सामग्रीमा केन्द्रित छ, परम्परागत सफ्टवेयर परीक्षणमा होइन। यहाँ कुनै परम्परागत परीक्षण सूट छैन।

### मान्यकरण विधिहरू:

1. **Jupyter Notebooks:** कोड उदाहरणहरू काम गर्छन् भनेर पुष्टि गर्न क्रमिक रूपमा सेलहरू चलाउनुहोस्
2. **क्विज एप परीक्षण:** विकास सर्भर मार्फत म्यानुअल परीक्षण
3. **अनुवाद मान्यकरण:** `translations/` फोल्डरमा अनुवादित सामग्री जाँच गर्नुहोस्
4. **क्विज एप लिन्टिङ:** `npm run lint` `etc/quiz-app/` मा चलाउनुहोस्

### कोड उदाहरणहरू चलाउँदै:

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

- शैक्षिक कोडका लागि मानक Python परम्पराहरू
- स्पष्ट, पढ्न सजिलो कोड, अनुकूलनभन्दा सिकाइलाई प्राथमिकता दिने
- प्रमुख अवधारणाहरू व्याख्या गर्ने टिप्पणीहरू
- Jupyter Notebook-अनुकूल: सेलहरू जहाँसम्म सम्भव छ आत्म-निहित हुनुपर्छ
- पाठ सामग्रीका लागि कडा लिन्टिङ आवश्यकताहरू छैनन्

### JavaScript/Vue.js (क्विज एप)

- `etc/quiz-app/package.json` मा ESLint कन्फिगरेसन
- `npm run lint` चलाएर समस्या जाँच र स्वतः सुधार गर्नुहोस्
- Vue 2.x परम्पराहरू
- कम्पोनेन्ट-आधारित आर्किटेक्चर

### फाइल संगठन

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

## निर्माण र परिनियोजन

### Jupyter सामग्री

कुनै निर्माण प्रक्रिया आवश्यक छैन - Jupyter Notebooks सीधा चलाइन्छ।

### क्विज एप

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

### दस्तावेजीकरण साइट

रिपोजिटरीले Docsify प्रयोग गरेर दस्तावेजीकरण गर्दछ:
- `index.html` प्रवेश बिन्दुको रूपमा सेवा गर्दछ
- कुनै निर्माण आवश्यक छैन - GitHub Pages मार्फत सीधा सेवा दिइन्छ
- पहुँच: https://microsoft.github.io/AI-For-Beginners/

## योगदान दिशानिर्देशहरू

### पुल अनुरोध प्रक्रिया

1. **शीर्षक ढाँचा:** परिवर्तनलाई वर्णन गर्ने स्पष्ट, वर्णनात्मक शीर्षकहरू
2. **CLA आवश्यकता:** Microsoft CLA हस्ताक्षर गर्नुपर्छ (स्वचालित जाँच)
3. **सामग्री दिशानिर्देशहरू:**
   - शैक्षिक फोकस र प्रारम्भिक-अनुकूल दृष्टिकोण कायम राख्नुहोस्
   - नोटबुकहरूमा सबै कोड उदाहरणहरू परीक्षण गर्नुहोस्
   - नोटबुकहरू अन्त-देखि-अन्त चल्छन् भनेर सुनिश्चित गर्नुहोस्
   - अंग्रेजी सामग्री परिमार्जन गर्दा अनुवाद अद्यावधिक गर्नुहोस्
4. **क्विज एप परिवर्तनहरू:** प्रतिबद्ध गर्नु अघि `npm run lint` चलाउनुहोस्

### अनुवाद योगदानहरू

- अनुवादहरू GitHub Actions मार्फत स्वचालित रूपमा गरिन्छ co-op-translator प्रयोग गरेर
- म्यानुअल अनुवादहरू `translations/<language-code>/` मा जान्छन्
- क्विज अनुवादहरू `etc/quiz-app/src/assets/translations/` मा
- समर्थित भाषाहरू: ४०+ भाषाहरू (पूर्ण सूचीको लागि README हेर्नुहोस्)

### सक्रिय योगदान क्षेत्रहरू

`etc/CONTRIBUTING.md` मा हालको आवश्यकताहरू हेर्नुहोस्:
- गहिरो सुदृढीकरण शिक्षण खण्डहरू
- वस्तु पहिचान सुधारहरू
- नामित इकाई पहिचान उदाहरणहरू
- अनुकूल एम्बेडिङ प्रशिक्षण नमूनाहरू

## वातावरण कन्फिगरेसन

### आवश्यक निर्भरताहरू

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

### वातावरण चरहरू

आधारभूत प्रयोगको लागि कुनै विशेष वातावरण चरहरू आवश्यक छैनन्।

Azure परिनियोजनहरूको लागि (क्विज एप):
- `AZURE_STATIC_WEB_APPS_API_TOKEN` (Azure द्वारा स्वचालित रूपमा सेट गरिन्छ)

## डिबगिङ र समस्या समाधान

### सामान्य समस्याहरू

**समस्या:** कन्डा वातावरण सिर्जना असफल भयो
- **समाधान:** पहिले कन्डा अद्यावधिक गर्नुहोस्: `conda update conda -y`
- पर्याप्त डिस्क स्थान सुनिश्चित गर्नुहोस् (५०GB सिफारिस)

**समस्या:** Jupyter कर्नेल फेला परेन
- **समाधान:** 
  ```bash
  conda activate ai4beg
  python -m ipykernel install --user --name ai4beg
  ```

**समस्या:** नोटबुकहरूमा GPU पत्ता लागेन
- **समाधान:** 
  - CUDA स्थापना पुष्टि गर्नुहोस्: `nvidia-smi`
  - PyTorch GPU जाँच गर्नुहोस्: `python -c "import torch; print(torch.cuda.is_available())"`
  - TensorFlow GPU जाँच गर्नुहोस्: `python -c "import tensorflow as tf; print(tf.config.list_physical_devices('GPU'))"`

**समस्या:** क्विज एप सुरु भएन
- **समाधान:**
  ```bash
  cd etc/quiz-app
  rm -rf node_modules package-lock.json
  npm install
  npm run serve
  ```

**समस्या:** Binder समय समाप्त भयो वा डाउनलोडहरू रोकियो
- **समाधान:** GitHub Codespaces वा स्थानीय सेटअप प्रयोग गर्नुहोस् राम्रो स्रोत पहुँचको लागि

### मेमोरी समस्याहरू

केही पाठहरूले महत्वपूर्ण RAM (८GB+ सिफारिस) आवश्यक छ:
- स्रोत-गहन पाठहरूको लागि क्लाउड VM प्रयोग गर्नुहोस्
- मोडेलहरू प्रशिक्षण गर्दा अन्य एप्लिकेसनहरू बन्द गर्नुहोस्
- यदि मेमोरी सकिन्छ भने नोटबुकहरूमा ब्याच साइज घटाउनुहोस्

## थप नोटहरू

### पाठ्यक्रम प्रशिक्षकहरूको लागि

- शिक्षण मार्गदर्शनको लागि `lessons/0-course-setup/for-teachers.md` हेर्नुहोस्
- पाठहरू आत्म-निहित छन् र क्रमशः वा व्यक्तिगत रूपमा चयन गरेर सिकाउन सकिन्छ
- अनुमानित समय: १२ हप्ता, हरेक हप्ता २ पाठ

### क्लाउड स्रोतहरू

- **Azure for Students:** विद्यार्थीहरूका लागि निःशुल्क क्रेडिट उपलब्ध
- **Microsoft Learn:** पूरक सिकाइ मार्गहरू लिंक गरिएको
- **Binder:** निःशुल्क तर सीमित स्रोतहरू र केही नेटवर्क प्रतिबन्धहरू

### कोड कार्यान्वयन विकल्पहरू

1. **स्थानीय (सिफारिस गरिएको):** पूर्ण नियन्त्रण, उत्कृष्ट प्रदर्शन, GPU समर्थन
2. **GitHub Codespaces:** क्लाउड-आधारित VS Code, छिटो पहुँचको लागि राम्रो
3. **Binder:** ब्राउजर-आधारित Jupyter, निःशुल्क तर सीमित
4. **Azure ML Notebooks:** GPU समर्थनसहित उद्यम विकल्प
5. **Google Colab:** व्यक्तिगत रूपमा नोटबुकहरू अपलोड गर्नुहोस्, निःशुल्क GPU स्तर उपलब्ध

### नोटबुकहरूसँग काम गर्दै

- नोटबुकहरू सिकाइका लागि सेल-दर-सेल चलाउन डिजाइन गरिएको छ
- धेरै नोटबुकहरूले पहिलो पटक चलाउँदा डेटासेटहरू डाउनलोड गर्छन् (समय लाग्न सक्छ)
- केही मोडेलहरू प्रशिक्षणका लागि GPU आवश्यक छ
- पूर्व-प्रशिक्षित मोडेलहरू जहाँसम्म सम्भव छ प्रयोग गरिन्छ कम्प्युट आवश्यकताहरू घटाउन

### प्रदर्शन विचारहरू

- कम्प्युटर भिजनका पछिल्ला पाठहरू (CNNs, GANs) GPU बाट फाइदा लिन्छन्
- NLP ट्रान्सफर्मर पाठहरूले महत्वपूर्ण RAM आवश्यक हुन सक्छ
- स्क्र्याचबाट प्रशिक्षण शैक्षिक छ तर समय-लाग्दो छ
- ट्रान्सफर शिक्षण उदाहरणहरूले प्रशिक्षण समय कम गर्छन्

---

**अस्वीकरण**:  
यो दस्तावेज़ AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) प्रयोग गरी अनुवाद गरिएको हो। हामी यथासम्भव सटीकता सुनिश्चित गर्न प्रयास गर्छौं, तर कृपया ध्यान दिनुहोस् कि स्वचालित अनुवादहरूमा त्रुटि वा अशुद्धता हुन सक्छ। यसको मूल भाषामा रहेको मूल दस्तावेज़लाई आधिकारिक स्रोत मानिनुपर्छ। महत्त्वपूर्ण जानकारीका लागि, व्यावसायिक मानव अनुवाद सिफारिस गरिन्छ। यस अनुवादको प्रयोगबाट उत्पन्न हुने कुनै पनि गलतफहमी वा गलत व्याख्याको लागि हामी जिम्मेवार हुने छैनौं।