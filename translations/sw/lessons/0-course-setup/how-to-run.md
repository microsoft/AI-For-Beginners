# Jinsi ya Kuendesha Msimbo

Mtaala huu una mifano mingi inayotekelezeka na maabara ambazo ungependa kuendesha. Ili kufanya hivyo, unahitaji uwezo wa kutekeleza msimbo wa Python katika Jupyter Notebooks zinazotolewa kama sehemu ya mtaala huu. Una chaguzi kadhaa za kuendesha msimbo:

## Endesha kwa ndani kwenye kompyuta yako

Ili kuendesha msimbo kwa ndani kwenye kompyuta yako, unahitaji usakinishaji wa Python. Pendekezo moja ni kusakinisha **[miniconda](https://conda.io/en/latest/miniconda.html)** - ni usakinishaji mwepesi unaounga mkono meneja wa kifurushi wa `conda` kwa mazingira tofauti ya Python **virtual environments**.

Baada ya kusakinisha miniconda, nakili (clone) hazina na unda mazingira ya virtual yatakayotumika kwa kozi hii:

```bash
git clone http://github.com/microsoft/ai-for-beginners
cd ai-for-beginners
conda env create --name ai4beg --file .devcontainer/environment.yml
conda activate ai4beg
```

> **Kumbuka kwa Windows**: Ikiwa kuunda mazingira kunashindwa wakati wa kusakinisha `gdk-pixbuf` na `UnicodeDecodeError` inayotaja codec ya `gbk`, wwezeshaji hali ya UTF-8 ya Python kwenye terminal yako na jaribu tena. Tumia sarufi kwa terminal unayotumia:
>
> **PowerShell:**
>
> ```powershell
> $env:PYTHONUTF8 = "1"
> conda env create --name ai4beg --file .devcontainer/environment.yml
> ```
>
> **Command Prompt (`cmd.exe`) au Anaconda Prompt:**
>
> ```cmd
> set PYTHONUTF8=1
> conda env create --name ai4beg --file .devcontainer/environment.yml
> ```
>
> **Bash, ikiwa ni pamoja na Git Bash:**
>
> ```bash
> export PYTHONUTF8=1
> conda env create --name ai4beg --file .devcontainer/environment.yml
> ```
>
> Ikiwa jaribio lililoshindwa liliacha mazingira ya `ai4beg`, zima mazingira hayo na uondoe kabla ya kujaribu tena. Tumia `conda deactivate` kwanza wakati mazingira yakiwa yanafanya kazi:
>
> ```text
> conda deactivate
> conda env remove --name ai4beg
> ```

### Kutumia Visual Studio Code na Ugani wa Python

Mtaala huu unatumika vyema zaidi unapoufungua katika [Visual Studio Code](http://code.visualstudio.com/?WT.mc_id=academic-77998-cacaste) ukiwa na [Python Extension](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-77998-cacaste).

> **Kumbuka**: Mara tu unapofanya clone na ufungue saraka ndani ya VS Code, itapendekeza moja kwa moja kusakinisha ugani wa Python. Pia utalazimika kusakinisha miniconda kama ilivyoelezwa hapo juu.

> **Kumbuka**: Ikiwa VS Code itapendekeza kufungua tena hazina ndani ya kontena, unapaswa kukataa ili utumie usakinishaji wa Python wa ndani.

### Kutumia Jupyter kwenye Kivinjari

Unaweza pia kutumia mazingira ya Jupyter kutoka kwenye kivinjari cha kompyuta yako binafsi. Jupyter ya kawaida na JupyterHub hutoa mazingira rahisi ya maendeleo yenye kukamilisha kiotomatiki, kuangazia msimbo, n.k.

Ili kuanzisha Jupyter kwa ndani, nenda kwenye saraka ya kozi, kisha tekeleza:

```bash
jupyter notebook
```
au
```bash
jupyterhub
```
Kisha unaweza vinjari hadi faili yoyote ya `.ipynb`, ufungue na kuanza kufanya kazi.

### Kuendesha ndani ya kontena

Chaguo jingine badala ya usakinishaji wa Python ni kuendesha msimbo ndani ya kontena. Kwa kuwa hazina yetu inatoa folda maalum ya `.devcontainer` inayotoa maagizo ya jinsi ya kujenga kontena kwa hazina hii, VS Code inatoa fursa ya kufungua tena msimbo ndani ya kontena. Hii itahitaji usakinishaji wa Docker, pia itakuwa ngumu zaidi, hivyo tunapendekeza hii kwa watumiaji wenye uzoefu zaidi.

## Kuendesha kwenye Wingu

Ikiwa hutaki kusakinisha Python kwa ndani, na unayo fursa ya kutumia rasilimali za wingu - chaguo nzuri ni kuendesha msimbo kwenye wingu. Kuna njia kadhaa za kufanya hivyo:

* Kutumia **[GitHub Codespaces](https://github.com/features/codespaces)**, ambayo ni mazingira ya virtual yaliyotengenezwa kwa ajili yako kwenye GitHub, yanayopatikana kupitia kiolesura cha kivinjari cha VS Code. Ikiwa una ufikiaji wa Codespaces, unaweza tu kubofya kitufe cha **Code** kwenye hazina, anzisha codespace, na kuanza haraka.
* Kutumia **[Binder](https://mybinder.org/v2/gh/microsoft/ai-for-beginners/HEAD)**. [Binder](https://mybinder.org) hutoa rasilimali za kompyuta bure zinazotolewa kwenye wingu kwa watu kama wewe kujaribu msimbo fulani kwenye GitHub. Kuna kitufe kwenye ukurasa wa mbele cha kufungua hazina kwenye Binder - hii itakupeleka haraka kwenye tovuti ya binder, ambayo itajenga kontena la msingi na kuanzisha kiolesura cha mtandao cha Jupyter kwako bila matatizo.

> **Kumbuka**: Ili kuzuia matumizi mabaya, Binder ina vizuizi kwenye baadhi ya rasilimali za mtandao. Hii inaweza kuzuia baadhi ya msimbo kufanya kazi, ambao hupakua mifano na/au seti za data kutoka mtandao wa umma. Huenda utahitaji kupata mbinu mbadala. Pia, rasilimali za kompyuta zinazotolewa na Binder ni za msingi kabisa, hivyo mafunzo yatakuwa polepole, hasa katika masomo ya baadaye, zaidi yenye ugumu.

## Kuendesha kwenye Wingu kwa GPU

Baadhi ya masomo ya baadaye katika mtaala huu yangepata faida kubwa kutoka kwa msaada wa GPU. Mafunzo ya modeli, kwa mfano, yanaweza kuwa polepole mno vinginevyo. Kuna chaguzi chache unaweza kufuata, hasa ikiwa una ufikiaji wa wingu kupitia [Azure for Students](https://azure.microsoft.com/free/students/?WT.mc_id=academic-77998-cacaste), au kupitia taasisi yako:

* Unda [Data Science Virtual Machine](https://docs.microsoft.com/learn/modules/intro-to-azure-data-science-virtual-machine/?WT.mc_id=academic-77998-cacaste) na uungane nayo kupitia Jupyter. Basi unaweza nakili hazina moja kwa moja kwenye mashine hiyo, na kuanza kujifunza. NC-series VMs zina msaada wa GPU.

> **Kumbuka**: Baadhi ya usajili, ikiwa ni pamoja na Azure for Students, hazitoi msaada wa GPU moja kwa moja. Huenda utahitaji kuomba cores za ziada za GPU kwa ombi la msaada wa kiufundi.

* Unda [Azure Machine Learning Workspace](https://azure.microsoft.com/services/machine-learning/?WT.mc_id=academic-77998-cacaste) kisha tumia kipengele cha Notebook huko. [Video hii](https://azure-for-academics.github.io/quickstart/azureml-papers/) inaonyesha jinsi ya kufanya clone ya hazina ndani ya daftari la Azure ML na kuanza kuitumia.

Unaweza pia kutumia Google Colab, ambayo inakuja na msaada wa GPU wa bure, na kupakia Jupyter Notebooks huko na kuziendesha moja moja.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Kionyozo**:
Hati hii imetafsiriwa kwa kutumia huduma ya tafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kupata usahihi, tafadhali fahamu kwamba tafsiri za kiotomatiki zinaweza kuwa na makosa au upungufu wa usahihi. Hati ya asili katika lugha yake halisi inapaswa kuchukuliwa kama chanzo cha mamlaka. Kwa taarifa muhimu, tafsiri ya kitaalamu inayofanywa na binadamu inapendekezwa. Hatutojibu kwa kuelewa vibaya au tafsiri potofu zinazotokea kutokana na matumizi ya tafsiri hii.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->