# NER

Trabalho prático do [Currículo de IA para Iniciantes](https://github.com/microsoft/ai-for-beginners).

## Tarefa

Neste laboratório, precisas de treinar um modelo de reconhecimento de entidades nomeadas (NER) para termos médicos.

## O Conjunto de Dados

Para treinar o modelo NER, precisamos de um conjunto de dados devidamente etiquetado com entidades médicas. O [conjunto de dados BC5CDR](https://biocreative.bioinformatics.udel.edu/tasks/biocreative-v/track-3-cdr/) contém entidades de doenças e químicos etiquetadas a partir de mais de 1500 artigos. Podes descarregar o conjunto de dados após te registares no site deles.

O conjunto de dados BC5CDR tem o seguinte aspeto:

```
6794356|t|Tricuspid valve regurgitation and lithium carbonate toxicity in a newborn infant.
6794356|a|A newborn with massive tricuspid regurgitation, atrial flutter, congestive heart failure, and a high serum lithium level is described. This is the first patient to initially manifest tricuspid regurgitation and atrial flutter, and the 11th described patient with cardiac disease among infants exposed to lithium compounds in the first trimester of pregnancy. Sixty-three percent of these infants had tricuspid valve involvement. Lithium carbonate may be a factor in the increasing incidence of congenital heart disease when taken during early pregnancy. It also causes neurologic depression, cyanosis, and cardiac arrhythmia when consumed prior to delivery.
6794356	0	29	Tricuspid valve regurgitation	Disease	D014262
6794356	34	51	lithium carbonate	Chemical	D016651
6794356	52	60	toxicity	Disease	D064420
...
```

Neste conjunto de dados, o título e o resumo do artigo estão nas duas primeiras linhas, seguidos pelas entidades individuais, com as posições de início e fim dentro do bloco título+resumo. Além do tipo de entidade, obténs o ID de ontologia dessa entidade dentro de uma ontologia médica.

Precisarás de escrever algum código em Python para converter isto para a codificação BIO.

## A Rede

A primeira tentativa de NER pode ser feita utilizando uma rede LSTM, como no exemplo que viste durante a aula. No entanto, em tarefas de PLN, a [arquitetura transformer](https://en.wikipedia.org/wiki/Transformer_(machine_learning_model)), e especificamente os [modelos de linguagem BERT](https://en.wikipedia.org/wiki/BERT_(language_model)), apresentam resultados muito melhores. Modelos BERT pré-treinados compreendem a estrutura geral de uma linguagem e podem ser ajustados para tarefas específicas com conjuntos de dados relativamente pequenos e custos computacionais reduzidos.

Como planeamos aplicar NER a um cenário médico, faz sentido usar um modelo BERT treinado em textos médicos. A Microsoft Research lançou um modelo pré-treinado chamado [PubMedBERT][PubMedBERT] ([publicação][PubMedBERT-Pub]), que foi ajustado utilizando textos do repositório [PubMed](https://pubmed.ncbi.nlm.nih.gov/).

O padrão *de facto* para treinar modelos transformer é a biblioteca [Hugging Face Transformers](https://huggingface.co/). Esta também contém um repositório de modelos pré-treinados mantidos pela comunidade, incluindo o PubMedBERT. Para carregar e usar este modelo, só precisas de algumas linhas de código:

```python
model_name = "microsoft/BiomedNLP-PubMedBERT-base-uncased-abstract"
classes = ... # number of classes: 2*entities+1
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = BertForTokenClassification.from_pretrained(model_name, classes)
```

Isto fornece-nos o `model` propriamente dito, construído para a tarefa de classificação de tokens usando `classes` número de classes, bem como o objeto `tokenizer` que pode dividir o texto de entrada em tokens. Precisarás de converter o conjunto de dados para o formato BIO, tendo em conta a tokenização do PubMedBERT. Podes usar [este trecho de código Python](https://gist.github.com/shwars/580b55684be3328eb39ecf01b9cbbd88) como inspiração.

## Conclusão

Esta tarefa é muito próxima da tarefa real que provavelmente terás se quiseres obter mais insights sobre grandes volumes de textos em linguagem natural. No nosso caso, podemos aplicar o nosso modelo treinado ao [conjunto de dados de artigos relacionados com a COVID](https://www.kaggle.com/allen-institute-for-ai/CORD-19-research-challenge) e ver que insights conseguimos obter. [Este artigo de blog](https://soshnikov.com/science/analyzing-medical-papers-with-azure-and-text-analytics-for-health/) e [este artigo científico](https://www.mdpi.com/2504-2289/6/1/4) descrevem a investigação que pode ser feita neste corpus de artigos utilizando NER.

**Aviso Legal**:  
Este documento foi traduzido utilizando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos pela precisão, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original na sua língua nativa deve ser considerado a fonte autoritária. Para informações críticas, recomenda-se a tradução profissional realizada por humanos. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes do uso desta tradução.