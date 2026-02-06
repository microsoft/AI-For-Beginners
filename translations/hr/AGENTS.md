# AGENTS.md

## Pregled projekta

AI for Beginners je sveobuhvatan 12-tjedni, 24-lekcijski kurikulum koji pokriva osnove umjetne inteligencije. Ovaj edukacijski repozitorij uključuje praktične lekcije koristeći Jupyter Notebooks, kvizove i laboratorijske vježbe. Kurikulum obuhvaća:

- Simboličku AI s reprezentacijom znanja i ekspertnih sustava
- Neuronske mreže i duboko učenje s TensorFlowom i PyTorchom
- Tehnike i arhitekture računalnog vida
- Obradu prirodnog jezika (NLP), uključujući transformere i BERT
- Specijalizirane teme: genetski algoritmi, učenje pojačanjem, sustavi s više agenata
- Etičke principe AI i odgovornu umjetnu inteligenciju

**Ključne tehnologije:** Python 3, Jupyter Notebooks, TensorFlow, PyTorch, Keras, OpenCV, Vue.js (za aplikaciju kvizova)

**Arhitektura:** Edukacijski repozitorij sadržaja s Jupyter Notebooks organiziranim po tematskim područjima, dopunjen aplikacijom kvizova temeljenom na Vue.js i opsežnom podrškom za više jezika.

## Postavljanje okruženja

### Primarno razvojno okruženje (Python/Jupyter)

Kurikulum je dizajniran za rad s Pythonom i Jupyter Notebooks. Preporučeni pristup je korištenje miniconde:

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

### Alternativa: Korištenje devcontainer-a

```bash
# Open in VS Code and select "Reopen in Container" when prompted
# The devcontainer will automatically set up the environment
```

### Postavljanje aplikacije kvizova

Aplikacija kvizova je zasebna Vue.js aplikacija smještena u `etc/quiz-app/`:

```bash
cd etc/quiz-app
npm install
npm run serve  # Development server
npm run build  # Production build
npm run lint   # Lint and fix files
```

## Razvojni tijek rada

### Rad s Jupyter Notebooks

1. **Lokalni razvoj:**
   - Aktivirajte conda okruženje: `conda activate ai4beg`
   - Pokrenite Jupyter: `jupyter notebook` ili `jupyter lab`
   - Navigirajte do mapa s lekcijama i otvorite `.ipynb` datoteke
   - Interaktivno pokrenite ćelije kako biste pratili lekcije

2. **VS Code s Python ekstenzijom:**
   - Otvorite repozitorij u VS Code
   - Instalirajte Python ekstenziju
   - VS Code automatski detektira i koristi conda okruženje
   - Otvorite `.ipynb` datoteke direktno u VS Code

3. **Razvoj u oblaku:**
   - **GitHub Codespaces:** Kliknite "Code" → "Codespaces" → "Create codespace on main"
   - **Binder:** Koristite Binder značku u README za pokretanje u pregledniku
   - Napomena: Binder ima ograničene resurse i neka ograničenja pristupa internetu

### Podrška za GPU u naprednim lekcijama

Kasnije lekcije značajno koriste GPU akceleraciju:

- **Azure Data Science VM:** Koristite NC-serije VM-ova s podrškom za GPU
- **Azure Machine Learning:** Koristite značajke bilježnica s GPU računalom
- **Google Colab:** Pojedinačno učitajte bilježnice (ima besplatnu GPU podršku)

### Razvoj aplikacije kvizova

```bash
cd etc/quiz-app
npm run serve  # Hot-reload development server at http://localhost:8080
```

## Upute za testiranje

Ovo je edukacijski repozitorij fokusiran na sadržaj za učenje, a ne na testiranje softvera. Ne postoji tradicionalni testni paket.

### Pristupi validaciji:

1. **Jupyter Notebooks:** Izvršite ćelije redom kako biste provjerili da primjeri koda rade
2. **Testiranje aplikacije kvizova:** Ručno testiranje putem razvojnog servera
3. **Validacija prijevoda:** Provjerite prevedeni sadržaj u mapi `translations/`
4. **Linting aplikacije kvizova:** `npm run lint` u `etc/quiz-app/`

### Pokretanje primjera koda:

```bash
# Activate environment first
conda activate ai4beg

# Run Python scripts directly
python lessons/4-ComputerVision/07-ConvNets/pytorchcv.py

# Or execute notebooks
jupyter notebook lessons/3-NeuralNetworks/03-Perceptron/Perceptron.ipynb
```

## Stil kodiranja

### Stil Python koda

- Standardne Python konvencije za edukacijski kod
- Jasan, čitljiv kod koji prioritizira učenje nad optimizacijom
- Komentari koji objašnjavaju ključne koncepte
- Prilagođeno Jupyter Notebooku: ćelije trebaju biti samostalne gdje je moguće
- Nema stroge zahtjeve za linting sadržaja lekcija

### JavaScript/Vue.js (aplikacija kvizova)

- ESLint konfiguracija u `etc/quiz-app/package.json`
- Pokrenite `npm run lint` za provjeru i automatsko ispravljanje problema
- Konvencije Vue 2.x
- Arhitektura temeljena na komponentama

### Organizacija datoteka

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

## Izrada i implementacija

### Sadržaj Jupyter

Nije potreban proces izrade - Jupyter Notebooks se direktno izvršavaju.

### Aplikacija kvizova

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

### Dokumentacijska stranica

Repozitorij koristi Docsify za dokumentaciju:
- `index.html` služi kao ulazna točka
- Nije potrebna izrada - direktno se poslužuje putem GitHub Pages
- Pristupite na: https://microsoft.github.io/AI-For-Beginners/

## Smjernice za doprinos

