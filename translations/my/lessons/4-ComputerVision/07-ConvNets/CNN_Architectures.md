<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "2f7b97b375358cb51a1e098df306bf73",
  "translation_date": "2025-08-25T22:57:27+00:00",
  "source_file": "lessons/4-ComputerVision/07-ConvNets/CNN_Architectures.md",
  "language_code": "my"
}
-->
# လူသိများသော CNN အဆောက်အအုံများ

### VGG-16

VGG-16 သည် 2014 ခုနှစ်တွင် ImageNet top-5 classification တွင် 92.7% တိကျမှုရရှိခဲ့သော network တစ်ခုဖြစ်သည်။ ၎င်းတွင် အောက်ပါ layer အဆောက်အအုံပါရှိသည်-

![ImageNet Layers](../../../../../translated_images/vgg-16-arch1.d901a5583b3a51baeaab3e768567d921e5d54befa46e1e642616c5458c934028.my.jpg)

VGG သည် convolution-pooling layers များ၏ အစဉ်အတိုင်း pyramid architecture ကို လိုက်နာသည်ကို သင်တွေ့နိုင်ပါသည်။

![ImageNet Pyramid](../../../../../translated_images/vgg-16-arch.64ff2137f50dd49fdaa786e3f3a975b3f22615efd13efb19c5d22f12e01451a1.my.jpg)

