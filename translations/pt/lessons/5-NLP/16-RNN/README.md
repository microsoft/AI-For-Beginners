# Redes Neurais Recorrentes

## [Quiz pré-aula](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/116)

Nas seções anteriores, temos utilizado representações semânticas ricas de texto e um classificador linear simples em cima das embeddings. O que essa arquitetura faz é capturar o significado agregado das palavras em uma frase, mas não leva em consideração a **ordem** das palavras, porque a operação de agregação em cima das embeddings removeu essa informação do texto original. Como esses modelos não conseguem modelar a ordem das palavras, eles não conseguem resolver tarefas mais complexas ou ambíguas, como geração de texto ou resposta a perguntas.

Para capturar o significado de uma sequência de texto, precisamos usar outra arquitetura de rede neural, chamada de **rede neural recorrente**, ou RNN. Na RNN, passamos nossa frase pela rede um símbolo de cada vez, e a rede produz um **estado**, que então passamos para a rede novamente com o próximo símbolo.

![RNN](../../../../../translated_images/rnn.27f5c29c53d727b546ad3961637a267f0fe9ec5ab01f2a26a853c92fcefbb574.pt.png)

> Imagem do autor

Dada a sequência de tokens de entrada X<sub>0</sub>,...,X<sub>n</sub>, a RNN cria uma sequência de blocos de rede neural e treina essa sequência de ponta a ponta usando retropropagação. Cada bloco da rede recebe um par (X<sub>i</sub>,S<sub>i</sub>) como entrada e produz S<sub>i+1</sub> como resultado. O estado final S<sub>n</sub> ou (saída Y<sub>n</sub>) vai para um classificador linear para produzir o resultado. Todos os blocos da rede compartilham os mesmos pesos e são treinados de ponta a ponta usando uma passagem de retropropagação.

Como os vetores de estado S<sub>0</sub>,...,S<sub>n</sub> são passados pela rede, ela é capaz de aprender as dependências sequenciais entre as palavras. Por exemplo, quando a palavra *not* aparece em algum lugar na sequência, ela pode aprender a negar certos elementos dentro do vetor de estado, resultando em negação.

> ✅ Como os pesos de todos os blocos RNN na imagem acima são compartilhados, a mesma imagem pode ser representada como um bloco (à direita) com um loop de feedback recorrente, que passa o estado de saída da rede de volta para a entrada.

## Anatomia de uma Célula RNN

Vamos ver como uma célula RNN simples é organizada. Ela aceita o estado anterior S<sub>i-1</sub> e o símbolo atual X<sub>i</sub> como entradas, e deve produzir o estado de saída S<sub>i</sub> (e, às vezes, também estamos interessados em alguma outra saída Y<sub>i</sub>, como no caso de redes generativas).

Uma célula RNN simples tem duas matrizes de pesos internas: uma transforma um símbolo de entrada (vamos chamá-la de W), e a outra transforma um estado de entrada (H). Neste caso, a saída da rede é calculada como σ(W×X<sub>i</sub>+H×S<sub>i-1</sub>+b), onde σ é a função de ativação e b é um viés adicional.

<img alt="Anatomia da Célula RNN" src="images/rnn-anatomy.png" width="50%"/>

> Imagem do autor

Em muitos casos, os tokens de entrada são passados pela camada de embedding antes de entrar na RNN para reduzir a dimensionalidade. Nesse caso, se a dimensão dos vetores de entrada é *emb_size*, e o vetor de estado é *hid_size* - o tamanho de W é *emb_size*×*hid_size*, e o tamanho de H é *hid_size*×*hid_size*.

## Memória de Longo e Curto Prazo (LSTM)

Um dos principais problemas das RNNs clássicas é o chamado problema dos **gradientes que desaparecem**. Como as RNNs são treinadas de ponta a ponta em uma única passagem de retropropagação, elas têm dificuldade em propagar o erro para as primeiras camadas da rede e, assim, a rede não consegue aprender relações entre tokens distantes. Uma das maneiras de evitar esse problema é introduzir **gerenciamento de estado explícito** usando os chamados **portões**. Existem duas arquiteturas bem conhecidas desse tipo: **Memória de Longo e Curto Prazo** (LSTM) e **Unidade de Relé com Portão** (GRU).

![Imagem mostrando um exemplo de célula de memória de longo e curto prazo](../../../../../lessons/5-NLP/16-RNN/images/long-short-term-memory-cell.svg)

> Fonte da imagem TBD

