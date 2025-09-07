<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "7df19702b8d2d3f7c4238c51bec2c8fc",
  "translation_date": "2025-08-25T21:05:27+00:00",
  "source_file": "lessons/0-course-setup/how-to-run.md",
  "language_code": "sw"
}
-->
# Jinsi ya Kuendesha Msimbo

Mtaala huu una mifano mingi inayoweza kutekelezwa na maabara ambayo ungependa kuendesha. Ili kufanya hivyo, unahitaji uwezo wa kutekeleza msimbo wa Python katika Jupyter Notebooks zinazotolewa kama sehemu ya mtaala huu. Una chaguo kadhaa za kuendesha msimbo:

## Kuendesha kwenye Kompyuta Yako

Ili kuendesha msimbo kwenye kompyuta yako, unahitaji kuwa na toleo fulani la Python lililowekwa. Ninapendekeza sana kusakinisha **[miniconda](https://conda.io/en/latest/miniconda.html)** - ni usakinishaji mwepesi unaosaidia meneja wa kifurushi cha `conda` kwa mazingira tofauti ya **Python**.

Baada ya kusakinisha miniconda, unahitaji kunakili hifadhi na kuunda mazingira ya kawaida yatakayotumika kwa kozi hii:

```bash
git clone http://github.com/microsoft/ai-for-beginners
cd ai-for-beginners
conda env create --name ai4beg --file .devcontainer/environment.yml
conda activate ai4beg
```

### Kutumia Visual Studio Code na Kiendelezi cha Python

Njia bora zaidi ya kutumia mtaala huu ni kuufungua katika [Visual Studio Code](http://code.visualstudio.com/?WT.mc_id=academic-77998-cacaste) na [Python Extension](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-77998-cacaste).

> **Note**: Mara tu unapokopi na kufungua folda katika VS Code, itakupendekezea kusakinisha viendelezi vya Python. Pia utahitaji kusakinisha miniconda kama ilivyoelezwa hapo juu.

> **Note**: Ikiwa VS Code inapendekeza kufungua hifadhi katika kontena, unapaswa kukataa hili ili kutumia usakinishaji wa Python wa ndani.

### Kutumia Jupyter kwenye Kivinjari

Unaweza pia kutumia mazingira ya Jupyter moja kwa moja kutoka kwenye kivinjari kwenye kompyuta yako. Kwa kweli, Jupyter ya kawaida na Jupyter Hub hutoa mazingira mazuri ya maendeleo yenye uwezo wa kukamilisha msimbo kiotomatiki, kuonyesha rangi ya msimbo, n.k.

Ili kuanza Jupyter ndani ya nchi, nenda kwenye folda ya kozi, na utekeleze:

```bash
jupyter notebook
```
au
```bash
jupyterhub
```
Kisha unaweza kuvinjari faili zozote za `.ipynb`, kuzifungua na kuanza kufanya kazi.

### Kuendesha katika Kontena

Njia mbadala ya usakinishaji wa Python ni kuendesha msimbo katika kontena. Kwa kuwa hifadhi yetu ina folda maalum ya `.devcontainer` inayotoa maelekezo ya jinsi ya kujenga kontena kwa hifadhi hii, VS Code itakupendekezea kufungua msimbo katika kontena. Hii itahitaji usakinishaji wa Docker, na pia itakuwa ngumu zaidi, kwa hivyo tunapendekeza hii kwa watumiaji wenye uzoefu zaidi.

## Kuendesha Mtandaoni

Ikiwa hutaki kusakinisha Python ndani ya nchi, na una rasilimali za wingu - njia nzuri ni kuendesha msimbo mtandaoni. Kuna njia kadhaa za kufanya hivi:

* Kutumia **[GitHub Codespaces](https://github.com/features/codespaces)**, ambayo ni mazingira ya kawaida yaliyoundwa kwa ajili yako kwenye GitHub, yanayopatikana kupitia kiolesura cha kivinjari cha VS Code. Ikiwa una ufikiaji wa Codespaces, unaweza kubofya kitufe cha **Code** kwenye hifadhi, kuanzisha codespace, na kuanza mara moja.
* Kutumia **[Binder](https://mybinder.org/v2/gh/microsoft/ai-for-beginners/HEAD)**. [Binder](https://mybinder.org) ni rasilimali za bure za kompyuta zinazotolewa mtandaoni kwa watu kama wewe kujaribu msimbo kwenye GitHub. Kuna kitufe kwenye ukurasa wa mbele kufungua hifadhi katika Binder - hii inapaswa kukuchukua haraka kwenye tovuti ya Binder, ambayo itajenga kontena msingi na kuanzisha kiolesura cha wavuti cha Jupyter kwa urahisi.

> **Note**: Ili kuzuia matumizi mabaya, Binder imezuia ufikiaji wa baadhi ya rasilimali za wavuti. Hii inaweza kuzuia baadhi ya misimbo inayopakua mifano na/au seti za data kutoka mtandao wa umma kufanya kazi. Unaweza kuhitaji kutafuta njia mbadala. Pia, rasilimali za kompyuta zinazotolewa na Binder ni za msingi sana, kwa hivyo mafunzo yatakuwa polepole, hasa katika masomo magumu zaidi.

## Kuendesha Mtandaoni na GPU

Baadhi ya masomo ya baadaye katika mtaala huu yatanufaika sana na msaada wa GPU, kwa sababu vinginevyo mafunzo yatakuwa ya polepole sana. Kuna chaguo chache unazoweza kufuata, hasa ikiwa una ufikiaji wa wingu kupitia [Azure for Students](https://azure.microsoft.com/free/students/?WT.mc_id=academic-77998-cacaste), au kupitia taasisi yako:

* Unda [Data Science Virtual Machine](https://docs.microsoft.com/learn/modules/intro-to-azure-data-science-virtual-machine/?WT.mc_id=academic-77998-cacaste) na uunganishe nayo kupitia Jupyter. Unaweza kisha kunakili hifadhi moja kwa moja kwenye mashine, na kuanza kujifunza. Mashine za NC-series zina msaada wa GPU.

> **Note**: Baadhi ya usajili, ikiwa ni pamoja na Azure for Students, hazitoi msaada wa GPU moja kwa moja. Unaweza kuhitaji kuomba nyongeza ya cores za GPU kupitia ombi la msaada wa kiufundi.

* Unda [Azure Machine Learning Workspace](https://azure.microsoft.com/services/machine-learning/?WT.mc_id=academic-77998-cacaste) na kisha utumie kipengele cha Notebook huko. [Video hii](https://azure-for-academics.github.io/quickstart/azureml-papers/) inaonyesha jinsi ya kunakili hifadhi kwenye daftari la Azure ML na kuanza kuitumia.

Unaweza pia kutumia Google Colab, ambayo inakuja na msaada wa GPU wa bure, na kupakia Jupyter Notebooks huko ili kuzitekeleza moja baada ya nyingine.

**Kanusho**:  
Hati hii imetafsiriwa kwa kutumia huduma ya kutafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kuhakikisha usahihi, tafadhali fahamu kuwa tafsiri za kiotomatiki zinaweza kuwa na makosa au kutokuwa sahihi. Hati ya asili katika lugha yake ya awali inapaswa kuzingatiwa kama chanzo cha mamlaka. Kwa taarifa muhimu, tafsiri ya kitaalamu ya binadamu inapendekezwa. Hatutawajibika kwa kutoelewana au tafsiri zisizo sahihi zinazotokana na matumizi ya tafsiri hii.