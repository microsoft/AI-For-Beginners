# Genetic Algorithms

**Genetic Algorithms** (GA) are based on **evolutionary approach** to AI, in which methods of evolution of population is used to obtain an optimal solution for a given problem. They were proposed in 1975 by [John Henry Holland](https://en.wikipedia.org/wiki/John_Henry_Holland).

Genetic Algorithms are based on the following ideas:

* Valid solutions to the problem can be represented as **genes**
* **Crossover** allows us to combine two solutions together to obtain new valid solution
* **Selection** is used to select more optimal solutions using some **fitness function**
* **Mutations** are introduced to destabilize optimization and get us out of the local minimum 

If you want to implement a Genetic Algorithm, you need the following:

 * To find a method of coding our problem solutions using **genes** g&in;&Gamma;
 * On the set of genes &Gamma; we need to define **fitness function** fit: &Gamma;&rightarrow;**R**. Smaller function values correspond to better solutions.
 * To define **crossover** mechanism to combine two genes together to get a new valid solution crossover: &Gamma;<sup>2</sub>&rightarrow;&Gamma;.
 * To define **mutation** mechanism mutate: &Gamma;&rightarrow;&Gamma;.
In many cases, crossover and mutation are quite simple algorithms to manipulate genes as numeric sequences or bit vectors.

Specific implementation of a genetic algorithm can vary from case to case, but overall structure is the following:

1. Select initial population G&subset;&Gamma;
2. Randomly select one of the operations that will be performed at this step: crossover or mutation 
3. **Crossover**:
  * Randomly select two genes g<sub>1</sub>, g<sub>2</sub> &in; G
  * Compute crossover g=crossover(g<sub>1</sub>,g<sub>2</sub>)
  * If fit(g)<fit(g<sub>1</sub>) or fit(g)<fit(g<sub>2</sub>) - replace corresponding gene in the population by g.
4. **Mutation** - select random gene g&in;G and replace it by mutate(g)
5. Repeat from step 2, until we get sufficiently small value of fit, or until the limit on the number of steps is reached.

## Typical Tasks

Tasks typically solved by GA:
1. Schedule optimization
1. Optimal packing
1. Optimal cutting
1. Speeding up exhaustive search


## Notebooks

Go to [Genetic.ipynb](Genetic.ipynb) notebooks to see two examples of using Genetic Algorithms:

1. Fair division of treasure
1. 8 Queen Problem

## Assignment

Your goal is to solve so-called **Diophantine equation** - an equation with integer roots. For example, consider the equation a+2b+3c+4d=30. You need to find integer roots that satisfy this equation.

Hints:
1. You can consider roots to be in the interval [0;30]
1. As a gene, consider using the list of root values

Use [Diophantine.ipynb](Diophantine.ipynb) as a starting point.

*This assignment is inspired by [this post](https://habr.com/post/128704/).*
