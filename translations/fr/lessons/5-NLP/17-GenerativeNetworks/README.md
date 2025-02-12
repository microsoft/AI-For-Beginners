# Réseaux génératifs

## [Quiz pré-conférence](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/117)

Les réseaux de neurones récurrents (RNN) et leurs variantes à cellules gatées telles que les cellules de mémoire à long terme et à court terme (LSTM) et les unités récurrentes gatées (GRU) ont fourni un mécanisme pour la modélisation du langage en ce sens qu'ils peuvent apprendre l'ordre des mots et fournir des prédictions pour le mot suivant dans une séquence. Cela nous permet d'utiliser les RNN pour des **tâches génératives**, telles que la génération de texte ordinaire, la traduction automatique et même la légende d'images.

> ✅ Pensez à toutes les fois où vous avez bénéficié de tâches génératives telles que la complétion de texte pendant que vous tapez. Faites des recherches sur vos applications préférées pour voir si elles ont utilisé des RNN.

Dans l'architecture RNN que nous avons discutée dans l'unité précédente, chaque unité RNN produisait le prochain état caché en sortie. Cependant, nous pouvons également ajouter une autre sortie à chaque unité récurrente, ce qui nous permettrait de produire une **séquence** (qui est de la même longueur que la séquence originale). De plus, nous pouvons utiliser des unités RNN qui n'acceptent pas une entrée à chaque étape, mais prennent simplement un vecteur d'état initial, puis produisent une séquence de sorties.

Cela permet différentes architectures neuronales qui sont montrées dans l'image ci-dessous :

![Image montrant des motifs courants de réseaux de neurones récurrents.](../../../../../translated_images/unreasonable-effectiveness-of-rnn.541ead816778f42dce6c42d8a56c184729aa2378d059b851be4ce12b993033df.fr.jpg)

