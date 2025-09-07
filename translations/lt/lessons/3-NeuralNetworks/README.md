<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "5abc5f7978919be90cd313f0c20e8228",
  "translation_date": "2025-09-07T14:38:11+00:00",
  "source_file": "lessons/3-NeuralNetworks/README.md",
  "language_code": "lt"
}
-->
# Įvadas į neuroninius tinklus

![Santrauka apie neuroninių tinklų įvadą piešinyje](../../../../translated_images/ai-neuralnetworks.1c687ae40bc86e834f497844866a26d3e0886650a67a4bbe29442e2f157d3b18.lt.png)

Kaip aptarėme įvade, vienas iš būdų pasiekti intelektą yra treniruoti **kompiuterinį modelį** arba **dirbtines smegenis**. Nuo XX a. vidurio mokslininkai bandė įvairius matematinius modelius, kol pastaraisiais metais ši kryptis tapo itin sėkminga. Tokie smegenų matematiniai modeliai vadinami **neuroniniais tinklais**.

> Kartais neuroniniai tinklai vadinami *Dirbtiniais neuroniniais tinklais* (angl. Artificial Neural Networks, ANNs), siekiant pabrėžti, kad kalbame apie modelius, o ne apie tikrus neuronų tinklus.

## Mašininis mokymasis

Neuroniniai tinklai yra platesnės disciplinos, vadinamos **Mašininiu mokymusi**, dalis. Jos tikslas – naudoti duomenis kompiuteriniams modeliams treniruoti, kad jie galėtų spręsti problemas. Mašininis mokymasis sudaro didelę dalį Dirbtinio intelekto, tačiau šiame kurse klasikinio mašininio mokymosi neaptarsime.

> Apsilankykite mūsų atskirame kurse **[Mašininis mokymasis pradedantiesiems](http://github.com/microsoft/ml-for-beginners)**, kad sužinotumėte daugiau apie klasikinį mašininį mokymąsi.

Mašininiame mokymesi daroma prielaida, kad turime tam tikrą pavyzdžių duomenų rinkinį **X** ir atitinkamas išėjimo reikšmes **Y**. Pavyzdžiai dažnai yra N-dimensijų vektoriai, sudaryti iš **savybių**, o išėjimai vadinami **žymėmis**.

Mes nagrinėsime dvi dažniausiai pasitaikančias mašininio mokymosi problemas:

* **Klasifikacija**, kai reikia priskirti įvesties objektą vienai iš dviejų ar daugiau klasių.
* **Regresija**, kai reikia prognozuoti skaitinę reikšmę kiekvienam įvesties pavyzdžiui.

> Kai įvestys ir išėjimai pateikiami kaip tensoriai, įvesties duomenų rinkinys yra M×N dydžio matrica, kur M – pavyzdžių skaičius, o N – savybių skaičius. Išėjimo žymės Y yra M dydžio vektorius.

Šiame kurse dėmesį sutelksime tik į neuroninių tinklų modelius.

## Neurono modelis

Iš biologijos žinome, kad mūsų smegenys sudarytos iš neuroninių ląstelių, kurių kiekviena turi kelis „įėjimus“ (aksonus) ir vieną išėjimą (dendritą). Aksonai ir dendritai gali perduoti elektrinius signalus, o jungtys tarp aksonų ir dendritų gali turėti skirtingą laidumą (kontroliuojamą neuromediatoriais).

![Neurono modelis](../../../../translated_images/synapse-wikipedia.ed20a9e4726ea1c6a3ce8fec51c0b9bec6181946dca0fe4e829bc12fa3bacf01.lt.jpg) | ![Neurono modelis](../../../../translated_images/artneuron.1a5daa88d20ebe6f5824ddb89fba0bdaaf49f67e8230c1afbec42909df1fc17e.lt.png)
----|----
Tikras neuronas *([Vaizdas](https://en.wikipedia.org/wiki/Synapse#/media/File:SynapseSchematic_lines.svg) iš Vikipedijos)* | Dirbtinis neuronas *(Autoriaus vaizdas)*

Taigi, paprasčiausias neurono matematinis modelis turi kelis įėjimus X<sub>1</sub>, ..., X<sub>N</sub>, vieną išėjimą Y ir svorių rinkinį W<sub>1</sub>, ..., W<sub>N</sub>. Išėjimas apskaičiuojamas taip:

<img src="images/netout.png" alt="Y = f\left(\sum_{i=1}^N X_iW_i\right)" width="131" height="53" align="center"/>

kur f yra tam tikra nelinijinė **aktyvavimo funkcija**.

> Ankstyvieji neurono modeliai buvo aprašyti klasikiniame straipsnyje [A logical calculus of the ideas immanent in nervous activity](https://www.cs.cmu.edu/~./epxing/Class/10715/reading/McCulloch.and.Pitts.pdf), kurį 1943 m. parašė Warren McCullock ir Walter Pitts. Donald Hebb savo knygoje "[The Organization of Behavior: A Neuropsychological Theory](https://books.google.com/books?id=VNetYrB8EBoC)" pasiūlė, kaip šiuos tinklus galima treniruoti.

## Šiame skyriuje

Šiame skyriuje sužinosime apie:
* [Perceptroną](03-Perceptron/README.md), vieną iš ankstyviausių neuroninių tinklų modelių, skirtų dviejų klasių klasifikacijai
* [Daugiasluoksnius tinklus](04-OwnFramework/README.md) su susietu užrašų knygele [kaip sukurti savo sistemą](04-OwnFramework/OwnFramework.ipynb)
* [Neuroninių tinklų sistemas](05-Frameworks/README.md), su šiomis užrašų knygelėmis: [PyTorch](05-Frameworks/IntroPyTorch.ipynb) ir [Keras/Tensorflow](05-Frameworks/IntroKerasTF.ipynb)
* [Perdidelį pritaikymą](../../../../lessons/3-NeuralNetworks/05-Frameworks)

---

**Atsakomybės apribojimas**:  
Šis dokumentas buvo išverstas naudojant AI vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba turėtų būti laikomas autoritetingu šaltiniu. Kritinei informacijai rekomenduojama naudoti profesionalų žmogaus vertimą. Mes neprisiimame atsakomybės už nesusipratimus ar klaidingus interpretavimus, atsiradusius dėl šio vertimo naudojimo.