<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4522e22e150be0845e03aa41209a39d5",
  "translation_date": "2025-08-31T18:02:10+00:00",
  "source_file": "lessons/5-NLP/13-TextRep/README.md",
  "language_code": "lt"
}
-->
# Teksto atvaizdavimas kaip tensoriai

## [Prieš paskaitos testas](https://ff-quizzes.netlify.app/en/ai/quiz/25)

## Teksto klasifikavimas

Pirmoje šios dalies dalyje mes sutelksime dėmesį į **teksto klasifikavimo** užduotį. Naudosime [AG News](https://www.kaggle.com/amananandrai/ag-news-classification-dataset) duomenų rinkinį, kuriame yra naujienų straipsniai, pavyzdžiui:

* Kategorija: Mokslas/Technologijos  
* Pavadinimas: Ky. Įmonė laimi dotaciją peptidų tyrimams (AP)  
* Turinys: AP - Įmonė, įkurta chemijos tyrėjo iš Luisvilio universiteto, laimėjo dotaciją, skirtą plėtrai...

Mūsų tikslas bus klasifikuoti naujienų straipsnį į vieną iš kategorijų pagal tekstą.

## Teksto atvaizdavimas

Jei norime spręsti natūralios kalbos apdorojimo (NLP) užduotis naudojant neuroninius tinklus, mums reikia būdo, kaip tekstą paversti tensoriais. Kompiuteriai jau atvaizduoja tekstinius simbolius kaip skaičius, kurie atitinka šriftus jūsų ekrane, naudodami tokius kodavimus kaip ASCII ar UTF-8.

<img alt="Vaizdas, rodantis simbolio atvaizdavimą ASCII ir dvejetainiu formatu" src="images/ascii-character-map.png" width="50%"/>

> [Vaizdo šaltinis](https://www.seobility.net/en/wiki/ASCII)

Kaip žmonės, mes suprantame, ką kiekviena raidė **reiškia**, ir kaip visi simboliai susijungia į žodžius sakinyje. Tačiau kompiuteriai patys savaime tokio supratimo neturi, o neuroninis tinklas turi išmokti reikšmę mokymo metu.

Todėl galime naudoti skirtingus požiūrius, kai atvaizduojame tekstą:

* **Simbolių lygmens atvaizdavimas**, kai tekstą atvaizduojame, kiekvieną simbolį traktuodami kaip skaičių. Jei turime *C* skirtingų simbolių savo teksto korpuse, žodis *Hello* būtų atvaizduotas kaip 5x*C* tensorius. Kiekviena raidė atitiktų tensoriaus stulpelį vieno karšto kodavimo (one-hot encoding) formatu.  
* **Žodžių lygmens atvaizdavimas**, kai sukuriame visų žodžių **žodyną** ir tada žodžius atvaizduojame naudojant vieno karšto kodavimą. Šis požiūris yra šiek tiek geresnis, nes kiekviena raidė pati savaime neturi daug reikšmės, todėl naudojant aukštesnio lygio semantines sąvokas – žodžius – supaprastiname užduotį neuroniniam tinklui. Tačiau dėl didelio žodyno dydžio turime susidoroti su didelės dimensijos retiniais tensoriais.

Nepriklausomai nuo atvaizdavimo, pirmiausia turime tekstą paversti **ženklais** (tokenais), kur vienas ženklas gali būti simbolis, žodis ar net žodžio dalis. Tada ženklą paverčiame skaičiumi, paprastai naudodami **žodyną**, ir šis skaičius gali būti perduotas į neuroninį tinklą naudojant vieno karšto kodavimą.

## N-Gramai

Natūralioje kalboje tiksli žodžių reikšmė gali būti nustatyta tik kontekste. Pavyzdžiui, *neuroninis tinklas* ir *žvejybinis tinklas* turi visiškai skirtingas reikšmes. Vienas iš būdų tai įvertinti yra kurti modelį, pagrįstą žodžių poromis, ir traktuoti žodžių poras kaip atskirus žodyno ženklus. Tokiu būdu sakinys *Man patinka eiti žvejoti* bus atvaizduotas tokia ženklų seka: *Man patinka*, *patinka eiti*, *eiti žvejoti*. Problema su šiuo požiūriu yra ta, kad žodyno dydis žymiai padidėja, o tokios kombinacijos kaip *eiti žvejoti* ir *eiti apsipirkti* yra pateikiamos kaip skirtingi ženklai, kurie neturi jokio semantinio panašumo, nepaisant to paties veiksmažodžio.

Kai kuriais atvejais galime apsvarstyti tri-gramų – trijų žodžių kombinacijų – naudojimą. Todėl šis požiūris dažnai vadinamas **n-gramais**. Taip pat prasminga naudoti n-gramus su simbolių lygmens atvaizdavimu, tokiu atveju n-gramai apytiksliai atitiks skirtingus skiemenis.

## Žodžių maišas (Bag-of-Words) ir TF/IDF

Sprendžiant tokias užduotis kaip teksto klasifikavimas, mums reikia galimybės atvaizduoti tekstą kaip vieną fiksuoto dydžio vektorių, kurį naudosime kaip įvestį galutiniam tankiam klasifikatoriui. Vienas paprasčiausių būdų tai padaryti yra sujungti visas atskiras žodžių reprezentacijas, pvz., jas sudedant. Jei sudėsime kiekvieno žodžio vieno karšto kodavimus, gausime dažnių vektorių, rodantį, kiek kartų kiekvienas žodis pasirodo tekste. Toks teksto atvaizdavimas vadinamas **žodžių maišu** (BoW).

<img src="images/bow.png" width="90%"/>

> Vaizdas sukurtas autoriaus

BoW iš esmės parodo, kurie žodžiai pasirodo tekste ir kokiais kiekiais, o tai gali būti geras rodiklis, apie ką yra tekstas. Pavyzdžiui, naujienų straipsnis apie politiką greičiausiai turės tokius žodžius kaip *prezidentas* ir *šalis*, o mokslinis straipsnis – tokius kaip *kolideris*, *atrasta* ir pan. Taigi, žodžių dažniai daugeliu atvejų gali būti geras teksto turinio rodiklis.

Problema su BoW yra ta, kad tam tikri dažni žodžiai, tokie kaip *ir*, *yra* ir pan., pasirodo daugumoje tekstų ir turi didžiausius dažnius, užgoždami tikrai svarbius žodžius. Mes galime sumažinti šių žodžių svarbą, atsižvelgdami į dažnį, kuriuo žodžiai pasirodo visoje dokumentų kolekcijoje. Tai yra pagrindinė TF/IDF metodo idėja, kuri išsamiau aptariama šios pamokos pridedamuose užrašuose.

Tačiau nė vienas iš šių metodų negali visiškai įvertinti teksto **semantikos**. Tam mums reikia galingesnių neuroninių tinklų modelių, kuriuos aptarsime vėliau šioje dalyje.

## ✍️ Pratimai: Teksto atvaizdavimas

Tęskite mokymąsi šiuose užrašuose:

* [Teksto atvaizdavimas su PyTorch](TextRepresentationPyTorch.ipynb)  
* [Teksto atvaizdavimas su TensorFlow](TextRepresentationTF.ipynb)  

## Išvada

Iki šiol išnagrinėjome metodus, kurie gali pridėti dažnio svorį skirtingiems žodžiams. Tačiau jie negali atvaizduoti reikšmės ar tvarkos. Kaip garsus lingvistas J. R. Firth pasakė 1935 m., „Visapusiška žodžio reikšmė visada yra kontekstinė, ir joks reikšmės tyrimas, atskirtas nuo konteksto, negali būti laikomas rimtu.“ Vėliau kurse sužinosime, kaip iš teksto išgauti kontekstinę informaciją naudojant kalbos modeliavimą.

## 🚀 Iššūkis

Išbandykite kitus pratimus, naudodami žodžių maišą ir skirtingus duomenų modelius. Jus gali įkvėpti šis [Kaggle konkursas](https://www.kaggle.com/competitions/word2vec-nlp-tutorial/overview/part-1-for-beginners-bag-of-words).

## [Po paskaitos testas](https://ff-quizzes.netlify.app/en/ai/quiz/26)

## Peržiūra ir savarankiškas mokymasis

Praktikuokite savo įgūdžius su teksto įterpimais ir žodžių maišo technikomis [Microsoft Learn](https://docs.microsoft.com/learn/modules/intro-natural-language-processing-pytorch/?WT.mc_id=academic-77998-cacaste).

## [Užduotis: Užrašai](assignment.md)

---

**Atsakomybės apribojimas**:  
Šis dokumentas buvo išverstas naudojant AI vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba turėtų būti laikomas autoritetingu šaltiniu. Kritinei informacijai rekomenduojama naudoti profesionalų žmogaus vertimą. Mes neprisiimame atsakomybės už nesusipratimus ar klaidingus interpretavimus, atsiradusius dėl šio vertimo naudojimo.