<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "d76a7eda28de5210c8b1ba50a6216c69",
  "translation_date": "2025-09-23T10:17:59+00:00",
  "source_file": "lessons/4-ComputerVision/11-ObjectDetection/README.md",
  "language_code": "he"
}
-->
# זיהוי אובייקטים

המודלים של סיווג תמונות שעסקנו בהם עד כה לקחו תמונה והפיקו תוצאה קטגורית, כמו הקטגוריה 'מספר' בבעיה של MNIST. עם זאת, במקרים רבים אנחנו לא רוצים רק לדעת שתמונה מציגה אובייקטים - אנחנו רוצים להיות מסוגלים לקבוע את המיקום המדויק שלהם. זה בדיוק הנקודה של **זיהוי אובייקטים**.

## [שאלון לפני השיעור](https://ff-quizzes.netlify.app/en/ai/quiz/21)

![זיהוי אובייקטים](../../../../../translated_images/Screen_Shot_2016-11-17_at_11.14.54_AM.b4bb3769353287be1b905373ed9c858102c054b16e4595c76ec3f7bba0feb549.he.png)

> תמונה מתוך [אתר YOLO v2](https://pjreddie.com/darknet/yolov2/)

## גישה נאיבית לזיהוי אובייקטים

נניח שרצינו למצוא חתול בתמונה, גישה נאיבית מאוד לזיהוי אובייקטים תהיה כדלקמן:

1. לחלק את התמונה למספר אריחים.
2. להריץ סיווג תמונה על כל אריח.
3. אריחים שמפיקים הפעלה גבוהה מספיק יכולים להיחשב ככאלה שמכילים את האובייקט המדובר.

![זיהוי נאיבי של אובייקטים](../../../../../translated_images/naive-detection.e7f1ba220ccd08c68a2ea8e06a7ed75c3fcc738c2372f9e00b7f4299a8659c01.he.png)

> *תמונה מתוך [מחברת התרגילים](ObjectDetection-TF.ipynb)*

עם זאת, גישה זו רחוקה מלהיות אידיאלית, מכיוון שהיא מאפשרת לאלגוריתם לאתר את תיבת הגבול של האובייקט בצורה מאוד לא מדויקת. כדי למקם בצורה מדויקת יותר, עלינו להריץ סוג של **רגרסיה** כדי לחזות את הקואורדינטות של תיבות הגבול - ולשם כך אנו זקוקים למערכי נתונים ספציפיים.

## רגרסיה לזיהוי אובייקטים

[פוסט הבלוג הזה](https://towardsdatascience.com/object-detection-with-neural-networks-a4e2c46b4491) מציע מבוא עדין ומעולה לזיהוי צורות.

## מערכי נתונים לזיהוי אובייקטים

ייתכן שתיתקלו במערכי הנתונים הבאים למשימה זו:

* [PASCAL VOC](http://host.robots.ox.ac.uk/pascal/VOC/) - 20 קטגוריות
* [COCO](http://cocodataset.org/#home) - אובייקטים נפוצים בהקשר. 80 קטגוריות, תיבות גבול ומסכות סגמנטציה

![COCO](../../../../../translated_images/coco-examples.71bc60380fa6cceb7caad48bd09e35b6028caabd363aa04fee89c414e0870e86.he.jpg)

## מדדים לזיהוי אובייקטים

### חיתוך על איחוד (Intersection over Union)

בעוד שבסיווג תמונות קל למדוד עד כמה האלגוריתם מצליח, בזיהוי אובייקטים עלינו למדוד גם את נכונות הקטגוריה וגם את דיוק מיקום תיבת הגבול שחוזה האלגוריתם. עבור האחרון, אנו משתמשים במדד שנקרא **חיתוך על איחוד** (IoU), שמודד עד כמה שתי תיבות (או שני אזורים שרירותיים) חופפים.

![IoU](../../../../../translated_images/iou_equation.9a4751d40fff4e119ecd0a7bcca4e71ab1dc83e0d4f2a0d66ff0859736f593cf.he.png)

> *איור 2 מתוך [פוסט בלוג מצוין על IoU](https://pyimagesearch.com/2016/11/07/intersection-over-union-iou-for-object-detection/)*

הרעיון פשוט - אנו מחלקים את שטח החיתוך בין שתי הצורות בשטח האיחוד שלהן. עבור שני אזורים זהים, IoU יהיה 1, בעוד שעבור אזורים שאינם חופפים כלל הוא יהיה 0. אחרת הוא ינוע בין 0 ל-1. בדרך כלל אנו מתחשבים רק בתיבות גבול עבורן IoU מעל ערך מסוים.

### דיוק ממוצע (Average Precision)

נניח שאנחנו רוצים למדוד עד כמה קטגוריה מסוימת של אובייקטים $C$ מזוהה היטב. כדי למדוד זאת, אנו משתמשים במדד **דיוק ממוצע**, שמחושב כך:

1. עקומת דיוק-שליפה (Precision-Recall) מציגה את הדיוק בהתאם לערך סף זיהוי (מ-0 עד 1).
2. בהתאם לסף, נקבל יותר או פחות אובייקטים מזוהים בתמונה, וערכים שונים של דיוק ושליפה.
3. העקומה תיראה כך:

<img src="https://github.com/shwars/NeuroWorkshop/raw/master/images/ObjDetectionPrecisionRecall.png"/>

> *תמונה מתוך [NeuroWorkshop](http://github.com/shwars/NeuroWorkshop)*

הדיוק הממוצע עבור קטגוריה נתונה $C$ הוא השטח מתחת לעקומה זו. באופן מדויק יותר, ציר השליפה מחולק בדרך כלל ל-10 חלקים, והדיוק מחושב כממוצע על כל הנקודות הללו:

$$
AP = {1\over11}\sum_{i=0}^{10}\mbox{Precision}(\mbox{Recall}={i\over10})
$$

### AP ו-IoU

נשקול רק את הזיהויים עבורם IoU מעל ערך מסוים. לדוגמה, במערך הנתונים PASCAL VOC בדרך כלל $\mbox{IoU Threshold} = 0.5$, בעוד שב-COCO AP נמדד עבור ערכים שונים של $\mbox{IoU Threshold}$.

<img src="https://github.com/shwars/NeuroWorkshop/raw/master/images/ObjDetectionPrecisionRecallIoU.png"/>

> *תמונה מתוך [NeuroWorkshop](http://github.com/shwars/NeuroWorkshop)*

### דיוק ממוצע כולל - mAP

המדד המרכזי לזיהוי אובייקטים נקרא **דיוק ממוצע כולל**, או **mAP**. זהו ערך הדיוק הממוצע, מחושב כממוצע על פני כל קטגוריות האובייקטים, ולעיתים גם על פני $\mbox{IoU Threshold}$. תהליך חישוב **mAP** מתואר בפירוט
[בפוסט בלוג הזה](https://medium.com/@timothycarlen/understanding-the-map-evaluation-metric-for-object-detection-a07fe6962cf3)), וגם [כאן עם דוגמאות קוד](https://gist.github.com/tarlen5/008809c3decf19313de216b9208f3734).

## גישות שונות לזיהוי אובייקטים

ישנן שתי קטגוריות עיקריות של אלגוריתמים לזיהוי אובייקטים:

* **רשתות הצעת אזורים** (R-CNN, Fast R-CNN, Faster R-CNN). הרעיון המרכזי הוא ליצור **אזורים מעניינים** (ROI) ולהריץ CNN עליהם, בחיפוש אחר הפעלה מקסימלית. זה קצת דומה לגישה הנאיבית, למעט העובדה שה-ROI נוצרים בצורה חכמה יותר. אחד החסרונות המרכזיים של שיטות אלו הוא שהן איטיות, מכיוון שצריך לבצע מספר רב של מעברים של מסווג CNN על התמונה.
* **מעבר אחד** (YOLO, SSD, RetinaNet). בארכיטקטורות אלו אנו מעצבים את הרשת כך שתנבא גם קטגוריות וגם ROI במעבר אחד.

### R-CNN: רשת CNN מבוססת אזורים

[R-CNN](http://islab.ulsan.ac.kr/files/announcement/513/rcnn_pami.pdf) משתמשת ב-[חיפוש סלקטיבי](http://www.huppelen.nl/publications/selectiveSearchDraft.pdf) כדי ליצור מבנה היררכי של אזורי ROI, אשר מועברים לאחר מכן דרך מחלצי תכונות של CNN ומסווגי SVM כדי לקבוע את קטגוריית האובייקט, ורגרסיה ליניארית כדי לקבוע את קואורדינטות *תיבת הגבול*. [מאמר רשמי](https://arxiv.org/pdf/1506.01497v1.pdf)

![RCNN](../../../../../translated_images/rcnn1.cae407020dfb1d1fb572656e44f75cd6c512cc220591c116c506652c10e47f26.he.png)

> *תמונה מתוך van de Sande et al. ICCV’11*

![RCNN-1](../../../../../translated_images/rcnn2.2d9530bb83516484ec65b250c22dbf37d3d23244f32864ebcb91d98fe7c3112c.he.png)

> *תמונות מתוך [הבלוג הזה](https://towardsdatascience.com/r-cnn-fast-r-cnn-faster-r-cnn-yolo-object-detection-algorithms-36d53571365e)*

### F-RCNN - Fast R-CNN

גישה זו דומה ל-R-CNN, אך האזורים מוגדרים לאחר יישום שכבות הקונבולוציה.

![FRCNN](../../../../../translated_images/f-rcnn.3cda6d9bb41888754037d2d9763e2298a96de5d9bc2a21db3147357aa5da9b1a.he.png)

> תמונה מתוך [המאמר הרשמי](https://www.cv-foundation.org/openaccess/content_iccv_2015/papers/Girshick_Fast_R-CNN_ICCV_2015_paper.pdf), [arXiv](https://arxiv.org/pdf/1504.08083.pdf), 2015

### Faster R-CNN

הרעיון המרכזי בגישה זו הוא להשתמש ברשת עצבית כדי לנבא ROI - מה שנקרא *רשת הצעת אזורים*. [מאמר](https://arxiv.org/pdf/1506.01497.pdf), 2016

![FasterRCNN](../../../../../translated_images/faster-rcnn.8d46c099b87ef30ab2ea26dbc4bdd85b974a57ba8eb526f65dc4cd0a4711de30.he.png)

> תמונה מתוך [המאמר הרשמי](https://arxiv.org/pdf/1506.01497.pdf)

### R-FCN: רשת מבוססת אזורים עם קונבולוציה מלאה

אלגוריתם זה מהיר יותר מ-Faster R-CNN. הרעיון המרכזי הוא כדלקמן:

1. אנו מחלצים תכונות באמצעות ResNet-101.
2. התכונות מעובדות על ידי **מפת ניקוד רגישה למיקום**. כל אובייקט מתוך $C$ קטגוריות מחולק ל-$k\times k$ אזורים, ואנו מאמנים לחזות חלקים של אובייקטים.
3. עבור כל חלק מתוך $k\times k$ אזורים כל הרשתות מצביעות על קטגוריות אובייקטים, וקטגוריית האובייקט עם ההצבעה המקסימלית נבחרת.

![r-fcn image](../../../../../translated_images/r-fcn.13eb88158b99a3da50fa2787a6be5cb310d47f0e9655cc93a1090dc7aab338d1.he.png)

> תמונה מתוך [המאמר הרשמי](https://arxiv.org/abs/1605.06409)

### YOLO - You Only Look Once

YOLO הוא אלגוריתם בזמן אמת במעבר אחד. הרעיון המרכזי הוא כדלקמן:

 * התמונה מחולקת ל-$S\times S$ אזורים.
 * עבור כל אזור, **CNN** מנבא $n$ אובייקטים אפשריים, *קואורדינטות תיבת הגבול* ו-*ביטחון*=*הסתברות* * IoU.

 ![YOLO](../../../../../translated_images/yolo.a2648ec82ee8bb4ea27537677adb482fd4b733ca1705c561b6a24a85102dced5.he.png)

> תמונה מתוך [המאמר הרשמי](https://arxiv.org/abs/1506.02640)

### אלגוריתמים נוספים

* RetinaNet: [מאמר רשמי](https://arxiv.org/abs/1708.02002)
   - [מימוש ב-PyTorch ב-Torchvision](https://pytorch.org/vision/stable/_modules/torchvision/models/detection/retinanet.html)
   - [מימוש ב-Keras](https://github.com/fizyr/keras-retinanet)
   - [זיהוי אובייקטים עם RetinaNet](https://keras.io/examples/vision/retinanet/) בדוגמאות של Keras
* SSD (Single Shot Detector): [מאמר רשמי](https://arxiv.org/abs/1512.02325)

## ✍️ תרגילים: זיהוי אובייקטים

המשיכו את הלמידה במחברת הבאה:

[ObjectDetection.ipynb](ObjectDetection.ipynb)

## סיכום

בשיעור זה עשיתם סיור מהיר בכל הדרכים השונות שבהן ניתן לבצע זיהוי אובייקטים!

## 🚀 אתגר

קראו את המאמרים והמחברות על YOLO ונסו אותם בעצמכם:

* [פוסט בלוג טוב](https://www.analyticsvidhya.com/blog/2018/12/practical-guide-object-detection-yolo-framewor-python/) שמתאר את YOLO
 * [אתר רשמי](https://pjreddie.com/darknet/yolo/)
 * YOLO: [מימוש ב-Keras](https://github.com/experiencor/keras-yolo2), [מחברת שלב-אחר-שלב](https://github.com/experiencor/basic-yolo-keras/blob/master/Yolo%20Step-by-Step.ipynb)
 * YOLO v2: [מימוש ב-Keras](https://github.com/experiencor/keras-yolo2), [מחברת שלב-אחר-שלב](https://github.com/experiencor/keras-y

---

