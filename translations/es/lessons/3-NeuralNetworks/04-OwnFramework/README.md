# Introducción a las Redes Neuronales. Perceptrón Multicapa

En la sección anterior, aprendiste sobre el modelo de red neuronal más simple: el perceptrón de una sola capa, un modelo de clasificación lineal de dos clases.

En esta sección, ampliaremos este modelo a un marco más flexible, que nos permitirá:

* realizar **clasificación de múltiples clases** además de la clasificación de dos clases
* resolver **problemas de regresión** además de la clasificación
* separar clases que no son linealmente separables

También desarrollaremos nuestro propio marco modular en Python que nos permitirá construir diferentes arquitecturas de redes neuronales.

## [Cuestionario previo a la clase](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/104)

## Formalización del Aprendizaje Automático

Comencemos formalizando el problema del Aprendizaje Automático. Supongamos que tenemos un conjunto de datos de entrenamiento **X** con etiquetas **Y**, y necesitamos construir un modelo *f* que haga las predicciones más precisas. La calidad de las predicciones se mide mediante la **función de pérdida** ℒ. Las siguientes funciones de pérdida se utilizan a menudo:

* Para el problema de regresión, cuando necesitamos predecir un número, podemos usar el **error absoluto** ∑<sub>i</sub>|f(x<sup>(i)</sup>)-y<sup>(i)</sup>|, o el **error cuadrático** ∑<sub>i</sub>(f(x<sup>(i)</sup>)-y<sup>(i)</sup>)<sup>2</sup>
* Para la clasificación, utilizamos la **pérdida 0-1** (que es esencialmente lo mismo que la **exactitud** del modelo), o la **pérdida logística**.

Para el perceptrón de una sola capa, la función *f* se definió como una función lineal *f(x)=wx+b* (aquí *w* es la matriz de pesos, *x* es el vector de características de entrada, y *b* es el vector de sesgo). Para diferentes arquitecturas de redes neuronales, esta función puede tomar una forma más compleja.

> En el caso de la clasificación, a menudo es deseable obtener probabilidades de las clases correspondientes como salida de la red. Para convertir números arbitrarios en probabilidades (por ejemplo, para normalizar la salida), a menudo utilizamos la función **softmax** σ, y la función *f* se convierte en *f(x)=σ(wx+b)*

En la definición de *f* anterior, *w* y *b* se llaman **parámetros** θ=⟨*w,b*⟩. Dado el conjunto de datos ⟨**X**,**Y**⟩, podemos calcular un error general en todo el conjunto de datos como una función de los parámetros θ.

> ✅ **El objetivo del entrenamiento de la red neuronal es minimizar el error variando los parámetros θ**

## Optimización por Descenso de Gradiente

Hay un método bien conocido de optimización de funciones llamado **descenso de gradiente**. La idea es que podemos calcular una derivada (en el caso multidimensional llamada **gradiente**) de la función de pérdida con respecto a los parámetros, y variar los parámetros de tal manera que el error disminuya. Esto se puede formalizar de la siguiente manera:

* Inicializar los parámetros con algunos valores aleatorios w<sup>(0)</sup>, b<sup>(0)</sup>
* Repetir el siguiente paso muchas veces:
    - w<sup>(i+1)</sup> = w<sup>(i)</sup>-η∂ℒ/∂w
    - b<sup>(i+1)</sup> = b<sup>(i)</sup>-η∂ℒ/∂b

Durante el entrenamiento, se supone que los pasos de optimización se calculan considerando todo el conjunto de datos (recuerda que la pérdida se calcula como una suma a través de todas las muestras de entrenamiento). Sin embargo, en la vida real tomamos pequeñas porciones del conjunto de datos llamadas **minibatches**, y calculamos gradientes basados en un subconjunto de datos. Debido a que el subconjunto se toma aleatoriamente cada vez, este método se llama **descenso de gradiente estocástico** (SGD).

## Perceptrones Multicapa y Retropropagación

La red de una sola capa, como hemos visto anteriormente, es capaz de clasificar clases que son linealmente separables. Para construir un modelo más rico, podemos combinar varias capas de la red. Matemáticamente, esto significaría que la función *f* tendría una forma más compleja y se calcularía en varios pasos:
* z<sub>1</sub>=w<sub>1</sub>x+b<sub>1</sub>
* z<sub>2</sub>=w<sub>2</sub>α(z<sub>1</sub>)+b<sub>2</sub>
* f = σ(z<sub>2</sub>)

Aquí, α es una **función de activación no lineal**, σ es una función softmax, y los parámetros son θ=<*w<sub>1</sub>,b<sub>1</sub>,w<sub>2</sub>,b<sub>2</sub>*.

El algoritmo de descenso de gradiente seguiría siendo el mismo, pero sería más difícil calcular los gradientes. Dada la regla de diferenciación en cadena, podemos calcular las derivadas como:

* ∂ℒ/∂w<sub>2</sub> = (∂ℒ/∂σ)(∂σ/∂z<sub>2</sub>)(∂z<sub>2</sub>/∂w<sub>2</sub>)
* ∂ℒ/∂w<sub>1</sub> = (∂ℒ/∂σ)(∂σ/∂z<sub>2</sub>)(∂z<sub>2</sub>/∂α)(∂α/∂z<sub>1</sub>)(∂z<sub>1</sub>/∂w<sub>1</sub>)

> ✅ La regla de diferenciación en cadena se utiliza para calcular las derivadas de la función de pérdida con respecto a los parámetros.

Ten en cuenta que la parte más a la izquierda de todas esas expresiones es la misma, y así podemos calcular efectivamente las derivadas comenzando desde la función de pérdida y yendo "hacia atrás" a través del gráfico computacional. Así, el método de entrenamiento de un perceptrón multicapa se llama **retropropagación**, o 'backprop'.

<img alt="gráfico de computación" src="images/ComputeGraphGrad.png"/>

> TODO: cita de la imagen

> ✅ Cubriremos la retropropagación con mucho más detalle en nuestro ejemplo de cuaderno.  

## Conclusión

En esta lección, hemos construido nuestra propia biblioteca de redes neuronales y la hemos utilizado para una simple tarea de clasificación bidimensional.

## 🚀 Desafío

En el cuaderno que acompaña, implementarás tu propio marco para construir y entrenar perceptrones multicapa. Podrás ver en detalle cómo operan las redes neuronales modernas.

Procede al cuaderno [OwnFramework](../../../../../lessons/3-NeuralNetworks/04-OwnFramework/OwnFramework.ipynb) y trabaja en él.

## [Cuestionario posterior a la clase](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/204)

## Revisión y Autoestudio

La retropropagación es un algoritmo comúnmente utilizado en IA y ML, que vale la pena estudiar [con más detalle](https://wikipedia.org/wiki/Backpropagation)

## [Asignación](lab/README.md)

En este laboratorio, se te pide que uses el marco que construiste en esta lección para resolver la clasificación de dígitos manuscritos de MNIST.

* [Instrucciones](lab/README.md)
* [Cuaderno](../../../../../lessons/3-NeuralNetworks/04-OwnFramework/lab/MyFW_MNIST.ipynb)

**Descargo de responsabilidad**:  
Este documento ha sido traducido utilizando servicios de traducción automática basados en IA. Aunque nos esforzamos por lograr precisión, tenga en cuenta que las traducciones automatizadas pueden contener errores o inexactitudes. El documento original en su idioma nativo debe considerarse la fuente autorizada. Para información crítica, se recomienda una traducción profesional humana. No somos responsables de malentendidos o malas interpretaciones que surjan del uso de esta traducción.