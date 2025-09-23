<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f07c85bbf05a1f67505da98f4ecc124c",
  "translation_date": "2025-08-25T22:42:31+00:00",
  "source_file": "lessons/4-ComputerVision/10-GANs/README.md",
  "language_code": "my"
}
-->
# Generative Adversarial Networks

မကြာသေးမီကပိုင်းတွင် **generative models** အကြောင်းကိုလေ့လာခဲ့ပါသည်။ Generative models ဆိုသည်မှာ သင်ကြားမှု dataset ထဲရှိပုံများနှင့်တူသော ပုံအသစ်များကို ဖန်တီးနိုင်သော မော်ဒယ်များဖြစ်သည်။ VAE သည် generative model တစ်ခုအနေဖြင့် ကောင်းမွန်သော ဥပမာတစ်ခုဖြစ်သည်။

## [Pre-lecture quiz](https://ff-quizzes.netlify.app/en/ai/quiz/19)

သို့သော် VAE ကို အသုံးပြု၍ အဓိပ္ပါယ်ရှိသော ပုံများကို သင့်တင့်သော resolution ဖြင့် ဖန်တီးရန်ကြိုးစားပါက သင်ကြားမှုသည် ကောင်းစွာမရောက်ရှိနိုင်ပါ။ ဒီလိုအခြေအနေတွင် generative models အတွက် အထူးသီးသန့်ဖန်တီးထားသော architecture တစ်ခုဖြစ်သည့် **Generative Adversarial Networks** (GANs) အကြောင်းကို လေ့လာရမည်ဖြစ်သည်။

GAN ၏ အဓိကအကြောင်းအရာမှာ neural networks နှစ်ခုကို အချင်းချင်းယှဉ်ပြိုင်စွမ်းရည်မြှင့်တင်ရန် သင်ကြားခြင်းဖြစ်သည်။

<img src="images/gan_architecture.png" width="70%"/>

