# Frameworks de Redes Neurais

Como já aprendemos, para treinar redes neurais de forma eficiente, precisamos fazer duas coisas:

* Operar em tensores, por exemplo, multiplicar, adicionar e calcular algumas funções como sigmoid ou softmax
* Calcular gradientes de todas as expressões, a fim de realizar a otimização por descida de gradiente

## [Questionário pré-aula](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/105)

Enquanto a biblioteca `numpy` pode realizar a primeira parte, precisamos de algum mecanismo para calcular gradientes. No [nosso framework](../../../../../lessons/3-NeuralNetworks/04-OwnFramework/OwnFramework.ipynb) que desenvolvemos na seção anterior, tivemos que programar manualmente todas as funções derivadas dentro do método `backward`, que realiza a retropropagação. Idealmente, um framework deve nos oferecer a oportunidade de calcular gradientes de *qualquer expressão* que possamos definir.

Outra coisa importante é ser capaz de realizar cálculos em GPU ou em outras unidades de computação especializadas, como o [TPU](https://en.wikipedia.org/wiki/Tensor_Processing_Unit). O treinamento de redes neurais profundas exige *muitos* cálculos, e a capacidade de paralelizar esses cálculos em GPUs é muito importante.

> ✅ O termo 'paralelizar' significa distribuir os cálculos entre vários dispositivos.

Atualmente, os dois frameworks de redes neurais mais populares são: [TensorFlow](http://TensorFlow.org) e [PyTorch](https://pytorch.org/). Ambos fornecem uma API de baixo nível para operar com tensores tanto em CPU quanto em GPU. Além da API de baixo nível, também existe uma API de nível superior, chamada [Keras](https://keras.io/) e [PyTorch Lightning](https://pytorchlightning.ai/) respectivamente.

API de Baixo Nível | [TensorFlow](http://TensorFlow.org) | [PyTorch](https://pytorch.org/)
-------------------|-------------------------------------|--------------------------------
API de Alto Nível  | [Keras](https://keras.io/) | [PyTorch Lightning](https://pytorchlightning.ai/)

**APIs de baixo nível** em ambos os frameworks permitem que você construa os chamados **gráficos computacionais**. Este gráfico define como calcular a saída (geralmente a função de perda) com parâmetros de entrada dados, e pode ser enviado para computação na GPU, se disponível. Existem funções para diferenciar esse gráfico computacional e calcular gradientes, que podem então ser usados para otimizar os parâmetros do modelo.

**APIs de alto nível** consideram essencialmente redes neurais como uma **sequência de camadas**, tornando a construção da maioria das redes neurais muito mais fácil. O treinamento do modelo geralmente requer a preparação dos dados e, em seguida, a chamada de uma função `fit` para realizar a tarefa.

A API de alto nível permite que você construa redes neurais típicas rapidamente, sem se preocupar com muitos detalhes. Ao mesmo tempo, a API de baixo nível oferece muito mais controle sobre o processo de treinamento, e, portanto, é muito utilizada em pesquisas, quando você está lidando com novas arquiteturas de redes neurais.

É também importante entender que você pode usar ambas as APIs juntas, por exemplo, você pode desenvolver sua própria arquitetura de camada de rede usando a API de baixo nível e, em seguida, usá-la dentro da rede maior construída e treinada com a API de alto nível. Ou você pode definir uma rede usando a API de alto nível como uma sequência de camadas e, em seguida, usar seu próprio loop de treinamento de baixo nível para realizar a otimização. Ambas as APIs utilizam os mesmos conceitos básicos subjacentes e são projetadas para funcionar bem juntas.

## Aprendizado

Neste curso, oferecemos a maior parte do conteúdo tanto para PyTorch quanto para TensorFlow. Você pode escolher seu framework preferido e apenas percorrer os notebooks correspondentes. Se você não tiver certeza de qual framework escolher, leia algumas discussões na internet sobre **PyTorch vs. TensorFlow**. Você também pode dar uma olhada em ambos os frameworks para obter uma melhor compreensão.

Sempre que possível, usaremos APIs de Alto Nível por uma questão de simplicidade. No entanto, acreditamos que é importante entender como as redes neurais funcionam desde o início, portanto, no começo, começamos trabalhando com a API de baixo nível e tensores. Contudo, se você quiser avançar rapidamente e não quiser passar muito tempo aprendendo esses detalhes, pode pular essas partes e ir direto para os notebooks da API de alto nível.

## ✍️ Exercícios: Frameworks

Continue seu aprendizado nos seguintes notebooks:

API de Baixo Nível | [Notebook TensorFlow+Keras](../../../../../lessons/3-NeuralNetworks/05-Frameworks/IntroKerasTF.ipynb) | [PyTorch](../../../../../lessons/3-NeuralNetworks/05-Frameworks/IntroPyTorch.ipynb)
-------------------|-------------------------------------|--------------------------------
API de Alto Nível  | [Keras](../../../../../lessons/3-NeuralNetworks/05-Frameworks/IntroKeras.ipynb) | *PyTorch Lightning*

Após dominar os frameworks, vamos recapitular a noção de sobreajuste.

# Sobreajuste

O sobreajuste é um conceito extremamente importante em aprendizado de máquina, e é crucial compreendê-lo corretamente!

Considere o seguinte problema de aproximar 5 pontos (representados por `x` nos gráficos abaixo):

![linear](../../../../../translated_images/overfit1.f24b71c6f652e59e6bed7245ffbeaecc3ba320e16e2221f6832b432052c4da43.it.jpg) | ![overfit](../../../../../translated_images/overfit2.131f5800ae10ca5e41d12a411f5f705d9ee38b1b10916f284b787028dd55cc1c.it.jpg)
-------------------------|--------------------------
**Modelo linear, 2 parâmetros** | **Modelo não-linear, 7 parâmetros**
Erro de treinamento = 5.3 | Erro de validação = 0
Erro de validação = 5.1 | Erro de validação = 20

* À esquerda, vemos uma boa aproximação de linha reta. Como o número de parâmetros é adequado, o modelo compreende bem a distribuição dos pontos.
* À direita, o modelo é muito poderoso. Como temos apenas 5 pontos e o modelo possui 7 parâmetros, ele pode se ajustar de tal forma a passar por todos os pontos, fazendo com que o erro de treinamento seja 0. No entanto, isso impede que o modelo entenda o padrão correto por trás dos dados, resultando em um erro de validação muito alto.

É muito importante encontrar um equilíbrio adequado entre a complexidade do modelo (número de parâmetros) e o número de amostras de treinamento.

## Por que o sobreajuste ocorre

  * Dados de treinamento insuficientes
  * Modelo excessivamente poderoso
  * Muito ruído nos dados de entrada

## Como detectar o sobreajuste

Como você pode ver no gráfico acima, o sobreajuste pode ser detectado por um erro de treinamento muito baixo e um erro de validação alto. Normalmente, durante o treinamento, observamos ambos os erros de treinamento e validação começando a diminuir, e então, em algum momento, o erro de validação pode parar de diminuir e começar a aumentar. Isso será um sinal de sobreajuste e um indicativo de que devemos provavelmente parar o treinamento neste ponto (ou pelo menos fazer uma captura do modelo).

![overfitting](../../../../../translated_images/Overfitting.408ad91cd90b4371d0a81f4287e1409c359751adeb1ae450332af50e84f08c3e.it.png)

## Como prevenir o sobreajuste

Se você perceber que o sobreajuste está ocorrendo, pode fazer uma das seguintes ações:

 * Aumentar a quantidade de dados de treinamento
 * Diminuir a complexidade do modelo
 * Utilizar alguma [técnica de regularização](../../4-ComputerVision/08-TransferLearning/TrainingTricks.md), como [Dropout](../../4-ComputerVision/08-TransferLearning/TrainingTricks.md#Dropout), que consideraremos mais adiante.

## Sobreajuste e a Troca de Viés-Variância

O sobreajuste é, na verdade, um caso de um problema mais genérico em estatísticas chamado [Troca de Viés-Variância](https://en.wikipedia.org/wiki/Bias%E2%80%93variance_tradeoff). Se considerarmos as possíveis fontes de erro em nosso modelo, podemos observar dois tipos de erros:

* **Erros de viés** são causados pelo fato de nosso algoritmo não conseguir capturar corretamente a relação entre os dados de treinamento. Isso pode resultar do fato de nosso modelo não ser poderoso o suficiente (**subajuste**).
* **Erros de variância**, que são causados pelo modelo aproximar o ruído nos dados de entrada em vez de uma relação significativa (**sobreajuste**).

Durante o treinamento, o erro de viés diminui (à medida que nosso modelo aprende a aproximar os dados), e o erro de variância aumenta. É importante parar o treinamento - seja manualmente (quando detectamos sobreajuste) ou automaticamente (introduzindo regularização) - para evitar o sobreajuste.

## Conclusão

Nesta lição, você aprendeu sobre as diferenças entre as várias APIs dos dois frameworks de IA mais populares, TensorFlow e PyTorch. Além disso, você aprendeu sobre um tópico muito importante, o sobreajuste.

## 🚀 Desafio

Nos notebooks acompanhantes, você encontrará 'tarefas' na parte inferior; trabalhe pelos notebooks e complete as tarefas.

## [Questionário pós-aula](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/205)

## Revisão e Autoestudo

Faça uma pesquisa sobre os seguintes tópicos:

- TensorFlow
- PyTorch
- Sobreajuste

Pergunte a si mesmo as seguintes questões:

- Qual é a diferença entre TensorFlow e PyTorch?
- Qual é a diferença entre sobreajuste e subajuste?

## [Tarefa](lab/README.md)

Neste laboratório, você é solicitado a resolver dois problemas de classificação usando redes totalmente conectadas de uma e várias camadas, utilizando PyTorch ou TensorFlow.

* [Instruções](lab/README.md)
* [Notebook](../../../../../lessons/3-NeuralNetworks/05-Frameworks/lab/LabFrameworks.ipynb)

**Disclaimer**:  
This document has been translated using machine-based AI translation services. While we strive for accuracy, please be aware that automated translations may contain errors or inaccuracies. The original document in its native language should be considered the authoritative source. For critical information, professional human translation is recommended. We are not liable for any misunderstandings or misinterpretations arising from the use of this translation.