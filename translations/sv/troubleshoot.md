# AI-For-Beginners Felsökningsguide

Den här guiden hjälper dig att lösa vanliga problem som kan uppstå när du använder eller bidrar till [AI-For-Beginners](https://github.com/microsoft/AI-For-Beginners)-repositoryn. Varje problem inkluderar bakgrund, symtom, förklaringar och steg-för-steg-lösningar.

---

## Innehållsförteckning

- [Allmänna problem](../..)
- [Installationsproblem](../..)
- [Konfigurationsproblem](../..)
- [Köra notebooks](../..)
- [Prestandaproblem](../..)
- [Problem med lärobokswebbplatsen](../..)
- [Problem med att bidra](../..)
- [FAQ](../..)
- [Få hjälp](../..)

---

## Allmänna problem

### 1. Repositoryn klonas inte korrekt

**Bakgrund:** Kloning gör att du kan kopiera repositoryn till din dator.

**Symtom:**
- Fel: `fatal: repository not found`
- Fel: `Permission denied (publickey)`

**Möjliga orsaker:**
- Felaktig repository-URL
- Otillräckliga behörigheter
- SSH-nycklar är inte konfigurerade

**Lösningar:**
1. **Kontrollera repository-URL.**  
   Använd HTTPS-URL:  
   ```
   git clone https://github.com/microsoft/AI-For-Beginners.git
   ```
2. **Byt till HTTPS om SSH misslyckas.**  
   Om du ser `Permission denied (publickey)`, använd HTTPS-länken ovan istället för SSH.
3. **Konfigurera SSH-nycklar (valfritt).**  
   Om du vill använda SSH, följ [GitHubs SSH-guide](https://docs.github.com/en/authentication/connecting-to-github-with-ssh).

---

## Installationsproblem

### 2. Problem med Python-miljön

**Bakgrund:** Repositoryn är beroende av Python och olika bibliotek.

**Symtom:**
- Fel: `ModuleNotFoundError: No module named '<package>'`
- Importfel när du kör skript eller notebooks

**Möjliga orsaker:**
- Beroenden är inte installerade
- Fel Python-version

**Lösningar:**
1. **Ställ in en virtuell miljö.**  
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```
2. **Installera beroenden.**  
   ```bash
   pip install -r requirements.txt
   ```
3. **Kontrollera Python-versionen.**  
   Använd Python 3.7 eller nyare.  
   ```bash
   python --version
   ```

### 3. Jupyter är inte installerat

**Bakgrund:** Notebooks är en central lärresurs.

**Symtom:**
- Fel: `jupyter: command not found`
- Notebooks misslyckas med att starta

**Möjliga orsaker:**
- Jupyter är inte installerat

**Lösningar:**
1. **Installera Jupyter Notebook.**  
   ```bash
   pip install notebook
   ```
   eller, om du använder Anaconda:
   ```bash
   conda install notebook
   ```
2. **Starta Jupyter Notebook.**  
   ```bash
   jupyter notebook
   ```

### 4. Konflikter mellan beroendeversioner

**Bakgrund:** Projekt kan sluta fungera om paketversioner inte matchar.

**Symtom:**
- Fel eller varningar om inkompatibla versioner

**Möjliga orsaker:**
- Gamla eller motstridiga Python-paket

**Lösningar:**
1. **Installera i en ren miljö.**  
   Ta bort gammal venv/conda-miljö och skapa en ny.
2. **Använd exakta versioner.**  
   Kör alltid:
   ```bash
   pip install -r requirements.txt
   ```
   Om detta misslyckas, installera saknade paket manuellt enligt README.

---

## Konfigurationsproblem

### 5. Miljövariabler är inte inställda

**Bakgrund:** Vissa moduler kan kräva nycklar, tokens eller konfigurationsinställningar.

**Symtom:**
- Fel: `KeyError` eller varningar om saknad konfiguration

**Möjliga orsaker:**
- Nödvändiga miljövariabler är inte inställda

**Lösningar:**
1. **Kontrollera `.env.example` eller liknande filer.**
2. **Skapa en `.env`-fil och fyll i nödvändiga värden.**
3. **Ladda om din terminal eller IDE efter att ha ställt in miljövariabler.**

---

## Köra notebooks

### 6. Notebook öppnas eller körs inte

**Bakgrund:** Jupyter notebooks kräver korrekt installation.

**Symtom:**
- Notebook misslyckas med att starta
- Webbläsaren öppnas inte automatiskt

**Möjliga orsaker:**
- Jupyter är inte installerat
- Problem med webbläsarkonfiguration

**Lösningar:**
1. **Installera Jupyter (se Installationsproblem ovan).**
2. **Öppna notebooks manuellt.**
   - Kopiera URL från terminalen (t.ex. `http://localhost:8888/?token=...`) och klistra in den i din webbläsare.

### 7. Kernel kraschar eller fryser

**Bakgrund:** Notebook-kärnor kan krascha på grund av resursbegränsningar eller kodfel.

**Symtom:**
- Kernel dör eller startar om upprepade gånger
- Fel relaterade till minnesbrist

**Möjliga orsaker:**
- Stora dataset
- Inkompatibel kod eller paket

**Lösningar:**
1. **Starta om kärnan.**  
   Använd knappen "Restart Kernel" i Jupyter.
2. **Kontrollera minnesanvändning.**  
   Stäng oanvända applikationer.
3. **Kör notebooks på molnplattformar.**  
   Använd [Google Colab](https://colab.research.google.com/) eller [Azure Notebooks](https://notebooks.azure.com/).

---

## Prestandaproblem

### 8. Notebooks körs långsamt

**Bakgrund:** Vissa AI-uppgifter kräver mycket minne och CPU.

**Symtom:**
- Långsam exekvering
- Laptopens fläkt går högt

**Möjliga orsaker:**
- Stora dataset eller modeller
- Begränsade systemresurser

**Lösningar:**
1. **Använd en molnplattform.**
   - Ladda upp notebook till Colab eller Azure Notebooks.
2. **Minska datasetets storlek.**
   - Använd exempeldata för övning.
3. **Stäng onödiga program.**
   - Frigör systemets RAM.

---

## Problem med lärobokswebbplatsen

### 9. Kapitel laddas inte

**Bakgrund:** Den onlinebaserade läroboken visar lektioner och kapitel.

**Symtom:**
- Ett kapitel (t.ex. Transformers/BERT) saknas eller öppnas inte

**Känt problem:**  
- [Problem #303](https://github.com/microsoft/AI-For-Beginners/issues/303): “18 Transformers. BERT. kan inte öppnas på lärobokswebbplatsen.” Orsakat av ett filnamnsfel (`READMEtransformers.md` istället för `README.md`).

**Lösningar:**
1. **Kontrollera filnamnsfel.**  
   Om du är en bidragsgivare, se till att kapitel-filer är namngivna `README.md`.
2. **Rapportera saknade filer.**  
   Öppna ett GitHub-problem med kapitelnamnet och felinformationen.

---

## Problem med att bidra

### 10. PR accepteras inte eller byggen misslyckas

**Bakgrund:** Bidrag måste klara tester och följa riktlinjer.

**Symtom:**
- Pull request avvisad
- CI/CD-pipelinefel

**Möjliga orsaker:**
- Misslyckade tester
- Kodstandarder följs inte

**Lösningar:**
1. **Läs riktlinjerna för bidrag.**
   - Följ repositoryns [CONTRIBUTING.md](https://github.com/microsoft/AI-For-Beginners/blob/main/CONTRIBUTING.md).
2. **Kör tester lokalt innan du pushar.**
3. **Kontrollera regler för kodformatering eller linting.**

---

## FAQ

### Var kan jag hitta hjälp för specifika moduler?
- Varje modul har vanligtvis sin egen README. Börja där för installations- och användningstips.

### Hur rapporterar jag en bugg eller begär en funktion?
- [Öppna ett GitHub-problem](https://github.com/microsoft/AI-For-Beginners/issues/new) med en tydlig beskrivning och steg för att återskapa problemet.

### Kan jag be om hjälp om mitt problem inte finns med?
- Ja! Sök först bland befintliga problem, och om du inte hittar ditt problem, skapa ett nytt.

---

## Få hjälp

- **Kontrollera problem:** [GitHub-problem](https://github.com/microsoft/AI-For-Beginners/issues)
- **Ställ frågor:** Använd GitHub-diskussioner eller öppna ett problem.
- **Community:** Se repositoryns länkar för chatt-/forumalternativ.

---

_Senast uppdaterad: 2025-09-20_

---

**Ansvarsfriskrivning**:  
Detta dokument har översatts med hjälp av AI-översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Även om vi strävar efter noggrannhet, bör det noteras att automatiserade översättningar kan innehålla fel eller felaktigheter. Det ursprungliga dokumentet på dess ursprungliga språk bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för eventuella missförstånd eller feltolkningar som uppstår vid användning av denna översättning.