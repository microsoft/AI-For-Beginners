<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "e40b47ac3fd48f71304ede1474e66293",
  "translation_date": "2025-08-24T20:46:15+00:00",
  "source_file": "lessons/5-NLP/14-Embeddings/README.md",
  "language_code": "fr"
}
-->
# Intégrations

## [Quiz avant le cours](https://ff-quizzes.netlify.app/en/ai/quiz/27)

Lors de l'entraînement de classificateurs basés sur BoW ou TF/IDF, nous travaillions avec des vecteurs bag-of-words de haute dimension de longueur `vocab_size`, et nous convertissions explicitement des vecteurs de représentation positionnelle de basse dimension en une représentation sparse one-hot. Cependant, cette représentation one-hot n'est pas efficace en termes de mémoire. De plus, chaque mot est traité indépendamment des autres, c'est-à-dire que les vecteurs encodés en one-hot n'expriment aucune similarité sémantique entre les mots.

L'idée des **intégrations** est de représenter les mots par des vecteurs denses de plus faible dimension, qui reflètent d'une certaine manière le sens sémantique d'un mot. Nous discuterons plus tard de la manière de construire des intégrations de mots significatives, mais pour l'instant, considérons simplement les intégrations comme un moyen de réduire la dimensionnalité d'un vecteur de mots.

Ainsi, la couche d'intégration prendrait un mot en entrée et produirait un vecteur de sortie de taille `embedding_size` spécifiée. En un sens, cela ressemble beaucoup à une couche `Linear`, mais au lieu de prendre un vecteur encodé en one-hot, elle pourra prendre un numéro de mot en entrée, nous permettant d'éviter de créer de grands vecteurs encodés en one-hot.

En utilisant une couche d'intégration comme première couche dans notre réseau de classification, nous pouvons passer d'un modèle bag-of-words à un modèle **embedding bag**, où nous convertissons d'abord chaque mot de notre texte en l'intégration correspondante, puis calculons une fonction d'agrégation sur toutes ces intégrations, comme `sum`, `average` ou `max`.  

![Image montrant un classificateur basé sur des intégrations pour cinq mots d'une séquence.](../../../../../translated_images/embedding-classifier-example.b77f021a7ee67eeec8e68bfe11636c5b97d6eaa067515a129bfb1d0034b1ac5b.fr.png)

> Image de l'auteur

## ✍️ Exercices : Intégrations

Poursuivez votre apprentissage dans les notebooks suivants :
* [Intégrations avec PyTorch](../../../../../lessons/5-NLP/14-Embeddings/EmbeddingsPyTorch.ipynb)
* [Intégrations avec TensorFlow](../../../../../lessons/5-NLP/14-Embeddings/EmbeddingsTF.ipynb)

## Intégrations sémantiques : Word2Vec

Bien que la couche d'intégration apprenne à mapper les mots à une représentation vectorielle, cette représentation n'a pas nécessairement beaucoup de sens sémantique. Il serait intéressant d'apprendre une représentation vectorielle telle que des mots similaires ou des synonymes correspondent à des vecteurs proches les uns des autres en termes de distance vectorielle (par exemple, distance euclidienne).

Pour cela, nous devons pré-entraîner notre modèle d'intégration sur une grande collection de textes d'une manière spécifique. Une méthode pour entraîner des intégrations sémantiques s'appelle [Word2Vec](https://en.wikipedia.org/wiki/Word2vec). Elle repose sur deux principales architectures utilisées pour produire une représentation distribuée des mots :

 - **Continuous bag-of-words** (CBoW) — dans cette architecture, nous entraînons le modèle à prédire un mot à partir du contexte environnant. Étant donné le ngram $(W_{-2},W_{-1},W_0,W_1,W_2)$, l'objectif du modèle est de prédire $W_0$ à partir de $(W_{-2},W_{-1},W_1,W_2)$.
 - **Continuous skip-gram** est l'opposé de CBoW. Le modèle utilise une fenêtre de mots de contexte environnants pour prédire le mot actuel.

CBoW est plus rapide, tandis que skip-gram est plus lent, mais représente mieux les mots peu fréquents.

![Image montrant les algorithmes CBoW et Skip-Gram pour convertir des mots en vecteurs.](../../../../../translated_images/example-algorithms-for-converting-words-to-vectors.fbe9207a726922f6f0f5de66427e8a6eda63809356114e28fb1fa5f4a83ebda7.fr.png)

> Image tirée de [cet article](https://arxiv.org/pdf/1301.3781.pdf)

Les intégrations pré-entraînées Word2Vec (ainsi que d'autres modèles similaires, comme GloVe) peuvent également être utilisées à la place de la couche d'intégration dans les réseaux neuronaux. Cependant, nous devons gérer les vocabulaires, car le vocabulaire utilisé pour pré-entraîner Word2Vec/GloVe est probablement différent du vocabulaire de notre corpus de texte. Consultez les notebooks ci-dessus pour voir comment résoudre ce problème.

## Intégrations contextuelles

Une limitation clé des représentations d'intégrations pré-entraînées traditionnelles comme Word2Vec est le problème de désambiguïsation des sens des mots. Bien que les intégrations pré-entraînées puissent capturer une partie du sens des mots dans leur contexte, chaque sens possible d'un mot est encodé dans la même intégration. Cela peut poser des problèmes dans les modèles en aval, car de nombreux mots, comme le mot "play", ont des significations différentes selon le contexte dans lequel ils sont utilisés.

Par exemple, le mot "play" dans ces deux phrases a des significations très différentes :

- Je suis allé voir une **pièce** au théâtre.
- John veut **jouer** avec ses amis.

Les intégrations pré-entraînées ci-dessus représentent ces deux significations du mot "play" dans la même intégration. Pour surmonter cette limitation, nous devons construire des intégrations basées sur le **modèle de langage**, qui est entraîné sur un large corpus de texte et *sait* comment les mots peuvent être assemblés dans différents contextes. La discussion sur les intégrations contextuelles dépasse le cadre de ce tutoriel, mais nous y reviendrons lorsque nous parlerons des modèles de langage plus tard dans le cours.

## Conclusion

Dans cette leçon, vous avez découvert comment construire et utiliser des couches d'intégration dans TensorFlow et PyTorch pour mieux refléter les significations sémantiques des mots.

## 🚀 Défi

Word2Vec a été utilisé pour des applications intéressantes, notamment la génération de paroles de chansons et de poésie. Consultez [cet article](https://www.politetype.com/blog/word2vec-color-poems) qui explique comment l'auteur a utilisé Word2Vec pour générer de la poésie. Regardez également [cette vidéo de Dan Shiffmann](https://www.youtube.com/watch?v=LSS_bos_TPI&ab_channel=TheCodingTrain) pour découvrir une autre explication de cette technique. Ensuite, essayez d'appliquer ces techniques à votre propre corpus de texte, peut-être issu de Kaggle.

## [Quiz après le cours](https://ff-quizzes.netlify.app/en/ai/quiz/28)

## Révision & Auto-apprentissage

Lisez cet article sur Word2Vec : [Efficient Estimation of Word Representations in Vector Space](https://arxiv.org/pdf/1301.3781.pdf)

## [Devoir : Notebooks](assignment.md)

**Avertissement** :  
Ce document a été traduit à l'aide du service de traduction automatique [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforcions d'assurer l'exactitude, veuillez noter que les traductions automatisées peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue d'origine doit être considéré comme la source faisant autorité. Pour des informations critiques, il est recommandé de recourir à une traduction humaine professionnelle. Nous déclinons toute responsabilité en cas de malentendus ou d'interprétations erronées résultant de l'utilisation de cette traduction.