# למידה חיזוקית עמוקה

למידה חיזוקית (RL) נחשבת לאחד מהפרדיגמות הבסיסיות של למידת מכונה, לצד למידה מונחית ולמידה בלתי מונחית. בעוד שבלמידה מונחית אנו מסתמכים על מערך נתונים עם תוצאות ידועות, RL מבוססת על **למידה מתוך עשייה**. לדוגמה, כשאנו רואים לראשונה משחק מחשב, אנו מתחילים לשחק, גם בלי לדעת את החוקים, ובמהרה אנו מצליחים לשפר את הכישורים שלנו רק דרך תהליך המשחק והתאמת ההתנהגות שלנו.

## [שאלון לפני ההרצאה](https://ff-quizzes.netlify.app/en/ai/quiz/43)

כדי לבצע RL, אנו צריכים:

* **סביבה** או **סימולטור** שמגדיר את חוקי המשחק. עלינו להיות מסוגלים להריץ ניסויים בסימולטור ולצפות בתוצאות.
* **פונקציית תגמול**, שמצביעה על מידת ההצלחה של הניסוי שלנו. במקרה של למידה לשחק משחק מחשב, התגמול יהיה הניקוד הסופי שלנו.

בהתבסס על פונקציית התגמול, אנו צריכים להיות מסוגלים להתאים את ההתנהגות שלנו ולשפר את הכישורים שלנו, כך שבפעם הבאה נשחק טוב יותר. ההבדל המרכזי בין סוגי למידת מכונה אחרים לבין RL הוא שב-RL בדרך כלל איננו יודעים אם ניצחנו או הפסדנו עד לסיום המשחק. לכן, איננו יכולים לומר אם מהלך מסוים בפני עצמו הוא טוב או לא - אנו מקבלים תגמול רק בסוף המשחק.

במהלך RL, אנו בדרך כלל מבצעים ניסויים רבים. בכל ניסוי, עלינו לאזן בין שימוש באסטרטגיה האופטימלית שלמדנו עד כה (**ניצול**) לבין חקר מצבים חדשים אפשריים (**חקר**).

## OpenAI Gym

