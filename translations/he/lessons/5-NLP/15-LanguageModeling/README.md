<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "31b46ba1f3aa78578134d4829f88be53",
  "translation_date": "2025-08-28T20:00:21+00:00",
  "source_file": "lessons/5-NLP/15-LanguageModeling/README.md",
  "language_code": "he"
}
-->
# מודלים לשוניים

הטמעות סמנטיות, כמו Word2Vec ו-GloVe, הן למעשה צעד ראשון לקראת **מודלים לשוניים** - יצירת מודלים שמסוגלים *להבין* (או *לייצג*) את טבע השפה.

## [שאלון לפני השיעור](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/115)

הרעיון המרכזי מאחורי מודלים לשוניים הוא לאמן אותם על מערכי נתונים לא מתויגים בצורה לא מפוקחת. זה חשוב מכיוון שיש לנו כמויות עצומות של טקסט לא מתויג, בעוד שכמות הטקסט המתויג תמיד תהיה מוגבלת על ידי המאמץ שנוכל להשקיע בתיוג. לרוב, ניתן לבנות מודלים לשוניים שיכולים **לחזות מילים חסרות** בטקסט, מכיוון שקל להסתיר מילה אקראית בטקסט ולהשתמש בה כדוגמת אימון.

## אימון הטמעות

בדוגמאות הקודמות שלנו, השתמשנו בהטמעות סמנטיות מאומנות מראש, אבל מעניין לראות איך ניתן לאמן את ההטמעות הללו. ישנן כמה גישות אפשריות שניתן להשתמש בהן:

* **מודל לשוני מבוסס N-Gram**, שבו אנו חוזים טוקן על ידי התבוננות ב-N הטוקנים הקודמים (N-gram).
* **Continuous Bag-of-Words** (CBoW), שבו אנו חוזים את הטוקן האמצעי $W_0$ ברצף טוקנים $W_{-N}$, ..., $W_N$.
* **Skip-gram**, שבו אנו חוזים סט של טוקנים סמוכים {$W_{-N},\dots, W_{-1}, W_1,\dots, W_N$} מתוך הטוקן האמצעי $W_0$.

![תמונה מתוך מאמר על המרת מילים לווקטורים](../../../../../translated_images/example-algorithms-for-converting-words-to-vectors.fbe9207a726922f6f0f5de66427e8a6eda63809356114e28fb1fa5f4a83ebda7.he.png)

> תמונה מתוך [המאמר הזה](https://arxiv.org/pdf/1301.3781.pdf)

## ✍️ מחברות לדוגמה: אימון מודל CBoW

המשיכו ללמוד במחברות הבאות:

* [אימון CBoW Word2Vec עם TensorFlow](CBoW-TF.ipynb)
* [אימון CBoW Word2Vec עם PyTorch](CBoW-PyTorch.ipynb)

## סיכום

בשיעור הקודם ראינו שהטמעות מילים פועלות כמו קסם! עכשיו אנחנו יודעים שאימון הטמעות מילים הוא לא משימה מורכבת במיוחד, ואנחנו יכולים לאמן הטמעות משלנו לטקסטים ייעודיים אם נדרש.

## [שאלון אחרי השיעור](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/215)

## סקירה ולמידה עצמית

* [המדריך הרשמי של PyTorch על מודלים לשוניים](https://pytorch.org/tutorials/beginner/nlp/word_embeddings_tutorial.html).
* [המדריך הרשמי של TensorFlow על אימון מודל Word2Vec](https://www.TensorFlow.org/tutorials/text/word2vec).
* שימוש במסגרת **gensim** לאימון ההטמעות הנפוצות ביותר בכמה שורות קוד מתואר [בתיעוד הזה](https://pytorch.org/tutorials/beginner/nlp/word_embeddings_tutorial.html).

## 🚀 [משימה: אימון מודל Skip-Gram](lab/README.md)

במעבדה, אנו מאתגרים אתכם לשנות את הקוד מהשיעור הזה כדי לאמן מודל Skip-Gram במקום CBoW. [קראו את הפרטים](lab/README.md)

---

**כתב ויתור**:  
מסמך זה תורגם באמצעות שירות תרגום מבוסס בינה מלאכותית [Co-op Translator](https://github.com/Azure/co-op-translator). בעוד שאנו שואפים לדיוק, יש להיות מודעים לכך שתרגומים אוטומטיים עשויים להכיל שגיאות או אי דיוקים. המסמך המקורי בשפתו המקורית צריך להיחשב כמקור סמכותי. עבור מידע קריטי, מומלץ להשתמש בתרגום מקצועי על ידי אדם. איננו נושאים באחריות לאי הבנות או לפרשנויות שגויות הנובעות משימוש בתרגום זה.