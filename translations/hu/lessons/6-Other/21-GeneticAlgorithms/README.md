<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "893aa368cb485da704b466a0f3775587",
  "translation_date": "2025-08-25T23:17:44+00:00",
  "source_file": "lessons/6-Other/21-GeneticAlgorithms/README.md",
  "language_code": "hu"
}
-->
# Genetikus Algoritmusok

## [Előadás előtti kvíz](https://ff-quizzes.netlify.app/en/ai/quiz/41)

A **Genetikus Algoritmusok** (GA) egy **evolúciós megközelítésen** alapulnak a mesterséges intelligenciában, amely során egy populáció evolúciós módszereit használjuk egy adott probléma optimális megoldásának megtalálására. Az ötletet 1975-ben [John Henry Holland](https://wikipedia.org/wiki/John_Henry_Holland) javasolta.

A Genetikus Algoritmusok az alábbi alapelveken nyugszanak:

* A probléma érvényes megoldásai **génekként** reprezentálhatók
* A **keresztezés** lehetővé teszi, hogy két megoldást kombináljunk, és egy új, érvényes megoldást kapjunk
* A **szelekció** segítségével a **fitness függvény** alapján kiválasztjuk az optimálisabb megoldásokat
* **Mutációkat** vezetünk be, hogy destabilizáljuk az optimalizálást, és elkerüljük a lokális minimumokat

Ha Genetikus Algoritmust szeretnél megvalósítani, az alábbiakra van szükséged:

 * Meg kell találnod egy módszert, amellyel a probléma megoldásait **génekként** kódolhatod, g∈Γ
 * A Γ génhalmazon definiálnod kell egy **fitness függvényt**, fit: Γ→**R**. A kisebb függvényértékek jobb megoldásokat jelentenek.
 * Definiálnod kell egy **keresztezési** mechanizmust, amely két gént kombinálva új, érvényes megoldást ad crossover: Γ<sup>2</sub>→Γ.
 * Definiálnod kell egy **mutációs** mechanizmust mutate: Γ→Γ.

Sok esetben a keresztezés és a mutáció egyszerű algoritmusok, amelyek numerikus sorozatokkal vagy bitvektorokkal manipulálnak.

A genetikus algoritmus konkrét megvalósítása esetről esetre változhat, de az általános struktúra a következő:

1. Válassz egy kezdeti populációt G⊂Γ
2. Véletlenszerűen válaszd ki, hogy a következő lépésben melyik műveletet hajtod végre: keresztezés vagy mutáció
3. **Keresztezés**:
  * Véletlenszerűen válassz ki két gént g<sub>1</sub>, g<sub>2</sub> ∈ G
  * Számítsd ki a keresztezést g=crossover(g<sub>1</sub>,g<sub>2</sub>)
  * Ha fit(g)<fit(g<sub>1</sub>) vagy fit(g)<fit(g<sub>2</sub>), cseréld ki a populáció megfelelő génjét g-re.
4. **Mutáció** - válassz ki véletlenszerűen egy gént g∈G, és cseréld ki mutate(g)-re
5. Ismételd a 2. lépéstől, amíg el nem érünk egy elég kicsi fit értéket, vagy amíg el nem érjük a lépések maximális számát.

## Tipikus Feladatok

A Genetikus Algoritmusokkal általában az alábbi feladatokat oldják meg:

1. Ütemezés optimalizálása
1. Optimális csomagolás
1. Optimális vágás
1. Kimerítő keresés felgyorsítása

## ✍️ Gyakorlatok: Genetikus Algoritmusok

Folytasd a tanulást az alábbi jegyzetfüzetekben:

Nézd meg [ezt a jegyzetfüzetet](../../../../../lessons/6-Other/21-GeneticAlgorithms/Genetic.ipynb), amely két példát mutat be a Genetikus Algoritmusok használatára:

1. Kincs igazságos elosztása
1. 8 Királynő Probléma

## Összegzés

A Genetikus Algoritmusokat számos probléma megoldására használják, beleértve a logisztikai és keresési problémákat. A területet a pszichológia és a számítástechnika témáinak ötvözése inspirálta.

## 🚀 Kihívás

"A genetikus algoritmusok egyszerűen megvalósíthatók, de a viselkedésük nehezen érthető." [forrás](https://wikipedia.org/wiki/Genetic_algorithm) Kutass utána egy genetikus algoritmus megvalósításának, például egy Sudoku rejtvény megoldásának, és magyarázd el, hogyan működik, akár vázlatként, akár folyamatábraként.

## [Előadás utáni kvíz](https://ff-quizzes.netlify.app/en/ai/quiz/42)

## Áttekintés és Önálló Tanulás

Nézd meg [ezt a nagyszerű videót](https://www.youtube.com/watch?v=qv6UVOQ0F44), amely bemutatja, hogyan tanulhat meg egy számítógép Super Mario-t játszani genetikus algoritmusokkal tanított neurális hálózatok segítségével. A következő részben [többet tanulunk arról, hogyan tanulnak a számítógépek ilyen játékokat játszani](../22-DeepRL/README.md).

## [Feladat: Diofantikus Egyenlet](../../../../../lessons/6-Other/21-GeneticAlgorithms/Diophantine.ipynb)

A célod egy úgynevezett **Diofantikus egyenlet** megoldása - egy olyan egyenleté, amelynek egész számú gyökei vannak. Például, tekintsük az a+2b+3c+4d=30 egyenletet. Meg kell találnod azokat az egész számú gyököket, amelyek kielégítik ezt az egyenletet.

*Ezt a feladatot [ez az írás](https://habr.com/post/128704/) inspirálta.*

Tippek:

1. A gyököket tekintheted a [0;30] intervallumban
1. Génként használhatod a gyökértékek listáját

Használd a [Diophantine.ipynb](../../../../../lessons/6-Other/21-GeneticAlgorithms/Diophantine.ipynb) fájlt kiindulópontként.

**Felelősség kizárása**:  
Ez a dokumentum az AI fordítási szolgáltatás, a [Co-op Translator](https://github.com/Azure/co-op-translator) segítségével lett lefordítva. Bár törekszünk a pontosságra, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az eredeti nyelvén tekintendő hiteles forrásnak. Kritikus információk esetén javasolt professzionális emberi fordítást igénybe venni. Nem vállalunk felelősséget az ebből a fordításból eredő félreértésekért vagy téves értelmezésekért.