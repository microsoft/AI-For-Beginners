# Flerklassklassificering med Perceptron

Laborationsuppgift från [AI för nybörjare läroplan](https://github.com/microsoft/ai-for-beginners).

## Uppgift

Använd koden vi har utvecklat i den här lektionen för binär klassificering av handskrivna MNIST-siffror för att skapa en flerklassklassificerare som kan känna igen vilken siffra som helst. Beräkna klassificeringsnoggrannheten på tränings- och testdatasetet, och skriv ut förvirringsmatrisen.

## Tips

1. För varje siffra, skapa ett dataset för binär klassificering av "denna siffra vs. alla andra siffror"
1. Träna 10 olika perceptroner för binär klassificering (en för varje siffra)
1. Definiera en funktion som kommer att klassificera en inmatad siffra

> **Tips**: Om vi kombinerar vikterna från alla 10 perceptroner till en matris, bör vi kunna tillämpa alla 10 perceptroner på inmatade siffror genom en matris-multiplikation. Den mest sannolika siffran kan sedan hittas genom att tillämpa `argmax` operation på utdata.

## Starta anteckningsblock

Börja laborationen genom att öppna [PerceptronMultiClass.ipynb](../../../../../../lessons/3-NeuralNetworks/03-Perceptron/lab/PerceptronMultiClass.ipynb)

**Ansvarsfriskrivning**:  
Detta dokument har översatts med hjälp av maskinbaserade AI-översättningstjänster. Även om vi strävar efter noggrannhet, vänligen var medveten om att automatiska översättningar kan innehålla fel eller brister. Det ursprungliga dokumentet på sitt modersmål bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för några missförstånd eller felaktiga tolkningar som uppstår till följd av användningen av denna översättning.