# Redes generativas

## [Quiz pré-aula](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/117)

Redes Neurais Recorrentes (RNNs) e suas variantes com células portadas, como Células de Memória de Longo e Curto Prazo (LSTMs) e Unidades Recorrentes Portadas (GRUs), fornecem um mecanismo para modelagem de linguagem, pois podem aprender a ordem das palavras e fazer previsões para a próxima palavra em uma sequência. Isso nos permite usar RNNs para **tarefas generativas**, como geração de texto comum, tradução automática e até mesmo legendagem de imagens.

> ✅ Pense em todas as vezes que você se beneficiou de tarefas generativas, como a conclusão de texto enquanto digita. Faça uma pesquisa sobre seus aplicativos favoritos para ver se eles utilizaram RNNs.

Na arquitetura de RNN que discutimos na unidade anterior, cada unidade RNN produzia o próximo estado oculto como uma saída. No entanto, também podemos adicionar outra saída a cada unidade recorrente, o que nos permitiria gerar uma **sequência** (que tem o mesmo comprimento da sequência original). Além disso, podemos usar unidades RNN que não aceitam uma entrada em cada passo, e apenas pegam algum vetor de estado inicial, e então produzem uma sequência de saídas.

Isso permite diferentes arquiteturas neurais que são mostradas na imagem abaixo:

![Imagem mostrando padrões comuns de redes neurais recorrentes.](../../../../../translated_images/unreasonable-effectiveness-of-rnn.541ead816778f42dce6c42d8a56c184729aa2378d059b851be4ce12b993033df.pt.jpg)

> Imagem do post do blog [Eficácia Irresistível das Redes Neurais Recorrentes](http://karpathy.github.io/2015/05/21/rnn-effectiveness/) de [Andrej Karpaty](http://karpathy.github.io/)

* **Um-para-um** é uma rede neural tradicional com uma entrada e uma saída
* **Um-para-muitos** é uma arquitetura generativa que aceita um valor de entrada e gera uma sequência de valores de saída. Por exemplo, se quisermos treinar uma rede de **legendagem de imagens** que produza uma descrição textual de uma imagem, podemos usar uma imagem como entrada, passá-la por uma CNN para obter seu estado oculto, e então ter uma cadeia recorrente gerando a legenda palavra por palavra
* **Muitos-para-um** corresponde às arquiteturas RNN que descrevemos na unidade anterior, como a classificação de texto
* **Muitos-para-muitos**, ou **sequência-para-sequência**, corresponde a tarefas como **tradução automática**, onde temos a primeira RNN coletando todas as informações da sequência de entrada no estado oculto, e outra cadeia RNN desenrolando esse estado na sequência de saída.

Nesta unidade, vamos nos concentrar em modelos generativos simples que nos ajudam a gerar texto. Para simplificar, usaremos tokenização em nível de caractere.

Vamos treinar esta RNN para gerar texto passo a passo. Em cada passo, pegaremos uma sequência de caracteres de comprimento `nchars` e pediremos à rede para gerar o próximo caractere de saída para cada caractere de entrada:

![Imagem mostrando um exemplo de geração RNN da palavra 'OLÁ'.](../../../../../translated_images/rnn-generate.56c54afb52f9781d63a7c16ea9c1b86cb70e6e1eae6a742b56b7b37468576b17.pt.png)

Ao gerar texto (durante a inferência), começamos com algum **prompt**, que é passado pelas células RNN para gerar seu estado intermediário, e então a partir desse estado a geração começa. Geramos um caractere de cada vez e passamos o estado e o caractere gerado para outra célula RNN para gerar o próximo, até gerarmos caracteres suficientes.

<img src="images/rnn-generate-inf.png" width="60%"/>

> Imagem do autor

## ✍️ Exercícios: Redes Generativas

Continue seu aprendizado nos seguintes notebooks:

* [Redes Generativas com PyTorch](../../../../../lessons/5-NLP/17-GenerativeNetworks/GenerativePyTorch.ipynb)
* [Redes Generativas com TensorFlow](../../../../../lessons/5-NLP/17-GenerativeNetworks/GenerativeTF.ipynb)

## Geração de texto suave e temperatura

A saída de cada célula RNN é uma distribuição de probabilidade de caracteres. Se sempre pegarmos o caractere com a maior probabilidade como o próximo caractere no texto gerado, o texto pode frequentemente "circular" entre as mesmas sequências de caracteres repetidamente, como neste exemplo:

```
today of the second the company and a second the company ...
```

No entanto, se olharmos para a distribuição de probabilidade do próximo caractere, pode ser que a diferença entre algumas das maiores probabilidades não seja enorme, por exemplo, um caractere pode ter probabilidade 0.2, outro - 0.19, etc. Por exemplo, ao procurar o próximo caractere na sequência '*play*', o próximo caractere pode ser igualmente um espaço ou **e** (como na palavra *player*).

Isso nos leva à conclusão de que não é sempre "justo" selecionar o caractere com a maior probabilidade, porque escolher o segundo mais alto ainda pode nos levar a um texto significativo. É mais sábio **amostrar** caracteres da distribuição de probabilidade dada pela saída da rede. Também podemos usar um parâmetro, **temperatura**, que irá achatar a distribuição de probabilidade, caso queiramos adicionar mais aleatoriedade, ou torná-la mais acentuada, se quisermos nos apegar mais aos caracteres de maior probabilidade.

Explore como essa geração de texto suave é implementada nos notebooks vinculados acima.

## Conclusão

Embora a geração de texto possa ser útil por si só, os principais benefícios vêm da capacidade de gerar texto usando RNNs a partir de algum vetor de características inicial. Por exemplo, a geração de texto é usada como parte da tradução automática (sequência-para-sequência, neste caso o vetor de estado do *codificador* é usado para gerar ou *decodificar* a mensagem traduzida), ou gerando uma descrição textual de uma imagem (caso em que o vetor de características viria do extrator CNN).

## 🚀 Desafio

Faça algumas lições no Microsoft Learn sobre este tópico

* Geração de Texto com [PyTorch](https://docs.microsoft.com/learn/modules/intro-natural-language-processing-pytorch/6-generative-networks/?WT.mc_id=academic-77998-cacaste)/[TensorFlow](https://docs.microsoft.com/learn/modules/intro-natural-language-processing-tensorflow/5-generative-networks/?WT.mc_id=academic-77998-cacaste)

## [Quiz pós-aula](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/217)

## Revisão & Estudo Autônomo

Aqui estão alguns artigos para expandir seu conhecimento

* Diferentes abordagens para geração de texto com Cadeia de Markov, LSTM e GPT-2: [post do blog](https://towardsdatascience.com/text-generation-gpt-2-lstm-markov-chain-9ea371820e1e)
* Exemplo de geração de texto na [documentação do Keras](https://keras.io/examples/generative/lstm_character_level_text_generation/)

## [Tarefa](lab/README.md)

Vimos como gerar texto caractere por caractere. No laboratório, você explorará a geração de texto em nível de palavra.

**Isenção de responsabilidade**:  
Este documento foi traduzido usando serviços de tradução automática baseados em IA. Embora nos esforcemos pela precisão, esteja ciente de que traduções automatizadas podem conter erros ou imprecisões. O documento original em sua língua nativa deve ser considerado a fonte autoritária. Para informações críticas, recomenda-se a tradução profissional feita por humanos. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes do uso desta tradução.