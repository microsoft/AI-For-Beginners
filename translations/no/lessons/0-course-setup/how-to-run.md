<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "7df19702b8d2d3f7c4238c51bec2c8fc",
  "translation_date": "2025-08-28T15:09:08+00:00",
  "source_file": "lessons/0-course-setup/how-to-run.md",
  "language_code": "no"
}
-->
# Hvordan kjøre koden

Dette kurset inneholder mange eksekverbare eksempler og laboratorier som du vil ønske å kjøre. For å gjøre dette trenger du muligheten til å kjøre Python-kode i Jupyter Notebooks som er inkludert i dette kurset. Du har flere alternativer for å kjøre koden:

## Kjøre lokalt på din datamaskin

For å kjøre koden lokalt på din datamaskin, må du ha en versjon av Python installert. Jeg anbefaler personlig å installere **[miniconda](https://conda.io/en/latest/miniconda.html)** - det er en lettvektsinstallasjon som støtter `conda` pakkebehandler for ulike Python **virtuelle miljøer**.

Etter at du har installert miniconda, må du klone repositoryen og opprette et virtuelt miljø som skal brukes for dette kurset:

```bash
git clone http://github.com/microsoft/ai-for-beginners
cd ai-for-beginners
conda env create --name ai4beg --file .devcontainer/environment.yml
conda activate ai4beg
```

### Bruke Visual Studio Code med Python-utvidelse

Den beste måten å bruke kurset på er sannsynligvis å åpne det i [Visual Studio Code](http://code.visualstudio.com/?WT.mc_id=academic-77998-cacaste) med [Python-utvidelse](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-77998-cacaste).

> **Note**: Når du kloner og åpner katalogen i VS Code, vil det automatisk foreslå at du installerer Python-utvidelser. Du må også installere miniconda som beskrevet ovenfor.

> **Note**: Hvis VS Code foreslår at du åpner repositoryen i en container, må du avslå dette for å bruke lokal Python-installasjon.

### Bruke Jupyter i nettleseren

Du kan også bruke Jupyter-miljøet direkte fra nettleseren på din egen datamaskin. Faktisk gir både klassisk Jupyter og Jupyter Hub et ganske praktisk utviklingsmiljø med autoutfylling, kodefremheving, osv.

For å starte Jupyter lokalt, gå til katalogen for kurset og kjør:

```bash
jupyter notebook
```
eller
```bash
jupyterhub
```
Du kan deretter navigere til en av `.ipynb`-filene, åpne dem og begynne å jobbe.

### Kjøre i container

Et alternativ til Python-installasjon er å kjøre koden i en container. Siden repositoryen vår inneholder en spesiell `.devcontainer`-mappe som instruerer hvordan man bygger en container for dette repoet, vil VS Code tilby deg å åpne koden i en container. Dette krever Docker-installasjon og er mer komplekst, så vi anbefaler dette for mer erfarne brukere.

## Kjøre i skyen

Hvis du ikke ønsker å installere Python lokalt og har tilgang til noen skyressurser, er et godt alternativ å kjøre koden i skyen. Det finnes flere måter du kan gjøre dette på:

* Bruke **[GitHub Codespaces](https://github.com/features/codespaces)**, som er et virtuelt miljø opprettet for deg på GitHub, tilgjengelig gjennom VS Code-nettlesergrensesnittet. Hvis du har tilgang til Codespaces, kan du bare klikke på **Code**-knappen i repoet, starte en codespace og komme i gang på kort tid.
* Bruke **[Binder](https://mybinder.org/v2/gh/microsoft/ai-for-beginners/HEAD)**. [Binder](https://mybinder.org) er gratis databehandlingsressurser tilgjengelig i skyen for folk som deg til å teste ut kode på GitHub. Det er en knapp på forsiden for å åpne repositoryen i Binder - dette bør raskt ta deg til Binder-siden, som vil bygge den underliggende containeren og starte Jupyter-nettgrensesnittet for deg sømløst.

> **Note**: For å forhindre misbruk har Binder tilgang til noen nettressurser blokkert. Dette kan forhindre at noe av koden fungerer, som henter modeller og/eller datasett fra offentlig Internett. Du må kanskje finne noen løsninger. Dessuten er databehandlingsressursene som tilbys av Binder ganske grunnleggende, så trening vil være treg, spesielt i senere mer komplekse leksjoner.

## Kjøre i skyen med GPU

Noen av de senere leksjonene i dette kurset vil ha stor nytte av GPU-støtte, fordi trening ellers vil være smertefullt tregt. Det finnes noen alternativer du kan følge, spesielt hvis du har tilgang til skyen enten gjennom [Azure for Students](https://azure.microsoft.com/free/students/?WT.mc_id=academic-77998-cacaste) eller gjennom din institusjon:

* Opprett [Data Science Virtual Machine](https://docs.microsoft.com/learn/modules/intro-to-azure-data-science-virtual-machine/?WT.mc_id=academic-77998-cacaste) og koble til den via Jupyter. Du kan deretter klone repoet direkte på maskinen og begynne å lære. NC-serien VMs har GPU-støtte.

> **Note**: Noen abonnementer, inkludert Azure for Students, gir ikke GPU-støtte som standard. Du må kanskje be om ekstra GPU-kjerner gjennom en teknisk supportforespørsel.

* Opprett [Azure Machine Learning Workspace](https://azure.microsoft.com/services/machine-learning/?WT.mc_id=academic-77998-cacaste) og bruk deretter Notebook-funksjonen der. [Denne videoen](https://azure-for-academics.github.io/quickstart/azureml-papers/) viser hvordan du kloner et repository inn i Azure ML-notebook og begynner å bruke det.

Du kan også bruke Google Colab, som kommer med noe gratis GPU-støtte, og laste opp Jupyter Notebooks der for å kjøre dem én etter én.

---

**Ansvarsfraskrivelse**:  
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi streber etter nøyaktighet, vær oppmerksom på at automatiserte oversettelser kan inneholde feil eller unøyaktigheter. Det originale dokumentet på sitt opprinnelige språk bør anses som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.