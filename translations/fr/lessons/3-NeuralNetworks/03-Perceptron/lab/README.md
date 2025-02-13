# Classification Multi-Classe avec Perceptron

Devoir du [Curriculum AI pour Débutants](https://github.com/microsoft/ai-for-beginners).

## Tâche

En utilisant le code que nous avons développé dans cette leçon pour la classification binaire des chiffres manuscrits MNIST, créez un classificateur multi-classe capable de reconnaître n'importe quel chiffre. Calculez la précision de classification sur les ensembles de données d'entraînement et de test, et imprimez la matrice de confusion.

## Indices

1. Pour chaque chiffre, créez un ensemble de données pour le classificateur binaire "ce chiffre contre tous les autres chiffres"
1. Entraînez 10 perceptrons différents pour la classification binaire (un pour chaque chiffre)
1. Définissez une fonction qui classera un chiffre d'entrée

> **Indice** : Si nous combinons les poids des 10 perceptrons en une seule matrice, nous devrions être capables d'appliquer les 10 perceptrons aux chiffres d'entrée par une multiplication de matrices. Le chiffre le plus probable peut ensuite être trouvé simplement en appliquant l'opération `argmax` sur la sortie.

## Notebook de Début

Commencez le laboratoire en ouvrant [PerceptronMultiClass.ipynb](../../../../../../lessons/3-NeuralNetworks/03-Perceptron/lab/PerceptronMultiClass.ipynb)

**Avertissement** :  
Ce document a été traduit à l'aide de services de traduction automatique basés sur l'IA. Bien que nous nous efforçons d'assurer l'exactitude, veuillez noter que les traductions automatiques peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue native doit être considéré comme la source autorisée. Pour des informations critiques, une traduction humaine professionnelle est recommandée. Nous ne sommes pas responsables des malentendus ou des interprétations erronées résultant de l'utilisation de cette traduction.