<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "bd10f434e444bce61b7f97eeb1ff6a55",
  "translation_date": "2025-08-24T08:55:35+00:00",
  "source_file": "lessons/5-NLP/19-NER/README.md",
  "language_code": "pt"
}
-->
# Reconhecimento de Entidades Nomeadas

Até agora, temos nos concentrado principalmente em uma tarefa de PLN - classificação. No entanto, existem outras tarefas de PLN que podem ser realizadas com redes neurais. Uma dessas tarefas é o **[Reconhecimento de Entidades Nomeadas](https://wikipedia.org/wiki/Reconhecimento_de_entidades_nomeadas)** (NER), que lida com o reconhecimento de entidades específicas em um texto, como locais, nomes de pessoas, intervalos de data e hora, fórmulas químicas, entre outros.

## [Questionário pré-aula](https://ff-quizzes.netlify.app/en/ai/quiz/37)

## Exemplo de Uso do NER

Suponha que queira desenvolver um chatbot de linguagem natural, semelhante à Amazon Alexa ou ao Google Assistant. A forma como chatbots inteligentes funcionam é *entendendo* o que o utilizador deseja, realizando a classificação de texto na frase de entrada. O resultado dessa classificação é o chamado **intento**, que determina o que o chatbot deve fazer.

<img alt="Bot NER" src="images/bot-ner.png" width="50%"/>

> Imagem do autor

No entanto, um utilizador pode fornecer alguns parâmetros como parte da frase. Por exemplo, ao perguntar sobre o tempo, ele pode especificar uma localização ou uma data. Um bot deve ser capaz de compreender essas entidades e preencher os campos de parâmetros adequadamente antes de executar a ação. É exatamente aqui que o NER entra em cena.

> ✅ Outro exemplo seria [analisar artigos científicos na área médica](https://soshnikov.com/science/analyzing-medical-papers-with-azure-and-text-analytics-for-health/). Um dos principais objetivos é identificar termos médicos específicos, como doenças e substâncias médicas. Enquanto um pequeno número de doenças pode ser extraído usando busca por subcadeias, entidades mais complexas, como compostos químicos e nomes de medicamentos, exigem uma abordagem mais sofisticada.

## NER como Classificação de Tokens

Os modelos de NER são essencialmente **modelos de classificação de tokens**, porque para cada token de entrada precisamos decidir se ele pertence a uma entidade ou não, e, se pertence, a qual classe de entidade.

Considere o seguinte título de artigo:

**Regurgitação da válvula tricúspide** e **carbonato de lítio** **toxicidade** em um recém-nascido.

As entidades aqui são:

* Regurgitação da válvula tricúspide é uma doença (`DIS`)
* Carbonato de lítio é uma substância química (`CHEM`)
* Toxicidade também é uma doença (`DIS`)

Note que uma entidade pode abranger vários tokens. E, como neste caso, precisamos distinguir entre duas entidades consecutivas. Assim, é comum usar duas classes para cada entidade - uma especificando o primeiro token da entidade (geralmente o prefixo `B-` é usado, para **b**eginning/início), e outra para a continuação da entidade (`I-`, para **i**nner token/token interno). Também usamos `O` como uma classe para representar todos os **o**utros tokens. Essa marcação de tokens é chamada de [marcação BIO](https://en.wikipedia.org/wiki/Inside%E2%80%93outside%E2%80%93beginning_(tagging)) (ou IOB). Quando marcado, nosso título ficará assim:

Token | Tag
------|-----
Tricúspide | B-DIS
válvula | I-DIS
regurgitação | I-DIS
e | O
carbonato | B-CHEM
de | I-CHEM
lítio | I-CHEM
toxicidade | B-DIS
em | O
um | O
recém-nascido | O
. | O

Como precisamos construir uma correspondência um-para-um entre tokens e classes, podemos treinar um modelo de rede neural **muitos-para-muitos** da seguinte forma:

![Imagem mostrando padrões comuns de redes neurais recorrentes.](../../../../../lessons/5-NLP/17-GenerativeNetworks/images/unreasonable-effectiveness-of-rnn.jpg)

> *Imagem retirada [deste artigo](http://karpathy.github.io/2015/05/21/rnn-effectiveness/) de [Andrej Karpathy](http://karpathy.github.io/). Os modelos de classificação de tokens NER correspondem à arquitetura de rede mais à direita nesta imagem.*

## Treinamento de Modelos NER

Como um modelo NER é essencialmente um modelo de classificação de tokens, podemos usar RNNs, com as quais já estamos familiarizados, para essa tarefa. Nesse caso, cada bloco da rede recorrente retornará o ID do token. O seguinte notebook de exemplo mostra como treinar um LSTM para classificação de tokens.

## ✍️ Notebooks de Exemplo: NER

Continue o seu aprendizado no seguinte notebook:

* [NER com TensorFlow](../../../../../lessons/5-NLP/19-NER/NER-TF.ipynb)

## Conclusão

Um modelo NER é um **modelo de classificação de tokens**, o que significa que ele pode ser usado para realizar a classificação de tokens. Esta é uma tarefa muito comum em PLN, ajudando a reconhecer entidades específicas em textos, incluindo locais, nomes, datas e muito mais.

## 🚀 Desafio

Complete o exercício abaixo para treinar um modelo de reconhecimento de entidades nomeadas para termos médicos e, em seguida, experimente-o em um conjunto de dados diferente.

## [Questionário pós-aula](https://ff-quizzes.netlify.app/en/ai/quiz/38)

## Revisão e Autoestudo

Leia o artigo [The Unreasonable Effectiveness of Recurrent Neural Networks](http://karpathy.github.io/2015/05/21/rnn-effectiveness/) e explore a seção de Leituras Adicionais para aprofundar o seu conhecimento.

## [Exercício](lab/README.md)

No exercício desta lição, terá de treinar um modelo de reconhecimento de entidades médicas. Pode começar treinando um modelo LSTM, como descrito nesta lição, e depois avançar para o uso do modelo transformer BERT. Leia [as instruções](lab/README.md) para obter todos os detalhes.

**Aviso Legal**:  
Este documento foi traduzido utilizando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos pela precisão, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original na sua língua nativa deve ser considerado a fonte autoritária. Para informações críticas, recomenda-se a tradução profissional realizada por humanos. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes do uso desta tradução.