# Multi-Classificatie met Perceptron

Labopdracht uit [AI for Beginners Curriculum](https://github.com/microsoft/ai-for-beginners).

## Taak

Gebruik de code die we in deze les hebben ontwikkeld voor binaire classificatie van MNIST-handgeschreven cijfers om een multi-class classifier te maken die elk cijfer kan herkennen. Bereken de classificatienauwkeurigheid op de trainings- en testdataset en print de verwarringsmatrix.

## Tips

1. Maak voor elk cijfer een dataset voor een binaire classifier van "dit cijfer versus alle andere cijfers".
1. Train 10 verschillende perceptrons voor binaire classificatie (één voor elk cijfer).
1. Definieer een functie die een invoercijfer kan classificeren.

> **Tip**: Als we de gewichten van alle 10 perceptrons combineren in één matrix, zouden we alle 10 perceptrons op de invoercijfers kunnen toepassen door middel van één matrixvermenigvuldiging. Het meest waarschijnlijke cijfer kan vervolgens worden gevonden door simpelweg de `argmax`-operatie toe te passen op de uitvoer.

## Start Notebook

Begin de labopdracht door [PerceptronMultiClass.ipynb](PerceptronMultiClass.ipynb) te openen.

---

**Disclaimer**:  
Dit document is vertaald met behulp van de AI-vertalingsservice [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we streven naar nauwkeurigheid, dient u zich ervan bewust te zijn dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het originele document in de oorspronkelijke taal moet worden beschouwd als de gezaghebbende bron. Voor kritieke informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.