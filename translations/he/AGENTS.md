# AGENTS.md

## סקירת הפרויקט

AI for Beginners הוא תוכנית לימודים מקיפה בת 12 שבועות ו-24 שיעורים המכסה את יסודות הבינה המלאכותית. מאגר חינוכי זה כולל שיעורים מעשיים באמצעות Jupyter Notebooks, חידונים ומעבדות מעשיות. התוכנית כוללת:

- בינה מלאכותית סימבולית עם ייצוג ידע ומערכות מומחה
- רשתות נוירונים ולמידה עמוקה עם TensorFlow ו-PyTorch
- טכניקות וארכיטקטורות של ראייה ממוחשבת
- עיבוד שפה טבעית (NLP) כולל transformers ו-BERT
- נושאים מתקדמים: אלגוריתמים גנטיים, למידה מחזקת, מערכות מרובות סוכנים
- אתיקה בבינה מלאכותית ועקרונות AI אחראי

**טכנולוגיות מרכזיות:** Python 3, Jupyter Notebooks, TensorFlow, PyTorch, Keras, OpenCV, Vue.js (לאפליקציית החידונים)

**ארכיטקטורה:** מאגר תוכן חינוכי עם Jupyter Notebooks מאורגנים לפי תחומי נושא, בתוספת אפליקציית חידונים מבוססת Vue.js ותמיכה רחבה בריבוי שפות.

## פקודות התקנה

### סביבת פיתוח ראשית (Python/Jupyter)

התוכנית מיועדת להרצה עם Python ו-Jupyter Notebooks. הגישה המומלצת היא שימוש ב-miniconda:

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

### חלופה: שימוש ב-devcontainer

```bash
# Open in VS Code and select "Reopen in Container" when prompted
# The devcontainer will automatically set up the environment
```

### התקנת אפליקציית החידונים

אפליקציית החידונים היא אפליקציית Vue.js נפרדת הממוקמת ב-`etc/quiz-app/`:

```bash
cd etc/quiz-app
npm install
npm run serve  # Development server
npm run build  # Production build
npm run lint   # Lint and fix files
```

## זרימת עבודה בפיתוח

### עבודה עם Jupyter Notebooks

1. **פיתוח מקומי:**
   - הפעלת סביבת conda: `conda activate ai4beg`
   - הפעלת Jupyter: `jupyter notebook` או `jupyter lab`
   - ניווט לתיקיות השיעורים ופתיחת קבצי `.ipynb`
   - הרצת תאים באופן אינטראקטיבי כדי לעקוב אחר השיעורים

2. **VS Code עם הרחבת Python:**
   - פתיחת המאגר ב-VS Code
   - התקנת הרחבת Python
   - VS Code מזהה ומשתמש אוטומטית בסביבת conda
   - פתיחת קבצי `.ipynb` ישירות ב-VS Code

3. **פיתוח בענן:**
   - **GitHub Codespaces:** לחיצה על "Code" → "Codespaces" → "Create codespace on main"
   - **Binder:** שימוש בתג Binder ב-README כדי להפעיל בדפדפן
   - הערה: ל-Binder יש משאבים מוגבלים ומגבלות גישה מסוימות לאינטרנט

### תמיכה ב-GPU לשיעורים מתקדמים

שיעורים מאוחרים יותר נהנים משמעותית מהאצת GPU:

- **Azure Data Science VM:** שימוש ב-NC-series VMs עם תמיכה ב-GPU
- **Azure Machine Learning:** שימוש בתכונות מחברת עם חישוב GPU
- **Google Colab:** העלאת מחברות בנפרד (תמיכה חינמית ב-GPU)

### פיתוח אפליקציית החידונים

```bash
cd etc/quiz-app
npm run serve  # Hot-reload development server at http://localhost:8080
```

## הוראות בדיקה

זהו מאגר חינוכי המתמקד בתוכן לימודי ולא בבדיקת תוכנה. אין מערך בדיקות מסורתי.

