# Classification des Visages des Animaux de Compagnie

Devoir de laboratoire du [Curriculum AI pour Débutants](https://github.com/microsoft/ai-for-beginners).

## Tâche

Imaginez que vous devez développer une application pour une nursery d'animaux de compagnie afin de cataloguer tous les animaux. L'une des grandes fonctionnalités d'une telle application serait de découvrir automatiquement la race à partir d'une photographie. Cela peut être réalisé avec succès en utilisant des réseaux de neurones.

Vous devez entraîner un réseau de neurones convolutionnel pour classifier différentes races de chats et de chiens en utilisant le jeu de données **Visages d'Animaux de Compagnie**.

## Le Jeu de Données

Nous allons utiliser le jeu de données **Visages d'Animaux de Compagnie**, dérivé du jeu de données [Oxford-IIIT](https://www.robots.ox.ac.uk/~vgg/data/pets/) sur les animaux de compagnie. Il contient 35 races différentes de chiens et de chats.

![Jeu de données avec lequel nous allons travailler](../../../../../../translated_images/data.50b2a9d5484bdbf0f52f5765b381cec9efe2bd296a98f007f90bedb6ac67f2a8.fr.png)

Pour télécharger le jeu de données, utilisez ce extrait de code :

```python
!wget https://mslearntensorflowlp.blob.core.windows.net/data/petfaces.tar.gz
!tar xfz petfaces.tar.gz
!rm petfaces.tar.gz
```

## Début du Notebook

Commencez le laboratoire en ouvrant [PetFaces.ipynb](../../../../../../lessons/4-ComputerVision/07-ConvNets/lab/PetFaces.ipynb)

## À Retenir

Vous avez résolu un problème de classification d'images relativement complexe depuis le début ! Il y avait pas mal de classes, et vous avez tout de même réussi à obtenir une précision raisonnable ! Il est également judicieux de mesurer la précision top-k, car il est facile de confondre certaines classes qui ne sont pas clairement différentes même pour les êtres humains.

**Avertissement** :  
Ce document a été traduit à l'aide de services de traduction automatique basés sur l'IA. Bien que nous nous efforçons d'assurer l'exactitude, veuillez noter que les traductions automatiques peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue native doit être considéré comme la source faisant autorité. Pour des informations critiques, une traduction professionnelle par un humain est recommandée. Nous ne sommes pas responsables des malentendus ou des interprétations erronées résultant de l'utilisation de cette traduction.