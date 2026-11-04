# Trucos para Entrenamiento de Deep Learning

A medida que las redes neuronales se hacen más profundas, el proceso de su entrenamiento se vuelve cada vez más desafiante. Un problema importante son los llamados [gradientes que desaparecen](https://en.wikipedia.org/wiki/Vanishing_gradient_problem) o [gradientes que explotan](https://deepai.org/machine-learning-glossary-and-terms/exploding-gradient-problem#:~:text=Exploding%20gradients%20are%20a%20problem,updates%20are%20small%20and%20controlled.). [Esta publicación](https://towardsdatascience.com/the-vanishing-exploding-gradient-problem-in-deep-neural-networks-191358470c11) ofrece una buena introducción a estos problemas.

Para hacer el entrenamiento de redes profundas más eficiente, existen algunas técnicas que se pueden usar.

## Mantener los valores dentro de un intervalo razonable

Para hacer los cálculos numéricos más estables, queremos asegurarnos de que todos los valores dentro de nuestra red neuronal estén dentro de una escala razonable, típicamente [-1..1] o [0..1]. No es un requisito muy estricto, pero la naturaleza de los cálculos en coma flotante es tal que valores de diferentes magnitudes no pueden manipularse con precisión juntos. Por ejemplo, si sumamos 10<sup>-10</sup> y 10<sup>10</sup>, es probable que obtengamos 10<sup>10</sup>, porque el valor más pequeño sería "convertido" al mismo orden que el más grande, y por lo tanto se perdería la mantisa.

La mayoría de las funciones de activación tienen no linealidades alrededor de [-1..1], por lo que tiene sentido escalar todos los datos de entrada al intervalo [-1..1] o [0..1].

## Inicialización de Pesos Inicial

Idealmente, queremos que los valores estén en el mismo rango después de pasar por las capas de la red. Por lo tanto, es importante inicializar los pesos de manera que se preserve la distribución de valores.

La distribución normal **N(0,1)** no es una buena idea, porque si tenemos *n* entradas, la desviación estándar de la salida sería *&radic;n*, y los valores probablemente se saldrían del intervalo [0..1].

Las siguientes inicializaciones se usan frecuentemente:

 * Distribución uniforme -- `uniform`
 * **N(0,1/n)** -- `gaussian`
 * **N(0,1/&radic;n_in)** garantiza que para entradas con media cero y desviación estándar 1, permanecerá la misma media/desviación estándar
 * **N(0,&radic;2/(n_in+n_out))** -- la llamada **inicialización Xavier** (`glorot`), ayuda a mantener las señales dentro del rango durante la propagación hacia adelante y hacia atrás

## Normalización de Lote

Incluso con una inicialización adecuada de pesos, los pesos pueden volverse arbitrariamente grandes o pequeños durante el entrenamiento, y sacarán las señales fuera del rango adecuado. Podemos devolver las señales al rango correcto usando una de las técnicas de **normalización**. Aunque existen varias (normalización de pesos, normalización de capa), la más usada es la Normalización de Lote.

La idea de la **normalización de lote** es tener en cuenta todos los valores a través del minibatch y realizar la normalización (es decir, restar la media y dividir por la desviación estándar) basándose en esos valores. Se implementa como una capa de red que realiza esta normalización después de aplicar los pesos, pero antes de la función de activación. Como resultado, probablemente veamos mayor precisión final y entrenamiento más rápido.

Aquí está el [artículo original](https://arxiv.org/pdf/1502.03167.pdf) sobre batch normalization, la [explicación en Wikipedia](https://en.wikipedia.org/wiki/Batch_normalization) y [un buen post introductorio de blog](https://towardsdatascience.com/batch-normalization-in-3-levels-of-understanding-14c2da90a338) (y otro [en ruso](https://habrahabr.ru/post/309302/)).

## Dropout

**Dropout** es una técnica interesante que elimina un porcentaje aleatorio de neuronas durante el entrenamiento. También se implementa como una capa con un parámetro (porcentaje de neuronas a eliminar, típicamente 10%-50%), y durante el entrenamiento pone a cero elementos aleatorios del vector de entrada, antes de pasarlo a la siguiente capa.

Aunque esto pueda sonar extraño, puedes ver el efecto de dropout en el entrenamiento de un clasificador de dígitos MNIST en el cuaderno [`Dropout.ipynb`](Dropout.ipynb). Acelera el entrenamiento y nos permite lograr mayor precisión en menos épocas.

Este efecto puede explicarse de varias maneras:

 * Puede considerarse un factor aleatorio de choque para el modelo, que saca la optimización de mínimos locales
 * Puede considerarse como un *promedio implícito de modelos*, porque podemos decir que durante dropout estamos entrenando un modelo ligeramente diferente

> *Algunas personas dicen que cuando una persona borracha trata de aprender algo, lo recordará mejor a la mañana siguiente en comparación con una persona sobria, debido a que un cerebro con ciertas neuronas que funcionan mal trata de adaptarse mejor para captar el significado. Nunca lo hemos probado para ver si es cierto o no.*

## Prevención de overfitting

Uno de los aspectos muy importantes del deep learning es poder prevenir el [sobreajuste](../../3-NeuralNetworks/05-Frameworks/Overfitting.md). Aunque puede ser tentador usar un modelo de red neuronal muy potente, siempre debemos equilibrar el número de parámetros del modelo con el número de muestras de entrenamiento.

> ¡Asegúrate de entender el concepto de [sobreajuste](../../3-NeuralNetworks/05-Frameworks/Overfitting.md) que presentamos anteriormente!

Hay varias maneras de prevenir el sobreajuste:

 * Parada temprana -- monitorear continuamente el error en el conjunto de validación y detener el entrenamiento cuando el error de validación comienza a aumentar.
 * Decaimiento explícito de pesos / regularización -- agregar una penalización extra a la función de pérdida por valores absolutos altos de los pesos, lo cual previene que el modelo tenga resultados muy inestables
 * Promedio de modelos -- entrenar varios modelos y luego promediar los resultados. Esto ayuda a minimizar la varianza.
 * Dropout (promedio implícito de modelos)

## Optimizadores / Algoritmos de Entrenamiento

Otro aspecto importante del entrenamiento es elegir un buen algoritmo de entrenamiento. Aunque el clásico **gradiente descendente** es una opción razonable, a veces puede ser muy lento o causar otros problemas.

En deep learning, usamos **Gradiente Descendente Estocástico** (SGD), que es el gradiente descendente aplicado a minibatches seleccionados aleatoriamente del conjunto de entrenamiento. Los pesos se ajustan usando esta fórmula:

w<sup>t+1</sup> = w<sup>t</sup> - &eta;&nabla;&lagran;

### Momentum

En **momentum SGD**, mantenemos una porción del gradiente de pasos previos. Es similar a cuando nos movemos con inercia y recibimos un golpe en dirección diferente, nuestra trayectoria no cambia inmediatamente, sino que mantiene parte del movimiento original. Aquí introducimos otro vector v para representar la *velocidad*:

* v<sup>t+1</sup> = &gamma; v<sup>t</sup> - &eta;&nabla;&lagran;
* w<sup>t+1</sup> = w<sup>t</sup>+v<sup>t+1</sup>

Aquí el parámetro &gamma; indica en qué medida tomamos en cuenta la inercia: &gamma;=0 corresponde al SGD clásico; &gamma;=1 es una ecuación pura de movimiento.

### Adam, Adagrad, etc.

Dado que en cada capa multiplicamos señales por alguna matriz W<sub>i</sub>, dependiendo de ||W<sub>i</sub>||, el gradiente puede disminuir y acercarse a 0, o crecer indefinidamente. Esta es la esencia del problema de gradientes que desaparecen o explotan.

Una de las soluciones a este problema es usar solo la dirección del gradiente en la ecuación e ignorar el valor absoluto, es decir:

w<sup>t+1</sup> = w<sup>t</sup> - &eta;(&nabla;&lagran;/||&nabla;&lagran;||), donde ||&nabla;&lagran;|| = &radic;&sum;(&nabla;&lagran;)<sup>2</sup>

Este algoritmo se llama **Adagrad**. Otros algoritmos que usan la misma idea son: **RMSProp**, **Adam**

> **Adam** se considera un algoritmo muy eficiente para muchas aplicaciones, así que si no estás seguro cuál usar, utiliza Adam.

### Recorte de gradiente

El recorte de gradiente es una extensión de la idea anterior. Cuando ||&nabla;&lagran;|| &le; &theta;, consideramos el gradiente original en la optimización del peso, y cuando ||&nabla;&lagran;|| > &theta; - dividimos el gradiente por su norma. Aquí &theta; es un parámetro; en la mayoría de los casos podemos tomar &theta;=1 o &theta;=10.

### Decaimiento de la tasa de aprendizaje

El éxito del entrenamiento a menudo depende del parámetro de tasa de aprendizaje &eta;. Es lógico asumir que valores mayores de &eta; resultan en un entrenamiento más rápido, lo que típicamente queremos al inicio del entrenamiento, y luego valores menores de &eta; nos permiten ajustar finamente la red. Por lo tanto, en la mayoría de los casos queremos disminuir &eta; durante el entrenamiento.

Esto se puede hacer multiplicando &eta; por algún número (por ejemplo, 0.98) después de cada época de entrenamiento, o usando un **programa de tasa de aprendizaje** más complejo.

## Diferentes arquitecturas de red

Seleccionar la arquitectura de red correcta para tu problema puede ser complicado. Normalmente, tomaríamos una arquitectura que haya demostrado funcionar para nuestra tarea específica (o una similar). Aquí hay una [buena visión general](https://www.topbots.com/a-brief-history-of-neural-network-architectures/) de arquitecturas de redes neuronales para visión computacional.

> Es importante seleccionar una arquitectura que sea lo suficientemente potente para el número de muestras de entrenamiento que tenemos. Seleccionar un modelo demasiado potente puede resultar en [sobreajuste](../../3-NeuralNetworks/05-Frameworks/Overfitting.md)

Otra buena opción sería usar una arquitectura que se ajuste automáticamente a la complejidad requerida. En cierta medida, la arquitectura **ResNet** y **Inception** son autoajustables. [Más sobre arquitecturas para visión por computadora](../07-ConvNets/CNN_Architectures.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Descargo de responsabilidad**:
Este documento ha sido traducido utilizando el servicio de traducción automática [Co-op Translator](https://github.com/Azure/co-op-translator). Aunque nos esforzamos por la precisión, tenga en cuenta que las traducciones automatizadas pueden contener errores o inexactitudes. El documento original en su idioma nativo debe considerarse la fuente autorizada. Para información crítica, se recomienda una traducción profesional humana. No somos responsables de cualquier malentendido o interpretación errónea que surja del uso de esta traducción.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->