> [Researchgate](https://www.researchgate.net/figure/Vgg16-model-structure-To-get-the-VGG-NIN-model-we-replace-the-2-nd-4-th-6-th-7-th_fig2_335194493) မှရရှိသောပုံ

### ResNet

ResNet သည် Microsoft Research မှ 2015 ခုနှစ်တွင် တင်ပြခဲ့သော model များ၏ မိသားစုဖြစ်သည်။ ResNet ၏ အဓိကအကြောင်းအရာမှာ **residual blocks** ကို အသုံးပြုခြင်းဖြစ်သည်-

<img src="images/resnet-block.png" width="300"/>

> [ဒီစာတမ်း](https://arxiv.org/pdf/1512.03385.pdf) မှရရှိသောပုံ

Identity pass-through ကို အသုံးပြုရသည့်အကြောင်းရင်းမှာ layer ၏ အရလွန်ကို **residual block ၏ output** နှင့် ယှဉ်၍ ခွဲခြားမှုကို ခန့်မှန်းရန်ဖြစ်သည် - ထို့ကြောင့် *residual* ဟုအမည်ပေးထားသည်။ ၎င်း block များကို လွယ်ကူစွာ training ပြုလုပ်နိုင်ပြီး၊ block များရာနှင့်ချီသော network များကို တည်ဆောက်နိုင်သည် (အများဆုံးအသုံးပြုသော variant များမှာ ResNet-52, ResNet-101 နှင့် ResNet-152 ဖြစ်သည်)။

ဤ network ကို dataset အပေါ်တွင် ၎င်း၏ ရှုပ်ထွေးမှုကို ချိန်ညှိနိုင်သောအနေဖြင့်လည်း တွေးဆနိုင်သည်။ အစပိုင်းတွင် network ကို training စတင်သောအခါ weight များသည် သေးငယ်ပြီး၊ signal အများစုသည် passthrough identity layers မှတဆင့်သွားသည်။ Training တိုးတက်လာပြီး weight များကြီးလာသည်နှင့် network parameters ၏ အရေးပါမှုများတိုးလာပြီး၊ training images များကို မှန်ကန်စွာခွဲခြားရန်လိုအပ်သော expressive power ကို network သင့်တော်စွာ ချိန်ညှိသည်။

### Google Inception

Google Inception architecture သည် ဤအကြောင်းအရာကို တစ်ဆင့်ပိုမိုတိုးတက်စေပြီး၊ network layer တစ်ခုစီကို အမျိုးမျိုးသော path များ၏ ပေါင်းစပ်အဖြစ် တည်ဆောက်သည်-

<img src="images/inception.png" width="400"/>

> [Researchgate](https://www.researchgate.net/figure/Inception-module-with-dimension-reductions-left-and-schema-for-Inception-ResNet-v1_fig2_355547454) မှရရှိသောပုံ

ဤနေရာတွင် 1x1 convolution များ၏ အရေးပါမှုကို အထူးပြောဆိုရန်လိုအပ်သည်၊ အစပိုင်းတွင် ၎င်းသည် အဓိပ္ပာယ်မရှိသလိုပင် ထင်ရနိုင်သည်။ 1x1 filter ဖြင့် image ကို run လုပ်ရန် ဘာကြောင့်လိုအပ်သလဲ? သို့သော် convolution filter များသည် depth channel များ (မူလတွင် - RGB အရောင်များ၊ နောက် layer များတွင် - filter များအတွက် channel များ) နှင့်အတူ လုပ်ဆောင်သည်ကို သတိပြုရန်လိုအပ်သည်။ 1x1 convolution သည် input channel များကို trainable weight များကို အသုံးပြု၍ ပေါင်းစပ်ရန်အသုံးပြုသည်။ ၎င်းကို channel dimension အပေါ်တွင် downsampling (pooling) အဖြစ်လည်း တွေးဆနိုင်သည်။

ဤအကြောင်းအရာနှင့်ပတ်သက်သော [blog post](https://medium.com/analytics-vidhya/talented-mr-1x1-comprehensive-look-at-1x1-convolution-in-deep-learning-f6b355825578) တစ်ခုနှင့် [မူရင်းစာတမ်း](https://arxiv.org/pdf/1312.4400.pdf) ကို ကြည့်ရှုနိုင်ပါသည်။

### MobileNet

MobileNet သည် အရွယ်အစားလျော့ချထားသော model များ၏ မိသားစုဖြစ်ပြီး၊ mobile device များအတွက် သင့်တော်သည်။ အရင်းအမြစ်များနည်းပါးပြီး accuracy အနည်းငယ်လျော့နည်းနိုင်သည်ကို လက်ခံနိုင်ပါက ၎င်းကို အသုံးပြုပါ။ ၎င်း၏ အဓိကအကြောင်းအရာမှာ **depthwise separable convolution** ဖြစ်ပြီး၊ spatial convolution များနှင့် depth channel များအပေါ် 1x1 convolution တို့၏ ပေါင်းစပ်ဖြင့် convolution filter များကို ကိုယ်စားပြုနိုင်သည်။ ၎င်းသည် parameter များ၏ အရေအတွက်ကို အလွန်လျော့ချပြီး၊ network ကို အရွယ်အစားသေးငယ်စေကာ၊ data နည်းပါးစွာဖြင့် training ပြုလုပ်ရန်လည်း လွယ်ကူစေသည်။

MobileNet နှင့်ပတ်သက်သော [blog post](https://medium.com/analytics-vidhya/image-classification-with-mobilenet-cc6fbb2cd470) တစ်ခုကို ကြည့်ရှုနိုင်ပါသည်။

## နိဂုံး

ဤ unit တွင် သင်သည် computer vision neural networks ၏ အဓိကအကြောင်းအရာ - convolutional networks ကို သင်ယူခဲ့ပါသည်။ အမှန်တကယ် image classification, object detection နှင့် image generation network များကို အားပေးသော architecture များသည် CNN များအပေါ် အခြေခံထားပြီး၊ အလွှာများပိုမိုများပြားခြင်းနှင့် training tricks အချို့ကို ထည့်သွင်းထားသည်။

## 🚀 စိန်ခေါ်မှု

ထည့်သွင်းထားသော notebooks တွင် တိကျမှုပိုမိုရရှိရန်အကြောင်းအရာများကို အောက်ဆုံးတွင် မှတ်ချက်ထားရှိထားသည်။ တိကျမှုပိုမိုရရှိနိုင်မည်ကို စမ်းသပ်ကြည့်ပါ။

## [Post-lecture quiz](https://ff-quizzes.netlify.app/en/ai/quiz/14)

## ပြန်လည်သုံးသပ်ခြင်းနှင့် ကိုယ်တိုင်လေ့လာခြင်း

CNN များကို Computer Vision အလုပ်များအတွက် အများဆုံးအသုံးပြုသော်လည်း၊ fixed-sized pattern များကို ထုတ်ယူရန်အတွက်လည်း အထူးကောင်းမွန်သည်။ ဥပမာအားဖြင့်၊ အသံများနှင့်ဆက်နွယ်နေပါက audio signal တွင် pattern အချို့ကို ရှာဖွေရန် CNN များကို အသုံးပြုလိုနိုင်သည် - ဤအခါ filter များသည် 1-dimensional ဖြစ်ပြီး (ဤ CNN ကို 1D-CNN ဟုခေါ်သည်)။ ထို့အပြင် 3D-CNN ကိုလည်း multi-dimensional space တွင် feature များကို ထုတ်ယူရန် အသုံးပြုနိုင်သည်၊ ဥပမာအားဖြင့် video တွင်ဖြစ်ပျက်နေသော အဖြစ်အပျက်အချို့ကို - CNN သည် feature များအချို့၏ အချိန်အတွင်းပြောင်းလဲမှု pattern များကို ဖမ်းဆီးနိုင်သည်။ CNN များဖြင့် ပြုလုပ်နိုင်သော အခြားအလုပ်များကို ပြန်လည်သုံးသပ်ပြီး ကိုယ်တိုင်လေ့လာပါ။

## [Assignment](lab/README.md)

ဤ lab တွင် သင်သည် ကြောင်နှင့် ခွေးမျိုးစုံကို ခွဲခြားရန်တာဝန်ရှိသည်။ ဤပုံများသည် MNIST dataset ထက် ပိုမိုရှုပ်ထွေးပြီး၊ အရွယ်အစားပိုမိုကြီးမားသည်။ class များ 10 ကျော်ပါရှိသည်။

**အကြောင်းကြားချက်**:  
ဤစာရွက်စာတမ်းကို AI ဘာသာပြန်ဝန်ဆောင်မှု [Co-op Translator](https://github.com/Azure/co-op-translator) ကို အသုံးပြု၍ ဘာသာပြန်ထားပါသည်။ ကျွန်ုပ်တို့သည် တိကျမှုအတွက် ကြိုးစားနေသော်လည်း၊ အလိုအလျောက် ဘာသာပြန်ခြင်းတွင် အမှားများ သို့မဟုတ် မမှန်ကန်မှုများ ပါရှိနိုင်သည်ကို သတိပြုပါ။ မူရင်းစာရွက်စာတမ်းကို ၎င်း၏ မူရင်းဘာသာစကားဖြင့် အာဏာတရားရှိသော အရင်းအမြစ်အဖြစ် သတ်မှတ်သင့်ပါသည်။ အရေးကြီးသော အချက်အလက်များအတွက် လူက ဘာသာပြန်ခြင်းကို အကြံပြုပါသည်။ ဤဘာသာပြန်ကို အသုံးပြုခြင်းမှ ဖြစ်ပေါ်လာသော အလွဲသုံးစားမှု သို့မဟုတ် အနားလည်မှားမှုများအတွက် ကျွန်ုပ်တို့သည် တာဝန်မယူပါ။