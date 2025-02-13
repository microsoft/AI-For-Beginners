# Réseaux de Neurones Récurrents

## [Quiz pré-cours](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/116)

Dans les sections précédentes, nous avons utilisé des représentations sémantiques riches du texte et un simple classificateur linéaire au-dessus des embeddings. Ce que fait cette architecture, c'est capturer le sens agrégé des mots dans une phrase, mais elle ne prend pas en compte l'**ordre** des mots, car l'opération d'agrégation sur les embeddings a supprimé cette information du texte original. Étant donné que ces modèles ne peuvent pas modéliser l'ordre des mots, ils ne peuvent pas résoudre des tâches plus complexes ou ambiguës telles que la génération de texte ou la réponse à des questions.

Pour capturer le sens d'une séquence de texte, nous devons utiliser une autre architecture de réseau de neurones, appelée **réseau de neurones récurrents**, ou RNN. Dans un RNN, nous faisons passer notre phrase à travers le réseau un symbole à la fois, et le réseau produit un **état**, que nous renvoyons ensuite au réseau avec le symbole suivant.

![RNN](../../../../../translated_images/rnn.27f5c29c53d727b546ad3961637a267f0fe9ec5ab01f2a26a853c92fcefbb574.fr.png)

> Image par l'auteur

Étant donné la séquence d'entrée de tokens X<sub>0</sub>,...,X<sub>n</sub>, le RNN crée une séquence de blocs de réseaux de neurones et entraîne cette séquence de bout en bout en utilisant la rétropropagation. Chaque bloc de réseau prend une paire (X<sub>i</sub>,S<sub>i</sub>) comme entrée et produit S<sub>i+1</sub> en résultat. L'état final S<sub>n</sub> ou (sortie Y<sub>n</sub>) passe dans un classificateur linéaire pour produire le résultat. Tous les blocs de réseau partagent les mêmes poids et sont entraînés de bout en bout en utilisant un passage de rétropropagation.

Puisque les vecteurs d'état S<sub>0</sub>,...,S<sub>n</sub> sont passés à travers le réseau, il est capable d'apprendre les dépendances séquentielles entre les mots. Par exemple, lorsque le mot *not* apparaît quelque part dans la séquence, il peut apprendre à nier certains éléments au sein du vecteur d'état, ce qui entraîne une négation.

> ✅ Étant donné que les poids de tous les blocs RNN sur l'image ci-dessus sont partagés, la même image peut être représentée comme un seul bloc (à droite) avec une boucle de rétroaction récurrente, qui renvoie l'état de sortie du réseau à l'entrée.

## Anatomie d'une cellule RNN

Voyons comment une cellule RNN simple est organisée. Elle accepte l'état précédent S<sub>i-1</sub> et le symbole actuel X<sub>i</sub> comme entrées, et doit produire l'état de sortie S<sub>i</sub> (et, parfois, nous sommes également intéressés par une autre sortie Y<sub>i</sub>, comme dans le cas des réseaux génératifs).

Une cellule RNN simple possède deux matrices de poids à l'intérieur : l'une transforme un symbole d'entrée (appelons-la W), et l'autre transforme un état d'entrée (H). Dans ce cas, la sortie du réseau est calculée comme σ(W×X<sub>i</sub>+H×S<sub>i-1</sub>+b), où σ est la fonction d'activation et b est un biais supplémentaire.

<img alt="Anatomie de la cellule RNN" src="images/rnn-anatomy.png" width="50%"/>

> Image par l'auteur

Dans de nombreux cas, les tokens d'entrée sont passés par la couche d'embedding avant d'entrer dans le RNN pour réduire la dimensionnalité. Dans ce cas, si la dimension des vecteurs d'entrée est *emb_size*, et que le vecteur d'état est *hid_size* - la taille de W est *emb_size*×*hid_size*, et la taille de H est *hid_size*×*hid_size*.

## Mémoire à Long Terme et à Court Terme (LSTM)

Un des principaux problèmes des RNN classiques est le problème des **gradients qui disparaissent**. Étant donné que les RNN sont entraînés de bout en bout en un seul passage de rétropropagation, il a des difficultés à propager l'erreur vers les premières couches du réseau, et donc le réseau ne peut pas apprendre les relations entre des tokens éloignés. Une des façons d'éviter ce problème est d'introduire une **gestion explicite de l'état** en utilisant ce que l'on appelle des **portes**. Il existe deux architectures bien connues de ce type : **Long Short Term Memory** (LSTM) et **Gated Relay Unit** (GRU).

![Image montrant un exemple de cellule mémoire à long terme](../../../../../lessons/5-NLP/16-RNN/images/long-short-term-memory-cell.svg)

> Source de l'image à déterminer

