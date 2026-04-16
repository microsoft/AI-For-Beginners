# Frameworks de réseaux neuronaux

Comme nous l'avons déjà appris, pour entraîner efficacement des réseaux neuronaux, nous devons faire deux choses :

* Manipuler des tenseurs, par exemple les multiplier, les additionner et calculer certaines fonctions comme sigmoid ou softmax.
* Calculer les gradients de toutes les expressions afin de réaliser l'optimisation par descente de gradient.

## [Quiz avant le cours](https://ff-quizzes.netlify.app/en/ai/quiz/9)

Bien que la bibliothèque `numpy` puisse effectuer la première tâche, nous avons besoin d'un mécanisme pour calculer les gradients. Dans [notre framework](../04-OwnFramework/OwnFramework.ipynb) que nous avons développé dans la section précédente, nous avons dû programmer manuellement toutes les fonctions dérivées dans la méthode `backward`, qui réalise la rétropropagation. Idéalement, un framework devrait nous permettre de calculer les gradients de *n'importe quelle expression* que nous pouvons définir.

Un autre aspect important est de pouvoir effectuer des calculs sur GPU, ou sur d'autres unités de calcul spécialisées, comme le [TPU](https://en.wikipedia.org/wiki/Tensor_Processing_Unit). L'entraînement des réseaux neuronaux profonds nécessite *beaucoup* de calculs, et la possibilité de paralléliser ces calculs sur des GPUs est cruciale.

> ✅ Le terme "paralléliser" signifie répartir les calculs sur plusieurs dispositifs.

