# Redes neuronales recurrentes

## [Pre-lecture quiz](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/116)

En secciones anteriores, hemos estado utilizando representaciones semánticas ricas de texto y un clasificador lineal simple además de las incrustaciones. Lo que hace esta arquitectura es capturar el significado agregado de las palabras en una oración, pero no tiene en cuenta el **orden** de las palabras, porque la operación de agregación además de las incrustaciones eliminó esta información del texto original. Debido a que estos modelos no pueden modelar el orden de las palabras, no pueden resolver tareas más complejas o ambiguas, como la generación de texto o la respuesta a preguntas.

Para capturar el significado de la secuencia de texto, necesitamos utilizar otra arquitectura de red neuronal, que se denomina **red neuronal recurrente** o RNN. En RNN, pasamos nuestra oración a través de la red, un símbolo a la vez, y la red produce algún **estado**, que luego pasamos a la red nuevamente con el siguiente símbolo.

![RNN](./images/rnn.png)

> Imagen del autor

Dada la secuencia de entrada de tokens X<sub>0</sub>,...,X<sub>n</sub>, RNN crea una secuencia de bloques de red neuronal y entrena esta secuencia de un extremo a otro mediante retropropagación. . Cada bloque de red toma un par (X<sub>i</sub>,S<sub>i</sub>) como entrada y produce S<sub>i+1</sub> como resultado. El estado final S<sub>n</sub> o (salida Y<sub>n</sub>) entra en un clasificador lineal para producir el resultado. Todos los bloques de red comparten los mismos pesos y se entrenan de un extremo a otro mediante un paso de retropropagación.

Debido a que los vectores de estado S<sub>0</sub>,...,S<sub>n</sub> pasan a través de la red, es posible aprender las dependencias secuenciales entre palabras. Por ejemplo, cuando la palabra *no* aparece en algún lugar de la secuencia, puede aprender a negar ciertos elementos dentro del vector de estado, lo que resulta en negación.

> ✅ Dado que los pesos de todos los bloques RNN en la imagen de arriba son compartidos, la misma imagen se puede representar como un bloque (a la derecha) con un bucle de retroalimentación recurrente, que devuelve el estado de salida de la red a la entrada.

## Anatomía de una célula RNN

Veamos cómo se organiza una celda RNN simple. Acepta el estado anterior S<sub>i-1</sub> y el símbolo actual X<sub>i</sub> como entradas, y tiene que producir el estado de salida S<sub>i</sub> (y, A veces, también estamos interesados en algún otro resultado Y<sub>i</sub>,como en el caso de las redes generativas).

Una celda RNN simple tiene dos matrices de peso en su interior: una transforma un símbolo de entrada (llamémoslo W) y otra transforma un estado de entrada (H). En este caso, la salida de la red se calcula como &sigma;(W&times;X<sub>i</sub>+H&times;S<sub>i-1</sub>+b), donde &sigma; es la función de activación y b es el sesgo adicional.

<img alt="RNN Cell Anatomy" src="images/rnn-anatomy.png" width="50%"/>

> Imagen del autor

En muchos casos, los tokens de entrada pasan a través de la capa de incrustación antes de ingresar al RNN para reducir la dimensionalidad. En este caso, si la dimensión de los vectores de entrada es *emb_size* y el vector de estado es *hid_size*, el tamaño de W es *emb_size*&times;*hid_size* y el tamaño de H es *hid_size*&times;* tamaño_hid*.

## Memoria a largo plazo (LSTM)

Uno de los principales problemas de los RNN clásicos es el llamado problema de los **gradientes de fuga**. Debido a que los RNN se entrenan de un extremo a otro en un paso de retropropagación, tienen dificultades para propagar el error a las primeras capas de la red y, por lo tanto, la red no puede aprender las relaciones entre tokens distantes. Una de las formas de evitar este problema es introducir **administración de estado explícita** mediante el uso de las llamadas **puertas**. Hay dos arquitecturas bien conocidas de este tipo: **Memoria a corto plazo** (LSTM) y **Unidad de retransmisión cerrada** (GRU).

![Image showing an example long short term memory cell](./images/long-short-term-memory-cell.svg)

> Fuente de la imagen por determinar

