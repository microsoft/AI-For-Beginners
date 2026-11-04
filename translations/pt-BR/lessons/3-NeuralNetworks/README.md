# Introdução às Redes Neurais

![Resumo do conteúdo introdutório de Redes Neurais em um rabisco](../../../../translated_images/pt-BR/ai-neuralnetworks.1c687ae40bc86e83.webp)

Como discutimos na introdução, uma das formas de alcançar inteligência é treinar um **modelo computacional** ou um **cérebro artificial**. Desde meados do século XX, pesquisadores tentaram diferentes modelos matemáticos, até que nos últimos anos essa direção provou ser extremamente bem-sucedida. Tais modelos matemáticos do cérebro são chamados de **redes neurais**.

> Às vezes, redes neurais são chamadas de *Redes Neurais Artificiais*, RNAs, para indicar que estamos falando de modelos, não de redes reais de neurônios.

## Aprendizado de Máquina

Redes Neurais são parte de uma disciplina maior chamada **Aprendizado de Máquina**, cujo objetivo é usar dados para treinar modelos computacionais capazes de resolver problemas. Aprendizado de Máquina constitui uma grande parte da Inteligência Artificial, entretanto, não cobrimos aprendizado de máquina clássico neste currículo.

> Visite nosso currículo separado **[Aprendizado de Máquina para Iniciantes](http://github.com/microsoft/ml-for-beginners)** para saber mais sobre aprendizado de máquina clássico.

Em Aprendizado de Máquina, assumimos que temos um conjunto de dados com exemplos **X**, e valores correspondentes de saída **Y**. Os exemplos são frequentemente vetores N-dimensionais que consistem em **características**, e as saídas são chamadas de **rótulos**.

Nós consideraremos os dois problemas de aprendizado de máquina mais comuns:

* **Classificação**, onde precisamos classificar um objeto de entrada em duas ou mais classes.
* **Regressão**, onde precisamos prever um número numérico para cada uma das amostras de entrada.

> Ao representar entradas e saídas como tensores, o conjunto de dados de entrada é uma matriz de tamanho M&times;N, onde M é o número de amostras e N é o número de características. Os rótulos de saída Y são o vetor de tamanho M.

Neste currículo, focaremos apenas em modelos de redes neurais.

## Um Modelo de um Neurônio

Pela biologia, sabemos que nosso cérebro consiste em células neurais (neurônios), cada uma delas tendo múltiplas "entradas" (dendritos) e uma única "saída" (axônio). Tanto dendritos quanto axônios podem conduzir sinais elétricos, e as conexões entre eles — conhecidas como sinapses — podem exibir diferentes graus de condutividade, que são reguladas por neurotransmissores.

![Modelo de um Neurônio](../../../../translated_images/pt-BR/synapse-wikipedia.ed20a9e4726ea1c6.webp) | ![Modelo de um Neurônio](../../../../translated_images/pt-BR/artneuron.1a5daa88d20ebe6f.webp)
----|----
Neurônio Real *([Imagem](https://en.wikipedia.org/wiki/Synapse#/media/File:SynapseSchematic_lines.svg) da Wikipedia)* | Neurônio Artificial *(Imagem do Autor)*

Assim, o modelo matemático mais simples de um neurônio contém várias entradas X<sub>1</sub>, ..., X<sub>N</sub> e uma saída Y, e uma série de pesos W<sub>1</sub>, ..., W<sub>N</sub>. Uma saída é calculada como:

<img src="../../../../translated_images/pt-BR/netout.1eb15eb76fd76731.webp" alt="Y = f\left(\sum_{i=1}^N X_iW_i\right)" width="131" height="53" align="center"/>

onde f é alguma **função de ativação** não linear.

> Modelos iniciais de neurônio foram descritos no artigo clássico [A logical calculus of the ideas immanent in nervous activity](https://www.cs.cmu.edu/~./epxing/Class/10715/reading/McCulloch.and.Pitts.pdf) por Warren McCullock e Walter Pitts em 1943. Donald Hebb, em seu livro "[The Organization of Behavior: A Neuropsychological Theory](https://books.google.com/books?id=VNetYrB8EBoC)", propôs a maneira pela qual essas redes podem ser treinadas.

## Nesta Seção

Nesta seção iremos aprender sobre:
* [Perceptron](03-Perceptron/README.md), um dos primeiros modelos de redes neurais para classificação binária
* [Redes multicamadas](04-OwnFramework/README.md) com um notebook pareado [como construir nosso próprio framework](04-OwnFramework/OwnFramework.ipynb)
* [Frameworks de Redes Neurais](05-Frameworks/README.md), com estes notebooks: [PyTorch](05-Frameworks/IntroPyTorch.ipynb) e [Keras/Tensorflow](05-Frameworks/IntroKerasTF.ipynb)
* [Overfitting](../../../../lessons/3-NeuralNetworks/05-Frameworks#overfitting)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Aviso Legal**:
Este documento foi traduzido usando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos pela precisão, por favor, esteja ciente de que traduções automatizadas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes do uso desta tradução.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->