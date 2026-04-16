# AI-For-Beginners Hibaelhárítási Útmutató

Ez az útmutató segít megoldani a gyakori problémákat, amelyek az [AI-For-Beginners](https://github.com/microsoft/AI-For-Beginners) repozitórium használata vagy hozzájárulása során merülhetnek fel. Minden probléma tartalmaz háttérinformációt, tüneteket, magyarázatokat és lépésről lépésre megoldásokat.

---

## Tartalomjegyzék

- [Általános problémák](../..)
- [Telepítési problémák](../..)
- [Konfigurációs problémák](../..)
- [Notebookok futtatása](../..)
- [Teljesítményproblémák](../..)
- [Tankönyv weboldal problémák](../..)
- [Hozzájárulási problémák](../..)
- [GYIK](../..)
- [Segítség kérése](../..)

---

## Általános problémák

### 1. A repozitórium nem klónozható megfelelően

**Háttér:** A klónozás lehetővé teszi, hogy a repozitóriumot lemásold a gépedre.

**Tünetek:**
- Hiba: `fatal: repository not found`
- Hiba: `Permission denied (publickey)`

**Lehetséges okok:**
- Hibás repozitórium URL
- Elégtelen jogosultságok
- SSH kulcsok nincsenek konfigurálva

**Megoldások:**
1. **Ellenőrizd a repozitórium URL-t.**  
   Használd a HTTPS URL-t:  
   ```
   git clone https://github.com/microsoft/AI-For-Beginners.git
   ```
2. **Válts HTTPS-re, ha az SSH nem működik.**  
   Ha `Permission denied (publickey)` hibát látsz, használd a fenti HTTPS linket az SSH helyett.
3. **Konfiguráld az SSH kulcsokat (opcionális).**  
   Ha SSH-t szeretnél használni, kövesd a [GitHub SSH útmutatóját](https://docs.github.com/en/authentication/connecting-to-github-with-ssh).

---

## Telepítési problémák

### 2. Python környezet problémák

**Háttér:** A repozitórium Pythonra és különböző könyvtárakra támaszkodik.

**Tünetek:**
- Hiba: `ModuleNotFoundError: No module named '<package>'`
- Importálási hibák szkriptek vagy notebookok futtatásakor

**Lehetséges okok:**
- Függőségek nincsenek telepítve
- Hibás Python verzió

**Megoldások:**
1. **Hozz létre egy virtuális környezetet.**  
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```
2. **Telepítsd a függőségeket.**  
   ```bash
   pip install -r requirements.txt
   ```
3. **Ellenőrizd a Python verziót.**  
   Használj Python 3.7 vagy újabbat.  
   ```bash
   python --version
   ```

### 3. Jupyter nincs telepítve

**Háttér:** A notebookok alapvető tanulási erőforrások.

**Tünetek:**
- Hiba: `jupyter: command not found`
- A notebookok nem indulnak el

**Lehetséges okok:**
- Jupyter nincs telepítve

**Megoldások:**
1. **Telepítsd a Jupyter Notebookot.**  
   ```bash
   pip install notebook
   ```
   vagy, ha Anacondát használsz:
   ```bash
   conda install notebook
   ```
2. **Indítsd el a Jupyter Notebookot.**  
   ```bash
   jupyter notebook
   ```

### 4. Függőségek verzióütközései

**Háttér:** A projektek összeomolhatnak, ha a csomagok verziói nem kompatibilisek.

**Tünetek:**
- Hibák vagy figyelmeztetések inkompatibilis verziókról

**Lehetséges okok:**
- Régi vagy ütköző Python csomagok

**Megoldások:**
1. **Telepítsd egy tiszta környezetbe.**  
   Töröld a régi venv/conda környezetet, és hozz létre egy újat.
2. **Használj pontos verziókat.**  
   Mindig futtasd:
   ```bash
   pip install -r requirements.txt
   ```
   Ha ez nem működik, manuálisan telepítsd a hiányzó csomagokat a README-ben leírtak szerint.

---

## Konfigurációs problémák

### 5. Környezeti változók nincsenek beállítva

**Háttér:** Néhány modul kulcsokat, tokeneket vagy konfigurációs beállításokat igényelhet.

**Tünetek:**
- Hiba: `KeyError` vagy figyelmeztetések hiányzó konfigurációról

**Lehetséges okok:**
- Szükséges környezeti változók nincsenek beállítva

**Megoldások:**
1. **Ellenőrizd a `.env.example` vagy hasonló fájlokat.**
2. **Hozz létre egy `.env` fájlt, és töltsd ki a szükséges értékeket.**
3. **Indítsd újra a terminált vagy az IDE-t a környezeti változók beállítása után.**

---

## Notebookok futtatása

### 6. A notebook nem nyílik meg vagy nem fut

**Háttér:** A Jupyter notebookok megfelelő beállítást igényelnek.

**Tünetek:**
- A notebook nem indul el
- A böngésző nem nyílik meg automatikusan

**Lehetséges okok:**
- Jupyter nincs telepítve
- Böngésző konfigurációs problémák

**Megoldások:**
1. **Telepítsd a Jupyter-t (lásd Telepítési problémák fent).**
2. **Nyisd meg a notebookokat manuálisan.**
   - Másold ki az URL-t a terminálból (pl. `http://localhost:8888/?token=...`), és illeszd be a böngésződbe.

### 7. Kernel összeomlik vagy lefagy

**Háttér:** A notebook kernelek összeomolhatnak erőforráskorlátok vagy kódhibák miatt.

**Tünetek:**
- A kernel folyamatosan leáll vagy újraindul
- Memóriahiányos hibák

**Lehetséges okok:**
- Nagy adathalmazok
- Inkompatibilis kód vagy csomagok

**Megoldások:**
1. **Indítsd újra a kernelt.**  
   Használd a "Restart Kernel" gombot a Jupyterben.
2. **Ellenőrizd a memóriahasználatot.**  
   Zárd be a nem használt alkalmazásokat.
3. **Futtasd a notebookokat felhőplatformokon.**  
   Használd a [Google Colab](https://colab.research.google.com/) vagy az [Azure Notebooks](https://notebooks.azure.com/) szolgáltatást.

---

## Teljesítményproblémák

### 8. A notebookok lassan futnak

**Háttér:** Néhány AI feladat jelentős memóriát és CPU-t igényel.

**Tünetek:**
- Lassú végrehajtás
- A laptop ventilátora hangosan működik

**Lehetséges okok:**
- Nagy adathalmazok vagy modellek
- Korlátozott rendszererőforrások

**Megoldások:**
1. **Használj felhőplatformot.**
   - Töltsd fel a notebookot a Colabra vagy az Azure Notebooksra.
2. **Csökkentsd az adathalmaz méretét.**
   - Gyakorláshoz használj mintaadatokat.
3. **Zárd be a felesleges programokat.**
   - Szabadíts fel rendszer RAM-ot.

---

## Tankönyv weboldal problémák

### 9. A fejezet nem töltődik be

**Háttér:** Az online tankönyv leckéket és fejezeteket jelenít meg.

**Tünetek:**
- Egy fejezet (pl. Transformers/BERT) hiányzik vagy nem nyílik meg

**Ismert probléma:**  
- [Issue #303](https://github.com/microsoft/AI-For-Beginners/issues/303): „18 Transformers. BERT. nem nyitható meg a tankönyv weboldalán.” Fájlnév hiba okozza (`READMEtransformers.md` helyett `README.md`).

**Megoldások:**
1. **Ellenőrizd a fájl átnevezési hibákat.**  
   Ha hozzájáruló vagy, győződj meg róla, hogy a fejezetfájlok neve `README.md`.
2. **Jelentsd a hiányzó fájlokat.**  
   Nyiss egy GitHub hibajegyet a fejezet nevével és a hiba részleteivel.

---

## Hozzájárulási problémák

### 10. PR nem elfogadott vagy a build hibás

**Háttér:** A hozzájárulásoknak teszteken kell átmenniük, és követniük kell az irányelveket.

**Tünetek:**
- Pull request elutasítva
- CI/CD pipeline hibák

**Lehetséges okok:**
- Hibás tesztek
- Nem megfelelő kódolási szabványok

**Megoldások:**
1. **Olvasd el a hozzájárulási irányelveket.**
   - Kövesd a repozitórium [CONTRIBUTING.md](https://github.com/microsoft/AI-For-Beginners/blob/main/CONTRIBUTING.md) fájlját.
2. **Futtasd a teszteket helyben, mielőtt feltöltöd.**
3. **Ellenőrizd a linting szabályokat vagy formázási követelményeket.**

---

## GYIK

### Hol találok segítséget az egyes modulokhoz?
- Minden modulnak általában van saját README fájlja. Kezdd ott a beállítási és használati tippekért.

### Hogyan jelenthetek hibát vagy kérhetek új funkciót?
- [Nyiss egy GitHub hibajegyet](https://github.com/microsoft/AI-For-Beginners/issues/new) egyértelmű leírással és reprodukálási lépésekkel.

### Kérhetek segítséget, ha a problémám nincs felsorolva?
- Igen! Először keresd meg a meglévő hibajegyeket, és ha nem találod a problémádat, hozz létre egy új hibajegyet.

---

## Segítség kérése

- **Ellenőrizd a hibajegyeket:** [GitHub Issues](https://github.com/microsoft/AI-For-Beginners/issues)
- **Tegyél fel kérdéseket:** Használd a GitHub Discussions-t vagy nyiss egy hibajegyet.
- **Közösség:** Nézd meg a repozitórium linkjeit chat/forum lehetőségekért.

---

_Utolsó frissítés: 2025-09-20_

---

**Felelősség kizárása**:  
Ez a dokumentum az [Co-op Translator](https://github.com/Azure/co-op-translator) AI fordítási szolgáltatás segítségével került lefordításra. Bár törekszünk a pontosságra, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az eredeti nyelvén tekintendő hiteles forrásnak. Kritikus információk esetén javasolt professzionális emberi fordítást igénybe venni. Nem vállalunk felelősséget semmilyen félreértésért vagy téves értelmezésért, amely a fordítás használatából eredhet.