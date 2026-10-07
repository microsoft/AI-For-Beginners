# Hollywood Heads Dataset ka use karke Head Detection

[AI for Beginners Curriculum](https://github.com/microsoft/ai-for-beginners) se lab assignment.

## Task

Video surveillance camera stream par logon ki sankhya count karna ek important task hai, jo humein shops mein visitors ki sankhya, restaurants mein busy hours, aadi ka estimate lagane mein madad karega. Is task ko solve karne ke liye, humein alag-alag angles se insaani sir (human head) detect kar paana chahiye. Insaani sir detect karne ke liye object detection model train karne ke liye, hum [Hollywood Heads Dataset](https://www.di.ens.fr/willow/research/headdetection/) use kar sakte hain.

## Dataset

[Hollywood Heads Dataset](https://www.di.ens.fr/willow/research/headdetection/release/HollywoodHeads.zip) mein 369,846 human heads hain, jo Hollywood movies ke 224,740 movie frames mein annotate kiye gaye hain. Ise [https://host.robots.ox.ac.uk/pascal/VOC/](../../../../../../lessons/4-ComputerVision/11-ObjectDetection/lab/PASCAL VOC) format mein diya gaya hai, jahan har image ke liye ek XML description file bhi hoti hai, jo is tarah dikhti hai:

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

Is dataset mein sirf ek object class `head` hai, aur har head ke liye aapko box boundaries ke coordinates milte hain. Aap XML ko Python libraries se parse kar sakte hain, ya [is library](https://pypi.org/project/pascal-voc/) ka use karke seedhe PASCAL VOC format ke saath kaam kar sakte hain.

## Object Detection ki Training

Aap object detection model ko neeche diye gaye tareeko mein se kisi ek se train kar sakte hain:

* [Azure Custom Vision](https://docs.microsoft.com/azure/cognitive-services/custom-vision-service/quickstarts/object-detection?tabs=visual-studio&WT.mc_id=academic-77998-cacaste) aur uska Python API use karke cloud mein programmatically model train kijiye. Custom Vision model train karne ke liye kuch sau images se zyada use nahi kar sakta, isliye aapko dataset ko limit karna pad sakta hai.
* [Keras tutorial](https://keras.io/examples/vision/retinanet/) ka example use karke RetunaNet model train kijiye.
* [torchvision.models.detection.RetinaNet](https://pytorch.org/vision/stable/_modules/torchvision/models/detection/retinanet.html) mein available module use kijiye.

## Conclusion

Object detection ek aisa task hai jiski industry mein aksar zaroorat padti hai. Halanki kuch services hain jo object detection karne ke liye use ki ja sakti hain (jaise [Azure Custom Vision](https://docs.microsoft.com/azure/cognitive-services/custom-vision-service/quickstarts/object-detection?tabs=visual-studio&WT.mc_id=academic-77998-cacaste)), yeh samajhna zaroori hai ki object detection kaise kaam karta hai aur apne khud ke models train kar paana bhi aana chahiye.

---

<!-- HINGLISH NOTE START -->
**Note**:
Yeh document Hindi translation ko Hinglish (Roman script) mein convert karke banaya gaya hai, taaki padhna aur samajhna aasaan ho.
Isme kuch galtiyan ya anuvaad ki kamiyan ho sakti hain. Sabse sahi jaankari ke liye original English document ko hi authoritative source maanein.
<!-- HINGLISH NOTE END -->
