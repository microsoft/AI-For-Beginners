# NER

Laboratorio de Asignación del [Currículo de IA para Principiantes](https://github.com/microsoft/ai-for-beginners).

## Tarea

En este laboratorio, necesitas entrenar un modelo de reconocimiento de entidades nombradas para términos médicos.

## El Conjunto de Datos

Para entrenar el modelo NER, necesitamos un conjunto de datos debidamente etiquetado con entidades médicas. El [conjunto de datos BC5CDR](https://biocreative.bioinformatics.udel.edu/tasks/biocreative-v/track-3-cdr/) contiene enfermedades y entidades químicas etiquetadas de más de 1500 artículos. Puedes descargar el conjunto de datos después de registrarte en su sitio web.

El conjunto de datos BC5CDR se ve así:

```
6794356|t|Tricuspid valve regurgitation and lithium carbonate toxicity in a newborn infant.
6794356|a|A newborn with massive tricuspid regurgitation, atrial flutter, congestive heart failure, and a high serum lithium level is described. This is the first patient to initially manifest tricuspid regurgitation and atrial flutter, and the 11th described patient with cardiac disease among infants exposed to lithium compounds in the first trimester of pregnancy. Sixty-three percent of these infants had tricuspid valve involvement. Lithium carbonate may be a factor in the increasing incidence of congenital heart disease when taken during early pregnancy. It also causes neurologic depression, cyanosis, and cardiac arrhythmia when consumed prior to delivery.
6794356	0	29	Tricuspid valve regurgitation	Disease	D014262
6794356	34	51	lithium carbonate	Chemical	D016651
6794356	52	60	toxicity	Disease	D064420
...
```

En este conjunto de datos, hay un título de artículo y un resumen en las dos primeras líneas, y luego hay entidades individuales, con posiciones de inicio y fin dentro del bloque de título + resumen. Además del tipo de entidad, obtienes el ID de ontología de esta entidad dentro de alguna ontología médica.

Necesitarás escribir algo de código en Python para convertir esto en codificación BIO.

## La Red

El primer intento de NER se puede realizar utilizando una red LSTM, como en nuestro ejemplo que viste durante la lección. Sin embargo, en tareas de PLN, la [arquitectura transformer](https://en.wikipedia.org/wiki/Transformer_(machine_learning_model)), y específicamente los [modelos de lenguaje BERT](https://en.wikipedia.org/wiki/BERT_(language_model)), muestran resultados mucho mejores. Los modelos BERT preentrenados comprenden la estructura general de un idioma y pueden ser ajustados para tareas específicas con conjuntos de datos relativamente pequeños y costos computacionales bajos.

Dado que planeamos aplicar NER a un escenario médico, tiene sentido usar un modelo BERT entrenado en textos médicos. Microsoft Research ha lanzado un modelo preentrenado llamado [PubMedBERT][PubMedBERT] ([publicación][PubMedBERT-Pub]), que fue ajustado utilizando textos del repositorio de [PubMed](https://pubmed.ncbi.nlm.nih.gov/).

El estándar *de facto* para entrenar modelos transformer es la biblioteca [Hugging Face Transformers](https://huggingface.co/). También contiene un repositorio de modelos preentrenados mantenidos por la comunidad, incluyendo PubMedBERT. Para cargar y usar este modelo, solo necesitamos un par de líneas de código:

```python
model_name = "microsoft/BiomedNLP-PubMedBERT-base-uncased-abstract"
classes = ... # number of classes: 2*entities+1
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = BertForTokenClassification.from_pretrained(model_name, classes)
```

Esto nos proporciona el objeto `model` itself, built for token classification task using `classes` number of classes, as well as `tokenizer` que puede dividir el texto de entrada en tokens. Necesitarás convertir el conjunto de datos al formato BIO, teniendo en cuenta la tokenización de PubMedBERT. Puedes usar [este fragmento de código en Python](https://gist.github.com/shwars/580b55684be3328eb39ecf01b9cbbd88) como inspiración.

## Conclusión

Esta tarea está muy cerca de la tarea real que probablemente tendrás si deseas obtener más información sobre grandes volúmenes de textos en lenguaje natural. En nuestro caso, podemos aplicar nuestro modelo entrenado al [conjunto de datos de artículos relacionados con COVID](https://www.kaggle.com/allen-institute-for-ai/CORD-19-research-challenge) y ver qué información podremos obtener. [Esta publicación en el blog](https://soshnikov.com/science/analyzing-medical-papers-with-azure-and-text-analytics-for-health/) y [este artículo](https://www.mdpi.com/2504-2289/6/1/4) describen la investigación que se puede realizar sobre este corpus de artículos utilizando NER.

**Disclaimer**: 
This document has been translated using machine-based AI translation services. While we strive for accuracy, please be aware that automated translations may contain errors or inaccuracies. The original document in its native language should be considered the authoritative source. For critical information, professional human translation is recommended. We are not liable for any misunderstandings or misinterpretations arising from the use of this translation.