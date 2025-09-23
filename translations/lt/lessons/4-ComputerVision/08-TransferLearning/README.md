<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "717775c4050ccbffbe0c961ad8bf7bf7",
  "translation_date": "2025-08-31T17:37:23+00:00",
  "source_file": "lessons/4-ComputerVision/08-TransferLearning/README.md",
  "language_code": "lt"
}
-->
# Iš anksto apmokyti tinklai ir perkėlimo mokymasis

CNN mokymas gali užtrukti daug laiko, o tam reikia daug duomenų. Tačiau didžioji dalis laiko skiriama geriausių žemo lygio filtrų mokymuisi, kuriuos tinklas gali naudoti norėdamas išgauti vaizdų raštus. Kyla natūralus klausimas – ar galime naudoti neuroninį tinklą, apmokytą viename duomenų rinkinyje, ir pritaikyti jį skirtingų vaizdų klasifikavimui, nereikalaujant pilno mokymo proceso?

## [Prieš paskaitą viktorina](https://ff-quizzes.netlify.app/en/ai/quiz/15)

Šis metodas vadinamas **perkėlimo mokymusi**, nes mes perkeliam tam tikras žinias iš vieno neuroninio tinklo modelio į kitą. Perkėlimo mokymesi paprastai pradedame nuo iš anksto apmokyto modelio, kuris buvo apmokytas naudojant didelį vaizdų duomenų rinkinį, pvz., **ImageNet**. Šie modeliai jau gerai išgauna įvairias savybes iš bendrinių vaizdų, ir daugeliu atvejų tiesiog sukūrus klasifikatorių ant šių išgautų savybių galima pasiekti gerą rezultatą.

> ✅ Perkėlimo mokymasis yra terminas, kurį galite rasti ir kitose akademinėse srityse, pvz., švietime. Jis reiškia procesą, kai žinios iš vienos srities pritaikomos kitoje.

## Iš anksto apmokyti modeliai kaip savybių išgavimo įrankiai

Konvoliuciniai tinklai, apie kuriuos kalbėjome ankstesniame skyriuje, turi daugybę sluoksnių, kurių kiekvienas skirtas išgauti tam tikras savybes iš vaizdo, pradedant nuo žemo lygio pikselių kombinacijų (pvz., horizontalios/vertikalios linijos ar brūkšniai), iki aukštesnio lygio savybių kombinacijų, atitinkančių, pavyzdžiui, liepsnos akį. Jei apmokysime CNN su pakankamai dideliu bendrinių ir įvairių vaizdų duomenų rinkiniu, tinklas turėtų išmokti išgauti šias bendras savybes.

Tiek Keras, tiek PyTorch turi funkcijas, leidžiančias lengvai įkelti iš anksto apmokytus neuroninio tinklo svorius kai kurioms įprastoms architektūroms, dauguma kurių buvo apmokytos naudojant ImageNet vaizdus. Dažniausiai naudojamos architektūros aprašytos [CNN architektūrų](../07-ConvNets/CNN_Architectures.md) puslapyje iš ankstesnės pamokos. Ypač galite apsvarstyti vieną iš šių:

* **VGG-16/VGG-19** – tai palyginti paprasti modeliai, kurie vis dar suteikia gerą tikslumą. Dažnai VGG naudojimas kaip pirmasis bandymas yra geras pasirinkimas norint pamatyti, kaip veikia perkėlimo mokymasis.
* **ResNet** – tai modelių šeima, kurią 2015 m. pasiūlė Microsoft Research. Jie turi daugiau sluoksnių, todėl reikalauja daugiau resursų.
* **MobileNet** – tai modelių šeima su sumažintu dydžiu, tinkama mobiliesiems įrenginiams. Naudokite juos, jei turite mažai resursų ir galite paaukoti šiek tiek tikslumo.

Štai pavyzdinės savybės, išgautos iš katės nuotraukos naudojant VGG-16 tinklą:

![Savybės, išgautos VGG-16](../../../../../translated_images/features.6291f9c7ba3a0b951af88fc9864632b9115365410765680680d30c927dd67354.lt.png)

## Kačių ir šunų duomenų rinkinys

