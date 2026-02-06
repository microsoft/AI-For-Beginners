# ကြိုတင်လေ့ကျင့်ထားသော အကြီးစားဘာသာစကားမော်ဒယ်များ

ယခင်အလုပ်များအားလုံးတွင် ကျွန်ုပ်တို့သည် အမှတ်အသားပြုထားသော ဒေတာအစုအဝေးကို အသုံးပြု၍ neural network ကို သတ်မှတ်ထားသော အလုပ်တစ်ခုကို လုပ်ဆောင်ရန် လေ့ကျင့်နေခဲ့သည်။ BERT ကဲ့သို့သော အကြီးစား transformer မော်ဒယ်များတွင် self-supervised နည်းလမ်းဖြင့် ဘာသာစကားမော်ဒယ်တစ်ခုကို တည်ဆောက်ရန် language modelling ကို အသုံးပြုသည်။ ထို့နောက် အထူးသဖြင့် domain-specific လေ့ကျင့်မှုများဖြင့် အထူးပြုထားသော downstream task များအတွက် အသုံးပြုသည်။ သို့သော် အကြီးစားဘာသာစကားမော်ဒယ်များသည် domain-specific လေ့ကျင့်မှုမရှိဘဲ အလုပ်များစွာကို ဖြေရှင်းနိုင်သည်ဟု သက်သေပြထားသည်။ အလုပ်များစွာကို လုပ်ဆောင်နိုင်သော မော်ဒယ်များ၏ မိသားစုကို **GPT** (Generative Pre-Trained Transformer) ဟုခေါ်သည်။

## [Pre-lecture quiz](https://ff-quizzes.netlify.app/en/ai/quiz/39)

## စာသားထုတ်လုပ်ခြင်းနှင့် Perplexity

