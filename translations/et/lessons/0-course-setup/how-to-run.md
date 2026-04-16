# Kuidas Koodi Käivitada

See õppekava sisaldab palju täidetavaid näiteid ja töötoad, mida soovite jooksutada. Selleks peate saama käivitada Python koodi Jupyter märkmikes, mis on selle õppekava osana esitatud. Koodi käivitamiseks on teil mitu võimalust:

## Käivita lokaalselt oma arvutis

Koodi käivitamiseks lokaalselt oma arvutis on vajalik Python'i paigaldus. Üks soovitus on installida **[miniconda](https://conda.io/en/latest/miniconda.html)** – see on üsna kerge paigaldus, mis toetab `conda` pakihaldurit erinevate Python'i **virtuaalsete keskkondade** jaoks.

Pärast miniconda paigaldamist kloonige hoidla ja looge selle kursuse jaoks virtuaalne keskkond:

```bash
git clone http://github.com/microsoft/ai-for-beginners
cd ai-for-beginners
conda env create --name ai4beg --file .devcontainer/environment.yml
conda activate ai4beg
```

### Kasutades Visual Studio Code koos Python laiendiga

Seda õppekava on kõige parem kasutada, kui avate selle [Visual Studio Code’is](http://code.visualstudio.com/?WT.mc_id=academic-77998-cacaste) koos [Python laiendiga](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-77998-cacaste).

> **Märkus**: Kui kloonite ja avate kausta VS Code’is, soovitab see automaatselt paigaldada Python laiendused. Samuti peate paigaldama miniconda nagu eespool kirjeldatud.

> **Märkus**: Kui VS Code soovitab teil hoidlale konteineris uuesti ligi pääseda, peaksite selle keelduma, et kasutada lokaalset Python'i paigaldust.

### Kasutades Jupyterit brauseris

Võite kasutada ka Jupyter keskkonda brauserist oma arvutis. Nii klassikaline Jupyter kui ka JupyterHub pakuvad mugavat arenduskeskkonda automaatse täienduse, koodi esiletõstmise jms funktsioonidega.

Jupyterit käivitamiseks lokaalselt minge kursuse kataloogi ning käivitage:

```bash
jupyter notebook
```
 või  
```bash
jupyterhub
```
  
Seejärel saate minna mis tahes `.ipynb` faili juurde, avada selle ja alustada tööd.

### Käivitamine konteineris

Üks alternatiiv Python'i paigaldamisele on koodi käivitamine konteineris. Kuna meie hoidla sisaldab spetsiaalset `.devcontainer` kausta, mis juhendab konteineri ehitamist selle hoidlaga, pakub VS Code võimalust hoidlale konteineris uuesti ligi pääseda. Selleks on vajalik Docker’i installatsioon ja see on ka keerulisem, seega soovitame seda rohkem kogenud kasutajatele.

## Käivitamine pilves

Kui te ei soovi Pythonit lokaalselt paigaldada, kuid teil on ligipääs mõnele pilveteenusele, on hea alternatiiv koodi käivitamine pilvest. Seda saab teha mitmel viisil:

* Kasutades **[GitHub Codespaces](https://github.com/features/codespaces)**, mis on teile GitHubis loodav virtuaalne keskkond, mida pääseb ligi VS Code’i brauseri kaudu. Kui teil on Codespaces’i ligipääs, saate lihtsalt hoidla lehel vajutada nuppu **Code**, alustada codespace’i ning hakata kohe koodi jooksutama.
* Kasutades **[Binderit](https://mybinder.org/v2/gh/microsoft/ai-for-beginners/HEAD)**. [Binder](https://mybinder.org) pakub tasuta arvutusressursse pilves, mis võimaldab teil GitHubi koodi mugavalt testida. Esilehel on nupp, mis avab hoidla Binderis – see viib teid rapidamente Binderi lehele, mis ehitab taustal konteineri ja käivitab teie jaoks sujuvalt Jupyter veebiliidese.

> **Märkus**: Kuritarvituste vältimiseks on Binderi ligipääs mõnele veebiallikale piiratud. See võib takistada mõnel koodil toimimast, mis alla laadib mudeleid ja/või andmestasid avalikust internetist. Võite vajada mõnda lahendust nende piirangute vältimiseks. Samuti on Binderi pakutavad arvutusressursid üsna piiratud, mistõttu treeningud võivad olla aeglased, eriti hilisemates keerulisemates õppetundides.

## Käivitamine pilves koos GPU-toega

Mõned õppetunnid selles õppekavas kasutaksid oluliselt GPU-d, mis muudab mudelite treenimise palju kiiremaks. GPU toe olemasolu on eriti kasulik. Mõned võimalused:

* Loo [Data Science Virtual Machine](https://docs.microsoft.com/learn/modules/intro-to-azure-data-science-virtual-machine/?WT.mc_id=academic-77998-cacaste) ja ühenda sellega Jupyteri kaudu. Saate kloonida hoidla otse masinale ning alustada õppimist. NC-seeria VM-id toetavad GPU-d.

> **Märkus**: Mõned tellimused, sh Azure for Students, ei paku vaikimisi GPU tuge. Võib-olla peate esitama tehnilise toe taotluse täiendavate GPU tuumade saamiseks.

* Loo [Azure Machine Learning Workspace](https://azure.microsoft.com/services/machine-learning/?WT.mc_id=academic-77998-cacaste) ja kasuta seal Jupyter märkmiku funktsiooni. [See video](https://azure-for-academics.github.io/quickstart/azureml-papers/) näitab, kuidas kloonida hoidla Azure ML märkmikku ja seda kasutada.

Võite kasutada ka Google Colabit, mis pakub mõningast tasuta GPU tuge, ning üles laadida sinna Jupyteri märkmikud, mida sealt ükshaaval käivitada.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vastutusest loobumine**:
See dokument on tõlgitud kasutades AI tõlke teenust [Co-op Translator](https://github.com/Azure/co-op-translator). Kuigi püüame tagada täpsust, palun arvestage, et automaatsed tõlked võivad sisaldada vigu või ebatäpsusi. Algne dokument selle emakeeles tuleks pidada autoriteetseks allikaks. Olulise info puhul soovitatakse kasutada professionaalset inimtõlget. Me ei vastuta selle tõlke kasutamisest tulenevate arusaamatuste ega valesti mõistmiste eest.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->