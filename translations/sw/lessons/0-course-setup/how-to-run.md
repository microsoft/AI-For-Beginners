# Jinsi ya Kuendesha Msimbo

Mtaala huu una mifano mingi inayoweza kutekelezwa na maabara ambazo ungependa kuendesha. Ili kufanya hivi, unahitaji uwezo wa kutekeleza msimbo wa Python katika Jupyter Notebooks zinazotolewa kama sehemu ya mtaala huu. Una chaguzi kadhaa za kuendesha msimbo:

## Endesha kwa karibu kwenye kompyuta yako

Ili kuendesha msimbo kwa karibu kwenye kompyuta yako, usakinishaji wa Python unahitajika. Moja ya mapendekezo ni kusakinisha **[miniconda](https://conda.io/en/latest/miniconda.html)** - ni usakinishaji mzito mdogo unaounga mkono meneja wa pakiti `conda` kwa **mazingira pepe** tofauti za Python.

Baada ya kusakinisha miniconda, tengeneza nakala ya hazina na unda mazingira pepe yatakayotumika kwa kozi hii:

```bash
git clone http://github.com/microsoft/ai-for-beginners
cd ai-for-beginners
conda env create --name ai4beg --file .devcontainer/environment.yml
conda activate ai4beg
```

### Kutumia Visual Studio Code na Ongezeko la Python

Mtaala huu unatumika vyema unapoifungua katika [Visual Studio Code](http://code.visualstudio.com/?WT.mc_id=academic-77998-cacaste) pamoja na [Ongezeko la Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-77998-cacaste).

> **Kumbuka**: Mara tu unapochukua nakala na kufungua saraka katika VS Code, itapendekeza kiotomati kusakinisha ongezeko la Python. Pia utahitaji kusakinisha miniconda kama ilivyoelezwa hapo juu.

> **Kumbuka**: Ikiwa VS Code itapendekeza kufungua tena hazina katika chombo (container), unapaswa kukataa ili kutumia usakinishaji wa Python wenyewe wenyewe.

### Kutumia Jupyter katika Kivinjari

Unaweza pia kutumia mazingira ya Jupyter kutoka kwa kivinjari kwenye kompyuta yako mwenyewe. Jupyter wa kawaida na JupyterHub zote hutoa mazingira mazuri ya maendeleo yenye ukamilishaji wa kiotomatiki, kuangazia msimbo, n.k.

Kuanza Jupyter kwa karibu, nenda kwenye saraka ya kozi, na tekereza:

```bash
jupyter notebook
```
au
```bash
jupyterhub
```
Kisha unaweza kuvinjari kwenye faili yoyote za `.ipynb`, uzifungue na kuanza kufanya kazi.

### Kuendesha katika chombo (container)

Mbali na usakinishaji wa Python, utaratibu mwingine ni kuendesha msimbo katika chombo. Kwa kuwa hazina yetu hutoa folda maalum ya `.devcontainer` inayofundisha jinsi ya kujenga chombo kwa ajili ya hazina hii, VS Code hutoa fursa ya kufungua tena msimbo katika chombo. Hii itahitaji usakinishaji wa Docker, na pia itakuwa na ngumu zaidi, kwa hivyo tunapendekeza hii kwa watumiaji waliobobea zaidi.

## Kuendesha katika Wingu

Ikiwa hutaki kusakinisha Python kwa karibu, na una upatikanaji wa baadhi ya rasilimali za wingu - chaguo zuri ni kuendesha msimbo katika wingu. Kuna njia kadhaa unazoweza kufanya hivi:

* Kutumia **[GitHub Codespaces](https://github.com/features/codespaces)**, ambacho ni mazingira pepe yaliyoandaliwa kwa ajili yako kwenye GitHub, yanayoweza kufikiwa kupitia kiolesura cha kivinjari cha VS Code. Ikiwa una upatikanaji wa Codespaces, unaweza kubofya tu kitufe cha **Code** katika hazina, anza codespace, na kuanza kufanya kazi mara moja.
* Kutumia **[Binder](https://mybinder.org/v2/gh/microsoft/ai-for-beginners/HEAD)**. [Binder](https://mybinder.org) hutoa rasilimali za kompyuta bure mtandaoni kwa watu kama wewe kujaribu msimbo wa GitHub. Kuna kitufe katika ukurasa wa mwanzo kufungua hazina katika Binder - hii itakupeleka haraka kwenye tovuti ya binder, ambayo itajenga chombo cha msingi na kuanzisha kiolesura cha mtandao cha Jupyter kwa urahisi.

> **Kumbuka**: Ili kuzuia matumizi mabaya, Binder ina rasilimali za wavuti zilizo vizuiziwa. Hii inaweza kuzuia baadhi ya misimbo kufanya kazi, ambayo hupakua mifano na/au seti za data kutoka mtandao wa umma. Huenda ukahitaji kupata njia mbadala. Pia, rasilimali za kompyuta zinazotolewa na Binder ni za msingi, hivyo mafunzo yatachukua muda mrefu, hasa katika masomo ya baadaye yenye ugumu zaidi.

## Kuendesha katika Wingu na GPU

Baadhi ya masomo ya baadaye katika mtaala huu yatanufaika sana na msaada wa GPU. Mafunzo ya mfano, kwa mfano, yanaweza kuwa polepole sana vinginevyo. Kuna chaguzi kadhaa unazoweza kufuata, hasa ikiwa una upatikanaji wa wingu kupitia [Azure kwa Wanafunzi](https://azure.microsoft.com/free/students/?WT.mc_id=academic-77998-cacaste), au kupitia taasisi yako:

* Unda [Mashine Pepe ya Sayansi ya Data](https://docs.microsoft.com/learn/modules/intro-to-azure-data-science-virtual-machine/?WT.mc_id=academic-77998-cacaste) na uungane nayo kupitia Jupyter. Kisha unaweza kuunda nakala ya hazina moja kwa moja kwenye mashine, na kuanza kujifunza. VMs za mfululizo wa NC zina msaada wa GPU.

> **Kumbuka**: Baadhi ya usajili, ikiwa ni pamoja na Azure kwa Wanafunzi, hazitoi msaada wa GPU moja kwa moja. Huenda ukahitaji kuomba cores za GPU ziada kupitia ombi la msaada wa kiufundi.

* Unda [Eneo la Kazi la Azure Machine Learning](https://azure.microsoft.com/services/machine-learning/?WT.mc_id=academic-77998-cacaste) kisha tumia kipengele cha Notebook pale. [Video hii](https://azure-for-academics.github.io/quickstart/azureml-papers/) inaonyesha jinsi ya kunakili hazina katika daftari la Azure ML na kuanza kuitumia.

Unaweza pia kutumia Google Colab, ambayo inakuja na msaada wa bure wa GPU, na kupakia Jupyter Notebooks pale kuzikamilisha moja moja.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Kielezi cha Majumuisho**:  
Hati hii imetafsiriwa kwa kutumia huduma ya tafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kwa usahihi, tafadhali fahamu kwamba tafsiri za kiotomatiki zinaweza kuwa na makosa au upungufu wa usahihi. Hati ya awali katika lugha yake ya asili inapaswa kuchukuliwa kama chanzo halali. Kwa taarifa muhimu, tafsiri ya kitaalamu inayofanywa na watu inashauriwa. Hatuwajibiki kwa maelewano au ufafanuzi mbaya unaotokana na matumizi ya tafsiri hii.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->