Downstream လေ့ကျင့်မှုမရှိဘဲ neural network တစ်ခုသည် အထွေထွေအလုပ်များကို လုပ်ဆောင်နိုင်သည်ဆိုသော အယူအဆကို [Language Models are Unsupervised Multitask Learners](https://cdn.openai.com/better-language-models/language_models_are_unsupervised_multitask_learners.pdf) စာတမ်းတွင် ဖော်ပြထားသည်။ အဓိကအယူအဆမှာ အခြားသော အလုပ်များစွာကို **စာသားထုတ်လုပ်ခြင်း** ဖြင့် မော်ဒယ်နိုင်သည်ဟု ဆိုသည်။ အကြောင်းမှာ စာသားကို နားလည်ခြင်းသည် စာသားကို ထုတ်လုပ်နိုင်ခြင်းကို အဓိကထားသည်။ မော်ဒယ်သည် လူသားများ၏ အသိပညာကို ပါဝင်သော စာသားအကြီးစားအစုအဝေးပေါ်တွင် လေ့ကျင့်ထားသောကြောင့် အကြောင်းအရာများစွာကိုလည်း သိရှိလာသည်။

> စာသားကို နားလည်ပြီး ထုတ်လုပ်နိုင်ခြင်းသည် ပတ်ဝန်းကျင်အကြောင်းကို သိရှိထားခြင်းကိုလည်း အဓိကထားသည်။ လူများသည် စာဖတ်ခြင်းမှတစ်ဆင့် အများကြီးလေ့လာကြပြီး GPT network သည် ထိုနည်းလမ်းနှင့် ဆင်တူသည်။

စာသားထုတ်လုပ်မော်ဒယ်များသည် နောက်ထပ်စကားလုံး၏ probability $$P(w_N)$$ ကို ခန့်မှန်းခြင်းဖြင့် အလုပ်လုပ်သည်။ သို့သော် နောက်ထပ်စကားလုံး၏ unconditional probability သည် စာသားအစုအဝေးတွင် စကားလုံး၏ frequency နှင့် တူညီသည်။ GPT သည် နောက်ထပ်စကားလုံး၏ **conditional probability** ကို ပေးနိုင်သည်၊ ယခင်စကားလုံးများကို အခြေခံ၍ $$P(w_N | w_{n-1}, ..., w_0)$$

> Probability များအကြောင်းကို ကျွန်ုပ်တို့၏ [Data Science for Beginners Curriculum](https://github.com/microsoft/Data-Science-For-Beginners/tree/main/1-Introduction/04-stats-and-probability) တွင် ပိုမိုဖတ်ရှုနိုင်ပါသည်။

ဘာသာစကားထုတ်လုပ်မော်ဒယ်၏ အရည်အသွေးကို **perplexity** ဖြင့် သတ်မှတ်နိုင်သည်။ ၎င်းသည် task-specific dataset မလိုအပ်ဘဲ မော်ဒယ်အရည်အသွေးကို တိုင်းတာနိုင်သော intrinsic metric ဖြစ်သည်။ ၎င်းသည် *probability of a sentence* အယူအဆပေါ် အခြေခံသည် - မော်ဒယ်သည် အမှန်ဖြစ်နိုင်သော စာကြောင်းများကို (မော်ဒယ်သည် **perplexed** မဖြစ်သော) probability မြင့်မားစွာ သတ်မှတ်ပြီး အဓိပ္ပါယ်မရှိသော စာကြောင်းများကို (ဥပမာ *Can it does what?*) probability နိမ့်စွာ သတ်မှတ်သည်။ မော်ဒယ်ကို အမှန်တကယ်စာသားအစုအဝေးမှ စာကြောင်းများပေးသောအခါ ၎င်းတို့သည် probability မြင့်မားပြီး **perplexity** နိမ့်စွာ ရှိရန် မျှော်လင့်ရမည်။ သင်္ချာအရ ၎င်းကို test set ၏ normalized inverse probability အဖြစ် သတ်မှတ်သည်။
$$
\mathrm{Perplexity}(W) = \sqrt[N]{1\over P(W_1,...,W_N)}
$$ 

**[Hugging Face မှ GPT-powered text editor](https://transformer.huggingface.co/doc/gpt2-large)** ကို အသုံးပြု၍ စာသားထုတ်လုပ်မှုကို စမ်းသပ်နိုင်ပါသည်။ ဤ editor တွင် သင်၏ စာသားကို စတင်ရေးသားပြီး **[TAB]** ကို နှိပ်ပါက အချို့သော အပြီးသတ်ရွေးချယ်မှုများကို ပေးပါမည်။ ၎င်းတို့သည် အလွန်တိုသို့မဟုတ် သင်မကျေနပ်ပါက - [TAB] ကို ထပ်မံနှိပ်ပါက အရွေးချယ်မှုများ ပိုမိုရရှိမည်ဖြစ်ပြီး အရှည်ပိုင်းစာသားများပါဝင်နိုင်သည်။

## GPT သည် မိသားစုတစ်ခုဖြစ်သည်

GPT သည် တစ်ခုတည်းသော မော်ဒယ်မဟုတ်ပါ၊ [OpenAI](https://openai.com) မှ ဖွံ့ဖြိုးပြီး လေ့ကျင့်ထားသော မော်ဒယ်များစုစည်းမှုဖြစ်သည်။

GPT မော်ဒယ်များအောက်တွင် -

| [GPT-2](https://huggingface.co/docs/transformers/model_doc/gpt2#openai-gpt2) | [GPT 3](https://openai.com/research/language-models-are-few-shot-learners) | [GPT-4](https://openai.com/gpt-4) |
| -- | -- | -- |
|Language model with upto 1.5 billion parameters. | Language model with up to 175 billion parameters | 100T parameters and accepts both image and text inputs and outputs text. |

GPT-3 နှင့် GPT-4 မော်ဒယ်များကို [Microsoft Azure မှ cognitive service](https://azure.microsoft.com/en-us/services/cognitive-services/openai-service/#overview?WT.mc_id=academic-77998-cacaste) အဖြစ်နှင့် [OpenAI API](https://openai.com/api/) အဖြစ် ရရှိနိုင်ပါသည်။

## Prompt Engineering

GPT သည် စကားလုံးနှင့် code ကို နားလည်ရန် အကြီးစားဒေတာများပေါ်တွင် လေ့ကျင့်ထားသောကြောင့် input (prompt) များကို ဖြေကြားပေးသည်။ Prompt များသည် GPT input သို့မဟုတ် query များဖြစ်ပြီး မော်ဒယ်များကို လုပ်ဆောင်ရန် အလုပ်အကိုင်များအတွက် အညွှန်းပေးသည်။ မိမိလိုအပ်သော ရလဒ်ကို ရရှိရန် အကျိုးရှိဆုံး prompt ကို ရွေးချယ်ရန် လိုအပ်ပြီး ၎င်းတွင် စကားလုံးများ၊ format များ၊ phrase များ သို့မဟုတ် သင်္ကေတများကို ရွေးချယ်ခြင်းပါဝင်သည်။ ဤနည်းလမ်းကို [Prompt Engineering](https://learn.microsoft.com/en-us/shows/ai-show/the-basics-of-prompt-engineering-with-azure-openai-service?WT.mc_id=academic-77998-bethanycheum) ဟုခေါ်သည်။

[ဤ documentation](https://learn.microsoft.com/en-us/semantic-kernel/prompt-engineering/?WT.mc_id=academic-77998-bethanycheum) တွင် prompt engineering အကြောင်းပိုမိုသိရှိနိုင်ပါသည်။

## ✍️ နမူနာ Notebook: [Playing with OpenAI-GPT](GPT-PyTorch.ipynb)

အောက်ပါ notebook များတွင် သင့်လေ့လာမှုကို ဆက်လက်လုပ်ဆောင်ပါ-

* [Generating text with OpenAI-GPT and Hugging Face Transformers](GPT-PyTorch.ipynb)

## နိဂုံး

အသစ်သော general pre-trained language models များသည် ဘာသာစကားဖွဲ့စည်းမှုကိုသာမက သဘာဝဘာသာစကားအကြီးစားကိုလည်း မော်ဒယ်နိုင်သည်။ ထို့ကြောင့် zero-shot သို့မဟုတ် few-shot settings တွင် NLP အလုပ်များကို ထိရောက်စွာ ဖြေရှင်းနိုင်သည်။

## [Post-lecture quiz](https://ff-quizzes.netlify.app/en/ai/quiz/40)

---

