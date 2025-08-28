<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "717775c4050ccbffbe0c961ad8bf7bf7",
  "translation_date": "2025-08-28T15:14:57+00:00",
  "source_file": "lessons/4-ComputerVision/08-TransferLearning/README.md",
  "language_code": "da"
}
-->
# Forudtrænede netværk og transfer learning

Træning af CNN'er kan tage meget tid, og der kræves en stor mængde data til denne opgave. Meget af tiden bruges dog på at lære de bedste lavniveaufiltre, som et netværk kan bruge til at udtrække mønstre fra billeder. Et naturligt spørgsmål opstår - kan vi bruge et neuralt netværk, der er trænet på én datasæt, og tilpasse det til at klassificere forskellige billeder uden at kræve en fuld træningsproces?

## [Pre-lecture quiz](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/108)

Denne tilgang kaldes **transfer learning**, fordi vi overfører noget viden fra én neuralt netværksmodel til en anden. I transfer learning starter vi typisk med en forudtrænet model, som er blevet trænet på et stort billeddatasæt, såsom **ImageNet**. Disse modeller kan allerede gøre et godt stykke arbejde med at udtrække forskellige funktioner fra generiske billeder, og i mange tilfælde kan det give gode resultater blot at bygge en klassifikator oven på de udtrukne funktioner.

> ✅ Transfer learning er et begreb, du også finder i andre akademiske felter, såsom uddannelse. Det refererer til processen med at tage viden fra ét område og anvende det på et andet.

## Forudtrænede modeller som feature-ekstraktorer

De konvolutionelle netværk, vi har talt om i det foregående afsnit, indeholder en række lag, som hver især skal udtrække nogle funktioner fra billedet, startende med lavniveau pixelkombinationer (såsom horisontale/vertikale linjer eller streger) og op til højere niveau kombinationer af funktioner, der svarer til ting som et øje eller en flamme. Hvis vi træner CNN på et tilstrækkeligt stort datasæt af generiske og diverse billeder, bør netværket lære at udtrække disse fælles funktioner.

Både Keras og PyTorch indeholder funktioner til nemt at indlæse forudtrænede neurale netværksvægte for nogle almindelige arkitekturer, hvoraf de fleste er trænet på ImageNet-billeder. De mest anvendte er beskrevet på siden [CNN Architectures](../07-ConvNets/CNN_Architectures.md) fra den tidligere lektion. Især kan du overveje at bruge en af følgende:

* **VGG-16/VGG-19**, som er relativt simple modeller, der stadig giver god nøjagtighed. Ofte er det en god idé at starte med VGG for at se, hvordan transfer learning fungerer.
* **ResNet** er en familie af modeller foreslået af Microsoft Research i 2015. De har flere lag og kræver derfor flere ressourcer.
* **MobileNet** er en familie af modeller med reduceret størrelse, velegnet til mobile enheder. Brug dem, hvis du har begrænsede ressourcer og kan ofre lidt nøjagtighed.

Her er eksempler på funktioner udtrukket fra et billede af en kat af VGG-16-netværket:

![Features extracted by VGG-16](../../../../../translated_images/features.6291f9c7ba3a0b951af88fc9864632b9115365410765680680d30c927dd67354.da.png)

## Cats vs. Dogs Dataset

