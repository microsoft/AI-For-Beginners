# AGENTS.md

## Projektin yleiskatsaus

AI for Beginners on kattava 12 viikon, 24 oppitunnin kurssi, joka käsittelee tekoälyn perusteita. Tämä opetusmateriaali sisältää käytännön oppitunteja Jupyter Notebooks -ympäristössä, kyselyitä ja käytännön harjoituksia. Kurssi kattaa:

- Symbolinen tekoäly: Tiedon esitys ja asiantuntijajärjestelmät
- Neuroverkot ja syväoppiminen TensorFlow- ja PyTorch-työkaluilla
- Tietokonenäön tekniikat ja arkkitehtuurit
- Luonnollisen kielen käsittely (NLP), mukaan lukien transformerit ja BERT
- Erikoisaiheet: geneettiset algoritmit, vahvistusoppiminen, monen agentin järjestelmät
- Tekoälyn etiikka ja vastuullisen tekoälyn periaatteet

**Keskeiset teknologiat:** Python 3, Jupyter Notebooks, TensorFlow, PyTorch, Keras, OpenCV, Vue.js (kyselysovellusta varten)

**Arkkitehtuuri:** Opetusmateriaalin arkisto, jossa Jupyter Notebooks -tiedostot on järjestetty aihealueittain, täydennetty Vue.js-pohjaisella kyselysovelluksella ja laajalla monikielisellä tuella.

## Asennuskomennot

### Ensisijainen kehitysympäristö (Python/Jupyter)

Kurssi on suunniteltu toimimaan Pythonin ja Jupyter Notebooks -ympäristön kanssa. Suositeltu tapa on käyttää minicondaa:

```bash
# Clone the repository
git clone https://github.com/microsoft/ai-for-beginners
cd ai-for-beginners

# Create and activate conda environment
conda env create --name ai4beg --file environment.yml
conda activate ai4beg

# Start Jupyter Notebook
jupyter notebook
# OR
jupyter lab
```

### Vaihtoehto: devcontainerin käyttö

```bash
# Open in VS Code and select "Reopen in Container" when prompted
# The devcontainer will automatically set up the environment
```

### Kyselysovelluksen asennus

Kyselysovellus on erillinen Vue.js-sovellus, joka sijaitsee hakemistossa `etc/quiz-app/`:

```bash
cd etc/quiz-app
npm install
npm run serve  # Development server
npm run build  # Production build
npm run lint   # Lint and fix files
```

## Kehitystyön kulku

### Työskentely Jupyter Notebooks -ympäristössä

1. **Paikallinen kehitys:**
   - Aktivoi conda-ympäristö: `conda activate ai4beg`
   - Käynnistä Jupyter: `jupyter notebook` tai `jupyter lab`
   - Siirry oppituntikansioihin ja avaa `.ipynb`-tiedostot
   - Suorita solut vuorovaikutteisesti oppituntien seuraamiseksi

2. **VS Code Python-laajennuksella:**
   - Avaa arkisto VS Codessa
   - Asenna Python-laajennus
   - VS Code tunnistaa ja käyttää automaattisesti conda-ympäristöä
   - Avaa `.ipynb`-tiedostot suoraan VS Codessa

3. **Pilvikehitys:**
   - **GitHub Codespaces:** Klikkaa "Code" → "Codespaces" → "Create codespace on main"
   - **Binder:** Käytä README-tiedoston Binder-painiketta käynnistääksesi selaimessa
   - Huomio: Binderilla on rajalliset resurssit ja joitakin verkkopääsyrajoituksia

### GPU-tuki edistyneille oppitunneille

Myöhemmät oppitunnit hyötyvät merkittävästi GPU-kiihdytyksestä:

- **Azure Data Science VM:** Käytä NC-sarjan virtuaalikoneita, joissa on GPU-tuki
- **Azure Machine Learning:** Käytä muistikirjaominaisuuksia GPU-laskennan kanssa
- **Google Colab:** Lataa muistikirjat yksitellen (ilmainen GPU-tuki saatavilla)

### Kyselysovelluksen kehitys

```bash
cd etc/quiz-app
npm run serve  # Hot-reload development server at http://localhost:8080
```

## Testausohjeet

Tämä on opetusmateriaali, joka keskittyy oppimissisältöön eikä ohjelmistotestaukseen. Perinteistä testipakettia ei ole.

### Vahvistusmenetelmät:

