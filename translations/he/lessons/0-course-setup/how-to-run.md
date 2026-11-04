# כיצד להריץ את הקוד

תוכנית הלימודים הזו מכילה הרבה דוגמאות מעשיות ומעבדות שברצונך להריץ. כדי לעשות זאת, אתה צריך את היכולת להריץ קוד Python ב-Jupyter Notebooks המסופקים כחלק מתוכנית הלימודים הזו. יש לך כמה אפשרויות להרצת הקוד:

## להריץ מקומית במחשב שלך

כדי להריץ את הקוד מקומית במחשב שלך, נדרש התקנת Python. המלצה אחת היא להתקין את **[miniconda](https://conda.io/en/latest/miniconda.html)** - זו התקנה יחסית קלה שתומכת במנהל החבילות `conda` עבור **סביבות וירטואליות** שונות של Python.

לאחר שתתקין miniconda, שכפל את המאגר וצור סביבה וירטואלית שתשמש לקורס זה:

```bash
git clone http://github.com/microsoft/ai-for-beginners
cd ai-for-beginners
conda env create --name ai4beg --file .devcontainer/environment.yml
conda activate ai4beg
```

> **הערת Windows**: אם יצירת הסביבה נכשלה בזמן התקנת `gdk-pixbuf` עם `UnicodeDecodeError` שמציין את codec `gbk`, הפעל מצב UTF-8 של Python בטרמינל ונסה שוב. השתמש בתחביר המתאים לטרמינל שבו אתה משתמש:
>
> **PowerShell:**
>
> ```powershell
> $env:PYTHONUTF8 = "1"
> conda env create --name ai4beg --file .devcontainer/environment.yml
> ```
>
> **שורת הפקודה (`cmd.exe`) או Anaconda Prompt:**
>
> ```cmd
> set PYTHONUTF8=1
> conda env create --name ai4beg --file .devcontainer/environment.yml
> ```
>
> **Bash, כולל Git Bash:**
>
> ```bash
> export PYTHONUTF8=1
> conda env create --name ai4beg --file .devcontainer/environment.yml
> ```
>
> אם ניסיון כושל השאיר אחריו את סביבת `ai4beg`, בטל את ההפעלה שלה והסר את הסביבה לפני שתנסה שוב. השתמש ב-`conda deactivate` קודם כשיש סביבה פעילה:
>
> ```text
> conda deactivate
> conda env remove --name ai4beg
> ```

### שימוש ב-Visual Studio Code עם הרחבת Python

תוכנית הלימודים הזו הכי טובה כאשר פותחים אותה ב-[Visual Studio Code](http://code.visualstudio.com/?WT.mc_id=academic-77998-cacaste) עם [הרחבת Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-77998-cacaste).

> **הערה**: ברגע שתשכפל ותפתח את התיקייה ב-VS Code, תוצע לך באופן אוטומטי להתקין הרחבות Python. יהיה עליך גם להתקין את miniconda כמתואר מעלה.

> **הערה**: אם VS Code מציע לך לפתוח מחדש את המאגר במיכל, עליך לסרב לכך כדי להשתמש בהתקנת Python מקומית.

### שימוש ב-Jupyter בדפדפן

ניתן גם להשתמש בסביבת Jupyter מהדפדפן במחשב האישי שלך. גם ג'ופיטר הקלאסי וגם JupyterHub מספקים סביבת פיתוח נוחה עם השלמת אוטומטית, הדגשת קוד וכו'.

כדי להפעיל Jupyter מקומית, עבור לתיקיית הקורס, והרץ:

```bash
jupyter notebook
```
או
```bash
jupyterhub
```
 אז תוכל לגלוש לכל אחד מקבצי `.ipynb`, לפתוח אותם ולהתחיל לעבוד.

### הרצה במיכל (container)

אלטרנטיבה להתקנת Python תהיה להריץ את הקוד במיכל. מאחר שהמאגר שלנו מספק תיקיית `.devcontainer` מיוחדת שמסבירה כיצד לבנות מיכל עבור מאגר זה, VS Code מציע את האפשרות לפתוח מחדש את הקוד במיכל. זה ידרוש התקנת Docker, וגם יהיה מורכב יותר, ולכן אנו ממליצים זאת למשתמשים מנוסים יותר.

## הרצה בענן

אם אינך רוצה להתקין Python מקומית ויש לך גישה למשאבי ענן כלשהם - אלטרנטיבה טובה תהיה להריץ את הקוד בענן. יש כמה דרכים לעשות זאת:

* שימוש ב-**[GitHub Codespaces](https://github.com/features/codespaces)**, שהיא סביבה וירטואלית שנוצרה עבורך ב-GitHub, נגישה דרך ממשק דפדפן של VS Code. אם יש לך גישה לקודספייס, פשוט לחץ על כפתור **Code** במאגר, התחל קודספייס, ותוכל להתחיל להריץ במהירות.
* שימוש ב-**[Binder](https://mybinder.org/v2/gh/microsoft/ai-for-beginners/HEAD)**. [Binder](https://mybinder.org) מציע משאבי חישוב בחינם המסופקים בענן לאנשים כמוך לבדוק קוד ב-GitHub. יש כפתור בדף הראשי לפתיחת המאגר ב-Binder - זה יפנה אותך במהירות לאתר binder, שייבנה מיכל תשתית ויתחיל ממשק אינטרנטי של Jupyter עבורך בצורה חלקה.

> **הערה**: למניעת שימוש לרעה, ל-Binder חסומים משאבי רשת מסוימים. זה עשוי למנוע חלק מהקוד שפונה למודלים ו/או מערכי נתונים מהאינטרנט הציבורי. ייתכן שתצטרך למצוא דרכי עקיפה. בנוסף, משאבי החישוב של Binder בסיסיים למדי, כך שהאימון יהיה איטי, במיוחד בשיעורים מאוחרים ומורכבים יותר.

## הרצה בענן עם GPU

כמה מהשיעורים המאוחרים בתוכנית הזו ייהנו רבות מתמיכה ב-GPU. אימון מודלים, למשל, עלול להיות איטי מאוד אחרת. יש כמה אפשרויות שתוכל לבחור, במיוחד אם יש לך גישה לענן דרך [Azure for Students](https://azure.microsoft.com/free/students/?WT.mc_id=academic-77998-cacaste) או דרך המוסד שלך:

* צור [Data Science Virtual Machine](https://docs.microsoft.com/learn/modules/intro-to-azure-data-science-virtual-machine/?WT.mc_id=academic-77998-cacaste) ותחבר אליו דרך Jupyter. תוכל אז לשכפל את המאגר ישירות למכונה ולהתחיל ללמוד. מכונות וירטואליות מסדרת NC תומכות ב-GPU.

> **הערה**: במנויים מסוימים, כולל Azure for Students, אין תמיכה ב-GPU באופן אוטומטי. ייתכן שתצטרך לבקש ליבות GPU נוספות באמצעות בקשת תמיכה טכנית.

* צור [Azure Machine Learning Workspace](https://azure.microsoft.com/services/machine-learning/?WT.mc_id=academic-77998-cacaste) ואז השתמש בתכונת המחברת שם. [וידאו זה](https://azure-for-academics.github.io/quickstart/azureml-papers/) מראה כיצד לשכפל מאגר למחברת Azure ML ולהתחיל להשתמש בו.

תוכל גם להשתמש ב-Google Colab, שמספק מעט תמיכה חינמית ב-GPU, ולהעלות לשם Jupyter Notebooks כדי להריץ אותם אחד אחרי השני.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**כתב ויתור**:
מסמך זה תורגם באמצעות שירות תרגום אוטומטי [Co-op Translator](https://github.com/Azure/co-op-translator). למרות שאנו שואפים לדיוק, יש לקחת בחשבון שתרגומים אוטומטיים עלולים להכיל שגיאות או אי-דיוקים. יש להחשיב את המסמך המקורי בשפתו הטבעית כמקור הסמכות. למידע קריטי מומלץ להשתמש בתרגום מקצועי על ידי מתרגם אדם. אנו לא אחראים לכל אי-הבנה או פירוש שגוי הנובע מהשימוש בתרגום זה.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->