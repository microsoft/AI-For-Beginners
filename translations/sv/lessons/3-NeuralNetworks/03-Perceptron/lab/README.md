<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "7336583e4630220c835335da640016db",
  "translation_date": "2025-08-28T15:39:39+00:00",
  "source_file": "lessons/3-NeuralNetworks/03-Perceptron/lab/README.md",
  "language_code": "sv"
}
-->
# Multi-klassklassificering med Perceptron

Labuppgift från [AI for Beginners Curriculum](https://github.com/microsoft/ai-for-beginners).

## Uppgift

Använd koden vi har utvecklat i denna lektion för binär klassificering av MNIST handskrivna siffror, och skapa en multi-klassklassificerare som kan känna igen vilken siffra som helst. Beräkna klassificeringsnoggrannheten på tränings- och testdatasetet, och skriv ut förvirringsmatrisen.

## Tips

1. För varje siffra, skapa ett dataset för binär klassificering av "denna siffra vs. alla andra siffror"
1. Träna 10 olika perceptroner för binär klassificering (en för varje siffra)
1. Definiera en funktion som kan klassificera en inskriven siffra

> **Tips**: Om vi kombinerar vikterna från alla 10 perceptroner i en matris, bör vi kunna applicera alla 10 perceptroner på inskrivna siffror genom en enda matrismultiplikation. Den mest sannolika siffran kan sedan hittas genom att helt enkelt använda `argmax`-operationen på utdata.

## Startande Notebook

Starta labben genom att öppna [PerceptronMultiClass.ipynb](PerceptronMultiClass.ipynb)

---

**Ansvarsfriskrivning**:  
Detta dokument har översatts med hjälp av AI-översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Även om vi strävar efter noggrannhet, bör det noteras att automatiserade översättningar kan innehålla fel eller felaktigheter. Det ursprungliga dokumentet på dess ursprungliga språk bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för eventuella missförstånd eller feltolkningar som uppstår vid användning av denna översättning.