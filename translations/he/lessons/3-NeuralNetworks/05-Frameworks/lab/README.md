<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "e452d897efb9a89700f41021834cf6e5",
  "translation_date": "2025-08-28T19:51:04+00:00",
  "source_file": "lessons/3-NeuralNetworks/05-Frameworks/lab/README.md",
  "language_code": "he"
}
-->
# סיווג עם PyTorch/TensorFlow

מטלת מעבדה מתוך [AI for Beginners Curriculum](https://github.com/microsoft/ai-for-beginners).

## משימה

פתרו שתי בעיות סיווג באמצעות רשתות מחוברות-מלאות (fully-connected) חד-שכבתיות ורב-שכבתיות, תוך שימוש ב-PyTorch או TensorFlow:

1. בעיית **[סיווג איריס](https://en.wikipedia.org/wiki/Iris_flower_data_set)** - דוגמה לבעיה עם נתוני קלט טבלאיים, שניתן להתמודד איתה באמצעות למידת מכונה קלאסית. המטרה שלכם תהיה לסווג פרחי איריס ל-3 קטגוריות, בהתבסס על 4 פרמטרים מספריים.
2. בעיית סיווג ספרות כתובות-יד **MNIST**, אותה כבר ראינו בעבר.

נסו ארכיטקטורות רשת שונות כדי להשיג את הדיוק הטוב ביותר שתוכלו.

## מחברת התחלה

התחילו את המעבדה על ידי פתיחת [LabFrameworks.ipynb](LabFrameworks.ipynb)

---

**כתב ויתור**:  
מסמך זה תורגם באמצעות שירות תרגום מבוסס בינה מלאכותית [Co-op Translator](https://github.com/Azure/co-op-translator). למרות שאנו שואפים לדיוק, יש לקחת בחשבון שתרגומים אוטומטיים עשויים להכיל שגיאות או אי דיוקים. המסמך המקורי בשפתו המקורית צריך להיחשב כמקור סמכותי. עבור מידע קריטי, מומלץ להשתמש בתרגום מקצועי על ידי אדם. איננו נושאים באחריות לאי הבנות או לפרשנויות שגויות הנובעות משימוש בתרגום זה.