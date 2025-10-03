<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "b70fcf7fcee862990f848c679090943f",
  "translation_date": "2025-10-03T14:55:29+00:00",
  "source_file": "lessons/4-ComputerVision/07-ConvNets/lab/README.md",
  "language_code": "da"
}
-->
# Klassifikation af kæledyrs ansigter

Laboratorieopgave fra [AI for Beginners Curriculum](https://github.com/microsoft/ai-for-beginners).

## Opgave

Forestil dig, at du skal udvikle en applikation til en dyrepension for at katalogisere alle kæledyr. En af de fantastiske funktioner ved en sådan applikation ville være automatisk at identificere racen ud fra et fotografi. Dette kan med succes gøres ved hjælp af neurale netværk.

Du skal træne et konvolutionelt neuralt netværk til at klassificere forskellige racer af katte og hunde ved hjælp af **Pet Faces**-datasættet.

## Datasættet

Vi vil bruge [Oxford-IIIT Pet Dataset](https://www.robots.ox.ac.uk/~vgg/data/pets/), som indeholder billeder af 37 forskellige racer af hunde og katte.

![Datasæt vi skal arbejde med](../../../../../../translated_images/data.50b2a9d5484bdbf0f52f5765b381cec9efe2bd296a98f007f90bedb6ac67f2a8.da.png)

For at downloade datasættet, brug denne kode:

```python
!wget https://thor.robots.ox.ac.uk/~vgg/data/pets/images.tar.gz
!tar xfz images.tar.gz
!rm images.tar.gz
```

**Bemærk:** Billederne i Oxford-IIIT Pet Dataset er organiseret efter filnavn (f.eks. `Abyssinian_1.jpg`, `Bengal_2.jpg`). Notebogen inkluderer kode til at organisere disse billeder i race-specifikke underkataloger for lettere klassifikation.

## Startnotebook

Start laboratoriet ved at åbne [PetFaces.ipynb](PetFaces.ipynb)

## Konklusion

Du har løst et relativt komplekst problem med billedklassifikation fra bunden! Der var en hel del klasser, og du var stadig i stand til at opnå rimelig nøjagtighed! Det giver også mening at måle top-k nøjagtighed, fordi det er nemt at forveksle nogle af klasserne, som ikke er klart forskellige, selv for mennesker.

---

**Ansvarsfraskrivelse**:  
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på at sikre nøjagtighed, skal det bemærkes, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det originale dokument på dets oprindelige sprog bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi påtager os ikke ansvar for misforståelser eller fejltolkninger, der måtte opstå som følge af brugen af denne oversættelse.