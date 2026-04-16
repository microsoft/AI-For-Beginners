# Hoe de code uit te voeren

Dit curriculum bevat veel uitvoerbare voorbeelden en labs die je wilt uitvoeren. Om dit te doen, heb je de mogelijkheid nodig om Python-code uit te voeren in Jupyter Notebooks die als onderdeel van dit curriculum worden meegeleverd. Je hebt verschillende opties om de code uit te voeren:

## Lokaal op je computer uitvoeren

Om de code lokaal op je computer uit te voeren, is een Python-installatie nodig. Een aanbeveling is om **[miniconda](https://conda.io/en/latest/miniconda.html)** te installeren - het is een vrij lichte installatie die de `conda` package manager ondersteunt voor verschillende Python **virtuele omgevingen**.

Nadat je miniconda hebt geïnstalleerd, clone je de repository en maak je een virtuele omgeving aan die voor deze cursus gebruikt wordt:

```bash
git clone http://github.com/microsoft/ai-for-beginners
cd ai-for-beginners
conda env create --name ai4beg --file .devcontainer/environment.yml
conda activate ai4beg
```

### Visual Studio Code gebruiken met Python-extensie

Dit curriculum gebruik je het beste wanneer je het opent in [Visual Studio Code](http://code.visualstudio.com/?WT.mc_id=academic-77998-cacaste) met de [Python-extensie](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-77998-cacaste).

> **Opmerking**: Zodra je de directory clonet en opent in VS Code, wordt je automatisch voorgesteld om de Python-extensies te installeren. Je moet ook miniconda installeren zoals hierboven beschreven.

> **Opmerking**: Als VS Code je voorstelt om de repository opnieuw te openen in een container, moet je dit weigeren om de lokale Python-installatie te gebruiken. 

### Jupyter in de browser gebruiken

Je kunt ook een Jupyter-omgeving gebruiken vanuit de browser op je eigen computer. Zowel klassieke Jupyter als JupyterHub bieden een handige ontwikkelomgeving met automatische aanvulling, syntaxmarkering, etc.

Om Jupyter lokaal te starten, ga je naar de directory van de cursus, en voer je uit:

```bash
jupyter notebook
```
of
```bash
jupyterhub
```
Je kunt dan naar een van de `.ipynb`-bestanden navigeren, deze openen en beginnen met werken.

### Uitvoeren in een container

Een alternatief voor Python-installatie zou zijn om de code in een container uit te voeren. Omdat onze repository een speciale `.devcontainer` map aanlevert die instructies bevat over hoe een container voor deze repo te bouwen, biedt VS Code de mogelijkheid om de code opnieuw in een container te openen. Dit vereist een Docker-installatie en is ook wat complexer, daarom raden we dit aan voor meer ervaren gebruikers.

## Uitvoeren in de cloud

Als je Python niet lokaal wilt installeren, en toegang hebt tot wat cloudresources, is een goed alternatief om de code in de cloud uit te voeren. Er zijn verschillende manieren om dit te doen:

* Gebruik maken van **[GitHub Codespaces](https://github.com/features/codespaces)**, wat een virtuele omgeving is die voor jou op GitHub wordt aangemaakt, toegankelijk via een VS Code-browserinterface. Als je toegang hebt tot Codespaces, kun je gewoon op de **Code** knop in de repo klikken, een codespace starten en zonder vertraging aan de slag gaan.
* Gebruik maken van **[Binder](https://mybinder.org/v2/gh/microsoft/ai-for-beginners/HEAD)**. [Binder](https://mybinder.org) biedt gratis computerresources in de cloud voor mensen zoals jij om code op GitHub uit te proberen. Op de startpagina is een knop om de repository in Binder te openen - dit brengt je snel naar de Binder-site, die een onderliggende container bouwt en naadloos een Jupyter-webinterface voor je start.

> **Opmerking**: Om misbruik te voorkomen, heeft Binder toegang tot sommige webresources geblokkeerd. Dit kan voorkomen dat sommige code werkt die modellen en/of datasets van het openbare internet haalt. Mogelijk moet je enkele omwegen vinden. Ook zijn de computerresources van Binder behoorlijk beperkt, dus het trainen zal traag zijn, vooral in latere, meer complexe lessen.

## Uitvoeren in de cloud met GPU

Sommige van de latere lessen in dit curriculum profiteren aanzienlijk van GPU-ondersteuning. Modeltraining kan anders erg traag zijn. Er zijn een paar opties die je kunt volgen, vooral als je toegang hebt tot de cloud, bijvoorbeeld via [Azure for Students](https://azure.microsoft.com/free/students/?WT.mc_id=academic-77998-cacaste) of via je instelling:

* Maak een [Data Science Virtual Machine](https://docs.microsoft.com/learn/modules/intro-to-azure-data-science-virtual-machine/?WT.mc_id=academic-77998-cacaste) aan en verbind ermee via Jupyter. Je kunt de repo dan direct op de machine clonen en beginnen met leren. NC-series VM's hebben GPU-ondersteuning.

> **Opmerking**: Sommige abonnementen, waaronder Azure for Students, bieden standaard geen GPU-ondersteuning. Je moet mogelijk extra GPU-cores aanvragen via een technische supportaanvraag.

* Maak een [Azure Machine Learning Workspace](https://azure.microsoft.com/services/machine-learning/?WT.mc_id=academic-77998-cacaste) aan en gebruik dan de Notebook-functie daar. [Deze video](https://azure-for-academics.github.io/quickstart/azureml-papers/) laat zien hoe je een repository in een Azure ML-notebook clonet en gebruikt.

Je kunt ook Google Colab gebruiken, dat enige gratis GPU-ondersteuning heeft, en Jupyter Notebooks daar uploaden om ze stuk voor stuk uit te voeren.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Dit document is vertaald met behulp van de AI-vertalingsdienst [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we streven naar nauwkeurigheid, dient u er rekening mee te houden dat automatische vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het originele document in de oorspronkelijke taal dient als de gezaghebbende bron te worden beschouwd. Voor cruciale informatie wordt een professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->