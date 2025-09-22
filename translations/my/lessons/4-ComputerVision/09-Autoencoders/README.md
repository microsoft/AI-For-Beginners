<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "0b306c04f5337b6e7430e5c0b16bb5c0",
  "translation_date": "2025-08-25T22:32:54+00:00",
  "source_file": "lessons/4-ComputerVision/09-Autoencoders/README.md",
  "language_code": "my"
}
-->
# Autoencoders

CNN များကိုလေ့ကျင့်ရာတွင် အဓိကပြဿနာတစ်ခုမှာ အမှတ်အသားပြုထားသော ဒေတာများအများကြီးလိုအပ်သည်။ ဥပမာအားဖြင့် ပုံများကို အမျိုးအစားအလိုက်ခွဲခြားရန် လိုအပ်ပြီး၊ ၎င်းသည်လူ့အင်အားဖြင့် လုပ်ဆောင်ရမည့်အလုပ်ဖြစ်သည်။

## [Pre-lecture quiz](https://ff-quizzes.netlify.app/en/ai/quiz/17)

သို့သော်၊ CNN feature extractors များကိုလေ့ကျင့်ရန် အမှတ်အသားမပြုထားသော (raw) ဒေတာများကို အသုံးပြုလိုနိုင်သည်။ ၎င်းကို **self-supervised learning** ဟုခေါ်သည်။ အမှတ်အသားများအစား၊ ပုံများကို network input နှင့် output အဖြစ်အသုံးပြုမည်ဖြစ်သည်။ **autoencoder** ၏ အဓိကအကြောင်းအရာမှာ **encoder network** တစ်ခုကို အသုံးပြု၍ input ပုံကို **latent space** (အများအားဖြင့် အရွယ်အစားသေးငယ်သော vector) တစ်ခုအဖြစ် ပြောင်းလဲပြီး၊ **decoder network** သည် မူရင်းပုံကို ပြန်လည်ဖန်တီးရန် ရည်ရွယ်ထားသည်။

