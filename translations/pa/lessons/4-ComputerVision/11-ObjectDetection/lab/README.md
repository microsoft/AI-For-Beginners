# ਹਾਲੀਵੁੱਡ ਹੈਡਸ ਡੇਟਾਸੈਟ ਦੀ ਵਰਤੋਂ ਨਾਲ ਸਿਰ ਦੀ ਪਛਾਣ

[AI for Beginners Curriculum](https://github.com/microsoft/ai-for-beginners) ਤੋਂ ਲੈਬ ਅਸਾਈਨਮੈਂਟ।

## ਕੰਮ

ਵੀਡੀਓ ਨਿਗਰਾਨੀ ਕੈਮਰੇ ਦੇ ਸਟ੍ਰੀਮ 'ਤੇ ਲੋਕਾਂ ਦੀ ਗਿਣਤੀ ਕਰਨਾ ਇੱਕ ਮਹੱਤਵਪੂਰਨ ਕੰਮ ਹੈ, ਜੋ ਸਾਨੂੰ ਦੁਕਾਨਾਂ ਵਿੱਚ ਆਉਣ ਵਾਲੇ ਵਿਜ਼ਟਰਾਂ ਦੀ ਗਿਣਤੀ ਦਾ ਅੰਦਾਜ਼ਾ ਲਗਾਉਣ, ਰੈਸਟੋਰੈਂਟ ਦੇ ਵਿਆਸਤ ਘੰਟਿਆਂ ਦੀ ਪਛਾਣ ਕਰਨ ਆਦਿ ਵਿੱਚ ਮਦਦ ਕਰਦਾ ਹੈ। ਇਸ ਕੰਮ ਨੂੰ ਹੱਲ ਕਰਨ ਲਈ, ਸਾਨੂੰ ਵੱਖ-ਵੱਖ ਕੋਣਾਂ ਤੋਂ ਮਨੁੱਖੀ ਸਿਰਾਂ ਦੀ ਪਛਾਣ ਕਰਨ ਦੇ ਯੋਗ ਹੋਣਾ ਚਾਹੀਦਾ ਹੈ। ਮਨੁੱਖੀ ਸਿਰਾਂ ਦੀ ਪਛਾਣ ਕਰਨ ਲਈ ਆਬਜੈਕਟ ਡਿਟੈਕਸ਼ਨ ਮਾਡਲ ਨੂੰ ਟ੍ਰੇਨ ਕਰਨ ਲਈ, ਅਸੀਂ [ਹਾਲੀਵੁੱਡ ਹੈਡਸ ਡੇਟਾਸੈਟ](https://www.di.ens.fr/willow/research/headdetection/) ਦੀ ਵਰਤੋਂ ਕਰ ਸਕਦੇ ਹਾਂ।

## ਡੇਟਾਸੈਟ

[ਹਾਲੀਵੁੱਡ ਹੈਡਸ ਡੇਟਾਸੈਟ](https://www.di.ens.fr/willow/research/headdetection/release/HollywoodHeads.zip) ਵਿੱਚ 369,846 ਮਨੁੱਖੀ ਸਿਰ ਸ਼ਾਮਲ ਹਨ, ਜੋ ਕਿ ਹਾਲੀਵੁੱਡ ਫਿਲਮਾਂ ਦੇ 224,740 ਫਰੇਮਾਂ ਵਿੱਚ ਐਨੋਟੇਟ ਕੀਤੇ ਗਏ ਹਨ। ਇਹ [https://host.robots.ox.ac.uk/pascal/VOC/](../../../../../../lessons/4-ComputerVision/11-ObjectDetection/lab/PASCAL VOC) ਫਾਰਮੈਟ ਵਿੱਚ ਪ੍ਰਦਾਨ ਕੀਤਾ ਗਿਆ ਹੈ, ਜਿੱਥੇ ਹਰ ਚਿੱਤਰ ਲਈ ਇੱਕ XML ਵੇਰਵਾ ਫਾਈਲ ਵੀ ਹੁੰਦੀ ਹੈ, ਜੋ ਇਸ ਤਰ੍ਹਾਂ ਲੱਗਦੀ ਹੈ:

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

ਇਸ ਡੇਟਾਸੈਟ ਵਿੱਚ ਸਿਰਫ ਇੱਕ ਆਬਜੈਕਟ ਕਲਾਸ ਹੈ `head`, ਅਤੇ ਹਰ ਸਿਰ ਲਈ, ਤੁਹਾਨੂੰ ਬਾਊਂਡਿੰਗ ਬਾਕਸ ਦੇ ਕੋਆਰਡੀਨੇਟਸ ਮਿਲਦੇ ਹਨ। ਤੁਸੀਂ XML ਨੂੰ ਪਾਈਥਨ ਲਾਇਬ੍ਰੇਰੀਜ਼ ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਪਾਰਸ ਕਰ ਸਕਦੇ ਹੋ, ਜਾਂ [ਇਸ ਲਾਇਬ੍ਰੇਰੀ](https://pypi.org/project/pascal-voc/) ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਸਿੱਧੇ PASCAL VOC ਫਾਰਮੈਟ ਨਾਲ ਕੰਮ ਕਰ ਸਕਦੇ ਹੋ।

## ਆਬਜੈਕਟ ਡਿਟੈਕਸ਼ਨ ਟ੍ਰੇਨਿੰਗ

ਤੁਸੀਂ ਆਬਜੈਕਟ ਡਿਟੈਕਸ਼ਨ ਮਾਡਲ ਨੂੰ ਹੇਠਾਂ ਦਿੱਤੇ ਤਰੀਕਿਆਂ ਵਿੱਚੋਂ ਕਿਸੇ ਇੱਕ ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਟ੍ਰੇਨ ਕਰ ਸਕਦੇ ਹੋ:

* [Azure Custom Vision](https://docs.microsoft.com/azure/cognitive-services/custom-vision-service/quickstarts/object-detection?tabs=visual-studio&WT.mc_id=academic-77998-cacaste) ਅਤੇ ਇਸਦੀ Python API ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਕਲਾਉਡ ਵਿੱਚ ਮਾਡਲ ਨੂੰ ਪ੍ਰੋਗਰਾਮਮੈਟਿਕ ਤਰੀਕੇ ਨਾਲ ਟ੍ਰੇਨ ਕਰੋ। ਕਸਟਮ ਵਿਜ਼ਨ ਮਾਡਲ ਨੂੰ ਟ੍ਰੇਨ ਕਰਨ ਲਈ ਕੁਝ ਸੌ ਚਿੱਤਰਾਂ ਤੋਂ ਵੱਧ ਦੀ ਵਰਤੋਂ ਨਹੀਂ ਕਰ ਸਕੇਗਾ, ਇਸ ਲਈ ਤੁਹਾਨੂੰ ਡੇਟਾਸੈਟ ਨੂੰ ਸੀਮਿਤ ਕਰਨਾ ਪਵੇਗਾ।
* [Keras ਟਿਊਟੋਰਿਯਲ](https://keras.io/examples/vision/retinanet/) ਦੇ ਉਦਾਹਰਨ ਦੀ ਵਰਤੋਂ ਕਰਕੇ RetunaNet ਮਾਡਲ ਨੂੰ ਟ੍ਰੇਨ ਕਰੋ।
* [torchvision.models.detection.RetinaNet](https://pytorch.org/vision/stable/_modules/torchvision/models/detection/retinanet.html) ਵਿੱਚ ਮੌਜੂਦ ਬਿਲਟ-ਇਨ ਮੋਡੀਊਲ ਦੀ ਵਰਤੋਂ ਕਰੋ।

## ਸਿੱਖਣ ਵਾਲੀਆਂ ਗੱਲਾਂ

ਆਬਜੈਕਟ ਡਿਟੈਕਸ਼ਨ ਇੱਕ ਅਜਿਹਾ ਕੰਮ ਹੈ ਜੋ ਉਦਯੋਗ ਵਿੱਚ ਅਕਸਰ ਲੋੜੀਂਦਾ ਹੁੰਦਾ ਹੈ। ਜਦੋਂ ਕਿ ਕੁਝ ਸੇਵਾਵਾਂ ਹਨ ਜੋ ਆਬਜੈਕਟ ਡਿਟੈਕਸ਼ਨ ਕਰਨ ਲਈ ਵਰਤੀਆਂ ਜਾ ਸਕਦੀਆਂ ਹਨ (ਜਿਵੇਂ ਕਿ [Azure Custom Vision](https://docs.microsoft.com/azure/cognitive-services/custom-vision-service/quickstarts/object-detection?tabs=visual-studio&WT.mc_id=academic-77998-cacaste)), ਇਹ ਸਮਝਣਾ ਮਹੱਤਵਪੂਰਨ ਹੈ ਕਿ ਆਬਜੈਕਟ ਡਿਟੈਕਸ਼ਨ ਕਿਵੇਂ ਕੰਮ ਕਰਦਾ ਹੈ ਅਤੇ ਆਪਣੇ ਮਾਡਲ ਨੂੰ ਟ੍ਰੇਨ ਕਰਨ ਦੇ ਯੋਗ ਹੋਣਾ।

**ਅਸਵੀਕਰਤੀ**:  
ਇਹ ਦਸਤਾਵੇਜ਼ AI ਅਨੁਵਾਦ ਸੇਵਾ [Co-op Translator](https://github.com/Azure/co-op-translator) ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਅਨੁਵਾਦ ਕੀਤਾ ਗਿਆ ਹੈ। ਜਦੋਂ ਕਿ ਅਸੀਂ ਸਹੀ ਹੋਣ ਦਾ ਯਤਨ ਕਰਦੇ ਹਾਂ, ਕਿਰਪਾ ਕਰਕੇ ਧਿਆਨ ਦਿਓ ਕਿ ਸਵੈਚਾਲਿਤ ਅਨੁਵਾਦਾਂ ਵਿੱਚ ਗਲਤੀਆਂ ਜਾਂ ਅਸੁਣਤੀਆਂ ਹੋ ਸਕਦੀਆਂ ਹਨ। ਇਸ ਦੀ ਮੂਲ ਭਾਸ਼ਾ ਵਿੱਚ ਮੌਜੂਦ ਮੂਲ ਦਸਤਾਵੇਜ਼ ਨੂੰ ਪ੍ਰਮਾਣਿਕ ਸਰੋਤ ਮੰਨਿਆ ਜਾਣਾ ਚਾਹੀਦਾ ਹੈ। ਮਹੱਤਵਪੂਰਨ ਜਾਣਕਾਰੀ ਲਈ, ਪੇਸ਼ੇਵਰ ਮਨੁੱਖੀ ਅਨੁਵਾਦ ਦੀ ਸਿਫਾਰਸ਼ ਕੀਤੀ ਜਾਂਦੀ ਹੈ। ਇਸ ਅਨੁਵਾਦ ਦੇ ਪ੍ਰਯੋਗ ਤੋਂ ਪੈਦਾ ਹੋਣ ਵਾਲੇ ਕਿਸੇ ਵੀ ਗਲਤਫਹਮੀਆਂ ਜਾਂ ਗਲਤ ਵਿਆਖਿਆਵਾਂ ਲਈ ਅਸੀਂ ਜ਼ਿੰਮੇਵਾਰ ਨਹੀਂ ਹਾਂ।