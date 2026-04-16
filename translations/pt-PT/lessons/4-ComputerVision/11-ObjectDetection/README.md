# Detecção de Objetos

Os modelos de classificação de imagens que abordámos até agora recebiam uma imagem e produziam um resultado categórico, como a classe 'número' num problema MNIST. No entanto, em muitos casos, não queremos apenas saber que uma imagem retrata objetos - queremos determinar a sua localização precisa. Este é exatamente o objetivo da **detecção de objetos**.

## [Questionário pré-aula](https://ff-quizzes.netlify.app/en/ai/quiz/21)

![Detecção de Objetos](../../../../../translated_images/pt-PT/Screen_Shot_2016-11-17_at_11.14.54_AM.b4bb3769353287be.webp)

> Imagem do [site YOLO v2](https://pjreddie.com/darknet/yolov2/)

## Uma Abordagem Ingénua para Detecção de Objetos

Supondo que queremos encontrar um gato numa imagem, uma abordagem muito ingénua para detecção de objetos seria a seguinte:

1. Dividir a imagem em vários blocos.
2. Executar a classificação de imagem em cada bloco.
3. Os blocos que resultarem numa ativação suficientemente alta podem ser considerados como contendo o objeto em questão.

![Detecção Ingénua de Objetos](../../../../../translated_images/pt-PT/naive-detection.e7f1ba220ccd08c6.webp)

> *Imagem do [Caderno de Exercícios](ObjectDetection-TF.ipynb)*

No entanto, esta abordagem está longe de ser ideal, pois só permite ao algoritmo localizar a caixa delimitadora do objeto de forma muito imprecisa. Para uma localização mais precisa, precisamos de executar algum tipo de **regressão** para prever as coordenadas das caixas delimitadoras - e, para isso, necessitamos de conjuntos de dados específicos.

## Regressão para Detecção de Objetos

[Este artigo](https://towardsdatascience.com/object-detection-with-neural-networks-a4e2c46b4491) oferece uma excelente introdução à deteção de formas.

## Conjuntos de Dados para Detecção de Objetos

Poderá encontrar os seguintes conjuntos de dados para esta tarefa:

* [PASCAL VOC](http://host.robots.ox.ac.uk/pascal/VOC/) - 20 classes
* [COCO](http://cocodataset.org/#home) - Objetos Comuns em Contexto. 80 classes, caixas delimitadoras e máscaras de segmentação

![COCO](../../../../../translated_images/pt-PT/coco-examples.71bc60380fa6cceb.webp)

## Métricas de Detecção de Objetos

### Interseção sobre União

Enquanto na classificação de imagens é fácil medir o desempenho do algoritmo, na detecção de objetos precisamos de medir tanto a correção da classe como a precisão da localização da caixa delimitadora inferida. Para esta última, utilizamos a chamada **Interseção sobre União** (IoU), que mede o quão bem duas caixas (ou duas áreas arbitrárias) se sobrepõem.

![IoU](../../../../../translated_images/pt-PT/iou_equation.9a4751d40fff4e11.webp)

> *Figura 2 de [este excelente artigo sobre IoU](https://pyimagesearch.com/2016/11/07/intersection-over-union-iou-for-object-detection/)*

A ideia é simples - dividimos a área de interseção entre duas figuras pela área da sua união. Para duas áreas idênticas, o IoU seria 1, enquanto para áreas completamente disjuntas será 0. Caso contrário, variará entre 0 e 1. Normalmente, consideramos apenas as caixas delimitadoras para as quais o IoU está acima de um determinado valor.

### Precisão Média

Suponha que queremos medir o quão bem uma determinada classe de objetos $C$ é reconhecida. Para medir isso, utilizamos a métrica de **Precisão Média**, que é calculada da seguinte forma:

1. Consideramos a curva de Precisão-Recall que mostra a precisão dependendo de um valor de limiar de deteção (de 0 a 1).
2. Dependendo do limiar, obteremos mais ou menos objetos detetados na imagem e diferentes valores de precisão e recall.
3. A curva terá este aspeto:

<img src="https://github.com/shwars/NeuroWorkshop/raw/master/images/ObjDetectionPrecisionRecall.png"/>

> *Imagem de [NeuroWorkshop](http://github.com/shwars/NeuroWorkshop)*

A Precisão Média para uma classe $C$ é a área sob esta curva. Mais precisamente, o eixo Recall é normalmente dividido em 10 partes, e a Precisão é calculada como média em todos esses pontos:

$$
AP = {1\over11}\sum_{i=0}^{10}\mbox{Precision}(\mbox{Recall}={i\over10})
$$

### AP e IoU

Consideramos apenas as deteções para as quais o IoU está acima de um determinado valor. Por exemplo, no conjunto de dados PASCAL VOC, normalmente $\mbox{IoU Threshold} = 0.5$ é assumido, enquanto no COCO o AP é medido para diferentes valores de $\mbox{IoU Threshold}$.

<img src="https://github.com/shwars/NeuroWorkshop/raw/master/images/ObjDetectionPrecisionRecallIoU.png"/>

> *Imagem de [NeuroWorkshop](http://github.com/shwars/NeuroWorkshop)*

### Precisão Média Global - mAP

A principal métrica para Detecção de Objetos é chamada de **Precisão Média Global**, ou **mAP**. É o valor da Precisão Média, calculado como média entre todas as classes de objetos, e às vezes também sobre $\mbox{IoU Threshold}$. O processo de cálculo do **mAP** é descrito em mais detalhe
[neste artigo](https://medium.com/@timothycarlen/understanding-the-map-evaluation-metric-for-object-detection-a07fe6962cf3)), e também [aqui com exemplos de código](https://gist.github.com/tarlen5/008809c3decf19313de216b9208f3734).

## Diferentes Abordagens para Detecção de Objetos

Existem duas grandes classes de algoritmos de detecção de objetos:

* **Redes de Proposta de Região** (R-CNN, Fast R-CNN, Faster R-CNN). A ideia principal é gerar **Regiões de Interesse** (ROI) e executar CNN sobre elas, procurando a ativação máxima. É um pouco semelhante à abordagem ingénua, com a exceção de que as ROIs são geradas de forma mais inteligente. Uma das principais desvantagens desses métodos é que são lentos, pois necessitam de várias passagens do classificador CNN sobre a imagem.
* Métodos de **uma única passagem** (YOLO, SSD, RetinaNet). Nessas arquiteturas, projetamos a rede para prever tanto as classes como as ROIs numa única passagem.

### R-CNN: CNN Baseada em Região

[R-CNN](http://islab.ulsan.ac.kr/files/announcement/513/rcnn_pami.pdf) utiliza [Selective Search](http://www.huppelen.nl/publications/selectiveSearchDraft.pdf) para gerar uma estrutura hierárquica de regiões ROI, que são então passadas por extratores de características CNN e classificadores SVM para determinar a classe do objeto, e regressão linear para determinar as coordenadas da *caixa delimitadora*. [Artigo Oficial](https://arxiv.org/pdf/1506.01497v1.pdf)

![RCNN](../../../../../translated_images/pt-PT/rcnn1.cae407020dfb1d1f.webp)

> *Imagem de van de Sande et al. ICCV’11*

![RCNN-1](../../../../../translated_images/pt-PT/rcnn2.2d9530bb83516484.webp)

> *Imagens de [este artigo](https://towardsdatascience.com/r-cnn-fast-r-cnn-faster-r-cnn-yolo-object-detection-algorithms-36d53571365e)*

### F-RCNN - Fast R-CNN

Esta abordagem é semelhante à R-CNN, mas as regiões são definidas após as camadas de convolução terem sido aplicadas.

![FRCNN](../../../../../translated_images/pt-PT/f-rcnn.3cda6d9bb4188875.webp)

> Imagem do [Artigo Oficial](https://www.cv-foundation.org/openaccess/content_iccv_2015/papers/Girshick_Fast_R-CNN_ICCV_2015_paper.pdf), [arXiv](https://arxiv.org/pdf/1504.08083.pdf), 2015

### Faster R-CNN

A ideia principal desta abordagem é usar uma rede neural para prever ROIs - a chamada *Rede de Proposta de Região*. [Artigo](https://arxiv.org/pdf/1506.01497.pdf), 2016

![FasterRCNN](../../../../../translated_images/pt-PT/faster-rcnn.8d46c099b87ef30a.webp)

> Imagem do [artigo oficial](https://arxiv.org/pdf/1506.01497.pdf)

### R-FCN: Rede Totalmente Convolucional Baseada em Região

Este algoritmo é ainda mais rápido que o Faster R-CNN. A ideia principal é a seguinte:

1. Extraímos características usando ResNet-101.
1. As características são processadas por **Position-Sensitive Score Map**. Cada objeto das classes $C$ é dividido em regiões $k\times k$, e treinamos para prever partes dos objetos.
1. Para cada parte das regiões $k\times k$, todas as redes votam pelas classes de objetos, e a classe de objeto com o voto máximo é selecionada.

![r-fcn image](../../../../../translated_images/pt-PT/r-fcn.13eb88158b99a3da.webp)

> Imagem do [artigo oficial](https://arxiv.org/abs/1605.06409)

### YOLO - You Only Look Once

YOLO é um algoritmo de uma única passagem em tempo real. A ideia principal é a seguinte:

 * A imagem é dividida em regiões $S\times S$.
 * Para cada região, **CNN** prevê $n$ objetos possíveis, coordenadas da *caixa delimitadora* e *confiança*=*probabilidade* * IoU.

 ![YOLO](../../../../../translated_images/pt-PT/yolo.a2648ec82ee8bb4e.webp)

> Imagem do [artigo oficial](https://arxiv.org/abs/1506.02640)

### Outros Algoritmos

* RetinaNet: [artigo oficial](https://arxiv.org/abs/1708.02002)
   - [Implementação PyTorch em Torchvision](https://pytorch.org/vision/stable/_modules/torchvision/models/detection/retinanet.html)
   - [Implementação Keras](https://github.com/fizyr/keras-retinanet)
   - [Detecção de Objetos com RetinaNet](https://keras.io/examples/vision/retinanet/) em exemplos Keras
* SSD (Single Shot Detector): [artigo oficial](https://arxiv.org/abs/1512.02325)

## ✍️ Exercícios: Detecção de Objetos

Continue a sua aprendizagem no seguinte caderno:

[ObjectDetection.ipynb](ObjectDetection.ipynb)

## Conclusão

Nesta lição, fez uma rápida exploração de todas as várias formas de realizar detecção de objetos!

## 🚀 Desafio

Leia estes artigos e cadernos sobre YOLO e experimente por si mesmo:

* [Bom artigo](https://www.analyticsvidhya.com/blog/2018/12/practical-guide-object-detection-yolo-framewor-python/) descrevendo YOLO
 * [Site oficial](https://pjreddie.com/darknet/yolo/)
 * YOLO: [Implementação Keras](https://github.com/experiencor/keras-yolo2), [caderno passo-a-passo](https://github.com/experiencor/basic-yolo-keras/blob/master/Yolo%20Step-by-Step.ipynb)
 * YOLO v2: [Implementação Keras](https://github.com/experiencor/keras-yolo2), [caderno passo-a-passo](https://github.com/experiencor/keras-yolo2/blob/master/Yolo%20Step-by-Step.ipynb)

## [Questionário pós-aula](https://ff-quizzes.netlify.app/en/ai/quiz/22)

## Revisão e Autoestudo

* [Detecção de Objetos](https://tjmachinelearning.com/lectures/1718/obj/) por Nikhil Sardana
* [Uma boa comparação de algoritmos de detecção de objetos](https://lilianweng.github.io/lil-log/2018/12/27/object-detection-part-4.html)
* [Revisão de Algoritmos de Aprendizagem Profunda para Detecção de Objetos](https://medium.com/comet-app/review-of-deep-learning-algorithms-for-object-detection-c1f3d437b852)
* [Uma Introdução Passo-a-Passo aos Algoritmos Básicos de Detecção de Objetos](https://www.analyticsvidhya.com/blog/2018/10/a-step-by-step-introduction-to-the-basic-object-detection-algorithms-part-1/)
* [Implementação de Faster R-CNN em Python para Detecção de Objetos](https://www.analyticsvidhya.com/blog/2018/11/implementation-faster-r-cnn-python-object-detection/)

## [Tarefa: Detecção de Objetos](lab/README.md)

---