> ✅ [autoencoder](https://wikipedia.org/wiki/Autoencoder) သည် "အမှတ်အသားမပြုထားသော ဒေတာများကို ထိရောက်စွာ encode လုပ်ရန် လေ့လာသည့် artificial neural network အမျိုးအစားတစ်ခုဖြစ်သည်။"

autoencoder ကို accurate reconstruction ရရှိရန် မူရင်းပုံမှ အချက်အလက်များကို အများဆုံးဖမ်းယူရန် လေ့ကျင့်နေသောကြောင့်၊ network သည် input ပုံများ၏ အဓိပ္ပါယ်ကို ဖမ်းယူရန် အကောင်းဆုံး **embedding** ကို ရှာဖွေသည်။

![AutoEncoder Diagram](../../../../../translated_images/autoencoder_schema.5e6fc9ad98a5eb6197f3513cf3baf4dfbe1389a6ae74daebda64de9f1c99f142.my.jpg)

> ပုံကို [Keras blog](https://blog.keras.io/building-autoencoders-in-keras.html) မှရယူသည်

## Autoencoders အသုံးပြုနိုင်သောအခြေအနေများ

မူရင်းပုံများကို ပြန်လည်ဖန်တီးခြင်းသည် ကိုယ်တိုင်အသုံးဝင်သည်ဟု မထင်ရသော်လည်း၊ autoencoders အထူးအသုံးဝင်သော အခြေအနေများ ရှိသည်။

* **ပုံများ၏ dimension ကို လျှော့ချခြင်း** သို့မဟုတ် **image embeddings များကို လေ့ကျင့်ခြင်း**။ Autoencoders များသည် PCA ထက် ပိုမိုကောင်းမွန်သောရလဒ်များပေးနိုင်သည်၊ အကြောင်းမှာ ၎င်းသည် ပုံများ၏ spatial nature နှင့် hierarchical features များကို ထည့်သွင်းစဉ်းစားသောကြောင့်ဖြစ်သည်။
* **Denoising**၊ ပုံမှ ဆူညံသံကို ဖယ်ရှားခြင်း။ ဆူညံသံသည် အသုံးမဝင်သော အချက်အလက်များစွာကို ပါဝင်သောကြောင့် autoencoder သည် ၎င်းအား latent space သေးငယ်သောနေရာတွင် အားလုံးကို fit လုပ်၍မရနိုင်ပါ၊ ထို့ကြောင့် ပုံ၏ အရေးပါသောအပိုင်းကိုသာ ဖမ်းယူသည်။ Denoisers များကို လေ့ကျင့်ရာတွင် မူရင်းပုံများကို စတင်အသုံးပြုပြီး၊ ဆူညံသံ artificial ထည့်သွင်းထားသောပုံများကို autoencoder input အဖြစ်အသုံးပြုသည်။
* **Super-resolution**၊ ပုံ၏ resolution ကို မြှင့်တင်ခြင်း။ Resolution မြင့်သောပုံများကို စတင်အသုံးပြုပြီး၊ resolution နိမ့်သောပုံကို autoencoder input အဖြစ်အသုံးပြုသည်။
* **Generative models**။ autoencoder ကို လေ့ကျင့်ပြီးနောက်၊ decoder အပိုင်းကို random latent vectors မှ စတင်၍ object အသစ်များဖန်တီးရန် အသုံးပြုနိုင်သည်။

## Variational Autoencoders (VAE)

Traditional autoencoders များသည် input data ၏ dimension ကို လျှော့ချပြီး၊ input ပုံများ၏ အရေးပါသော features များကို ရှာဖွေသည်။ သို့သော် latent vectors များသည် အဓိပ္ပါယ်မရှိသောအခါများရှိသည်။ ဥပမာအားဖြင့် MNIST dataset ကိုယူကာ၊ latent vectors များနှင့် digit များကို ဆက်စပ်စဉ်းစားရန် မလွယ်ကူပါ၊ အနီးစပ်ဆုံး latent vectors များသည် တူညီသော digit များကို မဖြစ်စေပါ။

Generative models များကို လေ့ကျင့်ရန် latent space ကို နားလည်ရန် ပိုမိုကောင်းမွန်သည်။ ဤအကြောင်းအရာသည် **variational auto-encoder** (VAE) သို့ ဦးတည်စေသည်။

VAE သည် latent parameters ၏ *statistical distribution* ကို ခန့်မှန်းရန် လေ့ကျင့်သော autoencoder ဖြစ်ပြီး၊ ၎င်းကို **latent distribution** ဟုခေါ်သည်။ ဥပမာအားဖြင့် latent vectors များကို z<sub>mean</sub> နှင့် z<sub>sigma</sub> (mean နှင့် standard deviation သည် dimensionality d ရှိသော vectors ဖြစ်သည်) ဖြင့် normal distribution အတိုင်း ခန့်မှန်းလိုနိုင်သည်။ VAE ၏ encoder သည် ၎င်း parameters များကို ခန့်မှန်းပြီး၊ decoder သည် ဤ distribution မှ random vector ကိုယူကာ object ကို ပြန်လည်ဖန်တီးသည်။

အကျဉ်းချုပ်အားဖြင့် -

 * Input vector မှ `z_mean` နှင့် `z_log_sigma` ကို ခန့်မှန်းသည် (standard deviation ကို ခန့်မှန်းခြင်းမဟုတ်ဘဲ၊ ၎င်း၏ logarithm ကို ခန့်မှန်းသည်)
 * Distribution N(z<sub>mean</sub>,exp(z<sub>log\_sigma</sub>)) မှ `sample` vector ကို ရွေးချယ်သည်
 * Decoder သည် `sample` ကို input vector အဖြစ်အသုံးပြုကာ မူရင်းပုံကို ပြန်လည်ဖန်တီးရန် ကြိုးစားသည်

 <img src="images/vae.png" width="50%">

> ပုံကို [Isaak Dykeman](https://ijdykeman.github.io/ml/2016/12/21/cvae.html) ၏ blog post မှရယူသည်

Variational auto-encoders တွင် loss function အစိတ်အပိုင်းနှစ်ခုပါဝင်သည် -

* **Reconstruction loss** သည် target နှင့် ပြန်လည်ဖန်တီးထားသောပုံ၏ နီးစပ်မှုကို ပြသသော loss function ဖြစ်သည် (Mean Squared Error, MSE ဖြစ်နိုင်သည်)။ ၎င်းသည် normal autoencoders တွင် အသုံးပြုသော loss function နှင့် တူသည်။
* **KL loss** သည် latent variable distributions ကို normal distribution နှင့် နီးစပ်စေသည်။ ၎င်းသည် [Kullback-Leibler divergence](https://www.countbayesie.com/blog/2017/5/9/kullback-leibler-divergence-explained) အပေါ် အခြေခံသည် - statistical distributions နှစ်ခု၏ တူညီမှုကို ခန့်မှန်းရန် metric တစ်ခုဖြစ်သည်။

VAE ၏ အရေးပါသောအားသာချက်တစ်ခုမှာ latent vectors ကို sample လုပ်ရန် distribution ကို သိရှိထားသောကြောင့် ပုံအသစ်များကို လွယ်ကူစွာ ဖန်တီးနိုင်သည်။ ဥပမာအားဖြင့် MNIST dataset ကို 2D latent vector ဖြင့် VAE ကို လေ့ကျင့်ပါက latent vector ၏ components များကို ပြောင်းလဲကာ digit များကို ရနိုင်သည် -

<img alt="vaemnist" src="images/vaemnist.png" width="50%"/>

> ပုံကို [Dmitry Soshnikov](http://soshnikov.com) မှရယူသည်

latent parameter space ၏ အခြားအစိတ်အပိုင်းများမှ latent vectors များကို ရယူသောအခါ၊ ပုံများသည် တစ်ခုနှင့်တစ်ခု ပေါင်းစပ်နေသည်ကို တွေ့နိုင်သည်။ ဤ space ကို 2D အနေနှင့် visualization ပြုလုပ်နိုင်သည် -

<img alt="vaemnist cluster" src="images/vaemnist-diag.png" width="50%"/> 

> ပုံကို [Dmitry Soshnikov](http://soshnikov.com) မှရယူသည်

## ✍️ Exercises: Autoencoders

Autoencoders အကြောင်းကို အောက်ပါ notebooks များတွင် ပိုမိုလေ့လာပါ -

* [Autoencoders in TensorFlow](../../../../../lessons/4-ComputerVision/09-Autoencoders/AutoencodersTF.ipynb)
* [Autoencoders in PyTorch](../../../../../lessons/4-ComputerVision/09-Autoencoders/AutoEncodersPyTorch.ipynb)

## Autoencoders ၏ Properties

* **Data Specific** - ၎င်းသည် လေ့ကျင့်ထားသော ပုံအမျိုးအစားများတွင်သာ ကောင်းမွန်စွာ အလုပ်လုပ်သည်။ ဥပမာအားဖြင့် flower များအပေါ် super-resolution network ကို လေ့ကျင့်ပါက portrait များအပေါ် ကောင်းမွန်စွာ အလုပ်မလုပ်နိုင်ပါ။ ၎င်းသည် training dataset မှ features များကို အသုံးပြုကာ resolution မြင့်သောပုံကို ဖန်တီးသောကြောင့်ဖြစ်သည်။
* **Lossy** - ပြန်လည်ဖန်တီးထားသောပုံသည် မူရင်းပုံနှင့် တူညီမှုမရှိပါ။ Loss ၏ nature ကို training အတွင်း အသုံးပြုသော *loss function* က သတ်မှတ်သည်။
* **Unlabeled data** တွင် အလုပ်လုပ်သည်။

## [Post-lecture quiz](https://ff-quizzes.netlify.app/en/ai/quiz/18)

## အကျဉ်းချုပ်

ဤသင်ခန်းစာတွင် autoencoders ၏ အမျိုးအစားများနှင့် ၎င်းတို့ကို AI scientist အနေဖြင့် ဘယ်လိုအသုံးပြုရမည်ကို သင်လေ့လာခဲ့သည်။ ၎င်းတို့ကို ဘယ်လိုတည်ဆောက်ရမည်၊ ပုံများကို ပြန်လည်ဖန်တီးရန် ဘယ်လိုအသုံးပြုရမည်ကိုလည်း သင်လေ့လာခဲ့သည်။ VAE နှင့် ၎င်းကို အသုံးပြုကာ ပုံအသစ်များဖန်တီးရန် ဘယ်လိုလုပ်ရမည်ကိုလည်း သင်လေ့လာခဲ့သည်။

## 🚀 Challenge

ဤသင်ခန်းစာတွင် autoencoders ကို ပုံများအတွက် အသုံးပြုခြင်းကို သင်လေ့လာခဲ့သည်။ သို့သော်၊ ၎င်းတို့ကို ဂီတအတွက်လည်း အသုံးပြုနိုင်သည်! Magenta project ၏ [MusicVAE](https://magenta.tensorflow.org/music-vae) ကို ကြည့်ရှုပါ၊ autoencoders ကို အသုံးပြုကာ ဂီတကို ပြန်လည်ဖန်တီးရန် လေ့လာထားသည်။ ဤ library ကို အသုံးပြုကာ [အတွေ့အကြုံများ](https://colab.research.google.com/github/magenta/magenta-demos/blob/master/colab-notebooks/Multitrack_MusicVAE.ipynb) လုပ်ဆောင်ပြီး၊ သင်ဖန်တီးနိုင်သည့်အရာများကို ကြည့်ရှုပါ။

## [Post-lecture quiz](https://ff-quizzes.netlify.app/en/ai/quiz/16)

## Review & Self Study

Autoencoders အကြောင်းကို အောက်ပါ resources များတွင် ပိုမိုလေ့လာပါ -

* [Building Autoencoders in Keras](https://blog.keras.io/building-autoencoders-in-keras.html)
* [Blog post on NeuroHive](https://neurohive.io/ru/osnovy-data-science/variacionnyj-avtojenkoder-vae/)
* [Variational Autoencoders Explained](https://kvfrans.com/variational-autoencoders-explained/)
* [Conditional Variational Autoencoders](https://ijdykeman.github.io/ml/2016/12/21/cvae.html)

## Assignment

[AutoencodersTF.ipynb](../../../../../lessons/4-ComputerVision/09-Autoencoders/AutoencodersTF.ipynb) notebook ၏ အဆုံးတွင် 'task' ရှိသည် - ၎င်းကို သင်၏ assignment အဖြစ် အသုံးပြုပါ။

**အကြောင်းကြားချက်**:  
ဤစာရွက်စာတမ်းကို AI ဘာသာပြန်ဝန်ဆောင်မှု [Co-op Translator](https://github.com/Azure/co-op-translator) ကို အသုံးပြု၍ ဘာသာပြန်ထားပါသည်။ ကျွန်ုပ်တို့သည် တိကျမှုအတွက် ကြိုးစားနေသော်လည်း၊ အလိုအလျောက် ဘာသာပြန်ခြင်းတွင် အမှားများ သို့မဟုတ် မမှန်ကန်မှုများ ပါဝင်နိုင်သည်ကို သတိပြုပါ။ မူရင်းစာရွက်စာတမ်းကို ၎င်း၏ မူရင်းဘာသာစကားဖြင့် အာဏာတရားရှိသော အရင်းအမြစ်အဖြစ် သတ်မှတ်သင့်ပါသည်။ အရေးကြီးသော အချက်အလက်များအတွက် လူက ဘာသာပြန်ခြင်းကို အကြံပြုပါသည်။ ဤဘာသာပြန်ကို အသုံးပြုခြင်းမှ ဖြစ်ပေါ်လာသော အလွဲအမှားများ သို့မဟုတ် အနားလွဲမှုများအတွက် ကျွန်ုပ်တို့သည် တာဝန်မယူပါ။