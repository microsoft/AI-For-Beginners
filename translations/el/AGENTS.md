# AGENTS.md

## Επισκόπηση Έργου

Το AI for Beginners είναι ένα ολοκληρωμένο πρόγραμμα σπουδών διάρκειας 12 εβδομάδων και 24 μαθημάτων που καλύπτει τις βασικές αρχές της Τεχνητής Νοημοσύνης. Αυτό το εκπαιδευτικό αποθετήριο περιλαμβάνει πρακτικά μαθήματα με χρήση Jupyter Notebooks, κουίζ και εργαστήρια. Το πρόγραμμα σπουδών καλύπτει:

- Συμβολική Τεχνητή Νοημοσύνη με Αναπαράσταση Γνώσης και Εξειδικευμένα Συστήματα
- Νευρωνικά Δίκτυα και Βαθιά Μάθηση με TensorFlow και PyTorch
- Τεχνικές και αρχιτεκτονικές Υπολογιστικής Όρασης
- Επεξεργασία Φυσικής Γλώσσας (NLP), συμπεριλαμβανομένων των transformers και BERT
- Εξειδικευμένα θέματα: Γενετικοί Αλγόριθμοι, Ενισχυτική Μάθηση, Πολυπρακτορικά Συστήματα
- Ηθική της Τεχνητής Νοημοσύνης και αρχές Υπεύθυνης Τεχνητής Νοημοσύνης

**Κύριες Τεχνολογίες:** Python 3, Jupyter Notebooks, TensorFlow, PyTorch, Keras, OpenCV, Vue.js (για την εφαρμογή κουίζ)

**Αρχιτεκτονική:** Εκπαιδευτικό αποθετήριο περιεχομένου με Jupyter Notebooks οργανωμένα ανά θεματική ενότητα, συμπληρωμένα από μια εφαρμογή κουίζ βασισμένη στο Vue.js και εκτεταμένη υποστήριξη πολλών γλωσσών.

## Εντολές Ρύθμισης

### Κύριο Περιβάλλον Ανάπτυξης (Python/Jupyter)

Το πρόγραμμα σπουδών έχει σχεδιαστεί για να λειτουργεί με Python και Jupyter Notebooks. Η προτεινόμενη προσέγγιση είναι η χρήση του miniconda:

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

### Εναλλακτική: Χρήση devcontainer

```bash
# Open in VS Code and select "Reopen in Container" when prompted
# The devcontainer will automatically set up the environment
```

### Ρύθμιση Εφαρμογής Κουίζ

Η εφαρμογή κουίζ είναι μια ξεχωριστή εφαρμογή Vue.js που βρίσκεται στο `etc/quiz-app/`:

```bash
cd etc/quiz-app
npm install
npm run serve  # Development server
npm run build  # Production build
npm run lint   # Lint and fix files
```

## Ροή Εργασίας Ανάπτυξης

### Εργασία με Jupyter Notebooks

1. **Τοπική Ανάπτυξη:**
   - Ενεργοποιήστε το περιβάλλον conda: `conda activate ai4beg`
   - Ξεκινήστε το Jupyter: `jupyter notebook` ή `jupyter lab`
   - Μεταβείτε στους φακέλους μαθημάτων και ανοίξτε αρχεία `.ipynb`
   - Εκτελέστε τα κελιά διαδραστικά για να ακολουθήσετε τα μαθήματα

2. **VS Code με Επέκταση Python:**
   - Ανοίξτε το αποθετήριο στο VS Code
   - Εγκαταστήστε την επέκταση Python
   - Το VS Code ανιχνεύει και χρησιμοποιεί αυτόματα το περιβάλλον conda
   - Ανοίξτε αρχεία `.ipynb` απευθείας στο VS Code

3. **Ανάπτυξη στο Cloud:**
   - **GitHub Codespaces:** Κάντε κλικ στο "Code" → "Codespaces" → "Create codespace on main"
   - **Binder:** Χρησιμοποιήστε το σήμα Binder στο README για εκκίνηση στον περιηγητή
   - Σημείωση: Το Binder έχει περιορισμένους πόρους και κάποιους περιορισμούς πρόσβασης στο διαδίκτυο