1. **Jupyter Notebooks:** Suorita solut järjestyksessä varmistaaksesi, että koodiesimerkit toimivat
2. **Kyselysovelluksen testaus:** Manuaalinen testaus kehityspalvelimen kautta
3. **Käännösten tarkistus:** Tarkista käännetty sisältö `translations/`-kansiossa
4. **Kyselysovelluksen linttaus:** `npm run lint` hakemistossa `etc/quiz-app/`

### Koodiesimerkkien suorittaminen:

```bash
# Activate environment first
conda activate ai4beg

# Run Python scripts directly
python lessons/4-ComputerVision/07-ConvNets/pytorchcv.py

# Or execute notebooks
jupyter notebook lessons/3-NeuralNetworks/03-Perceptron/Perceptron.ipynb
```

## Koodityyli

### Python-koodityyli

- Standardit Python-käytännöt opetusmateriaalille
- Selkeä, helposti luettava koodi, joka painottaa oppimista optimoinnin sijaan
- Kommentit, jotka selittävät keskeiset käsitteet
- Jupyter Notebook -ystävällinen: solujen tulisi olla mahdollisimman itsenäisiä
- Ei tiukkoja linttausvaatimuksia oppituntisisällölle

### JavaScript/Vue.js (kyselysovellus)

- ESLint-konfiguraatio tiedostossa `etc/quiz-app/package.json`
- Suorita `npm run lint` tarkistaaksesi ja korjataksesi ongelmat automaattisesti
- Vue 2.x -käytännöt
- Komponenttipohjainen arkkitehtuuri

### Tiedostojen järjestely

```
lessons/
  ├── 0-course-setup/          # Setup instructions
  ├── 1-Intro/                 # Introduction to AI
  ├── 2-Symbolic/              # Symbolic AI
  ├── 3-NeuralNetworks/        # Neural Networks basics
  ├── 4-ComputerVision/        # Computer Vision
  ├── 5-NLP/                   # Natural Language Processing
  ├── 6-Other/                 # Other AI techniques
  ├── 7-Ethics/                # AI Ethics
  └── X-Extras/                # Additional content

etc/
  ├── quiz-app/                # Vue.js quiz application
  └── quiz-src/                # Quiz source files

translations/                  # Multi-language translations
```

## Rakennus ja käyttöönotto

### Jupyter-sisältö

Rakennusprosessia ei tarvita - Jupyter Notebooks -tiedostot suoritetaan suoraan.

### Kyselysovellus

```bash
cd etc/quiz-app

# Development
npm run serve

# Production build
npm run build  # Outputs to etc/quiz-app/dist/

# Deploy to Azure Static Web Apps
# Azure automatically creates GitHub Actions workflow
# See etc/quiz-app/README.md for detailed deployment instructions
```

### Dokumentaatiosivusto

Arkisto käyttää Docsifyä dokumentaatiota varten:
- `index.html` toimii aloituspisteenä
- Rakennusta ei tarvita - palvelu suoraan GitHub Pagesin kautta
- Pääsy osoitteessa: https://microsoft.github.io/AI-For-Beginners/

## Osallistumisohjeet

### Pull Request -prosessi

1. **Otsikon muoto:** Selkeät, kuvaavat otsikot, jotka kertovat muutoksesta
2. **CLA-vaatimus:** Microsoft CLA on allekirjoitettava (automaattinen tarkistus)
3. **Sisältöohjeet:**
   - Säilytä opetuslähtöisyys ja aloittelijaystävällinen lähestymistapa
   - Testaa kaikki koodiesimerkit muistikirjoissa
   - Varmista, että muistikirjat toimivat alusta loppuun
   - Päivitä käännökset, jos muutat englanninkielistä sisältöä
4. **Kyselysovelluksen muutokset:** Suorita `npm run lint` ennen sitoutumista

### Käännöspanokset

- Käännökset automatisoidaan GitHub Actionsin kautta co-op-translatorilla
- Manuaaliset käännökset sijoitetaan hakemistoon `translations/<language-code>/`
- Kyselykäännökset hakemistoon `etc/quiz-app/src/assets/translations/`
- Tuetut kielet: yli 40 kieltä (katso README täydellinen lista)

### Aktiiviset osallistumisalueet

Katso `etc/CONTRIBUTING.md` nykyiset tarpeet:
- Syvävahvistusoppimisen osiot
- Objektin tunnistuksen parannukset
- Esimerkkejä nimettyjen entiteettien tunnistuksesta
- Näytteitä mukautetusta upotuskoulutuksesta

## Ympäristön konfigurointi

### Vaaditut riippuvuudet

