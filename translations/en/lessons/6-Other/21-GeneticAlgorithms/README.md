<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "893aa368cb485da704b466a0f3775587",
  "translation_date": "2025-08-31T17:30:30+00:00",
  "source_file": "lessons/6-Other/21-GeneticAlgorithms/README.md",
  "language_code": "en"
}
-->
# Genetic Algorithms

## [Pre-lecture quiz](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/121)

**Genetic Algorithms** (GA) are based on an **evolutionary approach** to AI, where methods inspired by the evolution of a population are used to find an optimal solution to a given problem. They were introduced in 1975 by [John Henry Holland](https://wikipedia.org/wiki/John_Henry_Holland).

Genetic Algorithms are built on the following principles:

* Valid solutions to the problem can be represented as **genes**.
* **Crossover** allows combining two solutions to create a new valid solution.
* **Selection** is used to choose more optimal solutions based on a **fitness function**.
* **Mutations** are introduced to disrupt optimization and help escape local minima.

To implement a Genetic Algorithm, you need the following:

 * A method to encode problem solutions as **genes** g∈Γ.
 * A **fitness function** fit: Γ→**R** defined on the set of genes Γ. Smaller function values correspond to better solutions.
 * A **crossover** mechanism to combine two genes into a new valid solution: crossover: Γ<sup>2</sub>→Γ.
 * A **mutation** mechanism: mutate: Γ→Γ.

In many cases, crossover and mutation are relatively simple algorithms that manipulate genes as numeric sequences or bit vectors.

The specific implementation of a genetic algorithm can vary, but the general structure is as follows:

1. Select an initial population G⊂Γ.
2. Randomly choose one of the operations to perform at this step: crossover or mutation.
3. **Crossover**:
  * Randomly select two genes g<sub>1</sub>, g<sub>2</sub> ∈ G.
  * Compute crossover g=crossover(g<sub>1</sub>,g<sub>2</sub>).
  * If fit(g)<fit(g<sub>1</sub>) or fit(g)<fit(g<sub>2</sub>), replace the corresponding gene in the population with g.
4. **Mutation**: Select a random gene g∈G and replace it with mutate(g).
5. Repeat from step 2 until a sufficiently small value of fit is achieved, or until the step limit is reached.

## Typical Tasks

Tasks commonly solved by Genetic Algorithms include:

1. Schedule optimization
1. Optimal packing
1. Optimal cutting
1. Accelerating exhaustive search

## ✍️ Exercises: Genetic Algorithms

Continue your learning in the following notebooks:

Check out [this notebook](Genetic.ipynb) to explore two examples of using Genetic Algorithms:

1. Fair division of treasure
1. 8 Queens Problem

## Conclusion

Genetic Algorithms are used to solve a variety of problems, including logistics and search challenges. The field is inspired by research that combines ideas from Psychology and Computer Science.

## 🚀 Challenge

"Genetic algorithms are simple to implement, but their behavior is difficult to understand." [source](https://wikipedia.org/wiki/Genetic_algorithm) Research an implementation of a genetic algorithm, such as solving a Sudoku puzzle, and explain how it works using a sketch or flowchart.

## [Post-lecture quiz](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/221)

## Review & Self Study

Watch [this excellent video](https://www.youtube.com/watch?v=qv6UVOQ0F44) that explains how a computer can learn to play Super Mario using neural networks trained by genetic algorithms. We will explore more about computers learning to play games like this [in the next section](../22-DeepRL/README.md).

## [Assignment: Diophantine Equation](Diophantine.ipynb)

Your task is to solve a **Diophantine equation**—an equation with integer solutions. For example, consider the equation a+2b+3c+4d=30. You need to find the integer solutions that satisfy this equation.

*This assignment is inspired by [this post](https://habr.com/post/128704/).*

Hints:

1. You can assume the solutions are in the interval [0;30].
1. Use a list of root values as the gene representation.

Start with [Diophantine.ipynb](Diophantine.ipynb).

---

**Disclaimer**:  
This document has been translated using the AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). While we aim for accuracy, please note that automated translations may include errors or inaccuracies. The original document in its native language should be regarded as the authoritative source. For critical information, professional human translation is advised. We are not responsible for any misunderstandings or misinterpretations resulting from the use of this translation.