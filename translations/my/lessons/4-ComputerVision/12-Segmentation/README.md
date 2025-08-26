<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "d7f8a25ff13cfe9f4cd671cc23351fad",
  "translation_date": "2025-08-25T22:36:25+00:00",
  "source_file": "lessons/4-ComputerVision/12-Segmentation/README.md",
  "language_code": "my"
}
-->
# အပိုင်းခွဲခြားခြင်း

ယခင်က ကျွန်ုပ်တို့ Object Detection အကြောင်းကို လေ့လာခဲ့ပြီး၊ *bounding boxes* ကိုခန့်မှန်းခြင်းဖြင့် ပုံထဲရှိ objects တွေကို ရှာဖွေနိုင်ခဲ့ပါတယ်။ သို့သော် အချို့သောအလုပ်များအတွက် bounding boxes ပဲမဟုတ်ဘဲ၊ ပိုမိုတိကျသော object localization လည်းလိုအပ်ပါတယ်။ ဒီအလုပ်ကို **segmentation** လို့ခေါ်ပါတယ်။

## [Pre-lecture quiz](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/112)

Segmentation ကို **pixel classification** အနေနဲ့မြင်နိုင်ပြီး၊ ပုံရိပ်ရဲ့ **တစ်ခုချင်းစီ** pixel အတွက် class ကိုခန့်မှန်းရမယ် (*background* က classes တွေထဲကတစ်ခုဖြစ်ပါတယ်)။ Segmentation algorithm နှစ်မျိုးရှိပါတယ်-

* **Semantic segmentation** က pixel class ကိုသာပြောပြပြီး၊ အတူတူ class ရဲ့ object တွေကို ခွဲခြားမပြုလုပ်ပါဘူး။
* **Instance segmentation** ကတော့ class တွေကို အခြားသော instances တွေအဖြစ် ခွဲခြားပေးပါတယ်။

ဥပမာအားဖြင့် instance segmentation မှာ သိုးတွေဟာ object အနေနဲ့ ခွဲခြားထားပြီး၊ semantic segmentation မှာတော့ သိုးအားလုံးကို class တစ်ခုအနေနဲ့ပြသထားပါတယ်။

<img src="images/instance_vs_semantic.jpeg" width="50%">

