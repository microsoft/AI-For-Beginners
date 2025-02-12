# Architectures CNN Bien Connues

### VGG-16

VGG-16 est un réseau qui a atteint 92,7 % de précision dans la classification top-5 d'ImageNet en 2014. Il a la structure de couches suivante :

![Couches ImageNet](../../../../../translated_images/vgg-16-arch1.d901a5583b3a51baeaab3e768567d921e5d54befa46e1e642616c5458c934028.fr.jpg)

Comme vous pouvez le voir, VGG suit une architecture pyramidale traditionnelle, qui est une séquence de couches de convolution et de pooling.

![Pyramide ImageNet](../../../../../translated_images/vgg-16-arch.64ff2137f50dd49fdaa786e3f3a975b3f22615efd13efb19c5d22f12e01451a1.fr.jpg)

> Image de [Researchgate](https://www.researchgate.net/figure/Vgg16-model-structure-To-get-the-VGG-NIN-model-we-replace-the-2-nd-4-th-6-th-7-th_fig2_335194493)

### ResNet

ResNet est une famille de modèles proposée par Microsoft Research en 2015. L'idée principale de ResNet est d'utiliser des **blocs résiduels** :

<img src="images/resnet-block.png" width="300"/>

> Image de [cet article](https://arxiv.org/pdf/1512.03385.pdf)

La raison d'utiliser un passage identitaire est de faire en sorte que notre couche prédit **la différence** entre le résultat d'une couche précédente et la sortie du bloc résiduel - d'où le nom *résiduel*. Ces blocs sont beaucoup plus faciles à entraîner, et on peut construire des réseaux avec plusieurs centaines de ces blocs (les variantes les plus courantes sont ResNet-52, ResNet-101 et ResNet-152).

Vous pouvez également penser à ce réseau comme étant capable d'ajuster sa complexité au jeu de données. Au début, lorsque vous commencez à entraîner le réseau, les valeurs des poids sont faibles, et la plupart du signal passe à travers des couches identitaires. À mesure que l'entraînement progresse et que les poids deviennent plus grands, l'importance des paramètres du réseau augmente, et le réseau s'ajuste pour s'adapter à la puissance expressive requise pour classer correctement les images d'entraînement.

### Google Inception

L'architecture Google Inception pousse cette idée un peu plus loin et construit chaque couche du réseau comme une combinaison de plusieurs chemins différents :

<img src="images/inception.png" width="400"/>

> Image de [Researchgate](https://www.researchgate.net/figure/Inception-module-with-dimension-reductions-left-and-schema-for-Inception-ResNet-v1_fig2_355547454)

Ici, nous devons souligner le rôle des convolutions 1x1, car au premier abord, elles n'ont pas de sens. Pourquoi devrions-nous parcourir l'image avec un filtre 1x1 ? Cependant, vous devez vous rappeler que les filtres de convolution fonctionnent également avec plusieurs canaux de profondeur (à l'origine - couleurs RGB, dans les couches suivantes - canaux pour différents filtres), et la convolution 1x1 est utilisée pour mélanger ces canaux d'entrée ensemble en utilisant différents poids entraînables. Cela peut également être considéré comme un sous-échantillonnage (pooling) sur la dimension des canaux.

Voici [un bon article de blog](https://medium.com/analytics-vidhya/talented-mr-1x1-comprehensive-look-at-1x1-convolution-in-deep-learning-f6b355825578) sur le sujet, et [l'article original](https://arxiv.org/pdf/1312.4400.pdf).

### MobileNet

MobileNet est une famille de modèles de taille réduite, adaptés aux appareils mobiles. Utilisez-les si vous manquez de ressources et pouvez sacrifier un peu de précision. L'idée principale derrière eux est la **convolution séparablement en profondeur**, qui permet de représenter les filtres de convolution par une composition de convolutions spatiales et de convolutions 1x1 sur les canaux de profondeur. Cela réduit considérablement le nombre de paramètres, rendant le réseau plus petit en taille et également plus facile à entraîner avec moins de données.

Voici [un bon article de blog sur MobileNet](https://medium.com/analytics-vidhya/image-classification-with-mobilenet-cc6fbb2cd470).

## Conclusion

Dans cette unité, vous avez appris le concept principal derrière les réseaux neuronaux en vision par ordinateur - les réseaux de convolution. Les architectures réelles qui alimentent la classification d'images, la détection d'objets et même les réseaux de génération d'images sont toutes basées sur les CNN, mais avec plus de couches et quelques astuces d'entraînement supplémentaires.

## 🚀 Défi

Dans les notebooks accompagnants, il y a des notes en bas sur la façon d'obtenir une précision plus élevée. Faites quelques expériences pour voir si vous pouvez atteindre une précision supérieure.

## [Quiz post-conférence](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/207)

## Revue & Auto-étude

Bien que les CNN soient le plus souvent utilisés pour des tâches de vision par ordinateur, ils sont généralement bons pour extraire des motifs de taille fixe. Par exemple, si nous traitons des sons, nous pouvons également vouloir utiliser des CNN pour rechercher des motifs spécifiques dans un signal audio - dans ce cas, les filtres seraient unidimensionnels (et ce CNN serait appelé 1D-CNN). De plus, parfois, un 3D-CNN est utilisé pour extraire des caractéristiques dans un espace multidimensionnel, comme certains événements se produisant dans une vidéo - le CNN peut capturer certains motifs de changement de caractéristiques au fil du temps. Faites quelques recherches et auto-études sur d'autres tâches qui peuvent être réalisées avec des CNN.

## [Devoir](lab/README.md)

Dans ce laboratoire, vous devez classer différentes races de chats et de chiens. Ces images sont plus complexes que le jeu de données MNIST et ont des dimensions plus élevées, et il y a plus de 10 classes.

**Avertissement** :  
Ce document a été traduit à l'aide de services de traduction automatique basés sur l'IA. Bien que nous nous efforçons d'assurer l'exactitude, veuillez noter que les traductions automatisées peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue native doit être considéré comme la source faisant autorité. Pour des informations critiques, une traduction humaine professionnelle est recommandée. Nous ne sommes pas responsables des malentendus ou des interprétations erronées résultant de l'utilisation de cette traduction.