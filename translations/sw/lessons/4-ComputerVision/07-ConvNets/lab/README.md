# Klassificering av Husdjurs Ansikten

Laborationsuppgift från [AI för Nybörjare Läroplan](https://github.com/microsoft/ai-for-beginners).

## Uppgift

Tänk dig att du behöver utveckla en applikation för en djurförskola för att katalogisera alla husdjur. En av de fantastiska funktionerna i en sådan applikation skulle vara att automatiskt upptäcka rasen från ett fotografi. Detta kan framgångsrikt göras med hjälp av neurala nätverk.

Du behöver träna ett konvolutionellt neuralt nätverk för att klassificera olika raser av katter och hundar med hjälp av **Pet Faces** datasetet.

## Datasetet

Vi kommer att använda **Pet Faces** datasetet, som härstammar från [Oxford-IIIT](https://www.robots.ox.ac.uk/~vgg/data/pets/) husdjursdatasetet. Det innehåller 35 olika raser av hundar och katter.

![Datasetet vi kommer att hantera](../../../../../../translated_images/data.50b2a9d5484bdbf0f52f5765b381cec9efe2bd296a98f007f90bedb6ac67f2a8.sw.png)

För att ladda ner datasetet, använd denna kodsnutt:

```python
!wget https://mslearntensorflowlp.blob.core.windows.net/data/petfaces.tar.gz
!tar xfz petfaces.tar.gz
!rm petfaces.tar.gz
```

## Starta Anteckningsbok

Börja laborationen med att öppna [PetFaces.ipynb](../../../../../../lessons/4-ComputerVision/07-ConvNets/lab/PetFaces.ipynb)

## Sammanfattning

Du har löst ett relativt komplext problem med bildklassificering från grunden! Det fanns ganska många klasser, och du lyckades fortfarande få en rimlig noggrannhet! Det är också meningsfullt att mäta top-k noggrannhet, eftersom det är lätt att förväxla vissa av klasserna som inte är tydligt olika ens för människor.

**Ansvarsfriskrivning**:  
Detta dokument har översatts med hjälp av maskinbaserade AI-översättningstjänster. Även om vi strävar efter noggrannhet, vänligen var medveten om att automatiska översättningar kan innehålla fel eller brister. Det ursprungliga dokumentet på sitt modersmål bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för några missförstånd eller feltolkningar som uppstår från användningen av denna översättning.