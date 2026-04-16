# Head Detection using Hollywood Heads Dataset

[AI for Beginners Curriculum](https://github.com/microsoft/ai-for-beginners) မှ Lab Assignment။

## Task

ဗီဒီယိုစောင့်ကြည့်မှုကင်မရာစီးရီးတွင် လူဦးရေကိုရေတွက်ခြင်းသည် ဆိုင်များတွင်လာရောက်သူဦးရေ၊ စားသောက်ဆိုင်များတွင် လူအများစုစုဝေးသောအချိန်များကို ခန့်မှန်းနိုင်ရန်အရေးကြီးသောအလုပ်တစ်ခုဖြစ်သည်။ ဤအလုပ်ကို ဖြေရှင်းရန်အတွက် လူ့ခေါင်းများကို အမျိုးမျိုးသောထောင့်မှရှာဖွေနိုင်ရမည်။ လူ့ခေါင်းများကို ရှာဖွေနိုင်ရန် Object Detection မော်ဒယ်ကို သင်ကြားရန်အတွက် [Hollywood Heads Dataset](https://www.di.ens.fr/willow/research/headdetection/) ကို အသုံးပြုနိုင်သည်။

## The Dataset

[Hollywood Heads Dataset](https://www.di.ens.fr/willow/research/headdetection/release/HollywoodHeads.zip) တွင် ဟောလီဝုဒ်ရုပ်ရှင်များမှ ရုပ်ရှင်ဖရိမ်များ 224,740 ခုတွင် လူ့ခေါင်းများ 369,846 ခုကို အမှတ်အသားပြုထားသည်။ ၎င်းကို [https://host.robots.ox.ac.uk/pascal/VOC/](../../../../../../lessons/4-ComputerVision/11-ObjectDetection/lab/PASCAL VOC) ဖော်မတ်ဖြင့် ပေးထားပြီး၊ ရုပ်ပုံတစ်ပုံစီအတွက် XML ဖိုင်တစ်ခုပါရှိသည်။ ၎င်းသည် အောက်ပါအတိုင်းဖြစ်သည်-

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

ဤဒေတာစဉ်တွင် `head` ဟူသော အတန်းတစ်ခုသာပါရှိပြီး၊ ခေါင်းတစ်ခုစီအတွက် bounding box ၏ ကိုဩဒိနိတ်များကို ရရှိနိုင်သည်။ XML ကို Python libraries အသုံးပြု၍ parse လုပ်နိုင်သကဲ့သို့၊ [ဤစာကြည့်တိုက်](https://pypi.org/project/pascal-voc/) ကို အသုံးပြု၍ PASCAL VOC ဖော်မတ်ကို တိုက်ရိုက်ကိုင်တွယ်နိုင်သည်။

## Training Object Detection 

Object Detection မော်ဒယ်ကို အောက်ပါနည်းလမ်းများမှတစ်ခုဖြင့် သင်ကြားနိုင်သည်-

* [Azure Custom Vision](https://docs.microsoft.com/azure/cognitive-services/custom-vision-service/quickstarts/object-detection?tabs=visual-studio&WT.mc_id=academic-77998-cacaste) နှင့် ၎င်း၏ Python API ကို အသုံးပြု၍ မော်ဒယ်ကို cloud တွင် programmatically သင်ကြားနိုင်သည်။ Custom Vision သည် မော်ဒယ်ကို သင်ကြားရန် ရုပ်ပုံအချို့သာ အသုံးပြုနိုင်မည်ဖြစ်သောကြောင့် ဒေတာစဉ်ကို ကန့်သတ်ရန်လိုအပ်နိုင်သည်။
* [Keras tutorial](https://keras.io/examples/vision/retinanet/) မှ ဥပမာကို အသုံးပြု၍ RetunaNet မော်ဒယ်ကို သင်ကြားနိုင်သည်။
* [torchvision.models.detection.RetinaNet](https://pytorch.org/vision/stable/_modules/torchvision/models/detection/retinanet.html) ၏ torchvision တွင်ပါရှိသော build-in module ကို အသုံးပြုနိုင်သည်။

## Takeaway

Object Detection သည် စက်မှုလုပ်ငန်းတွင် မကြာခဏလိုအပ်သောအလုပ်တစ်ခုဖြစ်သည်။ [Azure Custom Vision](https://docs.microsoft.com/azure/cognitive-services/custom-vision-service/quickstarts/object-detection?tabs=visual-studio&WT.mc_id=academic-77998-cacaste) ကဲ့သို့သော ဝန်ဆောင်မှုများကို အသုံးပြု၍ Object Detection ကို ပြုလုပ်နိုင်သော်လည်း၊ Object Detection ၏ လုပ်ဆောင်ပုံကို နားလည်ရန်နှင့် မိမိ၏ မော်ဒယ်များကို သင်ကြားနိုင်ရန် အရေးကြီးသည်။

**အကြောင်းကြားချက်**:  
ဤစာရွက်စာတမ်းကို AI ဘာသာပြန်ဝန်ဆောင်မှု [Co-op Translator](https://github.com/Azure/co-op-translator) ကို အသုံးပြု၍ ဘာသာပြန်ထားပါသည်။ ကျွန်ုပ်တို့သည် တိကျမှုအတွက် ကြိုးစားနေသော်လည်း၊ အလိုအလျောက် ဘာသာပြန်ခြင်းတွင် အမှားများ သို့မဟုတ် မတိကျမှုများ ပါရှိနိုင်သည်ကို သတိပြုပါ။ မူရင်းဘာသာစကားဖြင့် ရေးသားထားသော စာရွက်စာတမ်းကို အာဏာတရ အရင်းအမြစ်အဖြစ် ရှုယူသင့်ပါသည်။ အရေးကြီးသော အချက်အလက်များအတွက် လူ့ဘာသာပြန်ပညာရှင်များမှ ပရော်ဖက်ရှင်နယ် ဘာသာပြန်ခြင်းကို အကြံပြုပါသည်။ ဤဘာသာပြန်ကို အသုံးပြုခြင်းမှ ဖြစ်ပေါ်လာသော အလွဲအလွတ်များ သို့မဟုတ် အနားလွဲမှုများအတွက် ကျွန်ုပ်တို့သည် တာဝန်မယူပါ။