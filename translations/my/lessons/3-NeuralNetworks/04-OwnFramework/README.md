<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "186bf7eeab776b36f557357ea56d4751",
  "translation_date": "2025-08-25T23:48:13+00:00",
  "source_file": "lessons/3-NeuralNetworks/04-OwnFramework/README.md",
  "language_code": "my"
}
-->
# နယူးရယ်နက်ဝက်များကို မိတ်ဆက်ခြင်း။ Multi-Layered Perceptron

ယခင်အခန်းတွင် သင်သည် အလွယ်တကူ နယူးရယ်နက်ဝက်မော်ဒယ် - တစ်လွှာတည်းရှိသော perceptron, linear two-class classification မော်ဒယ်ကို လေ့လာခဲ့ပါသည်။

ဤအခန်းတွင် ကျွန်ုပ်တို့သည် ဤမော်ဒယ်ကို ပိုမိုကျယ်ပြန့်သော framework သို့ တိုးချဲ့မည်ဖြစ်ပြီး၊ အောက်ပါအရာများကို ပြုလုပ်နိုင်စေမည်ဖြစ်သည်-

* **multi-class classification** ကို two-class classification အပြင် ပြုလုပ်နိုင်စေမည်
* classification အပြင် **regression problems** ကို ဖြေရှင်းနိုင်စေမည်
* linear မဖြတ်နိုင်သော classes များကို ခွဲခြားနိုင်စေမည်

ထို့အပြင် Python တွင် မိမိကိုယ်တိုင် modular framework တစ်ခုကို ဖွံ့ဖြိုးတိုးတက်စေပြီး၊ နယူးရယ်နက်ဝက် architecture များကို တည်ဆောက်နိုင်စေမည်။

## [Pre-lecture quiz](https://ff-quizzes.netlify.app/en/ai/quiz/7)

## Machine Learning ကို တိကျစွာ ဖော်ပြခြင်း

Machine Learning ပြဿနာကို တိကျစွာ ဖော်ပြခြင်းဖြင့် စတင်ကြပါစို့။ သင့်တွင် training dataset **X** နှင့် labels **Y** ရှိသည်ဟု ယူဆပါ။ ထို့နောက် အတိအကျဆုံး ခန့်မှန်းချက်များကို ပြုလုပ်နိုင်မည့် *f* မော်ဒယ်တစ်ခုကို တည်ဆောက်ရန် လိုအပ်ပါသည်။ ခန့်မှန်းချက်များ၏ အရည်အသွေးကို **Loss function** ℒ ဖြင့် တိုင်းတာသည်။ အောက်ပါ loss functions များကို မကြာခဏ အသုံးပြုသည်-

* regression problem အတွက်၊ နံပါတ်တစ်ခုကို ခန့်မှန်းရန် လိုအပ်သောအခါ **absolute error** ∑<sub>i</sub>|f(x<sup>(i)</sup>)-y<sup>(i)</sup>| သို့မဟုတ် **squared error** ∑<sub>i</sub>(f(x<sup>(i)</sup>)-y<sup>(i)</sup>)<sup>2</sup> ကို အသုံးပြုနိုင်သည်။
* classification အတွက် **0-1 loss** (မော်ဒယ်၏ **accuracy** နှင့် အတူတူပင်) သို့မဟုတ် **logistic loss** ကို အသုံးပြုသည်။

တစ်လွှာတည်းရှိသော perceptron အတွက် *f* function ကို *f(x)=wx+b* ဟု သတ်မှတ်ထားသည် (ဤနေရာတွင် *w* သည် weight matrix ဖြစ်ပြီး၊ *x* သည် input features vector ဖြစ်ပြီး၊ *b* သည် bias vector ဖြစ်သည်။) နယူးရယ်နက်ဝက် architecture များအတွက် ဤ function သည် ပိုမိုရှုပ်ထွေးသော ပုံစံကို ရရှိနိုင်သည်။

> classification အတွက်၊ network output အနေဖြင့် classes များ၏ probability များကို ရရှိရန် လိုအပ်သောအခါများစွာရှိသည်။ output ကို normalize ပြုလုပ်ရန် **softmax** function σ ကို အသုံးပြုသည်။ ထို့ကြောင့် function *f* သည် *f(x)=σ(wx+b)* ဖြစ်လာသည်။

*f* ၏ အထက်ပါ သတ်မှတ်ချက်တွင် *w* နှင့် *b* ကို **parameters** θ=⟨*w,b*⟩ ဟု ခေါ်သည်။ dataset ⟨**X**,**Y**⟩ ကို ပေးထားသောအခါ၊ parameters θ အပေါ် dataset တစ်ခုလုံး၏ error ကို function အနေဖြင့် တွက်ချက်နိုင်သည်။

