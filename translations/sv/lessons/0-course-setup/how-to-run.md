# Hur man kör koden

Detta kursmaterial innehåller många exekverbara exempel och labbar som du vill köra. För att göra detta behöver du möjligheten att köra Python-kod i Jupyter Notebook-filer som tillhandahålls som en del av detta kursmaterial. Du har flera alternativ för att köra koden:

## Kör lokalt på din dator

För att köra koden lokalt på din dator behövs en Python-installation. Ett rekommenderat alternativ är att installera **[miniconda](https://conda.io/en/latest/miniconda.html)** – det är en ganska lätt installation som stöder `conda` paketförvaltaren för olika Python **virtuella miljöer**.

Efter att du installerat miniconda, klona repot och skapa en virtuell miljö som ska användas för denna kurs:

```bash
git clone http://github.com/microsoft/ai-for-beginners
cd ai-for-beginners
conda env create --name ai4beg --file .devcontainer/environment.yml
conda activate ai4beg
```

### Använda Visual Studio Code med Python Extension

Detta kursmaterial används bäst när du öppnar det i [Visual Studio Code](http://code.visualstudio.com/?WT.mc_id=academic-77998-cacaste) med [Python Extension](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-77998-cacaste).

> **Notera**: När du klonar och öppnar katalogen i VS Code kommer det automatiskt att föreslå att du installerar Python extensions. Du behöver också installera miniconda som beskrivs ovan.

> **Notera**: Om VS Code föreslår att du öppnar repot i en container bör du tacka nej till detta för att kunna använda den lokala Python-installationen.

### Använda Jupyter i webbläsaren

Du kan också använda en Jupyter-miljö från webbläsaren på din egen dator. Både klassisk Jupyter och JupyterHub erbjuder en bekväm utvecklingsmiljö med automatiskt slutförande, kodmarkering med mera.

För att starta Jupyter lokalt, gå till kurskatalogen och kör:

```bash
jupyter notebook
```
 eller
```bash
jupyterhub
```
Du kan därefter navigera till vilken `.ipynb`-fil som helst, öppna dem och börja arbeta.

### Köra i container

Ett alternativ till Python-installation är att köra koden i en container. Eftersom vårt repo tillhandahåller en speciell `.devcontainer`-mapp som visar hur man bygger en container för detta repo, erbjuder VS Code möjligheten att öppna koden i en container. Detta kräver att Docker är installerat och är också mer komplext, så vi rekommenderar detta för mer erfarna användare.

## Köra i molnet

Om du inte vill installera Python lokalt och har tillgång till molnresurser är ett bra alternativ att köra koden i molnet. Det finns flera sätt att göra detta:

* Använd **[GitHub Codespaces](https://github.com/features/codespaces)**, som är en virtuell miljö skapad för dig på GitHub, tillgänglig genom ett VS Code-webbinslag. Om du har tillgång till Codespaces kan du bara klicka på **Code**-knappen i repot, starta ett codespace och komma igång snabbt.
* Använd **[Binder](https://mybinder.org/v2/gh/microsoft/ai-for-beginners/HEAD)**. [Binder](https://mybinder.org) erbjuder gratis datorresurser i molnet för personer som du att testa kod på GitHub. Det finns en knapp på startsidan för att öppna repot i Binder – detta tar dig snabbt till binder-sidan, som bygger en underliggande container och startar ett Jupyter-webbgränssnitt för dig sömlöst.

> **Notera**: För att förhindra missbruk har Binder blockerat tillgång till vissa webbresurser. Detta kan förhindra att viss kod, som hämtar modeller och/eller dataset från det offentliga internet, fungerar. Du kan behöva hitta lösningar. Dessutom är datorresurser som tillhandahålls av Binder ganska enkla, så träningen kan gå långsamt, särskilt i senare, mer komplexa lektioner.

## Köra i molnet med GPU

Några av de senare lektionerna i detta kursmaterial skulle ha stor nytta av GPU-stöd. Modellträning kan till exempel vara smärtsamt långsam annars. Det finns några alternativ du kan följa, särskilt om du har tillgång till molnet antingen via [Azure for Students](https://azure.microsoft.com/free/students/?WT.mc_id=academic-77998-cacaste) eller via din institution:

* Skapa [Data Science Virtual Machine](https://docs.microsoft.com/learn/modules/intro-to-azure-data-science-virtual-machine/?WT.mc_id=academic-77998-cacaste) och anslut till den via Jupyter. Du kan sedan klona repot direkt på maskinen och börja lära dig. NC-seriens virtuella maskiner har GPU-stöd.

> **Notera**: Vissa prenumerationer, inklusive Azure for Students, ger inte GPU-stöd från början. Du kan behöva begära extra GPU-kärnor med ett tekniskt supportärende.

* Skapa [Azure Machine Learning Workspace](https://azure.microsoft.com/services/machine-learning/?WT.mc_id=academic-77998-cacaste) och använd sedan Notebooks-funktionen där. [Den här videon](https://azure-for-academics.github.io/quickstart/azureml-papers/) visar hur man klonar ett repo till en Azure ML Notebook och börjar använda det.

Du kan också använda Google Colab, som har visst gratis GPU-stöd, och ladda upp Jupyter Notebook-filer där för att exekvera dem en i taget.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfriskrivning**:
Detta dokument har översatts med hjälp av AI-översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Även om vi strävar efter noggrannhet, vänligen var medveten om att automatiska översättningar kan innehålla fel eller brister. Det ursprungliga dokumentet på dess originalspråk bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för eventuella missförstånd eller feltolkningar som uppstår från användningen av denna översättning.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->