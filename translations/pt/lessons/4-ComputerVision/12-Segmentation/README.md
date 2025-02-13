# Segmentação

Anteriormente, aprendemos sobre Detecção de Objetos, que nos permite localizar objetos na imagem prevendo suas *caixas delimitadoras*. No entanto, para algumas tarefas, não precisamos apenas de caixas delimitadoras, mas também de uma localização de objeto mais precisa. Essa tarefa é chamada de **segmentação**.

## [Quiz pré-aula](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/112)

A segmentação pode ser vista como **classificação de pixels**, onde para **cada** pixel da imagem devemos prever sua classe (*fundo* sendo uma das classes). Existem dois principais algoritmos de segmentação:

* **Segmentação semântica** apenas informa a classe do pixel, e não faz distinção entre diferentes objetos da mesma classe.
* **Segmentação de instâncias** divide classes em diferentes instâncias.

Por exemplo, na segmentação de instâncias, essas ovelhas são objetos diferentes, mas na segmentação semântica todas as ovelhas são representadas por uma única classe.

<img src="images/instance_vs_semantic.jpeg" width="50%">

> Imagem de [este post de blog](https://nirmalamurali.medium.com/image-classification-vs-semantic-segmentation-vs-instance-segmentation-625c33a08d50)

Existem diferentes arquiteturas neurais para segmentação, mas todas têm a mesma estrutura. De certa forma, é semelhante ao autoencoder que você aprendeu anteriormente, mas em vez de deconstruir a imagem original, nosso objetivo é deconstruir uma **máscara**. Assim, uma rede de segmentação possui as seguintes partes:

* **Encoder** extrai características da imagem de entrada.
* **Decoder** transforma essas características na **imagem da máscara**, com o mesmo tamanho e número de canais correspondendo ao número de classes.

<img src="images/segm.png" width="80%">

> Imagem de [esta publicação](https://arxiv.org/pdf/2001.05566.pdf)

Devemos mencionar especialmente a função de perda que é usada para segmentação. Ao usar autoencoders clássicos, precisamos medir a similaridade entre duas imagens, e podemos usar o erro quadrático médio (MSE) para isso. Na segmentação, cada pixel na imagem da máscara alvo representa o número da classe (one-hot-encoded ao longo da terceira dimensão), então precisamos usar funções de perda específicas para classificação - perda de entropia cruzada, média sobre todos os pixels. Se a máscara for binária - **perda de entropia cruzada binária** (BCE) é utilizada.

> ✅ A codificação one-hot é uma forma de codificar um rótulo de classe em um vetor de comprimento igual ao número de classes. Dê uma olhada [neste artigo](https://datagy.io/sklearn-one-hot-encode/) sobre essa técnica.

## Segmentação para Imagens Médicas

Nesta lição, veremos a segmentação em ação treinando a rede para reconhecer nevos humanos (também conhecidos como manchas) em imagens médicas. Usaremos o <a href="https://www.fc.up.pt/addi/ph2%20database.html">Banco de Dados PH<sup>2</sup></a> de imagens de dermatoscopia como fonte de imagem. Este conjunto de dados contém 200 imagens de três classes: nevo típico, nevo atípico e melanoma. Todas as imagens também contêm uma **máscara** correspondente que contorna o nevo.

> ✅ Esta técnica é particularmente apropriada para este tipo de imagem médica, mas quais outras aplicações do mundo real você poderia imaginar?

<img alt="navi" src="images/navi.png"/>

> Imagem do Banco de Dados PH<sup>2</sup>

Treinaremos um modelo para segmentar qualquer nevo de seu fundo.

## ✍️ Exercícios: Segmentação Semântica

Abra os notebooks abaixo para aprender mais sobre diferentes arquiteturas de segmentação semântica, praticar trabalhando com elas e vê-las em ação.

* [Segmentação Semântica Pytorch](../../../../../lessons/4-ComputerVision/12-Segmentation/SemanticSegmentationPytorch.ipynb)
* [Segmentação Semântica TensorFlow](../../../../../lessons/4-ComputerVision/12-Segmentation/SemanticSegmentationTF.ipynb)

## [Quiz pós-aula](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/212)

## Conclusão

A segmentação é uma técnica muito poderosa para classificação de imagens, indo além das caixas delimitadoras para classificação em nível de pixel. É uma técnica usada em imagens médicas, entre outras aplicações.

## 🚀 Desafio

A segmentação do corpo é apenas uma das tarefas comuns que podemos realizar com imagens de pessoas. Outras tarefas importantes incluem **detecção de esqueleto** e **detecção de pose**. Experimente a biblioteca [OpenPose](https://github.com/CMU-Perceptual-Computing-Lab/openpose) para ver como a detecção de pose pode ser utilizada.

## Revisão & Autoestudo

Este [artigo da wikipedia](https://wikipedia.org/wiki/Image_segmentation) oferece uma boa visão geral das várias aplicações dessa técnica. Aprenda mais por conta própria sobre os subdomínios da segmentação de instâncias e segmentação panóptica neste campo de investigação.

## [Tarefa](lab/README.md)

Neste laboratório, tente **segmentação do corpo humano** usando o [Conjunto de Dados de Segmentação do Corpo Completo MADS](https://www.kaggle.com/datasets/tapakah68/segmentation-full-body-mads-dataset) do Kaggle.

**Isenção de responsabilidade**:  
Este documento foi traduzido utilizando serviços de tradução automática baseados em IA. Embora nos esforcemos pela precisão, esteja ciente de que traduções automatizadas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte autoritativa. Para informações críticas, recomenda-se a tradução profissional por um humano. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes do uso desta tradução.