> ✅ **နယူးရယ်နက်ဝက် training ၏ ရည်ရွယ်ချက်မှာ parameters θ ကို ပြောင်းလဲခြင်းဖြင့် error ကို လျှော့ချရန် ဖြစ်သည်**

## Gradient Descent Optimization

Function optimization ၏ နာမည်ကျော်နည်းလမ်းတစ်ခုကို **gradient descent** ဟု ခေါ်သည်။ အဆိုပါ idea သည် loss function ၏ derivative (multi-dimensional အတွက် **gradient** ဟု ခေါ်သည်) ကို parameters အပေါ်တွင် တွက်ချက်ပြီး၊ error ကို လျှော့ချနိုင်စေရန် parameters များကို ပြောင်းလဲခြင်းဖြစ်သည်။ ဤနည်းလမ်းကို အောက်ပါအတိုင်း formalize ပြုလုပ်နိုင်သည်-

* parameters များကို w<sup>(0)</sup>, b<sup>(0)</sup> အဖြစ် random values ဖြင့် initialize ပြုလုပ်ပါ
* အောက်ပါအဆင့်ကို မကြာခဏ ထပ်မံလုပ်ဆောင်ပါ-
    - w<sup>(i+1)</sup> = w<sup>(i)</sup>-η∂ℒ/∂w
    - b<sup>(i+1)</sup> = b<sup>(i)</sup>-η∂ℒ/∂b

Training အတွင်း optimization steps များကို dataset တစ်ခုလုံးကို အခြေခံ၍ တွက်ချက်ရန် ရည်ရွယ်ထားသည် (loss ကို training samples အားလုံးအတွက် စုစုပေါင်းအနေဖြင့် တွက်ချက်သည်ကို မှတ်ထားပါ။) သို့သော် အမှန်တကယ်တွင် dataset ၏ အပိုင်းငယ်များကို **minibatches** ဟု ခေါ်သည်။ ထို့နောက် data အစုတစ်ခုကို random အနေဖြင့် ရွေးချယ်ပြီး gradient များကို တွက်ချက်သည်။ အခါအားလျော်စွာ subset ကို random ရွေးချယ်သောကြောင့် ဤနည်းလမ်းကို **stochastic gradient descent** (SGD) ဟု ခေါ်သည်။

## Multi-Layered Perceptrons နှင့် Backpropagation

တစ်လွှာတည်းရှိသော network သည် linear separable classes များကို ခွဲခြားနိုင်စွမ်းရှိသည်ဟု ကျွန်ုပ်တို့ မြင်ခဲ့ပါသည်။ ပိုမိုချောမွေ့သော မော်ဒယ်တစ်ခုကို တည်ဆောက်ရန်၊ network ၏ လွှာများစွာကို ပေါင်းစည်းနိုင်သည်။ သင်္ချာအရ၊ function *f* သည် ပိုမိုရှုပ်ထွေးသော ပုံစံကို ရရှိမည်ဖြစ်ပြီး၊ အဆင့်များစွာတွင် တွက်ချက်မည်ဖြစ်သည်-

* z<sub>1</sub>=w<sub>1</sub>x+b<sub>1</sub>
* z<sub>2</sub>=w<sub>2</sub>α(z<sub>1</sub>)+b<sub>2</sub>
* f = σ(z<sub>2</sub>)

ဤနေရာတွင် α သည် **non-linear activation function** ဖြစ်ပြီး၊ σ သည် softmax function ဖြစ်သည်။ parameters θ=<*w<sub>1</sub>,b<sub>1</sub>,w<sub>2</sub>,b<sub>2</sub>*> ဖြစ်သည်။

Gradient descent algorithm သည် အတူတူပင်ရှိနေသော်လည်း gradient များကို တွက်ချက်ရန် ပိုမိုခက်ခဲလာမည်။ chain differentiation rule ကို အသုံးပြု၍ derivatives များကို အောက်ပါအတိုင်း တွက်ချက်နိုင်သည်-

* ∂ℒ/∂w<sub>2</sub> = (∂ℒ/∂σ)(∂σ/∂z<sub>2</sub>)(∂z<sub>2</sub>/∂w<sub>2</sub>)
* ∂ℒ/∂w<sub>1</sub> = (∂ℒ/∂σ)(∂σ/∂z<sub>2</sub>)(∂z<sub>2</sub>/∂α)(∂α/∂z<sub>1</sub>)(∂z<sub>1</sub>/∂w<sub>1</sub>)

