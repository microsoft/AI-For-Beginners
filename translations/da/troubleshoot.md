# AI-For-Beginners Fejlfindingsguide

Denne guide hjælper dig med at løse almindelige problemer, der opstår ved brug eller bidrag til [AI-For-Beginners](https://github.com/microsoft/AI-For-Beginners)-repositoryet. Hvert problem inkluderer baggrund, symptomer, forklaringer og trin-for-trin løsninger.

---

## Indholdsfortegnelse

- [Generelle Problemer](../..)
- [Installationsproblemer](../..)
- [Konfigurationsproblemer](../..)
- [Kørsel af Notebooks](../..)
- [Ydelsesproblemer](../..)
- [Problemer med Tekstbogswebsiden](../..)
- [Bidragsproblemer](../..)
- [FAQ](../..)
- [Få Hjælp](../..)

---

## Generelle Problemer

### 1. Repository Kloner Ikke Korrekt

**Baggrund:** Kloning giver dig mulighed for at kopiere repositoryet til din maskine.

**Symptomer:**
- Fejl: `fatal: repository not found`
- Fejl: `Permission denied (publickey)`

**Mulige Årsager:**
- Forkert repository-URL
- Utilstrækkelige tilladelser
- SSH-nøgler ikke konfigureret

**Løsninger:**
1. **Kontroller repository-URL'en.**  
   Brug HTTPS-URL'en:  
   ```
   git clone https://github.com/microsoft/AI-For-Beginners.git
   ```
2. **Skift til HTTPS, hvis SSH fejler.**  
   Hvis du ser `Permission denied (publickey)`, brug HTTPS-linket ovenfor i stedet for SSH.
3. **Konfigurer SSH-nøgler (valgfrit).**  
   Hvis du vil bruge SSH, følg [GitHubs SSH-guide](https://docs.github.com/en/authentication/connecting-to-github-with-ssh).

---

## Installationsproblemer

### 2. Problemer med Python-miljø

**Baggrund:** Repositoryet er afhængigt af Python og forskellige biblioteker.

**Symptomer:**
- Fejl: `ModuleNotFoundError: No module named '<package>'`
- Importfejl ved kørsel af scripts eller notebooks

**Mulige Årsager:**
- Afhængigheder ikke installeret
- Forkert Python-version

**Løsninger:**
1. **Opsæt et virtuelt miljø.**  
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```
2. **Installer afhængigheder.**  
   ```bash
   pip install -r requirements.txt
   ```
3. **Kontroller Python-versionen.**  
   Brug Python 3.7 eller nyere.  
   ```bash
   python --version
   ```

### 3. Jupyter Ikke Installeret

**Baggrund:** Notebooks er en central læringsressource.

**Symptomer:**
- Fejl: `jupyter: command not found`
- Notebooks kan ikke startes

**Mulige Årsager:**
- Jupyter ikke installeret

**Løsninger:**
1. **Installer Jupyter Notebook.**  
   ```bash
   pip install notebook
   ```
   eller, hvis du bruger Anaconda:
   ```bash
   conda install notebook
   ```
2. **Start Jupyter Notebook.**  
   ```bash
   jupyter notebook
   ```

### 4. Konflikter med Afhængighedsversioner

**Baggrund:** Projekter kan gå i stykker, hvis pakkeversioner ikke matcher.

**Symptomer:**
- Fejl eller advarsler om inkompatible versioner

**Mulige Årsager:**
- Gamle eller konfliktende Python-pakker

**Løsninger:**
1. **Installer i et rent miljø.**  
   Slet gamle venv/conda-miljøer og opret et nyt.
2. **Brug præcise versioner.**  
   Kør altid:
   ```bash
   pip install -r requirements.txt
   ```
   Hvis dette fejler, installer manglende pakker manuelt som beskrevet i README.

---

## Konfigurationsproblemer

### 5. Miljøvariabler Ikke Sat

**Baggrund:** Nogle moduler kan kræve nøgler, tokens eller konfigurationsindstillinger.

**Symptomer:**
- Fejl: `KeyError` eller advarsler om manglende konfiguration

**Mulige Årsager:**
- Påkrævede miljøvariabler ikke sat

**Løsninger:**
1. **Kontroller `.env.example` eller lignende filer.**
2. **Opret en `.env`-fil og udfyld påkrævede værdier.**
3. **Genindlæs din terminal eller IDE efter at have sat miljøvariabler.**

---

## Kørsel af Notebooks

### 6. Notebook Kan Ikke Åbnes eller Køre

**Baggrund:** Jupyter-notebooks kræver korrekt opsætning.

**Symptomer:**
- Notebook kan ikke startes
- Browser åbner ikke automatisk

**Mulige Årsager:**
- Jupyter ikke installeret
- Browserkonfigurationsproblemer

**Løsninger:**
1. **Installer Jupyter (se Installationsproblemer ovenfor).**
2. **Åbn notebooks manuelt.**
   - Kopier URL'en fra terminalen (f.eks. `http://localhost:8888/?token=...`) og indsæt den i din browser.

### 7. Kernel Crasher eller Fryser

**Baggrund:** Notebook-kernels kan crashe på grund af ressourcebegrænsninger eller kodefejl.

**Symptomer:**
- Kernel dør eller genstarter gentagne gange
- Fejl om manglende hukommelse

**Mulige Årsager:**
- Store datasæt
- Inkompatibel kode eller pakker

**Løsninger:**
1. **Genstart kernel.**  
   Brug "Restart Kernel"-knappen i Jupyter.
2. **Kontroller hukommelsesforbrug.**  
   Luk ubrugte applikationer.
3. **Kør notebooks på cloud-platforme.**  
   Brug [Google Colab](https://colab.research.google.com/) eller [Azure Notebooks](https://notebooks.azure.com/).

---

## Ydelsesproblemer

### 8. Notebooks Kører Langsomt

**Baggrund:** Nogle AI-opgaver kræver betydelig hukommelse og CPU.

**Symptomer:**
- Langsom udførelse
- Laptopens blæser kører højt

**Mulige Årsager:**
- Store datasæt eller modeller
- Begrænsede systemressourcer

**Løsninger:**
1. **Brug en cloud-platform.**
   - Upload notebook til Colab eller Azure Notebooks.
2. **Reducer datasætstørrelse.**
   - Brug prøvedata til øvelse.
3. **Luk unødvendige programmer.**
   - Frigør systemets RAM.

---

## Problemer med Tekstbogswebsiden

### 9. Kapitel Indlæses Ikke

**Baggrund:** Den online tekstbog viser lektioner og kapitler.

**Symptomer:**
- Et kapitel (f.eks. Transformers/BERT) mangler eller åbner ikke

**Kendt Problem:**  
- [Issue #303](https://github.com/microsoft/AI-For-Beginners/issues/303): “18 Transformers. BERT. kan ikke åbnes på tekstbogswebsiden.” Forårsaget af en filnavnsfejl (`READMEtransformers.md` i stedet for `README.md`).

**Løsninger:**
1. **Kontroller for fejl i filnavngivning.**  
   Hvis du er bidragsyder, sørg for, at kapitel-filer hedder `README.md`.
2. **Rapporter manglende filer.**  
   Åbn en GitHub-issue med kapitelnavn og fejlbeskrivelse.

---

## Bidragsproblemer

### 10. PR Ikke Accepteret eller Builds Fejler

**Baggrund:** Bidrag skal bestå tests og følge retningslinjer.

**Symptomer:**
- Pull request afvist
- CI/CD-pipeline fejl

**Mulige Årsager:**
- Fejlende tests
- Manglende overholdelse af kodestandarder

**Løsninger:**
1. **Læs bidragsretningslinjerne.**
   - Følg repositoryets [CONTRIBUTING.md](https://github.com/microsoft/AI-For-Beginners/blob/main/CONTRIBUTING.md).
2. **Kør tests lokalt før du pusher.**
3. **Kontroller for linting-regler eller formateringskrav.**

---

## FAQ

### Hvor kan jeg finde hjælp til specifikke moduler?
- Hvert modul har normalt sin egen README. Start der for opsætnings- og brugstips.

### Hvordan rapporterer jeg en fejl eller anmoder om en funktion?
- [Åbn en GitHub Issue](https://github.com/microsoft/AI-For-Beginners/issues/new) med en klar beskrivelse og trin til at genskabe problemet.

### Kan jeg bede om hjælp, hvis mit problem ikke er nævnt?
- Ja! Søg først efter eksisterende issues, og hvis du ikke finder dit problem, opret en ny issue.

---

## Få Hjælp

- **Kontroller Issues:** [GitHub Issues](https://github.com/microsoft/AI-For-Beginners/issues)
- **Stil Spørgsmål:** Brug GitHub Discussions eller åbn en issue.
- **Fællesskab:** Se repository-links for chat-/forum-muligheder.

---

_Sidst Opdateret: 2025-09-20_

---

**Ansvarsfraskrivelse**:  
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på nøjagtighed, skal det bemærkes, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det originale dokument på dets oprindelige sprog bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi påtager os ikke ansvar for eventuelle misforståelser eller fejltolkninger, der måtte opstå som følge af brugen af denne oversættelse.