<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "d7f8a25ff13cfe9f4cd671cc23351fad",
  "translation_date": "2025-08-28T15:25:37+00:00",
  "source_file": "lessons/4-ComputerVision/12-Segmentation/README.md",
  "language_code": "no"
}
-->
# Segmentering

Vi har tidligere lært om Objektgjenkjenning, som lar oss lokalisere objekter i et bilde ved å forutsi deres *avgrensningsbokser*. For noen oppgaver trenger vi imidlertid ikke bare avgrensningsbokser, men også mer presis objektlokalisering. Denne oppgaven kalles **segmentering**.

## [Pre-forelesningsquiz](https://ff-quizzes.netlify.app/en/ai/quiz/23)

Segmentering kan sees på som **pikselklassifisering**, der vi for **hver** piksel i bildet må forutsi dens klasse (*bakgrunn* er en av klassene). Det finnes to hovedtyper segmenteringsalgoritmer:

* **Semantisk segmentering** forteller kun pikselklassen og skiller ikke mellom ulike objekter innenfor samme klasse.
* **Instanssegmentering** deler klasser inn i forskjellige instanser.

For instanssegmentering er disse sauene forskjellige objekter, men for semantisk segmentering representeres alle sauene av én klasse.

<img src="images/instance_vs_semantic.jpeg" width="50%">

> Bilde fra [denne bloggposten](https://nirmalamurali.medium.com/image-classification-vs-semantic-segmentation-vs-instance-segmentation-625c33a08d50)

Det finnes ulike nevrale arkitekturer for segmentering, men de har alle samme struktur. På en måte ligner det på autoenkoderen du har lært om tidligere, men i stedet for å dekonstruere det originale bildet, er målet vårt å dekonstruere en **maske**. Dermed har et segmenteringsnettverk følgende deler:

* **Encoder** trekker ut funksjoner fra inngangsbilde.
* **Decoder** transformerer disse funksjonene til **maske-bildet**, med samme størrelse og antall kanaler som tilsvarer antall klasser.

<img src="images/segm.png" width="80%">

> Bilde fra [denne publikasjonen](https://arxiv.org/pdf/2001.05566.pdf)

Vi bør spesielt nevne tapfunksjonen som brukes for segmentering. Når vi bruker klassiske autoenkodere, må vi måle likheten mellom to bilder, og vi kan bruke gjennomsnittlig kvadratfeil (MSE) til dette. I segmentering representerer hver piksel i målmaske-bildet klassenumre (one-hot-enkodet langs den tredje dimensjonen), så vi må bruke tapfunksjoner spesifikke for klassifisering - kryssentropitap, gjennomsnittlig over alle piksler. Hvis masken er binær, brukes **binært kryssentropitap** (BCE).

> ✅ One-hot-enkoding er en måte å kode en klasseetikett inn i en vektor med lengde lik antall klasser. Ta en titt på [denne artikkelen](https://datagy.io/sklearn-one-hot-encode/) om denne teknikken.

## Segmentering for Medisinsk Bildediagnostikk

I denne leksjonen skal vi se segmentering i praksis ved å trene et nettverk til å gjenkjenne menneskelige nevi (også kjent som føflekker) på medisinske bilder. Vi vil bruke <a href="https://www.fc.up.pt/addi/ph2%20database.html">PH<sup>2</sup>-databasen</a> med dermoskopibilder som bildekilde. Dette datasettet inneholder 200 bilder av tre klasser: typisk nevus, atypisk nevus og melanom. Alle bildene inneholder også en tilsvarende **maske** som markerer nevusen.

> ✅ Denne teknikken er spesielt egnet for denne typen medisinsk bildediagnostikk, men hvilke andre virkelige applikasjoner kan du se for deg?

<img alt="navi" src="images/navi.png"/>

> Bilde fra PH<sup>2</sup>-databasen

Vi skal trene en modell til å segmentere enhver nevus fra bakgrunnen.

## ✍️ Øvelser: Semantisk Segmentering

Åpne notatbøkene nedenfor for å lære mer om ulike semantiske segmenteringsarkitekturer, øve på å jobbe med dem, og se dem i praksis.

* [Semantisk Segmentering Pytorch](SemanticSegmentationPytorch.ipynb)
* [Semantisk Segmentering TensorFlow](SemanticSegmentationTF.ipynb)

## [Etter-forelesningsquiz](https://ff-quizzes.netlify.app/en/ai/quiz/24)

## Konklusjon

Segmentering er en svært kraftig teknikk for bildegjenkjenning, som går utover avgrensningsbokser til klassifisering på pikselnivå. Det er en teknikk som brukes i medisinsk bildediagnostikk, blant andre applikasjoner.

## 🚀 Utfordring

Kroppssegmentering er bare én av de vanlige oppgavene vi kan utføre med bilder av mennesker. Andre viktige oppgaver inkluderer **skjelettdeteksjon** og **posisjonsdeteksjon**. Prøv ut [OpenPose](https://github.com/CMU-Perceptual-Computing-Lab/openpose)-biblioteket for å se hvordan posisjonsdeteksjon kan brukes.

## Gjennomgang & Selvstudium

Denne [Wikipedia-artikkelen](https://wikipedia.org/wiki/Image_segmentation) gir en god oversikt over de ulike applikasjonene til denne teknikken. Lær mer på egen hånd om underområdene Instanssegmentering og Panoptisk segmentering innen dette feltet.

## [Oppgave](lab/README.md)

I denne labben skal du prøve **kroppssegmentering** ved å bruke [Segmentation Full Body MADS Dataset](https://www.kaggle.com/datasets/tapakah68/segmentation-full-body-mads-dataset) fra Kaggle.

---

**Ansvarsfraskrivelse**:  
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi streber etter nøyaktighet, vær oppmerksom på at automatiserte oversettelser kan inneholde feil eller unøyaktigheter. Det originale dokumentet på sitt opprinnelige språk bør anses som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.