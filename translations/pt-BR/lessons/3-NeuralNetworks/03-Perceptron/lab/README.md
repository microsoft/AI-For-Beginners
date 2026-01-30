# Classificação Multi-Classe com Perceptron

Atividade prática do [Currículo de IA para Iniciantes](https://github.com/microsoft/ai-for-beginners).

## Tarefa

Usando o código que desenvolvemos nesta lição para classificação binária de dígitos manuscritos do MNIST, crie um classificador multi-classe que seja capaz de reconhecer qualquer dígito. Calcule a precisão da classificação nos conjuntos de dados de treinamento e teste, e exiba a matriz de confusão.

## Dicas

1. Para cada dígito, crie um conjunto de dados para o classificador binário de "este dígito vs. todos os outros dígitos".
1. Treine 10 perceptrons diferentes para classificação binária (um para cada dígito).
1. Defina uma função que classifique um dígito de entrada.

> **Dica**: Se combinarmos os pesos de todos os 10 perceptrons em uma matriz, devemos ser capazes de aplicar todos os 10 perceptrons aos dígitos de entrada por meio de uma única multiplicação de matriz. O dígito mais provável pode então ser encontrado simplesmente aplicando a operação `argmax` no resultado.

## Notebook Inicial

Inicie a atividade abrindo [PerceptronMultiClass.ipynb](PerceptronMultiClass.ipynb)

---

**Aviso Legal**:  
Este documento foi traduzido utilizando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos para garantir a precisão, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte oficial. Para informações críticas, recomenda-se a tradução profissional feita por humanos. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações equivocadas decorrentes do uso desta tradução.