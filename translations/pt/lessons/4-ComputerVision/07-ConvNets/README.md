<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "088837b42b7d99198bf62db8a42411e0",
  "translation_date": "2025-08-24T08:59:41+00:00",
  "source_file": "lessons/4-ComputerVision/07-ConvNets/README.md",
  "language_code": "pt"
}
-->
# Redes Neuronais Convolucionais

Já vimos anteriormente que as redes neuronais são bastante eficazes a lidar com imagens, e até mesmo um perceptron de uma camada consegue reconhecer dígitos manuscritos do conjunto de dados MNIST com uma precisão razoável. No entanto, o conjunto de dados MNIST é muito especial, pois todos os dígitos estão centrados na imagem, o que torna a tarefa mais simples.

## [Questionário pré-aula](https://ff-quizzes.netlify.app/en/ai/quiz/13)

Na vida real, queremos ser capazes de reconhecer objetos numa imagem independentemente da sua localização exata. A visão computacional é diferente da classificação genérica, porque, ao tentar encontrar um determinado objeto na imagem, estamos a analisar a imagem em busca de **padrões** específicos e suas combinações. Por exemplo, ao procurar um gato, podemos começar por procurar linhas horizontais, que podem formar os bigodes, e depois uma certa combinação de bigodes pode indicar que se trata de uma imagem de um gato. A posição relativa e a presença de certos padrões são importantes, e não a sua posição exata na imagem.

Para extrair padrões, utilizaremos o conceito de **filtros convolucionais**. Como sabemos, uma imagem é representada por uma matriz 2D ou um tensor 3D com profundidade de cor. Aplicar um filtro significa que usamos uma matriz relativamente pequena chamada **kernel do filtro**, e para cada pixel na imagem original calculamos a média ponderada com os pontos vizinhos. Podemos imaginar isto como uma pequena janela que desliza sobre toda a imagem, calculando a média de todos os pixels de acordo com os pesos na matriz kernel do filtro.

![Filtro de Borda Vertical](../../../../../lessons/4-ComputerVision/07-ConvNets/images/filter-vert.png) | ![Filtro de Borda Horizontal](../../../../../lessons/4-ComputerVision/07-ConvNets/images/filter-horiz.png)
----|----

> Imagem por Dmitry Soshnikov

Por exemplo, se aplicarmos filtros de borda vertical e horizontal de 3x3 aos dígitos do MNIST, podemos destacar (por exemplo, valores altos) onde há bordas verticais e horizontais na imagem original. Assim, esses dois filtros podem ser usados para "procurar" bordas. Da mesma forma, podemos projetar diferentes filtros para procurar outros padrões de baixo nível:

> Imagem do [Leung-Malik Filter Bank](https://www.robots.ox.ac.uk/~vgg/research/texclass/filters.html)

No entanto, embora possamos projetar os filtros manualmente para extrair alguns padrões, também podemos projetar a rede de forma que ela aprenda os padrões automaticamente. Esta é uma das principais ideias por trás das CNNs.

## Ideias principais por trás das CNNs

O funcionamento das CNNs baseia-se nas seguintes ideias importantes:

* Filtros convolucionais podem extrair padrões
* Podemos projetar a rede de forma que os filtros sejam treinados automaticamente
* Podemos usar a mesma abordagem para encontrar padrões em características de alto nível, não apenas na imagem original. Assim, a extração de características nas CNNs funciona numa hierarquia de características, começando por combinações de pixels de baixo nível até combinações de partes da imagem de nível mais alto.

![Extração Hierárquica de Características](../../../../../lessons/4-ComputerVision/07-ConvNets/images/FeatureExtractionCNN.png)

> Imagem de [um artigo de Hislop-Lynch](https://www.semanticscholar.org/paper/Computer-vision-based-pedestrian-trajectory-Hislop-Lynch/26e6f74853fc9bbb7487b06dc2cf095d36c9021d), baseado na [sua pesquisa](https://dl.acm.org/doi/abs/10.1145/1553374.1553453)

## ✍️ Exercícios: Redes Neuronais Convolucionais

Vamos continuar a explorar como funcionam as redes neuronais convolucionais e como podemos obter filtros treináveis, trabalhando nos notebooks correspondentes:

* [Redes Neuronais Convolucionais - PyTorch](../../../../../lessons/4-ComputerVision/07-ConvNets/ConvNetsPyTorch.ipynb)
* [Redes Neuronais Convolucionais - TensorFlow](../../../../../lessons/4-ComputerVision/07-ConvNets/ConvNetsTF.ipynb)

## Arquitetura em Pirâmide

A maioria das CNNs utilizadas para processamento de imagens segue uma arquitetura chamada de pirâmide. A primeira camada convolucional aplicada às imagens originais geralmente tem um número relativamente baixo de filtros (8-16), que correspondem a diferentes combinações de pixels, como linhas horizontais/verticais ou traços. No nível seguinte, reduzimos a dimensão espacial da rede e aumentamos o número de filtros, o que corresponde a mais combinações possíveis de características simples. Com cada camada, à medida que avançamos para o classificador final, as dimensões espaciais da imagem diminuem e o número de filtros aumenta.

Como exemplo, vejamos a arquitetura do VGG-16, uma rede que alcançou 92,7% de precisão na classificação top-5 do ImageNet em 2014:

![Camadas do ImageNet](../../../../../lessons/4-ComputerVision/07-ConvNets/images/vgg-16-arch1.jpg)

![Pirâmide do ImageNet](../../../../../lessons/4-ComputerVision/07-ConvNets/images/vgg-16-arch.jpg)

> Imagem de [Researchgate](https://www.researchgate.net/figure/Vgg16-model-structure-To-get-the-VGG-NIN-model-we-replace-the-2-nd-4-th-6-th-7-th_fig2_335194493)

## Arquiteturas de CNN Mais Conhecidas

[Continue o seu estudo sobre as arquiteturas de CNN mais conhecidas](CNN_Architectures.md)

**Aviso Legal**:  
Este documento foi traduzido utilizando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos para garantir a precisão, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original na sua língua nativa deve ser considerado a fonte autoritária. Para informações críticas, recomenda-se a tradução profissional realizada por humanos. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes do uso desta tradução.