<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "717775c4050ccbffbe0c961ad8bf7bf7",
  "translation_date": "2025-08-28T15:15:19+00:00",
  "source_file": "lessons/4-ComputerVision/08-TransferLearning/README.md",
  "language_code": "no"
}
-->
# Forhåndstrente nettverk og overføringslæring

Å trene CNN-er kan ta mye tid, og det kreves mye data for denne oppgaven. Imidlertid brukes mye av tiden på å lære de beste lavnivåfiltrene som et nettverk kan bruke for å trekke ut mønstre fra bilder. Et naturlig spørsmål oppstår - kan vi bruke et nevralt nettverk trent på ett datasett og tilpasse det til å klassifisere forskjellige bilder uten å kreve en full treningsprosess?

## [Quiz før forelesning](https://ff-quizzes.netlify.app/en/ai/quiz/15)

Denne tilnærmingen kalles **overføringslæring**, fordi vi overfører noe kunnskap fra én nevralt nettverksmodell til en annen. I overføringslæring starter vi vanligvis med en forhåndstrent modell, som har blitt trent på et stort bildedatasett, som for eksempel **ImageNet**. Disse modellene kan allerede gjøre en god jobb med å trekke ut ulike funksjoner fra generiske bilder, og i mange tilfeller kan det å bygge en klassifiserer på toppen av disse funksjonene gi gode resultater.

> ✅ Overføringslæring er et begrep du finner i andre akademiske felt, som utdanning. Det refererer til prosessen med å ta kunnskap fra ett område og anvende det på et annet.

## Forhåndstrente modeller som funksjonsekstraktorer

De konvolusjonsnettverkene vi har snakket om i forrige seksjon inneholder flere lag, hvor hvert lag skal trekke ut noen funksjoner fra bildet, fra lavnivå pikselkombinasjoner (som horisontale/vertikale linjer eller strøk), til høyere nivå kombinasjoner av funksjoner, som tilsvarer ting som et øye eller en flamme. Hvis vi trener CNN på et tilstrekkelig stort datasett med generiske og mangfoldige bilder, bør nettverket lære å trekke ut disse vanlige funksjonene.

Både Keras og PyTorch inneholder funksjoner for enkelt å laste inn forhåndstrente nevrale nettverksvekter for noen vanlige arkitekturer, de fleste av dem er trent på ImageNet-bilder. De mest brukte er beskrevet på siden [CNN Architectures](../07-ConvNets/CNN_Architectures.md) fra forrige leksjon. Spesielt kan du vurdere å bruke en av følgende:

* **VGG-16/VGG-19**, som er relativt enkle modeller som fortsatt gir god nøyaktighet. Ofte er det et godt valg å bruke VGG som et første forsøk for å se hvordan overføringslæring fungerer.
* **ResNet** er en familie av modeller foreslått av Microsoft Research i 2015. De har flere lag og krever derfor mer ressurser.
* **MobileNet** er en familie av modeller med redusert størrelse, egnet for mobile enheter. Bruk dem hvis du har begrensede ressurser og kan ofre litt nøyaktighet.

Her er eksempler på funksjoner som er trukket ut fra et bilde av en katt av VGG-16-nettverket:

![Funksjoner trukket ut av VGG-16](../../../../../translated_images/features.6291f9c7ba3a0b951af88fc9864632b9115365410765680680d30c927dd67354.no.png)

## Dataset for katter og hunder

