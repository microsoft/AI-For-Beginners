# ഹോളിവുഡ് ഹെഡ്സ് ഡാറ്റാസെറ്റ് ഉപയോഗിച്ച് തല കണ്ടെത്തൽ

[AI for Beginners Curriculum](https://github.com/microsoft/ai-for-beginners) ലെ ലാബ് അസൈൻമെന്റ്.

## ടാസ്‌ക്

വീഡിയോ നിരീക്ഷണ ക്യാമറ സ്ട്രീമിൽ ആളുകളുടെ എണ്ണം എണ്ണുക എന്നത് ഒരു പ്രധാന ടാസ്‌കാണ്, ഇത് കടകളിലെ സന്ദർശകരുടെ എണ്ണം, റെസ്റ്റോറന്റിലെ തിരക്കുള്ള സമയങ്ങൾ എന്നിവ കണക്കാക്കാൻ സഹായിക്കും. ഈ ടാസ്‌ക് പരിഹരിക്കാൻ, വ്യത്യസ്ത കോണുകളിൽ നിന്നുള്ള മനുഷ്യ തലകൾ കണ്ടെത്താൻ കഴിയണം. മനുഷ്യ തലകൾ കണ്ടെത്താൻ ഒബ്ജക്റ്റ് ഡിറ്റക്ഷൻ മോഡൽ പരിശീലിപ്പിക്കാൻ, [ഹോളിവുഡ് ഹെഡ്സ് ഡാറ്റാസെറ്റ്](https://www.di.ens.fr/willow/research/headdetection/) ഉപയോഗിക്കാം.

## ഡാറ്റാസെറ്റ്

[ഹോളിവുഡ് ഹെഡ്സ് ഡാറ്റാസെറ്റ്](https://www.di.ens.fr/willow/research/headdetection/release/HollywoodHeads.zip) 224,740 ഹോളിവുഡ് സിനിമാ ഫ്രെയിമുകളിൽ 369,846 മനുഷ്യ തലകൾ അനോട്ടേറ്റ് ചെയ്തിരിക്കുന്നു. ഇത് [https://host.robots.ox.ac.uk/pascal/VOC/](../../../../../../lessons/4-ComputerVision/11-ObjectDetection/lab/PASCAL VOC) ഫോർമാറ്റിൽ ലഭ്യമാണ്, ഓരോ ചിത്രത്തിനും അനുബന്ധമായ ഒരു XML വിവരണ ഫയൽ ഇതുപോലെയാണ്:

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

ഈ ഡാറ്റാസെറ്റിൽ, ഒറ്റ ക്ലാസ് മാത്രമേ ഉള്ളൂ, അതായത് `head`, ഓരോ തലത്തിനും ബൗണ്ടിംഗ് ബോക്സിന്റെ കോർഡിനേറ്റുകൾ ലഭ്യമാണ്. XML പാഴ്സുചെയ്യാൻ Python ലൈബ്രറികൾ ഉപയോഗിക്കാം, അല്ലെങ്കിൽ PASCAL VOC ഫോർമാറ്റ് നേരിട്ട് കൈകാര്യം ചെയ്യാൻ [ഈ ലൈബ്രറി](https://pypi.org/project/pascal-voc/) ഉപയോഗിക്കാം.

## ഒബ്ജക്റ്റ് ഡിറ്റക്ഷൻ പരിശീലനം

താഴെപ്പറയുന്ന വഴികളിൽ ഏതെങ്കിലും ഒരു വഴി ഉപയോഗിച്ച് ഒബ്ജക്റ്റ് ഡിറ്റക്ഷൻ മോഡൽ പരിശീലിപ്പിക്കാം:

* [Azure Custom Vision](https://docs.microsoft.com/azure/cognitive-services/custom-vision-service/quickstarts/object-detection?tabs=visual-studio&WT.mc_id=academic-77998-cacaste) ഉപയോഗിച്ച് Python API വഴി ക്ലൗഡിൽ പ്രോഗ്രാമാറ്റിക്കായി മോഡൽ പരിശീലിപ്പിക്കുക. Custom Vision മോഡൽ പരിശീലനത്തിന് കുറച്ച് നൂറു ചിത്രങ്ങൾക്കു മുകളിൽ ഉപയോഗിക്കാൻ കഴിയില്ല, അതിനാൽ ഡാറ്റാസെറ്റ് പരിധി കുറയ്ക്കേണ്ടിവരും.
* [Keras ട്യൂട്ടോറിയൽ](https://keras.io/examples/vision/retinanet/) ൽ നിന്നുള്ള ഉദാഹരണം ഉപയോഗിച്ച് RetinaNet മോഡൽ പരിശീലിപ്പിക്കുക.
* torchvision ൽ ഉള്ള [torchvision.models.detection.RetinaNet](https://pytorch.org/vision/stable/_modules/torchvision/models/detection/retinanet.html) ബിൽറ്റ്-ഇൻ മോഡ്യൂൾ ഉപയോഗിക്കുക.

## പ്രധാനപ്പെട്ട കാര്യങ്ങൾ

ഒബ്ജക്റ്റ് ഡിറ്റക്ഷൻ വ്യവസായത്തിൽ ആവശ്യമുള്ള ഒരു ടാസ്‌കാണ്. [Azure Custom Vision](https://docs.microsoft.com/azure/cognitive-services/custom-vision-service/quickstarts/object-detection?tabs=visual-studio&WT.mc_id=academic-77998-cacaste) പോലുള്ള സേവനങ്ങൾ ഉപയോഗിച്ച് ഒബ്ജക്റ്റ് ഡിറ്റക്ഷൻ നടത്താൻ കഴിയുന്നുണ്ടെങ്കിലും, ഒബ്ജക്റ്റ് ഡിറ്റക്ഷൻ എങ്ങനെ പ്രവർത്തിക്കുന്നു എന്ന് മനസ്സിലാക്കുകയും സ്വന്തം മോഡലുകൾ പരിശീലിപ്പിക്കാൻ കഴിയുകയും ചെയ്യുന്നത് വളരെ പ്രധാനമാണ്.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**അസൂയാ**:  
ഈ രേഖ AI വിവർത്തന സേവനം [Co-op Translator](https://github.com/Azure/co-op-translator) ഉപയോഗിച്ച് വിവർത്തനം ചെയ്തതാണ്. നാം കൃത്യതയ്ക്ക് ശ്രമിച്ചെങ്കിലും, സ്വയം പ്രവർത്തിക്കുന്ന വിവർത്തനങ്ങളിൽ പിശകുകൾ അല്ലെങ്കിൽ തെറ്റുകൾ ഉണ്ടാകാമെന്ന് ദയവായി ശ്രദ്ധിക്കുക. അതിന്റെ മാതൃഭാഷയിലുള്ള യഥാർത്ഥ രേഖ അധികാരപരമായ ഉറവിടമായി കണക്കാക്കണം. നിർണായക വിവരങ്ങൾക്ക്, പ്രൊഫഷണൽ മനുഷ്യ വിവർത്തനം ശുപാർശ ചെയ്യപ്പെടുന്നു. ഈ വിവർത്തനം ഉപയോഗിക്കുന്നതിൽ നിന്നുണ്ടാകുന്ന ഏതെങ്കിലും തെറ്റിദ്ധാരണകൾക്കോ തെറ്റായ വ്യാഖ്യാനങ്ങൾക്കോ ഞങ്ങൾ ഉത്തരവാദികളല്ല.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->