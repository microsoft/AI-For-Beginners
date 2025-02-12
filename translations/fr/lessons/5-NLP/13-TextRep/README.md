# Représentation du Texte en Tenseurs

## [Quiz pré-cours](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/113)

## Classification de Texte

Tout au long de la première partie de cette section, nous allons nous concentrer sur la tâche de **classification de texte**. Nous utiliserons le jeu de données [AG News](https://www.kaggle.com/amananandrai/ag-news-classification-dataset), qui contient des articles de presse comme les suivants :

* Catégorie : Sci/Tech
* Titre : Une entreprise du Kentucky remporte une subvention pour étudier les peptides (AP)
* Corps : AP - Une entreprise fondée par un chercheur en chimie à l'Université de Louisville a remporté une subvention pour développer...

Notre objectif sera de classer l'article d'actualité dans l'une des catégories en fonction du texte.

## Représentation du texte

Si nous voulons résoudre des tâches de traitement du langage naturel (NLP) avec des réseaux neuronaux, nous avons besoin d'un moyen de représenter le texte sous forme de tenseurs. Les ordinateurs représentent déjà les caractères textuels sous forme de nombres qui se mappent à des polices sur votre écran en utilisant des encodages tels que ASCII ou UTF-8.

<img alt="Image montrant un diagramme mappant un caractère à une représentation ASCII et binaire" src="images/ascii-character-map.png" width="50%"/>

> [Source de l'image](https://www.seobility.net/en/wiki/ASCII)

En tant qu'êtres humains, nous comprenons ce que chaque lettre **représente**, et comment tous les caractères se combinent pour former les mots d'une phrase. Cependant, les ordinateurs, à eux seuls, n'ont pas une telle compréhension, et le réseau neuronal doit apprendre la signification pendant l'entraînement.

Par conséquent, nous pouvons utiliser différentes approches pour représenter le texte :

* **Représentation au niveau des caractères**, lorsque nous représentons le texte en traitant chaque caractère comme un nombre. Étant donné que nous avons *C* caractères différents dans notre corpus de texte, le mot *Hello* serait représenté par un tenseur 5x*C*. Chaque lettre correspondrait à une colonne de tenseur en encodage one-hot.
* **Représentation au niveau des mots**, dans laquelle nous créons un **vocabulaire** de tous les mots de notre texte, puis représentons les mots en utilisant l'encodage one-hot. Cette approche est quelque peu meilleure, car chaque lettre prise isolément n'a pas beaucoup de sens, et donc en utilisant des concepts sémantiques de niveau supérieur - les mots - nous simplifions la tâche pour le réseau neuronal. Cependant, étant donné la taille importante du dictionnaire, nous devons gérer des tenseurs creux de haute dimension.

Quelle que soit la représentation, nous devons d'abord convertir le texte en une séquence de **tokens**, chaque token étant soit un caractère, un mot, ou parfois même une partie d'un mot. Ensuite, nous convertissons le token en un nombre, généralement en utilisant un **vocabulaire**, et ce nombre peut être alimenté dans un réseau neuronal en utilisant l'encodage one-hot.

## N-Grams

Dans le langage naturel, le sens précis des mots ne peut être déterminé que dans un contexte. Par exemple, les significations de *réseau neuronal* et *réseau de pêche* sont complètement différentes. L'une des façons de prendre cela en compte est de construire notre modèle sur des paires de mots, en considérant les paires de mots comme des tokens de vocabulaire séparés. De cette manière, la phrase *J'aime aller pêcher* sera représentée par la séquence de tokens suivante : *J'aime*, *aime aller*, *aller pêcher*. Le problème avec cette approche est que la taille du dictionnaire augmente considérablement, et des combinaisons comme *aller pêcher* et *aller faire du shopping* sont présentées par des tokens différents, qui ne partagent aucune similarité sémantique malgré le même verbe.

Dans certains cas, nous pouvons envisager d'utiliser des tri-grammes -- combinaisons de trois mots -- également. Ainsi, l'approche est souvent appelée **n-grams**. De plus, il est logique d'utiliser des n-grams avec une représentation au niveau des caractères, auquel cas les n-grams correspondront à différents syllabes.

## Sac de Mots et TF/IDF

Lors de la résolution de tâches telles que la classification de texte, nous devons être en mesure de représenter le texte par un vecteur de taille fixe, que nous utiliserons comme entrée pour le classificateur dense final. L'une des façons les plus simples de le faire est de combiner toutes les représentations de mots individuelles, par exemple en les additionnant. Si nous ajoutons les encodages one-hot de chaque mot, nous finirons par un vecteur de fréquences, montrant combien de fois chaque mot apparaît dans le texte. Cette représentation du texte est appelée **sac de mots** (BoW).

<img src="images/bow.png" width="90%"/>

> Image par l'auteur

Un BoW représente essentiellement quels mots apparaissent dans le texte et en quelles quantités, ce qui peut effectivement être une bonne indication de ce dont parle le texte. Par exemple, un article de presse sur la politique contiendra probablement des mots tels que *président* et *pays*, tandis qu'une publication scientifique aurait des termes comme *collisionneur*, *découvert*, etc. Ainsi, les fréquences des mots peuvent dans de nombreux cas être un bon indicateur du contenu du texte.

Le problème avec le BoW est que certains mots communs, tels que *et*, *est*, etc. apparaissent dans la plupart des textes, et ils ont les fréquences les plus élevées, masquant les mots qui sont vraiment importants. Nous pouvons réduire l'importance de ces mots en tenant compte de la fréquence à laquelle les mots apparaissent dans l'ensemble de la collection de documents. C'est l'idée principale derrière l'approche TF/IDF, qui est abordée plus en détail dans les notebooks joints à cette leçon.

Cependant, aucune de ces approches ne peut pleinement prendre en compte la **sémantique** du texte. Nous avons besoin de modèles de réseaux neuronaux plus puissants pour cela, que nous discuterons plus tard dans cette section.

## ✍️ Exercices : Représentation du Texte

Poursuivez votre apprentissage dans les notebooks suivants :

* [Représentation du Texte avec PyTorch](../../../../../lessons/5-NLP/13-TextRep/TextRepresentationPyTorch.ipynb)
* [Représentation du Texte avec TensorFlow](../../../../../lessons/5-NLP/13-TextRep/TextRepresentationTF.ipynb)

## Conclusion

Jusqu'à présent, nous avons étudié des techniques qui peuvent ajouter un poids de fréquence à différents mots. Cependant, elles ne peuvent pas représenter le sens ou l'ordre. Comme l'a dit le célèbre linguiste J. R. Firth en 1935, "Le sens complet d'un mot est toujours contextuel, et aucune étude du sens en dehors du contexte ne peut être prise au sérieux." Nous apprendrons plus tard dans le cours comment capturer les informations contextuelles à partir du texte en utilisant la modélisation du langage.

## 🚀 Défi

Essayez d'autres exercices en utilisant le sac de mots et différents modèles de données. Vous pourriez être inspiré par cette [compétition sur Kaggle](https://www.kaggle.com/competitions/word2vec-nlp-tutorial/overview/part-1-for-beginners-bag-of-words)

## [Quiz post-cours](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/213)

## Revue & Auto-apprentissage

Pratiquez vos compétences avec les embeddings de texte et les techniques de sac de mots sur [Microsoft Learn](https://docs.microsoft.com/learn/modules/intro-natural-language-processing-pytorch/?WT.mc_id=academic-77998-cacaste)

## [Devoir : Notebooks](assignment.md)

**Avertissement** :  
Ce document a été traduit à l'aide de services de traduction automatique basés sur l'IA. Bien que nous visons à garantir l'exactitude, veuillez noter que les traductions automatiques peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue native doit être considéré comme la source autoritaire. Pour des informations critiques, une traduction humaine professionnelle est recommandée. Nous ne sommes pas responsables des malentendus ou des interprétations erronées résultant de l'utilisation de cette traduction.