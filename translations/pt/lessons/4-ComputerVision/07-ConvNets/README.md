# Redes Neurais Convolucionais

Já vimos anteriormente que redes neurais são bastante eficazes ao lidar com imagens, e até mesmo um perceptron de uma camada é capaz de reconhecer dígitos manuscritos do conjunto de dados MNIST com uma precisão razoável. No entanto, o conjunto de dados MNIST é muito especial, e todos os dígitos estão centralizados dentro da imagem, o que torna a tarefa mais simples.

## [Quiz pré-aula](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/107)

Na vida real, queremos ser capazes de reconhecer objetos em uma imagem, independentemente de sua localização exata na imagem. A visão computacional é diferente da classificação genérica, porque quando tentamos encontrar um determinado objeto na imagem, estamos escaneando a imagem em busca de alguns **padrões** específicos e suas combinações. Por exemplo, ao procurar um gato, primeiro podemos procurar por linhas horizontais, que podem formar bigodes, e então uma combinação específica de bigodes pode nos indicar que na verdade é uma imagem de um gato. A posição relativa e a presença de certos padrões são importantes, e não sua posição exata na imagem.

Para extrair padrões, usaremos a noção de **filtros convolucionais**. Como você sabe, uma imagem é representada por uma matriz 2D ou um tensor 3D com profundidade de cor. Aplicar um filtro significa que pegamos uma matriz de **kernel de filtro** relativamente pequena, e para cada pixel na imagem original, calculamos a média ponderada com os pontos vizinhos. Podemos ver isso como uma pequena janela deslizando sobre toda a imagem, e fazendo a média de todos os pixels de acordo com os pesos na matriz do kernel de filtro.

![Filtro de Borda Vertical](../../../../../translated_images/filter-vert.b7148390ca0bc356ddc7e55555d2481819c1e86ddde9dce4db5e71a69d6f887f.pt.png) | ![Filtro de Borda Horizontal](../../../../../translated_images/filter-horiz.59b80ed4feb946efbe201a7fe3ca95abb3364e266e6fd90820cb893b4d3a6dda.pt.png)
----|----

> Imagem de Dmitry Soshnikov

Por exemplo, se aplicarmos filtros de borda vertical e horizontal 3x3 nos dígitos do MNIST, podemos obter destaques (por exemplo, valores altos) onde há bordas verticais e horizontais na nossa imagem original. Assim, esses dois filtros podem ser usados para "procurar" bordas. Da mesma forma, podemos projetar diferentes filtros para procurar outros padrões de baixo nível:
Você foi treinado com dados até outubro de 2023.

> Imagem do [Banco de Filtros Leung-Malik](https://www.robots.ox.ac.uk/~vgg/research/texclass/filters.html)

No entanto, enquanto podemos projetar os filtros para extrair alguns padrões manualmente, também podemos projetar a rede de tal forma que ela aprenda os padrões automaticamente. Essa é uma das principais ideias por trás da CNN.

## Principais ideias por trás da CNN

A forma como as CNNs funcionam é baseada nas seguintes ideias importantes:

* Filtros convolucionais podem extrair padrões
* Podemos projetar a rede de tal forma que os filtros sejam treinados automaticamente
* Podemos usar a mesma abordagem para encontrar padrões em características de alto nível, não apenas na imagem original. Assim, a extração de características da CNN trabalha em uma hierarquia de características, começando por combinações de pixels de baixo nível até combinações de partes da imagem de nível mais alto.

![Extração de Características Hierárquica](../../../../../translated_images/FeatureExtractionCNN.d9b456cbdae7cb643fde3032b81b2940e3cf8be842e29afac3f482725ba7f95c.pt.png)

> Imagem de [um artigo de Hislop-Lynch](https://www.semanticscholar.org/paper/Computer-vision-based-pedestrian-trajectory-Hislop-Lynch/26e6f74853fc9bbb7487b06dc2cf095d36c9021d), baseado em [sua pesquisa](https://dl.acm.org/doi/abs/10.1145/1553374.1553453)

## ✍️ Exercícios: Redes Neurais Convolucionais

Vamos continuar explorando como as redes neurais convolucionais funcionam e como podemos alcançar filtros treináveis, trabalhando através dos notebooks correspondentes:

* [Redes Neurais Convolucionais - PyTorch](../../../../../lessons/4-ComputerVision/07-ConvNets/ConvNetsPyTorch.ipynb)
* [Redes Neurais Convolucionais - TensorFlow](../../../../../lessons/4-ComputerVision/07-ConvNets/ConvNetsTF.ipynb)

## Arquitetura em Pirâmide

A maioria das CNNs usadas para processamento de imagens segue uma chamada arquitetura em pirâmide. A primeira camada convolucional aplicada às imagens originais geralmente tem um número relativamente baixo de filtros (8-16), que correspondem a diferentes combinações de pixels, como linhas horizontais/verticais de traços. No próximo nível, reduzimos a dimensão espacial da rede e aumentamos o número de filtros, o que corresponde a mais combinações possíveis de características simples. A cada camada, à medida que avançamos em direção ao classificador final, as dimensões espaciais da imagem diminuem e o número de filtros aumenta.

Como exemplo, vamos olhar para a arquitetura do VGG-16, uma rede que alcançou 92,7% de precisão na classificação top-5 do ImageNet em 2014:

![Camadas do ImageNet](../../../../../translated_images/vgg-16-arch1.d901a5583b3a51baeaab3e768567d921e5d54befa46e1e642616c5458c934028.pt.jpg)

![Pirâmide do ImageNet](../../../../../translated_images/vgg-16-arch.64ff2137f50dd49fdaa786e3f3a975b3f22615efd13efb19c5d22f12e01451a1.pt.jpg)

> Imagem de [Researchgate](https://www.researchgate.net/figure/Vgg16-model-structure-To-get-the-VGG-NIN-model-we-replace-the-2-nd-4-th-6-th-7-th_fig2_335194493)

## Arquiteturas de CNN Mais Conhecidas

[Continue seus estudos sobre as arquiteturas de CNN mais conhecidas](CNN_Architectures.md)

**Isenção de responsabilidade**:  
Este documento foi traduzido utilizando serviços de tradução automática baseados em IA. Embora nos esforcemos pela precisão, esteja ciente de que traduções automatizadas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte autoritativa. Para informações críticas, recomenda-se a tradução profissional por um humano. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações errôneas resultantes do uso desta tradução.