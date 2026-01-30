# AI-For-Beginners Vianmääritysopas

Tämä opas auttaa ratkaisemaan yleisiä ongelmia, joita voi kohdata käyttäessäsi tai osallistuessasi [AI-For-Beginners](https://github.com/microsoft/AI-For-Beginners) -repositoryyn. Jokainen ongelma sisältää taustatietoa, oireet, selitykset ja vaiheittaiset ratkaisut.

---

## Sisällysluettelo

- [Yleiset ongelmat](../..)
- [Asennusongelmat](../..)
- [Konfigurointiongelmat](../..)
- [Notebookien suorittaminen](../..)
- [Suorituskykyongelmat](../..)
- [Oppikirjasivuston ongelmat](../..)
- [Osallistumisongelmat](../..)
- [Usein kysytyt kysymykset](../..)
- [Apua ongelmiin](../..)

---

## Yleiset ongelmat

### 1. Repository ei kloonaudu oikein

**Tausta:** Kloonaaminen mahdollistaa repositoryn kopioimisen koneellesi.

**Oireet:**
- Virhe: `fatal: repository not found`
- Virhe: `Permission denied (publickey)`

**Mahdolliset syyt:**
- Väärä repositoryn URL
- Riittämättömät käyttöoikeudet
- SSH-avaimia ei ole konfiguroitu

**Ratkaisut:**
1. **Tarkista repositoryn URL.**  
   Käytä HTTPS-URL:ää:  
   ```
   git clone https://github.com/microsoft/AI-For-Beginners.git
   ```
2. **Vaihda HTTPS:ään, jos SSH epäonnistuu.**  
   Jos näet `Permission denied (publickey)`, käytä yllä olevaa HTTPS-linkkiä SSH:n sijaan.
3. **Konfiguroi SSH-avaimet (valinnainen).**  
   Jos haluat käyttää SSH:ta, seuraa [GitHubin SSH-opasta](https://docs.github.com/en/authentication/connecting-to-github-with-ssh).

---

## Asennusongelmat

### 2. Python-ympäristöongelmat

**Tausta:** Repository käyttää Pythonia ja erilaisia kirjastoja.

**Oireet:**
- Virhe: `ModuleNotFoundError: No module named '<package>'`
- Tuontivirheitä skriptejä tai notebookeja suoritettaessa

**Mahdolliset syyt:**
- Riippuvuuksia ei ole asennettu
- Väärä Python-versio

**Ratkaisut:**
1. **Luo virtuaaliympäristö.**  
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```
2. **Asenna riippuvuudet.**  
   ```bash
   pip install -r requirements.txt
   ```
3. **Tarkista Python-versio.**  
   Käytä Python 3.7 tai uudempaa.  
   ```bash
   python --version
   ```

### 3. Jupyter ei ole asennettu

**Tausta:** Notebookit ovat keskeinen oppimisresurssi.

**Oireet:**
- Virhe: `jupyter: command not found`
- Notebookit eivät käynnisty

**Mahdolliset syyt:**
- Jupyter ei ole asennettu

**Ratkaisut:**
1. **Asenna Jupyter Notebook.**  
   ```bash
   pip install notebook
   ```
   tai, jos käytät Anacondaa:
   ```bash
   conda install notebook
   ```
2. **Käynnistä Jupyter Notebook.**  
   ```bash
   jupyter notebook
   ```

### 4. Riippuvuuksien versioristiriidat

**Tausta:** Projektit voivat rikkoutua, jos pakettiversiot eivät täsmää.

**Oireet:**
- Virheitä tai varoituksia yhteensopimattomista versioista

**Mahdolliset syyt:**
- Vanhat tai ristiriitaiset Python-paketit

**Ratkaisut:**
1. **Asenna puhtaaseen ympäristöön.**  
   Poista vanha venv/conda-ympäristö ja luo uusi.
2. **Käytä tarkkoja versioita.**  
   Suorita aina:
   ```bash
   pip install -r requirements.txt
   ```
   Jos tämä epäonnistuu, asenna puuttuvat paketit manuaalisesti README:n ohjeiden mukaan.

---

## Konfigurointiongelmat

### 5. Ympäristömuuttujia ei ole asetettu

**Tausta:** Jotkut moduulit saattavat vaatia avaimia, tokeneita tai konfigurointiasetuksia.

**Oireet:**
- Virhe: `KeyError` tai varoituksia puuttuvista konfiguraatioista

**Mahdolliset syyt:**
- Tarvittavia ympäristömuuttujia ei ole asetettu

**Ratkaisut:**
1. **Tarkista `.env.example` tai vastaavat tiedostot.**
2. **Luo `.env`-tiedosto ja täytä tarvittavat arvot.**
3. **Lataa terminaali tai IDE uudelleen ympäristömuuttujien asettamisen jälkeen.**

---

## Notebookien suorittaminen

### 6. Notebook ei avaudu tai käynnisty

**Tausta:** Jupyter-notebookit vaativat oikeanlaisen asennuksen.

**Oireet:**
- Notebook ei käynnisty
- Selain ei avaudu automaattisesti

**Mahdolliset syyt:**
- Jupyter ei ole asennettu
- Selaimen konfigurointiongelmat

**Ratkaisut:**
1. **Asenna Jupyter (katso Asennusongelmat yllä).**
2. **Avaa notebookit manuaalisesti.**
   - Kopioi URL terminaalista (esim. `http://localhost:8888/?token=...`) ja liitä se selaimeesi.

### 7. Kernel kaatuu tai jäätyy

**Tausta:** Notebookien kernelit voivat kaatua resurssirajoitusten tai koodivirheiden vuoksi.

**Oireet:**
- Kernel kuolee tai käynnistyy uudelleen toistuvasti
- Muistivirheet

**Mahdolliset syyt:**
- Suuret datasetit
- Yhteensopimattomat koodit tai paketit

**Ratkaisut:**
1. **Käynnistä kernel uudelleen.**  
   Käytä Jupyterin "Restart Kernel" -painiketta.
2. **Tarkista muistin käyttö.**  
   Sulje käyttämättömät sovellukset.
3. **Suorita notebookit pilvialustoilla.**  
   Käytä [Google Colabia](https://colab.research.google.com/) tai [Azure Notebooksia](https://notebooks.azure.com/).

---

## Suorituskykyongelmat

### 8. Notebookit toimivat hitaasti

**Tausta:** Jotkut AI-tehtävät vaativat paljon muistia ja prosessoritehoa.

**Oireet:**
- Hidas suoritus
- Kannettavan tuuletin käy kovaa

**Mahdolliset syyt:**
- Suuret datasetit tai mallit
- Rajoitetut järjestelmäresurssit

**Ratkaisut:**
1. **Käytä pilvialustaa.**
   - Lataa notebook Colabiin tai Azure Notebooksille.
2. **Pienennä datasetin kokoa.**
   - Käytä harjoitteluun näyteaineistoa.
3. **Sulje tarpeettomat ohjelmat.**
   - Vapauta järjestelmän RAM-muistia.

---

## Oppikirjasivuston ongelmat

### 9. Luku ei lataudu

**Tausta:** Verkkokirja näyttää oppitunnit ja luvut.

**Oireet:**
- Luku (esim. Transformers/BERT) puuttuu tai ei avaudu

**Tunnettu ongelma:**  
- [Issue #303](https://github.com/microsoft/AI-For-Beginners/issues/303): “18 Transformers. BERT. ei avaudu oppikirjasivustolla.” Johtuu tiedostonimen virheestä (`READMEtransformers.md` sijasta `README.md`).

**Ratkaisut:**
1. **Tarkista tiedostonimen virheet.**  
   Jos olet kontribuoija, varmista, että luvun tiedostot on nimetty `README.md`.
2. **Ilmoita puuttuvista tiedostoista.**  
   Avaa GitHub-issue luvun nimen ja virheen yksityiskohtien kanssa.

---

## Osallistumisongelmat

### 10. PR ei hyväksytty tai buildit epäonnistuvat

**Tausta:** Kontribuutiot täytyy läpäistä testit ja noudattaa ohjeita.

**Oireet:**
- Pull request hylätty
- CI/CD-putkivirheet

**Mahdolliset syyt:**
- Epäonnistuneet testit
- Koodistandardien noudattamatta jättäminen

**Ratkaisut:**
1. **Lue kontribuutio-ohjeet.**
   - Noudata repositoryn [CONTRIBUTING.md](https://github.com/microsoft/AI-For-Beginners/blob/main/CONTRIBUTING.md).
2. **Suorita testit paikallisesti ennen pushia.**
3. **Tarkista linting-säännöt tai muotoiluvaatimukset.**

---

## Usein kysytyt kysymykset

### Mistä löydän apua tiettyihin moduuleihin?
- Jokaisella moduulilla on yleensä oma README. Aloita siitä asennus- ja käyttöohjeiden osalta.

### Miten raportoin bugin tai pyydän ominaisuutta?
- [Avaa GitHub-issue](https://github.com/microsoft/AI-For-Beginners/issues/new) selkeällä kuvauksella ja toistovaiheilla.

### Voinko pyytää apua, jos ongelmani ei ole listattu?
- Kyllä! Etsi ensin olemassa olevia issueita, ja jos et löydä ongelmaasi, luo uusi issue.

---

## Apua ongelmiin

- **Tarkista issueita:** [GitHub Issues](https://github.com/microsoft/AI-For-Beginners/issues)
- **Esitä kysymyksiä:** Käytä GitHubin keskusteluja tai avaa issue.
- **Yhteisö:** Katso repositoryn linkit chat-/foorumivaihtoehtoihin.

---

_Viimeksi päivitetty: 2025-09-20_

---

**Vastuuvapauslauseke**:  
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, huomioithan, että automaattiset käännökset voivat sisältää virheitä tai epätarkkuuksia. Alkuperäinen asiakirja sen alkuperäisellä kielellä tulisi pitää ensisijaisena lähteenä. Kriittisen tiedon osalta suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa väärinkäsityksistä tai virhetulkinnoista, jotka johtuvat tämän käännöksen käytöstä.