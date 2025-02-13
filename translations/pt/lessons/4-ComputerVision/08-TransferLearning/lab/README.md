# Classificação de Animais de Estimação de Oxford usando Aprendizado por Transferência

Trabalho de laboratório do [Currículo de IA para Iniciantes](https://github.com/microsoft/ai-for-beginners).

## Tarefa

Imagine que você precisa desenvolver uma aplicação para uma creche de animais de estimação para catalogar todos os pets. Uma das grandes funcionalidades de tal aplicação seria descobrir automaticamente a raça a partir de uma fotografia. Neste trabalho, usaremos aprendizado por transferência para classificar imagens de animais de estimação da vida real do conjunto de dados [Oxford-IIIT](https://www.robots.ox.ac.uk/~vgg/data/pets/).

## O Conjunto de Dados

Usaremos o conjunto de dados original de animais de estimação [Oxford-IIIT](https://www.robots.ox.ac.uk/~vgg/data/pets/), que contém 35 raças diferentes de cães e gatos.

Para baixar o conjunto de dados, utilize este trecho de código:

```python
!wget https://www.robots.ox.ac.uk/~vgg/data/pets/data/images.tar.gz
!tar xfz images.tar.gz
!rm images.tar.gz
```

## Iniciando o Notebook

Comece o laboratório abrindo [OxfordPets.ipynb](../../../../../../lessons/4-ComputerVision/08-TransferLearning/lab/OxfordPets.ipynb)

## Conclusão

O aprendizado por transferência e as redes pré-treinadas nos permitem resolver problemas de classificação de imagens do mundo real de maneira relativamente fácil. No entanto, redes pré-treinadas funcionam bem em imagens de tipos semelhantes, e se começarmos a classificar imagens muito diferentes (por exemplo, imagens médicas), é provável que obtenhamos resultados muito piores.

**Isenção de responsabilidade**:  
Este documento foi traduzido usando serviços de tradução automática baseados em IA. Embora nos esforcemos pela precisão, esteja ciente de que traduções automatizadas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte autoritária. Para informações críticas, recomenda-se a tradução profissional por um humano. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações erradas que possam surgir do uso desta tradução.