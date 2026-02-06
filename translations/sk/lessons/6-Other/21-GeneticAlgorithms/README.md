# Genetické algoritmy

## [Kvíz pred prednáškou](https://ff-quizzes.netlify.app/en/ai/quiz/41)

**Genetické algoritmy** (GA) sú založené na **evolučnom prístupe** k umelej inteligencii, kde sa využívajú metódy evolúcie populácie na získanie optimálneho riešenia pre daný problém. Navrhol ich v roku 1975 [John Henry Holland](https://wikipedia.org/wiki/John_Henry_Holland).

Genetické algoritmy sú založené na nasledujúcich myšlienkach:

* Platné riešenia problému môžu byť reprezentované ako **gény**
* **Kombinácia (crossover)** umožňuje spojiť dve riešenia a získať nové platné riešenie
* **Selektovanie** sa používa na výber optimálnejších riešení pomocou nejakej **fitness funkcie**
* **Mutácie** sa zavádzajú na destabilizáciu optimalizácie a na vyhnutie sa lokálnemu minimu

Ak chcete implementovať genetický algoritmus, potrebujete:

* Nájsť spôsob kódovania riešení problému pomocou **génov** g&in;&Gamma;
* Na množine génov &Gamma; definovať **fitness funkciu** fit: &Gamma;&rightarrow;**R**. Menšie hodnoty funkcie zodpovedajú lepším riešeniam.
* Definovať mechanizmus **kombinácie** na spojenie dvoch génov a získanie nového platného riešenia crossover: &Gamma;<sup>2</sub>&rightarrow;&Gamma;.
* Definovať mechanizmus **mutácie** mutate: &Gamma;&rightarrow;&Gamma;.

V mnohých prípadoch sú kombinácia a mutácia pomerne jednoduché algoritmy na manipuláciu s génmi ako číselnými sekvenciami alebo bitovými vektormi.

Konkrétna implementácia genetického algoritmu sa môže líšiť podľa prípadu, ale celková štruktúra je nasledovná:

1. Vyberte počiatočnú populáciu G&subset;&Gamma;
2. Náhodne vyberte jednu z operácií, ktorá sa vykoná v tomto kroku: kombinácia alebo mutácia
3. **Kombinácia**:
   * Náhodne vyberte dva gény g<sub>1</sub>, g<sub>2</sub> &in; G
   * Vypočítajte kombináciu g=crossover(g<sub>1</sub>,g<sub>2</sub>)
   * Ak fit(g)<fit(g<sub>1</sub>) alebo fit(g)<fit(g<sub>2</sub>) - nahraďte príslušný gén v populácii génom g.
4. **Mutácia** - vyberte náhodný gén g&in;G a nahraďte ho mutate(g)
5. Opakujte od kroku 2, kým nedosiahnete dostatočne malú hodnotu fit, alebo kým sa nedosiahne limit počtu krokov.

## Typické úlohy

Úlohy, ktoré sa typicky riešia pomocou genetických algoritmov, zahŕňajú:

1. Optimalizácia rozvrhov
1. Optimálne balenie
1. Optimálne rezanie
1. Urýchlenie vyčerpávajúceho vyhľadávania

## ✍️ Cvičenia: Genetické algoritmy

Pokračujte v učení v nasledujúcich notebookoch:

Prejdite na [tento notebook](Genetic.ipynb), kde nájdete dva príklady použitia genetických algoritmov:

1. Spravodlivé rozdelenie pokladu
1. Problém 8 dám

## Záver

Genetické algoritmy sa používajú na riešenie mnohých problémov, vrátane logistiky a vyhľadávacích problémov. Táto oblasť je inšpirovaná výskumom, ktorý spája témy z psychológie a informatiky.

## 🚀 Výzva

"Genetické algoritmy sú jednoduché na implementáciu, ale ich správanie je ťažké pochopiť." [zdroj](https://wikipedia.org/wiki/Genetic_algorithm) Urobte si výskum a nájdite implementáciu genetického algoritmu, napríklad na riešenie Sudoku, a vysvetlite, ako funguje, vo forme náčrtu alebo diagramu.

## [Kvíz po prednáške](https://ff-quizzes.netlify.app/en/ai/quiz/42)

## Prehľad a samostatné štúdium

Pozrite si [toto skvelé video](https://www.youtube.com/watch?v=qv6UVOQ0F44), ktoré hovorí o tom, ako sa počítač môže naučiť hrať Super Mario pomocou neurónových sietí trénovaných genetickými algoritmami. Viac sa o učení počítača hrať takéto hry dozvieme [v ďalšej sekcii](../22-DeepRL/README.md).

## [Úloha: Diofantická rovnica](Diophantine.ipynb)

Vašou úlohou je vyriešiť tzv. **Diofantickú rovnicu** - rovnicu s celočíselnými koreňmi. Napríklad zvážte rovnicu a+2b+3c+4d=30. Musíte nájsť celočíselné korene, ktoré túto rovnicu spĺňajú.

*Táto úloha je inšpirovaná [týmto článkom](https://habr.com/post/128704/).*

Tipy:

1. Môžete uvažovať korene v intervale [0;30]
1. Ako gén zvážte použitie zoznamu hodnôt koreňov

Použite [Diophantine.ipynb](Diophantine.ipynb) ako východiskový bod.

---

