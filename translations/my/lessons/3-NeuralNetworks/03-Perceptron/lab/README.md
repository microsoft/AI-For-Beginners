# Multi-Class Classification with Perceptron

[AI for Beginners Curriculum](https://github.com/microsoft/ai-for-beginners) မှ Lab Assignment။

## Task

ဒီသင်ခန်းစာမှာ MNIST လက်ရေးလက်သားဂဏန်းများကို binary classification အတွက် ဖန်တီးထားတဲ့ ကုဒ်ကို အသုံးပြုပြီး၊ မည်သည့်ဂဏန်းကိုမဆို အသိအမှတ်ပြုနိုင်မယ့် multi-class classifier တစ်ခု ဖန်တီးပါ။ Train dataset နဲ့ test dataset ပေါ်မှာ classification accuracy ကိုတွက်ချက်ပြီး၊ confusion matrix ကို print ထုတ်ပါ။

## Hints

1. ဂဏန်းတစ်ခုစီအတွက် "ဒီဂဏန်း vs. အခြားဂဏန်းအားလုံး" ဆိုတဲ့ binary classifier dataset တစ်ခုဖန်တီးပါ။
1. Binary classification အတွက် perceptron 10 ခု (ဂဏန်းတစ်ခုစီအတွက် တစ်ခုစီ) ကို train လုပ်ပါ။
1. Input digit ကို classify လုပ်ပေးမယ့် function တစ်ခုကို သတ်မှတ်ပါ။

> **Hint**: Perceptron 10 ခုရဲ့ weight တွေကို matrix တစ်ခုအဖြစ် ပေါင်းစည်းထားနိုင်ရင်၊ input digit တွေကို perceptron 10 ခုလုံးနဲ့ တစ်ကြိမ်တည်း matrix multiplication နဲ့ လျှောက်ထားနိုင်ပါတယ်။ အထွေထွေဆုံးဂဏန်းကို `argmax` operation ကို output ပေါ်မှာ လျှောက်ထားရုံနဲ့ ရှာနိုင်ပါတယ်။

## Starting Notebook

Lab ကို [PerceptronMultiClass.ipynb](PerceptronMultiClass.ipynb) ဖွင့်ပြီး စတင်ပါ။

---

**အကြောင်းကြားချက်**:  
ဤစာရွက်စာတမ်းကို AI ဘာသာပြန်ဝန်ဆောင်မှု [Co-op Translator](https://github.com/Azure/co-op-translator) ကို အသုံးပြု၍ ဘာသာပြန်ထားပါသည်။ ကျွန်ုပ်တို့သည် တိကျမှုအတွက် ကြိုးစားနေသော်လည်း၊ အလိုအလျောက် ဘာသာပြန်ခြင်းတွင် အမှားများ သို့မဟုတ် မတိကျမှုများ ပါဝင်နိုင်သည်ကို သတိပြုပါ။ မူရင်းစာရွက်စာတမ်းကို ၎င်း၏ မူရင်းဘာသာစကားဖြင့် အာဏာတရားရှိသော အရင်းအမြစ်အဖြစ် သတ်မှတ်သင့်ပါသည်။ အရေးကြီးသော အချက်အလက်များအတွက် လူ့ဘာသာပြန်ပညာရှင်များမှ ပရော်ဖက်ရှင်နယ် ဘာသာပြန်ခြင်းကို အကြံပြုပါသည်။ ဤဘာသာပြန်ကို အသုံးပြုခြင်းမှ ဖြစ်ပေါ်လာသော အလွဲအလွတ်များ သို့မဟုတ် အနားယူမှုများအတွက် ကျွန်ုပ်တို့သည် တာဝန်မယူပါ။