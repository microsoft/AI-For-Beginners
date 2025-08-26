<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "7df19702b8d2d3f7c4238c51bec2c8fc",
  "translation_date": "2025-08-26T00:34:49+00:00",
  "source_file": "lessons/0-course-setup/how-to-run.md",
  "language_code": "hu"
}
-->
# Hogyan futtassuk a kódot

Ez a tananyag számos futtatható példát és labort tartalmaz, amelyeket érdemes kipróbálni. Ehhez szükséged lesz arra, hogy Python kódot tudj futtatni a tananyaghoz mellékelt Jupyter Notebookokban. Több lehetőséged is van a kód futtatására:

## Futtatás helyben a számítógépeden

Ahhoz, hogy a kódot helyben futtasd a számítógépeden, szükséged lesz valamilyen Python verzió telepítésére. Személy szerint a **[miniconda](https://conda.io/en/latest/miniconda.html)** telepítését ajánlom – ez egy viszonylag könnyű telepítés, amely támogatja a `conda` csomagkezelőt különböző Python **virtuális környezetekhez**.

Miután telepítetted a minicondát, klónoznod kell a repót, és létre kell hoznod egy virtuális környezetet, amelyet a kurzushoz fogsz használni:

```bash
git clone http://github.com/microsoft/ai-for-beginners
cd ai-for-beginners
conda env create --name ai4beg --file .devcontainer/environment.yml
conda activate ai4beg
```

### Visual Studio Code használata Python kiterjesztéssel

Valószínűleg a legjobb módja a tananyag használatának, ha megnyitod [Visual Studio Code](http://code.visualstudio.com/?WT.mc_id=academic-77998-cacaste) alkalmazásban a [Python kiterjesztéssel](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-77998-cacaste).

> **Megjegyzés**: Miután klónoztad és megnyitottad a könyvtárat a VS Code-ban, az automatikusan javasolni fogja a Python kiterjesztések telepítését. A miniconda telepítésére is szükséged lesz, ahogy fentebb leírtuk.

> **Megjegyzés**: Ha a VS Code azt javasolja, hogy nyisd meg a repót konténerben, ezt el kell utasítanod, hogy a helyi Python telepítést használd.

### Jupyter használata a böngészőben

A Jupyter környezetet közvetlenül a böngészőből is használhatod a saját számítógépeden. Valójában mind a klasszikus Jupyter, mind a Jupyter Hub kényelmes fejlesztési környezetet biztosít automatikus kiegészítéssel, kódkiemeléssel stb.

A Jupyter helyi indításához menj a kurzus könyvtárába, és futtasd az alábbi parancsot:

```bash
jupyter notebook
```
vagy
```bash
jupyterhub
```
Ezután navigálhatsz bármely `.ipynb` fájlhoz, megnyithatod őket, és elkezdhetsz dolgozni.

### Futtatás konténerben

Egy alternatíva a Python telepítésére, ha a kódot konténerben futtatod. Mivel a repónk tartalmaz egy speciális `.devcontainer` mappát, amely leírja, hogyan építsünk konténert ehhez a repóhoz, a VS Code fel fogja ajánlani, hogy nyisd meg a kódot konténerben. Ehhez szükséged lesz a Docker telepítésére, és ez bonyolultabb is lehet, ezért inkább haladó felhasználóknak ajánljuk.

## Futtatás a felhőben

Ha nem szeretnél helyben Python-t telepíteni, és van hozzáférésed valamilyen felhőalapú erőforráshoz, egy jó alternatíva lehet a kód futtatása a felhőben. Több módja is van ennek:

* Használhatod a **[GitHub Codespaces](https://github.com/features/codespaces)** szolgáltatást, amely egy virtuális környezetet hoz létre számodra a GitHubon, és a VS Code böngészős felületén keresztül érhető el. Ha van hozzáférésed a Codespaces-hez, egyszerűen kattints a **Code** gombra a repóban, indíts el egy codespace-et, és máris kezdheted a munkát.
* Használhatod a **[Binder](https://mybinder.org/v2/gh/microsoft/ai-for-beginners/HEAD)** szolgáltatást. A [Binder](https://mybinder.org) ingyenes számítási erőforrásokat biztosít a felhőben, hogy kipróbálhass néhány kódot a GitHubon. Az első oldalon található egy gomb, amely megnyitja a repót a Binderben – ez gyorsan elvisz a Binder oldalára, amely felépíti az alapul szolgáló konténert, és zökkenőmentesen elindítja a Jupyter webes felületet.

> **Megjegyzés**: A visszaélések megelőzése érdekében a Binder bizonyos webes erőforrásokhoz való hozzáférést blokkol. Ez megakadályozhatja, hogy néhány kód működjön, amely modelleket és/vagy adatokat tölt le a nyilvános internetről. Lehet, hogy kerülőutakat kell találnod. Emellett a Binder által biztosított számítási erőforrások meglehetősen alapvetőek, így a tanulás későbbi, összetettebb leckéiben a tréning lassú lesz.

## Futtatás a felhőben GPU-val

A tananyag néhány későbbi leckéje nagyban profitálna a GPU támogatásból, mert különben a tréning fájdalmasan lassú lesz. Néhány lehetőség áll rendelkezésedre, különösen, ha van hozzáférésed a felhőhöz, például az [Azure for Students](https://azure.microsoft.com/free/students/?WT.mc_id=academic-77998-cacaste) vagy az intézményeden keresztül:

* Hozz létre egy [Data Science Virtual Machine](https://docs.microsoft.com/learn/modules/intro-to-azure-data-science-virtual-machine/?WT.mc_id=academic-77998-cacaste) gépet, és csatlakozz hozzá Jupyteren keresztül. Ezután klónozhatod a repót közvetlenül a gépre, és elkezdheted a tanulást. Az NC-sorozatú virtuális gépek GPU támogatással rendelkeznek.

> **Megjegyzés**: Néhány előfizetés, beleértve az Azure for Students-t, alapértelmezés szerint nem biztosít GPU támogatást. Lehet, hogy további GPU magokat kell kérned technikai támogatási kérelem útján.

* Hozz létre egy [Azure Machine Learning Workspace](https://azure.microsoft.com/services/machine-learning/?WT.mc_id=academic-77998-cacaste) munkaterületet, majd használd ott a Notebook funkciót. [Ez a videó](https://azure-for-academics.github.io/quickstart/azureml-papers/) bemutatja, hogyan klónozhatsz egy repót az Azure ML notebookba, és hogyan kezdheted el használni.

Használhatod a Google Colabot is, amely némi ingyenes GPU támogatást biztosít, és feltöltheted oda a Jupyter Notebookokat, hogy egyenként futtasd őket.

**Felelősség kizárása**:  
Ez a dokumentum az AI fordítási szolgáltatás [Co-op Translator](https://github.com/Azure/co-op-translator) segítségével lett lefordítva. Bár törekszünk a pontosságra, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az eredeti nyelvén tekintendő hiteles forrásnak. Kritikus információk esetén javasolt professzionális emberi fordítást igénybe venni. Nem vállalunk felelősséget semmilyen félreértésért vagy téves értelmezésért, amely a fordítás használatából eredhet.