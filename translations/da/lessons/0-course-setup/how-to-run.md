# Hvordan man kører koden

Dette pensum indeholder mange eksempler og laboratorier, som du gerne vil køre. For at gøre dette, skal du kunne køre Python-kode i Jupyter Notebooks, som følger med dette pensum. Du har flere muligheder for at køre koden:

## Kør lokalt på din computer

For at køre koden lokalt på din computer kræves en Python-installation. En anbefaling er at installere **[miniconda](https://conda.io/en/latest/miniconda.html)** - det er en forholdsvis let installation, som understøtter `conda` pakkehåndteringen for forskellige Python **virtuelle miljøer**.

Efter du har installeret miniconda, skal du klone repository'et og oprette et virtuelt miljø, som skal bruges til dette kursus:

```bash
git clone http://github.com/microsoft/ai-for-beginners
cd ai-for-beginners
conda env create --name ai4beg --file .devcontainer/environment.yml
conda activate ai4beg
```

> **Windows-notat**: Hvis oprettelsen af miljø mislykkes ved installation af `gdk-pixbuf` med en `UnicodeDecodeError`, der nævner `gbk` kodek, så aktiver Python’s UTF-8-tilstand i din terminal og prøv igen. Brug syntaksen til den terminal, du bruger:
>
> **PowerShell:**
>
> ```powershell
> $env:PYTHONUTF8 = "1"
> conda env create --name ai4beg --file .devcontainer/environment.yml
> ```
>
> **Kommandoprompt (`cmd.exe`) eller Anaconda Prompt:**
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
> Hvis et mislykket forsøg efterlod `ai4beg` miljøet, deaktiver det og fjern det miljø før du prøver igen. Brug `conda deactivate` først, når et miljø er aktivt:
>
> ```text
> conda deactivate
> conda env remove --name ai4beg
> ```

### Brug af Visual Studio Code med Python Extension

Dette pensum bruges bedst, når det åbnes i [Visual Studio Code](http://code.visualstudio.com/?WT.mc_id=academic-77998-cacaste) med [Python Extension](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-77998-cacaste).

> **Bemærk**: Når du kloner og åbner mappen i VS Code, vil det automatisk foreslå, at du installerer Python-udvidelser. Du skal også installere miniconda som beskrevet ovenfor.

> **Bemærk**: Hvis VS Code foreslår, at du åbner repository'et igen i en container, bør du takke nej for at bruge den lokale Python-installation.

### Brug af Jupyter i browseren

Du kan også bruge et Jupyter-miljø fra browseren på din egen computer. Både klassisk Jupyter og JupyterHub giver et praktisk udviklingsmiljø med autoudfyldelse, kodefremhævning osv.

For at starte Jupyter lokalt, gå til mappen for kurset, og kør:

```bash
jupyter notebook
```
eller
```bash
jupyterhub
```
Du kan derefter navigere til en hvilken som helst af `.ipynb` filerne, åbne dem og begynde at arbejde.

### Kørsel i container

Et alternativ til Python-installation er at køre koden i en container. Da vores repository leverer en særlig `.devcontainer` mappe, der instruerer, hvordan man bygger en container til dette repo, tilbyder VS Code muligheden for at genåbne koden i en container. Dette kræver Docker-installation og er også mere komplekst, så vi anbefaler dette til mere erfarne brugere.

## Kørsel i skyen

Hvis du ikke ønsker at installere Python lokalt, og har adgang til nogle skyressourcer – er et godt alternativ at køre koden i skyen. Der er flere måder, du kan gøre dette på:

* Brug af **[GitHub Codespaces](https://github.com/features/codespaces)**, som er et virtuelt miljø oprettet for dig på GitHub, tilgængeligt gennem en VS Code browsergrænseflade. Hvis du har adgang til Codespaces, kan du bare klikke på **Code** knappen i repoet, starte en codespace og komme i gang hurtigt.
* Brug af **[Binder](https://mybinder.org/v2/gh/microsoft/ai-for-beginners/HEAD)**. [Binder](https://mybinder.org) tilbyder gratis beregningsressourcer i skyen til folk som dig til at teste kode på GitHub. Der er en knap på forsiden til at åbne repository’et i Binder – det tager dig hurtigt til binder-siden, som bygger en underliggende container og starter en Jupyter webgrænseflade til dig uden problemer.

> **Bemærk**: For at forhindre misbrug, har Binder adgang til nogle webressourcer blokeret. Det kan forhindre noget af koden i at fungere, hvor der hentes modeller og/eller datasæt fra det offentlige Internet. Du kan få brug for nogle løsninger. Også, de beregningsressourcer, som Binder stiller til rådighed, er rimelige grundlæggende, så træning vil være langsom, især i senere, mere komplekse lektioner.

## Kørsel i skyen med GPU

Nogle af de senere lektioner i dette pensum vil have stor fordel af GPU-understøttelse. Modelltræning, for eksempel, kan være smertefuldt langsomt ellers. Der er et par muligheder, du kan følge, især hvis du har adgang til skyen enten gennem [Azure for Students](https://azure.microsoft.com/free/students/?WT.mc_id=academic-77998-cacaste) eller gennem din institution:

* Opret [Data Science Virtual Machine](https://docs.microsoft.com/learn/modules/intro-to-azure-data-science-virtual-machine/?WT.mc_id=academic-77998-cacaste) og forbind til den gennem Jupyter. Du kan så klone repoet direkte på maskinen og starte læringen. NC-serier VMer har GPU-understøttelse.

> **Bemærk**: Nogle abonnementer, inklusive Azure for Students, giver ikke GPU-understøttelse som standard. Du skal muligvis anmode om yderligere GPU-kerner med en teknisk supportanmodning.

* Opret [Azure Machine Learning Workspace](https://azure.microsoft.com/services/machine-learning/?WT.mc_id=academic-77998-cacaste) og brug derefter Notebook-funktionen der. [Denne video](https://azure-for-academics.github.io/quickstart/azureml-papers/) viser hvordan man kloner et repository ind i Azure ML-notebook og begynder at bruge det.

Du kan også bruge Google Colab, som kommer med noget gratis GPU-understøttelse, og uploade Jupyter Notebooks der for at køre dem enkeltvis.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på nøjagtighed, skal du være opmærksom på, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det originale dokument på dets oprindelige sprog bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi påtager os intet ansvar for misforståelser eller fejltolkninger, der opstår som følge af brugen af denne oversættelse.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->