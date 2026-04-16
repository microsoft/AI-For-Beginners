# Razvrščanje obrazov hišnih ljubljenčkov

Laboratorijska naloga iz [Učnega načrta za začetnike v AI](https://github.com/microsoft/ai-for-beginners).

## Naloga

Predstavljajte si, da morate razviti aplikacijo za vrtec hišnih ljubljenčkov, ki bo katalogizirala vse živali. Ena izmed odličnih funkcij takšne aplikacije bi bila samodejno prepoznavanje pasme s fotografije. To je mogoče uspešno doseči z uporabo nevronskih mrež.

Vaša naloga je, da usposobite konvolucijsko nevronsko mrežo za razvrščanje različnih pasem mačk in psov z uporabo podatkovne zbirke **Pet Faces**.

## Podatkovna zbirka

Uporabili bomo [Oxford-IIIT Pet Dataset](https://www.robots.ox.ac.uk/~vgg/data/pets/), ki vsebuje slike 37 različnih pasem psov in mačk.

![Podatkovna zbirka, s katero bomo delali](../../../../../../translated_images/sl/data.50b2a9d5484bdbf0.webp)

Za prenos podatkovne zbirke uporabite naslednji del kode:

```python
!wget https://thor.robots.ox.ac.uk/~vgg/data/pets/images.tar.gz
!tar xfz images.tar.gz
!rm images.tar.gz
```

**Opomba:** Slike v podatkovni zbirki Oxford-IIIT Pet Dataset so organizirane po imenu datoteke (npr. `Abyssinian_1.jpg`, `Bengal_2.jpg`). Zvezek vključuje kodo za organizacijo teh slik v podimenike, specifične za pasme, kar olajša razvrščanje.

## Začetni zvezek

Začnite laboratorijsko nalogo z odpiranjem [PetFaces.ipynb](PetFaces.ipynb)

## Ključne ugotovitve

Rešili ste razmeroma zapleten problem razvrščanja slik od začetka! Kljub velikemu številu razredov ste uspeli doseči razumno natančnost! Smiselno je tudi meriti top-k natančnost, saj je enostavno zamenjati nekatere razrede, ki niso jasno različni niti za ljudi.

---

**Omejitev odgovornosti**:  
Ta dokument je bil preveden z uporabo storitve AI za prevajanje [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas prosimo, da upoštevate, da lahko avtomatizirani prevodi vsebujejo napake ali netočnosti. Izvirni dokument v njegovem maternem jeziku je treba obravnavati kot avtoritativni vir. Za ključne informacije priporočamo profesionalni človeški prevod. Ne prevzemamo odgovornosti za morebitna nesporazumevanja ali napačne razlage, ki izhajajo iz uporabe tega prevoda.