### Υποστήριξη GPU για Προχωρημένα Μαθήματα

Τα μεταγενέστερα μαθήματα επωφελούνται σημαντικά από την επιτάχυνση GPU:

- **Azure Data Science VM:** Χρησιμοποιήστε VMs της σειράς NC με υποστήριξη GPU
- **Azure Machine Learning:** Χρησιμοποιήστε δυνατότητες notebook με υπολογιστική GPU
- **Google Colab:** Ανεβάστε notebooks μεμονωμένα (παρέχει δωρεάν υποστήριξη GPU)

### Ανάπτυξη Εφαρμογής Κουίζ

```bash
cd etc/quiz-app
npm run serve  # Hot-reload development server at http://localhost:8080
```

## Οδηγίες Δοκιμής

Αυτό είναι ένα εκπαιδευτικό αποθετήριο που επικεντρώνεται στο περιεχόμενο μάθησης και όχι στη δοκιμή λογισμικού. Δεν υπάρχει παραδοσιακή σουίτα δοκιμών.

### Προσεγγίσεις Επικύρωσης:

1. **Jupyter Notebooks:** Εκτελέστε τα κελιά διαδοχικά για να επαληθεύσετε ότι τα παραδείγματα κώδικα λειτουργούν
2. **Δοκιμή Εφαρμογής Κουίζ:** Χειροκίνητη δοκιμή μέσω διακομιστή ανάπτυξης
3. **Επικύρωση Μεταφράσεων:** Ελέγξτε το μεταφρασμένο περιεχόμενο στον φάκελο `translations/`
4. **Linting Εφαρμογής Κουίζ:** `npm run lint` στο `etc/quiz-app/`

### Εκτέλεση Παραδειγμάτων Κώδικα:

```bash
# Activate environment first
conda activate ai4beg

# Run Python scripts directly
python lessons/4-ComputerVision/07-ConvNets/pytorchcv.py

# Or execute notebooks
jupyter notebook lessons/3-NeuralNetworks/03-Perceptron/Perceptron.ipynb
```

## Στυλ Κώδικα

### Στυλ Κώδικα Python

- Τυπικές συμβάσεις Python για εκπαιδευτικό κώδικα
- Καθαρός, ευανάγνωστος κώδικας που δίνει προτεραιότητα στη μάθηση αντί στη βελτιστοποίηση
- Σχόλια που εξηγούν βασικές έννοιες
- Φιλικό προς Jupyter Notebook: τα κελιά πρέπει να είναι όσο το δυνατόν πιο αυτοτελή
- Δεν απαιτούνται αυστηρές απαιτήσεις linting για το περιεχόμενο των μαθημάτων

### JavaScript/Vue.js (Εφαρμογή Κουίζ)

- Ρύθμιση ESLint στο `etc/quiz-app/package.json`
- Εκτελέστε `npm run lint` για έλεγχο και αυτόματη διόρθωση προβλημάτων
- Συμβάσεις Vue 2.x
- Αρχιτεκτονική βασισμένη σε components

### Οργάνωση Αρχείων

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

## Δημιουργία και Ανάπτυξη

### Περιεχόμενο Jupyter

Δεν απαιτείται διαδικασία δημιουργίας - τα Jupyter Notebooks εκτελούνται απευθείας.

### Εφαρμογή Κουίζ

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

### Ιστότοπος Τεκμηρίωσης

Το αποθετήριο χρησιμοποιεί το Docsify για τεκμηρίωση:
- Το `index.html` λειτουργεί ως σημείο εισόδου
- Δεν απαιτείται δημιουργία - εξυπηρετείται απευθείας μέσω GitHub Pages
- Πρόσβαση στο: https://microsoft.github.io/AI-For-Beginners/

## Οδηγίες Συνεισφοράς

### Διαδικασία Pull Request