> ပုံရင်း [ဒီ blog post](https://nirmalamurali.medium.com/image-classification-vs-semantic-segmentation-vs-instance-segmentation-625c33a08d50) မှာရရှိပါတယ်။

Segmentation အတွက် neural architectures မျိုးစုံရှိပေမယ့်၊ အားလုံးမှာ တူညီတဲ့ဖွဲ့စည်းမှုရှိပါတယ်။ တစ်နည်းအားဖြင့်၊ အရင်ကလေ့လာခဲ့တဲ့ autoencoder နဲ့ဆင်တူပါတယ်၊ ဒါပေမယ့် original image ကို deconstruct လုပ်တာမဟုတ်ဘဲ၊ **mask** ကို deconstruct လုပ်ဖို့ရည်ရွယ်ပါတယ်။ ထို့ကြောင့် segmentation network မှာ အောက်ပါအစိတ်အပိုင်းတွေပါဝင်ပါတယ်-

* **Encoder** က input image မှ feature တွေကို extract လုပ်ပါတယ်။
* **Decoder** က feature တွေကို **mask image** အဖြစ်ပြောင်းလဲပေးပြီး၊ အရွယ်အစားတူညီပြီး channel အရေအတွက်က classes အရေအတွက်နဲ့ကိုက်ညီပါတယ်။

<img src="images/segm.png" width="80%">

> ပုံရင်း [ဒီ publication](https://arxiv.org/pdf/2001.05566.pdf) မှာရရှိပါတယ်။

Segmentation အတွက် အသုံးပြုတဲ့ loss function ကို အထူးပြောရမယ်။ Classical autoencoders အသုံးပြုတဲ့အခါမှာ၊ ပုံရိပ်နှစ်ခုအကြားတူညီမှုကိုတိုင်းတာဖို့လိုအပ်ပြီး၊ mean square error (MSE) ကိုအသုံးပြုနိုင်ပါတယ်။ Segmentation မှာတော့ target mask image ရဲ့ pixel တစ်ခုချင်းစီက class number ကို (third dimension အတိုင်း one-hot-encoded) ကိုယ်စားပြုပါတယ်၊ classification-specific loss functions - cross-entropy loss ကို pixel အားလုံးအတွက်ပျမ်းမျှတွက်ချက်ရပါတယ်။ Mask က binary ဖြစ်ရင် - **binary cross-entropy loss** (BCE) ကိုအသုံးပြုပါတယ်။

> ✅ One-hot encoding က class label ကို class အရေအတွက်နဲ့တူညီတဲ့အရှည်ရှိတဲ့ vector အဖြစ် encode လုပ်တဲ့နည်းလမ်းတစ်ခုဖြစ်ပါတယ်။ [ဒီ article](https://datagy.io/sklearn-one-hot-encode/) ကိုကြည့်ပြီး ဒီနည်းလမ်းအကြောင်းပိုမိုလေ့လာပါ။

## ဆေးဘက်ပုံရိပ်များအတွက် Segmentation

ဒီသင်ခန်းစာမှာ၊ human nevi (moles) ကို medical images မှာသိရှိနိုင်ဖို့ network ကို training လုပ်တဲ့အခါ segmentation ကိုအလုပ်လုပ်ပုံကိုမြင်ရပါမယ်။ <a href="https://www.fc.up.pt/addi/ph2%20database.html">PH<sup>2</sup> Database</a> of dermoscopy images ကို image source အနေနဲ့အသုံးပြုပါမယ်။ ဒီ dataset မှာ typical nevus, atypical nevus, နဲ့ melanoma ဆိုတဲ့ class သုံးမျိုးပါဝင်တဲ့ပုံရိပ် 200 ခုပါဝင်ပါတယ်။ အပုံရိပ်အားလုံးမှာ **mask** ပါဝင်ပြီး၊ nevus ကို outline လုပ်ထားပါတယ်။

> ✅ ဒီနည်းလမ်းက ဒီလို medical imaging အတွက် အထူးသင့်လျော်ပါတယ်၊ ဒါပေမယ့် အခြားသောလက်တွေ့အသုံးချမှုတွေကို သင်စဉ်းစားနိုင်မလား?

<img alt="navi" src="images/navi.png"/>

> ပုံရင်း PH<sup>2</sup> Database မှာရရှိပါတယ်။

ကျွန်ုပ်တို့ model ကို training လုပ်ပြီး၊ background မှ nevus ကို segment လုပ်ပါမယ်။

## ✍️ လေ့ကျင့်ခန်းများ: Semantic Segmentation

အောက်ပါ notebooks တွေကိုဖွင့်ပြီး၊ semantic segmentation architectures မျိုးစုံအကြောင်းပိုမိုလေ့လာပါ၊ အလုပ်လုပ်ပုံကိုလေ့ကျင့်ပါ၊ နဲ့အလုပ်လုပ်ပုံကိုမြင်ပါ။

* [Semantic Segmentation Pytorch](../../../../../lessons/4-ComputerVision/12-Segmentation/SemanticSegmentationPytorch.ipynb)
* [Semantic Segmentation TensorFlow](../../../../../lessons/4-ComputerVision/12-Segmentation/SemanticSegmentationTF.ipynb)

## [Post-lecture quiz](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/212)

## နိဂုံး

Segmentation က image classification အတွက် အလွန်အစွမ်းထက်တဲ့နည်းလမ်းဖြစ်ပြီး၊ bounding boxes ကိုကျော်လွန်ပြီး pixel-level classification ကိုလုပ်ဆောင်ပါတယ်။ ဒါဟာ medical imaging အပါအဝင် အခြားသော application တွေမှာအသုံးပြုတဲ့နည်းလမ်းတစ်ခုဖြစ်ပါတယ်။

## 🚀 စိန်ခေါ်မှု

ကိုယ်ခန္ဓာ segmentation က လူတွေ့ပုံရိပ်တွေနဲ့လုပ်နိုင်တဲ့ common tasks တွေထဲကတစ်ခုပါ။ အခြားသောအရေးကြီးတဲ့ tasks တွေမှာ **skeleton detection** နဲ့ **pose detection** ပါဝင်ပါတယ်။ [OpenPose](https://github.com/CMU-Perceptual-Computing-Lab/openpose) library ကိုစမ်းကြည့်ပြီး pose detection ကိုဘယ်လိုအသုံးပြုနိုင်လဲမြင်ပါ။

## Review & Self Study

ဒီ [wikipedia article](https://wikipedia.org/wiki/Image_segmentation) က ဒီနည်းလမ်းရဲ့ application မျိုးစုံအကြောင်းကို အကျဉ်းချုပ်ပေးထားပါတယ်။ Instance segmentation နဲ့ Panoptic segmentation ရဲ့ subdomains အကြောင်းကို သင်ကိုယ်တိုင်ပိုမိုလေ့လာပါ။

## [Assignment](lab/README.md)

ဒီ lab မှာ **human body segmentation** ကို [Segmentation Full Body MADS Dataset](https://www.kaggle.com/datasets/tapakah68/segmentation-full-body-mads-dataset) ကို Kaggle မှာရရှိနိုင်တဲ့ dataset ကိုအသုံးပြုပြီးစမ်းကြည့်ပါ။

**အကြောင်းကြားချက်**:  
ဤစာရွက်စာတမ်းကို AI ဘာသာပြန်ဝန်ဆောင်မှု [Co-op Translator](https://github.com/Azure/co-op-translator) ကို အသုံးပြု၍ ဘာသာပြန်ထားပါသည်။ ကျွန်ုပ်တို့သည် တိကျမှုအတွက် ကြိုးစားနေသော်လည်း၊ အလိုအလျောက် ဘာသာပြန်မှုများတွင် အမှားများ သို့မဟုတ် မမှန်ကန်မှုများ ပါဝင်နိုင်သည်ကို သတိပြုပါ။ မူရင်းစာရွက်စာတမ်းကို ၎င်း၏ မူရင်းဘာသာစကားဖြင့် အာဏာတရားရှိသော အရင်းအမြစ်အဖြစ် သတ်မှတ်သင့်ပါသည်။ အရေးကြီးသော အချက်အလက်များအတွက် လူ့ဘာသာပြန်ပညာရှင်များမှ ပရော်ဖက်ရှင်နယ် ဘာသာပြန်မှုကို အကြံပြုပါသည်။ ဤဘာသာပြန်မှုကို အသုံးပြုခြင်းမှ ဖြစ်ပေါ်လာသော အလွဲအလွတ်များ သို့မဟုတ် အနားလွဲမှုများအတွက် ကျွန်ုပ်တို့သည် တာဝန်မယူပါ။