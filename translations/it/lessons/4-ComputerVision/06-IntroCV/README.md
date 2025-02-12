# Introducción a la Visión por Computadora

[Visión por Computadora](https://wikipedia.org/wiki/Computer_vision) es una disciplina cuyo objetivo es permitir que las computadoras obtengan una comprensión de alto nivel de las imágenes digitales. Esta es una definición bastante amplia, porque *comprensión* puede significar muchas cosas diferentes, incluyendo encontrar un objeto en una imagen (**detección de objetos**), entender lo que está sucediendo (**detección de eventos**), describir una imagen en texto, o reconstruir una escena en 3D. También hay tareas especiales relacionadas con imágenes humanas: estimación de edad y emociones, detección e identificación de rostros, y estimación de pose en 3D, por nombrar algunas.

## [Cuestionario previo a la clase](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/106)

Una de las tareas más simples de la visión por computadora es **clasificación de imágenes**.

La visión por computadora a menudo se considera una rama de la IA. Hoy en día, la mayoría de las tareas de visión por computadora se resuelven utilizando redes neuronales. Aprenderemos más sobre el tipo especial de redes neuronales utilizadas para la visión por computadora, [redes neuronales convolucionales](../07-ConvNets/README.md), a lo largo de esta sección.

Sin embargo, antes de pasar la imagen a una red neuronal, en muchos casos tiene sentido utilizar algunas técnicas algorítmicas para mejorar la imagen.

Hay varias bibliotecas de Python disponibles para el procesamiento de imágenes:

* **[imageio](https://imageio.readthedocs.io/en/stable/)** se puede utilizar para leer/escribir diferentes formatos de imagen. También soporta ffmpeg, una herramienta útil para convertir fotogramas de video en imágenes.
* **[Pillow](https://pillow.readthedocs.io/en/stable/index.html)** (también conocido como PIL) es un poco más poderosa, y también soporta algunas manipulaciones de imágenes como morfología, ajustes de paleta, y más.
* **[OpenCV](https://opencv.org/)** es una poderosa biblioteca de procesamiento de imágenes escrita en C++, que se ha convertido en el estándar *de facto* para el procesamiento de imágenes. Tiene una interfaz conveniente para Python.
* **[dlib](http://dlib.net/)** es una biblioteca de C++ que implementa muchos algoritmos de aprendizaje automático, incluyendo algunos de los algoritmos de Visión por Computadora. También tiene una interfaz de Python y se puede utilizar para tareas desafiantes como la detección de rostros y puntos de referencia faciales.

## OpenCV

[OpenCV](https://opencv.org/) se considera el estándar *de facto* para el procesamiento de imágenes. Contiene muchos algoritmos útiles, implementados en C++. También puedes llamar a OpenCV desde Python.

Un buen lugar para aprender OpenCV es [este curso de Aprende OpenCV](https://learnopencv.com/getting-started-with-opencv/). En nuestro currículo, nuestro objetivo no es aprender OpenCV, sino mostrarte algunos ejemplos de cuándo se puede usar y cómo.

### Cargando Imágenes

Las imágenes en Python pueden ser representadas de manera conveniente por arreglos de NumPy. Por ejemplo, las imágenes en escala de grises con un tamaño de 320x200 píxeles se almacenarían en un arreglo de 200x320, y las imágenes a color de la misma dimensión tendrían una forma de 200x320x3 (para 3 canales de color). Para cargar una imagen, puedes usar el siguiente código:

```python
import cv2
import matplotlib.pyplot as plt

im = cv2.imread('image.jpeg')
plt.imshow(im)
```

Tradicionalmente, OpenCV utiliza codificación BGR (Azul-Verde-Rojo) para imágenes a color, mientras que el resto de las herramientas de Python utilizan el más tradicional RGB (Rojo-Verde-Azul). Para que la imagen se vea correctamente, necesitas convertirla al espacio de color RGB, ya sea intercambiando dimensiones en el arreglo de NumPy o llamando a una función de OpenCV:

```python
im = cv2.cvtColor(im,cv2.COLOR_BGR2RGB)
```

Las mismas funciones `cvtColor` function can be used to perform other color space transformations such as converting an image to grayscale or to the HSV (Hue-Saturation-Value) color space.

You can also use OpenCV to load video frame-by-frame - an example is given in the exercise [OpenCV Notebook](../../../../../lessons/4-ComputerVision/06-IntroCV/OpenCV.ipynb).

### Image Processing

Before feeding an image to a neural network, you may want to apply several pre-processing steps. OpenCV can do many things, including:

* **Resizing** the image using `im = cv2.resize(im, (320,200),interpolation=cv2.INTER_LANCZOS)`
* **Blurring** the image using `im = cv2.medianBlur(im,3)` or `im = cv2.GaussianBlur(im, (3,3), 0)`
* Changing the **brightness and contrast** of the image can be done by NumPy array manipulations, as described [in this Stackoverflow note](https://stackoverflow.com/questions/39308030/how-do-i-increase-the-contrast-of-an-image-in-python-opencv).
* Using [thresholding](https://docs.opencv.org/4.x/d7/d4d/tutorial_py_thresholding.html) by calling `cv2.threshold`/`cv2.adaptiveThreshold`, que a menudo son preferibles a ajustar el brillo o el contraste.
* Aplicar diferentes [transformaciones](https://docs.opencv.org/4.5.5/da/d6e/tutorial_py_geometric_transformations.html) a la imagen:
    - **[Transformaciones afines](https://docs.opencv.org/4.5.5/d4/d61/tutorial_warp_affine.html)** pueden ser útiles si necesitas combinar rotación, redimensionamiento y sesgo en la imagen y conoces la ubicación de origen y destino de tres puntos en la imagen. Las transformaciones afines mantienen las líneas paralelas.
    - **[Transformaciones de perspectiva](https://medium.com/analytics-vidhya/opencv-perspective-transformation-9edffefb2143)** pueden ser útiles cuando conoces las posiciones de origen y destino de 4 puntos en la imagen. Por ejemplo, si tomas una foto de un documento rectangular a través de la cámara de un smartphone desde algún ángulo, y deseas hacer una imagen rectangular del documento en sí.
* Comprender el movimiento dentro de la imagen utilizando **[flujo óptico](https://docs.opencv.org/4.5.5/d4/dee/tutorial_optical_flow.html)**.

## Ejemplos de uso de la Visión por Computadora

En nuestro [Cuaderno de OpenCV](../../../../../lessons/4-ComputerVision/06-IntroCV/OpenCV.ipynb), damos algunos ejemplos de cuándo se puede usar la visión por computadora para realizar tareas específicas:

* **Pre-procesar una fotografía de un libro en Braille**. Nos enfocamos en cómo podemos usar umbralización, detección de características, transformación de perspectiva y manipulaciones de NumPy para separar símbolos individuales de Braille para su posterior clasificación por una red neuronal.

![Imagen de Braille](../../../../../translated_images/braille.341962ff76b1bd7044409371d3de09ced5028132aef97344ea4b7468c1208126.it.jpeg) | ![Imagen de Braille Pre-procesada](../../../../../translated_images/braille-result.46530fea020b03c76aac532d7d6eeef7f6fb35b55b1001cd21627907dabef3ed.it.png) | ![Símbolos de Braille](../../../../../translated_images/braille-symbols.0159185ab69d533909dc4d7d26a1971b51401c6a80eb3a5584f250ea880af88b.it.png)
----|-----|-----

> Imagen de [OpenCV.ipynb](../../../../../lessons/4-ComputerVision/06-IntroCV/OpenCV.ipynb)

* **Detectar movimiento en video utilizando diferencia de fotogramas**. Si la cámara está fija, entonces los fotogramas del flujo de la cámara deberían ser bastante similares entre sí. Dado que los fotogramas se representan como arreglos, al restar esos arreglos de dos fotogramas subsecuentes obtendremos la diferencia de píxeles, que debería ser baja para fotogramas estáticos y aumentar una vez que haya un movimiento sustancial en la imagen.

![Imagen de fotogramas de video y diferencias de fotogramas](../../../../../translated_images/frame-difference.706f805491a0883c938e16447bf5eb2f7d69e812c7f743cbe7d7c7645168f81f.it.png)

> Imagen de [OpenCV.ipynb](../../../../../lessons/4-ComputerVision/06-IntroCV/OpenCV.ipynb)

* **Detectar movimiento utilizando Flujo Óptico**. [El flujo óptico](https://docs.opencv.org/3.4/d4/dee/tutorial_optical_flow.html) nos permite entender cómo se mueven los píxeles individuales en los fotogramas de video. Hay dos tipos de flujo óptico:

   - **Flujo Óptico Denso** calcula el campo vectorial que muestra para cada píxel hacia dónde se está moviendo.
   - **Flujo Óptico Escaso** se basa en tomar algunas características distintivas en la imagen (por ejemplo, bordes) y construir su trayectoria de un fotograma a otro.

![Imagen de Flujo Óptico](../../../../../translated_images/optical.1f4a94464579a83a10784f3c07fe7228514714b96782edf50e70ccd59d2d8c4f.it.png)

> Imagen de [OpenCV.ipynb](../../../../../lessons/4-ComputerVision/06-IntroCV/OpenCV.ipynb)

## ✍️ Cuadernos de Ejemplo: OpenCV [prueba OpenCV en acción](../../../../../lessons/4-ComputerVision/06-IntroCV/OpenCV.ipynb)

Hagamos algunos experimentos con OpenCV explorando [Cuaderno de OpenCV](../../../../../lessons/4-ComputerVision/06-IntroCV/OpenCV.ipynb)

## Conclusión

A veces, tareas relativamente complejas como la detección de movimiento o la detección de yemas de los dedos pueden resolverse puramente mediante visión por computadora. Por lo tanto, es muy útil conocer las técnicas básicas de visión por computadora y lo que bibliotecas como OpenCV pueden hacer.

## 🚀 Desafío

Mira [este video](https://docs.microsoft.com/shows/ai-show/ai-show--2021-opencv-ai-competition--grand-prize-winners--cortic-tigers--episode-32?WT.mc_id=academic-77998-cacaste) del programa de IA para aprender sobre el proyecto Cortic Tigers y cómo construyeron una solución basada en bloques para democratizar las tareas de visión por computadora a través de un robot. Investiga sobre otros proyectos como este que ayuden a nuevos aprendices a ingresar al campo.

## [Cuestionario posterior a la clase](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/206)

## Revisión y Autoestudio

Lee más sobre el flujo óptico [en este gran tutorial](https://learnopencv.com/optical-flow-in-opencv/).

## [Asignación](lab/README.md)

En este laboratorio, tomarás un video con gestos simples, y tu objetivo es extraer movimientos arriba/abajo/izquierda/derecha utilizando flujo óptico.

<img src="images/palm-movement.png" width="30%" alt="Marco de Movimiento de Palma"/>

**Disclaimer**: 
This document has been translated using machine-based AI translation services. While we strive for accuracy, please be aware that automated translations may contain errors or inaccuracies. The original document in its native language should be considered the authoritative source. For critical information, professional human translation is recommended. We are not liable for any misunderstandings or misinterpretations arising from the use of this translation.