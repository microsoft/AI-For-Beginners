<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "2f7b97b375358cb51a1e098df306bf73",
  "translation_date": "2025-08-24T08:59:55+00:00",
  "source_file": "lessons/4-ComputerVision/07-ConvNets/CNN_Architectures.md",
  "language_code": "pt"
}
-->
# Arquiteturas CNN Conhecidas

### VGG-16

VGG-16 é uma rede que alcançou 92,7% de precisão na classificação top-5 do ImageNet em 2014. Possui a seguinte estrutura de camadas:

![Camadas do ImageNet](../../../../../lessons/4-ComputerVision/07-ConvNets/images/vgg-16-arch1.jpg)

Como pode ver, a VGG segue uma arquitetura piramidal tradicional, que é uma sequência de camadas de convolução e pooling.

![Pirâmide do ImageNet](../../../../../lessons/4-ComputerVision/07-ConvNets/images/vgg-16-arch.jpg)

> Imagem de [Researchgate](https://www.researchgate.net/figure/Vgg16-model-structure-To-get-the-VGG-NIN-model-we-replace-the-2-nd-4-th-6-th-7-th_fig2_335194493)

### ResNet

ResNet é uma família de modelos proposta pela Microsoft Research em 2015. A ideia principal da ResNet é usar **blocos residuais**:

<img src="images/resnet-block.png" width="300"/>

> Imagem deste [artigo](https://arxiv.org/pdf/1512.03385.pdf)

A razão para usar a passagem de identidade é permitir que a camada preveja **a diferença** entre o resultado de uma camada anterior e a saída do bloco residual - daí o nome *residual*. Esses blocos são muito mais fáceis de treinar, e é possível construir redes com várias centenas desses blocos (as variantes mais comuns são ResNet-52, ResNet-101 e ResNet-152).

Pode também pensar nesta rede como sendo capaz de ajustar a sua complexidade ao conjunto de dados. Inicialmente, quando começa a treinar a rede, os valores dos pesos são pequenos, e a maior parte do sinal passa pelas camadas de identidade. À medida que o treino avança e os pesos se tornam maiores, a importância dos parâmetros da rede cresce, e a rede ajusta-se para acomodar o poder expressivo necessário para classificar corretamente as imagens de treino.

### Google Inception

A arquitetura Google Inception leva esta ideia um passo adiante e constrói cada camada da rede como uma combinação de vários caminhos diferentes:

<img src="images/inception.png" width="400"/>

> Imagem de [Researchgate](https://www.researchgate.net/figure/Inception-module-with-dimension-reductions-left-and-schema-for-Inception-ResNet-v1_fig2_355547454)

Aqui, é importante destacar o papel das convoluções 1x1, porque, à primeira vista, elas não fazem sentido. Por que precisaríamos passar pela imagem com um filtro 1x1? No entanto, é necessário lembrar que os filtros de convolução também trabalham com vários canais de profundidade (originalmente - cores RGB, em camadas subsequentes - canais para diferentes filtros), e a convolução 1x1 é usada para misturar esses canais de entrada usando diferentes pesos treináveis. Também pode ser vista como uma forma de downsampling (pooling) na dimensão dos canais.

Aqui está [um bom artigo](https://medium.com/analytics-vidhya/talented-mr-1x1-comprehensive-look-at-1x1-convolution-in-deep-learning-f6b355825578) sobre o assunto, e [o artigo original](https://arxiv.org/pdf/1312.4400.pdf).

### MobileNet

MobileNet é uma família de modelos com tamanho reduzido, adequada para dispositivos móveis. Use-os se tiver poucos recursos e puder sacrificar um pouco de precisão. A ideia principal por trás deles é a chamada **convolução separável por profundidade**, que permite representar filtros de convolução por uma composição de convoluções espaciais e convoluções 1x1 sobre os canais de profundidade. Isso reduz significativamente o número de parâmetros, tornando a rede menor em tamanho e também mais fácil de treinar com menos dados.

Aqui está [um bom artigo sobre MobileNet](https://medium.com/analytics-vidhya/image-classification-with-mobilenet-cc6fbb2cd470).

## Conclusão

Nesta unidade, aprendeu o conceito principal por trás das redes neurais de visão computacional - redes convolucionais. Arquiteturas reais que alimentam classificação de imagens, deteção de objetos e até redes de geração de imagens são todas baseadas em CNNs, apenas com mais camadas e alguns truques adicionais de treino.

## 🚀 Desafio

Nos notebooks que acompanham, há notas no final sobre como obter maior precisão. Faça alguns experimentos para ver se consegue alcançar uma precisão maior.

## [Questionário pós-aula](https://ff-quizzes.netlify.app/en/ai/quiz/14)

## Revisão e Autoestudo

Embora as CNNs sejam mais frequentemente usadas para tarefas de Visão Computacional, elas são geralmente boas para extrair padrões de tamanho fixo. Por exemplo, se estivermos a lidar com sons, também podemos querer usar CNNs para procurar padrões específicos no sinal de áudio - nesse caso, os filtros seriam unidimensionais (e essa CNN seria chamada de 1D-CNN). Além disso, às vezes é usada uma 3D-CNN para extrair características em espaço multidimensional, como certos eventos que ocorrem em vídeos - a CNN pode capturar certos padrões de mudança de características ao longo do tempo. Faça uma revisão e autoestudo sobre outras tarefas que podem ser realizadas com CNNs.

## [Tarefa](lab/README.md)

Neste laboratório, a sua tarefa é classificar diferentes raças de gatos e cães. Estas imagens são mais complexas do que o conjunto de dados MNIST, têm dimensões maiores e há mais de 10 classes.

**Aviso Legal**:  
Este documento foi traduzido utilizando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos para garantir a precisão, é importante ter em conta que traduções automáticas podem conter erros ou imprecisões. O documento original na sua língua nativa deve ser considerado a fonte autoritária. Para informações críticas, recomenda-se a tradução profissional realizada por humanos. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes da utilização desta tradução.