<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "d9de7847385eeeda67cfdcce1640ab72",
  "translation_date": "2025-08-25T21:47:24+00:00",
  "source_file": "lessons/5-NLP/17-GenerativeNetworks/README.md",
  "language_code": "my"
}
-->
# Generative networks

## [Pre-lecture quiz](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/117)

Recurrent Neural Networks (RNNs) နှင့် Long Short Term Memory Cells (LSTMs)၊ Gated Recurrent Units (GRUs) ကဲ့သို့သော gated cell မျိုးကွဲများသည် စကားလုံးများ၏ အစီအစဉ်ကို သင်ယူနိုင်ပြီး အစီအစဉ်အတွင်း နောက်တစ်ခုလာမည့် စကားလုံးကို ခန့်မှန်းပေးနိုင်သောကြောင့် ဘာသာစကားမော်ဒယ်ဖန်တီးရာတွင် အထောက်အကူဖြစ်စေပါသည်။ ၎င်းတို့ကို အသုံးပြု၍ RNNs ကို **ဖန်တီးမှုဆိုင်ရာ အလုပ်များ** (ဥပမာ- ပုံမှန်စာသားဖန်တီးခြင်း၊ စက်ဖြင့်ဘာသာပြန်ခြင်း၊ ပုံအကြောင်းဖော်ပြချက်ရေးခြင်း) အတွက် အသုံးပြုနိုင်ပါသည်။

> ✅ သင်ရိုက်နေစဉ် စာသားဖြည့်စွက်မှုကဲ့သို့သော ဖန်တီးမှုဆိုင်ရာ အလုပ်များမှ သင်ရရှိခဲ့သော အကျိုးကျေးဇူးများကို စဉ်းစားကြည့်ပါ။ သင်နှစ်သက်သော အက်ပ်လီကေးရှင်းများတွင် RNNs ကို အသုံးပြုထားမရှိစစ်ဆေးရန် သုတေသနပြုပါ။

ယခင်ယူနစ်တွင် ဆွေးနွေးခဲ့သော RNN အဆောက်အအုံတွင် RNN unit တစ်ခုစီသည် နောက်ထပ် hidden state ကို output အဖြစ် ထုတ်ပေးပါသည်။ သို့သော်လည်း RNN unit တစ်ခုစီတွင် ထပ်မံ output တစ်ခု ထည့်သွင်းနိုင်ပြီး ၎င်းသည် **sequence** (မူလ sequence နှင့် အရှည်တူညီသော) ကို ထုတ်ပေးနိုင်ပါသည်။ ထို့အပြင် RNN units များကို အဆင့်တိုင်းတွင် input မလိုအပ်ဘဲ အစအနေအနေအထား vector တစ်ခုသာ လက်ခံပြီး output sequence များကို ထုတ်ပေးနိုင်ပါသည်။

ဤအရာသည် အောက်ပါပုံတွင် ဖော်ပြထားသည့် မတူကွဲပြားသော နယူးရယ်အဆောက်အအုံများကို ဖန်တီးနိုင်စေပါသည်-

![Image showing common recurrent neural network patterns.](../../../../../translated_images/unreasonable-effectiveness-of-rnn.541ead816778f42dce6c42d8a56c184729aa2378d059b851be4ce12b993033df.my.jpg)

