<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "088837b42b7d99198bf62db8a42411e0",
  "translation_date": "2025-08-24T20:51:30+00:00",
  "source_file": "lessons/4-ComputerVision/07-ConvNets/README.md",
  "language_code": "fr"
}
-->
# Réseaux de Neurones Convolutionnels

Nous avons vu précédemment que les réseaux de neurones sont assez performants pour traiter des images, et même un perceptron à une seule couche est capable de reconnaître des chiffres manuscrits du jeu de données MNIST avec une précision raisonnable. Cependant, le jeu de données MNIST est très particulier, car tous les chiffres y sont centrés dans l'image, ce qui simplifie la tâche.

## [Quiz avant le cours](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/107)

Dans la vie réelle, nous souhaitons pouvoir reconnaître des objets sur une image, peu importe leur emplacement exact. La vision par ordinateur diffère de la classification générique, car lorsque nous cherchons un objet spécifique dans une image, nous analysons celle-ci à la recherche de certains **motifs** et de leurs combinaisons. Par exemple, en cherchant un chat, nous pouvons d'abord repérer des lignes horizontales qui pourraient former des moustaches, puis une certaine combinaison de moustaches peut nous indiquer qu'il s'agit effectivement d'une image de chat. La position relative et la présence de certains motifs sont importantes, mais pas leur emplacement exact dans l'image.

Pour extraire des motifs, nous utiliserons la notion de **filtres convolutionnels**. Comme vous le savez, une image est représentée par une matrice 2D ou un tenseur 3D avec une profondeur de couleur. Appliquer un filtre signifie que nous prenons une petite matrice appelée **noyau de filtre**, et pour chaque pixel de l'image originale, nous calculons la moyenne pondérée avec les points voisins. On peut imaginer cela comme une petite fenêtre glissant sur toute l'image et moyennant tous les pixels selon les poids du noyau de filtre.

![Filtre de bord vertical](../../../../../translated_images/filter-vert.b7148390ca0bc356ddc7e55555d2481819c1e86ddde9dce4db5e71a69d6f887f.fr.png) | ![Filtre de bord horizontal](../../../../../translated_images/filter-horiz.59b80ed4feb946efbe201a7fe3ca95abb3364e266e6fd90820cb893b4d3a6dda.fr.png)
----|----

> Image par Dmitry Soshnikov

Par exemple, si nous appliquons des filtres de bord vertical et horizontal 3x3 aux chiffres du MNIST, nous pouvons obtenir des zones mises en évidence (par exemple, des valeurs élevées) là où se trouvent des bords verticaux et horizontaux dans notre image originale. Ainsi, ces deux filtres peuvent être utilisés pour "chercher" des bords. De la même manière, nous pouvons concevoir différents filtres pour rechercher d'autres motifs de bas niveau :

> Image de [Leung-Malik Filter Bank](https://www.robots.ox.ac.uk/~vgg/research/texclass/filters.html)

Cependant, bien que nous puissions concevoir manuellement des filtres pour extraire certains motifs, nous pouvons également concevoir le réseau de manière à ce qu'il apprenne les motifs automatiquement. C'est l'une des idées principales derrière les CNN.

## Idées principales des CNN

Le fonctionnement des CNN repose sur les idées importantes suivantes :

* Les filtres convolutionnels peuvent extraire des motifs.
* Nous pouvons concevoir le réseau de manière à ce que les filtres soient entraînés automatiquement.
* Nous pouvons utiliser la même approche pour trouver des motifs dans des caractéristiques de haut niveau, et pas seulement dans l'image originale. Ainsi, l'extraction de caractéristiques par les CNN fonctionne sur une hiérarchie de caractéristiques, allant des combinaisons de pixels de bas niveau jusqu'aux combinaisons de parties d'image de haut niveau.

![Extraction hiérarchique de caractéristiques](../../../../../translated_images/FeatureExtractionCNN.d9b456cbdae7cb643fde3032b81b2940e3cf8be842e29afac3f482725ba7f95c.fr.png)

> Image tirée [d'un article de Hislop-Lynch](https://www.semanticscholar.org/paper/Computer-vision-based-pedestrian-trajectory-Hislop-Lynch/26e6f74853fc9bbb7487b06dc2cf095d36c9021d), basé sur [leurs recherches](https://dl.acm.org/doi/abs/10.1145/1553374.1553453)

## ✍️ Exercices : Réseaux de Neurones Convolutionnels

Continuons à explorer le fonctionnement des réseaux de neurones convolutionnels et comment nous pouvons obtenir des filtres entraînables, en travaillant sur les notebooks correspondants :

* [Réseaux de Neurones Convolutionnels - PyTorch](../../../../../lessons/4-ComputerVision/07-ConvNets/ConvNetsPyTorch.ipynb)
* [Réseaux de Neurones Convolutionnels - TensorFlow](../../../../../lessons/4-ComputerVision/07-ConvNets/ConvNetsTF.ipynb)

## Architecture Pyramidale

La plupart des CNN utilisés pour le traitement d'images suivent une architecture dite pyramidale. La première couche convolutionnelle appliquée aux images originales comporte généralement un nombre relativement faible de filtres (8-16), qui correspondent à différentes combinaisons de pixels, telles que des lignes horizontales ou verticales. Au niveau suivant, nous réduisons la dimension spatiale du réseau et augmentons le nombre de filtres, ce qui correspond à davantage de combinaisons possibles de caractéristiques simples. À chaque couche, à mesure que nous nous rapprochons du classificateur final, les dimensions spatiales de l'image diminuent et le nombre de filtres augmente.

À titre d'exemple, examinons l'architecture de VGG-16, un réseau qui a atteint une précision de 92,7 % dans la classification top-5 d'ImageNet en 2014 :

![Couches d'ImageNet](../../../../../translated_images/vgg-16-arch1.d901a5583b3a51baeaab3e768567d921e5d54befa46e1e642616c5458c934028.fr.jpg)

![Pyramide d'ImageNet](../../../../../translated_images/vgg-16-arch.64ff2137f50dd49fdaa786e3f3a975b3f22615efd13efb19c5d22f12e01451a1.fr.jpg)

> Image tirée de [Researchgate](https://www.researchgate.net/figure/Vgg16-model-structure-To-get-the-VGG-NIN-model-we-replace-the-2-nd-4-th-6-th-7-th_fig2_335194493)

## Architectures CNN les plus connues

[Continuez votre étude des architectures CNN les plus connues](CNN_Architectures.md)

**Avertissement** :  
Ce document a été traduit à l'aide du service de traduction automatique [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforcions d'assurer l'exactitude, veuillez noter que les traductions automatisées peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue d'origine doit être considéré comme la source faisant autorité. Pour des informations critiques, il est recommandé de recourir à une traduction humaine professionnelle. Nous déclinons toute responsabilité en cas de malentendus ou d'interprétations erronées résultant de l'utilisation de cette traduction.