Šiame pavyzdyje naudosime [Kačių ir šunų](https://www.microsoft.com/download/details.aspx?id=54765&WT.mc_id=academic-77998-cacaste) duomenų rinkinį, kuris yra labai artimas realaus gyvenimo vaizdų klasifikavimo scenarijui.

## ✍️ Pratimai: Perkėlimo mokymasis

Pažiūrėkime, kaip veikia perkėlimo mokymasis atitinkamuose užrašų knygelėse:

* [Perkėlimo mokymasis - PyTorch](TransferLearningPyTorch.ipynb)
* [Perkėlimo mokymasis - TensorFlow](TransferLearningTF.ipynb)

## Vizualizuojame priešišką katę

Iš anksto apmokytas neuroninis tinklas turi įvairius raštus savo *smegenyse*, įskaitant **idealios katės** (taip pat idealios šuns, idealios zebros ir kt.) sąvokas. Būtų įdomu kažkaip **vizualizuoti šį vaizdą**. Tačiau tai nėra paprasta, nes raštai yra išsklaidyti visame tinklo svoriuose ir taip pat organizuoti hierarchinėje struktūroje.

Vienas iš būdų, kurį galime naudoti, yra pradėti nuo atsitiktinio vaizdo ir tada pabandyti naudoti **gradientinio nusileidimo optimizavimo** techniką, kad pakoreguotume tą vaizdą taip, kad tinklas pradėtų manyti, jog tai yra katė.

![Vaizdo optimizavimo ciklas](../../../../../translated_images/ideal-cat-loop.999fbb8ff306e044f997032f4eef9152b453e6a990e449bbfb107de2493cc37e.lt.png)

Tačiau, jei tai padarysime, gausime kažką labai panašaus į atsitiktinį triukšmą. Taip yra todėl, kad *yra daug būdų, kaip tinklas gali manyti, kad įvesties vaizdas yra katė*, įskaitant kai kuriuos, kurie vizualiai neturi prasmės. Nors šie vaizdai turi daug raštų, būdingų katei, nėra nieko, kas apribotų juos būti vizualiai išskirtiniais.

Norėdami pagerinti rezultatą, galime pridėti kitą terminą į nuostolių funkciją, vadinamą **variacijos nuostoliu**. Tai metrika, rodanti, kaip panašūs yra kaimyniniai vaizdo pikseliai. Mažinant variacijos nuostolį vaizdas tampa lygesnis ir atsikratoma triukšmo – taip atskleidžiami vizualiai patrauklesni raštai. Štai pavyzdys tokių "idealių" vaizdų, kurie yra klasifikuojami kaip katė ir kaip zebra su didele tikimybe:

![Ideali katė](../../../../../translated_images/ideal-cat.203dd4597643d6b0bd73038b87f9c0464322725e3a06ab145d25d4a861c70592.lt.png) | ![Ideali zebra](../../../../../translated_images/ideal-zebra.7f70e8b54ee15a7a314000bb5df38a6cfe086ea04d60df4d3ef313d046b98a2b.lt.png)
-----|-----
 *Ideali katė* | *Ideali zebra*

Panašus metodas gali būti naudojamas vadinamiesiems **priešiškiems išpuoliams** prieš neuroninį tinklą atlikti. Tarkime, norime apgauti neuroninį tinklą ir priversti šunį atrodyti kaip katę. Jei paimsime šuns vaizdą, kurį tinklas atpažįsta kaip šunį, galime šiek tiek jį pakoreguoti naudodami gradientinio nusileidimo optimizavimą, kol tinklas pradės jį klasifikuoti kaip katę:

![Šuns nuotrauka](../../../../../translated_images/original-dog.8f68a67d2fe0911f33041c0f7fce8aa4ea919f9d3917ec4b468298522aeb6356.lt.png) | ![Šuns nuotrauka, klasifikuojama kaip katė](../../../../../translated_images/adversarial-dog.d9fc7773b0142b89752539bfbf884118de845b3851c5162146ea0b8809fc820f.lt.png)
-----|-----
*Originali šuns nuotrauka* | *Šuns nuotrauka, klasifikuojama kaip katė*

Žr. kodą, kaip atkurti aukščiau pateiktus rezultatus, šioje užrašų knygelėje:

* [Ideali ir priešiška katė - TensorFlow](AdversarialCat_TF.ipynb)

## Išvada

Naudodami perkėlimo mokymąsi, galite greitai sukurti klasifikatorių pagal užsakymą objektų klasifikavimo užduočiai ir pasiekti aukštą tikslumą. Matote, kad sudėtingesnės užduotys, kurias dabar sprendžiame, reikalauja didesnės skaičiavimo galios ir negali būti lengvai išspręstos naudojant CPU. Kitame skyriuje pabandysime naudoti lengvesnę įgyvendinimo versiją, kad apmokytume tą patį modelį naudodami mažesnius skaičiavimo resursus, o tai lemia tik šiek tiek mažesnį tikslumą.

## 🚀 Iššūkis

Pridedamose užrašų knygelėse yra pastabų apačioje apie tai, kaip perkėlimo žinios geriausiai veikia su šiek tiek panašiais mokymo duomenimis (galbūt naujo tipo gyvūnu). Atlikite eksperimentus su visiškai naujais vaizdų tipais, kad pamatytumėte, kaip gerai ar prastai veikia jūsų perkėlimo žinių modeliai.

## [Po paskaitos viktorina](https://ff-quizzes.netlify.app/en/ai/quiz/16)

## Apžvalga ir savarankiškas mokymasis

Perskaitykite [TrainingTricks.md](TrainingTricks.md), kad pagilintumėte savo žinias apie kitus būdus, kaip mokyti savo modelius.

## [Užduotis](lab/README.md)

Šioje laboratorijoje naudosime realaus gyvenimo [Oxford-IIIT](https://www.robots.ox.ac.uk/~vgg/data/pets/) naminių gyvūnų duomenų rinkinį su 35 kačių ir šunų veislėmis ir sukursime perkėlimo mokymosi klasifikatorių.

---

**Atsakomybės apribojimas**:  
Šis dokumentas buvo išverstas naudojant AI vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba turėtų būti laikomas autoritetingu šaltiniu. Kritinei informacijai rekomenduojama naudoti profesionalų žmogaus vertimą. Mes neprisiimame atsakomybės už nesusipratimus ar klaidingus interpretavimus, atsiradusius dėl šio vertimo naudojimo.