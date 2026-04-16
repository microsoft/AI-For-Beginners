# Classification des animaux d'Oxford à l'aide de l'apprentissage par transfert

Devoir pratique tiré du [programme AI for Beginners](https://github.com/microsoft/ai-for-beginners).

## Tâche

Imaginez que vous devez développer une application pour une garderie pour animaux afin de cataloguer tous les animaux. L'une des fonctionnalités intéressantes d'une telle application serait de reconnaître automatiquement la race à partir d'une photographie. Dans cet exercice, nous utiliserons l'apprentissage par transfert pour classifier des images réelles d'animaux issues du jeu de données [Oxford-IIIT](https://www.robots.ox.ac.uk/~vgg/data/pets/).

## Le jeu de données

Nous utiliserons le jeu de données original [Oxford-IIIT](https://www.robots.ox.ac.uk/~vgg/data/pets/), qui contient 35 races différentes de chiens et de chats.

Pour télécharger le jeu de données, utilisez cet extrait de code :

```python
!wget https://www.robots.ox.ac.uk/~vgg/data/pets/data/images.tar.gz
!tar xfz images.tar.gz
!rm images.tar.gz
```

## Démarrage du notebook

Commencez le devoir en ouvrant [OxfordPets.ipynb](../../../../../../lessons/4-ComputerVision/08-TransferLearning/lab/OxfordPets.ipynb)

## Points à retenir

L'apprentissage par transfert et les réseaux pré-entraînés nous permettent de résoudre relativement facilement des problèmes de classification d'images du monde réel. Cependant, les réseaux pré-entraînés fonctionnent bien sur des images de type similaire, et si nous commençons à classifier des images très différentes (par exemple, des images médicales), nous risquons d'obtenir des résultats bien moins satisfaisants.

**Avertissement** :  
Ce document a été traduit à l'aide du service de traduction automatique [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforcions d'assurer l'exactitude, veuillez noter que les traductions automatisées peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue d'origine doit être considéré comme la source faisant autorité. Pour des informations critiques, il est recommandé de recourir à une traduction humaine professionnelle. Nous déclinons toute responsabilité en cas de malentendus ou d'interprétations erronées résultant de l'utilisation de cette traduction.