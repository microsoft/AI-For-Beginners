<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "7336583e4630220c835335da640016db",
  "translation_date": "2025-08-26T00:01:34+00:00",
  "source_file": "lessons/3-NeuralNetworks/03-Perceptron/lab/README.md",
  "language_code": "my"
}
-->
# Multi-Class Classification with Perceptron

[AI for Beginners Curriculum](https://github.com/microsoft/ai-for-beginners) မှ လက်တွေ့လေ့ကျင့်ခန်း။

## လုပ်ငန်းတာဝန်

ဒီသင်ခန်းစာမှာ MNIST လက်ရေးလက်သားဂဏန်းများကို binary classification အတွက် ဖန်တီးထားတဲ့ ကုဒ်ကို အသုံးပြုပြီး၊ မည်သည့်ဂဏန်းကိုမဆို အသိအမှတ်ပြုနိုင်မည့် multi-class classified တစ်ခု ဖန်တီးပါ။ သင်ကြားမှုနှင့် စမ်းသပ်မှု dataset များပေါ်တွင် classification accuracy ကိုတွက်ချက်ပြီး confusion matrix ကို print ထုတ်ပါ။

## အကြံပြုချက်များ

1. ဂဏန်းတစ်ခုစီအတွက် "ဒီဂဏန်း vs. အခြားဂဏန်းအားလုံး" binary classifier အတွက် dataset တစ်ခုဖန်တီးပါ။
1. Binary classification အတွက် perceptron ၁၀ ခု (ဂဏန်းတစ်ခုစီအတွက် တစ်ခုစီ) ကို လေ့ကျင့်ပါ။
1. Input digit ကို အသိအမှတ်ပြုနိုင်မည့် function တစ်ခု သတ်မှတ်ပါ။

> **အကြံပြုချက်**: Perceptron ၁၀ ခု၏ အလေးချိန်များကို matrix တစ်ခုအဖြစ် ပေါင်းစည်းထားနိုင်ပါက၊ input digits များကို perceptron ၁၀ ခုလုံးဖြင့် matrix multiplication တစ်ခုတည်းဖြင့် လျှောက်ထားနိုင်ပါမည်။ ထွက်လာသောရလဒ်တွင် `argmax` operation ကို အသုံးပြုခြင်းဖြင့် အများဆုံးဖြစ်နိုင်သောဂဏန်းကို ရှာဖွေနိုင်ပါသည်။

## စတင်ရန် Notebook

[PerceptronMultiClass.ipynb](../../../../../../lessons/3-NeuralNetworks/03-Perceptron/lab/PerceptronMultiClass.ipynb) ကို ဖွင့်ပြီး လက်တွေ့လေ့ကျင့်ခန်းကို စတင်ပါ။

**အကြောင်းကြားချက်**:  
ဤစာရွက်စာတမ်းကို AI ဘာသာပြန်ဝန်ဆောင်မှု [Co-op Translator](https://github.com/Azure/co-op-translator) ကို အသုံးပြု၍ ဘာသာပြန်ထားပါသည်။ ကျွန်ုပ်တို့သည် တိကျမှုအတွက် ကြိုးစားနေသော်လည်း၊ အလိုအလျောက် ဘာသာပြန်ခြင်းတွင် အမှားများ သို့မဟုတ် မမှန်ကန်မှုများ ပါဝင်နိုင်သည်ကို သတိပြုပါ။ မူရင်းစာရွက်စာတမ်းကို ၎င်း၏ မူလဘာသာစကားဖြင့် အာဏာတရ အရင်းအမြစ်အဖြစ် သတ်မှတ်သင့်ပါသည်။ အရေးကြီးသော အချက်အလက်များအတွက် လူ့ဘာသာပြန်ပညာရှင်များမှ ပရော်ဖက်ရှင်နယ် ဘာသာပြန်ခြင်းကို အကြံပြုပါသည်။ ဤဘာသာပြန်ကို အသုံးပြုခြင်းမှ ဖြစ်ပေါ်လာသော အလွဲအမှားများ သို့မဟုတ် အနားလွဲမှုများအတွက် ကျွန်ုပ်တို့သည် တာဝန်မယူပါ။