I dette eksempel vil vi bruge et datasæt med [Cats and Dogs](https://www.microsoft.com/download/details.aspx?id=54765&WT.mc_id=academic-77998-cacaste), som er meget tæt på et virkelighedsnært billedklassifikationsscenarie.

## ✍️ Øvelse: Transfer Learning

Lad os se transfer learning i aktion i de tilsvarende notebooks:

* [Transfer Learning - PyTorch](TransferLearningPyTorch.ipynb)
* [Transfer Learning - TensorFlow](TransferLearningTF.ipynb)

## Visualisering af Adversarial Cat

Et forudtrænet neuralt netværk indeholder forskellige mønstre i sin *hjerne*, inklusive forestillinger om **den ideelle kat** (såvel som den ideelle hund, den ideelle zebra osv.). Det kunne være interessant på en eller anden måde at **visualisere dette billede**. Det er dog ikke simpelt, fordi mønstrene er spredt over netværkets vægte og også organiseret i en hierarkisk struktur.

En tilgang, vi kan tage, er at starte med et tilfældigt billede og derefter forsøge at bruge **gradient descent optimering** til at justere det billede på en sådan måde, at netværket begynder at tro, at det er en kat.

![Image Optimization Loop](../../../../../translated_images/ideal-cat-loop.999fbb8ff306e044f997032f4eef9152b453e6a990e449bbfb107de2493cc37e.da.png)

Men hvis vi gør dette, vil vi modtage noget, der ligner tilfældig støj. Dette skyldes, at *der er mange måder at få netværket til at tro, at inputbilledet er en kat*, inklusive nogle, der ikke giver mening visuelt. Selvom disse billeder indeholder mange mønstre, der er typiske for en kat, er der intet, der begrænser dem til at være visuelt genkendelige.

For at forbedre resultatet kan vi tilføje et andet led til tab-funktionen, som kaldes **variation loss**. Det er en metric, der viser, hvor ens nabopixels i billedet er. Ved at minimere variation loss bliver billedet glattere og fjerner støj - hvilket afslører mere visuelt tiltalende mønstre. Her er et eksempel på sådanne "ideelle" billeder, der klassificeres som kat og zebra med høj sandsynlighed:

![Ideal Cat](../../../../../translated_images/ideal-cat.203dd4597643d6b0bd73038b87f9c0464322725e3a06ab145d25d4a861c70592.da.png) | ![Ideal Zebra](../../../../../translated_images/ideal-zebra.7f70e8b54ee15a7a314000bb5df38a6cfe086ea04d60df4d3ef313d046b98a2b.da.png)
-----|-----
 *Ideel kat* | *Ideel zebra*

En lignende tilgang kan bruges til at udføre såkaldte **adversarial attacks** på et neuralt netværk. Antag, at vi vil narre et neuralt netværk og få en hund til at ligne en kat. Hvis vi tager et billede af en hund, som netværket genkender som en hund, kan vi derefter justere det lidt ved hjælp af gradient descent optimering, indtil netværket begynder at klassificere det som en kat:

![Picture of a Dog](../../../../../translated_images/original-dog.8f68a67d2fe0911f33041c0f7fce8aa4ea919f9d3917ec4b468298522aeb6356.da.png) | ![Picture of a dog classified as a cat](../../../../../translated_images/adversarial-dog.d9fc7773b0142b89752539bfbf884118de845b3851c5162146ea0b8809fc820f.da.png)
-----|-----
*Originalt billede af en hund* | *Billede af en hund klassificeret som en kat*

Se koden for at genskabe resultaterne ovenfor i følgende notebook:

* [Ideal and Adversarial Cat - TensorFlow](AdversarialCat_TF.ipynb)

## Konklusion

Ved hjælp af transfer learning kan du hurtigt sammensætte en klassifikator til en brugerdefineret objektklassifikationsopgave og opnå høj nøjagtighed. Du kan se, at mere komplekse opgaver, som vi løser nu, kræver højere computerkraft og ikke let kan løses på CPU'en. I den næste enhed vil vi forsøge at bruge en mere letvægtsimplementering til at træne den samme model ved hjælp af lavere computerressourcer, hvilket resulterer i kun lidt lavere nøjagtighed.

## 🚀 Udfordring

I de medfølgende notebooks er der noter nederst om, hvordan transfer learning fungerer bedst med nogenlunde lignende træningsdata (måske en ny type dyr). Lav nogle eksperimenter med helt nye typer billeder for at se, hvor godt eller dårligt dine transfer learning-modeller klarer sig.

## [Post-lecture quiz](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/208)

## Gennemgang & Selvstudie

Læs [TrainingTricks.md](TrainingTricks.md) for at uddybe din viden om andre måder at træne dine modeller på.

## [Opgave](lab/README.md)

I denne lab vil vi bruge det virkelighedsnære [Oxford-IIIT](https://www.robots.ox.ac.uk/~vgg/data/pets/) pets datasæt med 35 racer af katte og hunde, og vi vil bygge en transfer learning klassifikator.

---

**Ansvarsfraskrivelse**:  
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på at opnå nøjagtighed, skal du være opmærksom på, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det originale dokument på dets oprindelige sprog bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi er ikke ansvarlige for eventuelle misforståelser eller fejltolkninger, der måtte opstå som følge af brugen af denne oversættelse.