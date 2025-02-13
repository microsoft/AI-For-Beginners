# Astuces pour l'entraînement en Deep Learning

À mesure que les réseaux neuronaux deviennent plus profonds, le processus de leur entraînement devient de plus en plus complexe. Un problème majeur est le phénomène des [gradients qui disparaissent](https://en.wikipedia.org/wiki/Vanishing_gradient_problem) ou des [gradients explosifs](https://deepai.org/machine-learning-glossary-and-terms/exploding-gradient-problem#:~:text=Exploding%20gradients%20are%20a%20problem,updates%20are%20small%20and%20controlled.). [Cet article](https://towardsdatascience.com/the-vanishing-exploding-gradient-problem-in-deep-neural-networks-191358470c11) offre une bonne introduction à ces problèmes.

Pour rendre l'entraînement des réseaux profonds plus efficace, il existe quelques techniques à utiliser.

## Maintenir les valeurs dans un intervalle raisonnable

Pour rendre les calculs numériques plus stables, nous voulons nous assurer que toutes les valeurs au sein de notre réseau neuronal sont dans une échelle raisonnable, généralement [-1..1] ou [0..1]. Ce n'est pas une exigence très stricte, mais la nature des calculs en virgule flottante fait que des valeurs de différentes magnitudes ne peuvent pas être manipulées avec précision ensemble. Par exemple, si nous ajoutons 10<sup>-10</sup> et 10<sup>10</sup>, nous obtiendrons probablement 10<sup>10</sup>, car la valeur plus petite serait "convertie" au même ordre que la plus grande, et ainsi la mantisse serait perdue.

La plupart des fonctions d'activation ont des non-linéarités autour de [-1..1], et il est donc logique de mettre à l'échelle toutes les données d'entrée dans l'intervalle [-1..1] ou [0..1].

## Initialisation des poids

Idéalement, nous voulons que les valeurs soient dans la même plage après avoir traversé les couches du réseau. Il est donc important d'initialiser les poids de manière à préserver la distribution des valeurs.

La distribution normale **N(0,1)** n'est pas une bonne idée, car si nous avons *n* entrées, l'écart type de la sortie serait *n*, et les valeurs risquent de sortir de l'intervalle [0..1].

Les initialisations suivantes sont souvent utilisées :

 * Distribution uniforme -- `uniform`
 * **N(0,1/n)** -- `gaussian`
 * **N(0,1/√n_in)** garantit que pour des entrées avec une moyenne nulle et un écart type de 1, la même moyenne/écart type sera maintenue
 * **N(0,√2/(n_in+n_out))** -- ce qu'on appelle **initialisation Xavier** (`glorot`), cela aide à maintenir les signaux dans la plage pendant la propagation avant et arrière

## Normalisation par lots

Même avec une bonne initialisation des poids, ceux-ci peuvent devenir arbitrairement grands ou petits pendant l'entraînement, et ils feront sortir les signaux de la plage appropriée. Nous pouvons ramener les signaux en utilisant l'une des techniques de **normalisation**. Bien qu'il en existe plusieurs (normalisation des poids, normalisation de couche), la plus couramment utilisée est la normalisation par lots.

L'idée de la **normalisation par lots** est de prendre en compte toutes les valeurs à travers le mini-batch et de réaliser la normalisation (c'est-à-dire soustraire la moyenne et diviser par l'écart type) en fonction de ces valeurs. Cela est implémenté comme une couche de réseau qui effectue cette normalisation après l'application des poids, mais avant la fonction d'activation. En conséquence, nous sommes susceptibles de voir une précision finale plus élevée et un entraînement plus rapide.

Voici le [document original](https://arxiv.org/pdf/1502.03167.pdf) sur la normalisation par lots, l'[explication sur Wikipedia](https://en.wikipedia.org/wiki/Batch_normalization), et [un bon article de blog introductif](https://towardsdatascience.com/batch-normalization-in-3-levels-of-understanding-14c2da90a338) (et celui [en russe](https://habrahabr.ru/post/309302/)).

## Dropout

Le **dropout** est une technique intéressante qui supprime un certain pourcentage de neurones aléatoires pendant l'entraînement. Elle est également implémentée comme une couche avec un paramètre (pourcentage de neurones à supprimer, généralement de 10 % à 50 %), et pendant l'entraînement, elle annule des éléments aléatoires du vecteur d'entrée avant de le transmettre à la couche suivante.

Bien que cela puisse sembler une idée étrange, vous pouvez voir l'effet du dropout sur l'entraînement d'un classificateur de chiffres MNIST dans le carnet [`Dropout.ipynb`](../../../../../lessons/4-ComputerVision/08-TransferLearning/Dropout.ipynb). Cela accélère l'entraînement et nous permet d'atteindre une précision plus élevée en moins d'époques d'entraînement.

Cet effet peut être expliqué de plusieurs manières :

 * Cela peut être considéré comme un facteur de choc aléatoire pour le modèle, qui sort l'optimisation d'un minimum local
 * Cela peut être considéré comme un *moyennage implicite du modèle*, car nous pouvons dire qu'au cours du dropout, nous entraînons un modèle légèrement différent

> *Certaines personnes disent que lorsqu'une personne ivre essaie d'apprendre quelque chose, elle s'en souviendra mieux le lendemain matin, par rapport à une personne sobre, parce qu'un cerveau avec des neurones dysfonctionnels essaie de s'adapter mieux pour saisir le sens. Nous n'avons jamais testé nous-mêmes si cela est vrai ou non.*

## Prévenir le surajustement

Un des aspects très importants du deep learning est d'être capable de prévenir le [surajustement](../../3-NeuralNetworks/05-Frameworks/Overfitting.md). Bien qu'il puisse être tentant d'utiliser un modèle de réseau neuronal très puissant, nous devrions toujours équilibrer le nombre de paramètres du modèle avec le nombre d'échantillons d'entraînement.

> Assurez-vous de bien comprendre le concept de [surajustement](../../3-NeuralNetworks/05-Frameworks/Overfitting.md) que nous avons introduit précédemment !

Il existe plusieurs façons de prévenir le surajustement :

 * Arrêt précoce -- surveiller continuellement l'erreur sur l'ensemble de validation et arrêter l'entraînement lorsque l'erreur de validation commence à augmenter.
 * Décroissance de poids explicite / Régularisation -- ajout d'une pénalité supplémentaire à la fonction de perte pour des valeurs absolues élevées des poids, ce qui empêche le modèle d'obtenir des résultats très instables
 * Moyennage de modèles -- entraîner plusieurs modèles et ensuite moyenniser les résultats. Cela aide à minimiser la variance.
 * Dropout (Moyennage implicite du modèle)

## Optimisateurs / Algorithmes d'entraînement

Un autre aspect important de l'entraînement est de choisir un bon algorithme d'entraînement. Bien que la **descente de gradient** classique soit un choix raisonnable, elle peut parfois être trop lente ou entraîner d'autres problèmes.

En deep learning, nous utilisons la **descente de gradient stochastique** (SGD), qui est une descente de gradient appliquée aux mini-batchs, sélectionnés aléatoirement dans l'ensemble d'entraînement. Les poids sont ajustés à l'aide de cette formule :

w<sup>t+1</sup> = w<sup>t</sup> - η∇ℒ

### Momentum

Dans le **momentum SGD**, nous conservons une partie d'un gradient des étapes précédentes. C'est similaire à lorsque nous nous déplaçons avec une inertie, et que nous recevons un coup dans une direction différente, notre trajectoire ne change pas immédiatement, mais conserve une partie du mouvement original. Ici, nous introduisons un autre vecteur v pour représenter la *vitesse* :

* v<sup>t+1</sup> = γ v<sup>t</sup> - η∇ℒ
* w<sup>t+1</sup> = w<sup>t</sup> + v<sup>t+1</sup>

Ici, le paramètre γ indique dans quelle mesure nous prenons en compte l'inertie : γ=0 correspond à la SGD classique ; γ=1 est une équation de mouvement pure.

### Adam, Adagrad, etc.

Puisque dans chaque couche nous multiplions les signaux par une matrice W<sub>i</sub>, selon ||W<sub>i</sub>||, le gradient peut soit diminuer et être proche de 0, soit augmenter indéfiniment. C'est l'essence du problème des gradients explosifs/disparus.

Une des solutions à ce problème est d'utiliser uniquement la direction du gradient dans l'équation, et d'ignorer la valeur absolue, c'est-à-dire :

w<sup>t+1</sup> = w<sup>t</sup> - η(∇ℒ/||∇ℒ||), où ||∇ℒ|| = √∑(∇ℒ)<sup>2</sup>

Cet algorithme s'appelle **Adagrad**. D'autres algorithmes qui utilisent la même idée : **RMSProp**, **Adam**.

> **Adam** est considéré comme un algorithme très efficace pour de nombreuses applications, donc si vous n'êtes pas sûr du modèle à utiliser - utilisez Adam.

### Découpage de gradient

Le découpage de gradient est une extension de l'idée ci-dessus. Lorsque ||∇ℒ|| ≤ θ, nous considérons le gradient original dans l'optimisation des poids, et lorsque ||∇ℒ|| > θ - nous divisons le gradient par sa norme. Ici, θ est un paramètre, dans la plupart des cas, nous pouvons prendre θ=1 ou θ=10.

### Décroissance du taux d'apprentissage

Le succès de l'entraînement dépend souvent du paramètre de taux d'apprentissage η. Il est logique de supposer que des valeurs plus grandes de η entraînent un entraînement plus rapide, ce qui est quelque chose que nous voulons généralement au début de l'entraînement, et ensuite une valeur plus petite de η nous permet de peaufiner le réseau. Ainsi, dans la plupart des cas, nous voulons diminuer η au cours de l'entraînement.

Cela peut être fait en multipliant η par un certain nombre (par exemple 0.98) après chaque époque d'entraînement, ou en utilisant un **planning de taux d'apprentissage** plus complexe.

## Différentes architectures de réseau

Sélectionner la bonne architecture de réseau pour votre problème peut être délicat. Normalement, nous choisirions une architecture qui a prouvé son efficacité pour notre tâche spécifique (ou une tâche similaire). Voici un [bon aperçu](https://www.topbots.com/a-brief-history-of-neural-network-architectures/) des architectures de réseaux neuronaux pour la vision par ordinateur.

> Il est important de sélectionner une architecture qui sera suffisamment puissante pour le nombre d'échantillons d'entraînement que nous avons. Choisir un modèle trop puissant peut entraîner un [surajustement](../../3-NeuralNetworks/05-Frameworks/Overfitting.md).

Une autre bonne méthode serait d'utiliser une architecture qui s'ajustera automatiquement à la complexité requise. Dans une certaine mesure, les architectures **ResNet** et **Inception** sont auto-ajustables. [Plus sur les architectures de vision par ordinateur](../07-ConvNets/CNN_Architectures.md).

**Avertissement** :  
Ce document a été traduit à l'aide de services de traduction automatique basés sur l'IA. Bien que nous nous efforçons d'assurer l'exactitude, veuillez noter que les traductions automatiques peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue native doit être considéré comme la source autoritaire. Pour des informations critiques, une traduction humaine professionnelle est recommandée. Nous ne sommes pas responsables des malentendus ou des interprétations erronées résultant de l'utilisation de cette traduction.