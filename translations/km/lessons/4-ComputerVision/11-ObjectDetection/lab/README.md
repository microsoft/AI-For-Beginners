# ការរកមុខក្បាលដោយប្រើទិន្នន័យ Hollywood Heads Dataset

ភារកិច្ចមេរៀនពី [AI for Beginners Curriculum](https://github.com/microsoft/ai-for-beginners) ។

## ភារកិច្ច

ការរាប់ចំនួនមនុស្សនៅលើចរន្តកាមេរ៉ាសុវត្ថិភាព វីដេអូ គឺជាភារកិច្ចសំខាន់មួយ ដែលអាចអនុញ្ញាតឲ្យយើងប៉ាន់ស្មានចំនួនមាតឹកានៅក្នុងហាងម៉ូដម៉ាឌែល ម៉ោងវិស្សមកាលនៅភោជនីយដ្ឋាន និងផ្សេងៗទៀត។ ដើម្បីដោះស្រាយភារកិច្ចនេះ យើងត្រូវបានបាច់ត្រូវអាចរកមុខក្បាលមនុស្សពីទិសភាពផ្សេងៗគ្នា។ ដើម្បីបណ្តុះម៉ូដែលរកមុខតំណាងរូបវត្ថុសម្រាប់រកមុខក្បាលមនុស្ស យើងអាចប្រើ [Hollywood Heads Dataset](https://www.di.ens.fr/willow/research/headdetection/) ។

## ទិន្នន័យ

[Hollywood Heads Dataset](https://www.di.ens.fr/willow/research/headdetection/release/HollywoodHeads.zip) មានមុខក្បាលមនុស្សចំនួន 369,846 ដែលបានពិពណ៌នាឡើងក្នុង 224,740 ស៊េរីរូបភាពខ្សែភាពយន្តពីភាពយន្ត Hollywood ។ វាត្រូវបានផ្ដល់ជាការរូបបែប [https://host.robots.ox.ac.uk/pascal/VOC/](../../../../../../lessons/4-ComputerVision/11-ObjectDetection/lab/PASCAL VOC) ដែលសម្រាប់រូបភាពនីមួយៗ មានឯកសារ XML អธิบายដែលមើលទៅដូចជា៖

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

ក្នុងទិន្នន័យនេះ មានតែមួយចំណាត់ថ្នាក់របស់វត្ថុគឺ `head` ហើយសម្រាប់មុខក្បាលនីមួយៗ អ្នកទទួលបានតំបន់ចំណងបណ្ដោយទំហំ (bounding box) ។ អ្នកអាចអាន XML ដោយប្រើបណ្ណាល័យ Python ឬប្រើ [បណ្ណាល័យនេះ](https://pypi.org/project/pascal-voc/) ដើម្បីដោះស្រាយទ្រង់ទ្រាយ PASCAL VOC ដោយផ្ទាល់ ។

## បណ្តុះម៉ូដែលរកមុខវត្ថុ

អ្នកអាចបណ្តុះម៉ូដែលរកមុខវត្ថុដោយប្រើមធ្យោបាយដូចខាងក្រោម៖

* ប្រើ [Azure Custom Vision](https://docs.microsoft.com/azure/cognitive-services/custom-vision-service/quickstarts/object-detection?tabs=visual-studio&WT.mc_id=academic-77998-cacaste) និង Python API របស់វា ដើម្បីបណ្តុះម៉ូដែលវិញ្ញាសានៅពពក។ Custom vision មិនអាចប្រើរូបភាពលើសរយៈរាប់រយសម្រាប់បណ្តុះម៉ូដែលទេ ដូច្នេះអ្នកប្រហែលជា​ត្រូវកំណត់ទិន្នន័យ។
* ប្រើឧទាហរណ៍ពី [មេរៀន Keras](https://keras.io/examples/vision/retinanet/) ដើម្បីបណ្តុះម៉ូដែល RetunaNet។
* ប្រើ [torchvision.models.detection.RetinaNet](https://pytorch.org/vision/stable/_modules/torchvision/models/detection/retinanet.html) ដែលបង្កើតដោយ torchvision ។

## លទ្ធផលសំខាន់

ការរកមុខវត្ថុគឺជាភារកិច្ចដែលត្រូវបានទាមទារញឹកញាប់នៅក្នុងឧស្សាហកម្ម។ ទោះបីជាមានសេវាកម្មខ្លះៗដែលអាចប្រើសម្រាប់បំពេញភារកិច្ចនេះ (ដូចជា [Azure Custom Vision](https://docs.microsoft.com/azure/cognitive-services/custom-vision-service/quickstarts/object-detection?tabs=visual-studio&WT.mc_id=academic-77998-cacaste)) ក៏ដោយ វាសំខាន់ណាស់ក្នុងការយល់ដឹងពីរបៀបដែលបច្ចេកវិទ្យារកមុខវត្ថុដំណើរការ ហើយអាចបណ្តុះម៉ូដែលរបស់អ្នកឯងបានផង។

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ការបដិសេធ**៖  
ឯកសារនេះត្រូវបានបកប្រែដោយប្រើសេវាកម្មបកប្រែ AI [Co-op Translator](https://github.com/Azure/co-op-translator)។ ខណៈពេលដែលយើងខិតខំរកភាពត្រឹមត្រូវ សូមយល់ថាការបកប្រែដោយស្វ័យប្រវត្តិអាចមានកំហុស ឬភាពមិនถูกត្រូវ។ ឯកសារដើមក្នុងភាសាទូទៅគួរត្រូវបានចាត់ទុកជាផលិតផលផ្លូវការ។ សម្រាប់ព័ត៌មានសំខាន់ៗ ការបកប្រែដោយអ្នកជំនាញផ្នែកមនុស្សគឺត្រូវបានណែនាំ។ យើងមិនទទួលខុសត្រូវចំពោះការយល់ច្រឡំ ឬការបកប្រែខុសៗណាមួយដែលកើតឡើងពីការប្រើប្រាស់ការបកប្រែនេះទេ។
<!-- CO-OP TRANSLATOR DISCLAIMER END -->