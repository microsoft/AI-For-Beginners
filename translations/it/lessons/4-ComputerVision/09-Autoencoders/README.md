# Autoencoders

Cuando se entrena CNNs, uno de los problemas es que necesitamos una gran cantidad de datos etiquetados. En el caso de la clasificación de imágenes, debemos separar las imágenes en diferentes clases, lo que implica un esfuerzo manual.

## [Cuestionario previo a la clase](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/109)

Sin embargo, podríamos querer utilizar datos en bruto (sin etiquetar) para entrenar extractores de características de CNN, lo que se denomina **aprendizaje auto-supervisado**. En lugar de etiquetas, utilizaremos imágenes de entrenamiento como entrada y salida de la red. La idea principal de un **autoencoder** es que tendremos una **red de codificación** que convierte la imagen de entrada en un **espacio latente** (normalmente es solo un vector de menor tamaño), y luego la **red de decodificación**, cuyo objetivo es reconstruir la imagen original.

> ✅ Un [autoencoder](https://wikipedia.org/wiki/Autoencoder) es "un tipo de red neuronal artificial utilizada para aprender codificaciones eficientes de datos no etiquetados."

Dado que estamos entrenando un autoencoder para capturar la mayor cantidad de información posible de la imagen original para una reconstrucción precisa, la red intenta encontrar la mejor **inmersión** de las imágenes de entrada para capturar su significado.

![Diagrama de Autoencoder](../../../../../translated_images/autoencoder_schema.5e6fc9ad98a5eb6197f3513cf3baf4dfbe1389a6ae74daebda64de9f1c99f142.it.jpg)

> Imagen del [blog de Keras](https://blog.keras.io/building-autoencoders-in-keras.html)

## Escenarios para usar Autoencoders

Aunque reconstruir imágenes originales no parece útil por sí mismo, hay algunos escenarios donde los autoencoders son especialmente útiles:

* **Reducir la dimensión de las imágenes para visualización** o **entrenar embeddings de imágenes**. Generalmente, los autoencoders ofrecen mejores resultados que PCA, porque tienen en cuenta la naturaleza espacial de las imágenes y las características jerárquicas.
* **Eliminación de ruido**, es decir, quitar el ruido de la imagen. Debido a que el ruido contiene mucha información innecesaria, el autoencoder no puede ajustarlo todo en un espacio latente relativamente pequeño, y por lo tanto solo captura la parte importante de la imagen. Al entrenar eliminadores de ruido, comenzamos con imágenes originales y utilizamos imágenes con ruido añadido artificialmente como entrada para el autoencoder.
* **Super-resolución**, aumentando la resolución de la imagen. Comenzamos con imágenes de alta resolución y utilizamos imágenes de menor resolución como entrada para el autoencoder.
* **Modelos generativos**. Una vez que entrenamos el autoencoder, la parte del decodificador puede usarse para crear nuevos objetos a partir de vectores latentes aleatorios.

## Autoencoders Variacionales (VAE)

Los autoencoders tradicionales reducen la dimensión de los datos de entrada de alguna manera, identificando las características importantes de las imágenes de entrada. Sin embargo, los vectores latentes a menudo no tienen mucho sentido. En otras palabras, tomando como ejemplo el conjunto de datos MNIST, identificar qué dígitos corresponden a diferentes vectores latentes no es una tarea fácil, ya que vectores latentes cercanos no necesariamente corresponden a los mismos dígitos.

Por otro lado, para entrenar modelos *generativos*, es mejor tener cierta comprensión del espacio latente. Esta idea nos lleva a los **autoencoders variacionales** (VAE).

El VAE es el autoencoder que aprende a predecir la *distribución estadística* de los parámetros latentes, denominada **distribución latente**. Por ejemplo, podemos querer que los vectores latentes se distribuyan normalmente con una media z<sub>mean</sub> y una desviación estándar z<sub>sigma</sub> (tanto la media como la desviación estándar son vectores de alguna dimensionalidad d). El codificador en el VAE aprende a predecir esos parámetros, y luego el decodificador toma un vector aleatorio de esta distribución para reconstruir el objeto.

Para resumir:

 * Desde el vector de entrada, predecimos `z_mean` y `z_log_sigma` (en lugar de predecir la desviación estándar en sí, predecimos su logaritmo)
 * Muestreamos un vector `sample` de la distribución N(z<sub>mean</sub>,exp(z<sub>log\_sigma</sub>))
 * El decodificador intenta decodificar la imagen original utilizando `sample` como vector de entrada

 <img src="images/vae.png" width="50%">

> Imagen de [este post del blog](https://ijdykeman.github.io/ml/2016/12/21/cvae.html) de Isaak Dykeman

Los autoencoders variacionales utilizan una función de pérdida compleja que consiste en dos partes:

* **Pérdida de reconstrucción** es la función de pérdida que muestra cuán cerca está una imagen reconstruida del objetivo (puede ser el Error Cuadrático Medio, o MSE). Es la misma función de pérdida que en los autoencoders normales.
* **Pérdida KL**, que asegura que las distribuciones de variables latentes se mantengan cerca de la distribución normal. Se basa en la noción de [divergencia de Kullback-Leibler](https://www.countbayesie.com/blog/2017/5/9/kullback-leibler-divergence-explained) - una métrica para estimar cuán similares son dos distribuciones estadísticas.

Una ventaja importante de los VAE es que nos permiten generar nuevas imágenes de manera relativamente fácil, porque sabemos de qué distribución muestrear vectores latentes. Por ejemplo, si entrenamos un VAE con un vector latente 2D en MNIST, podemos variar los componentes del vector latente para obtener diferentes dígitos:

<img alt="vaemnist" src="images/vaemnist.png" width="50%"/>

> Imagen de [Dmitry Soshnikov](http://soshnikov.com)

Observa cómo las imágenes se fusionan entre sí, a medida que comenzamos a obtener vectores latentes de diferentes porciones del espacio de parámetros latentes. También podemos visualizar este espacio en 2D:

<img alt="vaemnist cluster" src="images/vaemnist-diag.png" width="50%"/> 

> Imagen de [Dmitry Soshnikov](http://soshnikov.com)

## ✍️ Ejercicios: Autoencoders

Aprende más sobre autoencoders en estos cuadernos correspondientes:

* [Autoencoders en TensorFlow](../../../../../lessons/4-ComputerVision/09-Autoencoders/AutoencodersTF.ipynb)
* [Autoencoders en PyTorch](../../../../../lessons/4-ComputerVision/09-Autoencoders/AutoEncodersPyTorch.ipynb)

## Propiedades de los Autoencoders

* **Específicos para datos** - solo funcionan bien con el tipo de imágenes en las que han sido entrenados. Por ejemplo, si entrenamos una red de super-resolución en flores, no funcionará bien en retratos. Esto se debe a que la red puede producir una imagen de mayor resolución tomando detalles finos de las características aprendidas del conjunto de datos de entrenamiento.
* **Con pérdida** - la imagen reconstruida no es la misma que la imagen original. La naturaleza de la pérdida está definida por la *función de pérdida* utilizada durante el entrenamiento.
* Funciona con **datos no etiquetados**.

## [Cuestionario posterior a la clase](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/209)

## Conclusión

En esta lección, aprendiste sobre los diversos tipos de autoencoders disponibles para el científico de IA. Aprendiste cómo construirlos y cómo usarlos para reconstruir imágenes. También aprendiste sobre el VAE y cómo utilizarlo para generar nuevas imágenes.

## 🚀 Desafío

En esta lección, aprendiste sobre el uso de autoencoders para imágenes. ¡Pero también pueden ser utilizados para música! Echa un vistazo al proyecto [MusicVAE](https://magenta.tensorflow.org/music-vae) del proyecto Magenta, que utiliza autoencoders para aprender a reconstruir música. Realiza algunos [experimentos](https://colab.research.google.com/github/magenta/magenta-demos/blob/master/colab-notebooks/Multitrack_MusicVAE.ipynb) con esta biblioteca para ver qué puedes crear.

## [Cuestionario posterior a la clase](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/208)

## Revisión y Autoestudio

Para referencia, lee más sobre autoencoders en estos recursos:

* [Construyendo Autoencoders en Keras](https://blog.keras.io/building-autoencoders-in-keras.html)
* [Publicación en el blog sobre NeuroHive](https://neurohive.io/ru/osnovy-data-science/variacionnyj-avtojenkoder-vae/)
* [Autoencoders Variacionales Explicados](https://kvfrans.com/variational-autoencoders-explained/)
* [Autoencoders Variacionales Condicionales](https://ijdykeman.github.io/ml/2016/12/21/cvae.html)

## Asignación

Al final de [este cuaderno usando TensorFlow](../../../../../lessons/4-ComputerVision/09-Autoencoders/AutoencodersTF.ipynb), encontrarás una 'tarea' - utiliza esto como tu asignación.

**Disclaimer**:  
Este documento ha sido traducido utilizando servicios de traducción automática basados en IA. Aunque nos esforzamos por lograr precisión, tenga en cuenta que las traducciones automatizadas pueden contener errores o inexactitudes. El documento original en su idioma nativo debe considerarse la fuente autorizada. Para información crítica, se recomienda una traducción profesional realizada por humanos. No somos responsables de malentendidos o malas interpretaciones que surjan del uso de esta traducción.