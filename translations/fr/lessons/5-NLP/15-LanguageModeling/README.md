<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "31b46ba1f3aa78578134d4829f88be53",
  "translation_date": "2025-08-24T20:47:39+00:00",
  "source_file": "lessons/5-NLP/15-LanguageModeling/README.md",
  "language_code": "fr"
}
-->
# Modélisation du langage

Les embeddings sémantiques, tels que Word2Vec et GloVe, sont en réalité une première étape vers la **modélisation du langage** - créer des modèles qui *comprennent* (ou *représentent*) d'une certaine manière la nature du langage.

## [Quiz avant le cours](https://ff-quizzes.netlify.app/en/ai/quiz/29)

L'idée principale derrière la modélisation du langage est de les entraîner sur des ensembles de données non étiquetés de manière non supervisée. Cela est important car nous disposons de grandes quantités de texte non étiqueté, tandis que la quantité de texte étiqueté sera toujours limitée par l'effort nécessaire pour l'étiquetage. Le plus souvent, nous pouvons construire des modèles de langage capables de **prédire les mots manquants** dans le texte, car il est facile de masquer un mot aléatoire dans le texte et de l'utiliser comme échantillon d'entraînement.

## Entraînement des embeddings

Dans nos exemples précédents, nous avons utilisé des embeddings sémantiques pré-entraînés, mais il est intéressant de voir comment ces embeddings peuvent être entraînés. Plusieurs idées peuvent être utilisées :

* **Modélisation de langage N-Gram**, où l'on prédit un token en se basant sur les N tokens précédents (N-gram).
* **Continuous Bag-of-Words** (CBoW), où l'on prédit le token central $W_0$ dans une séquence de tokens $W_{-N}$, ..., $W_N$.
* **Skip-gram**, où l'on prédit un ensemble de tokens voisins {$W_{-N},\dots, W_{-1}, W_1,\dots, W_N$} à partir du token central $W_0$.

![image tirée d'un article sur la conversion des mots en vecteurs](../../../../../translated_images/example-algorithms-for-converting-words-to-vectors.fbe9207a726922f6f0f5de66427e8a6eda63809356114e28fb1fa5f4a83ebda7.fr.png)

> Image tirée de [cet article](https://arxiv.org/pdf/1301.3781.pdf)

## ✍️ Notebooks d'exemple : Entraînement du modèle CBoW

Poursuivez votre apprentissage avec les notebooks suivants :

* [Entraînement de CBoW Word2Vec avec TensorFlow](../../../../../lessons/5-NLP/15-LanguageModeling/CBoW-TF.ipynb)
* [Entraînement de CBoW Word2Vec avec PyTorch](../../../../../lessons/5-NLP/15-LanguageModeling/CBoW-PyTorch.ipynb)

## Conclusion

Dans la leçon précédente, nous avons vu que les embeddings de mots fonctionnent comme par magie ! Nous savons maintenant que l'entraînement des embeddings de mots n'est pas une tâche très complexe, et nous devrions être capables d'entraîner nos propres embeddings de mots pour du texte spécifique à un domaine si nécessaire.

## [Quiz après le cours](https://ff-quizzes.netlify.app/en/ai/quiz/30)

## Révision et auto-apprentissage

* [Tutoriel officiel PyTorch sur la modélisation du langage](https://pytorch.org/tutorials/beginner/nlp/word_embeddings_tutorial.html).
* [Tutoriel officiel TensorFlow sur l'entraînement du modèle Word2Vec](https://www.TensorFlow.org/tutorials/text/word2vec).
* L'utilisation du framework **gensim** pour entraîner les embeddings les plus couramment utilisés en quelques lignes de code est décrite [dans cette documentation](https://pytorch.org/tutorials/beginner/nlp/word_embeddings_tutorial.html).

## 🚀 [Exercice : Entraîner un modèle Skip-Gram](lab/README.md)

Dans le laboratoire, nous vous mettons au défi de modifier le code de cette leçon pour entraîner un modèle Skip-Gram au lieu de CBoW. [Lisez les détails](lab/README.md).

**Avertissement** :  
Ce document a été traduit à l'aide du service de traduction automatique [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforcions d'assurer l'exactitude, veuillez noter que les traductions automatisées peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue d'origine doit être considéré comme la source faisant autorité. Pour des informations critiques, il est recommandé de recourir à une traduction humaine professionnelle. Nous déclinons toute responsabilité en cas de malentendus ou d'interprétations erronées résultant de l'utilisation de cette traduction.