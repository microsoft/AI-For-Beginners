<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "bd10f434e444bce61b7f97eeb1ff6a55",
  "translation_date": "2025-08-31T17:59:00+00:00",
  "source_file": "lessons/5-NLP/19-NER/README.md",
  "language_code": "lt"
}
-->
# Pavadinimų atpažinimas (NER)

Iki šiol daugiausia dėmesio skyrėme vienai NLP užduočiai – klasifikacijai. Tačiau yra ir kitų NLP užduočių, kurias galima atlikti naudojant neuroninius tinklus. Viena iš tokių užduočių yra **[Pavadinimų atpažinimas](https://wikipedia.org/wiki/Named-entity_recognition)** (NER), kuris susijęs su specifinių objektų atpažinimu tekste, tokių kaip vietovės, asmenų vardai, datos ir laiko intervalai, cheminės formulės ir pan.

## [Prieš paskaitą: klausimynas](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/119)

## NER naudojimo pavyzdys

Tarkime, norite sukurti natūralios kalbos pokalbių robotą, panašų į „Amazon Alexa“ ar „Google Assistant“. Išmanieji pokalbių robotai veikia taip, kad *supranta*, ko vartotojas nori, atlikdami teksto klasifikaciją pagal įvestą sakinį. Šios klasifikacijos rezultatas yra vadinamoji **intencija**, kuri nurodo, ką pokalbių robotas turėtų atlikti.

<img alt="Bot NER" src="images/bot-ner.png" width="50%"/>

> Paveikslėlis autoriaus

Tačiau vartotojas gali pateikti tam tikrus parametrus kaip frazės dalį. Pavyzdžiui, klausiant apie orą, jis gali nurodyti vietą ar datą. Robotui reikia suprasti šiuos objektus ir atitinkamai užpildyti parametrų laukus prieš atliekant veiksmą. Būtent čia pasitarnauja NER.

> ✅ Kitas pavyzdys galėtų būti [mokslinių medicininių straipsnių analizė](https://soshnikov.com/science/analyzing-medical-papers-with-azure-and-text-analytics-for-health/). Vienas iš pagrindinių dalykų, kuriuos reikia rasti, yra specifiniai medicininiai terminai, tokie kaip ligos ir medicininės medžiagos. Nors nedidelį ligų skaičių galima išgauti naudojant paprastą paiešką, sudėtingesniems objektams, tokiems kaip cheminiai junginiai ar vaistų pavadinimai, reikia sudėtingesnio požiūrio.

## NER kaip žymėjimas pagal žodžius

NER modeliai iš esmės yra **žodžių klasifikavimo modeliai**, nes kiekvienam įvesties žodžiui reikia nuspręsti, ar jis priklauso tam tikram objektui, ir jei taip – kokiai objektų klasei.

Apsvarstykime šį straipsnio pavadinimą:

**Trikuspidinio vožtuvo regurgitacija** ir **ličio karbonato** **toksikacija** naujagimiui.

Čia objektai yra:

* Trikuspidinio vožtuvo regurgitacija yra liga (`DIS`)
* Ličio karbonatas yra cheminė medžiaga (`CHEM`)
* Toksikacija taip pat yra liga (`DIS`)

Atkreipkite dėmesį, kad vienas objektas gali apimti kelis žodžius. Ir, kaip šiuo atveju, reikia atskirti du iš eilės einančius objektus. Todėl įprasta naudoti dvi klases kiekvienam objektui – vieną, nurodančią pirmąjį objekto žodį (dažnai naudojamas `B-` priešdėlis, reiškiantis **pradžią**), ir kitą – objekto tęsinį (`I-`, reiškia **vidinį žodį**). Taip pat naudojame `O` kaip klasę, žyminčią visus **kitus** žodžius. Toks žodžių žymėjimas vadinamas [BIO žymėjimu](https://en.wikipedia.org/wiki/Inside%E2%80%93outside%E2%80%93beginning_(tagging)) (arba IOB). Pažymėtas mūsų pavadinimas atrodys taip:

Žodis | Žyma
------|-----
Trikuspidinio | B-DIS
vožtuvo | I-DIS
regurgitacija | I-DIS
ir | O
ličio | B-CHEM
karbonato | I-CHEM
toksikacija | B-DIS
naujagimiui | O
. | O

Kadangi reikia sukurti vienas su vienu atitikimą tarp žodžių ir klasių, galime treniruoti dešinėje esančią **daug į daug** neuroninio tinklo architektūrą iš šio paveikslėlio:

![Paveikslėlis, rodantis įprastas pasikartojančių neuroninių tinklų struktūras.](../../../../../translated_images/unreasonable-effectiveness-of-rnn.541ead816778f42dce6c42d8a56c184729aa2378d059b851be4ce12b993033df.lt.jpg)

> *Paveikslėlis iš [šio tinklaraščio įrašo](http://karpathy.github.io/2015/05/21/rnn-effectiveness/) autoriaus [Andrejaus Karpathy](http://karpathy.github.io/). NER žodžių klasifikavimo modeliai atitinka dešinėje esančią tinklo architektūrą.*

## NER modelių treniravimas

Kadangi NER modelis iš esmės yra žodžių klasifikavimo modelis, šiai užduočiai galime naudoti RNN, su kuriais jau esame susipažinę. Šiuo atveju kiekvienas pasikartojančio tinklo blokas grąžins žodžio ID. Šiame pavyzdiniame užrašų knygelėje parodyta, kaip treniruoti LSTM žodžių klasifikavimui.

## ✍️ Pavyzdiniai užrašų knygelės: NER

Tęskite mokymąsi naudodamiesi šia užrašų knygele:

* [NER su TensorFlow](NER-TF.ipynb)

## Išvada

NER modelis yra **žodžių klasifikavimo modelis**, kuris gali būti naudojamas žodžių klasifikavimui atlikti. Tai labai dažna NLP užduotis, padedanti atpažinti specifinius objektus tekste, įskaitant vietas, vardus, datas ir kt.

## 🚀 Iššūkis

Atlikite žemiau pateiktą užduotį, kad ištreniruotumėte medicininių terminų atpažinimo modelį, o tada išbandykite jį su kitu duomenų rinkiniu.

## [Po paskaitos: klausimynas](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/219)

## Peržiūra ir savarankiškas mokymasis

Perskaitykite tinklaraštį [Nepagrįstas pasikartojančių neuroninių tinklų efektyvumas](http://karpathy.github.io/2015/05/21/rnn-effectiveness/) ir sekite straipsnio skyrių „Papildomas skaitymas“, kad pagilintumėte savo žinias.

## [Užduotis](lab/README.md)

Šios pamokos užduotyje turėsite ištreniruoti medicininių objektų atpažinimo modelį. Galite pradėti nuo LSTM modelio treniravimo, kaip aprašyta šioje pamokoje, ir pereiti prie BERT transformatoriaus modelio naudojimo. Perskaitykite [instrukcijas](lab/README.md), kad sužinotumėte visas detales.

---

**Atsakomybės apribojimas**:  
Šis dokumentas buvo išverstas naudojant AI vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba turėtų būti laikomas autoritetingu šaltiniu. Kritinei informacijai rekomenduojama naudoti profesionalų žmogaus vertimą. Mes neprisiimame atsakomybės už nesusipratimus ar klaidingus interpretavimus, atsiradusius dėl šio vertimo naudojimo.