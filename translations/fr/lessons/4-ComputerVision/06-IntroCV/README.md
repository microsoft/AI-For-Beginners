# Introduction à la Vision par Ordinateur

La [Vision par Ordinateur](https://wikipedia.org/wiki/Computer_vision) est une discipline dont l'objectif est de permettre aux ordinateurs d'acquérir une compréhension de haut niveau des images numériques. C'est une définition assez large, car *comprendre* peut signifier de nombreuses choses différentes, y compris trouver un objet sur une image (**détection d'objet**), comprendre ce qui se passe (**détection d'événements**), décrire une image en texte, ou reconstruire une scène en 3D. Il existe également des tâches spéciales liées aux images humaines : estimation de l'âge et des émotions, détection et identification de visages, et estimation de la pose en 3D, pour n'en nommer que quelques-unes.

## [Quiz avant le cours](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/106)

L'une des tâches les plus simples de la vision par ordinateur est **la classification d'images**.

La vision par ordinateur est souvent considérée comme une branche de l'IA. De nos jours, la plupart des tâches de vision par ordinateur sont résolues à l'aide de réseaux neuronaux. Nous allons en apprendre davantage sur le type spécial de réseaux neuronaux utilisés pour la vision par ordinateur, [les réseaux neuronaux convolutionnels](../07-ConvNets/README.md), tout au long de cette section.

Cependant, avant de passer l'image à un réseau neuronal, dans de nombreux cas, il est judicieux d'utiliser certaines techniques algorithmiques pour améliorer l'image.

Il existe plusieurs bibliothèques Python disponibles pour le traitement d'images :

* **[imageio](https://imageio.readthedocs.io/en/stable/)** peut être utilisé pour lire/écrire différents formats d'image. Il prend également en charge ffmpeg, un outil utile pour convertir des images de trames vidéo.
* **[Pillow](https://pillow.readthedocs.io/en/stable/index.html)** (également connu sous le nom de PIL) est un peu plus puissant et prend également en charge certaines manipulations d'images telles que le morphing, les ajustements de palette, et plus encore.
* **[OpenCV](https://opencv.org/)** est une bibliothèque de traitement d'images puissante écrite en C++, qui est devenue la norme *de facto* pour le traitement d'images. Elle dispose d'une interface Python pratique.
* **[dlib](http://dlib.net/)** est une bibliothèque C++ qui implémente de nombreux algorithmes d'apprentissage automatique, y compris certains des algorithmes de vision par ordinateur. Elle dispose également d'une interface Python et peut être utilisée pour des tâches difficiles telles que la détection de visages et de points de repère faciaux.

## OpenCV

[OpenCV](https://opencv.org/) est considérée comme la norme *de facto* pour le traitement d'images. Elle contient de nombreux algorithmes utiles, implémentés en C++. Vous pouvez également appeler OpenCV depuis Python.

Un bon endroit pour apprendre OpenCV est [ce cours Learn OpenCV](https://learnopencv.com/getting-started-with-opencv/). Dans notre programme, notre objectif n'est pas d'apprendre OpenCV, mais de vous montrer quelques exemples de quand cela peut être utilisé, et comment.

### Chargement des Images

Les images en Python peuvent être représentées de manière pratique par des tableaux NumPy. Par exemple, les images en niveaux de gris de taille 320x200 pixels seraient stockées dans un tableau de 200x320, et les images couleur de la même dimension auraient une forme de 200x320x3 (pour 3 canaux de couleur). Pour charger une image, vous pouvez utiliser le code suivant :

```python
import cv2
import matplotlib.pyplot as plt

im = cv2.imread('image.jpeg')
plt.imshow(im)
```

Traditionnellement, OpenCV utilise un encodage BGR (Bleu-Vert-Rouge) pour les images couleur, tandis que le reste des outils Python utilise le plus traditionnel RGB (Rouge-Vert-Bleu). Pour que l'image apparaisse correctement, vous devez la convertir en espace colorimétrique RGB, soit en échangeant les dimensions dans le tableau NumPy, soit en appelant une fonction OpenCV :

```python
im = cv2.cvtColor(im,cv2.COLOR_BGR2RGB)
```

Les mêmes fonctions `cvtColor` function can be used to perform other color space transformations such as converting an image to grayscale or to the HSV (Hue-Saturation-Value) color space.

You can also use OpenCV to load video frame-by-frame - an example is given in the exercise [OpenCV Notebook](../../../../../lessons/4-ComputerVision/06-IntroCV/OpenCV.ipynb).

### Image Processing

Before feeding an image to a neural network, you may want to apply several pre-processing steps. OpenCV can do many things, including:

* **Resizing** the image using `im = cv2.resize(im, (320,200),interpolation=cv2.INTER_LANCZOS)`
* **Blurring** the image using `im = cv2.medianBlur(im,3)` or `im = cv2.GaussianBlur(im, (3,3), 0)`
* Changing the **brightness and contrast** of the image can be done by NumPy array manipulations, as described [in this Stackoverflow note](https://stackoverflow.com/questions/39308030/how-do-i-increase-the-contrast-of-an-image-in-python-opencv).
* Using [thresholding](https://docs.opencv.org/4.x/d7/d4d/tutorial_py_thresholding.html) by calling `cv2.threshold`/`cv2.adaptiveThreshold`, qui sont souvent préférables à l'ajustement de la luminosité ou du contraste.
* Application de différentes [transformations](https://docs.opencv.org/4.5.5/da/d6e/tutorial_py_geometric_transformations.html) à l'image :
    - **[Transformations affines](https://docs.opencv.org/4.5.5/d4/d61/tutorial_warp_affine.html)** peuvent être utiles si vous devez combiner rotation, redimensionnement et déformation de l'image et que vous connaissez la position source et destination de trois points dans l'image. Les transformations affines gardent les lignes parallèles.
    - **[Transformations de perspective](https://medium.com/analytics-vidhya/opencv-perspective-transformation-9edffefb2143)** peuvent être utiles lorsque vous connaissez les positions source et destination de 4 points dans l'image. Par exemple, si vous prenez une photo d'un document rectangulaire avec un smartphone sous un certain angle, et que vous souhaitez obtenir une image rectangulaire du document lui-même.
* Comprendre le mouvement à l'intérieur de l'image en utilisant **[le flux optique](https://docs.opencv.org/4.5.5/d4/dee/tutorial_optical_flow.html)**.

## Exemples d'utilisation de la Vision par Ordinateur

Dans notre [Notebook OpenCV](../../../../../lessons/4-ComputerVision/06-IntroCV/OpenCV.ipynb), nous donnons quelques exemples de quand la vision par ordinateur peut être utilisée pour effectuer des tâches spécifiques :

* **Prétraitement d'une photographie d'un livre en braille**. Nous nous concentrons sur la façon dont nous pouvons utiliser le seuillage, la détection de caractéristiques, la transformation de perspective et les manipulations NumPy pour séparer les symboles braille individuels pour une classification ultérieure par un réseau neuronal.

![Image en Braille](../../../../../translated_images/braille.341962ff76b1bd7044409371d3de09ced5028132aef97344ea4b7468c1208126.fr.jpeg) | ![Image en Braille Prétraitée](../../../../../translated_images/braille-result.46530fea020b03c76aac532d7d6eeef7f6fb35b55b1001cd21627907dabef3ed.fr.png) | ![Symboles en Braille](../../../../../translated_images/braille-symbols.0159185ab69d533909dc4d7d26a1971b51401c6a80eb3a5584f250ea880af88b.fr.png)
----|-----|-----

> Image provenant de [OpenCV.ipynb](../../../../../lessons/4-ComputerVision/06-IntroCV/OpenCV.ipynb)

* **Détection de mouvement dans une vidéo à l'aide de la différence de trame**. Si la caméra est fixe, alors les trames du flux de la caméra devraient être assez similaires les unes aux autres. Puisque les trames sont représentées sous forme de tableaux, il suffit de soustraire ces tableaux pour deux trames consécutives afin d'obtenir la différence de pixels, qui devrait être faible pour des trames statiques et devenir plus élevée lorsqu'il y a un mouvement substantiel dans l'image.

![Image de trames vidéo et différences de trame](../../../../../translated_images/frame-difference.706f805491a0883c938e16447bf5eb2f7d69e812c7f743cbe7d7c7645168f81f.fr.png)

> Image provenant de [OpenCV.ipynb](../../../../../lessons/4-ComputerVision/06-IntroCV/OpenCV.ipynb)

* **Détection de mouvement à l'aide du Flux Optique**. [Le flux optique](https://docs.opencv.org/3.4/d4/dee/tutorial_optical_flow.html) nous permet de comprendre comment les pixels individuels sur les trames vidéo se déplacent. Il existe deux types de flux optique :

   - **Flux Optique Dense** calcule le champ vectoriel qui montre pour chaque pixel où il se déplace
   - **Flux Optique Sparse** est basé sur la prise de certaines caractéristiques distinctives dans l'image (par exemple, les contours), et la construction de leur trajectoire d'une trame à l'autre.

![Image du Flux Optique](../../../../../translated_images/optical.1f4a94464579a83a10784f3c07fe7228514714b96782edf50e70ccd59d2d8c4f.fr.png)

> Image provenant de [OpenCV.ipynb](../../../../../lessons/4-ComputerVision/06-IntroCV/OpenCV.ipynb)

## ✍️ Notebooks d'exemple : OpenCV [essayez OpenCV en action](../../../../../lessons/4-ComputerVision/06-IntroCV/OpenCV.ipynb)

Faisons quelques expériences avec OpenCV en explorant [le Notebook OpenCV](../../../../../lessons/4-ComputerVision/06-IntroCV/OpenCV.ipynb)

## Conclusion

Parfois, des tâches relativement complexes telles que la détection de mouvement ou la détection de bout de doigt peuvent être résolues uniquement par la vision par ordinateur. Ainsi, il est très utile de connaître les techniques de base de la vision par ordinateur, et ce que des bibliothèques comme OpenCV peuvent faire.

## 🚀 Défi

Regardez [cette vidéo](https://docs.microsoft.com/shows/ai-show/ai-show--2021-opencv-ai-competition--grand-prize-winners--cortic-tigers--episode-32?WT.mc_id=academic-77998-cacaste) de l'émission AI pour en savoir plus sur le projet Cortic Tigers et comment ils ont construit une solution basée sur des blocs pour démocratiser les tâches de vision par ordinateur via un robot. Faites des recherches sur d'autres projets similaires qui aident à intégrer de nouveaux apprenants dans le domaine.

## [Quiz après le cours](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/206)

## Revue & Auto-étude

Lisez-en plus sur le flux optique [dans ce super tutoriel](https://learnopencv.com/optical-flow-in-opencv/).

## [Devoir](lab/README.md)

Dans ce laboratoire, vous allez filmer une vidéo avec des gestes simples, et votre objectif est d'extraire les mouvements haut/bas/gauche/droite en utilisant le flux optique.

<img src="images/palm-movement.png" width="30%" alt="Image de Mouvement de la Paume"/>

**Avertissement** :  
Ce document a été traduit à l'aide de services de traduction automatique basés sur l'IA. Bien que nous nous efforçons d'assurer l'exactitude, veuillez noter que les traductions automatiques peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue native doit être considéré comme la source autoritaire. Pour des informations critiques, une traduction humaine professionnelle est recommandée. Nous ne sommes pas responsables des malentendus ou des interprétations erronées résultant de l'utilisation de cette traduction.