# AI-For-Beginners Tõrkeotsingu Juhend

See juhend aitab lahendada levinud probleeme, mis võivad tekkida [AI-For-Beginners](https://github.com/microsoft/AI-For-Beginners) repositooriumi kasutamisel või sellele panustamisel. Iga probleem sisaldab tausta, sümptomeid, selgitusi ja samm-sammult lahendusi.

---

## Sisukord

- [Üldised probleemid](../..)
- [Paigaldusprobleemid](../..)
- [Konfiguratsiooniprobleemid](../..)
- [Märkmike käivitamine](../..)
- [Jõudlusprobleemid](../..)
- [Õpikulehe probleemid](../..)
- [Panustamise probleemid](../..)
- [KKK](../..)
- [Abi saamine](../..)

---

## Üldised probleemid

### 1. Repositooriumi ei saa korralikult kloonida

**Taust:** Kloonimine võimaldab kopeerida repositooriumi oma arvutisse.

**Sümptomid:**
- Viga: `fatal: repository not found`
- Viga: `Permission denied (publickey)`

**Võimalikud põhjused:**
- Vale repositooriumi URL
- Ebapiisavad õigused
- SSH võtmed pole seadistatud

**Lahendused:**
1. **Kontrolli repositooriumi URL-i.**  
   Kasuta HTTPS URL-i:  
   ```
   git clone https://github.com/microsoft/AI-For-Beginners.git
   ```
2. **Vaheta HTTPS-i, kui SSH ei tööta.**  
   Kui näed `Permission denied (publickey)`, kasuta ülaltoodud HTTPS linki SSH asemel.
3. **Seadista SSH võtmed (valikuline).**  
   Kui soovid kasutada SSH-d, järgi [GitHubi SSH juhendit](https://docs.github.com/en/authentication/connecting-to-github-with-ssh).

---

## Paigaldusprobleemid

### 2. Python'i keskkonna probleemid

**Taust:** Repositoorium sõltub Pythonist ja mitmetest teekidest.

**Sümptomid:**
- Viga: `ModuleNotFoundError: No module named '<package>'`
- Importimise vead skriptide või märkmike käivitamisel

**Võimalikud põhjused:**
- Sõltuvused pole paigaldatud
- Vale Python'i versioon

**Lahendused:**
1. **Loo virtuaalne keskkond.**  
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```
2. **Paigalda sõltuvused.**  
   ```bash
   pip install -r requirements.txt
   ```
3. **Kontrolli Python'i versiooni.**  
   Kasuta Python 3.7 või uuemat.  
   ```bash
   python --version
   ```

### 3. Jupyter pole paigaldatud

**Taust:** Märkmikud on põhiline õppematerjal.

**Sümptomid:**
- Viga: `jupyter: command not found`
- Märkmikud ei käivitu

**Võimalikud põhjused:**
- Jupyter pole paigaldatud

**Lahendused:**
1. **Paigalda Jupyter Notebook.**  
   ```bash
   pip install notebook
   ```
   või, kui kasutad Anacondat:
   ```bash
   conda install notebook
   ```
2. **Käivita Jupyter Notebook.**  
   ```bash
   jupyter notebook
   ```

### 4. Sõltuvuste versioonide konfliktid

**Taust:** Projektid võivad katkeda, kui teekide versioonid ei ühildu.

**Sümptomid:**
- Veateated või hoiatused sobimatute versioonide kohta

**Võimalikud põhjused:**
- Vanad või vastuolulised Python'i paketid

**Lahendused:**
1. **Paigalda puhtasse keskkonda.**  
   Kustuta vana venv/conda keskkond ja loo uus.
2. **Kasuta täpseid versioone.**  
   Käivita alati:
   ```bash
   pip install -r requirements.txt
   ```
   Kui see ebaõnnestub, paigalda puuduvaid pakette käsitsi vastavalt README juhistele.

---

## Konfiguratsiooniprobleemid

### 5. Keskkonnamuutujad pole seadistatud

**Taust:** Mõned moodulid võivad vajada võtmeid, token'eid või konfiguratsiooniseadeid.

**Sümptomid:**
- Viga: `KeyError` või hoiatused puuduva konfiguratsiooni kohta

**Võimalikud põhjused:**
- Vajalikud keskkonnamuutujad pole seadistatud

**Lahendused:**
1. **Kontrolli `.env.example` või sarnaseid faile.**
2. **Loo `.env` fail ja täida vajalikud väärtused.**
3. **Laadi terminal või IDE uuesti pärast keskkonnamuutujate seadistamist.**

---

## Märkmike käivitamine

### 6. Märkmik ei avane ega tööta

**Taust:** Jupyter märkmikud vajavad korrektset seadistust.

**Sümptomid:**
- Märkmik ei käivitu
- Brauser ei avane automaatselt

**Võimalikud põhjused:**
- Jupyter pole paigaldatud
- Brauseri konfiguratsiooni probleemid

**Lahendused:**
1. **Paigalda Jupyter (vt Paigaldusprobleemid ülal).**
2. **Ava märkmikud käsitsi.**
   - Kopeeri URL terminalist (nt `http://localhost:8888/?token=...`) ja kleebi see oma brauserisse.

### 7. Kernel jookseb kokku või hangub

**Taust:** Märkmiku kernel võib kokku joosta ressursipiirangute või koodivigade tõttu.

**Sümptomid:**
- Kernel sureb või taaskäivitub korduvalt
- Mälu ületäitumise vead

**Võimalikud põhjused:**
- Suured andmekogumid
- Sobimatu kood või teegid

**Lahendused:**
1. **Taaskäivita kernel.**  
   Kasuta Jupyter'i "Restart Kernel" nuppu.
2. **Kontrolli mälukasutust.**  
   Sulge mittevajalikud rakendused.
3. **Käivita märkmikud pilveplatvormidel.**  
   Kasuta [Google Colab](https://colab.research.google.com/) või [Azure Notebooks](https://notebooks.azure.com/).

---

## Jõudlusprobleemid

### 8. Märkmikud töötavad aeglaselt

**Taust:** Mõned AI ülesanded vajavad palju mälu ja protsessorivõimsust.

**Sümptomid:**
- Aeglane täitmine
- Sülearvuti ventilaator töötab valjult

**Võimalikud põhjused:**
- Suured andmekogumid või mudelid
- Piiratud süsteemiressursid

**Lahendused:**
1. **Kasuta pilveplatvormi.**
   - Laadi märkmik üles Colab'i või Azure Notebooks'i.
2. **Vähenda andmekogumi suurust.**
   - Kasuta harjutamiseks näidisandmeid.
3. **Sulge mittevajalikud programmid.**
   - Vabasta süsteemi RAM.

---

## Õpikulehe probleemid

### 9. Peatükk ei laadi

**Taust:** Veebipõhine õpik kuvab õppetunde ja peatükke.

**Sümptomid:**
- Peatükk (nt Transformers/BERT) puudub või ei avane

**Teadaolev probleem:**  
- [Probleem #303](https://github.com/microsoft/AI-For-Beginners/issues/303): “18 Transformers. BERT. ei saa avada õpiku veebilehel.” Põhjustatud failinime veast (`READMEtransformers.md` asemel `README.md`).

**Lahendused:**
1. **Kontrolli failinime vigu.**  
   Kui oled panustaja, veendu, et peatüki failid oleksid nimega `README.md`.
2. **Teata puuduvaist failidest.**  
   Ava GitHub'i probleem peatüki nime ja veadetailidega.

---

## Panustamise probleemid

### 10. PR ei aktsepteerita või ehitused ebaõnnestuvad

**Taust:** Panused peavad läbima testid ja järgima juhiseid.

**Sümptomid:**
- Pull request tagasi lükatud
- CI/CD torujuhtme vead

**Võimalikud põhjused:**
- Testid ebaõnnestuvad
- Koodistandardite mittejärgimine

**Lahendused:**
1. **Loe panustamise juhiseid.**
   - Järgi repositooriumi [CONTRIBUTING.md](https://github.com/microsoft/AI-For-Beginners/blob/main/CONTRIBUTING.md).
2. **Käivita testid lokaalselt enne üleslaadimist.**
3. **Kontrolli lintimise reegleid või vormindamisnõudeid.**

---

## KKK

### Kust leida abi konkreetsete moodulite kohta?
- Igal moodulil on tavaliselt oma README. Alusta sealt seadistamise ja kasutamise näpunäidetega.

### Kuidas teatada veast või taotleda funktsiooni?
- [Ava GitHub'i probleem](https://github.com/microsoft/AI-For-Beginners/issues/new) selge kirjelduse ja kordamise sammudega.

### Kas ma saan abi küsida, kui minu probleem pole loetletud?
- Jah! Otsi esmalt olemasolevaid probleeme ja kui sa ei leia oma probleemi, loo uus probleem.

---

## Abi saamine

- **Kontrolli probleeme:** [GitHub'i probleemid](https://github.com/microsoft/AI-For-Beginners/issues)
- **Esita küsimusi:** Kasuta GitHub'i arutelusid või ava probleem.
- **Kogukond:** Vaata repositooriumi linke vestluse/foorumi valikute jaoks.

---

_Viimati uuendatud: 2025-09-20_

---

**Lahtiütlus**:  
See dokument on tõlgitud, kasutades AI tõlketeenust [Co-op Translator](https://github.com/Azure/co-op-translator). Kuigi püüame tagada täpsust, palun arvestage, et automaatsed tõlked võivad sisaldada vigu või ebatäpsusi. Algne dokument selle algkeeles tuleks lugeda autoriteetseks allikaks. Olulise teabe puhul on soovitatav kasutada professionaalset inimtõlget. Me ei vastuta selle tõlke kasutamisest tulenevate arusaamatuste või valede tõlgenduste eest.