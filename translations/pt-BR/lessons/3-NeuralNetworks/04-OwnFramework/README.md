# Introdução às Redes Neurais. Perceptron Multicamadas

Na seção anterior, você aprendeu sobre o modelo de rede neural mais simples - o perceptron de uma camada, um modelo linear de classificação de duas classes.

Nesta seção, vamos expandir esse modelo para um framework mais flexível, permitindo:

* realizar **classificação multiclasse** além de classificação de duas classes
* resolver **problemas de regressão** além de classificação
* separar classes que não são linearmente separáveis

Também desenvolveremos nosso próprio framework modular em Python que nos permitirá construir diferentes arquiteturas de redes neurais.

## [Quiz pré-aula](https://ff-quizzes.netlify.app/en/ai/quiz/7)

## Formalização de Aprendizado de Máquina

Vamos começar formalizando o problema de Aprendizado de Máquina. Suponha que temos um conjunto de dados de treinamento **X** com rótulos **Y**, e precisamos construir um modelo *f* que faça previsões mais precisas. A qualidade das previsões é medida pela **função de perda** &lagran;. As seguintes funções de perda são frequentemente usadas:

* Para problemas de regressão, quando precisamos prever um número, podemos usar **erro absoluto** &sum;<sub>i</sub>|f(x<sup>(i)</sup>)-y<sup>(i)</sup>|, ou **erro quadrático** &sum;<sub>i</sub>(f(x<sup>(i)</sup>)-y<sup>(i)</sup>)<sup>2</sup>
* Para classificação, usamos **perda 0-1** (que é essencialmente o mesmo que **acurácia** do modelo), ou **perda logística**.

Para o perceptron de uma camada, a função *f* foi definida como uma função linear *f(x)=wx+b* (aqui *w* é a matriz de pesos, *x* é o vetor de características de entrada, e *b* é o vetor de viés). Para diferentes arquiteturas de redes neurais, essa função pode assumir uma forma mais complexa.

> No caso de classificação, muitas vezes é desejável obter probabilidades das classes correspondentes como saída da rede. Para converter números arbitrários em probabilidades (por exemplo, para normalizar a saída), frequentemente usamos a função **softmax** &sigma;, e a função *f* torna-se *f(x)=&sigma;(wx+b)*

Na definição de *f* acima, *w* e *b* são chamados de **parâmetros** &theta;=⟨*w,b*⟩. Dado o conjunto de dados ⟨**X**,**Y**⟩, podemos calcular um erro geral em todo o conjunto de dados como uma função dos parâmetros &theta;.

> ✅ **O objetivo do treinamento de redes neurais é minimizar o erro variando os parâmetros &theta;**

## Otimização por Gradiente Descendente

Existe um método bem conhecido de otimização de funções chamado **gradiente descendente**. A ideia é que podemos calcular uma derivada (no caso multidimensional chamada de **gradiente**) da função de perda em relação aos parâmetros e variar os parâmetros de forma que o erro diminua. Isso pode ser formalizado da seguinte maneira:

* Inicializar os parâmetros com alguns valores aleatórios w<sup>(0)</sup>, b<sup>(0)</sup>
* Repetir o seguinte passo várias vezes:
    - w<sup>(i+1)</sup> = w<sup>(i)</sup>-&eta;&part;&lagran;/&part;w
    - b<sup>(i+1)</sup> = b<sup>(i)</sup>-&eta;&part;&lagran;/&part;b

Durante o treinamento, os passos de otimização devem ser calculados considerando todo o conjunto de dados (lembre-se de que a perda é calculada como uma soma de todas as amostras de treinamento). No entanto, na prática, usamos pequenas porções do conjunto de dados chamadas **minibatches**, e calculamos os gradientes com base em um subconjunto de dados. Como o subconjunto é escolhido aleatoriamente a cada vez, esse método é chamado de **gradiente descendente estocástico** (SGD).

## Perceptrons Multicamadas e Retropropagação

A rede de uma camada, como vimos acima, é capaz de classificar classes linearmente separáveis. Para construir um modelo mais rico, podemos combinar várias camadas da rede. Matematicamente, isso significaria que a função *f* teria uma forma mais complexa e seria calculada em várias etapas:
* z<sub>1</sub>=w<sub>1</sub>x+b<sub>1</sub>
* z<sub>2</sub>=w<sub>2</sub>&alpha;(z<sub>1</sub>)+b<sub>2</sub>
* f = &sigma;(z<sub>2</sub>)

Aqui, &alpha; é uma **função de ativação não linear**, &sigma; é uma função softmax, e os parâmetros &theta;=<*w<sub>1</sub>,b<sub>1</sub>,w<sub>2</sub>,b<sub>2</sub>*>.

O algoritmo de gradiente descendente permaneceria o mesmo, mas seria mais difícil calcular os gradientes. Dado o princípio da regra da cadeia de diferenciação, podemos calcular as derivadas como:

* &part;&lagran;/&part;w<sub>2</sub> = (&part;&lagran;/&part;&sigma;)(&part;&sigma;/&part;z<sub>2</sub>)(&part;z<sub>2</sub>/&part;w<sub>2</sub>)
* &part;&lagran;/&part;w<sub>1</sub> = (&part;&lagran;/&part;&sigma;)(&part;&sigma;/&part;z<sub>2</sub>)(&part;z<sub>2</sub>/&part;&alpha;)(&part;&alpha;/&part;z<sub>1</sub>)(&part;z<sub>1</sub>/&part;w<sub>1</sub>)

> ✅ A regra da cadeia de diferenciação é usada para calcular as derivadas da função de perda em relação aos parâmetros.

Note que a parte mais à esquerda de todas essas expressões é a mesma, e assim podemos calcular as derivadas de forma eficiente começando pela função de perda e indo "para trás" através do grafo computacional. Assim, o método de treinamento de um perceptron multicamadas é chamado de **retropropagação**, ou 'backprop'.

<img alt="grafo computacional" src="../../../../../translated_images/pt-BR/ComputeGraphGrad.4626252c0de03507.webp"/>

> TODO: citação da imagem

> ✅ Vamos abordar a retropropagação com muito mais detalhes em nosso exemplo no notebook.  

## Conclusão

Nesta lição, construímos nossa própria biblioteca de redes neurais e a usamos para uma tarefa simples de classificação bidimensional.

## 🚀 Desafio

No notebook que acompanha, você implementará seu próprio framework para construir e treinar perceptrons multicamadas. Você poderá ver em detalhes como as redes neurais modernas operam.

Acesse o notebook [OwnFramework](OwnFramework.ipynb) e trabalhe nele.

## [Quiz pós-aula](https://ff-quizzes.netlify.app/en/ai/quiz/8)

## Revisão e Autoestudo

Retropropagação é um algoritmo comum usado em IA e ML, vale a pena estudar [em mais detalhes](https://wikipedia.org/wiki/Backpropagation)

## [Tarefa](lab/README.md)

Neste laboratório, você será solicitado a usar o framework que construiu nesta lição para resolver a classificação de dígitos manuscritos do MNIST.

* [Instruções](lab/README.md)
* [Notebook](lab/MyFW_MNIST.ipynb)

---

