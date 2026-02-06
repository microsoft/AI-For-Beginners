# Mokymas Skip-Gram Modelio

Laboratorinis darbas iš [AI for Beginners Curriculum](https://github.com/microsoft/ai-for-beginners).

## Užduotis

Šiame laboratoriniame darbe jums siūloma išmokyti Word2Vec modelį naudojant Skip-Gram techniką. Išmokykite tinklą su įterpimais (embedding), kad jis galėtų prognozuoti kaimyninius žodžius $N$ žodžių pločio Skip-Gram lange. Galite naudoti [kodą iš šios pamokos](../CBoW-TF.ipynb) ir šiek tiek jį modifikuoti.

## Duomenų rinkinys

Galite naudoti bet kurią knygą. Daug nemokamų tekstų galite rasti [Project Gutenberg](https://www.gutenberg.org/), pavyzdžiui, čia yra tiesioginė nuoroda į [Alisos nuotykius Stebuklų šalyje](https://www.gutenberg.org/files/11/11-0.txt)) autoriaus Lewis Carroll. Arba galite naudoti Šekspyro pjeses, kurias galite gauti naudodami šį kodą:

```python
path_to_file = tf.keras.utils.get_file(
   'shakespeare.txt', 
   'https://storage.googleapis.com/download.tensorflow.org/data/shakespeare.txt')
text = open(path_to_file, 'rb').read().decode(encoding='utf-8')
```

## Tyrinėkite!

Jei turite laiko ir norite giliau pasinerti į temą, pabandykite ištirti keletą dalykų:

* Kaip įterpimo dydis veikia rezultatus?
* Kaip skirtingi teksto stiliai veikia rezultatą?
* Paimkite keletą labai skirtingų žodžių ir jų sinonimų, gaukite jų vektorinę reprezentaciją, pritaikykite PCA, kad sumažintumėte dimensijas iki 2, ir pavaizduokite juos 2D erdvėje. Ar pastebite kokius nors dėsningumus?

---

**Atsakomybės apribojimas**:  
Šis dokumentas buvo išverstas naudojant AI vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba turėtų būti laikomas autoritetingu šaltiniu. Kritinei informacijai rekomenduojama naudoti profesionalų žmogaus vertimą. Mes neprisiimame atsakomybės už nesusipratimus ar klaidingus interpretavimus, atsiradusius dėl šio vertimo naudojimo.