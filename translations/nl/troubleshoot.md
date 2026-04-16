# AI-For-Beginners Probleemoplossingsgids

Deze gids helpt je bij het oplossen van veelvoorkomende problemen die je kunt tegenkomen bij het gebruik of bijdragen aan de [AI-For-Beginners](https://github.com/microsoft/AI-For-Beginners) repository. Elk probleem bevat achtergrondinformatie, symptomen, uitleg en stapsgewijze oplossingen.

---

## Inhoudsopgave

- [Algemene Problemen](../..)
- [Installatieproblemen](../..)
- [Configuratieproblemen](../..)
- [Notebooks Uitvoeren](../..)
- [Prestatieproblemen](../..)
- [Problemen met de Leerboekwebsite](../..)
- [Bijdrageproblemen](../..)
- [FAQ](../..)
- [Hulp Krijgen](../..)

---

## Algemene Problemen

### 1. Repository Wordt Niet Correct Gekloond

**Achtergrond:** Klonen stelt je in staat om de repository naar je eigen computer te kopiëren.

**Symptomen:**
- Foutmelding: `fatal: repository not found`
- Foutmelding: `Permission denied (publickey)`

**Mogelijke Oorzaken:**
- Onjuiste repository-URL
- Onvoldoende rechten
- SSH-sleutels niet geconfigureerd

**Oplossingen:**
1. **Controleer de repository-URL.**  
   Gebruik de HTTPS-URL:  
   ```
   git clone https://github.com/microsoft/AI-For-Beginners.git
   ```
2. **Schakel over naar HTTPS als SSH faalt.**  
   Als je `Permission denied (publickey)` ziet, gebruik dan de HTTPS-link hierboven in plaats van SSH.
3. **Configureer SSH-sleutels (optioneel).**  
   Als je SSH wilt gebruiken, volg dan [GitHub's SSH-gids](https://docs.github.com/en/authentication/connecting-to-github-with-ssh).

---

## Installatieproblemen

### 2. Problemen met de Python-omgeving

**Achtergrond:** De repository maakt gebruik van Python en verschillende bibliotheken.

**Symptomen:**
- Foutmelding: `ModuleNotFoundError: No module named '<package>'`
- Importfouten bij het uitvoeren van scripts of notebooks

**Mogelijke Oorzaken:**
- Afhankelijkheden niet geïnstalleerd
- Verkeerde Python-versie

**Oplossingen:**
1. **Maak een virtuele omgeving aan.**  
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```
2. **Installeer afhankelijkheden.**  
   ```bash
   pip install -r requirements.txt
   ```
3. **Controleer de Python-versie.**  
   Gebruik Python 3.7 of nieuwer.  
   ```bash
   python --version
   ```

### 3. Jupyter Niet Geïnstalleerd

**Achtergrond:** Notebooks zijn een belangrijk leermiddel.

**Symptomen:**
- Foutmelding: `jupyter: command not found`
- Notebooks starten niet

**Mogelijke Oorzaken:**
- Jupyter niet geïnstalleerd

**Oplossingen:**
1. **Installeer Jupyter Notebook.**  
   ```bash
   pip install notebook
   ```
   of, als je Anaconda gebruikt:
   ```bash
   conda install notebook
   ```
2. **Start Jupyter Notebook.**  
   ```bash
   jupyter notebook
   ```

### 4. Versieconflicten van Afhankelijkheden

**Achtergrond:** Projecten kunnen breken als pakketversies niet overeenkomen.

**Symptomen:**
- Fouten of waarschuwingen over incompatibele versies

**Mogelijke Oorzaken:**
- Oude of conflicterende Python-pakketten

**Oplossingen:**
1. **Installeer in een schone omgeving.**  
   Verwijder oude venv/conda-omgeving en maak een nieuwe aan.
2. **Gebruik exacte versies.**  
   Voer altijd uit:
   ```bash
   pip install -r requirements.txt
   ```
   Als dit faalt, installeer ontbrekende pakketten handmatig zoals beschreven in de README.

---

## Configuratieproblemen

### 5. Omgevingsvariabelen Niet Ingesteld

**Achtergrond:** Sommige modules vereisen sleutels, tokens of configuratie-instellingen.

**Symptomen:**
- Foutmelding: `KeyError` of waarschuwingen over ontbrekende configuratie

**Mogelijke Oorzaken:**
- Vereiste omgevingsvariabelen niet ingesteld

**Oplossingen:**
1. **Controleer op `.env.example` of soortgelijke bestanden.**
2. **Maak een `.env`-bestand en vul de vereiste waarden in.**
3. **Herlaad je terminal of IDE na het instellen van omgevingsvariabelen.**

---

## Notebooks Uitvoeren

### 6. Notebook Wil Niet Openen of Uitvoeren

**Achtergrond:** Jupyter-notebooks vereisen een correcte setup.

**Symptomen:**
- Notebook start niet
- Browser opent niet automatisch

**Mogelijke Oorzaken:**
- Jupyter niet geïnstalleerd
- Browserconfiguratieproblemen

**Oplossingen:**
1. **Installeer Jupyter (zie Installatieproblemen hierboven).**
2. **Open notebooks handmatig.**
   - Kopieer de URL uit de terminal (bijv. `http://localhost:8888/?token=...`) en plak deze in je browser.

### 7. Kernel Crasht of Vriest

**Achtergrond:** Notebook-kernels kunnen crashen door resourcebeperkingen of codefouten.

**Symptomen:**
- Kernel sterft of herstart herhaaldelijk
- Out-of-memory fouten

**Mogelijke Oorzaken:**
- Grote datasets
- Incompatibele code of pakketten

**Oplossingen:**
1. **Herstart de kernel.**  
   Gebruik de knop "Restart Kernel" in Jupyter.
2. **Controleer het geheugengebruik.**  
   Sluit ongebruikte applicaties.
3. **Voer notebooks uit op cloudplatforms.**  
   Gebruik [Google Colab](https://colab.research.google.com/) of [Azure Notebooks](https://notebooks.azure.com/).

---

## Prestatieproblemen

### 8. Notebooks Werken Traag

**Achtergrond:** Sommige AI-taken vereisen veel geheugen en CPU.

**Symptomen:**
- Trage uitvoering
- Laptopventilator draait luid

**Mogelijke Oorzaken:**
- Grote datasets of modellen
- Beperkte systeembronnen

**Oplossingen:**
1. **Gebruik een cloudplatform.**
   - Upload de notebook naar Colab of Azure Notebooks.
2. **Verminder de datasetgrootte.**
   - Gebruik voorbeelddata voor oefening.
3. **Sluit onnodige programma's.**
   - Maak systeem-RAM vrij.

---

## Problemen met de Leerboekwebsite

### 9. Hoofdstuk Laadt Niet

**Achtergrond:** Het online leerboek toont lessen en hoofdstukken.

**Symptomen:**
- Een hoofdstuk (bijv. Transformers/BERT) ontbreekt of opent niet

**Bekend Probleem:**  
- [Issue #303](https://github.com/microsoft/AI-For-Beginners/issues/303): “18 Transformers. BERT. kan niet worden geopend op de leerboekwebsite.” Veroorzaakt door een bestandsnaamfout (`READMEtransformers.md` in plaats van `README.md`).

**Oplossingen:**
1. **Controleer op fouten bij het hernoemen van bestanden.**  
   Als je een bijdrager bent, zorg ervoor dat hoofdstukbestanden `README.md` heten.
2. **Rapporteer ontbrekende bestanden.**  
   Open een GitHub-issue met de naam van het hoofdstuk en foutdetails.

---

## Bijdrageproblemen

### 10. PR Wordt Niet Geaccepteerd of Builds Falen

**Achtergrond:** Bijdragen moeten tests doorstaan en richtlijnen volgen.

**Symptomen:**
- Pull request afgewezen
- CI/CD-pijplijnfouten

**Mogelijke Oorzaken:**
- Falen van tests
- Niet voldoen aan coderingsstandaarden

**Oplossingen:**
1. **Lees de richtlijnen voor bijdragen.**
   - Volg de [CONTRIBUTING.md](https://github.com/microsoft/AI-For-Beginners/blob/main/CONTRIBUTING.md) van de repository.
2. **Voer tests lokaal uit voordat je pusht.**
3. **Controleer op lintingregels of formatteringsvereisten.**

---

## FAQ

### Waar kan ik hulp vinden voor specifieke modules?
- Elke module heeft meestal een eigen README. Begin daar voor installatie- en gebruikstips.

### Hoe meld ik een bug of vraag ik een functie aan?
- [Open een GitHub Issue](https://github.com/microsoft/AI-For-Beginners/issues/new) met een duidelijke beschrijving en stappen om het probleem te reproduceren.

### Kan ik om hulp vragen als mijn probleem niet wordt vermeld?
- Ja! Zoek eerst naar bestaande issues, en als je je probleem niet vindt, maak een nieuw issue aan.

---

## Hulp Krijgen

- **Controleer Issues:** [GitHub Issues](https://github.com/microsoft/AI-For-Beginners/issues)
- **Stel Vragen:** Gebruik GitHub Discussions of open een issue.
- **Community:** Zie de repository-links voor chat-/forumopties.

---

_Laatst bijgewerkt: 2025-09-20_

---

**Disclaimer**:  
Dit document is vertaald met behulp van de AI-vertalingsservice [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we streven naar nauwkeurigheid, dient u zich ervan bewust te zijn dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het originele document in de oorspronkelijke taal moet worden beschouwd als de gezaghebbende bron. Voor cruciale informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.