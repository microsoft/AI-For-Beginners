# Clasificarea animalelor de companie Oxford folosind Transfer Learning

Temă de laborator din [Curriculumul AI pentru Începători](https://github.com/microsoft/ai-for-beginners).

## Sarcina

Imaginează-ți că trebuie să dezvolți o aplicație pentru o grădiniță de animale de companie pentru a cataloga toate animalele. Una dintre funcțiile grozave ale unei astfel de aplicații ar fi identificarea automată a rasei dintr-o fotografie. În această temă, vom folosi transfer learning pentru a clasifica imagini reale de animale de companie din setul de date [Oxford-IIIT](https://www.robots.ox.ac.uk/~vgg/data/pets/).

## Setul de date

Vom folosi setul de date original [Oxford-IIIT](https://www.robots.ox.ac.uk/~vgg/data/pets/), care conține 35 de rase diferite de câini și pisici.

Pentru a descărca setul de date, folosește acest fragment de cod:

```python
!wget https://www.robots.ox.ac.uk/~vgg/data/pets/data/images.tar.gz
!tar xfz images.tar.gz
!rm images.tar.gz
```

## Începerea notebook-ului

Începe laboratorul deschizând [OxfordPets.ipynb](../../../../../../lessons/4-ComputerVision/08-TransferLearning/lab/OxfordPets.ipynb)

## Concluzie

Transfer learning și rețelele pre-antrenate ne permit să rezolvăm relativ ușor probleme reale de clasificare a imaginilor. Totuși, rețelele pre-antrenate funcționează bine pe imagini de tip similar, iar dacă începem să clasificăm imagini foarte diferite (de exemplu, imagini medicale), este probabil să obținem rezultate mult mai slabe.

**Declinare de responsabilitate**:  
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). Deși ne străduim să asigurăm acuratețea, vă rugăm să fiți conștienți că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa natală ar trebui considerat sursa autoritară. Pentru informații critice, se recomandă traducerea profesională realizată de un specialist uman. Nu ne asumăm responsabilitatea pentru eventualele neînțelegeri sau interpretări greșite care pot apărea din utilizarea acestei traduceri.