> Image provenant de l'article de blog [L'efficacité déraisonnable des réseaux de neurones récurrents](http://karpathy.github.io/2015/05/21/rnn-effectiveness/) par [Andrej Karpaty](http://karpathy.github.io/)

* **Un à un** est un réseau de neurones traditionnel avec une entrée et une sortie
* **Un à plusieurs** est une architecture générative qui accepte une valeur d'entrée et génère une séquence de valeurs de sortie. Par exemple, si nous voulons entraîner un réseau de **légende d'images** qui produirait une description textuelle d'une image, nous pouvons prendre une image comme entrée, la passer à travers un CNN pour obtenir son état caché, puis faire générer une chaîne récurrente des mots de la légende un par un
* **Plusieurs à un** correspond aux architectures RNN que nous avons décrites dans l'unité précédente, telles que la classification de texte
* **Plusieurs à plusieurs**, ou **séquence à séquence**, correspond à des tâches telles que **la traduction automatique**, où nous avons d'abord un RNN qui collecte toutes les informations de la séquence d'entrée dans l'état caché, et une autre chaîne RNN déroule cet état dans la séquence de sortie.

Dans cette unité, nous nous concentrerons sur des modèles génératifs simples qui nous aident à générer du texte. Pour simplifier, nous utiliserons une tokenisation au niveau des caractères.

Nous allons entraîner ce RNN pour générer du texte étape par étape. À chaque étape, nous prendrons une séquence de caractères de longueur `nchars` et demanderons au réseau de générer le prochain caractère de sortie pour chaque caractère d'entrée :

![Image montrant un exemple de génération RNN du mot 'HELLO'.](../../../../../translated_images/rnn-generate.56c54afb52f9781d63a7c16ea9c1b86cb70e6e1eae6a742b56b7b37468576b17.fr.png)

Lors de la génération de texte (durant l'inférence), nous commençons avec un **prompt**, qui est passé à travers les cellules RNN pour générer son état intermédiaire, puis à partir de cet état, la génération commence. Nous générons un caractère à la fois et passons l'état et le caractère généré à une autre cellule RNN pour générer le suivant, jusqu'à ce que nous générions suffisamment de caractères.

<img src="images/rnn-generate-inf.png" width="60%"/>

> Image de l'auteur

## ✍️ Exercices : Réseaux génératifs

Poursuivez votre apprentissage dans les notebooks suivants :

* [Réseaux génératifs avec PyTorch](../../../../../lessons/5-NLP/17-GenerativeNetworks/GenerativePyTorch.ipynb)
* [Réseaux génératifs avec TensorFlow](../../../../../lessons/5-NLP/17-GenerativeNetworks/GenerativeTF.ipynb)

## Génération de texte douce et température

La sortie de chaque cellule RNN est une distribution de probabilité de caractères. Si nous prenons toujours le caractère avec la plus haute probabilité comme le prochain caractère dans le texte généré, le texte peut souvent devenir "cyclique" entre les mêmes séquences de caractères encore et encore, comme dans cet exemple :

```
today of the second the company and a second the company ...
```

Cependant, si nous regardons la distribution de probabilité pour le prochain caractère, il se pourrait que la différence entre quelques probabilités les plus élevées ne soit pas énorme, par exemple, un caractère peut avoir une probabilité de 0,2, un autre - 0,19, etc. Par exemple, en cherchant le prochain caractère dans la séquence '*play*', le prochain caractère peut tout aussi bien être un espace ou **e** (comme dans le mot *player*).

Cela nous amène à la conclusion qu'il n'est pas toujours "juste" de sélectionner le caractère avec une probabilité plus élevée, car choisir le deuxième plus élevé pourrait toujours nous mener à un texte significatif. Il est plus judicieux de **prélever** des caractères à partir de la distribution de probabilité donnée par la sortie du réseau. Nous pouvons également utiliser un paramètre, **température**, qui va aplatir la distribution de probabilité, dans le cas où nous voulons ajouter plus de randomité, ou la rendre plus abrupte, si nous voulons nous en tenir davantage aux caractères de plus haute probabilité.

Explorez comment cette génération de texte douce est mise en œuvre dans les notebooks liés ci-dessus.

## Conclusion

Bien que la génération de texte puisse être utile en soi, les principaux avantages proviennent de la capacité à générer du texte en utilisant des RNN à partir d'un certain vecteur de caractéristiques initial. Par exemple, la génération de texte est utilisée dans le cadre de la traduction automatique (séquence à séquence, dans ce cas le vecteur d'état de l'*encodeur* est utilisé pour générer ou *décoder* le message traduit), ou pour générer une description textuelle d'une image (dans ce cas, le vecteur de caractéristiques proviendrait d'un extracteur CNN).

## 🚀 Défi

Suivez quelques leçons sur Microsoft Learn sur ce sujet

* Génération de texte avec [PyTorch](https://docs.microsoft.com/learn/modules/intro-natural-language-processing-pytorch/6-generative-networks/?WT.mc_id=academic-77998-cacaste)/[TensorFlow](https://docs.microsoft.com/learn/modules/intro-natural-language-processing-tensorflow/5-generative-networks/?WT.mc_id=academic-77998-cacaste)

## [Quiz post-conférence](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/217)

## Revue & Auto-apprentissage

Voici quelques articles pour approfondir vos connaissances

* Différentes approches de génération de texte avec Markov Chain, LSTM et GPT-2 : [article de blog](https://towardsdatascience.com/text-generation-gpt-2-lstm-markov-chain-9ea371820e1e)
* Exemple de génération de texte dans [la documentation Keras](https://keras.io/examples/generative/lstm_character_level_text_generation/)

## [Devoir](lab/README.md)

Nous avons vu comment générer du texte caractère par caractère. Dans le laboratoire, vous explorerez la génération de texte au niveau des mots.

**Avertissement** :  
Ce document a été traduit à l'aide de services de traduction automatique basés sur l'IA. Bien que nous nous efforçons d'assurer l'exactitude, veuillez noter que les traductions automatisées peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue natale doit être considéré comme la source autoritaire. Pour des informations critiques, une traduction humaine professionnelle est recommandée. Nous ne sommes pas responsables des malentendus ou des interprétations erronées résultant de l'utilisation de cette traduction.