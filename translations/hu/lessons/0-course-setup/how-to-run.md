# Hogyan futtassuk a kódot

Ez a tanterv sok futtatható példát és laboratóriumi gyakorlatot tartalmaz, amelyeket szeretnél futtatni. Ehhez szükséged van arra, hogy a tanterv részeként biztosított Jupyter Notebookokban Python kódot tudj végrehajtani. Több lehetőséged is van a kód futtatására:

## Lokális futtatás a számítógépeden

A kód lokális futtatásához számítógépeden Python telepítés szükséges. Egy ajánlás a **[miniconda](https://conda.io/en/latest/miniconda.html)** telepítése – ez egy viszonylag könnyű telepítés, amely támogatja az `conda` csomagkezelőt különböző Python **virtuális környezetek** kezeléséhez.

Miután telepítetted a miniconda-t, klónozd le a tárolót, és hozz létre egy virtuális környezetet a kurzushoz:

```bash
git clone http://github.com/microsoft/ai-for-beginners
cd ai-for-beginners
conda env create --name ai4beg --file .devcontainer/environment.yml
conda activate ai4beg
```

> **Windows megjegyzés**: Ha az `gdk-pixbuf` telepítése közben a környezet létrehozása sikertelen egy `UnicodeDecodeError`-vel, amely megemlíti az `gbk` kódolót, engedélyezd a Python UTF-8 módját a terminálodban, majd próbáld újra. Használd a terminálodhoz tartozó szintaxist:
>
> **PowerShell:**
>
> ```powershell
> $env:PYTHONUTF8 = "1"
> conda env create --name ai4beg --file .devcontainer/environment.yml
> ```
>
> **Parancssor (`cmd.exe`) vagy Anaconda Prompt:**
>
> ```cmd
> set PYTHONUTF8=1
> conda env create --name ai4beg --file .devcontainer/environment.yml
> ```
>
> **Bash, beleértve a Git Bash-t is:**
>
> ```bash
> export PYTHONUTF8=1
> conda env create --name ai4beg --file .devcontainer/environment.yml
> ```
>
> Ha egy sikertelen próbálkozás hátrahagyta az `ai4beg` környezetet, deaktiváld azt és töröld a környezetet, mielőtt újrapróbálkozol. Először használhatod az `conda deactivate`-t, ha egy környezet aktív:
>
> ```text
> conda deactivate
> conda env remove --name ai4beg
> ```

### Visual Studio Code használata Python bővítménnyel

Ez a tanterv a legjobban használható, ha megnyitod a [Visual Studio Code](http://code.visualstudio.com/?WT.mc_id=academic-77998-cacaste)-ban a [Python bővítménnyel](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-77998-cacaste).

> **Megjegyzés**: Miután klónoztad és megnyitottad a könyvtárat VS Code-ban, automatikusan felajánlja a Python bővítmények telepítését. Illetve telepítened kell a minconda-t is a fentiek szerint.

> **Megjegyzés**: Ha a VS Code javasolja, hogy nyisd meg újra a tárolót egy konténerben, ezt el kell utasítanod, ha helyi Python telepítést szeretnél használni.

### Jupyter használata böngészőben

Használhatsz Jupyter környezetet saját számítógépeden a böngészőből is. Mind a klasszikus Jupyter, mind a JupyterHub kényelmes fejlesztői környezetet biztosít automatikus kiegészítéssel, kódkijelöléssel stb.

A Jupyter lokális indításához menj a kurzus könyvtárába, és futtasd:

```bash
jupyter notebook
```
 vagy
```bash
jupyterhub
```
 Ezután bármelyik `.ipynb` fájlra navigálhatsz, megnyithatod, és elkezdheted a munkát.

### Futtatás konténerben

Egy alternatíva a Python telepítés helyett, ha konténerben futtatod a kódot. Mivel a tárolónk egy speciális `.devcontainer` mappát tartalmaz, amely útmutatást ad a konténer készítéséhez, a VS Code lehetőséget biztosít arra, hogy a kódot konténerben nyisd meg újra. Ehhez szükséges a Docker telepítése, és ez bonyolultabb is lehet, ezért inkább tapasztaltabb felhasználóknak ajánljuk.

## Futtatás a felhőben

Ha nem szeretnél Python-t helyben telepíteni, és van hozzáférésed felhő erőforrásokhoz, jó alternatíva a kód futtatása felhőben. Több módja is van ennek:

* Használhatod a **[GitHub Codespaces](https://github.com/features/codespaces)**-t, amely egy GitHub által létrehozott virtuális környezet, elérhető VS Code böngésző felületen keresztül. Ha van hozzáférésed Codespaces-hez, egyszerűen kattints a tároló **Code** gombjára, indíts egy codespace-t, és pillanatok alatt futtathatsz.
* Használhatod a **[Binder](https://mybinder.org/v2/gh/microsoft/ai-for-beginners/HEAD)**-t. A [Binder](https://mybinder.org) ingyenes felhő alapú számítási erőforrásokat biztosít, hogy GitHub-on lévő kódokat kipróbálhass. A kezdőlapon van egy gomb, ami a tárolót Binder-ben nyitja meg - ez gyorsan elvisz a binder oldalra, ahol elkészül az alap konténer és elindul a Jupyter webes felület.

> **Megjegyzés**: A visszaélés megelőzése érdekében Binder blokkol bizonyos webes erőforrásokat. Ez megakadályozhatja egyes kódok működését, amelyek modelleket és/vagy adatállományokat töltenek le az internetről. Előfordulhat, hogy megoldásokat kell keresned. A Binder által biztosított számítási kapacitás is elég alap, így a tanulás lassú lesz, különösen az összetettebb, későbbi leckéknél.

## Futtatás GPU-val a felhőben

A tanterv későbbi leckéi nagyban profitálnának a GPU támogatásból. Például a modell képzése különben nagyon lassú lehet. Néhány lehetőség követhető, különösen, ha hozzáférsz felhőhöz például az [Azure for Students](https://azure.microsoft.com/free/students/?WT.mc_id=academic-77998-cacaste) révén, vagy intézményeden keresztül:

* Hozz létre [Data Science Virtual Machine](https://docs.microsoft.com/learn/modules/intro-to-azure-data-science-virtual-machine/?WT.mc_id=academic-77998-cacaste)-t, és kapcsolódj hozzá Jupyter-en keresztül. Ezután klónozd be közvetlenül a tárolót a gépre és kezdj el tanulni. Az NC sorozatú VM-ek támogatják a GPU-t.

> **Megjegyzés**: Bizonyos előfizetések, beleértve az Azure for Students-et, nem biztosítanak GPU támogatást alapból. Előfordulhat, hogy technikai támogatási kérvényt kell benyújtanod további GPU magok igényléséhez.

* Hozz létre [Azure Machine Learning Workspace](https://azure.microsoft.com/services/machine-learning/?WT.mc_id=academic-77998-cacaste)-t, és használd ott a Notebook funkciót. [Ez a videó](https://azure-for-academics.github.io/quickstart/azureml-papers/) megmutatja, hogyan lehet egy tárolót klónozni Azure ML notebookba és elkezdeni a használatát.

Használhatod a Google Colabot is, amely tartalmaz némi ingyenes GPU támogatást, és feltöltheted oda a Jupyter Notebookokat, hogy futtasd őket egyesével.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Jogi nyilatkozat**:
Ez a dokumentum az AI fordítási szolgáltatás, a [Co-op Translator](https://github.com/Azure/co-op-translator) segítségével készült. Bár az pontosságra törekszünk, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az anyanyelvén tekintendő hiteles forrásnak. Fontos információk esetén professzionális emberi fordítást javasolunk. Nem vállalunk felelősséget semmilyen félreértésért vagy téves értelmezésért, amely ebből a fordításból ered.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->