A Rede LSTM é organizada de maneira semelhante à RNN, mas existem dois estados que são passados de camada para camada: o estado real C e o vetor oculto H. Em cada unidade, o vetor oculto H<sub>i</sub> é concatenado com a entrada X<sub>i</sub>, e eles controlam o que acontece com o estado C por meio de **portões**. Cada portão é uma rede neural com ativação sigmoide (saída na faixa [0,1]), que pode ser pensada como uma máscara bit a bit quando multiplicada pelo vetor de estado. Existem os seguintes portões (da esquerda para a direita na imagem acima):

* O **portão de esquecimento** pega um vetor oculto e determina quais componentes do vetor C precisamos esquecer e quais passar adiante.
* O **portão de entrada** pega algumas informações dos vetores de entrada e ocultos e as insere no estado.
* O **portão de saída** transforma o estado por meio de uma camada linear com ativação *tanh*, e então seleciona alguns de seus componentes usando um vetor oculto H<sub>i</sub> para produzir um novo estado C<sub>i+1</sub>.

Os componentes do estado C podem ser pensados como alguns indicadores que podem ser ativados ou desativados. Por exemplo, quando encontramos um nome *Alice* na sequência, podemos querer assumir que se refere a uma personagem feminina e ativar o indicador no estado de que temos um substantivo feminino na frase. Quando encontramos mais adiante a frase *and Tom*, ativaremos o indicador de que temos um substantivo no plural. Assim, manipulando o estado, podemos supostamente acompanhar as propriedades gramaticais das partes da frase.

> ✅ Um excelente recurso para entender os detalhes internos do LSTM é este ótimo artigo [Understanding LSTM Networks](https://colah.github.io/posts/2015-08-Understanding-LSTMs/) de Christopher Olah.

## RNNs Bidirecionais e Multicamadas

Discutimos redes recorrentes que operam em uma direção, do início de uma sequência até o fim. Isso parece natural, porque se assemelha à maneira como lemos e ouvimos a fala. No entanto, como em muitos casos práticos temos acesso aleatório à sequência de entrada, pode fazer sentido executar o cálculo recorrente em ambas as direções. Essas redes são chamadas de RNNs **bidirecionais**. Ao lidar com uma rede bidirecional, precisaríamos de dois vetores de estado ocultos, um para cada direção.

Uma rede recorrente, seja unidirecional ou bidirecional, captura certos padrões dentro de uma sequência e pode armazená-los em um vetor de estado ou passar para a saída. Assim como nas redes convolucionais, podemos construir outra camada recorrente em cima da primeira para capturar padrões de nível superior e construir a partir de padrões de baixo nível extraídos pela primeira camada. Isso nos leva à noção de uma **RNN multicamada**, que consiste em duas ou mais redes recorrentes, onde a saída da camada anterior é passada para a próxima camada como entrada.

![Imagem mostrando uma RNN multicamada de memória de longo e curto prazo](../../../../../translated_images/multi-layer-lstm.dd975e29bb2a59fe58b429db833932d734c81f211cad2783797a9608984acb8c.pt.jpg)

*Imagem do [este maravilhoso post](https://towardsdatascience.com/from-a-lstm-cell-to-a-multilayer-lstm-network-with-pytorch-2899eb5696f3) de Fernando López*

## ✍️ Exercícios: Embeddings

Continue seu aprendizado nos seguintes notebooks:

* [RNNs com PyTorch](../../../../../lessons/5-NLP/16-RNN/RNNPyTorch.ipynb)
* [RNNs com TensorFlow](../../../../../lessons/5-NLP/16-RNN/RNNTF.ipynb)

## Conclusão

Nesta unidade, vimos que as RNNs podem ser usadas para classificação de sequências, mas, na verdade, elas podem lidar com muitas outras tarefas, como geração de texto, tradução automática e mais. Consideraremos essas tarefas na próxima unidade.

## 🚀 Desafio

Leia algumas literaturas sobre LSTMs e considere suas aplicações:

- [Grid Long Short-Term Memory](https://arxiv.org/pdf/1507.01526v1.pdf)
- [Show, Attend and Tell: Neural Image Caption Generation with Visual Attention](https://arxiv.org/pdf/1502.03044v2.pdf)

## [Quiz pós-aula](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/216)

## Revisão & Autoestudo

- [Understanding LSTM Networks](https://colah.github.io/posts/2015-08-Understanding-LSTMs/) de Christopher Olah.

## [Tarefa: Notebooks](assignment.md)

**Isenção de responsabilidade**:  
Este documento foi traduzido utilizando serviços de tradução automática baseados em IA. Embora nos esforcemos pela precisão, por favor, esteja ciente de que traduções automatizadas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte autoritária. Para informações críticas, recomenda-se a tradução profissional por um humano. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações errôneas decorrentes do uso desta tradução.