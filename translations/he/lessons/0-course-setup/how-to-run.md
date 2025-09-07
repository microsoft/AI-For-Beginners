<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "7df19702b8d2d3f7c4238c51bec2c8fc",
  "translation_date": "2025-08-28T19:20:05+00:00",
  "source_file": "lessons/0-course-setup/how-to-run.md",
  "language_code": "he"
}
-->
# איך להריץ את הקוד

תוכנית הלימודים הזו כוללת הרבה דוגמאות שניתן להריץ ומעבדות שתרצו לעבוד עליהן. כדי לעשות זאת, תצטרכו יכולת להריץ קוד Python ב-Jupyter Notebooks המסופקים כחלק מתוכנית הלימודים. יש לכם כמה אפשרויות להריץ את הקוד:

## הרצה מקומית על המחשב שלכם

כדי להריץ את הקוד מקומית על המחשב שלכם, תצטרכו להתקין גרסה כלשהי של Python. אני ממליץ באופן אישי להתקין **[miniconda](https://conda.io/en/latest/miniconda.html)** - התקנה קלה יחסית שתומכת במנהל החבילות `conda` עבור **סביבות וירטואליות** של Python.

לאחר התקנת miniconda, תצטרכו לשכפל (clone) את המאגר וליצור סביבה וירטואלית לשימוש בקורס:

```bash
git clone http://github.com/microsoft/ai-for-beginners
cd ai-for-beginners
conda env create --name ai4beg --file .devcontainer/environment.yml
conda activate ai4beg
```

### שימוש ב-Visual Studio Code עם הרחבת Python

כנראה הדרך הטובה ביותר להשתמש בתוכנית הלימודים היא לפתוח אותה ב-[Visual Studio Code](http://code.visualstudio.com/?WT.mc_id=academic-77998-cacaste) עם [הרחבת Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-77998-cacaste).

> **הערה**: לאחר שתשכפלו ותפתחו את התיקייה ב-VS Code, התוכנה תציע לכם להתקין את הרחבות ה-Python. תצטרכו גם להתקין את miniconda כפי שתואר לעיל.

> **הערה**: אם VS Code מציע לכם לפתוח את המאגר במכולה (container), תצטרכו לסרב לכך כדי להשתמש בהתקנת Python המקומית.

### שימוש ב-Jupyter בדפדפן

ניתן גם להשתמש בסביבת Jupyter ישירות מהדפדפן על המחשב שלכם. למעשה, גם Jupyter הקלאסי וגם Jupyter Hub מספקים סביבת פיתוח נוחה עם השלמה אוטומטית, הדגשת קוד ועוד.

כדי להפעיל את Jupyter מקומית, גשו לתיקיית הקורס והריצו:

```bash
jupyter notebook
```  
או  
```bash
jupyterhub
```  
לאחר מכן תוכלו לנווט לכל אחד מקבצי `.ipynb`, לפתוח אותם ולהתחיל לעבוד.

### הרצה במכולה

אלטרנטיבה להתקנת Python היא להריץ את הקוד במכולה (container). מכיוון שהמאגר שלנו מכיל תיקיית `.devcontainer` מיוחדת שמנחה כיצד לבנות מכולה עבור המאגר, VS Code יציע לכם לפתוח את הקוד במכולה. זה ידרוש התקנת Docker, וגם יהיה מורכב יותר, ולכן אנו ממליצים על כך למשתמשים מנוסים יותר.

## הרצה בענן

אם אינכם רוצים להתקין Python מקומית ויש לכם גישה למשאבי ענן, אלטרנטיבה טובה תהיה להריץ את הקוד בענן. יש כמה דרכים לעשות זאת:

* שימוש ב-**[GitHub Codespaces](https://github.com/features/codespaces)**, שהוא סביבה וירטואלית שנוצרת עבורכם ב-GitHub ונגישה דרך ממשק הדפדפן של VS Code. אם יש לכם גישה ל-Codespaces, פשוט לחצו על כפתור **Code** במאגר, התחילו Codespace, ותוכלו להתחיל לעבוד במהירות.
* שימוש ב-**[Binder](https://mybinder.org/v2/gh/microsoft/ai-for-beginners/HEAD)**. [Binder](https://mybinder.org) מספק משאבי מחשוב חינמיים בענן עבור אנשים כמוכם שרוצים לבדוק קוד ב-GitHub. יש כפתור בעמוד הראשי לפתיחת המאגר ב-Binder - זה ייקח אתכם במהירות לאתר Binder, שיבנה את המכולה ויפעיל את ממשק ה-Jupyter עבורכם בצורה חלקה.

> **הערה**: כדי למנוע שימוש לרעה, ל-Binder יש גישה מוגבלת למשאבי אינטרנט מסוימים. זה עשוי למנוע מקוד מסוים שעושה שימוש במודלים ו/או מערכי נתונים מהאינטרנט הציבורי לעבוד. ייתכן שתצטרכו למצוא פתרונות חלופיים. בנוסף, משאבי המחשוב שמספק Binder בסיסיים למדי, כך שהאימון יהיה איטי, במיוחד בשיעורים המורכבים יותר.

## הרצה בענן עם GPU

חלק מהשיעורים המאוחרים יותר בתוכנית הלימודים ייהנו מאוד מתמיכה ב-GPU, אחרת האימון יהיה איטי מאוד. יש כמה אפשרויות שתוכלו לשקול, במיוחד אם יש לכם גישה לענן דרך [Azure for Students](https://azure.microsoft.com/free/students/?WT.mc_id=academic-77998-cacaste) או דרך המוסד שלכם:

* יצירת [מכונה וירטואלית למדעי הנתונים](https://docs.microsoft.com/learn/modules/intro-to-azure-data-science-virtual-machine/?WT.mc_id=academic-77998-cacaste) והתחברות אליה דרך Jupyter. תוכלו לשכפל את המאגר ישירות למכונה ולהתחיל ללמוד. מכונות מסדרת NC כוללות תמיכה ב-GPU.

> **הערה**: חלק מהמנויים, כולל Azure for Students, אינם מספקים תמיכה ב-GPU כברירת מחדל. ייתכן שתצטרכו לבקש ליבות GPU נוספות דרך בקשת תמיכה טכנית.

* יצירת [סביבת עבודה של Azure Machine Learning](https://azure.microsoft.com/services/machine-learning/?WT.mc_id=academic-77998-cacaste) ואז שימוש בתכונת המחברות שם. [הווידאו הזה](https://azure-for-academics.github.io/quickstart/azureml-papers/) מראה כיצד לשכפל מאגר למחברת Azure ML ולהתחיל להשתמש בו.

תוכלו גם להשתמש ב-Google Colab, שמספק תמיכה חינמית מסוימת ב-GPU, ולהעלות לשם את ה-Jupyter Notebooks כדי להריץ אותם אחד-אחד.

---

**כתב ויתור**:  
מסמך זה תורגם באמצעות שירות תרגום מבוסס בינה מלאכותית [Co-op Translator](https://github.com/Azure/co-op-translator). למרות שאנו שואפים לדיוק, יש לקחת בחשבון שתרגומים אוטומטיים עשויים להכיל שגיאות או אי דיוקים. המסמך המקורי בשפתו המקורית צריך להיחשב כמקור סמכותי. עבור מידע קריטי, מומלץ להשתמש בתרגום מקצועי על ידי אדם. איננו נושאים באחריות לאי הבנות או לפרשנויות שגויות הנובעות משימוש בתרגום זה.