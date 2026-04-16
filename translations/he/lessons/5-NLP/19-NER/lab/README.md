# זיהוי ישויות בשם (NER)

משימת מעבדה מתוך [AI for Beginners Curriculum](https://github.com/microsoft/ai-for-beginners).

## משימה

במעבדה זו, עליכם לאמן מודל לזיהוי ישויות בשם עבור מונחים רפואיים.

## מערך הנתונים

כדי לאמן מודל NER, אנו זקוקים למערך נתונים מתויג כראוי עם ישויות רפואיות. [מערך הנתונים BC5CDR](https://biocreative.bioinformatics.udel.edu/tasks/biocreative-v/track-3-cdr/) מכיל ישויות מתויגות של מחלות וכימיקלים מתוך יותר מ-1500 מאמרים. ניתן להוריד את מערך הנתונים לאחר הרשמה באתר שלהם.

מערך הנתונים BC5CDR נראה כך:

```
6794356|t|Tricuspid valve regurgitation and lithium carbonate toxicity in a newborn infant.
6794356|a|A newborn with massive tricuspid regurgitation, atrial flutter, congestive heart failure, and a high serum lithium level is described. This is the first patient to initially manifest tricuspid regurgitation and atrial flutter, and the 11th described patient with cardiac disease among infants exposed to lithium compounds in the first trimester of pregnancy. Sixty-three percent of these infants had tricuspid valve involvement. Lithium carbonate may be a factor in the increasing incidence of congenital heart disease when taken during early pregnancy. It also causes neurologic depression, cyanosis, and cardiac arrhythmia when consumed prior to delivery.
6794356	0	29	Tricuspid valve regurgitation	Disease	D014262
6794356	34	51	lithium carbonate	Chemical	D016651
6794356	52	60	toxicity	Disease	D064420
...
```

במערך הנתונים הזה, יש כותרת מאמר ותקציר בשתי השורות הראשונות, ולאחר מכן יש ישויות בודדות, עם מיקומי התחלה וסיום בתוך בלוק הכותרת+תקציר. בנוסף לסוג הישויות, תקבלו את מזהה האונטולוגיה של כל ישות בתוך אונטולוגיה רפואית מסוימת.

תצטרכו לכתוב קוד ב-Python כדי להמיר את הנתונים לקידוד BIO.

## הרשת

ניסיון ראשון ב-NER יכול להתבצע באמצעות רשת LSTM, כפי שראיתם בדוגמה במהלך השיעור. עם זאת, במשימות עיבוד שפה טבעית (NLP), [ארכיטקטורת טרנספורמר](https://en.wikipedia.org/wiki/Transformer_(machine_learning_model)), ובמיוחד [מודלי שפה BERT](https://en.wikipedia.org/wiki/BERT_(language_model)) מציגים תוצאות טובות בהרבה. מודלי BERT מאומנים מראש מבינים את המבנה הכללי של השפה, וניתן להתאים אותם למשימות ספציפיות עם מערכי נתונים קטנים יחסית ועלויות חישוב נמוכות.

מכיוון שאנו מתכננים ליישם NER בתרחיש רפואי, הגיוני להשתמש במודל BERT שאומן על טקסטים רפואיים. Microsoft Research שחררה מודל מאומן מראש בשם [PubMedBERT][PubMedBERT] ([פרסום][PubMedBERT-Pub]), אשר הותאם באמצעות טקסטים ממאגר [PubMed](https://pubmed.ncbi.nlm.nih.gov/).

הסטנדרט *דה פקטו* לאימון מודלים טרנספורמרים הוא ספריית [Hugging Face Transformers](https://huggingface.co/). הספרייה מכילה גם מאגר של מודלים מאומנים מראש שמנוהלים על ידי הקהילה, כולל PubMedBERT. כדי לטעון ולהשתמש במודל הזה, נדרשות רק כמה שורות קוד:

```python
model_name = "microsoft/BiomedNLP-PubMedBERT-base-uncased-abstract"
classes = ... # number of classes: 2*entities+1
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = BertForTokenClassification.from_pretrained(model_name, classes)
```

זה מספק לנו את `model` עצמו, שנבנה עבור משימת סיווג טוקנים תוך שימוש במספר `classes` של קטגוריות, וכן את אובייקט ה-`tokenizer` שיכול לפצל טקסט קלט לטוקנים. תצטרכו להמיר את מערך הנתונים לפורמט BIO, תוך התחשבות בטוקניזציה של PubMedBERT. ניתן להשתמש [בקוד Python הזה](https://gist.github.com/shwars/580b55684be3328eb39ecf01b9cbbd88) כהשראה.

## מסקנות

המשימה הזו קרובה מאוד למשימה אמיתית שתיתקלו בה אם תרצו להפיק תובנות ממספר רב של טקסטים בשפה טבעית. במקרה שלנו, נוכל ליישם את המודל המאומן שלנו על [מערך הנתונים של מאמרים הקשורים ל-COVID](https://www.kaggle.com/allen-institute-for-ai/CORD-19-research-challenge) ולראות אילו תובנות נוכל להפיק. [פוסט הבלוג הזה](https://soshnikov.com/science/analyzing-medical-papers-with-azure-and-text-analytics-for-health/) ו-[המאמר הזה](https://www.mdpi.com/2504-2289/6/1/4) מתארים את המחקר שניתן לבצע על מאגר המאמרים הזה באמצעות NER.

---

**כתב ויתור**:  
מסמך זה תורגם באמצעות שירות תרגום מבוסס בינה מלאכותית [Co-op Translator](https://github.com/Azure/co-op-translator). למרות שאנו שואפים לדיוק, יש לקחת בחשבון שתרגומים אוטומטיים עשויים להכיל שגיאות או אי דיוקים. המסמך המקורי בשפתו המקורית צריך להיחשב כמקור סמכותי. עבור מידע קריטי, מומלץ להשתמש בתרגום מקצועי על ידי אדם. איננו נושאים באחריות לאי הבנות או לפרשנויות שגויות הנובעות משימוש בתרגום זה.