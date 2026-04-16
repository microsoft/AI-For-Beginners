# AI-For-Beginners Trikčių Šalinimo Vadovas

Šis vadovas padės išspręsti dažniausiai pasitaikančias problemas, susijusias su [AI-For-Beginners](https://github.com/microsoft/AI-For-Beginners) saugyklos naudojimu ar prisidėjimu prie jos. Kiekviena problema apima kontekstą, simptomus, paaiškinimus ir žingsnis po žingsnio sprendimus.

---

## Turinys

- [Bendros problemos](../..)
- [Diegimo problemos](../..)
- [Konfigūracijos problemos](../..)
- [Užrašų knygelių paleidimas](../..)
- [Našumo problemos](../..)
- [Vadovėlio svetainės problemos](../..)
- [Prisidėjimo problemos](../..)
- [DUK](../..)
- [Pagalbos gavimas](../..)

---

## Bendros problemos

### 1. Saugykla netinkamai klonuojama

**Kontekstas:** Klonavimas leidžia nukopijuoti saugyklą į jūsų kompiuterį.

**Simptomai:**
- Klaida: `fatal: repository not found`
- Klaida: `Permission denied (publickey)`

**Galimos priežastys:**
- Neteisingas saugyklos URL
- Nepakankamos teisės
- SSH raktai nėra sukonfigūruoti

**Sprendimai:**
1. **Patikrinkite saugyklos URL.**  
   Naudokite HTTPS URL:  
   ```
   git clone https://github.com/microsoft/AI-For-Beginners.git
   ```
2. **Pereikite prie HTTPS, jei SSH neveikia.**  
   Jei matote `Permission denied (publickey)`, vietoj SSH naudokite aukščiau pateiktą HTTPS nuorodą.
3. **Konfigūruokite SSH raktus (pasirinktinai).**  
   Jei norite naudoti SSH, sekite [GitHub SSH vadovą](https://docs.github.com/en/authentication/connecting-to-github-with-ssh).

---

## Diegimo problemos

### 2. Python aplinkos problemos

**Kontekstas:** Saugykla naudoja Python ir įvairias bibliotekas.

**Simptomai:**
- Klaida: `ModuleNotFoundError: No module named '<package>'`
- Importavimo klaidos paleidžiant skriptus ar užrašų knygeles

**Galimos priežastys:**
- Neįdiegtos priklausomybės
- Netinkama Python versija

**Sprendimai:**
1. **Sukurkite virtualią aplinką.**  
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```
2. **Įdiekite priklausomybes.**  
   ```bash
   pip install -r requirements.txt
   ```
3. **Patikrinkite Python versiją.**  
   Naudokite Python 3.7 ar naujesnę.  
   ```bash
   python --version
   ```

### 3. Jupyter neįdiegtas

**Kontekstas:** Užrašų knygelės yra pagrindinė mokymosi priemonė.

**Simptomai:**
- Klaida: `jupyter: command not found`
- Užrašų knygelės nepasileidžia

**Galimos priežastys:**
- Jupyter nėra įdiegtas

**Sprendimai:**
1. **Įdiekite Jupyter Notebook.**  
   ```bash
   pip install notebook
   ```
   arba, jei naudojate Anaconda:
   ```bash
   conda install notebook
   ```
2. **Paleiskite Jupyter Notebook.**  
   ```bash
   jupyter notebook
   ```

### 4. Priklausomybių versijų konfliktai

**Kontekstas:** Projektai gali neveikti, jei paketų versijos nesuderinamos.

**Simptomai:**
- Klaidos ar įspėjimai apie nesuderinamas versijas

**Galimos priežastys:**
- Senos ar konfliktuojančios Python bibliotekos

**Sprendimai:**
1. **Įdiekite švarioje aplinkoje.**  
   Ištrinkite seną venv/conda aplinką ir sukurkite naują.
2. **Naudokite tikslias versijas.**  
   Visada paleiskite:
   ```bash
   pip install -r requirements.txt
   ```
   Jei tai nepavyksta, rankiniu būdu įdiekite trūkstamus paketus, kaip aprašyta README.

---

## Konfigūracijos problemos

### 5. Aplinkos kintamieji nenustatyti

**Kontekstas:** Kai kurie moduliai gali reikalauti raktų, žetonų ar konfigūracijos nustatymų.

**Simptomai:**
- Klaida: `KeyError` arba įspėjimai apie trūkstamą konfigūraciją

**Galimos priežastys:**
- Reikalingi aplinkos kintamieji nenustatyti

**Sprendimai:**
1. **Patikrinkite `.env.example` ar panašius failus.**
2. **Sukurkite `.env` failą ir užpildykite reikalingas reikšmes.**
3. **Iš naujo paleiskite terminalą ar IDE po aplinkos kintamųjų nustatymo.**

---

## Užrašų knygelių paleidimas

### 6. Užrašų knygelė neatsidaro arba neveikia

**Kontekstas:** Jupyter užrašų knygelėms reikia tinkamos konfigūracijos.

**Simptomai:**
- Užrašų knygelė nepasileidžia
- Naršyklė automatiškai neatsidaro

**Galimos priežastys:**
- Jupyter nėra įdiegtas
- Naršyklės konfigūracijos problemos

**Sprendimai:**
1. **Įdiekite Jupyter (žr. Diegimo problemas aukščiau).**
2. **Atidarykite užrašų knygeles rankiniu būdu.**
   - Nukopijuokite URL iš terminalo (pvz., `http://localhost:8888/?token=...`) ir įklijuokite jį į naršyklę.

### 7. Branduolys stringa arba užšąla

**Kontekstas:** Užrašų knygelių branduoliai gali strigti dėl resursų apribojimų ar kodo klaidų.

**Simptomai:**
- Branduolys nuolat miršta arba persikrauna
- Atminties trūkumo klaidos

**Galimos priežastys:**
- Dideli duomenų rinkiniai
- Nesuderinamas kodas ar paketai

**Sprendimai:**
1. **Iš naujo paleiskite branduolį.**  
   Naudokite "Restart Kernel" mygtuką Jupyter.
2. **Patikrinkite atminties naudojimą.**  
   Uždarykite nenaudojamas programas.
3. **Paleiskite užrašų knygeles debesų platformose.**  
   Naudokite [Google Colab](https://colab.research.google.com/) arba [Azure Notebooks](https://notebooks.azure.com/).

---

## Našumo problemos

### 8. Užrašų knygelės veikia lėtai

**Kontekstas:** Kai kurios AI užduotys reikalauja daug atminties ir procesoriaus.

**Simptomai:**
- Lėtas vykdymas
- Kompiuterio ventiliatorius garsiai veikia

**Galimos priežastys:**
- Dideli duomenų rinkiniai ar modeliai
- Riboti sistemos resursai

**Sprendimai:**
1. **Naudokite debesų platformą.**
   - Įkelkite užrašų knygelę į Colab arba Azure Notebooks.
2. **Sumažinkite duomenų rinkinio dydį.**
   - Praktikai naudokite pavyzdinius duomenis.
3. **Uždarykite nereikalingas programas.**
   - Atlaisvinkite sistemos RAM.

---

## Vadovėlio svetainės problemos

### 9. Skyrius neatsidaro

**Kontekstas:** Internetinis vadovėlis rodo pamokas ir skyrius.

**Simptomai:**
- Skyrius (pvz., Transformers/BERT) trūksta arba neatsidaro

**Žinoma problema:**  
- [Problema #303](https://github.com/microsoft/AI-For-Beginners/issues/303): „18 Transformers. BERT. negalima atidaryti vadovėlio svetainėje.“ Sukelta failo pavadinimo klaidos (`READMEtransformers.md` vietoj `README.md`).

**Sprendimai:**
1. **Patikrinkite failų pervadinimo klaidas.**  
   Jei esate prisidėjęs, įsitikinkite, kad skyrių failai pavadinti `README.md`.
2. **Praneškite apie trūkstamus failus.**  
   Atidarykite GitHub problemą su skyriaus pavadinimu ir klaidos detalėmis.

---

## Prisidėjimo problemos

### 10. PR nepriimtas arba statymai nepavyksta

**Kontekstas:** Prisidėjimai turi praeiti testus ir atitikti gaires.

**Simptomai:**
- Pull request atmestas
- CI/CD pipeline klaidos

**Galimos priežastys:**
- Nepavykę testai
- Neatitikimas kodavimo standartams

**Sprendimai:**
1. **Perskaitykite prisidėjimo gaires.**
   - Sekite saugyklos [CONTRIBUTING.md](https://github.com/microsoft/AI-For-Beginners/blob/main/CONTRIBUTING.md).
2. **Paleiskite testus lokaliai prieš įkeldami.**
3. **Patikrinkite linting taisykles ar formatavimo reikalavimus.**

---

## DUK

### Kur galiu rasti pagalbą dėl konkrečių modulių?
- Kiekvienas modulis paprastai turi savo README. Pradėkite nuo ten, kad sužinotumėte nustatymo ir naudojimo patarimus.

### Kaip pranešti apie klaidą ar paprašyti funkcijos?
- [Atidarykite GitHub problemą](https://github.com/microsoft/AI-For-Beginners/issues/new) su aiškiu aprašymu ir žingsniais, kaip atkurti.

### Ar galiu paprašyti pagalbos, jei mano problema nėra išvardyta?
- Taip! Pirmiausia ieškokite esamų problemų, o jei nerandate savo problemos, sukurkite naują problemą.

---

## Pagalbos gavimas

- **Patikrinkite problemas:** [GitHub Issues](https://github.com/microsoft/AI-For-Beginners/issues)
- **Užduokite klausimus:** Naudokite GitHub Discussions arba atidarykite problemą.
- **Bendruomenė:** Žiūrėkite saugyklos nuorodas į pokalbių/forumo parinktis.

---

_Paskutinį kartą atnaujinta: 2025-09-20_

---

**Atsakomybės atsisakymas**:  
Šis dokumentas buvo išverstas naudojant AI vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors stengiamės užtikrinti tikslumą, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba turėtų būti laikomas autoritetingu šaltiniu. Kritinei informacijai rekomenduojama naudoti profesionalų žmogaus vertimą. Mes neprisiimame atsakomybės už nesusipratimus ar neteisingus aiškinimus, atsiradusius dėl šio vertimo naudojimo.