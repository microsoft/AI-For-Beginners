<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "2b544f20b796402507fb05a0df893323",
  "translation_date": "2025-08-31T17:51:21+00:00",
  "source_file": "lessons/3-NeuralNetworks/05-Frameworks/README.md",
  "language_code": "lt"
}
-->
# Neuroninių tinklų karkasai

Kaip jau išmokome, norint efektyviai treniruoti neuroninius tinklus, reikia atlikti du dalykus:

* Dirbti su tensoriais, pvz., dauginti, sudėti ir apskaičiuoti tam tikras funkcijas, tokias kaip sigmoidė ar softmax
* Apskaičiuoti visų išraiškų gradientus, kad būtų galima atlikti gradientinio nusileidimo optimizaciją

## [Prieš paskaitą atlikite testą](https://ff-quizzes.netlify.app/en/ai/quiz/9)

Nors `numpy` biblioteka gali atlikti pirmąją dalį, mums reikia mechanizmo gradientams apskaičiuoti. [Mūsų karkase](../04-OwnFramework/OwnFramework.ipynb), kurį sukūrėme ankstesniame skyriuje, turėjome rankiniu būdu programuoti visas išvestines funkcijas `backward` metode, kuris atlieka atgalinį sklidimą. Idealiu atveju karkasas turėtų suteikti galimybę apskaičiuoti *bet kurios išraiškos* gradientus, kuriuos galime apibrėžti.

