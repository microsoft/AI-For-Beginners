# זיהוי ראשים באמצעות Hollywood Heads Dataset

מטלת מעבדה מתוך [AI for Beginners Curriculum](https://github.com/microsoft/ai-for-beginners).

## משימה

ספירת מספר האנשים בזרם מצלמות אבטחה היא משימה חשובה שתאפשר לנו להעריך את מספר המבקרים בחנויות, שעות העומס במסעדות, ועוד. כדי לפתור משימה זו, עלינו להיות מסוגלים לזהות ראשים של בני אדם מזוויות שונות. כדי לאמן מודל לזיהוי אובייקטים שיזהה ראשים של בני אדם, ניתן להשתמש ב-[Hollywood Heads Dataset](https://www.di.ens.fr/willow/research/headdetection/).

## מערך הנתונים

[Hollywood Heads Dataset](https://www.di.ens.fr/willow/research/headdetection/release/HollywoodHeads.zip) מכיל 369,846 ראשים של בני אדם שסומנו ב-224,740 פריימים מסרטי הוליווד. הוא מסופק בפורמט [https://host.robots.ox.ac.uk/pascal/VOC/](../../../../../../lessons/4-ComputerVision/11-ObjectDetection/lab/PASCAL VOC), שבו לכל תמונה יש גם קובץ תיאור XML שנראה כך:

```xml
<annotation>
	<folder>HollywoodHeads</folder>
	<filename>mov_021_149390.jpeg</filename>
	<source>
		<database>HollywoodHeads 2015 Database</database>
		<annotation>HollywoodHeads 2015</annotation>
		<image>WILLOW</image>
	</source>
	<size>
		<width>608</width>
		<height>320</height>
		<depth>3</depth>
	</size>
	<segmented>0</segmented>
	<object>
		<name>head</name>
		<bndbox>
			<xmin>201</xmin>
			<ymin>1</ymin>
			<xmax>480</xmax>
			<ymax>263</ymax>
		</bndbox>
		<difficult>0</difficult>
	</object>
	<object>
		<name>head</name>
		<bndbox>
			<xmin>3</xmin>
			<ymin>4</ymin>
			<xmax>241</xmax>
			<ymax>285</ymax>
		</bndbox>
		<difficult>0</difficult>
	</object>
</annotation>
```

במערך נתונים זה יש רק מחלקה אחת של אובייקטים `head`, ולכל ראש מתקבלים הקואורדינטות של תיבת הגבול. ניתן לנתח את קבצי ה-XML באמצעות ספריות Python, או להשתמש ב-[ספרייה זו](https://pypi.org/project/pascal-voc/) כדי לעבוד ישירות עם פורמט PASCAL VOC.

## אימון זיהוי אובייקטים

ניתן לאמן מודל לזיהוי אובייקטים באחת מהדרכים הבאות:

* שימוש ב-[Azure Custom Vision](https://docs.microsoft.com/azure/cognitive-services/custom-vision-service/quickstarts/object-detection?tabs=visual-studio&WT.mc_id=academic-77998-cacaste) וב-API של Python כדי לאמן את המודל בענן באופן תכנותי. Custom Vision לא יוכל להשתמש ביותר מכמה מאות תמונות לאימון המודל, ולכן ייתכן שתצטרכו להגביל את מערך הנתונים.
* שימוש בדוגמה מתוך [המדריך של Keras](https://keras.io/examples/vision/retinanet/) לאימון מודל RetunaNet.
* שימוש במודול המובנה [torchvision.models.detection.RetinaNet](https://pytorch.org/vision/stable/_modules/torchvision/models/detection/retinanet.html) ב-torchvision.

## מסקנות

זיהוי אובייקטים הוא משימה שנדרשת לעיתים קרובות בתעשייה. למרות שישנם שירותים שיכולים לבצע זיהוי אובייקטים (כגון [Azure Custom Vision](https://docs.microsoft.com/azure/cognitive-services/custom-vision-service/quickstarts/object-detection?tabs=visual-studio&WT.mc_id=academic-77998-cacaste)), חשוב להבין כיצד זיהוי אובייקטים פועל ולהיות מסוגלים לאמן מודלים בעצמכם.

---

**כתב ויתור**:  
מסמך זה תורגם באמצעות שירות תרגום מבוסס בינה מלאכותית [Co-op Translator](https://github.com/Azure/co-op-translator). למרות שאנו שואפים לדיוק, יש לקחת בחשבון שתרגומים אוטומטיים עשויים להכיל שגיאות או אי דיוקים. המסמך המקורי בשפתו המקורית צריך להיחשב כמקור סמכותי. עבור מידע קריטי, מומלץ להשתמש בתרגום מקצועי על ידי אדם. איננו נושאים באחריות לאי הבנות או לפרשנויות שגויות הנובעות משימוש בתרגום זה.