### גישות אימות:

1. **Jupyter Notebooks:** הרצת תאים ברצף כדי לוודא שדוגמאות הקוד פועלות
2. **בדיקת אפליקציית החידונים:** בדיקה ידנית דרך שרת הפיתוח
3. **אימות תרגומים:** בדיקת תוכן מתורגם בתיקיית `translations/`
4. **Linting לאפליקציית החידונים:** `npm run lint` ב-`etc/quiz-app/`

### הרצת דוגמאות קוד:

```bash
# Activate environment first
conda activate ai4beg

# Run Python scripts directly
python lessons/4-ComputerVision/07-ConvNets/pytorchcv.py

# Or execute notebooks
jupyter notebook lessons/3-NeuralNetworks/03-Perceptron/Perceptron.ipynb
```

## סגנון קוד

### סגנון קוד Python

- מוסכמות Python סטנדרטיות לקוד חינוכי
- קוד ברור וקריא המעדיף למידה על פני אופטימיזציה
- הערות המסבירות מושגים מרכזיים
- ידידותי ל-Jupyter Notebook: תאים צריכים להיות עצמאיים ככל האפשר
- אין דרישות linting מחמירות לתוכן השיעורים

### JavaScript/Vue.js (אפליקציית החידונים)

- תצורת ESLint ב-`etc/quiz-app/package.json`
- הרצת `npm run lint` לבדיקה ותיקון אוטומטי של בעיות
- מוסכמות Vue 2.x
- ארכיטקטורה מבוססת רכיבים

### ארגון קבצים

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

## בנייה ופריסה

### תוכן Jupyter

אין צורך בתהליך בנייה - Jupyter Notebooks מבוצעים ישירות.

### אפליקציית החידונים

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

### אתר תיעוד

המאגר משתמש ב-Docsify לתיעוד:
- `index.html` משמש כנקודת כניסה
- אין צורך בבנייה - מוגש ישירות דרך GitHub Pages
- גישה בכתובת: https://microsoft.github.io/AI-For-Beginners/

## הנחיות לתרומה

### תהליך Pull Request

1. **פורמט כותרת:** כותרות ברורות ותיאוריות המתארות את השינוי
2. **דרישת CLA:** יש לחתום על Microsoft CLA (בדיקה אוטומטית)
3. **הנחיות תוכן:**
   - שמירה על מיקוד חינוכי וגישה ידידותית למתחילים
   - בדיקת כל דוגמאות הקוד במחברות
   - הבטחת הרצת מחברות מקצה לקצה
   - עדכון תרגומים אם משנים תוכן באנגלית
4. **שינויים באפליקציית החידונים:** הרצת `npm run lint` לפני התחייבות

### תרומות תרגום

- תרגומים מתבצעים אוטומטית דרך GitHub Actions באמצעות co-op-translator
- תרגומים ידניים נכנסים ל-`translations/<language-code>/`
- תרגומי חידונים ב-`etc/quiz-app/src/assets/translations/`
- שפות נתמכות: יותר מ-40 שפות (ראו README לרשימה מלאה)

### תחומי תרומה פעילים

ראו `etc/CONTRIBUTING.md` לצרכים הנוכחיים:
- חלקי למידה מחזקת עמוקה
- שיפורים בזיהוי אובייקטים
- דוגמאות לזיהוי ישויות בשם
- דוגמאות אימון מותאמות להטמעה

## תצורת סביבה

### תלות נדרשת

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

### משתני סביבה

אין צורך במשתני סביבה מיוחדים לשימוש בסיסי.

לפריסות Azure (אפליקציית החידונים):
- `AZURE_STATIC_WEB_APPS_API_TOKEN` (מוגדר אוטומטית על ידי Azure)

## איתור באגים ופתרון בעיות

### בעיות נפוצות

**בעיה:** יצירת סביבת conda נכשלת
- **פתרון:** עדכון conda תחילה: `conda update conda -y`
- הבטחת שטח דיסק מספיק (מומלץ 50GB)