1. **Μορφή Τίτλου:** Καθαροί, περιγραφικοί τίτλοι που περιγράφουν την αλλαγή
2. **Απαίτηση CLA:** Πρέπει να υπογραφεί το Microsoft CLA (αυτόματος έλεγχος)
3. **Οδηγίες Περιεχομένου:**
   - Διατηρήστε την εκπαιδευτική εστίαση και την προσέγγιση φιλική προς αρχάριους
   - Δοκιμάστε όλα τα παραδείγματα κώδικα στα notebooks
   - Βεβαιωθείτε ότι τα notebooks εκτελούνται από την αρχή μέχρι το τέλος
   - Ενημερώστε τις μεταφράσεις αν τροποποιήσετε το αγγλικό περιεχόμενο
4. **Αλλαγές Εφαρμογής Κουίζ:** Εκτελέστε `npm run lint` πριν από τη δέσμευση

### Συνεισφορές Μεταφράσεων

- Οι μεταφράσεις γίνονται αυτόματα μέσω GitHub Actions χρησιμοποιώντας το co-op-translator
- Χειροκίνητες μεταφράσεις τοποθετούνται στο `translations/<language-code>/`
- Μεταφράσεις κουίζ στο `etc/quiz-app/src/assets/translations/`
- Υποστηριζόμενες γλώσσες: 40+ γλώσσες (δείτε το README για πλήρη λίστα)

### Ενεργές Περιοχές Συνεισφοράς

Δείτε το `etc/CONTRIBUTING.md` για τις τρέχουσες ανάγκες:
- Ενότητες Βαθιάς Ενισχυτικής Μάθησης
- Βελτιώσεις Ανίχνευσης Αντικειμένων
- Παραδείγματα Αναγνώρισης Οντοτήτων
- Δείγματα εκπαίδευσης προσαρμοσμένων embeddings

## Ρύθμιση Περιβάλλοντος

### Απαιτούμενες Εξαρτήσεις

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

### Μεταβλητές Περιβάλλοντος

Δεν απαιτούνται ειδικές μεταβλητές περιβάλλοντος για βασική χρήση.

Για αναπτύξεις στο Azure (εφαρμογή κουίζ):
- `AZURE_STATIC_WEB_APPS_API_TOKEN` (ορίζεται αυτόματα από το Azure)

## Εντοπισμός Σφαλμάτων και Αντιμετώπιση Προβλημάτων

### Συνηθισμένα Προβλήματα

**Πρόβλημα:** Αποτυχία δημιουργίας περιβάλλοντος conda
- **Λύση:** Ενημερώστε πρώτα το conda: `conda update conda -y`
- Βεβαιωθείτε ότι υπάρχει αρκετός χώρος στο δίσκο (συνιστώνται 50GB)

**Πρόβλημα:** Δεν βρέθηκε πυρήνας Jupyter
- **Λύση:** 
  ```bash
  conda activate ai4beg
  python -m ipykernel install --user --name ai4beg
  ```

**Πρόβλημα:** Η GPU δεν ανιχνεύεται στα notebooks
- **Λύση:** 
  - Επαληθεύστε την εγκατάσταση CUDA: `nvidia-smi`
  - Ελέγξτε την GPU του PyTorch: `python -c "import torch; print(torch.cuda.is_available())"`
  - Ελέγξτε την GPU του TensorFlow: `python -c "import tensorflow as tf; print(tf.config.list_physical_devices('GPU'))"`

**Πρόβλημα:** Η εφαρμογή κουίζ δεν ξεκινά
- **Λύση:**
  ```bash
  cd etc/quiz-app
  rm -rf node_modules package-lock.json
  npm install
  npm run serve
  ```

**Πρόβλημα:** Το Binder λήγει ή μπλοκάρει λήψεις
- **Λύση:** Χρησιμοποιήστε το GitHub Codespaces ή τοπική ρύθμιση για καλύτερη πρόσβαση σε πόρους

### Προβλήματα Μνήμης

