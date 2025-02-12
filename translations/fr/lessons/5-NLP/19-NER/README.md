# Reconnaissance d'entités nommées

Jusqu'à présent, nous nous sommes principalement concentrés sur une tâche de traitement du langage naturel (NLP) - la classification. Cependant, il existe également d'autres tâches NLP qui peuvent être réalisées avec des réseaux neuronaux. L'une de ces tâches est la **[Reconnaissance d'entités nommées](https://wikipedia.org/wiki/Named-entity_recognition)** (NER), qui consiste à reconnaître des entités spécifiques dans un texte, telles que des lieux, des noms de personnes, des intervalles de date-heure, des formules chimiques, etc.

## [Quiz pré-cours](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/119)

## Exemple d'utilisation de NER

Supposons que vous souhaitiez développer un chatbot en langage naturel, similaire à Amazon Alexa ou Google Assistant. Le fonctionnement des chatbots intelligents consiste à *comprendre* ce que l'utilisateur veut en effectuant une classification de texte sur la phrase d'entrée. Le résultat de cette classification est ce que l'on appelle **l'intention**, qui détermine ce que le chatbot doit faire.

<img alt="Bot NER" src="images/bot-ner.png" width="50%"/>

> Image par l'auteur

Cependant, un utilisateur peut fournir certains paramètres dans le cadre de la phrase. Par exemple, lorsqu'elle demande la météo, elle peut spécifier un lieu ou une date. Un bot doit être capable de comprendre ces entités et de remplir les espaces de paramètres en conséquence avant d'effectuer l'action. C'est exactement là que NER entre en jeu.

> ✅ Un autre exemple serait [l'analyse de papiers médicaux scientifiques](https://soshnikov.com/science/analyzing-medical-papers-with-azure-and-text-analytics-for-health/). L'une des principales choses à rechercher sont des termes médicaux spécifiques, tels que des maladies et des substances médicales. Bien qu'un petit nombre de maladies puisse probablement être extrait par une recherche de sous-chaînes, des entités plus complexes, telles que des composés chimiques et des noms de médicaments, nécessitent une approche plus complexe.

## NER comme classification de tokens

Les modèles NER sont essentiellement des **modèles de classification de tokens**, car pour chacun des tokens d'entrée, nous devons décider s'il appartient à une entité ou non, et si c'est le cas - à quelle classe d'entité.

Considérons le titre de papier suivant :

**Régurgitation de la valve tricuspide** et **toxicité du carbonate de lithium** chez un nouveau-né.

Les entités ici sont :

* La régurgitation de la valve tricuspide est une maladie (`DIS`)
* Le carbonate de lithium est une substance chimique (`CHEM`)
* La toxicité est également une maladie (`DIS`)

Remarquez qu'une entité peut s'étendre sur plusieurs tokens. Et, comme dans ce cas, nous devons faire la distinction entre deux entités consécutives. Ainsi, il est courant d'utiliser deux classes pour chaque entité - une spécifiant le premier token de l'entité (souvent le préfixe `B-` est utilisé, pour **b**eginning), et une autre - la continuation d'une entité (`I-`, pour **i**nner token). Nous utilisons également `O` comme classe pour représenter tous les **o**tres tokens. Ce marquage de tokens est appelé [marquage BIO](https://en.wikipedia.org/wiki/Inside%E2%80%93outside%E2%80%93beginning_(tagging)) (ou IOB). Une fois étiqueté, notre titre ressemblera à ceci :

Token | Tag
------|-----
Tricuspid | B-DIS
valve | I-DIS
regurgitation | I-DIS
and | O
lithium | B-CHEM
carbonate | I-CHEM
toxicity | B-DIS
in | O
a | O
newborn | O
infant | O
. | O

Puisque nous devons établir une correspondance un à un entre les tokens et les classes, nous pouvons entraîner un modèle de réseau neuronal **many-to-many** à partir de cette image :

![Image montrant des motifs communs de réseaux neuronaux récurrents.](../../../../../translated_images/unreasonable-effectiveness-of-rnn.541ead816778f42dce6c42d8a56c184729aa2378d059b851be4ce12b993033df.fr.jpg)

> *Image tirée [de cet article de blog](http://karpathy.github.io/2015/05/21/rnn-effectiveness/) par [Andrej Karpathy](http://karpathy.github.io/). Les modèles de classification de tokens NER correspondent à l'architecture de réseau la plus à droite sur cette image.*

## Entraînement des modèles NER

Étant donné qu'un modèle NER est essentiellement un modèle de classification de tokens, nous pouvons utiliser des RNN que nous connaissons déjà pour cette tâche. Dans ce cas, chaque bloc de réseau récurrent renverra l'ID du token. L'exemple de notebook suivant montre comment entraîner un LSTM pour la classification de tokens.

## ✍️ Notebooks d'exemple : NER

Poursuivez votre apprentissage dans le notebook suivant :

* [NER avec TensorFlow](../../../../../lessons/5-NLP/19-NER/NER-TF.ipynb)

## Conclusion

Un modèle NER est un **modèle de classification de tokens**, ce qui signifie qu'il peut être utilisé pour effectuer une classification de tokens. C'est une tâche très courante en NLP, aidant à reconnaître des entités spécifiques dans le texte, y compris des lieux, des noms, des dates, et plus encore.

## 🚀 Défi

Complétez la tâche liée ci-dessous pour entraîner un modèle de reconnaissance d'entités nommées pour des termes médicaux, puis essayez-le sur un ensemble de données différent.

## [Quiz post-cours](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/219)

## Revue et auto-apprentissage

Lisez le blog [L'efficacité déraisonnable des réseaux neuronaux récurrents](http://karpathy.github.io/2015/05/21/rnn-effectiveness/) et suivez la section Lecture complémentaire dans cet article pour approfondir vos connaissances.

## [Devoir](lab/README.md)

Dans le devoir pour cette leçon, vous devrez entraîner un modèle de reconnaissance d'entités médicales. Vous pouvez commencer par entraîner un modèle LSTM comme décrit dans cette leçon, puis passer à l'utilisation du modèle de transformateur BERT. Lisez [les instructions](lab/README.md) pour obtenir tous les détails.

**Avertissement** :  
Ce document a été traduit à l'aide de services de traduction automatique basés sur l'IA. Bien que nous nous efforçons d'assurer l'exactitude, veuillez noter que les traductions automatiques peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue native doit être considéré comme la source autoritaire. Pour des informations critiques, une traduction humaine professionnelle est recommandée. Nous ne sommes pas responsables des malentendus ou des interprétations erronées résultant de l'utilisation de cette traduction.