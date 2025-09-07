<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "7df19702b8d2d3f7c4238c51bec2c8fc",
  "translation_date": "2025-08-28T15:08:51+00:00",
  "source_file": "lessons/0-course-setup/how-to-run.md",
  "language_code": "da"
}
-->
# Sådan kører du koden

Dette kursus indeholder mange eksekverbare eksempler og laboratorier, som du vil ønske at køre. For at gøre dette skal du kunne eksekvere Python-kode i Jupyter Notebooks, der leveres som en del af dette kursus. Du har flere muligheder for at køre koden:

## Kør lokalt på din computer

For at køre koden lokalt på din computer skal du have en version af Python installeret. Jeg anbefaler personligt at installere **[miniconda](https://conda.io/en/latest/miniconda.html)** - det er en let installation, der understøtter `conda`-pakkehåndtering til forskellige Python **virtuelle miljøer**.

Efter du har installeret miniconda, skal du klone repositoryet og oprette et virtuelt miljø, der skal bruges til dette kursus:

```bash
git clone http://github.com/microsoft/ai-for-beginners
cd ai-for-beginners
conda env create --name ai4beg --file .devcontainer/environment.yml
conda activate ai4beg
```

### Brug af Visual Studio Code med Python-udvidelse

Den bedste måde at bruge kurset på er sandsynligvis at åbne det i [Visual Studio Code](http://code.visualstudio.com/?WT.mc_id=academic-77998-cacaste) med [Python-udvidelse](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-77998-cacaste).

> **Note**: Når du kloner og åbner mappen i VS Code, vil det automatisk foreslå dig at installere Python-udvidelser. Du skal også installere miniconda som beskrevet ovenfor.

> **Note**: Hvis VS Code foreslår, at du genåbner repositoryet i en container, skal du afvise dette for at bruge den lokale Python-installation.

### Brug af Jupyter i browseren

Du kan også bruge Jupyter-miljøet direkte fra browseren på din egen computer. Faktisk tilbyder både klassisk Jupyter og Jupyter Hub et ret praktisk udviklingsmiljø med autoudfyldning, kodefremhævning osv.

For at starte Jupyter lokalt skal du gå til kursusmappen og eksekvere:

```bash
jupyter notebook
```  
eller  
```bash
jupyterhub
```  
Du kan derefter navigere til en af `.ipynb`-filerne, åbne dem og begynde at arbejde.

### Kørsel i container

Et alternativ til Python-installation er at køre koden i en container. Da vores repository indeholder en speciel `.devcontainer`-mappe, der instruerer, hvordan man bygger en container til dette repo, vil VS Code tilbyde dig at genåbne koden i en container. Dette kræver Docker-installation og er mere komplekst, så vi anbefaler dette til mere erfarne brugere.

## Kørsel i skyen

Hvis du ikke ønsker at installere Python lokalt og har adgang til nogle cloud-ressourcer, er en god alternativ mulighed at køre koden i skyen. Der er flere måder, du kan gøre dette på:

* Brug **[GitHub Codespaces](https://github.com/features/codespaces)**, som er et virtuelt miljø oprettet for dig på GitHub, tilgængeligt via VS Code-browsergrænsefladen. Hvis du har adgang til Codespaces, kan du blot klikke på **Code**-knappen i repoet, starte en codespace og komme i gang med det samme.
* Brug **[Binder](https://mybinder.org/v2/gh/microsoft/ai-for-beginners/HEAD)**. [Binder](https://mybinder.org) er gratis cloud-ressourcer, der stilles til rådighed for folk som dig til at teste noget kode på GitHub. Der er en knap på forsiden til at åbne repositoryet i Binder - dette bør hurtigt tage dig til Binder-siden, som vil bygge den underliggende container og starte Jupyter-webgrænsefladen for dig problemfrit.

> **Note**: For at forhindre misbrug har Binder blokeret adgang til nogle webressourcer. Dette kan forhindre noget af koden i at fungere, som henter modeller og/eller datasæt fra det offentlige internet. Du kan være nødt til at finde nogle løsninger. Desuden er de computermæssige ressourcer, der leveres af Binder, ret begrænsede, så træning vil være langsom, især i senere og mere komplekse lektioner.

## Kørsel i skyen med GPU

Nogle af de senere lektioner i dette kursus vil drage stor fordel af GPU-understøttelse, da træning ellers vil være meget langsom. Der er et par muligheder, du kan følge, især hvis du har adgang til skyen enten via [Azure for Students](https://azure.microsoft.com/free/students/?WT.mc_id=academic-77998-cacaste) eller via din institution:

* Opret en [Data Science Virtual Machine](https://docs.microsoft.com/learn/modules/intro-to-azure-data-science-virtual-machine/?WT.mc_id=academic-77998-cacaste) og forbind til den via Jupyter. Du kan derefter klone repoet direkte på maskinen og begynde at lære. NC-seriens virtuelle maskiner har GPU-understøttelse.

> **Note**: Nogle abonnementer, inklusive Azure for Students, tilbyder ikke GPU-understøttelse som standard. Du kan være nødt til at anmode om yderligere GPU-kerner via en teknisk supportanmodning.

* Opret et [Azure Machine Learning Workspace](https://azure.microsoft.com/services/machine-learning/?WT.mc_id=academic-77998-cacaste) og brug derefter Notebook-funktionen der. [Denne video](https://azure-for-academics.github.io/quickstart/azureml-papers/) viser, hvordan man kloner et repository til Azure ML Notebook og begynder at bruge det.

Du kan også bruge Google Colab, som tilbyder noget gratis GPU-understøttelse, og uploade Jupyter Notebooks der for at eksekvere dem én efter én.

---

**Ansvarsfraskrivelse**:  
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på nøjagtighed, skal du være opmærksom på, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det originale dokument på dets oprindelige sprog bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi påtager os ikke ansvar for eventuelle misforståelser eller fejltolkninger, der opstår som følge af brugen af denne oversættelse.