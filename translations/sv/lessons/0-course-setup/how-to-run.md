# Hur man kör koden

Denna läroplan innehåller många körbara exempel och labbar som du vill köra. För att göra detta behöver du möjligheten att köra Python-kod i Jupyter Notebooks som tillhandahålls som en del av denna läroplan. Du har flera alternativ för att köra koden:

## Kör lokalt på din dator

För att köra koden lokalt på din dator behövs en Python-installation. Ett rekommenderat alternativ är att installera **[miniconda](https://conda.io/en/latest/miniconda.html)** – det är en ganska lätt installation som stöder `conda` pakethanterare för olika Python **virtuella miljöer**.

Efter att du installerat miniconda, klona repot och skapa en virtuell miljö som ska användas för denna kurs:

```bash
git clone http://github.com/microsoft/ai-for-beginners
cd ai-for-beginners
conda env create --name ai4beg --file .devcontainer/environment.yml
conda activate ai4beg
```

> **Windows-anteckning**: Om skapandet av miljön misslyckas när du installerar `gdk-pixbuf` med ett `UnicodeDecodeError` som nämner `gbk`-kodeken, aktivera Pythons UTF-8-läge i din terminal och försök igen. Använd syntaxen för den terminal du använder:
>
> **PowerShell:**
>
> ```powershell
> $env:PYTHONUTF8 = "1"
> conda env create --name ai4beg --file .devcontainer/environment.yml
> ```
>
> **Kommandotolken (`cmd.exe`) eller Anaconda-prompt:**
>
> ```cmd
> set PYTHONUTF8=1
> conda env create --name ai4beg --file .devcontainer/environment.yml
> ```
>
> **Bash, inklusive Git Bash:**
>
> ```bash
> export PYTHONUTF8=1
> conda env create --name ai4beg --file .devcontainer/environment.yml
> ```
>
> Om ett misslyckat försök lämnade kvar `ai4beg`-miljön, avaktivera den och ta bort den miljön innan du försöker igen. Använd `conda deactivate` först när en miljö är aktiv:
>
> ```text
> conda deactivate
> conda env remove --name ai4beg
> ```

### Använda Visual Studio Code med Python Extension

Denna läroplan används bäst genom att öppna den i [Visual Studio Code](http://code.visualstudio.com/?WT.mc_id=academic-77998-cacaste) med [Python Extension](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-77998-cacaste).

> **Notera**: När du klonar och öppnar katalogen i VS Code kommer den automatiskt att föreslå att du installerar Python-tillägg. Du behöver också installera miniconda som beskrivs ovan.

> **Notera**: Om VS Code föreslår att du öppnar repot i en container bör du tacka nej till detta för att använda den lokala Python-installationen.

### Använda Jupyter i webbläsaren

Du kan också använda en Jupyter-miljö från webbläsaren på din egen dator. Både klassisk Jupyter och JupyterHub erbjuder en bekväm utvecklingsmiljö med automatisk komplettering, kodmarkering med mera.

För att starta Jupyter lokalt, gå till kurskatalogen och kör:

```bash
jupyter notebook
```
eller
```bash
jupyterhub
```
Du kan sedan navigera till någon av `.ipynb`-filerna, öppna dem och börja arbeta.

### Köra i container

Ett alternativ till Python-installation är att köra koden i en container. Eftersom vårt repo tillhandahåller en särskild `.devcontainer`-mapp som visar hur man bygger en container för detta repo, erbjuder VS Code möjligheten att öppna koden i en container. Detta kräver installation av Docker och är också mer komplext, så vi rekommenderar detta för mer erfarna användare.

## Körning i molnet

Om du inte vill installera Python lokalt och har tillgång till molnresurser är ett bra alternativ att köra koden i molnet. Det finns flera sätt du kan göra detta:

* Använd **[GitHub Codespaces](https://github.com/features/codespaces)**, vilket är en virtuell miljö skapad åt dig på GitHub, åtkomlig via ett VS Code-webbläsargränssnitt. Om du har tillgång till Codespaces kan du bara klicka på **Code**-knappen i repot, starta en codespace och komma igång snabbt.
* Använd **[Binder](https://mybinder.org/v2/gh/microsoft/ai-for-beginners/HEAD)**. [Binder](https://mybinder.org) erbjuder gratis beräkningsresurser i molnet för personer som du att testa kod från GitHub. Det finns en knapp på framsidan för att öppna repot i Binder – detta tar dig snabbt till Binder-sidan, som bygger en container i bakgrunden och startar ett Jupyter-webbgränssnitt sömlöst.

> **Notera**: För att förhindra missbruk har Binder blockerat tillgång till vissa webbresurser. Detta kan hindra viss kod från att fungera, särskilt sådan som hämtar modeller och/eller dataset från det publika internet. Du kan behöva hitta arbetsrundor. Dessutom är beräkningsresurserna som Binder tillhandahåller ganska grundläggande, så träning blir långsam, särskilt i senare och mer komplexa lektioner.

## Körning i molnet med GPU

Vissa av de senare lektionerna i denna läroplan skulle ha stor nytta av GPU-stöd. Modellträning kan till exempel annars bli smärtsamt långsam. Det finns några alternativ som du kan följa, särskilt om du har tillgång till molnet genom [Azure for Students](https://azure.microsoft.com/free/students/?WT.mc_id=academic-77998-cacaste) eller via din institution:

* Skapa [Data Science Virtual Machine](https://docs.microsoft.com/learn/modules/intro-to-azure-data-science-virtual-machine/?WT.mc_id=academic-77998-cacaste) och anslut till den via Jupyter. Du kan då klona repot direkt på maskinen och börja lära dig. NC-seriens VM:ar har GPU-stöd.

> **Notera**: Vissa prenumerationer, inklusive Azure for Students, erbjuder inte GPU-stöd direkt. Du kan behöva begära extra GPU-kärnor via en teknisk supportförfrågan.

* Skapa [Azure Machine Learning Workspace](https://azure.microsoft.com/services/machine-learning/?WT.mc_id=academic-77998-cacaste) och använd sedan Notebook-funktionen där. [Denna video](https://azure-for-academics.github.io/quickstart/azureml-papers/) visar hur du klonar ett repo i Azure ML-notebook och börjar använda det.

Du kan också använda Google Colab, som har viss gratis GPU-stöd, och ladda upp Jupyter Notebooks där för att köra dem en i taget.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfriskrivning**:
Detta dokument har översatts med hjälp av AI-översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Även om vi strävar efter noggrannhet, var vänlig notera att automatiska översättningar kan innehålla fel eller brister. Det ursprungliga dokumentet på dess modersmål bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för några missförstånd eller feltolkningar som uppstår till följd av användningen av denna översättning.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->