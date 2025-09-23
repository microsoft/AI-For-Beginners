<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a560d5b845962cf33dc102266e409568",
  "translation_date": "2025-09-23T08:19:15+00:00",
  "source_file": "lessons/4-ComputerVision/07-ConvNets/README.md",
  "language_code": "br"
}
-->
# Redes Neurais Convolucionais

Já vimos anteriormente que redes neurais são bastante eficazes ao lidar com imagens, e até mesmo um perceptron de uma camada consegue reconhecer dígitos manuscritos do conjunto de dados MNIST com uma precisão razoável. No entanto, o conjunto de dados MNIST é muito especial, pois todos os dígitos estão centralizados na imagem, o que torna a tarefa mais simples.

## [Quiz pré-aula](https://ff-quizzes.netlify.app/en/ai/quiz/13)

Na vida real, queremos ser capazes de reconhecer objetos em uma imagem independentemente de sua localização exata. Visão computacional é diferente de classificação genérica, porque, ao tentar encontrar um determinado objeto na imagem, estamos escaneando a imagem em busca de **padrões** específicos e suas combinações. Por exemplo, ao procurar um gato, podemos primeiro buscar linhas horizontais, que podem formar os bigodes, e então uma certa combinação de bigodes pode nos indicar que se trata de uma imagem de um gato. A posição relativa e a presença de certos padrões são importantes, e não sua posição exata na imagem.

Para extrair padrões, utilizaremos o conceito de **filtros convolucionais**. Como você sabe, uma imagem é representada por uma matriz 2D ou um tensor 3D com profundidade de cor. Aplicar um filtro significa que pegamos uma matriz relativamente pequena chamada **kernel do filtro**, e para cada pixel na imagem original calculamos a média ponderada com os pontos vizinhos. Podemos imaginar isso como uma pequena janela deslizando sobre toda a imagem e calculando a média de todos os pixels de acordo com os pesos na matriz do kernel do filtro.

![Filtro de Borda Vertical](../../../../../translated_images/filter-vert.b7148390ca0bc356ddc7e55555d2481819c1e86ddde9dce4db5e71a69d6f887f.br.png) | ![Filtro de Borda Horizontal](../../../../../translated_images/filter-horiz.59b80ed4feb946efbe201a7fe3ca95abb3364e266e6fd90820cb893b4d3a6dda.br.png)
----|----

> Imagem por Dmitry Soshnikov

Por exemplo, se aplicarmos filtros de borda vertical e horizontal de 3x3 aos dígitos do MNIST, podemos destacar (por exemplo, valores altos) onde há bordas verticais e horizontais na imagem original. Assim, esses dois filtros podem ser usados para "procurar" bordas. Da mesma forma, podemos projetar diferentes filtros para buscar outros padrões de baixo nível:

<img src="images/lmfilters.jpg" width="500" align="center"/>

> Imagem do [Leung-Malik Filter Bank](https://www.robots.ox.ac.uk/~vgg/research/texclass/filters.html)

No entanto, enquanto podemos projetar filtros manualmente para extrair alguns padrões, também podemos projetar a rede de forma que ela aprenda os padrões automaticamente. Essa é uma das principais ideias por trás das CNNs.

## Principais ideias por trás das CNNs

O funcionamento das CNNs é baseado nas seguintes ideias importantes:

* Filtros convolucionais podem extrair padrões
* Podemos projetar a rede de forma que os filtros sejam treinados automaticamente
* Podemos usar a mesma abordagem para encontrar padrões em características de alto nível, não apenas na imagem original. Assim, a extração de características pelas CNNs funciona em uma hierarquia de características, começando com combinações de pixels de baixo nível até combinações de alto nível de partes da imagem.

![Extração Hierárquica de Características](../../../../../translated_images/FeatureExtractionCNN.d9b456cbdae7cb643fde3032b81b2940e3cf8be842e29afac3f482725ba7f95c.br.png)

> Imagem de [um artigo de Hislop-Lynch](https://www.semanticscholar.org/paper/Computer-vision-based-pedestrian-trajectory-Hislop-Lynch/26e6f74853fc9bbb7487b06dc2cf095d36c9021d), baseado em [sua pesquisa](https://dl.acm.org/doi/abs/10.1145/1553374.1553453)

## ✍️ Exercícios: Redes Neurais Convolucionais

Vamos continuar explorando como as redes neurais convolucionais funcionam e como podemos obter filtros treináveis, trabalhando nos notebooks correspondentes:

* [Redes Neurais Convolucionais - PyTorch](ConvNetsPyTorch.ipynb)
* [Redes Neurais Convolucionais - TensorFlow](ConvNetsTF.ipynb)

## Arquitetura de Pirâmide

A maioria das CNNs usadas para processamento de imagens segue a chamada arquitetura de pirâmide. A primeira camada convolucional aplicada às imagens originais geralmente possui um número relativamente baixo de filtros (8-16), que correspondem a diferentes combinações de pixels, como linhas horizontais/verticais ou traços. No próximo nível, reduzimos a dimensão espacial da rede e aumentamos o número de filtros, o que corresponde a mais combinações possíveis de características simples. Com cada camada, à medida que avançamos para o classificador final, as dimensões espaciais da imagem diminuem e o número de filtros aumenta.

Como exemplo, vejamos a arquitetura do VGG-16, uma rede que alcançou 92,7% de precisão na classificação top-5 do ImageNet em 2014:

![Camadas do ImageNet](../../../../../translated_images/vgg-16-arch1.d901a5583b3a51baeaab3e768567d921e5d54befa46e1e642616c5458c934028.br.jpg)

![Pirâmide do ImageNet](../../../../../translated_images/vgg-16-arch.64ff2137f50dd49fdaa786e3f3a975b3f22615efd13efb19c5d22f12e01451a1.br.jpg)

> Imagem de [Researchgate](https://www.researchgate.net/figure/Vgg16-model-structure-To-get-the-VGG-NIN-model-we-replace-the-2-nd-4-th-6-th-7-th_fig2_335194493)

## Arquiteturas de CNN Mais Conhecidas

[Continue seus estudos sobre as arquiteturas de CNN mais conhecidas](CNN_Architectures.md)

---

