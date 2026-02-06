# Žmogaus kūno segmentacija

Laboratorinis darbas iš [AI for Beginners Curriculum](https://github.com/microsoft/ai-for-beginners).

## Užduotis

Vaizdo gamyboje, pavyzdžiui, orų prognozėse, dažnai reikia iškirpti žmogaus atvaizdą iš kameros ir uždėti jį ant kito vaizdo. Tai paprastai atliekama naudojant **chroma key** techniką, kai žmogus filmuojamas prieš vienodos spalvos foną, kuris vėliau pašalinamas. Šiame laboratoriniame darbe mes treniruosime neuroninį tinklą, kad jis galėtų iškirpti žmogaus siluetą.

## Duomenų rinkinys

Naudosime [Segmentation Full Body MADS Dataset](https://www.kaggle.com/datasets/tapakah68/segmentation-full-body-mads-dataset) iš Kaggle. Atsisiųskite duomenų rinkinį rankiniu būdu iš Kaggle.

## Pradinis užrašų knygelės failas

Pradėkite laboratorinį darbą atidarę [BodySegmentation.ipynb](BodySegmentation.ipynb)

## Išvada

Kūno segmentacija yra tik viena iš įprastų užduočių, kurias galima atlikti su žmonių vaizdais. Kitos svarbios užduotys apima **skeletų aptikimą** ir **pozų aptikimą**. Pažvelkite į [OpenPose](https://github.com/CMU-Perceptual-Computing-Lab/openpose) biblioteką, kad sužinotumėte, kaip šios užduotys gali būti įgyvendintos.

---

**Atsakomybės apribojimas**:  
Šis dokumentas buvo išverstas naudojant AI vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba turėtų būti laikomas autoritetingu šaltiniu. Kritinei informacijai rekomenduojama naudoti profesionalų žmogaus vertimą. Mes neprisiimame atsakomybės už nesusipratimus ar klaidingus interpretavimus, atsiradusius dėl šio vertimo naudojimo.