<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "7df19702b8d2d3f7c4238c51bec2c8fc",
  "translation_date": "2025-10-11T11:35:05+00:00",
  "source_file": "lessons/0-course-setup/how-to-run.md",
  "language_code": "et"
}
-->
# Koodi käivitamine

See õppekava sisaldab palju käivitatavaid näiteid ja laboreid, mida soovite proovida. Selleks on teil vaja võimalust käivitada Python-koodi Jupyter Notebookides, mis on osa sellest õppekavast. Koodi käivitamiseks on mitu võimalust:

## Käivita kohalikult oma arvutis

Koodi kohalikuks käivitamiseks oma arvutis peate olema installinud mõne Python'i versiooni. Soovitan isiklikult installida **[miniconda](https://conda.io/en/latest/miniconda.html)** - see on kerge paigaldus, mis toetab `conda` paketihaldurit erinevate Python'i **virtuaalsete keskkondade** jaoks.

Pärast miniconda installimist peate kloonima repositooriumi ja looma virtuaalse keskkonna, mida kasutatakse selle kursuse jaoks:

```bash
git clone http://github.com/microsoft/ai-for-beginners
cd ai-for-beginners
conda env create --name ai4beg --file .devcontainer/environment.yml
conda activate ai4beg
```

### Visual Studio Code'i kasutamine koos Python'i laiendusega

Tõenäoliselt on parim viis õppekava kasutamiseks avada see [Visual Studio Code'is](http://code.visualstudio.com/?WT.mc_id=academic-77998-cacaste) koos [Python'i laiendusega](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-77998-cacaste).

> **Märkus**: Kui kloonite ja avate kataloogi VS Code'is, soovitab see automaatselt Python'i laienduste installimist. Samuti peate installima miniconda, nagu eespool kirjeldatud.

> **Märkus**: Kui VS Code soovitab teil repositooriumi konteineris uuesti avada, peate selle tagasi lükkama, et kasutada kohalikku Python'i installatsiooni.

### Jupyter'i kasutamine brauseris

Samuti saate kasutada Jupyter'i keskkonda otse brauseris oma arvutis. Tegelikult pakuvad nii klassikaline Jupyter kui ka Jupyter Hub üsna mugavat arenduskeskkonda automaatse täiendamise, koodi esiletõstmise jms funktsioonidega.

Jupyter'i kohalikuks käivitamiseks minge kursuse kataloogi ja käivitage:

```bash
jupyter notebook
```
või
```bash
jupyterhub
```
Seejärel saate liikuda mis tahes `.ipynb` failini, avada selle ja alustada tööd.

### Käivitamine konteineris

Alternatiiv Python'i installatsioonile oleks koodi käivitamine konteineris. Kuna meie repositoorium sisaldab spetsiaalset `.devcontainer` kausta, mis juhendab, kuidas selle repositooriumi jaoks konteinerit ehitada, pakub VS Code teile võimalust avada kood konteineris. See nõuab Docker'i installimist ja on ka keerulisem, seega soovitame seda kogenumatele kasutajatele.

## Käivitamine pilves

Kui te ei soovi Python'i kohalikult installida ja teil on juurdepääs mõnele pilveressursile, siis hea alternatiiv oleks koodi käivitamine pilves. Selleks on mitu võimalust:

* Kasutades **[GitHub Codespaces](https://github.com/features/codespaces)**, mis on GitHub'is loodud virtuaalne keskkond, millele pääseb ligi VS Code'i brauseriliidese kaudu. Kui teil on juurdepääs Codespaces'ile, saate lihtsalt klõpsata repositooriumis **Code** nupul, käivitada Codespace'i ja alustada tööd hetkega.
* Kasutades **[Binder](https://mybinder.org/v2/gh/microsoft/ai-for-beginners/HEAD)**. [Binder](https://mybinder.org) pakub tasuta pilvearvutusressursse, et testida GitHub'is olevat koodi. Esilehel on nupp, mis avab repositooriumi Binder'is - see viib teid kiiresti Binder'i saidile, mis ehitab aluseks oleva konteineri ja käivitab Jupyter'i veebiliidese sujuvalt.

> **Märkus**: Kuritarvituste vältimiseks on Binder'il juurdepääs mõnele veebiresursile blokeeritud. See võib takistada mõne koodi töötamist, mis laadib mudeleid ja/või andmekogumeid avalikust internetist. Võimalik, et peate leidma mõningaid lahendusi. Samuti on Binder'i pakutavad arvutusressursid üsna piiratud, mistõttu treenimine on aeglane, eriti hilisemates keerukamates tundides.

## Käivitamine pilves GPU-ga

Mõned hilisemad õppetunnid selles õppekavas oleksid GPU toe korral palju tõhusamad, sest muidu on treenimine väga aeglane. Siin on mõned võimalused, mida saate kasutada, eriti kui teil on juurdepääs pilvele kas [Azure for Students](https://azure.microsoft.com/free/students/?WT.mc_id=academic-77998-cacaste) kaudu või oma asutuse kaudu:

* Looge [Data Science Virtual Machine](https://docs.microsoft.com/learn/modules/intro-to-azure-data-science-virtual-machine/?WT.mc_id=academic-77998-cacaste) ja ühendage sellega Jupyter'i kaudu. Seejärel saate repositooriumi otse masinasse kloonida ja õppimist alustada. NC-seeria virtuaalmasinatel on GPU tugi.

> **Märkus**: Mõned tellimused, sealhulgas Azure for Students, ei paku GPU tuge vaikimisi. Võimalik, et peate tehnilise toe kaudu taotlema täiendavaid GPU tuumasid.

* Looge [Azure Machine Learning Workspace](https://azure.microsoft.com/services/machine-learning/?WT.mc_id=academic-77998-cacaste) ja kasutage seal Notebook'i funktsiooni. [See video](https://azure-for-academics.github.io/quickstart/azureml-papers/) näitab, kuidas kloonida repositoorium Azure ML Notebook'i ja seda kasutama hakata.

Samuti saate kasutada Google Colab'i, mis pakub mõningast tasuta GPU tuge, ja laadida sinna Jupyter Notebook'e, et neid ükshaaval käivitada.

---

**Lahtiütlus**:  
See dokument on tõlgitud AI tõlketeenuse [Co-op Translator](https://github.com/Azure/co-op-translator) abil. Kuigi püüame tagada täpsust, palume arvestada, et automaatsed tõlked võivad sisaldada vigu või ebatäpsusi. Algne dokument selle algses keeles tuleks pidada autoriteetseks allikaks. Olulise teabe puhul soovitame kasutada professionaalset inimtõlget. Me ei vastuta selle tõlke kasutamisest tulenevate arusaamatuste või valesti tõlgenduste eest.