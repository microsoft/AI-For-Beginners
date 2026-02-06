# AGENTS.md

## Projekt áttekintése

Az AI for Beginners egy átfogó, 12 hetes, 24 leckéből álló tananyag, amely az alapvető mesterséges intelligencia ismereteket fedi le. Ez az oktatási gyűjtemény gyakorlati leckéket tartalmaz Jupyter Notebooks segítségével, kvízeket és gyakorlati laborokat. A tananyag az alábbiakat tartalmazza:

- Szimbolikus AI tudásreprezentációval és szakértői rendszerekkel
- Neurális hálózatok és mélytanulás TensorFlow-val és PyTorch-csal
- Számítógépes látás technikák és architektúrák
- Természetes nyelvfeldolgozás (NLP), beleértve a transformereket és a BERT-et
- Speciális témák: genetikus algoritmusok, megerősítéses tanulás, többügynökös rendszerek
- AI etika és felelős AI elvek

**Kulcstechnológiák:** Python 3, Jupyter Notebooks, TensorFlow, PyTorch, Keras, OpenCV, Vue.js (kvíz alkalmazáshoz)

**Architektúra:** Oktatási tartalomgyűjtemény Jupyter Notebooks formájában, témakörök szerint rendezve, kiegészítve egy Vue.js alapú kvíz alkalmazással és kiterjedt többnyelvű támogatással.

## Telepítési parancsok

### Elsődleges fejlesztési környezet (Python/Jupyter)

A tananyag Python és Jupyter Notebooks használatára van tervezve. Az ajánlott megközelítés a miniconda használata:

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

### Alternatíva: devcontainer használata

```bash
# Open in VS Code and select "Reopen in Container" when prompted
# The devcontainer will automatically set up the environment
```

### Kvíz alkalmazás telepítése

A kvíz alkalmazás egy különálló Vue.js alkalmazás, amely az `etc/quiz-app/` mappában található:

```bash
cd etc/quiz-app
npm install
npm run serve  # Development server
npm run build  # Production build
npm run lint   # Lint and fix files
```

## Fejlesztési munkafolyamat

### Jupyter Notebooks használata

1. **Helyi fejlesztés:**
   - Aktiváld a conda környezetet: `conda activate ai4beg`
   - Indítsd el a Jupyter-t: `jupyter notebook` vagy `jupyter lab`
   - Navigálj a lecke mappákhoz, és nyisd meg a `.ipynb` fájlokat
   - Futtasd interaktívan a cellákat a leckék követéséhez

2. **VS Code Python bővítménnyel:**
   - Nyisd meg a gyűjteményt a VS Code-ban
   - Telepítsd a Python bővítményt
   - A VS Code automatikusan felismeri és használja a conda környezetet
   - Nyisd meg közvetlenül a `.ipynb` fájlokat a VS Code-ban

3. **Felhő alapú fejlesztés:**
   - **GitHub Codespaces:** Kattints a "Code" → "Codespaces" → "Create codespace on main" opcióra
   - **Binder:** Használd a Binder jelvényt a README-ben a böngészőben való indításhoz
   - Megjegyzés: A Binder korlátozott erőforrásokkal rendelkezik, és néhány webes hozzáférési korlátozással

### GPU támogatás haladó leckékhez

A későbbi leckék jelentősen profitálnak a GPU gyorsításból:

- **Azure Data Science VM:** Használj NC-sorozatú VM-eket GPU támogatással
- **Azure Machine Learning:** Használj notebook funkciókat GPU számítással
- **Google Colab:** Töltsd fel egyenként a notebookokat (ingyenes GPU támogatás)

### Kvíz alkalmazás fejlesztése

```bash
cd etc/quiz-app
npm run serve  # Hot-reload development server at http://localhost:8080
```

## Tesztelési utasítások

Ez egy oktatási gyűjtemény, amely a tanulási tartalomra összpontosít, nem pedig a szoftver tesztelésére. Nincs hagyományos tesztcsomag.

