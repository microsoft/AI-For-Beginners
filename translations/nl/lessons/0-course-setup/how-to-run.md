# Hoe de code uit te voeren

Deze cursus bevat veel uitvoerbare voorbeelden en labs die je wilt uitvoeren. Om dit te doen, moet je de mogelijkheid hebben om Python-code uit te voeren in Jupyter Notebooks die als onderdeel van deze cursus worden geleverd. Je hebt verschillende opties om de code uit te voeren:

## Lokaal op je computer uitvoeren

Om de code lokaal op je computer uit te voeren, is een Python-installatie nodig. Een aanbeveling is om **[miniconda](https://conda.io/en/latest/miniconda.html)** te installeren – dit is een tamelijk lichtgewicht installatie die de `conda` package manager ondersteunt voor verschillende Python **virtuele omgevingen**.

Nadat je miniconda hebt geïnstalleerd, clone je de repository en maak je een virtuele omgeving aan die voor deze cursus zal worden gebruikt:

```bash
git clone http://github.com/microsoft/ai-for-beginners
cd ai-for-beginners
conda env create --name ai4beg --file .devcontainer/environment.yml
conda activate ai4beg
```

> **Windows-opmerking**: Als het aanmaken van een omgeving mislukt tijdens het installeren van `gdk-pixbuf` met een `UnicodeDecodeError` waarin de `gbk` codec wordt genoemd, schakel dan de UTF-8 modus van Python in je terminal in en probeer het opnieuw. Gebruik de syntaxis voor de terminal die je gebruikt:
>
> **PowerShell:**
>
> ```powershell
> $env:PYTHONUTF8 = "1"
> conda env create --name ai4beg --file .devcontainer/environment.yml
> ```
>
> **Command Prompt (`cmd.exe`) of Anaconda Prompt:**
>
> ```cmd
> set PYTHONUTF8=1
> conda env create --name ai4beg --file .devcontainer/environment.yml
> ```
>
> **Bash, inclusief Git Bash:**
>
> ```bash
> export PYTHONUTF8=1
> conda env create --name ai4beg --file .devcontainer/environment.yml
> ```
>
> Als een mislukte poging de `ai4beg` omgeving heeft achtergelaten, deactiveer deze dan en verwijder die omgeving voordat je het opnieuw probeert. Gebruik eerst `conda deactivate` wanneer een omgeving actief is:
>
> ```text
> conda deactivate
> conda env remove --name ai4beg
> ```

### Visual Studio Code gebruiken met Python-extensie

Dit curriculum wordt het best gebruikt wanneer u het opent in [Visual Studio Code](http://code.visualstudio.com/?WT.mc_id=academic-77998-cacaste) met de [Python-extensie](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-77998-cacaste).

> **Opmerking**: Zodra u de directory kloont en opent in VS Code, zal het automatisch voorstellen om Python-extensies te installeren. U moet ook miniconda installeren zoals hierboven beschreven.

> **Opmerking**: Als VS Code u suggereert om de repository opnieuw te openen in een container, moet u dit weigeren om de lokale Python-installatie te gebruiken.

### Gebruik van Jupyter in de browser

U kunt ook een Jupyter-omgeving vanuit de browser op uw eigen computer gebruiken. Zowel klassieke Jupyter als JupyterHub bieden een handige ontwikkelomgeving met auto-aanvulling, code-highlighting, enzovoort.

Om Jupyter lokaal te starten, gaat u naar de map van de cursus en voert u uit:

```bash
jupyter notebook
```
of
```bash
jupyterhub
```
U kunt dan naar elk van de `.ipynb`-bestanden navigeren, ze openen en beginnen met werken.

### Uitvoeren in een container

Een alternatief voor de Python-installatie zou zijn om de code in een container uit te voeren. Omdat onze repository een speciale `.devcontainer` map bevat die aangeeft hoe een container voor deze repo gebouwd kan worden, biedt VS Code de mogelijkheid om de code opnieuw te openen in een container. Dit vereist de installatie van Docker en is ook complexer, dus we bevelen dit aan voor meer ervaren gebruikers.

## Uitvoeren in de cloud

Als u Python niet lokaal wilt installeren en toegang heeft tot cloudresources, is een goed alternatief om de code in de cloud uit te voeren. Er zijn verschillende manieren om dit te doen:

* Gebruik maken van **[GitHub Codespaces](https://github.com/features/codespaces)**, wat een virtuele omgeving voor u creëert op GitHub, toegankelijk via een VS Code-browserinterface. Als u toegang heeft tot Codespaces, kunt u gewoon op de **Code**-knop in de repository klikken, een codespace starten en direct aan de slag gaan.
* Gebruik maken van **[Binder](https://mybinder.org/v2/gh/microsoft/ai-for-beginners/HEAD)**. [Binder](https://mybinder.org) biedt gratis computerresources in de cloud voor mensen zoals u om code op GitHub uit te proberen. Er is een knop op de voorkant om de repository in Binder te openen – dit brengt u snel naar de bindersite, die een onderliggende container bouwt en naadloos een Jupyter-webinterface voor u start.

> **Opmerking**: Om misbruik te voorkomen, heeft Binder toegang tot sommige webresources geblokkeerd. Dit kan voorkomen dat sommige code werkt die modellen en/of datasets van het openbare internet haalt. U moet mogelijk een oplossing vinden. Ook zijn de computerresources die door Binder worden aangeboden vrij basic, dus training zal traag zijn, vooral in latere, meer complexe lessen.

## Uitvoeren in de cloud met GPU

Sommige latere lessen in dit curriculum zouden sterk profiteren van GPU-ondersteuning. Modeltraining kan bijvoorbeeld anders erg traag zijn. Er zijn een paar opties die u kunt volgen, vooral als u toegang heeft tot de cloud via [Azure for Students](https://azure.microsoft.com/free/students/?WT.mc_id=academic-77998-cacaste) of via uw instelling:

* Maak een [Data Science Virtual Machine](https://docs.microsoft.com/learn/modules/intro-to-azure-data-science-virtual-machine/?WT.mc_id=academic-77998-cacaste) en maak verbinding via Jupyter. U kunt dan de repo direct op de machine klonen en beginnen met leren. NC-serie VM's hebben GPU-ondersteuning.

> **Opmerking**: Sommige abonnementen, waaronder Azure for Students, bieden niet standaard GPU-ondersteuning. U moet mogelijk extra GPU-cores aanvragen via een technisch ondersteuningsverzoek.

* Maak een [Azure Machine Learning Workspace](https://azure.microsoft.com/services/machine-learning/?WT.mc_id=academic-77998-cacaste) en gebruik vervolgens de Notebook-functie daar. [Deze video](https://azure-for-academics.github.io/quickstart/azureml-papers/) toont hoe u een repository kloont in een Azure ML-notebook en het gaat gebruiken.

U kunt ook Google Colab gebruiken, dat enige gratis GPU-ondersteuning biedt, en Jupyter-notebooks daar uploaden om ze stuk voor stuk uit te voeren.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Dit document is vertaald met behulp van de AI vertaaldienst [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we streven naar nauwkeurigheid, dient u er rekening mee te houden dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het originele document in de oorspronkelijke taal moet worden beschouwd als de gezaghebbende bron. Voor kritieke informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor eventuele misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->