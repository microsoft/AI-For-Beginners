# Mga Genetic Algorithm

## [Pre-lecture quiz](https://ff-quizzes.netlify.app/en/ai/quiz/41)

Ang **Genetic Algorithms** (GA) ay nakabatay sa isang **evolutionary approach** sa AI, kung saan ginagamit ang mga pamamaraan ng ebolusyon ng isang populasyon upang makuha ang pinakamainam na solusyon para sa isang partikular na problema. Ito ay iminungkahi noong 1975 ni [John Henry Holland](https://wikipedia.org/wiki/John_Henry_Holland).

Ang Genetic Algorithms ay nakabatay sa mga sumusunod na ideya:

* Ang mga wastong solusyon sa problema ay maaaring i-representa bilang **genes**
* Ang **Crossover** ay nagbibigay-daan upang pagsamahin ang dalawang solusyon upang makabuo ng bagong wastong solusyon
* Ang **Selection** ay ginagamit upang pumili ng mas mainam na solusyon gamit ang isang **fitness function**
* Ang **Mutations** ay ipinapasok upang ma-destabilize ang optimization at makalabas sa local minimum

Kung nais mong mag-implement ng Genetic Algorithm, kailangan mo ng mga sumusunod:

 * Maghanap ng paraan upang i-code ang mga solusyon sa problema gamit ang **genes** g&in;&Gamma;
 * Sa set ng genes &Gamma;, kailangang magtakda ng **fitness function** fit: &Gamma;&rightarrow;**R**. Ang mas mababang halaga ng function ay tumutukoy sa mas mainam na solusyon.
 * Magtakda ng mekanismo ng **crossover** upang pagsamahin ang dalawang genes upang makabuo ng bagong wastong solusyon crossover: &Gamma;<sup>2</sub>&rightarrow;&Gamma;.
 * Magtakda ng mekanismo ng **mutation** mutate: &Gamma;&rightarrow;&Gamma;.

Sa maraming kaso, ang crossover at mutation ay mga simpleng algorithm upang manipulahin ang genes bilang mga numeric sequence o bit vectors.

Ang partikular na implementasyon ng genetic algorithm ay maaaring magbago depende sa kaso, ngunit ang pangkalahatang istruktura ay ang mga sumusunod:

1. Pumili ng panimulang populasyon G&subset;&Gamma;
2. Random na pumili ng isa sa mga operasyon na isasagawa sa hakbang na ito: crossover o mutation
3. **Crossover**:
  * Random na pumili ng dalawang genes g<sub>1</sub>, g<sub>2</sub> &in; G
  * Kalkulahin ang crossover g=crossover(g<sub>1</sub>,g<sub>2</sub>)
  * Kung fit(g)<fit(g<sub>1</sub>) o fit(g)<fit(g<sub>2</sub>) - palitan ang kaukulang gene sa populasyon ng g.
4. **Mutation** - pumili ng random na gene g&in;G at palitan ito ng mutate(g)
5. Ulitin mula sa hakbang 2, hanggang makuha ang sapat na maliit na halaga ng fit, o hanggang maabot ang limitasyon sa bilang ng mga hakbang.

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
1. 8 Queens Problem

## Konklusyon

Ang Genetic Algorithms ay ginagamit upang malutas ang maraming problema, kabilang ang mga problema sa logistics at paghahanap. Ang larangang ito ay inspirasyon ng pananaliksik na pinagsama ang mga paksa sa Psychology at Computer Science.

## 🚀 Hamon

"Ang genetic algorithms ay madaling i-implement, ngunit mahirap maintindihan ang kanilang kilos." [source](https://wikipedia.org/wiki/Genetic_algorithm) Maghanap ng isang implementasyon ng genetic algorithm tulad ng paglutas ng Sudoku puzzle, at ipaliwanag kung paano ito gumagana gamit ang isang sketch o flowchart.

## [Post-lecture quiz](https://ff-quizzes.netlify.app/en/ai/quiz/42)

## Review at Pag-aaral sa Sarili

Panoorin ang [napakagandang video na ito](https://www.youtube.com/watch?v=qv6UVOQ0F44) na nagpapakita kung paano natututo ang computer na maglaro ng Super Mario gamit ang neural networks na sinanay ng genetic algorithms. Matututo tayo ng higit pa tungkol sa computer na natututo maglaro ng mga ganitong laro [sa susunod na seksyon](../22-DeepRL/README.md).

## [Takdang-Aralin: Diophantine Equation](Diophantine.ipynb)

Ang iyong layunin ay lutasin ang tinatawag na **Diophantine equation** - isang equation na may mga integer na ugat. Halimbawa, isaalang-alang ang equation na a+2b+3c+4d=30. Kailangan mong hanapin ang mga integer na ugat na tumutugon sa equation na ito.

*Ang takdang-araling ito ay inspirasyon ng [post na ito](https://habr.com/post/128704/).*

Mga Pahiwatig:

1. Maaari mong isaalang-alang ang mga ugat na nasa interval na [0;30]
1. Bilang gene, isaalang-alang ang paggamit ng listahan ng mga halaga ng ugat

Gamitin ang [Diophantine.ipynb](Diophantine.ipynb) bilang panimulang punto.

---

