# Introdução às Redes Neurais: Perceptron

## [Quiz pré-aula](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/103)

Uma das primeiras tentativas de implementar algo semelhante a uma rede neural moderna foi feita por Frank Rosenblatt, do Cornell Aeronautical Laboratory, em 1957. Foi uma implementação de hardware chamada "Mark-1", projetada para reconhecer figuras geométricas primitivas, como triângulos, quadrados e círculos.

|      |      |
|--------------|-----------|
|<img src='images/Rosenblatt-wikipedia.jpg' alt='Frank Rosenblatt'/> | <img src='images/Mark_I_perceptron_wikipedia.jpg' alt='The Mark 1 Perceptron' />|

> Imagens [da Wikipedia](https://en.wikipedia.org/wiki/Perceptron)

Uma imagem de entrada era representada por uma matriz de fotocélulas de 20x20, então a rede neural tinha 400 entradas e uma saída binária. Uma rede simples continha um neurônio, também chamado de **unidade lógica de limiar**. Os pesos da rede neural agiam como potenciômetros que exigiam ajuste manual durante a fase de treinamento.

> ✅ Um potenciômetro é um dispositivo que permite ao usuário ajustar a resistência de um circuito.

> O New York Times escreveu sobre o perceptron na época: *o embrião de um computador eletrônico que [a Marinha] espera que possa andar, falar, ver, escrever, se reproduzir e estar consciente de sua existência.*

## Modelo Perceptron

Suponha que temos N características em nosso modelo, nesse caso, o vetor de entrada seria um vetor de tamanho N. Um perceptron é um modelo de **classificação binária**, ou seja, pode distinguir entre duas classes de dados de entrada. Vamos supor que, para cada vetor de entrada x, a saída do nosso perceptron seria +1 ou -1, dependendo da classe. A saída será calculada usando a fórmula:

y(x) = f(w<sup>T</sup>x)

onde f é uma função de ativação em degrau

<!-- img src="http://www.sciweavers.org/tex2img.php?eq=f%28x%29%20%3D%20%5Cbegin%7Bcases%7D%0A%20%20%20%20%20%20%20%20%20%2B1%20%26%20x%20%5Cgeq%200%20%5C%5C%0A%20%20%20%20%20%20%20%20%20-1%20%26%20x%20%3C%200%0A%20%20%20%20%20%20%20%5Cend%7Bcases%7D%20%5C%5C%0A&bc=White&fc=Black&im=jpg&fs=12&ff=arev&edit=0" align="center" border="0" alt="f(x) = \begin{cases} +1 & x \geq 0 \\ -1 & x < 0 \end{cases} \\" width="154" height="50" / -->
<img src="images/activation-func.png"/>

## Treinando o Perceptron

Para treinar um perceptron, precisamos encontrar um vetor de pesos w que classifique a maioria dos valores corretamente, ou seja, resulte no menor **erro**. Este erro E é definido pelo **critério do perceptron** da seguinte maneira:

E(w) = -∑w<sup>T</sup>x<sub>i</sub>t<sub>i</sub>

onde:

* a soma é feita sobre aqueles pontos de dados de treinamento i que resultam em classificação errada
* x<sub>i</sub> é o dado de entrada, e t<sub>i</sub> é -1 ou +1 para exemplos negativos e positivos, respectivamente.

Este critério é considerado uma função dos pesos w, e precisamos minimizá-lo. Muitas vezes, um método chamado **descida do gradiente** é utilizado, no qual começamos com alguns pesos iniciais w<sup>(0)</sup>, e então, a cada passo, atualizamos os pesos de acordo com a fórmula:

w<sup>(t+1)</sup> = w<sup>(t)</sup> - η∇E(w)

Aqui, η é a chamada **taxa de aprendizado**, e ∇E(w) denota o **gradiente** de E. Depois de calcular o gradiente, terminamos com

w<sup>(t+1)</sup> = w<sup>(t)</sup> + ∑ηx<sub>i</sub>t<sub>i</sub>

O algoritmo em Python se parece com isso:

```python
def train(positive_examples, negative_examples, num_iterations = 100, eta = 1):

    weights = [0,0,0] # Initialize weights (almost randomly :)
        
    for i in range(num_iterations):
        pos = random.choice(positive_examples)
        neg = random.choice(negative_examples)

        z = np.dot(pos, weights) # compute perceptron output
        if z < 0: # positive example classified as negative
            weights = weights + eta*weights.shape

        z  = np.dot(neg, weights)
        if z >= 0: # negative example classified as positive
            weights = weights - eta*weights.shape

    return weights
```

## Conclusão

Nesta lição, você aprendeu sobre um perceptron, que é um modelo de classificação binária, e como treiná-lo usando um vetor de pesos.

## 🚀 Desafio

Se você gostaria de tentar construir seu próprio perceptron, experimente [este laboratório no Microsoft Learn](https://docs.microsoft.com/en-us/azure/machine-learning/component-reference/two-class-averaged-perceptron?WT.mc_id=academic-77998-cacaste) que usa o [Azure ML designer](https://docs.microsoft.com/en-us/azure/machine-learning/concept-designer?WT.mc_id=academic-77998-cacaste).

## [Quiz pós-aula](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/203)

## Revisão & Autoestudo

Para ver como podemos usar o perceptron para resolver um problema simples, bem como problemas da vida real, e para continuar aprendendo - vá para o caderno [Perceptron](../../../../../lessons/3-NeuralNetworks/03-Perceptron/Perceptron.ipynb).

Aqui está um [artigo interessante sobre perceptrons](https://towardsdatascience.com/what-is-a-perceptron-basics-of-neural-networks-c4cfea20c590) também.

## [Tarefa](lab/README.md)

Nesta lição, implementamos um perceptron para a tarefa de classificação binária e o usamos para classificar entre dois dígitos manuscritos. Neste laboratório, você é solicitado a resolver o problema de classificação de dígitos completamente, ou seja, determinar qual dígito é mais provável que corresponda a uma determinada imagem.

* [Instruções](lab/README.md)
* [Caderno](../../../../../lessons/3-NeuralNetworks/03-Perceptron/lab/PerceptronMultiClass.ipynb)

**Isenção de responsabilidade**:  
Este documento foi traduzido usando serviços de tradução automática baseados em IA. Embora nos esforcemos pela precisão, esteja ciente de que traduções automatizadas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte autoritativa. Para informações críticas, recomenda-se a tradução profissional realizada por humanos. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações errôneas decorrentes do uso desta tradução.