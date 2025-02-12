# Introduktion till Datorseende

[Datorseende](https://wikipedia.org/wiki/Computer_vision) är en disciplin vars syfte är att möjliggöra för datorer att få en hög nivå av förståelse av digitala bilder. Detta är en ganska bred definition, eftersom *förståelse* kan betyda många olika saker, inklusive att hitta ett objekt på en bild (**objektdetektering**), förstå vad som händer (**händelsedetektering**), beskriva en bild med text eller rekonstruera en scen i 3D. Det finns också särskilda uppgifter relaterade till mänskliga bilder: ålders- och känslomätningsuppskattning, ansiktsdetektering och identifiering, samt 3D-hållningsuppskattning, för att nämna några.

## [För-föreläsningsquiz](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/106)

En av de enklaste uppgifterna inom datorseende är **bildklassificering**.

Datorseende betraktas ofta som en gren av AI. Numera löses de flesta uppgifter inom datorseende med hjälp av neurala nätverk. Vi kommer att lära oss mer om den speciella typen av neurala nätverk som används för datorseende, [konvolutionella neurala nätverk](../07-ConvNets/README.md), under denna sektion.

Innan du skickar bilden till ett neuralt nätverk är det dock i många fall förnuftigt att använda några algoritmiska tekniker för att förbättra bilden.

Det finns flera Python-bibliotek tillgängliga för bildbehandling:

* **[imageio](https://imageio.readthedocs.io/en/stable/)** kan användas för att läsa/skriva olika bildformat. Det stöder också ffmpeg, ett användbart verktyg för att konvertera videoramar till bilder.
* **[Pillow](https://pillow.readthedocs.io/en/stable/index.html)** (även känt som PIL) är något mer kraftfullt och stöder även viss bildmanipulation såsom morphing, palettjusteringar och mer.
* **[OpenCV](https://opencv.org/)** är ett kraftfullt bildbehandlingsbibliotek skrivet i C++, som har blivit den *de facto* standarden för bildbehandling. Det har ett praktiskt Python-gränssnitt.
* **[dlib](http://dlib.net/)** är ett C++-bibliotek som implementerar många maskininlärningsalgoritmer, inklusive några av datorseendets algoritmer. Det har också ett Python-gränssnitt och kan användas för utmanande uppgifter såsom ansikts- och ansiktslandmarksdetektering.

## OpenCV

[OpenCV](https://opencv.org/) anses vara den *de facto* standarden för bildbehandling. Det innehåller många användbara algoritmer, implementerade i C++. Du kan även anropa OpenCV från Python.

En bra plats att lära sig OpenCV är [denna Learn OpenCV-kurs](https://learnopencv.com/getting-started-with-opencv/). I vår läroplan är vårt mål inte att lära oss OpenCV, utan att visa dig några exempel på när det kan användas och hur.

### Ladda Bilder

Bilder i Python kan bekvämt representeras av NumPy-arrayer. Till exempel skulle gråskalebilder med storleken 320x200 pixlar lagras i en 200x320-array, och färgbilder av samma dimension skulle ha formen 200x320x3 (för 3 färgkanaler). För att ladda en bild kan du använda följande kod:

```python
import cv2
import matplotlib.pyplot as plt

im = cv2.imread('image.jpeg')
plt.imshow(im)
```

Traditionellt använder OpenCV BGR (Blå-Grön-Röd) kodning för färgbilder, medan resten av Python-verktygen använder den mer traditionella RGB (Röd-Grön-Blå). För att bilden ska se korrekt ut måste du konvertera den till RGB-färgrymden, antingen genom att byta dimensioner i NumPy-arrayen eller genom att anropa en OpenCV-funktion:

```python
im = cv2.cvtColor(im,cv2.COLOR_BGR2RGB)
```

De samma `cvtColor` function can be used to perform other color space transformations such as converting an image to grayscale or to the HSV (Hue-Saturation-Value) color space.

You can also use OpenCV to load video frame-by-frame - an example is given in the exercise [OpenCV Notebook](../../../../../lessons/4-ComputerVision/06-IntroCV/OpenCV.ipynb).

### Image Processing

Before feeding an image to a neural network, you may want to apply several pre-processing steps. OpenCV can do many things, including:

* **Resizing** the image using `im = cv2.resize(im, (320,200),interpolation=cv2.INTER_LANCZOS)`
* **Blurring** the image using `im = cv2.medianBlur(im,3)` or `im = cv2.GaussianBlur(im, (3,3), 0)`
* Changing the **brightness and contrast** of the image can be done by NumPy array manipulations, as described [in this Stackoverflow note](https://stackoverflow.com/questions/39308030/how-do-i-increase-the-contrast-of-an-image-in-python-opencv).
* Using [thresholding](https://docs.opencv.org/4.x/d7/d4d/tutorial_py_thresholding.html) by calling `cv2.threshold`/`cv2.adaptiveThreshold` funktionerna, som ofta är att föredra framför att justera ljusstyrka eller kontrast.
* Tillämpa olika [transformeringar](https://docs.opencv.org/4.5.5/da/d6e/tutorial_py_geometric_transformations.html) på bilden:
    - **[Affina transformationer](https://docs.opencv.org/4.5.5/d4/d61/tutorial_warp_affine.html)** kan vara användbara om du behöver kombinera rotation, ändring av storlek och snedvridning på bilden och du känner till käll- och destinationslägen för tre punkter i bilden. Affina transformationer håller parallella linjer parallella.
    - **[Perspektivtransformationer](https://medium.com/analytics-vidhya/opencv-perspective-transformation-9edffefb2143)** kan vara användbara när du känner till käll- och destinationspositionerna för 4 punkter i bilden. Till exempel, om du tar en bild av ett rektangulärt dokument via en smartphonekamera från en viss vinkel, och du vill göra en rektangulär bild av dokumentet självt.
* Förstå rörelse inuti bilden genom att använda **[optisk flöde](https://docs.opencv.org/4.5.5/d4/dee/tutorial_optical_flow.html)**.

## Exempel på att använda Datorseende

I vår [OpenCV Notebook](../../../../../lessons/4-ComputerVision/06-IntroCV/OpenCV.ipynb) ger vi några exempel på när datorseende kan användas för att utföra specifika uppgifter:

* **Förbehandling av ett fotografi av en Braillebok**. Vi fokuserar på hur vi kan använda tröskelvärden, funktionsdetektering, perspektivtransformation och NumPy-manipulationer för att separera individuella Braille-symboler för vidare klassificering av ett neuralt nätverk.

![Braille Image](../../../../../translated_images/braille.341962ff76b1bd7044409371d3de09ced5028132aef97344ea4b7468c1208126.sw.jpeg) | ![Braille Image Pre-processed](../../../../../translated_images/braille-result.46530fea020b03c76aac532d7d6eeef7f6fb35b55b1001cd21627907dabef3ed.sw.png) | ![Braille Symbols](../../../../../translated_images/braille-symbols.0159185ab69d533909dc4d7d26a1971b51401c6a80eb3a5584f250ea880af88b.sw.png)
----|-----|-----

> Bild från [OpenCV.ipynb](../../../../../lessons/4-ComputerVision/06-IntroCV/OpenCV.ipynb)

* **Detektera rörelse i video med hjälp av ramdiff**. Om kameran är fixerad, bör ramar från kameraflödet vara ganska lika varandra. Eftersom ramar representeras som arrayer, får vi genom att subtrahera dessa arrayer för två efterföljande ramar pixel-differensen, som bör vara låg för statiska ramar och bli högre när det finns betydande rörelse i bilden.

![Image of video frames and frame differences](../../../../../translated_images/frame-difference.706f805491a0883c938e16447bf5eb2f7d69e812c7f743cbe7d7c7645168f81f.sw.png)

> Bild från [OpenCV.ipynb](../../../../../lessons/4-ComputerVision/06-IntroCV/OpenCV.ipynb)

* **Detektera rörelse med hjälp av Optisk Flöde**. [Optisk flöde](https://docs.opencv.org/3.4/d4/dee/tutorial_optical_flow.html) gör att vi kan förstå hur individuella pixlar på videoramrörelser. Det finns två typer av optiskt flöde:

   - **Tätt optiskt flöde** beräknar vektorfältet som visar för varje pixel var den rör sig.
   - **Spars optiskt flöde** baseras på att ta några distinkta funktioner i bilden (t.ex. kanter) och bygga deras bana från ram till ram.

![Image of Optical Flow](../../../../../translated_images/optical.1f4a94464579a83a10784f3c07fe7228514714b96782edf50e70ccd59d2d8c4f.sw.png)

> Bild från [OpenCV.ipynb](../../../../../lessons/4-ComputerVision/06-IntroCV/OpenCV.ipynb)

## ✍️ Exempel Notebooks: OpenCV [prova OpenCV i praktiken](../../../../../lessons/4-ComputerVision/06-IntroCV/OpenCV.ipynb)

Låt oss göra några experiment med OpenCV genom att utforska [OpenCV Notebook](../../../../../lessons/4-ComputerVision/06-IntroCV/OpenCV.ipynb)

## Slutsats

Ibland kan relativt komplexa uppgifter som rörelsedetektering eller fingertoppsdetektering lösas enbart med datorseende. Därför är det mycket hjälpsamt att känna till de grundläggande teknikerna inom datorseende och vad bibliotek som OpenCV kan göra.

## 🚀 Utmaning

Titta på [denna video](https://docs.microsoft.com/shows/ai-show/ai-show--2021-opencv-ai-competition--grand-prize-winners--cortic-tigers--episode-32?WT.mc_id=academic-77998-cacaste) från AI-showen för att lära dig om Cortic Tigers-projektet och hur de byggde en blockbaserad lösning för att demokratisera datorseendeuppgifter via en robot. Gör lite forskning om andra projekt som detta som hjälper nya inlärare att komma in i området.

## [Efter-föreläsningsquiz](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/206)

## Granskning & Självstudie

Läs mer om optiskt flöde [i denna fantastiska handledning](https://learnopencv.com/optical-flow-in-opencv/).

## [Uppgift](lab/README.md)

I detta laboratorium kommer du att spela in en video med enkla gester, och ditt mål är att extrahera upp/ned/vänster/höger rörelser med hjälp av optiskt flöde.

<img src="images/palm-movement.png" width="30%" alt="Palm Movement Frame"/>

**Ansvarsfriskrivning**:  
Detta dokument har översatts med hjälp av maskinbaserade AI-översättningstjänster. Även om vi strävar efter noggrannhet, vänligen var medveten om att automatiserade översättningar kan innehålla fel eller brister. Det ursprungliga dokumentet på sitt modersmål bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för några missförstånd eller feltolkningar som uppstår från användningen av denna översättning.