> ပုံကို [Dmitry Soshnikov](http://soshnikov.com) မှ ဖန်တီးထားသည်။

> ✅ အသုံးအနှုန်းအနည်းငယ်:
> * **Generator** ဆိုသည်မှာ random vector တစ်ခုကိုယူပြီး အဖြေအနေဖြင့် ပုံတစ်ခုကို ဖန်တီးပေးသော network ဖြစ်သည်။
> * **Discriminator** ဆိုသည်မှာ ပုံတစ်ခုကိုယူပြီး အဲဒီပုံသည် training dataset ထဲမှ အမှန်ပုံဖြစ်သည်လား၊ generator မှ ဖန်တီးထားသော ပုံဖြစ်သည်လားဆိုတာကို ခွဲခြားပေးရမည်။ အဓိကအားဖြင့် image classifier တစ်ခုဖြစ်သည်။

### Discriminator

Discriminator ၏ architecture သည် အခြား image classification network များနှင့် မတူကွဲပြားမှုမရှိပါ။ အလွယ်ဆုံးအနေဖြင့် fully-connected classifier ဖြစ်နိုင်သလို၊ [convolutional network](../07-ConvNets/README.md) ဖြစ်နိုင်ပါသည်။

> ✅ Convolutional networks အပေါ်အခြေခံထားသော GAN ကို [DCGAN](https://arxiv.org/pdf/1511.06434.pdf) ဟုခေါ်သည်။

CNN discriminator တွင် ပါဝင်သော layer များမှာ - convolution+pooling အတန်းများ (spatial size လျော့နည်းလာသော) နှင့် "feature vector" ရရှိရန် fully-connected layer တစ်ခု (သို့မဟုတ်) အများအပြားပါဝင်သည်။ နောက်ဆုံး binary classifier တစ်ခုဖြစ်သည်။

> ✅ "Pooling" ဆိုသည်မှာ ပုံ၏အရွယ်အစားကို လျော့နည်းစေသောနည်းလမ်းတစ်ခုဖြစ်သည်။ "Pooling layers သည် data ၏ dimension များကို လျော့နည်းစေပြီး layer တစ်ခုတွင် neuron cluster များ၏ output များကို နောက်တစ်ခု layer တွင် neuron တစ်ခုအဖြစ်ပေါင်းစည်းပေးသည်။" - [source](https://wikipedia.org/wiki/Convolutional_neural_network#Pooling_layers)

### Generator

Generator သည် အနည်းငယ်ပိုရှုပ်ထွေးသည်။ Discriminator ကို ပြန်လှည့်ထားသည့်အနေဖြင့် တွေးနိုင်သည်။ latent vector (feature vector ၏နေရာတွင်) မှစတင်ပြီး၊ fully-connected layer တစ်ခုဖြင့် လိုအပ်သော size/shape သို့ ပြောင်းလဲပေးပြီး၊ deconvolutions+upscaling ဖြင့် ဆက်လက်လုပ်ဆောင်သည်။ ၎င်းသည် [autoencoder](../09-Autoencoders/README.md) ၏ *decoder* အပိုင်းနှင့် ဆင်တူသည်။

> ✅ Convolution layer ကို linear filter အနေဖြင့် ပုံကို traverse လုပ်သော logic ဖြင့် implement လုပ်ထားသည့်အတွက် deconvolution သည် convolution နှင့် ဆင်တူပြီး၊ အတူတူသော layer logic ကို အသုံးပြု၍ implement လုပ်နိုင်သည်။

<img src="images/gan_arch_detail.png" width="70%"/>

> ပုံကို [Dmitry Soshnikov](http://soshnikov.com) မှ ဖန်တီးထားသည်။

### GAN သင်ကြားခြင်း

GANs ကို **adversarial** ဟုခေါ်သည်မှာ generator နှင့် discriminator အချင်းချင်း ယှဉ်ပြိုင်မှုရှိနေသောကြောင့်ဖြစ်သည်။ ယှဉ်ပြိုင်မှုအတွင်း generator နှင့် discriminator နှစ်ခုစလုံးကောင်းမွန်လာပြီး၊ network သည် ပိုမိုကောင်းမွန်သော ပုံများကို ဖန်တီးနိုင်ရန် သင်ကြားသည်။

သင်ကြားမှုသည် အဆင့်နှစ်ခုဖြင့် ဆောင်ရွက်သည် -

* **Discriminator ကို သင်ကြားခြင်း**။ ဒီအလုပ်ကို လွယ်ကူစွာလုပ်ဆောင်နိုင်သည် - generator မှ ဖန်တီးထားသော ပုံများ batch တစ်ခုကိုယူပြီး၊ ၎င်းကို 0 (fake image) ဟု label လုပ်သည်။ input dataset မှ ပုံများ batch တစ်ခုကိုယူပြီး (label 1, real image) ဖြင့် သတ်မှတ်သည်။ *discriminator loss* တစ်ခုရရှိပြီး၊ backprop လုပ်ဆောင်သည်။
* **Generator ကို သင်ကြားခြင်း**။ ဒီအလုပ်သည် အနည်းငယ်ပိုရှုပ်ထွေးသည်၊ generator ၏ အနိမ့်ဆုံး output ကို တိုင်းတာရန် မသိသောကြောင့်ဖြစ်သည်။ GAN network တစ်ခုလုံးကို generator နှင့် discriminator ပေါင်းစပ်ထားသောအနေဖြင့်ယူပြီး၊ random vectors များဖြင့် input ပေးကာ၊ output ကို 1 (real images) ဖြစ်ရန် မျှော်မှန်းသည်။ Discriminator ၏ parameters များကို freeze လုပ်ပြီး (ဒီအဆင့်တွင် သင်ကြားလိုမထားပါ)၊ backprop လုပ်ဆောင်သည်။

ဒီလုပ်ငန်းစဉ်အတွင်း generator နှင့် discriminator loss များသည် အနိမ့်ဆုံးမရောက်ရှိနိုင်ပါ။ အကောင်းဆုံးအခြေအနေတွင် loss များသည် တုန်လှုပ်မှုရှိပြီး၊ network နှစ်ခုစလုံးကောင်းမွန်လာသည်ကို ဖော်ပြသည်။

## ✍️ Exercises: GANs

* [GAN Notebook in TensorFlow/Keras](../../../../../lessons/4-ComputerVision/10-GANs/GANTF.ipynb)
* [GAN Notebook in PyTorch](../../../../../lessons/4-ComputerVision/10-GANs/GANPyTorch.ipynb)

### GAN သင်ကြားမှု၏ ပြဿနာများ

GANs သည် သင်ကြားရန် အထူးခက်ခဲသော network များအဖြစ်လူသိများသည်။ အောက်ပါပြဿနာများရှိနိုင်သည် -

* **Mode Collapse**။ Generator သည် discriminator ကို လှည့်စားနိုင်သော ပုံတစ်ခုကိုသာ ဖန်တီးပြီး၊ ပုံအမျိုးမျိုးကို ဖန်တီးရန် မလေ့လာနိုင်သောအခြေအနေကို mode collapse ဟုခေါ်သည်။
* **Hyperparameters sensitivity**။ GAN သည် မတိုင်မီ convergence မရောက်ရှိနိုင်ပြီး၊ sudden learning rate လျော့နည်းမှုကြောင့် convergence ရောက်ရှိနိုင်သည်။
* **Generator နှင့် discriminator အချင်းချင်း balance ထိန်းသိမ်းမှု**။ Discriminator loss သည် အလွန်မြန်စွာ 0 သို့ရောက်ရှိနိုင်ပြီး၊ generator သည် ဆက်လက်သင်ကြားရန် မရနိုင်သောအခြေအနေဖြစ်နိုင်သည်။ ဒီပြဿနာကို generator နှင့် discriminator အတွက် learning rate မတူကွဲပြားစွာ သတ်မှတ်ခြင်း၊ သို့မဟုတ် discriminator loss အလွန်နိမ့်နေပါက training ကို ချန်ထားခြင်းဖြင့် ဖြေရှင်းနိုင်သည်။
* **High resolution training**။ Autoencoders တွင်ရှိသောပြဿနာနှင့်တူသောပြဿနာဖြစ်ပြီး၊ convolutional network layer များအများအပြားကို ပြန်လည်ဖန်တီးရန်ကြိုးစားမှုကြောင့် artifacts ဖြစ်ပေါ်သည်။ ဒီပြဿနာကို **progressive growing** ဖြင့် ဖြေရှင်းနိုင်သည် - layer အနည်းငယ်ကို low-res images တွင် training လုပ်ပြီး၊ layer များကို "unblock" သို့မဟုတ် ထပ်မံထည့်သွင်းသည်။ အခြားနည်းလမ်းမှာ layer များအကြား extra connections ထည့်သွင်းပြီး၊ resolution အမျိုးမျိုးကို တစ်ချိန်တည်း training လုပ်ခြင်းဖြစ်သည်။ [Multi-Scale Gradient GANs paper](https://arxiv.org/abs/1903.06048) ကို အသေးစိတ်ဖတ်ရှုပါ။

## Style Transfer

GANs သည် အနုပညာပုံများ ဖန်တီးရန် ကောင်းမွန်သောနည်းလမ်းဖြစ်သည်။ အခြားစိတ်ဝင်စားဖွယ်နည်းလမ်းတစ်ခုမှာ **style transfer** ဖြစ်ပြီး၊ **content image** တစ်ခုကိုယူကာ၊ **style image** ၏ filter များကို အသုံးပြု၍ ပုံကို ပြန်လည်ရေးဆွဲပေးသည်။

၎င်း၏လုပ်ဆောင်ပုံမှာ -

* Random noise image (content image ကိုလည်းစတင်အသုံးပြုနိုင်သော်လည်း၊ random noise image မှစတင်ခြင်းသည် နားလည်ရန်ပိုလွယ်ကူသည်) မှစတင်သည်။
* Content image နှင့် style image နှစ်ခုလုံးနှင့် နီးစပ်သော image တစ်ခုကို ဖန်တီးရန် ရည်ရွယ်သည်။ Loss function နှစ်ခုဖြင့် သတ်မှတ်သည် -
   - **Content loss** ကို current image နှင့် content image မှ CNN ၏ layer များမှ extract လုပ်ထားသော features အပေါ်အခြေခံ၍ တွက်ချက်သည်။
   - **Style loss** ကို current image နှင့် style image အကြား Gram matrices ကို အသုံးပြု၍ တွက်ချက်သည် (အသေးစိတ်ကို [example notebook](../../../../../lessons/4-ComputerVision/10-GANs/StyleTransfer.ipynb) တွင်ကြည့်ပါ)။
* ပုံကို ပိုမိုချောမွေ့စေရန်နှင့် noise ကို ဖယ်ရှားရန် **Variation loss** ကို ထည့်သွင်းသည်။ Neighboring pixels အကြားအကွာအဝေးကို တွက်ချက်သည်။
* Optimization loop ၏အဓိကလုပ်ငန်းစဉ်မှာ gradient descent (သို့မဟုတ် အခြား optimization algorithm) ကို အသုံးပြု၍ total loss (loss သုံးခု၏ weighted sum) ကို လျော့နည်းစေရန် current image ကို ပြင်ဆင်သည်။

## ✍️ Example: [Style Transfer](../../../../../lessons/4-ComputerVision/10-GANs/StyleTransfer.ipynb)

## [Post-lecture quiz](https://ff-quizzes.netlify.app/en/ai/quiz/20)

## နိဂုံး

ဒီသင်ခန်းစာတွင် GANs နှင့် ၎င်းတို့ကို သင်ကြားပုံကို လေ့လာခဲ့ပါသည်။ GANs ၏ အထူးပြဿနာများနှင့် ၎င်းတို့ကို ဖြေရှင်းရန်နည်းလမ်းများကိုလည်း လေ့လာခဲ့ပါသည်။

## 🚀 Challenge

သင်၏ပုံများကို အသုံးပြု၍ [Style Transfer notebook](../../../../../lessons/4-ComputerVision/10-GANs/StyleTransfer.ipynb) ကို run လုပ်ပါ။

## Review & Self Study

GANs အကြောင်းကို အောက်ပါရင်းမြစ်များတွင် ပိုမိုလေ့လာပါ -

* Marco Pasini, [10 Lessons I Learned Training GANs for one Year](https://towardsdatascience.com/10-lessons-i-learned-training-generative-adversarial-networks-gans-for-a-year-c9071159628)
* [StyleGAN](https://en.wikipedia.org/wiki/StyleGAN), GAN architecture အနေဖြင့် စဉ်ဆက်မပြတ်အသုံးပြုနေသောနည်းလမ်း
* [Creating Generative Art using GANs on Azure ML](https://soshnikov.com/scienceart/creating-generative-art-using-gan-on-azureml/)

## Assignment

ဒီသင်ခန်းစာနှင့်ဆက်စပ်ထားသော notebook နှစ်ခုမှ တစ်ခုကို ပြန်လည်လေ့လာပြီး၊ သင်၏ပုံများကို အသုံးပြု၍ GAN ကို retrain လုပ်ပါ။ သင်ဘာတွေဖန်တီးနိုင်မလဲ?

**အကြောင်းကြားချက်**:  
ဤစာရွက်စာတမ်းကို AI ဘာသာပြန်ဝန်ဆောင်မှု [Co-op Translator](https://github.com/Azure/co-op-translator) ကို အသုံးပြု၍ ဘာသာပြန်ထားပါသည်။ ကျွန်ုပ်တို့သည် တိကျမှန်ကန်မှုအတွက် ကြိုးစားနေသော်လည်း၊ အလိုအလျောက် ဘာသာပြန်မှုများတွင် အမှားများ သို့မဟုတ် မမှန်ကန်မှုများ ပါဝင်နိုင်သည်ကို သတိပြုပါ။ မူရင်းစာရွက်စာတမ်းကို ၎င်း၏ မူလဘာသာစကားဖြင့် အာဏာရှိသောအရင်းအမြစ်အဖြစ် ရှုလေ့လာသင့်ပါသည်။ အရေးကြီးသော အချက်အလက်များအတွက် လူ့ဘာသာပြန်ပညာရှင်များမှ ပရော်ဖက်ရှင်နယ် ဘာသာပြန်မှုကို အကြံပြုပါသည်။ ဤဘာသာပြန်မှုကို အသုံးပြုခြင်းမှ ဖြစ်ပေါ်လာသော နားလည်မှုမှားများ သို့မဟုတ် အဓိပ္ပာယ်မှားများအတွက် ကျွန်ုပ်တို့သည် တာဝန်မယူပါ။