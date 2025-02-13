# Introdução às Redes Neurais

![Resumo do conteúdo de Introdução às Redes Neurais em um doodle](../../../../translated_images/ai-neuralnetworks.1c687ae40bc86e834f497844866a26d3e0886650a67a4bbe29442e2f157d3b18.pt.png)

Como discutimos na introdução, uma das maneiras de alcançar a inteligência é treinar um **modelo de computador** ou um **cérebro artificial**. Desde meados do século XX, pesquisadores tentaram diferentes modelos matemáticos, até que, nos últimos anos, essa abordagem se mostrou extremamente bem-sucedida. Esses modelos matemáticos do cérebro são chamados de **redes neurais**.

> Às vezes, as redes neurais são chamadas de *Redes Neurais Artificiais*, ANNs, para indicar que estamos falando de modelos, e não de redes reais de neurônios.

## Aprendizado de Máquina

As Redes Neurais são parte de uma disciplina maior chamada **Aprendizado de Máquina**, cujo objetivo é usar dados para treinar modelos de computador capazes de resolver problemas. O Aprendizado de Máquina constitui uma grande parte da Inteligência Artificial; no entanto, não abordamos o ML clássico neste currículo.

> Visite nosso currículo separado **[Aprendizado de Máquina para Iniciantes](http://github.com/microsoft/ml-for-beginners)** para saber mais sobre o Aprendizado de Máquina clássico.

No Aprendizado de Máquina, assumimos que temos um conjunto de dados de exemplos **X** e os valores de saída correspondentes **Y**. Os exemplos são frequentemente vetores N-dimensionais que consistem em **características**, e as saídas são chamadas de **rótulos**.

Consideraremos os dois problemas mais comuns de aprendizado de máquina:

* **Classificação**, onde precisamos classificar um objeto de entrada em duas ou mais classes.
* **Regressão**, onde precisamos prever um número numérico para cada uma das amostras de entrada.

> Ao representar entradas e saídas como tensores, o conjunto de dados de entrada é uma matriz de tamanho M×N, onde M é o número de amostras e N é o número de características. Os rótulos de saída Y são o vetor de tamanho M.

Neste currículo, focaremos apenas em modelos de redes neurais.

## Um Modelo de Neurônio

Da biologia, sabemos que nosso cérebro consiste em células neurais, cada uma delas tendo múltiplas "entradas" (axônios) e uma saída (dendrito). Axônios e dendritos podem conduzir sinais elétricos, e as conexões entre axônios e dendritos podem exibir diferentes graus de condutividade (controlados por neuromediadores).

![Modelo de um Neurônio](../../../../translated_images/synapse-wikipedia.ed20a9e4726ea1c6a3ce8fec51c0b9bec6181946dca0fe4e829bc12fa3bacf01.pt.jpg) | ![Modelo de um Neurônio](../../../../translated_images/artneuron.1a5daa88d20ebe6f5824ddb89fba0bdaaf49f67e8230c1afbec42909df1fc17e.pt.png)
----|----
Neurônio Real *([Imagem](https://en.wikipedia.org/wiki/Synapse#/media/File:SynapseSchematic_lines.svg) da Wikipedia)* | Neurônio Artificial *(Imagem do Autor)*

Assim, o modelo matemático mais simples de um neurônio contém várias entradas X<sub>1</sub>, ..., X<sub>N</sub> e uma saída Y, além de uma série de pesos W<sub>1</sub>, ..., W<sub>N</sub>. A saída é calculada como:

<img src="images/netout.png" alt="Y = f\left(\sum_{i=1}^N X_iW_i\right)" width="131" height="53" align="center"/>

onde f é alguma **função de ativação** não linear.

> Modelos iniciais de neurônios foram descritos no artigo clássico [A logical calculus of the ideas immanent in nervous activity](https://www.cs.cmu.edu/~./epxing/Class/10715/reading/McCulloch.and.Pitts.pdf) de Warren McCullock e Walter Pitts em 1943. Donald Hebb, em seu livro "[The Organization of Behavior: A Neuropsychological Theory](https://books.google.com/books?id=VNetYrB8EBoC)", propôs a maneira como essas redes podem ser treinadas.

## Nesta Seção

Nesta seção, aprenderemos sobre:
* [Perceptron](03-Perceptron/README.md), um dos primeiros modelos de rede neural para classificação em duas classes
* [Redes de múltiplas camadas](04-OwnFramework/README.md) com um caderno associado [como construir nossa própria estrutura](../../../../lessons/3-NeuralNetworks/04-OwnFramework/OwnFramework.ipynb)
* [Estruturas de Redes Neurais](05-Frameworks/README.md), com estes cadernos: [PyTorch](../../../../lessons/3-NeuralNetworks/05-Frameworks/IntroPyTorch.ipynb) e [Keras/Tensorflow](../../../../lessons/3-NeuralNetworks/05-Frameworks/IntroKerasTF.ipynb)
* [Overfitting](../../../../lessons/3-NeuralNetworks/05-Frameworks)

**Aviso Legal**:  
Este documento foi traduzido utilizando serviços de tradução automática baseados em IA. Embora nos esforcemos pela precisão, esteja ciente de que traduções automatizadas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte autoritativa. Para informações críticas, recomenda-se a tradução profissional feita por humanos. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações errôneas decorrentes do uso desta tradução.