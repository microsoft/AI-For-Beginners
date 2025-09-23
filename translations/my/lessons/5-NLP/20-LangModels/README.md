<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "2efbb183384a50f0fc0cde02534d912f",
  "translation_date": "2025-08-25T22:09:37+00:00",
  "source_file": "lessons/5-NLP/20-LangModels/README.md",
  "language_code": "my"
}
-->
# ကြိုတင်လေ့ကျင့်ထားသော အကြီးစားဘာသာစကားမော်ဒယ်များ

ယခင်အလုပ်များအားလုံးတွင် ကျွန်ုပ်တို့သည် တိကျသောအလုပ်တစ်ခုကို ဆောင်ရွက်ရန်အတွက် အမှတ်အသားပြုထားသောဒေတာအစုတစ်ခုကို အသုံးပြု၍ နယူးရယ်နက်ဝက်ကို လေ့ကျင့်နေခဲ့သည်။ သို့သော် BERT ကဲ့သို့သော အကြီးစား Transformer မော်ဒယ်များတွင် ဘာသာစကားမော်ဒယ်တစ်ခုကို တည်ဆောက်ရန် Language Modelling ကို Self-Supervised နည်းလမ်းဖြင့် အသုံးပြုသည်။ ထို့နောက် အထူးပြုလေ့ကျင့်မှုများဖြင့် အထူးပြုလုပ်ထားသော Downstream Task များအတွက် အသုံးပြုသည်။ သို့သော်လည်း အကြီးစားဘာသာစကားမော်ဒယ်များသည် Domain-Specific Training မလိုဘဲ အလုပ်အမျိုးမျိုးကို ဖြေရှင်းနိုင်ကြောင်း သက်သေပြထားသည်။ ထိုသို့လုပ်ဆောင်နိုင်သော မော်ဒယ်များကို **GPT** (Generative Pre-Trained Transformer) ဟုခေါ်သည်။

## [Pre-lecture quiz](https://ff-quizzes.netlify.app/en/ai/quiz/39)

## စာသားထုတ်လုပ်ခြင်းနှင့် Perplexity