I dette eksemplet vil vi bruke et datasett med [Katter og Hunder](https://www.microsoft.com/download/details.aspx?id=54765&WT.mc_id=academic-77998-cacaste), som er veldig nært en reell bildeklassifiseringsscenario.

## ✍️ Øvelse: Overføringslæring

La oss se overføringslæring i praksis i de tilhørende notatbøkene:

* [Overføringslæring - PyTorch](TransferLearningPyTorch.ipynb)
* [Overføringslæring - TensorFlow](TransferLearningTF.ipynb)

## Visualisering av en "ideell katt"

Et forhåndstrent nevralt nettverk inneholder ulike mønstre i sin *hjerne*, inkludert forestillinger om **ideell katt** (samt ideell hund, ideell sebra, osv.). Det ville være interessant å på en eller annen måte **visualisere dette bildet**. Men det er ikke enkelt, fordi mønstrene er spredt over hele nettverkets vekter og også organisert i en hierarkisk struktur.

En tilnærming vi kan ta er å starte med et tilfeldig bilde, og deretter prøve å bruke **gradient descent-optimalisering** for å justere det bildet på en slik måte at nettverket begynner å tro at det er en katt.

![Bildeoptimaliseringssløyfe](../../../../../translated_images/ideal-cat-loop.999fbb8ff306e044f997032f4eef9152b453e6a990e449bbfb107de2493cc37e.no.png)

Men hvis vi gjør dette, vil vi få noe som ligner veldig på tilfeldig støy. Dette er fordi *det er mange måter å få nettverket til å tro at inngangsbilde er en katt*, inkludert noen som ikke gir mening visuelt. Selv om disse bildene inneholder mange mønstre som er typiske for en katt, er det ingenting som begrenser dem til å være visuelt distinkte.

For å forbedre resultatet kan vi legge til et annet ledd i tapfunksjonen, som kalles **varians-tap**. Det er en metrikk som viser hvor like nabopiksler i bildet er. Å minimere varians-tap gjør bildet jevnere og fjerner støy - og avslører dermed mer visuelt tiltalende mønstre. Her er et eksempel på slike "ideelle" bilder, som klassifiseres som katt og som sebra med høy sannsynlighet:

![Ideell katt](../../../../../translated_images/ideal-cat.203dd4597643d6b0bd73038b87f9c0464322725e3a06ab145d25d4a861c70592.no.png) | ![Ideell sebra](../../../../../translated_images/ideal-zebra.7f70e8b54ee15a7a314000bb5df38a6cfe086ea04d60df4d3ef313d046b98a2b.no.png)
-----|-----
 *Ideell katt* | *Ideell sebra*

En lignende tilnærming kan brukes til å utføre såkalte **adversarielle angrep** på et nevralt nettverk. Anta at vi ønsker å lure et nevralt nettverk og få en hund til å se ut som en katt. Hvis vi tar et bilde av en hund, som er gjenkjent av nettverket som en hund, kan vi deretter justere det litt ved hjelp av gradient descent-optimalisering, til nettverket begynner å klassifisere det som en katt:

![Bilde av en hund](../../../../../translated_images/original-dog.8f68a67d2fe0911f33041c0f7fce8aa4ea919f9d3917ec4b468298522aeb6356.no.png) | ![Bilde av en hund klassifisert som en katt](../../../../../translated_images/adversarial-dog.d9fc7773b0142b89752539bfbf884118de845b3851c5162146ea0b8809fc820f.no.png)
-----|-----
*Originalt bilde av en hund* | *Bilde av en hund klassifisert som en katt*

Se koden for å gjenskape resultatene ovenfor i følgende notatbok:

* [Ideell og Adversariell Katt - TensorFlow](AdversarialCat_TF.ipynb)

## Konklusjon

Ved å bruke overføringslæring kan du raskt sette sammen en klassifiserer for en tilpasset objektklassifiseringsoppgave og oppnå høy nøyaktighet. Du kan se at mer komplekse oppgaver som vi løser nå krever høyere datakraft og ikke enkelt kan løses på CPU. I neste enhet vil vi prøve å bruke en mer lettvektsimplementasjon for å trene den samme modellen ved hjelp av lavere datakraft, noe som resulterer i bare litt lavere nøyaktighet.

## 🚀 Utfordring

I de tilhørende notatbøkene er det notater nederst om hvordan overføringskunnskap fungerer best med noe lignende treningsdata (en ny type dyr, kanskje). Gjør noen eksperimenter med helt nye typer bilder for å se hvor godt eller dårlig dine modeller for overføringskunnskap presterer.

## [Quiz etter forelesning](https://ff-quizzes.netlify.app/en/ai/quiz/16)

## Gjennomgang og selvstudium

Les gjennom [TrainingTricks.md](TrainingTricks.md) for å utdype kunnskapen din om andre måter å trene modellene dine på.

## [Oppgave](lab/README.md)

I denne laben vil vi bruke det virkelige [Oxford-IIIT](https://www.robots.ox.ac.uk/~vgg/data/pets/) kjæledyrdatasettet med 35 raser av katter og hunder, og vi vil bygge en klassifiserer basert på overføringslæring.

---

**Ansvarsfraskrivelse**:  
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi streber etter nøyaktighet, vær oppmerksom på at automatiserte oversettelser kan inneholde feil eller unøyaktigheter. Det originale dokumentet på sitt opprinnelige språk bør anses som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.