<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "7df19702b8d2d3f7c4238c51bec2c8fc",
  "translation_date": "2025-08-24T20:59:31+00:00",
  "source_file": "lessons/0-course-setup/how-to-run.md",
  "language_code": "fr"
}
-->
# Comment exécuter le code

Ce programme contient de nombreux exemples exécutables et laboratoires que vous souhaiterez exécuter. Pour ce faire, vous devez pouvoir exécuter du code Python dans des Jupyter Notebooks fournis dans le cadre de ce programme. Vous avez plusieurs options pour exécuter le code :

## Exécuter localement sur votre ordinateur

Pour exécuter le code localement sur votre ordinateur, vous devez avoir une version de Python installée. Je recommande personnellement d'installer **[miniconda](https://conda.io/en/latest/miniconda.html)** - une installation légère qui prend en charge le gestionnaire de paquets `conda` pour différents **environnements virtuels** Python.

Après avoir installé miniconda, vous devez cloner le dépôt et créer un environnement virtuel à utiliser pour ce cours :

```bash
git clone http://github.com/microsoft/ai-for-beginners
cd ai-for-beginners
conda env create --name ai4beg --file .devcontainer/environment.yml
conda activate ai4beg
```

### Utiliser Visual Studio Code avec l'extension Python

La meilleure façon d'utiliser ce programme est probablement de l'ouvrir dans [Visual Studio Code](http://code.visualstudio.com/?WT.mc_id=academic-77998-cacaste) avec l'[extension Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-77998-cacaste).

> **Note** : Une fois que vous avez cloné et ouvert le répertoire dans VS Code, il vous suggérera automatiquement d'installer les extensions Python. Vous devrez également installer miniconda comme décrit ci-dessus.

> **Note** : Si VS Code vous propose de rouvrir le dépôt dans un conteneur, vous devez refuser pour utiliser l'installation Python locale.

### Utiliser Jupyter dans le navigateur

Vous pouvez également utiliser l'environnement Jupyter directement depuis le navigateur sur votre propre ordinateur. En fait, Jupyter classique et Jupyter Hub offrent un environnement de développement assez pratique avec autocomplétion, surlignage de code, etc.

Pour démarrer Jupyter localement, allez dans le répertoire du cours et exécutez :

```bash
jupyter notebook
```
ou
```bash
jupyterhub
```
Vous pouvez ensuite naviguer vers n'importe quel fichier `.ipynb`, l'ouvrir et commencer à travailler.

### Exécuter dans un conteneur

Une alternative à l'installation de Python serait d'exécuter le code dans un conteneur. Étant donné que notre dépôt contient un dossier spécial `.devcontainer` qui indique comment construire un conteneur pour ce dépôt, VS Code vous proposera de rouvrir le code dans un conteneur. Cela nécessitera l'installation de Docker et sera également plus complexe, donc nous recommandons cette option aux utilisateurs plus expérimentés.

## Exécuter dans le cloud

Si vous ne souhaitez pas installer Python localement et que vous avez accès à des ressources cloud, une bonne alternative serait d'exécuter le code dans le cloud. Il existe plusieurs façons de le faire :

* Utiliser **[GitHub Codespaces](https://github.com/features/codespaces)**, qui est un environnement virtuel créé pour vous sur GitHub, accessible via l'interface navigateur de VS Code. Si vous avez accès à Codespaces, vous pouvez simplement cliquer sur le bouton **Code** dans le dépôt, démarrer un codespace et commencer à travailler rapidement.
* Utiliser **[Binder](https://mybinder.org/v2/gh/microsoft/ai-for-beginners/HEAD)**. [Binder](https://mybinder.org) fournit des ressources informatiques gratuites dans le cloud pour permettre aux utilisateurs de tester du code sur GitHub. Il y a un bouton sur la page d'accueil pour ouvrir le dépôt dans Binder - cela vous amènera rapidement au site Binder, qui construira le conteneur sous-jacent et démarrera l'interface web Jupyter pour vous de manière transparente.

> **Note** : Pour éviter les abus, Binder bloque l'accès à certaines ressources web. Cela peut empêcher certains codes qui récupèrent des modèles et/ou des ensembles de données depuis Internet de fonctionner. Vous devrez peut-être trouver des solutions alternatives. De plus, les ressources informatiques fournies par Binder sont assez basiques, donc l'entraînement sera lent, en particulier dans les leçons plus complexes.

## Exécuter dans le cloud avec GPU

Certaines des leçons plus avancées de ce programme bénéficieraient grandement du support GPU, car sinon l'entraînement serait extrêmement lent. Voici quelques options, surtout si vous avez accès au cloud via [Azure pour les étudiants](https://azure.microsoft.com/free/students/?WT.mc_id=academic-77998-cacaste) ou via votre institution :

* Créez une [Machine Virtuelle Data Science](https://docs.microsoft.com/learn/modules/intro-to-azure-data-science-virtual-machine/?WT.mc_id=academic-77998-cacaste) et connectez-vous à celle-ci via Jupyter. Vous pouvez ensuite cloner le dépôt directement sur la machine et commencer à apprendre. Les machines virtuelles de la série NC disposent du support GPU.

> **Note** : Certaines abonnements, y compris Azure pour les étudiants, ne fournissent pas de support GPU par défaut. Vous devrez peut-être demander des cœurs GPU supplémentaires via une demande de support technique.

* Créez un [Espace de travail Azure Machine Learning](https://azure.microsoft.com/services/machine-learning/?WT.mc_id=academic-77998-cacaste) et utilisez ensuite la fonctionnalité Notebook. [Cette vidéo](https://azure-for-academics.github.io/quickstart/azureml-papers/) montre comment cloner un dépôt dans un notebook Azure ML et commencer à l'utiliser.

Vous pouvez également utiliser Google Colab, qui offre un support GPU gratuit, et y télécharger des Jupyter Notebooks pour les exécuter un par un.

**Avertissement** :  
Ce document a été traduit à l'aide du service de traduction automatique [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforcions d'assurer l'exactitude, veuillez noter que les traductions automatisées peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue d'origine doit être considéré comme la source faisant autorité. Pour des informations critiques, il est recommandé de recourir à une traduction humaine professionnelle. Nous déclinons toute responsabilité en cas de malentendus ou d'interprétations erronées résultant de l'utilisation de cette traduction.