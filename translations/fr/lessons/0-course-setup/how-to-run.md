# Comment exécuter le code

Ce programme contient beaucoup d’exemples exécutables et de travaux pratiques que vous voudrez exécuter. Pour ce faire, vous avez besoin de pouvoir exécuter du code Python dans les notebooks Jupyter fournis dans le cadre de ce programme. Vous disposez de plusieurs options pour exécuter le code :

## Exécuter localement sur votre ordinateur

Pour exécuter le code localement sur votre ordinateur, une installation de Python est nécessaire. Une recommandation est d’installer **[miniconda](https://conda.io/en/latest/miniconda.html)** – c’est une installation plutôt légère qui supporte le gestionnaire de paquets `conda` pour différents **environnements virtuels** Python.

Après avoir installé miniconda, clonez le dépôt et créez un environnement virtuel à utiliser pour ce cours :

```bash
git clone http://github.com/microsoft/ai-for-beginners
cd ai-for-beginners
conda env create --name ai4beg --file .devcontainer/environment.yml
conda activate ai4beg
```

### Utilisation de Visual Studio Code avec l'extension Python

Ce programme est mieux utilisé en l’ouvrant dans [Visual Studio Code](http://code.visualstudio.com/?WT.mc_id=academic-77998-cacaste) avec l’[extension Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-77998-cacaste).

> **Note** : Une fois que vous avez cloné et ouvert le répertoire dans VS Code, il vous suggérera automatiquement d’installer les extensions Python. Vous devrez également installer miniconda comme décrit ci-dessus.

> **Note** : Si VS Code vous suggère de rouvrir le dépôt dans un conteneur, vous devriez refuser cela pour utiliser l’installation Python locale.

### Utilisation de Jupyter dans le navigateur

Vous pouvez aussi utiliser un environnement Jupyter depuis le navigateur sur votre propre ordinateur. À la fois Jupyter classique et JupyterHub fournissent un environnement de développement pratique avec autocomplétion, coloration syntaxique, etc.

Pour démarrer Jupyter localement, allez dans le répertoire du cours et exécutez :

```bash
jupyter notebook
```
ou
```bash
jupyterhub
```
Vous pouvez alors naviguer vers n’importe lequel des fichiers `.ipynb`, les ouvrir et commencer à travailler.

### Exécution dans un conteneur

Une alternative à l’installation de Python serait d’exécuter le code dans un conteneur. Puisque notre dépôt fournit un dossier spécial `.devcontainer` qui indique comment construire un conteneur pour ce dépôt, VS Code offre la possibilité de rouvrir le code dans un conteneur. Cela nécessitera l’installation de Docker, et serait aussi plus complexe, c’est pourquoi nous recommandons cela aux utilisateurs plus expérimentés.

## Exécution dans le cloud

Si vous ne souhaitez pas installer Python localement et avez accès à des ressources cloud, une bonne alternative serait d’exécuter le code dans le cloud. Plusieurs options s’offrent à vous :

* Utilisation de **[GitHub Codespaces](https://github.com/features/codespaces)**, qui est un environnement virtuel créé pour vous sur GitHub, accessible via une interface VS Code dans le navigateur. Si vous avez accès à Codespaces, vous pouvez simplement cliquer sur le bouton **Code** dans le dépôt, démarrer un codespace et vous lancer en un rien de temps.
* Utilisation de **[Binder](https://mybinder.org/v2/gh/microsoft/ai-for-beginners/HEAD)**. [Binder](https://mybinder.org) offre des ressources informatiques gratuites fournies dans le cloud pour permettre à des personnes comme vous de tester du code sur GitHub. Il y a un bouton sur la page d’accueil pour ouvrir le dépôt dans Binder – cela devrait rapidement vous amener sur le site de Binder, qui construira un conteneur sous-jacent et lancera une interface web Jupyter pour vous de manière transparente.

> **Note** : Pour éviter les abus, Binder a bloqué l’accès à certaines ressources web. Cela peut empêcher certains codes de fonctionner, notamment ceux qui téléchargent des modèles et/ou jeux de données depuis Internet public. Vous devrez peut-être trouver des solutions de contournement. En outre, les ressources de calcul fournies par Binder sont assez basiques, donc l’entraînement sera lent, surtout dans les leçons plus avancées et complexes.

## Exécution dans le cloud avec GPU

Certaines leçons avancées de ce programme bénéficieraient grandement du support GPU. L’entraînement de modèles, par exemple, peut être très lent autrement. Vous pouvez suivre quelques options, surtout si vous avez accès au cloud via [Azure for Students](https://azure.microsoft.com/free/students/?WT.mc_id=academic-77998-cacaste) ou via votre institution :

* Créez une [Machine virtuelle Data Science](https://docs.microsoft.com/learn/modules/intro-to-azure-data-science-virtual-machine/?WT.mc_id=academic-77998-cacaste) et connectez-vous à celle-ci via Jupyter. Vous pourrez alors cloner le dépôt directement sur la machine et commencer à apprendre. Les machines virtuelles série NC offrent un support GPU.

> **Note** : Certains abonnements, y compris Azure for Students, ne fournissent pas nativement de support GPU. Vous devrez peut-être demander des cœurs GPU supplémentaires via une demande de support technique.

* Créez un [Espace de travail Azure Machine Learning](https://azure.microsoft.com/services/machine-learning/?WT.mc_id=academic-77998-cacaste) puis utilisez la fonctionnalité Notebook. [Cette vidéo](https://azure-for-academics.github.io/quickstart/azureml-papers/) montre comment cloner un dépôt dans un notebook Azure ML et commencer à l’utiliser.

Vous pouvez aussi utiliser Google Colab, qui offre un support GPU gratuit, et y téléverser vos notebooks Jupyter pour les exécuter un par un.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Clause de non-responsabilité** :  
Ce document a été traduit à l’aide du service de traduction automatique [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforcions d’assurer l’exactitude, veuillez noter que les traductions automatiques peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue d’origine doit être considéré comme la source officielle. Pour les informations critiques, une traduction professionnelle réalisée par un humain est recommandée. Nous ne pouvons être tenus responsables des malentendus ou des erreurs d’interprétation résultant de l’utilisation de cette traduction.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->