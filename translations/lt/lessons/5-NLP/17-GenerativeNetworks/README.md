# Generatyviniai tinklai

## [Klausimynas prieš paskaitą](https://ff-quizzes.netlify.app/en/ai/quiz/33)

Pasikartojančių neuroninių tinklų (RNN) ir jų vartų ląstelių variantų, tokių kaip ilgos trumpos atminties ląstelės (LSTM) ir vartų pasikartojančios vienetai (GRU), mechanizmas leidžia modeliuoti kalbą, nes jie gali išmokti žodžių tvarką ir numatyti kitą žodį sekoje. Tai leidžia naudoti RNN **generatyvinėms užduotims**, tokioms kaip paprastas teksto generavimas, mašininis vertimas ar net vaizdų aprašymas.

> ✅ Pagalvokite apie visas situacijas, kai pasinaudojote generatyvinėmis užduotimis, pavyzdžiui, teksto užbaigimu rašant. Pasidomėkite savo mėgstamomis programomis ir sužinokite, ar jos naudojo RNN.

RNN architektūroje, kurią aptarėme ankstesniame skyriuje, kiekvienas RNN vienetas generavo kitą paslėptą būseną kaip išvestį. Tačiau mes taip pat galime pridėti kitą išvestį prie kiekvieno pasikartojančio vieneto, kuris leistų generuoti **seką** (lygią pradinės sekos ilgiui). Be to, galime naudoti RNN vienetus, kurie kiekviename žingsnyje nepriima įvesties, o tiesiog naudoja pradinį būsenos vektorių ir generuoja išvesties seką.

Tai leidžia sukurti skirtingas neuronines architektūras, kurios parodytos žemiau esančiame paveikslėlyje:

![Paveikslėlis, rodantis įprastus pasikartojančių neuroninių tinklų modelius.](../../../../../translated_images/lt/unreasonable-effectiveness-of-rnn.541ead816778f42d.webp)

