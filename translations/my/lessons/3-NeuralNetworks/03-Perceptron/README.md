<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "0c37770bba4fff3c71dc00eb261ee61b",
  "translation_date": "2025-08-25T23:59:51+00:00",
  "source_file": "lessons/3-NeuralNetworks/03-Perceptron/README.md",
  "language_code": "my"
}
-->
# နယူးရယ်နက်ဝက်များအကြောင်း အကျဉ်းချုပ်: ပာစက်ထရွန်

## [မဆွေးနွေးမီ စမ်းမေးခွန်း](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/103)

နယူးရယ်နက်ဝက်တစ်ခုကို အချိန်မီနည်းလမ်းဖြင့် ဖန်တီးရန် ပထမဆုံးကြိုးစားမှုတစ်ခုကို 1957 ခုနှစ်တွင် Cornell Aeronautical Laboratory မှ Frank Rosenblatt က ပြုလုပ်ခဲ့သည်။ ၎င်းသည် "Mark-1" ဟုခေါ်သော ဟာ့ဒ်ဝဲတစ်ခုဖြစ်ပြီး၊ တိရိစ္ဆာန်ပုံစံများ (ဥပမာ- တြိဂံ၊ စတုရန်း၊ စက်ဝိုင်း) ကို အသိအမှတ်ပြုနိုင်ရန် ဒီဇိုင်းပြုလုပ်ထားသည်။

|      |      |
|--------------|-----------|
|<img src='images/Rosenblatt-wikipedia.jpg' alt='Frank Rosenblatt'/> | <img src='images/Mark_I_perceptron_wikipedia.jpg' alt='The Mark 1 Perceptron' />|

