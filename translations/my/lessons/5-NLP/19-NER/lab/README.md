# NER

လေ့လာရေးအတွက် [AI for Beginners Curriculum](https://github.com/microsoft/ai-for-beginners) မှ Lab Assignment။

## တာဝန်

ဒီ Lab မှာ သင့်အနေနဲ့ ဆေးဘက်ဆိုင်ရာအမည်ပြုမူအသိအမှတ်ပြုမှု (NER) မော်ဒယ်ကို လေ့ကျင့်ရမည်ဖြစ်သည်။

## ဒေတာဆက်စုစည်းမှု

NER မော်ဒယ်ကို လေ့ကျင့်ရန်အတွက် ဆေးဘက်ဆိုင်ရာအဖွဲ့အစည်းများကို မှန်ကန်စွာတပ်ဆင်ထားသော ဒေတာဆက်စုစည်းမှုလိုအပ်သည်။ [BC5CDR dataset](https://biocreative.bioinformatics.udel.edu/tasks/biocreative-v/track-3-cdr/) တွင် 1500 ကျော်သော စာတမ်းများမှ ရောဂါများနှင့် ဓာတုဗေဒဆိုင်ရာအဖွဲ့အစည်းများကို တပ်ဆင်ထားသည်။ ၎င်းဒေတာကို ၎င်းတို့၏ဝဘ်ဆိုဒ်တွင် မှတ်ပုံတင်ပြီးနောက် ဒေါင်းလုဒ်လုပ်နိုင်သည်။

BC5CDR Dataset သည် အောက်ပါအတိုင်းဖြစ်သည်-

```
6794356|t|Tricuspid valve regurgitation and lithium carbonate toxicity in a newborn infant.
6794356|a|A newborn with massive tricuspid regurgitation, atrial flutter, congestive heart failure, and a high serum lithium level is described. This is the first patient to initially manifest tricuspid regurgitation and atrial flutter, and the 11th described patient with cardiac disease among infants exposed to lithium compounds in the first trimester of pregnancy. Sixty-three percent of these infants had tricuspid valve involvement. Lithium carbonate may be a factor in the increasing incidence of congenital heart disease when taken during early pregnancy. It also causes neurologic depression, cyanosis, and cardiac arrhythmia when consumed prior to delivery.
6794356	0	29	Tricuspid valve regurgitation	Disease	D014262
6794356	34	51	lithium carbonate	Chemical	D016651
6794356	52	60	toxicity	Disease	D064420
...
```

ဒီဒေတာတွင် ပထမနှစ်ကြောင်းမှာ စာတမ်းခေါင်းစဉ်နှင့် အကျဉ်းချုပ်ဖြစ်ပြီး၊ ထို့နောက် title+abstract block အတွင်းရှိ အဖွဲ့အစည်းတစ်ခုစီ၏ စတင်နှင့် အဆုံးနေရာများပါရှိသည်။ အဖွဲ့အစည်းအမျိုးအစားအပြင်၊ ၎င်းအဖွဲ့အစည်း၏ ဆေးဘက်ဆိုင်ရာ ontology အတွင်းရှိ ontology ID ကိုလည်း ရရှိနိုင်သည်။

ဤဒေတာကို BIO encoding သို့ ပြောင်းရန် Python ကုဒ်အချို့ရေးရန် လိုအပ်မည်ဖြစ်သည်။

## ကွန်ယက်

NER အတွက် ပထမဆုံးကြိုးစားမှုကို သင်ခန်းစာအတွင်း တွေ့ရှိခဲ့သည့် ဥပမာအတိုင်း LSTM ကွန်ယက်ကို အသုံးပြု၍ ပြုလုပ်နိုင်သည်။ သို့သော် NLP လုပ်ငန်းများတွင် [transformer architecture](https://en.wikipedia.org/wiki/Transformer_(machine_learning_model)) နှင့် အထူးသဖြင့် [BERT language models](https://en.wikipedia.org/wiki/BERT_(language_model)) သည် ပိုမိုကောင်းမွန်သောရလဒ်များကို ပြသသည်။ Pre-trained BERT မော်ဒယ်များသည် ဘာသာစကားတစ်ခု၏ အခြေခံဖွဲ့စည်းမှုကို နားလည်ပြီး၊ သေးငယ်သော ဒေတာဆက်စုစည်းမှုများနှင့် တွက်ချက်မှုကုန်ကျစရိတ်နည်းသော အထူးလုပ်ငန်းများအတွက် ပြန်လည်လေ့ကျင့်နိုင်သည်။

NER ကို ဆေးဘက်ဆိုင်ရာအခြေအနေတွင် အသုံးပြုရန် စီစဉ်နေသောကြောင့် ဆေးဘက်ဆိုင်ရာစာသားများပေါ်တွင် လေ့ကျင့်ထားသော BERT မော်ဒယ်ကို အသုံးပြုခြင်းမှာ make sense ဖြစ်သည်။ Microsoft Research သည် [PubMed](https://pubmed.ncbi.nlm.nih.gov/) repository မှ စာသားများကို အသုံးပြု၍ လေ့ကျင့်ထားသော [PubMedBERT][PubMedBERT] ([publication][PubMedBERT-Pub]) ဟုခေါ်သော pre-trained မော်ဒယ်ကို ထုတ်ဝေထားသည်။

Transformer မော်ဒယ်များကို လေ့ကျင့်ရန် *de facto* စံဖြစ်သော [Hugging Face Transformers](https://huggingface.co/) library ကို အသုံးပြုနိုင်သည်။ ၎င်းတွင် PubMedBERT အပါအဝင် community-maintained pre-trained မော်ဒယ်များကိုလည်း ပါဝင်သည်။ ဤမော်ဒယ်ကို load လုပ်ပြီး အသုံးပြုရန်အတွက် ကုဒ်အကြောင်းအရာအနည်းငယ်သာ လိုအပ်သည်-

```python
model_name = "microsoft/BiomedNLP-PubMedBERT-base-uncased-abstract"
classes = ... # number of classes: 2*entities+1
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = BertForTokenClassification.from_pretrained(model_name, classes)
```

ဤကုဒ်သည် `classes` အရေအတွက်အလိုက် token classification လုပ်ငန်းအတွက် တည်ဆောက်ထားသော `model` ကိုပေးပြီး၊ input text ကို token များအဖြစ် ခွဲခြားနိုင်သော `tokenizer` object ကိုလည်း ပေးသည်။ PubMedBERT tokenization ကို ထည့်သွင်းစဉ်းစားပြီး ဒေတာကို BIO format သို့ ပြောင်းရန် လိုအပ်မည်။ [ဒီ Python ကုဒ်](https://gist.github.com/shwars/580b55684be3328eb39ecf01b9cbbd88) ကို အကြံဉာဏ်အဖြစ် အသုံးပြုနိုင်သည်။

## အဓိကအချက်

ဤတာဝန်သည် သင့်အနေနဲ့ သဘာဝဘာသာစကားစာသားများ၏ အကြီးအကျယ်ကို နက်နက်ရှိုင်းရှိုင်း နားလည်လိုပါက ရှိနိုင်သော အမှန်တကယ်လုပ်ငန်းနှင့် အလွန်နီးစပ်သည်။ ကျွန်ုပ်တို့၏အမှုတွင်၊ လေ့ကျင့်ထားသောမော်ဒယ်ကို [COVID-19 ဆိုင်ရာစာတမ်းများ၏ ဒေတာဆက်စုစည်းမှု](https://www.kaggle.com/allen-institute-for-ai/CORD-19-research-challenge) တွင် အသုံးပြု၍ ရရှိနိုင်သော အချက်အလက်များကို ကြည့်ရှုနိုင်သည်။ [ဒီဘလော့ဂ်ပို့စ်](https://soshnikov.com/science/analyzing-medical-papers-with-azure-and-text-analytics-for-health/) နှင့် [ဒီစာတမ်း](https://www.mdpi.com/2504-2289/6/1/4) တွင် NER ကို အသုံးပြု၍ စာတမ်းများအပေါ် ပြုလုပ်နိုင်သော သုတေသနကို ဖော်ပြထားသည်။

**အကြောင်းကြားချက်**:  
ဤစာရွက်စာတမ်းကို AI ဘာသာပြန်ဝန်ဆောင်မှု [Co-op Translator](https://github.com/Azure/co-op-translator) ကို အသုံးပြု၍ ဘာသာပြန်ထားပါသည်။ ကျွန်ုပ်တို့သည် တိကျမှုအတွက် ကြိုးစားနေပါသော်လည်း၊ အလိုအလျောက် ဘာသာပြန်မှုများတွင် အမှားများ သို့မဟုတ် မတိကျမှုများ ပါရှိနိုင်သည်ကို သတိပြုပါ။ မူရင်းစာရွက်စာတမ်းကို ၎င်း၏ မူရင်းဘာသာစကားဖြင့် အာဏာတရားရှိသော အရင်းအမြစ်အဖြစ် သတ်မှတ်သင့်ပါသည်။ အရေးကြီးသော အချက်အလက်များအတွက် လူက ဘာသာပြန်မှုကို အသုံးပြုရန် အကြံပြုပါသည်။ ဤဘာသာပြန်မှုကို အသုံးပြုခြင်းမှ ဖြစ်ပေါ်လာသော အလွဲအလွတ်များ သို့မဟုတ် အနားယူမှုများအတွက် ကျွန်ုပ်တို့သည် တာဝန်မယူပါ။