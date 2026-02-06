# Processamento de Linguagem Natural

![Resumo das tarefas de PLN em um desenho](../../../../translated_images/pt-BR/ai-nlp.b22dcb8ca4707cea.webp)

Nesta seção, vamos focar no uso de Redes Neurais para lidar com tarefas relacionadas ao **Processamento de Linguagem Natural (PLN)**. Existem muitos problemas de PLN que queremos que os computadores sejam capazes de resolver:

* **Classificação de texto** é um problema típico de classificação relacionado a sequências de texto. Exemplos incluem classificar mensagens de e-mail como spam ou não-spam, ou categorizar artigos como esportes, negócios, política, etc. Além disso, ao desenvolver chatbots, frequentemente precisamos entender o que o usuário quis dizer — nesse caso, estamos lidando com **classificação de intenção**. Muitas vezes, na classificação de intenção, precisamos lidar com muitas categorias.
* **Análise de sentimento** é um problema típico de regressão, onde precisamos atribuir um número (um sentimento) correspondente ao quão positivo/negativo é o significado de uma frase. Uma versão mais avançada da análise de sentimento é a **análise de sentimento baseada em aspectos** (ABSA), onde atribuímos o sentimento não à frase inteira, mas a diferentes partes dela (aspectos), por exemplo: *Neste restaurante, gostei da culinária, mas a atmosfera era horrível*.
* **Reconhecimento de Entidades Nomeadas** (NER) refere-se ao problema de extrair certas entidades de um texto. Por exemplo, podemos precisar entender que na frase *Preciso voar para Paris amanhã* a palavra *amanhã* refere-se a uma DATA, e *Paris* é um LOCAL.
* **Extração de palavras-chave** é semelhante ao NER, mas precisamos extrair palavras importantes para o significado da frase automaticamente, sem pré-treinamento para tipos específicos de entidades.
* **Agrupamento de texto** pode ser útil quando queremos agrupar frases semelhantes, por exemplo, solicitações similares em conversas de suporte técnico.
* **Resposta a perguntas** refere-se à capacidade de um modelo de responder a uma pergunta específica. O modelo recebe um trecho de texto e uma pergunta como entradas, e precisa fornecer um local no texto onde a resposta à pergunta está contida (ou, às vezes, gerar o texto da resposta).
* **Geração de texto** é a capacidade de um modelo de gerar novo texto. Pode ser considerado como uma tarefa de classificação que prevê a próxima letra/palavra com base em algum *texto inicial*. Modelos avançados de geração de texto, como o GPT-3, são capazes de resolver outras tarefas de PLN usando uma técnica chamada [programação de prompts](https://towardsdatascience.com/software-3-0-how-prompting-will-change-the-rules-of-the-game-a982fbfe1e0) ou [engenharia de prompts](https://medium.com/swlh/openai-gpt-3-and-prompt-engineering-dcdc2c5fcd29).
* **Resumo de texto** é uma técnica em que queremos que um computador "leia" um texto longo e o resuma em algumas frases.
* **Tradução automática** pode ser vista como uma combinação de compreensão de texto em um idioma e geração de texto em outro.

Inicialmente, a maioria das tarefas de PLN era resolvida usando métodos tradicionais, como gramáticas. Por exemplo, na tradução automática, analisadores eram usados para transformar a frase inicial em uma árvore sintática, depois estruturas semânticas de nível superior eram extraídas para representar o significado da frase, e com base nesse significado e na gramática do idioma de destino, o resultado era gerado. Hoje em dia, muitas tarefas de PLN são resolvidas de forma mais eficaz usando redes neurais.

> Muitos métodos clássicos de PLN estão implementados na biblioteca Python [Natural Language Processing Toolkit (NLTK)](https://www.nltk.org). Há um excelente [Livro do NLTK](https://www.nltk.org/book/) disponível online que cobre como diferentes tarefas de PLN podem ser resolvidas usando o NLTK.

Em nosso curso, vamos focar principalmente no uso de Redes Neurais para PLN, e usaremos o NLTK quando necessário.

Já aprendemos sobre o uso de redes neurais para lidar com dados tabulares e imagens. A principal diferença entre esses tipos de dados e texto é que o texto é uma sequência de comprimento variável, enquanto o tamanho da entrada no caso de imagens é conhecido antecipadamente. Embora redes convolucionais possam extrair padrões de dados de entrada, os padrões em texto são mais complexos. Por exemplo, podemos ter uma negação separada do sujeito por muitas palavras arbitrárias (ex.: *Eu não gosto de laranjas*, vs. *Eu não gosto dessas grandes laranjas coloridas e saborosas*), e isso ainda deve ser interpretado como um único padrão. Assim, para lidar com a linguagem, precisamos introduzir novos tipos de redes neurais, como *redes recorrentes* e *transformers*.

## Instalar Bibliotecas

Se você estiver usando uma instalação local do Python para executar este curso, pode ser necessário instalar todas as bibliotecas necessárias para PLN usando os seguintes comandos:

**Para PyTorch**
```bash
pip install -r requirements-torch.txt
```
**Para TensorFlow**
```bash
pip install -r requirements-tf.txt
```

> Você pode experimentar PLN com TensorFlow no [Microsoft Learn](https://docs.microsoft.com/learn/modules/intro-natural-language-processing-tensorflow/?WT.mc_id=academic-77998-cacaste)

## Aviso sobre GPU

Nesta seção, em alguns dos exemplos, treinaremos modelos bastante grandes.
* **Use um computador com GPU**: É recomendável executar seus notebooks em um computador com GPU para reduzir o tempo de espera ao trabalhar com modelos grandes.
* **Restrições de memória da GPU**: Executar em uma GPU pode levar a situações em que você fique sem memória da GPU, especialmente ao treinar modelos grandes.
* **Consumo de memória da GPU**: A quantidade de memória da GPU consumida durante o treinamento depende de vários fatores, incluindo o tamanho do minibatch.
* **Minimize o tamanho do minibatch**: Se você encontrar problemas de memória da GPU, considere reduzir o tamanho do minibatch em seu código como uma solução potencial.
* **Liberação de memória da GPU no TensorFlow**: Versões mais antigas do TensorFlow podem não liberar corretamente a memória da GPU ao treinar vários modelos dentro de um único kernel Python. Para gerenciar o uso de memória da GPU de forma eficaz, você pode configurar o TensorFlow para alocar memória da GPU apenas conforme necessário.
* **Inclusão de código**: Para configurar o TensorFlow para aumentar a alocação de memória da GPU apenas quando necessário, inclua o seguinte código em seus notebooks:

```python
physical_devices = tf.config.list_physical_devices('GPU') 
if len(physical_devices)>0:
    tf.config.experimental.set_memory_growth(physical_devices[0], True) 
```

Se você estiver interessado em aprender sobre PLN a partir de uma perspectiva de aprendizado de máquina clássico, visite [esta coleção de lições](https://github.com/microsoft/ML-For-Beginners/tree/main/6-NLP).

## Nesta Seção
Nesta seção, aprenderemos sobre:

* [Representação de texto como tensores](13-TextRep/README.md)
* [Embeddings de palavras](14-Emdeddings/README.md)
* [Modelagem de linguagem](15-LanguageModeling/README.md)
* [Redes Neurais Recorrentes](16-RNN/README.md)
* [Redes Generativas](17-GenerativeNetworks/README.md)
* [Transformers](18-Transformers/README.md)

**Aviso Legal**:  
Este documento foi traduzido utilizando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos para garantir a precisão, esteja ciente de que traduções automatizadas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte autoritativa. Para informações críticas, recomenda-se a tradução profissional realizada por humanos. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações equivocadas decorrentes do uso desta tradução.