# Traitement du Langage Naturel

![Résumé des tâches de traitement du langage naturel dans un doodle](../../../../translated_images/ai-nlp.b22dcb8ca4707ceaee8576db1c5f4089c8cac2f454e9e03ea554f07fda4556b8.fr.png)

Dans cette section, nous allons nous concentrer sur l'utilisation des réseaux de neurones pour gérer des tâches liées au **Traitement du Langage Naturel (NLP)**. Il existe de nombreux problèmes de NLP que nous souhaitons que les ordinateurs soient capables de résoudre :

* **Classification de texte** est un problème de classification typique concernant des séquences de texte. Des exemples incluent la classification des messages e-mail en spam ou non-spam, ou la catégorisation des articles en sport, affaires, politique, etc. De plus, lors du développement de chatbots, nous devons souvent comprendre ce qu'un utilisateur voulait dire -- dans ce cas, nous traitons de la **classification d'intentions**. Souvent, dans la classification d'intentions, nous devons gérer de nombreuses catégories.
* **Analyse de sentiment** est un problème de régression typique, où nous devons attribuer un nombre (un sentiment) correspondant à la manière dont le sens d'une phrase est positif ou négatif. Une version plus avancée de l'analyse de sentiment est l'**analyse de sentiment basée sur les aspects** (ABSA), où nous attribuons un sentiment non pas à l'ensemble de la phrase, mais à différentes parties de celle-ci (aspects), par exemple *Dans ce restaurant, j'ai aimé la cuisine, mais l'atmosphère était horrible*.
* **Reconnaissance d'entités nommées** (NER) fait référence au problème d'extraction de certaines entités d'un texte. Par exemple, nous pourrions avoir besoin de comprendre que dans la phrase *J'ai besoin de voler à Paris demain*, le mot *demain* fait référence à une DATE, et *Paris* est un LIEU.  
* **Extraction de mots-clés** est similaire à NER, mais nous devons extraire automatiquement des mots importants pour le sens de la phrase, sans pré-entraînement pour des types d'entités spécifiques.
* **Clustering de texte** peut être utile lorsque nous voulons regrouper des phrases similaires, par exemple, des demandes similaires dans des conversations de support technique.
* **Réponse à des questions** fait référence à la capacité d'un modèle à répondre à une question spécifique. Le modèle reçoit un passage de texte et une question en entrée, et il doit fournir un endroit dans le texte où la réponse à la question se trouve (ou, parfois, générer le texte de réponse).
* **Génération de texte** est la capacité d'un modèle à générer du nouveau texte. Cela peut être considéré comme une tâche de classification qui prédit la prochaine lettre/mot en fonction d'un *texte d'invite*. Des modèles de génération de texte avancés, tels que GPT-3, sont capables de résoudre d'autres tâches de NLP telles que la classification en utilisant une technique appelée [programmation par invite](https://towardsdatascience.com/software-3-0-how-prompting-will-change-the-rules-of-the-game-a982fbfe1e0) ou [ingénierie d'invite](https://medium.com/swlh/openai-gpt-3-and-prompt-engineering-dcdc2c5fcd29).
* **Résumé de texte** est une technique lorsque nous voulons qu'un ordinateur "lise" un long texte et le résume en quelques phrases.
* **Traduction automatique** peut être vue comme une combinaison de compréhension de texte dans une langue et de génération de texte dans une autre.

Au départ, la plupart des tâches de NLP étaient résolues en utilisant des méthodes traditionnelles telles que les grammaires. Par exemple, dans la traduction automatique, des analyseurs étaient utilisés pour transformer la phrase initiale en un arbre syntaxique, puis des structures sémantiques de niveau supérieur étaient extraites pour représenter le sens de la phrase, et sur la base de ce sens et de la grammaire de la langue cible, le résultat était généré. De nos jours, de nombreuses tâches de NLP sont plus efficacement résolues en utilisant des réseaux de neurones.

> De nombreuses méthodes classiques de NLP sont implémentées dans la bibliothèque Python [Natural Language Processing Toolkit (NLTK)](https://www.nltk.org). Il existe un excellent [livre NLTK](https://www.nltk.org/book/) disponible en ligne qui couvre comment différentes tâches de NLP peuvent être résolues en utilisant NLTK.

Dans notre cours, nous nous concentrerons principalement sur l'utilisation des réseaux de neurones pour le NLP, et nous utiliserons NLTK lorsque cela sera nécessaire.

Nous avons déjà appris à utiliser des réseaux de neurones pour traiter des données tabulaires et des images. La principale différence entre ces types de données et le texte est que le texte est une séquence de longueur variable, tandis que la taille d'entrée dans le cas des images est connue à l'avance. Bien que les réseaux de neurones convolutifs puissent extraire des motifs des données d'entrée, les motifs dans le texte sont plus complexes. Par exemple, nous pouvons avoir une négation séparée du sujet qui peut être arbitraire pour de nombreux mots (par exemple, *Je n'aime pas les oranges*, contre *Je n'aime pas ces grosses oranges colorées et savoureuses*), et cela doit toujours être interprété comme un seul motif. Ainsi, pour traiter le langage, nous devons introduire de nouveaux types de réseaux de neurones, tels que les *réseaux récurrents* et les *transformateurs*.

## Installer les bibliothèques

Si vous utilisez une installation locale de Python pour suivre ce cours, vous devrez peut-être installer toutes les bibliothèques requises pour le NLP en utilisant les commandes suivantes :

**Pour PyTorch**
```bash
pip install -r requirements-torch.txt
```
**Pour TensorFlow**
```bash
pip install -r requirements-tf.txt
```

> Vous pouvez essayer le NLP avec TensorFlow sur [Microsoft Learn](https://docs.microsoft.com/learn/modules/intro-natural-language-processing-tensorflow/?WT.mc_id=academic-77998-cacaste)

## Avertissement GPU

Dans cette section, dans certains exemples, nous allons entraîner des modèles assez volumineux.
* **Utilisez un ordinateur avec GPU** : Il est conseillé d'exécuter vos notebooks sur un ordinateur avec GPU pour réduire les temps d'attente lors du travail avec de grands modèles.
* **Contraintes de mémoire GPU** : L'exécution sur un GPU peut entraîner des situations où vous manquez de mémoire GPU, surtout lors de l'entraînement de grands modèles.
* **Consommation de mémoire GPU** : La quantité de mémoire GPU consommée pendant l'entraînement dépend de divers facteurs, y compris la taille du mini-lot.
* **Minimiser la taille du mini-lot** : Si vous rencontrez des problèmes de mémoire GPU, envisagez de réduire la taille du mini-lot dans votre code comme solution potentielle.
* **Libération de mémoire GPU TensorFlow** : Les anciennes versions de TensorFlow peuvent ne pas libérer correctement la mémoire GPU lors de l'entraînement de plusieurs modèles dans un même noyau Python. Pour gérer efficacement l'utilisation de la mémoire GPU, vous pouvez configurer TensorFlow pour allouer de la mémoire GPU uniquement au besoin.
* **Inclusion de code** : Pour configurer TensorFlow afin de faire croître l'allocation de mémoire GPU uniquement lorsque cela est nécessaire, incluez le code suivant dans vos notebooks :

```python
physical_devices = tf.config.list_physical_devices('GPU') 
if len(physical_devices)>0:
    tf.config.experimental.set_memory_growth(physical_devices[0], True) 
```

Si vous êtes intéressé par l'apprentissage du NLP d'un point de vue classique du ML, visitez [cette suite de leçons](https://github.com/microsoft/ML-For-Beginners/tree/main/6-NLP).

## Dans cette section
Dans cette section, nous allons apprendre sur :

* [Représentation du texte en tant que tenseurs](13-TextRep/README.md)
* [Mots d'embedding](14-Emdeddings/README.md)
* [Modélisation de la langue](15-LanguageModeling/README.md)
* [Réseaux de neurones récurrents](16-RNN/README.md)
* [Réseaux génératifs](17-GenerativeNetworks/README.md)
* [Transformateurs](18-Transformers/README.md)

**Avertissement** :  
Ce document a été traduit à l'aide de services de traduction automatique basés sur l'IA. Bien que nous nous efforçons d'assurer l'exactitude, veuillez noter que les traductions automatiques peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue native doit être considéré comme la source autoritaire. Pour des informations critiques, une traduction humaine professionnelle est recommandée. Nous ne sommes pas responsables des malentendus ou des interprétations erronées résultant de l'utilisation de cette traduction.