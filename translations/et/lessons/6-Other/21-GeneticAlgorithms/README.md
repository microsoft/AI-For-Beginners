# Geneetilised algoritmid

## [Eelloengu viktoriin](https://ff-quizzes.netlify.app/en/ai/quiz/41)

**Geneetilised algoritmid** (GA) põhinevad **evolutsioonilisel lähenemisel** tehisintellektile, kus populatsiooni evolutsioonimeetodeid kasutatakse optimaalse lahenduse leidmiseks antud probleemile. Need pakkus välja [John Henry Holland](https://wikipedia.org/wiki/John_Henry_Holland) aastal 1975.

Geneetilised algoritmid põhinevad järgmistel ideedel:

* Kehtivaid lahendusi probleemile saab esitada **geenidena**
* **Ristamine** võimaldab kombineerida kahte lahendust, et saada uus kehtiv lahendus
* **Valik** kasutatakse optimaalsemate lahenduste leidmiseks, kasutades **sobivusfunktsiooni**
* **Mutatsioonid** lisatakse, et destabiliseerida optimeerimist ja vältida lokaalset miinimumi

Geneetilise algoritmi rakendamiseks on vaja järgmist:

 * Leida meetod, kuidas kodeerida probleemilahendusi **geenide** abil g&in;&Gamma;
 * Geenide hulgal &Gamma; tuleb defineerida **sobivusfunktsioon** fit: &Gamma;&rightarrow;**R**. Väiksemad funktsiooni väärtused vastavad parematele lahendustele.
 * Defineerida **ristamismehhanism**, et kombineerida kaks geeni ja saada uus kehtiv lahendus crossover: &Gamma;<sup>2</sub>&rightarrow;&Gamma;.
 * Defineerida **mutatsioonimehhanism** mutate: &Gamma;&rightarrow;&Gamma;.

Paljudel juhtudel on ristamine ja mutatsioon üsna lihtsad algoritmid, mis manipuleerivad geene numbriliste jadade või bittvektoritena.

Geneetilise algoritmi konkreetne rakendus võib juhtumiti erineda, kuid üldine struktuur on järgmine:

1. Valida algpopulatsioon G&subset;&Gamma;
2. Juhuslikult valida operatsioon, mida sellel sammul teostatakse: ristamine või mutatsioon
3. **Ristamine**:
  * Juhuslikult valida kaks geeni g<sub>1</sub>, g<sub>2</sub> &in; G
  * Arvutada ristamine g=crossover(g<sub>1</sub>,g<sub>2</sub>)
  * Kui fit(g)<fit(g<sub>1</sub>) või fit(g)<fit(g<sub>2</sub>) - asendada vastav geen populatsioonis geeniga g.
4. **Mutatsioon** - valida juhuslik geen g&in;G ja asendada see mutate(g)-ga
5. Korrata alates sammust 2, kuni saavutatakse piisavalt väike sobivusfunktsiooni väärtus või kuni sammude arv jõuab piirini.

## Tüüpilised ülesanded

Geneetiliste algoritmidega lahendatavad ülesanded hõlmavad:

1. Graafiku optimeerimine
1. Optimaalne pakkimine
1. Optimaalne lõikamine
1. Kurnava otsingu kiirendamine

## ✍️ Harjutused: Geneetilised algoritmid

Jätka õppimist järgmistes märkmikes:

Mine [sellele märkmikule](Genetic.ipynb), et näha kahte näidet geneetiliste algoritmide kasutamisest:

1. Aarde õiglane jagamine
1. 8 kuninganna probleem

## Kokkuvõte

Geneetilisi algoritme kasutatakse paljude probleemide lahendamiseks, sealhulgas logistika ja otsinguprobleemid. Valdkond on inspireeritud uurimistööst, mis ühendas psühholoogia ja arvutiteaduse teemasid.

## 🚀 Väljakutse

"Geneetilisi algoritme on lihtne rakendada, kuid nende käitumist on raske mõista." [allikas](https://wikipedia.org/wiki/Genetic_algorithm) Uuri geneetilise algoritmi rakendust, näiteks Sudoku lahendamist, ja selgita, kuidas see töötab visandi või vooskeemi abil.

## [Järelloengu viktoriin](https://ff-quizzes.netlify.app/en/ai/quiz/42)

## Ülevaade ja iseseisev õppimine

Vaata [seda suurepärast videot](https://www.youtube.com/watch?v=qv6UVOQ0F44), mis räägib sellest, kuidas arvuti saab õppida mängima Super Mariot, kasutades geneetiliste algoritmidega treenitud närvivõrke. Õpime rohkem arvuti õppimisest selliste mängude mängimiseks [järgmises osas](../22-DeepRL/README.md).

## [Ülesanne: Diofantiline võrrand](Diophantine.ipynb)

Sinu eesmärk on lahendada nn **Diofantiline võrrand** - võrrand täisarvuliste juurtega. Näiteks kaalu võrrandit a+2b+3c+4d=30. Pead leidma täisarvulised juured, mis rahuldavad seda võrrandit.

*See ülesanne on inspireeritud [sellest postitusest](https://habr.com/post/128704/).*

Vihjed:

1. Võid kaaluda juuri vahemikus [0;30]
1. Geenina võid kasutada juurväärtuste loendit

Kasuta [Diophantine.ipynb](Diophantine.ipynb) lähtepunktina.

---

**Lahtiütlus**:  
See dokument on tõlgitud AI tõlketeenuse [Co-op Translator](https://github.com/Azure/co-op-translator) abil. Kuigi püüame tagada täpsust, palume arvestada, et automaatsed tõlked võivad sisaldada vigu või ebatäpsusi. Algne dokument selle algses keeles tuleks pidada autoriteetseks allikaks. Olulise teabe puhul soovitame kasutada professionaalset inimtõlget. Me ei vastuta selle tõlke kasutamisest tulenevate arusaamatuste või valesti tõlgenduste eest.