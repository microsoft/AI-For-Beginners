<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f3d2cee9cb3c52160419e560c57a690e",
  "translation_date": "2025-08-24T20:52:03+00:00",
  "source_file": "lessons/4-ComputerVision/07-ConvNets/lab/README.md",
  "language_code": "fr"
}
-->
# Classification des visages d'animaux de compagnie

Devoir de laboratoire tiré du [programme AI for Beginners](https://github.com/microsoft/ai-for-beginners).

## Tâche

Imaginez que vous devez développer une application pour une garderie pour animaux afin de cataloguer tous les animaux. L'une des fonctionnalités intéressantes d'une telle application serait de reconnaître automatiquement la race à partir d'une photographie. Cela peut être réalisé avec succès en utilisant des réseaux neuronaux.

Vous devez entraîner un réseau neuronal convolutif pour classer différentes races de chats et de chiens en utilisant le dataset **Pet Faces**.

## Le Dataset

Nous utiliserons le dataset **Pet Faces**, dérivé du dataset [Oxford-IIIT](https://www.robots.ox.ac.uk/~vgg/data/pets/) pour animaux. Il contient 35 races différentes de chiens et de chats.

![Dataset que nous allons utiliser](../../../../../../translated_images/data.50b2a9d5484bdbf0f52f5765b381cec9efe2bd296a98f007f90bedb6ac67f2a8.fr.png)

Pour télécharger le dataset, utilisez cet extrait de code :

```python
!wget https://mslearntensorflowlp.blob.core.windows.net/data/petfaces.tar.gz
!tar xfz petfaces.tar.gz
!rm petfaces.tar.gz
```

## Démarrage du Notebook

Commencez le laboratoire en ouvrant [PetFaces.ipynb](../../../../../../lessons/4-ComputerVision/07-ConvNets/lab/PetFaces.ipynb)

## Résultat

Vous avez résolu un problème relativement complexe de classification d'images à partir de zéro ! Il y avait un grand nombre de classes, et vous avez tout de même réussi à obtenir une précision raisonnable ! Il est également pertinent de mesurer la précision top-k, car il est facile de confondre certaines classes qui ne sont pas clairement distinctes, même pour des êtres humains.

**Avertissement** :  
Ce document a été traduit à l'aide du service de traduction automatique [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforcions d'assurer l'exactitude, veuillez noter que les traductions automatisées peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue d'origine doit être considéré comme la source faisant autorité. Pour des informations critiques, il est recommandé de recourir à une traduction humaine professionnelle. Nous déclinons toute responsabilité en cas de malentendus ou d'interprétations erronées résultant de l'utilisation de cette traduction.