# AI-For-Beginners ပြဿနာဖြေရှင်းလမ်းညွှန်

ဤလမ်းညွှန်သည် [AI-For-Beginners](https://github.com/microsoft/AI-For-Beginners) repository ကို အသုံးပြုခြင်း သို့မဟုတ် အထောက်အကူပြုခြင်းအတွင်း တွေ့ကြုံရသော ပုံမှန်ပြဿနာများကို ဖြေရှင်းရန် ကူညီပေးပါသည်။ ပြဿနာတစ်ခုစီတွင် နောက်ခံအချက်အလက်များ၊ ရောဂါလက္ခဏာများ၊ ရှင်းလင်းချက်များနှင့် အဆင့်လိုက်ဖြေရှင်းနည်းများ ပါဝင်သည်။

---

## အကြောင်းအရာများ

- [အထွေထွေပြဿနာများ](../..)
- [Installation ပြဿနာများ](../..)
- [Configuration ပြဿနာများ](../..)
- [Notebook များကို အလုပ်လုပ်စေခြင်း](../..)
- [Performance ပြဿနာများ](../..)
- [Textbook Website ပြဿနာများ](../..)
- [Contributing ပြဿနာများ](../..)
- [FAQ](../..)
- [အကူအညီရယူခြင်း](../..)

---

## အထွေထွေပြဿနာများ

### 1. Repository ကို မှန်ကန်စွာ Clone မလုပ်နိုင်ခြင်း

**နောက်ခံ:** Clone လုပ်ခြင်းသည် repository ကို သင့်စက်ပေါ်သို့ ကူးယူရန် ခွင့်ပြုသည်။

**ရောဂါလက္ခဏာများ:**
- Error: `fatal: repository not found`
- Error: `Permission denied (publickey)`

**ဖြစ်နိုင်သော အကြောင်းရင်းများ:**
- Repository URL မှားနေခြင်း
- ခွင့်ပြုချက်မလုံလောက်ခြင်း
- SSH key မရှိခြင်း

**ဖြေရှင်းနည်းများ:**
1. **Repository URL ကို စစ်ဆေးပါ။**  
   HTTPS URL ကို အသုံးပြုပါ။  
   ```
   git clone https://github.com/microsoft/AI-For-Beginners.git
   ```
2. **SSH မအောင်မြင်ပါက HTTPS ကို ပြောင်းပါ။**  
   `Permission denied (publickey)` တွေ့ပါက SSH အစား HTTPS link ကို အသုံးပြုပါ။
3. **SSH key များကို Configure လုပ်ပါ (optional).**  
   SSH ကို အသုံးပြုလိုပါက [GitHub's SSH guide](https://docs.github.com/en/authentication/connecting-to-github-with-ssh) ကို လိုက်နာပါ။

---

## Installation ပြဿနာများ

### 2. Python Environment ပြဿနာများ

**နောက်ခံ:** Repository သည် Python နှင့် library များစွာကို အခြေခံထားသည်။

**ရောဂါလက္ခဏာများ:**
- Error: `ModuleNotFoundError: No module named '<package>'`
- Script သို့မဟုတ် notebook များကို run လုပ်သောအခါ Import error

**ဖြစ်နိုင်သော အကြောင်းရင်းများ:**
- Dependencies မရှိခြင်း
- Python version မှားနေခြင်း

**ဖြေရှင်းနည်းများ:**
1. **Virtual environment တစ်ခုကို Set up လုပ်ပါ။**  
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```
2. **Dependencies များကို Install လုပ်ပါ။**  
   ```bash
   pip install -r requirements.txt
   ```
3. **Python version ကို စစ်ဆေးပါ။**  
   Python 3.7 သို့မဟုတ် အနောက်ဆုံး version ကို အသုံးပြုပါ။  
   ```bash
   python --version
   ```

### 3. Jupyter မရှိခြင်း

**နောက်ခံ:** Notebook များသည် အဓိက သင်ကြားရေးအရင်းအမြစ်ဖြစ်သည်။

**ရောဂါလက္ခဏာများ:**
- Error: `jupyter: command not found`
- Notebook များကို မဖွင့်နိုင်ခြင်း

**ဖြစ်နိုင်သော အကြောင်းရင်းများ:**
- Jupyter မရှိခြင်း

**ဖြေရှင်းနည်းများ:**
1. **Jupyter Notebook ကို Install လုပ်ပါ။**  
   ```bash
   pip install notebook
   ```
   သို့မဟုတ် Anaconda ကို အသုံးပြုပါက:
   ```bash
   conda install notebook
   ```
2. **Jupyter Notebook ကို စတင်ပါ။**  
   ```bash
   jupyter notebook
   ```

### 4. Dependency Version Conflict

**နောက်ခံ:** Package version များ မကိုက်ညီပါက Project များ ပျက်စီးနိုင်သည်။

**ရောဂါလက္ခဏာများ:**
- Version မကိုက်ညီသော Error သို့မဟုတ် Warning

**ဖြစ်နိုင်သော အကြောင်းရင်းများ:**
- အဟောင်း Python package များ သို့မဟုတ် Conflict ဖြစ်နေသော package များ

**ဖြေရှင်းနည်းများ:**
1. **သန့်ရှင်းသော environment တွင် Install လုပ်ပါ။**  
   အဟောင်း venv/conda env ကို ဖျက်ပြီး အသစ်တစ်ခုကို ဖန်တီးပါ။
2. **တိကျသော version များကို အသုံးပြုပါ။**  
   အမြဲ run လုပ်ပါ:
   ```bash
   pip install -r requirements.txt
   ```
   မအောင်မြင်ပါက README တွင် ဖော်ပြထားသော missing package များကို လက်ဖြင့် Install လုပ်ပါ။

---

## Configuration ပြဿနာများ

### 5. Environment Variable များ မရှိခြင်း

**နောက်ခံ:** Module တချို့တွင် key, token သို့မဟုတ် config setting များ လိုအပ်နိုင်သည်။

**ရောဂါလက္ခဏာများ:**
- Error: `KeyError` သို့မဟုတ် configuration မရှိခြင်းအကြောင်း Warning

**ဖြစ်နိုင်သော အကြောင်းရင်းများ:**
- လိုအပ်သော environment variable မရှိခြင်း

**ဖြေရှင်းနည်းများ:**
1. **`.env.example` သို့မဟုတ် ဆင်တူသော file များကို စစ်ဆေးပါ။**
2. **`.env` file တစ်ခု ဖန်တီးပြီး လိုအပ်သောတန်ဖိုးများဖြည့်ပါ။**
3. **Environment variable များကို set လုပ်ပြီးနောက် terminal သို့မဟုတ် IDE ကို ပြန်ဖွင့်ပါ။**

---

## Notebook များကို အလုပ်လုပ်စေခြင်း

### 6. Notebook မဖွင့်နိုင်ခြင်း သို့မဟုတ် Run မလုပ်နိုင်ခြင်း

**နောက်ခံ:** Jupyter notebook များသည် သင့်စက်ပေါ်မှာ မှန်ကန်စွာ setup လုပ်ထားရန် လိုအပ်သည်။

**ရောဂါလက္ခဏာများ:**
- Notebook မဖွင့်နိုင်ခြင်း
- Browser မအလိုအလျောက် မဖွင့်ခြင်း

**ဖြစ်နိုင်သော အကြောင်းရင်းများ:**
- Jupyter မရှိခြင်း
- Browser configuration ပြဿနာများ

**ဖြေရှင်းနည်းများ:**
1. **Jupyter ကို Install လုပ်ပါ (Installation ပြဿနာများတွင် ဖော်ပြထားသည်။)**
2. **Notebook များကို လက်ဖြင့် ဖွင့်ပါ။**
   - Terminal မှ URL ကို (ဥပမာ `http://localhost:8888/?token=...`) ကူးယူပြီး Browser တွင် Paste လုပ်ပါ။

### 7. Kernel Crash ဖြစ်ခြင်း သို့မဟုတ် ရပ်တန့်ခြင်း

**နောက်ခံ:** Notebook kernel များသည် resource limit သို့မဟုတ် code error များကြောင့် crash ဖြစ်နိုင်သည်။

**ရောဂါလက္ခဏာများ:**
- Kernel သေသွားခြင်း သို့မဟုတ် အကြိမ်ကြိမ် restart ဖြစ်ခြင်း
- Memory မလုံလောက်ခြင်း error

**ဖြစ်နိုင်သော အကြောင်းရင်းများ:**
- Dataset များကြီးမားခြင်း
- Code သို့မဟုတ် package မကိုက်ညီခြင်း

**ဖြေရှင်းနည်းများ:**
1. **Kernel ကို Restart လုပ်ပါ။**  
   Jupyter တွင် "Restart Kernel" ခလုတ်ကို အသုံးပြုပါ။
2. **Memory အသုံးပြုမှုကို စစ်ဆေးပါ။**  
   မလိုအပ်သော application များကို ပိတ်ပါ။
3. **Notebook များကို Cloud Platform များပေါ်တွင် Run လုပ်ပါ။**  
   [Google Colab](https://colab.research.google.com/) သို့မဟုတ် [Azure Notebooks](https://notebooks.azure.com/) ကို အသုံးပြုပါ။

---

## Performance ပြဿနာများ

### 8. Notebook များ အလွန်နှေးကွေးခြင်း

**နောက်ခံ:** AI task တချို့တွင် memory နှင့် CPU အလွန်များစွာ လိုအပ်သည်။

**ရောဂါလက္ခဏာများ:**
- Run လုပ်ရာတွင် နှေးကွေးခြင်း
- Laptop fan အလွန်လှုပ်ရှားခြင်း

**ဖြစ်နိုင်သော အကြောင်းရင်းများ:**
- Dataset သို့မဟုတ် model များကြီးမားခြင်း
- System resource မလုံလောက်ခြင်း

**ဖြေရှင်းနည်းများ:**
1. **Cloud Platform ကို အသုံးပြုပါ။**
   - Notebook ကို Colab သို့မဟုတ် Azure Notebooks သို့ upload လုပ်ပါ။
2. **Dataset အရွယ်အစားကို လျှော့ချပါ။**
   - လေ့ကျင့်ရန် sample data ကို အသုံးပြုပါ။
3. **မလိုအပ်သော program များကို ပိတ်ပါ။**
   - System RAM ကို လွတ်လပ်စေပါ။

---

## Textbook Website ပြဿနာများ

### 9. Chapter မဖွင့်နိုင်ခြင်း

**နောက်ခံ:** Online textbook သည် သင်ခန်းစာများနှင့် chapter များကို ပြသသည်။

**ရောဂါလက္ခဏာများ:**
- Chapter (ဥပမာ Transformers/BERT) မရှိခြင်း သို့မဟုတ် မဖွင့်နိုင်ခြင်း

**အတည်ပြုထားသော ပြဿနာ:**  
- [Issue #303](https://github.com/microsoft/AI-For-Beginners/issues/303): “18 Transformers. BERT. can't be opened on the textbook website.” Filename error (`READMEtransformers.md` အစား `README.md`) ကြောင့် ဖြစ်သည်။

**ဖြေရှင်းနည်းများ:**
1. **File rename error များကို စစ်ဆေးပါ။**  
   Contributor ဖြစ်ပါက chapter file များကို `README.md` ဟု အမည်ပေးထားကြောင်း သေချာပါစေ။
2. **Missing file များကို Report လုပ်ပါ။**  
   Chapter အမည်နှင့် error အချက်အလက်များဖြင့် GitHub issue တစ်ခု ဖွင့်ပါ။

---

## Contributing ပြဿနာများ

### 10. PR မလက်ခံခြင်း သို့မဟုတ် Build မအောင်မြင်ခြင်း

**နောက်ခံ:** Contribution များသည် test များကို ဖြတ်သန်းရမည်ဖြစ်ပြီး guideline များကို လိုက်နာရမည်။

**ရောဂါလက္ခဏာများ:**
- Pull request ကို ငြင်းပယ်ခြင်း
- CI/CD pipeline error

**ဖြစ်နိုင်သော အကြောင်းရင်းများ:**
- Test fail ဖြစ်ခြင်း
- Coding standard မလိုက်နာခြင်း

**ဖြေရှင်းနည်းများ:**
1. **Contribution guideline များကို ဖတ်ပါ။**
   - Repository ၏ [CONTRIBUTING.md](https://github.com/microsoft/AI-For-Beginners/blob/main/CONTRIBUTING.md) ကို လိုက်နာပါ။
2. **Push လုပ်မီ Test များကို Local တွင် Run လုပ်ပါ။**
3. **Linting rule သို့မဟုတ် formatting requirement များကို စစ်ဆေးပါ။**

---

## FAQ

### Module တစ်ခုချင်းစီအတွက် အကူအညီကို ဘယ်မှာ ရှာနိုင်မလဲ?
- Module တစ်ခုချင်းစီတွင် မိမိ၏ README ရှိသည်။ Setup နှင့် အသုံးပြုမှုအကြံဉာဏ်များအတွက် အဲဒီမှာ စတင်ပါ။

### Bug report သို့မဟုတ် feature request ကို ဘယ်လိုလုပ်ရမလဲ?
- [GitHub Issue ဖွင့်ပါ](https://github.com/microsoft/AI-For-Beginners/issues/new) သို့မဟုတ် ရှင်းလင်းသောဖော်ပြချက်နှင့် ပြဿနာကို ပြန်လုပ်နိုင်သောအဆင့်များကို ထည့်သွင်းပါ။

### ဤပြဿနာစာရင်းတွင် မပါဝင်သော ပြဿနာအတွက် အကူအညီတောင်းနိုင်မလား?
- တောင်းနိုင်ပါသည်! ရှိပြီးသား issue များကို ရှာဖွေပြီး သင့်ပြဿနာကို မတွေ့ပါက အသစ် issue တစ်ခု ဖွင့်ပါ။

---

## အကူအညီရယူခြင်း

- **Issue စစ်ဆေးပါ:** [GitHub Issues](https://github.com/microsoft/AI-For-Beginners/issues)
- **မေးခွန်းမေးပါ:** GitHub Discussions သို့မဟုတ် issue တစ်ခု ဖွင့်ပါ။
- **Community:** Chat/forum option များအတွက် repository link များကို ကြည့်ပါ။

---

_နောက်ဆုံးအပ်ဒိတ်: 2025-09-20_

---

**အကြောင်းကြားချက်**:  
ဤစာရွက်စာတမ်းကို AI ဘာသာပြန်ဝန်ဆောင်မှု [Co-op Translator](https://github.com/Azure/co-op-translator) ကို အသုံးပြု၍ ဘာသာပြန်ထားပါသည်။ ကျွန်ုပ်တို့သည် တိကျမှုအတွက် ကြိုးစားနေသော်လည်း အလိုအလျောက် ဘာသာပြန်မှုများတွင် အမှားများ သို့မဟုတ် မမှန်ကန်မှုများ ပါဝင်နိုင်သည်ကို သတိပြုပါ။ မူရင်းဘာသာစကားဖြင့် ရေးသားထားသော စာရွက်စာတမ်းကို အာဏာတရ အရင်းအမြစ်အဖြစ် သတ်မှတ်သင့်ပါသည်။ အရေးကြီးသော အချက်အလက်များအတွက် လူက ဘာသာပြန်မှုကို အသုံးပြုရန် အကြံပြုပါသည်။ ဤဘာသာပြန်မှုကို အသုံးပြုခြင်းမှ ဖြစ်ပေါ်လာသော အလွဲအမှားများ သို့မဟုတ် အနားယူမှုများအတွက် ကျွန်ုပ်တို့သည် တာဝန်မယူပါ။