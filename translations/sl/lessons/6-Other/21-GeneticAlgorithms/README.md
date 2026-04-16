# Genetski algoritmi

## [Predhodni kviz](https://ff-quizzes.netlify.app/en/ai/quiz/41)

**Genetski algoritmi** (GA) temeljijo na **evolucijskem pristopu** k umetni inteligenci, pri katerem se uporabljajo metode evolucije populacije za pridobitev optimalne rešitve za določen problem. Predlagal jih je leta 1975 [John Henry Holland](https://wikipedia.org/wiki/John_Henry_Holland).

Genetski algoritmi temeljijo na naslednjih idejah:

* Veljavne rešitve problema lahko predstavimo kot **gene**
* **Križanje** omogoča združevanje dveh rešitev za pridobitev nove veljavne rešitve
* **Selekcija** se uporablja za izbiro bolj optimalnih rešitev z uporabo **funkcije ustreznosti**
* **Mutacije** se uvajajo za destabilizacijo optimizacije in izogibanje lokalnemu minimumu

Če želite implementirati genetski algoritem, potrebujete naslednje:

 * Najti način kodiranja rešitev problema z uporabo **genov** g&in;&Gamma;
 * Na množici genov &Gamma; morate definirati **funkcijo ustreznosti** fit: &Gamma;&rightarrow;**R**. Manjše vrednosti funkcije ustrezajo boljšim rešitvam.
 * Definirati mehanizem **križanja**, da združite dva gena in dobite novo veljavno rešitev crossover: &Gamma;<sup>2</sub>&rightarrow;&Gamma;.
 * Definirati mehanizem **mutacije** mutate: &Gamma;&rightarrow;&Gamma;.

V mnogih primerih sta križanje in mutacija precej preprosta algoritma za manipulacijo genov kot numeričnih zaporedij ali bitnih vektorjev.

Specifična implementacija genetskega algoritma se lahko razlikuje od primera do primera, vendar je splošna struktura naslednja:

1. Izberite začetno populacijo G&subset;&Gamma;
2. Naključno izberite eno od operacij, ki se bo izvedla v tem koraku: križanje ali mutacija
3. **Križanje**:
  * Naključno izberite dva gena g<sub>1</sub>, g<sub>2</sub> &in; G
  * Izračunajte križanje g=crossover(g<sub>1</sub>,g<sub>2</sub>)
  * Če fit(g)<fit(g<sub>1</sub>) ali fit(g)<fit(g<sub>2</sub>) - zamenjajte ustrezni gen v populaciji z g.
4. **Mutacija** - naključno izberite gen g&in;G in ga zamenjajte z mutate(g)
5. Ponavljajte od koraka 2, dokler ne dosežete dovolj majhne vrednosti fit ali dokler ne dosežete omejitve števila korakov.

## Tipične naloge

Naloge, ki jih običajno rešujejo genetski algoritmi, vključujejo:

1. Optimizacija urnikov
1. Optimalno pakiranje
1. Optimalno rezanje
1. Pospeševanje izčrpnega iskanja

## ✍️ Vaje: Genetski algoritmi

Nadaljujte z učenjem v naslednjih zvezkih:

Pojdite na [ta zvezek](Genetic.ipynb), da si ogledate dva primera uporabe genetskih algoritmov:

1. Poštena delitev zaklada
1. Problem osmih kraljic

## Zaključek

Genetski algoritmi se uporabljajo za reševanje številnih problemov, vključno z logističnimi in iskalnimi problemi. Področje je navdihnjeno z raziskavami, ki združujejo teme iz psihologije in računalništva.

## 🚀 Izziv

"Genetski algoritmi so enostavni za implementacijo, vendar je njihovo obnašanje težko razumeti." [vir](https://wikipedia.org/wiki/Genetic_algorithm) Raziskujte in poiščite implementacijo genetskega algoritma, kot je reševanje Sudoku uganke, ter razložite, kako deluje, kot skico ali diagram poteka.

## [Kviz po predavanju](https://ff-quizzes.netlify.app/en/ai/quiz/42)

## Pregled in samostojno učenje

Oglejte si [ta odličen video](https://www.youtube.com/watch?v=qv6UVOQ0F44), ki govori o tem, kako računalnik lahko naučimo igrati Super Mario z uporabo nevronskih mrež, treniranih z genetskimi algoritmi. Več o učenju računalnika za igranje takšnih iger bomo izvedeli [v naslednjem poglavju](../22-DeepRL/README.md).

## [Naloga: Diofantova enačba](Diophantine.ipynb)

Vaš cilj je rešiti tako imenovano **Diofantovo enačbo** - enačbo z celoštevilskimi koreni. Na primer, razmislite o enačbi a+2b+3c+4d=30. Najti morate celoštevilske korene, ki zadovoljijo to enačbo.

*Ta naloga je navdihnjena z [tem prispevkom](https://habr.com/post/128704/).*

Namigi:

1. Korene lahko obravnavate v intervalu [0;30]
1. Kot gen razmislite o uporabi seznama vrednosti korenov

Uporabite [Diophantine.ipynb](Diophantine.ipynb) kot izhodišče.

---

