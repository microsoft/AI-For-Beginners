# हॉलिवूड हेड्स डेटासेट वापरून हेड डिटेक्शन

[AI फॉर बिगिनर्स करिक्युलम](https://github.com/microsoft/ai-for-beginners) मधील लॅब असाइनमेंट.

## कार्य

व्हिडिओ सर्व्हिलन्स कॅमेरा स्ट्रीमवर लोकांची संख्या मोजणे हे एक महत्त्वाचे कार्य आहे, ज्यामुळे आपल्याला दुकानांमधील भेट देणाऱ्यांची संख्या, रेस्टॉरंटमधील व्यस्त तास इत्यादींचा अंदाज लावता येतो. हे कार्य सोडवण्यासाठी, आपल्याला वेगवेगळ्या कोनांमधून मानवी डोके ओळखता यायला हवे. मानवी डोके ओळखण्यासाठी ऑब्जेक्ट डिटेक्शन मॉडेल प्रशिक्षण देण्यासाठी आपण [हॉलिवूड हेड्स डेटासेट](https://www.di.ens.fr/willow/research/headdetection/) वापरू शकतो.

## डेटासेट

[हॉलिवूड हेड्स डेटासेट](https://www.di.ens.fr/willow/research/headdetection/release/HollywoodHeads.zip) मध्ये हॉलिवूड चित्रपटांमधील 224,740 फ्रेम्समध्ये 369,846 मानवी डोक्यांची अ‍ॅनोटेशन आहे. हे [https://host.robots.ox.ac.uk/pascal/VOC/](../../../../../../lessons/4-ComputerVision/11-ObjectDetection/lab/PASCAL VOC) स्वरूपात प्रदान केले आहे, जिथे प्रत्येक प्रतिमेसाठी एक XML वर्णन फाइल देखील आहे, जी अशा प्रकारे दिसते:

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

या डेटासेटमध्ये फक्त एकच ऑब्जेक्ट वर्ग आहे `head`, आणि प्रत्येक डोक्यासाठी, तुम्हाला बाउंडिंग बॉक्सचे समन्वय मिळतात. तुम्ही XML पार्स करण्यासाठी Python लायब्ररी वापरू शकता, किंवा [ही लायब्ररी](https://pypi.org/project/pascal-voc/) वापरून थेट PASCAL VOC स्वरूप हाताळू शकता.

## ऑब्जेक्ट डिटेक्शन प्रशिक्षण

तुम्ही ऑब्जेक्ट डिटेक्शन मॉडेल खालीलपैकी कोणत्याही पद्धतीने प्रशिक्षण देऊ शकता:

* [Azure Custom Vision](https://docs.microsoft.com/azure/cognitive-services/custom-vision-service/quickstarts/object-detection?tabs=visual-studio&WT.mc_id=academic-77998-cacaste) आणि त्याच्या Python API चा वापर करून क्लाउडमध्ये प्रोग्रामॅटिकली मॉडेल प्रशिक्षण द्या. कस्टम व्हिजन काहीशे प्रतिमांपेक्षा जास्त डेटासेटसाठी प्रशिक्षण देऊ शकणार नाही, त्यामुळे तुम्हाला डेटासेट मर्यादित करावे लागेल.
* [Keras ट्युटोरियल](https://keras.io/examples/vision/retinanet/) मधील उदाहरण वापरून RetunaNet मॉडेल प्रशिक्षण द्या.
* [torchvision.models.detection.RetinaNet](https://pytorch.org/vision/stable/_modules/torchvision/models/detection/retinanet.html) या torchvision मधील बिल्ट-इन मॉड्यूलचा वापर करा.

## मुख्य मुद्दे

ऑब्जेक्ट डिटेक्शन हे उद्योगात वारंवार आवश्यक असलेले कार्य आहे. जरी काही सेवा (जसे की [Azure Custom Vision](https://docs.microsoft.com/azure/cognitive-services/custom-vision-service/quickstarts/object-detection?tabs=visual-studio&WT.mc_id=academic-77998-cacaste)) ऑब्जेक्ट डिटेक्शन करण्यासाठी वापरता येतात, तरीही ऑब्जेक्ट डिटेक्शन कसे कार्य करते हे समजून घेणे आणि स्वतःचे मॉडेल प्रशिक्षण देण्यास सक्षम असणे महत्त्वाचे आहे.

**अस्वीकरण**:  
हा दस्तऐवज AI भाषांतर सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) चा वापर करून भाषांतरित करण्यात आला आहे. आम्ही अचूकतेसाठी प्रयत्नशील असलो तरी, कृपया लक्षात घ्या की स्वयंचलित भाषांतरांमध्ये त्रुटी किंवा अचूकतेचा अभाव असू शकतो. मूळ भाषेतील मूळ दस्तऐवज हा अधिकृत स्रोत मानला जावा. महत्त्वाच्या माहितीसाठी, व्यावसायिक मानवी भाषांतराची शिफारस केली जाते. या भाषांतराचा वापर केल्यामुळे उद्भवणाऱ्या कोणत्याही गैरसमज किंवा चुकीच्या अर्थासाठी आम्ही जबाबदार राहणार नाही.