<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "7df19702b8d2d3f7c4238c51bec2c8fc",
  "translation_date": "2025-08-28T15:08:25+00:00",
  "source_file": "lessons/0-course-setup/how-to-run.md",
  "language_code": "sv"
}
-->
# Hur man Kör Koden

Den här kursplanen innehåller många exekverbara exempel och labbar som du kanske vill köra. För att göra detta behöver du möjlighet att köra Python-kod i Jupyter Notebooks som tillhandahålls som en del av kursplanen. Du har flera alternativ för att köra koden:

## Kör lokalt på din dator

För att köra koden lokalt på din dator behöver du ha någon version av Python installerad. Jag rekommenderar personligen att installera **[miniconda](https://conda.io/en/latest/miniconda.html)** – det är en ganska lättviktig installation som stöder `conda` paketmanager för olika Python **virtuella miljöer**.

Efter att du har installerat miniconda behöver du klona repot och skapa en virtuell miljö som ska användas för den här kursen:

```bash
git clone http://github.com/microsoft/ai-for-beginners
cd ai-for-beginners
conda env create --name ai4beg --file .devcontainer/environment.yml
conda activate ai4beg
```

### Använda Visual Studio Code med Python-tillägg

Det bästa sättet att använda kursplanen är förmodligen att öppna den i [Visual Studio Code](http://code.visualstudio.com/?WT.mc_id=academic-77998-cacaste) med [Python-tillägg](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-77998-cacaste).

> **Note**: När du klonar och öppnar katalogen i VS Code kommer det automatiskt föreslå att du installerar Python-tillägg. Du måste också installera miniconda som beskrivs ovan.

> **Note**: Om VS Code föreslår att du ska öppna repot i en container, behöver du avböja detta för att använda den lokala Python-installationen.

### Använda Jupyter i webbläsaren

Du kan också använda Jupyter-miljön direkt från webbläsaren på din egen dator. Faktum är att både klassisk Jupyter och Jupyter Hub erbjuder en ganska bekväm utvecklingsmiljö med autokomplettering, kodmarkering, etc.

För att starta Jupyter lokalt, gå till kursens katalog och kör:

```bash
jupyter notebook
```
eller
```bash
jupyterhub
```
Du kan sedan navigera till någon av `.ipynb`-filerna, öppna dem och börja arbeta.

### Kör i en container

Ett alternativ till att installera Python är att köra koden i en container. Eftersom vårt repo innehåller en speciell `.devcontainer`-mapp som instruerar hur man bygger en container för detta repo, kommer VS Code att erbjuda dig att öppna koden i en container. Detta kräver Docker-installation och är också mer komplext, så vi rekommenderar detta för mer erfarna användare.

## Kör i molnet

Om du inte vill installera Python lokalt och har tillgång till några molnresurser – ett bra alternativ är att köra koden i molnet. Det finns flera sätt att göra detta:

* Använda **[GitHub Codespaces](https://github.com/features/codespaces)**, som är en virtuell miljö skapad för dig på GitHub, tillgänglig via VS Codes webbläsargränssnitt. Om du har tillgång till Codespaces kan du bara klicka på **Code**-knappen i repot, starta en codespace och komma igång direkt.
* Använda **[Binder](https://mybinder.org/v2/gh/microsoft/ai-for-beginners/HEAD)**. [Binder](https://mybinder.org) är en gratis molnresurs som tillhandahålls för att testa kod på GitHub. Det finns en knapp på startsidan för att öppna repot i Binder – detta tar dig snabbt till Binder-webbplatsen, som bygger den underliggande containern och startar Jupyter-webbgränssnittet åt dig sömlöst.

> **Note**: För att förhindra missbruk har Binder blockerat åtkomst till vissa webbresurser. Detta kan förhindra att viss kod fungerar, särskilt sådan som hämtar modeller och/eller dataset från det offentliga internet. Du kan behöva hitta några lösningar. Dessutom är de beräkningsresurser som Binder tillhandahåller ganska grundläggande, så träning kommer att vara långsam, särskilt i senare mer komplexa lektioner.

## Kör i molnet med GPU

Vissa av de senare lektionerna i den här kursplanen skulle dra stor nytta av GPU-stöd, eftersom träning annars kommer att vara smärtsamt långsam. Det finns några alternativ du kan följa, särskilt om du har tillgång till molnet antingen via [Azure for Students](https://azure.microsoft.com/free/students/?WT.mc_id=academic-77998-cacaste) eller via din institution:

* Skapa en [Data Science Virtual Machine](https://docs.microsoft.com/learn/modules/intro-to-azure-data-science-virtual-machine/?WT.mc_id=academic-77998-cacaste) och anslut till den via Jupyter. Du kan sedan klona repot direkt till maskinen och börja lära dig. NC-seriens virtuella maskiner har GPU-stöd.

> **Note**: Vissa prenumerationer, inklusive Azure for Students, erbjuder inte GPU-stöd som standard. Du kan behöva begära ytterligare GPU-kärnor via en teknisk supportförfrågan.

* Skapa en [Azure Machine Learning Workspace](https://azure.microsoft.com/services/machine-learning/?WT.mc_id=academic-77998-cacaste) och använd sedan Notebook-funktionen där. [Den här videon](https://azure-for-academics.github.io/quickstart/azureml-papers/) visar hur du klonar ett repo till Azure ML Notebook och börjar använda det.

Du kan också använda Google Colab, som erbjuder viss gratis GPU-stöd, och ladda upp Jupyter Notebooks där för att köra dem en i taget.

---

**Ansvarsfriskrivning**:  
Detta dokument har översatts med hjälp av AI-översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Även om vi strävar efter noggrannhet, bör du vara medveten om att automatiserade översättningar kan innehålla fel eller felaktigheter. Det ursprungliga dokumentet på dess ursprungliga språk bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för eventuella missförstånd eller feltolkningar som uppstår vid användning av denna översättning.