> Paveikslėlis iš tinklaraščio įrašo [Unreasonable Effectiveness of Recurrent Neural Networks](http://karpathy.github.io/2015/05/21/rnn-effectiveness/) autoriaus [Andrej Karpaty](http://karpathy.github.io/)

* **Vienas su vienu** yra tradicinis neuroninis tinklas su viena įvestimi ir viena išvestimi
* **Vienas su daugeliu** yra generatyvinė architektūra, kuri priima vieną įvesties reikšmę ir generuoja išvesties reikšmių seką. Pavyzdžiui, jei norime išmokyti tinklą **vaizdų aprašymui**, kuris generuotų tekstinį paveikslėlio aprašymą, galime naudoti paveikslėlį kaip įvestį, perduoti jį per CNN, kad gautume paslėptą būseną, o tada pasikartojanti grandinė generuotų aprašymą žodis po žodžio.
* **Daug su vienu** atitinka RNN architektūras, kurias aprašėme ankstesniame skyriuje, pavyzdžiui, teksto klasifikavimą.
* **Daug su daugeliu**, arba **seka į seką**, atitinka užduotis, tokias kaip **mašininis vertimas**, kur pirmasis RNN surenka visą informaciją iš įvesties sekos į paslėptą būseną, o kita RNN grandinė išskleidžia šią būseną į išvesties seką.

Šiame skyriuje mes sutelksime dėmesį į paprastus generatyvinius modelius, kurie padeda generuoti tekstą. Paprastumo dėlei naudosime simbolių lygio tokenizaciją.

Mes išmokysime šį RNN generuoti tekstą žingsnis po žingsnio. Kiekviename žingsnyje imsime simbolių seką, kurios ilgis yra `nchars`, ir paprašysime tinklo generuoti kitą išvesties simbolį kiekvienam įvesties simboliui:

![Paveikslėlis, rodantis RNN generavimo pavyzdį su žodžiu 'HELLO'.](../../../../../translated_images/lt/rnn-generate.56c54afb52f9781d.webp)

Generuojant tekstą (inference metu), pradedame nuo tam tikro **pradžios taško**, kuris perduodamas per RNN ląsteles, kad būtų generuojama tarpinė būsena, o tada iš šios būsenos prasideda generavimas. Generuojame po vieną simbolį, perduodame būseną ir sugeneruotą simbolį kitai RNN ląstelei, kad sugeneruotume kitą, kol sugeneruojame pakankamai simbolių.

<img src="../../../../../translated_images/lt/rnn-generate-inf.5168dc65e0370eea.webp" width="60%"/>

> Paveikslėlis autoriaus

## ✍️ Pratimai: Generatyviniai tinklai

Tęskite mokymąsi šiuose užrašuose:

* [Generatyviniai tinklai su PyTorch](GenerativePyTorch.ipynb)
* [Generatyviniai tinklai su TensorFlow](GenerativeTF.ipynb)

## Minkštas teksto generavimas ir temperatūra

Kiekvienos RNN ląstelės išvestis yra simbolių tikimybių pasiskirstymas. Jei visada pasirinksime simbolį su didžiausia tikimybe kaip kitą simbolį generuojamame tekste, tekstas dažnai gali "užstrigti" tarp tų pačių simbolių sekų, kaip šiame pavyzdyje:

```
today of the second the company and a second the company ...
```

Tačiau, jei pažvelgsime į tikimybių pasiskirstymą kitam simboliui, gali būti, kad kelių didžiausių tikimybių skirtumas nėra didelis, pvz., vienas simbolis gali turėti tikimybę 0.2, o kitas - 0.19 ir pan. Pavyzdžiui, ieškant kito simbolio sekoje '*play*', kitas simbolis gali būti tiek tarpas, tiek **e** (kaip žodyje *player*).

Tai veda prie išvados, kad ne visada "teisinga" pasirinkti simbolį su didžiausia tikimybe, nes pasirinkus antrą pagal dydį vis tiek galime gauti prasmingą tekstą. Protingiau yra **imti mėginius** iš tikimybių pasiskirstymo, kurį pateikia tinklo išvestis. Taip pat galime naudoti parametrą **temperatūra**, kuris išlygins tikimybių pasiskirstymą, jei norime pridėti daugiau atsitiktinumo, arba padaryti jį statesnį, jei norime labiau laikytis didžiausios tikimybės simbolių.

Išbandykite, kaip šis minkštas teksto generavimas įgyvendinamas aukščiau pateiktuose užrašuose.

## Išvada

Nors teksto generavimas gali būti naudingas pats savaime, pagrindiniai privalumai atsiranda iš galimybės generuoti tekstą naudojant RNN iš tam tikro pradinio funkcijų vektoriaus. Pavyzdžiui, teksto generavimas naudojamas kaip mašininio vertimo dalis (seka į seką, šiuo atveju būsenos vektorius iš *encoder* naudojamas generuoti arba *decode* išverstą pranešimą) arba generuojant tekstinį vaizdo aprašymą (šiuo atveju funkcijų vektorius būtų gaunamas iš CNN ekstraktoriaus).

## 🚀 Iššūkis

Pasimokykite apie šią temą Microsoft Learn platformoje:

* Teksto generavimas su [PyTorch](https://docs.microsoft.com/learn/modules/intro-natural-language-processing-pytorch/6-generative-networks/?WT.mc_id=academic-77998-cacaste)/[TensorFlow](https://docs.microsoft.com/learn/modules/intro-natural-language-processing-tensorflow/5-generative-networks/?WT.mc_id=academic-77998-cacaste)

## [Klausimynas po paskaitos](https://ff-quizzes.netlify.app/en/ai/quiz/34)

## Apžvalga ir savarankiškas mokymasis

Štai keletas straipsnių, kurie padės praplėsti žinias:

* Skirtingi teksto generavimo metodai naudojant Markovo grandinę, LSTM ir GPT-2: [tinklaraščio įrašas](https://towardsdatascience.com/text-generation-gpt-2-lstm-markov-chain-9ea371820e1e)
* Teksto generavimo pavyzdys [Keras dokumentacijoje](https://keras.io/examples/generative/lstm_character_level_text_generation/)

## [Užduotis](lab/README.md)

Mes matėme, kaip generuoti tekstą simbolis po simbolio. Laboratorijoje tyrinėsite teksto generavimą žodžių lygiu.

---

