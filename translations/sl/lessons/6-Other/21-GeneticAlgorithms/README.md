<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "893aa368cb485da704b466a0f3775587",
  "translation_date": "2025-08-25T23:19:46+00:00",
  "source_file": "lessons/6-Other/21-GeneticAlgorithms/README.md",
  "language_code": "sl"
}
-->
# Genetski algoritmi

## [Preizkus pred predavanjem](https://ff-quizzes.netlify.app/en/ai/quiz/41)

**Genetski algoritmi** (GA) temeljijo na **evolucijskem pristopu** k umetni inteligenci, kjer se metode evolucije populacije uporabljajo za iskanje optimalne rešitve za določen problem. Leta 1975 jih je predlagal [John Henry Holland](https://wikipedia.org/wiki/John_Henry_Holland).

Genetski algoritmi temeljijo na naslednjih idejah:

* Veljavne rešitve problema lahko predstavimo kot **gene**
* S pomočjo **križanja** lahko združimo dve rešitvi in pridobimo novo veljavno rešitev
* **Izbor** se uporablja za izbiro bolj optimalnih rešitev z uporabo neke **funkcije ustreznosti**
* **Mutacije** se uvajajo za destabilizacijo optimizacije in izogibanje lokalnim minimumom

Če želite implementirati genetski algoritem, potrebujete naslednje:

* Najti metodo za kodiranje rešitev problema z uporabo **genov** g∈Γ
* Na množici genov Γ je treba definirati **funkcijo ustreznosti** fit: Γ→**R**. Manjše vrednosti funkcije ustrezajo boljšim rešitvam.
* Definirati mehanizem za **križanje**, ki združuje dva gena v novo veljavno rešitev crossover: Γ<sup>2</sub>→Γ.
* Definirati mehanizem za **mutacijo** mutate: Γ→Γ.

V mnogih primerih so algoritmi za križanje in mutacijo precej preprosti in manipulirajo gene kot številske zaporedja ali bitne vektorje.

Specifična implementacija genetskega algoritma se lahko razlikuje od primera do primera, vendar je splošna struktura naslednja:

1. Izberite začetno populacijo G⊂Γ
2. Naključno izberite eno od operacij, ki se bo izvedla v tem koraku: križanje ali mutacija
3. **Križanje**:
   * Naključno izberite dva gena g<sub>1</sub>, g<sub>2</sub> ∈ G
   * Izračunajte križanje g=crossover(g<sub>1</sub>,g<sub>2</sub>)
   * Če fit(g)<fit(g<sub>1</sub>) ali fit(g)<fit(g<sub>2</sub>) - zamenjajte ustrezen gen v populaciji z g.
4. **Mutacija** - izberite naključni gen g∈G in ga zamenjajte z mutate(g)
5. Ponovite od koraka 2, dokler ne dosežete dovolj majhne vrednosti fit ali dokler ne dosežete omejitve števila korakov.

## Tipične naloge

Naloge, ki jih običajno rešujemo z genetskimi algoritmi, vključujejo:

1. Optimizacija urnikov
1. Optimalno pakiranje
1. Optimalno rezanje
1. Pospeševanje izčrpnega iskanja

## ✍️ Vaje: Genetski algoritmi

Nadaljujte z učenjem v naslednjih beležnicah:

Pojdite na [to beležnico](../../../../../lessons/6-Other/21-GeneticAlgorithms/Genetic.ipynb), kjer sta prikazana dva primera uporabe genetskih algoritmov:

1. Poštena delitev zaklada
1. Problem osmih dam

## Zaključek

Genetski algoritmi se uporabljajo za reševanje številnih problemov, vključno z logističnimi in iskalnimi problemi. Področje je navdihnjeno z raziskavami, ki združujejo teme iz psihologije in računalništva.

## 🚀 Izziv

"Genetski algoritmi so preprosti za implementacijo, vendar je njihovo obnašanje težko razumeti." [vir](https://wikipedia.org/wiki/Genetic_algorithm) Raziskujte in poiščite implementacijo genetskega algoritma, na primer za reševanje Sudoku uganke, ter razložite, kako deluje, s skico ali diagramom poteka.

## [Preizkus po predavanju](https://ff-quizzes.netlify.app/en/ai/quiz/42)

## Pregled in samostojno učenje

Oglejte si [ta odličen video](https://www.youtube.com/watch?v=qv6UVOQ0F44), ki govori o tem, kako računalnik lahko uči igrati Super Mario z uporabo nevronskih mrež, treniranih z genetskimi algoritmi. Več o učenju računalnika za igranje takšnih iger bomo izvedeli [v naslednjem poglavju](../22-DeepRL/README.md).

## [Naloga: Diofantova enačba](../../../../../lessons/6-Other/21-GeneticAlgorithms/Diophantine.ipynb)

Vaš cilj je rešiti tako imenovano **Diofantovo enačbo** - enačbo s celimi koreni. Na primer, razmislite o enačbi a+2b+3c+4d=30. Poiščite cele korene, ki zadovoljijo to enačbo.

*Ta naloga je navdihnjena z [tem prispevkom](https://habr.com/post/128704/).*

Namigi:

1. Korene lahko obravnavate v intervalu [0;30]
1. Kot gen razmislite o uporabi seznama vrednosti korenov

Uporabite [Diophantine.ipynb](../../../../../lessons/6-Other/21-GeneticAlgorithms/Diophantine.ipynb) kot izhodišče.

**Omejitev odgovornosti**:  
Ta dokument je bil preveden z uporabo storitve AI za prevajanje [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas prosimo, da upoštevate, da lahko avtomatizirani prevodi vsebujejo napake ali netočnosti. Izvirni dokument v njegovem maternem jeziku naj se šteje za avtoritativni vir. Za ključne informacije priporočamo profesionalni človeški prevod. Ne prevzemamo odgovornosti za morebitna nesporazumevanja ali napačne razlage, ki izhajajo iz uporabe tega prevoda.