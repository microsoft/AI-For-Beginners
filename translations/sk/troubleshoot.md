# AI-For-Beginners Príručka na riešenie problémov

Táto príručka vám pomôže vyriešiť bežné problémy, ktoré sa môžu vyskytnúť pri používaní alebo prispievaní do [AI-For-Beginners](https://github.com/microsoft/AI-For-Beginners) repozitára. Každý problém obsahuje pozadie, príznaky, vysvetlenia a postupné riešenia.

---

## Obsah

- [Všeobecné problémy](../..)
- [Problémy s inštaláciou](../..)
- [Problémy s konfiguráciou](../..)
- [Spúšťanie notebookov](../..)
- [Problémy s výkonom](../..)
- [Problémy s webovou stránkou učebnice](../..)
- [Problémy s prispievaním](../..)
- [FAQ](../..)
- [Získanie pomoci](../..)

---

## Všeobecné problémy

### 1. Repozitár sa nedá správne naklonovať

**Pozadie:** Klonovanie vám umožňuje skopírovať repozitár na váš počítač.

**Príznaky:**
- Chyba: `fatal: repository not found`
- Chyba: `Permission denied (publickey)`

**Možné príčiny:**
- Nesprávna URL adresa repozitára
- Nedostatočné oprávnenia
- SSH kľúče nie sú nakonfigurované

**Riešenia:**
1. **Skontrolujte URL adresu repozitára.**  
   Použite HTTPS URL:  
   ```
   git clone https://github.com/microsoft/AI-For-Beginners.git
   ```
2. **Prepnite na HTTPS, ak SSH zlyhá.**  
   Ak vidíte `Permission denied (publickey)`, použite namiesto SSH vyššie uvedený HTTPS odkaz.
3. **Nakonfigurujte SSH kľúče (voliteľné).**  
   Ak chcete používať SSH, postupujte podľa [GitHub SSH príručky](https://docs.github.com/en/authentication/connecting-to-github-with-ssh).

---

## Problémy s inštaláciou

### 2. Problémy s Python prostredím

**Pozadie:** Repozitár je závislý na Pythone a rôznych knižniciach.

**Príznaky:**
- Chyba: `ModuleNotFoundError: No module named '<package>'`
- Chyby pri importe pri spúšťaní skriptov alebo notebookov

**Možné príčiny:**
- Závislosti nie sú nainštalované
- Nesprávna verzia Pythonu

**Riešenia:**
1. **Nastavte virtuálne prostredie.**  
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```
2. **Nainštalujte závislosti.**  
   ```bash
   pip install -r requirements.txt
   ```
3. **Skontrolujte verziu Pythonu.**  
   Použite Python 3.7 alebo novší.  
   ```bash
   python --version
   ```

### 3. Jupyter nie je nainštalovaný

**Pozadie:** Notebooky sú kľúčovým zdrojom učenia.

**Príznaky:**
- Chyba: `jupyter: command not found`
- Notebooky sa nedajú spustiť

**Možné príčiny:**
- Jupyter nie je nainštalovaný

**Riešenia:**
1. **Nainštalujte Jupyter Notebook.**  
   ```bash
   pip install notebook
   ```
   alebo, ak používate Anacondu:
   ```bash
   conda install notebook
   ```
2. **Spustite Jupyter Notebook.**  
   ```bash
   jupyter notebook
   ```

### 4. Konflikty verzií závislostí

**Pozadie:** Projekty môžu zlyhať, ak sú verzie balíkov nekompatibilné.

**Príznaky:**
- Chyby alebo varovania o nekompatibilných verziách

**Možné príčiny:**
- Staré alebo konfliktné Python balíky

**Riešenia:**
1. **Inštalujte v čistom prostredí.**  
   Odstráňte staré venv/conda prostredie a vytvorte nové.
2. **Používajte presné verzie.**  
   Vždy spustite:
   ```bash
   pip install -r requirements.txt
   ```
   Ak to zlyhá, manuálne nainštalujte chýbajúce balíky podľa README.

---

## Problémy s konfiguráciou

### 5. Environmentálne premenné nie sú nastavené

**Pozadie:** Niektoré moduly môžu vyžadovať kľúče, tokeny alebo konfiguračné nastavenia.

**Príznaky:**
- Chyba: `KeyError` alebo varovania o chýbajúcej konfigurácii

**Možné príčiny:**
- Požadované environmentálne premenné nie sú nastavené

**Riešenia:**
1. **Skontrolujte `.env.example` alebo podobné súbory.**
2. **Vytvorte `.env` súbor a vyplňte požadované hodnoty.**
3. **Znovu načítajte terminál alebo IDE po nastavení environmentálnych premenných.**

---

## Spúšťanie notebookov

### 6. Notebook sa nedá otvoriť alebo spustiť

**Pozadie:** Jupyter notebooky vyžadujú správne nastavenie.

**Príznaky:**
- Notebook sa nedá spustiť
- Prehliadač sa neotvára automaticky

**Možné príčiny:**
- Jupyter nie je nainštalovaný
- Problémy s konfiguráciou prehliadača

**Riešenia:**
1. **Nainštalujte Jupyter (pozrite Problémy s inštaláciou vyššie).**
2. **Otvorte notebooky manuálne.**
   - Skopírujte URL z terminálu (napr. `http://localhost:8888/?token=...`) a vložte ho do prehliadača.

### 7. Kernel padá alebo zamŕza

**Pozadie:** Kernel notebooku môže padnúť kvôli limitom zdrojov alebo chybám v kóde.

**Príznaky:**
- Kernel sa opakovane vypína alebo reštartuje
- Chyby nedostatku pamäte

**Možné príčiny:**
- Veľké datasety
- Nekompatibilný kód alebo balíky

**Riešenia:**
1. **Reštartujte kernel.**  
   Použite tlačidlo "Restart Kernel" v Jupyteri.
2. **Skontrolujte využitie pamäte.**  
   Zatvorte nepoužívané aplikácie.
3. **Spúšťajte notebooky na cloudových platformách.**  
   Použite [Google Colab](https://colab.research.google.com/) alebo [Azure Notebooks](https://notebooks.azure.com/).

---

## Problémy s výkonom

### 8. Notebooky bežia pomaly

**Pozadie:** Niektoré AI úlohy vyžadujú značnú pamäť a CPU.

**Príznaky:**
- Pomalé vykonávanie
- Hlučný ventilátor na notebooku

**Možné príčiny:**
- Veľké datasety alebo modely
- Obmedzené systémové zdroje

**Riešenia:**
1. **Použite cloudovú platformu.**
   - Nahrajte notebook na Colab alebo Azure Notebooks.
2. **Zmenšite veľkosť datasetu.**
   - Použite vzorové dáta na precvičovanie.
3. **Zatvorte nepotrebné programy.**
   - Uvoľnite systémovú RAM.

---

## Problémy s webovou stránkou učebnice

### 9. Kapitola sa nenačítava

**Pozadie:** Online učebnica zobrazuje lekcie a kapitoly.

**Príznaky:**
- Kapitola (napr. Transformers/BERT) chýba alebo sa nedá otvoriť

**Známý problém:**  
- [Problém #303](https://github.com/microsoft/AI-For-Beginners/issues/303): „18 Transformers. BERT. sa nedá otvoriť na webovej stránke učebnice.“ Spôsobené chybou názvu súboru (`READMEtransformers.md` namiesto `README.md`).

**Riešenia:**
1. **Skontrolujte chyby v názvoch súborov.**  
   Ak ste prispievateľ, uistite sa, že kapitoly sú pomenované `README.md`.
2. **Nahláste chýbajúce súbory.**  
   Otvorte GitHub issue s názvom kapitoly a podrobnosťami o chybe.

---

## Problémy s prispievaním

### 10. PR nie je prijatý alebo buildy zlyhávajú

**Pozadie:** Príspevky musia prejsť testami a dodržiavať pokyny.

**Príznaky:**
- Pull request zamietnutý
- Chyby v CI/CD pipeline

**Možné príčiny:**
- Zlyhávajúce testy
- Nedodržiavanie štandardov kódovania

**Riešenia:**
1. **Prečítajte si pokyny na prispievanie.**
   - Dodržiavajte [CONTRIBUTING.md](https://github.com/microsoft/AI-For-Beginners/blob/main/CONTRIBUTING.md) repozitára.
2. **Spustite testy lokálne pred odoslaním.**
3. **Skontrolujte pravidlá lintingu alebo požiadavky na formátovanie.**

---

## FAQ

### Kde nájdem pomoc pre konkrétne moduly?
- Každý modul má zvyčajne vlastný README. Začnite tam pre tipy na nastavenie a používanie.

### Ako nahlásim chybu alebo požiadam o funkciu?
- [Otvorte GitHub Issue](https://github.com/microsoft/AI-For-Beginners/issues/new) s jasným popisom a krokmi na reprodukciu.

### Môžem požiadať o pomoc, ak môj problém nie je uvedený?
- Áno! Najskôr vyhľadajte existujúce issues, a ak svoj problém nenájdete, vytvorte nový issue.

---

## Získanie pomoci

- **Skontrolujte Issues:** [GitHub Issues](https://github.com/microsoft/AI-For-Beginners/issues)
- **Pýtajte sa otázky:** Použite GitHub Discussions alebo otvorte issue.
- **Komunita:** Pozrite si odkazy na repozitári pre možnosti chatu/fóra.

---

_Posledná aktualizácia: 2025-09-20_

---

**Upozornenie**:  
Tento dokument bol preložený pomocou služby AI prekladu [Co-op Translator](https://github.com/Azure/co-op-translator). Hoci sa snažíme o presnosť, prosím, berte na vedomie, že automatizované preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho rodnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nenesieme zodpovednosť za akékoľvek nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.