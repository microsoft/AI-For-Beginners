<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "7df19702b8d2d3f7c4238c51bec2c8fc",
  "translation_date": "2025-08-28T19:19:47+00:00",
  "source_file": "lessons/0-course-setup/how-to-run.md",
  "language_code": "nl"
}
-->
# Hoe de code uit te voeren

Deze cursus bevat veel uitvoerbare voorbeelden en labs die je wilt uitvoeren. Om dit te doen, moet je de mogelijkheid hebben om Python-code uit te voeren in Jupyter Notebooks die als onderdeel van deze cursus worden geleverd. Er zijn verschillende opties om de code uit te voeren:

## Lokaal uitvoeren op je computer

Om de code lokaal op je computer uit te voeren, moet je een versie van Python geïnstalleerd hebben. Ik raad persoonlijk aan om **[miniconda](https://conda.io/en/latest/miniconda.html)** te installeren - het is een vrij lichte installatie die de `conda` pakketbeheerder ondersteunt voor verschillende Python **virtuele omgevingen**.

Nadat je miniconda hebt geïnstalleerd, moet je de repository klonen en een virtuele omgeving maken die voor deze cursus wordt gebruikt:

```bash
git clone http://github.com/microsoft/ai-for-beginners
cd ai-for-beginners
conda env create --name ai4beg --file .devcontainer/environment.yml
conda activate ai4beg
```

### Visual Studio Code gebruiken met Python-extensie

Waarschijnlijk is de beste manier om de cursus te gebruiken deze te openen in [Visual Studio Code](http://code.visualstudio.com/?WT.mc_id=academic-77998-cacaste) met de [Python-extensie](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-77998-cacaste).

> **Opmerking**: Zodra je de directory in VS Code kloont en opent, zal het automatisch voorstellen om Python-extensies te installeren. Je moet ook miniconda installeren zoals hierboven beschreven.

> **Opmerking**: Als VS Code je voorstelt om de repository in een container opnieuw te openen, moet je dit weigeren om de lokale Python-installatie te gebruiken.

### Jupyter in de browser gebruiken

Je kunt ook de Jupyter-omgeving rechtstreeks vanuit de browser op je eigen computer gebruiken. Zowel klassieke Jupyter als Jupyter Hub bieden een vrij handige ontwikkelomgeving met automatische aanvulling, code-highlighting, enz.

Om Jupyter lokaal te starten, ga naar de directory van de cursus en voer uit:

```bash
jupyter notebook
```
of
```bash
jupyterhub
```
Je kunt dan naar een van de `.ipynb`-bestanden navigeren, ze openen en beginnen met werken.

### Uitvoeren in een container

Een alternatief voor een Python-installatie is het uitvoeren van de code in een container. Omdat onze repository een speciale `.devcontainer`-map bevat die instructies geeft over hoe een container voor deze repo te bouwen, zal VS Code je aanbieden om de code in een container opnieuw te openen. Dit vereist een Docker-installatie en is ook wat complexer, dus we raden dit aan voor meer ervaren gebruikers.

## Uitvoeren in de cloud

Als je Python niet lokaal wilt installeren en toegang hebt tot enkele cloudresources, is een goed alternatief om de code in de cloud uit te voeren. Er zijn verschillende manieren waarop je dit kunt doen:

* Gebruik **[GitHub Codespaces](https://github.com/features/codespaces)**, een virtuele omgeving die voor je wordt gecreëerd op GitHub, toegankelijk via de browserinterface van VS Code. Als je toegang hebt tot Codespaces, kun je gewoon op de **Code**-knop in de repo klikken, een codespace starten en binnen no-time aan de slag gaan.
* Gebruik **[Binder](https://mybinder.org/v2/gh/microsoft/ai-for-beginners/HEAD)**. [Binder](https://mybinder.org) biedt gratis computermiddelen in de cloud voor mensen zoals jij om wat code op GitHub te testen. Er is een knop op de startpagina om de repository in Binder te openen - dit zou je snel naar de Binder-site moeten brengen, die de onderliggende container bouwt en naadloos de Jupyter-webinterface start.

> **Opmerking**: Om misbruik te voorkomen, heeft Binder toegang tot sommige webresources geblokkeerd. Dit kan voorkomen dat sommige code werkt die modellen en/of datasets van het openbare internet haalt. Je moet mogelijk enkele alternatieven vinden. Bovendien zijn de computermiddelen die door Binder worden geleverd vrij basaal, dus training zal traag zijn, vooral in latere, meer complexe lessen.

## Uitvoeren in de cloud met GPU

Sommige van de latere lessen in deze cursus profiteren enorm van GPU-ondersteuning, omdat training anders extreem traag zal zijn. Er zijn een paar opties die je kunt volgen, vooral als je toegang hebt tot de cloud via [Azure for Students](https://azure.microsoft.com/free/students/?WT.mc_id=academic-77998-cacaste) of via je instelling:

* Maak een [Data Science Virtual Machine](https://docs.microsoft.com/learn/modules/intro-to-azure-data-science-virtual-machine/?WT.mc_id=academic-77998-cacaste) en verbind ermee via Jupyter. Je kunt dan de repo rechtstreeks op de machine klonen en beginnen met leren. NC-serie VM's hebben GPU-ondersteuning.

> **Opmerking**: Sommige abonnementen, waaronder Azure for Students, bieden standaard geen GPU-ondersteuning. Je moet mogelijk extra GPU-cores aanvragen via een technisch ondersteuningsverzoek.

* Maak een [Azure Machine Learning Workspace](https://azure.microsoft.com/services/machine-learning/?WT.mc_id=academic-77998-cacaste) en gebruik vervolgens de Notebook-functie daar. [Deze video](https://azure-for-academics.github.io/quickstart/azureml-papers/) laat zien hoe je een repository kunt klonen in een Azure ML-notebook en ermee aan de slag kunt gaan.

Je kunt ook Google Colab gebruiken, dat enige gratis GPU-ondersteuning biedt, en Jupyter Notebooks daar uploaden om ze één voor één uit te voeren.

---

**Disclaimer**:  
Dit document is vertaald met behulp van de AI-vertalingsservice [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we streven naar nauwkeurigheid, dient u zich ervan bewust te zijn dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het originele document in de oorspronkelijke taal moet worden beschouwd als de gezaghebbende bron. Voor cruciale informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.