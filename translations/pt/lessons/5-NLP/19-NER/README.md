# Reconhecimento de Entidades Nomeadas

Até agora, temos nos concentrado principalmente em uma tarefa de PLN - classificação. No entanto, também existem outras tarefas de PLN que podem ser realizadas com redes neurais. Uma dessas tarefas é o **[Reconhecimento de Entidades Nomeadas](https://wikipedia.org/wiki/Named-entity_recognition)** (NER), que lida com o reconhecimento de entidades específicas dentro do texto, como lugares, nomes de pessoas, intervalos de data-hora, fórmulas químicas e assim por diante.

## [Quiz pré-aula](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/119)

## Exemplo de Uso do NER

Suponha que você queira desenvolver um chatbot de linguagem natural, semelhante ao Amazon Alexa ou ao Google Assistant. A forma como os chatbots inteligentes funcionam é *entendendo* o que o usuário deseja, realizando a classificação de texto na frase de entrada. O resultado dessa classificação é chamado de **intenção**, que determina o que um chatbot deve fazer.

<img alt="Bot NER" src="images/bot-ner.png" width="50%"/>

> Imagem do autor

No entanto, um usuário pode fornecer alguns parâmetros como parte da frase. Por exemplo, ao perguntar sobre o clima, ela pode especificar uma localização ou data. Um bot deve ser capaz de entender essas entidades e preencher os espaços dos parâmetros de acordo antes de executar a ação. É exatamente aqui que o NER entra em cena.

> ✅ Outro exemplo seria [analisar artigos médicos científicos](https://soshnikov.com/science/analyzing-medical-papers-with-azure-and-text-analytics-for-health/). Uma das principais coisas que precisamos procurar são termos médicos específicos, como doenças e substâncias médicas. Embora um pequeno número de doenças possa ser extraído usando busca de substring, entidades mais complexas, como compostos químicos e nomes de medicamentos, necessitam de uma abordagem mais complexa.

## NER como Classificação de Tokens

Os modelos de NER são essencialmente **modelos de classificação de tokens**, porque para cada um dos tokens de entrada precisamos decidir se ele pertence a uma entidade ou não, e se sim - a qual classe de entidade.

Considere o seguinte título de artigo:

**Regurgitação da válvula tricúspide** e **toxicidade do carbonato de lítio** em um recém-nascido.

As entidades aqui são:

* Regurgitação da válvula tricúspide é uma doença (`DIS`)
* Carbonato de lítio é uma substância química (`CHEM`)
* Toxicidade também é uma doença (`DIS`)

Observe que uma entidade pode abranger vários tokens. E, como neste caso, precisamos distinguir entre duas entidades consecutivas. Assim, é comum usar duas classes para cada entidade - uma especificando o primeiro token da entidade (frequentemente o prefixo `B-` é usado, para **b**eginning), e outra - a continuação de uma entidade (`I-`, para **i**nner token). Também usamos `O` como uma classe para representar todos os **o**utros tokens. Essa marcação de tokens é chamada de [BIO tagging](https://en.wikipedia.org/wiki/Inside%E2%80%93outside%E2%80%93beginning_(tagging)) (ou IOB). Quando marcados, nosso título ficará assim:

Token | Tag
------|-----
Tricúspide | B-DIS
válvula | I-DIS
regurgitação | I-DIS
e | O
lítio | B-CHEM
carbonato | I-CHEM
toxicidade | B-DIS
em | O
um | O
recém-nascido | O
. | O

Como precisamos construir uma correspondência um a um entre tokens e classes, podemos treinar um modelo de rede neural **muitos-para-muitos** a partir desta imagem:

![Imagem mostrando padrões comuns de redes neurais recorrentes.](../../../../../translated_images/unreasonable-effectiveness-of-rnn.541ead816778f42dce6c42d8a56c184729aa2378d059b851be4ce12b993033df.pt.jpg)

> *Imagem de [este post no blog](http://karpathy.github.io/2015/05/21/rnn-effectiveness/) por [Andrej Karpathy](http://karpathy.github.io/). Os modelos de classificação de tokens NER correspondem à arquitetura de rede mais à direita nesta imagem.*

## Treinamento de Modelos NER

Como um modelo NER é essencialmente um modelo de classificação de tokens, podemos usar RNNs com os quais já estamos familiarizados para essa tarefa. Nesse caso, cada bloco da rede recorrente retornará o ID do token. O exemplo de notebook a seguir mostra como treinar LSTM para classificação de tokens.

## ✍️ Notebooks de Exemplo: NER

Continue seu aprendizado no seguinte notebook:

* [NER com TensorFlow](../../../../../lessons/5-NLP/19-NER/NER-TF.ipynb)

## Conclusão

Um modelo NER é um **modelo de classificação de tokens**, o que significa que pode ser usado para realizar classificação de tokens. Esta é uma tarefa muito comum em PLN, ajudando a reconhecer entidades específicas dentro do texto, incluindo lugares, nomes, datas e mais.

## 🚀 Desafio

Complete a tarefa vinculada abaixo para treinar um modelo de reconhecimento de entidades nomeadas para termos médicos e, em seguida, experimente em um conjunto de dados diferente.

## [Quiz pós-aula](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/219)

## Revisão e Autoestudo

Leia o blog [A Eficácia Irresistível das Redes Neurais Recorrentes](http://karpathy.github.io/2015/05/21/rnn-effectiveness/) e siga a seção de Leitura Adicional nesse artigo para aprofundar seu conhecimento.

## [Tarefa](lab/README.md)

Na tarefa para esta lição, você terá que treinar um modelo de reconhecimento de entidades médicas. Você pode começar treinando um modelo LSTM conforme descrito nesta lição e prosseguir com o uso do modelo de transformador BERT. Leia [as instruções](lab/README.md) para obter todos os detalhes.

**Isenção de responsabilidade**:  
Este documento foi traduzido utilizando serviços de tradução automática baseados em IA. Embora nos esforcemos pela precisão, esteja ciente de que traduções automatizadas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte autoritativa. Para informações críticas, recomenda-se a tradução profissional por um humano. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações errôneas decorrentes do uso desta tradução.