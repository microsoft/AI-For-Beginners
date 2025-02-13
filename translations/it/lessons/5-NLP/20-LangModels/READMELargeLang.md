# Modèles de Langage de Grande Taille Pré-entrainés

Dans toutes nos tâches précédentes, nous avons entraîné un réseau de neurones pour accomplir une tâche spécifique en utilisant un ensemble de données étiquetées. Avec de grands modèles transformateurs, tels que BERT, nous utilisons la modélisation du langage de manière auto-supervisée pour construire un modèle linguistique, qui est ensuite spécialisé pour une tâche en aval spécifique grâce à un entraînement supplémentaire spécifique au domaine. Cependant, il a été démontré que les grands modèles de langage peuvent également résoudre de nombreuses tâches sans AUCUN entraînement spécifique au domaine. Une famille de modèles capables de le faire est appelée **GPT** : Transformateur Génératif Pré-entrainé.

## [Quiz pré-conférence](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/120)

## Génération de Texte et Perplexité

L'idée qu'un réseau de neurones puisse accomplir des tâches générales sans entraînement en aval est présentée dans l'article [Language Models are Unsupervised Multitask Learners](https://cdn.openai.com/better-language-models/language_models_are_unsupervised_multitask_learners.pdf). L'idée principale est que de nombreuses autres tâches peuvent être modélisées en utilisant **la génération de texte**, car comprendre le texte signifie essentiellement être capable de le produire. Étant donné que le modèle est entraîné sur une énorme quantité de texte qui englobe les connaissances humaines, il devient également informé sur une grande variété de sujets.

> Comprendre et être capable de produire du texte implique également de connaître quelque chose sur le monde qui nous entoure. Les gens apprennent également en lisant dans une large mesure, et le réseau GPT est similaire à cet égard.

Les réseaux de génération de texte fonctionnent en prédisant la probabilité du mot suivant $$P(w_N)$$. Cependant, la probabilité inconditionnelle du mot suivant est égale à la fréquence de ce mot dans le corpus de texte. GPT est capable de nous donner la **probabilité conditionnelle** du mot suivant, étant donné les mots précédents : $$P(w_N | w_{n-1}, ..., w_0)$$

> Vous pouvez en apprendre davantage sur les probabilités dans notre [Curriculum de Science des Données pour Débutants](https://github.com/microsoft/Data-Science-For-Beginners/tree/main/1-Introduction/04-stats-and-probability).

La qualité d'un modèle de génération de langage peut être définie à l'aide de la **perplexité**. C'est une métrique intrinsèque qui nous permet de mesurer la qualité du modèle sans aucun ensemble de données spécifique à la tâche. Elle est basée sur la notion de *probabilité d'une phrase* - le modèle attribue une haute probabilité à une phrase qui est susceptible d'être réelle (c'est-à-dire que le modèle n'est pas **perplexe** par rapport à elle), et une faible probabilité aux phrases qui ont moins de sens (par exemple, *Peut-il faire quoi ?*). Lorsque nous fournissons à notre modèle des phrases provenant d'un corpus de texte réel, nous nous attendons à ce qu'elles aient une haute probabilité et une faible **perplexité**. Mathématiquement, elle est définie comme la probabilité inverse normalisée de l'ensemble de test :
$$
\mathrm{Perplexity}(W) = \sqrt[N]{1\over P(W_1,...,W_N)}
$$ 

**Vous pouvez expérimenter avec la génération de texte en utilisant [l'éditeur de texte alimenté par GPT de Hugging Face](https://transformer.huggingface.co/doc/gpt2-large)**. Dans cet éditeur, vous commencez à écrire votre texte, et en appuyant sur **[TAB]**, plusieurs options de complétion vous seront proposées. Si elles sont trop courtes, ou si vous n'êtes pas satisfait, appuyez à nouveau sur [TAB], et vous aurez plus d'options, y compris des morceaux de texte plus longs.

## GPT est une Famille

GPT n'est pas un modèle unique, mais plutôt une collection de modèles développés et entraînés par [OpenAI](https://openai.com). 

Sous les modèles GPT, nous avons :

| [GPT-2](https://huggingface.co/docs/transformers/model_doc/gpt2#openai-gpt2) | [GPT 3](https://openai.com/research/language-models-are-few-shot-learners) | [GPT-4](https://openai.com/gpt-4) |
| -- | -- | -- |
|Modèle de langage avec jusqu'à 1,5 milliard de paramètres. | Modèle de langage avec jusqu'à 175 milliards de paramètres | 100T paramètres et accepte à la fois des entrées d'images et de texte et produit du texte. |


Les modèles GPT-3 et GPT-4 sont disponibles [en tant que service cognitif de Microsoft Azure](https://azure.microsoft.com/en-us/services/cognitive-services/openai-service/#overview?WT.mc_id=academic-77998-cacaste), et en tant que [API OpenAI](https://openai.com/api/).

## Ingénierie des Prompts

Étant donné que GPT a été entraîné sur de vastes volumes de données pour comprendre le langage et le code, il fournit des sorties en réponse à des entrées (prompts). Les prompts sont les entrées ou requêtes de GPT par lesquelles on donne des instructions aux modèles sur les tâches qu'ils doivent ensuite accomplir. Pour obtenir un résultat souhaité, vous avez besoin du prompt le plus efficace, ce qui implique de choisir les bons mots, formats, phrases ou même symboles. Cette approche est appelée [Ingénierie des Prompts](https://learn.microsoft.com/en-us/shows/ai-show/the-basics-of-prompt-engineering-with-azure-openai-service?WT.mc_id=academic-77998-bethanycheum).

[Cette documentation](https://learn.microsoft.com/en-us/semantic-kernel/prompt-engineering/?WT.mc_id=academic-77998-bethanycheum) vous fournit plus d'informations sur l'ingénierie des prompts.

## ✍️ Exemple de Notebook : [Jouer avec OpenAI-GPT](../../../../../lessons/5-NLP/20-LangModels/GPT-PyTorch.ipynb)

Poursuivez votre apprentissage dans les notebooks suivants :

* [Générer du texte avec OpenAI-GPT et Hugging Face Transformers](../../../../../lessons/5-NLP/20-LangModels/GPT-PyTorch.ipynb)

## Conclusion

Les nouveaux modèles de langage pré-entraînés en général ne modélisent pas seulement la structure du langage, mais contiennent également une vaste quantité de langage naturel. Ainsi, ils peuvent être utilisés efficacement pour résoudre certaines tâches de traitement du langage naturel dans des contextes zéro-shot ou few-shot.

## [Quiz post-conférence](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/220)

**Disclaimer**:  
This document has been translated using machine-based AI translation services. While we strive for accuracy, please be aware that automated translations may contain errors or inaccuracies. The original document in its native language should be considered the authoritative source. For critical information, professional human translation is recommended. We are not liable for any misunderstandings or misinterpretations arising from the use of this translation.