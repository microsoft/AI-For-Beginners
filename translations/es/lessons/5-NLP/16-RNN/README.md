# Redes Neuronales Recurrentes

## [Cuestionario previo a la clase](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/116)

En secciones anteriores, hemos estado utilizando representaciones semánticas ricas del texto y un clasificador lineal simple sobre las incrustaciones. Lo que hace esta arquitectura es capturar el significado agregado de las palabras en una oración, pero no toma en cuenta el **orden** de las palabras, ya que la operación de agregación sobre las incrustaciones eliminó esta información del texto original. Debido a que estos modelos no pueden modelar el orden de las palabras, no pueden resolver tareas más complejas o ambiguas, como la generación de texto o la respuesta a preguntas.

Para capturar el significado de la secuencia de texto, necesitamos utilizar otra arquitectura de red neuronal, que se llama **red neuronal recurrente**, o RNN. En una RNN, pasamos nuestra oración a través de la red un símbolo a la vez, y la red produce algún **estado**, que luego pasamos a la red nuevamente con el siguiente símbolo.

![RNN](../../../../../translated_images/rnn.27f5c29c53d727b546ad3961637a267f0fe9ec5ab01f2a26a853c92fcefbb574.es.png)

> Imagen del autor

Dada la secuencia de entrada de tokens X<sub>0</sub>,...,X<sub>n</sub>, la RNN crea una secuencia de bloques de red neuronal y entrena esta secuencia de extremo a extremo utilizando retropropagación. Cada bloque de red toma un par (X<sub>i</sub>,S<sub>i</sub>) como entrada y produce S<sub>i+1</sub> como resultado. El estado final S<sub>n</sub> o (salida Y<sub>n</sub>) entra en un clasificador lineal para producir el resultado. Todos los bloques de red comparten los mismos pesos y se entrenan de extremo a extremo utilizando un pase de retropropagación.

Debido a que los vectores de estado S<sub>0</sub>,...,S<sub>n</sub> se pasan a través de la red, es capaz de aprender las dependencias secuenciales entre las palabras. Por ejemplo, cuando la palabra *not* aparece en algún lugar de la secuencia, puede aprender a negar ciertos elementos dentro del vector de estado, resultando en negación.

> ✅ Dado que los pesos de todos los bloques RNN en la imagen anterior se comparten, la misma imagen puede representarse como un bloque (a la derecha) con un bucle de retroalimentación recurrente, que pasa el estado de salida de la red de vuelta a la entrada.

## Anatomía de una Celda RNN

Veamos cómo está organizada una celda RNN simple. Acepta el estado anterior S<sub>i-1</sub> y el símbolo actual X<sub>i</sub> como entradas, y tiene que producir el estado de salida S<sub>i</sub> (y, a veces, también estamos interesados en alguna otra salida Y<sub>i</sub>, como en el caso de las redes generativas).

Una celda RNN simple tiene dos matrices de pesos en su interior: una transforma un símbolo de entrada (llamémosla W), y otra transforma un estado de entrada (H). En este caso, la salida de la red se calcula como σ(W×X<sub>i</sub>+H×S<sub>i-1</sub>+b), donde σ es la función de activación y b es un sesgo adicional.

<img alt="Anatomía de la Celda RNN" src="images/rnn-anatomy.png" width="50%"/>

> Imagen del autor

En muchos casos, los tokens de entrada se pasan a través de la capa de incrustación antes de entrar en la RNN para reducir la dimensionalidad. En este caso, si la dimensión de los vectores de entrada es *emb_size*, y el vector de estado es *hid_size* - el tamaño de W es *emb_size*×*hid_size*, y el tamaño de H es *hid_size*×*hid_size*.

## Memoria a Largo y Corto Plazo (LSTM)

Uno de los principales problemas de las RNN clásicas es el problema de los **gradientes que desaparecen**. Debido a que las RNN se entrenan de extremo a extremo en un solo pase de retropropagación, tienen dificultades para propagar el error a las primeras capas de la red, y por lo tanto, la red no puede aprender relaciones entre tokens distantes. Una de las formas de evitar este problema es introducir **gestión de estado explícita** mediante el uso de lo que se llama **puertas**. Hay dos arquitecturas bien conocidas de este tipo: **Memoria a Largo y Corto Plazo** (LSTM) y **Unidad de Relé con Puerta** (GRU).

![Imagen que muestra un ejemplo de celda de memoria a largo y corto plazo](../../../../../lessons/5-NLP/16-RNN/images/long-short-term-memory-cell.svg)

> Fuente de la imagen TBD

