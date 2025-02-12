# Cadres de Réseaux de Neurones

Comme nous l'avons déjà appris, pour pouvoir entraîner des réseaux de neurones de manière efficace, nous devons faire deux choses :

* Opérer sur des tenseurs, par exemple, multiplier, additionner et calculer certaines fonctions telles que sigmoid ou softmax
* Calculer les gradients de toutes les expressions, afin d'effectuer une optimisation par descente de gradient

## [Quiz pré-cours](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/105)

Bien que la bibliothèque `numpy` puisse faire la première partie, nous avons besoin d'un mécanisme pour calculer les gradients. Dans [notre cadre](../../../../../lessons/3-NeuralNetworks/04-OwnFramework/OwnFramework.ipynb) que nous avons développé dans la section précédente, nous devions programmer manuellement toutes les fonctions dérivées à l'intérieur de la méthode `backward`, qui effectue la rétropropagation. Idéalement, un cadre devrait nous donner la possibilité de calculer les gradients de *n'importe quelle expression* que nous pouvons définir.

Une autre chose importante est de pouvoir effectuer des calculs sur GPU, ou sur toute autre unité de calcul spécialisée, comme [TPU](https://en.wikipedia.org/wiki/Tensor_Processing_Unit). L'entraînement des réseaux de neurones profonds nécessite *beaucoup* de calculs, et pouvoir paralléliser ces calculs sur des GPU est très important.

> ✅ Le terme 'paralléliser' signifie distribuer les calculs sur plusieurs appareils.

Actuellement, les deux cadres de réseaux de neurones les plus populaires sont : [TensorFlow](http://TensorFlow.org) et [PyTorch](https://pytorch.org/). Les deux fournissent une API de bas niveau pour travailler avec des tenseurs à la fois sur CPU et GPU. En plus de l'API de bas niveau, il existe également une API de niveau supérieur, appelée [Keras](https://keras.io/) et [PyTorch Lightning](https://pytorchlightning.ai/) respectivement.

API de Bas Niveau | [TensorFlow](http://TensorFlow.org) | [PyTorch](https://pytorch.org/)
------------------|-------------------------------------|--------------------------------
API de Niveau Supérieur| [Keras](https://keras.io/) | [PyTorch Lightning](https://pytorchlightning.ai/)

**Les API de bas niveau** dans les deux cadres vous permettent de construire ce que l'on appelle des **graphes computationnels**. Ce graphe définit comment calculer la sortie (généralement la fonction de perte) avec des paramètres d'entrée donnés, et peut être poussé pour le calcul sur GPU, si disponible. Il existe des fonctions pour différencier ce graphe computationnel et calculer les gradients, qui peuvent ensuite être utilisés pour optimiser les paramètres du modèle.

**Les API de niveau supérieur** considèrent en grande partie les réseaux de neurones comme une **séquence de couches**, et facilitent la construction de la plupart des réseaux de neurones. L'entraînement du modèle nécessite généralement de préparer les données, puis d'appeler une fonction `fit` pour effectuer le travail.

L'API de niveau supérieur vous permet de construire des réseaux de neurones typiques très rapidement sans vous soucier de nombreux détails. En même temps, l'API de bas niveau offre beaucoup plus de contrôle sur le processus d'entraînement, et c'est pourquoi elles sont souvent utilisées dans la recherche, lorsque vous travaillez avec de nouvelles architectures de réseaux de neurones.

Il est également important de comprendre que vous pouvez utiliser les deux API ensemble, par exemple, vous pouvez développer votre propre architecture de couche de réseau en utilisant l'API de bas niveau, puis l'utiliser à l'intérieur d'un réseau plus large construit et entraîné avec l'API de niveau supérieur. Ou vous pouvez définir un réseau en utilisant l'API de niveau supérieur comme une séquence de couches, puis utiliser votre propre boucle d'entraînement de bas niveau pour effectuer l'optimisation. Les deux API utilisent les mêmes concepts sous-jacents de base, et elles sont conçues pour bien fonctionner ensemble.

## Apprentissage

Dans ce cours, nous offrons la plupart du contenu à la fois pour PyTorch et TensorFlow. Vous pouvez choisir votre cadre préféré et ne passer qu'à travers les notebooks correspondants. Si vous n'êtes pas sûr du cadre à choisir, lisez quelques discussions sur Internet concernant **PyTorch vs. TensorFlow**. Vous pouvez également jeter un œil aux deux cadres pour mieux comprendre.

Lorsque cela est possible, nous utiliserons des API de niveau supérieur pour plus de simplicité. Cependant, nous pensons qu'il est important de comprendre comment fonctionnent les réseaux de neurones depuis le début, donc au début, nous commençons par travailler avec l'API de bas niveau et les tenseurs. Cependant, si vous souhaitez avancer rapidement et ne pas passer trop de temps à apprendre ces détails, vous pouvez les ignorer et aller directement dans les notebooks de l'API de niveau supérieur.

## ✍️ Exercices : Cadres

Continuez votre apprentissage dans les notebooks suivants :

API de Bas Niveau | [Notebook TensorFlow+Keras](../../../../../lessons/3-NeuralNetworks/05-Frameworks/IntroKerasTF.ipynb) | [PyTorch](../../../../../lessons/3-NeuralNetworks/05-Frameworks/IntroPyTorch.ipynb)
------------------|-------------------------------------|--------------------------------
API de Niveau Supérieur| [Keras](../../../../../lessons/3-NeuralNetworks/05-Frameworks/IntroKeras.ipynb) | *PyTorch Lightning*

Après avoir maîtrisé les cadres, récapitulons la notion de surapprentissage.

# Surapprentissage

Le surapprentissage est un concept extrêmement important en apprentissage automatique, et il est crucial de bien le comprendre !

Considérons le problème suivant d'approximation de 5 points (représentés par `x` sur les graphiques ci-dessous) :

![linear](../../../../../translated_images/overfit1.f24b71c6f652e59e6bed7245ffbeaecc3ba320e16e2221f6832b432052c4da43.fr.jpg) | ![overfit](../../../../../translated_images/overfit2.131f5800ae10ca5e41d12a411f5f705d9ee38b1b10916f284b787028dd55cc1c.fr.jpg)
-------------------------|--------------------------
**Modèle linéaire, 2 paramètres** | **Modèle non linéaire, 7 paramètres**
Erreur d'entraînement = 5.3 | Erreur de validation = 0
Erreur de validation = 5.1 | Erreur de validation = 20

* À gauche, nous voyons une bonne approximation par une ligne droite. Parce que le nombre de paramètres est adéquat, le modèle saisit bien l'idée derrière la distribution des points.
* À droite, le modèle est trop puissant. Étant donné que nous n'avons que 5 points et que le modèle a 7 paramètres, il peut s'ajuster de manière à passer par tous les points, rendant l'erreur d'entraînement égale à 0. Cependant, cela empêche le modèle de comprendre le bon motif derrière les données, donc l'erreur de validation est très élevée.

Il est très important de trouver un bon équilibre entre la richesse du modèle (nombre de paramètres) et le nombre d'échantillons d'entraînement.

## Pourquoi le surapprentissage se produit

  * Pas assez de données d'entraînement
  * Modèle trop puissant
  * Trop de bruit dans les données d'entrée

## Comment détecter le surapprentissage

Comme vous pouvez le voir sur le graphique ci-dessus, le surapprentissage peut être détecté par une très faible erreur d'entraînement et une erreur de validation élevée. Normalement, pendant l'entraînement, nous verrons à la fois les erreurs d'entraînement et de validation commencer à diminuer, puis à un certain moment, l'erreur de validation pourrait cesser de diminuer et commencer à augmenter. Cela sera un signe de surapprentissage, et l'indicateur que nous devrions probablement arrêter l'entraînement à ce stade (ou au moins faire un instantané du modèle).

![overfitting](../../../../../translated_images/Overfitting.408ad91cd90b4371d0a81f4287e1409c359751adeb1ae450332af50e84f08c3e.fr.png)

## Comment prévenir le surapprentissage

Si vous constatez que le surapprentissage se produit, vous pouvez faire l'une des choses suivantes :

 * Augmenter la quantité de données d'entraînement
 * Diminuer la complexité du modèle
 * Utiliser une [technique de régularisation](../../4-ComputerVision/08-TransferLearning/TrainingTricks.md), telle que [Dropout](../../4-ComputerVision/08-TransferLearning/TrainingTricks.md#Dropout), que nous considérerons plus tard.

## Surapprentissage et compromis biais-variance

Le surapprentissage est en fait un cas d'un problème plus générique en statistique appelé [compromis biais-variance](https://en.wikipedia.org/wiki/Bias%E2%80%93variance_tradeoff). Si nous considérons les sources possibles d'erreur dans notre modèle, nous pouvons voir deux types d'erreurs :

* **Erreurs de biais** causées par le fait que notre algorithme n'est pas capable de capturer correctement la relation entre les données d'entraînement. Cela peut résulter du fait que notre modèle n'est pas assez puissant (**sous-apprentissage**).
* **Erreurs de variance**, qui sont causées par le modèle qui approxime le bruit dans les données d'entrée au lieu de la relation significative (**surapprentissage**).

Pendant l'entraînement, l'erreur de biais diminue (à mesure que notre modèle apprend à approximer les données), et l'erreur de variance augmente. Il est important d'arrêter l'entraînement - soit manuellement (lorsque nous détectons le surapprentissage), soit automatiquement (en introduisant une régularisation) - pour prévenir le surapprentissage.

## Conclusion

Dans cette leçon, vous avez appris les différences entre les différentes API des deux cadres d'IA les plus populaires, TensorFlow et PyTorch. De plus, vous avez appris un sujet très important, le surapprentissage.

## 🚀 Défi

Dans les notebooks accompagnants, vous trouverez des 'tâches' en bas ; parcourez les notebooks et complétez les tâches.

## [Quiz post-cours](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/205)

## Revue & Auto-apprentissage

Faites des recherches sur les sujets suivants :

- TensorFlow
- PyTorch
- Surapprentissage

Posez-vous les questions suivantes :

- Quelle est la différence entre TensorFlow et PyTorch ?
- Quelle est la différence entre surapprentissage et sous-apprentissage ?

## [Devoir](lab/README.md)

Dans ce laboratoire, vous êtes invité à résoudre deux problèmes de classification en utilisant des réseaux entièrement connectés à une et plusieurs couches en utilisant PyTorch ou TensorFlow.

* [Instructions](lab/README.md)
* [Notebook](../../../../../lessons/3-NeuralNetworks/05-Frameworks/lab/LabFrameworks.ipynb)

**Avertissement** :  
Ce document a été traduit à l'aide de services de traduction automatisés basés sur l'IA. Bien que nous visons à garantir l'exactitude, veuillez noter que les traductions automatiques peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue native doit être considéré comme la source autorisée. Pour des informations critiques, une traduction professionnelle par un humain est recommandée. Nous ne sommes pas responsables des malentendus ou des interprétations erronées résultant de l'utilisation de cette traduction.