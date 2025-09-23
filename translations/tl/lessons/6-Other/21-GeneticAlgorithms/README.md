<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "893aa368cb485da704b466a0f3775587",
  "translation_date": "2025-08-28T02:26:20+00:00",
  "source_file": "lessons/6-Other/21-GeneticAlgorithms/README.md",
  "language_code": "tl"
}
-->
# Mga Genetic Algorithm

## [Pre-lecture quiz](https://ff-quizzes.netlify.app/en/ai/quiz/41)

Ang **Genetic Algorithms** (GA) ay batay sa isang **evolutionary approach** sa AI, kung saan ginagamit ang mga pamamaraan ng ebolusyon ng isang populasyon upang makuha ang pinakamainam na solusyon para sa isang partikular na problema. Iminungkahi ito noong 1975 ni [John Henry Holland](https://wikipedia.org/wiki/John_Henry_Holland).

Ang Genetic Algorithms ay nakabatay sa mga sumusunod na ideya:

* Ang mga wastong solusyon sa problema ay maaaring irepresenta bilang **genes**
* Ang **Crossover** ay nagbibigay-daan upang pagsamahin ang dalawang solusyon upang makakuha ng bagong wastong solusyon
* Ang **Selection** ay ginagamit upang pumili ng mas optimal na solusyon gamit ang isang **fitness function**
* Ang **Mutations** ay ipinapasok upang destabilize ang optimization at makalabas sa local minimum

Kung nais mong mag-implement ng Genetic Algorithm, kailangan mo ang mga sumusunod:

 * Maghanap ng paraan upang i-code ang mga solusyon sa problema gamit ang **genes** g∈Γ
 * Sa set ng genes Γ, kailangang mag-define ng **fitness function** fit: Γ→**R**. Ang mas maliit na halaga ng function ay tumutukoy sa mas mahusay na solusyon.
 * Mag-define ng mekanismo ng **crossover** upang pagsamahin ang dalawang genes upang makakuha ng bagong wastong solusyon crossover: Γ<sup>2</sub>→Γ.
 * Mag-define ng mekanismo ng **mutation** mutate: Γ→Γ.

Sa maraming kaso, ang crossover at mutation ay medyo simpleng algorithm upang manipulahin ang genes bilang numeric sequences o bit vectors.

Ang partikular na implementasyon ng genetic algorithm ay maaaring mag-iba depende sa kaso, ngunit ang pangkalahatang istruktura ay ang mga sumusunod:

1. Pumili ng paunang populasyon G⊂Γ
2. Random na pumili ng isa sa mga operasyon na gagawin sa hakbang na ito: crossover o mutation
3. **Crossover**:
  * Random na pumili ng dalawang genes g<sub>1</sub>, g<sub>2</sub> ∈ G
  * I-compute ang crossover g=crossover(g<sub>1</sub>,g<sub>2</sub>)
  * Kung fit(g)<fit(g<sub>1</sub>) o fit(g)<fit(g<sub>2</sub>) - palitan ang kaukulang gene sa populasyon ng g.
4. **Mutation** - pumili ng random na gene g∈G at palitan ito ng mutate(g)
5. Ulitin mula sa hakbang 2, hanggang makuha ang sapat na maliit na halaga ng fit, o hanggang maabot ang limitasyon ng bilang ng mga hakbang.

## Karaniwang Gawain

Ang mga gawain na karaniwang nalulutas gamit ang Genetic Algorithms ay kinabibilangan ng:

1. Pag-optimize ng iskedyul
1. Optimal na pag-iimpake
1. Optimal na pagputol
1. Pagpapabilis ng exhaustive search

## ✍️ Mga Ehersisyo: Genetic Algorithms

Ipagpatuloy ang iyong pag-aaral sa mga sumusunod na notebook:

Pumunta sa [notebook na ito](Genetic.ipynb) upang makita ang dalawang halimbawa ng paggamit ng Genetic Algorithms:

1. Makatarungang paghahati ng kayamanan
1. Problema ng 8 Reyna

## Konklusyon

Ang Genetic Algorithms ay ginagamit upang malutas ang maraming problema, kabilang ang mga problema sa logistics at paghahanap. Ang larangan ay inspirasyon ng pananaliksik na pinagsama ang mga paksa sa Psychology at Computer Science.

## 🚀 Hamon

"Ang genetic algorithms ay madaling i-implement, ngunit mahirap maintindihan ang kanilang pag-uugali." [source](https://wikipedia.org/wiki/Genetic_algorithm) Mag-research upang makahanap ng implementasyon ng genetic algorithm tulad ng paglutas ng Sudoku puzzle, at ipaliwanag kung paano ito gumagana gamit ang sketch o flowchart.

## [Post-lecture quiz](https://ff-quizzes.netlify.app/en/ai/quiz/42)

## Review at Pag-aaral sa Sarili

Panoorin ang [napakagandang video na ito](https://www.youtube.com/watch?v=qv6UVOQ0F44) na nagpapaliwanag kung paano natututo ang computer na maglaro ng Super Mario gamit ang neural networks na sinanay ng genetic algorithms. Matututo tayo nang higit pa tungkol sa computer na natututo maglaro ng mga ganitong laro [sa susunod na seksyon](../22-DeepRL/README.md).

## [Takdang Aralin: Diophantine Equation](Diophantine.ipynb)

Ang iyong layunin ay lutasin ang tinatawag na **Diophantine equation** - isang equation na may integer roots. Halimbawa, isaalang-alang ang equation na a+2b+3c+4d=30. Kailangan mong hanapin ang integer roots na tumutugma sa equation na ito.

*Ang takdang araling ito ay inspirasyon ng [post na ito](https://habr.com/post/128704/).*

Mga Pahiwatig:

1. Maaari mong isaalang-alang ang roots na nasa interval [0;30]
1. Bilang gene, isaalang-alang ang paggamit ng listahan ng mga root values

Gamitin ang [Diophantine.ipynb](Diophantine.ipynb) bilang panimulang punto.

---

**Paunawa**:  
Ang dokumentong ito ay isinalin gamit ang AI translation service na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagama't sinisikap naming maging tumpak, tandaan na ang mga awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o hindi pagkakatugma. Ang orihinal na dokumento sa kanyang katutubong wika ang dapat ituring na opisyal na sanggunian. Para sa mahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang hindi pagkakaunawaan o maling interpretasyon na maaaring magmula sa paggamit ng pagsasaling ito.