# Klasifikacija Oxford kućnih ljubimaca koristeći prijenosno učenje

Laboratorijska vježba iz [AI for Beginners Curriculum](https://github.com/microsoft/ai-for-beginners).

## Zadatak

Zamislite da trebate razviti aplikaciju za vrtić za kućne ljubimce kako biste katalogizirali sve ljubimce. Jedna od sjajnih značajki takve aplikacije bila bi automatsko prepoznavanje pasmine iz fotografije. U ovom zadatku koristit ćemo prijenosno učenje za klasifikaciju stvarnih slika kućnih ljubimaca iz [Oxford-IIIT](https://www.robots.ox.ac.uk/~vgg/data/pets/) skupa podataka o kućnim ljubimcima.

## Skup podataka

Koristit ćemo originalni skup podataka [Oxford-IIIT](https://www.robots.ox.ac.uk/~vgg/data/pets/), koji sadrži 35 različitih pasmina pasa i mačaka.

Za preuzimanje skupa podataka, koristite ovaj isječak koda:

```python
!wget https://www.robots.ox.ac.uk/~vgg/data/pets/data/images.tar.gz
!tar xfz images.tar.gz
!rm images.tar.gz
```

## Početak rada s bilježnicom

Započnite laboratorij otvaranjem [OxfordPets.ipynb](../../../../../../lessons/4-ComputerVision/08-TransferLearning/lab/OxfordPets.ipynb)

## Zaključak

Prijenosno učenje i unaprijed trenirane mreže omogućuju nam relativno jednostavno rješavanje problema klasifikacije slika iz stvarnog svijeta. Međutim, unaprijed trenirane mreže dobro funkcioniraju na slikama slične vrste, a ako počnemo klasificirati vrlo različite slike (npr. medicinske slike), vjerojatno ćemo dobiti znatno lošije rezultate.

**Odricanje od odgovornosti**:  
Ovaj dokument je preveden pomoću AI usluge za prevođenje [Co-op Translator](https://github.com/Azure/co-op-translator). Iako nastojimo osigurati točnost, imajte na umu da automatski prijevodi mogu sadržavati pogreške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati autoritativnim izvorom. Za ključne informacije preporučuje se profesionalni prijevod od strane čovjeka. Ne preuzimamo odgovornost za nesporazume ili pogrešna tumačenja koja mogu proizaći iz korištenja ovog prijevoda.