Actuellement, les deux frameworks de réseaux neuronaux les plus populaires sont : [TensorFlow](http://TensorFlow.org) et [PyTorch](https://pytorch.org/). Les deux offrent une API de bas niveau pour manipuler les tenseurs sur CPU et GPU. En plus de l'API de bas niveau, il existe également une API de haut niveau, appelée [Keras](https://keras.io/) et [PyTorch Lightning](https://pytorchlightning.ai/) respectivement.

API de bas niveau | [TensorFlow](http://TensorFlow.org) | [PyTorch](https://pytorch.org/)
------------------|-------------------------------------|--------------------------------
API de haut niveau| [Keras](https://keras.io/) | [PyTorch Lightning](https://pytorchlightning.ai/)

**Les APIs de bas niveau** dans les deux frameworks permettent de construire ce qu'on appelle des **graphes computationnels**. Ce graphe définit comment calculer la sortie (généralement la fonction de perte) avec des paramètres d'entrée donnés, et peut être envoyé pour calcul sur GPU, si disponible. Il existe des fonctions pour différencier ce graphe computationnel et calculer les gradients, qui peuvent ensuite être utilisés pour optimiser les paramètres du modèle.

**Les APIs de haut niveau** considèrent les réseaux neuronaux comme une **séquence de couches**, et simplifient considérablement la construction de la plupart des réseaux neuronaux. L'entraînement du modèle nécessite généralement de préparer les données, puis d'appeler une fonction `fit` pour effectuer le travail.

L'API de haut niveau permet de construire des réseaux neuronaux typiques très rapidement sans se soucier de nombreux détails. En revanche, l'API de bas niveau offre beaucoup plus de contrôle sur le processus d'entraînement, et est donc largement utilisée en recherche, notamment lorsqu'on travaille sur de nouvelles architectures de réseaux neuronaux.

Il est également important de comprendre que vous pouvez utiliser les deux APIs ensemble. Par exemple, vous pouvez développer votre propre architecture de couche de réseau avec l'API de bas niveau, puis l'utiliser dans un réseau plus large construit et entraîné avec l'API de haut niveau. Ou vous pouvez définir un réseau avec l'API de haut niveau comme une séquence de couches, puis utiliser votre propre boucle d'entraînement de bas niveau pour effectuer l'optimisation. Les deux APIs reposent sur les mêmes concepts fondamentaux et sont conçues pour bien fonctionner ensemble.

## Apprentissage

Dans ce cours, nous proposons la plupart du contenu à la fois pour PyTorch et TensorFlow. Vous pouvez choisir votre framework préféré et ne parcourir que les notebooks correspondants. Si vous ne savez pas quel framework choisir, consultez des discussions sur Internet concernant **PyTorch vs. TensorFlow**. Vous pouvez également examiner les deux frameworks pour mieux les comprendre.

Lorsque cela est possible, nous utiliserons les APIs de haut niveau pour simplifier les choses. Cependant, nous pensons qu'il est important de comprendre comment fonctionnent les réseaux neuronaux depuis la base. Ainsi, au début, nous travaillons avec l'API de bas niveau et les tenseurs. Cependant, si vous souhaitez avancer rapidement et ne pas passer trop de temps à apprendre ces détails, vous pouvez les ignorer et passer directement aux notebooks de l'API de haut niveau.

## ✍️ Exercices : Frameworks

Poursuivez votre apprentissage dans les notebooks suivants :

API de bas niveau | [Notebook TensorFlow+Keras](IntroKerasTF.ipynb) | [PyTorch](IntroPyTorch.ipynb)
------------------|-------------------------------------|--------------------------------
API de haut niveau| [Keras](IntroKeras.ipynb) | *PyTorch Lightning*

Après avoir maîtrisé les frameworks, récapitulons la notion de surapprentissage.

# Surapprentissage

Le surapprentissage est un concept extrêmement important en apprentissage automatique, et il est essentiel de bien le comprendre !

Considérons le problème suivant d'approximation de 5 points (représentés par des `x` sur les graphiques ci-dessous) :

![linear](../../../../../translated_images/fr/overfit1.f24b71c6f652e59e.webp) | ![overfit](../../../../../translated_images/fr/overfit2.131f5800ae10ca5e.webp)
-------------------------|--------------------------
**Modèle linéaire, 2 paramètres** | **Modèle non linéaire, 7 paramètres**
Erreur d'entraînement = 5.3 | Erreur d'entraînement = 0
Erreur de validation = 5.1 | Erreur de validation = 20

* À gauche, nous voyons une bonne approximation par une ligne droite. Parce que le nombre de paramètres est adéquat, le modèle saisit correctement la distribution des points.
* À droite, le modèle est trop puissant. Comme nous n'avons que 5 points et que le modèle a 7 paramètres, il peut s'ajuster de manière à passer par tous les points, rendant l'erreur d'entraînement égale à 0. Cependant, cela empêche le modèle de comprendre le véritable motif derrière les données, ce qui entraîne une erreur de validation très élevée.

Il est crucial de trouver un équilibre correct entre la richesse du modèle (nombre de paramètres) et le nombre d'échantillons d'entraînement.

## Pourquoi le surapprentissage se produit-il ?

  * Pas assez de données d'entraînement
  * Modèle trop puissant
  * Trop de bruit dans les données d'entrée

## Comment détecter le surapprentissage ?

Comme vous pouvez le voir sur le graphique ci-dessus, le surapprentissage peut être détecté par une erreur d'entraînement très faible et une erreur de validation élevée. Normalement, pendant l'entraînement, nous verrons les erreurs d'entraînement et de validation commencer à diminuer, puis à un certain moment, l'erreur de validation pourrait arrêter de diminuer et commencer à augmenter. Ce sera un signe de surapprentissage, et un indicateur que nous devrions probablement arrêter l'entraînement à ce moment-là (ou au moins faire une sauvegarde du modèle).

![surapprentissage](../../../../../translated_images/fr/Overfitting.408ad91cd90b4371.webp)

## Comment prévenir le surapprentissage ?

Si vous constatez que le surapprentissage se produit, vous pouvez faire l'une des choses suivantes :

 * Augmenter la quantité de données d'entraînement
 * Réduire la complexité du modèle
 * Utiliser une [technique de régularisation](../../4-ComputerVision/08-TransferLearning/TrainingTricks.md), comme le [Dropout](../../4-ComputerVision/08-TransferLearning/TrainingTricks.md#Dropout), que nous examinerons plus tard.

## Surapprentissage et compromis biais-variance

Le surapprentissage est en réalité un cas d'un problème plus général en statistique appelé [compromis biais-variance](https://en.wikipedia.org/wiki/Bias%E2%80%93variance_tradeoff). Si nous considérons les sources possibles d'erreur dans notre modèle, nous pouvons identifier deux types d'erreurs :

* **Les erreurs de biais** sont causées par notre algorithme qui ne parvient pas à capturer correctement la relation entre les données d'entraînement. Cela peut résulter du fait que notre modèle n'est pas assez puissant (**sous-apprentissage**).
* **Les erreurs de variance**, qui sont causées par le modèle qui approxime le bruit dans les données d'entrée au lieu de la relation significative (**surapprentissage**).

Pendant l'entraînement, l'erreur de biais diminue (car notre modèle apprend à approximer les données), et l'erreur de variance augmente. Il est important d'arrêter l'entraînement - soit manuellement (lorsque nous détectons le surapprentissage), soit automatiquement (en introduisant une régularisation) - pour éviter le surapprentissage.

## Conclusion

Dans cette leçon, vous avez appris les différences entre les diverses APIs des deux frameworks d'IA les plus populaires, TensorFlow et PyTorch. En outre, vous avez découvert un sujet très important : le surapprentissage.

## 🚀 Défi

Dans les notebooks associés, vous trouverez des "tâches" en bas ; parcourez les notebooks et complétez les tâches.

## [Quiz après le cours](https://ff-quizzes.netlify.app/en/ai/quiz/10)

## Révision et auto-apprentissage

Faites des recherches sur les sujets suivants :

- TensorFlow
- PyTorch
- Surapprentissage

Posez-vous les questions suivantes :

- Quelle est la différence entre TensorFlow et PyTorch ?
- Quelle est la différence entre surapprentissage et sous-apprentissage ?

## [Devoir](lab/README.md)

Dans ce laboratoire, vous êtes invité à résoudre deux problèmes de classification en utilisant des réseaux entièrement connectés à une ou plusieurs couches avec PyTorch ou TensorFlow.

* [Instructions](lab/README.md)
* [Notebook](lab/LabFrameworks.ipynb)

---

