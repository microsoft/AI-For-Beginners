<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "d7f8a25ff13cfe9f4cd671cc23351fad",
  "translation_date": "2025-08-26T09:11:33+00:00",
  "source_file": "lessons/4-ComputerVision/12-Segmentation/README.md",
  "language_code": "br"
}
-->
# Segmentação

Anteriormente, aprendemos sobre Detecção de Objetos, que nos permite localizar objetos em uma imagem ao prever suas *caixas delimitadoras* (*bounding boxes*). No entanto, para algumas tarefas, não precisamos apenas das caixas delimitadoras, mas também de uma localização mais precisa dos objetos. Essa tarefa é chamada de **segmentação**.

## [Pré-quiz da aula](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/112)

A segmentação pode ser vista como uma **classificação de pixels**, onde para **cada** pixel da imagem devemos prever sua classe (*fundo* sendo uma das classes). Existem dois principais algoritmos de segmentação:

* **Segmentação semântica** informa apenas a classe do pixel, sem distinguir entre diferentes objetos da mesma classe.
* **Segmentação por instância** divide as classes em diferentes instâncias.

Na segmentação por instância, essas ovelhas são objetos diferentes, mas na segmentação semântica todas as ovelhas são representadas por uma única classe.

<img src="images/instance_vs_semantic.jpeg" width="50%">

> Imagem retirada [deste post no blog](https://nirmalamurali.medium.com/image-classification-vs-semantic-segmentation-vs-instance-segmentation-625c33a08d50)

Existem diferentes arquiteturas neurais para segmentação, mas todas possuem a mesma estrutura. De certa forma, é semelhante ao autoencoder que você aprendeu anteriormente, mas em vez de reconstruir a imagem original, nosso objetivo é reconstruir uma **máscara**. Assim, uma rede de segmentação possui as seguintes partes:

* **Codificador (Encoder)** extrai características da imagem de entrada.
* **Decodificador (Decoder)** transforma essas características na **imagem da máscara**, com o mesmo tamanho e número de canais correspondentes ao número de classes.

<img src="images/segm.png" width="80%">

> Imagem retirada [desta publicação](https://arxiv.org/pdf/2001.05566.pdf)

Devemos destacar especialmente a função de perda usada para segmentação. Ao usar autoencoders clássicos, precisamos medir a similaridade entre duas imagens, e podemos usar o erro quadrático médio (MSE) para isso. Na segmentação, cada pixel na imagem de máscara de destino representa o número da classe (codificado em one-hot ao longo da terceira dimensão), então precisamos usar funções de perda específicas para classificação - perda de entropia cruzada, média sobre todos os pixels. Se a máscara for binária - usa-se a **perda de entropia cruzada binária** (BCE).

> ✅ One-hot encoding é uma técnica para codificar um rótulo de classe em um vetor de comprimento igual ao número de classes. Confira [este artigo](https://datagy.io/sklearn-one-hot-encode/) sobre essa técnica.

## Segmentação para Imagens Médicas

Nesta lição, veremos a segmentação em ação treinando uma rede para reconhecer nevos humanos (também conhecidos como pintas) em imagens médicas. Utilizaremos o <a href="https://www.fc.up.pt/addi/ph2%20database.html">Banco de Dados PH<sup>2</sup></a> de imagens dermatoscópicas como fonte de imagens. Este conjunto de dados contém 200 imagens de três classes: nevo típico, nevo atípico e melanoma. Todas as imagens também possuem uma **máscara** correspondente que delimita o nevo.

> ✅ Essa técnica é particularmente apropriada para este tipo de imagem médica, mas quais outras aplicações do mundo real você consegue imaginar?

<img alt="navi" src="images/navi.png"/>

> Imagem retirada do Banco de Dados PH<sup>2</sup>

Treinaremos um modelo para segmentar qualquer nevo do fundo.

## ✍️ Exercícios: Segmentação Semântica

Abra os notebooks abaixo para aprender mais sobre diferentes arquiteturas de segmentação semântica, praticar com elas e vê-las em ação.

* [Segmentação Semântica com Pytorch](../../../../../lessons/4-ComputerVision/12-Segmentation/SemanticSegmentationPytorch.ipynb)
* [Segmentação Semântica com TensorFlow](../../../../../lessons/4-ComputerVision/12-Segmentation/SemanticSegmentationTF.ipynb)

## [Pós-quiz da aula](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/212)

## Conclusão

A segmentação é uma técnica muito poderosa para classificação de imagens, indo além das caixas delimitadoras para a classificação em nível de pixel. É uma técnica usada em imagens médicas, entre outras aplicações.

## 🚀 Desafio

A segmentação do corpo é apenas uma das tarefas comuns que podemos realizar com imagens de pessoas. Outras tarefas importantes incluem **detecção de esqueleto** e **detecção de pose**. Experimente a biblioteca [OpenPose](https://github.com/CMU-Perceptual-Computing-Lab/openpose) para ver como a detecção de pose pode ser utilizada.

## Revisão e Autoestudo

Este [artigo da Wikipedia](https://wikipedia.org/wiki/Image_segmentation) oferece uma boa visão geral das várias aplicações dessa técnica. Aprenda mais por conta própria sobre os subdomínios de Segmentação por Instância e Segmentação Panóptica neste campo de estudo.

## [Tarefa](lab/README.md)

Neste laboratório, experimente a **segmentação do corpo humano** usando o [Segmentation Full Body MADS Dataset](https://www.kaggle.com/datasets/tapakah68/segmentation-full-body-mads-dataset) do Kaggle.

**Aviso Legal**:  
Este documento foi traduzido utilizando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos para garantir a precisão, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte oficial. Para informações críticas, recomenda-se a tradução profissional feita por humanos. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes do uso desta tradução.