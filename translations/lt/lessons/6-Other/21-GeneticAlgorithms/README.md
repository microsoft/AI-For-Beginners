# Genetiniai algoritmai

## [Prieš paskaitos testą](https://ff-quizzes.netlify.app/en/ai/quiz/41)

**Genetiniai algoritmai** (GA) yra pagrįsti **evoliuciniu požiūriu** į dirbtinį intelektą, kuriame naudojami populiacijos evoliucijos metodai, siekiant rasti optimalią sprendimo būdą tam tikrai problemai. Jie buvo pasiūlyti 1975 m. [John Henry Holland](https://wikipedia.org/wiki/John_Henry_Holland).

Genetiniai algoritmai remiasi šiomis idėjomis:

* Galimi problemos sprendimai gali būti pateikti kaip **genai**
* **Kryžminimas** leidžia sujungti du sprendimus ir gauti naują galiojantį sprendimą
* **Atranka** naudojama optimalesnių sprendimų pasirinkimui pagal tam tikrą **tinkamumo funkciją**
* **Mutacijos** įvedamos siekiant destabilizuoti optimizaciją ir išvengti vietinio minimumo

Norint įgyvendinti genetinį algoritmą, reikia:

 * Rasti būdą, kaip koduoti problemos sprendimus naudojant **genus** g&in;&Gamma;
 * Genų rinkinyje &Gamma; apibrėžti **tinkamumo funkciją** fit: &Gamma;&rightarrow;**R**. Mažesnės funkcijos reikšmės atitinka geresnius sprendimus.
 * Apibrėžti **kryžminimo** mechanizmą, kad būtų galima sujungti du genus ir gauti naują galiojantį sprendimą crossover: &Gamma;<sup>2</sub>&rightarrow;&Gamma;.
 * Apibrėžti **mutacijos** mechanizmą mutate: &Gamma;&rightarrow;&Gamma;.

Daugeliu atvejų kryžminimas ir mutacija yra gana paprasti algoritmai, skirti manipuliuoti genais kaip skaitmeninėmis sekų ar bitų vektoriais.

Konkreti genetinio algoritmo įgyvendinimo forma gali skirtis priklausomai nuo atvejo, tačiau bendras struktūra yra tokia:

1. Pasirinkti pradinę populiaciją G&subset;&Gamma;
2. Atsitiktinai pasirinkti vieną iš operacijų, kurios bus atliekamos šiame žingsnyje: kryžminimas arba mutacija
3. **Kryžminimas**:
  * Atsitiktinai pasirinkti du genus g<sub>1</sub>, g<sub>2</sub> &in; G
  * Apskaičiuoti kryžminimą g=crossover(g<sub>1</sub>,g<sub>2</sub>)
  * Jei fit(g)<fit(g<sub>1</sub>) arba fit(g)<fit(g<sub>2</sub>) - pakeisti atitinkamą geną populiacijoje g.
4. **Mutacija** - pasirinkti atsitiktinį geną g&in;G ir pakeisti jį mutate(g)
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

Genetiniai algoritmai naudojami spręsti daugelį problemų, įskaitant logistikos ir paieškos problemas. Ši sritis įkvėpta tyrimų, kurie sujungė psichologijos ir kompiuterių mokslo temas.

## 🚀 Iššūkis

"Genetiniai algoritmai yra paprasti įgyvendinti, tačiau jų elgesį sunku suprasti." [šaltinis](https://wikipedia.org/wiki/Genetic_algorithm) Atlikite tyrimą, kad rastumėte genetinio algoritmo įgyvendinimą, pavyzdžiui, sprendžiant Sudoku galvosūkį, ir paaiškinkite, kaip jis veikia eskizu arba srauto diagrama.

## [Po paskaitos testą](https://ff-quizzes.netlify.app/en/ai/quiz/42)

## Apžvalga ir savarankiškas mokymasis

Žiūrėkite [šį puikų vaizdo įrašą](https://www.youtube.com/watch?v=qv6UVOQ0F44), kuriame kalbama apie tai, kaip kompiuteris gali išmokti žaisti Super Mario, naudojant neuroninius tinklus, treniruotus genetiniais algoritmais. Daugiau apie kompiuterio mokymąsi žaisti tokio tipo žaidimus sužinosime [kitame skyriuje](../22-DeepRL/README.md).

## [Užduotis: Diofantinė lygtis](Diophantine.ipynb)

Jūsų tikslas yra išspręsti vadinamąją **Diofantinę lygtį** - lygtį su sveikaisiais sprendiniais. Pavyzdžiui, apsvarstykite lygtį a+2b+3c+4d=30. Jums reikia rasti sveikuosius sprendinius, kurie atitinka šią lygtį.

*Ši užduotis įkvėpta [šio įrašo](https://habr.com/post/128704/).*

Patarimai:

1. Galite apsvarstyti sprendinius intervale [0;30]
1. Kaip geną, apsvarstykite šaknų reikšmių sąrašą

Naudokite [Diophantine.ipynb](Diophantine.ipynb) kaip pradinį tašką.

---

