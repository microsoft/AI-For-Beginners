<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "893aa368cb485da704b466a0f3775587",
  "translation_date": "2025-08-25T23:19:29+00:00",
  "source_file": "lessons/6-Other/21-GeneticAlgorithms/README.md",
  "language_code": "hr"
}
-->
# Genetski algoritmi

## [Pre-lecture quiz](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/121)

**Genetski algoritmi** (GA) temelje se na **evolucijskom pristupu** umjetnoj inteligenciji, gdje se metode evolucije populacije koriste za pronalaženje optimalnog rješenja za određeni problem. Predložio ih je 1975. godine [John Henry Holland](https://wikipedia.org/wiki/John_Henry_Holland).

Genetski algoritmi temelje se na sljedećim idejama:

* Valjana rješenja problema mogu se predstaviti kao **geni**
* **Kombiniranje** omogućuje spajanje dvaju rješenja kako bi se dobilo novo valjano rješenje
* **Selekcija** se koristi za odabir optimalnijih rješenja pomoću neke **funkcije prilagodbe**
* **Mutacije** se uvode kako bi se destabilizirala optimizacija i izbjeglo lokalno minimum

Ako želite implementirati genetski algoritam, trebate sljedeće:

 * Pronaći način kodiranja rješenja problema pomoću **gena** g∈Γ
 * Na skupu gena Γ trebate definirati **funkciju prilagodbe** fit: Γ→**R**. Manje vrijednosti funkcije odgovaraju boljim rješenjima.
 * Definirati mehanizam **kombiniranja** za spajanje dvaju gena kako bi se dobilo novo valjano rješenje crossover: Γ<sup>2</sub>→Γ.
 * Definirati mehanizam **mutacije** mutate: Γ→Γ.

U mnogim slučajevima, kombiniranje i mutacija su prilično jednostavni algoritmi za manipulaciju genima kao numeričkim nizovima ili bitnim vektorima.

Specifična implementacija genetskog algoritma može se razlikovati od slučaja do slučaja, ali opća struktura je sljedeća:

1. Odabrati početnu populaciju G⊂Γ
2. Nasumično odabrati jednu od operacija koja će se izvesti u ovom koraku: kombiniranje ili mutacija
3. **Kombiniranje**:
  * Nasumično odabrati dva gena g<sub>1</sub>, g<sub>2</sub> ∈ G
  * Izračunati kombiniranje g=crossover(g<sub>1</sub>,g<sub>2</sub>)
  * Ako fit(g)<fit(g<sub>1</sub>) ili fit(g)<fit(g<sub>2</sub>) - zamijeniti odgovarajući gen u populaciji s g.
4. **Mutacija** - odabrati nasumični gen g∈G i zamijeniti ga s mutate(g)
5. Ponavljati od koraka 2, dok ne dobijemo dovoljno malu vrijednost fit ili dok se ne dostigne ograničenje broja koraka.

## Tipični zadaci

Zadaci koji se obično rješavaju genetskim algoritmima uključuju:

1. Optimizacija rasporeda
1. Optimalno pakiranje
1. Optimalno rezanje
1. Ubrzavanje iscrpne pretrage

## ✍️ Vježbe: Genetski algoritmi

Nastavite učiti u sljedećim bilježnicama:

Idite na [ovu bilježnicu](../../../../../lessons/6-Other/21-GeneticAlgorithms/Genetic.ipynb) kako biste vidjeli dva primjera korištenja genetskih algoritama:

1. Pravedna podjela blaga
1. Problem 8 kraljica

## Zaključak

Genetski algoritmi koriste se za rješavanje mnogih problema, uključujući logističke i probleme pretrage. Ovo područje inspirirano je istraživanjima koja spajaju teme iz psihologije i računalnih znanosti.

## 🚀 Izazov

"Genetski algoritmi su jednostavni za implementaciju, ali njihovo ponašanje je teško razumjeti." [izvor](https://wikipedia.org/wiki/Genetic_algorithm) Provedite istraživanje kako biste pronašli implementaciju genetskog algoritma, poput rješavanja Sudoku zagonetke, i objasnite kako funkcionira kao skica ili dijagram toka.

## [Post-lecture quiz](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/221)

## Pregled i samostalno učenje

Pogledajte [ovaj odličan video](https://www.youtube.com/watch?v=qv6UVOQ0F44) koji govori o tome kako računalo može naučiti igrati Super Mario koristeći neuronske mreže trenirane genetskim algoritmima. Više o učenju računala za igranje takvih igara naučit ćemo [u sljedećem odjeljku](../22-DeepRL/README.md).

## [Zadatak: Diofantova jednadžba](../../../../../lessons/6-Other/21-GeneticAlgorithms/Diophantine.ipynb)

Vaš cilj je riješiti tzv. **Diofantovu jednadžbu** - jednadžbu s cijelim korijenima. Na primjer, razmotrite jednadžbu a+2b+3c+4d=30. Trebate pronaći cijele korijene koji zadovoljavaju ovu jednadžbu.

*Ovaj zadatak inspiriran je [ovim postom](https://habr.com/post/128704/).*

Savjeti:

1. Možete razmotriti korijene u intervalu [0;30]
1. Kao gen, razmotrite korištenje popisa vrijednosti korijena

Koristite [Diophantine.ipynb](../../../../../lessons/6-Other/21-GeneticAlgorithms/Diophantine.ipynb) kao početnu točku.

**Odricanje od odgovornosti**:  
Ovaj dokument je preveden pomoću AI usluge za prevođenje [Co-op Translator](https://github.com/Azure/co-op-translator). Iako nastojimo osigurati točnost, imajte na umu da automatski prijevodi mogu sadržavati pogreške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati autoritativnim izvorom. Za ključne informacije preporučuje se profesionalni prijevod od strane čovjeka. Ne preuzimamo odgovornost za nesporazume ili pogrešna tumačenja koja mogu proizaći iz korištenja ovog prijevoda.