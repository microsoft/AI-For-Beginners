# Algorithmes Génétiques

## [Quiz avant le cours](https://ff-quizzes.netlify.app/en/ai/quiz/41)

Les **Algorithmes Génétiques** (AG) reposent sur une **approche évolutionnaire** de l'IA, dans laquelle les méthodes d'évolution d'une population sont utilisées pour obtenir une solution optimale à un problème donné. Ils ont été proposés en 1975 par [John Henry Holland](https://wikipedia.org/wiki/John_Henry_Holland).

Les Algorithmes Génétiques sont basés sur les idées suivantes :

* Les solutions valides au problème peuvent être représentées sous forme de **gènes**
* Le **croisement** permet de combiner deux solutions pour obtenir une nouvelle solution valide
* La **sélection** est utilisée pour choisir les solutions les plus optimales à l'aide d'une **fonction d'évaluation**
* Des **mutations** sont introduites pour déstabiliser l'optimisation et sortir d'un minimum local

Pour implémenter un Algorithme Génétique, vous avez besoin de :

 * Trouver une méthode pour coder les solutions de votre problème en utilisant des **gènes** g&in;&Gamma;
 * Sur l'ensemble des gènes &Gamma;, définir une **fonction d'évaluation** fit: &Gamma;&rightarrow;**R**. Les valeurs plus petites de la fonction correspondent à de meilleures solutions.
 * Définir un mécanisme de **croisement** pour combiner deux gènes et obtenir une nouvelle solution valide crossover: &Gamma;<sup>2</sub>&rightarrow;&Gamma;.
 * Définir un mécanisme de **mutation** mutate: &Gamma;&rightarrow;&Gamma;.

Dans de nombreux cas, les mécanismes de croisement et de mutation sont des algorithmes assez simples pour manipuler les gènes sous forme de séquences numériques ou de vecteurs binaires.

La mise en œuvre spécifique d'un algorithme génétique peut varier selon les cas, mais la structure générale est la suivante :

1. Sélectionner une population initiale G&subset;&Gamma;
2. Sélectionner aléatoirement une des opérations à effectuer à cette étape : croisement ou mutation
3. **Croisement** :
  * Sélectionner aléatoirement deux gènes g<sub>1</sub>, g<sub>2</sub> &in; G
  * Calculer le croisement g=crossover(g<sub>1</sub>,g<sub>2</sub>)
  * Si fit(g)<fit(g<sub>1</sub>) ou fit(g)<fit(g<sub>2</sub>) - remplacer le gène correspondant dans la population par g.
4. **Mutation** - sélectionner un gène aléatoire g&in;G et le remplacer par mutate(g)
5. Répéter à partir de l'étape 2, jusqu'à obtenir une valeur suffisamment petite de fit, ou jusqu'à atteindre la limite du nombre d'étapes.

## Tâches typiques

Les tâches généralement résolues par les Algorithmes Génétiques incluent :

1. Optimisation des plannings
1. Emballage optimal
1. Découpe optimale
1. Accélération de la recherche exhaustive

## ✍️ Exercices : Algorithmes Génétiques

Poursuivez votre apprentissage dans les notebooks suivants :

Rendez-vous sur [ce notebook](Genetic.ipynb) pour voir deux exemples d'utilisation des Algorithmes Génétiques :

1. Partage équitable d'un trésor
1. Problème des 8 reines

## Conclusion

Les Algorithmes Génétiques sont utilisés pour résoudre de nombreux problèmes, notamment en logistique et en recherche. Ce domaine s'inspire de recherches qui ont fusionné des sujets en Psychologie et en Informatique.

## 🚀 Défi

"Les algorithmes génétiques sont simples à implémenter, mais leur comportement est difficile à comprendre." [source](https://wikipedia.org/wiki/Genetic_algorithm) Faites des recherches pour trouver une implémentation d'un algorithme génétique, comme pour résoudre un puzzle Sudoku, et expliquez son fonctionnement sous forme de croquis ou de diagramme de flux.

## [Quiz après le cours](https://ff-quizzes.netlify.app/en/ai/quiz/42)

## Révision & Auto-apprentissage

Regardez [cette excellente vidéo](https://www.youtube.com/watch?v=qv6UVOQ0F44) qui explique comment un ordinateur peut apprendre à jouer à Super Mario en utilisant des réseaux neuronaux entraînés par des algorithmes génétiques. Nous en apprendrons davantage sur l'apprentissage des jeux par ordinateur [dans la section suivante](../22-DeepRL/README.md).

## [Devoir : Équation Diophantienne](Diophantine.ipynb)

Votre objectif est de résoudre une **équation diophantienne** - une équation avec des racines entières. Par exemple, considérez l'équation a+2b+3c+4d=30. Vous devez trouver les racines entières qui satisfont cette équation.

*Cet exercice est inspiré de [cet article](https://habr.com/post/128704/).*

Conseils :

1. Vous pouvez considérer les racines dans l'intervalle [0;30]
1. Comme gène, envisagez d'utiliser la liste des valeurs des racines

Utilisez [Diophantine.ipynb](Diophantine.ipynb) comme point de départ.

---

