<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "7765935c35fcee69b9fe2d0cfd6963e2",
  "translation_date": "2025-08-31T17:38:50+00:00",
  "source_file": "lessons/4-ComputerVision/08-TransferLearning/lab/README.md",
  "language_code": "lt"
}
-->
# Oksfordo augintinių klasifikavimas naudojant perkėlimo mokymą

Laboratorinis darbas iš [AI for Beginners Curriculum](https://github.com/microsoft/ai-for-beginners).

## Užduotis

Įsivaizduokite, kad jums reikia sukurti programą augintinių darželiui, kuri kataloguotų visus augintinius. Viena iš puikių tokios programos funkcijų būtų automatiškai nustatyti veislę iš nuotraukos. Šiame užduotyje naudosime perkėlimo mokymą, kad klasifikuotume realias augintinių nuotraukas iš [Oxford-IIIT](https://www.robots.ox.ac.uk/~vgg/data/pets/) augintinių duomenų rinkinio.

## Duomenų rinkinys

Naudosime originalų [Oxford-IIIT](https://www.robots.ox.ac.uk/~vgg/data/pets/) augintinių duomenų rinkinį, kuriame yra 35 skirtingos šunų ir kačių veislės.

Norėdami atsisiųsti duomenų rinkinį, naudokite šį kodo fragmentą:

```python
!wget https://www.robots.ox.ac.uk/~vgg/data/pets/data/images.tar.gz
!tar xfz images.tar.gz
!rm images.tar.gz
```

## Pradinis užrašų knygelės failas

Pradėkite laboratorinį darbą atidarydami [OxfordPets.ipynb](OxfordPets.ipynb)

## Pamoka

Perkėlimo mokymas ir iš anksto apmokyti tinklai leidžia gana lengvai spręsti realaus pasaulio vaizdų klasifikavimo problemas. Tačiau iš anksto apmokyti tinklai gerai veikia su panašaus tipo vaizdais, o jei pradėsime klasifikuoti labai skirtingus vaizdus (pvz., medicininius vaizdus), rezultatai greičiausiai bus daug prastesni.

---

**Atsakomybės apribojimas**:  
Šis dokumentas buvo išverstas naudojant AI vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba turėtų būti laikomas autoritetingu šaltiniu. Kritinei informacijai rekomenduojama naudoti profesionalų žmogaus vertimą. Mes neprisiimame atsakomybės už nesusipratimus ar klaidingus interpretavimus, atsiradusius dėl šio vertimo naudojimo.