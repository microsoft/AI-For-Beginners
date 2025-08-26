<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "e40b47ac3fd48f71304ede1474e66293",
  "translation_date": "2025-08-25T21:41:43+00:00",
  "source_file": "lessons/5-NLP/14-Embeddings/README.md",
  "language_code": "my"
}
-->
# Embeddings

## [Pre-lecture quiz](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/114)

BoW သို့မဟုတ် TF/IDF အခြေခံထားသော classifier များကို သင်ကြားသင့်သောအခါတွင် `vocab_size` အရှည်ရှိသော အမြင့် dimension bag-of-words vectors များကို အသုံးပြုခဲ့ပြီး၊ အနိမ့် dimension positional representation vectors များမှ sparse one-hot representation သို့ အတိအကျပြောင်းလဲခဲ့သည်။ သို့သော် one-hot representation သည် memory ကို ထိရောက်စွာ အသုံးမပြုနိုင်ပါ။ ထို့အပြင်၊ စကားလုံးတစ်လုံးချင်းစီကို တစ်ခုချင်းစီ သီးခြားစီဆက်ဆံသည်၊ ဤအနေအထားတွင် one-hot encoded vectors များသည် စကားလုံးများအကြား semantic ဆက်စပ်မှုကို မဖော်ပြနိုင်ပါ။

**Embedding** ဆိုသည်မှာ စကားလုံးများကို အနိမ့် dimension dense vectors များဖြင့် ကိုယ်စားပြုရန်အယူအဆဖြစ်ပြီး၊ စကားလုံးတစ်လုံး၏ semantic အဓိပ္ပါယ်ကို တစ်နည်းနည်းဖြင့် ရှင်းလင်းဖော်ပြသည်။ စကားလုံး embedding များကို ဘယ်လိုဖန်တီးရမည်ကို နောက်ပိုင်းတွင် ဆွေးနွေးမည်ဖြစ်သော်လည်း၊ ယခုအချိန်တွင် embedding များကို စကားလုံး vector ၏ dimension ကို လျှော့ချရန် နည်းလမ်းတစ်ခုအဖြစ်သာ စဉ်းစားပါ။

ထို့ကြောင့် embedding layer သည် စကားလုံးတစ်လုံးကို input အဖြစ်ယူပြီး၊ သတ်မှတ်ထားသော `embedding_size` output vector ကို ထုတ်ပေးမည်ဖြစ်သည်။ တစ်နည်းအားဖြင့်၊ ၎င်းသည် `Linear` layer နှင့် အလွန်ဆင်တူသည်၊ သို့သော် one-hot encoded vector ကို မယူဘဲ၊ စကားလုံးနံပါတ်ကို input အဖြစ်ယူနိုင်မည်ဖြစ်ပြီး၊ အကြီးမားသော one-hot-encoded vectors များ ဖန်တီးရန် မလိုအပ်တော့ပါ။

Classifier network ၏ ပထမဆုံး layer အဖြစ် embedding layer ကို အသုံးပြုခြင်းဖြင့်၊ bag-of-words မှ **embedding bag** မော်ဒယ်သို့ ပြောင်းလဲနိုင်ပြီး၊ ကျွန်ုပ်တို့၏ စာသားအတွင်းရှိ စကားလုံးတစ်လုံးချင်းစီကို သက်ဆိုင်ရာ embedding သို့ ပထမဆုံး ပြောင်းလဲပြီး၊ ထို့နောက် `sum`၊ `average` သို့မဟုတ် `max` ကဲ့သို့သော aggregate function တစ်ခုကို အဲဒီ embedding များအားလုံးအပေါ်တွင် တွက်ချက်နိုင်သည်။

![Image showing an embedding classifier for five sequence words.](../../../../../translated_images/embedding-classifier-example.b77f021a7ee67eeec8e68bfe11636c5b97d6eaa067515a129bfb1d0034b1ac5b.my.png)

> ပုံကို စာရေးသူမှ ဖန်တီးသည်

## ✍️ လေ့ကျင့်မှုများ: Embeddings

အောက်ပါ notebooks များတွင် သင့်လေ့လာမှုကို ဆက်လက်လုပ်ဆောင်ပါ:
* [Embeddings with PyTorch](../../../../../lessons/5-NLP/14-Embeddings/EmbeddingsPyTorch.ipynb)
* [Embeddings TensorFlow](../../../../../lessons/5-NLP/14-Embeddings/EmbeddingsTF.ipynb)

## Semantic Embeddings: Word2Vec

