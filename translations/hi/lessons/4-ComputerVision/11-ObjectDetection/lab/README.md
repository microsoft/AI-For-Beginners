# हॉलीवुड हेड्स डेटासेट का उपयोग करके हेड डिटेक्शन

[AI for Beginners Curriculum](https://github.com/microsoft/ai-for-beginners) से लैब असाइनमेंट।

## कार्य

वीडियो सर्विलांस कैमरा स्ट्रीम पर लोगों की संख्या गिनना एक महत्वपूर्ण कार्य है, जो हमें दुकानों में आगंतुकों की संख्या, रेस्तरां में व्यस्त समय आदि का अनुमान लगाने में मदद करेगा। इस कार्य को हल करने के लिए, हमें विभिन्न कोणों से मानव सिर का पता लगाने में सक्षम होना चाहिए। मानव सिर का पता लगाने के लिए ऑब्जेक्ट डिटेक्शन मॉडल को प्रशिक्षित करने के लिए, हम [हॉलीवुड हेड्स डेटासेट](https://www.di.ens.fr/willow/research/headdetection/) का उपयोग कर सकते हैं।

## डेटासेट

[हॉलीवुड हेड्स डेटासेट](https://www.di.ens.fr/willow/research/headdetection/release/HollywoodHeads.zip) में 369,846 मानव सिर शामिल हैं, जो हॉलीवुड फिल्मों के 224,740 मूवी फ्रेम्स में एनोटेट किए गए हैं। इसे [https://host.robots.ox.ac.uk/pascal/VOC/](../../../../../../lessons/4-ComputerVision/11-ObjectDetection/lab/PASCAL VOC) फॉर्मेट में प्रदान किया गया है, जहां प्रत्येक इमेज के लिए एक XML विवरण फ़ाइल भी होती है, जो इस प्रकार दिखती है:

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

इस डेटासेट में केवल एक ऑब्जेक्ट क्लास `head` है, और प्रत्येक सिर के लिए आपको बॉक्स की सीमाओं के निर्देशांक मिलते हैं। आप XML को Python लाइब्रेरीज़ का उपयोग करके पार्स कर सकते हैं, या [इस लाइब्रेरी](https://pypi.org/project/pascal-voc/) का उपयोग करके सीधे PASCAL VOC फॉर्मेट के साथ काम कर सकते हैं।

## ऑब्जेक्ट डिटेक्शन का प्रशिक्षण

आप ऑब्जेक्ट डिटेक्शन मॉडल को निम्नलिखित तरीकों में से किसी एक का उपयोग करके प्रशिक्षित कर सकते हैं:

* [Azure Custom Vision](https://docs.microsoft.com/azure/cognitive-services/custom-vision-service/quickstarts/object-detection?tabs=visual-studio&WT.mc_id=academic-77998-cacaste) और इसका Python API का उपयोग करके क्लाउड में प्रोग्रामेटिक रूप से मॉडल को प्रशिक्षित करें। कस्टम विजन कुछ सौ इमेज से अधिक का उपयोग मॉडल को प्रशिक्षित करने के लिए नहीं कर सकता, इसलिए आपको डेटासेट को सीमित करना पड़ सकता है।
* [Keras tutorial](https://keras.io/examples/vision/retinanet/) के उदाहरण का उपयोग करके RetunaNet मॉडल को प्रशिक्षित करें।
* [torchvision.models.detection.RetinaNet](https://pytorch.org/vision/stable/_modules/torchvision/models/detection/retinanet.html) में उपलब्ध मॉड्यूल का उपयोग करें।

## निष्कर्ष

ऑब्जेक्ट डिटेक्शन एक ऐसा कार्य है जिसकी उद्योग में अक्सर आवश्यकता होती है। जबकि कुछ सेवाएं हैं जो ऑब्जेक्ट डिटेक्शन करने के लिए उपयोग की जा सकती हैं (जैसे [Azure Custom Vision](https://docs.microsoft.com/azure/cognitive-services/custom-vision-service/quickstarts/object-detection?tabs=visual-studio&WT.mc_id=academic-77998-cacaste)), यह समझना महत्वपूर्ण है कि ऑब्जेक्ट डिटेक्शन कैसे काम करता है और अपने स्वयं के मॉडल को प्रशिक्षित करने में सक्षम होना चाहिए।

**अस्वीकरण**:  
यह दस्तावेज़ AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) का उपयोग करके अनुवादित किया गया है। जबकि हम सटीकता के लिए प्रयासरत हैं, कृपया ध्यान दें कि स्वचालित अनुवाद में त्रुटियां या अशुद्धियां हो सकती हैं। मूल भाषा में उपलब्ध मूल दस्तावेज़ को प्रामाणिक स्रोत माना जाना चाहिए। महत्वपूर्ण जानकारी के लिए, पेशेवर मानव अनुवाद की सिफारिश की जाती है। इस अनुवाद के उपयोग से उत्पन्न किसी भी गलतफहमी या गलत व्याख्या के लिए हम उत्तरदायी नहीं हैं।