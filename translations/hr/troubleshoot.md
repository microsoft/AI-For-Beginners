# AI-For-Beginners Vodič za rješavanje problema

Ovaj vodič pomaže u rješavanju uobičajenih problema koji se javljaju prilikom korištenja ili doprinosa [AI-For-Beginners](https://github.com/microsoft/AI-For-Beginners) repozitoriju. Svaki problem uključuje pozadinu, simptome, objašnjenja i korak-po-korak rješenja.

---

## Sadržaj

- [Opći problemi](../..)
- [Problemi s instalacijom](../..)
- [Problemi s konfiguracijom](../..)
- [Pokretanje bilježnica](../..)
- [Problemi s performansama](../..)
- [Problemi s web-stranicom udžbenika](../..)
- [Problemi s doprinosima](../..)
- [Česta pitanja](../..)
- [Dobivanje pomoći](../..)

---

## Opći problemi

### 1. Repozitorij se ne klonira ispravno

**Pozadina:** Kloniranje omogućuje kopiranje repozitorija na vaše računalo.

**Simptomi:**
- Pogreška: `fatal: repository not found`
- Pogreška: `Permission denied (publickey)`

**Mogući uzroci:**
- Neispravan URL repozitorija
- Nedovoljne dozvole
- SSH ključevi nisu konfigurirani

**Rješenja:**
1. **Provjerite URL repozitorija.**  
   Koristite HTTPS URL:  
   ```
   git clone https://github.com/microsoft/AI-For-Beginners.git
   ```
2. **Prebacite se na HTTPS ako SSH ne radi.**  
   Ako vidite `Permission denied (publickey)`, koristite HTTPS link umjesto SSH-a.
3. **Konfigurirajte SSH ključeve (opcionalno).**  
   Ako želite koristiti SSH, slijedite [GitHubov vodič za SSH](https://docs.github.com/en/authentication/connecting-to-github-with-ssh).

---

## Problemi s instalacijom

### 2. Problemi s Python okruženjem

**Pozadina:** Repozitorij se oslanja na Python i razne biblioteke.

**Simptomi:**
- Pogreška: `ModuleNotFoundError: No module named '<package>'`
- Pogreške pri uvozu prilikom pokretanja skripti ili bilježnica

**Mogući uzroci:**
- Ovisnosti nisu instalirane
- Pogrešna verzija Pythona

**Rješenja:**
1. **Postavite virtualno okruženje.**  
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```
2. **Instalirajte ovisnosti.**  
   ```bash
   pip install -r requirements.txt
   ```
3. **Provjerite verziju Pythona.**  
   Koristite Python 3.7 ili noviji.  
   ```bash
   python --version
   ```

### 3. Jupyter nije instaliran

**Pozadina:** Bilježnice su ključni resurs za učenje.

**Simptomi:**
- Pogreška: `jupyter: command not found`
- Bilježnice se ne pokreću

**Mogući uzroci:**
- Jupyter nije instaliran

**Rješenja:**
1. **Instalirajte Jupyter Notebook.**  
   ```bash
   pip install notebook
   ```
   ili, ako koristite Anacondu:
   ```bash
   conda install notebook
   ```
2. **Pokrenite Jupyter Notebook.**  
   ```bash
   jupyter notebook
   ```

### 4. Sukobi verzija ovisnosti

**Pozadina:** Projekti mogu prestati raditi ako verzije paketa nisu usklađene.

**Simptomi:**
- Pogreške ili upozorenja o nekompatibilnim verzijama

**Mogući uzroci:**
- Stari ili sukobljeni Python paketi

**Rješenja:**
1. **Instalirajte u čistom okruženju.**  
   Obrišite staro venv/conda okruženje i kreirajte novo.
2. **Koristite točne verzije.**  
   Uvijek pokrenite:
   ```bash
   pip install -r requirements.txt
   ```
   Ako ovo ne uspije, ručno instalirajte nedostajuće pakete prema uputama u README datoteci.

---

## Problemi s konfiguracijom

### 5. Varijable okruženja nisu postavljene

**Pozadina:** Neki moduli mogu zahtijevati ključeve, tokene ili postavke konfiguracije.

**Simptomi:**
- Pogreška: `KeyError` ili upozorenja o nedostajućoj konfiguraciji

**Mogući uzroci:**
- Potrebne varijable okruženja nisu postavljene

**Rješenja:**
1. **Provjerite `.env.example` ili slične datoteke.**
2. **Kreirajte `.env` datoteku i popunite potrebne vrijednosti.**
3. **Ponovno učitajte terminal ili IDE nakon postavljanja varijabli okruženja.**

---

## Pokretanje bilježnica

### 6. Bilježnica se ne otvara ili ne pokreće

**Pozadina:** Jupyter bilježnice zahtijevaju pravilnu postavku.

**Simptomi:**
- Bilježnica se ne pokreće
- Preglednik se ne otvara automatski

**Mogući uzroci:**
- Jupyter nije instaliran
- Problemi s konfiguracijom preglednika

**Rješenja:**
1. **Instalirajte Jupyter (pogledajte Problemi s instalacijom gore).**
2. **Ručno otvorite bilježnice.**
   - Kopirajte URL iz terminala (npr., `http://localhost:8888/?token=...`) i zalijepite ga u preglednik.

### 7. Kernel se ruši ili zamrzava

**Pozadina:** Kernel bilježnice može se srušiti zbog ograničenja resursa ili grešaka u kodu.

**Simptomi:**
- Kernel se stalno gasi ili ponovno pokreće
- Pogreške zbog nedostatka memorije

**Mogući uzroci:**
- Veliki skupovi podataka
- Neodgovarajući kod ili paketi

**Rješenja:**
1. **Ponovno pokrenite kernel.**  
   Koristite gumb "Restart Kernel" u Jupyteru.
2. **Provjerite korištenje memorije.**  
   Zatvorite nepotrebne aplikacije.
3. **Pokrenite bilježnice na cloud platformama.**  
   Koristite [Google Colab](https://colab.research.google.com/) ili [Azure Notebooks](https://notebooks.azure.com/).

---

## Problemi s performansama

### 8. Bilježnice rade sporo

**Pozadina:** Neki AI zadaci zahtijevaju značajnu memoriju i CPU.

**Simptomi:**
- Sporo izvršavanje
- Ventilator na laptopu radi glasno

**Mogući uzroci:**
- Veliki skupovi podataka ili modeli
- Ograničeni resursi sustava

**Rješenja:**
1. **Koristite cloud platformu.**
   - Prenesite bilježnicu na Colab ili Azure Notebooks.
2. **Smanjite veličinu skupa podataka.**
   - Koristite uzorak podataka za vježbu.
3. **Zatvorite nepotrebne programe.**
   - Oslobodite RAM sustava.

---

## Problemi s web-stranicom udžbenika

### 9. Poglavlje se ne učitava

**Pozadina:** Online udžbenik prikazuje lekcije i poglavlja.

**Simptomi:**
- Poglavlje (npr., Transformers/BERT) nedostaje ili se ne otvara

**Poznati problem:**  
- [Problem #303](https://github.com/microsoft/AI-For-Beginners/issues/303): “18 Transformers. BERT. ne može se otvoriti na web-stranici udžbenika.” Uzrokovan greškom u nazivu datoteke (`READMEtransformers.md` umjesto `README.md`).

**Rješenja:**
1. **Provjerite greške u preimenovanju datoteka.**  
   Ako ste suradnik, osigurajte da su datoteke poglavlja nazvane `README.md`.
2. **Prijavite nedostajuće datoteke.**  
   Otvorite GitHub problem s nazivom poglavlja i detaljima o grešci.

---

## Problemi s doprinosima

### 10. PR nije prihvaćen ili gradnje ne uspijevaju

**Pozadina:** Doprinosi moraju proći testove i slijediti smjernice.

**Simptomi:**
- Pull request odbijen
- Pogreške u CI/CD procesu

**Mogući uzroci:**
- Testovi ne prolaze
- Nepoštivanje standarda kodiranja

**Rješenja:**
1. **Pročitajte smjernice za doprinos.**
   - Slijedite [CONTRIBUTING.md](https://github.com/microsoft/AI-For-Beginners/blob/main/CONTRIBUTING.md) repozitorija.
2. **Pokrenite testove lokalno prije slanja.**
3. **Provjerite pravila za formatiranje ili linting.**

---

## Česta pitanja

### Gdje mogu pronaći pomoć za određene module?
- Svaki modul obično ima svoj README. Počnite tamo za savjete o postavljanju i korištenju.

### Kako prijaviti grešku ili zatražiti značajku?
- [Otvorite GitHub problem](https://github.com/microsoft/AI-For-Beginners/issues/new) s jasnim opisom i koracima za reprodukciju.

### Mogu li zatražiti pomoć ako moj problem nije naveden?
- Da! Prvo pretražite postojeće probleme, a ako ne pronađete svoj problem, kreirajte novi.

---

## Dobivanje pomoći

- **Provjerite probleme:** [GitHub Issues](https://github.com/microsoft/AI-For-Beginners/issues)
- **Postavite pitanja:** Koristite GitHub Discussions ili otvorite problem.
- **Zajednica:** Pogledajte poveznice repozitorija za opcije chata/foruma.

---

_Zadnje ažurirano: 2025-09-20_

---

**Odricanje od odgovornosti**:  
Ovaj dokument je preveden pomoću AI usluge za prevođenje [Co-op Translator](https://github.com/Azure/co-op-translator). Iako nastojimo osigurati točnost, imajte na umu da automatski prijevodi mogu sadržavati pogreške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati autoritativnim izvorom. Za ključne informacije preporučuje se profesionalni prijevod od strane čovjeka. Ne preuzimamo odgovornost za nesporazume ili pogrešna tumačenja koja proizlaze iz korištenja ovog prijevoda.