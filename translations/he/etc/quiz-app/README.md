# חידונים

החידונים האלו הם החידונים שלפני ואחרי ההרצאות בתוכנית הלימודים של AI בכתובת https://aka.ms/ai-beginners

## הוספת סט חידונים מתורגם

ניתן להוסיף תרגום לחידון על ידי יצירת מבנה חידונים תואם בתיקיית `assets/translations`. החידונים המקוריים נמצאים ב-`assets/translations/en`. החידונים מחולקים למספר קבוצות לפי שיעור. יש לוודא שהמספור תואם את החלק הנכון של החידון. בתוכנית הלימודים הזו יש סך הכול 40 חידונים, והמספור מתחיל מ-0.

לאחר עריכת התרגומים, ערכו את קובץ `index.js` בתיקיית התרגום כדי לייבא את כל הקבצים בהתאם למבנה שב-`en`.

ערכו את קובץ `index.js` ב-`assets/translations` כדי לייבא את הקבצים המתורגמים החדשים.

לאחר מכן, ערכו את התפריט הנפתח ב-`App.vue` באפליקציה הזו כדי להוסיף את השפה שלכם. התאימו את הקיצור המקומי לשם התיקייה של השפה שלכם.

לבסוף, ערכו את כל קישורי החידונים בשיעורים המתורגמים, אם הם קיימים, כדי לכלול את הלוקליזציה כפרמטר בשאילתה: `?loc=fr` לדוגמה.

## הגדרת הפרויקט

```
npm install
```

### הידור וטעינה מחדש בזמן פיתוח

```
npm run serve
```

### הידור ומזעור עבור פרודקשן

```
npm run build
```

### בדיקת קוד ותיקון קבצים

```
npm run lint
```

### התאמת ההגדרות

ראו [תיעוד ההגדרות](https://cli.vuejs.org/config/).

קרדיטים: תודה לגרסה המקורית של אפליקציית החידונים הזו: https://github.com/arpan45/simple-quiz-vue

## פריסה ב-Azure

הנה מדריך שלב-אחר-שלב שיעזור לכם להתחיל:

1. מזגו את מאגר ה-GitHub
ודאו שקוד האפליקציה הסטטית שלכם נמצא במאגר ה-GitHub שלכם. מזגו את המאגר הזה.

2. צרו אפליקציה סטטית ב-Azure
- צרו [חשבון Azure](http://azure.microsoft.com)
- היכנסו ל-[פורטל Azure](https://portal.azure.com) 
- לחצו על "Create a resource" וחפשו "Static Web App".
- לחצו על "Create".

3. הגדירו את האפליקציה הסטטית
- פרטים בסיסיים: 
  - Subscription: בחרו את המנוי שלכם ב-Azure.
  - Resource Group: צרו קבוצת משאבים חדשה או השתמשו בקיימת.
  - Name: תנו שם לאפליקציה הסטטית שלכם.
  - Region: בחרו את האזור הקרוב ביותר למשתמשים שלכם.

- #### פרטי פריסה:
  - Source: בחרו "GitHub".
  - GitHub Account: אשרו ל-Azure גישה לחשבון ה-GitHub שלכם.
  - Organization: בחרו את הארגון שלכם ב-GitHub.
  - Repository: בחרו את המאגר שמכיל את האפליקציה הסטטית שלכם.
  - Branch: בחרו את הענף שממנו תרצו לפרוס.

- #### פרטי בנייה:
  - Build Presets: בחרו את המסגרת שבה נבנתה האפליקציה שלכם (לדוגמה, React, Angular, Vue וכו').
  - App Location: ציינו את התיקייה שמכילה את קוד האפליקציה שלכם (לדוגמה, / אם היא בתיקיית השורש).
  - API Location: אם יש לכם API, ציינו את המיקום שלו (אופציונלי).
  - Output Location: ציינו את התיקייה שבה נוצר פלט הבנייה (לדוגמה, build או dist).

4. סקירה ויצירה
עברו על ההגדרות שלכם ולחצו "Create". Azure יגדיר את המשאבים הנדרשים וייצור קובץ GitHub Actions במאגר שלכם.

5. קובץ GitHub Actions Workflow
Azure ייצור אוטומטית קובץ GitHub Actions Workflow במאגר שלכם (.github/workflows/azure-static-web-apps-<name>.yml). קובץ זה יטפל בתהליך הבנייה והפריסה.

6. מעקב אחר הפריסה
עברו ללשונית "Actions" במאגר ה-GitHub שלכם.
תוכלו לראות Workflow רץ. Workflow זה יבנה ויפרס את האפליקציה הסטטית שלכם ב-Azure.
לאחר שה-Workflow יסתיים, האפליקציה שלכם תהיה זמינה בכתובת ה-URL שסופקה על ידי Azure.

### דוגמה לקובץ Workflow

הנה דוגמה לאיך קובץ GitHub Actions Workflow עשוי להיראות:
name: Azure Static Web Apps CI/CD
```
on:
  push:
    branches:
      - main
  pull_request:
    types: [opened, synchronize, reopened, closed]
    branches:
      - main

jobs:
  build_and_deploy_job:
    runs-on: ubuntu-latest
    name: Build and Deploy Job
    steps:
      - uses: actions/checkout@v2
      - name: Build And Deploy
        id: builddeploy
        uses: Azure/static-web-apps-deploy@v1
        with:
          azure_static_web_apps_api_token: ${{ secrets.AZURE_STATIC_WEB_APPS_API_TOKEN }}
          repo_token: ${{ secrets.GITHUB_TOKEN }}
          action: "upload"
          app_location: "etc/quiz-app # App source code path"
          api_location: ""API source code path optional
          output_location: "dist" #Built app content directory - optional
```

### משאבים נוספים
- [תיעוד Azure Static Web Apps](https://learn.microsoft.com/azure/static-web-apps/getting-started)
- [תיעוד GitHub Actions](https://docs.github.com/actions/use-cases-and-examples/deploying/deploying-to-azure-static-web-app)

---

**כתב ויתור**:  
מסמך זה תורגם באמצעות שירות תרגום מבוסס בינה מלאכותית [Co-op Translator](https://github.com/Azure/co-op-translator). למרות שאנו שואפים לדיוק, יש לקחת בחשבון שתרגומים אוטומטיים עשויים להכיל שגיאות או אי-דיוקים. המסמך המקורי בשפתו המקורית נחשב למקור הסמכותי. למידע קריטי, מומלץ להשתמש בתרגום מקצועי על ידי מתרגם אנושי. איננו נושאים באחריות לכל אי-הבנה או פרשנות שגויה הנובעת משימוש בתרגום זה.