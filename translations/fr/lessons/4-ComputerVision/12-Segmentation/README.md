# Segmentation

Nous avons précédemment appris sur la détection d'objets, qui nous permet de localiser des objets dans l'image en prédisant leurs *boîtes englobantes*. Cependant, pour certaines tâches, nous avons besoin non seulement de boîtes englobantes, mais aussi d'une localisation d'objet plus précise. Cette tâche est appelée **segmentation**.

## [Quiz pré-cours](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/112)

La segmentation peut être considérée comme une **classification de pixels**, où pour **chaque** pixel de l'image, nous devons prédire sa classe (*l'arrière-plan* étant l'une des classes). Il existe deux principaux algorithmes de segmentation :

* **Segmentation sémantique** indique uniquement la classe du pixel, sans faire de distinction entre différents objets de la même classe.
* **Segmentation d'instance** divise les classes en différentes instances.

Pour la segmentation d'instance, ces moutons sont des objets différents, mais pour la segmentation sémantique, tous les moutons sont représentés par une seule classe.

<img src="images/instance_vs_semantic.jpeg" width="50%">

> Image tirée de [cet article de blog](https://nirmalamurali.medium.com/image-classification-vs-semantic-segmentation-vs-instance-segmentation-625c33a08d50)

Il existe différentes architectures neuronales pour la segmentation, mais elles ont toutes la même structure. D'une certaine manière, c'est similaire à l'autoencodeur dont vous avez appris précédemment, mais au lieu de déconstruire l'image originale, notre objectif est de déconstruire un **masque**. Ainsi, un réseau de segmentation se compose des parties suivantes :

* **Encodeur** extrait des caractéristiques de l'image d'entrée
* **Décodeur** transforme ces caractéristiques en **image de masque**, avec la même taille et le même nombre de canaux correspondant au nombre de classes.

<img src="images/segm.png" width="80%">

> Image tirée de [cette publication](https://arxiv.org/pdf/2001.05566.pdf)

Nous devons particulièrement mentionner la fonction de perte utilisée pour la segmentation. Lors de l'utilisation d'autoencodeurs classiques, nous devons mesurer la similarité entre deux images, et nous pouvons utiliser l'erreur quadratique moyenne (MSE) pour cela. En segmentation, chaque pixel dans l'image de masque cible représente le numéro de classe (encodé en one-hot le long de la troisième dimension), donc nous devons utiliser des fonctions de perte spécifiques à la classification - la perte d'entropie croisée, moyennée sur tous les pixels. Si le masque est binaire - **la perte d'entropie croisée binaire** (BCE) est utilisée.

> ✅ L'encodage one-hot est une manière d'encoder une étiquette de classe en un vecteur de longueur égale au nombre de classes. Consultez [cet article](https://datagy.io/sklearn-one-hot-encode/) sur cette technique.

## Segmentation pour l'imagerie médicale

Dans cette leçon, nous allons voir la segmentation en action en entraînant le réseau à reconnaître les nævi humains (également connus sous le nom de grains de beauté) sur des images médicales. Nous utiliserons la <a href="https://www.fc.up.pt/addi/ph2%20database.html">base de données PH<sup>2</sup></a> d'images de dermoscopie comme source d'images. Ce jeu de données contient 200 images de trois classes : nævus typique, nævus atypique et mélanome. Toutes les images contiennent également un **masque** correspondant qui délimite le nævus.

> ✅ Cette technique est particulièrement adaptée à ce type d'imagerie médicale, mais quelles autres applications dans le monde réel pourriez-vous envisager ?

<img alt="navi" src="images/navi.png"/>

> Image provenant de la base de données PH<sup>2</sup>

Nous allons entraîner un modèle pour segmenter n'importe quel nævus de son arrière-plan.

## ✍️ Exercices : Segmentation Sémantique

Ouvrez les notebooks ci-dessous pour en savoir plus sur les différentes architectures de segmentation sémantique, vous entraîner à travailler avec elles et les voir en action.

* [Segmentation Sémantique Pytorch](../../../../../lessons/4-ComputerVision/12-Segmentation/SemanticSegmentationPytorch.ipynb)
* [Segmentation Sémantique TensorFlow](../../../../../lessons/4-ComputerVision/12-Segmentation/SemanticSegmentationTF.ipynb)

## [Quiz post-cours](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/212)

## Conclusion

La segmentation est une technique très puissante pour la classification d'images, allant au-delà des boîtes englobantes pour une classification au niveau des pixels. C'est une technique utilisée dans l'imagerie médicale, entre autres applications.

## 🚀 Défi

La segmentation corporelle n'est qu'une des tâches courantes que nous pouvons réaliser avec des images de personnes. D'autres tâches importantes incluent la **détection de squelette** et la **détection de pose**. Essayez la bibliothèque [OpenPose](https://github.com/CMU-Perceptual-Computing-Lab/openpose) pour voir comment la détection de pose peut être utilisée.

## Revue & Auto-apprentissage

Cet [article de wikipedia](https://wikipedia.org/wiki/Image_segmentation) offre un bon aperçu des diverses applications de cette technique. Apprenez-en davantage par vous-même sur les sous-domaines de la segmentation d'instance et de la segmentation panoptique dans ce domaine d'étude.

## [Devoir](lab/README.md)

Dans ce laboratoire, essayez la **segmentation du corps humain** en utilisant le [Segmentation Full Body MADS Dataset](https://www.kaggle.com/datasets/tapakah68/segmentation-full-body-mads-dataset) de Kaggle.

**Avertissement** :  
Ce document a été traduit à l'aide de services de traduction automatique basés sur l'IA. Bien que nous nous efforçons d'assurer l'exactitude, veuillez noter que les traductions automatisées peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue native doit être considéré comme la source autoritaire. Pour des informations critiques, une traduction humaine professionnelle est recommandée. Nous ne sommes pas responsables des malentendus ou des interprétations erronées résultant de l'utilisation de cette traduction.