> ပုံကို [Andrej Karpaty](http://karpathy.github.io/) ၏ [Unreasonable Effectiveness of Recurrent Neural Networks](http://karpathy.github.io/2015/05/21/rnn-effectiveness/) ဆိုသော ဘလော့ဂ်မှ ယူဆောင်ထားပါသည်။

* **One-to-one** သည် input တစ်ခုနှင့် output တစ်ခုသာရှိသော ရိုးရိုးနယူးရယ်ကွန်ရက်ဖြစ်သည်။
* **One-to-many** သည် input တန်ဖိုးတစ်ခုကို လက်ခံပြီး output တန်ဖိုးများ၏ အစီအစဉ်တစ်ခုကို ဖန်တီးပေးသော ဖန်တီးမှုဆိုင်ရာ အဆောက်အအုံဖြစ်သည်။ ဥပမာအားဖြင့် **ပုံအကြောင်းဖော်ပြချက်ရေးခြင်း** network ကို သင်ယူလိုပါက ပုံတစ်ပုံကို input အဖြစ်ထည့်သွင်းပြီး CNN မှ hidden state ကို ရယူကာ RNN chain မှ စကားလုံးတစ်လုံးချင်းစီဖြင့် ဖော်ပြချက်ကို ဖန်တီးနိုင်ပါသည်။
* **Many-to-one** သည် ယခင်ယူနစ်တွင် ဖော်ပြခဲ့သော RNN အဆောက်အအုံများ (ဥပမာ- စာသားအမျိုးအစားခွဲခြားခြင်း) ကို ကိုယ်စားပြုသည်။
* **Many-to-many** သို့မဟုတ် **sequence-to-sequence** သည် **စက်ဖြင့်ဘာသာပြန်ခြင်း** ကဲ့သို့သော အလုပ်များကို ကိုယ်စားပြုသည်။ ဤတွင် ပထမ RNN သည် input sequence မှ hidden state ကို စုဆောင်းပြီး နောက်ထပ် RNN chain မှ hidden state ကို output sequence အဖြစ် ပြန်လည်ဖော်ထုတ်သည်။

ဤယူနစ်တွင် စာသားဖန်တီးရန် အထောက်အကူပြုသော ရိုးရှင်းသော ဖန်တီးမှုမော်ဒယ်များကို အဓိကထားလေ့လာမည်ဖြစ်သည်။ ရိုးရှင်းစွာဖော်ပြရန် character-level tokenization ကို အသုံးပြုမည်ဖြစ်သည်။

ဤ RNN ကို စာသားကို အဆင့်ဆင့်ဖန်တီးရန် သင်ကြားမည်ဖြစ်သည်။ အဆင့်တစ်ခုစီတွင် `nchars` အရှည်ရှိသော စာလုံးများ၏ အစီအစဉ်ကို ယူပြီး input character တစ်ခုစီအတွက် နောက်တစ်ခုလာမည့် output character ကို ဖန်တီးရန် network ကို မေးမြန်းမည်ဖြစ်သည်-

![Image showing an example RNN generation of the word 'HELLO'.](../../../../../translated_images/rnn-generate.56c54afb52f9781d63a7c16ea9c1b86cb70e6e1eae6a742b56b7b37468576b17.my.png)

စာသားဖန်တီးရာတွင် (inference အဆင့်တွင်) **prompt** တစ်ခုကို RNN cells မှတဆင့် hidden state ကို ဖန်တီးပြီး ထို state မှ စတင်ဖန်တီးသည်။ စာလုံးတစ်လုံးစီကို အဆင့်ဆင့်ဖန်တီးကာ state နှင့် ဖန်တီးထားသော စာလုံးကို နောက်ထပ် RNN cell သို့ ပေးပို့ပြီး နောက်တစ်လုံးကို ဖန်တီးသည်။ ဤလုပ်ငန်းစဉ်ကို လိုအပ်သလောက် စာလုံးများ ဖန်တီးသည်အထိ ဆက်လက်လုပ်ဆောင်သည်။

<img src="images/rnn-generate-inf.png" width="60%"/>

> ပုံကို စာရေးသူမှ ဖန်တီးထားပါသည်။

## ✍️ Exercises: Generative Networks

အောက်ပါ notebooks များတွင် သင်ကြားမှုကို ဆက်လက်လေ့လာပါ-

* [Generative Networks with PyTorch](../../../../../lessons/5-NLP/17-GenerativeNetworks/GenerativePyTorch.ipynb)
* [Generative Networks with TensorFlow](../../../../../lessons/5-NLP/17-GenerativeNetworks/GenerativeTF.ipynb)

## Soft text generation and temperature

RNN cell တစ်ခုစီ၏ output သည် စာလုံးများ၏ probability distribution ဖြစ်သည်။ generated text တွင် နောက်တစ်လုံးလာမည့် စာလုံးအဖြစ် အမြင့်ဆုံး probability ရှိသော စာလုံးကိုသာ အမြဲရွေးချယ်ပါက စာသားသည် အချို့သော စာလုံးအစီအစဉ်များကို ထပ်ခါထပ်ခါ ပြန်လည်ဖန်တီးသည့် "cycled" ဖြစ်နိုင်ပါသည်။ ဥပမာအားဖြင့်-

```
today of the second the company and a second the company ...
```

သို့သော် probability distribution ကို ကြည့်ပါက အမြင့်ဆုံး probability ရှိသော စာလုံးနှင့် ဒုတိယမြင့်ဆုံး probability ရှိသော စာလုံးကြားကွာဟချက်သည် များစွာမရှိနိုင်ပါ။ ဥပမာအားဖြင့် '*play*' sequence တွင် နောက်တစ်လုံးလာမည့် စာလုံးသည် space သို့မဟုတ် **e** (ဥပမာ- *player*) ဖြစ်နိုင်ပါသည်။

ထို့ကြောင့် အမြင့်ဆုံး probability ရှိသော စာလုံးကိုသာ ရွေးချယ်ခြင်းသည် အမြဲတမ်း "တရားမျှတ" မဖြစ်နိုင်ပါ။ ဒုတိယမြင့်ဆုံး probability ရှိသော စာလုံးကို ရွေးချယ်ခြင်းသည်လည်း အဓိပ္ပာယ်ရှိသော စာသားကို ဖန်တီးနိုင်ပါသည်။ ထို့ကြောင့် network output မှ probability distribution ကို အသုံးပြု၍ စာလုံးများကို **sample** လုပ်ခြင်းသည် ပိုမိုလျှောက်လွှာဖြစ်သည်။ ထို့အပြင် **temperature** ဟုခေါ်သော parameter ကို အသုံးပြု၍ probability distribution ကို ပိုမို random ဖြစ်စေခြင်း (သို့မဟုတ်) အမြင့်ဆုံး probability ရှိသော စာလုံးများကို ပိုမိုရွေးချယ်စေခြင်းတို့ကို ပြုလုပ်နိုင်ပါသည်။

ဤ soft text generation ကို အထက်ပါ notebooks များတွင် လေ့လာပါ။

## Conclusion

စာသားဖန်တီးခြင်းသည် ကိုယ်တိုင်အသုံးဝင်နိုင်သော်လည်း RNNs ကို အသုံးပြု၍ အစအနေအနေအထား vector တစ်ခုမှ စာသားဖန်တီးနိုင်စွမ်းသည် အဓိကအားသာချက်ဖြစ်သည်။ ဥပမာအားဖြင့် စာသားဖန်တီးခြင်းကို စက်ဖြင့်ဘာသာပြန်ခြင်း (sequence-to-sequence, ဤတွင် *encoder* မှ state vector ကို အသုံးပြု၍ *decode* ပြုလုပ်သည်) သို့မဟုတ် ပုံ၏ စာသားဖော်ပြချက်ဖန်တီးခြင်း (ဤတွင် feature vector ကို CNN extractor မှ ရယူသည်) အတွက် အသုံးပြုနိုင်ပါသည်။

## 🚀 Challenge

Microsoft Learn တွင် ဤအကြောင်းအရာနှင့်ပတ်သက်သော သင်ခန်းစာများကို လေ့လာပါ-

* [PyTorch](https://docs.microsoft.com/learn/modules/intro-natural-language-processing-pytorch/6-generative-networks/?WT.mc_id=academic-77998-cacaste) / [TensorFlow](https://docs.microsoft.com/learn/modules/intro-natural-language-processing-tensorflow/5-generative-networks/?WT.mc_id=academic-77998-cacaste) ဖြင့် စာသားဖန်တီးခြင်း

## [Post-lecture quiz](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/217)

## Review & Self Study

သင့်ရဲ့ အသိပညာကို တိုးချဲ့ရန် အောက်ပါဆောင်းပါးများကို ဖတ်ရှုပါ-

* Markov Chain, LSTM နှင့် GPT-2 ဖြင့် စာသားဖန်တီးခြင်းအတွက် မတူကွဲပြားသော နည်းလမ်းများ: [blog post](https://towardsdatascience.com/text-generation-gpt-2-lstm-markov-chain-9ea371820e1e)
* [Keras documentation](https://keras.io/examples/generative/lstm_character_level_text_generation/) တွင် စာသားဖန်တီးမှုနမူနာ

## [Assignment](lab/README.md)

စာလုံးတစ်လုံးချင်းစီဖြင့် စာသားဖန်တီးပုံကို ကြည့်ရှုခဲ့ပါသည်။ lab တွင် စကားလုံးအဆင့်စာသားဖန်တီးမှုကို လေ့လာပါ။

**အကြောင်းကြားချက်**:  
ဤစာရွက်စာတမ်းကို AI ဘာသာပြန်ဝန်ဆောင်မှု [Co-op Translator](https://github.com/Azure/co-op-translator) ကို အသုံးပြု၍ ဘာသာပြန်ထားပါသည်။ ကျွန်ုပ်တို့သည် တိကျမှုအတွက် ကြိုးစားနေပါသော်လည်း၊ အလိုအလျောက် ဘာသာပြန်မှုများတွင် အမှားများ သို့မဟုတ် မမှန်ကန်မှုများ ပါဝင်နိုင်သည်ကို သတိပြုပါ။ မူရင်းစာရွက်စာတမ်းကို ၎င်း၏ မူလဘာသာစကားဖြင့် အာဏာတရ အရင်းအမြစ်အဖြစ် သတ်မှတ်သင့်ပါသည်။ အရေးကြီးသော အချက်အလက်များအတွက် လူ့ဘာသာပြန်ပညာရှင်များမှ ပရော်ဖက်ရှင်နယ် ဘာသာပြန်မှုကို အကြံပြုပါသည်။ ဤဘာသာပြန်မှုကို အသုံးပြုခြင်းမှ ဖြစ်ပေါ်လာသော အလွဲအမှားများ သို့မဟုတ် အနားလွဲမှုများအတွက် ကျွန်ုပ်တို့သည် တာဝန်မယူပါ။