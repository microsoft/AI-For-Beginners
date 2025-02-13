# Classificação Multi-Classe com Perceptron

Tarefa do [Currículo AI para Iniciantes](https://github.com/microsoft/ai-for-beginners).

## Tarefa

Usando o código que desenvolvemos nesta lição para classificação binária de dígitos manuscritos MNIST, crie um classificador multi-classe que seja capaz de reconhecer qualquer dígito. Calcule a precisão da classificação nos conjuntos de dados de treino e teste, e imprima a matriz de confusão.

## Dicas

1. Para cada dígito, crie um conjunto de dados para o classificador binário de "este dígito vs. todos os outros dígitos"
1. Treine 10 perceptrons diferentes para classificação binária (um para cada dígito)
1. Defina uma função que irá classificar um dígito de entrada

> **Dica**: Se combinarmos os pesos de todos os 10 perceptrons em uma única matriz, devemos ser capazes de aplicar todos os 10 perceptrons aos dígitos de entrada por meio de uma multiplicação de matriz. O dígito mais provável pode então ser encontrado apenas aplicando a operação `argmax` na saída.

## Notebook Inicial

Comece o laboratório abrindo [PerceptronMultiClass.ipynb](../../../../../../lessons/3-NeuralNetworks/03-Perceptron/lab/PerceptronMultiClass.ipynb)

**Aviso Legal**:  
Este documento foi traduzido usando serviços de tradução automática baseados em IA. Embora nos esforcemos pela precisão, esteja ciente de que traduções automatizadas podem conter erros ou imprecisões. O documento original em sua língua nativa deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se a tradução profissional por um humano. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações errôneas decorrentes do uso desta tradução.