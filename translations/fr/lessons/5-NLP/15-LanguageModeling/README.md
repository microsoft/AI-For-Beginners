# Modélisation du Langage

Les embeddings sémantiques, tels que Word2Vec et GloVe, représentent en fait une première étape vers la **modélisation du langage** - créer des modèles qui comprennent (ou représentent) d'une certaine manière la nature du langage.

## [Quiz pré-conférence](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/115)

L'idée principale derrière la modélisation du langage est de les entraîner sur des ensembles de données non étiquetés de manière non supervisée. Cela est important car nous disposons de quantités énormes de texte non étiqueté, tandis que la quantité de texte étiqueté serait toujours limitée par l'effort que nous pouvons consacrer à l'étiquetage. Le plus souvent, nous pouvons construire des modèles de langage capables de **prédire les mots manquants** dans le texte, car il est facile de masquer un mot aléatoire dans le texte et de l'utiliser comme échantillon d'entraînement.

## Entraînement des Embeddings

Dans nos exemples précédents, nous avons utilisé des embeddings sémantiques pré-entraînés, mais il est intéressant de voir comment ces embeddings peuvent être entraînés. Plusieurs idées possibles peuvent être utilisées :

* Modélisation du langage **N-Gram**, lorsque nous prédisons un jeton en regardant N jetons précédents (N-gram)
* **Continuous Bag-of-Words** (CBoW), lorsque nous prédisons le jeton du milieu $W_0$ dans une séquence de jetons $W_{-N}$, ..., $W_N$.
* **Skip-gram**, où nous prédisons un ensemble de jetons voisins {$W_{-N},\dots, W_{-1}, W_1,\dots, W_N$} à partir du jeton du milieu $W_0$.

![image provenant d'un article sur la conversion de mots en vecteurs](../../../../../translated_images/example-algorithms-for-converting-words-to-vectors.fbe9207a726922f6f0f5de66427e8a6eda63809356114e28fb1fa5f4a83ebda7.fr.png)

> Image tirée [de cet article](https://arxiv.org/pdf/1301.3781.pdf)

## ✍️ Notebooks d'Exemple : Entraînement du modèle CBoW

Poursuivez votre apprentissage dans les notebooks suivants :

* [Entraînement de CBoW Word2Vec avec TensorFlow](../../../../../lessons/5-NLP/15-LanguageModeling/CBoW-TF.ipynb)
* [Entraînement de CBoW Word2Vec avec PyTorch](../../../../../lessons/5-NLP/15-LanguageModeling/CBoW-PyTorch.ipynb)

## Conclusion

Dans la leçon précédente, nous avons vu que les embeddings de mots fonctionnent comme par magie ! Maintenant, nous savons que l'entraînement des embeddings de mots n'est pas une tâche très complexe, et nous devrions être en mesure d'entraîner nos propres embeddings de mots pour un texte spécifique à un domaine si nécessaire.

## [Quiz post-conférence](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/215)

## Revue & Auto-apprentissage

* [Tutoriel officiel PyTorch sur la Modélisation du Langage](https://pytorch.org/tutorials/beginner/nlp/word_embeddings_tutorial.html).
* [Tutoriel officiel TensorFlow sur l'entraînement du modèle Word2Vec](https://www.TensorFlow.org/tutorials/text/word2vec).
* L'utilisation du cadre **gensim** pour entraîner les embeddings les plus couramment utilisés en quelques lignes de code est décrite [dans cette documentation](https://pytorch.org/tutorials/beginner/nlp/word_embeddings_tutorial.html).

## 🚀 [Devoir : Entraîner un Modèle Skip-Gram](lab/README.md)

Dans le laboratoire, nous vous mettons au défi de modifier le code de cette leçon pour entraîner un modèle skip-gram au lieu de CBoW. [Lisez les détails](lab/README.md)

**Avertissement** :  
Ce document a été traduit à l'aide de services de traduction automatique basés sur l'IA. Bien que nous visons à garantir l'exactitude, veuillez noter que les traductions automatiques peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue natale doit être considéré comme la source autoritaire. Pour des informations critiques, une traduction professionnelle par un humain est recommandée. Nous ne sommes pas responsables des malentendus ou des interprétations erronées résultant de l'utilisation de cette traduction.