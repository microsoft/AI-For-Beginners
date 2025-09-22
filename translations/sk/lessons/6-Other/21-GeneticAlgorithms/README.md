<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "893aa368cb485da704b466a0f3775587",
  "translation_date": "2025-08-25T23:18:19+00:00",
  "source_file": "lessons/6-Other/21-GeneticAlgorithms/README.md",
  "language_code": "sk"
}
-->
# Genetické algoritmy

## [Kvíz pred prednáškou](https://ff-quizzes.netlify.app/en/ai/quiz/41)

**Genetické algoritmy** (GA) sú založené na **evolučnom prístupe** k AI, kde sa využívajú metódy evolúcie populácie na získanie optimálneho riešenia pre daný problém. Boli navrhnuté v roku 1975 [Johnom Henrym Hollandom](https://wikipedia.org/wiki/John_Henry_Holland).

Genetické algoritmy sú založené na nasledujúcich princípoch:

* Platné riešenia problému môžu byť reprezentované ako **gény**
* **Kombinácia** nám umožňuje spojiť dve riešenia a získať nové platné riešenie
* **Selektovanie** sa používa na výber optimálnejších riešení pomocou nejakej **fitness funkcie**
* **Mutácie** sa zavádzajú na destabilizáciu optimalizácie a na vyhnutie sa lokálnemu minimu

Ak chcete implementovať genetický algoritmus, potrebujete nasledovné:

 * Nájsť spôsob kódovania riešení problému pomocou **génov** g∈Γ
 * Na množine génov Γ definovať **fitness funkciu** fit: Γ→**R**. Menšie hodnoty funkcie zodpovedajú lepším riešeniam.
 * Definovať mechanizmus **kombinácie**, ktorý spája dva gény a vytvára nové platné riešenie crossover: Γ<sup>2</sub>→Γ.
 * Definovať mechanizmus **mutácie** mutate: Γ→Γ.

V mnohých prípadoch sú mechanizmy kombinácie a mutácie pomerne jednoduché algoritmy na manipuláciu génov ako číselných sekvencií alebo bitových vektorov.

Konkrétna implementácia genetického algoritmu sa môže líšiť od prípadu k prípadu, ale všeobecná štruktúra je nasledovná:

1. Vyberte počiatočnú populáciu G⊂Γ
2. Náhodne vyberte jednu z operácií, ktorá sa vykoná v tomto kroku: kombinácia alebo mutácia
3. **Kombinácia**:
  * Náhodne vyberte dva gény g<sub>1</sub>, g<sub>2</sub> ∈ G
  * Vypočítajte kombináciu g=crossover(g<sub>1</sub>,g<sub>2</sub>)
  * Ak fit(g)<fit(g<sub>1</sub>) alebo fit(g)<fit(g<sub>2</sub>) - nahraďte príslušný gén v populácii génom g.
4. **Mutácia** - vyberte náhodný gén g∈G a nahraďte ho mutate(g)
5. Opakujte od kroku 2, až kým nedosiahnete dostatočne malú hodnotu fit alebo kým sa nedosiahne limit počtu krokov.

## Typické úlohy

Úlohy, ktoré sa zvyčajne riešia pomocou genetických algoritmov, zahŕňajú:

1. Optimalizácia rozvrhu
1. Optimálne balenie
1. Optimálne rezanie
1. Urýchlenie vyčerpávajúceho vyhľadávania

## ✍️ Cvičenia: Genetické algoritmy

Pokračujte vo svojom učení v nasledujúcich notebookoch:

Prejdite na [tento notebook](../../../../../lessons/6-Other/21-GeneticAlgorithms/Genetic.ipynb), kde nájdete dva príklady použitia genetických algoritmov:

1. Spravodlivé rozdelenie pokladu
1. Problém 8 kráľovien

## Záver

Genetické algoritmy sa používajú na riešenie mnohých problémov, vrátane logistiky a vyhľadávacích problémov. Táto oblasť je inšpirovaná výskumom, ktorý spája témy z psychológie a informatiky.

## 🚀 Výzva

"Genetické algoritmy sú jednoduché na implementáciu, ale ich správanie je ťažké pochopiť." [zdroj](https://wikipedia.org/wiki/Genetic_algorithm) Urobte si výskum a nájdite implementáciu genetického algoritmu, napríklad na riešenie Sudoku, a vysvetlite, ako funguje pomocou náčrtu alebo diagramu toku.

## [Kvíz po prednáške](https://ff-quizzes.netlify.app/en/ai/quiz/42)

## Prehľad a samostatné štúdium

Pozrite si [toto skvelé video](https://www.youtube.com/watch?v=qv6UVOQ0F44), ktoré hovorí o tom, ako sa počítač môže naučiť hrať Super Mario pomocou neurónových sietí trénovaných genetickými algoritmami. Viac o tom, ako sa počítače učia hrať hry, sa dozviete [v ďalšej sekcii](../22-DeepRL/README.md).

## [Úloha: Diofantická rovnica](../../../../../lessons/6-Other/21-GeneticAlgorithms/Diophantine.ipynb)

Vaším cieľom je vyriešiť tzv. **Diofantickú rovnicu** - rovnicu s celočíselnými koreňmi. Napríklad zvážte rovnicu a+2b+3c+4d=30. Musíte nájsť celočíselné korene, ktoré túto rovnicu spĺňajú.

*Túto úlohu inšpiroval [tento príspevok](https://habr.com/post/128704/).*

Tipy:

1. Môžete zvážiť korene v intervale [0;30]
1. Ako gén zvážte použitie zoznamu hodnôt koreňov

Použite [Diophantine.ipynb](../../../../../lessons/6-Other/21-GeneticAlgorithms/Diophantine.ipynb) ako východiskový bod.

**Upozornenie**:  
Tento dokument bol preložený pomocou služby AI prekladu [Co-op Translator](https://github.com/Azure/co-op-translator). Aj keď sa snažíme o presnosť, prosím, berte na vedomie, že automatizované preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho rodnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nenesieme zodpovednosť za akékoľvek nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.