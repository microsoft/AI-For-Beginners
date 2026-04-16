# Konvolutionella neurala nätverk

Vi har tidigare sett att neurala nätverk är ganska bra på att hantera bilder, och till och med en enkel lager-perceptron kan känna igen handskrivna siffror från MNIST-datasetet med rimlig noggrannhet. Men MNIST-datasetet är väldigt speciellt, eftersom alla siffror är centrerade i bilden, vilket gör uppgiften enklare.

## [Quiz före föreläsningen](https://ff-quizzes.netlify.app/en/ai/quiz/13)

I verkligheten vill vi kunna känna igen objekt på en bild oavsett deras exakta position i bilden. Datorseende skiljer sig från generell klassificering, eftersom vi, när vi försöker hitta ett visst objekt på en bild, skannar bilden och letar efter specifika **mönster** och deras kombinationer. Till exempel, när vi letar efter en katt, kan vi först leta efter horisontella linjer som kan bilda morrhår, och sedan kan en viss kombination av morrhår indikera att det faktiskt är en bild av en katt. Den relativa positionen och förekomsten av vissa mönster är viktig, inte deras exakta position i bilden.

För att extrahera mönster kommer vi att använda begreppet **konvolutionella filter**. Som du vet representeras en bild av en 2D-matris eller en 3D-tensor med färgdjup. Att applicera ett filter innebär att vi tar en relativt liten **filterkärna**-matris, och för varje pixel i den ursprungliga bilden beräknar vi det viktade medelvärdet med angränsande punkter. Vi kan se detta som ett litet fönster som glider över hela bilden och jämnar ut alla pixlar enligt vikterna i filterkärnan.

![Vertikalt kantfilter](../../../../../translated_images/sv/filter-vert.b7148390ca0bc356.webp) | ![Horisontellt kantfilter](../../../../../translated_images/sv/filter-horiz.59b80ed4feb946ef.webp)
----|----

> Bild av Dmitry Soshnikov

Till exempel, om vi applicerar 3x3 vertikala och horisontella kantfilter på MNIST-siffrorna, kan vi få framhöjningar (t.ex. höga värden) där det finns vertikala och horisontella kanter i vår ursprungliga bild. Således kan dessa två filter användas för att "leta efter" kanter. På samma sätt kan vi designa olika filter för att leta efter andra låg-nivå mönster:

<img src="../../../../../translated_images/sv/lmfilters.ea9e4868a82cf74c.webp" width="500" align="center"/>

> Bild av [Leung-Malik Filter Bank](https://www.robots.ox.ac.uk/~vgg/research/texclass/filters.html)

Men även om vi kan designa filter för att manuellt extrahera vissa mönster, kan vi också designa nätverket på ett sätt som gör att det lär sig mönstren automatiskt. Detta är en av huvudidéerna bakom CNN.

## Huvudidéer bakom CNN

Så här fungerar CNN baserat på följande viktiga idéer:

* Konvolutionella filter kan extrahera mönster
* Vi kan designa nätverket så att filtren tränas automatiskt
* Vi kan använda samma metod för att hitta mönster i hög-nivå egenskaper, inte bara i den ursprungliga bilden. Således arbetar CNN med en hierarki av egenskaper, från låg-nivå pixelkombinationer till högre nivå kombinationer av bilddelar.

![Hierarkisk egenskapsutvinning](../../../../../translated_images/sv/FeatureExtractionCNN.d9b456cbdae7cb64.webp)

> Bild från [en artikel av Hislop-Lynch](https://www.semanticscholar.org/paper/Computer-vision-based-pedestrian-trajectory-Hislop-Lynch/26e6f74853fc9bbb7487b06dc2cf095d36c9021d), baserad på [deras forskning](https://dl.acm.org/doi/abs/10.1145/1553374.1553453)

## ✍️ Övningar: Konvolutionella neurala nätverk

Låt oss fortsätta utforska hur konvolutionella neurala nätverk fungerar och hur vi kan uppnå träningsbara filter genom att arbeta igenom motsvarande anteckningsböcker:

* [Konvolutionella neurala nätverk - PyTorch](ConvNetsPyTorch.ipynb)
* [Konvolutionella neurala nätverk - TensorFlow](ConvNetsTF.ipynb)

## Pyramidarkitektur

De flesta CNN som används för bildbehandling följer en så kallad pyramidarkitektur. Det första konvolutionella lagret som appliceras på de ursprungliga bilderna har vanligtvis ett relativt lågt antal filter (8-16), som motsvarar olika pixelkombinationer, såsom horisontella/vertikala linjer eller streck. På nästa nivå minskar vi nätverkets spatiala dimension och ökar antalet filter, vilket motsvarar fler möjliga kombinationer av enkla egenskaper. Med varje lager, när vi rör oss mot den slutliga klassificeraren, minskar bildens spatiala dimensioner och antalet filter ökar.

Som exempel, låt oss titta på arkitekturen för VGG-16, ett nätverk som uppnådde 92,7% noggrannhet i ImageNet's topp-5 klassificering år 2014:

![ImageNet-lager](../../../../../translated_images/sv/vgg-16-arch1.d901a5583b3a51ba.webp)

![ImageNet-pyramid](../../../../../translated_images/sv/vgg-16-arch.64ff2137f50dd49f.webp)

> Bild från [Researchgate](https://www.researchgate.net/figure/Vgg16-model-structure-To-get-the-VGG-NIN-model-we-replace-the-2-nd-4-th-6-th-7-th_fig2_335194493)

## Mest kända CNN-arkitekturer

[Fortsätt din studie om de mest kända CNN-arkitekturerna](CNN_Architectures.md)

---

