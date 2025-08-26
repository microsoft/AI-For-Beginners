<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "bd10f434e444bce61b7f97eeb1ff6a55",
  "translation_date": "2025-08-26T08:49:16+00:00",
  "source_file": "lessons/5-NLP/19-NER/README.md",
  "language_code": "br"
}
-->
# Reconhecimento de Entidades Nomeadas

Até agora, temos nos concentrado principalmente em uma tarefa de PLN - classificação. No entanto, existem outras tarefas de PLN que podem ser realizadas com redes neurais. Uma dessas tarefas é o **[Reconhecimento de Entidades Nomeadas](https://wikipedia.org/wiki/Named-entity_recognition)** (NER), que lida com o reconhecimento de entidades específicas dentro de um texto, como lugares, nomes de pessoas, intervalos de data e hora, fórmulas químicas, entre outros.

## [Questionário pré-aula](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/119)

## Exemplo de Uso do NER

Suponha que você queira desenvolver um chatbot de linguagem natural, semelhante ao Amazon Alexa ou Google Assistente. A forma como chatbots inteligentes funcionam é *entendendo* o que o usuário deseja, realizando a classificação de texto na frase de entrada. O resultado dessa classificação é o chamado **intento**, que determina o que o chatbot deve fazer.

<img alt="Bot NER" src="images/bot-ner.png" width="50%"/>

> Imagem do autor

No entanto, um usuário pode fornecer alguns parâmetros como parte da frase. Por exemplo, ao perguntar sobre o clima, ele pode especificar um local ou uma data. Um bot deve ser capaz de entender essas entidades e preencher os campos de parâmetros adequadamente antes de executar a ação. É exatamente aqui que o NER entra em cena.

> ✅ Outro exemplo seria [analisar artigos científicos médicos](https://soshnikov.com/science/analyzing-medical-papers-with-azure-and-text-analytics-for-health/). Um dos principais objetivos é identificar termos médicos específicos, como doenças e substâncias médicas. Enquanto um pequeno número de doenças pode ser extraído usando busca por substring, entidades mais complexas, como compostos químicos e nomes de medicamentos, exigem uma abordagem mais sofisticada.

## NER como Classificação de Tokens

Modelos de NER são essencialmente **modelos de classificação de tokens**, porque para cada um dos tokens de entrada precisamos decidir se ele pertence a uma entidade ou não, e, se pertence, a qual classe de entidade.

Considere o seguinte título de artigo:

**Regurgitação da válvula tricúspide** e **carbonato de lítio** **toxicidade** em um recém-nascido.

As entidades aqui são:

* Regurgitação da válvula tricúspide é uma doença (`DIS`)
* Carbonato de lítio é uma substância química (`CHEM`)
* Toxicidade também é uma doença (`DIS`)

Observe que uma entidade pode abranger vários tokens. E, como neste caso, precisamos distinguir entre duas entidades consecutivas. Assim, é comum usar duas classes para cada entidade - uma especificando o primeiro token da entidade (geralmente o prefixo `B-` é usado, para **b**eginning/início), e outra para a continuação de uma entidade (`I-`, para **i**nner token/token interno). Também usamos `O` como uma classe para representar todos os **o**utros tokens. Essa marcação de tokens é chamada de [marcação BIO](https://en.wikipedia.org/wiki/Inside%E2%80%93outside%E2%80%93beginning_(tagging)) (ou IOB). Quando marcada, nosso título ficará assim:

Token | Tag
------|-----
Regurgitação | B-DIS
da | I-DIS
válvula | I-DIS
tricúspide | I-DIS
e | O
carbonato | B-CHEM
de | I-CHEM
lítio | I-CHEM
toxicidade | B-DIS
em | O
um | O
recém-nascido | O
. | O

Como precisamos construir uma correspondência um-para-um entre tokens e classes, podemos treinar um modelo neural **muitos-para-muitos** da seguinte forma:

![Imagem mostrando padrões comuns de redes neurais recorrentes.](../../../../../translated_images/unreasonable-effectiveness-of-rnn.541ead816778f42dce6c42d8a56c184729aa2378d059b851be4ce12b993033df.br.jpg)

> *Imagem retirada [deste post no blog](http://karpathy.github.io/2015/05/21/rnn-effectiveness/) por [Andrej Karpathy](http://karpathy.github.io/). Modelos de classificação de tokens NER correspondem à arquitetura de rede mais à direita nesta imagem.*

## Treinando Modelos de NER

Como um modelo de NER é essencialmente um modelo de classificação de tokens, podemos usar RNNs, com as quais já estamos familiarizados, para essa tarefa. Nesse caso, cada bloco da rede recorrente retornará o ID do token. O notebook de exemplo a seguir mostra como treinar um LSTM para classificação de tokens.

## ✍️ Notebooks de Exemplo: NER

Continue seu aprendizado no seguinte notebook:

* [NER com TensorFlow](../../../../../lessons/5-NLP/19-NER/NER-TF.ipynb)

## Conclusão

Um modelo de NER é um **modelo de classificação de tokens**, o que significa que ele pode ser usado para realizar a classificação de tokens. Essa é uma tarefa muito comum em PLN, ajudando a reconhecer entidades específicas dentro de um texto, incluindo lugares, nomes, datas e mais.

## 🚀 Desafio

Complete a tarefa vinculada abaixo para treinar um modelo de reconhecimento de entidades nomeadas para termos médicos e, em seguida, experimente em um conjunto de dados diferente.

## [Questionário pós-aula](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/219)

## Revisão e Autoestudo

Leia o blog [The Unreasonable Effectiveness of Recurrent Neural Networks](http://karpathy.github.io/2015/05/21/rnn-effectiveness/) e siga a seção de Leituras Adicionais nesse artigo para aprofundar seu conhecimento.

## [Tarefa](lab/README.md)

Na tarefa desta lição, você terá que treinar um modelo de reconhecimento de entidades médicas. Você pode começar treinando um modelo LSTM, como descrito nesta lição, e depois avançar para usar o modelo transformer BERT. Leia [as instruções](lab/README.md) para obter todos os detalhes.

**Aviso Legal**:  
Este documento foi traduzido utilizando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos para garantir a precisão, esteja ciente de que traduções automatizadas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte autoritativa. Para informações críticas, recomenda-se a tradução profissional realizada por humanos. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações equivocadas decorrentes do uso desta tradução.