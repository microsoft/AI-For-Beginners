<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "186bf7eeab776b36f557357ea56d4751",
  "translation_date": "2025-08-26T10:28:29+00:00",
  "source_file": "lessons/3-NeuralNetworks/04-OwnFramework/README.md",
  "language_code": "br"
}
-->
# Introdução às Redes Neurais. Perceptron Multicamadas

Na seção anterior, você aprendeu sobre o modelo mais simples de rede neural - o perceptron de uma camada, um modelo linear de classificação para duas classes.

Nesta seção, vamos expandir esse modelo para um framework mais flexível, permitindo-nos:

* realizar **classificação multiclasse** além da classificação de duas classes  
* resolver **problemas de regressão** além da classificação  
* separar classes que não são linearmente separáveis  

Também desenvolveremos nosso próprio framework modular em Python, que nos permitirá construir diferentes arquiteturas de redes neurais.

## [Questionário pré-aula](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/104)

## Formalização de Aprendizado de Máquina

Vamos começar formalizando o problema de Aprendizado de Máquina. Suponha que temos um conjunto de dados de treinamento **X** com rótulos **Y**, e precisamos construir um modelo *f* que faça previsões mais precisas. A qualidade das previsões é medida pela **função de perda** ℒ. As seguintes funções de perda são frequentemente usadas:

* Para problemas de regressão, quando precisamos prever um número, podemos usar o **erro absoluto** ∑<sub>i</sub>|f(x<sup>(i)</sup>)-y<sup>(i)</sup>| ou o **erro quadrático** ∑<sub>i</sub>(f(x<sup>(i)</sup>)-y<sup>(i)</sup>)<sup>2</sup>  
* Para classificação, usamos a **perda 0-1** (que é essencialmente o mesmo que a **acurácia** do modelo) ou a **perda logística**.

Para o perceptron de uma camada, a função *f* foi definida como uma função linear *f(x)=wx+b* (aqui *w* é a matriz de pesos, *x* é o vetor de características de entrada e *b* é o vetor de viés). Para diferentes arquiteturas de redes neurais, essa função pode assumir uma forma mais complexa.

> No caso de classificação, muitas vezes é desejável obter probabilidades das classes correspondentes como saída da rede. Para converter números arbitrários em probabilidades (por exemplo, para normalizar a saída), frequentemente usamos a função **softmax** σ, e a função *f* torna-se *f(x)=σ(wx+b)*.

Na definição de *f* acima, *w* e *b* são chamados de **parâmetros** θ=⟨*w,b*⟩. Dado o conjunto de dados ⟨**X**,**Y**⟩, podemos calcular um erro geral em todo o conjunto de dados como uma função dos parâmetros θ.

> ✅ **O objetivo do treinamento de redes neurais é minimizar o erro variando os parâmetros θ**

## Otimização por Gradiente Descendente

Existe um método bem conhecido de otimização de funções chamado **gradiente descendente**. A ideia é que podemos calcular a derivada (no caso multidimensional chamada de **gradiente**) da função de perda em relação aos parâmetros e variar os parâmetros de forma que o erro diminua. Isso pode ser formalizado da seguinte maneira:

* Inicialize os parâmetros com alguns valores aleatórios w<sup>(0)</sup>, b<sup>(0)</sup>  
* Repita o seguinte passo várias vezes:  
    - w<sup>(i+1)</sup> = w<sup>(i)</sup>-η∂ℒ/∂w  
    - b<sup>(i+1)</sup> = b<sup>(i)</sup>-η∂ℒ/∂b  

Durante o treinamento, os passos de otimização devem ser calculados considerando todo o conjunto de dados (lembre-se de que a perda é calculada como uma soma de todas as amostras de treinamento). No entanto, na prática, usamos pequenas porções do conjunto de dados chamadas **minilotes**, e calculamos os gradientes com base em um subconjunto de dados. Como o subconjunto é escolhido aleatoriamente a cada vez, esse método é chamado de **gradiente descendente estocástico** (SGD).

## Perceptrons Multicamadas e Retropropagação

A rede de uma camada, como vimos acima, é capaz de classificar classes linearmente separáveis. Para construir um modelo mais rico, podemos combinar várias camadas da rede. Matematicamente, isso significa que a função *f* terá uma forma mais complexa e será calculada em várias etapas:  
* z<sub>1</sub>=w<sub>1</sub>x+b<sub>1</sub>  
* z<sub>2</sub>=w<sub>2</sub>α(z<sub>1</sub>)+b<sub>2</sub>  
* f = σ(z<sub>2</sub>)  

Aqui, α é uma **função de ativação não linear**, σ é uma função softmax, e os parâmetros θ=<*w<sub>1</sub>,b<sub>1</sub>,w<sub>2</sub>,b<sub>2</sub>*>.

O algoritmo de gradiente descendente permaneceria o mesmo, mas calcular os gradientes seria mais difícil. Dado o princípio da regra da cadeia de diferenciação, podemos calcular as derivadas como:

* ∂ℒ/∂w<sub>2</sub> = (∂ℒ/∂σ)(∂σ/∂z<sub>2</sub>)(∂z<sub>2</sub>/∂w<sub>2</sub>)  
* ∂ℒ/∂w<sub>1</sub> = (∂ℒ/∂σ)(∂σ/∂z<sub>2</sub>)(∂z<sub>2</sub>/∂α)(∂α/∂z<sub>1</sub>)(∂z<sub>1</sub>/∂w<sub>1</sub>)  

> ✅ A regra da cadeia de diferenciação é usada para calcular as derivadas da função de perda em relação aos parâmetros.

Observe que a parte mais à esquerda de todas essas expressões é a mesma, e assim podemos calcular as derivadas de forma eficiente começando pela função de perda e indo "para trás" através do grafo computacional. Assim, o método de treinamento de um perceptron multicamadas é chamado de **retropropagação**, ou 'backprop'.

<img alt="grafo computacional" src="images/ComputeGraphGrad.png"/>

> TODO: citação da imagem

> ✅ Vamos abordar a retropropagação com muito mais detalhes em nosso exemplo no notebook.

## Conclusão

Nesta lição, construímos nossa própria biblioteca de redes neurais e a utilizamos para uma tarefa simples de classificação bidimensional.

## 🚀 Desafio

No notebook que acompanha, você implementará seu próprio framework para construir e treinar perceptrons multicamadas. Você poderá ver em detalhes como as redes neurais modernas operam.

Acesse o notebook [OwnFramework](../../../../../lessons/3-NeuralNetworks/04-OwnFramework/OwnFramework.ipynb) e trabalhe nele.

## [Questionário pós-aula](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/204)

## Revisão e Autoestudo

A retropropagação é um algoritmo comum usado em IA e ML, valendo a pena estudá-lo [em mais detalhes](https://wikipedia.org/wiki/Backpropagation).

## [Tarefa](lab/README.md)

Neste laboratório, você será solicitado a usar o framework que construiu nesta lição para resolver a classificação de dígitos manuscritos do MNIST.

* [Instruções](lab/README.md)  
* [Notebook](../../../../../lessons/3-NeuralNetworks/04-OwnFramework/lab/MyFW_MNIST.ipynb)  

**Aviso Legal**:  
Este documento foi traduzido utilizando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos para garantir a precisão, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte oficial. Para informações críticas, recomenda-se a tradução profissional realizada por humanos. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações equivocadas decorrentes do uso desta tradução.