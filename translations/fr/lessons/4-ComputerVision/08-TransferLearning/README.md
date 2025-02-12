# Réseaux pré-entraînés et apprentissage par transfert

L'entraînement des CNN peut prendre beaucoup de temps et nécessite une grande quantité de données. Cependant, une grande partie du temps est consacrée à l'apprentissage des meilleurs filtres de bas niveau qu'un réseau peut utiliser pour extraire des motifs à partir d'images. Une question naturelle se pose : peut-on utiliser un réseau de neurones entraîné sur un ensemble de données et l'adapter pour classer différentes images sans avoir besoin d'un processus d'entraînement complet ?

## [Quiz avant le cours](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/108)

Cette approche s'appelle **l'apprentissage par transfert**, car nous transférons une partie des connaissances d'un modèle de réseau de neurones à un autre. Dans l'apprentissage par transfert, nous commençons généralement avec un modèle pré-entraîné, qui a été entraîné sur un grand ensemble de données d'images, comme **ImageNet**. Ces modèles peuvent déjà faire un bon travail d'extraction de différentes caractéristiques à partir d'images génériques, et dans de nombreux cas, construire simplement un classificateur sur les caractéristiques extraites peut donner un bon résultat.

> ✅ L'apprentissage par transfert est un terme que l'on trouve dans d'autres domaines académiques, comme l'éducation. Il fait référence au processus de prise de connaissances d'un domaine et de leur application à un autre.

## Modèles pré-entraînés en tant qu'extracteurs de caractéristiques

Les réseaux de convolution dont nous avons parlé dans la section précédente contenaient un certain nombre de couches, chacune étant censée extraire certaines caractéristiques de l'image, à partir de combinaisons de pixels de bas niveau (comme des lignes horizontales/verticales ou des traits), jusqu'à des combinaisons de caractéristiques de niveau supérieur, correspondant à des choses comme l'œil d'une flamme. Si nous entraînons un CNN sur un ensemble de données suffisamment large d'images génériques et diverses, le réseau devrait apprendre à extraire ces caractéristiques communes.

Keras et PyTorch contiennent des fonctions pour charger facilement les poids de réseaux de neurones pré-entraînés pour certaines architectures courantes, dont la plupart ont été entraînées sur des images ImageNet. Les plus souvent utilisés sont décrits sur la page [Architectures CNN](../07-ConvNets/CNN_Architectures.md) de la leçon précédente. En particulier, vous voudrez peut-être envisager d'utiliser l'un des suivants :

* **VGG-16/VGG-19**, qui sont des modèles relativement simples mais qui offrent une bonne précision. Utiliser VGG comme première tentative est souvent un bon choix pour voir comment fonctionne l'apprentissage par transfert.
* **ResNet** est une famille de modèles proposés par Microsoft Research en 2015. Ils ont plus de couches et nécessitent donc plus de ressources.
* **MobileNet** est une famille de modèles de taille réduite, adaptés aux appareils mobiles. Utilisez-les si vous manquez de ressources et pouvez sacrifier un peu de précision.

Voici des caractéristiques extraites d'une image de chat par le réseau VGG-16 :

![Caractéristiques extraites par VGG-16](../../../../../translated_images/features.6291f9c7ba3a0b951af88fc9864632b9115365410765680680d30c927dd67354.fr.png)

## Ensemble de données Chats vs. Chiens

