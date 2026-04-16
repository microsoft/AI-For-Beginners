# Klasifikavimas į kelias klases naudojant perceptroną

Laboratorinis darbas iš [AI for Beginners Curriculum](https://github.com/microsoft/ai-for-beginners).

## Užduotis

Naudodami kodą, kurį sukūrėme šioje pamokoje MNIST ranka rašytų skaitmenų dvejetainiam klasifikavimui, sukurkite klasifikatorių, kuris galėtų atpažinti bet kurį skaitmenį. Apskaičiuokite klasifikavimo tikslumą treniravimo ir testavimo duomenų rinkiniuose ir išveskite painiavos matricą.

## Patarimai

1. Kiekvienam skaitmeniui sukurkite duomenų rinkinį dvejetainiam klasifikatoriui „šis skaitmuo prieš visus kitus skaitmenis“.
1. Išmokykite 10 skirtingų perceptronų dvejetainiam klasifikavimui (po vieną kiekvienam skaitmeniui).
1. Apibrėžkite funkciją, kuri klasifikuos įvestą skaitmenį.

> **Patarimas**: Jei sujungsime visų 10 perceptronų svorius į vieną matricą, galėsime pritaikyti visus 10 perceptronų įvestiems skaitmenims vienu matricos daugyba. Labiausiai tikėtinas skaitmuo gali būti nustatytas tiesiog pritaikant `argmax` operaciją išvestyje.

## Pradinis užrašų knygelės failas

Pradėkite laboratorinį darbą atidarę [PerceptronMultiClass.ipynb](PerceptronMultiClass.ipynb)

---

**Atsakomybės atsisakymas**:  
Šis dokumentas buvo išverstas naudojant AI vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba turėtų būti laikomas autoritetingu šaltiniu. Kritinei informacijai rekomenduojama profesionali žmogaus vertimo paslauga. Mes neprisiimame atsakomybės už nesusipratimus ar klaidingus interpretavimus, atsiradusius naudojant šį vertimą.