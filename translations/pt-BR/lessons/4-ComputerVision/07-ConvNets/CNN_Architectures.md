# Arquiteturas Conhecidas de CNN

### VGG-16

VGG-16 é uma rede que alcançou 92,7% de precisão na classificação top-5 do ImageNet em 2014. Ela possui a seguinte estrutura de camadas:

![Camadas do ImageNet](../../../../../translated_images/pt-BR/vgg-16-arch1.d901a5583b3a51ba.webp)

Como você pode ver, a VGG segue uma arquitetura tradicional em forma de pirâmide, que é uma sequência de camadas de convolução e pooling.

![Pirâmide do ImageNet](../../../../../translated_images/pt-BR/vgg-16-arch.64ff2137f50dd49f.webp)

> Imagem de [Researchgate](https://www.researchgate.net/figure/Vgg16-model-structure-To-get-the-VGG-NIN-model-we-replace-the-2-nd-4-th-6-th-7-th_fig2_335194493)

### ResNet

ResNet é uma família de modelos proposta pela Microsoft Research em 2015. A ideia principal da ResNet é usar **blocos residuais**:

<img src="../../../../../translated_images/pt-BR/resnet-block.aba4ccbcc0944434.webp" width="300"/>

> Imagem deste [artigo](https://arxiv.org/pdf/1512.03385.pdf)

A razão para usar a passagem de identidade é fazer com que nossa camada preveja **a diferença** entre o resultado de uma camada anterior e a saída do bloco residual - daí o nome *residual*. Esses blocos são muito mais fáceis de treinar, e é possível construir redes com centenas desses blocos (as variantes mais comuns são ResNet-52, ResNet-101 e ResNet-152).

Você também pode pensar nessa rede como sendo capaz de ajustar sua complexidade ao conjunto de dados. Inicialmente, quando você começa a treinar a rede, os valores dos pesos são pequenos, e a maior parte do sinal passa pelas camadas de identidade. À medida que o treinamento avança e os pesos se tornam maiores, a importância dos parâmetros da rede cresce, e a rede se ajusta para acomodar o poder expressivo necessário para classificar corretamente as imagens de treinamento.

### Google Inception

A arquitetura Google Inception leva essa ideia um passo adiante e constrói cada camada da rede como uma combinação de vários caminhos diferentes:

<img src="../../../../../translated_images/pt-BR/inception.a6605b85bcbc6f52.webp" width="400"/>

> Imagem de [Researchgate](https://www.researchgate.net/figure/Inception-module-with-dimension-reductions-left-and-schema-for-Inception-ResNet-v1_fig2_355547454)

Aqui, precisamos enfatizar o papel das convoluções 1x1, porque, à primeira vista, elas não fazem sentido. Por que precisaríamos passar pela imagem com um filtro 1x1? No entanto, é importante lembrar que os filtros de convolução também trabalham com vários canais de profundidade (originalmente - cores RGB, em camadas subsequentes - canais para diferentes filtros), e a convolução 1x1 é usada para misturar esses canais de entrada usando diferentes pesos treináveis. Ela também pode ser vista como uma redução de dimensão (pooling) sobre a dimensão dos canais.

Aqui está [um bom post de blog](https://medium.com/analytics-vidhya/talented-mr-1x1-comprehensive-look-at-1x1-convolution-in-deep-learning-f6b355825578) sobre o assunto, e [o artigo original](https://arxiv.org/pdf/1312.4400.pdf).

### MobileNet

MobileNet é uma família de modelos com tamanho reduzido, adequada para dispositivos móveis. Use-os se você tiver poucos recursos e puder sacrificar um pouco de precisão. A ideia principal por trás deles é a chamada **convolução separável por profundidade**, que permite representar filtros de convolução por uma composição de convoluções espaciais e convolução 1x1 sobre canais de profundidade. Isso reduz significativamente o número de parâmetros, tornando a rede menor em tamanho e também mais fácil de treinar com menos dados.

Aqui está [um bom post de blog sobre MobileNet](https://medium.com/analytics-vidhya/image-classification-with-mobilenet-cc6fbb2cd470).

## Conclusão

Nesta unidade, você aprendeu o conceito principal por trás das redes neurais de visão computacional - redes convolucionais. Arquiteturas reais que alimentam classificação de imagens, detecção de objetos e até redes de geração de imagens são todas baseadas em CNNs, apenas com mais camadas e alguns truques adicionais de treinamento.

## 🚀 Desafio

Nos notebooks que acompanham, há notas no final sobre como obter maior precisão. Faça alguns experimentos para ver se você consegue alcançar maior precisão.

## [Quiz pós-aula](https://ff-quizzes.netlify.app/en/ai/quiz/14)

## Revisão e Autoestudo

Embora as CNNs sejam mais frequentemente usadas para tarefas de Visão Computacional, elas são geralmente boas para extrair padrões de tamanho fixo. Por exemplo, se estivermos lidando com sons, também podemos querer usar CNNs para procurar padrões específicos no sinal de áudio - nesse caso, os filtros seriam unidimensionais (e essa CNN seria chamada de 1D-CNN). Além disso, às vezes 3D-CNN é usada para extrair características em espaço multidimensional, como certos eventos ocorrendo em vídeos - a CNN pode capturar certos padrões de mudança de características ao longo do tempo. Faça uma revisão e autoestudo sobre outras tarefas que podem ser realizadas com CNNs.

## [Tarefa](lab/README.md)

Neste laboratório, você será encarregado de classificar diferentes raças de gatos e cães. Essas imagens são mais complexas do que o conjunto de dados MNIST, possuem dimensões maiores e há mais de 10 classes.

---

