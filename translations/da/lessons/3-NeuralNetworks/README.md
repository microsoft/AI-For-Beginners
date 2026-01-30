# Introduktion til Neurale Netværk

![Oversigt over indholdet i Intro Neural Networks i en doodle](../../../../translated_images/da/ai-neuralnetworks.1c687ae40bc86e83.webp)

Som vi diskuterede i introduktionen, er en af måderne at opnå intelligens på at træne en **computermodel** eller en **kunstig hjerne**. Siden midten af det 20. århundrede har forskere prøvet forskellige matematiske modeller, indtil denne tilgang i de seneste år har vist sig at være enormt succesfuld. Sådanne matematiske modeller af hjernen kaldes **neurale netværk**.

> Nogle gange kaldes neurale netværk for *Artificial Neural Networks*, ANNs, for at indikere, at vi taler om modeller og ikke om rigtige netværk af neuroner.

## Maskinlæring

Neurale netværk er en del af en større disciplin kaldet **Maskinlæring**, hvis mål er at bruge data til at træne computermodeller, der kan løse problemer. Maskinlæring udgør en stor del af Kunstig Intelligens, men vi dækker ikke klassisk ML i dette pensum.

> Besøg vores separate **[Maskinlæring for begyndere](http://github.com/microsoft/ml-for-beginners)** pensum for at lære mere om klassisk maskinlæring.

I maskinlæring antager vi, at vi har et datasæt med eksempler **X** og tilsvarende outputværdier **Y**. Eksempler er ofte N-dimensionelle vektorer, der består af **features**, og outputs kaldes **labels**.

Vi vil se på de to mest almindelige maskinlæringsproblemer:

* **Klassifikation**, hvor vi skal klassificere et inputobjekt i to eller flere klasser.
* **Regression**, hvor vi skal forudsige en numerisk værdi for hver af inputprøverne.

> Når inputs og outputs repræsenteres som tensorer, er inputdatasættet en matrix af størrelse M&times;N, hvor M er antallet af prøver, og N er antallet af features. Outputlabels Y er en vektor af størrelse M.

I dette pensum vil vi kun fokusere på neurale netværksmodeller.

## En model af en neuron

Fra biologien ved vi, at vores hjerne består af nerveceller (neuroner), som hver har flere "inputs" (dendritter) og en enkelt "output" (axon). Både dendritter og axoner kan lede elektriske signaler, og forbindelserne mellem dem — kendt som synapser — kan udvise varierende grader af ledningsevne, som reguleres af neurotransmittere.

![Model af en neuron](../../../../translated_images/da/synapse-wikipedia.ed20a9e4726ea1c6.webp) | ![Model af en neuron](../../../../translated_images/da/artneuron.1a5daa88d20ebe6f.webp)
----|----
Ægte neuron *([Billede](https://en.wikipedia.org/wiki/Synapse#/media/File:SynapseSchematic_lines.svg) fra Wikipedia)* | Kunstig neuron *(Billede af forfatteren)*

Den simpleste matematiske model af en neuron indeholder således flere inputs X<sub>1</sub>, ..., X<sub>N</sub> og et output Y samt en række vægte W<sub>1</sub>, ..., W<sub>N</sub>. Et output beregnes som:

<img src="../../../../translated_images/da/netout.1eb15eb76fd76731.webp" alt="Y = f\left(\sum_{i=1}^N X_iW_i\right)" width="131" height="53" align="center"/>

hvor f er en ikke-lineær **aktiveringsfunktion**.

> Tidlige modeller af neuroner blev beskrevet i den klassiske artikel [A logical calculus of the ideas immanent in nervous activity](https://www.cs.cmu.edu/~./epxing/Class/10715/reading/McCulloch.and.Pitts.pdf) af Warren McCullock og Walter Pitts i 1943. Donald Hebb foreslog i sin bog "[The Organization of Behavior: A Neuropsychological Theory](https://books.google.com/books?id=VNetYrB8EBoC)" en måde, hvorpå disse netværk kan trænes.

## I denne sektion

I denne sektion vil vi lære om:
* [Perceptron](03-Perceptron/README.md), en af de tidligste neurale netværksmodeller til to-klasse klassifikation
* [Flerlagede netværk](04-OwnFramework/README.md) med en tilhørende notebook [hvordan man bygger vores eget framework](04-OwnFramework/OwnFramework.ipynb)
* [Neurale netværksframeworks](05-Frameworks/README.md), med disse notebooks: [PyTorch](05-Frameworks/IntroPyTorch.ipynb) og [Keras/Tensorflow](05-Frameworks/IntroKerasTF.ipynb)
* [Overfitting](../../../../lessons/3-NeuralNetworks/05-Frameworks)

---

**Ansvarsfraskrivelse**:  
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på at sikre nøjagtighed, skal det bemærkes, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det originale dokument på dets oprindelige sprog bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi påtager os ikke ansvar for misforståelser eller fejltolkninger, der måtte opstå som følge af brugen af denne oversættelse.