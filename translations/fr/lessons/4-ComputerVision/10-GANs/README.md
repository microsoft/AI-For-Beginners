# Réseaux Antagonistes Génératifs

Dans la section précédente, nous avons appris sur les **modèles génératifs** : des modèles capables de générer de nouvelles images similaires à celles du jeu de données d'entraînement. Le VAE était un bon exemple de modèle génératif.

## [Quiz pré-cours](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/110)

Cependant, si nous essayons de générer quelque chose de vraiment significatif, comme une peinture à une résolution raisonnable, avec un VAE, nous verrons que l'entraînement ne converge pas bien. Pour ce cas d'utilisation, nous devrions nous renseigner sur une autre architecture spécifiquement destinée aux modèles génératifs - **Réseaux Antagonistes Génératifs**, ou GANs.

L'idée principale d'un GAN est d'avoir deux réseaux neuronaux qui seront entraînés l'un contre l'autre :

<img src="images/gan_architecture.png" width="70%"/>

> Image par [Dmitry Soshnikov](http://soshnikov.com)

> ✅ Un petit vocabulaire :
> * **Générateur** est un réseau qui prend un vecteur aléatoire et produit l'image en résultat
> * **Discriminateur** est un réseau qui prend une image et doit dire si c'est une image réelle (du jeu de données d'entraînement) ou si elle a été générée par un générateur. C'est essentiellement un classificateur d'images.

### Discriminateur

L'architecture du discriminateur ne diffère pas d'un réseau de classification d'images ordinaire. Dans le cas le plus simple, il peut s'agir d'un classificateur entièrement connecté, mais très probablement, il s'agira d'un [réseau de convolution](../07-ConvNets/README.md).

> ✅ Un GAN basé sur des réseaux de convolution est appelé un [DCGAN](https://arxiv.org/pdf/1511.06434.pdf)

Un discriminateur CNN se compose des couches suivantes : plusieurs convolutions+poolings (avec une taille spatiale décroissante) et une ou plusieurs couches entièrement connectées pour obtenir un "vecteur de caractéristiques", le classificateur binaire final.

> ✅ Un 'pooling' dans ce contexte est une technique qui réduit la taille de l'image. "Les couches de pooling réduisent les dimensions des données en combinant les sorties des clusters de neurones à une couche en un seul neurone à la couche suivante." - [source](https://wikipedia.org/wiki/Convolutional_neural_network#Pooling_layers)

### Générateur

Un générateur est légèrement plus complexe. Vous pouvez le considérer comme un discriminateur inversé. Partant d'un vecteur latent (à la place d'un vecteur de caractéristiques), il a une couche entièrement connectée pour le convertir en la taille/forme requise, suivie de déconvolutions+upsampling. Cela ressemble à la partie *décodeur* de l'[autoencodeur](../09-Autoencoders/README.md).

> ✅ Comme la couche de convolution est implémentée comme un filtre linéaire parcourant l'image, la déconvolution est essentiellement similaire à la convolution et peut être implémentée en utilisant la même logique de couche.

<img src="images/gan_arch_detail.png" width="70%"/>

> Image par [Dmitry Soshnikov](http://soshnikov.com)

### Entraînement du GAN

Les GANs sont appelés **antagonistes** car il y a une compétition constante entre le générateur et le discriminateur. Au cours de cette compétition, le générateur et le discriminateur s'améliorent, ainsi le réseau apprend à produire des images de meilleure qualité.

L'entraînement se déroule en deux étapes :

* **Entraînement du discriminateur**. Cette tâche est assez simple : nous générons un lot d'images par le générateur, les étiquetons 0, ce qui représente une image fausse, et prenons un lot d'images du jeu de données d'entrée (avec l'étiquette 1, image réelle). Nous obtenons une *perte du discriminateur*, et effectuons une rétropropagation.
* **Entraînement du générateur**. Cela est légèrement plus délicat, car nous ne connaissons pas directement la sortie attendue pour le générateur. Nous prenons l'ensemble du réseau GAN constitué d'un générateur suivi d'un discriminateur, le nourrissons avec des vecteurs aléatoires, et nous attendons que le résultat soit 1 (correspondant aux images réelles). Nous figeons ensuite les paramètres du discriminateur (nous ne voulons pas qu'il soit entraîné à cette étape), et effectuons la rétropropagation.

Au cours de ce processus, les pertes du générateur et du discriminateur ne diminuent pas significativement. Dans une situation idéale, elles devraient osciller, correspondant à l'amélioration des performances des deux réseaux.

## ✍️ Exercices : GANs

* [Notebook GAN en TensorFlow/Keras](../../../../../lessons/4-ComputerVision/10-GANs/GANTF.ipynb)
* [Notebook GAN en PyTorch](../../../../../lessons/4-ComputerVision/10-GANs/GANPyTorch.ipynb)

