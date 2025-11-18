<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "6bbd632dfe6c62e5f66bb51fd78c174a",
  "translation_date": "2025-11-18T18:49:38+00:00",
  "source_file": "lessons/6-Other/21-GeneticAlgorithms/README.md",
  "language_code": "pcm"
}
-->
# Genetic Algorithms

## [Pre-lecture quiz](https://ff-quizzes.netlify.app/en/ai/quiz/41)

**Genetic Algorithms** (GA) na method wey dey use **evolutionary approach** for AI, wey dey use how population dey evolve to find better solution for one problem. Na [John Henry Holland](https://wikipedia.org/wiki/John_Henry_Holland) propose am for 1975.

Genetic Algorithms dey base on dis ideas:

* Correct solutions for di problem fit dey represent as **genes**
* **Crossover** dey allow us join two solutions together to get new correct solution
* **Selection** dey help us choose better solutions using one **fitness function**
* **Mutations** dey help scatter optimization small so we fit comot from di local minimum

If you wan do Genetic Algorithm, you go need dis things:

 * Find way to code di problem solutions using **genes** g&in;&Gamma;
 * For di set of genes &Gamma;, you go need define **fitness function** fit: &Gamma;&rightarrow;**R**. Di smaller di function value, di better di solution.
 * Define **crossover** method to join two genes together to get new correct solution crossover: &Gamma;<sup>2</sub>&rightarrow;&Gamma;.
 * Define **mutation** method mutate: &Gamma;&rightarrow;&Gamma;.

Most times, crossover and mutation na simple algorithms wey dey manipulate genes as number sequence or bit vectors.

Di way wey Genetic Algorithm dey work fit change from one case to another, but di general structure be like dis:

1. Choose one initial population G&subset;&Gamma;
2. Randomly choose one operation wey go happen for dis step: crossover or mutation
3. **Crossover**:
  * Randomly choose two genes g<sub>1</sub>, g<sub>2</sub> &in; G
  * Calculate crossover g=crossover(g<sub>1</sub>,g<sub>2</sub>)
  * If fit(g)<fit(g<sub>1</sub>) or fit(g)<fit(g<sub>2</sub>) - replace di gene for di population with g.
4. **Mutation** - choose random gene g&in;G and replace am with mutate(g)
5. Repeat from step 2, until we get one small value of fit, or until di limit for di number of steps don reach.

## Typical Tasks

Di kind tasks wey Genetic Algorithms dey solve na:

1. Schedule optimization
1. Better packing
1. Better cutting
1. Make exhaustive search fast

## ✍️ Exercises: Genetic Algorithms

Continue your learning for di notebooks wey dey here:

Check [dis notebook](Genetic.ipynb) to see two examples of how Genetic Algorithms dey work:

1. How to share treasure well
1. 8 Queens Problem

## Conclusion

Genetic Algorithms dey solve plenty problems, like logistics and search problems. Di field dey inspired by research wey join Psychology and Computer Science together.

## 🚀 Challenge

"Genetic algorithms dey easy to do, but how dem dey behave dey hard to understand." [source](https://wikipedia.org/wiki/Genetic_algorithm) Do small research to find one Genetic Algorithm wey dey solve something like Sudoku puzzle, and explain how e dey work as sketch or flowchart.

## [Post-lecture quiz](https://ff-quizzes.netlify.app/en/ai/quiz/42)

## Review & Self Study

Watch [dis better video](https://www.youtube.com/watch?v=qv6UVOQ0F44) wey dey talk about how computer fit learn to play Super Mario using neural networks wey Genetic Algorithms train. We go learn more about how computer dey learn to play games like dat [for di next section](../22-DeepRL/README.md).

## [Assignment: Diophantine Equation](Diophantine.ipynb)

Your goal na to solve di **Diophantine equation** - equation wey get integer roots. For example, check di equation a+2b+3c+4d=30. You go need find di integer roots wey go make di equation correct.

*Dis assignment dey inspired by [dis post](https://habr.com/post/128704/).*

Hints:

1. You fit think say di roots dey for di interval [0;30]
1. As gene, you fit use di list of root values

Use [Diophantine.ipynb](Diophantine.ipynb) as your starting point.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:  
Dis docu wey you dey see don use AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator) take translate am. Even though we dey try make sure say e correct, abeg no forget say machine translation fit get mistake or no too accurate. Di original docu for di language wey dem first write am na di main correct one. If na important matter, e go better make you use professional human translation. We no go fit take blame for any misunderstanding or wrong interpretation wey fit happen because you use dis translation.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->