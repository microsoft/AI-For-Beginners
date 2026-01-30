# Guide de dépannage pour AI-For-Beginners

Ce guide vous aide à résoudre les problèmes courants rencontrés lors de l'utilisation ou de la contribution au dépôt [AI-For-Beginners](https://github.com/microsoft/AI-For-Beginners). Chaque problème inclut des informations de base, des symptômes, des explications et des solutions étape par étape.

---

## Table des matières

- [Problèmes généraux](../..)
- [Problèmes d'installation](../..)
- [Problèmes de configuration](../..)
- [Exécution des notebooks](../..)
- [Problèmes de performance](../..)
- [Problèmes du site web du manuel](../..)
- [Problèmes de contribution](../..)
- [FAQ](../..)
- [Obtenir de l'aide](../..)

---

## Problèmes généraux

### 1. Le dépôt ne se clone pas correctement

**Contexte :** Le clonage vous permet de copier le dépôt sur votre machine.

**Symptômes :**
- Erreur : `fatal: repository not found`
- Erreur : `Permission denied (publickey)`

**Causes possibles :**
- URL du dépôt incorrecte
- Permissions insuffisantes
- Clés SSH non configurées

**Solutions :**
1. **Vérifiez l'URL du dépôt.**  
   Utilisez l'URL HTTPS :  
   ```
   git clone https://github.com/microsoft/AI-For-Beginners.git
   ```
2. **Passez à HTTPS si SSH échoue.**  
   Si vous voyez `Permission denied (publickey)`, utilisez le lien HTTPS ci-dessus au lieu de SSH.
3. **Configurez les clés SSH (optionnel).**  
   Si vous souhaitez utiliser SSH, suivez le [guide SSH de GitHub](https://docs.github.com/en/authentication/connecting-to-github-with-ssh).

---

## Problèmes d'installation

### 2. Problèmes avec l'environnement Python

**Contexte :** Le dépôt repose sur Python et diverses bibliothèques.

**Symptômes :**
- Erreur : `ModuleNotFoundError: No module named '<package>'`
- Erreurs d'importation lors de l'exécution des scripts ou notebooks

**Causes possibles :**
- Dépendances non installées
- Version Python incorrecte

**Solutions :**
1. **Configurez un environnement virtuel.**  
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```
2. **Installez les dépendances.**  
   ```bash
   pip install -r requirements.txt
   ```
3. **Vérifiez la version de Python.**  
   Utilisez Python 3.7 ou une version plus récente.  
   ```bash
   python --version
   ```

### 3. Jupyter n'est pas installé

**Contexte :** Les notebooks sont une ressource d'apprentissage essentielle.

**Symptômes :**
- Erreur : `jupyter: command not found`
- Les notebooks ne se lancent pas

**Causes possibles :**
- Jupyter n'est pas installé

**Solutions :**
1. **Installez Jupyter Notebook.**  
   ```bash
   pip install notebook
   ```
   ou, si vous utilisez Anaconda :
   ```bash
   conda install notebook
   ```
2. **Lancez Jupyter Notebook.**  
   ```bash
   jupyter notebook
   ```

### 4. Conflits de versions des dépendances

**Contexte :** Les projets peuvent être interrompus si les versions des packages ne correspondent pas.

**Symptômes :**
- Erreurs ou avertissements concernant des versions incompatibles

**Causes possibles :**
- Packages Python anciens ou en conflit

**Solutions :**
1. **Installez dans un environnement propre.**  
   Supprimez l'ancien venv/env conda et créez-en un nouveau.
2. **Utilisez des versions exactes.**  
   Exécutez toujours :
   ```bash
   pip install -r requirements.txt
   ```
   Si cela échoue, installez manuellement les packages manquants comme décrit dans le README.

---

## Problèmes de configuration

### 5. Variables d'environnement non définies

**Contexte :** Certains modules peuvent nécessiter des clés, des tokens ou des paramètres de configuration.

**Symptômes :**
- Erreur : `KeyError` ou avertissements concernant une configuration manquante

**Causes possibles :**
- Variables d'environnement requises non définies

**Solutions :**
1. **Vérifiez les fichiers `.env.example` ou similaires.**
2. **Créez un fichier `.env` et remplissez les valeurs requises.**
3. **Rechargez votre terminal ou IDE après avoir défini les variables d'environnement.**

---

## Exécution des notebooks

### 6. Le notebook ne s'ouvre pas ou ne s'exécute pas

**Contexte :** Les notebooks Jupyter nécessitent une configuration correcte.

**Symptômes :**
- Le notebook ne se lance pas
- Le navigateur ne s'ouvre pas automatiquement

**Causes possibles :**
- Jupyter n'est pas installé
- Problèmes de configuration du navigateur

**Solutions :**
1. **Installez Jupyter (voir Problèmes d'installation ci-dessus).**
2. **Ouvrez les notebooks manuellement.**
   - Copiez l'URL depuis le terminal (par ex., `http://localhost:8888/?token=...`) et collez-la dans votre navigateur.

### 7. Le kernel plante ou se fige

**Contexte :** Les kernels des notebooks peuvent planter en raison de limites de ressources ou d'erreurs de code.

**Symptômes :**
- Le kernel meurt ou redémarre continuellement
- Erreurs de mémoire insuffisante

**Causes possibles :**
- Jeux de données volumineux
- Code ou packages incompatibles

**Solutions :**
1. **Redémarrez le kernel.**  
   Utilisez le bouton "Restart Kernel" dans Jupyter.
2. **Vérifiez l'utilisation de la mémoire.**  
   Fermez les applications inutilisées.
3. **Exécutez les notebooks sur des plateformes cloud.**  
   Utilisez [Google Colab](https://colab.research.google.com/) ou [Azure Notebooks](https://notebooks.azure.com/).

---

## Problèmes de performance

### 8. Les notebooks s'exécutent lentement

**Contexte :** Certaines tâches d'IA nécessitent une mémoire et un processeur importants.

**Symptômes :**
- Exécution lente
- Ventilateur de l'ordinateur portable bruyant

**Causes possibles :**
- Jeux de données ou modèles volumineux
- Ressources système limitées

**Solutions :**
1. **Utilisez une plateforme cloud.**
   - Téléchargez le notebook sur Colab ou Azure Notebooks.
2. **Réduisez la taille du jeu de données.**
   - Utilisez des données d'échantillon pour vous entraîner.
3. **Fermez les programmes inutiles.**
   - Libérez la RAM du système.

---

## Problèmes du site web du manuel

### 9. Un chapitre ne se charge pas

**Contexte :** Le manuel en ligne affiche les leçons et chapitres.

**Symptômes :**
- Un chapitre (par ex., Transformers/BERT) est manquant ou ne s'ouvre pas

**Problème connu :**  
- [Problème #303](https://github.com/microsoft/AI-For-Beginners/issues/303) : “18 Transformers. BERT. ne peut pas être ouvert sur le site web du manuel.” Causé par une erreur de nom de fichier (`READMEtransformers.md` au lieu de `README.md`).

**Solutions :**
1. **Vérifiez les erreurs de renommage de fichiers.**  
   Si vous êtes contributeur, assurez-vous que les fichiers des chapitres sont nommés `README.md`.
2. **Signalez les fichiers manquants.**  
   Ouvrez un problème GitHub avec le nom du chapitre et les détails de l'erreur.

---

## Problèmes de contribution

### 10. La PR n'est pas acceptée ou les builds échouent

**Contexte :** Les contributions doivent passer des tests et respecter les directives.

**Symptômes :**
- Pull request rejetée
- Erreurs dans le pipeline CI/CD

**Causes possibles :**
- Tests échoués
- Non-respect des standards de codage

**Solutions :**
1. **Lisez les directives de contribution.**
   - Suivez le [CONTRIBUTING.md](https://github.com/microsoft/AI-For-Beginners/blob/main/CONTRIBUTING.md) du dépôt.
2. **Exécutez les tests localement avant de pousser.**
3. **Vérifiez les règles de linting ou les exigences de formatage.**

---

## FAQ

### Où puis-je trouver de l'aide pour des modules spécifiques ?
- Chaque module a généralement son propre README. Commencez par là pour des conseils de configuration et d'utilisation.

### Comment signaler un bug ou demander une fonctionnalité ?
- [Ouvrez un problème GitHub](https://github.com/microsoft/AI-For-Beginners/issues/new) avec une description claire et les étapes pour reproduire.

### Puis-je demander de l'aide si mon problème n'est pas listé ?
- Oui ! Recherchez d'abord les problèmes existants, et si vous ne trouvez pas votre problème, créez un nouveau problème.

---

## Obtenir de l'aide

- **Vérifiez les problèmes :** [GitHub Issues](https://github.com/microsoft/AI-For-Beginners/issues)
- **Posez des questions :** Utilisez les discussions GitHub ou ouvrez un problème.
- **Communauté :** Consultez les liens du dépôt pour les options de chat/forum.

---

_Dernière mise à jour : 20/09/2025_

---

**Avertissement** :  
Ce document a été traduit à l'aide du service de traduction automatique [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforcions d'assurer l'exactitude, veuillez noter que les traductions automatisées peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue d'origine doit être considéré comme la source faisant autorité. Pour des informations critiques, il est recommandé de recourir à une traduction humaine professionnelle. Nous déclinons toute responsabilité en cas de malentendus ou d'interprétations erronées résultant de l'utilisation de cette traduction.