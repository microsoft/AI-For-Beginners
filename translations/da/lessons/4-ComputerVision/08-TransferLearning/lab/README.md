# Klassificering af Oxford Pets ved hjælp af Transfer Learning

Laboratorieopgave fra [AI for Beginners Curriculum](https://github.com/microsoft/ai-for-beginners).

## Opgave

Forestil dig, at du skal udvikle en applikation til en dyrepension for at katalogisere alle kæledyr. En af de fantastiske funktioner ved en sådan applikation ville være automatisk at identificere racen ud fra et fotografi. I denne opgave vil vi bruge transfer learning til at klassificere billeder af kæledyr fra det virkelige liv ved hjælp af [Oxford-IIIT](https://www.robots.ox.ac.uk/~vgg/data/pets/) kæledyrsdatabasen.

## Databasen

Vi vil bruge den originale [Oxford-IIIT](https://www.robots.ox.ac.uk/~vgg/data/pets/) kæledyrsdatabase, som indeholder 35 forskellige racer af hunde og katte.

For at downloade databasen, brug denne kode:

```python
!wget https://www.robots.ox.ac.uk/~vgg/data/pets/data/images.tar.gz
!tar xfz images.tar.gz
!rm images.tar.gz
```

## Start Notebook

Start laboratoriet ved at åbne [OxfordPets.ipynb](OxfordPets.ipynb)

## Læringspunkt

Transfer learning og forudtrænede netværk gør det relativt nemt at løse virkelige billedklassifikationsproblemer. Dog fungerer forudtrænede netværk bedst på billeder af lignende type, og hvis vi begynder at klassificere meget forskellige billeder (f.eks. medicinske billeder), vil resultaterne sandsynligvis være betydeligt dårligere.

---

**Ansvarsfraskrivelse**:  
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på at opnå nøjagtighed, skal det bemærkes, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det originale dokument på dets oprindelige sprog bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi påtager os ikke ansvar for eventuelle misforståelser eller fejltolkninger, der måtte opstå som følge af brugen af denne oversættelse.