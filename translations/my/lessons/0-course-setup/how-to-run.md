<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "7df19702b8d2d3f7c4238c51bec2c8fc",
  "translation_date": "2025-08-26T00:38:02+00:00",
  "source_file": "lessons/0-course-setup/how-to-run.md",
  "language_code": "my"
}
-->
# ကုဒ်ကို အလုပ်လုပ်စေခြင်း

ဒီသင်ခန်းစာမှာ သင်လုပ်ဆောင်လိုတဲ့ အလုပ်လုပ်နိုင်တဲ့ နမူနာများနဲ့ လက်တွေ့လေ့ကျင့်ခန်းများ ပါဝင်ပါတယ်။ ဒါကို အလုပ်လုပ်စေဖို့အတွက် Python ကုဒ်ကို Jupyter Notebooks မှာ အလုပ်လုပ်နိုင်ဖို့ လိုအပ်ပါတယ်။ သင့်မှာ ကုဒ်ကို အလုပ်လုပ်စေဖို့ အနည်းဆုံး အောက်ပါနည်းလမ်းများ ရှိပါတယ်:

## သင့်ကွန်ပျူတာမှာ တိုက်ရိုက် အလုပ်လုပ်စေခြင်း

သင့်ကွန်ပျူတာမှာ တိုက်ရိုက် အလုပ်လုပ်စေဖို့ Python ရဲ့ အချို့သော version တစ်ခုခုကို ထည့်သွင်းထားဖို့ လိုအပ်ပါတယ်။ **[miniconda](https://conda.io/en/latest/miniconda.html)** ကို ထည့်သွင်းဖို့ အကြံပြုပါတယ် - ဒါဟာ `conda` package manager ကို အသုံးပြုနိုင်တဲ့ Python **virtual environments** အတွက် အလွန်ပေါ့ပါးတဲ့ installation ဖြစ်ပါတယ်။

miniconda ကို ထည့်သွင်းပြီးနောက် သင့်မှာ repository ကို clone လုပ်ပြီး ဒီသင်ခန်းစာအတွက် အသုံးပြုမယ့် virtual environment ကို ဖန်တီးဖို့ လိုအပ်ပါတယ်:

```bash
git clone http://github.com/microsoft/ai-for-beginners
cd ai-for-beginners
conda env create --name ai4beg --file .devcontainer/environment.yml
conda activate ai4beg
```

### Visual Studio Code နဲ့ Python Extension ကို အသုံးပြုခြင်း

ဒီသင်ခန်းစာကို အသုံးပြုဖို့ အကောင်းဆုံးနည်းလမ်းက [Visual Studio Code](http://code.visualstudio.com/?WT.mc_id=academic-77998-cacaste) ကို [Python Extension](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-77998-cacaste) နဲ့ ဖွင့်ခြင်းဖြစ်ပါတယ်။

> **Note**: သင် repository ကို clone လုပ်ပြီး VS Code မှာ directory ကို ဖွင့်တဲ့အခါ Python extensions ကို ထည့်သွင်းဖို့ အလိုအလျောက် အကြံပြုပါလိမ့်မယ်။ Miniconda ကို အထက်မှာ ဖော်ပြထားတဲ့အတိုင်း ထည့်သွင်းဖို့လည်း လိုအပ်ပါတယ်။

> **Note**: VS Code က repository ကို container မှာ ပြန်ဖွင့်ဖို့ အကြံပြုလျှင်၊ local Python installation ကို အသုံးပြုဖို့ container ကို ဖွင့်ခြင်းကို ငြင်းပယ်ဖို့ လိုအပ်ပါတယ်။

### Browser မှာ Jupyter ကို အသုံးပြုခြင်း

သင့်ကွန်ပျူတာမှာ Browser မှာ Jupyter environment ကို အသုံးပြုနိုင်ပါတယ်။ အမှန်အားဖြင့် classical Jupyter နဲ့ Jupyter Hub နှစ်ခုလုံးမှာ auto-completion, code highlighting စတဲ့ အဆင်ပြေတဲ့ development environment တွေ ရှိပါတယ်။

Jupyter ကို locally စတင်ဖို့ သင့်သင်ခန်းစာ directory ကို သွားပြီး အောက်ပါ command ကို အလုပ်လုပ်စေပါ:

```bash
jupyter notebook
```  
or  
```bash
jupyterhub
```  
ပြီးရင် `.ipynb` ဖိုင်တွေကို သွားပြီး ဖွင့်ပြီး အလုပ်လုပ်နိုင်ပါပြီ။

### Container မှာ အလုပ်လုပ်စေခြင်း

Python installation ကို အစားထိုးတဲ့ နည်းလမ်းတစ်ခုက container မှာ အလုပ်လုပ်စေခြင်းဖြစ်ပါတယ်။ ကျွန်တော်တို့ရဲ့ repository မှာ `.devcontainer` folder ပါဝင်ပြီး ဒီ repo အတွက် container ကို ဘယ်လို build လုပ်မလဲဆိုတာကို သတ်မှတ်ထားပါတယ်။ ဒါကြောင့် VS Code က code ကို container မှာ ပြန်ဖွင့်ဖို့ အကြံပြုပါလိမ့်မယ်။ ဒါကို အသုံးပြုဖို့ Docker installation လိုအပ်ပြီး အနည်းငယ် ပိုရှုပ်ထွေးပါတယ်၊ ဒါကြောင့် အတွေ့အကြုံရှိတဲ့ အသုံးပြုသူများအတွက် အကြံပြုပါတယ်။

## Cloud မှာ အလုပ်လုပ်စေခြင်း

Python ကို locally ထည့်သွင်းချင်မရင်၊ Cloud resources ရှိရင် Cloud မှာ အလုပ်လုပ်စေဖို့ ကောင်းတဲ့ နည်းလမ်းတစ်ခုလည်း ရှိပါတယ်။ အောက်ပါနည်းလမ်းများကို အသုံးပြုနိုင်ပါတယ်:

* **[GitHub Codespaces](https://github.com/features/codespaces)** ကို အသုံးပြုခြင်း။ ဒါဟာ GitHub မှာ သင့်အတွက် ဖန်တီးထားတဲ့ virtual environment ဖြစ်ပြီး VS Code browser interface မှတစ်ဆင့် အသုံးပြုနိုင်ပါတယ်။ Codespaces ရှိရင် repo မှာ **Code** button ကို click လုပ်ပြီး codespace ကို စတင်နိုင်ပါတယ်၊ အချိန်မရွေး အလုပ်လုပ်နိုင်ပါပြီ။
* **[Binder](https://mybinder.org/v2/gh/microsoft/ai-for-beginners/HEAD)** ကို အသုံးပြုခြင်း။ [Binder](https://mybinder.org) ဟာ GitHub မှာ code တွေကို စမ်းသပ်ဖို့ Cloud မှာ အခမဲ့ computing resources ပေးတဲ့ နည်းလမ်းဖြစ်ပါတယ်။ Repository ရဲ့ front page မှာ Binder ကို ဖွင့်ဖို့ button ရှိပါတယ် - ဒါဟာ binder site ကို အလွယ်တကူ ပို့ပြီး underlying container ကို build လုပ်ပြီး Jupyter web interface ကို seamless အဖြစ် စတင်ပေးပါလိမ့်မယ်။

> **Note**: Binder ဟာ အချို့ web resources ကို အသုံးချမှုကို ကန့်သတ်ထားပါတယ်။ ဒါဟာ public Internet မှာ models နဲ့ datasets တွေကို fetch လုပ်တဲ့ code တွေ အလုပ်မလုပ်နိုင်စေပါလိမ့်မယ်။ Workarounds တွေ ရှာဖွေရန် လိုအပ်နိုင်ပါတယ်။ Binder မှာ ပေးထားတဲ့ compute resources တွေက အခြေခံဖြစ်ပြီး training အလွန်နှေးပါလိမ့်မယ်၊ အထူးသဖြင့် နောက်ပိုင်းမှာ ရှုပ်ထွေးတဲ့ သင်ခန်းစာတွေမှာ။

## GPU ပါဝင်တဲ့ Cloud မှာ အလုပ်လုပ်စေခြင်း

ဒီသင်ခန်းစာရဲ့ နောက်ပိုင်းမှာ GPU support ရှိရင် training အလွန်မြန်နိုင်ပါတယ်၊ မဟုတ်ရင် training အလွန်နှေးပါလိမ့်မယ်။ သင့်မှာ Cloud ကို [Azure for Students](https://azure.microsoft.com/free/students/?WT.mc_id=academic-77998-cacaste) သို့မဟုတ် သင့်အဖွဲ့အစည်းမှတစ်ဆင့် အသုံးပြုနိုင်ရင် အောက်ပါနည်းလမ်းများကို လိုက်နာနိုင်ပါတယ်:

* [Data Science Virtual Machine](https://docs.microsoft.com/learn/modules/intro-to-azure-data-science-virtual-machine/?WT.mc_id=academic-77998-cacaste) ကို ဖန်တီးပြီး Jupyter မှတစ်ဆင့် ချိတ်ဆက်ပါ။ Repo ကို machine မှာ တိုက်ရိုက် clone လုပ်ပြီး သင့်သင်ခန်းစာကို စတင်နိုင်ပါတယ်။ NC-series VMs တွေမှာ GPU support ရှိပါတယ်။

> **Note**: Azure for Students အပါအဝင် subscription အချို့မှာ GPU support ကို အလိုအလျောက် မပေးထားပါဘူး။ GPU cores အပိုတောင်းဖို့ technical support request တင်ဖို့ လိုအပ်နိုင်ပါတယ်။

* [Azure Machine Learning Workspace](https://azure.microsoft.com/services/machine-learning/?WT.mc_id=academic-77998-cacaste) ကို ဖန်တီးပြီး Notebook feature ကို အသုံးပြုပါ။ [ဒီဗီဒီယို](https://azure-for-academics.github.io/quickstart/azureml-papers/) မှာ Azure ML notebook မှာ repository ကို clone လုပ်ပြီး အသုံးပြုပုံကို ပြထားပါတယ်။

Google Colab ကိုလည်း အသုံးပြုနိုင်ပြီး အခမဲ့ GPU support ပါဝင်ပါတယ်၊ Jupyter Notebooks တွေကို upload လုပ်ပြီး တစ်ခုချင်းစီကို အလုပ်လုပ်စေပါ။

**အကြောင်းကြားချက်**:  
ဤစာရွက်စာတမ်းကို AI ဘာသာပြန်ဝန်ဆောင်မှု [Co-op Translator](https://github.com/Azure/co-op-translator) ကို အသုံးပြု၍ ဘာသာပြန်ထားပါသည်။ ကျွန်ုပ်တို့သည် တိကျမှုအတွက် ကြိုးစားနေသော်လည်း၊ အလိုအလျောက် ဘာသာပြန်ခြင်းတွင် အမှားများ သို့မဟုတ် မတိကျမှုများ ပါဝင်နိုင်သည်ကို သတိပြုပါ။ မူရင်းဘာသာစကားဖြင့် ရေးသားထားသော စာရွက်စာတမ်းကို အာဏာတရ အရင်းအမြစ်အဖြစ် ရှုလေ့လာသင့်ပါသည်။ အရေးကြီးသော အချက်အလက်များအတွက် လူ့ဘာသာပြန်ပညာရှင်များမှ ပရော်ဖက်ရှင်နယ် ဘာသာပြန်ခြင်းကို အကြံပြုပါသည်။ ဤဘာသာပြန်ကို အသုံးပြုခြင်းမှ ဖြစ်ပေါ်လာသော အလွဲအလွတ်များ သို့မဟုတ် အနားယူမှားမှုများအတွက် ကျွန်ုပ်တို့သည် တာဝန်မယူပါ။