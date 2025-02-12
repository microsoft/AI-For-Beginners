# Introduktion till Neurala Nätverk

![Sammanfattning av innehållet i Introduktion till Neurala Nätverk i en doodle](../../../../translated_images/ai-neuralnetworks.1c687ae40bc86e834f497844866a26d3e0886650a67a4bbe29442e2f157d3b18.sw.png)

Som vi diskuterade i introduktionen är en av metoderna för att uppnå intelligens att träna en **datormodell** eller en **konstgjord hjärna**. Sedan mitten av 1900-talet har forskare prövat olika matematiska modeller, tills detta område i de senaste åren visat sig vara oerhört framgångsrikt. Sådana matematiska modeller av hjärnan kallas **neurala nätverk**.

> Ibland kallas neurala nätverk *Artificiella Neurala Nätverk*, ANNs, för att indikera att vi pratar om modeller, inte verkliga nätverk av neuroner.

## Maskininlärning

Neurala Nätverk är en del av en större disciplin som kallas **Maskininlärning**, vars mål är att använda data för att träna datormodeller som kan lösa problem. Maskininlärning utgör en stor del av Artificiell Intelligens, men vi täcker inte klassisk ML i denna läroplan.

> Besök vår separata **[Maskininlärning för Nybörjare](http://github.com/microsoft/ml-for-beginners)** läroplan för att lära dig mer om klassisk Maskininlärning.

Inom Maskininlärning antar vi att vi har en dataset med exempel **X**, och motsvarande utdata **Y**. Exempel är ofta N-dimensionella vektorer som består av **funktioner**, och utdata kallas **etiketter**.

Vi kommer att överväga de två vanligaste problemen inom maskininlärning:

* **Klassificering**, där vi behöver klassificera ett indataobjekt i två eller fler klasser.
* **Regression**, där vi behöver förutsäga ett numeriskt värde för varje indataexempel.

> När vi representerar indata och utdata som tensorer, är indatauppsättningen en matris av storlek M×N, där M är antalet prover och N är antalet funktioner. Utdataetiketter Y är vektorn av storlek M.

I denna läroplan kommer vi endast att fokusera på modeller för neurala nätverk.

## En Modell av en Neuron

Från biologin vet vi att vår hjärna består av nervceller, där varje cell har flera "ingångar" (axon) och en utgång (dendrit). Axon och dendriter kan leda elektriska signaler, och kopplingarna mellan axon och dendriter kan uppvisa olika grader av ledningsförmåga (styrt av neuromediatörer).

![Modell av en Neuron](../../../../translated_images/synapse-wikipedia.ed20a9e4726ea1c6a3ce8fec51c0b9bec6181946dca0fe4e829bc12fa3bacf01.sw.jpg) | ![Modell av en Neuron](../../../../translated_images/artneuron.1a5daa88d20ebe6f5824ddb89fba0bdaaf49f67e8230c1afbec42909df1fc17e.sw.png)
----|----
Verklig Neuron *([Bild](https://en.wikipedia.org/wiki/Synapse#/media/File:SynapseSchematic_lines.svg) från Wikipedia)* | Konstgjord Neuron *(Bild av Författaren)*

Således innehåller den enklaste matematiska modellen av en neuron flera ingångar X<sub>1</sub>, ..., X<sub>N</sub> och en utgång Y, samt en serie vikter W<sub>1</sub>, ..., W<sub>N</sub>. En utgång beräknas som:

<img src="images/netout.png" alt="Y = f\left(\sum_{i=1}^N X_iW_i\right)" width="131" height="53" align="center"/>

där f är någon icke-linjär **aktiveringsfunktion**.

> Tidiga modeller av neuroner beskrevs i den klassiska artikeln [A logical calculus of the ideas immanent in nervous activity](https://www.cs.cmu.edu/~./epxing/Class/10715/reading/McCulloch.and.Pitts.pdf) av Warren McCullock och Walter Pitts år 1943. Donald Hebb föreslog i sin bok "[The Organization of Behavior: A Neuropsychological Theory](https://books.google.com/books?id=VNetYrB8EBoC)" hur dessa nätverk kan tränas.

## I denna Sektion

I denna sektion kommer vi att lära oss om:
* [Perceptron](03-Perceptron/README.md), en av de tidigaste modellerna för neurala nätverk för tvåklassklassificering
* [Flerlagersnätverk](04-OwnFramework/README.md) med en kopplad anteckningsbok [hur man bygger vårt eget ramverk](../../../../lessons/3-NeuralNetworks/04-OwnFramework/OwnFramework.ipynb)
* [Ramverk för Neurala Nätverk](05-Frameworks/README.md), med dessa anteckningsböcker: [PyTorch](../../../../lessons/3-NeuralNetworks/05-Frameworks/IntroPyTorch.ipynb) och [Keras/Tensorflow](../../../../lessons/3-NeuralNetworks/05-Frameworks/IntroKerasTF.ipynb)
* [Överanpassning](../../../../lessons/3-NeuralNetworks/05-Frameworks)

**Ansvarsfriskrivning**:  
Detta dokument har översatts med hjälp av maskinbaserade AI-översättningstjänster. Även om vi strävar efter noggrannhet, vänligen var medveten om att automatiska översättningar kan innehålla fel eller inkonsekvenser. Det ursprungliga dokumentet på sitt modersmål bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för eventuella missförstånd eller feltolkningar som uppstår från användningen av denna översättning.