Embedding layer သည် စကားလုံးများကို vector representation သို့ map လုပ်ရန် သင်ကြားခဲ့သော်လည်း၊ ၎င်း representation သည် အဓိပ္ပါယ်ဆိုင်ရာ အနက်အဓိပ္ပါယ်များကို မရှိမဖြစ် ဖော်ပြထားသည်မဟုတ်ပါ။ စကားလုံးများနှင့် အနီးကပ်ဆက်စပ်မှုရှိသော vector distance (ဥပမာ Euclidean distance) အရ၊ ဆင်တူသော စကားလုံးများ သို့မဟုတ် အဓိပ္ပါယ်တူများကို နီးကပ်သော vectors အဖြစ် ကိုယ်စားပြုနိုင်မည့် vector representation ကို သင်ကြားနိုင်ရမည်ဖြစ်သည်။

ဤအတွက်၊ စကားလုံး embedding မော်ဒယ်ကို စာသားအစုကြီးတစ်ခုအပေါ်တွင် သီးခြားနည်းလမ်းဖြင့် pre-train လုပ်ရန် လိုအပ်သည်။ Semantic embeddings များကို သင်ကြားရန် နည်းလမ်းတစ်ခုမှာ [Word2Vec](https://en.wikipedia.org/wiki/Word2vec) ဟုခေါ်သည်။ ၎င်းသည် စကားလုံးများ၏ distributed representation ကို ထုတ်လုပ်ရန် အသုံးပြုသော အဓိက architecture နှစ်ခုအပေါ် အခြေခံသည်။

 - **Continuous bag-of-words** (CBoW) — ဤ architecture တွင်၊ မော်ဒယ်ကို context ပတ်ဝန်းကျင်မှ စကားလုံးကို ခန့်မှန်းရန် သင်ကြားသည်။ ngram $(W_{-2},W_{-1},W_0,W_1,W_2)$ ကို ပေးထားပါက၊ မော်ဒယ်၏ ရည်မှန်းချက်မှာ $(W_{-2},W_{-1},W_1,W_2)$ မှ $W_0$ ကို ခန့်မှန်းရန်ဖြစ်သည်။
 - **Continuous skip-gram** သည် CBoW ၏ ဆန့်ကျင်ဘက်ဖြစ်သည်။ မော်ဒယ်သည် context စကားလုံးများ၏ window ကို အသုံးပြု၍ လက်ရှိစကားလုံးကို ခန့်မှန်းသည်။

CBoW သည် ပိုမြန်သော်လည်း၊ skip-gram သည် ပိုနှေးပြီး၊ မကြာခဏမတွေ့သော စကားလုံးများကို ကိုယ်စားပြုရာတွင် ပိုကောင်းသည်။

![Image showing both CBoW and Skip-Gram algorithms to convert words to vectors.](../../../../../translated_images/example-algorithms-for-converting-words-to-vectors.fbe9207a726922f6f0f5de66427e8a6eda63809356114e28fb1fa5f4a83ebda7.my.png)

> ပုံကို [ဤစာတမ်း](https://arxiv.org/pdf/1301.3781.pdf) မှ ယူဆောင်သည်

Word2Vec pre-trained embeddings (GloVe ကဲ့သို့သော အခြားမော်ဒယ်များနှင့်အတူ) ကို neural networks တွင် embedding layer အဖြစ် အသုံးပြုနိုင်သည်။ သို့သော် vocabularies ကို စီမံခန့်ခွဲရန် လိုအပ်သည်၊ အကြောင်းမှာ Word2Vec/GloVe ကို pre-train လုပ်ရန် အသုံးပြုသော vocabulary သည် ကျွန်ုပ်တို့၏ စာသား corpus ၏ vocabulary နှင့် မတူနိုင်ပါ။ ဤပြဿနာကို ဘယ်လိုဖြေရှင်းရမည်ကို အထက်ပါ Notebooks များတွင် ကြည့်ရှုပါ။

## Contextual Embeddings

Word2Vec ကဲ့သို့သော traditional pretrained embedding representations ၏ အဓိက ကန့်သတ်ချက်တစ်ခုမှာ စကားလုံးအဓိပ္ပါယ်များကို ရှင်းလင်းစွာ ခွဲခြားနိုင်မှု၏ ပြဿနာဖြစ်သည်။ Pretrained embeddings များသည် စကားလုံးများ၏ အဓိပ္ပါယ်ကို context အတွင်း ဖမ်းယူနိုင်သော်လည်း၊ စကားလုံးတစ်လုံး၏ အဓိပ္ပါယ်အားလုံးကို တစ်ခုတည်းသော embedding အတွင်း encode လုပ်ထားသည်။ ၎င်းသည် downstream မော်ဒယ်များတွင် ပြဿနာများ ဖြစ်စေနိုင်သည်၊ အကြောင်းမှာ စကားလုံးများ (ဥပမာ 'play') သည် အသုံးပြုသော context အပေါ်မူတည်၍ အဓိပ္ပါယ်ကွဲပြားမှုများ ရှိနိုင်သည်။

ဥပမာအားဖြင့် 'play' စကားလုံးသည် အောက်ပါ စာကြောင်းနှစ်ခုတွင် အဓိပ္ပါယ်ကွဲပြားမှုများ ရှိသည်-

- I went to a **play** at the theatre.
- John wants to **play** with his friends.

အထက်ပါ pretrained embeddings များသည် 'play' စကားလုံး၏ အဓိပ္ပါယ်နှစ်ခုလုံးကို တစ်ခုတည်းသော embedding အတွင်း ကိုယ်စားပြုထားသည်။ ဤကန့်သတ်ချက်ကို ကျော်လွှားရန်၊ စကားလုံးများကို အခြား context များတွင် ဘယ်လိုပေါင်းစပ်နိုင်သည်ကို *သိသော* **language model** အပေါ် အခြေခံထားသော embeddings များကို ဖန်တီးရန် လိုအပ်သည်။ Contextual embeddings များကို ဆွေးနွေးခြင်းသည် ဤသင်ခန်းစာ၏ အကျုံးအတွင်းမရှိသော်လည်း၊ သင်ခန်းစာ၏ နောက်ပိုင်းတွင် language models များကို ဆွေးနွေးသောအခါ ပြန်လည်ဆွေးနွေးမည်ဖြစ်သည်။

## အနှိပ်ချုပ်

ဤသင်ခန်းစာတွင်၊ TensorFlow နှင့် Pytorch တွင် embedding layers များကို ဖန်တီးခြင်းနှင့် အသုံးပြုခြင်းဖြင့် စကားလုံးများ၏ semantic အဓိပ္ပါယ်များကို ပိုမိုကောင်းမွန်စွာ ဖော်ပြနိုင်သည်ကို ရှာဖွေတွေ့ရှိခဲ့သည်။

## 🚀 စိန်ခေါ်မှု

Word2Vec ကို သီချင်းစာသားများနှင့် ကဗျာများ ဖန်တီးရန် အပါအဝင် စိတ်ဝင်စားဖွယ် အပလီကေးရှင်းများအတွက် အသုံးပြုခဲ့သည်။ [ဤဆောင်းပါး](https://www.politetype.com/blog/word2vec-color-poems) ကို ကြည့်ရှုပါ၊ ၎င်းတွင် စာရေးသူသည် Word2Vec ကို အသုံးပြု၍ ကဗျာများ ဖန်တီးပုံကို ရှင်းလင်းဖော်ပြထားသည်။ [Dan Shiffmann ၏ ဤဗီဒီယို](https://www.youtube.com/watch?v=LSS_bos_TPI&ab_channel=TheCodingTrain) ကိုလည်း ကြည့်ရှု၍ ဤနည်းလမ်း၏ အခြားရှင်းလင်းချက်တစ်ခုကို ရှာဖွေပါ။ ထို့နောက်၊ Kaggle မှ ရရှိနိုင်သော သင့်ကိုယ်ပိုင် စာသား corpus အပေါ်တွင် ဤနည်းလမ်းများကို လက်တွေ့အသုံးပြုကြည့်ပါ။

## [Post-lecture quiz](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/214)

## ပြန်လည်သုံးသပ်ခြင်းနှင့် ကိုယ်တိုင်လေ့လာခြင်း

Word2Vec အကြောင်း [Efficient Estimation of Word Representations in Vector Space](https://arxiv.org/pdf/1301.3781.pdf) စာတမ်းကို ဖတ်ရှုပါ။

## [Assignment: Notebooks](assignment.md)

**အကြောင်းကြားချက်**:  
ဤစာရွက်စာတမ်းကို AI ဘာသာပြန်ဝန်ဆောင်မှု [Co-op Translator](https://github.com/Azure/co-op-translator) ကို အသုံးပြု၍ ဘာသာပြန်ထားပါသည်။ ကျွန်ုပ်တို့သည် တိကျမှုအတွက် ကြိုးစားနေသော်လည်း၊ အလိုအလျောက် ဘာသာပြန်မှုများတွင် အမှားများ သို့မဟုတ် မမှန်ကန်မှုများ ပါဝင်နိုင်သည်ကို သတိပြုပါ။ မူရင်းစာရွက်စာတမ်းကို ၎င်း၏ မူရင်းဘာသာစကားဖြင့် အာဏာတရ အရင်းအမြစ်အဖြစ် သတ်မှတ်သင့်ပါသည်။ အရေးကြီးသော အချက်အလက်များအတွက် လူ့ဘာသာပြန်ပညာရှင်များမှ ပရော်ဖက်ရှင်နယ် ဘာသာပြန်မှုကို အကြံပြုပါသည်။ ဤဘာသာပြန်မှုကို အသုံးပြုခြင်းမှ ဖြစ်ပေါ်လာသော အလွဲအမှားများ သို့မဟုတ် အနားလွဲမှုများအတွက် ကျွန်ုပ်တို့သည် တာဝန်မယူပါ။