Ορισμένα μαθήματα απαιτούν σημαντική RAM (συνιστώνται 8GB+):
- Χρησιμοποιήστε cloud VMs για μαθήματα που απαιτούν πολλούς πόρους
- Κλείστε άλλες εφαρμογές κατά την εκπαίδευση μοντέλων
- Μειώστε τα μεγέθη παρτίδων στα notebooks αν εξαντλείται η μνήμη

## Πρόσθετες Σημειώσεις

### Για Εκπαιδευτές Μαθημάτων

- Δείτε το `lessons/0-course-setup/for-teachers.md` για οδηγίες διδασκαλίας
- Τα μαθήματα είναι αυτοτελή και μπορούν να διδαχθούν με τη σειρά ή να επιλεγούν μεμονωμένα
- Εκτιμώμενος χρόνος: 12 εβδομάδες με 2 μαθήματα ανά εβδομάδα

### Πόροι Cloud

- **Azure for Students:** Διαθέσιμες δωρεάν πιστώσεις για φοιτητές
- **Microsoft Learn:** Συμπληρωματικά μονοπάτια μάθησης συνδεδεμένα καθ' όλη τη διάρκεια
- **Binder:** Δωρεάν αλλά με περιορισμένους πόρους και κάποιους περιορισμούς δικτύου

### Επιλογές Εκτέλεσης Κώδικα

1. **Τοπικά (Συνιστάται):** Πλήρης έλεγχος, καλύτερη απόδοση, υποστήριξη GPU
2. **GitHub Codespaces:** Cloud-based VS Code, καλό για γρήγορη πρόσβαση
3. **Binder:** Jupyter βασισμένο στον περιηγητή, δωρεάν αλλά περιορισμένο
4. **Azure ML Notebooks:** Επιχειρηματική επιλογή με υποστήριξη GPU
5. **Google Colab:** Ανεβάστε notebooks μεμονωμένα, διαθέσιμη δωρεάν GPU

### Εργασία με Notebooks

- Τα notebooks έχουν σχεδιαστεί για εκτέλεση κελιού-κελιού για μάθηση
- Πολλά notebooks κατεβάζουν σύνολα δεδομένων κατά την πρώτη εκτέλεση (μπορεί να χρειαστεί χρόνος)
- Ορισμένα μοντέλα απαιτούν GPU για λογικούς χρόνους εκπαίδευσης
- Χρησιμοποιούνται προεκπαιδευμένα μοντέλα όπου είναι δυνατόν για μείωση των απαιτήσεων υπολογισμού

### Σκέψεις Απόδοσης

- Τα μεταγενέστερα μαθήματα υπολογιστικής όρασης (CNNs, GANs) επωφελούνται από GPU
- Τα μαθήματα NLP με transformers μπορεί να απαιτούν σημαντική RAM
- Η εκπαίδευση από την αρχή είναι εκπαιδευτική αλλά χρονοβόρα
- Τα παραδείγματα μεταφοράς μάθησης ελαχιστοποιούν τον χρόνο εκπαίδευσης

---

**Αποποίηση Ευθύνης**:  
Αυτό το έγγραφο έχει μεταφραστεί χρησιμοποιώντας την υπηρεσία αυτόματης μετάφρασης [Co-op Translator](https://github.com/Azure/co-op-translator). Παρόλο που καταβάλλουμε προσπάθειες για ακρίβεια, παρακαλούμε να γνωρίζετε ότι οι αυτόματες μεταφράσεις ενδέχεται να περιέχουν λάθη ή ανακρίβειες. Το πρωτότυπο έγγραφο στη μητρική του γλώσσα θα πρέπει να θεωρείται η αυθεντική πηγή. Για κρίσιμες πληροφορίες, συνιστάται επαγγελματική ανθρώπινη μετάφραση. Δεν φέρουμε ευθύνη για τυχόν παρεξηγήσεις ή εσφαλμένες ερμηνείες που προκύπτουν από τη χρήση αυτής της μετάφρασης.