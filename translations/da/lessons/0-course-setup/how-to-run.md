# Sådan kører du koden

Dette kursusindhold indeholder mange eksekverbare eksempler og laboratorier, som du vil ønske at køre. For at kunne gøre dette, har du brug for muligheden for at eksekvere Python-kode i Jupyter Notebooks, som leveres som en del af dette kursusindhold. Du har flere muligheder for at køre koden:

## Kør lokalt på din computer

For at køre koden lokalt på din computer, er der brug for en Python-installation. En anbefaling er at installere **[miniconda](https://conda.io/en/latest/miniconda.html)** - det er en forholdsvis letvægtsinstallation, der understøtter `conda` pakkestyringsværktøjet til forskellige Python **virtuelle miljøer**.

Efter du har installeret miniconda, klon da repositoryet og opret et virtuelt miljø, der skal bruges til dette kursus:

```bash
git clone http://github.com/microsoft/ai-for-beginners
cd ai-for-beginners
conda env create --name ai4beg --file .devcontainer/environment.yml
conda activate ai4beg
```

### Brug af Visual Studio Code med Python Extension

Dette kursusindhold bruges bedst ved at åbne det i [Visual Studio Code](http://code.visualstudio.com/?WT.mc_id=academic-77998-cacaste) med [Python Extension](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-77998-cacaste).

> **Note**: Når du har klonet og åbnet mappen i VS Code, vil det automatisk foreslå dig at installere Python-udvidelser. Du skal også installere miniconda som beskrevet ovenfor.

> **Note**: Hvis VS Code foreslår dig at genåbne repositoryet i en container, bør du afslå dette for at bruge den lokale Python-installation.

### Brug af Jupyter i browseren

Du kan også bruge et Jupyter-miljø fra browseren på din egen computer. Både klassisk Jupyter og JupyterHub tilbyder et praktisk udviklingsmiljø med autofuldendelse, kodefremhævning osv.

For at starte Jupyter lokalt, gå til kursusmappen, og eksekver:

```bash
jupyter notebook
```
eller
```bash
jupyterhub
```
Du kan derefter navigere til en hvilken som helst af `.ipynb` filerne, åbne dem og begynde at arbejde.

### Kørsel i container

Et alternativ til Python-installation ville være at køre koden i en container. Da vores repository leverer en særlig `.devcontainer` mappe, der instruerer hvordan man bygger en container til dette repo, tilbyder VS Code muligheden for at genåbne koden i en container. Dette kræver installation af Docker og er også mere komplekst, så vi anbefaler dette til mere erfarne brugere.

## Kørsel i skyen

Hvis du ikke ønsker at installere Python lokalt, og har adgang til nogle skyeressourcer – er et godt alternativ at køre koden i skyen. Der er flere måder, du kan gøre dette på:

* Brug af **[GitHub Codespaces](https://github.com/features/codespaces)**, som er et virtuelt miljø oprettet for dig på GitHub, tilgængeligt gennem en VS Code browsergrænseflade. Hvis du har adgang til Codespaces, kan du blot klikke på **Code** knappen i repositoriet, starte et codespace og komme i gang med det samme.
* Brug af **[Binder](https://mybinder.org/v2/gh/microsoft/ai-for-beginners/HEAD)**. [Binder](https://mybinder.org) tilbyder gratis beregningsressourcer i skyen til folk som dig, der vil teste noget kode på GitHub. Der er en knap på forsiden til at åbne repositoryet i Binder – dette vil hurtigt føre dig til binder-sitet, som vil bygge en underliggende container og starte en Jupyter webgrænseflade for dig glidende.

> **Note**: For at forhindre misbrug har Binder adgang til nogle webressourcer blokeret. Dette kan forhindre noget kode i at fungere, som henter modeller og/eller datasæt fra det offentlige Internet. Du skal måske finde nogle alternative løsninger. Derudover er de beregningsressourcer, som Binder tilbyder, ret simple, så træning vil gå langsomt, især i de senere, mere komplekse lektioner.

## Kørsel i skyen med GPU

Nogle af de senere lektioner i dette kursusindhold vil have stor gavn af GPU-understøttelse. Modeltræning, for eksempel, kan være smertefuldt langsomt ellers. Der er et par muligheder, du kan følge, især hvis du har adgang til skyen enten gennem [Azure for Students](https://azure.microsoft.com/free/students/?WT.mc_id=academic-77998-cacaste), eller gennem din institution:

* Opret en [Data Science Virtual Machine](https://docs.microsoft.com/learn/modules/intro-to-azure-data-science-virtual-machine/?WT.mc_id=academic-77998-cacaste) og forbind til den gennem Jupyter. Du kan så klone repoet direkte på maskinen og begynde at lære. NC-serie VM’er har GPU-understøttelse.

> **Note**: Nogle abonnementer, inklusiv Azure for Students, tilbyder ikke GPU-understøttelse som standard. Du skal muligvis anmode om ekstra GPU-kerner via en teknisk supportsag.

* Opret et [Azure Machine Learning Workspace](https://azure.microsoft.com/services/machine-learning/?WT.mc_id=academic-77998-cacaste) og brug dernæst Notebook-funktionen. [Denne video](https://azure-for-academics.github.io/quickstart/azureml-papers/) viser, hvordan man kloner et repository ind i Azure ML notebook og begynder at bruge det.

Du kan også bruge Google Colab, som kommer med noget gratis GPU-understøttelse, og uploade Jupyter Notebooks der for at eksekvere dem én efter én.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:  
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på nøjagtighed, skal du være opmærksom på, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det oprindelige dokument på dets modersmål skal betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi påtager os ikke ansvar for misforståelser eller fejltolkninger, der opstår ved brug af denne oversættelse.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->