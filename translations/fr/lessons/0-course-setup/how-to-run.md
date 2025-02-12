# Comment exécuter le code

Ce programme contient de nombreux exemples exécutables et laboratoires que vous souhaiterez exécuter. Pour ce faire, vous devez pouvoir exécuter du code Python dans des Jupyter Notebooks fournis dans le cadre de ce programme. Vous avez plusieurs options pour exécuter le code :

## Exécuter localement sur votre ordinateur

Pour exécuter le code localement sur votre ordinateur, vous devez avoir une version de Python installée. Je recommande personnellement d'installer **[miniconda](https://conda.io/en/latest/miniconda.html)** - c'est une installation plutôt légère qui prend en charge le gestionnaire de paquets `conda` pour différents **environnements virtuels** Python.

Après avoir installé miniconda, vous devez cloner le dépôt et créer un environnement virtuel à utiliser pour ce cours :

```bash
git clone http://github.com/microsoft/ai-for-beginners
cd ai-for-beginners
conda env create --name ai4beg --file .devcontainer/environment.yml
conda activate ai4beg
```

### Utiliser Visual Studio Code avec l'extension Python

Probablement la meilleure façon d'utiliser le programme est de l'ouvrir dans [Visual Studio Code](http://code.visualstudio.com/?WT.mc_id=academic-77998-cacaste) avec l'[extension Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-77998-cacaste).

> **Note** : Une fois que vous avez cloné et ouvert le répertoire dans VS Code, il vous suggérera automatiquement d'installer les extensions Python. Vous devrez également installer miniconda comme décrit ci-dessus.

> **Note** : Si VS Code vous suggère de réouvrir le dépôt dans un conteneur, vous devez refuser cela pour utiliser l'installation Python locale.

### Utiliser Jupyter dans le navigateur

Vous pouvez également utiliser l'environnement Jupyter directement depuis le navigateur sur votre propre ordinateur. En fait, à la fois Jupyter classique et Jupyter Hub offrent un environnement de développement assez pratique avec autocomplétion, mise en surbrillance du code, etc.

Pour démarrer Jupyter localement, allez dans le répertoire du cours et exécutez :

```bash
jupyter notebook
```
ou
```bash
jupyterhub
```
Vous pouvez ensuite naviguer vers n'importe quel dossier `.ipynb` files, open them and start working.

### Running in container

One alternative to Python installation would be to run the code in container. Since our repository contains special `.devcontainer` qui explique comment construire un conteneur pour ce dépôt. VS Code vous proposera de réouvrir le code dans un conteneur. Cela nécessitera l'installation de Docker, et sera également plus complexe, donc nous recommandons cela aux utilisateurs plus expérimentés.

## Exécution dans le Cloud

Si vous ne souhaitez pas installer Python localement, et que vous avez accès à des ressources cloud - une bonne alternative serait d'exécuter le code dans le cloud. Il existe plusieurs façons de le faire :

* Utiliser **[GitHub Codespaces](https://github.com/features/codespaces)**, qui est un environnement virtuel créé pour vous sur GitHub, accessible via l'interface du navigateur VS Code. Si vous avez accès à Codespaces, vous pouvez simplement cliquer sur le bouton **Code** dans le dépôt, démarrer un codespace et commencer à exécuter rapidement.
* Utiliser **[Binder](https://mybinder.org/v2/gh/microsoft/ai-for-beginners/HEAD)**. [Binder](https://mybinder.org) est une ressource de calcul gratuite fournie dans le cloud pour des personnes comme vous afin de tester du code sur GitHub. Il y a un bouton sur la page d'accueil pour ouvrir le dépôt dans Binder - cela devrait rapidement vous amener sur le site de binder, qui construira le conteneur sous-jacent et démarrera l'interface web Jupyter pour vous sans problème.

> **Note** : Pour prévenir les abus, Binder a accès à certaines ressources web bloquées. Cela peut empêcher certaines parties du code de fonctionner, notamment celles qui récupèrent des modèles et/ou des ensembles de données depuis Internet public. Vous devrez peut-être trouver des solutions de contournement. De plus, les ressources de calcul fournies par Binder sont assez basiques, donc l'entraînement sera lent, surtout dans les leçons plus complexes ultérieures.

## Exécution dans le Cloud avec GPU

Certaines des leçons ultérieures de ce programme bénéficieraient grandement du support GPU, car sinon l'entraînement sera douloureusement lent. Il existe quelques options que vous pouvez suivre, surtout si vous avez accès au cloud soit par [Azure for Students](https://azure.microsoft.com/free/students/?WT.mc_id=academic-77998-cacaste), soit par votre institution :

* Créer une [Machine Virtuelle de Science des Données](https://docs.microsoft.com/learn/modules/intro-to-azure-data-science-virtual-machine/?WT.mc_id=academic-77998-cacaste) et s'y connecter via Jupyter. Vous pouvez alors cloner le dépôt directement sur la machine et commencer à apprendre. Les VM de la série NC ont un support GPU.

> **Note** : Certaines souscriptions, y compris Azure for Students, ne fournissent pas de support GPU par défaut. Vous devrez peut-être demander des cœurs GPU supplémentaires via une demande de support technique.

* Créer un [Espace de Travail de Machine Learning Azure](https://azure.microsoft.com/services/machine-learning/?WT.mc_id=academic-77998-cacaste) et ensuite utiliser la fonctionnalité Notebook là-bas. [Cette vidéo](https://azure-for-academics.github.io/quickstart/azureml-papers/) montre comment cloner un dépôt dans un notebook Azure ML et commencer à l'utiliser.

Vous pouvez également utiliser Google Colab, qui propose un certain support GPU gratuit, et y télécharger des Jupyter Notebooks pour les exécuter un par un.

**Avertissement** :  
Ce document a été traduit à l'aide de services de traduction automatique basés sur l'IA. Bien que nous visons à garantir l'exactitude, veuillez noter que les traductions automatiques peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue native doit être considéré comme la source faisant autorité. Pour des informations critiques, une traduction humaine professionnelle est recommandée. Nous ne sommes pas responsables des malentendus ou des interprétations erronées résultant de l'utilisation de cette traduction.