### Érvényesítési megközelítések:

1. **Jupyter Notebooks:** Futtasd a cellákat sorban, hogy ellenőrizd a kódpéldák működését
2. **Kvíz alkalmazás tesztelése:** Manuális tesztelés fejlesztési szerveren keresztül
3. **Fordítás érvényesítése:** Ellenőrizd a fordított tartalmat a `translations/` mappában
4. **Kvíz alkalmazás lintelése:** `npm run lint` az `etc/quiz-app/` mappában

### Kódpéldák futtatása:

```bash
# Activate environment first
conda activate ai4beg

# Run Python scripts directly
python lessons/4-ComputerVision/07-ConvNets/pytorchcv.py

# Or execute notebooks
jupyter notebook lessons/3-NeuralNetworks/03-Perceptron/Perceptron.ipynb
```

## Kódstílus

### Python kódstílus

- Standard Python konvenciók oktatási kódhoz
- Tiszta, érthető kód, amely a tanulást helyezi előtérbe az optimalizációval szemben
- Kommentek, amelyek kulcsfogalmakat magyaráznak
- Jupyter Notebook-barát: a cellák lehetőség szerint önállóak legyenek
- Nincs szigorú lintelési követelmény a lecke tartalomhoz

### JavaScript/Vue.js (Kvíz alkalmazás)

- ESLint konfiguráció az `etc/quiz-app/package.json` fájlban
- Futtasd az `npm run lint` parancsot a problémák ellenőrzéséhez és automatikus javításához
- Vue 2.x konvenciók
- Komponens alapú architektúra

### Fájlok szervezése

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

## Build és telepítés

### Jupyter tartalom

Nincs szükség build folyamatra - a Jupyter Notebooks közvetlenül futtatható.

### Kvíz alkalmazás

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

### Dokumentációs oldal

A gyűjtemény Docsify-t használ a dokumentációhoz:
- Az `index.html` szolgál belépési pontként
- Nincs szükség buildre - közvetlenül a GitHub Pages-en keresztül szolgáltatva
- Elérhető itt: https://microsoft.github.io/AI-For-Beginners/

## Hozzájárulási irányelvek

### Pull Request folyamat

1. **Cím formátuma:** Tiszta, leíró címek, amelyek a változást ismertetik
2. **CLA követelmény:** A Microsoft CLA-t alá kell írni (automatikus ellenőrzés)
3. **Tartalmi irányelvek:**
   - Tartsd meg az oktatási fókuszt és a kezdőbarát megközelítést
   - Teszteld az összes kódpéldát a notebookokban
   - Biztosítsd, hogy a notebookok végigfutnak
   - Frissítsd a fordításokat, ha módosítod az angol tartalmat
4. **Kvíz alkalmazás változtatások:** Futtasd az `npm run lint` parancsot a commit előtt

### Fordítási hozzájárulások

- A fordításokat GitHub Actions automatizálja a co-op-translator segítségével
- Manuális fordítások a `translations/<language-code>/` mappába kerülnek
- Kvíz fordítások az `etc/quiz-app/src/assets/translations/` mappába kerülnek
- Támogatott nyelvek: 40+ nyelv (lásd README a teljes listáért)

### Aktív hozzájárulási területek

Lásd az `etc/CONTRIBUTING.md` fájlt az aktuális igényekért:
- Mély megerősítéses tanulás szekciók
- Objektumfelismerés fejlesztések
- Névelem felismerés példák
- Egyedi embedding tréning minták

## Környezet konfiguráció

### Szükséges függőségek

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

### Környezeti változók

Nincs szükség speciális környezeti változókra az alapvető használathoz.

Azure telepítésekhez (kvíz alkalmazás):
- `AZURE_STATIC_WEB_APPS_API_TOKEN` (automatikusan beállítva Azure által)

## Hibakeresés és problémamegoldás

