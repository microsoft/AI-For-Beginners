# Kuidas Koodi Käivitada

See õppekava sisaldab palju käivitatavaid näiteid ja labo töid, mida soovite käivitada. Selleks peate suutma täita Python-koodi Jupyter märkmikutes, mis on selle õppekava osana pakutud. Koodi käivitamiseks on teil mitu võimalust:

## Käivita kohapeal oma arvutis

Koodi käivitamiseks oma arvutis on vaja Python paigaldust. Soovitame installida **[miniconda](https://conda.io/en/latest/miniconda.html)** – see on suhteliselt kerge paigaldus, mis toetab `conda` pakihaldurit erinevate Python **virtuaalsete keskkondade** jaoks.

Pärast miniconda installimist kloonige repostiitorium ja looge selle kursuse jaoks kasutatav virtuaalne keskkond:

```bash
git clone http://github.com/microsoft/ai-for-beginners
cd ai-for-beginners
conda env create --name ai4beg --file .devcontainer/environment.yml
conda activate ai4beg
```

> **Windowsi märkus**: Kui virtuaalse keskkonna loomine ebaõnnestub `gdk-pixbuf` paigaldamise ajal ja kuvatakse `UnicodeDecodeError`, milles mainitakse `gbk` koodekit, aktiveerige terminalis Python UTF-8 režiim ja proovige uuesti. Kasutage terminali süntaksit, mida kasutate:
>
> **PowerShell:**
>
> ```powershell
> $env:PYTHONUTF8 = "1"
> conda env create --name ai4beg --file .devcontainer/environment.yml
> ```
>
> **Käsurida (`cmd.exe`) või Anaconda käsurida:**
>
> ```cmd
> set PYTHONUTF8=1
> conda env create --name ai4beg --file .devcontainer/environment.yml
> ```
>
> **Bash, sealhulgas Git Bash:**
>
> ```bash
> export PYTHONUTF8=1
> conda env create --name ai4beg --file .devcontainer/environment.yml
> ```
>
> Kui varasem ebaõnnestunud katse jättis `ai4beg` keskkonna alles, keelake see ja eemaldage see enne uue katse tegemist. Kasutage esmalt `conda deactivate`, kui virtuaalne keskkond on aktiivne:
>
> ```text
> conda deactivate
> conda env remove --name ai4beg
> ```

### Visual Studio Code kasutamine Python laiendusega

Seda õppekava on kõige parem kasutada, kui avate selle [Visual Studio Code’is](http://code.visualstudio.com/?WT.mc_id=academic-77998-cacaste) koos [Python Extension](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-77998-cacaste).

> **Märkus**: Kui olete repostiitoriumi klooninud ja avanud kataloogi VS Code’is, soovitab see automaatselt paigaldada Python laiendused. Lisaks peate installima miniconda nagu ülal kirjeldatud.

> **Märkus**: Kui VS Code soovitab repostiitoriumi avada konteineris, peaksite sellest keelduma, et kasutada kohaliku Python installatsiooni.

### Jupyteri kasutamine brauseris

Samuti võite kasutada Jupyteri keskkonda otse oma arvuti brauserist. Nii klassikaline Jupyter kui ka JupyterHub pakuvad mugavat arenduskeskkonda automaatse täienduse, koodi esiletõstmise jms-ga.

Jupyteri kohaliku alustamiseks minge kursuse kausta ja käivitage:

```bash
jupyter notebook
```
või
```bash
jupyterhub
```
Seejärel saate liikuda ükskõik millisesse `.ipynb` faili, avada selle ja alustada tööd.

### Käivitamine konteineris

Üks alternatiiv Python paigaldusele on koodi käivitamine konteineris. Kuna meie repostiitorium sisaldab spetsiaalset `.devcontainer` kausta, mis juhendab, kuidas koostada selles repostiitoriumis konteinerit, pakub VS Code võimalust selle koodi konteineris uuesti avada. Selleks on vaja Docker’i paigaldust, mis on veidi keerukam, seega soovitame seda kogenuimatele kasutajatele.

## Käivitamine pilves

Kui te ei soovi Pythonit kohapeal paigaldada ja teil on juurdepääs mõnele pilveteenusele, on hea alternatiiv koodi käivitamine pilves. Seda saab teha mitmel moel:

* Kasutades **[GitHub Codespaces](https://github.com/features/codespaces)**, mis on teie jaoks GitHubis loodud virtuaalne keskkond, millele pääseb ligi VS Code brauseriliidese kaudu. Kui teil on Codespacese juurdepääs, piisab repo **Code** nupule vajutamisest, et koodiruum alustada ja kiirelt tööga pihta hakata.
* Kasutades **[Binderit](https://mybinder.org/v2/gh/microsoft/ai-for-beginners/HEAD)**. [Binder](https://mybinder.org) pakub vaba arvutusvõimsust pilves inimestele nagu teie, et testida GitHubis koodi. Kodulehel on nupp, mis avab repostiitoriumi Binderis – see viib teid kiiresti Binderi lehele, mis koostab taustal konteineri ja avab sujuvalt Jupyteri veebiliidese.

> **Märkus**: Kuritarvituste vältimiseks on Binderi juurdepääs mõnele veebiteenusele blokeeritud. See võib takistada mõnel koodil töötada, kui see otsib mudeleid ja/või andmestikke avalikust internetist. Võite vajada mõningaid lahendusi. Lisaks on Binderi poolt pakutav arvutusressurss üsna lihtne, seega on treeningud aeglased, eriti hilisemates, keerukamates õppetundides.

## Käivitamine pilves GPU-ga

Selle õppekava mõned hilisemad õppetunnid kasutaksid suurel määral GPU tuge. Mudelite treenimine võib muidu olla valusalt aeglane. Teil on mõned võimalused, eriti kui teil on pilve juurdepääs kas [Azure for Students](https://azure.microsoft.com/free/students/?WT.mc_id=academic-77998-cacaste) kaudu või oma asutuse kaudu:

* Looge [Data Science Virtual Machine](https://docs.microsoft.com/learn/modules/intro-to-azure-data-science-virtual-machine/?WT.mc_id=academic-77998-cacaste) ja ühenduge sellega Jupyteri kaudu. Seejärel saab repostiitoriumi reponeerida otse masinasse ja alustada õppimist. NC-seeria masinatel on GPU tugi.

> **Märkus**: Mõned tellimused, sealhulgas Azure for Students, ei paku GPU tuge vaikimisi. Võite vajada täiendavate GPU tuumade küsimist tehnilise toe kaudu.

* Looge [Azure Machine Learning Workspace](https://azure.microsoft.com/services/machine-learning/?WT.mc_id=academic-77998-cacaste) ja kasutage seal Notebook funktsiooni. [See video](https://azure-for-academics.github.io/quickstart/azureml-papers/) näitab, kuidas kloonida repostiitorium Azure ML märkmikku ja alustada selle kasutamist.

Võite kasutada ka Google Colabi, mis tuleb mõningase tasuta GPU toetusega, ja üles laadida seal Jupyteri märkmikud, et neid ükshaaval täita.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Lahtiütlus**:
See dokument on tõlgitud kasutades AI tõlketeenust [Co-op Translator](https://github.com/Azure/co-op-translator). Kuigi me püüdleme täpsuse poole, palun pange tähele, et automatiseeritud tõlgetes võib esineda vigu või ebatäpsusi. Originaaldokument selle emakeeles tuleks pidada autoriteetseks allikaks. Olulise teabe puhul soovitatakse kasutada professionaalset inimtõlget. Me ei vastuta selle tõlkega seotud eksimustest või valesti mõistmistest.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->