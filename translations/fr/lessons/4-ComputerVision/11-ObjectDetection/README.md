<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "d85c8b08f6d1b48fd7f35b99f93c1138",
  "translation_date": "2025-08-24T20:50:42+00:00",
  "source_file": "lessons/4-ComputerVision/11-ObjectDetection/README.md",
  "language_code": "fr"
}
-->
# Détection d'Objets

Les modèles de classification d'images que nous avons étudiés jusqu'à présent prenaient une image et produisaient un résultat catégoriel, comme la classe 'nombre' dans un problème MNIST. Cependant, dans de nombreux cas, nous ne voulons pas seulement savoir qu'une image représente des objets - nous voulons également pouvoir déterminer leur emplacement précis. C'est précisément l'objectif de la **détection d'objets**.

## [Quiz avant le cours](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/111)

![Détection d'Objets](../../../../../translated_images/Screen_Shot_2016-11-17_at_11.14.54_AM.b4bb3769353287be1b905373ed9c858102c054b16e4595c76ec3f7bba0feb549.fr.png)

> Image tirée du [site web YOLO v2](https://pjreddie.com/darknet/yolov2/)

## Une Approche Naïve pour la Détection d'Objets

Supposons que nous voulions trouver un chat sur une image. Une approche très naïve pour la détection d'objets serait la suivante :

1. Diviser l'image en un certain nombre de tuiles.
2. Appliquer une classification d'images sur chaque tuile.
3. Les tuiles qui produisent une activation suffisamment élevée peuvent être considérées comme contenant l'objet en question.

![Détection Naïve](../../../../../translated_images/naive-detection.e7f1ba220ccd08c68a2ea8e06a7ed75c3fcc738c2372f9e00b7f4299a8659c01.fr.png)

> *Image tirée du [cahier d'exercices](../../../../../lessons/4-ComputerVision/11-ObjectDetection/ObjectDetection-TF.ipynb)*

Cependant, cette approche est loin d'être idéale, car elle ne permet à l'algorithme de localiser la boîte englobante de l'objet que de manière très imprécise. Pour une localisation plus précise, nous devons utiliser une forme de **régression** pour prédire les coordonnées des boîtes englobantes - et pour cela, nous avons besoin de jeux de données spécifiques.

## Régression pour la Détection d'Objets

[Cet article de blog](https://towardsdatascience.com/object-detection-with-neural-networks-a4e2c46b4491) offre une excellente introduction à la détection de formes.

## Jeux de Données pour la Détection d'Objets

Vous pourriez rencontrer les jeux de données suivants pour cette tâche :

* [PASCAL VOC](http://host.robots.ox.ac.uk/pascal/VOC/) - 20 classes
* [COCO](http://cocodataset.org/#home) - Common Objects in Context. 80 classes, boîtes englobantes et masques de segmentation

![COCO](../../../../../translated_images/coco-examples.71bc60380fa6cceb7caad48bd09e35b6028caabd363aa04fee89c414e0870e86.fr.jpg)

## Métriques pour la Détection d'Objets

### Intersection sur Union

Alors que pour la classification d'images, il est facile de mesurer les performances de l'algorithme, pour la détection d'objets, nous devons mesurer à la fois la justesse de la classe et la précision de la localisation de la boîte englobante déduite. Pour cette dernière, nous utilisons ce que l'on appelle l'**Intersection sur Union** (IoU), qui mesure à quel point deux boîtes (ou deux zones arbitraires) se chevauchent.

![IoU](../../../../../translated_images/iou_equation.9a4751d40fff4e119ecd0a7bcca4e71ab1dc83e0d4f2a0d66ff0859736f593cf.fr.png)

> *Figure 2 tirée de [cet excellent article de blog sur l'IoU](https://pyimagesearch.com/2016/11/07/intersection-over-union-iou-for-object-detection/)*

L'idée est simple : nous divisons la zone d'intersection entre deux figures par la zone de leur union. Pour deux zones identiques, l'IoU serait de 1, tandis que pour des zones complètement disjointes, il sera de 0. Sinon, il variera entre 0 et 1. Nous considérons généralement uniquement les boîtes englobantes pour lesquelles l'IoU dépasse une certaine valeur.

### Précision Moyenne

Supposons que nous voulions mesurer à quel point une classe d'objets donnée $C$ est bien reconnue. Pour cela, nous utilisons la métrique de **Précision Moyenne**, qui est calculée comme suit :

1. Considérer la courbe Précision-Rappel qui montre la précision en fonction d'une valeur seuil de détection (de 0 à 1).
2. En fonction du seuil, nous détecterons plus ou moins d'objets dans l'image, avec des valeurs différentes de précision et de rappel.
3. La courbe ressemblera à ceci :

<img src="https://github.com/shwars/NeuroWorkshop/raw/master/images/ObjDetectionPrecisionRecall.png"/>

> *Image tirée de [NeuroWorkshop](http://github.com/shwars/NeuroWorkshop)*

La Précision Moyenne pour une classe donnée $C$ est l'aire sous cette courbe. Plus précisément, l'axe du Rappel est généralement divisé en 10 parties, et la Précision est moyennée sur tous ces points :

$$
AP = {1\over11}\sum_{i=0}^{10}\mbox{Precision}(\mbox{Recall}={i\over10})
$$

### AP et IoU

Nous ne considérerons que les détections pour lesquelles l'IoU dépasse une certaine valeur. Par exemple, dans le jeu de données PASCAL VOC, on suppose généralement que $\mbox{IoU Threshold} = 0.5$, tandis que dans COCO, l'AP est mesuré pour différentes valeurs de $\mbox{IoU Threshold}$.

<img src="https://github.com/shwars/NeuroWorkshop/raw/master/images/ObjDetectionPrecisionRecallIoU.png"/>

> *Image tirée de [NeuroWorkshop](http://github.com/shwars/NeuroWorkshop)*

### Précision Moyenne Pondérée - mAP

La principale métrique pour la Détection d'Objets est appelée **Précision Moyenne Pondérée**, ou **mAP**. Il s'agit de la valeur de la Précision Moyenne, moyennée sur toutes les classes d'objets, et parfois aussi sur $\mbox{IoU Threshold}$. Le processus de calcul de la **mAP** est décrit en détail
[dans cet article de blog](https://medium.com/@timothycarlen/understanding-the-map-evaluation-metric-for-object-detection-a07fe6962cf3)), ainsi que [ici avec des exemples de code](https://gist.github.com/tarlen5/008809c3decf19313de216b9208f3734).

## Différentes Approches pour la Détection d'Objets

Il existe deux grandes catégories d'algorithmes de détection d'objets :

* **Réseaux de Propositions de Régions** (R-CNN, Fast R-CNN, Faster R-CNN). L'idée principale est de générer des **Régions d'Intérêt** (ROI) et d'exécuter un CNN sur celles-ci, en recherchant une activation maximale. Cela ressemble un peu à l'approche naïve, à la différence que les ROI sont générées de manière plus intelligente. L'un des principaux inconvénients de ces méthodes est qu'elles sont lentes, car nous avons besoin de nombreux passages du classificateur CNN sur l'image.
* Méthodes **en un seul passage** (YOLO, SSD, RetinaNet). Dans ces architectures, nous concevons le réseau pour prédire à la fois les classes et les ROI en un seul passage.

### R-CNN : CNN Basé sur les Régions

[R-CNN](http://islab.ulsan.ac.kr/files/announcement/513/rcnn_pami.pdf) utilise [Selective Search](http://www.huppelen.nl/publications/selectiveSearchDraft.pdf) pour générer une structure hiérarchique de régions ROI, qui sont ensuite passées à travers des extracteurs de caractéristiques CNN et des classificateurs SVM pour déterminer la classe de l'objet, et une régression linéaire pour déterminer les coordonnées de la *boîte englobante*. [Article Officiel](https://arxiv.org/pdf/1506.01497v1.pdf)

![RCNN](../../../../../translated_images/rcnn1.cae407020dfb1d1fb572656e44f75cd6c512cc220591c116c506652c10e47f26.fr.png)

> *Image tirée de van de Sande et al. ICCV’11*

![RCNN-1](../../../../../translated_images/rcnn2.2d9530bb83516484ec65b250c22dbf37d3d23244f32864ebcb91d98fe7c3112c.fr.png)

> *Images tirées de [cet article de blog](https://towardsdatascience.com/r-cnn-fast-r-cnn-faster-r-cnn-yolo-object-detection-algorithms-36d53571365e)*

### F-RCNN - Fast R-CNN

Cette approche est similaire à R-CNN, mais les régions sont définies après que les couches de convolution ont été appliquées.

![FRCNN](../../../../../translated_images/f-rcnn.3cda6d9bb41888754037d2d9763e2298a96de5d9bc2a21db3147357aa5da9b1a.fr.png)

> Image tirée de [l'Article Officiel](https://www.cv-foundation.org/openaccess/content_iccv_2015/papers/Girshick_Fast_R-CNN_ICCV_2015_paper.pdf), [arXiv](https://arxiv.org/pdf/1504.08083.pdf), 2015

### Faster R-CNN

L'idée principale de cette approche est d'utiliser un réseau neuronal pour prédire les ROI - le *Réseau de Propositions de Régions*. [Article](https://arxiv.org/pdf/1506.01497.pdf), 2016

![FasterRCNN](../../../../../translated_images/faster-rcnn.8d46c099b87ef30ab2ea26dbc4bdd85b974a57ba8eb526f65dc4cd0a4711de30.fr.png)

> Image tirée de [l'article officiel](https://arxiv.org/pdf/1506.01497.pdf)

### R-FCN : Réseau Complètement Convolutif Basé sur les Régions

Cet algorithme est encore plus rapide que Faster R-CNN. L'idée principale est la suivante :

1. Nous extrayons des caractéristiques à l'aide de ResNet-101.
2. Les caractéristiques sont traitées par une **Carte de Scores Sensibles à la Position**. Chaque objet parmi les $C$ classes est divisé en $k\times k$ régions, et nous entraînons le réseau à prédire des parties d'objets.
3. Pour chaque partie des $k\times k$ régions, tous les réseaux votent pour les classes d'objets, et la classe d'objet avec le maximum de votes est sélectionnée.

![r-fcn image](../../../../../translated_images/r-fcn.13eb88158b99a3da50fa2787a6be5cb310d47f0e9655cc93a1090dc7aab338d1.fr.png)

> Image tirée de [l'article officiel](https://arxiv.org/abs/1605.06409)

### YOLO - You Only Look Once

YOLO est un algorithme en temps réel en un seul passage. L'idée principale est la suivante :

 * L'image est divisée en $S\times S$ régions.
 * Pour chaque région, le **CNN** prédit $n$ objets possibles, les coordonnées des *boîtes englobantes* et la *confiance* = *probabilité* * IoU.

 ![YOLO](../../../../../translated_images/yolo.a2648ec82ee8bb4ea27537677adb482fd4b733ca1705c561b6a24a85102dced5.fr.png)

> Image tirée de [l'article officiel](https://arxiv.org/abs/1506.02640)

### Autres Algorithmes

* RetinaNet : [article officiel](https://arxiv.org/abs/1708.02002)
   - [Implémentation PyTorch dans Torchvision](https://pytorch.org/vision/stable/_modules/torchvision/models/detection/retinanet.html)
   - [Implémentation Keras](https://github.com/fizyr/keras-retinanet)
   - [Détection d'Objets avec RetinaNet](https://keras.io/examples/vision/retinanet/) dans les exemples Keras
* SSD (Single Shot Detector) : [article officiel](https://arxiv.org/abs/1512.02325)

## ✍️ Exercices : Détection d'Objets

Poursuivez votre apprentissage dans le cahier suivant :

[ObjectDetection.ipynb](../../../../../lessons/4-ComputerVision/11-ObjectDetection/ObjectDetection.ipynb)

## Conclusion

Dans cette leçon, vous avez exploré un aperçu des différentes façons dont la détection d'objets peut être réalisée !

## 🚀 Défi

Lisez ces articles et cahiers sur YOLO et essayez-les par vous-même :

* [Bon article de blog](https://www.analyticsvidhya.com/blog/2018/12/practical-guide-object-detection-yolo-framewor-python/) décrivant YOLO
 * [Site officiel](https://pjreddie.com/darknet/yolo/)
 * YOLO : [Implémentation Keras](https://github.com/experiencor/keras-yolo2), [cahier étape par étape](https://github.com/experiencor/basic-yolo-keras/blob/master/Yolo%20Step-by-Step.ipynb)
 * YOLO v2 : [Implémentation Keras](https://github.com/experiencor/keras-yolo2), [cahier étape par étape](https://github.com/experiencor/keras-yolo2/blob/master/Yolo%20Step-by-Step.ipynb)

## [Quiz après le cours](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/211)

## Révision & Étude Personnelle

* [Détection d'Objets](https://tjmachinelearning.com/lectures/1718/obj/) par Nikhil Sardana
* [Une bonne comparaison des algorithmes de détection d'objets](https://lilianweng.github.io/lil-log/2018/12/27/object-detection-part-4.html)
* [Revue des Algorithmes de Deep Learning pour la Détection d'Objets](https://medium.com/comet-app/review-of-deep-learning-algorithms-for-object-detection-c1f3d437b852)
* [Introduction Étape par Étape aux Algorithmes de Détection d'Objets de Base](https://www.analyticsvidhya.com/blog/2018/10/a-step-by-step-introduction-to-the-basic-object-detection-algorithms-part-1/)
* [Implémentation de Faster R-CNN en Python pour la Détection d'Objets](https://www.analyticsvidhya.com/blog/2018/11/implementation-faster-r-cnn-python-object-detection/)

## [Devoir : Détection d'Objets](lab/README.md)

**Avertissement** :  
Ce document a été traduit à l'aide du service de traduction automatique [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforcions d'assurer l'exactitude, veuillez noter que les traductions automatisées peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue d'origine doit être considéré comme la source faisant autorité. Pour des informations critiques, il est recommandé de recourir à une traduction humaine professionnelle. Nous déclinons toute responsabilité en cas de malentendus ou d'interprétations erronées résultant de l'utilisation de cette traduction.