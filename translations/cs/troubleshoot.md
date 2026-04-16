# Průvodce řešením problémů AI-For-Beginners

Tento průvodce vám pomůže vyřešit běžné problémy, na které můžete narazit při používání nebo přispívání do repozitáře [AI-For-Beginners](https://github.com/microsoft/AI-For-Beginners). Každý problém obsahuje pozadí, příznaky, vysvětlení a postupné řešení.

---

## Obsah

- [Obecné problémy](../..)
- [Problémy s instalací](../..)
- [Problémy s konfigurací](../..)
- [Spouštění notebooků](../..)
- [Problémy s výkonem](../..)
- [Problémy s webem učebnice](../..)
- [Problémy s přispíváním](../..)
- [Často kladené dotazy](../..)
- [Získání pomoci](../..)

---

## Obecné problémy

### 1. Repozitář se nedaří správně naklonovat

**Pozadí:** Klonování vám umožní zkopírovat repozitář na váš počítač.

**Příznaky:**
- Chyba: `fatal: repository not found`
- Chyba: `Permission denied (publickey)`

**Možné příčiny:**
- Nesprávná URL adresa repozitáře
- Nedostatečná oprávnění
- Nejsou nakonfigurovány SSH klíče

**Řešení:**
1. **Zkontrolujte URL repozitáře.**  
   Použijte HTTPS URL:  
   ```
   git clone https://github.com/microsoft/AI-For-Beginners.git
   ```
2. **Přepněte na HTTPS, pokud SSH selže.**  
   Pokud vidíte `Permission denied (publickey)`, použijte místo SSH odkaz na HTTPS.
3. **Nakonfigurujte SSH klíče (volitelné).**  
   Pokud chcete používat SSH, postupujte podle [průvodce SSH na GitHubu](https://docs.github.com/en/authentication/connecting-to-github-with-ssh).

---

## Problémy s instalací

### 2. Problémy s Python prostředím

**Pozadí:** Repozitář závisí na Pythonu a různých knihovnách.

**Příznaky:**
- Chyba: `ModuleNotFoundError: No module named '<package>'`
- Chyby při importu při spouštění skriptů nebo notebooků

**Možné příčiny:**
- Nejsou nainstalovány závislosti
- Nesprávná verze Pythonu

**Řešení:**
1. **Nastavte virtuální prostředí.**  
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```
2. **Nainstalujte závislosti.**  
   ```bash
   pip install -r requirements.txt
   ```
3. **Zkontrolujte verzi Pythonu.**  
   Použijte Python 3.7 nebo novější.  
   ```bash
   python --version
   ```

### 3. Jupyter není nainstalován

**Pozadí:** Notebooky jsou klíčovým zdrojem pro učení.

**Příznaky:**
- Chyba: `jupyter: command not found`
- Notebooky se nespustí

**Možné příčiny:**
- Jupyter není nainstalován

**Řešení:**
1. **Nainstalujte Jupyter Notebook.**  
   ```bash
   pip install notebook
   ```
   nebo, pokud používáte Anacondu:
   ```bash
   conda install notebook
   ```
2. **Spusťte Jupyter Notebook.**  
   ```bash
   jupyter notebook
   ```

### 4. Konflikty verzí závislostí

**Pozadí:** Projekty mohou selhat, pokud jsou verze balíčků nekompatibilní.

**Příznaky:**
- Chyby nebo varování o nekompatibilních verzích

**Možné příčiny:**
- Staré nebo konfliktní Python balíčky

**Řešení:**
1. **Nainstalujte v čistém prostředí.**  
   Smažte staré venv/conda prostředí a vytvořte nové.
2. **Používejte přesné verze.**  
   Vždy spusťte:
   ```bash
   pip install -r requirements.txt
   ```
   Pokud to selže, ručně nainstalujte chybějící balíčky podle README.

---

## Problémy s konfigurací

### 5. Prostředí není správně nastaveno

**Pozadí:** Některé moduly mohou vyžadovat klíče, tokeny nebo konfigurační nastavení.

**Příznaky:**
- Chyba: `KeyError` nebo varování o chybějící konfiguraci

**Možné příčiny:**
- Požadované proměnné prostředí nejsou nastaveny

**Řešení:**
1. **Zkontrolujte soubory jako `.env.example` nebo podobné.**
2. **Vytvořte soubor `.env` a vyplňte požadované hodnoty.**
3. **Po nastavení proměnných prostředí restartujte terminál nebo IDE.**

---

## Spouštění notebooků

### 6. Notebook se nespustí nebo neotevře

**Pozadí:** Jupyter notebooky vyžadují správné nastavení.

**Příznaky:**
- Notebook se nespustí
- Prohlížeč se neotevře automaticky

**Možné příčiny:**
- Jupyter není nainstalován
- Problémy s konfigurací prohlížeče

**Řešení:**
1. **Nainstalujte Jupyter (viz Problémy s instalací výše).**
2. **Otevřete notebooky ručně.**
   - Zkopírujte URL z terminálu (např. `http://localhost:8888/?token=...`) a vložte ji do prohlížeče.

### 7. Kernel se zhroutí nebo zamrzne

**Pozadí:** Kernel notebooku může selhat kvůli omezením zdrojů nebo chybám v kódu.

**Příznaky:**
- Kernel se opakovaně restartuje nebo umírá
- Chyby nedostatku paměti

**Možné příčiny:**
- Velké datové sady
- Nekompatibilní kód nebo balíčky

**Řešení:**
1. **Restartujte kernel.**  
   Použijte tlačítko "Restart Kernel" v Jupyteru.
2. **Zkontrolujte využití paměti.**  
   Zavřete nepoužívané aplikace.
3. **Spouštějte notebooky na cloudových platformách.**  
   Použijte [Google Colab](https://colab.research.google.com/) nebo [Azure Notebooks](https://notebooks.azure.com/).

---

## Problémy s výkonem

### 8. Notebooky běží pomalu

**Pozadí:** Některé AI úlohy vyžadují značné množství paměti a CPU.

**Příznaky:**
- Pomalé provádění
- Hlučný ventilátor notebooku

**Možné příčiny:**
- Velké datové sady nebo modely
- Omezené systémové zdroje

**Řešení:**
1. **Použijte cloudovou platformu.**
   - Nahrajte notebook na Colab nebo Azure Notebooks.
2. **Zmenšete velikost datové sady.**
   - Použijte vzorová data pro praxi.
3. **Zavřete nepotřebné programy.**
   - Uvolněte systémovou RAM.

---

## Problémy s webem učebnice

### 9. Kapitola se nenačítá

**Pozadí:** Online učebnice zobrazuje lekce a kapitoly.

**Příznaky:**
- Kapitola (např. Transformers/BERT) chybí nebo se neotevírá

**Známý problém:**  
- [Problém #303](https://github.com/microsoft/AI-For-Beginners/issues/303): „18 Transformers. BERT. nelze otevřít na webu učebnice.“ Způsobeno chybou názvu souboru (`READMEtransformers.md` místo `README.md`).

**Řešení:**
1. **Zkontrolujte chyby v názvech souborů.**  
   Pokud jste přispěvatelem, ujistěte se, že kapitoly mají název `README.md`.
2. **Nahlaste chybějící soubory.**  
   Otevřete GitHub issue s názvem kapitoly a detaily chyby.

---

## Problémy s přispíváním

### 10. PR není přijat nebo sestavení selhává

**Pozadí:** Příspěvky musí projít testy a splňovat pokyny.

**Příznaky:**
- Pull request zamítnut
- Chyby v CI/CD pipeline

**Možné příčiny:**
- Selhávající testy
- Nedodržení standardů kódování

**Řešení:**
1. **Přečtěte si pokyny pro přispívání.**
   - Postupujte podle [CONTRIBUTING.md](https://github.com/microsoft/AI-For-Beginners/blob/main/CONTRIBUTING.md) repozitáře.
2. **Spusťte testy lokálně před odesláním.**
3. **Zkontrolujte pravidla pro linting nebo požadavky na formátování.**

---

## Často kladené dotazy

### Kde najdu pomoc pro konkrétní moduly?
- Každý modul obvykle obsahuje vlastní README. Začněte tam pro tipy k nastavení a použití.

### Jak nahlásím chybu nebo požádám o funkci?
- [Otevřete GitHub Issue](https://github.com/microsoft/AI-For-Beginners/issues/new) s jasným popisem a kroky k reprodukci.

### Mohu požádat o pomoc, pokud můj problém není uveden?
- Ano! Nejprve vyhledejte existující problémy, a pokud svůj problém nenajdete, vytvořte nový issue.

---

## Získání pomoci

- **Zkontrolujte problémy:** [GitHub Issues](https://github.com/microsoft/AI-For-Beginners/issues)
- **Ptejte se:** Použijte GitHub Discussions nebo otevřete issue.
- **Komunita:** Viz odkazy v repozitáři na chat/fora.

---

_Naposledy aktualizováno: 20. září 2025_

---

**Prohlášení**:  
Tento dokument byl přeložen pomocí služby AI pro překlady [Co-op Translator](https://github.com/Azure/co-op-translator). I když se snažíme o přesnost, mějte prosím na paměti, že automatizované překlady mohou obsahovat chyby nebo nepřesnosti. Původní dokument v jeho původním jazyce by měl být považován za autoritativní zdroj. Pro důležité informace se doporučuje profesionální lidský překlad. Neodpovídáme za žádná nedorozumění nebo nesprávné interpretace vyplývající z použití tohoto překladu.