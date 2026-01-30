# Segmentação

Já aprendemos sobre Detecção de Objetos, que nos permite localizar objetos numa imagem ao prever os seus *bounding boxes*. No entanto, para algumas tarefas, não precisamos apenas de bounding boxes, mas também de uma localização mais precisa dos objetos. Esta tarefa chama-se **segmentação**.

## [Questionário pré-aula](https://ff-quizzes.netlify.app/en/ai/quiz/23)

A segmentação pode ser vista como **classificação de píxeis**, onde para **cada** píxel da imagem devemos prever a sua classe (*fundo* sendo uma das classes). Existem dois principais algoritmos de segmentação:

* **Segmentação semântica** apenas indica a classe do píxel, sem distinguir entre diferentes objetos da mesma classe.
* **Segmentação por instância** divide as classes em diferentes instâncias.

Na segmentação por instância, estas ovelhas são objetos diferentes, mas na segmentação semântica todas as ovelhas são representadas por uma única classe.

<img src="../../../../../translated_images/pt-PT/instance_vs_semantic.eee9812bebf8cd45.webp" width="50%">

> Imagem retirada [deste artigo](https://nirmalamurali.medium.com/image-classification-vs-semantic-segmentation-vs-instance-segmentation-625c33a08d50)

Existem diferentes arquiteturas neurais para segmentação, mas todas têm a mesma estrutura. De certa forma, é semelhante ao autoencoder que aprendeste anteriormente, mas em vez de desconstruir a imagem original, o nosso objetivo é desconstruir uma **máscara**. Assim, uma rede de segmentação tem as seguintes partes:

* **Codificador (Encoder)** extrai características da imagem de entrada.
* **Decodificador (Decoder)** transforma essas características na **imagem de máscara**, com o mesmo tamanho e número de canais correspondentes ao número de classes.

<img src="../../../../../translated_images/pt-PT/segm.92442f2cb42ff4fa.webp" width="80%">

> Imagem retirada [desta publicação](https://arxiv.org/pdf/2001.05566.pdf)

Devemos destacar especialmente a função de perda utilizada na segmentação. Ao usar autoencoders clássicos, precisamos medir a similaridade entre duas imagens, e podemos usar o erro quadrático médio (MSE) para isso. Na segmentação, cada píxel na imagem de máscara alvo representa o número da classe (codificado em one-hot ao longo da terceira dimensão), então precisamos usar funções de perda específicas para classificação - perda de entropia cruzada, média sobre todos os píxeis. Se a máscara for binária, utiliza-se a **perda de entropia cruzada binária** (BCE).

> ✅ A codificação one-hot é uma forma de codificar um rótulo de classe num vetor de comprimento igual ao número de classes. Dá uma vista de olhos [neste artigo](https://datagy.io/sklearn-one-hot-encode/) sobre esta técnica.

## Segmentação em Imagens Médicas

Nesta lição, veremos a segmentação em ação ao treinar uma rede para reconhecer nevos humanos (também conhecidos como sinais) em imagens médicas. Utilizaremos a <a href="https://www.fc.up.pt/addi/ph2%20database.html">Base de Dados PH<sup>2</sup></a> de imagens dermatoscópicas como fonte de imagens. Este conjunto de dados contém 200 imagens de três classes: nevo típico, nevo atípico e melanoma. Todas as imagens também contêm uma **máscara** correspondente que delineia o nevo.

> ✅ Esta técnica é particularmente adequada para este tipo de imagens médicas, mas que outras aplicações do mundo real consegues imaginar?

<img alt="navi" src="../../../../../translated_images/pt-PT/navi.2f20b727910110ea.webp"/>

> Imagem retirada da Base de Dados PH<sup>2</sup>

Vamos treinar um modelo para segmentar qualquer nevo do seu fundo.

## ✍️ Exercícios: Segmentação Semântica

Abre os notebooks abaixo para aprender mais sobre diferentes arquiteturas de segmentação semântica, praticar com elas e vê-las em ação.

* [Segmentação Semântica Pytorch](SemanticSegmentationPytorch.ipynb)
* [Segmentação Semântica TensorFlow](SemanticSegmentationTF.ipynb)

## [Questionário pós-aula](https://ff-quizzes.netlify.app/en/ai/quiz/24)

## Conclusão

A segmentação é uma técnica muito poderosa para classificação de imagens, indo além dos bounding boxes para a classificação a nível de píxeis. É uma técnica utilizada em imagens médicas, entre outras aplicações.

## 🚀 Desafio

A segmentação corporal é apenas uma das tarefas comuns que podemos realizar com imagens de pessoas. Outras tarefas importantes incluem **detecção de esqueleto** e **detecção de pose**. Experimenta a biblioteca [OpenPose](https://github.com/CMU-Perceptual-Computing-Lab/openpose) para ver como a detecção de pose pode ser utilizada.

## Revisão & Estudo Autónomo

Este [artigo da Wikipédia](https://wikipedia.org/wiki/Image_segmentation) oferece uma boa visão geral das várias aplicações desta técnica. Aprende mais por conta própria sobre os subdomínios de Segmentação por Instância e Segmentação Panóptica neste campo de estudo.

## [Trabalho prático](lab/README.md)

Neste laboratório, experimenta **segmentação do corpo humano** utilizando o [Segmentation Full Body MADS Dataset](https://www.kaggle.com/datasets/tapakah68/segmentation-full-body-mads-dataset) do Kaggle.

---

