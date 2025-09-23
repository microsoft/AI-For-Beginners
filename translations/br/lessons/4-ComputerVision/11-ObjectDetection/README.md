<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "d76a7eda28de5210c8b1ba50a6216c69",
  "translation_date": "2025-09-23T08:20:30+00:00",
  "source_file": "lessons/4-ComputerVision/11-ObjectDetection/README.md",
  "language_code": "br"
}
-->
# Detecção de Objetos

Os modelos de classificação de imagens que abordamos até agora tomavam uma imagem e produziam um resultado categórico, como a classe 'número' em um problema MNIST. No entanto, em muitos casos, não queremos apenas saber que uma imagem retrata objetos - queremos determinar sua localização precisa. Este é exatamente o objetivo da **detecção de objetos**.

## [Quiz pré-aula](https://ff-quizzes.netlify.app/en/ai/quiz/21)

![Detecção de Objetos](../../../../../translated_images/Screen_Shot_2016-11-17_at_11.14.54_AM.b4bb3769353287be1b905373ed9c858102c054b16e4595c76ec3f7bba0feb549.br.png)

> Imagem do [site YOLO v2](https://pjreddie.com/darknet/yolov2/)

## Uma Abordagem Ingênua para Detecção de Objetos

Suponha que queremos encontrar um gato em uma imagem. Uma abordagem muito ingênua para detecção de objetos seria a seguinte:

1. Dividir a imagem em vários blocos.
2. Executar a classificação de imagem em cada bloco.
3. Os blocos que resultarem em uma ativação suficientemente alta podem ser considerados como contendo o objeto em questão.

![Detecção Ingênua de Objetos](../../../../../translated_images/naive-detection.e7f1ba220ccd08c68a2ea8e06a7ed75c3fcc738c2372f9e00b7f4299a8659c01.br.png)

> *Imagem do [Notebook de Exercícios](ObjectDetection-TF.ipynb)*

No entanto, essa abordagem está longe de ser ideal, pois só permite que o algoritmo localize a caixa delimitadora do objeto de forma muito imprecisa. Para uma localização mais precisa, precisamos executar algum tipo de **regressão** para prever as coordenadas das caixas delimitadoras - e, para isso, precisamos de conjuntos de dados específicos.

## Regressão para Detecção de Objetos

[Este post no blog](https://towardsdatascience.com/object-detection-with-neural-networks-a4e2c46b4491) oferece uma ótima introdução à detecção de formas.

## Conjuntos de Dados para Detecção de Objetos

Você pode encontrar os seguintes conjuntos de dados para essa tarefa:

* [PASCAL VOC](http://host.robots.ox.ac.uk/pascal/VOC/) - 20 classes
* [COCO](http://cocodataset.org/#home) - Objetos Comuns em Contexto. 80 classes, caixas delimitadoras e máscaras de segmentação

![COCO](../../../../../translated_images/coco-examples.71bc60380fa6cceb7caad48bd09e35b6028caabd363aa04fee89c414e0870e86.br.jpg)

## Métricas de Detecção de Objetos

### Interseção sobre União

Enquanto na classificação de imagens é fácil medir o desempenho do algoritmo, na detecção de objetos precisamos medir tanto a correção da classe quanto a precisão da localização inferida da caixa delimitadora. Para este último, usamos a chamada **Interseção sobre União** (IoU), que mede o quão bem duas caixas (ou duas áreas arbitrárias) se sobrepõem.

![IoU](../../../../../translated_images/iou_equation.9a4751d40fff4e119ecd0a7bcca4e71ab1dc83e0d4f2a0d66ff0859736f593cf.br.png)

> *Figura 2 de [este excelente post sobre IoU](https://pyimagesearch.com/2016/11/07/intersection-over-union-iou-for-object-detection/)*

A ideia é simples - dividimos a área de interseção entre duas figuras pela área de sua união. Para duas áreas idênticas, o IoU seria 1, enquanto para áreas completamente disjuntas será 0. Caso contrário, variará de 0 a 1. Normalmente, consideramos apenas aquelas caixas delimitadoras para as quais o IoU está acima de um determinado valor.

### Precisão Média

Suponha que queremos medir o quão bem uma determinada classe de objetos $C$ é reconhecida. Para medir isso, usamos a métrica de **Precisão Média**, que é calculada da seguinte forma:

1. Considere a curva de Precisão-Recall que mostra a precisão dependendo de um valor de limiar de detecção (de 0 a 1).
2. Dependendo do limiar, detectaremos mais ou menos objetos na imagem, e diferentes valores de precisão e recall.
3. A curva terá este formato:

<img src="https://github.com/shwars/NeuroWorkshop/raw/master/images/ObjDetectionPrecisionRecall.png"/>

> *Imagem do [NeuroWorkshop](http://github.com/shwars/NeuroWorkshop)*

A Precisão Média para uma classe $C$ é a área sob essa curva. Mais precisamente, o eixo de Recall é normalmente dividido em 10 partes, e a Precisão é calculada como a média de todos esses pontos:

$$
AP = {1\over11}\sum_{i=0}^{10}\mbox{Precision}(\mbox{Recall}={i\over10})
$$

### AP e IoU

Consideramos apenas aquelas detecções para as quais o IoU está acima de um determinado valor. Por exemplo, no conjunto de dados PASCAL VOC, normalmente $\mbox{IoU Threshold} = 0.5$ é assumido, enquanto no COCO o AP é medido para diferentes valores de $\mbox{IoU Threshold}$.

<img src="https://github.com/shwars/NeuroWorkshop/raw/master/images/ObjDetectionPrecisionRecallIoU.png"/>

> *Imagem do [NeuroWorkshop](http://github.com/shwars/NeuroWorkshop)*

### Precisão Média Global - mAP

A principal métrica para Detecção de Objetos é chamada de **Precisão Média Global**, ou **mAP**. É o valor da Precisão Média, calculado como a média entre todas as classes de objetos, e às vezes também sobre $\mbox{IoU Threshold}$. Em mais detalhes, o processo de cálculo do **mAP** é descrito
[neste post do blog](https://medium.com/@timothycarlen/understanding-the-map-evaluation-metric-for-object-detection-a07fe6962cf3)), e também [aqui com exemplos de código](https://gist.github.com/tarlen5/008809c3decf19313de216b9208f3734).

## Diferentes Abordagens para Detecção de Objetos

Existem duas grandes classes de algoritmos de detecção de objetos:

* **Redes de Proposta de Região** (R-CNN, Fast R-CNN, Faster R-CNN). A ideia principal é gerar **Regiões de Interesse** (ROI) e executar CNN sobre elas, procurando a ativação máxima. É um pouco semelhante à abordagem ingênua, com a exceção de que as ROIs são geradas de forma mais inteligente. Uma das principais desvantagens desses métodos é que eles são lentos, porque precisamos de muitas passagens do classificador CNN sobre a imagem.
* Métodos de **uma única passagem** (YOLO, SSD, RetinaNet). Nessas arquiteturas, projetamos a rede para prever classes e ROIs em uma única passagem.

### R-CNN: CNN Baseada em Região

[R-CNN](http://islab.ulsan.ac.kr/files/announcement/513/rcnn_pami.pdf) usa [Selective Search](http://www.huppelen.nl/publications/selectiveSearchDraft.pdf) para gerar uma estrutura hierárquica de regiões ROI, que são então passadas por extratores de características CNN e classificadores SVM para determinar a classe do objeto, e regressão linear para determinar as coordenadas da *caixa delimitadora*. [Artigo Oficial](https://arxiv.org/pdf/1506.01497v1.pdf)

![RCNN](../../../../../translated_images/rcnn1.cae407020dfb1d1fb572656e44f75cd6c512cc220591c116c506652c10e47f26.br.png)

> *Imagem de van de Sande et al. ICCV’11*

![RCNN-1](../../../../../translated_images/rcnn2.2d9530bb83516484ec65b250c22dbf37d3d23244f32864ebcb91d98fe7c3112c.br.png)

> *Imagens de [este blog](https://towardsdatascience.com/r-cnn-fast-r-cnn-faster-r-cnn-yolo-object-detection-algorithms-36d53571365e)*

### F-RCNN - Fast R-CNN

Essa abordagem é semelhante à R-CNN, mas as regiões são definidas após as camadas de convolução terem sido aplicadas.

![FRCNN](../../../../../translated_images/f-rcnn.3cda6d9bb41888754037d2d9763e2298a96de5d9bc2a21db3147357aa5da9b1a.br.png)

> Imagem do [Artigo Oficial](https://www.cv-foundation.org/openaccess/content_iccv_2015/papers/Girshick_Fast_R-CNN_ICCV_2015_paper.pdf), [arXiv](https://arxiv.org/pdf/1504.08083.pdf), 2015

### Faster R-CNN

A ideia principal dessa abordagem é usar uma rede neural para prever ROIs - a chamada *Rede de Proposta de Região*. [Artigo](https://arxiv.org/pdf/1506.01497.pdf), 2016

![FasterRCNN](../../../../../translated_images/faster-rcnn.8d46c099b87ef30ab2ea26dbc4bdd85b974a57ba8eb526f65dc4cd0a4711de30.br.png)

> Imagem do [Artigo Oficial](https://arxiv.org/pdf/1506.01497.pdf)

### R-FCN: Rede Totalmente Convolucional Baseada em Região

Este algoritmo é ainda mais rápido que o Faster R-CNN. A ideia principal é a seguinte:

1. Extraímos características usando ResNet-101.
1. As características são processadas por **Position-Sensitive Score Map**. Cada objeto de $C$ classes é dividido em regiões $k\times k$, e treinamos para prever partes dos objetos.
1. Para cada parte das regiões $k\times k$, todas as redes votam pelas classes de objetos, e a classe de objeto com o maior número de votos é selecionada.

![r-fcn image](../../../../../translated_images/r-fcn.13eb88158b99a3da50fa2787a6be5cb310d47f0e9655cc93a1090dc7aab338d1.br.png)

> Imagem do [Artigo Oficial](https://arxiv.org/abs/1605.06409)

### YOLO - You Only Look Once

YOLO é um algoritmo de uma única passagem em tempo real. A ideia principal é a seguinte:

 * A imagem é dividida em regiões $S\times S$.
 * Para cada região, **CNN** prevê $n$ objetos possíveis, coordenadas da *caixa delimitadora* e *confiança*=*probabilidade* * IoU.

 ![YOLO](../../../../../translated_images/yolo.a2648ec82ee8bb4ea27537677adb482fd4b733ca1705c561b6a24a85102dced5.br.png)

> Imagem do [Artigo Oficial](https://arxiv.org/abs/1506.02640)

### Outros Algoritmos

* RetinaNet: [Artigo Oficial](https://arxiv.org/abs/1708.02002)
   - [Implementação em PyTorch no Torchvision](https://pytorch.org/vision/stable/_modules/torchvision/models/detection/retinanet.html)
   - [Implementação em Keras](https://github.com/fizyr/keras-retinanet)
   - [Detecção de Objetos com RetinaNet](https://keras.io/examples/vision/retinanet/) em Exemplos do Keras
* SSD (Single Shot Detector): [Artigo Oficial](https://arxiv.org/abs/1512.02325)

## ✍️ Exercícios: Detecção de Objetos

Continue seu aprendizado no seguinte notebook:

[ObjectDetection.ipynb](ObjectDetection.ipynb)

## Conclusão

Nesta lição, você fez um tour rápido por todas as várias maneiras de realizar a detecção de objetos!

## 🚀 Desafio

Leia estes artigos e notebooks sobre YOLO e experimente por conta própria:

* [Bom post no blog](https://www.analyticsvidhya.com/blog/2018/12/practical-guide-object-detection-yolo-framewor-python/) descrevendo YOLO
 * [Site Oficial](https://pjreddie.com/darknet/yolo/)
 * YOLO: [Implementação em Keras](https://github.com/experiencor/keras-yolo2), [notebook passo a passo](https://github.com/experiencor/basic-yolo-keras/blob/master/Yolo%20Step-by-Step.ipynb)
 * YOLO v2: [Implementação em Keras](https://github.com/experiencor/keras-yolo2), [notebook passo a passo](https://github.com/experiencor/keras-yolo2/blob/master/Yolo%20Step-by-Step.ipynb)

## [Quiz pós-aula](https://ff-quizzes.netlify.app/en/ai/quiz/22)

## Revisão & Autoestudo

* [Detecção de Objetos](https://tjmachinelearning.com/lectures/1718/obj/) por Nikhil Sardana
* [Uma boa comparação de algoritmos de detecção de objetos](https://lilianweng.github.io/lil-log/2018/12/27/object-detection-part-4.html)
* [Revisão de Algoritmos de Aprendizado Profundo para Detecção de Objetos](https://medium.com/comet-app/review-of-deep-learning-algorithms-for-object-detection-c1f3d437b852)
* [Uma Introdução Passo a Passo aos Algoritmos Básicos de Detecção de Objetos](https://www.analyticsvidhya.com/blog/2018/10/a-step-by-step-introduction-to-the-basic-object-detection-algorithms-part-1/)
* [Implementação de Faster R-CNN em Python para Detecção de Objetos](https://www.analyticsvidhya.com/blog/2018/11/implementation-faster-r-cnn-python-object-detection/)

## [Tarefa: Detecção de Objetos](lab/README.md)

---

