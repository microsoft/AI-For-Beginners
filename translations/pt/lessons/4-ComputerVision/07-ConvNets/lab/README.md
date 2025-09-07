<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f3d2cee9cb3c52160419e560c57a690e",
  "translation_date": "2025-08-24T09:00:11+00:00",
  "source_file": "lessons/4-ComputerVision/07-ConvNets/lab/README.md",
  "language_code": "pt"
}
-->
# Classificação de Rostos de Animais de Estimação

Trabalho de Laboratório do [Currículo de IA para Iniciantes](https://github.com/microsoft/ai-for-beginners).

## Tarefa

Imagine que precisa desenvolver uma aplicação para um berçário de animais de estimação para catalogar todos os animais. Uma das grandes funcionalidades de tal aplicação seria identificar automaticamente a raça a partir de uma fotografia. Isto pode ser feito com sucesso utilizando redes neuronais.

Precisa treinar uma rede neuronal convolucional para classificar diferentes raças de cães e gatos utilizando o dataset **Pet Faces**.

## O Dataset

Vamos utilizar o dataset **Pet Faces**, derivado do dataset de animais de estimação [Oxford-IIIT](https://www.robots.ox.ac.uk/~vgg/data/pets/). Este contém 35 raças diferentes de cães e gatos.

![Dataset com o qual iremos trabalhar](../../../../../../lessons/4-ComputerVision/07-ConvNets/lab/images/data.png)

Para descarregar o dataset, utilize este trecho de código:

```python
!wget https://mslearntensorflowlp.blob.core.windows.net/data/petfaces.tar.gz
!tar xfz petfaces.tar.gz
!rm petfaces.tar.gz
```

## Notebook Inicial

Comece o laboratório abrindo [PetFaces.ipynb](../../../../../../lessons/4-ComputerVision/07-ConvNets/lab/PetFaces.ipynb)

## Conclusão

Conseguiu resolver um problema relativamente complexo de classificação de imagens do zero! Havia bastantes classes, e ainda assim conseguiu obter uma precisão razoável! Também faz sentido medir a precisão top-k, porque é fácil confundir algumas classes que não são claramente diferentes, mesmo para seres humanos.

**Aviso Legal**:  
Este documento foi traduzido utilizando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos para garantir a precisão, é importante notar que traduções automáticas podem conter erros ou imprecisões. O documento original na sua língua nativa deve ser considerado a fonte autoritária. Para informações críticas, recomenda-se a tradução profissional realizada por humanos. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes do uso desta tradução.