### Proces Pull Requesta

1. **Format naslova:** Jasni, opisni naslovi koji opisuju promjenu
2. **Zahtjev za CLA:** Microsoft CLA mora biti potpisan (automatska provjera)
3. **Smjernice za sadržaj:**
   - Održavajte edukacijski fokus i pristup prilagođen početnicima
   - Testirajte sve primjere koda u bilježnicama
   - Osigurajte da bilježnice rade od početka do kraja
   - Ažurirajte prijevode ako mijenjate sadržaj na engleskom
4. **Promjene aplikacije kvizova:** Pokrenite `npm run lint` prije predaje

### Doprinos prijevodima

- Prijevodi se automatiziraju putem GitHub Actions koristeći co-op-translator
- Ručni prijevodi idu u `translations/<language-code>/`
- Prijevodi kvizova u `etc/quiz-app/src/assets/translations/`
- Podržani jezici: 40+ jezika (pogledajte README za potpuni popis)

### Aktivna područja doprinosa

Pogledajte `etc/CONTRIBUTING.md` za trenutne potrebe:
- Sekcije o dubokom učenju pojačanjem
- Poboljšanja u detekciji objekata
- Primjeri prepoznavanja imenovanih entiteta
- Uzorci za prilagođeno treniranje ugrađivanja

## Konfiguracija okruženja

### Potrebne ovisnosti

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

### Varijable okruženja

Nisu potrebne posebne varijable okruženja za osnovno korištenje.

Za implementaciju na Azureu (aplikacija kvizova):
- `AZURE_STATIC_WEB_APPS_API_TOKEN` (automatski postavlja Azure)

## Otklanjanje grešaka i rješavanje problema

### Uobičajeni problemi

**Problem:** Stvaranje conda okruženja ne uspijeva
- **Rješenje:** Prvo ažurirajte conda: `conda update conda -y`
- Osigurajte dovoljno prostora na disku (preporučeno 50GB)

**Problem:** Jupyter kernel nije pronađen
- **Rješenje:** 
  ```bash
  conda activate ai4beg
  python -m ipykernel install --user --name ai4beg
  ```

**Problem:** GPU nije detektiran u bilježnicama
- **Rješenje:** 
  - Provjerite instalaciju CUDA: `nvidia-smi`
  - Provjerite GPU u PyTorchu: `python -c "import torch; print(torch.cuda.is_available())"`
  - Provjerite GPU u TensorFlowu: `python -c "import tensorflow as tf; print(tf.config.list_physical_devices('GPU'))"`

**Problem:** Aplikacija kvizova se ne pokreće
- **Rješenje:**
  ```bash
  cd etc/quiz-app
  rm -rf node_modules package-lock.json
  npm install
  npm run serve
  ```

**Problem:** Binder se blokira ili prekida preuzimanja
- **Rješenje:** Koristite GitHub Codespaces ili lokalno postavljanje za bolji pristup resursima

### Problemi s memorijom

Neke lekcije zahtijevaju značajnu RAM memoriju (preporučeno 8GB+):
- Koristite VM-ove u oblaku za lekcije koje zahtijevaju puno resursa
- Zatvorite druge aplikacije tijekom treniranja modela
- Smanjite veličine batchova u bilježnicama ako ponestaje memorije

## Dodatne napomene

### Za instruktore tečaja

- Pogledajte `lessons/0-course-setup/for-teachers.md` za smjernice za podučavanje
- Lekcije su samostalne i mogu se podučavati redom ili odabrati pojedinačno
- Procijenjeno vrijeme: 12 tjedana s 2 lekcije tjedno

### Resursi u oblaku

- **Azure za studente:** Besplatni krediti dostupni studentima
- **Microsoft Learn:** Dopunski edukacijski putovi povezani kroz cijeli kurikulum
- **Binder:** Besplatno, ali s ograničenim resursima i nekim mrežnim ograničenjima

### Opcije za izvršavanje koda

1. **Lokalno (preporučeno):** Potpuna kontrola, najbolja izvedba, podrška za GPU
2. **GitHub Codespaces:** Cloud-based VS Code, dobro za brz pristup
3. **Binder:** Jupyter u pregledniku, besplatno ali ograničeno
4. **Azure ML Notebooks:** Enterprise opcija s podrškom za GPU
5. **Google Colab:** Pojedinačno učitajte bilježnice, dostupna besplatna GPU razina

### Rad s bilježnicama

- Bilježnice su dizajnirane za pokretanje ćeliju po ćeliju radi učenja
- Mnoge bilježnice preuzimaju skupove podataka pri prvom pokretanju (može potrajati)
- Neki modeli zahtijevaju GPU za razumno vrijeme treniranja
- Koriste se unaprijed trenirani modeli gdje je moguće kako bi se smanjili zahtjevi za računalom

### Razmatranja izvedbe

- Kasnije lekcije o računalnom vidu (CNN, GAN) koriste GPU
- Lekcije o NLP transformerima mogu zahtijevati značajnu RAM memoriju
- Treniranje od nule je edukativno, ali zahtijeva puno vremena
- Primjeri transfernog učenja minimiziraju vrijeme treniranja

---

**Izjava o odricanju odgovornosti**:  
Ovaj dokument je preveden pomoću AI usluge za prevođenje [Co-op Translator](https://github.com/Azure/co-op-translator). Iako nastojimo osigurati točnost, imajte na umu da automatski prijevodi mogu sadržavati pogreške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati autoritativnim izvorom. Za ključne informacije preporučuje se profesionalni prijevod od strane stručnjaka. Ne preuzimamo odgovornost za nesporazume ili pogrešne interpretacije koje mogu proizaći iz korištenja ovog prijevoda.