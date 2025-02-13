# Einführung in die Computer Vision

[Computer Vision](https://wikipedia.org/wiki/Computer_vision) ist ein Fachgebiet, das darauf abzielt, Computern ein umfassendes Verständnis digitaler Bilder zu ermöglichen. Diese Definition ist recht breit gefasst, da *Verstehen* viele verschiedene Bedeutungen haben kann, einschließlich der Identifizierung eines Objekts auf einem Bild (**Objekterkennung**), dem Verständnis dessen, was passiert (**Ereigniserkennung**), der Beschreibung eines Bildes in Text oder der Rekonstruktion einer Szene in 3D. Es gibt auch spezielle Aufgaben im Zusammenhang mit menschlichen Bildern: Alters- und Emotionserkennung, Gesichtserkennung und -identifikation sowie 3D-Pose-Schätzung, um nur einige zu nennen.

## [Vorlesungsquiz](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/106)

Eine der einfachsten Aufgaben der Computer Vision ist die **Bildklassifizierung**.

Computer Vision wird oft als ein Zweig der KI betrachtet. Heutzutage werden die meisten Aufgaben der Computer Vision mit Hilfe von neuronalen Netzwerken gelöst. In diesem Abschnitt werden wir mehr über die speziellen Arten von neuronalen Netzwerken lernen, die für Computer Vision verwendet werden, [faltungsneuronale Netzwerke](../07-ConvNets/README.md).

Bevor Sie jedoch das Bild an ein neuronales Netzwerk übergeben, macht es in vielen Fällen Sinn, einige algorithmische Techniken zur Verbesserung des Bildes zu verwenden.

Es gibt mehrere Python-Bibliotheken für die Bildverarbeitung:

* **[imageio](https://imageio.readthedocs.io/en/stable/)** kann zum Lesen/Schreiben verschiedener Bildformate verwendet werden. Es unterstützt auch ffmpeg, ein nützliches Tool zum Konvertieren von Videobildern in Bilder.
* **[Pillow](https://pillow.readthedocs.io/en/stable/index.html)** (auch bekannt als PIL) ist etwas leistungsfähiger und unterstützt auch einige Bildmanipulationen wie Morphing, Palettenanpassungen und mehr.
* **[OpenCV](https://opencv.org/)** ist eine leistungsstarke Bildverarbeitungsbibliothek, die in C++ geschrieben wurde und zum *de facto* Standard für die Bildverarbeitung geworden ist. Sie hat eine praktische Python-Schnittstelle.
* **[dlib](http://dlib.net/)** ist eine C++-Bibliothek, die viele Algorithmen des maschinellen Lernens implementiert, einschließlich einiger Algorithmen der Computer Vision. Sie hat ebenfalls eine Python-Schnittstelle und kann für herausfordernde Aufgaben wie Gesichtserkennung und Erkennung von Gesichtsmerkmalen verwendet werden.

## OpenCV

[OpenCV](https://opencv.org/) wird als der *de facto* Standard für die Bildverarbeitung angesehen. Es enthält viele nützliche Algorithmen, die in C++ implementiert sind. Sie können OpenCV auch aus Python heraus aufrufen.

Ein guter Ort, um OpenCV zu lernen, ist [dieser Learn OpenCV-Kurs](https://learnopencv.com/getting-started-with-opencv/). In unserem Lehrplan ist es nicht unser Ziel, OpenCV zu lernen, sondern Ihnen einige Beispiele zu zeigen, wann es verwendet werden kann und wie.

### Bilder laden

Bilder in Python können bequem durch NumPy-Arrays dargestellt werden. Beispielsweise würden Graustufenbilder mit einer Größe von 320x200 Pixeln in einem 200x320-Array gespeichert werden, während Farbbilder derselben Dimension die Form 200x320x3 (für 3 Farbkanäle) hätten. Um ein Bild zu laden, können Sie den folgenden Code verwenden:

```python
import cv2
import matplotlib.pyplot as plt

im = cv2.imread('image.jpeg')
plt.imshow(im)
```

Traditionell verwendet OpenCV die BGR (Blau-Grün-Rot) Kodierung für Farbbilder, während die meisten anderen Python-Tools das traditionellere RGB (Rot-Grün-Blau) verwenden. Damit das Bild richtig aussieht, müssen Sie es in den RGB-Farbraum konvertieren, entweder indem Sie die Dimensionen im NumPy-Array vertauschen oder eine OpenCV-Funktion aufrufen:

```python
im = cv2.cvtColor(im,cv2.COLOR_BGR2RGB)
```

Die gleiche `cvtColor` function can be used to perform other color space transformations such as converting an image to grayscale or to the HSV (Hue-Saturation-Value) color space.

You can also use OpenCV to load video frame-by-frame - an example is given in the exercise [OpenCV Notebook](../../../../../lessons/4-ComputerVision/06-IntroCV/OpenCV.ipynb).

### Image Processing

Before feeding an image to a neural network, you may want to apply several pre-processing steps. OpenCV can do many things, including:

* **Resizing** the image using `im = cv2.resize(im, (320,200),interpolation=cv2.INTER_LANCZOS)`
* **Blurring** the image using `im = cv2.medianBlur(im,3)` or `im = cv2.GaussianBlur(im, (3,3), 0)`
* Changing the **brightness and contrast** of the image can be done by NumPy array manipulations, as described [in this Stackoverflow note](https://stackoverflow.com/questions/39308030/how-do-i-increase-the-contrast-of-an-image-in-python-opencv).
* Using [thresholding](https://docs.opencv.org/4.x/d7/d4d/tutorial_py_thresholding.html) by calling `cv2.threshold`/`cv2.adaptiveThreshold` Funktionen, die oft vorzuziehen sind, um Helligkeit oder Kontrast anzupassen.
* Verschiedene [Transformationen](https://docs.opencv.org/4.5.5/da/d6e/tutorial_py_geometric_transformations.html) auf das Bild anwenden:
    - **[Affintransformationen](https://docs.opencv.org/4.5.5/d4/d61/tutorial_warp_affine.html)** können nützlich sein, wenn Sie Rotation, Größenänderung und Verzerrung des Bildes kombinieren müssen und die Quelle und Zielpositionen von drei Punkten im Bild kennen. Affintransformationen halten parallele Linien parallel.
    - **[Perspektivtransformationen](https://medium.com/analytics-vidhya/opencv-perspective-transformation-9edffefb2143)** können nützlich sein, wenn Sie die Quelle und Zielpositionen von 4 Punkten im Bild kennen. Zum Beispiel, wenn Sie ein Bild eines rechteckigen Dokuments mit einer Smartphone-Kamera aus einem bestimmten Winkel aufnehmen und ein rechteckiges Bild des Dokuments selbst erstellen möchten.
* Bewegung im Bild verstehen, indem Sie **[optischen Fluss](https://docs.opencv.org/4.5.5/d4/dee/tutorial_optical_flow.html)** verwenden.

## Beispiele für die Verwendung von Computer Vision

In unserem [OpenCV-Notebook](../../../../../lessons/4-ComputerVision/06-IntroCV/OpenCV.ipynb) geben wir einige Beispiele, wann Computer Vision verwendet werden kann, um spezifische Aufgaben auszuführen:

* **Vorverarbeitung eines Fotos eines Braille-Buchs**. Wir konzentrieren uns darauf, wie wir Schwellenwertbildung, Merkmalsdetektion, Perspektivtransformation und NumPy-Manipulationen verwenden können, um einzelne Braille-Symbole für eine weitere Klassifizierung durch ein neuronales Netzwerk zu trennen.

![Braille-Bild](../../../../../translated_images/braille.341962ff76b1bd7044409371d3de09ced5028132aef97344ea4b7468c1208126.de.jpeg) | ![Vorverarbeitetes Braille-Bild](../../../../../translated_images/braille-result.46530fea020b03c76aac532d7d6eeef7f6fb35b55b1001cd21627907dabef3ed.de.png) | ![Braille-Symbole](../../../../../translated_images/braille-symbols.0159185ab69d533909dc4d7d26a1971b51401c6a80eb3a5584f250ea880af88b.de.png)
----|-----|-----

> Bild aus [OpenCV.ipynb](../../../../../lessons/4-ComputerVision/06-IntroCV/OpenCV.ipynb)

* **Bewegung im Video mithilfe von Frame-Differenz erkennen**. Wenn die Kamera feststeht, sollten die Bilder aus dem Kamerafeed ziemlich ähnlich sein. Da Bilder als Arrays dargestellt werden, erhalten wir durch das Subtrahieren dieser Arrays für zwei aufeinanderfolgende Bilder den Pixelunterschied, der für statische Bilder niedrig sein sollte und höher wird, sobald es eine erhebliche Bewegung im Bild gibt.

![Bild von Video-Frames und Frame-Differenzen](../../../../../translated_images/frame-difference.706f805491a0883c938e16447bf5eb2f7d69e812c7f743cbe7d7c7645168f81f.de.png)

> Bild aus [OpenCV.ipynb](../../../../../lessons/4-ComputerVision/06-IntroCV/OpenCV.ipynb)

* **Bewegung mithilfe des optischen Flusses erkennen**. [Optischer Fluss](https://docs.opencv.org/3.4/d4/dee/tutorial_optical_flow.html) ermöglicht es uns zu verstehen, wie sich einzelne Pixel auf Video-Frames bewegen. Es gibt zwei Arten von optischem Fluss:

   - **Dichter optischer Fluss** berechnet das Vektorfeld, das zeigt, wo sich jeder Pixel bewegt
   - **Sparsame optische Flüsse** basieren darauf, einige markante Merkmale im Bild (z.B. Kanten) zu erfassen und deren Trajektorie von Frame zu Frame zu verfolgen.

![Bild des optischen Flusses](../../../../../translated_images/optical.1f4a94464579a83a10784f3c07fe7228514714b96782edf50e70ccd59d2d8c4f.de.png)

> Bild aus [OpenCV.ipynb](../../../../../lessons/4-ComputerVision/06-IntroCV/OpenCV.ipynb)

## ✍️ Beispielnotebooks: OpenCV [probieren Sie OpenCV in Aktion](../../../../../lessons/4-ComputerVision/06-IntroCV/OpenCV.ipynb)

Lassen Sie uns einige Experimente mit OpenCV durchführen, indem wir das [OpenCV-Notebook](../../../../../lessons/4-ComputerVision/06-IntroCV/OpenCV.ipynb) erkunden.

## Fazit

Manchmal können relativ komplexe Aufgaben wie Bewegungs- oder Fingerspitzen-Erkennung rein durch Computer Vision gelöst werden. Daher ist es sehr hilfreich, die grundlegenden Techniken der Computer Vision zu kennen und zu wissen, was Bibliotheken wie OpenCV leisten können.

## 🚀 Herausforderung

Sehen Sie sich [dieses Video](https://docs.microsoft.com/shows/ai-show/ai-show--2021-opencv-ai-competition--grand-prize-winners--cortic-tigers--episode-32?WT.mc_id=academic-77998-cacaste) aus der AI-Show an, um mehr über das Cortic Tigers-Projekt zu erfahren und wie sie eine blockbasierte Lösung entwickelt haben, um Computer Vision-Aufgaben über einen Roboter zu demokratisieren. Machen Sie etwas Recherche zu anderen Projekten dieser Art, die neuen Lernenden den Einstieg in das Feld erleichtern.

## [Nachlesequiz](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/206)

## Überprüfung & Selbststudium

Lesen Sie mehr über optischen Fluss [in diesem großartigen Tutorial](https://learnopencv.com/optical-flow-in-opencv/).

## [Aufgabe](lab/README.md)

In diesem Labor werden Sie ein Video mit einfachen Gesten aufnehmen, und Ihr Ziel ist es, Bewegungen nach oben/unten/links/rechts mithilfe des optischen Flusses zu extrahieren.

<img src="images/palm-movement.png" width="30%" alt="Palmbewegung Frame"/>

**Haftungsausschluss**:  
Dieses Dokument wurde mit maschinellen KI-Übersetzungsdiensten übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner ursprünglichen Sprache sollte als maßgebliche Quelle betrachtet werden. Für kritische Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die aus der Verwendung dieser Übersetzung resultieren.