La red LSTM está organizada de manera similar a RNN, pero hay dos estados que se pasan de una capa a otra: el estado real C y el vector oculto H. En cada unidad, el vector oculto H<sub>i< /sub> está concatenado con la entrada X<sub>i</sub>, y controlan lo que sucede con el estado C a través de **puertas**. Cada puerta es una red neuronal con activación sigmoidea (salida en el rango [0,1]), que puede considerarse como una máscara bit a bit cuando se multiplica por el vector de estado. Existen las siguientes puertas (de izquierda a derecha en la imagen de arriba):

* La **puerta del olvido** toma un vector oculto y determina qué componentes del vector C debemos olvidar y por cuáles pasar.
* La **puerta de entrada** toma información de los vectores ocultos y de entrada y la inserta en el estado.
* La **puerta de salida** transforma el estado a través de una capa lineal con activación *tanh*, luego selecciona algunos de sus componentes usando un vector oculto H<sub>i</sub> para producir un nuevo estado C<sub>i+ 1</sub>.

Los componentes del estado C pueden considerarse como algunas banderas que se pueden activar y desactivar. Por ejemplo, cuando encontramos un nombre *Alice* en la secuencia, podemos asumir que se refiere a un personaje femenino y levantar la bandera en el estado de que tenemos un sustantivo femenino en la oración. Cuando encontremos más frases *y Tom*, levantaremos la bandera de que tenemos un sustantivo plural. Así, manipulando el estado supuestamente podemos realizar un seguimiento de las propiedades gramaticales de las partes de la oración.

> ✅ Un excelente recurso para comprender los aspectos internos de LSTM es este excelente artículo [Understanding LSTM Networks](https://colah.github.io/posts/2015-08-Understanding-LSTMs/)
>
> ## RNN bidireccionales y multicapa

Hemos discutido redes recurrentes que operan en una dirección, desde el principio de una secuencia hasta el final. Parece natural porque se parece a la forma en que leemos y escuchamos el habla. Sin embargo, dado que en muchos casos prácticos tenemos acceso aleatorio a la secuencia de entrada, podría tener sentido ejecutar cálculos recurrentes en ambas direcciones. Estas redes se denominan RNN **bidireccionales**. Cuando se trata de una red bidireccional, necesitaríamos dos vectores de estado ocultos, uno para cada dirección.

Una red recurrente, ya sea unidireccional o bidireccional, captura ciertos patrones dentro de una secuencia y puede almacenarlos en un vector de estado o pasarlos a la salida. Al igual que con las redes convolucionales, podemos construir otra capa recurrente encima de la primera para capturar patrones de nivel superior y construir a partir de patrones de bajo nivel extraídos por la primera capa. Esto nos lleva a la noción de un **RNN multicapa** que consta de dos o más redes recurrentes, donde la salida de la capa anterior se pasa a la siguiente capa como entrada.

![Image showing a Multilayer long-short-term-memory- RNN](./images/multi-layer-lstm.jpg)

*Photo de [this wonderful post](https://towardsdatascience.com/from-a-lstm-cell-to-a-multilayer-lstm-network-with-pytorch-2899eb5696f3) by Fernando López*

## ✍️ Ejercicios: Incrustaciones

Continúa tu aprendizaje en los siguientes cuadernos:

* [RNNs with PyTorch](RNNPyTorch.ipynb)
* [RNNs with TensorFlow](RNNTF.ipynb)

## Conclusión

En esta unidad, hemos visto que los RNN se pueden usar para la clasificación de secuencias, pero de hecho, pueden manejar muchas más tareas, como generación de texto, traducción automática y más. Consideraremos esas tareas en la siguiente unidad.

## 🚀 Desafío

Lea algo de literatura sobre LSTM y considere sus aplicaciones:

- [Grid Long Short-Term Memory](https://arxiv.org/pdf/1507.01526v1.pdf)
- [Show, Attend and Tell: Neural Image Caption
Generation with Visual Attention](https://arxiv.org/pdf/1502.03044v2.pdf)

## [Post-lecture quiz](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/216)

## Revisión y autoestudio

- [Understanding LSTM Networks](https://colah.github.io/posts/2015-08-Understanding-LSTMs/) by Christopher Olah.

## [Assignment: Notebooks](assignment.md)



