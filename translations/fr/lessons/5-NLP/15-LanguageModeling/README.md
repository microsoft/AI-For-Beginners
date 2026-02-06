# Modélisation du langage

Les embeddings sémantiques, tels que Word2Vec et GloVe, constituent en réalité une première étape vers la **modélisation du langage** - créer des modèles qui *comprennent* (ou *représentent*) d'une certaine manière la nature du langage.

## [Quiz avant le cours](https://ff-quizzes.netlify.app/en/ai/quiz/29)

L'idée principale derrière la modélisation du langage est de les entraîner sur des ensembles de données non étiquetées de manière non supervisée. Cela est important car nous disposons de grandes quantités de texte non étiqueté, tandis que la quantité de texte étiqueté sera toujours limitée par l'effort nécessaire pour l'étiquetage. Le plus souvent, nous pouvons construire des modèles de langage capables de **prédire les mots manquants** dans un texte, car il est facile de masquer un mot aléatoire dans un texte et de l'utiliser comme exemple d'entraînement.

## Entraînement des embeddings

Dans nos exemples précédents, nous avons utilisé des embeddings sémantiques pré-entraînés, mais il est intéressant de voir comment ces embeddings peuvent être entraînés. Plusieurs idées peuvent être utilisées :

* **Modélisation de langage N-Gram**, où l'on prédit un token en se basant sur les N tokens précédents (N-gram).
* **Continuous Bag-of-Words** (CBoW), où l'on prédit le token central $W_0$ dans une séquence de tokens $W_{-N}$, ..., $W_N$.
* **Skip-gram**, où l'on prédit un ensemble de tokens voisins {$W_{-N},\dots, W_{-1}, W_1,\dots, W_N$} à partir du token central $W_0$.

![image tirée d'un article sur la conversion des mots en vecteurs](../../../../../translated_images/fr/example-algorithms-for-converting-words-to-vectors.fbe9207a726922f6.webp)

> Image tirée de [cet article](https://arxiv.org/pdf/1301.3781.pdf)

## ✍️ Notebooks d'exemple : Entraînement du modèle CBoW

Poursuivez votre apprentissage avec les notebooks suivants :

* [Entraînement de CBoW Word2Vec avec TensorFlow](CBoW-TF.ipynb)
* [Entraînement de CBoW Word2Vec avec PyTorch](CBoW-PyTorch.ipynb)

## Conclusion

Dans la leçon précédente, nous avons vu que les embeddings de mots fonctionnent comme par magie ! Nous savons maintenant que l'entraînement des embeddings de mots n'est pas une tâche très complexe, et nous devrions être capables d'entraîner nos propres embeddings pour des textes spécifiques à un domaine si nécessaire.

## [Quiz après le cours](https://ff-quizzes.netlify.app/en/ai/quiz/30)

## Révision & Auto-apprentissage

* [Tutoriel officiel PyTorch sur la modélisation du langage](https://pytorch.org/tutorials/beginner/nlp/word_embeddings_tutorial.html).
* [Tutoriel officiel TensorFlow sur l'entraînement du modèle Word2Vec](https://www.TensorFlow.org/tutorials/text/word2vec).
* Utiliser le framework **gensim** pour entraîner les embeddings les plus couramment utilisés en quelques lignes de code est décrit [dans cette documentation](https://pytorch.org/tutorials/beginner/nlp/word_embeddings_tutorial.html).

## 🚀 [Exercice : Entraîner un modèle Skip-Gram](lab/README.md)

Dans le laboratoire, nous vous mettons au défi de modifier le code de cette leçon pour entraîner un modèle Skip-Gram à la place de CBoW. [Lisez les détails](lab/README.md)

---

