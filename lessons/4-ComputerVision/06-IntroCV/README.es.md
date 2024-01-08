# Introducción a la visión por computadora

[Computer Vision](https://wikipedia.org/wiki/Computer_vision) es una disciplina cuyo objetivo es permitir que las computadoras obtengan un alto nivel de comprensión de las imágenes digitales. Esta es una definición bastante amplia, porque *comprender* puede significar muchas cosas diferentes, incluyendo encontrar un objeto en una imagen (**detección de objetos**), comprender lo que está sucediendo (**detección de eventos**), describir una imagen en texto o reconstruir una escena en 3D. También hay tareas especiales relacionadas con imágenes humanas: estimación de edad y emociones, detección e identificación de rostros y estimación de pose 3D, por nombrar algunas.

## [Pre-lecture quiz](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/106)

Una de las tareas más simples de la visión por computadora es la **clasificación de imágenes**.

La visión por computadora a menudo se considera una rama de la IA. Hoy en día, la mayoría de las tareas de visión por computadora se resuelven mediante redes neuronales. Aprenderemos más sobre el tipo especial de redes neuronales utilizadas para la visión por computadora, [convolutional neural networks](../07-ConvNets/README.md), a lo largo de esta sección.

Sin embargo, antes de pasar la imagen a una red neuronal, en muchos casos tiene sentido utilizar algunas técnicas algorítmicas para mejorar la imagen.

Hay varias bibliotecas de Python disponibles para el procesamiento de imágenes:

* **[imageio](https://imageio.readthedocs.io/en/stable/)** se puede utilizar para leer/escribir diferentes formatos de imagen. También es compatible con ffmpeg, una herramienta útil para convertir fotogramas de vídeo en imágenes.
* **[Pillow](https://pillow.readthedocs.io/en/stable/index.html)** (también conocido como PIL) es un poco más potente y también admite algunas manipulaciones de imágenes, como transformación, ajustes de paleta y más.
* **[OpenCV](https://opencv.org/)** es una potente biblioteca de procesamiento de imágenes escrita en C++, que se ha convertido en el estándar *de facto* para el procesamiento de imágenes. Tiene una cómoda interfaz Python.
* **[dlib](http://dlib.net/)** es una biblioteca de C++ que implementa muchos algoritmos de aprendizaje automático, incluidos algunos de los algoritmos de visión por computadora. También tiene una interfaz Python y se puede utilizar para tareas desafiantes como la detección de rostros y puntos de referencia faciales.

## OpenCV

[OpenCV](https://opencv.org/) se considera el estándar *de facto* para el procesamiento de imágenes. Contiene muchos algoritmos útiles, implementados en C++. También puedes llamar a OpenCV desde Python.

Un buen lugar para aprender OpenCV es [this Learn OpenCV course](https://learnopencv.com/getting-started-with-opencv/). En nuestro plan de estudios, nuestro objetivo no es aprender OpenCV, sino mostrarle algunos ejemplos de cuándo se puede utilizar y cómo.

### Cargando imágenes

Las imágenes en Python se pueden representar convenientemente mediante matrices NumPy. Por ejemplo, las imágenes en escala de grises con un tamaño de 320x200 píxeles se almacenarían en una matriz de 200x320, y las imágenes en color de la misma dimensión tendrían una forma de 200x320x3 (para 3 canales de color). Para cargar una imagen, puede utilizar el siguiente código:

```python
import cv2
import matplotlib.pyplot as plt

im = cv2.imread('image.jpeg')
plt.imshow(im)
```

Tradicionalmente, OpenCV usos Codificación BGR (Azul-Verde-Rojo) para imágenes en color, mientras que el resto de herramientas de Python utilizan la más tradicional RGB (Rojo-Verde-Azul). Para que la imagen se vea bien, debe convertirla al espacio de color RGB, ya sea intercambiando dimensiones en la matriz NumPy o llamando a una función OpenCV:

```python
im = cv2.cvtColor(im,cv2.COLOR_BGR2RGB)
```

La misma `cvtColor` La función se puede utilizar para realizar otras transformaciones del espacio de color, como convertir una imagen a escala de grises o al espacio de color HSV (Tono-Saturación-Valor).

También puede utilizar OpenCV para cargar vídeo fotograma a fotograma; en el ejercicio se proporciona un ejemplo [OpenCV Notebook](OpenCV.ipynb).

### Procesamiento de imágenes

Antes de enviar una imagen a una red neuronal, es posible que desee aplicar varios pasos de preprocesamiento.

* **Resizing** la imagen usando `im = cv2.resize(im, (320,200),interpolation=cv2.INTER_LANCZOS)`
* **Blurring** la imagen usando `im = cv2.medianBlur(im,3)` o `im = cv2.GaussianBlur(im, (3,3), 0)`
* Se puede cambiar el **brillo y contraste** de la imagen mediante manipulaciones de matriz NumPy, como se describe [in this Stackoverflow note](https://stackoverflow.com/questions/39308030/how-do-i-increase-the-contrast-of-an-image-in-python-opencv).
* Usando [thresholding](https://docs.opencv.org/4.x/d7/d4d/tutorial_py_thresholding.html) llamando `cv2.threshold`/`cv2.adaptiveThreshold` funciones, lo que a menudo es preferible a ajustar el brillo o el contraste.
* Aplicando diferentes [transformations](https://docs.opencv.org/4.5.5/da/d6e/tutorial_py_geometric_transformations.html) a la imagen:
    - **[Affine transformations](https://docs.opencv.org/4.5.5/d4/d61/tutorial_warp_affine.html)** Puede resultar útil si necesita combinar rotación, cambio de tamaño e inclinación de la imagen y conoce la ubicación de origen y destino de tres puntos de la imagen. Las transformaciones afines mantienen las líneas paralelas paralelas.
    - **[Perspective transformations](https://medium.com/analytics-vidhya/opencv-perspective-transformation-9edffefb2143)** Puede resultar útil cuando conoce las posiciones de origen y destino de 4 puntos en la imagen. Por ejemplo, si toma una fotografía de un documento rectangular con la cámara de un teléfono inteligente desde algún ángulo y desea crear una imagen rectangular del documento en sí.
* Comprender el movimiento dentro de la imagen mediante el uso **[optical flow](https://docs.opencv.org/4.5.5/d4/dee/tutorial_optical_flow.html)**.

## Ejemplos de uso de la visión por computadora

En nuestro [OpenCV Notebook](OpenCV.ipynb), damos algunos ejemplos de cuándo se puede utilizar la visión por computadora para realizar tareas específicas:

* **Preprocesamiento de una fotografía de un libro Braille**. Nos centramos en cómo podemos utilizar umbrales, detección de características, transformación de perspectiva y manipulaciones NumPy para separar símbolos Braille individuales para su posterior clasificación mediante una red neuronal.

![Braille Image](data/braille.jpeg) | ![Braille Image Pre-processed](images/braille-result.png) | ![Braille Symbols](images/braille-symbols.png)
----|-----|-----

> Imagen de [OpenCV.ipynb](OpenCV.ipynb)

* **Detección de movimiento en video usando diferencia de fotogramas**. Si la cámara está fija, los fotogramas de la cámara deberían ser bastante similares entre sí. Dado que los fotogramas se representan como matrices, simplemente restando esas matrices para dos fotogramas posteriores obtendremos la diferencia de píxeles, que debería ser baja para fotogramas estáticos y aumentar una vez que haya un movimiento sustancial en la imagen.

![Image of video frames and frame differences](images/frame-difference.png)

> Imagen de [OpenCV.ipynb](OpenCV.ipynb)

* **Detección de movimiento mediante flujo óptico**. [Optical flow](https://docs.opencv.org/3.4/d4/dee/tutorial_optical_flow.html) nos permite comprender cómo se mueven los píxeles individuales en los cuadros de video. Hay dos tipos de flujo óptico:

* - **Flujo óptico denso** calcula el campo vectorial que muestra para cada píxel dónde se mueve
    - **Flujo óptico disperso** se basa en tomar algunas características distintivas de la imagen (por ejemplo, bordes) y construir su trayectoria de cuadro a cuadro.
   
![Image of Optical Flow](images/optical.png)

> Imagen de [OpenCV.ipynb](OpenCV.ipynb)

## ✍️ Cuadernos de ejemplo: OpenCV [try OpenCV in Action](OpenCV.ipynb)

Hagamos algunos experimentos con OpenCV explorando [OpenCV Notebook](OpenCV.ipynb)

## Conclusión

A veces, tareas relativamente complejas, como la detección de movimiento o la detección de las yemas de los dedos, pueden resolverse únicamente mediante visión por computadora. Por lo tanto, es muy útil conocer las técnicas básicas de visión por computadora y qué pueden hacer bibliotecas como OpenCV.

## 🚀 Desafío

Mirar [this video](https://docs.microsoft.com/shows/ai-show/ai-show--2021-opencv-ai-competition--grand-prize-winners--cortic-tigers--episode-32?WT.mc_id=academic-77998-cacaste) del programa de IA para conocer el proyecto Cortic Tigers y cómo construyeron una solución basada en bloques para democratizar las tareas de visión por computadora a través de un robot. Investigue un poco sobre otros proyectos como este que ayuden a incorporar nuevos estudiantes al campo.

## [Post-lecture quiz](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/206)

## Revisión y autoestudio

Lea más sobre el flujo óptico [in this great tutorial](https://learnopencv.com/optical-flow-in-opencv/).

## [Assignment](lab/README.md)

En esta práctica de laboratorio, grabará un video con gestos simples y su objetivo es extraer movimientos hacia arriba/abajo/izquierda/derecha utilizando el flujo óptico.

<img src="images/palm-movement.png" width="30%" alt="Palm Movement Frame"/>
