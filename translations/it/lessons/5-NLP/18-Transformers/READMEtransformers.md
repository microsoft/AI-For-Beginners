# Mécanismes d'Attention et Transformateurs

## [Quiz pré-conférence](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/118)

L'un des problèmes les plus importants dans le domaine du traitement du langage naturel (NLP) est **la traduction automatique**, une tâche essentielle qui sous-tend des outils tels que Google Translate. Dans cette section, nous nous concentrerons sur la traduction automatique, ou, plus généralement, sur toute tâche *séquence-à-séquence* (également appelée **transduction de phrases**).

Avec les RNN, la séquence-à-séquence est mise en œuvre par deux réseaux récurrents, où un réseau, l'**encodeur**, réduit une séquence d'entrée en un état caché, tandis qu'un autre réseau, le **décodeur**, déploie cet état caché en un résultat traduit. Il y a quelques problèmes avec cette approche :

* L'état final du réseau encodeur a du mal à se souvenir du début d'une phrase, ce qui entraîne une mauvaise qualité du modèle pour les longues phrases.
* Tous les mots d'une séquence ont le même impact sur le résultat. En réalité, cependant, certains mots spécifiques dans la séquence d'entrée ont souvent plus d'impact sur les sorties séquentielles que d'autres.

**Les Mécanismes d'Attention** fournissent un moyen de pondérer l'impact contextuel de chaque vecteur d'entrée sur chaque prédiction de sortie du RNN. La façon dont cela est mis en œuvre consiste à créer des raccourcis entre les états intermédiaires du RNN d'entrée et du RNN de sortie. De cette manière, lors de la génération du symbole de sortie y<sub>t</sub>, nous prendrons en compte tous les états cachés d'entrée h<sub>i</sub>, avec différents coefficients de poids α<sub>t,i</sub>.

