# Introdução às Redes Neuronais: Perceptron

## [Questionário pré-aula](https://ff-quizzes.netlify.app/en/ai/quiz/5)

Uma das primeiras tentativas de implementar algo semelhante a uma rede neuronal moderna foi realizada por Frank Rosenblatt, do Cornell Aeronautical Laboratory, em 1957. Tratava-se de uma implementação em hardware chamada "Mark-1", projetada para reconhecer figuras geométricas primitivas, como triângulos, quadrados e círculos.

|      |      |
|--------------|-----------|
|<img src='../../../../../translated_images/pt-PT/Rosenblatt-wikipedia.294821b285ac796d.webp' alt='Frank Rosenblatt'/> | <img src='../../../../../translated_images/pt-PT/Mark_I_perceptron_wikipedia.1f84eaa2d4b76ec9.webp' alt='O Perceptron Mark 1' />|

> Imagens [da Wikipédia](https://en.wikipedia.org/wiki/Perceptron)

Uma imagem de entrada era representada por uma matriz de fotocélulas de 20x20, de modo que a rede neuronal tinha 400 entradas e uma saída binária. Uma rede simples continha um único neurónio, também chamado de **unidade lógica de limiar**. Os pesos da rede neuronal funcionavam como potenciômetros que precisavam ser ajustados manualmente durante a fase de treino.

> ✅ Um potenciômetro é um dispositivo que permite ao utilizador ajustar a resistência de um circuito.

> O New York Times escreveu sobre o perceptron na época: *o embrião de um computador eletrónico que [a Marinha] espera que seja capaz de andar, falar, ver, escrever, reproduzir-se e ter consciência da sua existência.*

## Modelo de Perceptron

Suponha que temos N características no nosso modelo, caso em que o vetor de entrada seria um vetor de tamanho N. Um perceptron é um modelo de **classificação binária**, ou seja, consegue distinguir entre duas classes de dados de entrada. Vamos assumir que, para cada vetor de entrada x, a saída do nosso perceptron será +1 ou -1, dependendo da classe. A saída será calculada usando a fórmula:

y(x) = f(w<sup>T</sup>x)

onde f é uma função de ativação em degrau.

<!-- img src="http://www.sciweavers.org/tex2img.php?eq=f%28x%29%20%3D%20%5Cbegin%7Bcases%7D%0A%20%20%20%20%20%20%20%20%20%2B1%20%26%20x%20%5Cgeq%200%20%5C%5C%0A%20%20%20%20%20%20%20%20%20-1%20%26%20x%20%3C%200%0A%20%20%20%20%20%20%20%5Cend%7Bcases%7D%20%5C%5C%0A&bc=White&fc=Black&im=jpg&fs=12&ff=arev&edit=0" align="center" border="0" alt="f(x) = \begin{cases} +1 & x \geq 0 \\ -1 & x < 0 \end{cases} \\" width="154" height="50" / -->
<img src="../../../../../translated_images/pt-PT/activation-func.b4924007c7ce7764.webp"/>

## Treinar o Perceptron

Para treinar um perceptron, precisamos encontrar um vetor de pesos w que classifique a maioria dos valores corretamente, ou seja, que resulte no menor **erro**. Este erro E é definido pelo **critério do perceptron** da seguinte forma:

E(w) = -&sum;w<sup>T</sup>x<sub>i</sub>t<sub>i</sub>

onde:

* a soma é feita sobre os pontos de dados de treino i que resultam numa classificação errada;
* x<sub>i</sub> é o dado de entrada, e t<sub>i</sub> é -1 ou +1 para exemplos negativos e positivos, respetivamente.

Este critério é considerado como uma função dos pesos w, e precisamos minimizá-lo. Muitas vezes, utiliza-se um método chamado **descida do gradiente**, no qual começamos com alguns pesos iniciais w<sup>(0)</sup> e, em cada passo, atualizamos os pesos de acordo com a fórmula:

w<sup>(t+1)</sup> = w<sup>(t)</sup> - &eta;&nabla;E(w)

Aqui, &eta; é a chamada **taxa de aprendizagem**, e &nabla;E(w) denota o **gradiente** de E. Após calcularmos o gradiente, obtemos:

w<sup>(t+1)</sup> = w<sup>(t)</sup> + &sum;&eta;x<sub>i</sub>t<sub>i</sub>

O algoritmo em Python é assim:

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

Nesta lição, aprendeste sobre o perceptron, que é um modelo de classificação binária, e como treiná-lo utilizando um vetor de pesos.

## 🚀 Desafio

Se quiseres tentar construir o teu próprio perceptron, experimenta [este laboratório no Microsoft Learn](https://docs.microsoft.com/en-us/azure/machine-learning/component-reference/two-class-averaged-perceptron?WT.mc_id=academic-77998-cacaste), que utiliza o [Azure ML designer](https://docs.microsoft.com/en-us/azure/machine-learning/concept-designer?WT.mc_id=academic-77998-cacaste).

## [Questionário pós-aula](https://ff-quizzes.netlify.app/en/ai/quiz/6)

## Revisão e Autoestudo

Para ver como podemos usar o perceptron para resolver um problema simples, bem como problemas do mundo real, e para continuar a aprender, consulta o caderno [Perceptron](Perceptron.ipynb).

Aqui está também um [artigo interessante sobre perceptrons](https://towardsdatascience.com/what-is-a-perceptron-basics-of-neural-networks-c4cfea20c590).

## [Tarefa](lab/README.md)

Nesta lição, implementámos um perceptron para uma tarefa de classificação binária e utilizámo-lo para classificar entre dois dígitos manuscritos. Neste laboratório, és desafiado a resolver o problema de classificação de dígitos por completo, ou seja, determinar qual o dígito mais provável correspondente a uma imagem dada.

* [Instruções](lab/README.md)
* [Caderno](lab/PerceptronMultiClass.ipynb)

---

