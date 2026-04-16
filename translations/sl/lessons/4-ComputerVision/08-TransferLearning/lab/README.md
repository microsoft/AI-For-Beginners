# Klasifikacija hišnih ljubljenčkov iz Oxforda z uporabo prenosa učenja

Laboratorijska naloga iz [Učnega načrta za začetnike v umetni inteligenci](https://github.com/microsoft/ai-for-beginners).

## Naloga

Predstavljajte si, da morate razviti aplikacijo za vrtec za hišne ljubljenčke, ki bi katalogizirala vse ljubljenčke. Ena izmed odličnih funkcij takšne aplikacije bi bila samodejno prepoznavanje pasme s fotografije. V tej nalogi bomo uporabili prenos učenja za klasifikacijo slik resničnih hišnih ljubljenčkov iz nabora podatkov [Oxford-IIIT](https://www.robots.ox.ac.uk/~vgg/data/pets/).

## Nabor podatkov

Uporabili bomo izvirni nabor podatkov [Oxford-IIIT](https://www.robots.ox.ac.uk/~vgg/data/pets/), ki vsebuje 35 različnih pasem psov in mačk.

Za prenos nabora podatkov uporabite to kodo:

```python
!wget https://www.robots.ox.ac.uk/~vgg/data/pets/data/images.tar.gz
!tar xfz images.tar.gz
!rm images.tar.gz
```

## Začetek zvezka

Začnite laboratorijsko nalogo z odpiranjem [OxfordPets.ipynb](../../../../../../lessons/4-ComputerVision/08-TransferLearning/lab/OxfordPets.ipynb)

## Ključna spoznanja

Prenos učenja in vnaprej naučena omrežja nam omogočajo, da relativno enostavno rešujemo resnične probleme klasifikacije slik. Vendar pa vnaprej naučena omrežja dobro delujejo na slikah podobne vrste, in če začnemo klasificirati zelo različne slike (npr. medicinske slike), bodo rezultati verjetno precej slabši.

**Omejitev odgovornosti**:  
Ta dokument je bil preveden z uporabo storitve AI za prevajanje [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas prosimo, da upoštevate, da lahko avtomatizirani prevodi vsebujejo napake ali netočnosti. Izvirni dokument v njegovem izvirnem jeziku je treba obravnavati kot avtoritativni vir. Za ključne informacije priporočamo profesionalni človeški prevod. Ne prevzemamo odgovornosti za morebitne nesporazume ali napačne razlage, ki bi nastale zaradi uporabe tega prevoda.