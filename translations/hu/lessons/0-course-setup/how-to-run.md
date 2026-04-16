# Hogyan futtassuk a kódot

Ez a tananyag rengeteg futtatható példát és laborokat tartalmaz, amelyeket érdemes lefuttatni. Ehhez szükség van arra, hogy Python kódot tudj végrehajtani a jupyter notebookokban, amelyek a tananyag részeként elérhetőek. Több lehetőséged is van a kód futtatására:

## Lokálisan a saját számítógépeden

A kód lokális futtatásához Python telepítés szükséges a gépeden. Egy ajánlás a **[miniconda](https://conda.io/en/latest/miniconda.html)** telepítése – ez egy viszonylag könnyű telepítés, amely támogatja a `conda` csomagkezelőt különböző Python **virtuális környezetek** használatára.

Miután telepítetted a minicondát, klónozd a repozitóriumot, és hozz létre egy virtuális környezetet, amelyet ezen a tanfolyamon használni fogsz:

```bash
git clone http://github.com/microsoft/ai-for-beginners
cd ai-for-beginners
conda env create --name ai4beg --file .devcontainer/environment.yml
conda activate ai4beg
```

### Visual Studio Code használata Python kiterjesztéssel

A tananyagot a legjobban úgy használhatod, ha megnyitod [Visual Studio Code](http://code.visualstudio.com/?WT.mc_id=academic-77998-cacaste) alkalmazásban, a [Python kiterjesztéssel](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-77998-cacaste).

> **Megjegyzés**: Miután klónoztad és megnyitottad a mappát VS Code-ban, automatikusan javasolni fogja a Python kiterjesztések telepítését. A minconda telepítését is el kell végezned a fentiek szerint.

> **Megjegyzés**: Ha a VS Code felajánlja, hogy egy konténerben nyissa meg újra a repozitóriumot, akkor ezt el kell utasítanod, ha a helyi Python telepítést szeretnéd használni.

### Jupyter használata böngészőben

Használhatsz Jupyter környezetet is a böngészőből a saját számítógépeden. Mind a klasszikus Jupyter, mind a JupyterHub kényelmes fejlesztői környezetet nyújt automatikus kiegészítéssel, kódkiemeléssel stb.

A Jupyter lokális elindításához menj a tananyag könyvtárába, és futtasd:

```bash
jupyter notebook
```
 vagy
```bash
jupyterhub
```
 Ezután tetszőleges `.ipynb` fájlra navigálhatsz, megnyithatod azokat és elkezdhetsz dolgozni.

### Konténerben futtatás

A Python telepítés alternatívája lehet, hogy a kódot egy konténerben futtatod. Mivel a repozitórium tartalmaz egy speciális `.devcontainer` mappát, amely útmutatást ad egy konténer felépítéséhez, a VS Code lehetőséget nyújt arra, hogy a kódot konténerben nyisd meg újra. Ehhez Docker telepítés szükséges, és bonyolultabb is, ezért ezt inkább haladóbb felhasználóknak ajánljuk.

## Felhőben futtatás

Ha nem szeretnéd helyben telepíteni a Pythont, és van hozzáférésed valamilyen felhő erőforráshoz – akkor jó alternatíva a kód futtatása a felhőben. Többféleképpen is megteheted ezt:

* Használhatod a **[GitHub Codespaces](https://github.com/features/codespaces)** szolgáltatást, amely egy virtuális környezet a GitHub-on, a VS Code böngészős felületén keresztül elérhető. Ha hozzáférsz Codespaces-hez, csak kattints a **Code** gombra a repóban, indíts el egy codespace-et és pillanatok alatt futtathatod a kódot.
* Használhatod a **[Binder](https://mybinder.org/v2/gh/microsoft/ai-for-beginners/HEAD)** szolgáltatást. A [Binder](https://mybinder.org) ingyenes számítási erőforrásokat biztosít a felhőben, hogy kipróbálhass kódokat a GitHub-ról. Van egy gomb a főoldalon, amely megnyitja a repót Binder-ben – ez gyorsan átvezet a Binder oldalra, amely felépíti a háttérben a konténert és elindít egy Jupyter webes felületet zökkenőmentesen.

> **Megjegyzés**: A visszaélések elkerülése érdekében Binder korlátozott hozzáféréssel rendelkezik bizonyos webes erőforrásokhoz. Ez megakadályozhat bizonyos kódok működését, amelyek modelleket és/vagy adatállományokat töltenek le a nyilvános internetről. Lehet, hogy megoldásokat kell keresned. Emellett a Binder által nyújtott számítási erőforrások alapvetőek, így az edzések lassúak lesznek, főleg a későbbi, összetettebb leckék esetén.

## Felhőben való futtatás GPU-val

A tananyag egyes későbbi leckéi nagyon profitálhatnak GPU támogatásból. Például a modell betanítása máskülönben fájdalmasan lassú lehet. Több lehetőség közül választhatsz, főleg ha hozzáférsz a felhőhöz az [Azure for Students](https://azure.microsoft.com/free/students/?WT.mc_id=academic-77998-cacaste) segítségével, vagy az intézményeden keresztül:

* Hozz létre egy [Data Science Virtual Machine](https://docs.microsoft.com/learn/modules/intro-to-azure-data-science-virtual-machine/?WT.mc_id=academic-77998-cacaste) virtuális gépet, és csatlakozz hozzá Jupyter segítségével. Ezt követően klónozhatod a repozitóriumot közvetlenül a gépre, és elkezdheted a tanulást. Az NC-sorozatú VM-ek támogatják a GPU-t.

> **Megjegyzés**: Egyes előfizetések, köztük az Azure for Students sem tartalmaznak GPU támogatást alapból. Ekkor további GPU magokat technikai támogatási kérelmen keresztül kell kérned.

* Hozz létre egy [Azure Machine Learning Workspace-et](https://azure.microsoft.com/services/machine-learning/?WT.mc_id=academic-77998-cacaste), majd használd a Notebook funkciót ott. [Ez a videó](https://azure-for-academics.github.io/quickstart/azureml-papers/) bemutatja, hogyan klónozz egy repót az Azure ML notebookba, és hogyan kezd el használni.

Használhatod a Google Colab-ot is, amely ingyenes GPU támogatással rendelkezik, és feltöltheted oda a Jupyter Notebookokat, hogy egyenként végrehajtsd őket.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Jogi nyilatkozat**:
Ez a dokumentum az AI fordító szolgáltatás [Co-op Translator](https://github.com/Azure/co-op-translator) segítségével készült. Bár az pontosságra törekszünk, kérjük, vegye figyelembe, hogy az automatikus fordítások tartalmazhatnak hibákat vagy pontatlanságokat. Az eredeti, anyanyelvi dokumentum tekintendő az illetékes forrásnak. Kritikus információk esetén professzionális, emberi fordítást javaslunk. Nem vállalunk felelősséget semmilyen félreértésért vagy téves értelmezésért, amely ebből a fordításból ered.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->