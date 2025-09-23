<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "0c37770bba4fff3c71dc00eb261ee61b",
  "translation_date": "2025-08-28T19:48:41+00:00",
  "source_file": "lessons/3-NeuralNetworks/03-Perceptron/README.md",
  "language_code": "he"
}
-->
# מבוא לרשתות נוירונים: פרספטרון

## [שאלון לפני השיעור](https://ff-quizzes.netlify.app/en/ai/quiz/5)

אחת הניסיונות הראשונים ליישם משהו דומה לרשת נוירונים מודרנית נעשתה על ידי פרנק רוזנבלט ממעבדת האווירונאוטיקה של קורנל בשנת 1957. זה היה יישום חומרה שנקרא "Mark-1", שתוכנן לזהות צורות גיאומטריות פשוטות, כמו משולשים, ריבועים ועיגולים.

|      |      |
|--------------|-----------|
|<img src='images/Rosenblatt-wikipedia.jpg' alt='Frank Rosenblatt'/> | <img src='images/Mark_I_perceptron_wikipedia.jpg' alt='The Mark 1 Perceptron' />|

> תמונות [מויקיפדיה](https://en.wikipedia.org/wiki/Perceptron)

תמונת הקלט יוצגה על ידי מערך של 20x20 תאים פוטואלקטריים, כך שלרשת הנוירונים היו 400 קלטים ופלט בינארי אחד. רשת פשוטה הכילה נוירון אחד, שנקרא גם **יחידת לוגיקה סף**. המשקלים של רשת הנוירונים פעלו כמו פוטנציומטרים שנדרשו לכיוונון ידני במהלך שלב האימון.

> ✅ פוטנציומטר הוא מכשיר שמאפשר למשתמש לכוון את ההתנגדות במעגל.

> הניו יורק טיימס כתב על הפרספטרון באותה תקופה: *העובר של מחשב אלקטרוני ש[הצי] מצפה שיוכל ללכת, לדבר, לראות, לכתוב, לשכפל את עצמו ולהיות מודע לקיומו.*

## מודל הפרספטרון

נניח שיש לנו N מאפיינים במודל שלנו, ובמקרה כזה וקטור הקלט יהיה וקטור בגודל N. פרספטרון הוא מודל של **סיווג בינארי**, כלומר הוא יכול להבחין בין שתי קטגוריות של נתוני קלט. נניח שלכל וקטור קלט x הפלט של הפרספטרון שלנו יהיה או +1 או -1, בהתאם לקטגוריה. הפלט יחושב באמצעות הנוסחה:

y(x) = f(w<sup>T</sup>x)

כאשר f היא פונקציית הפעלה מדרגתית.

<!-- img src="http://www.sciweavers.org/tex2img.php?eq=f%28x%29%20%3D%20%5Cbegin%7Bcases%7D%0A%20%20%20%20%20%20%20%20%20%2B1%20%26%20x%20%5Cgeq%200%20%5C%5C%0A%20%20%20%20%20%20%20%20%20-1%20%26%20x%20%3C%200%0A%20%20%20%20%20%20%20%5Cend%7Bcases%7D%20%5C%5C%0A&bc=White&fc=Black&im=jpg&fs=12&ff=arev&edit=0" align="center" border="0" alt="f(x) = \begin{cases} +1 & x \geq 0 \\ -1 & x < 0 \end{cases} \\" width="154" height="50" / -->
<img src="images/activation-func.png"/>

## אימון הפרספטרון

כדי לאמן פרספטרון, עלינו למצוא וקטור משקלים w שמסווג את רוב הערכים בצורה נכונה, כלומר מביא ל**שגיאה** הקטנה ביותר. שגיאה זו E מוגדרת על פי **קריטריון הפרספטרון** באופן הבא:

E(w) = -∑w<sup>T</sup>x<sub>i</sub>t<sub>i</sub>

כאשר:

* הסכום נלקח על נקודות נתוני האימון i שמובילות לסיווג שגוי.
* x<sub>i</sub> הוא נתון הקלט, ו-t<sub>i</sub> הוא או -1 או +1 עבור דוגמאות שליליות וחיוביות בהתאמה.

קריטריון זה נחשב כפונקציה של המשקלים w, ועלינו למזער אותו. לעיתים קרובות משתמשים בשיטה שנקראת **ירידת גרדיאנט**, שבה מתחילים עם משקלים ראשוניים w<sup>(0)</sup>, ואז בכל שלב מעדכנים את המשקלים לפי הנוסחה:

w<sup>(t+1)</sup> = w<sup>(t)</sup> - η∇E(w)

כאן η הוא מה שנקרא **קצב הלמידה**, ו-∇E(w) מסמן את **הגרדיאנט** של E. לאחר חישוב הגרדיאנט, מגיעים ל:

w<sup>(t+1)</sup> = w<sup>(t)</sup> + ∑ηx<sub>i</sub>t<sub>i</sub>

האלגוריתם ב-Python נראה כך:

```python
def train(positive_examples, negative_examples, num_iterations = 100, eta = 1):

    weights = [0,0,0] # Initialize weights (almost randomly :)
        
    for i in range(num_iterations):
        pos = random.choice(positive_examples)
        neg = random.choice(negative_examples)

        z = np.dot(pos, weights) # compute perceptron output
        if z < 0: # positive example classified as negative
            weights = weights + eta*weights.shape

        z  = np.dot(neg, weights)
        if z >= 0: # negative example classified as positive
            weights = weights - eta*weights.shape

    return weights
```

## סיכום

בשיעור זה למדתם על פרספטרון, שהוא מודל לסיווג בינארי, וכיצד לאמן אותו באמצעות וקטור משקלים.

## 🚀 אתגר

אם תרצו לנסות לבנות פרספטרון משלכם, נסו [את המעבדה הזו ב-Microsoft Learn](https://docs.microsoft.com/en-us/azure/machine-learning/component-reference/two-class-averaged-perceptron?WT.mc_id=academic-77998-cacaste) שמשתמשת ב-[Azure ML designer](https://docs.microsoft.com/en-us/azure/machine-learning/concept-designer?WT.mc_id=academic-77998-cacaste).

## [שאלון אחרי השיעור](https://ff-quizzes.netlify.app/en/ai/quiz/6)

## סקירה ולימוד עצמי

כדי לראות כיצד ניתן להשתמש בפרספטרון לפתרון בעיות פשוטות וגם בעיות מהחיים האמיתיים, ולהמשיך ללמוד - עברו למחברת [Perceptron](Perceptron.ipynb).

הנה [מאמר מעניין על פרספטרונים](https://towardsdatascience.com/what-is-a-perceptron-basics-of-neural-networks-c4cfea20c590) גם כן.

## [מטלה](lab/README.md)

בשיעור זה יישמנו פרספטרון למשימת סיווג בינארי, והשתמשנו בו כדי לסווג בין שתי ספרות כתובות ביד. במעבדה זו, תתבקשו לפתור את בעיית סיווג הספרות במלואה, כלומר לקבוע איזו ספרה סביר להניח תואמת לתמונה נתונה.

* [הוראות](lab/README.md)
* [מחברת](lab/PerceptronMultiClass.ipynb)

---

**כתב ויתור**:  
מסמך זה תורגם באמצעות שירות תרגום מבוסס בינה מלאכותית [Co-op Translator](https://github.com/Azure/co-op-translator). בעוד שאנו שואפים לדיוק, יש להיות מודעים לכך שתרגומים אוטומטיים עשויים להכיל שגיאות או אי דיוקים. המסמך המקורי בשפתו המקורית צריך להיחשב כמקור סמכותי. עבור מידע קריטי, מומלץ להשתמש בתרגום מקצועי על ידי אדם. איננו נושאים באחריות לאי הבנות או לפרשנויות שגויות הנובעות משימוש בתרגום זה.