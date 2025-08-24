<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "186bf7eeab776b36f557357ea56d4751",
  "translation_date": "2025-08-24T09:03:57+00:00",
  "source_file": "lessons/3-NeuralNetworks/04-OwnFramework/README.md",
  "language_code": "pt"
}
-->
# Introdução às Redes Neuronais. Perceptrão Multicamadas

Na secção anterior, aprendeste sobre o modelo mais simples de rede neuronal - o perceptrão de uma camada, um modelo linear de classificação de duas classes.

Nesta secção, iremos expandir este modelo para um framework mais flexível, permitindo-nos:

* realizar **classificação multiclasse** além de classificação de duas classes
* resolver **problemas de regressão** além de classificação
* separar classes que não são linearmente separáveis

Também iremos desenvolver o nosso próprio framework modular em Python que nos permitirá construir diferentes arquiteturas de redes neuronais.

## [Questionário pré-aula](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/104)

## Formalização de Aprendizagem Automática

Vamos começar por formalizar o problema de Aprendizagem Automática. Suponhamos que temos um conjunto de dados de treino **X** com etiquetas **Y**, e precisamos construir um modelo *f* que faça previsões o mais precisas possível. A qualidade das previsões é medida pela **função de perda** ℒ. As seguintes funções de perda são frequentemente utilizadas:

* Para problemas de regressão, quando precisamos prever um número, podemos usar **erro absoluto** ∑<sub>i</sub>|f(x<sup>(i)</sup>)-y<sup>(i)</sup>|, ou **erro quadrático** ∑<sub>i</sub>(f(x<sup>(i)</sup>)-y<sup>(i)</sup>)<sup>2</sup>
* Para classificação, usamos **perda 0-1** (que é essencialmente o mesmo que **precisão** do modelo), ou **perda logística**.

Para o perceptrão de uma camada, a função *f* foi definida como uma função linear *f(x)=wx+b* (aqui *w* é a matriz de pesos, *x* é o vetor de características de entrada, e *b* é o vetor de bias). Para diferentes arquiteturas de redes neuronais, esta função pode assumir uma forma mais complexa.

> No caso de classificação, é frequentemente desejável obter probabilidades das classes correspondentes como saída da rede. Para converter números arbitrários em probabilidades (por exemplo, para normalizar a saída), usamos frequentemente a função **softmax** σ, e a função *f* torna-se *f(x)=σ(wx+b)*

Na definição de *f* acima, *w* e *b* são chamados de **parâmetros** θ=⟨*w,b*⟩. Dado o conjunto de dados ⟨**X**,**Y**⟩, podemos calcular o erro geral em todo o conjunto de dados como uma função dos parâmetros θ.

> ✅ **O objetivo do treino de redes neuronais é minimizar o erro variando os parâmetros θ**

## Otimização por Gradiente Descendente

Existe um método bem conhecido de otimização de funções chamado **gradiente descendente**. A ideia é que podemos calcular uma derivada (no caso multidimensional chamada de **gradiente**) da função de perda em relação aos parâmetros, e variar os parâmetros de forma que o erro diminua. Isto pode ser formalizado da seguinte forma:

* Inicializar os parâmetros com alguns valores aleatórios w<sup>(0)</sup>, b<sup>(0)</sup>
* Repetir o seguinte passo várias vezes:
    - w<sup>(i+1)</sup> = w<sup>(i)</sup>-η∂ℒ/∂w
    - b<sup>(i+1)</sup> = b<sup>(i)</sup>-η∂ℒ/∂b

Durante o treino, os passos de otimização devem ser calculados considerando todo o conjunto de dados (lembra-te que a perda é calculada como uma soma de todas as amostras de treino). No entanto, na prática, usamos pequenas porções do conjunto de dados chamadas **minibatches**, e calculamos os gradientes com base num subconjunto de dados. Como o subconjunto é escolhido aleatoriamente a cada vez, este método é chamado de **gradiente descendente estocástico** (SGD).

## Perceptrões Multicamadas e Retropropagação

Uma rede de uma camada, como vimos acima, é capaz de classificar classes linearmente separáveis. Para construir um modelo mais rico, podemos combinar várias camadas da rede. Matematicamente, isso significaria que a função *f* teria uma forma mais complexa e seria calculada em vários passos:
* z<sub>1</sub>=w<sub>1</sub>x+b<sub>1</sub>
* z<sub>2</sub>=w<sub>2</sub>α(z<sub>1</sub>)+b<sub>2</sub>
* f = σ(z<sub>2</sub>)

Aqui, α é uma **função de ativação não linear**, σ é uma função softmax, e os parâmetros θ=<*w<sub>1</sub>,b<sub>1</sub>,w<sub>2</sub>,b<sub>2</sub>*>.

O algoritmo de gradiente descendente permaneceria o mesmo, mas seria mais difícil calcular os gradientes. Dado o princípio da regra da cadeia de diferenciação, podemos calcular as derivadas como:

* ∂ℒ/∂w<sub>2</sub> = (∂ℒ/∂σ)(∂σ/∂z<sub>2</sub>)(∂z<sub>2</sub>/∂w<sub>2</sub>)
* ∂ℒ/∂w<sub>1</sub> = (∂ℒ/∂σ)(∂σ/∂z<sub>2</sub>)(∂z<sub>2</sub>/∂α)(∂α/∂z<sub>1</sub>)(∂z<sub>1</sub>/∂w<sub>1</sub>)

> ✅ A regra da cadeia de diferenciação é usada para calcular as derivadas da função de perda em relação aos parâmetros.

Nota que a parte mais à esquerda de todas essas expressões é a mesma, e assim podemos calcular as derivadas de forma eficiente começando pela função de perda e indo "para trás" através do gráfico computacional. Assim, o método de treino de um perceptrão multicamadas é chamado de **retropropagação**, ou 'backprop'.

<img alt="compute graph" src="images/ComputeGraphGrad.png"/>

> TODO: citação da imagem

> ✅ Vamos abordar a retropropagação com muito mais detalhe no nosso exemplo no notebook.  

## Conclusão

Nesta lição, construímos a nossa própria biblioteca de redes neuronais e utilizámo-la para uma tarefa simples de classificação bidimensional.

## 🚀 Desafio

No notebook que acompanha, vais implementar o teu próprio framework para construir e treinar perceptrões multicamadas. Vais poder ver em detalhe como funcionam as redes neuronais modernas.

Segue para o notebook [OwnFramework](../../../../../lessons/3-NeuralNetworks/04-OwnFramework/OwnFramework.ipynb) e trabalha nele.

## [Questionário pós-aula](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/204)

## Revisão & Estudo Autónomo

A retropropagação é um algoritmo comum usado em IA e ML, vale a pena estudá-lo [em mais detalhe](https://wikipedia.org/wiki/Backpropagation)

## [Tarefa](lab/README.md)

Neste laboratório, és convidado a usar o framework que construíste nesta lição para resolver a classificação de dígitos manuscritos do MNIST.

* [Instruções](lab/README.md)
* [Notebook](../../../../../lessons/3-NeuralNetworks/04-OwnFramework/lab/MyFW_MNIST.ipynb)

**Aviso Legal**:  
Este documento foi traduzido utilizando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos para garantir a precisão, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original no seu idioma nativo deve ser considerado a fonte autoritativa. Para informações críticas, recomenda-se uma tradução profissional realizada por humanos. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas resultantes do uso desta tradução.