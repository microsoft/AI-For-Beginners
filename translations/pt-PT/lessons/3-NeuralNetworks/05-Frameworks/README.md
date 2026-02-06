# Frameworks de Redes Neuronais

Como já aprendemos, para treinar redes neuronais de forma eficiente, precisamos fazer duas coisas:

* Operar com tensores, por exemplo, multiplicar, somar e calcular algumas funções como sigmoid ou softmax.
* Calcular os gradientes de todas as expressões, para realizar a otimização por descida de gradiente.

## [Questionário pré-aula](https://ff-quizzes.netlify.app/en/ai/quiz/9)

Embora a biblioteca `numpy` consiga realizar a primeira parte, precisamos de um mecanismo para calcular gradientes. No [nosso framework](../04-OwnFramework/OwnFramework.ipynb) que desenvolvemos na seção anterior, tivemos que programar manualmente todas as funções derivadas dentro do método `backward`, que realiza a retropropagação. Idealmente, um framework deveria permitir-nos calcular os gradientes de *qualquer expressão* que possamos definir.

Outro ponto importante é a capacidade de realizar cálculos em GPU ou outras unidades de computação especializadas, como [TPU](https://en.wikipedia.org/wiki/Tensor_Processing_Unit). O treino de redes neuronais profundas exige *muitos* cálculos, e poder paralelizar esses cálculos em GPUs é fundamental.

> ✅ O termo 'paralelizar' significa distribuir os cálculos por vários dispositivos.

Atualmente, os dois frameworks de redes neuronais mais populares são: [TensorFlow](http://TensorFlow.org) e [PyTorch](https://pytorch.org/). Ambos oferecem uma API de baixo nível para operar com tensores tanto em CPU quanto em GPU. Além da API de baixo nível, também existe uma API de alto nível, chamada [Keras](https://keras.io/) e [PyTorch Lightning](https://pytorchlightning.ai/), respetivamente.

API de Baixo Nível | [TensorFlow](http://TensorFlow.org) | [PyTorch](https://pytorch.org/)
--------------------|-------------------------------------|--------------------------------
API de Alto Nível   | [Keras](https://keras.io/)         | [PyTorch Lightning](https://pytorchlightning.ai/)

**APIs de baixo nível** em ambos os frameworks permitem construir os chamados **grafos computacionais**. Este grafo define como calcular o resultado (geralmente a função de perda) com os parâmetros de entrada fornecidos e pode ser enviado para cálculo em GPU, se disponível. Existem funções para diferenciar este grafo computacional e calcular gradientes, que podem ser usados para otimizar os parâmetros do modelo.

**APIs de alto nível** consideram redes neuronais como uma **sequência de camadas**, facilitando muito a construção da maioria das redes neuronais. Treinar o modelo geralmente requer preparar os dados e, em seguida, chamar uma função `fit` para realizar o trabalho.

A API de alto nível permite construir redes neuronais típicas de forma muito rápida, sem se preocupar com muitos detalhes. Por outro lado, a API de baixo nível oferece muito mais controlo sobre o processo de treino e, por isso, é amplamente utilizada em pesquisa, quando se trabalha com novas arquiteturas de redes neuronais.

É também importante entender que ambas as APIs podem ser usadas em conjunto. Por exemplo, pode-se desenvolver a arquitetura de uma camada de rede usando a API de baixo nível e, em seguida, utilizá-la dentro de uma rede maior construída e treinada com a API de alto nível. Ou pode-se definir uma rede usando a API de alto nível como uma sequência de camadas e, depois, usar o próprio loop de treino de baixo nível para realizar a otimização. Ambas as APIs utilizam os mesmos conceitos básicos subjacentes e foram projetadas para funcionar bem juntas.

## Aprendizagem

Neste curso, oferecemos a maior parte do conteúdo tanto para PyTorch quanto para TensorFlow. Pode escolher o framework preferido e seguir apenas os notebooks correspondentes. Se não tiver certeza de qual framework escolher, leia algumas discussões na internet sobre **PyTorch vs. TensorFlow**. Também pode explorar ambos os frameworks para obter uma melhor compreensão.

Sempre que possível, utilizaremos APIs de alto nível para simplificar. No entanto, acreditamos que é importante entender como as redes neuronais funcionam desde o início, por isso começamos trabalhando com a API de baixo nível e tensores. Contudo, se quiser avançar rapidamente e não gastar muito tempo aprendendo esses detalhes, pode ignorar essa parte e ir diretamente para os notebooks de API de alto nível.

## ✍️ Exercícios: Frameworks

Continue a sua aprendizagem nos seguintes notebooks:

API de Baixo Nível | [Notebook TensorFlow+Keras](IntroKerasTF.ipynb) | [PyTorch](IntroPyTorch.ipynb)
--------------------|-------------------------------------|--------------------------------
API de Alto Nível   | [Keras](IntroKeras.ipynb)         | *PyTorch Lightning*

Depois de dominar os frameworks, vamos recapitular o conceito de overfitting.

# Overfitting

Overfitting é um conceito extremamente importante em aprendizagem automática, e é essencial compreendê-lo corretamente!

Considere o seguinte problema de aproximar 5 pontos (representados por `x` nos gráficos abaixo):

![linear](../../../../../translated_images/pt-PT/overfit1.f24b71c6f652e59e.webp) | ![overfit](../../../../../translated_images/pt-PT/overfit2.131f5800ae10ca5e.webp)
-------------------------|--------------------------
**Modelo linear, 2 parâmetros** | **Modelo não-linear, 7 parâmetros**
Erro de treino = 5.3 | Erro de treino = 0
Erro de validação = 5.1 | Erro de validação = 20

* À esquerda, vemos uma boa aproximação com uma linha reta. Como o número de parâmetros é adequado, o modelo compreende corretamente a distribuição dos pontos.
* À direita, o modelo é demasiado poderoso. Como temos apenas 5 pontos e o modelo possui 7 parâmetros, ele ajusta-se de forma a passar por todos os pontos, fazendo com que o erro de treino seja 0. No entanto, isso impede o modelo de entender o padrão correto dos dados, resultando num erro de validação muito alto.

É muito importante encontrar o equilíbrio correto entre a complexidade do modelo (número de parâmetros) e o número de amostras de treino.

## Por que ocorre o overfitting

  * Poucos dados de treino
  * Modelo demasiado poderoso
  * Demasiado ruído nos dados de entrada

## Como detetar o overfitting

Como pode ver no gráfico acima, o overfitting pode ser detetado por um erro de treino muito baixo e um erro de validação elevado. Normalmente, durante o treino, vemos tanto os erros de treino quanto de validação começarem a diminuir, e então, em algum momento, o erro de validação pode parar de diminuir e começar a aumentar. Este será um sinal de overfitting e um indicador de que provavelmente devemos parar o treino nesse ponto (ou pelo menos fazer um snapshot do modelo).

![overfitting](../../../../../translated_images/pt-PT/Overfitting.408ad91cd90b4371.webp)

## Como prevenir o overfitting

Se perceber que o overfitting está a ocorrer, pode fazer o seguinte:

 * Aumentar a quantidade de dados de treino.
 * Reduzir a complexidade do modelo.
 * Utilizar alguma [técnica de regularização](../../4-ComputerVision/08-TransferLearning/TrainingTricks.md), como [Dropout](../../4-ComputerVision/08-TransferLearning/TrainingTricks.md#Dropout), que será abordada mais tarde.

## Overfitting e o Tradeoff Viés-Variância

O overfitting é, na verdade, um caso de um problema mais genérico em estatística chamado [Tradeoff Viés-Variância](https://en.wikipedia.org/wiki/Bias%E2%80%93variance_tradeoff). Se considerarmos as possíveis fontes de erro no nosso modelo, podemos identificar dois tipos de erros:

* **Erros de viés** são causados pelo nosso algoritmo não conseguir capturar corretamente a relação entre os dados de treino. Isso pode resultar do facto de o modelo não ser suficientemente poderoso (**underfitting**).
* **Erros de variância**, que são causados pelo modelo aproximar o ruído nos dados de entrada em vez de uma relação significativa (**overfitting**).

Durante o treino, o erro de viés diminui (à medida que o modelo aprende a aproximar os dados) e o erro de variância aumenta. É importante parar o treino - seja manualmente (quando detetamos overfitting) ou automaticamente (introduzindo regularização) - para evitar o overfitting.

## Conclusão

Nesta lição, aprendeu sobre as diferenças entre as várias APIs dos dois frameworks de IA mais populares, TensorFlow e PyTorch. Além disso, aprendeu sobre um tópico muito importante: overfitting.

## 🚀 Desafio

Nos notebooks que acompanham esta lição, encontrará 'tarefas' no final; trabalhe nos notebooks e complete as tarefas.

## [Questionário pós-aula](https://ff-quizzes.netlify.app/en/ai/quiz/10)

## Revisão & Autoestudo

Pesquise sobre os seguintes tópicos:

- TensorFlow
- PyTorch
- Overfitting

Pergunte a si mesmo as seguintes questões:

- Qual é a diferença entre TensorFlow e PyTorch?
- Qual é a diferença entre overfitting e underfitting?

## [Trabalho prático](lab/README.md)

Neste trabalho prático, será solicitado que resolva dois problemas de classificação usando redes totalmente conectadas de uma ou várias camadas, utilizando PyTorch ou TensorFlow.

* [Instruções](lab/README.md)
* [Notebook](lab/LabFrameworks.ipynb)

---

