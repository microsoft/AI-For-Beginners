# Language Modeling

Semantic embeddings, Word2Vec နှင့် GloVe က **ဘာသာစကားမော်ဒယ်** ဖန်တီးခြင်းဆီသို့ ပထမအဆင့်အဖြစ် သွားရောက်နေသည်။ ၎င်းသည် ဘာသာစကား၏ သဘာဝကို *နားလည်* (သို့မဟုတ် *ကိုယ်စားပြု*) နိုင်သော မော်ဒယ်များ ဖန်တီးရန် ရည်ရွယ်သည်။

## [Pre-lecture quiz](https://ff-quizzes.netlify.app/en/ai/quiz/29)

ဘာသာစကားမော်ဒယ်ဖန်တီးခြင်း၏ အဓိကအကြောင်းအရာမှာ မော်ဒယ်များကို မမှတ်သားထားသော ဒေတာများပေါ်တွင် unsupervised နည်းလမ်းဖြင့် လေ့ကျင့်ခြင်းဖြစ်သည်။ ၎င်းသည် အရေးကြီးသည်မှာ မမှတ်သားထားသော စာသားများ အလွန်များစွာ ရရှိနိုင်သည့်အတွက်ဖြစ်ပြီး၊ မှတ်သားထားသော စာသားများသည် ကျွန်ုပ်တို့မှတ်သားရန် အချိန်နှင့် အင်အားကန့်သတ်ထားသောကြောင့် အမြဲကန့်သတ်ထားလိမ့်မည်။ အများအားဖြင့် မော်ဒယ်များကို **ပျောက်နေသော စကားလုံးများ** ခန့်မှန်းနိုင်ရန် ဖန်တီးနိုင်သည်။ ၎င်းသည် စာသားတွင် စိတ်ကြိုက် စကားလုံးတစ်လုံးကို ဖျောက်ထားပြီး ၎င်းကို လေ့ကျင့်မှုနမူနာအဖြစ် အသုံးပြုရန် လွယ်ကူသောကြောင့်ဖြစ်သည်။

## Training Embeddings

ယခင် ဥပမာများတွင် ကျွန်ုပ်တို့သည် pre-trained semantic embeddings ကို အသုံးပြုခဲ့သည်။ သို့သော် ၎င်းတို့ကို မည်သို့လေ့ကျင့်နိုင်သည်ကို သိရန် စိတ်ဝင်စားဖွယ်ကောင်းသည်။ အသုံးပြုနိုင်သော အကြံဉာဏ်အချို့မှာ:

* **N-Gram** ဘာသာစကားမော်ဒယ်ဖန်တီးခြင်း၊ N-Gram ကို အသုံးပြု၍ ယခင် token များကို ကြည့်ပြီး token တစ်ခုကို ခန့်မှန်းခြင်း။
* **Continuous Bag-of-Words** (CBoW)၊ token အစဉ် $W_{-N}$, ..., $W_N$ တွင် အလယ် token $W_0$ ကို ခန့်မှန်းခြင်း။
* **Skip-gram**၊ အလယ် token $W_0$ မှ အနီးအနား token များ {$W_{-N},\dots, W_{-1}, W_1,\dots, W_N$} ကို ခန့်မှန်းခြင်း။

![image from paper on converting words to vectors](../../../../../translated_images/my/example-algorithms-for-converting-words-to-vectors.fbe9207a726922f6.webp)

> Image from [this paper](https://arxiv.org/pdf/1301.3781.pdf)

## ✍️ Example Notebooks: Training CBoW model

အောက်ပါ notebooks များတွင် သင့်လေ့လာမှုကို ဆက်လက်လုပ်ဆောင်ပါ:

* [Training CBoW Word2Vec with TensorFlow](CBoW-TF.ipynb)
* [Training CBoW Word2Vec with PyTorch](CBoW-PyTorch.ipynb)

## Conclusion

ယခင် သင်ခန်းစာတွင် စကားလုံး embeddings များသည် မျိုးစုံသော အကျိုးကျေးဇူးများရှိသည်ကို ကျွန်ုပ်တို့တွေ့ရှိခဲ့သည်! ယခု ကျွန်ုပ်တို့သည် စကားလုံး embeddings များကို လေ့ကျင့်ခြင်းသည် အလွန်ရှုပ်ထွေးသော အလုပ်မဟုတ်ကြောင်း သိရှိပြီး၊ domain-specific စာသားများအတွက် လိုအပ်ပါက ကျွန်ုပ်တို့ကိုယ်တိုင် စကားလုံး embeddings များကို လေ့ကျင့်နိုင်သည်။

## [Post-lecture quiz](https://ff-quizzes.netlify.app/en/ai/quiz/30)

## Review & Self Study

* [Official PyTorch tutorial on Language Modeling](https://pytorch.org/tutorials/beginner/nlp/word_embeddings_tutorial.html)။
* [Official TensorFlow tutorial on training Word2Vec model](https://www.TensorFlow.org/tutorials/text/word2vec)။
* **gensim** framework ကို အသုံးပြု၍ အများဆုံးအသုံးပြုသော embeddings များကို အနည်းငယ်သော code ဖြင့် လေ့ကျင့်ခြင်းကို [ဤစာရွက်စာတမ်း](https://pytorch.org/tutorials/beginner/nlp/word_embeddings_tutorial.html) တွင် ဖော်ပြထားသည်။

## 🚀 [Assignment: Train Skip-Gram Model](lab/README.md)

Lab တွင် ကျွန်ုပ်တို့သည် CBoW မော်ဒယ်ကို Skip-gram မော်ဒယ်အဖြစ် ပြောင်းလဲရန် ဤသင်ခန်းစာမှ code ကို ပြင်ဆင်ရန် စိန်ခေါ်ပါသည်။ [အသေးစိတ်ဖတ်ရှုပါ](lab/README.md)

---

