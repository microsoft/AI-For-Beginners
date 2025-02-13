# Modèle Skip-Gram pour l'Entraînement

Devoir de [AI for Beginners Curriculum](https://github.com/microsoft/ai-for-beginners).

## Tâche

Dans ce laboratoire, nous vous mettons au défi d'entraîner un modèle Word2Vec en utilisant la technique Skip-Gram. Entraînez un réseau avec des embeddings pour prédire les mots voisins dans une fenêtre Skip-Gram de $N$-tokens de large. Vous pouvez utiliser [le code de cette leçon](../../../../../../lessons/5-NLP/15-LanguageModeling/CBoW-TF.ipynb) et le modifier légèrement.

## Le Jeu de Données

Vous êtes libre d'utiliser n'importe quel livre. Vous pouvez trouver de nombreux textes gratuits sur [Project Gutenberg](https://www.gutenberg.org/), par exemple, voici un lien direct vers [Les Aventures d'Alice au Pays des Merveilles](https://www.gutenberg.org/files/11/11-0.txt) de Lewis Carroll. Ou, vous pouvez utiliser les pièces de Shakespeare, que vous pouvez obtenir en utilisant le code suivant :

```python
path_to_file = tf.keras.utils.get_file(
   'shakespeare.txt', 
   'https://storage.googleapis.com/download.tensorflow.org/data/shakespeare.txt')
text = open(path_to_file, 'rb').read().decode(encoding='utf-8')
```

## Explorez !

Si vous avez le temps et que vous souhaitez approfondir le sujet, essayez d'explorer plusieurs éléments :

* Comment la taille de l'embedding affecte-t-elle les résultats ?
* Comment les différents styles de texte influencent-ils le résultat ?
* Prenez plusieurs types de mots très différents et leurs synonymes, obtenez leurs représentations vectorielles, appliquez l'ACP pour réduire les dimensions à 2 et tracez-les dans un espace 2D. Voyez-vous des motifs ?

**Avertissement** :  
Ce document a été traduit à l'aide de services de traduction automatique basés sur l'IA. Bien que nous nous efforçons d'assurer l'exactitude, veuillez noter que les traductions automatiques peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue native doit être considéré comme la source autorisée. Pour des informations critiques, une traduction humaine professionnelle est recommandée. Nous ne sommes pas responsables des malentendus ou des interprétations erronées résultant de l'utilisation de cette traduction.