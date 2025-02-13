# NER

Devoir de laboratoire du [Curriculum AI pour Débutants](https://github.com/microsoft/ai-for-beginners).

## Tâche

Dans ce laboratoire, vous devez entraîner un modèle de reconnaissance d'entités nommées pour des termes médicaux.

## Le Jeu de Données

Pour entraîner le modèle NER, nous avons besoin d'un jeu de données correctement étiqueté avec des entités médicales. Le [jeu de données BC5CDR](https://biocreative.bioinformatics.udel.edu/tasks/biocreative-v/track-3-cdr/) contient des entités de maladies et de produits chimiques étiquetées provenant de plus de 1500 articles. Vous pouvez télécharger le jeu de données après vous être inscrit sur leur site web.

Le jeu de données BC5CDR ressemble à ceci :

```
6794356|t|Tricuspid valve regurgitation and lithium carbonate toxicity in a newborn infant.
6794356|a|A newborn with massive tricuspid regurgitation, atrial flutter, congestive heart failure, and a high serum lithium level is described. This is the first patient to initially manifest tricuspid regurgitation and atrial flutter, and the 11th described patient with cardiac disease among infants exposed to lithium compounds in the first trimester of pregnancy. Sixty-three percent of these infants had tricuspid valve involvement. Lithium carbonate may be a factor in the increasing incidence of congenital heart disease when taken during early pregnancy. It also causes neurologic depression, cyanosis, and cardiac arrhythmia when consumed prior to delivery.
6794356	0	29	Tricuspid valve regurgitation	Disease	D014262
6794356	34	51	lithium carbonate	Chemical	D016651
6794356	52	60	toxicity	Disease	D064420
...
```

Dans ce jeu de données, il y a le titre de l'article et le résumé dans les deux premières lignes, puis il y a des entités individuelles, avec des positions de début et de fin dans le bloc titre+résumé. En plus du type d'entité, vous obtenez l'ID d'ontologie de cette entité dans une certaine ontologie médicale.

Vous devrez écrire un peu de code Python pour convertir cela en encodage BIO.

## Le Réseau

La première tentative de NER peut être réalisée en utilisant un réseau LSTM, comme dans notre exemple que vous avez vu pendant la leçon. Cependant, dans les tâches de NLP, l'[architecture de transformateur](https://en.wikipedia.org/wiki/Transformer_(machine_learning_model)), et spécifiquement les [modèles de langage BERT](https://en.wikipedia.org/wiki/BERT_(language_model)), montrent de bien meilleurs résultats. Les modèles BERT pré-entraînés comprennent la structure générale d'une langue et peuvent être affinés pour des tâches spécifiques avec des jeux de données relativement petits et des coûts computationnels réduits.

Étant donné que nous prévoyons d'appliquer NER à un scénario médical, il est logique d'utiliser un modèle BERT entraîné sur des textes médicaux. Microsoft Research a publié un modèle pré-entraîné appelé [PubMedBERT][PubMedBERT] ([publication][PubMedBERT-Pub]), qui a été affiné en utilisant des textes du dépôt [PubMed](https://pubmed.ncbi.nlm.nih.gov/).

Le standard *de facto* pour l'entraînement des modèles de transformateurs est la bibliothèque [Hugging Face Transformers](https://huggingface.co/). Elle contient également un dépôt de modèles pré-entraînés maintenus par la communauté, y compris PubMedBERT. Pour charger et utiliser ce modèle, nous avons juste besoin de quelques lignes de code :

```python
model_name = "microsoft/BiomedNLP-PubMedBERT-base-uncased-abstract"
classes = ... # number of classes: 2*entities+1
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = BertForTokenClassification.from_pretrained(model_name, classes)
```

Cela nous donne l'objet `model` itself, built for token classification task using `classes` number of classes, as well as `tokenizer` qui peut diviser le texte d'entrée en tokens. Vous devrez convertir le jeu de données au format BIO, en tenant compte de la tokenisation de PubMedBERT. Vous pouvez utiliser [ce morceau de code Python](https://gist.github.com/shwars/580b55684be3328eb39ecf01b9cbbd88) comme source d'inspiration.

## Conclusion

Cette tâche est très proche de la tâche réelle que vous serez probablement amené à réaliser si vous souhaitez obtenir plus d'informations sur de grands volumes de textes en langage naturel. Dans notre cas, nous pouvons appliquer notre modèle entraîné au [jeu de données d'articles liés au COVID](https://www.kaggle.com/allen-institute-for-ai/CORD-19-research-challenge) et voir quelles informations nous pourrons obtenir. [Cet article de blog](https://soshnikov.com/science/analyzing-medical-papers-with-azure-and-text-analytics-for-health/) et [ce papier](https://www.mdpi.com/2504-2289/6/1/4) décrivent les recherches qui peuvent être menées sur ce corpus d'articles en utilisant NER.

**Avertissement** :  
Ce document a été traduit à l'aide de services de traduction automatique basés sur l'IA. Bien que nous nous efforçons d'assurer l'exactitude, veuillez noter que les traductions automatisées peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue natale doit être considéré comme la source autoritaire. Pour des informations critiques, une traduction humaine professionnelle est recommandée. Nous ne sommes pas responsables des malentendus ou des interprétations erronées résultant de l'utilisation de cette traduction.