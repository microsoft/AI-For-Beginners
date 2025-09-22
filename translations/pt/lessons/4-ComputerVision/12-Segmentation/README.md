<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "d7f8a25ff13cfe9f4cd671cc23351fad",
  "translation_date": "2025-08-24T08:58:11+00:00",
  "source_file": "lessons/4-ComputerVision/12-Segmentation/README.md",
  "language_code": "pt"
}
-->
# Segmentação

Já aprendemos sobre Detecção de Objetos, que nos permite localizar objetos numa imagem ao prever as suas *caixas delimitadoras* (*bounding boxes*). No entanto, para algumas tarefas, não precisamos apenas das caixas delimitadoras, mas também de uma localização mais precisa dos objetos. Esta tarefa é chamada de **segmentação**.

## [Questionário pré-aula](https://ff-quizzes.netlify.app/en/ai/quiz/23)

A segmentação pode ser vista como uma **classificação de píxeis**, onde para **cada** píxel da imagem devemos prever a sua classe (*fundo* sendo uma das classes). Existem dois principais algoritmos de segmentação:

* **Segmentação semântica** apenas indica a classe do píxel, sem distinguir entre diferentes objetos da mesma classe.
* **Segmentação por instância** divide as classes em diferentes instâncias.

Por exemplo, na segmentação por instância, estas ovelhas são objetos diferentes, mas na segmentação semântica todas as ovelhas são representadas por uma única classe.

<img src="images/instance_vs_semantic.jpeg" width="50%">

> Imagem retirada [deste artigo](https://nirmalamurali.medium.com/image-classification-vs-semantic-segmentation-vs-instance-segmentation-625c33a08d50)

Existem diferentes arquiteturas neurais para segmentação, mas todas têm a mesma estrutura. De certa forma, é semelhante ao autoencoder que aprendemos anteriormente, mas em vez de reconstruir a imagem original, o nosso objetivo é reconstruir uma **máscara**. Assim, uma rede de segmentação possui as seguintes partes:

* **Codificador (Encoder)** extrai características da imagem de entrada.
* **Decodificador (Decoder)** transforma essas características na **imagem da máscara**, com o mesmo tamanho e número de canais correspondentes ao número de classes.

<img src="images/segm.png" width="80%">

> Imagem retirada [desta publicação](https://arxiv.org/pdf/2001.05566.pdf)

Devemos destacar especialmente a função de perda utilizada para segmentação. Ao usar autoencoders clássicos, precisamos medir a semelhança entre duas imagens, e podemos usar o erro quadrático médio (MSE) para isso. Na segmentação, cada píxel na imagem de máscara alvo representa o número da classe (codificado em one-hot ao longo da terceira dimensão), então precisamos usar funções de perda específicas para classificação - perda de entropia cruzada, média sobre todos os píxeis. Se a máscara for binária, utiliza-se a **perda de entropia cruzada binária** (BCE).

> ✅ A codificação one-hot é uma forma de codificar um rótulo de classe num vetor de comprimento igual ao número de classes. Consulte [este artigo](https://datagy.io/sklearn-one-hot-encode/) para saber mais sobre esta técnica.

## Segmentação para Imagens Médicas

Nesta lição, veremos a segmentação em ação ao treinar uma rede para reconhecer nevos humanos (também conhecidos como sinais) em imagens médicas. Utilizaremos a <a href="https://www.fc.up.pt/addi/ph2%20database.html">Base de Dados PH<sup>2</sup></a> de imagens de dermoscopia como fonte de imagens. Este conjunto de dados contém 200 imagens de três classes: nevo típico, nevo atípico e melanoma. Todas as imagens também possuem uma **máscara** correspondente que delimita o nevo.

> ✅ Esta técnica é particularmente adequada para este tipo de imagem médica, mas que outras aplicações do mundo real consegue imaginar?

<img alt="navi" src="images/navi.png"/>

> Imagem retirada da Base de Dados PH<sup>2</sup>

Treinaremos um modelo para segmentar qualquer nevo do seu fundo.

## ✍️ Exercícios: Segmentação Semântica

Abra os notebooks abaixo para aprender mais sobre diferentes arquiteturas de segmentação semântica, praticar com elas e vê-las em ação.

* [Segmentação Semântica com Pytorch](../../../../../lessons/4-ComputerVision/12-Segmentation/SemanticSegmentationPytorch.ipynb)
* [Segmentação Semântica com TensorFlow](../../../../../lessons/4-ComputerVision/12-Segmentation/SemanticSegmentationTF.ipynb)

## [Questionário pós-aula](https://ff-quizzes.netlify.app/en/ai/quiz/24)

## Conclusão

A segmentação é uma técnica muito poderosa para classificação de imagens, indo além das caixas delimitadoras para a classificação a nível de píxeis. É uma técnica utilizada em imagens médicas, entre outras aplicações.

## 🚀 Desafio

A segmentação corporal é apenas uma das tarefas comuns que podemos realizar com imagens de pessoas. Outras tarefas importantes incluem **detecção de esqueleto** e **detecção de pose**. Experimente a biblioteca [OpenPose](https://github.com/CMU-Perceptual-Computing-Lab/openpose) para ver como a detecção de pose pode ser utilizada.

## Revisão e Estudo Individual

Este [artigo da Wikipédia](https://wikipedia.org/wiki/Image_segmentation) oferece uma boa visão geral das várias aplicações desta técnica. Pesquise mais sobre os subdomínios de Segmentação por Instância e Segmentação Panóptica neste campo de estudo.

## [Tarefa](lab/README.md)

Neste laboratório, experimente a **segmentação do corpo humano** utilizando o [Segmentation Full Body MADS Dataset](https://www.kaggle.com/datasets/tapakah68/segmentation-full-body-mads-dataset) do Kaggle.

**Aviso Legal**:  
Este documento foi traduzido utilizando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos pela precisão, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original na sua língua nativa deve ser considerado a fonte autoritária. Para informações críticas, recomenda-se a tradução profissional realizada por humanos. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes do uso desta tradução.