# Genetické algoritmy

## [Kvíz před přednáškou](https://ff-quizzes.netlify.app/en/ai/quiz/41)

**Genetické algoritmy** (GA) jsou založeny na **evolučním přístupu** k umělé inteligenci, kde se využívají metody evoluce populace k nalezení optimálního řešení daného problému. Byly navrženy v roce 1975 [Johnem Henry Hollandem](https://wikipedia.org/wiki/John_Henry_Holland).

Genetické algoritmy vycházejí z následujících myšlenek:

* Platná řešení problému lze reprezentovat jako **geny**
* Pomocí **křížení** lze kombinovat dvě řešení a získat nové platné řešení
* **Selektivní výběr** se používá k výběru optimálnějších řešení pomocí nějaké **fitness funkce**
* **Mutace** se zavádějí, aby destabilizovaly optimalizaci a pomohly nám dostat se z lokálního minima

Pokud chcete implementovat genetický algoritmus, potřebujete následující:

 * Najít způsob kódování řešení problému pomocí **genů** g&in;&Gamma;
 * Na množině genů &Gamma; definovat **fitness funkci** fit: &Gamma;&rightarrow;**R**. Menší hodnoty funkce odpovídají lepším řešením.
 * Definovat mechanismus **křížení**, který kombinuje dva geny a vytváří nové platné řešení crossover: &Gamma;<sup>2</sub>&rightarrow;&Gamma;.
 * Definovat mechanismus **mutace** mutate: &Gamma;&rightarrow;&Gamma;.

V mnoha případech jsou algoritmy pro křížení a mutace poměrně jednoduché a manipulují s geny jako s číselnými sekvencemi nebo bitovými vektory.

Konkrétní implementace genetického algoritmu se může případ od případu lišit, ale obecná struktura je následující:

1. Vyberte počáteční populaci G&subset;&Gamma;
2. Náhodně vyberte jednu z operací, která bude v tomto kroku provedena: křížení nebo mutace
3. **Křížení**:
  * Náhodně vyberte dva geny g<sub>1</sub>, g<sub>2</sub> &in; G
  * Spočítejte křížení g=crossover(g<sub>1</sub>,g<sub>2</sub>)
  * Pokud fit(g)<fit(g<sub>1</sub>) nebo fit(g)<fit(g<sub>2</sub>), nahraďte odpovídající gen v populaci genem g.
4. **Mutace** - náhodně vyberte gen g&in;G a nahraďte jej mutate(g)
5. Opakujte od kroku 2, dokud nedosáhnete dostatečně malé hodnoty fit, nebo dokud nebude dosažen limit počtu kroků.

## Typické úlohy

Úlohy, které se obvykle řeší pomocí genetických algoritmů, zahrnují:

1. Optimalizace rozvrhů
1. Optimální balení
1. Optimální řezání
1. Zrychlení vyčerpávajícího prohledávání

## ✍️ Cvičení: Genetické algoritmy

Pokračujte ve studiu v následujících noteboocích:

Přejděte na [tento notebook](Genetic.ipynb), kde najdete dva příklady použití genetických algoritmů:

1. Spravedlivé rozdělení pokladu
1. Problém 8 dam

## Závěr

Genetické algoritmy se používají k řešení mnoha problémů, včetně logistiky a vyhledávacích problémů. Tato oblast je inspirována výzkumem, který spojil témata psychologie a informatiky.

## 🚀 Výzva

"Genetické algoritmy jsou jednoduché na implementaci, ale jejich chování je obtížné pochopit." [zdroj](https://wikipedia.org/wiki/Genetic_algorithm) Proveďte výzkum a najděte implementaci genetického algoritmu, například pro řešení sudoku, a vysvětlete, jak funguje, formou náčrtu nebo diagramu.

## [Kvíz po přednášce](https://ff-quizzes.netlify.app/en/ai/quiz/42)

## Přehled a samostudium

Podívejte se na [toto skvělé video](https://www.youtube.com/watch?v=qv6UVOQ0F44), které ukazuje, jak se počítač může naučit hrát Super Mario pomocí neuronových sítí trénovaných genetickými algoritmy. O tom, jak se počítače učí hrát hry, se dozvíme více [v další sekci](../22-DeepRL/README.md).

## [Úkol: Diofantická rovnice](Diophantine.ipynb)

Vaším cílem je vyřešit tzv. **Diofantickou rovnici** - rovnici s celočíselnými kořeny. Například uvažujme rovnici a+2b+3c+4d=30. Musíte najít celočíselné kořeny, které tuto rovnici splňují.

*Tento úkol je inspirován [tímto článkem](https://habr.com/post/128704/).*

Tipy:

1. Můžete uvažovat kořeny v intervalu [0;30]
1. Jako gen zvažte použití seznamu hodnot kořenů

Použijte [Diophantine.ipynb](Diophantine.ipynb) jako výchozí bod.

---

