# హాలీవుడ్ హెడ్ డేటాసెట్ ఉపయోగించి తల గుర్తింపు

[AI for Beginners Curriculum](https://github.com/microsoft/ai-for-beginners) నుండి ల్యాబ్ అసైన్‌మెంట్.

## పని

వీడియో సర్వేలెన్స్ కెమెరా స్ట్రీమ్‌లో ఉన్న వ్యక్తుల సంఖ్యను లెక్కించడం ఒక ముఖ్యమైన పని, ఇది షాపుల్లో సందర్శకుల సంఖ్య, రెస్టారెంట్‌లో బిజీ గంటలు మొదలైన వాటిని అంచనా వేయడానికి సహాయపడుతుంది. ఈ పనిని పరిష్కరించడానికి, మనం వివిధ కోణాల నుండి మానవ తలలను గుర్తించగలగాలి. మానవ తలలను గుర్తించడానికి ఆబ్జెక్ట్ డిటెక్షన్ మోడల్‌ను శిక్షణ ఇవ్వడానికి, మనం [హాలీవుడ్ హెడ్ డేటాసెట్](https://www.di.ens.fr/willow/research/headdetection/) ఉపయోగించవచ్చు.

## డేటాసెట్

[హాలీవుడ్ హెడ్ డేటాసెట్](https://www.di.ens.fr/willow/research/headdetection/release/HollywoodHeads.zip)లో 224,740 హాలీవుడ్ సినిమాల ఫ్రేమ్‌లలో 369,846 మానవ తలలు అనోటేట్ చేయబడ్డాయి. ఇది [https://host.robots.ox.ac.uk/pascal/VOC/](../../../../../../lessons/4-ComputerVision/11-ObjectDetection/lab/PASCAL VOC) ఫార్మాట్‌లో అందించబడింది, ఇందులో ప్రతి చిత్రానికి ఒక XML వివరణ ఫైల్ కూడా ఉంటుంది, ఇది ఇలా ఉంటుంది:

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

ఈ డేటాసెట్‌లో, ఒకే ఒక ఆబ్జెక్ట్ క్లాస్ `head` మాత్రమే ఉంటుంది, మరియు ప్రతి తల కోసం బౌండింగ్ బాక్స్ యొక్క కోఆర్డినేట్లు అందిస్తారు. మీరు XML ను Python లైబ్రరీలతో పార్స్ చేయవచ్చు, లేదా [ఈ లైబ్రరీ](https://pypi.org/project/pascal-voc/) ఉపయోగించి PASCAL VOC ఫార్మాట్‌ను నేరుగా హ్యాండిల్ చేయవచ్చు.

## ఆబ్జెక్ట్ డిటెక్షన్ శిక్షణ

మీరు క్రింది మార్గాల్లో ఒకదాన్ని ఉపయోగించి ఆబ్జెక్ట్ డిటెక్షన్ మోడల్‌ను శిక్షణ ఇవ్వవచ్చు:

* [Azure Custom Vision](https://docs.microsoft.com/azure/cognitive-services/custom-vision-service/quickstarts/object-detection?tabs=visual-studio&WT.mc_id=academic-77998-cacaste) మరియు దాని Python API ఉపయోగించి క్లౌడ్‌లో ప్రోగ్రామాటిక్‌గా మోడల్‌ను శిక్షణ ఇవ్వడం. కస్టమ్ విజన్ మోడల్ శిక్షణకు కొన్ని వందల చిత్రాలకంటే ఎక్కువ ఉపయోగించలేకపోవచ్చు, కాబట్టి డేటాసెట్ పరిమితం చేయాల్సి రావచ్చు.
* [Keras ట్యుటోరియల్](https://keras.io/examples/vision/retinanet/) నుండి ఉదాహరణ ఉపయోగించి RetinaNet మోడల్ శిక్షణ ఇవ్వడం.
* torchvisionలోని [torchvision.models.detection.RetinaNet](https://pytorch.org/vision/stable/_modules/torchvision/models/detection/retinanet.html) బిల్ట్-ఇన్ మాడ్యూల్ ఉపయోగించడం.

## ముఖ్యాంశం

ఆబ్జెక్ట్ డిటెక్షన్ అనేది పరిశ్రమలో తరచుగా అవసరమయ్యే పని. కొన్ని సర్వీసులు (ఉదాహరణకు [Azure Custom Vision](https://docs.microsoft.com/azure/cognitive-services/custom-vision-service/quickstarts/object-detection?tabs=visual-studio&WT.mc_id=academic-77998-cacaste)) ఆబ్జెక్ట్ డిటెక్షన్ చేయడానికి ఉపయోగించవచ్చు, కానీ ఆబ్జెక్ట్ డిటెక్షన్ ఎలా పనిచేస్తుందో అర్థం చేసుకోవడం మరియు మీ స్వంత మోడల్స్‌ను శిక్షణ ఇవ్వగలగడం చాలా ముఖ్యం.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**అస్పష్టత**:  
ఈ పత్రాన్ని AI అనువాద సేవ [Co-op Translator](https://github.com/Azure/co-op-translator) ఉపయోగించి అనువదించబడింది. మేము ఖచ్చితత్వానికి ప్రయత్నించినప్పటికీ, ఆటోమేటెడ్ అనువాదాల్లో పొరపాట్లు లేదా తప్పిదాలు ఉండవచ్చు. మూల పత్రం దాని స్వదేశీ భాషలో అధికారిక మూలంగా పరిగణించాలి. ముఖ్యమైన సమాచారానికి, ప్రొఫెషనల్ మానవ అనువాదం సిఫార్సు చేయబడుతుంది. ఈ అనువాదం వాడకంలో ఏర్పడిన ఏవైనా అపార్థాలు లేదా తప్పుదారితీసే అర్థాలు కోసం మేము బాధ్యత వహించము.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->