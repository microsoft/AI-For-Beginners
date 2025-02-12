# Processamento de Linguagem Natural

![Resumo das tarefas de PLN em um doodle](../../../../translated_images/ai-nlp.b22dcb8ca4707ceaee8576db1c5f4089c8cac2f454e9e03ea554f07fda4556b8.pt.png)

Nesta seção, focaremos no uso de Redes Neurais para lidar com tarefas relacionadas ao **Processamento de Linguagem Natural (PLN)**. Existem muitos problemas de PLN que queremos que os computadores sejam capazes de resolver:

* **Classificação de texto** é um problema típico de classificação relacionado a sequências de texto. Exemplos incluem classificar mensagens de e-mail como spam ou não-spam, ou categorizar artigos como esportes, negócios, política, etc. Além disso, ao desenvolver chatbots, muitas vezes precisamos entender o que um usuário queria dizer -- nesse caso, estamos lidando com **classificação de intenção**. Frequentemente, na classificação de intenção, precisamos lidar com muitas categorias.
* **Análise de sentimento** é um problema típico de regressão, onde precisamos atribuir um número (um sentimento) correspondente a quão positiva ou negativa é a significação de uma frase. Uma versão mais avançada da análise de sentimento é a **análise de sentimento baseada em aspectos** (ABSA), onde atribuímos sentimento não à frase inteira, mas a diferentes partes dela (aspectos), por exemplo, *Neste restaurante, gostei da culinária, mas a atmosfera era horrível*.
* **Reconhecimento de Entidades Nomeadas** (NER) refere-se ao problema de extrair certas entidades do texto. Por exemplo, podemos precisar entender que na frase *Preciso voar para Paris amanhã* a palavra *amanhã* refere-se a DATA, e *Paris* é uma LOCALIZAÇÃO.  
* **Extração de palavras-chave** é semelhante ao NER, mas precisamos extrair palavras importantes para o significado da frase automaticamente, sem pré-treinamento para tipos específicos de entidades.
* **Agrupamento de texto** pode ser útil quando queremos agrupar sentenças semelhantes, por exemplo, solicitações semelhantes em conversas de suporte técnico.
* **Resposta a perguntas** refere-se à capacidade de um modelo de responder a uma pergunta específica. O modelo recebe uma passagem de texto e uma pergunta como entradas, e precisa fornecer um local no texto onde a resposta à pergunta está contida (ou, às vezes, gerar o texto da resposta).
* **Geração de texto** é a capacidade de um modelo de gerar novo texto. Pode ser considerada uma tarefa de classificação que prevê a próxima letra/palavra com base em um *texto de entrada*. Modelos avançados de geração de texto, como o GPT-3, são capazes de resolver outras tarefas de PLN, como classificação, usando uma técnica chamada [programação de prompts](https://towardsdatascience.com/software-3-0-how-prompting-will-change-the-rules-of-the-game-a982fbfe1e0) ou [engenharia de prompts](https://medium.com/swlh/openai-gpt-3-and-prompt-engineering-dcdc2c5fcd29).
* **Resumir texto** é uma técnica quando queremos que um computador "leia" um texto longo e o resuma em algumas frases.
* **Tradução automática** pode ser vista como uma combinação de compreensão de texto em uma língua e geração de texto em outra.

Inicialmente, a maioria das tarefas de PLN eram resolvidas usando métodos tradicionais, como gramáticas. Por exemplo, na tradução automática, eram usados analisadores para transformar a frase inicial em uma árvore sintática, depois estruturas semânticas de nível superior eram extraídas para representar o significado da frase, e com base nesse significado e na gramática da língua-alvo, o resultado era gerado. Hoje em dia, muitas tarefas de PLN são resolvidas de forma mais eficaz usando redes neurais.

> Muitos métodos clássicos de PLN estão implementados na biblioteca Python [Natural Language Processing Toolkit (NLTK)](https://www.nltk.org). Há um ótimo [Livro NLTK](https://www.nltk.org/book/) disponível online que cobre como diferentes tarefas de PLN podem ser resolvidas usando o NLTK.

Em nosso curso, vamos nos concentrar principalmente no uso de Redes Neurais para PLN, e utilizaremos o NLTK quando necessário.

Já aprendemos sobre o uso de redes neurais para lidar com dados tabulares e com imagens. A principal diferença entre esses tipos de dados e texto é que o texto é uma sequência de comprimento variável, enquanto o tamanho da entrada no caso de imagens é conhecido com antecedência. Enquanto redes convolucionais podem extrair padrões dos dados de entrada, os padrões no texto são mais complexos. Por exemplo, a negação pode ser separada do sujeito para muitas palavras (por exemplo, *Eu não gosto de laranjas*, vs. *Eu não gosto dessas grandes laranjas coloridas e saborosas*), e isso ainda deve ser interpretado como um padrão. Assim, para lidar com a linguagem, precisamos introduzir novos tipos de redes neurais, como *redes recorrentes* e *transformadores*.

## Instalar Bibliotecas

Se você estiver usando uma instalação local do Python para executar este curso, pode precisar instalar todas as bibliotecas necessárias para PLN usando os seguintes comandos:

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

Nesta seção, em alguns dos exemplos, estaremos treinando modelos bastante grandes.
* **Use um Computador com GPU**: É aconselhável executar seus notebooks em um computador habilitado para GPU para reduzir os tempos de espera ao trabalhar com modelos grandes.
* **Restrições de Memória da GPU**: Executar em uma GPU pode levar a situações em que você fica sem memória da GPU, especialmente ao treinar modelos grandes.
* **Consumo de Memória da GPU**: A quantidade de memória da GPU consumida durante o treinamento depende de vários fatores, incluindo o tamanho do minibatch.
* **Minimizar o Tamanho do Minibatch**: Se você encontrar problemas de memória da GPU, considere reduzir o tamanho do minibatch em seu código como uma solução potencial.
* **Liberação de Memória da GPU no TensorFlow**: Versões mais antigas do TensorFlow podem não liberar a memória da GPU corretamente ao treinar vários modelos dentro de um kernel Python. Para gerenciar o uso da memória da GPU de forma eficaz, você pode configurar o TensorFlow para alocar memória da GPU apenas conforme necessário.
* **Inclusão de Código**: Para configurar o TensorFlow para aumentar a alocação de memória da GPU apenas quando necessário, inclua o seguinte código em seus notebooks:

```python
physical_devices = tf.config.list_physical_devices('GPU') 
if len(physical_devices)>0:
    tf.config.experimental.set_memory_growth(physical_devices[0], True) 
```

Se você estiver interessado em aprender sobre PLN a partir de uma perspectiva clássica de ML, visite [este conjunto de lições](https://github.com/microsoft/ML-For-Beginners/tree/main/6-NLP)

## Nesta Seção
Nesta seção, aprenderemos sobre:

* [Representando texto como tensores](13-TextRep/README.md)
* [Word Embeddings](14-Emdeddings/README.md)
* [Modelagem de Linguagem](15-LanguageModeling/README.md)
* [Redes Neurais Recorrentes](16-RNN/README.md)
* [Redes Generativas](17-GenerativeNetworks/README.md)
* [Transformadores](18-Transformers/README.md)

**Isenção de responsabilidade**:  
Este documento foi traduzido usando serviços de tradução automática baseados em IA. Embora nos esforcemos pela precisão, esteja ciente de que traduções automatizadas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte autoritativa. Para informações críticas, recomenda-se a tradução profissional feita por humanos. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações errôneas decorrentes do uso desta tradução.