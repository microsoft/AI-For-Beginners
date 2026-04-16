# AI စတင်လေ့လာသူများအတွက် နမူနာများ

ကြိုဆိုပါတယ်! ဒီ directory မှာ AI နဲ့ machine learning ကို စတင်လေ့လာဖို့အတွက် လွယ်ကူပြီး တစ်ခုချင်းစီ standalone နမူနာများ ပါဝင်ပါတယ်။ နမူနာတစ်ခုချင်းစီကို စတင်လေ့လာသူများအတွက် သက်သာစေဖို့ အကြောင်းအရာများကို အသေးစိတ် ရှင်းပြထားပြီး အဆင့်ဆင့် လမ်းညွှန်ချက်များ ပါဝင်ပါတယ်။

## 📚 နမူနာများအကြောင်းအကျဉ်း

| နမူနာ | ဖော်ပြချက် | အခက်အခဲအဆင့် | လိုအပ်ချက်များ |
|-------|------------|----------------|----------------|
| [Hello AI World](../../../examples/01-hello-ai-world.py) | သင့်ရဲ့ ပထမဆုံး AI အစီအစဉ် - လွယ်ကူတဲ့ pattern recognition | ⭐ စတင်လေ့လာသူ | Python အခြေခံ |
| [Simple Neural Network](../../../examples/02-simple-neural-network.py) | Neural network ကို အခြေခံကနေ တည်ဆောက်ခြင်း | ⭐⭐ စတင်လေ့လာသူ+ | Python, အခြေခံဂဏန်းသိပ္ပံ |
| [Image Classifier](./03-image-classifier.ipynb) | Pre-trained model နဲ့ ပုံတွေကို အမျိုးအစားခွဲခြားခြင်း | ⭐⭐ စတင်လေ့လာသူ+ | Python, numpy |
| [Text Sentiment](../../../examples/04-text-sentiment.py) | စာသား sentiment (အပြုသဘော/အဆိုးသဘော) ကို ခွဲခြားခြင်း | ⭐⭐ စတင်လေ့လာသူ+ | Python |

## 🚀 စတင်လေ့လာခြင်း

### လိုအပ်ချက်များ

Python (3.8 သို့မဟုတ် အထက်) ကို install လုပ်ထားပါ။ လိုအပ်တဲ့ packages တွေကို install လုပ်ပါ:

```bash
# For Python scripts
pip install numpy

# For Jupyter notebooks (image classifier)
pip install jupyter numpy pillow tensorflow
```

သို့မဟုတ် main curriculum မှ conda environment ကို အသုံးပြုပါ:

```bash
conda env create --name ai4beg --file ../environment.yml
conda activate ai4beg
```

### နမူနာများကို အလုပ်လုပ်စေခြင်း

**Python scripts (.py files) အတွက်:**
```bash
python 01-hello-ai-world.py
```

**Jupyter notebooks (.ipynb files) အတွက်:**
```bash
jupyter notebook 03-image-classifier.ipynb
```

## 📖 လေ့လာရေးလမ်းကြောင်း

နမူနာများကို အစဉ်လိုက် လေ့လာဖို့ အကြံပြုပါတယ်:

1. **"Hello AI World" နဲ့ စတင်ပါ** - pattern recognition အခြေခံကို လေ့လာပါ
2. **Simple Neural Network တည်ဆောက်ပါ** - neural networks ဘယ်လိုအလုပ်လုပ်သလဲ နားလည်ပါ
3. **Image Classifier ကို စမ်းကြည့်ပါ** - အမှန်တကယ် ပုံတွေနဲ့ AI အလုပ်လုပ်ပုံကို ကြည့်ပါ
4. **Text Sentiment ကို ခွဲခြားပါ** - natural language processing ကို စမ်းကြည့်ပါ

## 💡 စတင်လေ့လာသူများအတွက် အကြံပေးချက်များ

- **Code မှာပါတဲ့ မှတ်ချက်တွေကို သေချာဖတ်ပါ** - တစ်ကြောင်းချင်းစီ ဘာလုပ်သလဲ ရှင်းပြထားပါတယ်
- **စမ်းကြည့်ပါ!** - တန်ဖိုးတွေကို ပြောင်းပြီး ဘာဖြစ်မလဲ ကြည့်ပါ
- **အရာအားလုံးကို နားလည်ဖို့ စိတ်ပူမထားပါနဲ့** - လေ့လာခြင်းက အချိန်ယူရပါတယ်
- **မေးမြန်းပါ** - [Discussion board](https://github.com/microsoft/AI-For-Beginners/discussions) ကို အသုံးပြုပါ

## 🔗 နောက်တစ်ဆင့်များ

ဒီနမူနာတွေကို ပြီးမြောက်ပြီးနောက်မှာ အပြည့်အစုံ curriculum ကို လေ့လာပါ:
- [AI အကျဉ်းချုပ်](../lessons/1-Intro/README.md)
- [Neural Networks](../lessons/3-NeuralNetworks/README.md)
- [Computer Vision](../lessons/4-ComputerVision/README.md)
- [Natural Language Processing](../lessons/5-NLP/README.md)

## 🤝 အထောက်အပံ့ပေးခြင်း

ဒီနမူနာတွေကို အသုံးဝင်တယ်လို့ တွေ့ရင် ကျွန်တော်တို့ကို အကောင်းပြောပါ:
- ပြဿနာတွေကို report လုပ်ပါ သို့မဟုတ် တိုးတက်မှုအကြံပေးပါ
- စတင်လေ့လာသူများအတွက် နမူနာတွေ ပိုမိုထည့်ပါ
- Documentation နဲ့ မှတ်ချက်တွေကို တိုးတက်အောင်လုပ်ပါ

---

*သတိရပါ: ကျွမ်းကျင်သူတိုင်းဟာ တစ်ချိန်က စတင်လေ့လာသူတစ်ဦးဖြစ်ခဲ့ပါတယ်။ လေ့လာမှုကို ပျော်ရွှင်စွာ ဆက်လက်ပါ! 🎓*

---

**အကြောင်းကြားချက်**:  
ဤစာရွက်စာတမ်းကို AI ဘာသာပြန်ဝန်ဆောင်မှု [Co-op Translator](https://github.com/Azure/co-op-translator) ကို အသုံးပြု၍ ဘာသာပြန်ထားပါသည်။ ကျွန်ုပ်တို့သည် တိကျမှုအတွက် ကြိုးစားနေသော်လည်း၊ အလိုအလျောက် ဘာသာပြန်ခြင်းတွင် အမှားများ သို့မဟုတ် မတိကျမှုများ ပါရှိနိုင်သည်ကို သတိပြုပါ။ မူရင်းဘာသာစကားဖြင့် ရေးသားထားသော စာရွက်စာတမ်းကို အာဏာတရ အရင်းအမြစ်အဖြစ် သတ်မှတ်သင့်ပါသည်။ အရေးကြီးသော အချက်အလက်များအတွက် လူ့ဘာသာပြန်ပညာရှင်များကို အသုံးပြုရန် အကြံပြုပါသည်။ ဤဘာသာပြန်ကို အသုံးပြုခြင်းမှ ဖြစ်ပေါ်လာသော အလွဲအလွဲအချော်များ သို့မဟုတ် အနားယူမှုမှားများအတွက် ကျွန်ုပ်တို့သည် တာဝန်မယူပါ။