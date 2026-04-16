<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "6bbd632dfe6c62e5f66bb51fd78c174a",
  "translation_date": "2025-09-23T11:42:56+00:00",
  "source_file": "lessons/6-Other/21-GeneticAlgorithms/README.md",
  "language_code": "en"
}
-->
# Genetic Algorithms

## [Pre-lecture quiz](https://ff-quizzes.netlify.app/en/ai/quiz/41)

**Genetic Algorithms** (GA) are based on an **evolutionary approach** to AI, where methods inspired by the evolution of a population are used to find an optimal solution to a given problem. They were introduced in 1975 by [John Henry Holland](https://wikipedia.org/wiki/John_Henry_Holland).

Genetic Algorithms are built on the following principles:

* Valid solutions to the problem can be represented as **genes**.
* **Crossover** allows combining two solutions to create a new valid solution.
* **Selection** is used to choose more optimal solutions based on a **fitness function**.
* **Mutations** are introduced to disrupt optimization and help escape local minima.

To implement a Genetic Algorithm, you need the following:

 * A method to encode problem solutions as **genes** g&in;&Gamma;.
 * A **fitness function** fit: &Gamma;&rightarrow;**R** defined on the set of genes &Gamma;. Smaller values of the function correspond to better solutions.
 * A **crossover** mechanism to combine two genes into a new valid solution: crossover: &Gamma;<sup>2</sub>&rightarrow;&Gamma;.
 * A **mutation** mechanism: mutate: &Gamma;&rightarrow;&Gamma;.

In many cases, crossover and mutation are relatively simple algorithms that manipulate genes as numeric sequences or bit vectors.

The specific implementation of a genetic algorithm can vary, but the general structure is as follows:

1. Select an initial population G&subset;&Gamma;.
2. Randomly choose one of the operations to perform at this step: crossover or mutation.
3. **Crossover**:
  * Randomly select two genes g<sub>1</sub>, g<sub>2</sub> &in; G.
  * Compute crossover g=crossover(g<sub>1</sub>,g<sub>2</sub>).
  * If fit(g)<fit(g<sub>1</sub>) or fit(g)<fit(g<sub>2</sub>), replace the corresponding gene in the population with g.
4. **Mutation**: Select a random gene g&in;G and replace it with mutate(g).
5. Repeat from step 2 until a sufficiently small value of fit is achieved, or until the step limit is reached.

## Typical Tasks

Genetic Algorithms are commonly used to solve tasks such as:

1. Schedule optimization
1. Optimal packing
1. Optimal cutting
1. Accelerating exhaustive search

## ✍️ Exercises: Genetic Algorithms

Continue your learning in the following notebooks:

Visit [this notebook](Genetic.ipynb) to explore two examples of using Genetic Algorithms:

1. Fair division of treasure
1. 8 Queens Problem

## Conclusion

Genetic Algorithms are applied to solve a variety of problems, including logistics and search challenges. This field is inspired by research that combines ideas from Psychology and Computer Science.

## 🚀 Challenge

"Genetic algorithms are simple to implement, but their behavior is difficult to understand." [source](https://wikipedia.org/wiki/Genetic_algorithm) Research an implementation of a genetic algorithm, such as solving a Sudoku puzzle, and explain how it works using a sketch or flowchart.

## [Post-lecture quiz](https://ff-quizzes.netlify.app/en/ai/quiz/42)

## Review & Self Study

Watch [this excellent video](https://www.youtube.com/watch?v=qv6UVOQ0F44) that explains how a computer can learn to play Super Mario using neural networks trained by genetic algorithms. We will explore more about computers learning to play games like this [in the next section](../22-DeepRL/README.md).

## [Assignment: Diophantine Equation](Diophantine.ipynb)

Your task is to solve a **Diophantine equation**—an equation with integer solutions. For example, consider the equation a+2b+3c+4d=30. You need to find the integer solutions that satisfy this equation.

*This assignment is inspired by [this post](https://habr.com/post/128704/).*

Hints:

1. You can assume the roots are in the interval [0;30].
1. Use a list of root values as a gene.

Start with [Diophantine.ipynb](Diophantine.ipynb).

---

