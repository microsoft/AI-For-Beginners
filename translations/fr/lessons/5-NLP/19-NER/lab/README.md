# NER

Travail pratique issu du [programme AI for Beginners](https://github.com/microsoft/ai-for-beginners).

## Tâche

Dans ce travail pratique, vous devez entraîner un modèle de reconnaissance d'entités nommées (NER) pour les termes médicaux.

## Le jeu de données

Pour entraîner un modèle NER, nous avons besoin d'un jeu de données correctement annoté avec des entités médicales. Le [jeu de données BC5CDR](https://biocreative.bioinformatics.udel.edu/tasks/biocreative-v/track-3-cdr/) contient des entités annotées de maladies et de produits chimiques provenant de plus de 1500 articles. Vous pouvez télécharger ce jeu de données après vous être inscrit sur leur site web.

Le jeu de données BC5CDR ressemble à ceci :

```
6794356|t|Tricuspid valve regurgitation and lithium carbonate toxicity in a newborn infant.
6794356|a|A newborn with massive tricuspid regurgitation, atrial flutter, congestive heart failure, and a high serum lithium level is described. This is the first patient to initially manifest tricuspid regurgitation and atrial flutter, and the 11th described patient with cardiac disease among infants exposed to lithium compounds in the first trimester of pregnancy. Sixty-three percent of these infants had tricuspid valve involvement. Lithium carbonate may be a factor in the increasing incidence of congenital heart disease when taken during early pregnancy. It also causes neurologic depression, cyanosis, and cardiac arrhythmia when consumed prior to delivery.
6794356	0	29	Tricuspid valve regurgitation	Disease	D014262
6794356	34	51	lithium carbonate	Chemical	D016651
6794356	52	60	toxicity	Disease	D064420
...
```

Dans ce jeu de données, le titre de l'article et le résumé se trouvent dans les deux premières lignes, suivis des entités individuelles, avec leurs positions de début et de fin dans le bloc titre+résumé. En plus du type d'entité, vous obtenez l'ID d'ontologie de cette entité dans une ontologie médicale.

Vous devrez écrire du code Python pour convertir cela en encodage BIO.

## Le réseau

Une première tentative de NER peut être réalisée en utilisant un réseau LSTM, comme dans notre exemple vu pendant le cours. Cependant, dans les tâches de traitement du langage naturel (NLP), l'[architecture transformer](https://fr.wikipedia.org/wiki/Transformer_(mod%C3%A8le_d%27apprentissage_automatique)), et en particulier les [modèles de langage BERT](https://fr.wikipedia.org/wiki/BERT_(mod%C3%A8le_de_langage)), donnent de bien meilleurs résultats. Les modèles BERT pré-entraînés comprennent la structure générale d'une langue et peuvent être ajustés pour des tâches spécifiques avec des jeux de données relativement petits et des coûts computationnels réduits.

Étant donné que nous prévoyons d'appliquer le NER à un scénario médical, il est logique d'utiliser un modèle BERT entraîné sur des textes médicaux. Microsoft Research a publié un modèle pré-entraîné appelé [PubMedBERT][PubMedBERT] ([publication][PubMedBERT-Pub]), qui a été ajusté à l'aide de textes provenant du dépôt [PubMed](https://pubmed.ncbi.nlm.nih.gov/).

Le standard *de facto* pour entraîner des modèles transformer est la bibliothèque [Hugging Face Transformers](https://huggingface.co/). Elle contient également un dépôt de modèles pré-entraînés maintenus par la communauté, y compris PubMedBERT. Pour charger et utiliser ce modèle, il suffit de quelques lignes de code :

```python
model_name = "microsoft/BiomedNLP-PubMedBERT-base-uncased-abstract"
classes = ... # number of classes: 2*entities+1
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = BertForTokenClassification.from_pretrained(model_name, classes)
```

Cela nous donne le `model` lui-même, conçu pour une tâche de classification de tokens avec un nombre de `classes`, ainsi qu'un objet `tokenizer` qui peut diviser le texte d'entrée en tokens. Vous devrez convertir le jeu de données en format BIO, en tenant compte de la tokenisation de PubMedBERT. Vous pouvez utiliser [ce bout de code Python](https://gist.github.com/shwars/580b55684be3328eb39ecf01b9cbbd88) comme source d'inspiration.

## Conclusion

Cette tâche est très proche de celles que vous pourriez rencontrer si vous souhaitez obtenir des informations approfondies à partir de grands volumes de textes en langage naturel. Dans notre cas, nous pouvons appliquer notre modèle entraîné au [jeu de données d'articles liés au COVID](https://www.kaggle.com/allen-institute-for-ai/CORD-19-research-challenge) et voir quelles informations nous pourrons en tirer. [Cet article de blog](https://soshnikov.com/science/analyzing-medical-papers-with-azure-and-text-analytics-for-health/) et [cet article scientifique](https://www.mdpi.com/2504-2289/6/1/4) décrivent les recherches qui peuvent être effectuées sur ce corpus d'articles en utilisant le NER.

**Avertissement** :  
Ce document a été traduit à l'aide du service de traduction automatique [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforcions d'assurer l'exactitude, veuillez noter que les traductions automatisées peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue d'origine doit être considéré comme la source faisant autorité. Pour des informations critiques, il est recommandé de recourir à une traduction humaine professionnelle. Nous déclinons toute responsabilité en cas de malentendus ou d'interprétations erronées résultant de l'utilisation de cette traduction.