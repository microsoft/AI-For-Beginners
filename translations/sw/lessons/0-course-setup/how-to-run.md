# Hur man kör koden

Denna kursplan innehåller många exekverbara exempel och labbar som du vill köra. För att göra detta behöver du kunna köra Python-kod i Jupyter Notebooks som tillhandahålls som en del av denna kursplan. Du har flera alternativ för att köra koden:

## Kör lokalt på din dator

För att köra koden lokalt på din dator behöver du ha någon version av Python installerad. Jag rekommenderar personligen att installera **[miniconda](https://conda.io/en/latest/miniconda.html)** - det är en ganska lättviktsinstallation som stöder `conda` paketchef för olika Python **virtuella miljöer**.

Efter att du har installerat miniconda behöver du klona repositoryt och skapa en virtuell miljö som ska användas för denna kurs:

```bash
git clone http://github.com/microsoft/ai-for-beginners
cd ai-for-beginners
conda env create --name ai4beg --file .devcontainer/environment.yml
conda activate ai4beg
```

### Använda Visual Studio Code med Python-tillägg

Förmodligen det bästa sättet att använda kursplanen är att öppna den i [Visual Studio Code](http://code.visualstudio.com/?WT.mc_id=academic-77998-cacaste) med [Python-tillägget](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-77998-cacaste).

> **Obs!**: När du har klonat och öppnat katalogen i VS Code kommer den automatiskt att föreslå att du installerar Python-tillägg. Du måste också installera miniconda som beskrivits ovan.

> **Obs!**: Om VS Code föreslår att du ska öppna repositoryt i en container, behöver du avböja detta för att använda den lokala Python-installationen.

### Använda Jupyter i webbläsaren

Du kan också använda Jupyter-miljön direkt från webbläsaren på din egen dator. Faktum är att både klassiska Jupyter och Jupyter Hub erbjuder en ganska bekväm utvecklingsmiljö med automatisk komplettering, kodmarkering, etc.

För att starta Jupyter lokalt, gå till kursens katalog och kör:

```bash
jupyter notebook
```
eller
```bash
jupyterhub
```
Du kan sedan navigera till valfri `.ipynb` files, open them and start working.

### Running in container

One alternative to Python installation would be to run the code in container. Since our repository contains special `.devcontainer` mapp som instruerar hur man bygger en container för detta repo, VS Code skulle erbjuda dig att öppna koden i containern. Detta kräver Docker-installation och skulle också vara mer komplext, så vi rekommenderar detta för mer erfarna användare.

## Köra i molnet

Om du inte vill installera Python lokalt och har tillgång till några molnresurser - ett bra alternativ skulle vara att köra koden i molnet. Det finns flera sätt att göra detta:

* Använda **[GitHub Codespaces](https://github.com/features/codespaces)**, vilket är en virtuell miljö som skapats för dig på GitHub, tillgänglig via VS Code:s webbläsargränssnitt. Om du har tillgång till Codespaces kan du helt enkelt klicka på **Code**-knappen i repo, starta en codespace och komma igång på nolltid.
* Använda **[Binder](https://mybinder.org/v2/gh/microsoft/ai-for-beginners/HEAD)**. [Binder](https://mybinder.org) är en gratis datorkraft som tillhandahålls i molnet för personer som du att testa lite kod på GitHub. Det finns en knapp på förstasidan för att öppna repositoryt i Binder - detta bör snabbt ta dig till bindersidan, som kommer att bygga den underliggande containern och starta Jupyter-webbgränssnittet för dig sömlöst.

> **Obs!**: För att förhindra missbruk har Binder tillgång till vissa webbresurser blockerade. Detta kan förhindra att viss kod fungerar, som hämtar modeller och/eller dataset från offentliga Internet. Du kan behöva hitta några lösningar. Dessutom är de datorkraft som tillhandahålls av Binder ganska grundläggande, så träningen kommer att vara långsam, särskilt i senare mer komplexa lektioner.

## Köra i molnet med GPU

Vissa av de senare lektionerna i denna kursplan skulle dra stor nytta av GPU-stöd, eftersom träningen annars kommer att vara smärtsamt långsam. Det finns några alternativ du kan följa, särskilt om du har tillgång till molnet antingen genom [Azure for Students](https://azure.microsoft.com/free/students/?WT.mc_id=academic-77998-cacaste) eller genom din institution:

* Skapa [Data Science Virtual Machine](https://docs.microsoft.com/learn/modules/intro-to-azure-data-science-virtual-machine/?WT.mc_id=academic-77998-cacaste) och anslut till den via Jupyter. Du kan då klona repo direkt till maskinen och börja lära dig. NC-seriens virtuella maskiner har GPU-stöd.

> **Obs!**: Vissa prenumerationer, inklusive Azure for Students, erbjuder inte GPU-stöd direkt. Du kan behöva begära ytterligare GPU-kärnor genom en teknisk supportförfrågan.

* Skapa [Azure Machine Learning Workspace](https://azure.microsoft.com/services/machine-learning/?WT.mc_id=academic-77998-cacaste) och använd sedan Notebook-funktionen där. [Denna video](https://azure-for-academics.github.io/quickstart/azureml-papers/) visar hur man klonar ett repository till Azure ML-notebook och börjar använda det.

Du kan också använda Google Colab, som kommer med viss gratis GPU-stöd, och ladda upp Jupyter Notebooks dit för att köra dem en efter en.

**Ansvarsfriskrivning**:  
Detta dokument har översatts med hjälp av maskinbaserade AI-översättningstjänster. Även om vi strävar efter noggrannhet, var medveten om att automatiska översättningar kan innehålla fel eller oegentligheter. Det ursprungliga dokumentet på sitt modersmål bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi tar inget ansvar för missförstånd eller feltolkningar som uppstår på grund av användningen av denna översättning.