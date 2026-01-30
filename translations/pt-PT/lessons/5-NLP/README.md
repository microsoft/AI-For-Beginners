# Processamento de Linguagem Natural

![Resumo das tarefas de PLN em um desenho](../../../../lessons/sketchnotes/ai-nlp.png)

Nesta secção, vamos focar no uso de Redes Neuronais para lidar com tarefas relacionadas ao **Processamento de Linguagem Natural (PLN)**. Existem muitos problemas de PLN que queremos que os computadores sejam capazes de resolver:

* **Classificação de texto** é um problema típico de classificação relacionado a sequências de texto. Exemplos incluem classificar mensagens de e-mail como spam ou não-spam, ou categorizar artigos como desporto, negócios, política, etc. Além disso, ao desenvolver chatbots, muitas vezes precisamos entender o que o utilizador quis dizer — neste caso, estamos a lidar com **classificação de intenções**. Frequentemente, na classificação de intenções, precisamos lidar com muitas categorias.
* **Análise de sentimento** é um problema típico de regressão, onde precisamos atribuir um número (um sentimento) que corresponda ao quão positiva/negativa é a mensagem de uma frase. Uma versão mais avançada da análise de sentimento é a **análise de sentimento baseada em aspetos** (ABSA), onde atribuímos o sentimento não à frase inteira, mas a diferentes partes dela (aspeto), por exemplo: *Neste restaurante, gostei da cozinha, mas a atmosfera era horrível*.
* **Reconhecimento de Entidades Nomeadas** (NER) refere-se ao problema de extrair certas entidades de um texto. Por exemplo, podemos precisar entender que na frase *Preciso de voar para Paris amanhã*, a palavra *amanhã* refere-se a uma DATA, e *Paris* é uma LOCALIZAÇÃO.  
* **Extração de palavras-chave** é semelhante ao NER, mas precisamos extrair automaticamente palavras importantes para o significado da frase, sem pré-treino para tipos específicos de entidades.
* **Agrupamento de texto** pode ser útil quando queremos agrupar frases semelhantes, por exemplo, pedidos semelhantes em conversas de suporte técnico.
* **Resposta a perguntas** refere-se à capacidade de um modelo responder a uma pergunta específica. O modelo recebe um trecho de texto e uma pergunta como entradas, e precisa fornecer um local no texto onde a resposta à pergunta está contida (ou, por vezes, gerar o texto da resposta).
* **Geração de texto** é a capacidade de um modelo gerar novo texto. Pode ser considerado como uma tarefa de classificação que prevê a próxima letra/palavra com base num *texto inicial*. Modelos avançados de geração de texto, como o GPT-3, conseguem resolver outras tarefas de PLN, como classificação, usando uma técnica chamada [programação por prompts](https://towardsdatascience.com/software-3-0-how-prompting-will-change-the-rules-of-the-game-a982fbfe1e0) ou [engenharia de prompts](https://medium.com/swlh/openai-gpt-3-and-prompt-engineering-dcdc2c5fcd29).
* **Sumarização de texto** é uma técnica em que queremos que um computador "leia" um texto longo e o resuma em algumas frases.
* **Tradução automática** pode ser vista como uma combinação de compreensão de texto numa língua e geração de texto noutra.

Inicialmente, a maioria das tarefas de PLN era resolvida usando métodos tradicionais, como gramáticas. Por exemplo, na tradução automática, analisadores sintáticos eram usados para transformar a frase inicial numa árvore sintática, depois estruturas semânticas de nível superior eram extraídas para representar o significado da frase, e com base nesse significado e na gramática da língua de destino, o resultado era gerado. Atualmente, muitas tarefas de PLN são resolvidas de forma mais eficaz usando redes neuronais.

> Muitos métodos clássicos de PLN estão implementados na biblioteca Python [Natural Language Processing Toolkit (NLTK)](https://www.nltk.org). Existe um excelente [Livro NLTK](https://www.nltk.org/book/) disponível online que cobre como diferentes tarefas de PLN podem ser resolvidas usando o NLTK.

No nosso curso, vamos focar-nos principalmente no uso de Redes Neuronais para PLN, e usaremos o NLTK quando necessário.

Já aprendemos a usar redes neuronais para lidar com dados tabulares e com imagens. A principal diferença entre esses tipos de dados e texto é que o texto é uma sequência de comprimento variável, enquanto o tamanho da entrada no caso de imagens é conhecido antecipadamente. Embora redes convolucionais possam extrair padrões de dados de entrada, os padrões no texto são mais complexos. Por exemplo, podemos ter uma negação separada do sujeito por muitas palavras (ex.: *Eu não gosto de laranjas* vs. *Eu não gosto daquelas laranjas grandes, coloridas e saborosas*), e isso ainda deve ser interpretado como um único padrão. Assim, para lidar com a linguagem, precisamos introduzir novos tipos de redes neuronais, como *redes recorrentes* e *transformers*.

## Instalar Bibliotecas

Se estiver a usar uma instalação local de Python para executar este curso, pode ser necessário instalar todas as bibliotecas necessárias para PLN usando os seguintes comandos:

**Para PyTorch**  
```bash
pip install -r requirements-torch.txt
```  
**Para TensorFlow**  
```bash
pip install -r requirements-tf.txt
```  

> Pode experimentar PLN com TensorFlow no [Microsoft Learn](https://docs.microsoft.com/learn/modules/intro-natural-language-processing-tensorflow/?WT.mc_id=academic-77998-cacaste)

## Aviso sobre GPU

Nesta secção, em alguns dos exemplos, treinaremos modelos bastante grandes.  
* **Use um Computador com GPU**: É recomendável executar os seus notebooks num computador com GPU para reduzir os tempos de espera ao trabalhar com modelos grandes.  
* **Limitações de Memória da GPU**: Executar numa GPU pode levar a situações em que a memória da GPU se esgote, especialmente ao treinar modelos grandes.  
* **Consumo de Memória da GPU**: A quantidade de memória da GPU consumida durante o treino depende de vários fatores, incluindo o tamanho do minibatch.  
* **Minimize o Tamanho do Minibatch**: Se encontrar problemas de memória na GPU, considere reduzir o tamanho do minibatch no seu código como uma solução potencial.  
* **Libertação de Memória da GPU no TensorFlow**: Versões mais antigas do TensorFlow podem não libertar corretamente a memória da GPU ao treinar vários modelos num único kernel Python. Para gerir o uso da memória da GPU de forma eficaz, pode configurar o TensorFlow para alocar memória da GPU apenas conforme necessário.  
* **Inclusão de Código**: Para configurar o TensorFlow para aumentar a alocação de memória da GPU apenas quando necessário, inclua o seguinte código nos seus notebooks:  

```python
physical_devices = tf.config.list_physical_devices('GPU') 
if len(physical_devices)>0:
    tf.config.experimental.set_memory_growth(physical_devices[0], True) 
```  

Se estiver interessado em aprender sobre PLN numa perspetiva de ML clássico, visite [esta coleção de lições](https://github.com/microsoft/ML-For-Beginners/tree/main/6-NLP)

## Nesta Secção
Nesta secção, vamos aprender sobre:

* [Representar texto como tensores](13-TextRep/README.md)  
* [Embeddings de palavras](14-Emdeddings/README.md)  
* [Modelagem de linguagem](15-LanguageModeling/README.md)  
* [Redes Neuronais Recorrentes](16-RNN/README.md)  
* [Redes Generativas](17-GenerativeNetworks/README.md)  
* [Transformers](18-Transformers/README.md)  

**Aviso Legal**:  
Este documento foi traduzido utilizando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos para garantir a precisão, é importante notar que traduções automáticas podem conter erros ou imprecisões. O documento original na sua língua nativa deve ser considerado a fonte autoritária. Para informações críticas, recomenda-se a tradução profissional realizada por humanos. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes do uso desta tradução.