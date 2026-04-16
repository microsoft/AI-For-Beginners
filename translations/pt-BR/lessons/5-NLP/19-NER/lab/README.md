# NER

Trabalho prático do [Currículo de IA para Iniciantes](https://github.com/microsoft/ai-for-beginners).

## Tarefa

Neste laboratório, você precisa treinar um modelo de reconhecimento de entidades nomeadas (NER) para termos médicos.

## O Conjunto de Dados

Para treinar o modelo de NER, precisamos de um conjunto de dados devidamente rotulado com entidades médicas. O [conjunto de dados BC5CDR](https://biocreative.bioinformatics.udel.edu/tasks/biocreative-v/track-3-cdr/) contém entidades rotuladas de doenças e produtos químicos extraídas de mais de 1500 artigos. Você pode baixar o conjunto de dados após se registrar no site deles.

O conjunto de dados BC5CDR tem o seguinte formato:

```
6794356|t|Tricuspid valve regurgitation and lithium carbonate toxicity in a newborn infant.
6794356|a|A newborn with massive tricuspid regurgitation, atrial flutter, congestive heart failure, and a high serum lithium level is described. This is the first patient to initially manifest tricuspid regurgitation and atrial flutter, and the 11th described patient with cardiac disease among infants exposed to lithium compounds in the first trimester of pregnancy. Sixty-three percent of these infants had tricuspid valve involvement. Lithium carbonate may be a factor in the increasing incidence of congenital heart disease when taken during early pregnancy. It also causes neurologic depression, cyanosis, and cardiac arrhythmia when consumed prior to delivery.
6794356	0	29	Tricuspid valve regurgitation	Disease	D014262
6794356	34	51	lithium carbonate	Chemical	D016651
6794356	52	60	toxicity	Disease	D064420
...
```

Neste conjunto de dados, há o título e o resumo do artigo nas duas primeiras linhas, e depois há entidades individuais, com posições de início e fim dentro do bloco título+resumo. Além do tipo de entidade, você obtém o ID de ontologia dessa entidade dentro de alguma ontologia médica.

Você precisará escrever algum código em Python para converter isso em codificação BIO.

## A Rede

A primeira tentativa de NER pode ser feita usando uma rede LSTM, como no exemplo que você viu durante a aula. No entanto, em tarefas de PLN, a [arquitetura transformer](https://en.wikipedia.org/wiki/Transformer_(machine_learning_model)), e especificamente os [modelos de linguagem BERT](https://en.wikipedia.org/wiki/BERT_(language_model)), apresentam resultados muito melhores. Modelos BERT pré-treinados entendem a estrutura geral de uma linguagem e podem ser ajustados para tarefas específicas com conjuntos de dados relativamente pequenos e custos computacionais reduzidos.

Como planejamos aplicar NER a um cenário médico, faz sentido usar um modelo BERT treinado em textos médicos. A Microsoft Research lançou um modelo pré-treinado chamado [PubMedBERT][PubMedBERT] ([publicação][PubMedBERT-Pub]), que foi ajustado usando textos do repositório [PubMed](https://pubmed.ncbi.nlm.nih.gov/).

O padrão *de facto* para treinar modelos transformer é a biblioteca [Hugging Face Transformers](https://huggingface.co/). Ela também contém um repositório de modelos pré-treinados mantidos pela comunidade, incluindo o PubMedBERT. Para carregar e usar este modelo, precisamos apenas de algumas linhas de código:

```python
model_name = "microsoft/BiomedNLP-PubMedBERT-base-uncased-abstract"
classes = ... # number of classes: 2*entities+1
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = BertForTokenClassification.from_pretrained(model_name, classes)
```

Isso nos fornece o próprio `model`, construído para a tarefa de classificação de tokens usando o número de `classes`, bem como o objeto `tokenizer`, que pode dividir o texto de entrada em tokens. Você precisará converter o conjunto de dados para o formato BIO, levando em conta a tokenização do PubMedBERT. Você pode usar [este trecho de código Python](https://gist.github.com/shwars/580b55684be3328eb39ecf01b9cbbd88) como inspiração.

## Conclusão

Esta tarefa é muito próxima da tarefa real que você provavelmente terá se quiser obter mais insights sobre grandes volumes de textos em linguagem natural. No nosso caso, podemos aplicar o modelo treinado ao [conjunto de dados de artigos relacionados à COVID](https://www.kaggle.com/allen-institute-for-ai/CORD-19-research-challenge) e ver quais insights podemos obter. [Este post no blog](https://soshnikov.com/science/analyzing-medical-papers-with-azure-and-text-analytics-for-health/) e [este artigo](https://www.mdpi.com/2504-2289/6/1/4) descrevem as pesquisas que podem ser realizadas nesse corpus de artigos usando NER.

**Aviso Legal**:  
Este documento foi traduzido utilizando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos para garantir a precisão, esteja ciente de que traduções automatizadas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte autoritativa. Para informações críticas, recomenda-se a tradução profissional realizada por humanos. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações equivocadas decorrentes do uso desta tradução.