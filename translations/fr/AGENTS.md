# AGENTS.md

## Aperçu du projet

AI for Beginners est un programme éducatif complet de 12 semaines et 24 leçons couvrant les fondamentaux de l'intelligence artificielle. Ce dépôt éducatif inclut des leçons pratiques utilisant des Jupyter Notebooks, des quiz et des laboratoires interactifs. Le programme aborde :

- L'IA symbolique avec la représentation des connaissances et les systèmes experts
- Les réseaux neuronaux et l'apprentissage profond avec TensorFlow et PyTorch
- Les techniques et architectures de vision par ordinateur
- Le traitement du langage naturel (NLP), y compris les transformers et BERT
- Des sujets spécialisés : algorithmes génétiques, apprentissage par renforcement, systèmes multi-agents
- L'éthique de l'IA et les principes d'une IA responsable

**Technologies clés :** Python 3, Jupyter Notebooks, TensorFlow, PyTorch, Keras, OpenCV, Vue.js (pour l'application de quiz)

**Architecture :** Dépôt de contenu éducatif avec des Jupyter Notebooks organisés par domaines thématiques, complété par une application de quiz basée sur Vue.js et un support multilingue étendu.

## Commandes d'installation

### Environnement de développement principal (Python/Jupyter)

Le programme est conçu pour fonctionner avec Python et Jupyter Notebooks. L'approche recommandée est d'utiliser miniconda :

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

### Alternative : Utilisation de devcontainer

```bash
# Open in VS Code and select "Reopen in Container" when prompted
# The devcontainer will automatically set up the environment
```

### Configuration de l'application de quiz

L'application de quiz est une application Vue.js distincte située dans `etc/quiz-app/` :

```bash
cd etc/quiz-app
npm install
npm run serve  # Development server
npm run build  # Production build
npm run lint   # Lint and fix files
```

## Flux de développement

### Travailler avec les Jupyter Notebooks

1. **Développement local :**
   - Activez l'environnement conda : `conda activate ai4beg`
   - Lancez Jupyter : `jupyter notebook` ou `jupyter lab`
   - Naviguez dans les dossiers de leçons et ouvrez les fichiers `.ipynb`
   - Exécutez les cellules de manière interactive pour suivre les leçons

2. **VS Code avec l'extension Python :**
   - Ouvrez le dépôt dans VS Code
   - Installez l'extension Python
   - VS Code détecte et utilise automatiquement l'environnement conda
   - Ouvrez les fichiers `.ipynb` directement dans VS Code

3. **Développement dans le cloud :**
   - **GitHub Codespaces :** Cliquez sur "Code" → "Codespaces" → "Create codespace on main"
   - **Binder :** Utilisez le badge Binder dans le README pour lancer dans le navigateur
   - Remarque : Binder dispose de ressources limitées et de certaines restrictions d'accès web

### Support GPU pour les leçons avancées

Les leçons ultérieures bénéficient grandement de l'accélération GPU :

- **Azure Data Science VM :** Utilisez des machines virtuelles NC-series avec support GPU
- **Azure Machine Learning :** Utilisez les fonctionnalités de notebook avec des ressources GPU
- **Google Colab :** Téléchargez les notebooks individuellement (support GPU gratuit disponible)

### Développement de l'application de quiz

```bash
cd etc/quiz-app
npm run serve  # Hot-reload development server at http://localhost:8080
```

## Instructions de test

Ce dépôt éducatif est axé sur le contenu d'apprentissage plutôt que sur les tests logiciels. Il n'y a pas de suite de tests traditionnelle.

### Approches de validation :

1. **Jupyter Notebooks :** Exécutez les cellules séquentiellement pour vérifier que les exemples de code fonctionnent
2. **Test de l'application de quiz :** Test manuel via le serveur de développement
3. **Validation des traductions :** Vérifiez le contenu traduit dans le dossier `translations/`
4. **Linting de l'application de quiz :** `npm run lint` dans `etc/quiz-app/`

### Exécution des exemples de code :

```bash
# Activate environment first
conda activate ai4beg

# Run Python scripts directly
python lessons/4-ComputerVision/07-ConvNets/pytorchcv.py

# Or execute notebooks
jupyter notebook lessons/3-NeuralNetworks/03-Perceptron/Perceptron.ipynb
```

## Style de code

### Style de code Python

- Conventions Python standard pour le code éducatif
- Code clair et lisible, privilégiant l'apprentissage à l'optimisation
- Commentaires expliquant les concepts clés
- Compatible avec Jupyter Notebook : les cellules doivent être aussi autonomes que possible
- Pas d'exigences strictes de linting pour le contenu des leçons

### JavaScript/Vue.js (Application de quiz)

- Configuration ESLint dans `etc/quiz-app/package.json`
- Exécutez `npm run lint` pour vérifier et corriger automatiquement les problèmes
- Conventions Vue 2.x
- Architecture basée sur les composants

### Organisation des fichiers

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

## Construction et déploiement

### Contenu Jupyter

Aucun processus de construction requis - les Jupyter Notebooks sont exécutés directement.

### Application de quiz

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

### Site de documentation

Le dépôt utilise Docsify pour la documentation :
- `index.html` sert de point d'entrée
- Aucun processus de construction requis - servi directement via GitHub Pages
- Accessible à : https://microsoft.github.io/AI-For-Beginners/

## Directives de contribution

### Processus de pull request

1. **Format du titre :** Titres clairs et descriptifs décrivant le changement
2. **Exigence CLA :** Le CLA de Microsoft doit être signé (vérification automatisée)
3. **Directives de contenu :**
   - Maintenir un focus éducatif et une approche adaptée aux débutants
   - Tester tous les exemples de code dans les notebooks
   - S'assurer que les notebooks s'exécutent de bout en bout
   - Mettre à jour les traductions si le contenu en anglais est modifié
4. **Modifications de l'application de quiz :** Exécutez `npm run lint` avant de valider

### Contributions aux traductions

- Les traductions sont automatisées via GitHub Actions en utilisant co-op-translator
- Les traductions manuelles vont dans `translations/<language-code>/`
- Traductions des quiz dans `etc/quiz-app/src/assets/translations/`
- Langues prises en charge : plus de 40 langues (voir README pour la liste complète)

### Domaines de contribution actifs

Voir `etc/CONTRIBUTING.md` pour les besoins actuels :
- Sections sur l'apprentissage par renforcement profond
- Améliorations de la détection d'objets
- Exemples de reconnaissance d'entités nommées
- Échantillons d'entraînement d'embeddings personnalisés

## Configuration de l'environnement

### Dépendances requises

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

### Variables d'environnement

Aucune variable d'environnement spéciale requise pour une utilisation de base.

Pour les déploiements Azure (application de quiz) :
- `AZURE_STATIC_WEB_APPS_API_TOKEN` (défini automatiquement par Azure)

## Débogage et dépannage

### Problèmes courants

**Problème :** Échec de la création de l'environnement conda
- **Solution :** Mettez à jour conda d'abord : `conda update conda -y`
- Assurez-vous d'avoir suffisamment d'espace disque (50 Go recommandés)

**Problème :** Le noyau Jupyter est introuvable
- **Solution :** 
  ```bash
  conda activate ai4beg
  python -m ipykernel install --user --name ai4beg
  ```

**Problème :** GPU non détecté dans les notebooks
- **Solution :** 
  - Vérifiez l'installation de CUDA : `nvidia-smi`
  - Vérifiez le GPU avec PyTorch : `python -c "import torch; print(torch.cuda.is_available())"`
  - Vérifiez le GPU avec TensorFlow : `python -c "import tensorflow as tf; print(tf.config.list_physical_devices('GPU'))"`

**Problème :** L'application de quiz ne démarre pas
- **Solution :**
  ```bash
  cd etc/quiz-app
  rm -rf node_modules package-lock.json
  npm install
  npm run serve
  ```

**Problème :** Binder expire ou bloque les téléchargements
- **Solution :** Utilisez GitHub Codespaces ou une configuration locale pour un meilleur accès aux ressources

### Problèmes de mémoire

Certaines leçons nécessitent une RAM importante (8 Go+ recommandés) :
- Utilisez des machines virtuelles cloud pour les leçons gourmandes en ressources
- Fermez d'autres applications lors de l'entraînement des modèles
- Réduisez les tailles de lot dans les notebooks si vous manquez de mémoire

## Notes supplémentaires

### Pour les instructeurs du cours

- Consultez `lessons/0-course-setup/for-teachers.md` pour des conseils pédagogiques
- Les leçons sont autonomes et peuvent être enseignées dans l'ordre ou sélectionnées individuellement
- Temps estimé : 12 semaines à raison de 2 leçons par semaine

### Ressources cloud

- **Azure for Students :** Crédits gratuits disponibles pour les étudiants
- **Microsoft Learn :** Parcours d'apprentissage complémentaires liés tout au long du programme
- **Binder :** Gratuit mais avec des ressources limitées et certaines restrictions réseau

### Options d'exécution du code

1. **Local (recommandé) :** Contrôle total, meilleures performances, support GPU
2. **GitHub Codespaces :** VS Code basé sur le cloud, idéal pour un accès rapide
3. **Binder :** Jupyter basé sur le navigateur, gratuit mais limité
4. **Azure ML Notebooks :** Option d'entreprise avec support GPU
5. **Google Colab :** Téléchargez les notebooks individuellement, GPU gratuit disponible

### Travailler avec les notebooks

- Les notebooks sont conçus pour être exécutés cellule par cellule pour l'apprentissage
- De nombreux notebooks téléchargent des ensembles de données lors de la première exécution (cela peut prendre du temps)
- Certains modèles nécessitent un GPU pour des temps d'entraînement raisonnables
- Des modèles pré-entraînés sont utilisés autant que possible pour réduire les besoins en calcul

### Considérations de performance

- Les leçons avancées en vision par ordinateur (CNN, GAN) bénéficient d'un GPU
- Les leçons sur les transformers NLP peuvent nécessiter une RAM importante
- L'entraînement à partir de zéro est éducatif mais chronophage
- Les exemples de transfert d'apprentissage minimisent le temps d'entraînement

---

**Avertissement** :  
Ce document a été traduit à l'aide du service de traduction automatique [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforcions d'assurer l'exactitude, veuillez noter que les traductions automatisées peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue d'origine doit être considéré comme la source faisant autorité. Pour des informations critiques, il est recommandé de recourir à une traduction humaine professionnelle. Nous déclinons toute responsabilité en cas de malentendus ou d'interprétations erronées résultant de l'utilisation de cette traduction.