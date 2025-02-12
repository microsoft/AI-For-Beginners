# Algorithmes Génétiques

## [Quiz avant le cours](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/121)

Les **Algorithmes Génétiques** (AG) reposent sur une **approche évolutionnaire** de l'IA, dans laquelle des méthodes de l'évolution d'une population sont utilisées pour obtenir une solution optimale à un problème donné. Ils ont été proposés en 1975 par [John Henry Holland](https://wikipedia.org/wiki/John_Henry_Holland).

Les Algorithmes Génétiques sont basés sur les idées suivantes :

* Les solutions valides au problème peuvent être représentées sous forme de **gènes**
* **Le croisement** nous permet de combiner deux solutions pour obtenir une nouvelle solution valide
* **La sélection** est utilisée pour choisir des solutions plus optimales en utilisant une **fonction d'évaluation**
* **Les mutations** sont introduites pour déstabiliser l'optimisation et nous sortir du minimum local

Si vous souhaitez implémenter un Algorithme Génétique, vous avez besoin de ce qui suit :

 * Trouver une méthode de codage de nos solutions de problème en utilisant des **gènes** g∈Γ
 * Sur l'ensemble de gènes Γ, nous devons définir une **fonction d'évaluation** fit: Γ→**R**. Des valeurs de fonction plus petites correspondent à de meilleures solutions.
 * Définir un mécanisme de **croisement** pour combiner deux gènes afin d'obtenir une nouvelle solution valide crossover: Γ<sup>2</sub>→Γ.
 * Définir un mécanisme de **mutation** mutate: Γ→Γ.

Dans de nombreux cas, le croisement et la mutation sont des algorithmes assez simples pour manipuler les gènes sous forme de séquences numériques ou de vecteurs de bits.

L'implémentation spécifique d'un algorithme génétique peut varier d'un cas à l'autre, mais la structure générale est la suivante :

1. Sélectionner une population initiale G⊂Γ
2. Sélectionner aléatoirement l'une des opérations qui sera effectuée à cette étape : croisement ou mutation
3. **Croisement** :
  * Sélectionner aléatoirement deux gènes g<sub>1</sub>, g<sub>2</sub> ∈ G
  * Calculer le croisement g=crossover(g<sub>1</sub>,g<sub>2</sub>)
  * Si fit(g)<fit(g<sub>1</sub>) ou fit(g)<fit(g<sub>2</sub>) - remplacer le gène correspondant dans la population par g.
4. **Mutation** - sélectionner un gène aléatoire g∈G et le remplacer par mutate(g)
5. Répéter à partir de l'étape 2, jusqu'à ce que nous obtenions une valeur suffisamment petite de fit, ou jusqu'à ce que la limite du nombre d'étapes soit atteinte.

## Tâches Typiques

Les tâches généralement résolues par les Algorithmes Génétiques incluent :

1. Optimisation de l'emploi du temps
1. Emballage optimal
1. Découpe optimale
1. Accélération de la recherche exhaustive

## ✍️ Exercices : Algorithmes Génétiques

Poursuivez votre apprentissage dans les cahiers suivants :

Allez à [ce cahier](../../../../../lessons/6-Other/21-GeneticAlgorithms/Genetic.ipynb) pour voir deux exemples d'utilisation des Algorithmes Génétiques :

1. Division équitable du trésor
1. Problème des 8 Reines

## Conclusion

Les Algorithmes Génétiques sont utilisés pour résoudre de nombreux problèmes, y compris des problèmes de logistique et de recherche. Le domaine s'inspire de recherches qui ont fusionné des sujets en psychologie et en informatique.

## 🚀 Défi

"Les algorithmes génétiques sont simples à mettre en œuvre, mais leur comportement est difficile à comprendre." [source](https://wikipedia.org/wiki/Genetic_algorithm) Faites des recherches pour trouver une implémentation d'un algorithme génétique, comme la résolution d'un puzzle Sudoku, et expliquez comment cela fonctionne sous forme de croquis ou de diagramme de flux.

## [Quiz après le cours](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/221)

## Révision & Auto-apprentissage

Regardez [cette vidéo géniale](https://www.youtube.com/watch?v=qv6UVOQ0F44) qui parle de la façon dont un ordinateur peut apprendre à jouer à Super Mario en utilisant des réseaux neuronaux entraînés par des algorithmes génétiques. Nous en apprendrons davantage sur l'apprentissage des ordinateurs à jouer à des jeux comme celui-ci [dans la section suivante](../22-DeepRL/README.md).

## [Devoir : Équation Diophantienne](../../../../../lessons/6-Other/21-GeneticAlgorithms/Diophantine.ipynb)

Votre objectif est de résoudre ce qu'on appelle une **équation diophantienne** - une équation avec des racines entières. Par exemple, considérons l'équation a+2b+3c+4d=30. Vous devez trouver les racines entières qui satisfont cette équation.

*Cet devoir est inspiré par [ce post](https://habr.com/post/128704/).*

Indices :

1. Vous pouvez considérer que les racines se situent dans l'intervalle [0;30]
1. Comme gène, envisagez d'utiliser la liste des valeurs des racines

Utilisez [Diophantine.ipynb](../../../../../lessons/6-Other/21-GeneticAlgorithms/Diophantine.ipynb) comme point de départ.

**Avertissement** :  
Ce document a été traduit à l'aide de services de traduction automatique basés sur l'IA. Bien que nous nous efforçons d'assurer l'exactitude, veuillez noter que les traductions automatiques peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue native doit être considéré comme la source autorisée. Pour des informations critiques, une traduction humaine professionnelle est recommandée. Nous ne sommes pas responsables des malentendus ou des interprétations erronées résultant de l'utilisation de cette traduction.