# Classificatie van Oxford Huisdieren met Transfer Learning

Labopdracht uit [AI for Beginners Curriculum](https://github.com/microsoft/ai-for-beginners).

## Taak

Stel je voor dat je een applicatie moet ontwikkelen voor een dierenopvang om alle huisdieren te catalogiseren. Een geweldige functie van zo'n applicatie zou zijn om automatisch het ras te herkennen aan de hand van een foto. In deze opdracht gebruiken we transfer learning om echte foto's van huisdieren uit de [Oxford-IIIT](https://www.robots.ox.ac.uk/~vgg/data/pets/) dataset te classificeren.

## De Dataset

We gebruiken de originele [Oxford-IIIT](https://www.robots.ox.ac.uk/~vgg/data/pets/) huisdieren-dataset, die 35 verschillende rassen van honden en katten bevat.

Om de dataset te downloaden, gebruik deze codefragment:

```python
!wget https://www.robots.ox.ac.uk/~vgg/data/pets/data/images.tar.gz
!tar xfz images.tar.gz
!rm images.tar.gz
```

## Notebook Starten

Begin het lab door [OxfordPets.ipynb](OxfordPets.ipynb) te openen.

## Belangrijkste Leerpunten

Transfer learning en voorgetrainde netwerken stellen ons in staat om relatief eenvoudig echte beeldclassificatieproblemen op te lossen. Echter, voorgetrainde netwerken werken goed op afbeeldingen van een vergelijkbaar type, en als we heel andere afbeeldingen gaan classificeren (bijv. medische beelden), zullen de resultaten waarschijnlijk veel slechter zijn.

---

**Disclaimer**:  
Dit document is vertaald met behulp van de AI-vertalingsservice [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we streven naar nauwkeurigheid, dient u zich ervan bewust te zijn dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het originele document in zijn oorspronkelijke taal moet worden beschouwd als de gezaghebbende bron. Voor cruciale informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor eventuele misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.