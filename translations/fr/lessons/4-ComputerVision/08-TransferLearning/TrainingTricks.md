# Astuces pour l'entraînement en Deep Learning

À mesure que les réseaux neuronaux deviennent plus profonds, le processus de leur entraînement devient de plus en plus difficile. Un problème majeur est ce qu'on appelle les [gradients qui disparaissent](https://en.wikipedia.org/wiki/Vanishing_gradient_problem) ou les [gradients qui explosent](https://deepai.org/machine-learning-glossary-and-terms/exploding-gradient-problem#:~:text=Exploding%20gradients%20are%20a%20problem,updates%20are%20small%20and%20controlled.). [Ce post](https://towardsdatascience.com/the-vanishing-exploding-gradient-problem-in-deep-neural-networks-191358470c11) donne une bonne introduction à ces problèmes.

Pour rendre l'entraînement des réseaux profonds plus efficace, quelques techniques peuvent être utilisées.

## Garder les valeurs dans un intervalle raisonnable

Pour rendre les calculs numériques plus stables, nous voulons nous assurer que toutes les valeurs au sein de notre réseau neuronal sont dans une échelle raisonnable, typiquement [-1..1] ou [0..1]. Ce n'est pas une exigence très stricte, mais la nature des calculs en virgule flottante fait que des valeurs de différentes magnitudes ne peuvent pas être manipulées ensemble avec précision. Par exemple, si nous additionnons 10<sup>-10</sup> et 10<sup>10</sup>, il est probable que nous obtenions 10<sup>10</sup>, car la plus petite valeur serait « convertie » au même ordre de grandeur que la plus grande, et ainsi la mantisse serait perdue.

La plupart des fonctions d'activation ont des non-linéarités autour de [-1..1], il est donc logique de mettre à l'échelle toutes les données d'entrée dans l'intervalle [-1..1] ou [0..1].

## Initialisation des poids

Idéalement, nous voulons que les valeurs soient dans la même plage après avoir traversé les couches du réseau. Il est donc important d'initialiser les poids de manière à préserver la distribution des valeurs.

La distribution normale **N(0,1)** n'est pas une bonne idée, car si nous avons *n* entrées, l'écart type de la sortie serait *&radic;n*, et les valeurs risquent de sortir de l'intervalle [0..1].

Les initialisations suivantes sont souvent utilisées :

 * Distribution uniforme -- `uniform`
 * **N(0,1/n)** -- `gaussian`
 * **N(0,1/&radic;n_in)** garantit que pour les entrées avec moyenne nulle et écart type de 1, la moyenne / l'écart type restent les mêmes
 * **N(0,&radic;2/(n_in+n_out))** -- dite **initialisation Xavier** (`glorot`), cela aide à maintenir les signaux dans la plage pendant la propagation avant et arrière

## Normalisation par batch

Même avec une bonne initialisation des poids, ceux-ci peuvent devenir arbitrairement grands ou petits durant l'entraînement, ce qui déplace les signaux hors de la plage adéquate. Nous pouvons ramener les signaux à la normale en utilisant l'une des techniques de **normalisation**. Bien qu'il en existe plusieurs (normalisation des poids, normalisation de couche), la plus utilisée est la normalisation par batch.

L'idée de la **normalisation par batch** est de prendre en compte toutes les valeurs du mini-lot, et de réaliser une normalisation (c'est-à-dire soustraire la moyenne et diviser par l'écart type) basée sur ces valeurs. Elle est implémentée comme une couche du réseau qui fait cette normalisation après avoir appliqué les poids, mais avant la fonction d'activation. En conséquence, on observe souvent une précision finale plus élevée et un entraînement plus rapide.

