# Redes Generativas

## [Questionário pré-aula](https://ff-quizzes.netlify.app/en/ai/quiz/33)

As Redes Neuronais Recorrentes (RNNs) e suas variantes com células de controlo, como as Long Short Term Memory Cells (LSTMs) e Gated Recurrent Units (GRUs), proporcionaram um mecanismo para modelação de linguagem, permitindo aprender a ordem das palavras e prever a próxima palavra numa sequência. Isto permite-nos usar RNNs para **tarefas generativas**, como geração de texto comum, tradução automática e até legendagem de imagens.

> ✅ Pense em todas as vezes que beneficiou de tarefas generativas, como a conclusão de texto enquanto escreve. Pesquise sobre as suas aplicações favoritas para ver se utilizaram RNNs.

Na arquitetura de RNN discutida na unidade anterior, cada unidade RNN produzia o próximo estado oculto como saída. No entanto, também podemos adicionar outra saída a cada unidade recorrente, permitindo-nos gerar uma **sequência** (de comprimento igual à sequência original). Além disso, podemos usar unidades RNN que não aceitam uma entrada em cada passo, mas apenas um vetor de estado inicial, e depois produzem uma sequência de saídas.

Isto permite diferentes arquiteturas neuronais, como mostrado na imagem abaixo:

![Imagem mostrando padrões comuns de redes neuronais recorrentes.](../../../../../translated_images/pt-PT/unreasonable-effectiveness-of-rnn.541ead816778f42d.webp)

> Imagem do artigo [Unreasonable Effectiveness of Recurrent Neural Networks](http://karpathy.github.io/2015/05/21/rnn-effectiveness/) por [Andrej Karpaty](http://karpathy.github.io/)

* **Um-para-um** é uma rede neural tradicional com uma entrada e uma saída.
* **Um-para-muitos** é uma arquitetura generativa que aceita um valor de entrada e gera uma sequência de valores de saída. Por exemplo, se quisermos treinar uma rede de **legendagem de imagens** que produza uma descrição textual de uma imagem, podemos usar uma imagem como entrada, passá-la por uma CNN para obter o estado oculto e, em seguida, usar uma cadeia recorrente para gerar a legenda palavra por palavra.
* **Muitos-para-um** corresponde às arquiteturas RNN descritas na unidade anterior, como classificação de texto.
* **Muitos-para-muitos**, ou **sequência-para-sequência**, corresponde a tarefas como **tradução automática**, onde temos uma primeira RNN que recolhe toda a informação da sequência de entrada no estado oculto, e outra cadeia RNN que desenrola este estado na sequência de saída.

Nesta unidade, vamos focar-nos em modelos generativos simples que nos ajudam a gerar texto. Para simplificar, usaremos tokenização a nível de caracteres.

Vamos treinar esta RNN para gerar texto passo a passo. Em cada passo, tomaremos uma sequência de caracteres de comprimento `nchars` e pediremos à rede que gere o próximo carácter de saída para cada carácter de entrada:

![Imagem mostrando um exemplo de geração de RNN da palavra 'HELLO'.](../../../../../translated_images/pt-PT/rnn-generate.56c54afb52f9781d.webp)

Ao gerar texto (durante a inferência), começamos com um **prompt**, que é passado pelas células RNN para gerar o estado intermédio, e a partir deste estado começa a geração. Geramos um carácter de cada vez e passamos o estado e o carácter gerado para outra célula RNN para gerar o próximo, até gerarmos caracteres suficientes.

<img src="../../../../../translated_images/pt-PT/rnn-generate-inf.5168dc65e0370eea.webp" width="60%"/>

> Imagem do autor

## ✍️ Exercícios: Redes Generativas

Continue a sua aprendizagem nos seguintes notebooks:

* [Redes Generativas com PyTorch](GenerativePyTorch.ipynb)
* [Redes Generativas com TensorFlow](GenerativeTF.ipynb)

## Geração de texto suave e temperatura

A saída de cada célula RNN é uma distribuição de probabilidade de caracteres. Se sempre escolhermos o carácter com a maior probabilidade como o próximo carácter no texto gerado, o texto pode frequentemente tornar-se "cíclico", repetindo as mesmas sequências de caracteres repetidamente, como neste exemplo:

```
today of the second the company and a second the company ...
```

No entanto, se olharmos para a distribuição de probabilidade do próximo carácter, pode acontecer que a diferença entre algumas das maiores probabilidades não seja muito grande, por exemplo, um carácter pode ter probabilidade 0.2, outro 0.19, etc. Por exemplo, ao procurar o próximo carácter na sequência '*play*', o próximo carácter pode ser igualmente um espaço ou **e** (como na palavra *player*).

Isto leva-nos à conclusão de que nem sempre é "justo" selecionar o carácter com maior probabilidade, porque escolher o segundo maior ainda pode levar a texto significativo. É mais sensato **amostrar** caracteres da distribuição de probabilidade dada pela saída da rede. Podemos também usar um parâmetro, **temperatura**, que ajusta a distribuição de probabilidade, caso queiramos adicionar mais aleatoriedade ou torná-la mais íngreme, se quisermos aderir mais aos caracteres de maior probabilidade.

Explore como esta geração de texto suave é implementada nos notebooks acima mencionados.

## Conclusão

Embora a geração de texto possa ser útil por si só, os maiores benefícios vêm da capacidade de gerar texto usando RNNs a partir de algum vetor de características inicial. Por exemplo, a geração de texto é usada como parte da tradução automática (sequência-para-sequência, neste caso o vetor de estado do *encoder* é usado para gerar ou *decodificar* a mensagem traduzida) ou para gerar descrições textuais de uma imagem (neste caso, o vetor de características viria de um extrator CNN).

## 🚀 Desafio

Faça algumas lições na Microsoft Learn sobre este tópico:

* Geração de Texto com [PyTorch](https://docs.microsoft.com/learn/modules/intro-natural-language-processing-pytorch/6-generative-networks/?WT.mc_id=academic-77998-cacaste)/[TensorFlow](https://docs.microsoft.com/learn/modules/intro-natural-language-processing-tensorflow/5-generative-networks/?WT.mc_id=academic-77998-cacaste)

## [Questionário pós-aula](https://ff-quizzes.netlify.app/en/ai/quiz/34)

## Revisão & Autoestudo

Aqui estão alguns artigos para expandir o seu conhecimento:

* Diferentes abordagens para geração de texto com Markov Chain, LSTM e GPT-2: [artigo](https://towardsdatascience.com/text-generation-gpt-2-lstm-markov-chain-9ea371820e1e)
* Exemplo de geração de texto na [documentação do Keras](https://keras.io/examples/generative/lstm_character_level_text_generation/)

## [Tarefa](lab/README.md)

Vimos como gerar texto carácter por carácter. No laboratório, irá explorar a geração de texto a nível de palavras.

---

