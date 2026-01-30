# Truques para Treinamento de Deep Learning

À medida que as redes neurais se tornam mais profundas, o processo de treinamento delas se torna cada vez mais desafiador. Um dos principais problemas é o chamado [vanishing gradients](https://en.wikipedia.org/wiki/Vanishing_gradient_problem) (gradientes que desaparecem) ou [exploding gradients](https://deepai.org/machine-learning-glossary-and-terms/exploding-gradient-problem#:~:text=Exploding%20gradients%20are%20a%20problem,updates%20are%20small%20and%20controlled.) (gradientes que explodem). [Este artigo](https://towardsdatascience.com/the-vanishing-exploding-gradient-problem-in-deep-neural-networks-191358470c11) oferece uma boa introdução a esses problemas.

Para tornar o treinamento de redes profundas mais eficiente, existem algumas técnicas que podem ser utilizadas.

## Mantendo os valores em um intervalo razoável

Para tornar os cálculos numéricos mais estáveis, queremos garantir que todos os valores dentro da nossa rede neural estejam em uma escala razoável, tipicamente [-1..1] ou [0..1]. Não é um requisito muito rigoroso, mas a natureza dos cálculos em ponto flutuante é tal que valores de magnitudes diferentes não podem ser manipulados com precisão juntos. Por exemplo, se somarmos 10<sup>-10</sup> e 10<sup>10</sup>, provavelmente obteremos 10<sup>10</sup>, porque o valor menor seria "convertido" para a mesma ordem do maior, e assim a mantissa seria perdida.

A maioria das funções de ativação possui não-linearidades em torno de [-1..1], e, portanto, faz sentido escalar todos os dados de entrada para o intervalo [-1..1] ou [0..1].

## Inicialização de Pesos

Idealmente, queremos que os valores estejam na mesma faixa após passarem pelas camadas da rede. Assim, é importante inicializar os pesos de forma a preservar a distribuição dos valores.

A distribuição normal **N(0,1)** não é uma boa ideia, porque se tivermos *n* entradas, o desvio padrão da saída será *n*, e os valores provavelmente sairão do intervalo [0..1].

As seguintes inicializações são frequentemente usadas:

- Distribuição uniforme -- `uniform`
- **N(0,1/n)** -- `gaussian`
- **N(0,1/√n_in)** garante que, para entradas com média zero e desvio padrão de 1, a mesma média/desvio padrão será mantida
- **N(0,√2/(n_in+n_out))** -- a chamada **inicialização de Xavier** (`glorot`), que ajuda a manter os sinais na faixa durante a propagação direta e reversa

## Normalização em Lote (Batch Normalization)

Mesmo com uma inicialização adequada dos pesos, eles podem ficar arbitrariamente grandes ou pequenos durante o treinamento, o que levará os sinais para fora da faixa adequada. Podemos trazer os sinais de volta usando uma das técnicas de **normalização**. Embora existam várias delas (normalização de pesos, normalização de camadas), a mais utilizada é a Normalização em Lote.

A ideia da **normalização em lote** é levar em conta todos os valores dentro do minibatch e realizar a normalização (ou seja, subtrair a média e dividir pelo desvio padrão) com base nesses valores. Ela é implementada como uma camada da rede que realiza essa normalização após aplicar os pesos, mas antes da função de ativação. Como resultado, é provável que vejamos maior precisão final e treinamento mais rápido.

Aqui está o [artigo original](https://arxiv.org/pdf/1502.03167.pdf) sobre normalização em lote, a [explicação na Wikipedia](https://en.wikipedia.org/wiki/Batch_normalization) e [um bom post introdutório](https://towardsdatascience.com/batch-normalization-in-3-levels-of-understanding-14c2da90a338) (e outro [em russo](https://habrahabr.ru/post/309302/)).

## Dropout

**Dropout** é uma técnica interessante que remove uma certa porcentagem de neurônios aleatórios durante o treinamento. Ele também é implementado como uma camada com um parâmetro (percentual de neurônios a serem removidos, tipicamente 10%-50%), e durante o treinamento ele zera elementos aleatórios do vetor de entrada antes de passá-lo para a próxima camada.

Embora isso possa parecer uma ideia estranha, você pode ver o efeito do dropout no treinamento de um classificador de dígitos MNIST no notebook [`Dropout.ipynb`](../../../../../lessons/4-ComputerVision/08-TransferLearning/Dropout.ipynb). Ele acelera o treinamento e permite alcançar maior precisão em menos épocas de treinamento.

Esse efeito pode ser explicado de várias maneiras:

- Pode ser considerado como um fator de choque aleatório para o modelo, que tira a otimização de mínimos locais
- Pode ser considerado como uma *média implícita de modelos*, porque podemos dizer que durante o dropout estamos treinando modelos ligeiramente diferentes

> *Algumas pessoas dizem que, quando uma pessoa bêbada tenta aprender algo, ela se lembrará melhor disso na manhã seguinte, em comparação com uma pessoa sóbria, porque um cérebro com alguns neurônios "defeituosos" tenta se adaptar melhor para captar o significado. Nunca testamos se isso é verdade ou não.*

## Prevenindo Overfitting

Um dos aspectos muito importantes do deep learning é ser capaz de prevenir o [overfitting](../../3-NeuralNetworks/05-Frameworks/Overfitting.md). Embora possa ser tentador usar um modelo de rede neural muito poderoso, devemos sempre equilibrar o número de parâmetros do modelo com o número de amostras de treinamento.

> Certifique-se de entender o conceito de [overfitting](../../3-NeuralNetworks/05-Frameworks/Overfitting.md) que introduzimos anteriormente!

Existem várias maneiras de prevenir o overfitting:

- Parada antecipada (Early stopping) -- monitorar continuamente o erro no conjunto de validação e interromper o treinamento quando o erro de validação começar a aumentar.
- Decaimento de pesos explícito / Regularização -- adicionar uma penalidade extra à função de perda para valores absolutos altos dos pesos, o que evita que o modelo produza resultados muito instáveis
- Média de Modelos -- treinar vários modelos e depois fazer a média dos resultados. Isso ajuda a minimizar a variância.
- Dropout (Média Implícita de Modelos)

## Otimizadores / Algoritmos de Treinamento

Outro aspecto importante do treinamento é escolher um bom algoritmo de treinamento. Embora o **gradiente descendente** clássico seja uma escolha razoável, ele pode, às vezes, ser muito lento ou resultar em outros problemas.

No deep learning, usamos o **Stochastic Gradient Descent** (SGD), que é um gradiente descendente aplicado a minibatches, selecionados aleatoriamente do conjunto de treinamento. Os pesos são ajustados usando esta fórmula:

w<sup>t+1</sup> = w<sup>t</sup> - η∇ℒ

### Momentum

No **momentum SGD**, mantemos uma parte do gradiente dos passos anteriores. É semelhante a quando estamos nos movendo com inércia e recebemos um empurrão em uma direção diferente; nossa trajetória não muda imediatamente, mas mantém parte do movimento original. Aqui introduzimos outro vetor v para representar a *velocidade*:

- v<sup>t+1</sup> = γ v<sup>t</sup> - η∇ℒ
- w<sup>t+1</sup> = w<sup>t</sup> + v<sup>t+1</sup>

Aqui, o parâmetro γ indica a extensão em que levamos a inércia em conta: γ=0 corresponde ao SGD clássico; γ=1 é uma equação de movimento puro.

### Adam, Adagrad, etc.

Como em cada camada multiplicamos os sinais por alguma matriz W<sub>i</sub>, dependendo de ||W<sub>i</sub>||, o gradiente pode diminuir e ficar próximo de 0 ou crescer indefinidamente. Esse é o cerne do problema de Exploding/Vanishing Gradients.

Uma das soluções para esse problema é usar apenas a direção do gradiente na equação e ignorar o valor absoluto, ou seja:

w<sup>t+1</sup> = w<sup>t</sup> - η(∇ℒ/||∇ℒ||), onde ||∇ℒ|| = √∑(∇ℒ)<sup>2</sup>

Esse algoritmo é chamado de **Adagrad**. Outros algoritmos que usam a mesma ideia: **RMSProp**, **Adam**

> **Adam** é considerado um algoritmo muito eficiente para muitas aplicações, então, se você não tiver certeza de qual usar, use Adam.

### Gradient clipping

Gradient clipping é uma extensão da ideia acima. Quando ||∇ℒ|| ≤ θ, consideramos o gradiente original na otimização dos pesos, e quando ||∇ℒ|| > θ, dividimos o gradiente pela sua norma. Aqui, θ é um parâmetro; na maioria dos casos, podemos usar θ=1 ou θ=10.

### Decaimento da taxa de aprendizado

O sucesso do treinamento frequentemente depende do parâmetro de taxa de aprendizado η. É lógico supor que valores maiores de η resultam em treinamento mais rápido, algo que geralmente queremos no início do treinamento, e então valores menores de η permitem ajustar melhor a rede. Assim, na maioria dos casos, queremos diminuir η ao longo do treinamento.

Isso pode ser feito multiplicando η por algum número (por exemplo, 0,98) após cada época de treinamento ou usando um **cronograma de taxa de aprendizado** mais complexo.

## Diferentes Arquiteturas de Redes

Selecionar a arquitetura de rede certa para o seu problema pode ser complicado. Normalmente, escolheríamos uma arquitetura que tenha se mostrado eficaz para nossa tarefa específica (ou uma similar). Aqui está uma [boa visão geral](https://www.topbots.com/a-brief-history-of-neural-network-architectures/) de arquiteturas de redes neurais para visão computacional.

> É importante selecionar uma arquitetura que seja poderosa o suficiente para o número de amostras de treinamento que temos. Selecionar um modelo muito poderoso pode resultar em [overfitting](../../3-NeuralNetworks/05-Frameworks/Overfitting.md).

Outra boa abordagem seria usar uma arquitetura que se ajuste automaticamente à complexidade necessária. Até certo ponto, as arquiteturas **ResNet** e **Inception** são autoajustáveis. [Mais sobre arquiteturas para visão computacional](../07-ConvNets/CNN_Architectures.md)

**Aviso Legal**:  
Este documento foi traduzido utilizando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos para garantir a precisão, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte oficial. Para informações críticas, recomenda-se a tradução profissional feita por humanos. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações equivocadas decorrentes do uso desta tradução.