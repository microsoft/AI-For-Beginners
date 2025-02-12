> Imagen de [Dmitry Soshnikov](http://soshnikov.com)

A medida que pasó el tiempo, los recursos informáticos se volvieron más baratos y más datos se hicieron disponibles, por lo que los enfoques de redes neuronales comenzaron a demostrar un gran rendimiento en la competencia con los seres humanos en muchas áreas, como la visión por computadora o la comprensión del habla. En la última década, el término Inteligencia Artificial se ha utilizado principalmente como un sinónimo de Redes Neuronales, ya que la mayoría de los éxitos de IA de los que escuchamos se basan en ellas.

Podemos observar cómo cambiaron los enfoques, por ejemplo, en la creación de un programa de computadora para jugar ajedrez:

* Los primeros programas de ajedrez se basaban en la búsqueda: un programa intentaba estimar explícitamente los posibles movimientos de un oponente para un número determinado de movimientos siguientes y seleccionaba un movimiento óptimo basado en la posición óptima que se puede lograr en unos pocos movimientos. Esto llevó al desarrollo del algoritmo de búsqueda llamado [poda alfa-beta](https://en.wikipedia.org/wiki/Alpha%E2%80%93beta_pruning).
* Las estrategias de búsqueda funcionan bien hacia el final del juego, donde el espacio de búsqueda está limitado por un pequeño número de posibles movimientos. Sin embargo, al principio del juego, el espacio de búsqueda es enorme, y el algoritmo se puede mejorar aprendiendo de partidas existentes entre jugadores humanos. Experimentos posteriores emplearon el llamado [razonamiento basado en casos](https://en.wikipedia.org/wiki/Case-based_reasoning), donde el programa buscaba casos en la base de conocimientos muy similares a la posición actual en el juego.
* Los programas modernos que ganan a los jugadores humanos se basan en redes neuronales y [aprendizaje por refuerzo](https://en.wikipedia.org/wiki/Reinforcement_learning), donde los programas aprenden a jugar únicamente jugando mucho tiempo contra sí mismos y aprendiendo de sus propios errores, de manera similar a como lo hacen los seres humanos al aprender a jugar ajedrez. Sin embargo, un programa de computadora puede jugar muchos más juegos en mucho menos tiempo, y así puede aprender mucho más rápido.

✅ Investiga un poco sobre otros juegos que han sido jugados por IA.

De manera similar, podemos ver cómo cambió el enfoque hacia la creación de "programas que hablan" (que podrían pasar la prueba de Turing):

* Los primeros programas de este tipo, como [Eliza](https://en.wikipedia.org/wiki/ELIZA), se basaban en reglas gramaticales muy simples y la reformulación de la oración de entrada en una pregunta.
* Los asistentes modernos, como Cortana, Siri o Google Assistant, son todos sistemas híbridos que utilizan redes neuronales para convertir el habla en texto y reconocer nuestra intención, y luego emplean algún razonamiento o algoritmos explícitos para realizar las acciones requeridas.
* En el futuro, podemos esperar un modelo completamente basado en redes neuronales para manejar el diálogo por sí mismo. Las recientes redes neuronales de la familia GPT y [Turing-NLG](https://turing.microsoft.com/) muestran un gran éxito en esto.

> Imagen de Dmitry Soshnikov, [foto](https://unsplash.com/photos/r8LmVbUKgns) de [Marina Abrosimova](https://unsplash.com/@abrosimova_marina_foto), Unsplash

## Investigación reciente en IA

El enorme crecimiento reciente en la investigación de redes neuronales comenzó alrededor de 2010, cuando comenzaron a estar disponibles grandes conjuntos de datos públicos. Una enorme colección de imágenes llamada [ImageNet](https://en.wikipedia.org/wiki/ImageNet), que contiene alrededor de 14 millones de imágenes anotadas, dio origen al [Desafío de Reconocimiento Visual a Gran Escala de ImageNet](https://image-net.org/challenges/LSVRC/).

![Precisión de ILSVRC](../../../../lessons/1-Intro/images/ilsvrc.gif)

> Imagen de [Dmitry Soshnikov](http://soshnikov.com)
En 2012, se utilizaron por primera vez las [Redes Neuronales Convolucionales](../4-ComputerVision/07-ConvNets/README.md) en la clasificación de imágenes, lo que llevó a una disminución significativa de los errores de clasificación (de casi 30% a 16.4%). En 2015, la arquitectura ResNet de Microsoft Research [alcanzó una precisión a nivel humano](https://doi.org/10.1109/ICCV.2015.123).

Desde entonces, las Redes Neuronales han demostrado un comportamiento muy exitoso en muchas tareas:

---

Año | Paridad Humana alcanzada
-----|--------
2015 | [Clasificación de Imágenes](https://doi.org/10.1109/ICCV.2015.123)
2016 | [Reconocimiento de Voz Conversacional](https://arxiv.org/abs/1610.05256)
2018 | [Traducción Automática de Máquinas](https://arxiv.org/abs/1803.05567) (chino-inglés)
2020 | [Generación de Descripciones de Imágenes](https://arxiv.org/abs/2009.13682)

En los últimos años hemos sido testigos de grandes éxitos con modelos de lenguaje de gran tamaño, como BERT y GPT-3. Esto ocurrió principalmente debido al hecho de que hay una gran cantidad de datos de texto general disponibles que nos permiten entrenar modelos para capturar la estructura y el significado de los textos, preentrenarlos en colecciones de texto generales y luego especializar esos modelos para tareas más específicas. Aprenderemos más sobre [Procesamiento de Lenguaje Natural](../5-NLP/README.md) más adelante en este curso.

## 🚀 Desafío

Haz un recorrido por internet para determinar dónde, en tu opinión, se utiliza la IA de manera más efectiva. ¿Es en una aplicación de mapeo, en algún servicio de reconocimiento de voz a texto o en un videojuego? Investiga cómo se construyó el sistema.

## [Cuestionario posterior a la clase](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/201)

## Revisión y Autoestudio

Revisa la historia de la IA y el ML leyendo [esta lección](https://github.com/microsoft/ML-For-Beginners/tree/main/1-Introduction/2-history-of-ML). Toma un elemento de la sketchnote en la parte superior de esa lección o de esta y investígalo más a fondo para entender el contexto cultural que informa su evolución.

**Tarea**: [Game Jam](assignment.md)

**Descargo de responsabilidad**:  
Este documento ha sido traducido utilizando servicios de traducción automática basados en IA. Si bien nos esforzamos por lograr precisión, tenga en cuenta que las traducciones automáticas pueden contener errores o inexactitudes. El documento original en su idioma nativo debe considerarse la fuente autorizada. Para información crítica, se recomienda una traducción profesional humana. No somos responsables de malentendidos o malas interpretaciones que surjan del uso de esta traducción.