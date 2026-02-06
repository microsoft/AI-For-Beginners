# Astuces pour l'entraînement en Deep Learning

À mesure que les réseaux neuronaux deviennent plus profonds, leur entraînement devient de plus en plus complexe. Un problème majeur est celui des [gradients qui disparaissent](https://en.wikipedia.org/wiki/Vanishing_gradient_problem) ou des [gradients qui explosent](https://deepai.org/machine-learning-glossary-and-terms/exploding-gradient-problem#:~:text=Exploding%20gradients%20are%20a%20problem,updates%20are%20small%20and%20controlled.). [Cet article](https://towardsdatascience.com/the-vanishing-exploding-gradient-problem-in-deep-neural-networks-191358470c11) offre une bonne introduction à ces problèmes.

Pour rendre l'entraînement des réseaux profonds plus efficace, plusieurs techniques peuvent être utilisées.

## Maintenir les valeurs dans un intervalle raisonnable

Pour stabiliser les calculs numériques, il est important de s'assurer que toutes les valeurs dans le réseau neuronal restent dans une échelle raisonnable, généralement [-1..1] ou [0..1]. Ce n'est pas une exigence stricte, mais la nature des calculs en virgule flottante fait que des valeurs de magnitudes différentes ne peuvent pas être manipulées avec précision ensemble. Par exemple, si nous additionnons 10<sup>-10</sup> et 10<sup>10</sup>, nous obtiendrons probablement 10<sup>10</sup>, car la valeur plus petite sera "convertie" au même ordre que la plus grande, et la mantisse sera perdue.

La plupart des fonctions d'activation présentent des non-linéarités autour de [-1..1], et il est donc logique de mettre à l'échelle toutes les données d'entrée dans l'intervalle [-1..1] ou [0..1].

## Initialisation des poids

Idéalement, nous voulons que les valeurs restent dans la même plage après avoir traversé les couches du réseau. Il est donc important d'initialiser les poids de manière à préserver la distribution des valeurs.

La distribution normale **N(0,1)** n'est pas une bonne idée, car si nous avons *n* entrées, l'écart-type de la sortie serait *n*, et les valeurs risquent de sortir de l'intervalle [0..1].

Les initialisations suivantes sont souvent utilisées :

 * Distribution uniforme -- `uniform`
 * **N(0,1/n)** -- `gaussian`
 * **N(0,1/√n_in)** garantit que pour des entrées avec une moyenne nulle et un écart-type de 1, la même moyenne/écart-type sera conservée
 * **N(0,√2/(n_in+n_out))** -- appelée **initialisation Xavier** (`glorot`), elle aide à maintenir les signaux dans la plage pendant la propagation avant et arrière

## Normalisation par lot (Batch Normalization)

Même avec une bonne initialisation des poids, ceux-ci peuvent devenir arbitrairement grands ou petits pendant l'entraînement, ce qui fait sortir les signaux de leur plage appropriée. Nous pouvons ramener les signaux dans la plage correcte en utilisant des techniques de **normalisation**. Bien qu'il en existe plusieurs (normalisation des poids, normalisation par couche), la plus couramment utilisée est la normalisation par lot.

L'idée de la **normalisation par lot** est de prendre en compte toutes les valeurs d'un mini-lot et de normaliser (c'est-à-dire soustraire la moyenne et diviser par l'écart-type) en fonction de ces valeurs. Elle est implémentée comme une couche du réseau qui effectue cette normalisation après l'application des poids, mais avant la fonction d'activation. En conséquence, on observe généralement une meilleure précision finale et un entraînement plus rapide.

Voici l'[article original](https://arxiv.org/pdf/1502.03167.pdf) sur la normalisation par lot, l'[explication sur Wikipedia](https://en.wikipedia.org/wiki/Batch_normalization), et [un bon article introductif](https://towardsdatascience.com/batch-normalization-in-3-levels-of-understanding-14c2da90a338) (et un autre [en russe](https://habrahabr.ru/post/309302/)).

## Dropout

Le **Dropout** est une technique intéressante qui supprime un certain pourcentage de neurones aléatoires pendant l'entraînement. Il est également implémenté comme une couche avec un paramètre (pourcentage de neurones à supprimer, généralement entre 10 % et 50 %), et pendant l'entraînement, il met à zéro des éléments aléatoires du vecteur d'entrée avant de les transmettre à la couche suivante.

Bien que cela puisse sembler étrange, vous pouvez observer l'effet du dropout sur l'entraînement d'un classificateur de chiffres MNIST dans le notebook [`Dropout.ipynb`](../../../../../lessons/4-ComputerVision/08-TransferLearning/Dropout.ipynb). Cela accélère l'entraînement et permet d'atteindre une meilleure précision en moins d'époques.

Cet effet peut être expliqué de plusieurs manières :

 * On peut le considérer comme un facteur de choc aléatoire pour le modèle, qui le sort d'un minimum local
 * On peut le considérer comme une *moyenne implicite de modèles*, car on peut dire qu'avec le dropout, on entraîne un modèle légèrement différent

> *Certains disent qu'une personne ivre qui essaie d'apprendre quelque chose le retiendra mieux le lendemain matin, comparée à une personne sobre, car un cerveau avec des neurones dysfonctionnels essaie de mieux s'adapter pour saisir le sens. Nous n'avons jamais testé si cela est vrai ou non.*

## Prévenir le surapprentissage

Un aspect très important du deep learning est de savoir prévenir le [surapprentissage](../../3-NeuralNetworks/05-Frameworks/Overfitting.md). Bien qu'il puisse être tentant d'utiliser un modèle de réseau neuronal très puissant, il faut toujours équilibrer le nombre de paramètres du modèle avec le nombre d'échantillons d'entraînement.

> Assurez-vous de bien comprendre le concept de [surapprentissage](../../3-NeuralNetworks/05-Frameworks/Overfitting.md) que nous avons introduit précédemment !

Il existe plusieurs façons de prévenir le surapprentissage :

 * Arrêt anticipé -- surveiller en continu l'erreur sur l'ensemble de validation et arrêter l'entraînement lorsque l'erreur de validation commence à augmenter.
 * Décroissance explicite des poids / Régularisation -- ajouter une pénalité supplémentaire à la fonction de perte pour des valeurs absolues élevées des poids, ce qui empêche le modèle d'obtenir des résultats très instables
 * Moyenne des modèles -- entraîner plusieurs modèles et ensuite moyenner les résultats. Cela aide à minimiser la variance.
 * Dropout (Moyenne implicite des modèles)

## Optimiseurs / Algorithmes d'entraînement

Un autre aspect important de l'entraînement est de choisir un bon algorithme d'entraînement. Bien que le **gradient descent** classique soit un choix raisonnable, il peut parfois être trop lent ou entraîner d'autres problèmes.

En deep learning, nous utilisons le **Stochastic Gradient Descent** (SGD), qui est un gradient descent appliqué à des mini-lots sélectionnés aléatoirement dans l'ensemble d'entraînement. Les poids sont ajustés selon cette formule :

w<sup>t+1</sup> = w<sup>t</sup> - η∇ℒ

### Momentum

Dans le **momentum SGD**, nous conservons une partie du gradient des étapes précédentes. Cela ressemble à un mouvement avec inertie : si nous recevons une impulsion dans une direction différente, notre trajectoire ne change pas immédiatement, mais conserve une partie du mouvement initial. Ici, nous introduisons un autre vecteur v pour représenter la *vitesse* :

* v<sup>t+1</sup> = γ v<sup>t</sup> - η∇ℒ
* w<sup>t+1</sup> = w<sup>t</sup>+v<sup>t+1</sup>

Le paramètre γ indique dans quelle mesure nous prenons en compte l'inertie : γ=0 correspond au SGD classique ; γ=1 est une équation de mouvement pure.

### Adam, Adagrad, etc.

Dans chaque couche, nous multiplions les signaux par une matrice W<sub>i</sub>. Selon ||W<sub>i</sub>||, le gradient peut soit diminuer et être proche de 0, soit augmenter indéfiniment. C'est l'essence du problème des gradients qui explosent/disparaissent.

Une solution à ce problème est d'utiliser uniquement la direction du gradient dans l'équation, en ignorant la valeur absolue, c'est-à-dire :

w<sup>t+1</sup> = w<sup>t</sup> - η(∇ℒ/||∇ℒ||), où ||∇ℒ|| = √∑(∇ℒ)<sup>2</sup>

Cet algorithme est appelé **Adagrad**. D'autres algorithmes utilisant la même idée : **RMSProp**, **Adam**

> **Adam** est considéré comme un algorithme très efficace pour de nombreuses applications. Si vous ne savez pas lequel utiliser, choisissez Adam.

### Clipping des gradients

Le clipping des gradients est une extension de l'idée précédente. Lorsque ||∇ℒ|| ≤ θ, nous utilisons le gradient original dans l'optimisation des poids, et lorsque ||∇ℒ|| > θ, nous divisons le gradient par sa norme. Ici, θ est un paramètre, dans la plupart des cas, on peut prendre θ=1 ou θ=10.

### Décroissance du taux d'apprentissage

Le succès de l'entraînement dépend souvent du paramètre de taux d'apprentissage η. Il est logique de supposer que des valeurs plus grandes de η entraînent un apprentissage plus rapide, ce qui est souhaitable au début de l'entraînement, tandis que des valeurs plus petites de η permettent de peaufiner le réseau. Ainsi, dans la plupart des cas, nous voulons diminuer η au cours de l'entraînement.

Cela peut être fait en multipliant η par un certain nombre (par exemple, 0,98) après chaque époque d'entraînement, ou en utilisant un **planning de taux d'apprentissage** plus complexe.

## Différentes architectures de réseaux

Choisir la bonne architecture de réseau pour votre problème peut être délicat. En général, on choisit une architecture qui a fait ses preuves pour une tâche spécifique (ou similaire). Voici un [bon aperçu](https://www.topbots.com/a-brief-history-of-neural-network-architectures/) des architectures de réseaux neuronaux pour la vision par ordinateur.

> Il est important de choisir une architecture suffisamment puissante pour le nombre d'échantillons d'entraînement dont nous disposons. Choisir un modèle trop puissant peut entraîner un [surapprentissage](../../3-NeuralNetworks/05-Frameworks/Overfitting.md).

Une autre bonne approche consiste à utiliser une architecture qui s'ajuste automatiquement à la complexité requise. Dans une certaine mesure, les architectures **ResNet** et **Inception** sont auto-ajustables. [Plus d'informations sur les architectures de vision par ordinateur](../07-ConvNets/CNN_Architectures.md).

**Avertissement** :  
Ce document a été traduit à l'aide du service de traduction automatique [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforcions d'assurer l'exactitude, veuillez noter que les traductions automatisées peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue d'origine doit être considéré comme la source faisant autorité. Pour des informations critiques, il est recommandé de recourir à une traduction professionnelle réalisée par un humain. Nous déclinons toute responsabilité en cas de malentendus ou d'interprétations erronées résultant de l'utilisation de cette traduction.