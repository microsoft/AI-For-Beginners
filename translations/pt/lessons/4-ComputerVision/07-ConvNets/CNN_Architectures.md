# Arquiteturas de CNN Conhecidas

### VGG-16

VGG-16 é uma rede que alcançou 92,7% de precisão na classificação top-5 do ImageNet em 2014. Ela possui a seguinte estrutura de camadas:

![Camadas do ImageNet](../../../../../translated_images/vgg-16-arch1.d901a5583b3a51baeaab3e768567d921e5d54befa46e1e642616c5458c934028.pt.jpg)

Como você pode ver, o VGG segue uma arquitetura piramidal tradicional, que é uma sequência de camadas de convolução e pooling.

![Pirâmide do ImageNet](../../../../../translated_images/vgg-16-arch.64ff2137f50dd49fdaa786e3f3a975b3f22615efd13efb19c5d22f12e01451a1.pt.jpg)

> Imagem de [Researchgate](https://www.researchgate.net/figure/Vgg16-model-structure-To-get-the-VGG-NIN-model-we-replace-the-2-nd-4-th-6-th-7-th_fig2_335194493)

### ResNet

ResNet é uma família de modelos proposta pela Microsoft Research em 2015. A ideia principal do ResNet é usar **blocos residuais**:

<img src="images/resnet-block.png" width="300"/>

> Imagem deste [artigo](https://arxiv.org/pdf/1512.03385.pdf)

A razão para usar a passagem de identidade é fazer com que nossa camada preveja **a diferença** entre o resultado de uma camada anterior e a saída do bloco residual - daí o nome *residual*. Esses blocos são muito mais fáceis de treinar, e é possível construir redes com várias centenas desses blocos (as variantes mais comuns são ResNet-52, ResNet-101 e ResNet-152).

Você também pode pensar nesta rede como sendo capaz de ajustar sua complexidade ao conjunto de dados. Inicialmente, quando você começa a treinar a rede, os valores dos pesos são pequenos, e a maior parte do sinal passa por camadas de identidade. À medida que o treinamento avança e os pesos se tornam maiores, a importância dos parâmetros da rede cresce, e a rede se ajusta para acomodar o poder expressivo necessário para classificar corretamente as imagens de treinamento.

### Google Inception

A arquitetura Google Inception leva essa ideia um passo adiante e constrói cada camada da rede como uma combinação de vários caminhos diferentes:

<img src="images/inception.png" width="400"/>

> Imagem de [Researchgate](https://www.researchgate.net/figure/Inception-module-with-dimension-reductions-left-and-schema-for-Inception-ResNet-v1_fig2_355547454)

Aqui, precisamos enfatizar o papel das convoluções 1x1, porque à primeira vista elas não fazem sentido. Por que precisaríamos passar pela imagem com um filtro 1x1? No entanto, você precisa lembrar que os filtros de convolução também trabalham com vários canais de profundidade (originalmente - cores RGB, em camadas subsequentes - canais para diferentes filtros), e a convolução 1x1 é usada para misturar esses canais de entrada juntos usando diferentes pesos treináveis. Ela também pode ser vista como uma redução de dimensão (pooling) sobre a dimensão do canal.

Aqui está [um bom post no blog](https://medium.com/analytics-vidhya/talented-mr-1x1-comprehensive-look-at-1x1-convolution-in-deep-learning-f6b355825578) sobre o assunto, e [o artigo original](https://arxiv.org/pdf/1312.4400.pdf).

### MobileNet

MobileNet é uma família de modelos com tamanho reduzido, adequados para dispositivos móveis. Use-os se você estiver com recursos limitados e puder sacrificar um pouco de precisão. A ideia principal por trás deles é a chamada **convolução separável por profundidade**, que permite representar filtros de convolução por uma composição de convoluções espaciais e convolução 1x1 sobre canais de profundidade. Isso reduz significativamente o número de parâmetros, tornando a rede menor em tamanho e também mais fácil de treinar com menos dados.

Aqui está [um bom post no blog sobre MobileNet](https://medium.com/analytics-vidhya/image-classification-with-mobilenet-cc6fbb2cd470).

## Conclusão

Nesta unidade, você aprendeu o conceito principal por trás das redes neurais de visão computacional - redes convolucionais. Arquiteturas da vida real que impulsionam a classificação de imagens, detecção de objetos e até mesmo redes de geração de imagens são todas baseadas em CNNs, apenas com mais camadas e alguns truques de treinamento adicionais.

## 🚀 Desafio

Nos cadernos acompanhantes, há notas na parte inferior sobre como obter maior precisão. Faça alguns experimentos para ver se você consegue alcançar uma precisão mais alta.

## [Quiz pós-aula](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/207)

## Revisão e Estudo Autônomo

Embora as CNNs sejam mais frequentemente usadas para tarefas de Visão Computacional, elas são geralmente boas para extrair padrões de tamanho fixo. Por exemplo, se estivermos lidando com sons, também podemos querer usar CNNs para procurar padrões específicos em sinais de áudio - nesse caso, os filtros seriam unidimensionais (e essa CNN seria chamada de 1D-CNN). Além disso, às vezes, a 3D-CNN é usada para extrair características em espaço multidimensional, como certos eventos ocorrendo em vídeo - a CNN pode capturar certos padrões de mudança de características ao longo do tempo. Faça uma revisão e estudo autônomo sobre outras tarefas que podem ser realizadas com CNNs.

## [Tarefa](lab/README.md)

Neste laboratório, você tem a tarefa de classificar diferentes raças de gatos e cães. Essas imagens são mais complexas do que o conjunto de dados MNIST e têm dimensões mais altas, e há mais de 10 classes.

**Isenção de responsabilidade**:  
Este documento foi traduzido utilizando serviços de tradução automática baseados em IA. Embora nos esforcemos pela precisão, esteja ciente de que traduções automatizadas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte autoritária. Para informações críticas, recomenda-se a tradução profissional por um humano. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações errôneas decorrentes do uso desta tradução.