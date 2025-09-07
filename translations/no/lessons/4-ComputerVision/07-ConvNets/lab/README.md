<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f3d2cee9cb3c52160419e560c57a690e",
  "translation_date": "2025-08-28T15:14:27+00:00",
  "source_file": "lessons/4-ComputerVision/07-ConvNets/lab/README.md",
  "language_code": "no"
}
-->
# Klassifisering av kjæledyrs ansikter

Laboppgave fra [AI for Beginners Curriculum](https://github.com/microsoft/ai-for-beginners).

## Oppgave

Tenk deg at du må utvikle en applikasjon for en dyrebarnehage for å katalogisere alle kjæledyr. En av de flotte funksjonene i en slik applikasjon ville være å automatisk identifisere rasen fra et fotografi. Dette kan gjøres med suksess ved hjelp av nevrale nettverk.

Du må trene et konvolusjonelt nevralt nettverk for å klassifisere forskjellige raser av katter og hunder ved hjelp av **Pet Faces**-datasettet.

## Datasettet

Vi skal bruke **Pet Faces**-datasettet, som er avledet fra [Oxford-IIIT](https://www.robots.ox.ac.uk/~vgg/data/pets/) kjæledyrsdatasettet. Det inneholder 35 forskjellige raser av hunder og katter.

![Datasettet vi skal jobbe med](../../../../../../translated_images/data.50b2a9d5484bdbf0f52f5765b381cec9efe2bd296a98f007f90bedb6ac67f2a8.no.png)

For å laste ned datasettet, bruk denne kodebiten:

```python
!wget https://mslearntensorflowlp.blob.core.windows.net/data/petfaces.tar.gz
!tar xfz petfaces.tar.gz
!rm petfaces.tar.gz
```

## Startnotatbok

Start laben ved å åpne [PetFaces.ipynb](PetFaces.ipynb)

## Oppsummering

Du har løst et relativt komplekst problem med bildeklassifisering fra bunnen av! Det var ganske mange klasser, og du klarte likevel å oppnå rimelig nøyaktighet! Det gir også mening å måle top-k nøyaktighet, fordi det er lett å forveksle noen av klassene som ikke er tydelig forskjellige, selv for mennesker.

---

**Ansvarsfraskrivelse**:  
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi streber etter nøyaktighet, vær oppmerksom på at automatiserte oversettelser kan inneholde feil eller unøyaktigheter. Det originale dokumentet på sitt opprinnelige språk bør anses som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.