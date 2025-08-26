<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f3d2cee9cb3c52160419e560c57a690e",
  "translation_date": "2025-08-25T22:58:48+00:00",
  "source_file": "lessons/4-ComputerVision/07-ConvNets/lab/README.md",
  "language_code": "hr"
}
-->
# Klasifikacija lica kućnih ljubimaca

Laboratorijska vježba iz [AI for Beginners Curriculum](https://github.com/microsoft/ai-for-beginners).

## Zadatak

Zamislite da trebate razviti aplikaciju za vrtić za kućne ljubimce kako biste katalogizirali sve ljubimce. Jedna od sjajnih značajki takve aplikacije bila bi automatsko prepoznavanje pasmine s fotografije. To se može uspješno postići korištenjem neuronskih mreža.

Potrebno je trenirati konvolucijsku neuronsku mrežu za klasifikaciju različitih pasmina mačaka i pasa koristeći **Pet Faces** dataset.

## Dataset

Koristit ćemo **Pet Faces** dataset, izveden iz [Oxford-IIIT](https://www.robots.ox.ac.uk/~vgg/data/pets/) dataset-a za kućne ljubimce. Sadrži 35 različitih pasmina pasa i mačaka.

![Dataset s kojim ćemo raditi](../../../../../../translated_images/data.50b2a9d5484bdbf0f52f5765b381cec9efe2bd296a98f007f90bedb6ac67f2a8.hr.png)

Za preuzimanje dataset-a, koristite ovaj isječak koda:

```python
!wget https://mslearntensorflowlp.blob.core.windows.net/data/petfaces.tar.gz
!tar xfz petfaces.tar.gz
!rm petfaces.tar.gz
```

## Početak rada s bilježnicom

Započnite laboratorij otvaranjem [PetFaces.ipynb](../../../../../../lessons/4-ComputerVision/07-ConvNets/lab/PetFaces.ipynb)

## Zaključak

Riješili ste relativno složen problem klasifikacije slika od nule! Bilo je prilično mnogo klasa, a ipak ste uspjeli postići razumnu točnost! Također ima smisla mjeriti top-k točnost, jer je lako zamijeniti neke klase koje čak ni ljudima nisu jasno različite.

**Odricanje od odgovornosti**:  
Ovaj dokument je preveden pomoću AI usluge za prevođenje [Co-op Translator](https://github.com/Azure/co-op-translator). Iako nastojimo osigurati točnost, imajte na umu da automatski prijevodi mogu sadržavati pogreške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati autoritativnim izvorom. Za kritične informacije preporučuje se profesionalni prijevod od strane čovjeka. Ne preuzimamo odgovornost za nesporazume ili pogrešna tumačenja koja mogu proizaći iz korištenja ovog prijevoda.