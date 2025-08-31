<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "58bf4adb210aab53e8f78c8082040e7c",
  "translation_date": "2025-08-31T18:00:07+00:00",
  "source_file": "lessons/5-NLP/16-RNN/README.md",
  "language_code": "lt"
}
-->
# Rekurentiniai neuroniniai tinklai

## [Prieš paskaitą: testas](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/116)

Ankstesnėse dalyse naudojome turtingas semantines tekstų reprezentacijas ir paprastą linijinį klasifikatorių virš įterpimų. Ši architektūra padeda užfiksuoti bendrą žodžių prasmę sakinyje, tačiau ji neatsižvelgia į žodžių **tvarką**, nes įterpimų agregavimo operacija pašalina šią informaciją iš originalaus teksto. Kadangi šie modeliai negali modeliuoti žodžių tvarkos, jie negali spręsti sudėtingesnių ar dviprasmiškų užduočių, tokių kaip teksto generavimas ar klausimų atsakymas.

Norėdami užfiksuoti teksto sekos prasmę, turime naudoti kitą neuroninių tinklų architektūrą, vadinamą **rekurentiniais neuroniniais tinklais** arba RNN. RNN tinklu sakinį perduodame po vieną simbolį, o tinklas generuoja tam tikrą **būseną**, kurią vėliau perduodame tinklui kartu su kitu simboliu.

![RNN](../../../../../translated_images/rnn.27f5c29c53d727b546ad3961637a267f0fe9ec5ab01f2a26a853c92fcefbb574.lt.png)

> Vaizdas sukurtas autoriaus

Turint įvesties seką X<sub>0</sub>,...,X<sub>n</sub>, RNN sukuria neuroninių tinklų blokų seką ir treniruoja šią seką nuo pradžios iki pabaigos naudojant atgalinę sklaidą. Kiekvienas tinklo blokas kaip įvestį gauna porą (X<sub>i</sub>,S<sub>i</sub>) ir generuoja S<sub>i+1</sub> kaip rezultatą. Galutinė būsena S<sub>n</sub> arba (išvestis Y<sub>n</sub>) perduodama linijiniam klasifikatoriui, kad būtų gautas rezultatas. Visi tinklo blokai dalijasi tais pačiais svoriais ir yra treniruojami nuo pradžios iki pabaigos per vieną atgalinės sklaidos ciklą.

Kadangi būsenos vektoriai S<sub>0</sub>,...,S<sub>n</sub> perduodami per tinklą, jis gali išmokti sekos priklausomybes tarp žodžių. Pavyzdžiui, kai žodis *ne* pasirodo kažkur sekoje, tinklas gali išmokti paneigti tam tikrus būsenos vektoriaus elementus, sukeldamas neigimą.

> ✅ Kadangi visų RNN blokų svoriai aukščiau pateiktame paveikslėlyje yra bendri, tas pats paveikslėlis gali būti pavaizduotas kaip vienas blokas (dešinėje) su rekurentine grįžtamojo ryšio kilpa, kuri perduoda tinklo išvesties būseną atgal į įvestį.

## RNN ląstelės anatomija

Pažvelkime, kaip organizuota paprasta RNN ląstelė. Ji priima ankstesnę būseną S<sub>i-1</sub> ir dabartinį simbolį X<sub>i</sub> kaip įvestis ir turi generuoti išvesties būseną S<sub>i</sub> (kartais mus taip pat domina kita išvestis Y<sub>i</sub>, kaip generatyviniuose tinkluose).

Paprasta RNN ląstelė turi du svorio matricas viduje: viena transformuoja įvesties simbolį (vadinkime ją W), o kita transformuoja įvesties būseną (H). Tokiu atveju tinklo išvestis apskaičiuojama kaip σ(W×X<sub>i</sub>+H×S<sub>i-1</sub>+b), kur σ yra aktyvacijos funkcija, o b yra papildomas poslinkis.

<img alt="RNN ląstelės anatomija" src="images/rnn-anatomy.png" width="50%"/>

> Vaizdas sukurtas autoriaus

Daugeliu atvejų įvesties simboliai prieš patekdami į RNN perduodami per įterpimo sluoksnį, kad sumažėtų dimensija. Tokiu atveju, jei įvesties vektorių dimensija yra *emb_size*, o būsenos vektorius yra *hid_size*, W dydis yra *emb_size*×*hid_size*, o H dydis yra *hid_size*×*hid_size*.

## Ilgalaikė trumpalaikė atmintis (LSTM)

Viena pagrindinių klasikinių RNN problemų yra vadinamoji **nykstančių gradientų** problema. Kadangi RNN treniruojami nuo pradžios iki pabaigos per vieną atgalinės sklaidos ciklą, jiems sunku perduoti klaidą į pirmuosius tinklo sluoksnius, todėl tinklas negali išmokti ryšių tarp tolimų simbolių. Vienas iš būdų išvengti šios problemos yra įvesti **aiškų būsenos valdymą** naudojant vadinamuosius **vartus**. Yra dvi gerai žinomos tokios architektūros: **ilgalaikė trumpalaikė atmintis** (LSTM) ir **vartų relės vienetas** (GRU).

![Vaizdas, rodantis ilgalaikės trumpalaikės atminties ląstelės pavyzdį](../../../../../lessons/5-NLP/16-RNN/images/long-short-term-memory-cell.svg)

> Vaizdo šaltinis TBD