Kitas svarbus dalykas yra galimybė atlikti skaičiavimus GPU arba kitais specializuotais skaičiavimo įrenginiais, tokiais kaip [TPU](https://en.wikipedia.org/wiki/Tensor_Processing_Unit). Giliųjų neuroninių tinklų treniravimas reikalauja *labai daug* skaičiavimų, todėl galimybė juos paralelizuoti GPU yra labai svarbi.

> ✅ Terminas „paralelizuoti“ reiškia paskirstyti skaičiavimus per kelis įrenginius.

Šiuo metu du populiariausi neuroninių tinklų karkasai yra: [TensorFlow](http://TensorFlow.org) ir [PyTorch](https://pytorch.org/). Abu jie suteikia žemo lygio API darbui su tensoriais tiek CPU, tiek GPU. Be žemo lygio API, taip pat yra aukšto lygio API, vadinami [Keras](https://keras.io/) ir [PyTorch Lightning](https://pytorchlightning.ai/) atitinkamai.

Žemo lygio API | [TensorFlow](http://TensorFlow.org) | [PyTorch](https://pytorch.org/)
---------------|-------------------------------------|--------------------------------
Aukšto lygio API| [Keras](https://keras.io/) | [PyTorch Lightning](https://pytorchlightning.ai/)

**Žemo lygio API** abiejuose karkasuose leidžia kurti vadinamuosius **skaičiavimo grafus**. Šis grafas apibrėžia, kaip apskaičiuoti išvestį (dažniausiai nuostolių funkciją) su pateiktais įvesties parametrais ir gali būti perduotas skaičiavimams GPU, jei jis yra prieinamas. Yra funkcijos, leidžiančios diferencijuoti šį skaičiavimo grafą ir apskaičiuoti gradientus, kurie vėliau gali būti naudojami modelio parametrų optimizavimui.

**Aukšto lygio API** traktuoja neuroninius tinklus kaip **sluoksnių seką** ir leidžia daug lengviau konstruoti daugumą neuroninių tinklų. Modelio treniravimas paprastai reikalauja paruošti duomenis ir tada iškviesti `fit` funkciją, kad atliktų darbą.

Aukšto lygio API leidžia labai greitai sukurti tipinius neuroninius tinklus, nesirūpinant daugybe detalių. Tuo pačiu metu žemo lygio API suteikia daug daugiau kontrolės treniravimo procesui, todėl jie dažnai naudojami tyrimuose, kai dirbama su naujomis neuroninių tinklų architektūromis.

Taip pat svarbu suprasti, kad galite naudoti abu API kartu, pvz., galite sukurti savo tinklo sluoksnio architektūrą naudodami žemo lygio API ir tada naudoti ją didesniame tinkle, sukurtame ir treniruotame su aukšto lygio API. Arba galite apibrėžti tinklą naudodami aukšto lygio API kaip sluoksnių seką ir tada naudoti savo žemo lygio treniravimo ciklą optimizacijai atlikti. Abu API naudoja tuos pačius pagrindinius principus ir yra sukurti taip, kad gerai veiktų kartu.

## Mokymasis

Šiame kurse dauguma turinio pateikiama tiek PyTorch, tiek TensorFlow karkasams. Galite pasirinkti savo mėgstamą karkasą ir peržiūrėti tik atitinkamus užrašus. Jei nesate tikri, kurį karkasą pasirinkti, perskaitykite diskusijas internete apie **PyTorch vs. TensorFlow**. Taip pat galite peržiūrėti abu karkasus, kad geriau juos suprastumėte.

Kai tik įmanoma, naudosime aukšto lygio API dėl paprastumo. Tačiau manome, kad svarbu suprasti, kaip neuroniniai tinklai veikia nuo pagrindų, todėl pradžioje dirbsime su žemo lygio API ir tensoriais. Tačiau, jei norite greitai pradėti ir nenorite skirti daug laiko šioms detalėms mokytis, galite praleisti šią dalį ir iškart pereiti prie aukšto lygio API užrašų.

## ✍️ Pratimai: Karkasai

Tęskite mokymąsi šiuose užrašuose:

Žemo lygio API | [TensorFlow+Keras Užrašai](IntroKerasTF.ipynb) | [PyTorch](IntroPyTorch.ipynb)
---------------|-------------------------------------|--------------------------------
Aukšto lygio API| [Keras](IntroKeras.ipynb) | *PyTorch Lightning*

Įvaldę karkasus, prisiminkime per didelio pritaikymo (overfitting) sąvoką.

# Per didelis pritaikymas (Overfitting)

Per didelis pritaikymas yra itin svarbi sąvoka mašininio mokymosi srityje, ir labai svarbu ją teisingai suprasti!

Apsvarstykime šią problemą, kai reikia aproksimuoti 5 taškus (grafikuose žymimi kaip `x`):

![linear](../../../../../translated_images/overfit1.f24b71c6f652e59e6bed7245ffbeaecc3ba320e16e2221f6832b432052c4da43.lt.jpg) | ![overfit](../../../../../translated_images/overfit2.131f5800ae10ca5e41d12a411f5f705d9ee38b1b10916f284b787028dd55cc1c.lt.jpg)
-------------------------|--------------------------
**Linijinis modelis, 2 parametrai** | **Nelinijinis modelis, 7 parametrai**
Treniravimo klaida = 5.3 | Treniravimo klaida = 0
Validavimo klaida = 5.1 | Validavimo klaida = 20

* Kairėje matome gerą tiesios linijos aproksimaciją. Kadangi parametrų skaičius yra tinkamas, modelis teisingai supranta taškų pasiskirstymo esmę.
* Dešinėje modelis yra per daug galingas. Kadangi turime tik 5 taškus, o modelis turi 7 parametrus, jis gali prisitaikyti taip, kad praeitų per visus taškus, todėl treniravimo klaida tampa 0. Tačiau tai neleidžia modeliui suprasti teisingo duomenų modelio, todėl validavimo klaida yra labai didelė.

Labai svarbu rasti tinkamą pusiausvyrą tarp modelio sudėtingumo (parametrų skaičiaus) ir treniravimo pavyzdžių skaičiaus.

## Kodėl atsiranda per didelis pritaikymas

  * Nepakanka treniravimo duomenų
  * Per daug galingas modelis
  * Per daug triukšmo įvesties duomenyse

## Kaip aptikti per didelį pritaikymą

Kaip matote iš aukščiau pateikto grafiko, per didelį pritaikymą galima aptikti pagal labai mažą treniravimo klaidą ir didelę validavimo klaidą. Paprastai treniravimo metu matysime, kaip tiek treniravimo, tiek validavimo klaidos pradeda mažėti, o tada tam tikru momentu validavimo klaida gali nustoti mažėti ir pradėti didėti. Tai bus ženklas, kad atsirado per didelis pritaikymas, ir indikatorius, kad turėtume sustabdyti treniravimą (arba bent jau išsaugoti modelio būseną).

![overfitting](../../../../../translated_images/Overfitting.408ad91cd90b4371d0a81f4287e1409c359751adeb1ae450332af50e84f08c3e.lt.png)

## Kaip išvengti per didelio pritaikymo

Jei pastebite, kad atsiranda per didelis pritaikymas, galite atlikti vieną iš šių veiksmų:

 * Padidinti treniravimo duomenų kiekį
 * Sumažinti modelio sudėtingumą
 * Naudoti tam tikrą [reguliavimo techniką](../../4-ComputerVision/08-TransferLearning/TrainingTricks.md), pvz., [Dropout](../../4-ComputerVision/08-TransferLearning/TrainingTricks.md#Dropout), kurią aptarsime vėliau.

## Per didelis pritaikymas ir šališkumo-variacijos kompromisas

Per didelis pritaikymas iš tikrųjų yra bendresnės statistikos problemos, vadinamos [šališkumo-variacijos kompromisu](https://en.wikipedia.org/wiki/Bias%E2%80%93variance_tradeoff), atvejis. Jei apsvarstysime galimus klaidų šaltinius mūsų modelyje, galime išskirti dviejų tipų klaidas:

* **Šališkumo klaidos** atsiranda, kai mūsų algoritmas negali teisingai užfiksuoti ryšio tarp treniravimo duomenų. Tai gali būti dėl to, kad mūsų modelis nėra pakankamai galingas (**nepakankamas pritaikymas**).
* **Variacijos klaidos**, kurios atsiranda, kai modelis aproksimuoja triukšmą įvesties duomenyse vietoj prasmingo ryšio (**per didelis pritaikymas**).

Treniravimo metu šališkumo klaida mažėja (kai mūsų modelis mokosi aproksimuoti duomenis), o variacijos klaida didėja. Svarbu sustabdyti treniravimą - arba rankiniu būdu (kai aptinkame per didelį pritaikymą), arba automatiškai (įvedant reguliavimą) - kad išvengtume per didelio pritaikymo.

## Išvada

Šioje pamokoje sužinojote apie skirtumus tarp įvairių API dviejuose populiariausiuose AI karkasuose, TensorFlow ir PyTorch. Be to, sužinojote apie labai svarbią temą - per didelį pritaikymą.

## 🚀 Iššūkis

Pridedamuose užrašuose rasite „užduotis“ apačioje; peržiūrėkite užrašus ir atlikite užduotis.

## [Po paskaitos atlikite testą](https://ff-quizzes.netlify.app/en/ai/quiz/10)

## Peržiūra ir savarankiškas mokymasis

Atlikite tyrimą šiomis temomis:

- TensorFlow
- PyTorch
- Per didelis pritaikymas

Paklauskite savęs šių klausimų:

- Kuo skiriasi TensorFlow ir PyTorch?
- Kuo skiriasi per didelis pritaikymas ir nepakankamas pritaikymas?

## [Užduotis](lab/README.md)

Šioje laboratorijoje jūsų prašoma išspręsti dvi klasifikavimo problemas naudojant vieno ir kelių sluoksnių visiškai sujungtus tinklus su PyTorch arba TensorFlow.

* [Instrukcijos](lab/README.md)
* [Užrašai](lab/LabFrameworks.ipynb)

---

**Atsakomybės apribojimas**:  
Šis dokumentas buvo išverstas naudojant AI vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba turėtų būti laikomas autoritetingu šaltiniu. Kritinei informacijai rekomenduojama profesionali žmogaus vertimo paslauga. Mes neprisiimame atsakomybės už nesusipratimus ar klaidingus interpretavimus, atsiradusius naudojant šį vertimą.