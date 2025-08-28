<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "1c6b8c7c1778a35fc1139b7f2aecb7b3",
  "translation_date": "2025-08-28T15:35:48+00:00",
  "source_file": "lessons/3-NeuralNetworks/README.md",
  "language_code": "sv"
}
-->
# Introduktion till Neurala Nätverk

![Sammanfattning av innehållet i Introduktion till Neurala Nätverk i en skiss](../../../../translated_images/ai-neuralnetworks.1c687ae40bc86e834f497844866a26d3e0886650a67a4bbe29442e2f157d3b18.sv.png)

Som vi diskuterade i introduktionen är ett av sätten att uppnå intelligens att träna en **datormodell** eller en **artificiell hjärna**. Sedan mitten av 1900-talet har forskare testat olika matematiska modeller, och på senare år har denna riktning visat sig vara mycket framgångsrik. Sådana matematiska modeller av hjärnan kallas **neurala nätverk**.

> Ibland kallas neurala nätverk för *Artificiella Neurala Nätverk*, ANNs, för att tydliggöra att vi pratar om modeller och inte om verkliga nätverk av neuroner.

## Maskininlärning

Neurala nätverk är en del av en större disciplin som kallas **Maskininlärning**, vars mål är att använda data för att träna datormodeller som kan lösa problem. Maskininlärning utgör en stor del av Artificiell Intelligens, men vi täcker inte klassisk ML i detta läroplan.

> Besök vår separata **[Maskininlärning för nybörjare](http://github.com/microsoft/ml-for-beginners)** läroplan för att lära dig mer om klassisk maskininlärning.

Inom maskininlärning antar vi att vi har en dataset med exempel **X**, och motsvarande utvärden **Y**. Exempel är ofta N-dimensionella vektorer som består av **egenskaper**, och utvärden kallas **etiketter**.

Vi kommer att titta på de två vanligaste problemen inom maskininlärning:

* **Klassificering**, där vi behöver klassificera ett indataobjekt i två eller fler klasser.
* **Regression**, där vi behöver förutsäga ett numeriskt värde för varje indataexempel.

> När vi representerar indata och utdata som tensorer är datasetet för indata en matris av storlek M×N, där M är antalet exempel och N är antalet egenskaper. Utdataetiketter Y är en vektor av storlek M.

I denna läroplan kommer vi endast att fokusera på modeller för neurala nätverk.

## En modell av en neuron

Från biologin vet vi att vår hjärna består av nervceller, var och en med flera "indata" (axoner) och en utdata (dendrit). Axoner och dendriter kan leda elektriska signaler, och kopplingarna mellan axoner och dendriter kan ha olika grad av ledningsförmåga (styrt av neurotransmittorer).

![Modell av en Neuron](../../../../translated_images/synapse-wikipedia.ed20a9e4726ea1c6a3ce8fec51c0b9bec6181946dca0fe4e829bc12fa3bacf01.sv.jpg) | ![Modell av en Neuron](../../../../translated_images/artneuron.1a5daa88d20ebe6f5824ddb89fba0bdaaf49f67e8230c1afbec42909df1fc17e.sv.png)
----|----
Verklig Neuron *([Bild](https://en.wikipedia.org/wiki/Synapse#/media/File:SynapseSchematic_lines.svg) från Wikipedia)* | Artificiell Neuron *(Bild av författaren)*

Således innehåller den enklaste matematiska modellen av en neuron flera indata X<sub>1</sub>, ..., X<sub>N</sub> och en utdata Y, samt en serie vikter W<sub>1</sub>, ..., W<sub>N</sub>. Utdatan beräknas som:

<img src="images/netout.png" alt="Y = f\left(\sum_{i=1}^N X_iW_i\right)" width="131" height="53" align="center"/>

där f är någon icke-linjär **aktiveringsfunktion**.

> Tidiga modeller av neuroner beskrevs i den klassiska artikeln [A logical calculus of the ideas immanent in nervous activity](https://www.cs.cmu.edu/~./epxing/Class/10715/reading/McCulloch.and.Pitts.pdf) av Warren McCullock och Walter Pitts år 1943. Donald Hebb föreslog i sin bok "[The Organization of Behavior: A Neuropsychological Theory](https://books.google.com/books?id=VNetYrB8EBoC)" hur dessa nätverk kan tränas.

## I denna sektion

I denna sektion kommer vi att lära oss om:
* [Perceptron](03-Perceptron/README.md), en av de tidigaste modellerna för neurala nätverk för tvåklassklassificering
* [Flerlagers nätverk](04-OwnFramework/README.md) med en tillhörande notebook [hur man bygger vårt eget ramverk](04-OwnFramework/OwnFramework.ipynb)
* [Ramverk för neurala nätverk](05-Frameworks/README.md), med dessa notebooks: [PyTorch](05-Frameworks/IntroPyTorch.ipynb) och [Keras/Tensorflow](05-Frameworks/IntroKerasTF.ipynb)
* [Överanpassning](../../../../lessons/3-NeuralNetworks/05-Frameworks)

---

**Ansvarsfriskrivning**:  
Detta dokument har översatts med hjälp av AI-översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Även om vi strävar efter noggrannhet, bör det noteras att automatiserade översättningar kan innehålla fel eller brister. Det ursprungliga dokumentet på dess originalspråk bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för eventuella missförstånd eller feltolkningar som kan uppstå vid användning av denna översättning.