LSTM tinklas organizuotas panašiai kaip RNN, tačiau yra dvi būsenos, kurios perduodamos iš sluoksnio į sluoksnį: faktinė būsena C ir paslėptas vektorius H. Kiekviename vienete paslėptas vektorius H<sub>i</sub> sujungiamas su įvestimi X<sub>i</sub>, ir jie kontroliuoja, kas vyksta su būsena C per **vartus**. Kiekvienas vartas yra neuroninis tinklas su sigmoidine aktyvacija (išvestis diapazone [0,1]), kuris gali būti laikomas bitų kauke, kai dauginamas iš būsenos vektoriaus. Yra šie vartai (iš kairės į dešinę paveikslėlyje aukščiau):

* **Užmaršumo vartai** priima paslėptą vektorių ir nustato, kuriuos vektoriaus C komponentus reikia pamiršti, o kuriuos perduoti.
* **Įvesties vartai** paima tam tikrą informaciją iš įvesties ir paslėptų vektorių ir įterpia ją į būseną.
* **Išvesties vartai** transformuoja būseną per linijinį sluoksnį su *tanh* aktyvacija, tada pasirenka kai kuriuos jos komponentus naudodami paslėptą vektorių H<sub>i</sub>, kad generuotų naują būseną C<sub>i+1</sub>.

Būsenos C komponentai gali būti laikomi tam tikrais ženklais, kuriuos galima įjungti ir išjungti. Pavyzdžiui, kai sekoje sutinkame vardą *Alisa*, galime manyti, kad jis nurodo moterišką veikėją, ir pakelti ženklą būsenoje, kad sakinyje turime moterišką daiktavardį. Kai toliau sutinkame frazę *ir Tomas*, pakelsime ženklą, kad turime daugiskaitinį daiktavardį. Taigi manipuliuodami būsena galime sekti sakinio dalių gramatines savybes.

> ✅ Puikus šaltinis, padedantis suprasti LSTM vidinę struktūrą, yra šis puikus straipsnis [Understanding LSTM Networks](https://colah.github.io/posts/2015-08-Understanding-LSTMs/) Christopher Olah.

## Dvikrypčiai ir daugiasluoksniai RNN

Aptarėme rekurentinius tinklus, kurie veikia viena kryptimi, nuo sekos pradžios iki pabaigos. Tai atrodo natūralu, nes primena, kaip skaitome ir klausome kalbos. Tačiau, kadangi daugeliu praktinių atvejų turime atsitiktinę prieigą prie įvesties sekos, gali būti prasminga vykdyti rekursinį skaičiavimą abiem kryptimis. Tokie tinklai vadinami **dvikrypčiais** RNN. Dirbant su dvikrypčiu tinklu, mums reikės dviejų paslėptų būsenos vektorių, po vieną kiekvienai krypčiai.

Rekurentinis tinklas, nesvarbu, ar vienkryptis, ar dvikryptis, užfiksuoja tam tikrus sekos modelius ir gali juos saugoti būsenos vektoriuje arba perduoti į išvestį. Kaip ir konvoliuciniuose tinkluose, galime sukurti kitą rekursinį sluoksnį virš pirmojo, kad užfiksuotume aukštesnio lygio modelius ir sukurtume iš žemo lygio modelių, kuriuos ištraukė pirmasis sluoksnis. Tai veda mus prie **daugiasluoksnio RNN** sąvokos, kurią sudaro du ar daugiau rekursinių tinklų, kur ankstesnio sluoksnio išvestis perduodama kitam sluoksniui kaip įvestis.

![Vaizdas, rodantis daugiasluoksnį ilgalaikės trumpalaikės atminties RNN](../../../../../translated_images/multi-layer-lstm.dd975e29bb2a59fe58b429db833932d734c81f211cad2783797a9608984acb8c.lt.jpg)

*Paveikslas iš [šio nuostabaus įrašo](https://towardsdatascience.com/from-a-lstm-cell-to-a-multilayer-lstm-network-with-pytorch-2899eb5696f3) Fernando López*

## ✍️ Pratimai: Įterpimai

Tęskite mokymąsi šiuose užrašų knygelėse:

* [RNN su PyTorch](RNNPyTorch.ipynb)
* [RNN su TensorFlow](RNNTF.ipynb)

## Išvada

Šiame skyriuje matėme, kad RNN gali būti naudojami sekų klasifikavimui, tačiau iš tiesų jie gali atlikti daug daugiau užduočių, tokių kaip teksto generavimas, mašininis vertimas ir kt. Šias užduotis aptarsime kitame skyriuje.

## 🚀 Iššūkis

Perskaitykite literatūrą apie LSTM ir apsvarstykite jų taikymą:

- [Grid Long Short-Term Memory](https://arxiv.org/pdf/1507.01526v1.pdf)
- [Show, Attend and Tell: Neural Image Caption
Generation with Visual Attention](https://arxiv.org/pdf/1502.03044v2.pdf)

## [Po paskaitos: testas](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/216)

## Apžvalga ir savarankiškas mokymasis

- [Understanding LSTM Networks](https://colah.github.io/posts/2015-08-Understanding-LSTMs/) Christopher Olah.

## [Užduotis: Užrašų knygelės](assignment.md)

---

**Atsakomybės apribojimas**:  
Šis dokumentas buvo išverstas naudojant AI vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba turėtų būti laikomas autoritetingu šaltiniu. Kritinei informacijai rekomenduojama naudoti profesionalų žmogaus vertimą. Mes neprisiimame atsakomybės už nesusipratimus ar klaidingus interpretavimus, atsiradusius dėl šio vertimo naudojimo.