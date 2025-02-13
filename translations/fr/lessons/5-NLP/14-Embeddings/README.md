# Intégrations

## [Quiz avant le cours](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/114)

Lors de l'entraînement de classificateurs basés sur BoW ou TF/IDF, nous avons travaillé avec des vecteurs de sac de mots de haute dimension de longueur `vocab_size`, et nous convertissions explicitement des vecteurs de représentation positionnelle de faible dimension en une représentation one-hot éparse. Cependant, cette représentation one-hot n'est pas efficace en termes de mémoire. De plus, chaque mot est traité indépendamment des autres, c'est-à-dire que les vecteurs encodés en one-hot n'expriment aucune similarité sémantique entre les mots.

L'idée de **l'intégration** est de représenter les mots par des vecteurs denses de dimension inférieure, qui reflètent d'une certaine manière le sens sémantique d'un mot. Nous discuterons plus tard de la façon de construire des intégrations de mots significatives, mais pour l'instant, considérons simplement les intégrations comme un moyen de réduire la dimensionnalité d'un vecteur de mots.

Ainsi, la couche d'intégration prendrait un mot comme entrée et produirait un vecteur de sortie de dimension spécifiée `embedding_size`. En un sens, c'est très similaire à une couche `Linear`, mais au lieu de prendre un vecteur encodé en one-hot, elle pourra prendre un numéro de mot comme entrée, ce qui nous permet d'éviter de créer de grands vecteurs encodés en one-hot.

En utilisant une couche d'intégration comme première couche dans notre réseau de classificateurs, nous pouvons passer d'un modèle de sac de mots à un modèle de **sac d'intégrations**, où nous convertissons d'abord chaque mot de notre texte en l'intégration correspondante, puis nous calculons une fonction agrégée sur toutes ces intégrations, telle que `sum`, `average` ou `max`.  

![Image montrant un classificateur d'intégration pour cinq mots en séquence.](../../../../../translated_images/embedding-classifier-example.b77f021a7ee67eeec8e68bfe11636c5b97d6eaa067515a129bfb1d0034b1ac5b.fr.png)

> Image par l'auteur

## ✍️ Exercices : Intégrations

Continuez votre apprentissage dans les cahiers suivants :
* [Intégrations avec PyTorch](../../../../../lessons/5-NLP/14-Embeddings/EmbeddingsPyTorch.ipynb)
* [Intégrations TensorFlow](../../../../../lessons/5-NLP/14-Embeddings/EmbeddingsTF.ipynb)

## Intégrations sémantiques : Word2Vec

Bien que la couche d'intégration ait appris à mapper les mots à une représentation vectorielle, cette représentation n'avait pas nécessairement beaucoup de signification sémantique. Il serait souhaitable d'apprendre une représentation vectorielle telle que des mots similaires ou des synonymes correspondent à des vecteurs qui sont proches les uns des autres en termes de distance vectorielle (par exemple, distance euclidienne).

Pour ce faire, nous devons pré-entraîner notre modèle d'intégration sur une grande collection de textes d'une manière spécifique. Une façon d'entraîner des intégrations sémantiques est appelée [Word2Vec](https://en.wikipedia.org/wiki/Word2vec). Elle est basée sur deux architectures principales utilisées pour produire une représentation distribuée des mots :

 - **Sac de mots continu** (CBoW) — dans cette architecture, nous entraînons le modèle à prédire un mot à partir du contexte environnant. Étant donné le ngram $(W_{-2},W_{-1},W_0,W_1,W_2)$, l'objectif du modèle est de prédire $W_0$ à partir de $(W_{-2},W_{-1},W_1,W_2)$.
 - **Skip-gram continu** est l'opposé de CBoW. Le modèle utilise une fenêtre de mots contextuels environnants pour prédire le mot actuel.

CBoW est plus rapide, tandis que skip-gram est plus lent, mais il fait un meilleur travail de représentation des mots peu fréquents.

![Image montrant à la fois les algorithmes CBoW et Skip-Gram pour convertir des mots en vecteurs.](../../../../../translated_images/example-algorithms-for-converting-words-to-vectors.fbe9207a726922f6f0f5de66427e8a6eda63809356114e28fb1fa5f4a83ebda7.fr.png)

> Image tirée [de cet article](https://arxiv.org/pdf/1301.3781.pdf)

Les intégrations pré-entraînées Word2Vec (ainsi que d'autres modèles similaires, comme GloVe) peuvent également être utilisées à la place de la couche d'intégration dans les réseaux de neurones. Cependant, nous devons traiter les vocabulaires, car le vocabulaire utilisé pour pré-entraîner Word2Vec/GloVe est susceptible de différer du vocabulaire de notre corpus de texte. Consultez les cahiers ci-dessus pour voir comment ce problème peut être résolu.

## Intégrations contextuelles

Une limitation clé des représentations d'intégration pré-entraînées traditionnelles telles que Word2Vec est le problème de la désambiguïsation du sens des mots. Bien que les intégrations pré-entraînées puissent capturer une partie du sens des mots dans un contexte, chaque signification possible d'un mot est encodée dans la même intégration. Cela peut poser des problèmes dans les modèles en aval, car de nombreux mots, comme le mot 'play', ont des significations différentes selon le contexte dans lequel ils sont utilisés.

Par exemple, le mot 'play' dans ces deux phrases différentes a des significations assez différentes :

- Je suis allé à une **pièce** au théâtre.
- John veut **jouer** avec ses amis.

Les intégrations pré-entraînées ci-dessus représentent ces deux significations du mot 'play' dans la même intégration. Pour surmonter cette limitation, nous devons construire des intégrations basées sur le **modèle linguistique**, qui est entraîné sur un grand corpus de texte et *sait* comment les mots peuvent être assemblés dans différents contextes. La discussion sur les intégrations contextuelles est hors de portée de ce tutoriel, mais nous y reviendrons lorsque nous parlerons des modèles linguistiques plus tard dans le cours.

## Conclusion

Dans cette leçon, vous avez découvert comment construire et utiliser des couches d'intégration dans TensorFlow et Pytorch pour mieux refléter les significations sémantiques des mots.

## 🚀 Défi

Word2Vec a été utilisé pour des applications intéressantes, y compris la génération de paroles de chansons et de poésie. Jetez un œil à [cet article](https://www.politetype.com/blog/word2vec-color-poems) qui explique comment l'auteur a utilisé Word2Vec pour générer de la poésie. Regardez également [cette vidéo de Dan Shiffmann](https://www.youtube.com/watch?v=LSS_bos_TPI&ab_channel=TheCodingTrain) pour découvrir une autre explication de cette technique. Ensuite, essayez d'appliquer ces techniques à votre propre corpus de texte, peut-être provenant de Kaggle.

## [Quiz après le cours](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/214)

## Revue & Auto-apprentissage

Lisez cet article sur Word2Vec : [Estimation efficace des représentations de mots dans l'espace vectoriel](https://arxiv.org/pdf/1301.3781.pdf)

## [Devoir : Cahiers](assignment.md)

**Avertissement** :  
Ce document a été traduit à l'aide de services de traduction automatique basés sur l'IA. Bien que nous nous efforçons d'assurer l'exactitude, veuillez noter que les traductions automatiques peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue native doit être considéré comme la source autorisée. Pour des informations critiques, une traduction humaine professionnelle est recommandée. Nous ne sommes pas responsables des malentendus ou des interprétations erronées résultant de l'utilisation de cette traduction.