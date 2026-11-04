# Dicas para Treinamento de Deep Learning

À medida que as redes neurais se tornam mais profundas, o processo de treino torna-se cada vez mais desafiante. Um problema principal são os chamados [gradientes desaparecidos](https://en.wikipedia.org/wiki/Vanishing_gradient_problem) ou [gradientes explosivos](https://deepai.org/machine-learning-glossary-and-terms/exploding-gradient-problem#:~:text=Exploding%20gradients%20are%20a%20problem,updates%20are%20small%20and%20controlled.). [Este post](https://towardsdatascience.com/the-vanishing-exploding-gradient-problem-in-deep-neural-networks-191358470c11) dá uma boa introdução a esses problemas.

Para tornar o treino de redes profundas mais eficiente, existem algumas técnicas que podem ser usadas.

## Manter os valores num intervalo razoável

Para tornar os cálculos numéricos mais estáveis, queremos garantir que todos os valores dentro da nossa rede neural estejam numa escala razoável, tipicamente [-1..1] ou [0..1]. Não é um requisito muito estrito, mas a natureza dos cálculos em ponto flutuante é tal que valores de magnitudes diferentes não podem ser manipulados com precisão em conjunto. Por exemplo, se somarmos 10<sup>-10</sup> e 10<sup>10</sup>, provavelmente obteremos 10<sup>10</sup>, porque o valor menor será "convertido" para a mesma ordem do valor maior, e assim a mantissa será perdida.

A maioria das funções de ativação apresenta não linearidades em torno de [-1..1], pelo que faz sentido escalar todos os dados de entrada para o intervalo [-1..1] ou [0..1].

## Inicialização Inicial dos Pesos

Idealmente, queremos que os valores estejam no mesmo intervalo após passar pelas camadas da rede. Assim, é importante inicializar os pesos de forma a preservar a distribuição dos valores.

A distribuição normal **N(0,1)** não é uma boa ideia, porque se tivermos *n* entradas, o desvio padrão da saída será *&radic;n*, e os valores provavelmente sairão do intervalo [0..1].

As seguintes inicializações são frequentemente usadas:

 * Distribuição uniforme -- `uniform`
 * **N(0,1/n)** -- `gaussian`
 * **N(0,1/&radic;n_in)** garante que para entradas com média zero e desvio padrão 1 se mantenham média/ desvio padrão iguais
 * **N(0,&radic;2/(n_in+n_out))** – a chamada **inicialização Xavier** (`glorot`), ajuda a manter os sinais no intervalo durante a propagação direta e inversa

## Normalização por Lote (Batch Normalization)

Mesmo com a inicialização adequada dos pesos, os pesos podem ficar arbitrariamente grandes ou pequenos durante o treino, e vão afastar os sinais do intervalo adequado. Podemos trazer os sinais de volta usando uma das técnicas de **normalização**. Embora existam várias (Normalização de Pesos, Normalização de Camada), a mais usada é a normalização por lote.

A ideia da **normalização por lote** é considerar todos os valores através do minibatch e realizar a normalização (ou seja, subtrair a média e dividir pelo desvio padrão) com base nesses valores. É implementado como uma camada da rede que faz essa normalização após aplicar os pesos, mas antes da função de ativação. Como resultado, é provável que vejamos maior precisão final e treino mais rápido.

Aqui está o [artigo original](https://arxiv.org/pdf/1502.03167.pdf) sobre normalização por lote, a [explicação na Wikipedia](https://en.wikipedia.org/wiki/Batch_normalization), e [um bom post introdutório](https://towardsdatascience.com/batch-normalization-in-3-levels-of-understanding-14c2da90a338) (e outro [em Russo](https://habrahabr.ru/post/309302/)).

## Dropout

**Dropout** é uma técnica interessante que remove uma certa percentagem de neurónios aleatoriamente durante o treino. Também é implementado como uma camada com um parâmetro (percentagem de neurónios a remover, tipicamente 10%-50%), que durante o treino zera elementos aleatórios do vetor de entrada, antes de passar para a camada seguinte.

Embora isto possa parecer uma ideia estranha, pode ver o efeito do dropout no treino de um classificador de dígitos MNIST no notebook [`Dropout.ipynb`](Dropout.ipynb). Acelera o treino e permite atingir maior precisão em menos épocas de treino.

Este efeito pode ser explicado de várias maneiras:

 * Pode ser considerado como um fator de choque aleatório para o modelo, que tira a otimização de mínimos locais
 * Pode ser considerado como *média implícita do modelo*, porque durante o dropout estamos a treinar um modelo ligeiramente diferente

> *Algumas pessoas dizem que quando uma pessoa bêbeda tenta aprender algo, vai lembrar-se melhor na manhã seguinte, comparado com uma pessoa sóbria, porque o cérebro com alguns neurónios com mau funcionamento tenta adaptar-se melhor para captar o significado. Nunca testámos se isto é verdade ou não.*

## Prevenir Overfitting

Um aspeto muito importante do deep learning é conseguir prevenir o [overfitting](../../3-NeuralNetworks/05-Frameworks/Overfitting.md). Embora possa ser tentador usar um modelo de rede neural muito poderoso, devemos sempre equilibrar o número de parâmetros do modelo com o número de amostras de treino.

> Certifique-se de que entende o conceito de [overfitting](../../3-NeuralNetworks/05-Frameworks/Overfitting.md) que introduzimos anteriormente!

Existem várias formas de prevenir o overfitting:

 * Paragem precoce – monitorizar continuamente o erro no conjunto de validação e parar o treino quando o erro de validação começar a aumentar.
 * Decaimento Explícito de Pesos / Regularização – adicionar um penalizador extra à função de perda para valores absolutos altos de pesos, o que evita que o modelo obtenha resultados muito instáveis
 * Média do Modelo – treinar vários modelos e depois fazer a média do resultado. Isto ajuda a minimizar a variância.
 * Dropout (Média Implicita do Modelo)

## Otimizadores / Algoritmos de Treino

Outro aspeto importante do treino é escolher um bom algoritmo de treino. Embora o clássico **gradiente descendente** seja uma escolha razoável, pode por vezes ser muito lento ou causar outros problemas.

No deep learning, usamos o **Gradiente Descendente Estocástico** (SGD), que é o gradiente descendente aplicado a minibatches, selecionados aleatoriamente do conjunto de treino. Os pesos são ajustados usando esta fórmula:

w<sup>t+1</sup> = w<sup>t</sup> - &eta;&nabla;&lagran;

### Momento

Em **momentum SGD**, mantemos uma parcela do gradiente das etapas anteriores. É semelhante a quando nos movemos com inércia e recebemos um golpe numa direção diferente, a nossa trajetória não muda imediatamente, mas mantém parte do movimento original. Aqui introduzimos outro vetor v para representar a *velocidade*:

* v<sup>t+1</sup> = &gamma; v<sup>t</sup> - &eta;&nabla;&lagran;
* w<sup>t+1</sup> = w<sup>t</sup> + v<sup>t+1</sup>

Aqui o parâmetro &gamma; indica a medida do quanto consideramos a inércia: &gamma;=0 corresponde ao SGD clássico; &gamma;=1 é uma equação pura de movimento.

### Adam, Adagrad, etc.

Como em cada camada multiplicamos os sinais por alguma matriz W<sub>i</sub>, dependendo de ||W<sub>i</sub>||, o gradiente pode ou diminuir e aproximar-se de 0, ou crescer indefinidamente. Esta é a essência do problema dos Gradientes Explosivos/Desaparecidos.

Uma das soluções para este problema é usar apenas a direção do gradiente na equação, ignorando o valor absoluto, ou seja,

w<sup>t+1</sup> = w<sup>t</sup> - &eta;(&nabla;&lagran;/||&nabla;&lagran;||), onde ||&nabla;&lagran;|| = &radic;&sum;(&nabla;&lagran;)<sup>2</sup>

Este algoritmo chama-se **Adagrad**. Outros algoritmos que usam a mesma ideia: **RMSProp**, **Adam**

> **Adam** é considerado um algoritmo muito eficiente para muitas aplicações, por isso se não tem certeza qual usar – use Adam.

### Recorte de gradiente

O recorte de gradiente é uma extensão da ideia acima. Quando ||&nabla;&lagran;|| &le; &theta;, consideramos o gradiente original na otimização dos pesos, e quando ||&nabla;&lagran;|| > &theta; – dividimos o gradiente pelo seu norma. Aqui &theta; é um parâmetro, na maioria dos casos podemos usar &theta;=1 ou &theta;=10.

### Decaimento da taxa de aprendizagem

O sucesso do treino muitas vezes depende do parâmetro da taxa de aprendizagem &eta;. É lógico assumir que valores maiores de &eta; resultam em treino mais rápido, algo que tipicamente queremos no início do treino, e depois valores mais pequenos de &eta; permitem-nos ajustar finamente a rede. Assim, na maioria dos casos queremos diminuir &eta; durante o treino.

Isto pode ser feito multiplicando &eta; por algum número (ex. 0.98) após cada época de treino, ou usando um **esquema de taxa de aprendizagem** mais complexo.

## Diferentes Arquiteturas de Rede

Escolher a arquitetura correta para o seu problema pode ser complicado. Normalmente, escolheríamos uma arquitetura que já provou funcionar para a nossa tarefa específica (ou similar). Aqui está uma [boa visão geral](https://www.topbots.com/a-brief-history-of-neural-network-architectures/) das arquiteturas de redes neurais para visão computacional.

> É importante selecionar uma arquitetura que seja suficientemente poderosa para o número de amostras de treino que temos. Escolher um modelo demasiado poderoso pode resultar em [overfitting](../../3-NeuralNetworks/05-Frameworks/Overfitting.md)

Outra boa opção é usar uma arquitetura que se ajuste automaticamente à complexidade necessária. Até certo ponto, as arquiteturas **ResNet** e **Inception** são autoajustáveis. [Mais sobre arquiteturas de visão computacional](../07-ConvNets/CNN_Architectures.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Aviso Legal**:
Este documento foi traduzido utilizando o serviço de tradução automática [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos pela precisão, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original na sua língua nativa deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas resultantes da utilização desta tradução.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->