# Algoritmos Genéticos

## [Cuestionario previo a la clase](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/121)

**Algoritmos Genéticos** (GA) se basan en un **enfoque evolutivo** para la IA, en el que se utilizan métodos de la evolución de una población para obtener una solución óptima para un problema dado. Fueron propuestos en 1975 por [John Henry Holland](https://wikipedia.org/wiki/John_Henry_Holland).

Los Algoritmos Genéticos se basan en las siguientes ideas:

* Las soluciones válidas al problema pueden ser representadas como **genes**
* **Crossover** nos permite combinar dos soluciones para obtener una nueva solución válida
* **Selección** se utiliza para seleccionar soluciones más óptimas utilizando alguna **función de aptitud**
* Se introducen **mutaciones** para desestabilizar la optimización y salir del mínimo local

Si deseas implementar un Algoritmo Genético, necesitas lo siguiente:

 * Encontrar un método para codificar nuestras soluciones de problema utilizando **genes** g∈Γ
 * En el conjunto de genes Γ, necesitamos definir la **función de aptitud** fit: Γ→**R**. Los valores más pequeños de la función corresponden a mejores soluciones.
 * Definir un mecanismo de **crossover** para combinar dos genes y obtener una nueva solución válida crossover: Γ<sup>2</sub>→Γ.
 * Definir un mecanismo de **mutación** mutate: Γ→Γ.

En muchos casos, el crossover y la mutación son algoritmos bastante simples para manipular genes como secuencias numéricas o vectores de bits.

La implementación específica de un algoritmo genético puede variar de un caso a otro, pero la estructura general es la siguiente:

1. Seleccionar una población inicial G⊂Γ
2. Seleccionar aleatoriamente una de las operaciones que se realizarán en este paso: crossover o mutación
3. **Crossover**:
  * Seleccionar aleatoriamente dos genes g<sub>1</sub>, g<sub>2</sub> ∈ G
  * Calcular crossover g=crossover(g<sub>1</sub>,g<sub>2</sub>)
  * Si fit(g)<fit(g<sub>1</sub>) o fit(g)<fit(g<sub>2</sub>) - reemplazar el gen correspondiente en la población por g.
4. **Mutación** - seleccionar un gen aleatorio g∈G y reemplazarlo por mutate(g)
5. Repetir desde el paso 2, hasta que obtengamos un valor de fit suficientemente pequeño, o hasta que se alcance el límite en el número de pasos.

## Tareas Típicas

Las tareas que normalmente se resuelven con Algoritmos Genéticos incluyen:

1. Optimización de horarios
1. Empaque óptimo
1. Corte óptimo
1. Aceleración de búsqueda exhaustiva

## ✍️ Ejercicios: Algoritmos Genéticos

Continúa tu aprendizaje en los siguientes cuadernos:

Ve a [este cuaderno](../../../../../lessons/6-Other/21-GeneticAlgorithms/Genetic.ipynb) para ver dos ejemplos de uso de Algoritmos Genéticos:

1. División justa del tesoro
1. Problema de las 8 Reinas

## Conclusión

Los Algoritmos Genéticos se utilizan para resolver muchos problemas, incluidos problemas de logística y búsqueda. El campo se inspira en investigaciones que fusionaron temas de Psicología y Ciencias de la Computación.

## 🚀 Desafío

"Los algoritmos genéticos son simples de implementar, pero su comportamiento es difícil de entender." [fuente](https://wikipedia.org/wiki/Genetic_algorithm) Realiza una investigación para encontrar una implementación de un algoritmo genético, como resolver un rompecabezas de Sudoku, y explica cómo funciona en un esquema o diagrama de flujo.

## [Cuestionario posterior a la clase](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/221)

## Revisión y Autoestudio

Mira [este gran video](https://www.youtube.com/watch?v=qv6UVOQ0F44) que habla sobre cómo las computadoras pueden aprender a jugar Super Mario utilizando redes neuronales entrenadas por algoritmos genéticos. Aprenderemos más sobre cómo las computadoras aprenden a jugar juegos como ese [en la siguiente sección](../22-DeepRL/README.md).

## [Tarea: Ecuación Diofantina](../../../../../lessons/6-Other/21-GeneticAlgorithms/Diophantine.ipynb)

Tu objetivo es resolver la llamada **ecuación diofantina** - una ecuación con raíces enteras. Por ejemplo, considera la ecuación a+2b+3c+4d=30. Necesitas encontrar las raíces enteras que satisfacen esta ecuación.

*Esta tarea está inspirada en [esta publicación](https://habr.com/post/128704/).*

Consejos:

1. Puedes considerar que las raíces están en el intervalo [0;30]
1. Como gen, considera usar la lista de valores de raíz

Utiliza [Diophantine.ipynb](../../../../../lessons/6-Other/21-GeneticAlgorithms/Diophantine.ipynb) como punto de partida.

**Descargo de responsabilidad**:  
Este documento ha sido traducido utilizando servicios de traducción automática basados en IA. Aunque nos esforzamos por lograr la precisión, tenga en cuenta que las traducciones automatizadas pueden contener errores o inexactitudes. El documento original en su idioma nativo debe considerarse la fuente autorizada. Para información crítica, se recomienda una traducción profesional por parte de un humano. No somos responsables de malentendidos o malas interpretaciones que surjan del uso de esta traducción.