> ပုံများ [Wikipedia မှ](https://en.wikipedia.org/wiki/Perceptron)

အထဲသို့ ထည့်သွင်းသော ပုံကို 20x20 ဖိုတိုဆဲလ်အကွက်ဖြင့် ကိုယ်စားပြုထားပြီး၊ နယူးရယ်နက်ဝက်တွင် 400 ခုသော အထွက်အချက်အလက်များနှင့် binary output တစ်ခုသာ ရှိသည်။ ရိုးရှင်းသော နက်ဝက်တစ်ခုတွင် **threshold logic unit** ဟုခေါ်သော နယူးရွန်တစ်ခုသာ ပါဝင်သည်။ နယူးရယ်နက်ဝက်၏ အလေးချိန်များသည် ပိုတင်ရှိုမီတာများကဲ့သို့ လုပ်ဆောင်ပြီး၊ သင်ကြားမှုအဆင့်တွင် လက်ဖြင့် ပြင်ဆင်ရန် လိုအပ်သည်။

> ✅ ပိုတင်ရှိုမီတာသည် စက်ဝိုင်း၏ ခုခံမှုကို အသုံးပြုသူက ပြင်ဆင်နိုင်စေသော စက်ကိရိယာတစ်ခုဖြစ်သည်။

> အဲဒီအချိန်တွင် The New York Times သည် ပာစက်ထရွန်အကြောင်းကို *[Navy] သည် လမ်းလျှောက်နိုင်၊ စကားပြောနိုင်၊ မြင်နိုင်၊ ရေးနိုင်၊ ကိုယ့်ကိုယ်ကို ထပ်မံဖန်တီးနိုင်ပြီး၊ ကိုယ့်ရဲ့ တည်ရှိမှုကို သိနိုင်မည့် အီလက်ထရွန်နစ် ကွန်ပျူတာ၏ စတင်အဆင့်* ဟု ဖော်ပြခဲ့သည်။

## ပာစက်ထရွန် မော်ဒယ်

မော်ဒယ်တွင် N အချက်အလက်များ ရှိသည်ဟု ယူဆပါစို့။ ထိုအခါ input vector သည် N အရွယ်အစားရှိသော ဗက်တာတစ်ခုဖြစ်သည်။ ပာစက်ထရွန်သည် **binary classification** မော်ဒယ်တစ်ခုဖြစ်ပြီး၊ အချက်အလက်နှစ်မျိုးကို ခွဲခြားနိုင်သည်။ အချက်အလက်များအတွက် input vector x တစ်ခုစီအတွက် ပာစက်ထရွန်၏ output သည် +1 သို့မဟုတ် -1 ဖြစ်မည်ဟု ယူဆပါမည်။ ထို output ကို အောက်ပါဖော်မြူလာဖြင့် တွက်ချက်မည်-

y(x) = f(w<sup>T</sup>x)

f သည် step activation function ဖြစ်သည်။

<!-- img src="http://www.sciweavers.org/tex2img.php?eq=f%28x%29%20%3D%20%5Cbegin%7Bcases%7D%0A%20%20%20%20%20%20%20%20%20%2B1%20%26%20x%20%5Cgeq%200%20%5C%5C%0A%20%20%20%20%20%20%20%20%20-1%20%26%20x%20%3C%200%0A%20%20%20%20%20%20%20%5Cend%7Bcases%7D%20%5C%5C%0A&bc=White&fc=Black&im=jpg&fs=12&ff=arev&edit=0" align="center" border="0" alt="f(x) = \begin{cases} +1 & x \geq 0 \\ -1 & x < 0 \end{cases} \\" width="154" height="50" / -->
<img src="images/activation-func.png"/>

## ပာစက်ထရွန်ကို သင်ကြားခြင်း

ပာစက်ထရွန်ကို သင်ကြားရန်အတွက် အမှားအနည်းဆုံးဖြစ်စေရန် အများစုသော input data များကို မှန်ကန်စွာ ခွဲခြားနိုင်သော အလေးချိန်ဗက်တာ w ကို ရှာဖွေရမည်။ ထိုအမှား E ကို **perceptron criterion** ဖြင့် အောက်ပါအတိုင်း သတ်မှတ်သည်-

E(w) = -∑w<sup>T</sup>x<sub>i</sub>t<sub>i</sub>

ဒီမှာ:

* စုစုပေါင်းသည် မှားယွင်းသော ခွဲခြားမှုဖြစ်သော training data points i များအပေါ်တွင် ပြုလုပ်သည်။
* x<sub>i</sub> သည် input data ဖြစ်ပြီး၊ t<sub>i</sub> သည် -1 သို့မဟုတ် +1 ဖြစ်သည် (negative နှင့် positive ตัวอย่างများအတွက်)။

ဤ criteria ကို အလေးချိန် w ၏ function အဖြစ် သတ်မှတ်ပြီး၊ ၎င်းကို အနည်းဆုံးအဆင့်သို့ လျှော့ချရန် လိုအပ်သည်။ မကြာခဏ **gradient descent** ဟုခေါ်သော နည်းလမ်းကို အသုံးပြုသည်။ ဤနည်းလမ်းတွင် စတင်အလေးချိန် w<sup>(0)</sup> ဖြင့် စတင်ပြီး၊ အဆင့်တစ်ခုစီတွင် အောက်ပါဖော်မြူလာအတိုင်း အလေးချိန်များကို ပြင်ဆင်သည်-

w<sup>(t+1)</sup> = w<sup>(t)</sup> - η∇E(w)

ဒီမှာ η သည် **learning rate** ဟုခေါ်ပြီး၊ ∇E(w) သည် E ၏ **gradient** ဖြစ်သည်။ Gradient ကို တွက်ချက်ပြီးနောက်-

w<sup>(t+1)</sup> = w<sup>(t)</sup> + ∑ηx<sub>i</sub>t<sub>i</sub>

Python ဖြင့် ရေးသားထားသော အဲဒီ algorithm သည် အောက်ပါအတိုင်းဖြစ်သည်-

```python
def train(positive_examples, negative_examples, num_iterations = 100, eta = 1):

    weights = [0,0,0] # Initialize weights (almost randomly :)
        
    for i in range(num_iterations):
        pos = random.choice(positive_examples)
        neg = random.choice(negative_examples)

        z = np.dot(pos, weights) # compute perceptron output
        if z < 0: # positive example classified as negative
            weights = weights + eta*weights.shape

        z  = np.dot(neg, weights)
        if z >= 0: # negative example classified as positive
            weights = weights - eta*weights.shape

    return weights
```

## အကျဉ်းချုပ်

ဒီသင်ခန်းစာတွင် binary classification မော်ဒယ်ဖြစ်သော ပာစက်ထရွန်နှင့် ၎င်းကို အလေးချိန်ဗက်တာကို အသုံးပြု၍ သင်ကြားနည်းကို သင်ယူခဲ့ပါသည်။

## 🚀 စိန်ခေါ်မှု

သင့်ကိုယ်ပိုင် ပာစက်ထရွန်တစ်ခု ဖန်တီးကြည့်လိုပါက၊ [Microsoft Learn](https://docs.microsoft.com/en-us/azure/machine-learning/component-reference/two-class-averaged-perceptron?WT.mc_id=academic-77998-cacaste) တွင်ရှိသော [Azure ML designer](https://docs.microsoft.com/en-us/azure/machine-learning/concept-designer?WT.mc_id=academic-77998-cacaste) ကို အသုံးပြု၍ လေ့လာကြည့်ပါ။

## [သင်ခန်းစာပြီးနောက် စမ်းမေးခွန်း](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/203)

## ပြန်လည်သုံးသပ်ခြင်းနှင့် ကိုယ်တိုင်လေ့လာခြင်း

ပာစက်ထရွန်ကို အသုံးပြု၍ သေးငယ်သော ပြဿနာများနှင့် အမှန်တကယ် ပြဿနာများကို ဖြေရှင်းနိုင်ပုံကို ကြည့်ရှုရန်နှင့် ဆက်လက်လေ့လာရန် - [Perceptron](../../../../../lessons/3-NeuralNetworks/03-Perceptron/Perceptron.ipynb) notebook သို့ သွားပါ။

ပာစက်ထရွန်များအကြောင်း စိတ်ဝင်စားဖွယ် [ဆောင်းပါး](https://towardsdatascience.com/what-is-a-perceptron-basics-of-neural-networks-c4cfea20c590) တစ်ပုဒ်လည်း ရှိပါသည်။

## [အိမ်စာ](lab/README.md)

ဒီသင်ခန်းစာတွင် binary classification အလုပ်ကို ဆောင်ရွက်ရန် ပာစက်ထရွန်တစ်ခုကို ဖန်တီးခဲ့ပြီး၊ လက်ရေးလက်သားနံပါတ်နှစ်ခုကို ခွဲခြားရန် အသုံးပြုခဲ့သည်။ ဒီ lab တွင် သင့်အား နံပါတ်ခွဲခြားမှု ပြဿနာကို အပြည့်အစုံ ဖြေရှင်းရန် တိုက်တွန်းပါမည်။ အဓိကအားဖြင့် ပုံတစ်ပုံနှင့် ကိုက်ညီနိုင်သော နံပါတ်ကို သတ်မှတ်ရန် လိုအပ်သည်။

* [ညွှန်ကြားချက်များ](lab/README.md)
* [Notebook](../../../../../lessons/3-NeuralNetworks/03-Perceptron/lab/PerceptronMultiClass.ipynb)

**အကြောင်းကြားချက်**:  
ဤစာရွက်စာတမ်းကို AI ဘာသာပြန်ဝန်ဆောင်မှု [Co-op Translator](https://github.com/Azure/co-op-translator) ကို အသုံးပြု၍ ဘာသာပြန်ထားပါသည်။ ကျွန်ုပ်တို့သည် တိကျမှုအတွက် ကြိုးစားနေသော်လည်း၊ အလိုအလျောက် ဘာသာပြန်မှုများတွင် အမှားများ သို့မဟုတ် မမှန်ကန်မှုများ ပါဝင်နိုင်သည်ကို သတိပြုပါ။ မူရင်းစာရွက်စာတမ်းကို ၎င်း၏ မူရင်းဘာသာစကားဖြင့် အာဏာတရားရှိသော အရင်းအမြစ်အဖြစ် သတ်မှတ်သင့်ပါသည်။ အရေးကြီးသော အချက်အလက်များအတွက် လူ့ဘာသာပြန်ပညာရှင်များမှ ပရော်ဖက်ရှင်နယ် ဘာသာပြန်မှုကို အကြံပြုပါသည်။ ဤဘာသာပြန်မှုကို အသုံးပြုခြင်းမှ ဖြစ်ပေါ်လာသော အလွဲအမှားများ သို့မဟုတ် အနားလွဲမှုများအတွက် ကျွန်ုပ်တို့သည် တာဝန်မယူပါ။