Voici le [papier original](https://arxiv.org/pdf/1502.03167.pdf) sur la normalisation par batch, la [explication sur Wikipedia](https://en.wikipedia.org/wiki/Batch_normalization), et [un bon article de blog introductif](https://towardsdatascience.com/batch-normalization-in-3-levels-of-understanding-14c2da90a338) (et un autre [en russe](https://habrahabr.ru/post/309302/)).

## Dropout

Le **dropout** est une technique intéressante qui supprime un certain pourcentage de neurones aléatoires pendant l'entraînement. C'est aussi implémenté comme une couche avec un paramètre (pourcentage de neurones à supprimer, typiquement 10 % à 50 %), et pendant l'entraînement elle met à zéro des éléments aléatoires du vecteur d'entrée, avant de le transmettre à la couche suivante.

Bien que cela puisse sembler une idée étrange, vous pouvez voir l'effet du dropout sur l'entraînement d'un classifieur de chiffres MNIST dans le notebook [`Dropout.ipynb`](Dropout.ipynb). Cela accélère l'entraînement et permet d'atteindre une meilleure précision en moins d'époques.

Cet effet peut s'expliquer de plusieurs façons :

 * On peut le considérer comme un facteur de choc aléatoire pour le modèle, qui sort l'optimisation d'un minimum local
 * On peut le considérer comme un *moyennage implicite du modèle*, car on peut dire qu'avec le dropout on entraîne un modèle légèrement différent

> *Certaines personnes disent que lorsqu'une personne ivre essaie d'apprendre quelque chose, elle s’en souviendra mieux le lendemain matin comparée à une personne sobre, car un cerveau avec certains neurones défaillants essaie de mieux s’adapter pour saisir le sens. Nous ne l’avons jamais testé nous-mêmes pour savoir si c’est vrai ou non*

## Prévenir le surapprentissage

Un des aspects très importants du deep learning est de pouvoir prévenir le [surapprentissage](../../3-NeuralNetworks/05-Frameworks/Overfitting.md). Bien qu'il puisse être tentant d'utiliser un modèle de réseau neuronal très puissant, nous devons toujours équilibrer le nombre de paramètres du modèle avec le nombre d'échantillons d'entraînement.

> Assurez-vous de bien comprendre le concept de [surapprentissage](../../3-NeuralNetworks/05-Frameworks/Overfitting.md) que nous avons introduit plus tôt !

Il existe plusieurs façons de prévenir le surapprentissage :

 * Arrêt précoce -- surveiller continuellement l'erreur sur le jeu de validation et arrêter l'entraînement lorsque l'erreur de validation commence à augmenter.
 * Décroissance/regularisation explicite des poids -- ajouter une pénalité supplémentaire à la fonction de perte pour les valeurs absolues élevées des poids, ce qui empêche le modèle d’obtenir des résultats très instables
 * Moyennage du modèle -- entraîner plusieurs modèles puis moyenniser le résultat. Cela aide à minimiser la variance.
 * Dropout (moyennage implicite du modèle)

## Optimiseurs / Algorithmes d'entraînement

Un autre aspect important de l'entraînement est de choisir un bon algorithme d'entraînement. Bien que la **descente de gradient** classique soit un choix raisonnable, elle peut parfois être trop lente ou entraîner d'autres problèmes.

En deep learning, nous utilisons la **descente de gradient stochastique** (SGD), qui est une descente de gradient appliquée à des mini-lots, sélectionnés aléatoirement à partir du jeu d'entraînement. Les poids sont ajustés en utilisant cette formule :

w<sup>t+1</sup> = w<sup>t</sup> - &eta;&nabla;&lagran;

### Momentum

En **momentum SGD**, nous conservons une partie du gradient des étapes précédentes. C'est similaire à lorsque nous nous déplaçons quelque part avec une inertie, et que nous recevons un coup dans une direction différente, notre trajectoire ne change pas immédiatement, mais conserve une partie du mouvement initial. Ici, nous introduisons un autre vecteur v pour représenter la *vitesse* :

* v<sup>t+1</sup> = &gamma; v<sup>t</sup> - &eta;&nabla;&lagran;
* w<sup>t+1</sup> = w<sup>t</sup>+v<sup>t+1</sup>

Ici, le paramètre &gamma; indique dans quelle mesure nous prenons en compte l'inertie : &gamma;=0 correspond au SGD classique ; &gamma;=1 est une équation pure de mouvement.

### Adam, Adagrad, etc.

Puisque dans chaque couche nous multiplions les signaux par une matrice W<sub>i</sub>, selon ||W<sub>i</sub>||, le gradient peut soit diminuer et devenir proche de 0, soit croître indéfiniment. C'est l'essence du problème des gradients explosifs / disparus.

Une des solutions à ce problème est d'utiliser uniquement la direction du gradient dans l'équation, en ignorant sa valeur absolue, c’est-à-dire

w<sup>t+1</sup> = w<sup>t</sup> - &eta;(&nabla;&lagran;/||&nabla;&lagran;||), où ||&nabla;&lagran;|| = &radic;&sum;(&nabla;&lagran;)<sup>2</sup>

Cet algorithme s'appelle **Adagrad**. D'autres algorithmes utilisant la même idée : **RMSProp**, **Adam**

> **Adam** est considéré comme un algorithme très efficace pour de nombreuses applications, donc si vous ne savez pas lequel utiliser - utilisez Adam.

### Découpage du gradient (gradient clipping)

Le découpage du gradient est une extension de l'idée ci-dessus. Lorsque ||&nabla;&lagran;|| &le; &theta;, nous considérons le gradient original dans l'optimisation des poids ; et lorsque ||&nabla;&lagran;|| > &theta;, nous divisons le gradient par sa norme. Ici, &theta; est un paramètre, dans la plupart des cas on peut prendre &theta;=1 ou &theta;=10.

### Décroissance du taux d'apprentissage

Le succès de l'entraînement dépend souvent du paramètre taux d'apprentissage &eta;. Il est logique de supposer que des valeurs grandes de &eta; entraînent un entraînement plus rapide, ce que nous désirons typiquement au début de l'entraînement, puis des valeurs plus petites de &eta; nous permettent d'affiner le réseau. Ainsi, dans la plupart des cas, nous voulons diminuer &eta; au cours de l'entraînement.

Cela peut se faire en multipliant &eta; par un certain nombre (par ex. 0.98) après chaque époque d'entraînement, ou en utilisant un **planning de taux d'apprentissage** plus compliqué.

## Différentes architectures de réseau

Choisir la bonne architecture de réseau pour votre problème peut être délicat. Normalement, nous prendrions une architecture qui a fait ses preuves pour notre tâche spécifique (ou similaire). Voici un [bon aperçu](https://www.topbots.com/a-brief-history-of-neural-network-architectures/) des architectures de réseaux neuronaux pour la vision par ordinateur.

> Il est important de choisir une architecture suffisamment puissante pour le nombre d'échantillons d'entraînement que nous avons. Choisir un modèle trop puissant peut entraîner du [surapprentissage](../../3-NeuralNetworks/05-Frameworks/Overfitting.md)

Une autre bonne méthode serait d'utiliser une architecture qui s'adapte automatiquement à la complexité requise. Dans une certaine mesure, les architectures **ResNet** et **Inception** s'ajustent d'elles-mêmes. [Plus sur les architectures pour la vision par ordinateur](../07-ConvNets/CNN_Architectures.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Avertissement** :
Ce document a été traduit à l'aide du service de traduction automatique [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforçions d'assurer l'exactitude, veuillez noter que les traductions automatisées peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue native doit être considéré comme la source faisant autorité. Pour les informations critiques, il est recommandé de recourir à une traduction professionnelle réalisée par un humain. Nous ne saurions être tenus responsables des malentendus ou erreurs d'interprétation découlant de l'utilisation de cette traduction.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->