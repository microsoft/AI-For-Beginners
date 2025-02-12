# NER

Trabalho de laboratório do [Currículo de IA para Iniciantes](https://github.com/microsoft/ai-for-beginners).

## Tarefa

Neste laboratório, você precisa treinar um modelo de reconhecimento de entidades nomeadas para termos médicos.

## O Conjunto de Dados

Para treinar o modelo NER, precisamos de um conjunto de dados devidamente rotulado com entidades médicas. O [conjunto de dados BC5CDR](https://biocreative.bioinformatics.udel.edu/tasks/biocreative-v/track-3-cdr/) contém doenças e entidades químicas rotuladas de mais de 1500 artigos. Você pode baixar o conjunto de dados após se registrar no site deles.

O conjunto de dados BC5CDR se parece com isto:

```
6794356|t|Tricuspid valve regurgitation and lithium carbonate toxicity in a newborn infant.
6794356|a|A newborn with massive tricuspid regurgitation, atrial flutter, congestive heart failure, and a high serum lithium level is described. This is the first patient to initially manifest tricuspid regurgitation and atrial flutter, and the 11th described patient with cardiac disease among infants exposed to lithium compounds in the first trimester of pregnancy. Sixty-three percent of these infants had tricuspid valve involvement. Lithium carbonate may be a factor in the increasing incidence of congenital heart disease when taken during early pregnancy. It also causes neurologic depression, cyanosis, and cardiac arrhythmia when consumed prior to delivery.
6794356	0	29	Tricuspid valve regurgitation	Disease	D014262
6794356	34	51	lithium carbonate	Chemical	D016651
6794356	52	60	toxicity	Disease	D064420
...
```

Neste conjunto de dados, há o título e o resumo do artigo nas duas primeiras linhas, seguidos pelas entidades individuais, com as posições inicial e final dentro do bloco título+resumo. Além do tipo de entidade, você obtém o ID da ontologia dessa entidade dentro de alguma ontologia médica.

Você precisará escrever algum código em Python para converter isso em codificação BIO.

## A Rede

A primeira tentativa de NER pode ser feita usando uma rede LSTM, como no nosso exemplo que você viu durante a aula. No entanto, em tarefas de NLP, a [arquitetura transformer](https://en.wikipedia.org/wiki/Transformer_(machine_learning_model)), e especificamente os [modelos de linguagem BERT](https://en.wikipedia.org/wiki/BERT_(language_model)), mostram resultados muito melhores. Os modelos BERT pré-treinados entendem a estrutura geral de uma língua e podem ser ajustados para tarefas específicas com conjuntos de dados relativamente pequenos e custos computacionais baixos.

Como estamos planejando aplicar NER a um cenário médico, faz sentido usar um modelo BERT treinado em textos médicos. A Microsoft Research lançou um modelo pré-treinado chamado [PubMedBERT][PubMedBERT] ([publicação][PubMedBERT-Pub]), que foi ajustado usando textos do repositório [PubMed](https://pubmed.ncbi.nlm.nih.gov/).

O padrão *de fato* para treinar modelos transformer é a biblioteca [Hugging Face Transformers](https://huggingface.co/). Ela também contém um repositório de modelos pré-treinados mantidos pela comunidade, incluindo o PubMedBERT. Para carregar e usar este modelo, precisamos apenas de algumas linhas de código:

```python
model_name = "microsoft/BiomedNLP-PubMedBERT-base-uncased-abstract"
classes = ... # number of classes: 2*entities+1
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = BertForTokenClassification.from_pretrained(model_name, classes)
```

Isso nos dá o objeto `model` itself, built for token classification task using `classes` number of classes, as well as `tokenizer` que pode dividir o texto de entrada em tokens. Você precisará converter o conjunto de dados para o formato BIO, levando em conta a tokenização do PubMedBERT. Você pode usar [este trecho de código Python](https://gist.github.com/shwars/580b55684be3328eb39ecf01b9cbbd88) como inspiração.

## Conclusão

Essa tarefa é muito próxima da tarefa real que você provavelmente terá se quiser obter mais insights sobre grandes volumes de textos em linguagem natural. No nosso caso, podemos aplicar nosso modelo treinado ao [conjunto de dados de artigos relacionados ao COVID](https://www.kaggle.com/allen-institute-for-ai/CORD-19-research-challenge) e ver quais insights conseguiremos obter. [Este post de blog](https://soshnikov.com/science/analyzing-medical-papers-with-azure-and-text-analytics-for-health/) e [este artigo](https://www.mdpi.com/2504-2289/6/1/4) descrevem a pesquisa que pode ser realizada sobre este corpus de artigos usando NER.

**Isenção de responsabilidade**:  
Este documento foi traduzido utilizando serviços de tradução automática baseados em IA. Embora nos esforcemos pela precisão, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original em sua língua nativa deve ser considerado a fonte autoritativa. Para informações críticas, recomenda-se a tradução profissional por um humano. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações errôneas resultantes do uso desta tradução.