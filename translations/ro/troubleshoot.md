# Ghid de depanare AI-For-Beginners

Acest ghid te ajută să rezolvi problemele comune întâlnite în utilizarea sau contribuția la repository-ul [AI-For-Beginners](https://github.com/microsoft/AI-For-Beginners). Fiecare problemă include context, simptome, explicații și soluții pas cu pas.

---

## Cuprins

- [Probleme Generale](../..)
- [Probleme de Instalare](../..)
- [Probleme de Configurare](../..)
- [Rularea Notebooks](../..)
- [Probleme de Performanță](../..)
- [Probleme cu Website-ul Manualului](../..)
- [Probleme de Contribuție](../..)
- [FAQ](../..)
- [Obținerea Ajutorului](../..)

---

## Probleme Generale

### 1. Repository-ul nu se clonează corect

**Context:** Clonarea îți permite să copiezi repository-ul pe dispozitivul tău.

**Simptome:**
- Eroare: `fatal: repository not found`
- Eroare: `Permission denied (publickey)`

**Cauze posibile:**
- URL-ul repository-ului este incorect
- Permisiuni insuficiente
- Cheile SSH nu sunt configurate

**Soluții:**
1. **Verifică URL-ul repository-ului.**  
   Folosește URL-ul HTTPS:  
   ```
   git clone https://github.com/microsoft/AI-For-Beginners.git
   ```
2. **Comută la HTTPS dacă SSH eșuează.**  
   Dacă vezi `Permission denied (publickey)`, folosește linkul HTTPS de mai sus în loc de SSH.
3. **Configurează cheile SSH (opțional).**  
   Dacă vrei să folosești SSH, urmează [ghidul SSH de la GitHub](https://docs.github.com/en/authentication/connecting-to-github-with-ssh).

---

## Probleme de Instalare

### 2. Probleme cu mediul Python

**Context:** Repository-ul se bazează pe Python și diverse biblioteci.

**Simptome:**
- Eroare: `ModuleNotFoundError: No module named '<package>'`
- Erori de import la rularea scripturilor sau notebooks

**Cauze posibile:**
- Dependențele nu sunt instalate
- Versiunea Python este greșită

**Soluții:**
1. **Configurează un mediu virtual.**  
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```
2. **Instalează dependențele.**  
   ```bash
   pip install -r requirements.txt
   ```
3. **Verifică versiunea Python.**  
   Folosește Python 3.7 sau mai nou.  
   ```bash
   python --version
   ```

### 3. Jupyter nu este instalat

**Context:** Notebooks sunt o resursă esențială pentru învățare.

**Simptome:**
- Eroare: `jupyter: command not found`
- Notebooks nu se lansează

**Cauze posibile:**
- Jupyter nu este instalat

**Soluții:**
1. **Instalează Jupyter Notebook.**  
   ```bash
   pip install notebook
   ```
   sau, dacă folosești Anaconda:
   ```bash
   conda install notebook
   ```
2. **Pornește Jupyter Notebook.**  
   ```bash
   jupyter notebook
   ```

### 4. Conflicte de versiuni ale dependențelor

**Context:** Proiectele pot eșua dacă versiunile pachetelor nu sunt compatibile.

**Simptome:**
- Erori sau avertismente despre versiuni incompatibile

**Cauze posibile:**
- Pachete Python vechi sau conflictuale

**Soluții:**
1. **Instalează într-un mediu curat.**  
   Șterge vechiul venv/env conda și creează unul nou.
2. **Folosește versiuni exacte.**  
   Rulează mereu:
   ```bash
   pip install -r requirements.txt
   ```
   Dacă acest lucru eșuează, instalează manual pachetele lipsă conform README.

---

## Probleme de Configurare

### 5. Variabilele de mediu nu sunt setate

**Context:** Unele module pot necesita chei, token-uri sau setări de configurare.

**Simptome:**
- Eroare: `KeyError` sau avertismente despre configurări lipsă

**Cauze posibile:**
- Variabilele de mediu necesare nu sunt setate

**Soluții:**
1. **Verifică fișierele `.env.example` sau similare.**
2. **Creează un fișier `.env` și completează valorile necesare.**
3. **Reîncarcă terminalul sau IDE-ul după setarea variabilelor de mediu.**

---

## Rularea Notebooks

### 6. Notebook-ul nu se deschide sau nu rulează

**Context:** Notebooks Jupyter necesită o configurare corectă.

**Simptome:**
- Notebook-ul nu se lansează
- Browserul nu se deschide automat

**Cauze posibile:**
- Jupyter nu este instalat
- Probleme de configurare a browserului

**Soluții:**
1. **Instalează Jupyter (vezi Probleme de Instalare de mai sus).**
2. **Deschide notebooks manual.**
   - Copiază URL-ul din terminal (ex.: `http://localhost:8888/?token=...`) și lipește-l în browser.

### 7. Kernel-ul se blochează sau se oprește

**Context:** Kernel-urile notebook-urilor pot eșua din cauza limitelor de resurse sau erorilor de cod.

**Simptome:**
- Kernel-ul moare sau se repornește repetat
- Erori de memorie insuficientă

**Cauze posibile:**
- Seturi de date mari
- Cod sau pachete incompatibile

**Soluții:**
1. **Repornește kernel-ul.**  
   Folosește butonul "Restart Kernel" din Jupyter.
2. **Verifică utilizarea memoriei.**  
   Închide aplicațiile neutilizate.
3. **Rulează notebooks pe platforme cloud.**  
   Folosește [Google Colab](https://colab.research.google.com/) sau [Azure Notebooks](https://notebooks.azure.com/).

---

## Probleme de Performanță

### 8. Notebooks rulează lent

**Context:** Unele sarcini AI necesită memorie și CPU semnificative.

**Simptome:**
- Execuție lentă
- Ventilatorul laptopului funcționează intens

**Cauze posibile:**
- Seturi de date sau modele mari
- Resurse limitate ale sistemului

**Soluții:**
1. **Folosește o platformă cloud.**
   - Încarcă notebook-ul pe Colab sau Azure Notebooks.
2. **Redu dimensiunea setului de date.**
   - Folosește date de probă pentru practică.
3. **Închide programele inutile.**
   - Eliberează RAM-ul sistemului.

---

## Probleme cu Website-ul Manualului

### 9. Capitolul nu se încarcă

**Context:** Manualul online afișează lecții și capitole.

**Simptome:**
- Un capitol (ex.: Transformers/BERT) lipsește sau nu se deschide

**Problemă cunoscută:**  
- [Issue #303](https://github.com/microsoft/AI-For-Beginners/issues/303): „18 Transformers. BERT. nu poate fi deschis pe website-ul manualului.” Cauzată de o eroare de denumire a fișierului (`READMEtransformers.md` în loc de `README.md`).

**Soluții:**
1. **Verifică erorile de redenumire a fișierelor.**  
   Dacă ești contributor, asigură-te că fișierele capitolului sunt denumite `README.md`.
2. **Raportează fișierele lipsă.**  
   Deschide un issue pe GitHub cu numele capitolului și detaliile erorii.

---

## Probleme de Contribuție

### 10. PR nu este acceptat sau build-urile eșuează

**Context:** Contribuțiile trebuie să treacă teste și să respecte ghidurile.

**Simptome:**
- Pull request respins
- Erori în pipeline-ul CI/CD

**Cauze posibile:**
- Teste eșuate
- Nerespectarea standardelor de codare

**Soluții:**
1. **Citește ghidul de contribuție.**
   - Urmează [CONTRIBUTING.md](https://github.com/microsoft/AI-For-Beginners/blob/main/CONTRIBUTING.md) al repository-ului.
2. **Rulează testele local înainte de a face push.**
3. **Verifică regulile de linting sau cerințele de formatare.**

---

## FAQ

### Unde pot găsi ajutor pentru module specifice?
- Fiecare modul are de obicei propriul README. Începe acolo pentru sfaturi de configurare și utilizare.

### Cum raportez un bug sau cer o funcționalitate?
- [Deschide un Issue pe GitHub](https://github.com/microsoft/AI-For-Beginners/issues/new) cu o descriere clară și pași pentru reproducere.

### Pot cere ajutor dacă problema mea nu este listată?
- Da! Caută mai întâi în issues existente, iar dacă nu găsești problema ta, creează un issue nou.

---

## Obținerea Ajutorului

- **Verifică Issues:** [GitHub Issues](https://github.com/microsoft/AI-For-Beginners/issues)
- **Pune întrebări:** Folosește GitHub Discussions sau deschide un issue.
- **Comunitate:** Vezi linkurile repository-ului pentru opțiuni de chat/forum.

---

_Ultima actualizare: 20-09-2025_

---

**Declinare de responsabilitate**:  
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). Deși ne străduim să asigurăm acuratețea, vă rugăm să fiți conștienți că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa natală ar trebui considerat sursa autoritară. Pentru informații critice, se recomandă traducerea profesională realizată de un specialist uman. Nu ne asumăm responsabilitatea pentru eventualele neînțelegeri sau interpretări greșite care pot apărea din utilizarea acestei traduceri.