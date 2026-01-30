# Classification multi-classes avec Perceptron

Travail pratique tiré du [Curriculum AI pour les débutants](https://github.com/microsoft/ai-for-beginners).

## Tâche

En utilisant le code que nous avons développé dans cette leçon pour la classification binaire des chiffres manuscrits MNIST, créez un classificateur multi-classes capable de reconnaître n'importe quel chiffre. Calculez la précision de la classification sur les ensembles de données d'entraînement et de test, et affichez la matrice de confusion.

## Conseils

1. Pour chaque chiffre, créez un ensemble de données pour un classificateur binaire de "ce chiffre contre tous les autres".
1. Entraînez 10 perceptrons différents pour la classification binaire (un pour chaque chiffre).
1. Définissez une fonction qui classera un chiffre donné en entrée.

> **Conseil** : Si nous combinons les poids des 10 perceptrons dans une seule matrice, nous devrions être capables d'appliquer les 10 perceptrons aux chiffres en entrée par une seule multiplication matricielle. Le chiffre le plus probable peut ensuite être trouvé simplement en appliquant l'opération `argmax` sur la sortie.

## Notebook de départ

Commencez le travail pratique en ouvrant [PerceptronMultiClass.ipynb](PerceptronMultiClass.ipynb)

---

**Avertissement** :  
Ce document a été traduit à l'aide du service de traduction automatique [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforcions d'assurer l'exactitude, veuillez noter que les traductions automatisées peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue d'origine doit être considéré comme la source faisant autorité. Pour des informations critiques, il est recommandé de recourir à une traduction humaine professionnelle. Nous déclinons toute responsabilité en cas de malentendus ou d'interprétations erronées résultant de l'utilisation de cette traduction.