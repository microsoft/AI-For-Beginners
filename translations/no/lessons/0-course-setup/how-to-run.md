# Hvordan kjøre koden

Dette pensumet inneholder mange kjørbare eksempler og laboratorier som du vil kjøre. For å gjøre dette, trenger du muligheten til å kjøre Python-kode i Jupyter Notebooks som leveres som en del av dette pensumet. Du har flere alternativer for å kjøre koden:

## Kjør lokalt på din datamaskin

For å kjøre koden lokalt på din datamaskin, er en Python-installasjon nødvendig. En anbefaling er å installere **[miniconda](https://conda.io/en/latest/miniconda.html)** – det er en relativt lettvektsinstallasjon som støtter `conda` pakkehåndterer for forskjellige Python **virtuelle miljøer**.

Etter at du har installert miniconda, klon depotet og opprett et virtuelt miljø som skal brukes for dette kurset:

```bash
git clone http://github.com/microsoft/ai-for-beginners
cd ai-for-beginners
conda env create --name ai4beg --file .devcontainer/environment.yml
conda activate ai4beg
```

> **Merk for Windows**: Hvis opprettelse av miljø feiler under installasjon av `gdk-pixbuf` med en `UnicodeDecodeError` som nevner `gbk`-kodek, aktiver Pythons UTF-8-modus i terminalen og prøv igjen. Bruk syntaksen for terminalen du bruker:
>
> **PowerShell:**
>
> ```powershell
> $env:PYTHONUTF8 = "1"
> conda env create --name ai4beg --file .devcontainer/environment.yml
> ```
>
> **Kommandoprompt (`cmd.exe`) eller Anaconda-prompt:**
>
> ```cmd
> set PYTHONUTF8=1
> conda env create --name ai4beg --file .devcontainer/environment.yml
> ```
>
> **Bash, inkludert Git Bash:**
>
> ```bash
> export PYTHONUTF8=1
> conda env create --name ai4beg --file .devcontainer/environment.yml
> ```
>
> Hvis et mislykket forsøk etterlot det `ai4beg`-miljøet, deaktiver det og fjern det miljøet før du prøver igjen. Bruk `conda deactivate` først når et miljø er aktivt:
>
> ```text
> conda deactivate
> conda env remove --name ai4beg
> ```

### Bruke Visual Studio Code med Python-utvidelse

Dette pensumet brukes best når du åpner det i [Visual Studio Code](http://code.visualstudio.com/?WT.mc_id=academic-77998-cacaste) med [Python Extension](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-77998-cacaste).

> **Merk**: Når du har klonet og åpnet mappen i VS Code, vil den automatisk foreslå at du installerer Python-utvidelser. Du må også installere miniconda som beskrevet ovenfor.

> **Merk**: Hvis VS Code foreslår at du åpner depotet på nytt i en container, bør du avslå dette for å bruke den lokale Python-installasjonen.

### Bruke Jupyter i nettleseren

Du kan også bruke et Jupyter-miljø fra nettleseren på din egen datamaskin. Både klassisk Jupyter og JupyterHub tilbyr et praktisk utviklingsmiljø med autfullføring, kodeutheving, osv.

For å starte Jupyter lokalt, gå til katalogen for kurset, og kjør:

```bash
jupyter notebook
```
eller
```bash
jupyterhub
```
Du kan da navigere til en av `.ipynb` filene, åpne dem og begynne å arbeide.

### Kjøring i container

Et alternativ til Python-installasjon er å kjøre koden i en container. Siden vårt repo leverer en spesiell `.devcontainer` mappe som instruerer hvordan bygge en container for dette repoet, tilbyr VS Code muligheten til å åpne koden i en container. Dette krever Docker-installasjon, og vil også være mer komplekst, så vi anbefaler dette for mer erfarne brukere.

## Kjøring i skyen

Hvis du ikke vil installere Python lokalt, og har tilgang til noen skyressurser – vil et godt alternativ være å kjøre koden i skyen. Det finnes flere måter å gjøre dette på:

* Bruke **[GitHub Codespaces](https://github.com/features/codespaces)**, som er et virtuelt miljø opprettet for deg på GitHub, tilgjengelig gjennom VS Code-nettlesergrensesnitt. Hvis du har tilgang til Codespaces, kan du bare klikke på **Code**-knappen i repoet, starte et codespace, og komme i gang på et blunk.
* Bruke **[Binder](https://mybinder.org/v2/gh/microsoft/ai-for-beginners/HEAD)**. [Binder](https://mybinder.org) tilbyr gratis datakraft i skyen for folk som deg til å teste kode på GitHub. Det finnes en knapp på førstesiden for å åpne depotet i Binder – dette vil raskt ta deg til bindersiden, som bygger en underliggende container og starter et Jupyter-nettgrensesnitt sømløst for deg.

> **Merk**: For å forhindre misbruk har Binder blokkert tilgang til noen webressurser. Dette kan forhindre at noe av koden som henter modeller og/eller datasett fra det offentlige Internett fungerer. Du må kanskje finne noen løsninger. I tillegg er beregningsressursene fra Binder ganske grunnleggende, så trening vil være sakte, spesielt i senere, mer komplekse leksjoner.

## Kjøring i skyen med GPU

Noen av de senere leksemplene i dette pensumet vil ha stor fordel av støtte for GPU. Modelltrening, for eksempel, kan ellers være smertefullt langsom. Det finnes noen alternativer du kan følge, spesielt hvis du har tilgang til skyen gjennom enten [Azure for Students](https://azure.microsoft.com/free/students/?WT.mc_id=academic-77998-cacaste) eller gjennom din institusjon:

* Opprett [Data Science Virtual Machine](https://docs.microsoft.com/learn/modules/intro-to-azure-data-science-virtual-machine/?WT.mc_id=academic-77998-cacaste) og koble til via Jupyter. Du kan da klone repoet direkte på maskinen, og starte læring. NC-serie VM-er har GPU-støtte.

> **Merk**: Noen abonnementer, inkludert Azure for Students, gir ikke GPU-støtte rett ut av boksen. Du må kanskje be om ekstra GPU-kjerner med en teknisk supportforespørsel.

* Opprett [Azure Machine Learning Workspace](https://azure.microsoft.com/services/machine-learning/?WT.mc_id=academic-77998-cacaste) og bruk Notebook-funksjonen der. [Denne videoen](https://azure-for-academics.github.io/quickstart/azureml-papers/) viser hvordan du kloner et repository inn i Azure ML-notebook og begynner å bruke det.

Du kan også bruke Google Colab, som kommer med noe gratis GPU-støtte, og laste opp Jupyter Notebooks der for å kjøre dem én etter én.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi streber etter nøyaktighet, vær oppmerksom på at automatiske oversettelser kan inneholde feil eller unøyaktigheter. Det opprinnelige dokumentet på originalspråket skal betraktes som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for eventuelle misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->