### Gyakori problémák

**Probléma:** Conda környezet létrehozása sikertelen
- **Megoldás:** Frissítsd először a condát: `conda update conda -y`
- Biztosíts elegendő lemezterületet (ajánlott: 50GB)

**Probléma:** Jupyter kernel nem található
- **Megoldás:** 
  ```bash
  conda activate ai4beg
  python -m ipykernel install --user --name ai4beg
  ```

**Probléma:** GPU nem észlelhető a notebookokban
- **Megoldás:** 
  - Ellenőrizd a CUDA telepítést: `nvidia-smi`
  - Ellenőrizd a PyTorch GPU-t: `python -c "import torch; print(torch.cuda.is_available())"`
  - Ellenőrizd a TensorFlow GPU-t: `python -c "import tensorflow as tf; print(tf.config.list_physical_devices('GPU'))"`

**Probléma:** Kvíz alkalmazás nem indul
- **Megoldás:**
  ```bash
  cd etc/quiz-app
  rm -rf node_modules package-lock.json
  npm install
  npm run serve
  ```

**Probléma:** Binder időtúllépés vagy letöltési blokkok
- **Megoldás:** Használj GitHub Codespaces-t vagy helyi beállítást a jobb erőforrás-hozzáférés érdekében

### Memória problémák

Néhány lecke jelentős RAM-ot igényel (ajánlott: 8GB+):
- Használj felhő alapú VM-eket az erőforrásigényes leckékhez
- Zárd be más alkalmazásokat modellek tanítása közben
- Csökkentsd a batch méreteket a notebookokban, ha kifogysz a memóriából

## További megjegyzések

### Tanfolyam oktatóknak

- Lásd a `lessons/0-course-setup/for-teachers.md` fájlt oktatási útmutatóért
- A leckék önállóak, és sorrendben vagy egyenként választhatók
- Becsült idő: 12 hét, heti 2 lecke

### Felhő erőforrások

- **Azure for Students:** Ingyenes kreditek elérhetők diákok számára
- **Microsoft Learn:** Kiegészítő tanulási útvonalak linkelve
- **Binder:** Ingyenes, de korlátozott erőforrásokkal és néhány hálózati korlátozással

### Kód futtatási lehetőségek

1. **Helyi (Ajánlott):** Teljes kontroll, legjobb teljesítmény, GPU támogatás
2. **GitHub Codespaces:** Felhő alapú VS Code, gyors hozzáféréshez
3. **Binder:** Böngésző alapú Jupyter, ingyenes, de korlátozott
4. **Azure ML Notebooks:** Vállalati opció GPU támogatással
5. **Google Colab:** Töltsd fel egyenként a notebookokat, ingyenes GPU szint elérhető

### Notebookok használata

- A notebookok cellánkénti futtatásra vannak tervezve tanulási célból
- Sok notebook első futtatáskor adatokat tölt le (időigényes lehet)
- Néhány modell GPU-t igényel a megfelelő tanítási idő érdekében
- Előre betanított modellek használata csökkenti a számítási igényt

### Teljesítmény szempontok

- A későbbi számítógépes látás leckék (CNN-ek, GAN-ek) GPU-t igényelnek
- Az NLP transformer leckék jelentős RAM-ot igényelhetnek
- A nulláról való tanítás oktató jellegű, de időigényes
- Az átvitel tanulási példák minimalizálják a tanítási időt

---

**Felelősségi nyilatkozat**:  
Ez a dokumentum az [Co-op Translator](https://github.com/Azure/co-op-translator) AI fordítási szolgáltatás segítségével került lefordításra. Bár törekszünk a pontosságra, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az eredeti nyelvén tekintendő hiteles forrásnak. Kritikus információk esetén javasolt professzionális emberi fordítást igénybe venni. Nem vállalunk felelősséget semmilyen félreértésért vagy téves értelmezésért, amely a fordítás használatából eredhet.