# Truques para Treinamento em Deep Learning

Conforme as redes neurais ficam mais profundas, o processo de treinamento delas se torna cada vez mais desafiador. Um grande problema são os chamados [gradientes que desaparecem](https://en.wikipedia.org/wiki/Vanishing_gradient_problem) ou [gradientes que explodem](https://deepai.org/machine-learning-glossary-and-terms/exploding-gradient-problem#:~:text=Exploding%20gradients%20are%20a%20problem,updates%20are%20small%20and%20controlled.). [Este post](https://towardsdatascience.com/the-vanishing-exploding-gradient-problem-in-deep-neural-networks-191358470c11) oferece uma boa introdução a esses problemas.

Para tornar o treinamento de redes profundas mais eficiente, existem algumas técnicas que podem ser utilizadas.

## Manter valores em um intervalo razoável

Para tornar os cálculos numéricos mais estáveis, queremos garantir que todos os valores dentro da nossa rede neural estejam dentro de uma escala razoável, tipicamente [-1..1] ou [0..1]. Não é um requisito muito rígido, mas a natureza dos cálculos em ponto flutuante é tal que valores de magnitudes diferentes não podem ser manipulados com precisão juntos. Por exemplo, se somarmos 10<sup>-10</sup> e 10<sup>10</sup>, provavelmente obteremos 10<sup>10</sup>, porque o valor menor seria "convertido" para a mesma ordem do maior, e assim a mantissa seria perdida.

A maioria das funções de ativação tem não-linearidades em torno de [-1..1], portanto faz sentido escalar todos os dados de entrada para o intervalo [-1..1] ou [0..1].

## Inicialização Inicial dos Pesos

Idealmente, queremos que os valores fiquem na mesma faixa após passarem pelas camadas da rede. Portanto, é importante inicializar os pesos de maneira a preservar a distribuição dos valores.

A distribuição normal **N(0,1)** não é uma boa ideia, porque se temos *n* entradas, o desvio padrão da saída seria *&radic;n*, e os valores provavelmente sairão do intervalo [0..1].

As seguintes inicializações são frequentemente usadas:

 * Distribuição uniforme -- `uniform`
 * **N(0,1/n)** -- `gaussian`
 * **N(0,1/&radic;n_in)** garante que para entradas com média zero e desvio padrão 1, a mesma média/desvio padrão permaneça
 * **N(0,&radic;2/(n_in+n_out))** -- chamada **inicialização Xavier** (`glorot`), ajuda a manter os sinais na faixa durante a propagação direta e reversa

## Normalização em Lote

Mesmo com a inicialização adequada dos pesos, eles podem crescer muito ou diminuir muito durante o treinamento, trazendo os sinais para fora da faixa apropriada. Podemos trazer os sinais de volta usando uma das técnicas de **normalização**. Embora haja várias (Normalização de Peso, Normalização de Camada), a mais usada é a Normalização em Lote.

A ideia da **normalização em lote** é levar em conta todos os valores no minibatch e realizar a normalização (ou seja, subtrair a média e dividir pelo desvio padrão) com base nesses valores. Ela é implementada como uma camada da rede que faz essa normalização após a aplicação dos pesos, mas antes da função de ativação. Como resultado, provavelmente veremos maior precisão final e treinamento mais rápido.

Aqui está o [artigo original](https://arxiv.org/pdf/1502.03167.pdf) sobre normalização em lote, a [explicação na Wikipedia](https://en.wikipedia.org/wiki/Batch_normalization) e [um bom post introdutório no blog](https://towardsdatascience.com/batch-normalization-in-3-levels-of-understanding-14c2da90a338) (e outro [em russo](https://habrahabr.ru/post/309302/)).

## Dropout

**Dropout** é uma técnica interessante que remove uma certa porcentagem de neurônios aleatórios durante o treinamento. Também é implementado como uma camada com um parâmetro (percentual de neurônios a remover, tipicamente 10%-50%), e durante o treinamento ele zera elementos aleatórios do vetor de entrada antes de passá-lo para a próxima camada.

Embora isso possa parecer uma ideia estranha, você pode ver o efeito do dropout no treinamento de um classificador de dígitos MNIST no notebook [`Dropout.ipynb`](Dropout.ipynb). Ele acelera o treinamento e nos permite alcançar maior precisão em menos épocas de treinamento.

Esse efeito pode ser explicado de várias formas:

 * Pode ser considerado um fator de choque aleatório para o modelo, que tira a otimização de mínimos locais
 * Pode ser considerado uma *média implícita do modelo*, porque podemos dizer que durante o dropout estamos treinando um modelo ligeiramente diferente

> *Algumas pessoas dizem que quando uma pessoa bêbada tenta aprender algo, ela se lembra melhor no dia seguinte em comparação a uma pessoa sóbria, porque um cérebro com alguns neurônios com mau funcionamento tenta se adaptar melhor para captar o significado. Nós nunca testamos nós mesmos se isso é verdade ou não*

## Prevenção de overfitting

Um dos aspectos muito importantes do deep learning é ser capaz de prevenir o [overfitting](../../3-NeuralNetworks/05-Frameworks/Overfitting.md). Embora possa ser tentador usar um modelo de rede neural muito poderoso, sempre devemos equilibrar o número de parâmetros do modelo com o número de amostras de treinamento.

> Certifique-se de entender o conceito de [overfitting](../../3-NeuralNetworks/05-Frameworks/Overfitting.md) que apresentamos anteriormente!

Existem várias maneiras de prevenir o overfitting:

 * Parada antecipada (early stopping) -- monitorar continuamente o erro no conjunto de validação e parar o treinamento quando o erro de validação começar a aumentar.
 * Decaimento explícito do peso / Regularização -- adicionar uma penalidade extra à função de perda para pesos com valores absolutos altos, o que previne que o modelo se torne muito instável
 * Média de modelos -- treinar vários modelos e então fazer a média do resultado. Isso ajuda a minimizar a variância.
 * Dropout (média implícita do modelo)

## Otimizadores / Algoritmos de Treinamento

Outro aspecto importante do treinamento é escolher um bom algoritmo de treinamento. Embora o clássico **gradiente descendente** seja uma escolha razoável, às vezes pode ser lento demais ou resultar em outros problemas.

Em deep learning, usamos o **Gradiente Descendente Estocástico** (SGD), que é o gradiente descendente aplicado a minibatches, selecionados aleatoriamente do conjunto de treinamento. Os pesos são ajustados usando esta fórmula:

w<sup>t+1</sup> = w<sup>t</sup> - &eta;&nabla;&lagran;

### Momentum

No **momentum SGD**, mantemos uma porção do gradiente dos passos anteriores. É semelhante a quando estamos nos movendo com inércia e recebemos um golpe em uma direção diferente, nossa trajetória não muda imediatamente, mas mantém parte do movimento original. Aqui introduzimos outro vetor v para representar a *velocidade*:

* v<sup>t+1</sup> = &gamma; v<sup>t</sup> - &eta;&nabla;&lagran;
* w<sup>t+1</sup> = w<sup>t</sup>+v<sup>t+1</sup>

Aqui o parâmetro &gamma; indica em que medida levamos a inércia em conta: &gamma;=0 corresponde ao SGD clássico; &gamma;=1 é uma equação de movimento puro.

### Adam, Adagrad, etc.

Como em cada camada multiplicamos sinais por alguma matriz W<sub>i</sub>, dependendo de ||W<sub>i</sub>||, o gradiente pode tanto diminuir e ficar próximo de zero, quanto aumentar indefinidamente. Essa é a essência do problema dos Gradientes Explodindo/Desaparecendo.

Uma das soluções para esse problema é usar apenas a direção do gradiente na equação e ignorar o valor absoluto, ou seja,

w<sup>t+1</sup> = w<sup>t</sup> - &eta;(&nabla;&lagran;/||&nabla;&lagran;||), onde ||&nabla;&lagran;|| = &radic;&sum;(&nabla;&lagran;)<sup>2</sup>

Esse algoritmo é chamado **Adagrad**. Outros algoritmos que usam a mesma ideia: **RMSProp**, **Adam**

> **Adam** é considerado um algoritmo muito eficiente para muitas aplicações, então se você não tiver certeza de qual usar - use Adam.

### Clipping de gradiente

Clipping de gradiente é uma extensão da ideia acima. Quando ||&nabla;&lagran;|| &le; &theta;, consideramos o gradiente original na otimização dos pesos, e quando ||&nabla;&lagran;|| > &theta; - dividimos o gradiente pela sua norma. Aqui &theta; é um parâmetro, na maioria dos casos podemos usar &theta;=1 ou &theta;=10.

### Decaimento da taxa de aprendizado

O sucesso do treinamento frequentemente depende do parâmetro da taxa de aprendizado &eta;. É lógico assumir que valores maiores de &eta; resultam em treinamento mais rápido, algo que normalmente queremos no início do treinamento, e então um valor menor de &eta; nos permite ajustar finamente a rede. Portanto, na maioria dos casos queremos diminuir &eta; durante o processo de treinamento.

Isso pode ser feito multiplicando &eta; por algum número (exemplo, 0.98) após cada época de treinamento, ou usando um **cronograma de taxa de aprendizado** mais complicado.

## Diferentes Arquiteturas de Rede

Escolher a arquitetura certa de rede para seu problema pode ser complicado. Normalmente, escolheríamos uma arquitetura que tenha provado funcionar para nossa tarefa específica (ou similar). Aqui está uma [boa visão geral](https://www.topbots.com/a-brief-history-of-neural-network-architectures/) de arquiteturas de redes neurais para visão computacional.

> É importante selecionar uma arquitetura que seja poderosa o suficiente para o número de amostras de treinamento que temos. Selecionar um modelo muito poderoso pode resultar em [overfitting](../../3-NeuralNetworks/05-Frameworks/Overfitting.md)

Outra boa forma seria usar uma arquitetura que se ajuste automaticamente à complexidade requerida. Até certo ponto, as arquiteturas **ResNet** e **Inception** são autoajustáveis. [Mais sobre arquiteturas para visão computacional](../07-ConvNets/CNN_Architectures.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Aviso Legal**:
Este documento foi traduzido usando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos pela precisão, por favor, esteja ciente de que traduções automatizadas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes do uso desta tradução.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->