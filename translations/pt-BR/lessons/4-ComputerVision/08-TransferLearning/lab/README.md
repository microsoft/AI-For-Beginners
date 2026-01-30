# Classificação de Oxford Pets usando Transfer Learning

Trabalho prático do [Currículo AI for Beginners](https://github.com/microsoft/ai-for-beginners).

## Tarefa

Imagine que você precisa desenvolver um aplicativo para uma creche de animais para catalogar todos os pets. Uma das grandes funcionalidades de tal aplicativo seria identificar automaticamente a raça a partir de uma fotografia. Neste exercício, usaremos transfer learning para classificar imagens reais de animais de estimação do conjunto de dados [Oxford-IIIT](https://www.robots.ox.ac.uk/~vgg/data/pets/).

## O Conjunto de Dados

Usaremos o conjunto de dados original [Oxford-IIIT](https://www.robots.ox.ac.uk/~vgg/data/pets/), que contém 35 raças diferentes de cães e gatos.

Para baixar o conjunto de dados, use este trecho de código:

```python
!wget https://www.robots.ox.ac.uk/~vgg/data/pets/data/images.tar.gz
!tar xfz images.tar.gz
!rm images.tar.gz
```

## Iniciando o Notebook

Comece o exercício abrindo [OxfordPets.ipynb](../../../../../../lessons/4-ComputerVision/08-TransferLearning/lab/OxfordPets.ipynb)

## Conclusão

Transfer learning e redes pré-treinadas nos permitem resolver problemas reais de classificação de imagens de forma relativamente simples. No entanto, redes pré-treinadas funcionam bem em imagens de tipos semelhantes, e se começarmos a classificar imagens muito diferentes (por exemplo, imagens médicas), é provável que obtenhamos resultados muito piores.

**Aviso Legal**:  
Este documento foi traduzido utilizando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos para garantir a precisão, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte oficial. Para informações críticas, recomenda-se a tradução profissional feita por humanos. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações equivocadas decorrentes do uso desta tradução.