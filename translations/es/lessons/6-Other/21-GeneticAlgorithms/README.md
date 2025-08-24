<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "893aa368cb485da704b466a0f3775587",
  "translation_date": "2025-08-24T09:20:04+00:00",
  "source_file": "lessons/6-Other/21-GeneticAlgorithms/README.md",
  "language_code": "es"
}
-->
# Algoritmos Genéticos

## [Cuestionario previo a la clase](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/121)

Los **Algoritmos Genéticos** (AG) se basan en un **enfoque evolutivo** de la IA, en el que se utilizan métodos de evolución de una población para obtener una solución óptima para un problema dado. Fueron propuestos en 1975 por [John Henry Holland](https://wikipedia.org/wiki/John_Henry_Holland).

Los Algoritmos Genéticos se basan en las siguientes ideas:

* Las soluciones válidas al problema pueden representarse como **genes**.
* El **cruce** nos permite combinar dos soluciones para obtener una nueva solución válida.
* La **selección** se utiliza para elegir las soluciones más óptimas usando alguna **función de aptitud**.
* Se introducen **mutaciones** para desestabilizar la optimización y salir de mínimos locales.

Si deseas implementar un Algoritmo Genético, necesitas lo siguiente:

 * Encontrar un método para codificar las soluciones de nuestro problema usando **genes** g∈Γ.
 * En el conjunto de genes Γ, definir una **función de aptitud** fit: Γ→**R**. Los valores más pequeños de la función corresponden a mejores soluciones.
 * Definir un mecanismo de **cruce** para combinar dos genes y obtener una nueva solución válida crossover: Γ<sup>2</sub>→Γ.
 * Definir un mecanismo de **mutación** mutate: Γ→Γ.

En muchos casos, los algoritmos de cruce y mutación son bastante simples para manipular genes como secuencias numéricas o vectores de bits.

La implementación específica de un algoritmo genético puede variar según el caso, pero la estructura general es la siguiente:

1. Seleccionar una población inicial G⊂Γ.
2. Seleccionar aleatoriamente una de las operaciones que se realizarán en este paso: cruce o mutación.
3. **Cruce**:
  * Seleccionar aleatoriamente dos genes g<sub>1</sub>, g<sub>2</sub> ∈ G.
  * Calcular el cruce g=crossover(g<sub>1</sub>,g<sub>2</sub>).
  * Si fit(g)<fit(g<sub>1</sub>) o fit(g)<fit(g<sub>2</sub>), reemplazar el gen correspondiente en la población por g.
4. **Mutación**: seleccionar un gen aleatorio g∈G y reemplazarlo por mutate(g).
5. Repetir desde el paso 2, hasta obtener un valor suficientemente pequeño de fit, o hasta alcanzar el límite en el número de pasos.

## Tareas típicas

Las tareas que suelen resolverse con Algoritmos Genéticos incluyen:

1. Optimización de horarios
1. Empaque óptimo
1. Corte óptimo
1. Aceleración de búsquedas exhaustivas

## ✍️ Ejercicios: Algoritmos Genéticos

Continúa tu aprendizaje en los siguientes notebooks:

Ve a [este notebook](../../../../../lessons/6-Other/21-GeneticAlgorithms/Genetic.ipynb) para ver dos ejemplos de uso de Algoritmos Genéticos:

1. División justa de un tesoro
1. Problema de las 8 reinas

## Conclusión

Los Algoritmos Genéticos se utilizan para resolver muchos problemas, incluidos problemas de logística y búsqueda. Este campo está inspirado en investigaciones que fusionaron temas de Psicología y Ciencias de la Computación.

## 🚀 Desafío

"Los algoritmos genéticos son simples de implementar, pero su comportamiento es difícil de entender." [fuente](https://wikipedia.org/wiki/Genetic_algorithm) Investiga para encontrar una implementación de un algoritmo genético, como resolver un rompecabezas de Sudoku, y explica cómo funciona mediante un esquema o diagrama de flujo.

## [Cuestionario posterior a la clase](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/221)

## Revisión y autoestudio

Mira [este excelente video](https://www.youtube.com/watch?v=qv6UVOQ0F44) que habla sobre cómo una computadora puede aprender a jugar Super Mario usando redes neuronales entrenadas por algoritmos genéticos. Aprenderemos más sobre cómo las computadoras aprenden a jugar juegos como este [en la siguiente sección](../22-DeepRL/README.md).

## [Asignación: Ecuación Diofántica](../../../../../lessons/6-Other/21-GeneticAlgorithms/Diophantine.ipynb)

Tu objetivo es resolver la llamada **ecuación diofántica**, una ecuación con raíces enteras. Por ejemplo, considera la ecuación a+2b+3c+4d=30. Necesitas encontrar las raíces enteras que satisfacen esta ecuación.

*Esta asignación está inspirada en [este artículo](https://habr.com/post/128704/).*

Pistas:

1. Puedes considerar las raíces en el intervalo [0;30].
1. Como gen, considera usar la lista de valores de las raíces.

Usa [Diophantine.ipynb](../../../../../lessons/6-Other/21-GeneticAlgorithms/Diophantine.ipynb) como punto de partida.

**Descargo de responsabilidad**:  
Este documento ha sido traducido utilizando el servicio de traducción automática [Co-op Translator](https://github.com/Azure/co-op-translator). Si bien nos esforzamos por lograr precisión, tenga en cuenta que las traducciones automáticas pueden contener errores o imprecisiones. El documento original en su idioma nativo debe considerarse como la fuente autorizada. Para información crítica, se recomienda una traducción profesional realizada por humanos. No nos hacemos responsables de malentendidos o interpretaciones erróneas que puedan surgir del uso de esta traducción.