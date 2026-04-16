# ಹಾಲಿವುಡ್ ಹೆಡ್ಸ್ ಡೇಟಾಸೆಟ್ ಬಳಸಿ ತಲೆ ಗುರುತಿಸುವಿಕೆ

[AI for Beginners Curriculum](https://github.com/microsoft/ai-for-beginners) ನಿಂದ ಪ್ರಯೋಗಾಲಯ ಕಾರ್ಯ.

## ಕಾರ್ಯ

ವೀಡಿಯೋ ನಿಗಾ ಕ್ಯಾಮೆರಾ ಸ್ಟ್ರೀಮ್‌ನಲ್ಲಿ ಜನರ ಸಂಖ್ಯೆಯನ್ನು ಎಣಿಸುವುದು ಒಂದು ಪ್ರಮುಖ ಕಾರ್ಯವಾಗಿದೆ, ಇದು ಅಂಗಡಿಗಳಲ್ಲಿ ಭೇಟಿ ನೀಡುವವರ ಸಂಖ್ಯೆ, ರೆಸ್ಟೋರೆಂಟ್‌ನ ಬ್ಯುಸಿ ಸಮಯಗಳು ಇತ್ಯಾದಿಗಳನ್ನು ಅಂದಾಜಿಸಲು ಸಹಾಯ ಮಾಡುತ್ತದೆ. ಈ ಕಾರ್ಯವನ್ನು ಪರಿಹರಿಸಲು, ನಾವು ವಿವಿಧ ಕೋನಗಳಿಂದ ಮಾನವ ತಲೆಗಳನ್ನು ಗುರುತಿಸಲು ಸಾಧ್ಯವಾಗಬೇಕು. ಮಾನವ ತಲೆಗಳನ್ನು ಗುರುತಿಸಲು ವಸ್ತು ಗುರುತಿಸುವ ಮಾದರಿಯನ್ನು ತರಬೇತುಗೊಳಿಸಲು, ನಾವು [ಹಾಲಿವುಡ್ ಹೆಡ್ಸ್ ಡೇಟಾಸೆಟ್](https://www.di.ens.fr/willow/research/headdetection/) ಅನ್ನು ಬಳಸಬಹುದು.

## ಡೇಟಾಸೆಟ್

[ಹಾಲಿವುಡ್ ಹೆಡ್ಸ್ ಡೇಟಾಸೆಟ್](https://www.di.ens.fr/willow/research/headdetection/release/HollywoodHeads.zip) ನಲ್ಲಿ 224,740 ಹಾಲಿವುಡ್ ಚಲನಚಿತ್ರದ ಫ್ರೇಮ್‌ಗಳಲ್ಲಿ 369,846 ಮಾನವ ತಲೆಗಳನ್ನು ಅಂಕಿತಗೊಳಿಸಲಾಗಿದೆ. ಇದು [https://host.robots.ox.ac.uk/pascal/VOC/](../../../../../../lessons/4-ComputerVision/11-ObjectDetection/lab/PASCAL VOC) ಫಾರ್ಮ್ಯಾಟ್‌ನಲ್ಲಿ ಒದಗಿಸಲಾಗಿದೆ, ಇಲ್ಲಿ ಪ್ರತಿ ಚಿತ್ರಕ್ಕೆ ಒಂದು XML ವಿವರಣೆ ಫೈಲ್ ಕೂಡ ಇರುತ್ತದೆ, ಅದು ಹೀಗೆ ಕಾಣುತ್ತದೆ:

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

ಈ ಡೇಟಾಸೆಟ್‌ನಲ್ಲಿ, ಒಂದು ಮಾತ್ರ ವಸ್ತು ವರ್ಗ `head` ಇದೆ, ಮತ್ತು ಪ್ರತಿ ತಲೆಗೆ ಬೌಂಡಿಂಗ್ ಬಾಕ್ಸ್‌ನ ಸಂಯೋಜನೆಗಳನ್ನು ಪಡೆಯಬಹುದು. ನೀವು Python ಗ್ರಂಥಾಲಯಗಳನ್ನು ಬಳಸಿ XML ಅನ್ನು ಪಾರ್ಸ್ ಮಾಡಬಹುದು, ಅಥವಾ [ಈ ಗ್ರಂಥಾಲಯ](https://pypi.org/project/pascal-voc/) ಅನ್ನು ಬಳಸಿಕೊಂಡು ನೇರವಾಗಿ PASCAL VOC ಫಾರ್ಮ್ಯಾಟ್ ಅನ್ನು ನಿರ್ವಹಿಸಬಹುದು.

## ವಸ್ತು ಗುರುತಿಸುವಿಕೆ ತರಬೇತಿ

ನೀವು ಕೆಳಗಿನ ವಿಧಾನಗಳಲ್ಲಿ ಒಂದನ್ನು ಬಳಸಿಕೊಂಡು ವಸ್ತು ಗುರುತಿಸುವಿಕೆ ಮಾದರಿಯನ್ನು ತರಬೇತುಗೊಳಿಸಬಹುದು:

* [Azure Custom Vision](https://docs.microsoft.com/azure/cognitive-services/custom-vision-service/quickstarts/object-detection?tabs=visual-studio&WT.mc_id=academic-77998-cacaste) ಮತ್ತು ಅದರ Python API ಬಳಸಿ ಕ್ಲೌಡ್‌ನಲ್ಲಿ ಪ್ರೋಗ್ರಾಮ್ ಮೂಲಕ ಮಾದರಿಯನ್ನು ತರಬೇತುಗೊಳಿಸುವುದು. ಕಸ್ಟಮ್ ವೀಷನ್ ಮಾದರಿಯನ್ನು ತರಬೇತುಗೊಳಿಸಲು ಕೆಲವು ನೂರು ಚಿತ್ರಗಳಿಗಿಂತ ಹೆಚ್ಚು ಬಳಸಲು ಸಾಧ್ಯವಿಲ್ಲ, ಆದ್ದರಿಂದ ನೀವು ಡೇಟಾಸೆಟ್ ಅನ್ನು ಸೀಮಿತಗೊಳಿಸಬೇಕಾಗಬಹುದು.
* [Keras ಟ್ಯುಟೋರಿಯಲ್](https://keras.io/examples/vision/retinanet/) ನ ಉದಾಹರಣೆಯನ್ನು ಬಳಸಿ RetinaNet ಮಾದರಿಯನ್ನು ತರಬೇತುಗೊಳಿಸುವುದು.
* torchvision ನಲ್ಲಿ ಇರುವ [torchvision.models.detection.RetinaNet](https://pytorch.org/vision/stable/_modules/torchvision/models/detection/retinanet.html) ಬಿಲ್ಟ್-ಇನ್ ಮೋಡ್ಯೂಲ್ ಬಳಸಿ.

## ಸಾರಾಂಶ

ವಸ್ತು ಗುರುತಿಸುವಿಕೆ ಉದ್ಯಮದಲ್ಲಿ ಬಹುಮಾನವಾಗಿ ಅಗತ್ಯವಿರುವ ಕಾರ್ಯವಾಗಿದೆ. ವಸ್ತು ಗುರುತಿಸುವಿಕೆಗೆ ಬಳಸಬಹುದಾದ ಕೆಲವು ಸೇವೆಗಳು ಇದ್ದರೂ (ಉದಾಹರಣೆಗೆ [Azure Custom Vision](https://docs.microsoft.com/azure/cognitive-services/custom-vision-service/quickstarts/object-detection?tabs=visual-studio&WT.mc_id=academic-77998-cacaste)), ವಸ್ತು ಗುರುತಿಸುವಿಕೆ ಹೇಗೆ ಕಾರ್ಯನಿರ್ವಹಿಸುತ್ತದೆ ಎಂಬುದನ್ನು ಅರ್ಥಮಾಡಿಕೊಳ್ಳುವುದು ಮತ್ತು ನಿಮ್ಮದೇ ಮಾದರಿಗಳನ್ನು ತರಬೇತುಗೊಳಿಸುವ ಸಾಮರ್ಥ್ಯ ಹೊಂದಿರುವುದು ಮುಖ್ಯ.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ಅಸ್ವೀಕರಣ**:  
ಈ ದಸ್ತಾವೇಜು AI ಅನುವಾದ ಸೇವೆ [Co-op Translator](https://github.com/Azure/co-op-translator) ಬಳಸಿ ಅನುವಾದಿಸಲಾಗಿದೆ. ನಾವು ನಿಖರತೆಯಿಗಾಗಿ ಪ್ರಯತ್ನಿಸುತ್ತಿದ್ದರೂ, ಸ್ವಯಂಚಾಲಿತ ಅನುವಾದಗಳಲ್ಲಿ ದೋಷಗಳು ಅಥವಾ ಅಸತ್ಯತೆಗಳು ಇರಬಹುದು ಎಂದು ದಯವಿಟ್ಟು ಗಮನಿಸಿ. ಮೂಲ ಭಾಷೆಯಲ್ಲಿರುವ ಮೂಲ ದಸ್ತಾವೇಜನ್ನು ಅಧಿಕೃತ ಮೂಲವಾಗಿ ಪರಿಗಣಿಸಬೇಕು. ಮಹತ್ವದ ಮಾಹಿತಿಗಾಗಿ, ವೃತ್ತಿಪರ ಮಾನವ ಅನುವಾದವನ್ನು ಶಿಫಾರಸು ಮಾಡಲಾಗುತ್ತದೆ. ಈ ಅನುವಾದ ಬಳಕೆಯಿಂದ ಉಂಟಾಗುವ ಯಾವುದೇ ತಪ್ಪು ಅರ್ಥಮಾಡಿಕೊಳ್ಳುವಿಕೆ ಅಥವಾ ತಪ್ಪು ವಿವರಣೆಗಳಿಗೆ ನಾವು ಹೊಣೆಗಾರರಾಗುವುದಿಲ್ಲ.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->