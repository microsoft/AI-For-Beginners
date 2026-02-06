# Segmentation du Corps Humain

Devoir de laboratoire tiré du [Curriculum AI pour Débutants](https://github.com/microsoft/ai-for-beginners).

## Tâche

Dans la production vidéo, par exemple lors des bulletins météo, il est souvent nécessaire de découper l'image d'une personne filmée par une caméra et de la placer sur une autre séquence. Cela se fait généralement à l'aide de techniques de **chroma key**, où une personne est filmée devant un fond de couleur uniforme, qui est ensuite supprimé. Dans ce laboratoire, nous allons entraîner un modèle de réseau neuronal pour découper la silhouette humaine.

## Le Jeu de Données

Nous utiliserons le [jeu de données Segmentation Full Body MADS](https://www.kaggle.com/datasets/tapakah68/segmentation-full-body-mads-dataset) disponible sur Kaggle. Téléchargez le jeu de données manuellement depuis Kaggle.

## Notebook de Départ

Commencez le laboratoire en ouvrant [BodySegmentation.ipynb](../../../../../../lessons/4-ComputerVision/12-Segmentation/lab/BodySegmentation.ipynb)

## Points à Retenir

La segmentation du corps n'est qu'une des nombreuses tâches courantes que l'on peut réaliser avec des images de personnes. Parmi les autres tâches importantes, on trouve la **détection de squelette** et la **détection de pose**. Consultez la bibliothèque [OpenPose](https://github.com/CMU-Perceptual-Computing-Lab/openpose) pour voir comment ces tâches peuvent être mises en œuvre.

**Avertissement** :  
Ce document a été traduit à l'aide du service de traduction automatique [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforcions d'assurer l'exactitude, veuillez noter que les traductions automatisées peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue d'origine doit être considéré comme la source faisant autorité. Pour des informations critiques, il est recommandé de recourir à une traduction humaine professionnelle. Nous déclinons toute responsabilité en cas de malentendus ou d'interprétations erronées résultant de l'utilisation de cette traduction.