### Problèmes avec l'entraînement des GAN

Les GANs sont connus pour être particulièrement difficiles à entraîner. Voici quelques problèmes :

* **Effondrement de mode**. Par ce terme, nous entendons que le générateur apprend à produire une image réussie qui trompe le discriminateur, et non une variété d'images différentes.
* **Sensibilité aux hyperparamètres**. Souvent, vous pouvez voir qu'un GAN ne converge pas du tout, puis soudainement diminue dans le taux d'apprentissage conduisant à la convergence.
* Maintenir un **équilibre** entre le générateur et le discriminateur. Dans de nombreux cas, la perte du discriminateur peut tomber à zéro relativement rapidement, ce qui empêche le générateur de s'entraîner davantage. Pour surmonter cela, nous pouvons essayer de définir différents taux d'apprentissage pour le générateur et le discriminateur, ou sauter l'entraînement du discriminateur si la perte est déjà trop basse.
* Entraînement pour une **haute résolution**. Réfléchissant au même problème qu'avec les autoencodeurs, ce problème est déclenché car reconstruire trop de couches de réseau de convolution conduit à des artefacts. Ce problème est généralement résolu par ce qu'on appelle la **croissance progressive**, lorsque d'abord quelques couches sont entraînées sur des images basse résolution, puis les couches sont "débloquées" ou ajoutées. Une autre solution consisterait à ajouter des connexions supplémentaires entre les couches et à entraîner plusieurs résolutions à la fois - voir cet article sur les [GANs à gradient multi-échelle](https://arxiv.org/abs/1903.06048) pour plus de détails.

## Transfert de style

Les GANs sont un excellent moyen de générer des images artistiques. Une autre technique intéressante est le **transfert de style**, qui prend une **image de contenu** et la redessine dans un style différent, appliquant des filtres de l'**image de style**.

Le fonctionnement est le suivant :
* Nous commençons avec une image de bruit aléatoire (ou avec une image de contenu, mais pour mieux comprendre, il est plus facile de commencer par du bruit aléatoire)
* Notre objectif serait de créer une image qui serait proche à la fois de l'image de contenu et de l'image de style. Cela serait déterminé par deux fonctions de perte :
   - La **perte de contenu** est calculée en fonction des caractéristiques extraites par le CNN à certaines couches de l'image actuelle et de l'image de contenu
   - La **perte de style** est calculée entre l'image actuelle et l'image de style de manière astucieuse en utilisant des matrices de Gram (plus de détails dans le [notebook exemple](../../../../../lessons/4-ComputerVision/10-GANs/StyleTransfer.ipynb))
* Pour rendre l'image plus lisse et éliminer le bruit, nous introduisons également une **perte de variation**, qui calcule la distance moyenne entre les pixels voisins
* La boucle d'optimisation principale ajuste l'image actuelle en utilisant la descente de gradient (ou un autre algorithme d'optimisation) pour minimiser la perte totale, qui est une somme pondérée de toutes les trois pertes.

## ✍️ Exemple : [Transfert de style](../../../../../lessons/4-ComputerVision/10-GANs/StyleTransfer.ipynb)

## [Quiz post-cours](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/210)

## Conclusion

Dans cette leçon, vous avez appris sur les GANs et comment les entraîner. Vous avez également appris les défis particuliers que ce type de réseau de neurones peut rencontrer, ainsi que quelques stratégies pour les surmonter.

## 🚀 Défi

Parcourez le [notebook de transfert de style](../../../../../lessons/4-ComputerVision/10-GANs/StyleTransfer.ipynb) en utilisant vos propres images.

## Révision et auto-apprentissage

Pour référence, lisez-en plus sur les GANs dans ces ressources :

* Marco Pasini, [10 leçons que j'ai apprises en entraînant des GANs pendant un an](https://towardsdatascience.com/10-lessons-i-learned-training-generative-adversarial-networks-gans-for-a-year-c9071159628)
* [StyleGAN](https://en.wikipedia.org/wiki/StyleGAN), une architecture GAN à considérer
* [Créer de l'art génératif avec des GANs sur Azure ML](https://soshnikov.com/scienceart/creating-generative-art-using-gan-on-azureml/)

## Assignment

Revisitez l'un des deux notebooks associés à cette leçon et réentraînez le GAN sur vos propres images. Que pouvez-vous créer ?

**Avertissement** :  
Ce document a été traduit à l'aide de services de traduction automatique basés sur l'IA. Bien que nous visons à l'exactitude, veuillez noter que les traductions automatisées peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue native doit être considéré comme la source faisant autorité. Pour des informations critiques, une traduction humaine professionnelle est recommandée. Nous ne sommes pas responsables des malentendus ou des interprétations erronées résultant de l'utilisation de cette traduction.