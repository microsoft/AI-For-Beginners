# אלגוריתמים גנטיים

## [שאלון לפני ההרצאה](https://ff-quizzes.netlify.app/en/ai/quiz/41)

**אלגוריתמים גנטיים** (GA) מבוססים על גישה **אבולוציונית** לבינה מלאכותית, שבה נעשה שימוש בשיטות של אבולוציה של אוכלוסייה כדי להגיע לפתרון אופטימלי לבעיה נתונה. הם הוצעו לראשונה בשנת 1975 על ידי [ג'ון הנרי הולנד](https://wikipedia.org/wiki/John_Henry_Holland).

אלגוריתמים גנטיים מבוססים על הרעיונות הבאים:

* פתרונות תקפים לבעיה יכולים להיות מיוצגים כ**גנים**
* **שחלוף** מאפשר לנו לשלב שני פתרונות יחד כדי לקבל פתרון חדש ותקף
* **סלקציה** משמשת לבחירת פתרונות אופטימליים יותר באמצעות **פונקציית התאמה**
* **מוטציות** מוכנסות כדי לערער את האופטימיזציה ולהוציא אותנו ממינימום מקומי

אם ברצונך ליישם אלגוריתם גנטי, תצטרך את הדברים הבאים:

* למצוא שיטה לקידוד פתרונות הבעיה באמצעות **גנים** g&in;&Gamma;
* על קבוצת הגנים &Gamma; יש להגדיר **פונקציית התאמה** fit: &Gamma;&rightarrow;**R**. ערכים קטנים יותר של הפונקציה מתאימים לפתרונות טובים יותר.
* להגדיר מנגנון **שחלוף** לשילוב שני גנים יחד כדי לקבל פתרון חדש ותקף crossover: &Gamma;<sup>2</sub>&rightarrow;&Gamma;.
* להגדיר מנגנון **מוטציה** mutate: &Gamma;&rightarrow;&Gamma;.

במקרים רבים, שחלוף ומוטציה הם אלגוריתמים פשוטים למדי שמבצעים מניפולציה על גנים כמחרוזות מספריות או וקטורי ביטים.

היישום הספציפי של אלגוריתם גנטי יכול להשתנות ממקרה למקרה, אך המבנה הכללי הוא כדלקמן:

1. לבחור אוכלוסייה התחלתית G&subset;&Gamma;
2. לבחור באופן אקראי אחת מהפעולות שתבוצע בשלב זה: שחלוף או מוטציה
3. **שחלוף**:
   * לבחור באופן אקראי שני גנים g<sub>1</sub>, g<sub>2</sub> &in; G
   * לחשב שחלוף g=crossover(g<sub>1</sub>,g<sub>2</sub>)
   * אם fit(g)<fit(g<sub>1</sub>) או fit(g)<fit(g<sub>2</sub>) - להחליף את הגן המתאים באוכלוסייה ב-g.
4. **מוטציה** - לבחור גן אקראי g&in;G ולהחליפו ב-mutate(g)
5. לחזור לשלב 2, עד שנקבל ערך קטן מספיק של fit, או עד שנגיע למגבלת מספר השלבים.

## משימות טיפוסיות

משימות שנפתרות בדרך כלל באמצעות אלגוריתמים גנטיים כוללות:

1. אופטימיזציה של לוחות זמנים
1. אריזה אופטימלית
1. חיתוך אופטימלי
1. האצת חיפוש ממצה

## ✍️ תרגילים: אלגוריתמים גנטיים

המשך ללמוד במחברות הבאות:

עבור ל[מחברת זו](Genetic.ipynb) כדי לראות שני דוגמאות לשימוש באלגוריתמים גנטיים:

1. חלוקה הוגנת של אוצר
1. בעיית 8 המלכות

## סיכום

אלגוריתמים גנטיים משמשים לפתרון בעיות רבות, כולל לוגיסטיקה ובעיות חיפוש. התחום נוצר בהשראת מחקרים ששילבו נושאים בפסיכולוגיה ומדעי המחשב.

## 🚀 אתגר

"אלגוריתמים גנטיים פשוטים ליישום, אך התנהגותם קשה להבנה." [מקור](https://wikipedia.org/wiki/Genetic_algorithm) בצע מחקר כדי למצוא יישום של אלגוריתם גנטי, כמו פתרון חידת סודוקו, והסבר כיצד הוא עובד באמצעות סקיצה או תרשים זרימה.

## [שאלון אחרי ההרצאה](https://ff-quizzes.netlify.app/en/ai/quiz/42)

## סקירה ולימוד עצמי

צפה [בסרטון הנהדר הזה](https://www.youtube.com/watch?v=qv6UVOQ0F44) שמדבר על איך מחשב יכול ללמוד לשחק סופר מריו באמצעות רשתות עצביות שמאומנות על ידי אלגוריתמים גנטיים. נלמד עוד על מחשבים שלומדים לשחק משחקים כאלה [בקטע הבא](../22-DeepRL/README.md).

## [מטלה: משוואה דיופנטית](Diophantine.ipynb)

המטרה שלך היא לפתור את מה שנקרא **משוואה דיופנטית** - משוואה עם שורשים שלמים. לדוגמה, שקול את המשוואה a+2b+3c+4d=30. עליך למצוא את השורשים השלמים שמקיימים את המשוואה.

*מטלה זו בהשראת [הפוסט הזה](https://habr.com/post/128704/).*

רמזים:

1. ניתן לשקול שורשים בטווח [0;30]
1. כגן, שקול להשתמש ברשימת ערכי השורשים

השתמש ב-[Diophantine.ipynb](Diophantine.ipynb) כנקודת התחלה.

---

