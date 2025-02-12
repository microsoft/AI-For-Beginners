# Segmentation du Corps Humain

Devoir de [AI for Beginners Curriculum](https://github.com/microsoft/ai-for-beginners).

## Tâche

Dans la production vidéo, par exemple dans les prévisions météorologiques, nous avons souvent besoin de découper une image humaine prise par la caméra et de la placer sur un autre plan. Cela se fait généralement à l'aide de techniques de **chroma key**, lorsque l'humain est filmé devant un fond de couleur uniforme, qui est ensuite retiré. Dans ce laboratoire, nous allons entraîner un modèle de réseau de neurones pour découper la silhouette humaine.

## Le Jeu de Données

Nous utiliserons le [Segmentation Full Body MADS Dataset](https://www.kaggle.com/datasets/tapakah68/segmentation-full-body-mads-dataset) de Kaggle. Téléchargez le jeu de données manuellement depuis Kaggle.

## Lancement du Notebook

Commencez le laboratoire en ouvrant [BodySegmentation.ipynb](../../../../../../lessons/4-ComputerVision/12-Segmentation/lab/BodySegmentation.ipynb)

## À Retenir

La segmentation du corps est l'une des tâches courantes que nous pouvons réaliser avec des images de personnes. D'autres tâches importantes incluent la **détection de squelette** et la **détection de pose**. Consultez la bibliothèque [OpenPose](https://github.com/CMU-Perceptual-Computing-Lab/openpose) pour voir comment ces tâches peuvent être mises en œuvre.

**Avertissement** :  
Ce document a été traduit à l'aide de services de traduction automatique basés sur l'IA. Bien que nous nous efforçons d'assurer l'exactitude, veuillez noter que les traductions automatiques peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue native doit être considéré comme la source autoritaire. Pour des informations critiques, une traduction humaine professionnelle est recommandée. Nous ne sommes pas responsables des malentendus ou des interprétations erronées résultant de l'utilisation de cette traduction.