> ✅ chain differentiation rule ကို loss function ၏ parameters အပေါ် derivatives တွက်ချက်ရန် အသုံးပြုသည်။

ဤ expression များ၏ ဘယ်ဘက်ဆုံးအစိတ်အပိုင်းသည် အတူတူပင်ဖြစ်ပြီး၊ loss function မှ စတင်၍ computational graph ကို "backwards" သို့ သွားပြီး derivatives တွက်ချက်နိုင်သည်။ ထို့ကြောင့် multi-layered perceptron ကို training ပြုလုပ်ရန် **backpropagation** သို့မဟုတ် 'backprop' ဟု ခေါ်သော နည်းလမ်းကို အသုံးပြုသည်။

<img alt="compute graph" src="images/ComputeGraphGrad.png"/>

> TODO: image citation

> ✅ ကျွန်ုပ်တို့၏ notebook ဥပမာတွင် backprop ကို ပိုမိုအသေးစိတ်လေ့လာမည်။

## နိဂုံး

ဤသင်ခန်းစာတွင် ကျွန်ုပ်တို့သည် မိမိကိုယ်တိုင် neural network library တစ်ခုကို တည်ဆောက်ခဲ့ပြီး၊ two-dimensional classification task အတွက် အသုံးပြုခဲ့သည်။

## 🚀 စိန်ခေါ်မှု

ပါဝင်သော notebook တွင် သင်သည် multi-layered perceptrons တည်ဆောက်ခြင်းနှင့် training ပြုလုပ်ခြင်းအတွက် မိမိကိုယ်တိုင် framework တစ်ခုကို အကောင်အထည်ဖော်မည်။ သင်သည် modern neural networks မည်သို့ လုပ်ဆောင်သည်ကို အသေးစိတ်ကြည့်ရှုနိုင်မည်။

[OwnFramework](../../../../../lessons/3-NeuralNetworks/04-OwnFramework/OwnFramework.ipynb) notebook သို့ သွားပြီး အလုပ်လုပ်ပါ။

## [Post-lecture quiz](https://ff-quizzes.netlify.app/en/ai/quiz/8)

## Review & Self Study

Backpropagation သည် AI နှင့် ML တွင် အသုံးပြုသော နည်းလမ်းတစ်ခုဖြစ်ပြီး၊ [ပိုမိုအသေးစိတ်](https://wikipedia.org/wiki/Backpropagation) လေ့လာရန် တန်ဖိုးရှိသည်။

## [Assignment](lab/README.md)

ဤ lab တွင် သင်သည် ဤသင်ခန်းစာတွင် တည်ဆောက်ခဲ့သော framework ကို အသုံးပြု၍ MNIST handwritten digit classification ကို ဖြေရှင်းရန် တိုက်တွန်းထားသည်။

* [Instructions](lab/README.md)
* [Notebook](../../../../../lessons/3-NeuralNetworks/04-OwnFramework/lab/MyFW_MNIST.ipynb)

**အကြောင်းကြားချက်**:  
ဤစာရွက်စာတမ်းကို AI ဘာသာပြန်ဝန်ဆောင်မှု [Co-op Translator](https://github.com/Azure/co-op-translator) ကို အသုံးပြု၍ ဘာသာပြန်ထားပါသည်။ ကျွန်ုပ်တို့သည် တိကျမှုအတွက် ကြိုးစားနေသော်လည်း၊ အလိုအလျောက် ဘာသာပြန်မှုများတွင် အမှားများ သို့မဟုတ် မတိကျမှုများ ပါဝင်နိုင်သည်ကို သတိပြုပါ။ မူရင်းစာရွက်စာတမ်းကို ၎င်း၏ မူလဘာသာစကားဖြင့် အာဏာတရားရှိသော အရင်းအမြစ်အဖြစ် သတ်မှတ်သင့်ပါသည်။ အရေးကြီးသော အချက်အလက်များအတွက် လူ့ဘာသာပြန်ပညာရှင်များမှ ပရော်ဖက်ရှင်နယ် ဘာသာပြန်မှုကို အကြံပြုပါသည်။ ဤဘာသာပြန်မှုကို အသုံးပြုခြင်းမှ ဖြစ်ပေါ်လာသော အလွဲအလွတ်များ သို့မဟုတ် အနားလွဲမှုများအတွက် ကျွန်ုပ်တို့သည် တာဝန်မယူပါ။