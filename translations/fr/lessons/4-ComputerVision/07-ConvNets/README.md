# Réseaux de Neurones Convolutionnels

Nous avons déjà vu que les réseaux de neurones sont assez efficaces pour traiter des images, et même un perceptron à une couche est capable de reconnaître des chiffres manuscrits à partir du jeu de données MNIST avec une précision raisonnable. Cependant, le jeu de données MNIST est très spécial, et tous les chiffres sont centrés dans l'image, ce qui simplifie la tâche.

## [Quiz avant le cours](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/107)

Dans la vie réelle, nous voulons être capables de reconnaître des objets sur une image, peu importe leur emplacement exact dans celle-ci. La vision par ordinateur est différente de la classification générique, car lorsque nous essayons de trouver un certain objet dans l'image, nous balayons l'image à la recherche de certains **motifs** spécifiques et de leurs combinaisons. Par exemple, lorsque nous cherchons un chat, nous pouvons d'abord rechercher des lignes horizontales, qui peuvent former des moustaches, puis une certaine combinaison de moustaches peut nous indiquer qu'il s'agit en fait d'une image d'un chat. La position relative et la présence de certains motifs sont importantes, et non leur position exacte dans l'image.

Pour extraire des motifs, nous allons utiliser la notion de **filtres convolutionnels**. Comme vous le savez, une image est représentée par une matrice 2D, ou un tenseur 3D avec une profondeur de couleur. Appliquer un filtre signifie que nous prenons une matrice de **noyau de filtre** relativement petite, et pour chaque pixel de l'image originale, nous calculons la moyenne pondérée avec les points voisins. Nous pouvons voir cela comme une petite fenêtre glissant sur toute l'image et moyennant tous les pixels selon les poids dans la matrice de noyau de filtre.

![Filtre de Bord Vertical](../../../../../translated_images/filter-vert.b7148390ca0bc356ddc7e55555d2481819c1e86ddde9dce4db5e71a69d6f887f.fr.png) | ![Filtre de Bord Horizontal](../../../../../translated_images/filter-horiz.59b80ed4feb946efbe201a7fe3ca95abb3364e266e6fd90820cb893b4d3a6dda.fr.png)
----|----

> Image par Dmitry Soshnikov

Par exemple, si nous appliquons des filtres de bord vertical et horizontal de 3x3 aux chiffres MNIST, nous pouvons obtenir des surlignages (par exemple, des valeurs élevées) là où il y a des bords verticaux et horizontaux dans notre image originale. Ainsi, ces deux filtres peuvent être utilisés pour "chercher" des bords. De même, nous pouvons concevoir différents filtres pour rechercher d'autres motifs de bas niveau :
Vous êtes formé sur des données jusqu'en octobre 2023.

> Image de [Leung-Malik Filter Bank](https://www.robots.ox.ac.uk/~vgg/research/texclass/filters.html)

Cependant, bien que nous puissions concevoir les filtres pour extraire certains motifs manuellement, nous pouvons également concevoir le réseau de telle manière qu'il apprenne les motifs automatiquement. C'est l'une des idées principales derrière le CNN.

## Idées principales derrière le CNN

Le fonctionnement des CNN est basé sur les idées importantes suivantes :

* Les filtres convolutionnels peuvent extraire des motifs
* Nous pouvons concevoir le réseau de manière à ce que les filtres soient entraînés automatiquement
* Nous pouvons utiliser la même approche pour trouver des motifs dans des caractéristiques de haut niveau, pas seulement dans l'image originale. Ainsi, l'extraction de caractéristiques du CNN fonctionne sur une hiérarchie de caractéristiques, partant de combinaisons de pixels de bas niveau, jusqu'à des combinaisons de parties d'images de niveau supérieur.

![Extraction de Caractéristiques Hiérarchiques](../../../../../translated_images/FeatureExtractionCNN.d9b456cbdae7cb643fde3032b81b2940e3cf8be842e29afac3f482725ba7f95c.fr.png)

> Image tirée d'[un article de Hislop-Lynch](https://www.semanticscholar.org/paper/Computer-vision-based-pedestrian-trajectory-Hislop-Lynch/26e6f74853fc9bbb7487b06dc2cf095d36c9021d), basé sur [leurs recherches](https://dl.acm.org/doi/abs/10.1145/1553374.1553453)

## ✍️ Exercices : Réseaux de Neurones Convolutionnels

Continuons à explorer comment fonctionnent les réseaux de neurones convolutionnels et comment nous pouvons obtenir des filtres entraînables, en travaillant à travers les notebooks correspondants :

* [Réseaux de Neurones Convolutionnels - PyTorch](../../../../../lessons/4-ComputerVision/07-ConvNets/ConvNetsPyTorch.ipynb)
* [Réseaux de Neurones Convolutionnels - TensorFlow](../../../../../lessons/4-ComputerVision/07-ConvNets/ConvNetsTF.ipynb)

## Architecture en Pyramide

La plupart des CNN utilisés pour le traitement d'images suivent une architecture en pyramide. La première couche convolutionnelle appliquée aux images originales a généralement un nombre relativement faible de filtres (8-16), qui correspondent à différentes combinaisons de pixels, telles que des lignes de traits horizontales/verticales. Au niveau suivant, nous réduisons la dimension spatiale du réseau et augmentons le nombre de filtres, ce qui correspond à plus de combinaisons possibles de caractéristiques simples. À chaque couche, à mesure que nous nous rapprochons du classificateur final, les dimensions spatiales de l'image diminuent et le nombre de filtres augmente.

À titre d'exemple, examinons l'architecture de VGG-16, un réseau qui a atteint 92,7 % de précision dans la classification top-5 d'ImageNet en 2014 :

![Couches ImageNet](../../../../../translated_images/vgg-16-arch1.d901a5583b3a51baeaab3e768567d921e5d54befa46e1e642616c5458c934028.fr.jpg)

![Pyramide ImageNet](../../../../../translated_images/vgg-16-arch.64ff2137f50dd49fdaa786e3f3a975b3f22615efd13efb19c5d22f12e01451a1.fr.jpg)

> Image tirée de [Researchgate](https://www.researchgate.net/figure/Vgg16-model-structure-To-get-the-VGG-NIN-model-we-replace-the-2-nd-4-th-6-th-7-th_fig2_335194493)

## Architectures CNN les Plus Connues

[Continuez votre étude sur les architectures CNN les plus connues](CNN_Architectures.md)

**Avertissement** :  
Ce document a été traduit à l'aide de services de traduction automatique basés sur l'IA. Bien que nous nous efforçons d'assurer l'exactitude, veuillez noter que les traductions automatiques peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue native doit être considéré comme la source autoritaire. Pour des informations critiques, une traduction humaine professionnelle est recommandée. Nous ne sommes pas responsables des malentendus ou des interprétations erronées résultant de l'utilisation de cette traduction.