Le réseau LSTM est organisé de manière similaire au RNN, mais il y a deux états qui sont passés de couche en couche : l'état actuel C, et le vecteur caché H. À chaque unité, le vecteur caché H<sub>i</sub> est concaténé avec l'entrée X<sub>i</sub>, et ils contrôlent ce qui arrive à l'état C via des **portes**. Chaque porte est un réseau de neurones avec une activation sigmoïde (sortie dans la plage [0,1]), qui peut être considéré comme un masque au niveau des bits lorsqu'il est multiplié par le vecteur d'état. Il y a les portes suivantes (de gauche à droite sur l'image ci-dessus) :

* La **porte d'oubli** prend un vecteur caché et détermine quels composants du vecteur C nous devons oublier, et lesquels passer.
* La **porte d'entrée** prend certaines informations des vecteurs d'entrée et cachés et les insère dans l'état.
* La **porte de sortie** transforme l'état via une couche linéaire avec activation *tanh*, puis sélectionne certains de ses composants en utilisant un vecteur caché H<sub>i</sub> pour produire un nouvel état C<sub>i+1</sub>.

Les composants de l'état C peuvent être considérés comme des indicateurs qui peuvent être activés ou désactivés. Par exemple, lorsque nous rencontrons un nom *Alice* dans la séquence, nous pouvons vouloir supposer qu'il fait référence à un personnage féminin et activer l'indicateur dans l'état que nous avons un nom féminin dans la phrase. Lorsque nous rencontrons ensuite des phrases comme *et Tom*, nous activerons l'indicateur que nous avons un nom pluriel. Ainsi, en manipulant l'état, nous pouvons supposément garder une trace des propriétés grammaticales des parties de la phrase.

> ✅ Une excellente ressource pour comprendre les rouages des LSTM est cet excellent article [Understanding LSTM Networks](https://colah.github.io/posts/2015-08-Understanding-LSTMs/) par Christopher Olah.

## RNNs Bidirectionnels et Multicouches

Nous avons discuté des réseaux récurrents qui fonctionnent dans une seule direction, du début d'une séquence à la fin. Cela semble naturel, car cela ressemble à la façon dont nous lisons et écoutons la parole. Cependant, puisque dans de nombreux cas pratiques nous avons un accès aléatoire à la séquence d'entrée, il peut être judicieux d'exécuter un calcul récurrent dans les deux directions. De tels réseaux sont appelés RNNs **bidirectionnels**. Lorsqu'on traite un réseau bidirectionnel, nous aurions besoin de deux vecteurs d'état cachés, un pour chaque direction.

Un réseau récurrent, qu'il soit unidirectionnel ou bidirectionnel, capture certains motifs au sein d'une séquence et peut les stocker dans un vecteur d'état ou les passer en sortie. Comme avec les réseaux convolutifs, nous pouvons construire une autre couche récurrente au-dessus de la première pour capturer des motifs de niveau supérieur et construire à partir de motifs de bas niveau extraits par la première couche. Cela nous conduit à la notion de **RNN multicouche** qui se compose de deux réseaux récurrents ou plus, où la sortie de la couche précédente est passée à la couche suivante en tant qu'entrée.

![Image montrant un RNN multicouche de mémoire à long terme](../../../../../translated_images/multi-layer-lstm.dd975e29bb2a59fe58b429db833932d734c81f211cad2783797a9608984acb8c.fr.jpg)

*Image tirée [de cet excellent article](https://towardsdatascience.com/from-a-lstm-cell-to-a-multilayer-lstm-network-with-pytorch-2899eb5696f3) par Fernando López*

## ✍️ Exercices : Embeddings

Continuez votre apprentissage dans les notebooks suivants :

* [RNNs avec PyTorch](../../../../../lessons/5-NLP/16-RNN/RNNPyTorch.ipynb)
* [RNNs avec TensorFlow](../../../../../lessons/5-NLP/16-RNN/RNNTF.ipynb)

## Conclusion

Dans cette unité, nous avons vu que les RNNs peuvent être utilisés pour la classification de séquences, mais en fait, ils peuvent gérer de nombreuses autres tâches, telles que la génération de texte, la traduction automatique, et plus encore. Nous considérerons ces tâches dans la prochaine unité.

## 🚀 Défi

Lisez quelques documents sur les LSTMs et envisagez leurs applications :

- [Grid Long Short-Term Memory](https://arxiv.org/pdf/1507.01526v1.pdf)
- [Show, Attend and Tell: Neural Image Caption
Generation with Visual Attention](https://arxiv.org/pdf/1502.03044v2.pdf)

## [Quiz post-cours](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/216)

## Révision & Auto-étude

- [Understanding LSTM Networks](https://colah.github.io/posts/2015-08-Understanding-LSTMs/) par Christopher Olah.

## [Devoir : Notebooks](assignment.md)

**Avertissement** :  
Ce document a été traduit à l'aide de services de traduction automatique basés sur l'IA. Bien que nous nous efforçons d'assurer l'exactitude, veuillez noter que les traductions automatiques peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue native doit être considéré comme la source faisant autorité. Pour des informations critiques, une traduction humaine professionnelle est recommandée. Nous ne sommes pas responsables des malentendus ou des interprétations erronées résultant de l'utilisation de cette traduction.