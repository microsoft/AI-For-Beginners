<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "2b544f20b796402507fb05a0df893323",
  "translation_date": "2025-08-26T10:34:24+00:00",
  "source_file": "lessons/3-NeuralNetworks/05-Frameworks/README.md",
  "language_code": "br"
}
-->
# Frameworks de Redes Neurais

Como já aprendemos, para treinar redes neurais de forma eficiente, precisamos fazer duas coisas:

* Operar com tensores, por exemplo, multiplicar, somar e calcular algumas funções como sigmoid ou softmax.
* Calcular os gradientes de todas as expressões, para realizar a otimização por descida do gradiente.

## [Pré-aula: Quiz](https://ff-quizzes.netlify.app/en/ai/quiz/9)

Embora a biblioteca `numpy` possa realizar a primeira parte, precisamos de algum mecanismo para calcular os gradientes. No [nosso framework](../../../../../lessons/3-NeuralNetworks/04-OwnFramework/OwnFramework.ipynb) que desenvolvemos na seção anterior, tivemos que programar manualmente todas as funções derivadas dentro do método `backward`, que realiza a retropropagação. Idealmente, um framework deveria nos oferecer a possibilidade de calcular os gradientes de *qualquer expressão* que possamos definir.

Outra coisa importante é ser capaz de realizar cálculos em GPU ou em outras unidades de processamento especializadas, como [TPU](https://en.wikipedia.org/wiki/Tensor_Processing_Unit). O treinamento de redes neurais profundas exige *muitos* cálculos, e a capacidade de paralelizar esses cálculos em GPUs é muito importante.

> ✅ O termo 'paralelizar' significa distribuir os cálculos em vários dispositivos.

Atualmente, os dois frameworks de redes neurais mais populares são: [TensorFlow](http://TensorFlow.org) e [PyTorch](https://pytorch.org/). Ambos fornecem uma API de baixo nível para operar com tensores tanto em CPU quanto em GPU. Além da API de baixo nível, também há uma API de alto nível, chamada [Keras](https://keras.io/) e [PyTorch Lightning](https://pytorchlightning.ai/), respectivamente.

API de Baixo Nível | [TensorFlow](http://TensorFlow.org) | [PyTorch](https://pytorch.org/)
--------------------|-------------------------------------|--------------------------------
API de Alto Nível   | [Keras](https://keras.io/)         | [PyTorch Lightning](https://pytorchlightning.ai/)

As **APIs de baixo nível** em ambos os frameworks permitem construir os chamados **grafos computacionais**. Esse grafo define como calcular a saída (geralmente a função de perda) com os parâmetros de entrada fornecidos e pode ser enviado para cálculo em GPU, se disponível. Existem funções para diferenciar esse grafo computacional e calcular gradientes, que podem ser usados para otimizar os parâmetros do modelo.

As **APIs de alto nível** consideram redes neurais como uma **sequência de camadas**, tornando a construção da maioria das redes neurais muito mais fácil. Treinar o modelo geralmente exige preparar os dados e, em seguida, chamar uma função `fit` para realizar o treinamento.

A API de alto nível permite construir redes neurais típicas muito rapidamente, sem se preocupar com muitos detalhes. Ao mesmo tempo, a API de baixo nível oferece muito mais controle sobre o processo de treinamento e, por isso, é amplamente utilizada em pesquisas, quando se trabalha com novas arquiteturas de redes neurais.

Também é importante entender que você pode usar ambas as APIs juntas. Por exemplo, você pode desenvolver sua própria arquitetura de camada de rede usando a API de baixo nível e, em seguida, usá-la dentro de uma rede maior construída e treinada com a API de alto nível. Ou você pode definir uma rede usando a API de alto nível como uma sequência de camadas e, em seguida, usar seu próprio loop de treinamento de baixo nível para realizar a otimização. Ambas as APIs utilizam os mesmos conceitos básicos subjacentes e são projetadas para funcionar bem juntas.

## Aprendizado

Neste curso, oferecemos a maior parte do conteúdo tanto para PyTorch quanto para TensorFlow. Você pode escolher o framework de sua preferência e seguir apenas os notebooks correspondentes. Se não tiver certeza de qual framework escolher, leia algumas discussões na internet sobre **PyTorch vs. TensorFlow**. Você também pode explorar ambos os frameworks para obter uma melhor compreensão.

Sempre que possível, utilizaremos as APIs de alto nível para simplificar. No entanto, acreditamos que é importante entender como as redes neurais funcionam desde o início, por isso começamos trabalhando com a API de baixo nível e tensores. No entanto, se você quiser começar rapidamente e não gastar muito tempo aprendendo esses detalhes, pode pular essa parte e ir direto para os notebooks de API de alto nível.

## ✍️ Exercícios: Frameworks

Continue seu aprendizado nos seguintes notebooks:

API de Baixo Nível | [Notebook TensorFlow+Keras](../../../../../lessons/3-NeuralNetworks/05-Frameworks/IntroKerasTF.ipynb) | [PyTorch](../../../../../lessons/3-NeuralNetworks/05-Frameworks/IntroPyTorch.ipynb)
--------------------|-------------------------------------|--------------------------------
API de Alto Nível   | [Keras](../../../../../lessons/3-NeuralNetworks/05-Frameworks/IntroKeras.ipynb)          | *PyTorch Lightning*

Depois de dominar os frameworks, vamos revisar o conceito de overfitting.

# Overfitting

Overfitting é um conceito extremamente importante em aprendizado de máquina, e é essencial compreendê-lo corretamente!

Considere o seguinte problema de aproximar 5 pontos (representados por `x` nos gráficos abaixo):

![linear](../../../../../translated_images/overfit1.f24b71c6f652e59e6bed7245ffbeaecc3ba320e16e2221f6832b432052c4da43.br.jpg) | ![overfit](../../../../../translated_images/overfit2.131f5800ae10ca5e41d12a411f5f705d9ee38b1b10916f284b787028dd55cc1c.br.jpg)
-------------------------|--------------------------
**Modelo linear, 2 parâmetros** | **Modelo não-linear, 7 parâmetros**
Erro de treinamento = 5.3 | Erro de treinamento = 0
Erro de validação = 5.1 | Erro de validação = 20

* À esquerda, vemos uma boa aproximação com uma linha reta. Como o número de parâmetros é adequado, o modelo compreende corretamente a distribuição dos pontos.
* À direita, o modelo é muito poderoso. Como temos apenas 5 pontos e o modelo possui 7 parâmetros, ele pode se ajustar de forma a passar por todos os pontos, fazendo com que o erro de treinamento seja 0. No entanto, isso impede o modelo de entender o padrão correto dos dados, resultando em um erro de validação muito alto.

É muito importante encontrar um equilíbrio correto entre a complexidade do modelo (número de parâmetros) e o número de amostras de treinamento.

## Por que o overfitting ocorre

  * Poucos dados de treinamento
  * Modelo muito complexo
  * Muito ruído nos dados de entrada

## Como detectar overfitting

Como você pode ver no gráfico acima, o overfitting pode ser detectado por um erro de treinamento muito baixo e um erro de validação alto. Normalmente, durante o treinamento, veremos tanto o erro de treinamento quanto o de validação diminuindo, mas em algum momento o erro de validação pode parar de diminuir e começar a aumentar. Isso será um sinal de overfitting e um indicador de que devemos provavelmente parar o treinamento nesse ponto (ou pelo menos salvar um snapshot do modelo).

![overfitting](../../../../../translated_images/Overfitting.408ad91cd90b4371d0a81f4287e1409c359751adeb1ae450332af50e84f08c3e.br.png)

## Como prevenir o overfitting

Se você perceber que o overfitting está ocorrendo, pode fazer uma das seguintes ações:

 * Aumentar a quantidade de dados de treinamento
 * Diminuir a complexidade do modelo
 * Usar alguma [técnica de regularização](../../4-ComputerVision/08-TransferLearning/TrainingTricks.md), como [Dropout](../../4-ComputerVision/08-TransferLearning/TrainingTricks.md#Dropout), que será abordada mais adiante.

## Overfitting e o Compromisso Viés-Variância

O overfitting é, na verdade, um caso de um problema mais genérico em estatística chamado [Compromisso Viés-Variância](https://en.wikipedia.org/wiki/Bias%E2%80%93variance_tradeoff). Se considerarmos as possíveis fontes de erro em nosso modelo, podemos identificar dois tipos de erros:

* **Erros de viés** são causados pelo fato de nosso algoritmo não conseguir capturar corretamente a relação nos dados de treinamento. Isso pode ocorrer porque nosso modelo não é suficientemente poderoso (**underfitting**).
* **Erros de variância**, que são causados pelo modelo ao aproximar o ruído nos dados de entrada em vez de relações significativas (**overfitting**).

Durante o treinamento, o erro de viés diminui (à medida que nosso modelo aprende a aproximar os dados) e o erro de variância aumenta. É importante parar o treinamento - seja manualmente (quando detectamos overfitting) ou automaticamente (introduzindo regularização) - para evitar o overfitting.

## Conclusão

Nesta lição, você aprendeu sobre as diferenças entre as várias APIs dos dois frameworks de IA mais populares, TensorFlow e PyTorch. Além disso, você aprendeu sobre um tema muito importante: o overfitting.

## 🚀 Desafio

Nos notebooks que acompanham esta lição, você encontrará 'tarefas' no final; trabalhe nos notebooks e complete as tarefas.

## [Pós-aula: Quiz](https://ff-quizzes.netlify.app/en/ai/quiz/10)

## Revisão e Autoestudo

Pesquise sobre os seguintes tópicos:

- TensorFlow
- PyTorch
- Overfitting

Pergunte a si mesmo:

- Qual é a diferença entre TensorFlow e PyTorch?
- Qual é a diferença entre overfitting e underfitting?

## [Tarefa](lab/README.md)

Neste laboratório, você será solicitado a resolver dois problemas de classificação usando redes totalmente conectadas de uma ou várias camadas, utilizando PyTorch ou TensorFlow.

* [Instruções](lab/README.md)
* [Notebook](../../../../../lessons/3-NeuralNetworks/05-Frameworks/lab/LabFrameworks.ipynb)

**Aviso Legal**:  
Este documento foi traduzido utilizando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos para garantir a precisão, esteja ciente de que traduções automatizadas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte autoritativa. Para informações críticas, recomenda-se a tradução profissional realizada por humanos. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações equivocadas decorrentes do uso desta tradução.