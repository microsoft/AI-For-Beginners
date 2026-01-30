# နည်းလမ်း အတိုင်း ကုတ်ကို လည်ပတ်ရန်

ဒီ သင်ခန်းစာဟာ အလုပ်လုပ်နိုင်တဲ့ ဥပမာတွေ နဲ့ လက်တွေ့လေ့ကျင့်ခန်းတွေ များစွာ ပါဝင်ပြီး သင် လည်ပတ်ချင်မယ်။ ဒါကို လုပ်ဖို့ သင် လိုအပ်တာက ဒီသင်ခန်းစာ၏ အစိတ်အပိုင်းတစ်ခုအနေဖြင့် ပေးထားတဲ့ Jupyter Notebooks ထဲမှာ Python ကုတ်ကို လည်ပတ်နိုင်စွမ်းရှိဖို့ ဖြစ်ပါတယ်။ ကုတ်ကို လည်ပတ်ဖို့ အနည်းငယ် ရွေးချယ်စရာရှိပါတယ်-

## သင့် ကွန်ပျူတာပေါ်မှာ ဒေသခံ လည်ပတ်ရန်

သင့် ကွန်ပျူတာပေါ်မှာ ဒေသခံ လည်ပတ်ဖို့ Python တပ်ဆင်ထားဖို့ လိုအပ်ပါတယ်။ တစ်ခုအတွဲအနေနဲ့ အကြံပြုတာက **[miniconda](https://conda.io/en/latest/miniconda.html)** ကို တပ်ဆင်ဖို့ ဖြစ်ပြီး ဒါဟာ `conda` package manager ကို ထောက်ပံ့တဲ့ ပိုလွယ်ကူတဲ့ Python **virtual environment** များအတွက် တပ်ဆင်ဖို့ တစ်ခုလေးပါ။

miniconda တပ်ဆင်ပြီးပါက repository ကို clone ဆွဲပြီး ဒီသင်တန်းအတွက် အသုံးပြုမဲ့ virtual environment တစ်ခု ဖန်တီးပါ-

```bash
git clone http://github.com/microsoft/ai-for-beginners
cd ai-for-beginners
conda env create --name ai4beg --file .devcontainer/environment.yml
conda activate ai4beg
```

### Visual Studio Code ကို Python Extension နဲ့ အသုံးပြုခြင်း

ဒီ သင်ခန်းစာကို အသုံးပြုရာမှာ [Visual Studio Code](http://code.visualstudio.com/?WT.mc_id=academic-77998-cacaste) ကို [Python Extension](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-77998-cacaste) နဲ့ဖွင့်၍ သုံးလို့ အကောင်းဆုံးပါ။

> **မှတ်ချက်**: VS Code ထဲမှာ directory ကို clone ဆွဲပြီးဖွင့်လိုက်တာနဲ့ Python extensions ကို အလိုအလျောက် တပ်ဆင်ဖို့ ပေးရှုံ့ပေးမှာ ဖြစ်ပါတယ်။ အထက်မှာ ဖော်ပြထားတဲ့အတိုင်း miniconda ကိုလည်း တပ်ဆင်ထားဖို့ လိုအပ်မှာ ဖြစ်ပါတယ်။

> **မှတ်ချက်**: VS Code က container အတွင်းမှာ repo ကို ပြန်ဖွင့်ဖို့ 제안လာရင် ဒေသခံ Python တပ်ဆင်မှုကို အသုံးပြုဖို့ ထို ပြန်ဖွင့်ခြင်းကို ငြင်းဆန်သင့်ပါတယ်။

### Browser တွင် Jupyter အသုံးပြုခြင်း

သင့် ရှိရာ ကွန်ပျူတာမှာ browser မှတစ်ဆင့် Jupyter ပတ်ဝန်းကျင်ကိုလည်း အသုံးပြုနိုင်ပါတယ်။ classical Jupyter နဲ့ JupyterHub နှစ်ခုလုံးမှာ auto-completion, ကုတ်အလင်းပေးခြင်း စသည်တို့ ပါဝင်တဲ့ သက်တောင့်သက်သာ ဖွံ့ဖြိုးမှုပတ်ဝန်းကျင်ကို ရရှိစေပါတယ်။

ဒေသခံ Jupyter ကို စတင်ရန် သင်တန်း folder ကိုသွားပြီး အောက်ပါအတိုင်း လည်ပတ်ပါ-

```bash
jupyter notebook
```
or
```bash
jupyterhub
```
ပြီးရင် `.ipynb` ဖိုင် ဘယ်ဟာမဆို သွားရှာဖွေ၊ ဖွင့်ပြီး အလုပ်ဆောင်နိုင်ပါပြီ။

### Container မှာ လည်ပတ်ခြင်း

Python တပ်ဆင်မထားဘဲ container ထဲမှာ ကုတ်တွေ လည်ပတ်လိုက်ရင်နည်းလမ်းတစ်ခုရှိပါတယ်။ ကျွန်တော်တို့ရဲ့ repo ထဲမှာ `.devcontainer` ဆိုတဲ့ folder က container ဖန်တီးနည်းကို ဖော်ပြပေးတာကြောင့် VS Code က container မှာ repo ကို ပြန်ဖွင့်ဖို့ အခွင့်အလမ်းပေးပါတယ်။ ဒီအတွက် Docker ကို တပ်ဆင်ထားရမှာဖြစ်ပြီး ပိုကြမ်းတမ်းရှုပ်ထွေးတဲ့ နယ်ပယ်ဖြစ်လို့ နည်းပညာပိုင်းမှာ ကျွမ်းကျင်သူတွေအတွက်သာ အသုံးပြုဖို့ အကြံပြုပါတယ်။ 

## Cloud မှာ လည်ပတ်ခြင်း

Python ကို ဒေသခံမှာ တပ်ဆင်ချင် မထားဘူး၊ cloud資源အသုံးပြုခွင့်ရှိရင် cloud မှာ ကုတ်ကို လည်ပတ်အသုံးပြုဖို့ ကောင်းတဲ့ နည်းလမ်းများ ရှိပါတယ်-

* **[GitHub Codespaces](https://github.com/features/codespaces)** ကို အသုံးပြုခြင်း။ GitHub မှာ သင့်အတွက် virtual environment ဖန်တီးပေးပြီး VS Code browser များဖြင့် ရရှိနိုင်ပါတယ်။ Codespaces အသုံးပြုခွင့် ရှိရင် repo မှာ **Code** ခလုတ်ကို နှိပ်ပြီး codespace စတင်ပြီး အခက်အခဲမရှိတတ်နိုင်ပြီ။
* **[Binder](https://mybinder.org/v2/gh/microsoft/ai-for-beginners/HEAD)** ကို အသုံးပြုခြင်း။ [Binder](https://mybinder.org) က GitHub မှာရှိတဲ့ ကုတ်တွေကို စမ်းသပ်ဖို့အတွက် cloud မှကွန်ပျူတာ အရင်းအမြစ်များကို အခမဲ့ ပေးအပ်ပါတယ်။ repo ကို Binder မှာဖွင့်ဖို့ front page မှာ ခလုတ်တစ်ခုရှိပြီး ၎င်းက သင့်အတွက် container တစ်ခုပြုလုပ်ပြီး Jupyter web interface ကို စတင်ပေးပါလိမ့်မယ်။

> **မှတ်ချက်**: မမှန်ကန်စွာ အသုံးပြုမှု တားမြစ်ဖို့ Binder ကတချို့ web resources များကို ပိတ်ထားပါတယ်။ ထို့ကြောင့် မော်ဒယ်များ သို့မဟုတ် ဒေတာအစုံများကို အွန်လိုင်းမှ ယူလာတဲ့ ကုတ်တချို့ ဘာလုပ်မရဘူး ဖြစ်နိုင်ပါတယ်။ အလုပ်ဖြေရှင်းနည်းခြင်းတွေလည်း လိုအပ်နိုင်ပါတယ်။ ထို့အပြင် Binder ပေးတဲ့ ကွန်ပျူတာ အရင်းအမြစ်တွေ အခြေခံအဆင့်ဖြစ်လို့ သင်ကြားမှု မြန်မရနိုင်ပါ၊ အထူးသဖြင့် နောက်ပိုင်းမှာ ပိုခက်ခဲမယ့် သင်ခန်းစာများမှာပြသနာဖြစ်နိုင်ပါတယ်။

## GPU ပါ Cloud မှာ လည်ပတ်ခြင်း

ဒီသင်ခန်းစာအတွင်း နောက်ပိုင်းသင်ခန်းစာအချို့မှာ GPU ပံ့ပိုးမှုက အလွန် အကျိုးရှိပါလိမ့်မယ်။ မော်ဒယ် သင်ကြားမှုကို ပိုမြန်စေမှာ ဖြစ်ပြီး မရှိမဖြစ်လိုအပ်ပါတယ်။ [Azure for Students](https://azure.microsoft.com/free/students/?WT.mc_id=academic-77998-cacaste) သို့မဟုတ် သင့်တက္ကသိုလ်မှတဆင့် cloud ရရှိသူတွေ အတွက် အောက်ပါနည်းလမ်းများ ရှိပါတယ်-

* [Data Science Virtual Machine](https://docs.microsoft.com/learn/modules/intro-to-azure-data-science-virtual-machine/?WT.mc_id=academic-77998-cacaste) တစ်ခု ဖန်တီးပြီး Jupyter မှတစ်ဆင့် ချိတ်ဆက်ပြီး အသုံးပြုနိုင်ပါတယ်။ repo ကို တိုက်ရိုက် machine မှာ clone ဆွဲပြီး စတင်လေ့လာနိုင်ပါတယ်။ NC-series VMs တွေဟာ GPU ပါဝင်ပါတယ်။

> **မှတ်ချက်**: Azure for Students စသည့် subscription တချို့ဟာ ပုံမှန်အတိုင်း GPU ပံ့ပိုးမှု မပေးပါ၊ technical support ကနေ GPU cores ပိုများအောင် တောင်းဆိုရပါမယ်။

* [Azure Machine Learning Workspace](https://azure.microsoft.com/services/machine-learning/?WT.mc_id=academic-77998-cacaste) တစ်ခု ဖန်တီးပြီး Notebook feature ကို အသုံးပြုနိုင်ပါတယ်။ [ဤဗီဒီယို](https://azure-for-academics.github.io/quickstart/azureml-papers/) သည် Azure ML Notebook တွင် repo တစ်ခုကို clone ဆွဲပြီး အသုံးပြုနည်းကို ပြသထားပါတယ်။

Google Colab ကိုလည်း အသုံးပြုနိုင်ပြီး အခမဲ့ GPU ပံ့ပိုးမှု နဲ့ Jupyter Notebooks တွေကို တစ်ခုချင်းစီ တင်ပြီး လည်ပတ်နိုင်ပါတယ်။

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**အကြောင်းကြားချက်**:
ဤစာတမ်းကို AI ဘာသာပြန်ဝန်ဆောင်မှု [Co-op Translator](https://github.com/Azure/co-op-translator) အသုံးပြု၍ ဘာသာပြန်ထားပါသည်။ မှန်ကန်မှုအတွက် ကြိုးစားပေမယ့် စက်မြန်မာဘာသာပြန်ချက်များတွင် အမှားများ သို့မဟုတ် မမှန်ကန်မှုများ ပါဝင်နိုင်ကြောင်း သတိပြုပါရန် အပ်ပါသည်။ မူရင်းစာတမ်းကို မိခင်ဘာသာဖြင့်သာ ထောက်ခံချက်အဖြစ်ယူဆသင့်ပါသည်။ အရေးကြီးသည့် သတင်းအချက်အလက်များအတွက်တော့ တတ်ကျွမ်းသော လူ့ဘာသာပြန်သူများ၏ ဘာသာပြန်ခြင်းကို အကြံပြုပါသည်။ ဤဘာသာပြန်ချက်ကို အသုံးပြုမှုမှဖြစ်ပေါ်လာသော လွဲမှား သို့မဟုတ် နားလည်မှုမှားများအတွက် ကျွန်ုပ်တို့ မည်သည့် တာဝန်မရှိပါ။
<!-- CO-OP TRANSLATOR DISCLAIMER END -->