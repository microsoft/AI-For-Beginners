# Classification des animaux de compagnie d'Oxford en utilisant l'apprentissage par transfert

Devoir du [Curriculum AI pour Débutants](https://github.com/microsoft/ai-for-beginners).

## Tâche

Imaginez que vous devez développer une application pour une crèche pour animaux afin de cataloguer tous les animaux de compagnie. L'une des grandes fonctionnalités d'une telle application serait de découvrir automatiquement la race à partir d'une photographie. Dans ce devoir, nous utiliserons l'apprentissage par transfert pour classifier des images réelles d'animaux de compagnie à partir du jeu de données [Oxford-IIIT](https://www.robots.ox.ac.uk/~vgg/data/pets/).

## Le Jeu de Données

Nous utiliserons le jeu de données original [Oxford-IIIT](https://www.robots.ox.ac.uk/~vgg/data/pets/), qui contient 35 races différentes de chiens et de chats.

Pour télécharger le jeu de données, utilisez ce fragment de code :

```python
!wget https://www.robots.ox.ac.uk/~vgg/data/pets/data/images.tar.gz
!tar xfz images.tar.gz
!rm images.tar.gz
```

## Démarrage du Notebook

Commencez le laboratoire en ouvrant [OxfordPets.ipynb](../../../../../../lessons/4-ComputerVision/08-TransferLearning/lab/OxfordPets.ipynb)

## Conclusion

L'apprentissage par transfert et les réseaux pré-entraînés nous permettent de résoudre des problèmes de classification d'images du monde réel relativement facilement. Cependant, les réseaux pré-entraînés fonctionnent bien sur des images de type similaire, et si nous commençons à classifier des images très différentes (par exemple, des images médicales), nous risquons d'obtenir des résultats beaucoup moins bons.

**Avertissement** :  
Ce document a été traduit à l'aide de services de traduction automatique basés sur l'IA. Bien que nous nous efforçons d'assurer l'exactitude, veuillez noter que les traductions automatisées peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue native doit être considéré comme la source autorisée. Pour des informations critiques, une traduction professionnelle par un humain est recommandée. Nous ne sommes pas responsables des malentendus ou des erreurs d'interprétation résultant de l'utilisation de cette traduction.