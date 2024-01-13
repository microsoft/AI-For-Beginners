# Algoritmos genéticos

## [Pre-lecture quiz](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/121)

Los **Algoritmos genéticos** (GA) se basan en un **enfoque evolutivo** de la IA, en el que se utilizan métodos de evolución de una población para obtener una solución óptima para un problema determinado. Fueron propuestos en 1975 por [John Henry Holland](https://wikipedia.org/wiki/John_Henry_Holland).

Los algoritmos genéticos se basan en las siguientes ideas:

* Las soluciones válidas al problema se pueden representar como **genes**
* **Crossover** nos permite combinar dos soluciones para obtener una nueva solución válida
* **Selección** se utiliza para seleccionar soluciones más óptimas usando alguna **función de fitness**
* **Se introducen mutaciones** para desestabilizar la optimización y sacarnos del mínimo local

Si desea implementar un algoritmo genético, necesita lo siguiente:

  * Encontrar un método para codificar las soluciones de nuestros problemas utilizando **genes** g&in;&Gamma;
  * Sobre el conjunto de genes &Gamma; Necesitamos definir **función de aptitud** ajuste: &Gamma;&rightarrow;**R**. Los valores de función más pequeños corresponden a mejores soluciones.
  * Definir el mecanismo de **cruce** para combinar dos genes para obtener una nueva solución de cruce válida: &Gamma;<sup>2</sub>&rightarrow;&Gamma;.
  * Para definir el mecanismo de **mutación** mutar: &Gamma;&rightarrow;&Gamma;.

En muchos casos, el cruce y la mutación son algoritmos bastante simples para manipular genes como secuencias numéricas o vectores de bits.

La implementación específica de un algoritmo genético puede variar de un caso a otro, pero la estructura general es la siguiente:

1. Seleccione una población inicial G=&Gamma;
2. Seleccione aleatoriamente una de las operaciones que se realizarán en este paso: cruce o mutación
3. **Cruce**:
   * Seleccione aleatoriamente dos genes g<sub>1</sub>, g<sub>2</sub> &in; GRAMO
   * Calcular el cruce g=crossover(g<sub>1</sub>,g<sub>2</sub>)
   * Si fit(g)<fit(g<sub>1</sub>) o fit(g)<fit(g<sub>2</sub>) - reemplace el gen correspondiente en la población por g.
4. **Mutación**: seleccione el gen aleatorio g&in;G y reemplácelo por mutate(g)
5. Repita desde el paso 2, hasta que obtengamos un valor de ajuste suficientemente pequeño, o hasta que se alcance el límite en el número de pasos.

## Tareas típicas

Las tareas que normalmente resuelven los algoritmos genéticos incluyen:

1. Optimización de horarios
1. Embalaje óptimo
1. Corte óptimo
1. Acelerar la búsqueda exhaustiva

## ✍️ Ejercicios: Algoritmos Genéticos

Continúa tu aprendizaje en los siguientes cuadernos:

Ir a [this notebook](Genetic.ipynb) para ver dos ejemplos de uso de Algoritmos Genéticos:

1. División justa del tesoro
1. Problema de las 8 reinas

## Conclusión

Los algoritmos genéticos se utilizan para resolver muchos problemas, incluidos problemas de logística y búsqueda. El campo está inspirado en investigaciones que fusionaron temas de Psicología e Informática.

## 🚀 Desafío

"Los algoritmos genéticos son sencillos de implementar, pero su comportamiento es difícil de entender" [source](https://wikipedia.org/wiki/Genetic_algorithm) Investigue un poco para encontrar una implementación de un algoritmo genético, como resolver un Sudoku, y explique cómo funciona como un boceto o diagrama de flujo.

## [Post-lecture quiz](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/221)

## Revisión y autoestudio

Mirar [this great video](https://www.youtube.com/watch?v=qv6UVOQ0F44) hablando de cómo una computadora puede aprender a jugar Super Mario usando redes neuronales entrenadas por algoritmos genéticos. Aprenderemos más sobre el aprendizaje por computadora para jugar juegos como ese [in the next section](../22-DeepRL/README.md).

## [Assignment: Diophantine Equation](Diophantine.ipynb)

Tu objetivo es resolver la llamada **ecuación diofántica**, una ecuación con raíces enteras. Por ejemplo, considere la ecuación a+2b+3c+4d=30. Necesitas encontrar las raíces enteras que satisfagan esta ecuación.

*Esta tarea está inspirada en [this post](https://habr.com/post/128704/).*

Consejos:

1. Puedes considerar que las raíces están en el intervalo [0;30]
1. Como gen, considere usar la lista de valores raíz.

Usar [Diophantine.ipynb](Diophantine.ipynb) como punto de partida.
