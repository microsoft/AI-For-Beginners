# Genetikus Algoritmusok

## [Előadás előtti kvíz](https://ff-quizzes.netlify.app/en/ai/quiz/41)

A **Genetikus Algoritmusok** (GA) az AI egy **evolúciós megközelítésén** alapulnak, amelyben egy populáció evolúciós módszereit használjuk egy adott probléma optimális megoldásának megtalálására. Az algoritmusokat 1975-ben [John Henry Holland](https://wikipedia.org/wiki/John_Henry_Holland) javasolta.

A Genetikus Algoritmusok az alábbi ötleteken alapulnak:

* A probléma érvényes megoldásai **génekként** reprezentálhatók
* A **keresztezés** lehetővé teszi két megoldás kombinálását, hogy új érvényes megoldást kapjunk
* A **szelekció** segítségével a **fitness függvény** alapján kiválaszthatjuk az optimálisabb megoldásokat
* **Mutációkat** vezetünk be, hogy destabilizáljuk az optimalizálást és elkerüljük a lokális minimumot

Ha Genetikus Algoritmust szeretnél implementálni, az alábbiakra van szükséged:

 * Meg kell találnod egy módszert, amellyel a probléma megoldásait **génekként** kódolhatod g&in;&Gamma;
 * A gének halmazán &Gamma; definiálnod kell egy **fitness függvényt** fit: &Gamma;&rightarrow;**R**. A kisebb függvényértékek jobb megoldásokat jelentenek.
 * Definiálnod kell egy **keresztezési** mechanizmust, amely két gént kombinálva új érvényes megoldást hoz létre crossover: &Gamma;<sup>2</sub>&rightarrow;&Gamma;.
 * Definiálnod kell egy **mutációs** mechanizmust mutate: &Gamma;&rightarrow;&Gamma;.

Sok esetben a keresztezés és a mutáció egyszerű algoritmusok, amelyek numerikus sorozatokkal vagy bitvektorokkal manipulálnak.

A genetikus algoritmus konkrét implementációja esetről esetre változhat, de az általános struktúra a következő:

1. Válassz egy kezdeti populációt G&subset;&Gamma;
2. Véletlenszerűen válassz egy műveletet, amelyet ebben a lépésben végrehajtasz: keresztezés vagy mutáció
3. **Keresztezés**:
  * Véletlenszerűen válassz két gént g<sub>1</sub>, g<sub>2</sub> &in; G
  * Számítsd ki a keresztezést g=crossover(g<sub>1</sub>,g<sub>2</sub>)
  * Ha fit(g)<fit(g<sub>1</sub>) vagy fit(g)<fit(g<sub>2</sub>) - cseréld ki a megfelelő gént a populációban g-re.
4. **Mutáció** - válassz véletlenszerűen egy gént g&in;G és cseréld ki mutate(g)-re
5. Ismételd a 2. lépéstől, amíg el nem érünk egy elég kicsi fit értéket, vagy amíg el nem érjük a lépések számának korlátját.

## Tipikus Feladatok

A Genetikus Algoritmusokkal általában megoldott feladatok:

1. Ütemezés optimalizálása
1. Optimális csomagolás
1. Optimális vágás
1. Kimerítő keresés felgyorsítása

## ✍️ Gyakorlatok: Genetikus Algoritmusok

Folytasd a tanulást az alábbi jegyzetfüzetekben:

Látogass el [ebbe a jegyzetfüzetbe](Genetic.ipynb), hogy két példát láss a Genetikus Algoritmusok használatára:

1. Kincsek igazságos elosztása
1. 8 Királynő probléma

## Összegzés

A Genetikus Algoritmusokat számos probléma megoldására használják, beleértve a logisztikai és keresési problémákat. A területet a Pszichológia és Számítástechnika témáinak összeolvadása ihlette.

## 🚀 Kihívás

"A genetikus algoritmusok egyszerűen implementálhatók, de viselkedésük nehezen érthető." [forrás](https://wikipedia.org/wiki/Genetic_algorithm) Kutass utána egy genetikus algoritmus implementációjának, például egy Sudoku rejtvény megoldásának, és magyarázd el, hogyan működik vázlat vagy folyamatábra formájában.

## [Előadás utáni kvíz](https://ff-quizzes.netlify.app/en/ai/quiz/42)

## Áttekintés és Önálló Tanulás

Nézd meg [ezt a remek videót](https://www.youtube.com/watch?v=qv6UVOQ0F44), amely arról szól, hogyan tanulhatnak a számítógépek Super Mario-t játszani genetikus algoritmusokkal tanított neurális hálózatok segítségével. A következő szekcióban [többet fogunk tanulni](../22-DeepRL/README.md) az ilyen típusú játékok tanulásáról.

## [Feladat: Diofantoszi Egyenlet](Diophantine.ipynb)

A célod az úgynevezett **Diofantoszi egyenlet** megoldása - egy egyenlet, amelynek egész számú gyökei vannak. Például, tekintsük az a+2b+3c+4d=30 egyenletet. Meg kell találnod azokat az egész számú gyököket, amelyek kielégítik ezt az egyenletet.

*Ezt a feladatot [ez a bejegyzés](https://habr.com/post/128704/) ihlette.*

Tippek:

1. Tekintsd a gyököket a [0;30] intervallumban
1. Génként használj egy listát a gyökértékekről

Használd [Diophantine.ipynb](Diophantine.ipynb) kiindulópontként.

---

