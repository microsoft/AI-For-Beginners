<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "893aa368cb485da704b466a0f3775587",
  "translation_date": "2025-08-25T20:57:44+00:00",
  "source_file": "lessons/6-Other/21-GeneticAlgorithms/README.md",
  "language_code": "sw"
}
-->
# Algorithms za Kijenetiki

## [Maswali ya awali ya mihadhara](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/121)

**Algorithms za Kijenetiki** (GA) zinategemea mbinu ya **mabadiliko ya kimaumbile** katika AI, ambapo mbinu za mabadiliko ya idadi ya watu zinatumika kupata suluhisho bora kwa tatizo fulani. Zilianzishwa mwaka 1975 na [John Henry Holland](https://wikipedia.org/wiki/John_Henry_Holland).

Algorithms za Kijenetiki zinategemea mawazo yafuatayo:

* Suluhisho halali za tatizo zinaweza kuwakilishwa kama **jini**
* **Crossover** inatuwezesha kuchanganya suluhisho mbili pamoja ili kupata suluhisho jipya halali
* **Uteuzi** hutumika kuchagua suluhisho bora zaidi kwa kutumia **kazi ya ufanisi**
* **Mabadiliko** huletwa ili kuvuruga uboreshaji na kututoa kwenye kiwango cha chini cha ndani

Ikiwa unataka kutekeleza Algorithm ya Kijenetiki, unahitaji yafuatayo:

 * Kupata njia ya kuweka suluhisho za tatizo letu kwa kutumia **jini** g∈Γ
 * Kwenye seti ya jini Γ tunahitaji kufafanua **kazi ya ufanisi** fit: Γ→**R**. Thamani ndogo za kazi zinahusiana na suluhisho bora.
 * Kufafanua mfumo wa **crossover** wa kuchanganya jini mbili pamoja ili kupata suluhisho jipya crossover: Γ<sup>2</sub>→Γ.
 * Kufafanua mfumo wa **mabadiliko** mutate: Γ→Γ.

Katika hali nyingi, crossover na mabadiliko ni algorithms rahisi za kudhibiti jini kama mfuatano wa namba au vekta za biti.

Utekelezaji maalum wa algorithm ya kijenetiki unaweza kutofautiana kulingana na kesi, lakini muundo wa jumla ni kama ifuatavyo:

1. Chagua idadi ya watu ya awali G⊂Γ
2. Chagua kwa nasibu moja ya operesheni zitakazofanywa katika hatua hii: crossover au mabadiliko
3. **Crossover**:
  * Chagua kwa nasibu jini mbili g<sub>1</sub>, g<sub>2</sub> ∈ G
  * Hesabu crossover g=crossover(g<sub>1</sub>,g<sub>2</sub>)
  * Ikiwa fit(g)<fit(g<sub>1</sub>) au fit(g)<fit(g<sub>2</sub>) - badilisha jini husika katika idadi ya watu kwa g.
4. **Mabadiliko** - chagua jini moja kwa nasibu g∈G na ibadilishe kwa mutate(g)
5. Rudia kutoka hatua ya 2, hadi tupate thamani ndogo ya kutosha ya fit, au hadi kikomo cha idadi ya hatua kifikiwe.

## Kazi za Kawaida

Kazi zinazotatuliwa mara kwa mara na Algorithms za Kijenetiki ni pamoja na:

1. Uboreshaji wa ratiba
1. Upangaji bora wa mizigo
1. Ukataji bora
1. Kuharakisha utafutaji wa kina

## ✍️ Mazoezi: Algorithms za Kijenetiki

Endelea kujifunza katika daftari zifuatazo:

Nenda kwenye [daftari hili](../../../../../lessons/6-Other/21-GeneticAlgorithms/Genetic.ipynb) kuona mifano miwili ya kutumia Algorithms za Kijenetiki:

1. Mgawanyo wa haki wa hazina
1. Tatizo la Malkia 8

## Hitimisho

Algorithms za Kijenetiki zinatumika kutatua matatizo mengi, ikiwa ni pamoja na matatizo ya usafirishaji na utafutaji. Uwanja huu umechochewa na utafiti uliochanganya mada za Saikolojia na Sayansi ya Kompyuta.

## 🚀 Changamoto

"Algorithms za kijenetiki ni rahisi kutekeleza, lakini tabia zake ni ngumu kuelewa." [chanzo](https://wikipedia.org/wiki/Genetic_algorithm) Fanya utafiti ili kupata utekelezaji wa algorithm ya kijenetiki kama kutatua fumbo la Sudoku, na eleza jinsi inavyofanya kazi kwa mchoro au mtiririko wa hatua.

## [Maswali ya baada ya mihadhara](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/221)

## Mapitio & Kujifunza Binafsi

Tazama [video hii nzuri](https://www.youtube.com/watch?v=qv6UVOQ0F44) inayozungumzia jinsi kompyuta inavyoweza kujifunza kucheza Super Mario kwa kutumia mitandao ya neva iliyofunzwa na algorithms za kijenetiki. Tutajifunza zaidi kuhusu kompyuta kujifunza kucheza michezo kama hiyo [katika sehemu inayofuata](../22-DeepRL/README.md).

## [Kazi: Mlinganyo wa Diophantine](../../../../../lessons/6-Other/21-GeneticAlgorithms/Diophantine.ipynb)

Lengo lako ni kutatua kinachoitwa **mlinganyo wa Diophantine** - mlinganyo wenye mizizi ya namba nzima. Kwa mfano, fikiria mlinganyo a+2b+3c+4d=30. Unahitaji kupata mizizi ya namba nzima inayokidhi mlinganyo huu.

*Kazi hii imechochewa na [chapisho hili](https://habr.com/post/128704/).*

Vidokezo:

1. Unaweza kuzingatia mizizi kuwa katika kipengele [0;30]
1. Kama jini, fikiria kutumia orodha ya thamani za mizizi

Tumia [Diophantine.ipynb](../../../../../lessons/6-Other/21-GeneticAlgorithms/Diophantine.ipynb) kama sehemu ya kuanzia.

**Kanusho**:  
Hati hii imetafsiriwa kwa kutumia huduma ya kutafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kuhakikisha usahihi, tafadhali fahamu kuwa tafsiri za kiotomatiki zinaweza kuwa na makosa au kutokuwa sahihi. Hati ya asili katika lugha yake ya awali inapaswa kuzingatiwa kama chanzo cha mamlaka. Kwa taarifa muhimu, tafsiri ya kitaalamu ya binadamu inapendekezwa. Hatutawajibika kwa kutoelewana au tafsiri zisizo sahihi zinazotokana na matumizi ya tafsiri hii.