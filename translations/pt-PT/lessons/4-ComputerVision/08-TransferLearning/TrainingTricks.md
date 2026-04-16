# Truques para Treino em Deep Learning

À medida que as redes neurais se tornam mais profundas, o processo de treino torna-se cada vez mais desafiador. Um dos principais problemas é o chamado [vanishing gradients](https://en.wikipedia.org/wiki/Vanishing_gradient_problem) ou [exploding gradients](https://deepai.org/machine-learning-glossary-and-terms/exploding-gradient-problem#:~:text=Exploding%20gradients%20are%20a%20problem,updates%20are%20small%20and%20controlled.). [Este artigo](https://towardsdatascience.com/the-vanishing-exploding-gradient-problem-in-deep-neural-networks-191358470c11) oferece uma boa introdução a esses problemas.

Para tornar o treino de redes profundas mais eficiente, existem algumas técnicas que podem ser utilizadas.

## Manter valores num intervalo razoável

Para tornar os cálculos numéricos mais estáveis, é importante garantir que todos os valores dentro da rede neural estejam numa escala razoável, tipicamente [-1..1] ou [0..1]. Não é um requisito muito rígido, mas a natureza dos cálculos em ponto flutuante é tal que valores de magnitudes diferentes não podem ser manipulados com precisão juntos. Por exemplo, se somarmos 10<sup>-10</sup> e 10<sup>10</sup>, é provável que obtenhamos 10<sup>10</sup>, porque o valor menor seria "convertido" para a mesma ordem do maior, e assim a mantissa seria perdida.

A maioria das funções de ativação tem não-linearidades em torno de [-1..1], e por isso faz sentido escalar todos os dados de entrada para o intervalo [-1..1] ou [0..1].

## Inicialização de Pesos

Idealmente, queremos que os valores permaneçam na mesma faixa após passarem pelas camadas da rede. Assim, é importante inicializar os pesos de forma a preservar a distribuição dos valores.

A distribuição normal **N(0,1)** não é uma boa ideia, porque se tivermos *n* entradas, o desvio padrão da saída seria *n*, e os valores provavelmente sairão do intervalo [0..1].

As seguintes inicializações são frequentemente utilizadas:

 * Distribuição uniforme -- `uniform`
 * **N(0,1/n)** -- `gaussian`
 * **N(0,1/√n_in)** garante que para entradas com média zero e desvio padrão de 1, a mesma média/desvio padrão será mantida
 * **N(0,√2/(n_in+n_out))** -- chamada **Xavier initialization** (`glorot`), ajuda a manter os sinais na faixa durante a propagação direta e reversa

## Normalização por Lote

Mesmo com uma inicialização adequada dos pesos, estes podem ficar arbitrariamente grandes ou pequenos durante o treino, levando os sinais para fora da faixa apropriada. Podemos trazer os sinais de volta utilizando uma das técnicas de **normalização**. Embora existam várias delas (Normalização de Pesos, Normalização de Camadas), a mais utilizada é a Normalização por Lote.

A ideia da **normalização por lote** é considerar todos os valores do minibatch e realizar a normalização (ou seja, subtrair a média e dividir pelo desvio padrão) com base nesses valores. É implementada como uma camada na rede que realiza essa normalização após aplicar os pesos, mas antes da função de ativação. Como resultado, é provável que se obtenha maior precisão final e treino mais rápido.

Aqui está o [artigo original](https://arxiv.org/pdf/1502.03167.pdf) sobre normalização por lote, a [explicação na Wikipedia](https://en.wikipedia.org/wiki/Batch_normalization), e [um bom artigo introdutório](https://towardsdatascience.com/batch-normalization-in-3-levels-of-understanding-14c2da90a338) (e outro [em russo](https://habrahabr.ru/post/309302/)).

## Dropout

**Dropout** é uma técnica interessante que remove uma certa percentagem de neurónios aleatórios durante o treino. É implementada como uma camada com um parâmetro (percentagem de neurónios a remover, tipicamente 10%-50%), e durante o treino zera elementos aleatórios do vetor de entrada antes de passá-lo para a próxima camada.

Embora possa parecer uma ideia estranha, pode-se observar o efeito do dropout no treino de um classificador de dígitos MNIST no notebook [`Dropout.ipynb`](../../../../../lessons/4-ComputerVision/08-TransferLearning/Dropout.ipynb). Ele acelera o treino e permite alcançar maior precisão em menos épocas de treino.

Este efeito pode ser explicado de várias formas:

 * Pode ser considerado como um fator de choque aleatório para o modelo, que o tira de mínimos locais
 * Pode ser considerado como *média implícita de modelos*, porque durante o dropout estamos a treinar modelos ligeiramente diferentes

> *Algumas pessoas dizem que quando uma pessoa bêbada tenta aprender algo, ela lembra-se melhor no dia seguinte, comparando com uma pessoa sóbria, porque um cérebro com alguns neurónios a funcionar mal tenta adaptar-se melhor para captar o significado. Nunca testámos se isto é verdade ou não.*

## Prevenir overfitting

Um dos aspetos muito importantes do deep learning é ser capaz de prevenir o [overfitting](../../3-NeuralNetworks/05-Frameworks/Overfitting.md). Embora possa ser tentador usar um modelo de rede neural muito poderoso, devemos sempre equilibrar o número de parâmetros do modelo com o número de amostras de treino.

> Certifique-se de que compreende o conceito de [overfitting](../../3-NeuralNetworks/05-Frameworks/Overfitting.md) que introduzimos anteriormente!

Existem várias formas de prevenir o overfitting:

 * Paragem antecipada -- monitorizar continuamente o erro no conjunto de validação e parar o treino quando o erro de validação começar a aumentar.
 * Decaimento explícito de pesos / Regularização -- adicionar uma penalização extra à função de perda para valores absolutos altos de pesos, o que previne resultados muito instáveis no modelo
 * Média de Modelos -- treinar vários modelos e depois fazer a média dos resultados. Isto ajuda a minimizar a variância.
 * Dropout (Média Implícita de Modelos)

## Otimizadores / Algoritmos de Treino

Outro aspeto importante do treino é escolher um bom algoritmo de treino. Embora o **gradient descent** clássico seja uma escolha razoável, pode por vezes ser demasiado lento ou resultar em outros problemas.

Em deep learning, utilizamos **Stochastic Gradient Descent** (SGD), que é um gradient descent aplicado a minibatches, selecionados aleatoriamente do conjunto de treino. Os pesos são ajustados utilizando esta fórmula:

w<sup>t+1</sup> = w<sup>t</sup> - η∇ℒ

### Momentum

No **momentum SGD**, mantemos uma parte do gradiente dos passos anteriores. É semelhante a quando nos movemos com inércia e recebemos um empurrão numa direção diferente; a nossa trajetória não muda imediatamente, mas mantém parte do movimento original. Aqui introduzimos outro vetor v para representar a *velocidade*:

* v<sup>t+1</sup> = γ v<sup>t</sup> - η∇ℒ
* w<sup>t+1</sup> = w<sup>t</sup>+v<sup>t+1</sup>

Aqui o parâmetro γ indica até que ponto consideramos a inércia: γ=0 corresponde ao SGD clássico; γ=1 é uma equação de movimento puro.

### Adam, Adagrad, etc.

Como em cada camada multiplicamos os sinais por uma matriz W<sub>i</sub>, dependendo de ||W<sub>i</sub>||, o gradiente pode diminuir e ser próximo de 0, ou crescer indefinidamente. Este é o cerne do problema de Exploding/Vanishing Gradients.

Uma das soluções para este problema é usar apenas a direção do gradiente na equação e ignorar o valor absoluto, ou seja:

w<sup>t+1</sup> = w<sup>t</sup> - η(∇ℒ/||∇ℒ||), onde ||∇ℒ|| = √∑(∇ℒ)<sup>2</sup>

Este algoritmo é chamado **Adagrad**. Outros algoritmos que utilizam a mesma ideia: **RMSProp**, **Adam**

> **Adam** é considerado um algoritmo muito eficiente para muitas aplicações, por isso, se não tiver certeza de qual usar - use Adam.

### Gradient clipping

Gradient clipping é uma extensão da ideia acima. Quando ||∇ℒ|| ≤ θ, consideramos o gradiente original na otimização dos pesos, e quando ||∇ℒ|| > θ - dividimos o gradiente pela sua norma. Aqui θ é um parâmetro; na maioria dos casos podemos usar θ=1 ou θ=10.

### Decaimento da taxa de aprendizagem

O sucesso do treino muitas vezes depende do parâmetro de taxa de aprendizagem η. É lógico assumir que valores maiores de η resultam em treino mais rápido, algo que normalmente queremos no início do treino, e depois valores menores de η permitem ajustar melhor a rede. Assim, na maioria dos casos queremos diminuir η durante o processo de treino.

Isto pode ser feito multiplicando η por um número (ex. 0.98) após cada época de treino, ou utilizando um **cronograma de taxa de aprendizagem** mais complicado.

## Diferentes Arquiteturas de Redes

Selecionar a arquitetura certa para o seu problema pode ser complicado. Normalmente, escolhemos uma arquitetura que já tenha demonstrado funcionar para a nossa tarefa específica (ou uma semelhante). Aqui está uma [boa visão geral](https://www.topbots.com/a-brief-history-of-neural-network-architectures/) de arquiteturas de redes neurais para visão computacional.

> É importante selecionar uma arquitetura que seja suficientemente poderosa para o número de amostras de treino que temos. Escolher um modelo demasiado poderoso pode resultar em [overfitting](../../3-NeuralNetworks/05-Frameworks/Overfitting.md).

Outra boa abordagem seria usar uma arquitetura que se ajuste automaticamente à complexidade necessária. Até certo ponto, as arquiteturas **ResNet** e **Inception** são autoajustáveis. [Mais sobre arquiteturas de visão computacional](../07-ConvNets/CNN_Architectures.md)

**Aviso Legal**:  
Este documento foi traduzido utilizando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos para garantir a precisão, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original no seu idioma nativo deve ser considerado a fonte autoritativa. Para informações críticas, recomenda-se a tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas resultantes do uso desta tradução.