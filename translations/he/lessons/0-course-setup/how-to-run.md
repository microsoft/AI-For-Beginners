# כיצד להריץ את הקוד

תכנית הלימודים הזו מכילה הרבה דוגמאות מעשיות ומעבדות שתרצו להריץ. כדי לעשות זאת, עליכם להיות מסוגלים להריץ קוד פייתון ב-Jupyter Notebooks המסופקים כחלק מתכנית הלימודים הזו. יש לכם כמה אפשרויות להרצת הקוד:

## הרצה מקומית במחשב שלכם

כדי להריץ את הקוד במחשב המקומי, נדרשת התקנת פייתון. אחת ההמלצות היא להתקין **[miniconda](https://conda.io/en/latest/miniconda.html)** - זוהי התקנה קלה יחסית התומכת במנהל החבילות `conda` ליצירת **סביבות וירטואליות** שונות של פייתון.

לאחר התקנת miniconda, שכפלו את המאגר (repository) וצור סביבה וירטואלית לשימוש בקורס זה:

```bash
git clone http://github.com/microsoft/ai-for-beginners
cd ai-for-beginners
conda env create --name ai4beg --file .devcontainer/environment.yml
conda activate ai4beg
```

### שימוש ב-Visual Studio Code עם הרחבת פייתון

תכנית הלימודים הזו הכי נוחה לשימוש בעת פתיחתה ב-[Visual Studio Code](http://code.visualstudio.com/?WT.mc_id=academic-77998-cacaste) עם [הרחבת פייתון](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-77998-cacaste).

> **הערה**: לאחר ששכפלתם ופתחתם את התיקייה ב-VS Code, הוא יציע אוטומטית להתקין את הרחבות הפייתון. תצטרכו גם להתקין את miniconda כפי שתואר למעלה.

> **הערה**: אם VS Code יציע לכם לפתוח מחדש את המאגר בתוך container, כדאי לסרב לכך ולהשתמש בהתקנה המקומית של פייתון.

### שימוש ב-Jupyter בדפדפן

ניתן גם להשתמש בסביבת Jupyter דרך הדפדפן במחשב שלכם. הן Jupyter הקלאסי והן JupyterHub מספקים סביבת פיתוח נוחה עם השלמה אוטומטית, הדגשת קוד ועוד.

כדי להפעיל Jupyter מקומית, עבורו לתיקיית הקורס והריצו:

```bash
jupyter notebook
```
או
```bash
jupyterhub
```
אז תוכלו לנווט אל כל אחד מהקבצים עם הסיומת `.ipynb`, לפתוח אותם ולהתחיל לעבוד.

### הרצה בתוך container

אפשרות נוספת במקום התקנת פייתון היא להריץ את הקוד בתוך container. מכיוון שהמאגר שלנו כולל תיקיית `.devcontainer` שמסבירה כיצד לבנות container עבור המאגר, VS Code מציע אפשרות לפתוח מחדש את הקוד בתוך container. זה ידרוש התקנת Docker, ויהיה מורכב יותר, לכן אנו ממליצים על כך למשתמשים עם ניסיון.

## הרצה בענן

אם אינכם רוצים להתקין פייתון במחשב המקומי ואפשר לכם גישה למשאבי ענן - אפשרות טובה היא להריץ את הקוד בענן. יש כמה דרכים לעשות זאת:

* שימוש ב-**[GitHub Codespaces](https://github.com/features/codespaces)**, סביבה וירטואלית הנוצרת עבורכם ב-GitHub, נגישה דרך ממשק דפדפן של VS Code. אם יש לכם גישה ל-Codespaces, תוכלו רק ללחוץ על כפתור **Code** במאגר, לפתוח codespace ולרוץ את הקוד תוך זמן קצר.
* שימוש ב-**[Binder](https://mybinder.org/v2/gh/microsoft/ai-for-beginners/HEAD)**. [Binder](https://mybinder.org) מספקת משאבי מחשוב בחינם בענן כדי שתוכלו לבדוק קוד ב-GitHub. יש כפתור בדף הראשי לפתיחת המאגר ב-Binder - זה יוביל אתכם במהירות לאתר Binder, שיבנה container ויתחיל ממשק Jupyter בשקיפות.

> **הערה**: כדי למנוע שימוש לרעה, ל-Binder חסום גישה לחלק ממשאבי רשת. זה עלול למנוע עבודה של קוד שמוריד מודלים ו/או מערכי נתונים מהאינטרנט הציבורי. ייתכן שתצטרכו למצוא פתרונות חלופיים. בנוסף, משאבי המחשוב של Binder בסיסיים יחסית, ולכן האימון יהיה איטי, במיוחד בשיעורים מתקדמים ומורכבים יותר.

## הרצה בענן עם GPU

חלק מהשיעורים המתקדמים בתכנית הלימודים ייהנו מאוד מתמיכה ב-GPU. לדוגמה, אימון מודלים יכול להיות איטי מאוד אחרת. יש כמה אפשרויות:

* יצירת [Data Science Virtual Machine](https://docs.microsoft.com/learn/modules/intro-to-azure-data-science-virtual-machine/?WT.mc_id=academic-77998-cacaste) וחיבור אליה דרך Jupyter. תוכלו לשכפל את המאגר ישירות למכונה ולהתחיל ללמוד. מכונות NC-series תומכות ב-GPU.

> **הערה**: חלק מהמנויים, כולל Azure for Students, לא כוללים תמיכה ב-GPU כברירת מחדל. ייתכן שתצטרכו לבקש ליבות GPU נוספות באמצעות קריאת שירות תמיכה טכנית.

* יצירת [Azure Machine Learning Workspace](https://azure.microsoft.com/services/machine-learning/?WT.mc_id=academic-77998-cacaste) ואז שימוש בתכונת ה-Notebook שם. [וידאו זה](https://azure-for-academics.github.io/quickstart/azureml-papers/) מראה כיצד לשכפל מאגר לתוך פנקס הערות ב-Azure ML ולהתחיל להשתמש בו.

ניתן גם להשתמש ב-Google Colab, הכולל תמיכה חינמית מסוימת ב-GPU, ולהעלות אליו Jupyter Notebooks כדי להריץ אותם אחד-אחד.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**כתב הבהרה**:  
מסמך זה תורגם באמצעות שירות תרגום מבוסס בינה מלאכותית [Co-op Translator](https://github.com/Azure/co-op-translator). אנו שואפים לדייק, אך יש לקחת בחשבון כי תרגומים אוטומטיים עלולים להכיל טעויות או אי דיוקים. יש להתייחס למסמך המקורי בשפתו כמקור הסמכותי. למידע קריטי מומלץ להשתמש בשירות תרגום מקצועי אנושי. אנו לא נושאים באחריות לכל אי הבנה או פרשנות שגויה הנובעת משימוש בתרגום זה.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->