![Image montrant un modèle encodeur/décodeur avec une couche d'attention additive](../../../../../translated_images/encoder-decoder-attention.7a726296894fb567aa2898c94b17b3289087f6705c11907df8301df9e5eeb3de.it.png)

> Le modèle encodeur-décodeur avec un mécanisme d'attention additive dans [Bahdanau et al., 2015](https://arxiv.org/pdf/1409.0473.pdf), cité depuis [ce billet de blog](https://lilianweng.github.io/lil-log/2018/06/24/attention-attention.html)

La matrice d'attention {α<sub>i,j</sub>} représenterait le degré d'importance de certains mots d'entrée dans la génération d'un mot donné dans la séquence de sortie. Ci-dessous se trouve un exemple de telle matrice :

![Image montrant un alignement d'exemple trouvé par RNNsearch-50, tirée de Bahdanau - arviz.org](../../../../../translated_images/bahdanau-fig3.09ba2d37f202a6af11de6c82d2d197830ba5f4528d9ea430eb65fd3a75065973.it.png)

> Figure de [Bahdanau et al., 2015](https://arxiv.org/pdf/1409.0473.pdf) (Fig.3)

Les mécanismes d'attention sont responsables d'une grande partie de l'état de l'art actuel ou presque dans le NLP. Cependant, l'ajout d'attention augmente considérablement le nombre de paramètres du modèle, ce qui a conduit à des problèmes d'échelle avec les RNN. Une contrainte clé de l'échelle des RNN est que la nature récurrente des modèles rend difficile le traitement par lots et la parallélisation de l'entraînement. Dans un RNN, chaque élément d'une séquence doit être traité dans un ordre séquentiel, ce qui signifie qu'il ne peut pas être facilement parallélisé.

![Encodeur Décodeur avec Attention](../../../../../lessons/5-NLP/18-Transformers/images/EncDecAttention.gif)

> Figure provenant du [Blog de Google](https://research.googleblog.com/2016/09/a-neural-network-for-machine.html)

L'adoption des mécanismes d'attention combinée à cette contrainte a conduit à la création des modèles de transformateurs désormais à la pointe de la technologie que nous connaissons et utilisons aujourd'hui, tels que BERT et Open-GPT3.

## Modèles de Transformateurs

L'une des idées principales derrière les transformateurs est d'éviter la nature séquentielle des RNN et de créer un modèle qui soit parallélisable pendant l'entraînement. Cela est réalisé en mettant en œuvre deux idées :

* encodage positionnel
* utilisation du mécanisme d'auto-attention pour capturer des motifs au lieu des RNN (ou des CNN) (c'est pourquoi le document qui introduit les transformateurs est intitulé *[Attention is all you need](https://arxiv.org/abs/1706.03762)*)

### Encodage/Emballage Positionnel

L'idée de l'encodage positionnel est la suivante. 
1. Lors de l'utilisation des RNN, la position relative des tokens est représentée par le nombre d'étapes, et n'a donc pas besoin d'être explicitement représentée. 
2. Cependant, une fois que nous passons à l'attention, nous devons connaître les positions relatives des tokens au sein d'une séquence. 
3. Pour obtenir l'encodage positionnel, nous augmentons notre séquence de tokens avec une séquence de positions de tokens dans la séquence (c'est-à-dire, une séquence de nombres 0,1, ...).
4. Nous mélangeons ensuite la position du token avec un vecteur d'embedding de token. Pour transformer la position (entier) en un vecteur, nous pouvons utiliser différentes approches :

* Embedding entraînable, similaire à l'embedding de token. C'est l'approche que nous considérons ici. Nous appliquons des couches d'embedding sur les tokens et leurs positions, résultant en des vecteurs d'embedding de mêmes dimensions, que nous ajoutons ensuite ensemble.
* Fonction d'encodage de position fixe, comme proposé dans l'article original.

<img src="images/pos-embedding.png" width="50%"/>

> Image par l'auteur

Le résultat que nous obtenons avec l'embedding positionnel incorpore à la fois le token original et sa position au sein d'une séquence.

### Auto-Attention Multi-Tête

Ensuite, nous devons capturer certains motifs au sein de notre séquence. Pour ce faire, les transformateurs utilisent un mécanisme d'**auto-attention**, qui est essentiellement une attention appliquée à la même séquence en tant qu'entrée et sortie. L'application de l'auto-attention nous permet de prendre en compte le **contexte** au sein de la phrase et de voir quels mots sont inter-reliés. Par exemple, cela nous permet de voir quels mots sont référés par des co-références, telles que *il*, et également de prendre en compte le contexte :

![](../../../../../translated_images/CoreferenceResolution.861924d6d384a7d68d8d0039d06a71a151f18a796b8b1330239d3590bd4947eb.it.png)

> Image provenant du [Blog de Google](https://research.googleblog.com/2017/08/transformer-novel-neural-network.html)

Dans les transformateurs, nous utilisons **l'Attention Multi-Tête** afin de donner au réseau la capacité de capturer plusieurs types de dépendances différents, par exemple les relations entre mots à long terme et à court terme, co-référence par rapport à autre chose, etc.

[Notebook TensorFlow](../../../../../lessons/5-NLP/18-Transformers/TransformersTF.ipynb) contient plus de détails sur la mise en œuvre des couches de transformateurs.

### Attention Encodeur-Décodeur

Dans les transformateurs, l'attention est utilisée à deux endroits :

* Pour capturer des motifs au sein du texte d'entrée à l'aide de l'auto-attention
* Pour effectuer la traduction de séquence - c'est la couche d'attention entre l'encodeur et le décodeur.

L'attention encodeur-décodeur est très similaire au mécanisme d'attention utilisé dans les RNN, comme décrit au début de cette section. Ce diagramme animé explique le rôle de l'attention encodeur-décodeur.

![GIF animé montrant comment les évaluations sont effectuées dans les modèles de transformateurs.](../../../../../lessons/5-NLP/18-Transformers/images/transformer-animated-explanation.gif)

Puisque chaque position d'entrée est mappée indépendamment à chaque position de sortie, les transformateurs peuvent mieux se paralléliser que les RNN, ce qui permet des modèles de langage beaucoup plus grands et plus expressifs. Chaque tête d'attention peut être utilisée pour apprendre différentes relations entre les mots, ce qui améliore les tâches de traitement du langage naturel en aval.

## BERT

**BERT** (Représentations d'Encodeur Bidirectionnelles à partir de Transformateurs) est un très grand réseau de transformateurs à plusieurs couches avec 12 couches pour *BERT-base*, et 24 pour *BERT-large*. Le modèle est d'abord pré-entraîné sur un grand corpus de données textuelles (WikiPedia + livres) en utilisant un entraînement non supervisé (prédiction de mots masqués dans une phrase). Au cours de la pré-formation, le modèle absorbe des niveaux significatifs de compréhension linguistique qui peuvent ensuite être exploités avec d'autres ensembles de données via un ajustement fin. Ce processus est appelé **apprentissage par transfert**.

![image de http://jalammar.github.io/illustrated-bert/](../../../../../translated_images/jalammarBERT-language-modeling-masked-lm.34f113ea5fec4362e39ee4381aab7cad06b5465a0b5f053a0f2aa05fbe14e746.it.png)

> Image [source](http://jalammar.github.io/illustrated-bert/)

## ✍️ Exercices : Transformateurs

Poursuivez votre apprentissage dans les notebooks suivants :

* [Transformateurs en PyTorch](../../../../../lessons/5-NLP/18-Transformers/TransformersPyTorch.ipynb)
* [Transformateurs en TensorFlow](../../../../../lessons/5-NLP/18-Transformers/TransformersTF.ipynb)

## Conclusion

Dans cette leçon, vous avez appris sur les Transformateurs et les Mécanismes d'Attention, tous des outils essentiels dans la boîte à outils NLP. Il existe de nombreuses variations des architectures de Transformateurs, y compris BERT, DistilBERT, BigBird, OpenGPT3 et plus encore qui peuvent être ajustées. Le [package HuggingFace](https://github.com/huggingface/) fournit un référentiel pour entraîner bon nombre de ces architectures avec PyTorch et TensorFlow.

## 🚀 Défi

## [Quiz post-conférence](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/218)

## Révision et Auto-étude

* [Billet de blog](https://mchromiak.github.io/articles/2017/Sep/12/Transformer-Attention-is-all-you-need/), expliquant l'article classique [Attention is all you need](https://arxiv.org/abs/1706.03762) sur les transformateurs.
* [Une série de billets de blog](https://towardsdatascience.com/transformers-explained-visually-part-1-overview-of-functionality-95a6dd460452) sur les transformateurs, expliquant l'architecture en détail.

## [Devoir](assignment.md)

**Disclaimer**: 
This document has been translated using machine-based AI translation services. While we strive for accuracy, please be aware that automated translations may contain errors or inaccuracies. The original document in its native language should be considered the authoritative source. For critical information, professional human translation is recommended. We are not liable for any misunderstandings or misinterpretations arising from the use of this translation.