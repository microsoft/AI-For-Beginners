# Arquiteturas Conhecidas de CNN

### VGG-16

VGG-16 é uma rede que alcançou 92,7% de precisão na classificação top-5 do ImageNet em 2014. Tem a seguinte estrutura de camadas:

![Camadas do ImageNet](../../../../../translated_images/pt-PT/vgg-16-arch1.d901a5583b3a51ba.webp)

Como pode ver, a VGG segue uma arquitetura tradicional em pirâmide, que consiste numa sequência de camadas de convolução e pooling.

![Pirâmide do ImageNet](../../../../../translated_images/pt-PT/vgg-16-arch.64ff2137f50dd49f.webp)

> Imagem de [Researchgate](https://www.researchgate.net/figure/Vgg16-model-structure-To-get-the-VGG-NIN-model-we-replace-the-2-nd-4-th-6-th-7-th_fig2_335194493)

### ResNet

ResNet é uma família de modelos proposta pela Microsoft Research em 2015. A ideia principal da ResNet é utilizar **blocos residuais**:

<img src="../../../../../translated_images/pt-PT/resnet-block.aba4ccbcc0944434.webp" width="300"/>

> Imagem retirada [deste artigo](https://arxiv.org/pdf/1512.03385.pdf)

A razão para usar a passagem de identidade é fazer com que a camada preveja **a diferença** entre o resultado de uma camada anterior e a saída do bloco residual - daí o nome *residual*. Estes blocos são muito mais fáceis de treinar, e é possível construir redes com centenas destes blocos (as variantes mais comuns são ResNet-52, ResNet-101 e ResNet-152).

Pode também pensar nesta rede como sendo capaz de ajustar a sua complexidade ao conjunto de dados. Inicialmente, quando começa a treinar a rede, os valores dos pesos são pequenos, e a maior parte do sinal passa pelas camadas de identidade. À medida que o treino avança e os pesos se tornam maiores, a importância dos parâmetros da rede cresce, e a rede ajusta-se para acomodar o poder expressivo necessário para classificar corretamente as imagens de treino.

### Google Inception

A arquitetura Google Inception leva esta ideia um passo mais além e constrói cada camada da rede como uma combinação de vários caminhos diferentes:

<img src="../../../../../translated_images/pt-PT/inception.a6605b85bcbc6f52.webp" width="400"/>

> Imagem de [Researchgate](https://www.researchgate.net/figure/Inception-module-with-dimension-reductions-left-and-schema-for-Inception-ResNet-v1_fig2_355547454)

Aqui, é importante destacar o papel das convoluções 1x1, porque à primeira vista não fazem sentido. Por que razão precisaríamos de passar pela imagem com um filtro 1x1? No entanto, é necessário lembrar que os filtros de convolução também trabalham com vários canais de profundidade (originalmente - cores RGB, em camadas subsequentes - canais para diferentes filtros), e a convolução 1x1 é usada para misturar esses canais de entrada utilizando diferentes pesos treináveis. Pode também ser vista como uma redução dimensional (pooling) sobre a dimensão dos canais.

Aqui está [um bom artigo](https://medium.com/analytics-vidhya/talented-mr-1x1-comprehensive-look-at-1x1-convolution-in-deep-learning-f6b355825578) sobre o assunto, e [o artigo original](https://arxiv.org/pdf/1312.4400.pdf).

### MobileNet

MobileNet é uma família de modelos com tamanho reduzido, adequada para dispositivos móveis. Utilize-os se tiver poucos recursos e puder sacrificar um pouco de precisão. A ideia principal por trás destes modelos é a chamada **convolução separável por profundidade**, que permite representar filtros de convolução através de uma composição de convoluções espaciais e convoluções 1x1 sobre os canais de profundidade. Isto reduz significativamente o número de parâmetros, tornando a rede menor em tamanho e também mais fácil de treinar com menos dados.

Aqui está [um bom artigo sobre MobileNet](https://medium.com/analytics-vidhya/image-classification-with-mobilenet-cc6fbb2cd470).

## Conclusão

Nesta unidade, aprendeu o conceito principal por trás das redes neurais de visão computacional - redes convolucionais. Arquiteturas reais que alimentam classificação de imagens, deteção de objetos e até redes de geração de imagens são todas baseadas em CNNs, apenas com mais camadas e alguns truques adicionais de treino.

## 🚀 Desafio

Nos notebooks que acompanham esta unidade, há notas no final sobre como obter maior precisão. Faça alguns experimentos para ver se consegue alcançar uma precisão mais elevada.

## [Questionário pós-aula](https://ff-quizzes.netlify.app/en/ai/quiz/14)

## Revisão e Autoestudo

Embora as CNNs sejam mais frequentemente usadas para tarefas de Visão Computacional, elas são geralmente boas para extrair padrões de tamanho fixo. Por exemplo, se estivermos a lidar com sons, também podemos querer usar CNNs para procurar padrões específicos no sinal de áudio - neste caso, os filtros seriam unidimensionais (e esta CNN seria chamada de 1D-CNN). Além disso, às vezes utiliza-se 3D-CNN para extrair características em espaço multidimensional, como certos eventos que ocorrem em vídeos - a CNN pode capturar certos padrões de mudança de características ao longo do tempo. Faça uma revisão e autoestudo sobre outras tarefas que podem ser realizadas com CNNs.

## [Tarefa](lab/README.md)

Neste laboratório, a sua tarefa é classificar diferentes raças de gatos e cães. Estas imagens são mais complexas do que o conjunto de dados MNIST, têm dimensões mais elevadas e há mais de 10 classes.

---