Downstream Training မလိုဘဲ အလုပ်များကို အထွေထွေကျကျ ဆောင်ရွက်နိုင်သော နယူးရယ်နက်ဝက်၏ အယူအဆကို [Language Models are Unsupervised Multitask Learners](https://cdn.openai.com/better-language-models/language_models_are_unsupervised_multitask_learners.pdf) စာတမ်းတွင် ဖော်ပြထားသည်။ အဓိကအယူအဆမှာ အခြားသောအလုပ်များစွာကို **စာသားထုတ်လုပ်ခြင်း** ဖြင့် မော်ဒယ်လုပ်နိုင်သည်ဟု ဆိုသည်။ အကြောင်းမှာ စာသားကို နားလည်ခြင်းသည် စာသားကို ထုတ်လုပ်နိုင်ခြင်းနှင့် ဆက်စပ်နေသည်။ မော်ဒယ်သည် လူ့အသိပညာပါဝင်သော စာသားအကြီးစားအစုအဝေးကို လေ့ကျင့်ထားသောကြောင့် အကြောင်းအရာအမျိုးမျိုးကိုလည်း သိရှိလာသည်။

> စာသားကို နားလည်ပြီး ထုတ်လုပ်နိုင်ခြင်းသည် ပတ်ဝန်းကျင်အကြောင်းကို သိရှိထားရမည်ဟု ဆိုလိုသည်။ လူများသည်လည်း စာဖတ်ခြင်းမှတစ်ဆင့် သိမြင်လာကြသည်။ GPT နက်ဝက်သည်လည်း ထိုနည်းတူပင်ဖြစ်သည်။

စာသားထုတ်လုပ်မော်ဒယ်များသည် နောက်တစ်လုံးသော စကားလုံး၏ ဖြစ်နိုင်ခြေကို ခန့်မှန်းခြင်းဖြင့် အလုပ်လုပ်သည် $$P(w_N)$$ သို့သော် စကားလုံးတစ်လုံး၏ Unconditional ဖြစ်နိုင်ခြေသည် စာသားအစုအဝေးတွင် စကားလုံး၏ မကြာခဏဖြစ်ပေါ်မှုနှုန်းနှင့် ညီမျှသည်။ GPT သည် ယခင်စကားလုံးများကို အခြေခံ၍ နောက်တစ်လုံးသော စကားလုံး၏ **Conditional ဖြစ်နိုင်ခြေ** ကို ပေးနိုင်သည် $$P(w_N | w_{n-1}, ..., w_0)$$

> ဖြစ်နိုင်ခြေများအကြောင်းကို ကျွန်ုပ်တို့၏ [Data Science for Beginners Curriculum](https://github.com/microsoft/Data-Science-For-Beginners/tree/main/1-Introduction/04-stats-and-probability) တွင် ပိုမိုလေ့လာနိုင်ပါသည်။

ဘာသာစကားထုတ်လုပ်မော်ဒယ်၏ အရည်အသွေးကို **Perplexity** ဖြင့် သတ်မှတ်နိုင်သည်။ ၎င်းသည် Task-Specific Dataset မလိုဘဲ မော်ဒယ်အရည်အသွေးကို တိုင်းတာနိုင်သော Intrinsic Metric တစ်ခုဖြစ်သည်။ ၎င်းသည် *စာကြောင်းတစ်ကြောင်း၏ ဖြစ်နိုင်ခြေ* အယူအဆအပေါ် အခြေခံထားသည်။ မော်ဒယ်သည် ဖြစ်နိုင်ခြေမြင့်သော စာကြောင်းများကို (ဥပမာ- အမှန်တကယ်ဖြစ်နိုင်သော စာကြောင်းများ) မြင့်မားသော ဖြစ်နိုင်ခြေ ပေးပြီး Perplexity နည်းသော စာကြောင်းများကို (ဥပမာ- *Can it does what?* ကဲ့သို့သော စာကြောင်းများ) နိမ့်သော ဖြစ်နိုင်ခြေ ပေးသည်။ စာသားအစုအဝေးမှ စာကြောင်းများကို မော်ဒယ်ထံပေးသောအခါ ၎င်းတို့သည် မြင့်မားသော ဖြစ်နိုင်ခြေနှင့် နိမ့်သော **Perplexity** ရှိရမည်ဟု မျှော်လင့်ရသည်။ သင်္ချာပိုင်းဆိုင်ရာအားဖြင့် ၎င်းကို စမ်းသပ်မှုအစုအဝေး၏ Normalized Inverse Probability အဖြစ် သတ်မှတ်ထားသည်။
$$
\mathrm{Perplexity}(W) = \sqrt[N]{1\over P(W_1,...,W_N)}
$$ 

**[Hugging Face မှ GPT-powered စာသားတည်းဖြတ်ရေးကိရိယာ](https://transformer.huggingface.co/doc/gpt2-large)** ကို အသုံးပြု၍ စာသားထုတ်လုပ်မှုကို စမ်းသပ်နိုင်ပါသည်။ ဤကိရိယာတွင် သင်၏ စာသားကို စတင်ရေးသားပြီး **[TAB]** ကို နှိပ်ပါက အချို့သော အပြီးသတ်ရွေးချယ်မှုများကို ပေးပါမည်။ ၎င်းတို့သည် တိုတောင်းလွန်းသည်ဟု သင်ထင်ပါက သို့မဟုတ် သင်မကျေနပ်ပါက **[TAB]** ကို ထပ်မံနှိပ်ပါက ပိုမိုရှည်လျားသော စာသားများပါဝင်သော ရွေးချယ်မှုများကို ရရှိပါမည်။

## GPT သည် မော်ဒယ်မိသားစုတစ်ခုဖြစ်သည်

GPT သည် တစ်ခုတည်းသော မော်ဒယ်မဟုတ်ဘဲ [OpenAI](https://openai.com) မှ ဖွံ့ဖြိုးတိုးတက်စွာ လေ့ကျင့်ထားသော မော်ဒယ်များစုစည်းမှုတစ်ခုဖြစ်သည်။

GPT မော်ဒယ်များတွင် အောက်ပါအတိုင်း ပါဝင်သည်-

| [GPT-2](https://huggingface.co/docs/transformers/model_doc/gpt2#openai-gpt2) | [GPT 3](https://openai.com/research/language-models-are-few-shot-learners) | [GPT-4](https://openai.com/gpt-4) |
| -- | -- | -- |
|Language model with upto 1.5 billion parameters. | Language model with up to 175 billion parameters | 100T parameters and accepts both image and text inputs and outputs text. |

GPT-3 နှင့် GPT-4 မော်ဒယ်များကို [Microsoft Azure မှ Cognitive Service](https://azure.microsoft.com/en-us/services/cognitive-services/openai-service/#overview?WT.mc_id=academic-77998-cacaste) အဖြစ်နှင့် [OpenAI API](https://openai.com/api/) အဖြစ် ရရှိနိုင်ပါသည်။

## Prompt Engineering

GPT သည် ဘာသာစကားနှင့် ကုဒ်ကို နားလည်ရန် အကြီးစားဒေတာများကို လေ့ကျင့်ထားသောကြောင့် Input (Prompt) များအပေါ် Output များကို ပေးသည်။ Prompt များသည် GPT Input သို့မဟုတ် Query များဖြစ်ပြီး မော်ဒယ်များကို အလုပ်များကို ဆောင်ရွက်ရန် ညွှန်ကြားချက်များပေးသည်။ လိုအပ်သောရလဒ်ကို ရရှိရန် အကျိုးရှိဆုံး Prompt ကို ရွေးချယ်ရမည်ဖြစ်ပြီး ၎င်းတွင် စကားလုံးများ၊ ပုံစံများ၊ စကားစုများ သို့မဟုတ် သင်္ကေတများကို ရွေးချယ်ခြင်းပါဝင်သည်။ ဤနည်းလမ်းကို [Prompt Engineering](https://learn.microsoft.com/en-us/shows/ai-show/the-basics-of-prompt-engineering-with-azure-openai-service?WT.mc_id=academic-77998-bethanycheum) ဟုခေါ်သည်။

[ဤစာရွက်စာတမ်း](https://learn.microsoft.com/en-us/semantic-kernel/prompt-engineering/?WT.mc_id=academic-77998-bethanycheum) သည် Prompt Engineering အကြောင်း ပိုမိုသိရှိစေရန် အချက်အလက်များကို ပေးသည်။

## ✍️ နမူနာ Notebook: [Playing with OpenAI-GPT](../../../../../lessons/5-NLP/20-LangModels/GPT-PyTorch.ipynb)

အောက်ပါ Notebook များတွင် သင်၏ သင်ကြားမှုကို ဆက်လက်လုပ်ဆောင်ပါ-

* [Generating text with OpenAI-GPT and Hugging Face Transformers](../../../../../lessons/5-NLP/20-LangModels/GPT-PyTorch.ipynb)

## နိဂုံးချုပ်

အသစ်သော အထွေထွေကြိုတင်လေ့ကျင့်ထားသော ဘာသာစကားမော်ဒယ်များသည် ဘာသာစကားဖွဲ့စည်းမှုကိုသာမက သဘာဝဘာသာစကား၏ အကြီးစားပမာဏကိုလည်း မော်ဒယ်လုပ်ထားသည်။ ထို့ကြောင့် Zero-shot သို့မဟုတ် Few-shot Settings များတွင် NLP အလုပ်အချို့ကို ထိရောက်စွာ ဖြေရှင်းနိုင်သည်။

## [Post-lecture quiz](https://ff-quizzes.netlify.app/en/ai/quiz/40)

**အကြောင်းကြားချက်**:  
ဤစာရွက်စာတမ်းကို AI ဘာသာပြန်ဝန်ဆောင်မှု [Co-op Translator](https://github.com/Azure/co-op-translator) ကို အသုံးပြု၍ ဘာသာပြန်ထားပါသည်။ ကျွန်ုပ်တို့သည် တိကျမှုအတွက် ကြိုးစားနေသော်လည်း၊ အလိုအလျောက် ဘာသာပြန်မှုများတွင် အမှားများ သို့မဟုတ် မတိကျမှုများ ပါဝင်နိုင်သည်ကို သတိပြုပါ။ မူရင်းစာရွက်စာတမ်းကို ၎င်း၏ မူလဘာသာစကားဖြင့် အာဏာတရားရှိသော အရင်းအမြစ်အဖြစ် သတ်မှတ်သင့်ပါသည်။ အရေးကြီးသော အချက်အလက်များအတွက် လူက ဘာသာပြန်မှုကို အသုံးပြုရန် အကြံပြုပါသည်။ ဤဘာသာပြန်မှုကို အသုံးပြုခြင်းမှ ဖြစ်ပေါ်လာသော အလွဲအလွတ်များ သို့မဟုတ် အနားယူမှုများအတွက် ကျွန်ုပ်တို့သည် တာဝန်မယူပါ။