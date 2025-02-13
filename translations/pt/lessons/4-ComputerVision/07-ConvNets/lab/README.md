# Classificação de Rostos de Animais de Estimação

Trabalho de laboratório do [Currículo de IA para Iniciantes](https://github.com/microsoft/ai-for-beginners).

## Tarefa

Imagine que você precisa desenvolver uma aplicação para uma creche de animais de estimação para catalogar todos os pets. Uma das grandes funcionalidades de tal aplicação seria descobrir automaticamente a raça a partir de uma fotografia. Isso pode ser feito com sucesso usando redes neurais.

Você precisa treinar uma rede neural convolucional para classificar diferentes raças de gatos e cães usando o conjunto de dados **Pet Faces**.

## O Conjunto de Dados

Usaremos o conjunto de dados **Pet Faces**, derivado do conjunto de dados de pets [Oxford-IIIT](https://www.robots.ox.ac.uk/~vgg/data/pets/). Ele contém 35 raças diferentes de cães e gatos.

![Conjunto de dados com o qual vamos trabalhar](../../../../../../translated_images/data.50b2a9d5484bdbf0f52f5765b381cec9efe2bd296a98f007f90bedb6ac67f2a8.pt.png)

Para baixar o conjunto de dados, use este trecho de código:

```python
!wget https://mslearntensorflowlp.blob.core.windows.net/data/petfaces.tar.gz
!tar xfz petfaces.tar.gz
!rm petfaces.tar.gz
```

## Iniciando o Notebook

Comece o laboratório abrindo [PetFaces.ipynb](../../../../../../lessons/4-ComputerVision/07-ConvNets/lab/PetFaces.ipynb)

## Conclusão

Você resolveu um problema relativamente complexo de classificação de imagens do zero! Havia muitas classes, e você ainda conseguiu obter uma precisão razoável! Também faz sentido medir a precisão top-k, porque é fácil confundir algumas das classes que não são claramente diferentes, mesmo para seres humanos.

**Isenção de responsabilidade**:  
Este documento foi traduzido utilizando serviços de tradução automática baseados em IA. Embora nos esforcemos pela precisão, esteja ciente de que traduções automatizadas podem conter erros ou imprecisões. O documento original em sua língua nativa deve ser considerado a fonte autoritativa. Para informações críticas, recomenda-se a tradução profissional por humanos. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações errôneas decorrentes do uso desta tradução.