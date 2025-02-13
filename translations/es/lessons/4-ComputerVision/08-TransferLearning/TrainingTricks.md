# Trucos de Entrenamiento en Aprendizaje Profundo

A medida que las redes neuronales se vuelven más profundas, el proceso de su entrenamiento se vuelve cada vez más desafiante. Un problema importante es el llamado [gradientes que se desvanecen](https://en.wikipedia.org/wiki/Vanishing_gradient_problem) o [gradientes que explotan](https://deepai.org/machine-learning-glossary-and-terms/exploding-gradient-problem#:~:text=Exploding%20gradients%20are%20a%20problem,updates%20are%20small%20and%20controlled.). [Esta publicación](https://towardsdatascience.com/the-vanishing-exploding-gradient-problem-in-deep-neural-networks-191358470c11) ofrece una buena introducción a estos problemas.

Para hacer que el entrenamiento de redes profundas sea más eficiente, se pueden utilizar algunas técnicas.

## Manteniendo valores en un intervalo razonable

Para hacer que los cálculos numéricos sean más estables, queremos asegurarnos de que todos los valores dentro de nuestra red neuronal estén en una escala razonable, típicamente [-1..1] o [0..1]. No es un requisito muy estricto, pero la naturaleza de los cálculos en punto flotante es tal que los valores de diferentes magnitudes no pueden ser manipulados con precisión juntos. Por ejemplo, si sumamos 10<sup>-10</sup> y 10<sup>10</sup>, probablemente obtendremos 10<sup>10</sup>, porque el valor más pequeño se "convertiría" al mismo orden que el mayor, y así se perdería la mantisa.

La mayoría de las funciones de activación tienen no linealidades alrededor de [-1..1], por lo que tiene sentido escalar todos los datos de entrada al intervalo [-1..1] o [0..1].

## Inicialización de Pesos Inicial

Idealmente, queremos que los valores estén en el mismo rango después de pasar a través de las capas de la red. Por lo tanto, es importante inicializar los pesos de tal manera que se preserve la distribución de valores.

La distribución normal **N(0,1)** no es una buena idea, porque si tenemos *n* entradas, la desviación estándar de la salida sería *n*, y los valores probablemente saldrían del intervalo [0..1].

Las siguientes inicializaciones son a menudo utilizadas:

 * Distribución uniforme -- `uniform`
 * **N(0,1/n)** -- `gaussian`
 * **N(0,1/√n_in)** garantiza que para entradas con media cero y desviación estándar de 1, la misma media/desviación estándar se mantendrá
 * **N(0,√2/(n_in+n_out))** -- la llamada **inicialización de Xavier** (`glorot`), ayuda a mantener las señales en rango durante la propagación hacia adelante y hacia atrás

## Normalización por Lotes

Incluso con una correcta inicialización de pesos, estos pueden volverse arbitrariamente grandes o pequeños durante el entrenamiento, y traerán señales fuera del rango adecuado. Podemos devolver las señales utilizando una de las técnicas de **normalización**. Aunque hay varias de ellas (Normalización de peso, Normalización de capa), la más utilizada es la Normalización por lotes.

La idea de la **normalización por lotes** es tener en cuenta todos los valores a través del minibatch, y realizar la normalización (es decir, restar la media y dividir por la desviación estándar) en función de esos valores. Se implementa como una capa de red que realiza esta normalización después de aplicar los pesos, pero antes de la función de activación. Como resultado, es probable que veamos una mayor precisión final y un entrenamiento más rápido.

Aquí está el [artículo original](https://arxiv.org/pdf/1502.03167.pdf) sobre la normalización por lotes, la [explicación en Wikipedia](https://en.wikipedia.org/wiki/Batch_normalization), y [una buena publicación introductoria en un blog](https://towardsdatascience.com/batch-normalization-in-3-levels-of-understanding-14c2da90a338) (y una [en ruso](https://habrahabr.ru/post/309302/)).

## Dropout

**Dropout** es una técnica interesante que elimina un cierto porcentaje de neuronas aleatorias durante el entrenamiento. También se implementa como una capa con un parámetro (porcentaje de neuronas a eliminar, típicamente del 10% al 50%), y durante el entrenamiento, pone a cero elementos aleatorios del vector de entrada, antes de pasarlo a la siguiente capa.

Aunque esto puede sonar como una idea extraña, puedes ver el efecto de dropout en el entrenamiento de un clasificador de dígitos MNIST en el cuaderno [`Dropout.ipynb`](../../../../../lessons/4-ComputerVision/08-TransferLearning/Dropout.ipynb). Acelera el entrenamiento y nos permite lograr una mayor precisión en menos épocas de entrenamiento.

Este efecto puede explicarse de varias maneras:

 * Puede considerarse un factor de choque aleatorio para el modelo, que saca la optimización del mínimo local
 * Puede considerarse como *promedio implícito del modelo*, porque podemos decir que durante el dropout estamos entrenando un modelo ligeramente diferente

> *Algunas personas dicen que cuando una persona borracha intenta aprender algo, lo recordará mejor a la mañana siguiente, en comparación con una persona sobria, porque un cerebro con algunos neuronas malfuncionantes intenta adaptarse mejor para captar el significado. Nunca hemos probado si esto es cierto o no*

## Previniendo el sobreajuste

Uno de los aspectos muy importantes del aprendizaje profundo es poder prevenir el [sobreajuste](../../3-NeuralNetworks/05-Frameworks/Overfitting.md). Aunque puede ser tentador usar un modelo de red neuronal muy poderoso, siempre debemos equilibrar el número de parámetros del modelo con el número de muestras de entrenamiento.

> ¡Asegúrate de entender el concepto de [sobreajuste](../../3-NeuralNetworks/05-Frameworks/Overfitting.md) que hemos introducido anteriormente!

Hay varias formas de prevenir el sobreajuste:

 * Parada temprana -- monitorear continuamente el error en el conjunto de validación y detener el entrenamiento cuando el error de validación comienza a aumentar.
 * Decaimiento de peso explícito / Regularización -- agregar una penalización extra a la función de pérdida por valores absolutos altos de los pesos, lo que evita que el modelo obtenga resultados muy inestables
 * Promedio de modelos -- entrenar varios modelos y luego promediar el resultado. Esto ayuda a minimizar la varianza.
 * Dropout (Promedio implícito del modelo)

## Optimizadores / Algoritmos de Entrenamiento

Otro aspecto importante del entrenamiento es elegir un buen algoritmo de entrenamiento. Aunque el **descenso de gradiente** clásico es una elección razonable, a veces puede ser demasiado lento o resultar en otros problemas.

En el aprendizaje profundo, utilizamos **Descenso de Gradiente Estocástico** (SGD), que es un descenso de gradiente aplicado a minibatches, seleccionados aleatoriamente del conjunto de entrenamiento. Los pesos se ajustan utilizando esta fórmula:

w<sup>t+1</sup> = w<sup>t</sup> - η∇ℒ

### Momento

En **SGD con momento**, mantenemos una porción de un gradiente de pasos anteriores. Es similar a cuando nos movemos con inercia, y recibimos un golpe en una dirección diferente; nuestra trayectoria no cambia de inmediato, sino que mantiene parte del movimiento original. Aquí introducimos otro vector v para representar la *velocidad*:

* v<sup>t+1</sup> = γ v<sup>t</sup> - η∇ℒ
* w<sup>t+1</sup> = w<sup>t</sup>+v<sup>t+1</sup>

Aquí, el parámetro γ indica el grado en que tomamos en cuenta la inercia: γ=0 corresponde al SGD clásico; γ=1 es una ecuación de movimiento puro.

### Adam, Adagrad, etc.

Dado que en cada capa multiplicamos señales por alguna matriz W<sub>i</sub>, dependiendo de ||W<sub>i</sub>||, el gradiente puede disminuir y acercarse a 0, o aumentar indefinidamente. Esta es la esencia del problema de los Gradientes que Explotan/Desvanecen.

Una de las soluciones a este problema es usar solo la dirección del gradiente en la ecuación, e ignorar el valor absoluto, es decir,

w<sup>t+1</sup> = w<sup>t</sup> - η(∇ℒ/||∇ℒ||), donde ||∇ℒ|| = √∑(∇ℒ)<sup>2</sup>

Este algoritmo se llama **Adagrad**. Otros algoritmos que utilizan la misma idea son: **RMSProp**, **Adam**

> **Adam** se considera un algoritmo muy eficiente para muchas aplicaciones, así que si no estás seguro de cuál usar, utiliza Adam.

### Recorte de Gradiente

El recorte de gradiente es una extensión de la idea anterior. Cuando ||∇ℒ|| ≤ θ, consideramos el gradiente original en la optimización de pesos, y cuando ||∇ℒ|| > θ - dividimos el gradiente por su norma. Aquí θ es un parámetro, en la mayoría de los casos podemos tomar θ=1 o θ=10.

### Decaimiento de la tasa de aprendizaje

El éxito del entrenamiento a menudo depende del parámetro de tasa de aprendizaje η. Es lógico suponer que valores más grandes de η resultan en un entrenamiento más rápido, que es algo que normalmente queremos al principio del entrenamiento, y luego un valor más pequeño de η nos permite afinar la red. Por lo tanto, en la mayoría de los casos queremos disminuir η en el proceso del entrenamiento.

Esto se puede hacer multiplicando η por algún número (por ejemplo, 0.98) después de cada época de entrenamiento, o utilizando un **programa de tasa de aprendizaje** más complicado.

## Diferentes Arquitecturas de Red

Seleccionar la arquitectura de red adecuada para tu problema puede ser complicado. Normalmente, elegiríamos una arquitectura que ha demostrado funcionar para nuestra tarea específica (o una similar). Aquí hay una [buena visión general](https://www.topbots.com/a-brief-history-of-neural-network-architectures/) de arquitecturas de redes neuronales para visión por computadora.

> Es importante seleccionar una arquitectura que sea lo suficientemente poderosa para el número de muestras de entrenamiento que tenemos. Seleccionar un modelo demasiado poderoso puede resultar en [sobreajuste](../../3-NeuralNetworks/05-Frameworks/Overfitting.md).

Otra buena forma sería utilizar una arquitectura que se ajuste automáticamente a la complejidad requerida. Hasta cierto punto, la arquitectura **ResNet** y **Inception** son autoajustables. [Más sobre arquitecturas de visión por computadora](../07-ConvNets/CNN_Architectures.md)

**Descargo de responsabilidad**:  
Este documento ha sido traducido utilizando servicios de traducción automática basados en IA. Si bien nos esforzamos por lograr la precisión, tenga en cuenta que las traducciones automáticas pueden contener errores o inexactitudes. El documento original en su idioma nativo debe considerarse la fuente autorizada. Para información crítica, se recomienda una traducción profesional realizada por humanos. No nos hacemos responsables de malentendidos o malas interpretaciones que surjan del uso de esta traducción.