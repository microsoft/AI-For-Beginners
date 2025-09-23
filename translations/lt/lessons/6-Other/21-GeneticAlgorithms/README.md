<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "893aa368cb485da704b466a0f3775587",
  "translation_date": "2025-08-31T17:30:44+00:00",
  "source_file": "lessons/6-Other/21-GeneticAlgorithms/README.md",
  "language_code": "lt"
}
-->
# Genetiniai algoritmai

## [Klausimynas prieš paskaitą](https://ff-quizzes.netlify.app/en/ai/quiz/41)

**Genetiniai algoritmai** (GA) yra pagrįsti **evoliuciniu požiūriu** į dirbtinį intelektą, kuriame naudojami populiacijos evoliucijos metodai, siekiant rasti optimalią sprendimo problemą. Jie buvo pasiūlyti 1975 m. [John Henry Holland](https://wikipedia.org/wiki/John_Henry_Holland).

Genetiniai algoritmai remiasi šiomis idėjomis:

* Galimi problemos sprendimai gali būti pateikti kaip **genai**
* **Kryžminimas** leidžia sujungti du sprendimus ir gauti naują galiojantį sprendimą
* **Atranka** naudojama optimalesnių sprendimų pasirinkimui pagal tam tikrą **tinkamumo funkciją**
* **Mutacijos** įvedamos siekiant destabilizuoti optimizaciją ir išvengti vietinio minimumo

Jei norite įgyvendinti genetinį algoritmą, jums reikės:

* Rasti būdą, kaip užkoduoti problemos sprendimus naudojant **genus** g∈Γ
* Genų rinkinyje Γ apibrėžti **tinkamumo funkciją** fit: Γ→**R**. Mažesnės funkcijos reikšmės atitinka geresnius sprendimus.
* Apibrėžti **kryžminimo** mechanizmą, kad būtų galima sujungti du genus ir gauti naują galiojantį sprendimą crossover: Γ<sup>2</sub>→Γ.
* Apibrėžti **mutacijos** mechanizmą mutate: Γ→Γ.

Daugeliu atvejų kryžminimas ir mutacija yra gana paprasti algoritmai, skirti manipuliuoti genais kaip skaitmeninėmis sekų ar bitų vektoriais.

Konkreti genetinio algoritmo įgyvendinimo forma gali skirtis priklausomai nuo atvejo, tačiau bendras struktūra yra tokia:

1. Pasirinkti pradinę populiaciją G⊂Γ
2. Atsitiktinai pasirinkti vieną iš operacijų, kurios bus atliekamos šiame žingsnyje: kryžminimas arba mutacija
3. **Kryžminimas**:
   * Atsitiktinai pasirinkti du genus g<sub>1</sub>, g<sub>2</sub> ∈ G
   * Apskaičiuoti kryžminimą g=crossover(g<sub>1</sub>,g<sub>2</sub>)
   * Jei fit(g)<fit(g<sub>1</sub>) arba fit(g)<fit(g<sub>2</sub>) - pakeisti atitinkamą geną populiacijoje g.
4. **Mutacija** - pasirinkti atsitiktinį geną g∈G ir pakeisti jį mutate(g)
5. Kartoti nuo 2 žingsnio, kol pasieksime pakankamai mažą fit reikšmę arba kol bus pasiektas žingsnių limitas.

## Tipinės užduotys

Užduotys, kurias dažniausiai sprendžia genetiniai algoritmai, apima:

1. Tvarkaraščių optimizavimas
1. Optimalus pakavimas
1. Optimalus pjovimas
1. Išsamios paieškos pagreitinimas

## ✍️ Pratimai: Genetiniai algoritmai

Tęskite mokymąsi šiuose užrašuose:

Eikite į [šį užrašą](Genetic.ipynb), kad pamatytumėte du genetinių algoritmų naudojimo pavyzdžius:

1. Teisingas lobio padalijimas
1. 8 karalienių problema

## Išvada

Genetiniai algoritmai naudojami spręsti daugelį problemų, įskaitant logistikos ir paieškos problemas. Ši sritis įkvėpta tyrimų, kurie sujungė psichologijos ir informatikos temas.

## 🚀 Iššūkis

"Genetiniai algoritmai yra paprasti įgyvendinti, tačiau jų elgesį sunku suprasti." [šaltinis](https://wikipedia.org/wiki/Genetic_algorithm) Atlikite tyrimą, kad rastumėte genetinio algoritmo įgyvendinimą, pavyzdžiui, sprendžiant Sudoku galvosūkį, ir paaiškinkite, kaip jis veikia eskizu arba srauto schema.

## [Klausimynas po paskaitos](https://ff-quizzes.netlify.app/en/ai/quiz/42)

## Apžvalga ir savarankiškas mokymasis

Žiūrėkite [šį puikų vaizdo įrašą](https://www.youtube.com/watch?v=qv6UVOQ0F44), kuriame pasakojama, kaip kompiuteris gali išmokti žaisti Super Mario naudojant neuroninius tinklus, apmokytus genetiniais algoritmais. Daugiau apie kompiuterio mokymąsi žaisti tokio tipo žaidimus sužinosime [kitame skyriuje](../22-DeepRL/README.md).

## [Užduotis: Diofantinė lygtis](Diophantine.ipynb)

Jūsų tikslas yra išspręsti vadinamąją **Diofantinę lygtį** - lygtį su sveikaisiais šaknimis. Pavyzdžiui, apsvarstykite lygtį a+2b+3c+4d=30. Jums reikia rasti sveikąsias šaknis, kurios atitinka šią lygtį.

*Ši užduotis įkvėpta [šio įrašo](https://habr.com/post/128704/).*

Patarimai:

1. Galite apsvarstyti šaknis intervale [0;30]
1. Kaip geną, apsvarstykite šaknų reikšmių sąrašą

Naudokite [Diophantine.ipynb](Diophantine.ipynb) kaip pradinį tašką.

---

**Atsakomybės apribojimas**:  
Šis dokumentas buvo išverstas naudojant AI vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba turėtų būti laikomas autoritetingu šaltiniu. Kritinei informacijai rekomenduojama profesionali žmogaus vertimo paslauga. Mes neprisiimame atsakomybės už nesusipratimus ar klaidingus interpretavimus, atsiradusius naudojant šį vertimą.