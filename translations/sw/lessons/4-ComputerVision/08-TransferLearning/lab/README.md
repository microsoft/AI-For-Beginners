# Klassificering av Oxford-djur med Transfer Learning

Laborationsuppgift från [AI for Beginners Curriculum](https://github.com/microsoft/ai-for-beginners).

## Uppgift

Föreställ dig att du behöver utveckla en applikation för djurdagis för att katalogisera alla husdjur. En av de fantastiska funktionerna i en sådan applikation skulle vara att automatiskt upptäcka rasen från ett fotografi. I denna uppgift kommer vi att använda transfer learning för att klassificera verkliga djurbilder från datasetet [Oxford-IIIT](https://www.robots.ox.ac.uk/~vgg/data/pets/).

## Datasetet

Vi kommer att använda det ursprungliga datasetet [Oxford-IIIT](https://www.robots.ox.ac.uk/~vgg/data/pets/), som innehåller 35 olika raser av hundar och katter.

För att ladda ner datasetet, använd denna kodsnutt:

```python
!wget https://www.robots.ox.ac.uk/~vgg/data/pets/data/images.tar.gz
!tar xfz images.tar.gz
!rm images.tar.gz
```

## Starta Notebook

Börja laborationen med att öppna [OxfordPets.ipynb](../../../../../../lessons/4-ComputerVision/08-TransferLearning/lab/OxfordPets.ipynb)

## Sammanfattning

Transfer learning och förtränade nätverk gör det möjligt för oss att lösa verkliga problem med bildklassificering relativt enkelt. Dock fungerar förtränade nätverk bra på bilder av liknande slag, och om vi börjar klassificera mycket olika bilder (t.ex. medicinska bilder) är det troligt att vi får mycket sämre resultat.

**Ansvarsfriskrivning**:  
Detta dokument har översatts med hjälp av maskinbaserade AI-översättningstjänster. Även om vi strävar efter noggrannhet, bör du vara medveten om att automatiserade översättningar kan innehålla fel eller brister. Det ursprungliga dokumentet på sitt modersmål bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för några missförstånd eller feltolkningar som uppstår till följd av användningen av denna översättning.