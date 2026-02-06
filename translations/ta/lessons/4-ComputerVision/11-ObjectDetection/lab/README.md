# ஹாலிவுட் ஹெட்ஸ் டேட்டாசெட் பயன்படுத்தி தலை கண்டறிதல்

[AI for Beginners Curriculum](https://github.com/microsoft/ai-for-beginners) இல் இருந்து ஆய்வகப் பணிக்கான ஒதுக்கீடு.

## பணிகள்

வீடியோ கண்காணிப்பு கேமரா ஸ்ட்ரீமில் உள்ள மனிதர்களின் எண்ணிக்கையை கணக்கிடுவது முக்கியமான பணியாகும். இது கடைகளில் வருகையாளர்களின் எண்ணிக்கையை, உணவகங்களில் பிஸியான நேரங்களை மதிப்பீடு செய்ய உதவும். இந்த பணியை தீர்க்க, பல்வேறு கோணங்களில் இருந்து மனித தலைகளை கண்டறிய வேண்டும். மனித தலைகளை கண்டறிய ஒரு பொருள் கண்டறிதல் மாடலை பயிற்சி செய்ய, [ஹாலிவுட் ஹெட்ஸ் டேட்டாசெட்](https://www.di.ens.fr/willow/research/headdetection/) பயன்படுத்தலாம்.

## டேட்டாசெட்

[ஹாலிவுட் ஹெட்ஸ் டேட்டாசெட்](https://www.di.ens.fr/willow/research/headdetection/release/HollywoodHeads.zip) 369,846 மனித தலைகளை 224,740 ஹாலிவுட் திரைப்படக் காட்சிகளில் குறிக்கோள் வைத்து வழங்குகிறது. இது [https://host.robots.ox.ac.uk/pascal/VOC/](../../../../../../lessons/4-ComputerVision/11-ObjectDetection/lab/PASCAL VOC) வடிவத்தில் வழங்கப்படுகிறது, இதில் ஒவ்வொரு படத்திற்கும் XML விளக்கம் கோப்பும் உள்ளது. அது இவ்வாறு இருக்கும்:

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

இந்த டேட்டாசெட்டில், `head` என்ற ஒரே வகை பொருள் உள்ளது, மேலும் ஒவ்வொரு தலைக்கும், பவுண்டிங் பாக்ஸ் கோர்டினேட்கள் வழங்கப்படுகின்றன. XML-ஐ Python நூலகங்களைப் பயன்படுத்தி பார்ச் செய்யலாம் அல்லது [இந்த நூலகத்தை](https://pypi.org/project/pascal-voc/) பயன்படுத்தி PASCAL VOC வடிவத்துடன் நேரடியாக செயல்படலாம்.

## பொருள் கண்டறிதல் மாடல் பயிற்சி 

பொருள் கண்டறிதல் மாடலை பின்வரும் வழிகளில் பயிற்சி செய்யலாம்:

* [Azure Custom Vision](https://docs.microsoft.com/azure/cognitive-services/custom-vision-service/quickstarts/object-detection?tabs=visual-studio&WT.mc_id=academic-77998-cacaste) மற்றும் அதன் Python API-யை பயன்படுத்தி மாடலை மேகத்தில் நிரலாக்கமாக பயிற்சி செய்யலாம். Custom Vision ஒரு சில நூற்றுக்கணக்கான படங்களை மட்டுமே பயிற்சிக்க பயன்படுத்த முடியும், எனவே டேட்டாசெட்டை வரையறுக்க வேண்டியிருக்கும்.
* [Keras tutorial](https://keras.io/examples/vision/retinanet/) உதாரணத்தைப் பயன்படுத்தி RetunaNet மாடலை பயிற்சி செய்யலாம்.
* [torchvision.models.detection.RetinaNet](https://pytorch.org/vision/stable/_modules/torchvision/models/detection/retinanet.html) இல் உள்ள build-in மாடியூலை பயன்படுத்தி பயிற்சி செய்யலாம்.

## முக்கியக் கருத்து

பொருள் கண்டறிதல் என்பது தொழில்துறையில் அடிக்கடி தேவைப்படும் ஒரு பணி. [Azure Custom Vision](https://docs.microsoft.com/azure/cognitive-services/custom-vision-service/quickstarts/object-detection?tabs=visual-studio&WT.mc_id=academic-77998-cacaste) போன்ற சில சேவைகளைப் பயன்படுத்தி பொருள் கண்டறிதல் செய்ய முடியும், ஆனால் பொருள் கண்டறிதல் எப்படி செயல்படுகிறது என்பதைப் புரிந்து கொள்ளவும், உங்கள் சொந்த மாடல்களை பயிற்சி செய்யவும் முடியும் என்பதும் முக்கியம்.

---

**குறிப்பு**:  
இந்த ஆவணம் [Co-op Translator](https://github.com/Azure/co-op-translator) என்ற AI மொழிபெயர்ப்பு சேவையைப் பயன்படுத்தி மொழிபெயர்க்கப்பட்டுள்ளது. நாங்கள் துல்லியத்திற்காக முயற்சிக்கின்றோம், ஆனால் தானியங்கி மொழிபெயர்ப்புகளில் பிழைகள் அல்லது தவறான தகவல்கள் இருக்கக்கூடும் என்பதை தயவுசெய்து கவனத்தில் கொள்ளுங்கள். அதன் தாய்மொழியில் உள்ள மூல ஆவணம் அதிகாரப்பூர்வ ஆதாரமாக கருதப்பட வேண்டும். முக்கியமான தகவல்களுக்கு, தொழில்முறை மனித மொழிபெயர்ப்பு பரிந்துரைக்கப்படுகிறது. இந்த மொழிபெயர்ப்பைப் பயன்படுத்துவதால் ஏற்படும் எந்த தவறான புரிதல்கள் அல்லது தவறான விளக்கங்களுக்கு நாங்கள் பொறுப்பல்ல.