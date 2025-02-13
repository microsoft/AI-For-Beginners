# Truques de Treinamento em Deep Learning

À medida que as redes neurais se tornam mais profundas, o processo de treinamento se torna cada vez mais desafiador. Um dos principais problemas é o chamado [gradientes que desaparecem](https://en.wikipedia.org/wiki/Vanishing_gradient_problem) ou [gradientes explodindo](https://deepai.org/machine-learning-glossary-and-terms/exploding-gradient-problem#:~:text=Exploding%20gradients%20are%20a%20problem,updates%20are%20small%20and%20controlled.). [Este post](https://towardsdatascience.com/the-vanishing-exploding-gradient-problem-in-deep-neural-networks-191358470c11) oferece uma boa introdução a esses problemas.

Para tornar o treinamento de redes profundas mais eficiente, existem algumas técnicas que podem ser utilizadas.

## Manter valores em intervalo razoável

Para tornar os cálculos numéricos mais estáveis, queremos garantir que todos os valores dentro de nossa rede neural estejam em uma escala razoável, tipicamente [-1..1] ou [0..1]. Não é um requisito muito rígido, mas a natureza dos cálculos em ponto flutuante é tal que valores de magnitudes diferentes não podem ser manipulados com precisão juntos. Por exemplo, se somarmos 10<sup>-10</sup> e 10<sup>10</sup>, provavelmente obteremos 10<sup>10</sup>, porque o valor menor seria "convertido" para a mesma ordem que o maior, e assim a mantissa seria perdida.

A maioria das funções de ativação tem não-linearidades em torno de [-1..1], e, portanto, faz sentido escalar todos os dados de entrada para o intervalo [-1..1] ou [0..1].

## Inicialização de Pesos

Idealmente, queremos que os valores estejam na mesma faixa após passar pelas camadas da rede. Portanto, é importante inicializar os pesos de maneira a preservar a distribuição dos valores.

A distribuição normal **N(0,1)** não é uma boa ideia, porque se tivermos *n* entradas, o desvio padrão da saída seria *n*, e os valores provavelmente sairão do intervalo [0..1].

As seguintes inicializações são frequentemente utilizadas:

 * Distribuição uniforme -- `uniform`
 * **N(0,1/n)** -- `gaussian`
 * **N(0,1/√n_in)** garante que para entradas com média zero e desvio padrão de 1, a mesma média/desvio padrão permanecerá
 * **N(0,√2/(n_in+n_out))** -- a chamada **inicialização Xavier** (`glorot`), ajuda a manter os sinais dentro da faixa durante a propagação tanto para frente quanto para trás

## Normalização em Lote

Mesmo com a inicialização adequada dos pesos, os pesos podem ficar arbitrariamente grandes ou pequenos durante o treinamento, e isso pode levar os sinais para fora da faixa adequada. Podemos trazer os sinais de volta usando uma das técnicas de **normalização**. Embora haja várias delas (Normalização de pesos, Normalização de camadas), a mais utilizada é a Normalização em Lote.

A ideia da **normalização em lote** é levar em conta todos os valores do minibatch e realizar a normalização (ou seja, subtrair a média e dividir pelo desvio padrão) com base nesses valores. Isso é implementado como uma camada de rede que realiza essa normalização após aplicar os pesos, mas antes da função de ativação. Como resultado, é provável que vejamos uma maior precisão final e um treinamento mais rápido.

Aqui está o [artigo original](https://arxiv.org/pdf/1502.03167.pdf) sobre normalização em lote, a [explicação na Wikipedia](https://en.wikipedia.org/wiki/Batch_normalization) e [um bom post introdutório no blog](https://towardsdatascience.com/batch-normalization-in-3-levels-of-understanding-14c2da90a338) (e um [em russo](https://habrahabr.ru/post/309302/)).

## Dropout

**Dropout** é uma técnica interessante que remove uma certa porcentagem de neurônios aleatórios durante o treinamento. Também é implementado como uma camada com um parâmetro (percentagem de neurônios a serem removidos, tipicamente 10%-50%), e durante o treinamento, zera elementos aleatórios do vetor de entrada, antes de passá-lo para a próxima camada.

Embora isso possa parecer uma ideia estranha, você pode ver o efeito do dropout no treinamento do classificador de dígitos MNIST no notebook [`Dropout.ipynb`](../../../../../lessons/4-ComputerVision/08-TransferLearning/Dropout.ipynb). Isso acelera o treinamento e nos permite alcançar maior precisão em menos épocas de treinamento.

Esse efeito pode ser explicado de várias maneiras:

 * Pode ser considerado um fator de choque aleatório para o modelo, que tira a otimização de um mínimo local
 * Pode ser considerado como *média implícita de modelos*, porque podemos dizer que durante o dropout estamos treinando um modelo ligeiramente diferente

> *Algumas pessoas dizem que quando uma pessoa bêbada tenta aprender algo, ela se lembrará disso melhor na manhã seguinte, em comparação com uma pessoa sóbria, porque um cérebro com alguns neurônios mal funcionando tenta se adaptar melhor para entender o significado. Nunca testamos se isso é verdade ou não.*

## Prevenindo o overfitting

Um dos aspectos muito importantes do deep learning é ser capaz de prevenir [overfitting](../../3-NeuralNetworks/05-Frameworks/Overfitting.md). Embora possa ser tentador usar um modelo de rede neural muito poderoso, devemos sempre equilibrar o número de parâmetros do modelo com o número de amostras de treinamento.

> Certifique-se de entender o conceito de [overfitting](../../3-NeuralNetworks/05-Frameworks/Overfitting.md) que introduzimos anteriormente!

Existem várias maneiras de prevenir o overfitting:

 * Parada antecipada -- monitorar continuamente o erro no conjunto de validação e interromper o treinamento quando o erro de validação começar a aumentar.
 * Decaimento de peso explícito / Regularização -- adicionar uma penalidade extra à função de perda para altos valores absolutos de pesos, o que impede o modelo de obter resultados muito instáveis
 * Média de Modelos -- treinar vários modelos e, em seguida, fazer a média dos resultados. Isso ajuda a minimizar a variância.
 * Dropout (Média Implícita de Modelos)

## Otimizadores / Algoritmos de Treinamento

Outro aspecto importante do treinamento é escolher um bom algoritmo de treinamento. Embora o clássico **gradiente descendente** seja uma escolha razoável, às vezes pode ser muito lento ou resultar em outros problemas.

Em deep learning, usamos **Descent Gradient Estocástico** (SGD), que é um gradiente descendente aplicado a minibatches, selecionados aleatoriamente do conjunto de treinamento. Os pesos são ajustados usando esta fórmula:

w<sup>t+1</sup> = w<sup>t</sup> - η∇ℒ

### Momento

No **SGD com momento**, mantemos uma parte do gradiente de passos anteriores. É semelhante a quando estamos nos movendo em algum lugar com inércia, e recebemos um golpe em uma direção diferente; nossa trajetória não muda imediatamente, mas mantém parte do movimento original. Aqui introduzimos outro vetor v para representar a *velocidade*:

* v<sup>t+1</sup> = γ v<sup>t</sup> - η∇ℒ
* w<sup>t+1</sup> = w<sup>t</sup>+v<sup>t+1</sup>

Aqui, o parâmetro γ indica a extensão em que levamos a inércia em conta: γ=0 corresponde ao SGD clássico; γ=1 é uma equação de movimento puro.

### Adam, Adagrad, etc.

Uma vez que em cada camada multiplicamos sinais por alguma matriz W<sub>i</sub>, dependendo de ||W<sub>i</sub>||, o gradiente pode tanto diminuir e se aproximar de 0, quanto aumentar indefinidamente. Essa é a essência do problema dos Gradientes Explodindo/Desaparecendo.

Uma das soluções para esse problema é usar apenas a direção do gradiente na equação e ignorar o valor absoluto, ou seja,

w<sup>t+1</sup> = w<sup>t</sup> - η(∇ℒ/||∇ℒ||), onde ||∇ℒ|| = √∑(∇ℒ)<sup>2</sup>

Esse algoritmo é chamado de **Adagrad**. Outros algoritmos que usam a mesma ideia: **RMSProp**, **Adam**.

> **Adam** é considerado um algoritmo muito eficiente para muitas aplicações, então, se você não tem certeza de qual usar - use Adam.

### Recorte de Gradiente

O recorte de gradiente é uma extensão da ideia acima. Quando ||∇ℒ|| ≤ θ, consideramos o gradiente original na otimização de pesos, e quando ||∇ℒ|| > θ - dividimos o gradiente pela sua norma. Aqui θ é um parâmetro, na maioria dos casos podemos tomar θ=1 ou θ=10.

### Decaimento da taxa de aprendizado

O sucesso do treinamento muitas vezes depende do parâmetro da taxa de aprendizado η. É lógico supor que valores maiores de η resultem em um treinamento mais rápido, que é algo que normalmente queremos no início do treinamento, e então um valor menor de η nos permite ajustar a rede. Assim, na maioria dos casos, queremos diminuir η durante o processo de treinamento.

Isso pode ser feito multiplicando η por algum número (por exemplo, 0.98) após cada época de treinamento, ou usando um **cronograma de taxa de aprendizado** mais complicado.

## Diferentes Arquiteturas de Rede

Selecionar a arquitetura de rede certa para o seu problema pode ser complicado. Normalmente, escolheríamos uma arquitetura que já se provou eficaz para nossa tarefa específica (ou uma semelhante). Aqui está uma [boa visão geral](https://www.topbots.com/a-brief-history-of-neural-network-architectures/) das arquiteturas de redes neurais para visão computacional.

> É importante selecionar uma arquitetura que seja poderosa o suficiente para o número de amostras de treinamento que temos. Selecionar um modelo muito poderoso pode resultar em [overfitting](../../3-NeuralNetworks/05-Frameworks/Overfitting.md).

Outra boa abordagem seria usar uma arquitetura que se ajuste automaticamente à complexidade necessária. Em certa medida, as arquiteturas **ResNet** e **Inception** são autoajustáveis. [Mais sobre arquiteturas de visão computacional](../07-ConvNets/CNN_Architectures.md).

**Aviso Legal**:  
Este documento foi traduzido utilizando serviços de tradução automática baseados em IA. Embora nos esforcemos pela precisão, esteja ciente de que traduções automatizadas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte autoritativa. Para informações críticas, recomenda-se a tradução profissional por um humano. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações errôneas decorrentes do uso desta tradução.