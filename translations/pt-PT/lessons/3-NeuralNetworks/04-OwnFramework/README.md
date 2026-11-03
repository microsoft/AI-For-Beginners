# Introdução às Redes Neuronais. Perceptrão Multicamadas

Na secção anterior, aprendeste sobre o modelo mais simples de rede neuronal - o perceptrão de uma camada, um modelo linear de classificação de duas classes.

Nesta secção, vamos expandir este modelo para um framework mais flexível, permitindo-nos:

* realizar **classificação de múltiplas classes** além de duas classes
* resolver **problemas de regressão** além de classificação
* separar classes que não são linearmente separáveis

Também iremos desenvolver o nosso próprio framework modular em Python, que nos permitirá construir diferentes arquiteturas de redes neuronais.

## [Questionário pré-aula](https://ff-quizzes.netlify.app/en/ai/quiz/7)

## Formalização de Aprendizagem Automática

Vamos começar por formalizar o problema de Aprendizagem Automática. Suponhamos que temos um conjunto de dados de treino **X** com etiquetas **Y**, e precisamos construir um modelo *f* que faça previsões o mais precisas possível. A qualidade das previsões é medida pela **função de perda** &lagran;. As seguintes funções de perda são frequentemente utilizadas:

* Para problemas de regressão, quando precisamos prever um número, podemos usar **erro absoluto** &sum;<sub>i</sub>|f(x<sup>(i)</sup>)-y<sup>(i)</sup>|, ou **erro quadrático** &sum;<sub>i</sub>(f(x<sup>(i)</sup>)-y<sup>(i)</sup>)<sup>2</sup>
* Para classificação, usamos **perda 0-1** (que é essencialmente o mesmo que **precisão** do modelo), ou **perda logística**.

Para o perceptrão de uma camada, a função *f* foi definida como uma função linear *f(x)=wx+b* (aqui *w* é a matriz de pesos, *x* é o vetor de características de entrada, e *b* é o vetor de bias). Para diferentes arquiteturas de redes neuronais, esta função pode assumir uma forma mais complexa.

> No caso de classificação, é frequentemente desejável obter probabilidades das classes correspondentes como saída da rede. Para converter números arbitrários em probabilidades (por exemplo, para normalizar a saída), usamos frequentemente a função **softmax** &sigma;, e a função *f* torna-se *f(x)=&sigma;(wx+b)*

Na definição de *f* acima, *w* e *b* são chamados **parâmetros** &theta;=⟨*w,b*⟩. Dado o conjunto de dados ⟨**X**,**Y**⟩, podemos calcular um erro geral em todo o conjunto de dados como uma função dos parâmetros &theta;.

> ✅ **O objetivo do treino de redes neuronais é minimizar o erro variando os parâmetros &theta;**

## Otimização por Gradiente Descendente

Existe um método bem conhecido de otimização de funções chamado **gradiente descendente**. A ideia é que podemos calcular uma derivada (no caso multidimensional chamada **gradiente**) da função de perda em relação aos parâmetros, e variar os parâmetros de forma que o erro diminua. Isto pode ser formalizado da seguinte forma:

* Inicializar os parâmetros com alguns valores aleatórios w<sup>(0)</sup>, b<sup>(0)</sup>
* Repetir o seguinte passo várias vezes:
    - w<sup>(i+1)</sup> = w<sup>(i)</sup>-&eta;&part;&lagran;/&part;w
    - b<sup>(i+1)</sup> = b<sup>(i)</sup>-&eta;&part;&lagran;/&part;b

Durante o treino, os passos de otimização devem ser calculados considerando todo o conjunto de dados (lembra-te que a perda é calculada como uma soma através de todas as amostras de treino). No entanto, na prática, usamos pequenas porções do conjunto de dados chamadas **minibatches**, e calculamos os gradientes com base num subconjunto de dados. Como o subconjunto é escolhido aleatoriamente cada vez, tal método é chamado **gradiente descendente estocástico** (SGD).

## Perceptrões Multicamadas e Retropropagação

A rede de uma camada, como vimos acima, é capaz de classificar classes linearmente separáveis. Para construir um modelo mais rico, podemos combinar várias camadas da rede. Matematicamente, isso significaria que a função *f* teria uma forma mais complexa e seria calculada em vários passos:
* z<sub>1</sub>=w<sub>1</sub>x+b<sub>1</sub>
* z<sub>2</sub>=w<sub>2</sub>&alpha;(z<sub>1</sub>)+b<sub>2</sub>
* f = &sigma;(z<sub>2</sub>)

Aqui, &alpha; é uma **função de ativação não linear**, &sigma; é uma função softmax, e os parâmetros &theta;=<*w<sub>1</sub>,b<sub>1</sub>,w<sub>2</sub>,b<sub>2</sub>*>.

O algoritmo de gradiente descendente permaneceria o mesmo, mas seria mais difícil calcular os gradientes. Dado o princípio da regra da cadeia de diferenciação, podemos calcular as derivadas como:

* &part;&lagran;/&part;w<sub>2</sub> = (&part;&lagran;/&part;&sigma;)(&part;&sigma;/&part;z<sub>2</sub>)(&part;z<sub>2</sub>/&part;w<sub>2</sub>)
* &part;&lagran;/&part;w<sub>1</sub> = (&part;&lagran;/&part;&sigma;)(&part;&sigma;/&part;z<sub>2</sub>)(&part;z<sub>2</sub>/&part;&alpha;)(&part;&alpha;/&part;z<sub>1</sub>)(&part;z<sub>1</sub>/&part;w<sub>1</sub>)

> ✅ A regra da cadeia de diferenciação é usada para calcular as derivadas da função de perda em relação aos parâmetros.

Nota que a parte mais à esquerda de todas essas expressões é a mesma, e assim podemos calcular eficazmente as derivadas começando pela função de perda e indo "para trás" através do gráfico computacional. Assim, o método de treino de um perceptrão multicamadas é chamado **retropropagação**, ou 'backprop'.

<img alt="compute graph" src="../../../../../translated_images/pt-PT/ComputeGraphGrad.4626252c0de03507.webp"/>

> Image by [Dmitry Soshnikov](http://soshnikov.com)

> ✅ Vamos abordar a retropropagação com muito mais detalhe no nosso exemplo em notebook.  

## Conclusão

Nesta aula, construímos a nossa própria biblioteca de redes neuronais e utilizámo-la para uma tarefa simples de classificação bidimensional.

## 🚀 Desafio

No notebook que acompanha, vais implementar o teu próprio framework para construir e treinar perceptrões multicamadas. Vais poder ver em detalhe como funcionam as redes neuronais modernas.

Segue para o notebook [OwnFramework](OwnFramework.ipynb) e trabalha nele.

## [Questionário pós-aula](https://ff-quizzes.netlify.app/en/ai/quiz/8)

## Revisão e Estudo Autónomo

A retropropagação é um algoritmo comum usado em IA e ML, vale a pena estudar [em mais detalhe](https://wikipedia.org/wiki/Backpropagation)

## [Tarefa](lab/README.md)

Neste laboratório, és convidado a usar o framework que construíste nesta aula para resolver a classificação de dígitos manuscritos MNIST.

* [Instruções](lab/README.md)
* [Notebook](lab/MyFW_MNIST.ipynb)

---

