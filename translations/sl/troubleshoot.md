# Vodnik za odpravljanje težav pri AI-For-Beginners

Ta vodnik vam pomaga rešiti pogoste težave, ki se pojavijo pri uporabi ali prispevanju v repozitorij [AI-For-Beginners](https://github.com/microsoft/AI-For-Beginners). Vsaka težava vključuje ozadje, simptome, razlage in korake za rešitev.

---

## Kazalo vsebine

- [Splošne težave](../..)
- [Težave pri namestitvi](../..)
- [Težave pri konfiguraciji](../..)
- [Zagon beležk](../..)
- [Težave z zmogljivostjo](../..)
- [Težave s spletno stranjo učbenika](../..)
- [Težave pri prispevanju](../..)
- [Pogosta vprašanja](../..)
- [Pomoč](../..)

---

## Splošne težave

### 1. Repozitorija ni mogoče klonirati

**Ozadje:** Kloniranje omogoča kopiranje repozitorija na vaš računalnik.

**Simptomi:**
- Napaka: `fatal: repository not found`
- Napaka: `Permission denied (publickey)`

**Možni vzroki:**
- Napačen URL repozitorija
- Nezadostna dovoljenja
- SSH ključi niso konfigurirani

**Rešitve:**
1. **Preverite URL repozitorija.**  
   Uporabite HTTPS URL:  
   ```
   git clone https://github.com/microsoft/AI-For-Beginners.git
   ```
2. **Preklopite na HTTPS, če SSH ne deluje.**  
   Če vidite `Permission denied (publickey)`, uporabite zgornji HTTPS povezavo namesto SSH.
3. **Konfigurirajte SSH ključe (neobvezno).**  
   Če želite uporabljati SSH, sledite [GitHubovemu vodniku za SSH](https://docs.github.com/en/authentication/connecting-to-github-with-ssh).

---

## Težave pri namestitvi

### 2. Težave s Python okoljem

**Ozadje:** Repozitorij temelji na Pythonu in različnih knjižnicah.

**Simptomi:**
- Napaka: `ModuleNotFoundError: No module named '<package>'`
- Napake pri uvozu ob zagonu skriptov ali beležk

**Možni vzroki:**
- Odvisnosti niso nameščene
- Napačna različica Pythona

**Rešitve:**
1. **Nastavite virtualno okolje.**  
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```
2. **Namestite odvisnosti.**  
   ```bash
   pip install -r requirements.txt
   ```
3. **Preverite različico Pythona.**  
   Uporabite Python 3.7 ali novejši.  
   ```bash
   python --version
   ```

### 3. Jupyter ni nameščen

**Ozadje:** Beležke so ključni učni vir.

**Simptomi:**
- Napaka: `jupyter: command not found`
- Beležke se ne zaženejo

**Možni vzroki:**
- Jupyter ni nameščen

**Rešitve:**
1. **Namestite Jupyter Notebook.**  
   ```bash
   pip install notebook
   ```
   ali, če uporabljate Anaconda:
   ```bash
   conda install notebook
   ```
2. **Zaženite Jupyter Notebook.**  
   ```bash
   jupyter notebook
   ```

### 4. Konflikti med različicami odvisnosti

**Ozadje:** Projekti lahko prenehajo delovati, če se različice paketov ne ujemajo.

**Simptomi:**
- Napake ali opozorila o nezdružljivih različicah

**Možni vzroki:**
- Stari ali konfliktni Python paketi

**Rešitve:**
1. **Namestite v čisto okolje.**  
   Izbrišite staro venv/conda okolje in ustvarite novo.
2. **Uporabite točne različice.**  
   Vedno zaženite:
   ```bash
   pip install -r requirements.txt
   ```
   Če to ne uspe, ročno namestite manjkajoče pakete, kot je opisano v README.

---

## Težave pri konfiguraciji

### 5. Okoljske spremenljivke niso nastavljene

**Ozadje:** Nekateri moduli lahko zahtevajo ključe, žetone ali nastavitve konfiguracije.

**Simptomi:**
- Napaka: `KeyError` ali opozorila o manjkajoči konfiguraciji

**Možni vzroki:**
- Zahtevane okoljske spremenljivke niso nastavljene

**Rešitve:**
1. **Preverite `.env.example` ali podobne datoteke.**
2. **Ustvarite `.env` datoteko in izpolnite zahtevane vrednosti.**
3. **Ponovno naložite terminal ali IDE po nastavitvi okoljskih spremenljivk.**

---

## Zagon beležk

### 6. Beležka se ne odpre ali ne zažene

**Ozadje:** Jupyter beležke zahtevajo ustrezno nastavitev.

**Simptomi:**
- Beležka se ne zažene
- Brskalnik se ne odpre samodejno

**Možni vzroki:**
- Jupyter ni nameščen
- Težave s konfiguracijo brskalnika

**Rešitve:**
1. **Namestite Jupyter (glejte Težave pri namestitvi zgoraj).**
2. **Ročno odprite beležke.**
   - Kopirajte URL iz terminala (npr. `http://localhost:8888/?token=...`) in ga prilepite v brskalnik.

### 7. Jedro beležke se sesuje ali zamrzne

**Ozadje:** Jedra beležk se lahko sesujejo zaradi omejitev virov ali napak v kodi.

**Simptomi:**
- Jedro se večkrat sesuje ali znova zažene
- Napake zaradi pomanjkanja pomnilnika

**Možni vzroki:**
- Veliki podatkovni nizi
- Nezdružljiva koda ali paketi

**Rešitve:**
1. **Znova zaženite jedro.**  
   Uporabite gumb "Restart Kernel" v Jupyterju.
2. **Preverite uporabo pomnilnika.**  
   Zaprite neuporabljene aplikacije.
3. **Zaženite beležke na oblačnih platformah.**  
   Uporabite [Google Colab](https://colab.research.google.com/) ali [Azure Notebooks](https://notebooks.azure.com/).

---

## Težave z zmogljivostjo

### 8. Beležke delujejo počasi

**Ozadje:** Nekatere naloge AI zahtevajo veliko pomnilnika in procesorske moči.

**Simptomi:**
- Počasno izvajanje
- Glasno delovanje ventilatorja prenosnika

**Možni vzroki:**
- Veliki podatkovni nizi ali modeli
- Omejeni sistemski viri

**Rešitve:**
1. **Uporabite oblačno platformo.**
   - Naložite beležko na Colab ali Azure Notebooks.
2. **Zmanjšajte velikost podatkovnega niza.**
   - Uporabite vzorčne podatke za vajo.
3. **Zaprite nepotrebne programe.**
   - Sprostite sistemski RAM.

---

## Težave s spletno stranjo učbenika

### 9. Poglavje se ne naloži

**Ozadje:** Spletni učbenik prikazuje lekcije in poglavja.

**Simptomi:**
- Poglavje (npr. Transformers/BERT) manjka ali se ne odpre

**Znana težava:**  
- [Težava #303](https://github.com/microsoft/AI-For-Beginners/issues/303): “18 Transformers. BERT. ne morem odpreti na spletni strani učbenika.” Povzročeno zaradi napake v imenu datoteke (`READMEtransformers.md` namesto `README.md`).

**Rešitve:**
1. **Preverite napake pri preimenovanju datotek.**  
   Če ste prispevalec, poskrbite, da so datoteke poglavij poimenovane `README.md`.
2. **Prijavite manjkajoče datoteke.**  
   Odprite GitHub težavo z imenom poglavja in podrobnostmi o napaki.

---

## Težave pri prispevanju

### 10. PR ni sprejet ali gradnje ne uspejo

**Ozadje:** Prispevki morajo prestati teste in slediti smernicam.

**Simptomi:**
- Zahteva za združitev zavrnjena
- Napake v CI/CD procesu

**Možni vzroki:**
- Neuspešni testi
- Neupoštevanje kodnih standardov

**Rešitve:**
1. **Preberite smernice za prispevanje.**
   - Sledite [CONTRIBUTING.md](https://github.com/microsoft/AI-For-Beginners/blob/main/CONTRIBUTING.md) repozitorija.
2. **Zaženite teste lokalno pred potiskanjem.**
3. **Preverite pravila za oblikovanje kode ali zahteve za formatiranje.**

---

## Pogosta vprašanja

### Kje lahko najdem pomoč za določene module?
- Vsak modul običajno vsebuje svoj README. Začnite tam za nasvete o nastavitvi in uporabi.

### Kako prijavim napako ali zahtevam funkcijo?
- [Odprite GitHub težavo](https://github.com/microsoft/AI-For-Beginners/issues/new) z jasnim opisom in koraki za reprodukcijo.

### Ali lahko prosim za pomoč, če moj problem ni naveden?
- Seveda! Najprej poiščite obstoječe težave, in če ne najdete svojega problema, ustvarite novo težavo.

---

## Pomoč

- **Preverite težave:** [GitHub Issues](https://github.com/microsoft/AI-For-Beginners/issues)
- **Postavite vprašanja:** Uporabite GitHub Discussions ali odprite težavo.
- **Skupnost:** Oglejte si povezave repozitorija za klepet/forum možnosti.

---

_Zadnja posodobitev: 2025-09-20_

---

**Omejitev odgovornosti**:  
Ta dokument je bil preveden z uporabo storitve AI za prevajanje [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas prosimo, da upoštevate, da lahko avtomatizirani prevodi vsebujejo napake ali netočnosti. Izvirni dokument v njegovem maternem jeziku je treba obravnavati kot avtoritativni vir. Za ključne informacije priporočamo profesionalni človeški prevod. Ne prevzemamo odgovornosti za morebitna nesporazumevanja ali napačne razlage, ki izhajajo iz uporabe tega prevoda.