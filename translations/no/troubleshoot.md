# AI-For-Beginners Feilsøkingsguide

Denne guiden hjelper deg med å løse vanlige problemer som oppstår når du bruker eller bidrar til [AI-For-Beginners](https://github.com/microsoft/AI-For-Beginners)-repositoryet. Hvert problem inkluderer bakgrunn, symptomer, forklaringer og trinnvise løsninger.

---

## Innholdsfortegnelse

- [Generelle Problemer](../..)
- [Installasjonsproblemer](../..)
- [Konfigurasjonsproblemer](../..)
- [Kjøre Notebooks](../..)
- [Ytelsesproblemer](../..)
- [Problemer med Læreboknettstedet](../..)
- [Bidragsproblemer](../..)
- [FAQ](../..)
- [Få Hjelp](../..)

---

## Generelle Problemer

### 1. Repository Kloner Ikke Riktig

**Bakgrunn:** Kloning lar deg kopiere repositoryet til din maskin.

**Symptomer:**
- Feil: `fatal: repository not found`
- Feil: `Permission denied (publickey)`

**Mulige Årsaker:**
- Feil repository-URL
- Manglende tillatelser
- SSH-nøkler ikke konfigurert

**Løsninger:**
1. **Sjekk repository-URL.**  
   Bruk HTTPS-URL:  
   ```
   git clone https://github.com/microsoft/AI-For-Beginners.git
   ```
2. **Bytt til HTTPS hvis SSH feiler.**  
   Hvis du ser `Permission denied (publickey)`, bruk HTTPS-lenken ovenfor i stedet for SSH.
3. **Konfigurer SSH-nøkler (valgfritt).**  
   Hvis du vil bruke SSH, følg [GitHubs SSH-guide](https://docs.github.com/en/authentication/connecting-to-github-with-ssh).

---

## Installasjonsproblemer

### 2. Problemer med Python-miljø

**Bakgrunn:** Repositoryet er avhengig av Python og ulike biblioteker.

**Symptomer:**
- Feil: `ModuleNotFoundError: No module named '<package>'`
- Importfeil når du kjører skript eller notebooks

**Mulige Årsaker:**
- Avhengigheter ikke installert
- Feil Python-versjon

**Løsninger:**
1. **Sett opp et virtuelt miljø.**  
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```
2. **Installer avhengigheter.**  
   ```bash
   pip install -r requirements.txt
   ```
3. **Sjekk Python-versjon.**  
   Bruk Python 3.7 eller nyere.  
   ```bash
   python --version
   ```

### 3. Jupyter Ikke Installert

**Bakgrunn:** Notebooks er en sentral læringsressurs.

**Symptomer:**
- Feil: `jupyter: command not found`
- Notebooks starter ikke

**Mulige Årsaker:**
- Jupyter ikke installert

**Løsninger:**
1. **Installer Jupyter Notebook.**  
   ```bash
   pip install notebook
   ```
   eller, hvis du bruker Anaconda:
   ```bash
   conda install notebook
   ```
2. **Start Jupyter Notebook.**  
   ```bash
   jupyter notebook
   ```

### 4. Konflikter med Avhengighetsversjoner

**Bakgrunn:** Prosjekter kan slutte å fungere hvis pakkeversjoner ikke stemmer overens.

**Symptomer:**
- Feil eller advarsler om inkompatible versjoner

**Mulige Årsaker:**
- Gamle eller motstridende Python-pakker

**Løsninger:**
1. **Installer i et rent miljø.**  
   Slett gammelt venv/conda-miljø og opprett et nytt.
2. **Bruk eksakte versjoner.**  
   Kjør alltid:
   ```bash
   pip install -r requirements.txt
   ```
   Hvis dette feiler, installer manglende pakker manuelt som beskrevet i README.

---

## Konfigurasjonsproblemer

### 5. Miljøvariabler Ikke Satt

**Bakgrunn:** Noen moduler kan kreve nøkler, tokens eller konfigurasjonsinnstillinger.

**Symptomer:**
- Feil: `KeyError` eller advarsler om manglende konfigurasjon

**Mulige Årsaker:**
- Nødvendige miljøvariabler ikke satt

**Løsninger:**
1. **Sjekk etter `.env.example` eller lignende filer.**
2. **Opprett en `.env`-fil og fyll inn nødvendige verdier.**
3. **Last inn terminalen eller IDE-en på nytt etter å ha satt miljøvariabler.**

---

## Kjøre Notebooks

### 6. Notebook Vil Ikke Åpne eller Kjøre

**Bakgrunn:** Jupyter-notebooks krever riktig oppsett.

**Symptomer:**
- Notebook starter ikke
- Nettleser åpner seg ikke automatisk

**Mulige Årsaker:**
- Jupyter ikke installert
- Problemer med nettleserkonfigurasjon

**Løsninger:**
1. **Installer Jupyter (se Installasjonsproblemer ovenfor).**
2. **Åpne notebooks manuelt.**
   - Kopier URL-en fra terminalen (f.eks. `http://localhost:8888/?token=...`) og lim den inn i nettleseren din.

### 7. Kernel Krasjer eller Fryser

**Bakgrunn:** Notebook-kjerner kan krasje på grunn av ressursbegrensninger eller kodefeil.

**Symptomer:**
- Kernel dør eller starter på nytt gjentatte ganger
- Feil om manglende minne

**Mulige Årsaker:**
- Store datasett
- Inkompatibel kode eller pakker

**Løsninger:**
1. **Start kernel på nytt.**  
   Bruk "Restart Kernel"-knappen i Jupyter.
2. **Sjekk minnebruk.**  
   Lukk ubrukte applikasjoner.
3. **Kjør notebooks på skyplattformer.**  
   Bruk [Google Colab](https://colab.research.google.com/) eller [Azure Notebooks](https://notebooks.azure.com/).

---

## Ytelsesproblemer

### 8. Notebooks Kjører Sakte

**Bakgrunn:** Noen AI-oppgaver krever betydelig minne og CPU.

**Symptomer:**
- Langsom utførelse
- Laptop-vifte går høyt

**Mulige Årsaker:**
- Store datasett eller modeller
- Begrensede systemressurser

**Løsninger:**
1. **Bruk en skyplattform.**
   - Last opp notebook til Colab eller Azure Notebooks.
2. **Reduser datasettstørrelse.**
   - Bruk eksempeldata for øving.
3. **Lukk unødvendige programmer.**
   - Frigjør system-RAM.

---

## Problemer med Læreboknettstedet

### 9. Kapittel Laster Ikke

**Bakgrunn:** Den nettbaserte læreboken viser leksjoner og kapitler.

**Symptomer:**
- Et kapittel (f.eks. Transformers/BERT) mangler eller åpnes ikke

**Kjent Problem:**  
- [Problem #303](https://github.com/microsoft/AI-For-Beginners/issues/303): “18 Transformers. BERT. kan ikke åpnes på læreboknettstedet.” Forårsaket av en filnavnsfeil (`READMEtransformers.md` i stedet for `README.md`).

**Løsninger:**
1. **Sjekk etter feil i filnavn.**  
   Hvis du er en bidragsyter, sørg for at kapittelfiler heter `README.md`.
2. **Rapporter manglende filer.**  
   Åpne en GitHub-issue med kapittelnavn og feildetaljer.

---

## Bidragsproblemer

### 10. PR Ikke Akseptert eller Bygg Feiler

**Bakgrunn:** Bidrag må bestå tester og følge retningslinjer.

**Symptomer:**
- Pull request avvist
- CI/CD-pipeline-feil

**Mulige Årsaker:**
- Feilende tester
- Ikke fulgt kodestandarder

**Løsninger:**
1. **Les retningslinjene for bidrag.**
   - Følg repositoryets [CONTRIBUTING.md](https://github.com/microsoft/AI-For-Beginners/blob/main/CONTRIBUTING.md).
2. **Kjør tester lokalt før du pusher.**
3. **Sjekk regler for linting eller formatering.**

---

## FAQ

### Hvor kan jeg finne hjelp for spesifikke moduler?
- Hver modul har vanligvis sin egen README. Start der for oppsett og brukstips.

### Hvordan rapporterer jeg en feil eller ber om en funksjon?
- [Åpne en GitHub Issue](https://github.com/microsoft/AI-For-Beginners/issues/new) med en klar beskrivelse og trinn for å gjenskape problemet.

### Kan jeg be om hjelp hvis problemet mitt ikke er oppført?
- Ja! Søk etter eksisterende issues først, og hvis du ikke finner problemet ditt, opprett en ny issue.

---

## Få Hjelp

- **Sjekk Issues:** [GitHub Issues](https://github.com/microsoft/AI-For-Beginners/issues)
- **Still Spørsmål:** Bruk GitHub Discussions eller åpne en issue.
- **Community:** Se repository-lenker for chat-/forumalternativer.

---

_Sist Oppdatert: 2025-09-20_

---

**Ansvarsfraskrivelse**:  
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi streber etter nøyaktighet, vær oppmerksom på at automatiserte oversettelser kan inneholde feil eller unøyaktigheter. Det originale dokumentet på sitt opprinnelige språk bør anses som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.