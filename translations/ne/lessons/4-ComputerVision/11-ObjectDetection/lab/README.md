# हलिवुड हेड्स डेटासेट प्रयोग गरेर हेड डिटेक्शन

[AI for Beginners Curriculum](https://github.com/microsoft/ai-for-beginners) बाट ल्याब असाइनमेन्ट।

## कार्य

भिडियो निगरानी क्यामेरा स्ट्रिममा मानिसहरूको संख्या गणना गर्नु महत्त्वपूर्ण कार्य हो जसले हामीलाई पसलहरूमा आगन्तुकहरूको संख्या, रेस्टुरेन्टको व्यस्त समय आदि अनुमान गर्न मद्दत गर्दछ। यो कार्य समाधान गर्न, हामीले विभिन्न कोणबाट मानव टाउकोहरू पत्ता लगाउन सक्षम हुनुपर्छ। मानव टाउकोहरू पत्ता लगाउनको लागि वस्तु डिटेक्शन मोडेललाई प्रशिक्षण दिन, हामी [हलिवुड हेड्स डेटासेट](https://www.di.ens.fr/willow/research/headdetection/) प्रयोग गर्न सक्छौं।

## डेटासेट

[हलिवुड हेड्स डेटासेट](https://www.di.ens.fr/willow/research/headdetection/release/HollywoodHeads.zip) मा हलिवुड फिल्मका 224,740 फ्रेमहरूमा 369,846 मानव टाउकोहरू एनोटेट गरिएको छ। यो [https://host.robots.ox.ac.uk/pascal/VOC/](../../../../../../lessons/4-ComputerVision/11-ObjectDetection/lab/PASCAL VOC) फर्म्याटमा प्रदान गरिएको छ, जहाँ प्रत्येक तस्बिरको लागि XML विवरण फाइल पनि हुन्छ, जुन यस प्रकार देखिन्छ:

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

यस डेटासेटमा केवल एक प्रकारको वस्तु `head` छ, र प्रत्येक टाउकोको लागि तपाईंलाई बाउन्डिङ बक्सको समन्वय प्राप्त हुन्छ। तपाईं Python लाइब्रेरीहरू प्रयोग गरेर XML पार्स गर्न सक्नुहुन्छ, वा [यो लाइब्रेरी](https://pypi.org/project/pascal-voc/) प्रयोग गरेर PASCAL VOC फर्म्याटसँग सीधा काम गर्न सक्नुहुन्छ।

## वस्तु डिटेक्शन प्रशिक्षण

तपाईं वस्तु डिटेक्शन मोडेललाई निम्न तरिकाहरू प्रयोग गरेर प्रशिक्षण दिन सक्नुहुन्छ:

* [Azure Custom Vision](https://docs.microsoft.com/azure/cognitive-services/custom-vision-service/quickstarts/object-detection?tabs=visual-studio&WT.mc_id=academic-77998-cacaste) र यसको Python API प्रयोग गरेर क्लाउडमा मोडेललाई प्रोग्रामेटिक रूपमा प्रशिक्षण दिन। Custom Vision ले मोडेल प्रशिक्षणको लागि केही सय तस्बिरहरू मात्र प्रयोग गर्न सक्नेछ, त्यसैले तपाईंले डेटासेट सीमित गर्न आवश्यक पर्न सक्छ।
* [Keras ट्युटोरियल](https://keras.io/examples/vision/retinanet/) बाट उदाहरण प्रयोग गरेर RetunaNet मोडेल प्रशिक्षण गर्न।
* [torchvision.models.detection.RetinaNet](https://pytorch.org/vision/stable/_modules/torchvision/models/detection/retinanet.html) मा उपलब्ध बिल्ट-इन मोड्युल प्रयोग गरेर।

## मुख्य कुरा

वस्तु डिटेक्शन उद्योगमा बारम्बार आवश्यक पर्ने कार्य हो। जबकि केही सेवाहरू (जस्तै [Azure Custom Vision](https://docs.microsoft.com/azure/cognitive-services/custom-vision-service/quickstarts/object-detection?tabs=visual-studio&WT.mc_id=academic-77998-cacaste)) वस्तु डिटेक्शन गर्न प्रयोग गर्न सकिन्छ, वस्तु डिटेक्शन कसरी काम गर्छ भन्ने बुझ्न र आफ्नै मोडेलहरू प्रशिक्षण दिन सक्षम हुनु महत्त्वपूर्ण छ।

**अस्वीकरण**:  
यो दस्तावेज़ AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) प्रयोग गरी अनुवाद गरिएको हो। हामी यथासम्भव सटीकता सुनिश्चित गर्न प्रयास गर्छौं, तर कृपया ध्यान दिनुहोस् कि स्वचालित अनुवादहरूमा त्रुटि वा अशुद्धता हुन सक्छ। यसको मूल भाषामा रहेको मूल दस्तावेज़लाई आधिकारिक स्रोत मानिनुपर्छ। महत्त्वपूर्ण जानकारीका लागि, व्यावसायिक मानव अनुवाद सिफारिस गरिन्छ। यस अनुवादको प्रयोगबाट उत्पन्न हुने कुनै पनि गलतफहमी वा गलत व्याख्याका लागि हामी जिम्मेवार हुने छैनौं।