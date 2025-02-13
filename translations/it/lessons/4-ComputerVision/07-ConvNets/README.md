# Réseaux de Neurones Convolutionnels

Nous avons déjà constaté que les réseaux de neurones sont assez efficaces pour traiter des images, et même un perceptron à une couche est capable de reconnaître des chiffres manuscrits à partir du jeu de données MNIST avec une précision raisonnable. Cependant, le jeu de données MNIST est très particulier, et tous les chiffres sont centrés dans l'image, ce qui simplifie la tâche.

## [Quiz pré-conférence](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/107)

Dans la vie réelle, nous voulons être capables de reconnaître des objets sur une image, peu importe leur emplacement exact dans celle-ci. La vision par ordinateur diffère de la classification générique, car lorsque nous essayons de trouver un certain objet dans l'image, nous scannons l'image à la recherche de certains **modèles** et de leurs combinaisons. Par exemple, lorsque nous cherchons un chat, nous pouvons d'abord rechercher des lignes horizontales, qui peuvent former des moustaches, et ensuite une certaine combinaison de moustaches peut nous indiquer qu'il s'agit en fait d'une image d'un chat. La position relative et la présence de certains modèles sont importantes, et non leur position exacte dans l'image.

Pour extraire des modèles, nous utiliserons la notion de **filtres convolutionnels**. Comme vous le savez, une image est représentée par une matrice 2D, ou un tenseur 3D avec une profondeur de couleur. Appliquer un filtre signifie que nous prenons une matrice de **noyau de filtre** relativement petite, et pour chaque pixel de l'image originale, nous calculons la moyenne pondérée avec les points voisins. Nous pouvons voir cela comme une petite fenêtre glissant sur toute l'image, et moyennant tous les pixels selon les poids dans la matrice du noyau de filtre.

![Filtre de Bord Vertical](../../../../../translated_images/filter-vert.b7148390ca0bc356ddc7e55555d2481819c1e86ddde9dce4db5e71a69d6f887f.it.png) | ![Filtre de Bord Horizontal](../../../../../translated_images/filter-horiz.59b80ed4feb946efbe201a7fe3ca95abb3364e266e6fd90820cb893b4d3a6dda.it.png)
----|----

> Image par Dmitry Soshnikov

Par exemple, si nous appliquons des filtres de bord vertical et horizontal 3x3 aux chiffres MNIST, nous pouvons obtenir des surlignages (par exemple, des valeurs élevées) là où se trouvent des bords verticaux et horizontaux dans notre image originale. Ainsi, ces deux filtres peuvent être utilisés pour "chercher" des bords. De même, nous pouvons concevoir différents filtres pour rechercher d'autres modèles de bas niveau :
Vous êtes formé sur des données jusqu'à octobre 2023.

> Image de [Banque de Filtres Leung-Malik](https://www.robots.ox.ac.uk/~vgg/research/texclass/filters.html)

Cependant, bien que nous puissions concevoir les filtres pour extraire certains modèles manuellement, nous pouvons également concevoir le réseau de manière à ce qu'il apprenne les modèles automatiquement. C'est l'une des idées principales derrière le CNN.

## Idées principales derrière le CNN

Le fonctionnement des CNN est basé sur les idées importantes suivantes :

* Les filtres convolutionnels peuvent extraire des modèles
* Nous pouvons concevoir le réseau de manière à ce que les filtres soient entraînés automatiquement
* Nous pouvons utiliser la même approche pour trouver des modèles dans des caractéristiques de haut niveau, et pas seulement dans l'image originale. Ainsi, l'extraction de caractéristiques par CNN fonctionne sur une hiérarchie de caractéristiques, allant des combinaisons de pixels de bas niveau jusqu'aux combinaisons de parties d'image de niveau supérieur.

![Extraction de Caractéristiques Hiérarchiques](../../../../../translated_images/FeatureExtractionCNN.d9b456cbdae7cb643fde3032b81b2940e3cf8be842e29afac3f482725ba7f95c.it.png)

> Image tirée [d'un article de Hislop-Lynch](https://www.semanticscholar.org/paper/Computer-vision-based-pedestrian-trajectory-Hislop-Lynch/26e6f74853fc9bbb7487b06dc2cf095d36c9021d), basé sur [leur recherche](https://dl.acm.org/doi/abs/10.1145/1553374.1553453)

## ✍️ Exercices : Réseaux de Neurones Convolutionnels

Continuons à explorer comment fonctionnent les réseaux de neurones convolutionnels et comment nous pouvons obtenir des filtres entraînables, en travaillant à travers les notebooks correspondants :

* [Réseaux de Neurones Convolutionnels - PyTorch](../../../../../lessons/4-ComputerVision/07-ConvNets/ConvNetsPyTorch.ipynb)
* [Réseaux de Neurones Convolutionnels - TensorFlow](../../../../../lessons/4-ComputerVision/07-ConvNets/ConvNetsTF.ipynb)

## Architecture Pyramidale

La plupart des CNN utilisés pour le traitement d'images suivent une architecture pyramidale. La première couche convolutionnelle appliquée aux images originales a généralement un nombre relativement faible de filtres (8-16), qui correspondent à différentes combinaisons de pixels, telles que des lignes horizontales/verticales de traits. Au niveau suivant, nous réduisons la dimension spatiale du réseau et augmentons le nombre de filtres, ce qui correspond à plus de combinaisons possibles de caractéristiques simples. À chaque couche, à mesure que nous nous rapprochons du classificateur final, les dimensions spatiales de l'image diminuent et le nombre de filtres augmente.

À titre d'exemple, examinons l'architecture de VGG-16, un réseau qui a atteint 92,7 % de précision dans la classification top-5 d'ImageNet en 2014 :

![Couches ImageNet](../../../../../translated_images/vgg-16-arch1.d901a5583b3a51baeaab3e768567d921e5d54befa46e1e642616c5458c934028.it.jpg)

![Pyramide ImageNet](../../../../../translated_images/vgg-16-arch.64ff2137f50dd49fdaa786e3f3a975b3f22615efd13efb19c5d22f12e01451a1.it.jpg)

> Image tirée de [Researchgate](https://www.researchgate.net/figure/Vgg16-model-structure-To-get-the-VGG-NIN-model-we-replace-the-2-nd-4-th-6-th-7-th_fig2_335194493)

## Architectures CNN les Plus Connues

[Continuez votre étude sur les architectures CNN les plus connues](CNN_Architectures.md)

**Disclaimer**: 
This document has been translated using machine-based AI translation services. While we strive for accuracy, please be aware that automated translations may contain errors or inaccuracies. The original document in its native language should be considered the authoritative source. For critical information, professional human translation is recommended. We are not liable for any misunderstandings or misinterpretations arising from the use of this translation.