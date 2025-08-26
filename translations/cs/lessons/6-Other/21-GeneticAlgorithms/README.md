<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "893aa368cb485da704b466a0f3775587",
  "translation_date": "2025-08-25T23:18:02+00:00",
  "source_file": "lessons/6-Other/21-GeneticAlgorithms/README.md",
  "language_code": "cs"
}
-->
# Genetické algoritmy

## [Kvíz před přednáškou](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/121)

**Genetické algoritmy** (GA) jsou založeny na **evolučním přístupu** k AI, při kterém se využívají metody evoluce populace k nalezení optimálního řešení daného problému. Byly navrženy v roce 1975 [Johnem Henry Hollandem](https://wikipedia.org/wiki/John_Henry_Holland).

Genetické algoritmy vycházejí z následujících principů:

* Platná řešení problému mohou být reprezentována jako **geny**
* **Křížení** nám umožňuje kombinovat dvě řešení dohromady a získat nové platné řešení
* **Selektivní výběr** se používá k výběru optimálnějších řešení pomocí nějaké **fitness funkce**
* **Mutace** se zavádějí, aby destabilizovaly optimalizaci a dostaly nás z lokálního minima

Pokud chcete implementovat genetický algoritmus, potřebujete následující:

 * Najít způsob kódování řešení problému pomocí **genů** g∈Γ
 * Na množině genů Γ definovat **fitness funkci** fit: Γ→**R**. Menší hodnoty funkce odpovídají lepším řešením.
 * Definovat mechanismus **křížení**, který kombinuje dva geny dohromady a vytváří nové platné řešení crossover: Γ<sup>2</sub>→Γ.
 * Definovat mechanismus **mutace** mutate: Γ→Γ.

V mnoha případech jsou křížení a mutace poměrně jednoduché algoritmy pro manipulaci s geny jako číselnými sekvencemi nebo bitovými vektory.

Konkrétní implementace genetického algoritmu se může případ od případu lišit, ale obecná struktura je následující:

1. Vyberte počáteční populaci G⊂Γ
2. Náhodně vyberte jednu z operací, která bude provedena v tomto kroku: křížení nebo mutace
3. **Křížení**:
  * Náhodně vyberte dva geny g<sub>1</sub>, g<sub>2</sub> ∈ G
  * Vypočítejte křížení g=crossover(g<sub>1</sub>,g<sub>2</sub>)
  * Pokud fit(g)<fit(g<sub>1</sub>) nebo fit(g)<fit(g<sub>2</sub>) - nahraďte odpovídající gen v populaci genem g.
4. **Mutace** - vyberte náhodný gen g∈G a nahraďte ho mutate(g)
5. Opakujte od kroku 2, dokud nedosáhnete dostatečně malé hodnoty fit nebo dokud nebude dosažen limit počtu kroků.

## Typické úlohy

Úlohy, které se obvykle řeší pomocí genetických algoritmů, zahrnují:

1. Optimalizace rozvrhu
1. Optimální balení
1. Optimální řezání
1. Zrychlení vyčerpávajícího hledání

## ✍️ Cvičení: Genetické algoritmy

Pokračujte ve svém učení v následujících noteboocích:

Přejděte na [tento notebook](../../../../../lessons/6-Other/21-GeneticAlgorithms/Genetic.ipynb), kde najdete dva příklady použití genetických algoritmů:

1. Spravedlivé rozdělení pokladu
1. Problém 8 dam

## Závěr

Genetické algoritmy se používají k řešení mnoha problémů, včetně logistiky a vyhledávacích úloh. Tento obor je inspirován výzkumem, který spojil témata z psychologie a informatiky.

## 🚀 Výzva

"Genetické algoritmy jsou jednoduché na implementaci, ale jejich chování je obtížné pochopit." [zdroj](https://wikipedia.org/wiki/Genetic_algorithm) Proveďte výzkum a najděte implementaci genetického algoritmu, například pro řešení Sudoku, a vysvětlete, jak funguje pomocí náčrtu nebo diagramu.

## [Kvíz po přednášce](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/221)

## Přehled a samostudium

Podívejte se na [toto skvělé video](https://www.youtube.com/watch?v=qv6UVOQ0F44), které ukazuje, jak se počítač může naučit hrát Super Mario pomocí neuronových sítí trénovaných genetickými algoritmy. O tom, jak se počítač učí hrát hry, se dozvíme více [v další sekci](../22-DeepRL/README.md).

## [Úkol: Diofantická rovnice](../../../../../lessons/6-Other/21-GeneticAlgorithms/Diophantine.ipynb)

Vaším cílem je vyřešit tzv. **Diofantickou rovnici** - rovnici s celočíselnými kořeny. Například zvažte rovnici a+2b+3c+4d=30. Musíte najít celočíselné kořeny, které tuto rovnici splňují.

*Tento úkol je inspirován [tímto příspěvkem](https://habr.com/post/128704/).*

Tipy:

1. Můžete uvažovat kořeny v intervalu [0;30]
1. Jako gen zvažte použití seznamu hodnot kořenů

Použijte [Diophantine.ipynb](../../../../../lessons/6-Other/21-GeneticAlgorithms/Diophantine.ipynb) jako výchozí bod.

**Prohlášení:**  
Tento dokument byl přeložen pomocí služby pro automatický překlad [Co-op Translator](https://github.com/Azure/co-op-translator). Ačkoli se snažíme o přesnost, mějte prosím na paměti, že automatické překlady mohou obsahovat chyby nebo nepřesnosti. Původní dokument v jeho původním jazyce by měl být považován za autoritativní zdroj. Pro důležité informace doporučujeme profesionální lidský překlad. Neodpovídáme za žádná nedorozumění nebo nesprávné interpretace vyplývající z použití tohoto překladu.