# Classificação de Oxford Pets usando Transfer Learning

Trabalho prático do [Currículo AI for Beginners](https://github.com/microsoft/ai-for-beginners).

## Tarefa

Imagine que precisa desenvolver uma aplicação para um berçário de animais de estimação para catalogar todos os animais. Uma das grandes funcionalidades de tal aplicação seria identificar automaticamente a raça a partir de uma fotografia. Neste trabalho, vamos usar transfer learning para classificar imagens reais de animais de estimação do conjunto de dados [Oxford-IIIT](https://www.robots.ox.ac.uk/~vgg/data/pets/).

## O Conjunto de Dados

Usaremos o conjunto de dados original [Oxford-IIIT](https://www.robots.ox.ac.uk/~vgg/data/pets/), que contém 35 raças diferentes de cães e gatos.

Para descarregar o conjunto de dados, utilize este trecho de código:

```python
!wget https://www.robots.ox.ac.uk/~vgg/data/pets/data/images.tar.gz
!tar xfz images.tar.gz
!rm images.tar.gz
```

## Notebook Inicial

Comece o trabalho prático abrindo [OxfordPets.ipynb](../../../../../../lessons/4-ComputerVision/08-TransferLearning/lab/OxfordPets.ipynb)

## Conclusão

Transfer learning e redes pré-treinadas permitem-nos resolver problemas reais de classificação de imagens de forma relativamente simples. No entanto, redes pré-treinadas funcionam bem em imagens de tipos semelhantes, e se começarmos a classificar imagens muito diferentes (por exemplo, imagens médicas), é provável que obtenhamos resultados significativamente piores.

**Aviso Legal**:  
Este documento foi traduzido utilizando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos para garantir a precisão, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original na sua língua nativa deve ser considerado a fonte autoritária. Para informações críticas, recomenda-se a tradução profissional realizada por humanos. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes do uso desta tradução.