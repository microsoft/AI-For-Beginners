# Hvordan kjøre koden

Dette pensumet inneholder mange kjørbare eksempler og laboratorier som du vil kjøre. For å gjøre dette trenger du muligheten til å kjøre Python-kode i Jupyter Notebooks som følger med i dette pensumet. Du har flere alternativer for å kjøre koden:

## Kjør lokalt på din egen datamaskin

For å kjøre koden lokalt på din datamaskin, trengs en Python-installasjon. En anbefaling er å installere **[miniconda](https://conda.io/en/latest/miniconda.html)** - det er en ganske lett installasjon som støtter `conda` pakkebehandler for forskjellige Python **virtuelle miljøer**.

Etter at du har installert miniconda, klon depotet og opprett et virtuelt miljø som skal brukes for dette kurset:

```bash
git clone http://github.com/microsoft/ai-for-beginners
cd ai-for-beginners
conda env create --name ai4beg --file .devcontainer/environment.yml
conda activate ai4beg
```

### Bruke Visual Studio Code med Python Extension

Dette pensumet fungerer best når du åpner det i [Visual Studio Code](http://code.visualstudio.com/?WT.mc_id=academic-77998-cacaste) med [Python Extension](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-77998-cacaste).

> **Merk**: Når du har klonet og åpnet mappen i VS Code, vil det automatisk foreslå deg å installere Python-utvidelser. Du må også installere miniconda som beskrevet ovenfor.

> **Merk**: Hvis VS Code foreslår deg å åpne depotet på nytt i en container, bør du avslå dette for å bruke den lokale Python-installasjonen.

### Bruke Jupyter i nettleseren

Du kan også bruke et Jupyter-miljø fra nettleseren på din egen datamaskin. Både klassisk Jupyter og JupyterHub tilbyr et praktisk utviklingsmiljø med automatisk utfylling, kodeutheving, osv.

For å starte Jupyter lokalt, gå til mappen for kurset, og kjør:

```bash
jupyter notebook
```
eller
```bash
jupyterhub
```
Du kan da navigere til hvilke som helst `.ipynb`-filer, åpne dem og begynne å jobbe.

### Kjøring i container

Et alternativ til Python-installasjon er å kjøre koden i en container. Siden vårt depot inneholder en spesiell `.devcontainer`-mappe som beskriver hvordan man bygger en container for dette depotet, tilbyr VS Code muligheten til å åpne koden i en container. Dette krever Docker-installasjon, og vil også være mer komplekst, så vi anbefaler dette for mer erfarne brukere.

## Kjøring i skyen

Hvis du ikke ønsker å installere Python lokalt, og har tilgang til noen skyressurser – vil det være et godt alternativ å kjøre koden i skyen. Det finnes flere måter du kan gjøre dette på:

* Bruke **[GitHub Codespaces](https://github.com/features/codespaces)**, som er et virtuelt miljø opprettet for deg på GitHub, tilgjengelig gjennom en VS Code nettlesergrensesnitt. Hvis du har tilgang til Codespaces, kan du bare trykke på **Code**-knappen i depotet, starte et codespace, og komme i gang på kort tid.
* Bruke **[Binder](https://mybinder.org/v2/gh/microsoft/ai-for-beginners/HEAD)**. [Binder](https://mybinder.org) tilbyr gratis databehandlingsressurser i skyen for folk som deg for å teste ut kode på GitHub. Det finnes en knapp på forsiden for å åpne depotet i Binder – dette vil raskt ta deg til binder-siden, som vil bygge en underliggende container og starte et Jupyter-nettgrensesnitt for deg sømløst.

> **Merk**: For å forhindre misbruk har Binder blokkert tilgang til noen nettressurser. Dette kan forhindre at noe av koden fungerer, som henter modeller og/eller datasett fra det offentlige Internett. Du må kanskje finne noen alternative løsninger. Også de beregningsressursene som tilbys av Binder er ganske enkle, så trening vil være treg, spesielt i senere, mer komplekse leksjoner.

## Kjøring i skyen med GPU

Noen av de senere leksjonene i dette pensumet vil ha stor nytte av GPU-støtte. Modelltrening kan ellers bli smertefullt langsom. Det finnes noen få alternativer du kan følge, spesielt hvis du har tilgang til skyen enten via [Azure for Students](https://azure.microsoft.com/free/students/?WT.mc_id=academic-77998-cacaste), eller gjennom din utdanningsinstitusjon:

* Opprett [Data Science Virtual Machine](https://docs.microsoft.com/learn/modules/intro-to-azure-data-science-virtual-machine/?WT.mc_id=academic-77998-cacaste) og koble til den via Jupyter. Du kan da klone depotet rett på maskinen, og begynne å lære. NC-serie VM-er har GPU-støtte.

> **Merk**: Noen abonnementer, inkludert Azure for Students, tilbyr ikke GPU-støtte som standard. Du må kanskje be om ekstra GPU-kjerner via en teknisk støtteforespørsel.

* Opprett [Azure Machine Learning Workspace](https://azure.microsoft.com/services/machine-learning/?WT.mc_id=academic-77998-cacaste) og bruk deretter Notebook-funksjonen der. [Denne videoen](https://azure-for-academics.github.io/quickstart/azureml-papers/) viser hvordan du kloner et depot inn i Azure ML-notatbok og begynner å bruke det.

Du kan også bruke Google Colab, som kommer med noe gratis GPU-støtte, og laste opp Jupyter Notebooks der for å kjøre dem én etter én.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:  
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi søker å oppnå nøyaktighet, vennligst vær oppmerksom på at automatiske oversettelser kan inneholde feil eller unøyaktigheter. Det opprinnelige dokumentet på originalspråket bør anses som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for misforståelser eller feiltolkninger som følge av bruk av denne oversettelsen.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->