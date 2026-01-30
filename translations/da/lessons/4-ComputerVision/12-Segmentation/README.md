# Segmentering

Vi har tidligere lært om Objektgenkendelse, som giver os mulighed for at lokalisere objekter i et billede ved at forudsige deres *bounding boxes*. Men til nogle opgaver har vi ikke kun brug for bounding boxes, men også mere præcis objektlokalisering. Denne opgave kaldes **segmentering**.

## [Pre-lecture quiz](https://ff-quizzes.netlify.app/en/ai/quiz/23)

Segmentering kan betragtes som **pixelklassificering**, hvor vi for **hver** pixel i billedet skal forudsige dens klasse (*baggrund* er en af klasserne). Der findes to hovedtyper af segmenteringsalgoritmer:

* **Semantisk segmentering** angiver kun pixelklassen og skelner ikke mellem forskellige objekter af samme klasse.
* **Instance segmentering** opdeler klasser i forskellige instanser.

Ved instance segmentering er disse får forskellige objekter, men ved semantisk segmentering repræsenteres alle får af én klasse.

<img src="../../../../../translated_images/da/instance_vs_semantic.eee9812bebf8cd45.webp" width="50%">

> Billede fra [denne blogpost](https://nirmalamurali.medium.com/image-classification-vs-semantic-segmentation-vs-instance-segmentation-625c33a08d50)

Der findes forskellige neurale arkitekturer til segmentering, men de har alle samme struktur. På en måde minder det om den autoencoder, du tidligere har lært om, men i stedet for at dekonstruere det originale billede, er målet at dekonstruere en **maske**. Derfor har et segmenteringsnetværk følgende dele:

* **Encoder** udtrækker features fra inputbilledet.
* **Decoder** transformerer disse features til **maske-billedet**, med samme størrelse og antal kanaler svarende til antallet af klasser.

<img src="../../../../../translated_images/da/segm.92442f2cb42ff4fa.webp" width="80%">

> Billede fra [denne publikation](https://arxiv.org/pdf/2001.05566.pdf)

Vi bør især nævne den tab-funktion, der bruges til segmentering. Når vi bruger klassiske autoencoders, skal vi måle ligheden mellem to billeder, og vi kan bruge mean square error (MSE) til dette. Ved segmentering repræsenterer hver pixel i målmaske-billedet klassens nummer (one-hot-encoded langs den tredje dimension), så vi skal bruge tab-funktioner specifikt til klassificering - cross-entropy loss, gennemsnitligt over alle pixels. Hvis masken er binær, bruges **binary cross-entropy loss** (BCE).

> ✅ One-hot encoding er en metode til at kode en klasse-label som en vektor med en længde svarende til antallet af klasser. Tag et kig på [denne artikel](https://datagy.io/sklearn-one-hot-encode/) om denne teknik.

## Segmentering inden for Medicinsk Billedbehandling

I denne lektion vil vi se segmentering i praksis ved at træne et netværk til at genkende menneskelige nevi (også kendt som modermærker) på medicinske billeder. Vi vil bruge <a href="https://www.fc.up.pt/addi/ph2%20database.html">PH<sup>2</sup> Database</a> af dermoskopi-billeder som billedkilde. Dette datasæt indeholder 200 billeder af tre klasser: typisk nevus, atypisk nevus og melanom. Alle billeder indeholder også en tilsvarende **maske**, der afgrænser nevus.

> ✅ Denne teknik er særligt velegnet til denne type medicinsk billedbehandling, men hvilke andre anvendelser i den virkelige verden kan du forestille dig?

<img alt="navi" src="../../../../../translated_images/da/navi.2f20b727910110ea.webp"/>

> Billede fra PH<sup>2</sup> Database

Vi vil træne en model til at segmentere enhver nevus fra dens baggrund.

## ✍️ Øvelser: Semantisk Segmentering

Åbn nedenstående notebooks for at lære mere om forskellige semantiske segmenteringsarkitekturer, øve dig i at arbejde med dem og se dem i aktion.

* [Semantic Segmentation Pytorch](SemanticSegmentationPytorch.ipynb)
* [Semantic Segmentation TensorFlow](SemanticSegmentationTF.ipynb)

## [Post-lecture quiz](https://ff-quizzes.netlify.app/en/ai/quiz/24)

## Konklusion

Segmentering er en meget kraftfuld teknik til billedklassificering, der går ud over bounding boxes til pixel-niveau klassificering. Det er en teknik, der bruges inden for medicinsk billedbehandling, blandt andre anvendelser.

## 🚀 Udfordring

Kropssegmentering er blot en af de almindelige opgaver, vi kan udføre med billeder af mennesker. Andre vigtige opgaver inkluderer **skeletdetektion** og **posedetektion**. Prøv [OpenPose](https://github.com/CMU-Perceptual-Computing-Lab/openpose)-biblioteket for at se, hvordan posedetektion kan bruges.

## Gennemgang & Selvstudie

Denne [Wikipedia-artikel](https://wikipedia.org/wiki/Image_segmentation) giver et godt overblik over de forskellige anvendelser af denne teknik. Lær mere på egen hånd om underområderne Instance segmentering og Panoptisk segmentering inden for dette felt.

## [Opgave](lab/README.md)

I denne lab skal du prøve **kropssegmentering** ved hjælp af [Segmentation Full Body MADS Dataset](https://www.kaggle.com/datasets/tapakah68/segmentation-full-body-mads-dataset) fra Kaggle.

---