Dans cet exemple, nous allons utiliser un ensemble de données de [Chats et Chiens](https://www.microsoft.com/download/details.aspx?id=54765&WT.mc_id=academic-77998-cacaste), qui est très proche d'un scénario de classification d'images en conditions réelles.

## ✍️ Exercice : Apprentissage par Transfert

Voyons l'apprentissage par transfert en action dans les notebooks correspondants :

* [Apprentissage par Transfert - PyTorch](../../../../../lessons/4-ComputerVision/08-TransferLearning/TransferLearningPyTorch.ipynb)
* [Apprentissage par Transfert - TensorFlow](../../../../../lessons/4-ComputerVision/08-TransferLearning/TransferLearningTF.ipynb)

## Visualisation du Chat Adversarial

Le réseau de neurones pré-entraîné contient différents motifs dans son *cerveau*, y compris des notions de **chat idéal** (ainsi que de chien idéal, de zèbre idéal, etc.). Il serait intéressant de **visualiser cette image** d'une certaine manière. Cependant, ce n'est pas simple, car les motifs sont répartis sur tous les poids du réseau et sont également organisés dans une structure hiérarchique.

Une approche que nous pouvons adopter est de commencer avec une image aléatoire, puis d'essayer d'utiliser la technique **d'optimisation par descente de gradient** pour ajuster cette image de manière à ce que le réseau commence à penser qu'il s'agit d'un chat.

![Boucle d'Optimisation d'Image](../../../../../translated_images/ideal-cat-loop.999fbb8ff306e044f997032f4eef9152b453e6a990e449bbfb107de2493cc37e.fr.png)

Cependant, si nous faisons cela, nous obtiendrons quelque chose de très similaire à un bruit aléatoire. Cela est dû au fait qu'il *existe de nombreuses façons de faire croire au réseau que l'image d'entrée est un chat*, y compris certaines qui n'ont pas de sens visuellement. Bien que ces images contiennent de nombreux motifs typiques d'un chat, il n'y a rien pour les contraindre à être visuellement distinctives.

Pour améliorer le résultat, nous pouvons ajouter un autre terme dans la fonction de perte, qui est appelé **perte de variation**. C'est une métrique qui montre à quel point les pixels voisins de l'image sont similaires. Minimiser la perte de variation rend l'image plus lisse et élimine le bruit, révélant ainsi des motifs plus visuellement attrayants. Voici un exemple de telles images "idéales", qui sont classées comme chat et comme zèbre avec une forte probabilité :

![Chat Idéal](../../../../../translated_images/ideal-cat.203dd4597643d6b0bd73038b87f9c0464322725e3a06ab145d25d4a861c70592.fr.png) | ![Zèbre Idéal](../../../../../translated_images/ideal-zebra.7f70e8b54ee15a7a314000bb5df38a6cfe086ea04d60df4d3ef313d046b98a2b.fr.png)
-----|-----
 *Chat Idéal* | *Zèbre Idéal*

Une approche similaire peut être utilisée pour effectuer ce que l'on appelle des **attaques adversariales** sur un réseau de neurones. Supposons que nous voulons tromper un réseau de neurones et faire en sorte qu'un chien ressemble à un chat. Si nous prenons une image de chien, qui est reconnue par un réseau comme un chien, nous pouvons ensuite l'ajuster un peu à l'aide de l'optimisation par descente de gradient, jusqu'à ce que le réseau commence à la classifier comme un chat :

![Image d'un Chien](../../../../../translated_images/original-dog.8f68a67d2fe0911f33041c0f7fce8aa4ea919f9d3917ec4b468298522aeb6356.fr.png) | ![Image d'un chien classé comme un chat](../../../../../translated_images/adversarial-dog.d9fc7773b0142b89752539bfbf884118de845b3851c5162146ea0b8809fc820f.fr.png)
-----|-----
*Image originale d'un chien* | *Image d'un chien classé comme un chat*

Consultez le code pour reproduire les résultats ci-dessus dans le notebook suivant :

* [Chat Idéal et Adversarial - TensorFlow](../../../../../lessons/4-ComputerVision/08-TransferLearning/AdversarialCat_TF.ipynb)

## Conclusion

En utilisant l'apprentissage par transfert, vous pouvez rapidement assembler un classificateur pour une tâche de classification d'objets personnalisée et atteindre une haute précision. Vous pouvez constater que les tâches plus complexes que nous résolvons maintenant nécessitent une plus grande puissance de calcul et ne peuvent pas être facilement résolues sur un CPU. Dans l'unité suivante, nous essaierons d'utiliser une implémentation plus légère pour entraîner le même modèle en utilisant moins de ressources de calcul, ce qui se traduira par une précision légèrement inférieure.

## 🚀 Défi

Dans les notebooks accompagnants, il y a des notes en bas sur la façon dont le transfert de connaissances fonctionne mieux avec des données d'entraînement quelque peu similaires (un nouveau type d'animal, peut-être). Faites quelques expériences avec des types d'images complètement nouveaux pour voir à quel point vos modèles de transfert de connaissances fonctionnent bien ou mal.

## [Quiz après le cours](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/208)

## Révision et Auto-étude

Lisez [TrainingTricks.md](TrainingTricks.md) pour approfondir vos connaissances sur d'autres manières d'entraîner vos modèles.

## [Devoir](lab/README.md)

Dans ce laboratoire, nous utiliserons un ensemble de données de [Oxford-IIIT](https://www.robots.ox.ac.uk/~vgg/data/pets/) sur les animaux de compagnie avec 35 races de chats et de chiens, et nous construirons un classificateur d'apprentissage par transfert.

**Avertissement** :  
Ce document a été traduit à l'aide de services de traduction automatique basés sur l'IA. Bien que nous nous efforçons d'assurer l'exactitude, veuillez noter que les traductions automatisées peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue d'origine doit être considéré comme la source faisant autorité. Pour des informations critiques, une traduction humaine professionnelle est recommandée. Nous ne sommes pas responsables des malentendus ou des interprétations erronées résultant de l'utilisation de cette traduction.