כלי מצוין ל-RL הוא [OpenAI Gym](https://gym.openai.com/) - **סביבת סימולציה**, שיכולה לדמות סביבות רבות ושונות, החל ממשחקי Atari ועד פיזיקה של איזון מוט. זו אחת מסביבות הסימולציה הפופולריות ביותר לאימון אלגוריתמים של למידה חיזוקית, והיא מתוחזקת על ידי [OpenAI](https://openai.com/).

> **Note**: ניתן לראות את כל הסביבות הזמינות ב-OpenAI Gym [כאן](https://gym.openai.com/envs/#classic_control).

## איזון מוט על עגלה

כנראה שכולכם ראיתם מכשירי איזון מודרניים כמו *Segway* או *Gyroscooters*. הם מסוגלים להתאזן אוטומטית על ידי התאמת הגלגלים שלהם בתגובה לאות ממאיץ או גירוסקופ. בחלק זה, נלמד כיצד לפתור בעיה דומה - איזון מוט. זה דומה למצב שבו אמן קרקס צריך לאזן מוט על ידו - אך איזון המוט כאן מתרחש רק בממד אחד.

גרסה פשוטה של איזון זו ידועה כבעיה של **CartPole**. בעולם ה-CartPole, יש לנו מחוון אופקי שיכול לזוז שמאלה או ימינה, והמטרה היא לאזן מוט אנכי על גבי המחוון בזמן שהוא זז.

<img alt="a cartpole" src="../../../../../translated_images/he/cartpole.f52a67f27e058170.webp" width="200"/>

כדי ליצור ולהשתמש בסביבה זו, אנו צריכים כמה שורות קוד ב-Python:

```python
import gym
env = gym.make("CartPole-v1")

env.reset()
done = False
total_reward = 0
while not done:
   env.render()
   action = env.action_space.sample()
   observaton, reward, done, info = env.step(action)
   total_reward += reward

print(f"Total reward: {total_reward}")
```

כל סביבה נגישה בדיוק באותו אופן:
* `env.reset` מתחיל ניסוי חדש
* `env.step` מבצע צעד סימולציה. הוא מקבל **פעולה** מתוך **מרחב הפעולות**, ומחזיר **תצפית** (ממרחב התצפיות), וכן תגמול ודגל סיום.

בדוגמה לעיל אנו מבצעים פעולה אקראית בכל צעד, ולכן אורך החיים של הניסוי קצר מאוד:

![non-balancing cartpole](../../../../../lessons/6-Other/22-DeepRL/images/cartpole-nobalance.gif)

המטרה של אלגוריתם RL היא לאמן מודל - מה שנקרא **מדיניות** &pi; - שיחזיר את הפעולה בתגובה למצב נתון. ניתן גם להתייחס למדיניות כאל הסתברותית, כלומר עבור כל מצב *s* ופעולה *a* היא תחזיר את ההסתברות &pi;(*a*|*s*) שעלינו לבצע את *a* במצב *s*.

## אלגוריתם Policy Gradients

הדרך הברורה ביותר למודל מדיניות היא על ידי יצירת רשת עצבית שתיקח מצבים כקלט ותחזיר פעולות מתאימות (או ליתר דיוק את ההסתברויות של כל הפעולות). במובן מסוים, זה יהיה דומה למשימת סיווג רגילה, עם הבדל מרכזי - איננו יודעים מראש אילו פעולות עלינו לבצע בכל אחד מהצעדים.

הרעיון כאן הוא להעריך את ההסתברויות הללו. אנו בונים וקטור של **תגמולים מצטברים** שמראה את התגמול הכולל שלנו בכל צעד של הניסוי. אנו גם מיישמים **הנחתת תגמול** על ידי הכפלת תגמולים מוקדמים יותר במקדם מסוים &gamma;=0.99, כדי להקטין את השפעתם של תגמולים מוקדמים. לאחר מכן, אנו מחזקים את הצעדים לאורך מסלול הניסוי שמניבים תגמולים גדולים יותר.

> למדו עוד על אלגוריתם Policy Gradient וצפו בו בפעולה ב-[מחברת הדוגמה](CartPole-RL-TF.ipynb).

## אלגוריתם Actor-Critic

גרסה משופרת של גישת Policy Gradients נקראת **Actor-Critic**. הרעיון המרכזי מאחוריה הוא שהרשת העצבית תתאמנה להחזיר שני דברים:

* המדיניות, שקובעת איזו פעולה לבצע. חלק זה נקרא **actor**
* הערכה של התגמול הכולל שאנו יכולים לצפות לקבל במצב זה - חלק זה נקרא **critic**.

במובן מסוים, הארכיטקטורה הזו מזכירה [GAN](../../4-ComputerVision/10-GANs/README.md), שבה יש לנו שתי רשתות שמתאמנות אחת נגד השנייה. במודל Actor-Critic, ה-actor מציע את הפעולה שעלינו לבצע, וה-critic מנסה להיות ביקורתי ולהעריך את התוצאה. עם זאת, המטרה שלנו היא לאמן את הרשתות הללו בהרמוניה.

מכיוון שאנו יודעים גם את התגמולים המצטברים האמיתיים וגם את התוצאות שה-critic מחזיר במהלך הניסוי, קל יחסית לבנות פונקציית הפסד שתמזער את ההבדל ביניהם. זה ייתן לנו **critic loss**. אנו יכולים לחשב **actor loss** באמצעות אותה גישה כמו באלגוריתם Policy Gradient.

לאחר הרצת אחד מהאלגוריתמים הללו, אנו יכולים לצפות שה-CartPole שלנו יתנהג כך:

![a balancing cartpole](../../../../../lessons/6-Other/22-DeepRL/images/cartpole-balance.gif)

## ✍️ תרגילים: Policy Gradients ו-Actor-Critic RL

המשיכו ללמוד במחברות הבאות:

* [RL ב-TensorFlow](CartPole-RL-TF.ipynb)
* [RL ב-PyTorch](CartPole-RL-PyTorch.ipynb)

## משימות RL אחרות

למידה חיזוקית כיום היא תחום מחקר שצומח במהירות. כמה דוגמאות מעניינות ללמידה חיזוקית הן:

* לימוד מחשב לשחק **משחקי Atari**. החלק המאתגר בבעיה זו הוא שאין לנו מצב פשוט שמיוצג כווקטור, אלא צילום מסך - ואנו צריכים להשתמש ב-CNN כדי להמיר את תמונת המסך לווקטור תכונות או לחלץ מידע על תגמול. משחקי Atari זמינים ב-Gym.
* לימוד מחשב לשחק משחקי לוח, כמו שחמט וגו. לאחרונה תוכניות מתקדמות כמו **Alpha Zero** אומנו מאפס על ידי שני סוכנים ששיחקו אחד נגד השני ושיפרו את עצמם בכל צעד.
* בתעשייה, RL משמש ליצירת מערכות בקרה מסימולציה. שירות בשם [Bonsai](https://azure.microsoft.com/services/project-bonsai/?WT.mc_id=academic-77998-cacaste) מיועד במיוחד לכך.

## סיכום

כעת למדנו כיצד לאמן סוכנים להשיג תוצאות טובות רק על ידי מתן פונקציית תגמול שמגדירה את מצב המשחק הרצוי, ועל ידי מתן הזדמנות לחקור את מרחב החיפוש בצורה חכמה. ניסינו בהצלחה שני אלגוריתמים, והשגנו תוצאה טובה בפרק זמן יחסית קצר. עם זאת, זהו רק תחילתו של המסע שלכם לתוך RL, וכדאי לכם לשקול לקחת קורס נפרד אם אתם רוצים להעמיק.

## 🚀 אתגר

חקור את היישומים המפורטים בסעיף 'משימות RL אחרות' ונסה ליישם אחד מהם!

## [שאלון לאחר ההרצאה](https://ff-quizzes.netlify.app/en/ai/quiz/44)

## סקירה ולימוד עצמי

למדו עוד על למידה חיזוקית קלאסית בתוכנית הלימודים שלנו [Machine Learning for Beginners](https://github.com/microsoft/ML-For-Beginners/blob/main/8-Reinforcement/README.md).

צפו ב-[סרטון נהדר זה](https://www.youtube.com/watch?v=qv6UVOQ0F44) שמדבר על איך מחשב יכול ללמוד לשחק סופר מריו.

## משימה: [אמן מכונית הרים](lab/README.md)

המטרה שלכם במשימה זו תהיה לאמן סביבה אחרת ב-Gym - [Mountain Car](https://www.gymlibrary.ml/environments/classic_control/mountain_car/).

---