**בעיה:** Kernel של Jupyter לא נמצא
- **פתרון:** 
  ```bash
  conda activate ai4beg
  python -m ipykernel install --user --name ai4beg
  ```

**בעיה:** GPU לא מזוהה במחברות
- **פתרון:** 
  - אימות התקנת CUDA: `nvidia-smi`
  - בדיקת GPU ב-PyTorch: `python -c "import torch; print(torch.cuda.is_available())"`
  - בדיקת GPU ב-TensorFlow: `python -c "import tensorflow as tf; print(tf.config.list_physical_devices('GPU'))"`

**בעיה:** אפליקציית החידונים לא מתחילה
- **פתרון:**
  ```bash
  cd etc/quiz-app
  rm -rf node_modules package-lock.json
  npm install
  npm run serve
  ```

**בעיה:** Binder מתנתק או חוסם הורדות
- **פתרון:** שימוש ב-GitHub Codespaces או התקנה מקומית לגישה טובה יותר למשאבים

### בעיות זיכרון

חלק מהשיעורים דורשים זיכרון RAM משמעותי (מומלץ 8GB+):
- שימוש ב-VMs בענן לשיעורים עתירי משאבים
- סגירת יישומים אחרים בעת אימון מודלים
- הקטנת גודל קבוצות במחברות אם נגמר הזיכרון

## הערות נוספות

### למדריכי הקורס

- ראו `lessons/0-course-setup/for-teachers.md` להנחיות הוראה
- השיעורים עצמאיים וניתן ללמד אותם ברצף או לבחור בנפרד
- זמן משוער: 12 שבועות עם 2 שיעורים בשבוע

### משאבי ענן

- **Azure for Students:** קרדיטים חינמיים זמינים לסטודנטים
- **Microsoft Learn:** מסלולי לימוד משלימים מקושרים לאורך הקורס
- **Binder:** חינמי אך עם משאבים מוגבלים ומגבלות רשת מסוימות

### אפשרויות הרצת קוד

1. **מקומי (מומלץ):** שליטה מלאה, ביצועים מיטביים, תמיכה ב-GPU
2. **GitHub Codespaces:** VS Code מבוסס ענן, טוב לגישה מהירה
3. **Binder:** Jupyter מבוסס דפדפן, חינמי אך מוגבל
4. **Azure ML Notebooks:** אפשרות ארגונית עם תמיכה ב-GPU
5. **Google Colab:** העלאת מחברות בנפרד, שכבת GPU חינמית זמינה

### עבודה עם מחברות

- המחברות מיועדות להרצה תא-אחר-תא ללמידה
- רבות מהמחברות מורידות מערכי נתונים בהרצה הראשונה (עשוי לקחת זמן)
- חלק מהמודלים דורשים GPU לזמני אימון סבירים
- נעשה שימוש במודלים מאומנים מראש ככל האפשר כדי להפחית דרישות חישוב

### שיקולי ביצועים

- שיעורי ראייה ממוחשבת מאוחרים יותר (CNNs, GANs) נהנים מתמיכה ב-GPU
- שיעורי NLP עם transformers עשויים לדרוש זיכרון RAM משמעותי
- אימון מאפס הוא חינוכי אך גוזל זמן רב
- דוגמאות ללמידת העברה ממזערות את זמן האימון

---

**כתב ויתור**:  
מסמך זה תורגם באמצעות שירות תרגום מבוסס בינה מלאכותית [Co-op Translator](https://github.com/Azure/co-op-translator). למרות שאנו שואפים לדיוק, יש לקחת בחשבון שתרגומים אוטומטיים עשויים להכיל שגיאות או אי דיוקים. המסמך המקורי בשפתו המקורית צריך להיחשב כמקור סמכותי. למידע קריטי, מומלץ להשתמש בתרגום מקצועי על ידי אדם. איננו נושאים באחריות לאי הבנות או לפרשנויות שגויות הנובעות משימוש בתרגום זה.