La Red LSTM está organizada de manera similar a la RNN, pero hay dos estados que se pasan de capa a capa: el estado actual C y el vector oculto H. En cada unidad, el vector oculto H<sub>i</sub> se concatena con la entrada X<sub>i</sub>, y ellos controlan lo que sucede con el estado C a través de **puertas**. Cada puerta es una red neuronal con activación sigmoide (salida en el rango [0,1]), que se puede considerar como una máscara a nivel de bits cuando se multiplica por el vector de estado. Hay las siguientes puertas (de izquierda a derecha en la imagen anterior):

* La **puerta de olvido** toma un vector oculto y determina qué componentes del vector C necesitamos olvidar y cuáles pasar.
* La **puerta de entrada** toma cierta información de los vectores de entrada y ocultos e inserta en el estado.
* La **puerta de salida** transforma el estado a través de una capa lineal con activación *tanh*, luego selecciona algunos de sus componentes utilizando un vector oculto H<sub>i</sub> para producir un nuevo estado C<sub>i+1</sub>.

Los componentes del estado C se pueden considerar como algunas banderas que pueden activarse y desactivarse. Por ejemplo, cuando encontramos un nombre *Alice* en la secuencia, podemos querer suponer que se refiere a un personaje femenino y activar la bandera en el estado de que tenemos un sustantivo femenino en la oración. Cuando encontramos más adelante las frases *and Tom*, levantaremos la bandera de que tenemos un sustantivo plural. Así, manipulando el estado, supuestamente podemos hacer un seguimiento de las propiedades gramaticales de las partes de la oración.

> ✅ Un recurso excelente para entender los entresijos de LSTM es este gran artículo [Understanding LSTM Networks](https://colah.github.io/posts/2015-08-Understanding-LSTMs/) de Christopher Olah.

## RNNs Bidireccionales y Multicapa

Hemos discutido redes recurrentes que operan en una dirección, desde el comienzo de una secuencia hasta el final. Esto parece natural, ya que se asemeja a la forma en que leemos y escuchamos el habla. Sin embargo, dado que en muchos casos prácticos tenemos acceso aleatorio a la secuencia de entrada, podría tener sentido realizar cálculos recurrentes en ambas direcciones. Tales redes se llaman RNNs **bidireccionales**. Al tratar con una red bidireccional, necesitaríamos dos vectores de estado oculto, uno para cada dirección.

Una red recurrente, ya sea unidireccional o bidireccional, captura ciertos patrones dentro de una secuencia y puede almacenarlos en un vector de estado o pasarlos a la salida. Al igual que con las redes convolucionales, podemos construir otra capa recurrente sobre la primera para capturar patrones de nivel superior y construir a partir de patrones de bajo nivel extraídos por la primera capa. Esto nos lleva a la noción de una **RNN multicapa** que consiste en dos o más redes recurrentes, donde la salida de la capa anterior se pasa a la siguiente capa como entrada.

![Imagen que muestra una RNN multicapa de memoria a largo y corto plazo](../../../../../translated_images/multi-layer-lstm.dd975e29bb2a59fe58b429db833932d734c81f211cad2783797a9608984acb8c.es.jpg)

*Imagen de [esta maravillosa publicación](https://towardsdatascience.com/from-a-lstm-cell-to-a-multilayer-lstm-network-with-pytorch-2899eb5696f3) de Fernando López*

## ✍️ Ejercicios: Incrustaciones

Continúa tu aprendizaje en los siguientes cuadernos:

* [RNNs con PyTorch](../../../../../lessons/5-NLP/16-RNN/RNNPyTorch.ipynb)
* [RNNs con TensorFlow](../../../../../lessons/5-NLP/16-RNN/RNNTF.ipynb)

## Conclusión

En esta unidad, hemos visto que las RNNs se pueden utilizar para la clasificación de secuencias, pero de hecho, pueden manejar muchas más tareas, como la generación de texto, la traducción automática y más. Consideraremos esas tareas en la próxima unidad.

## 🚀 Desafío

Lee algo de literatura sobre LSTMs y considera sus aplicaciones:

- [Grid Long Short-Term Memory](https://arxiv.org/pdf/1507.01526v1.pdf)
- [Show, Attend and Tell: Neural Image Caption
Generation with Visual Attention](https://arxiv.org/pdf/1502.03044v2.pdf)

## [Cuestionario posterior a la clase](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/216)

## Revisión y Autoestudio

- [Understanding LSTM Networks](https://colah.github.io/posts/2015-08-Understanding-LSTMs/) de Christopher Olah.

## [Asignación: Cuadernos](assignment.md)

**Descargo de responsabilidad**:  
Este documento ha sido traducido utilizando servicios de traducción automática basados en IA. Si bien nos esforzamos por lograr precisión, tenga en cuenta que las traducciones automáticas pueden contener errores o inexactitudes. El documento original en su idioma nativo debe considerarse la fuente autorizada. Para información crítica, se recomienda una traducción profesional realizada por humanos. No nos hacemos responsables de malentendidos o malas interpretaciones que surjan del uso de esta traducción.