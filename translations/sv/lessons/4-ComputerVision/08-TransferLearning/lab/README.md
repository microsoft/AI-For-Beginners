# Klassificering av Oxford Pets med Transfer Learning

Labuppgift från [AI for Beginners Curriculum](https://github.com/microsoft/ai-for-beginners).

## Uppgift

Föreställ dig att du behöver utveckla en applikation för ett djurdagis för att katalogisera alla husdjur. En fantastisk funktion i en sådan applikation skulle vara att automatiskt identifiera rasen från ett fotografi. I denna uppgift kommer vi att använda transfer learning för att klassificera verkliga bilder av husdjur från [Oxford-IIIT](https://www.robots.ox.ac.uk/~vgg/data/pets/) husdjursdataset.

## Datasetet

Vi kommer att använda det ursprungliga [Oxford-IIIT](https://www.robots.ox.ac.uk/~vgg/data/pets/) husdjursdatasetet, som innehåller 35 olika raser av hundar och katter.

För att ladda ner datasetet, använd denna kodsnutt:

```python
!wget https://www.robots.ox.ac.uk/~vgg/data/pets/data/images.tar.gz
!tar xfz images.tar.gz
!rm images.tar.gz
```

## Starta Notebook

Börja labben genom att öppna [OxfordPets.ipynb](OxfordPets.ipynb)

## Slutsats

Transfer learning och förtränade nätverk gör det möjligt för oss att lösa verkliga bildklassificeringsproblem relativt enkelt. Dock fungerar förtränade nätverk bäst på bilder av liknande typ, och om vi börjar klassificera mycket olika bilder (t.ex. medicinska bilder) är det troligt att resultaten blir betydligt sämre.

---

**Ansvarsfriskrivning**:  
Detta dokument har översatts med hjälp av AI-översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Även om vi strävar efter noggrannhet, bör du vara medveten om att automatiserade översättningar kan innehålla fel eller felaktigheter. Det ursprungliga dokumentet på dess ursprungliga språk bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för eventuella missförstånd eller feltolkningar som uppstår vid användning av denna översättning.