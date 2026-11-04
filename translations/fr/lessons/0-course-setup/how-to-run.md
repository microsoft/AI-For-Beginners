# Comment exécuter le code

Ce programme contient de nombreux exemples exécutables et des laboratoires que vous souhaiterez exécuter. Pour ce faire, vous devez pouvoir exécuter du code Python dans les notebooks Jupyter fournis dans le cadre de ce programme. Vous avez plusieurs options pour exécuter le code :

## Exécuter localement sur votre ordinateur

Pour exécuter le code localement sur votre ordinateur, une installation de Python est nécessaire. Une recommandation est d’installer **[miniconda](https://conda.io/en/latest/miniconda.html)** - c’est une installation plutôt légère qui supporte le gestionnaire de paquets `conda` pour différentes **environnements virtuels** Python.

Après avoir installé miniconda, clonez le dépôt et créez un environnement virtuel à utiliser pour ce cours :

```bash
git clone http://github.com/microsoft/ai-for-beginners
cd ai-for-beginners
conda env create --name ai4beg --file .devcontainer/environment.yml
conda activate ai4beg
```

> **Note Windows** : Si la création de l’environnement échoue lors de l’installation de `gdk-pixbuf` avec un `UnicodeDecodeError` qui mentionne le codec `gbk`, activez le mode UTF-8 de Python dans votre terminal puis réessayez. Utilisez la syntaxe correspondant à votre terminal :
>
> **PowerShell :**
>
> ```powershell
> $env:PYTHONUTF8 = "1"
> conda env create --name ai4beg --file .devcontainer/environment.yml
> ```
>
> **Invite de commandes (`cmd.exe`) ou Anaconda Prompt :**
>
> ```cmd
> set PYTHONUTF8=1
> conda env create --name ai4beg --file .devcontainer/environment.yml
> ```
>
> **Bash, y compris Git Bash :**
>
> ```bash
> export PYTHONUTF8=1
> conda env create --name ai4beg --file .devcontainer/environment.yml
> ```
>
> Si une tentative échouée a laissé l’environnement `ai4beg` derrière, désactivez-le puis supprimez cet environnement avant de réessayer. Utilisez `conda deactivate` en premier quand un environnement est actif :
>
> ```text
> conda deactivate
> conda env remove --name ai4beg
> ```

### Utilisation de Visual Studio Code avec l’extension Python

Ce programme s’utilise au mieux en l’ouvrant dans [Visual Studio Code](http://code.visualstudio.com/?WT.mc_id=academic-77998-cacaste) avec [l’extension Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-77998-cacaste).

> **Note** : Une fois que vous avez cloné et ouvert le répertoire dans VS Code, il vous suggérera automatiquement d’installer les extensions Python. Vous devrez également installer miniconda comme décrit ci-dessus.

> **Note** : Si VS Code vous suggère de rouvrir le dépôt dans un conteneur, vous devriez refuser ceci pour utiliser l’installation locale de Python.

### Utilisation de Jupyter dans le navigateur

Vous pouvez aussi utiliser un environnement Jupyter depuis le navigateur sur votre propre ordinateur. Jupyter classique comme JupyterHub offrent un environnement de développement pratique avec autocomplétion, surlignage de code, etc.

Pour démarrer Jupyter localement, placez-vous dans le répertoire du cours, et exécutez :

```bash
jupyter notebook
```
ou
```bash
jupyterhub
```
Vous pouvez ensuite naviguer vers n’importe quel fichier `.ipynb`, les ouvrir et commencer à travailler.

### Exécution dans un conteneur

Une alternative à l’installation de Python serait d’exécuter le code dans un conteneur. Comme notre dépôt fournit un dossier spécial `.devcontainer` qui explique comment construire un conteneur pour ce dépôt, VS Code propose la possibilité de rouvrir le code dans un conteneur. Cela nécessite l’installation de Docker et serait également plus complexe, nous recommandons donc cette option aux utilisateurs plus expérimentés.

## Exécution dans le cloud

Si vous ne souhaitez pas installer Python localement, et que vous avez accès à certaines ressources cloud, une bonne alternative est d’exécuter le code dans le cloud. Plusieurs façons existent pour cela :

* Utiliser **[GitHub Codespaces](https://github.com/features/codespaces)**, qui est un environnement virtuel créé pour vous sur GitHub, accessible via une interface navigateur VS Code. Si vous avez accès à Codespaces, vous pouvez simplement cliquer sur le bouton **Code** dans le dépôt, démarrer un codespace, et commencer rapidement.
* Utiliser **[Binder](https://mybinder.org/v2/gh/microsoft/ai-for-beginners/HEAD)**. [Binder](https://mybinder.org) offre des ressources informatiques gratuites fournies dans le cloud pour que des personnes comme vous puissent tester du code sur GitHub. Il y a un bouton sur la page d'accueil pour ouvrir le dépôt dans Binder - cela devrait rapidement vous amener sur le site Binder, qui construira un conteneur sous-jacent et lancera une interface web Jupyter pour vous de manière transparente.

> **Note** : Pour prévenir les abus, Binder a l'accès à certaines ressources web bloqué. Cela peut empêcher une partie du code de fonctionner, notamment lorsque celui-ci récupère des modèles et/ou des ensembles de données depuis Internet public. Vous pourriez avoir besoin de trouver des solutions de contournement. De plus, les ressources informatiques fournies par Binder sont assez basiques, donc l'entraînement sera lent, surtout dans les leçons plus complexes ultérieures.

## Exécution dans le Cloud avec GPU

Certaines leçons ultérieures de ce cursus bénéficieraient grandement du support GPU. L'entraînement de modèles, par exemple, peut être douloureusement lent sinon. Il existe plusieurs options, notamment si vous avez accès au cloud via [Azure for Students](https://azure.microsoft.com/free/students/?WT.mc_id=academic-77998-cacaste) ou via votre institution :

* Créez une [Data Science Virtual Machine](https://docs.microsoft.com/learn/modules/intro-to-azure-data-science-virtual-machine/?WT.mc_id=academic-77998-cacaste) et connectez-vous via Jupyter. Vous pouvez alors cloner le dépôt directement sur la machine, et commencer à apprendre. Les VM de la série NC disposent du support GPU.

> **Note** : Certains abonnements, notamment Azure for Students, ne fournissent pas le support GPU d'emblée. Vous devrez peut-être demander des cœurs GPU supplémentaires via une demande de support technique.

* Créez un [Azure Machine Learning Workspace](https://azure.microsoft.com/services/machine-learning/?WT.mc_id=academic-77998-cacaste) puis utilisez la fonctionnalité Notebook disponible. [Cette vidéo](https://azure-for-academics.github.io/quickstart/azureml-papers/) montre comment cloner un dépôt dans un notebook Azure ML et commencer à l'utiliser.

Vous pouvez aussi utiliser Google Colab, qui propose un certain support GPU gratuit, et y téléverser les notebooks Jupyter pour les exécuter un par un.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Avertissement** :
Ce document a été traduit à l'aide du service de traduction automatique [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforçions d'assurer l'exactitude, veuillez noter que les traductions automatisées peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue native doit être considéré comme la source faisant autorité. Pour les informations critiques, il est recommandé de recourir à une traduction professionnelle réalisée par un humain. Nous ne saurions être tenus responsables des malentendus ou erreurs d'interprétation découlant de l'utilisation de cette traduction.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->