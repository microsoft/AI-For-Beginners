### YOLO - Você Só Olha Uma Vez

YOLO é um algoritmo de uma única passagem em tempo real. A ideia principal é a seguinte:

* A imagem é dividida em regiões de $S\times S$ 
* Para cada região, a **CNN** prevê $n$ possíveis objetos, as coordenadas da *bounding box* e *confiança* = *probabilidade* * IoU.

![YOLO](../../../../../translated_images/yolo.a2648ec82ee8bb4ea27537677adb482fd4b733ca1705c561b6a24a85102dced5.pt.png)

### SSD - Single Shot MultiBox Detector

O SSD é outro método de detecção em uma única passagem. Ele funciona de maneira semelhante ao YOLO, mas usa diferentes escalas de detecção em várias camadas da rede.

![SSD](../../../../../translated_images/ssd.8f409ceb7ad470415f8995994dd89282b57541bff09ecde650902217c84f4c0d.pt.png)

> Imagem de [oficial paper](https://arxiv.org/pdf/1512.02325.pdf)

### RetinaNet

O RetinaNet introduz a ideia de *Focal Loss*, que ajuda a lidar com o problema de classes desbalanceadas em detecção de objetos. Ele usa uma arquitetura de rede semelhante ao SSD, mas com um foco maior em melhorar a precisão na detecção de objetos menos frequentes.

![RetinaNet](../../../../../translated_images/retinanet.cfd3ebd2e5c63692a1c543b868134b66e4b0789230c22679b07eebd0e69d7cbc.pt.png)

> Imagem de [oficial paper](https://arxiv.org/pdf/1708.02002.pdf)

### Conclusão

A detecção de objetos é uma área ativa de pesquisa em visão computacional. Com o advento de novas arquiteturas e técnicas, como YOLO, SSD e RetinaNet, a precisão e a eficiência dos algoritmos de detecção de objetos continuam a melhorar. O uso de redes neurais profundas e técnicas de aprendizado de máquina tem revolucionado essa área, tornando-a mais acessível e eficaz em uma variedade de aplicações do mundo real.
> Imagem do [artigo oficial](https://arxiv.org/abs/1506.02640)

### Outros Algoritmos

* RetinaNet: [artigo oficial](https://arxiv.org/abs/1708.02002)
   - [Implementação em PyTorch no Torchvision](https://pytorch.org/vision/stable/_modules/torchvision/models/detection/retinanet.html)
   - [Implementação em Keras](https://github.com/fizyr/keras-retinanet)
   - [Detecção de Objetos com RetinaNet](https://keras.io/examples/vision/retinanet/) nos Exemplos do Keras
* SSD (Single Shot Detector): [artigo oficial](https://arxiv.org/abs/1512.02325)

## ✍️ Exercícios: Detecção de Objetos

Continue seu aprendizado no seguinte notebook:

[ObjectDetection.ipynb](../../../../../lessons/4-ComputerVision/11-ObjectDetection/ObjectDetection.ipynb)

## Conclusão

Nesta lição, você fez um tour rápido por todas as diversas maneiras de realizar a detecção de objetos!

## 🚀 Desafio

Leia esses artigos e notebooks sobre YOLO e experimente por conta própria

* [Bom post de blog](https://www.analyticsvidhya.com/blog/2018/12/practical-guide-object-detection-yolo-framewor-python/) descrevendo o YOLO
 * [Site oficial](https://pjreddie.com/darknet/yolo/)
 * Yolo: [implementação em Keras](https://github.com/experiencor/keras-yolo2), [notebook passo a passo](https://github.com/experiencor/basic-yolo-keras/blob/master/Yolo%20Step-by-Step.ipynb)
 * Yolo v2: [implementação em Keras](https://github.com/experiencor/keras-yolo2), [notebook passo a passo](https://github.com/experiencor/keras-yolo2/blob/master/Yolo%20Step-by-Step.ipynb)

## [Quiz pós-aula](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/211)

## Revisão & Autoestudo

* [Detecção de Objetos](https://tjmachinelearning.com/lectures/1718/obj/) por Nikhil Sardana
* [Uma boa comparação de algoritmos de detecção de objetos](https://lilianweng.github.io/lil-log/2018/12/27/object-detection-part-4.html)
* [Revisão de Algoritmos de Aprendizado Profundo para Detecção de Objetos](https://medium.com/comet-app/review-of-deep-learning-algorithms-for-object-detection-c1f3d437b852)
* [Uma Introdução Passo a Passo aos Algoritmos Básicos de Detecção de Objetos](https://www.analyticsvidhya.com/blog/2018/10/a-step-by-step-introduction-to-the-basic-object-detection-algorithms-part-1/)
* [Implementação do Faster R-CNN em Python para Detecção de Objetos](https://www.analyticsvidhya.com/blog/2018/11/implementation-faster-r-cnn-python-object-detection/)

## [Tarefa: Detecção de Objetos](lab/README.md)

**Aviso Legal**:  
Este documento foi traduzido utilizando serviços de tradução automática baseados em IA. Embora nos esforcemos pela precisão, esteja ciente de que traduções automatizadas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se a tradução profissional feita por humanos. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações errôneas decorrentes do uso desta tradução.