```bash
# Core Python packages (from requirements.txt)
tensorflow==2.17.0
torch (via conda)
torchvision (via conda)
keras==3.5.0
opencv (via conda)
scikit-learn
numpy==1.26
pandas==2.2.2
matplotlib==3.9
jupyter
```

### Ympäristömuuttujat

Peruskäyttöön ei tarvita erityisiä ympäristömuuttujia.

Azure-käyttöönottoa varten (kyselysovellus):
- `AZURE_STATIC_WEB_APPS_API_TOKEN` (Azure asettaa automaattisesti)

## Vianmääritys ja ongelmien ratkaisu

### Yleiset ongelmat

**Ongelma:** Conda-ympäristön luominen epäonnistuu
- **Ratkaisu:** Päivitä ensin conda: `conda update conda -y`
- Varmista riittävä levytila (suositus 50GB)

**Ongelma:** Jupyter-ydintä ei löydy
- **Ratkaisu:** 
  ```bash
  conda activate ai4beg
  python -m ipykernel install --user --name ai4beg
  ```

**Ongelma:** GPU ei tunnistu muistikirjoissa
- **Ratkaisu:** 
  - Varmista CUDA-asennus: `nvidia-smi`
  - Tarkista PyTorch GPU: `python -c "import torch; print(torch.cuda.is_available())"`
  - Tarkista TensorFlow GPU: `python -c "import tensorflow as tf; print(tf.config.list_physical_devices('GPU'))"`

**Ongelma:** Kyselysovellus ei käynnisty
- **Ratkaisu:**
  ```bash
  cd etc/quiz-app
  rm -rf node_modules package-lock.json
  npm install
  npm run serve
  ```

**Ongelma:** Binder aikakatkaisee tai estää lataukset
- **Ratkaisu:** Käytä GitHub Codespacesia tai paikallista asennusta parempien resurssien saamiseksi

### Muistiongelmat

Jotkut oppitunnit vaativat merkittävää RAM-muistia (suositus 8GB+):
- Käytä pilvipalvelun virtuaalikoneita resurssiintensiivisille oppitunneille
- Sulje muut sovellukset mallien koulutuksen aikana
- Pienennä eräkokoja muistikirjoissa, jos muisti loppuu

## Lisähuomioita

### Kurssin opettajille

- Katso `lessons/0-course-setup/for-teachers.md` opetusohjeita varten
- Oppitunnit ovat itsenäisiä ja niitä voidaan opettaa järjestyksessä tai valikoiden
- Arvioitu kesto: 12 viikkoa, 2 oppituntia viikossa

### Pilviresurssit

- **Azure for Students:** Ilmaisia krediittejä opiskelijoille
- **Microsoft Learn:** Täydentävät oppimispolut linkitetty oppituntien yhteydessä
- **Binder:** Ilmainen mutta rajalliset resurssit ja joitakin verkkorajoituksia

### Koodin suoritusvaihtoehdot

1. **Paikallinen (suositeltu):** Täysi hallinta, paras suorituskyky, GPU-tuki
2. **GitHub Codespaces:** Pilvipohjainen VS Code, hyvä nopeaan käyttöön
3. **Binder:** Selaimessa toimiva Jupyter, ilmainen mutta rajallinen
4. **Azure ML Notebooks:** Yrityskäyttö GPU-tuella
5. **Google Colab:** Lataa muistikirjat yksitellen, ilmainen GPU-taso saatavilla

### Työskentely muistikirjojen kanssa

- Muistikirjat on suunniteltu suoritettavaksi solu kerrallaan oppimista varten
- Monet muistikirjat lataavat datat ensimmäisellä suorituskerralla (voi kestää aikaa)
- Jotkut mallit vaativat GPU:n kohtuullisiin koulutusaikoihin
- Esikoulutetut mallit käytössä, missä mahdollista, laskentavaatimusten vähentämiseksi

### Suorituskykyhuomiot

- Myöhemmät tietokonenäköoppitunnit (CNN:t, GAN:t) hyötyvät GPU:sta
- NLP-transformer-oppitunnit voivat vaatia merkittävää RAM-muistia
- Koulutus alusta asti on opettavaista mutta aikaa vievää
- Siirto-oppimisen esimerkit minimoivat koulutusaikaa

---

**Vastuuvapauslauseke**:  
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, huomioithan, että automaattiset käännökset voivat sisältää virheitä tai epätarkkuuksia. Alkuperäistä asiakirjaa sen alkuperäisellä kielellä tulisi pitää ensisijaisena lähteenä. Kriittisen tiedon osalta suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa väärinkäsityksistä tai virhetulkinnoista, jotka johtuvat tämän käännöksen käytöstä.