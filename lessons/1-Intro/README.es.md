# Introducción a la IA

![Summary of Introduction of AI content in a doodle](../sketchnotes/ai-intro.png)

> Sketchnote by [Tomomi Imura](https://twitter.com/girlie_mac)

## [Pre-lecture quiz](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/101)

**La Inteligencia Artificial** es una apasionante disciplina científica que estudia cómo podemos hacer que las computadoras muestren un comportamiento inteligente, p. hacer aquellas cosas que los seres humanos hacen bien.
Originalmente, las computadoras fueron inventadas por [Charles Babbage](https://en.wikipedia.org/wiki/Charles_Babbage) para operar con números siguiendo un procedimiento bien definido - un algoritmo. Las computadoras modernas, aunque significativamente más avanzadas que el modelo original propuesto en el siglo XIX, todavía siguen la misma idea de cálculos controlados. Por lo tanto, es posible programar una computadora para que haga algo si conocemos la secuencia exacta de pasos que debemos seguir para lograr el objetivo.
![Photo of a person](images/dsh_age.png)

> Foto de [Vickie Soshnikova](http://twitter.com/vickievalerie)

> ✅ Definir la edad de una persona a partir de su fotografía es una tarea que no se puede programar explícitamente, porque no sabemos cómo se nos ocurre un número dentro de la cabeza cuando lo hacemos.
---

Sin embargo, hay algunas tareas que no sabemos explícitamente cómo resolver. Considere determinar la edad de una persona a partir de su fotografía. De alguna manera aprendemos a hacerlo, porque hemos visto muchos ejemplos de personas de diferentes edades, pero no podemos explicar explícitamente cómo lo hacemos, ni podemos programar la computadora para que lo haga. Este es exactamente el tipo de tarea que interesa a la **Inteligencia Artificial** (IA para abreviar).
> ✅ Piense en algunas tareas que podría descargar a una computadora que se beneficiaría de la IA. Consideremos los campos de las finanzas, la medicina y las artes: ¿cómo se benefician hoy estos campos de la IA?

## IA débil versus IA fuerte

La tarea de resolver un problema humano específico, como determinar la edad de una persona a partir de una fotografía, se puede llamar **IA débil**, porque estamos creando un sistema para una sola tarea, y no un sistema que pueda resolver muchas. tareas que pueden ser realizadas por un ser humano. Por supuesto, el desarrollo de un sistema informático generalmente inteligente también es muy interesante desde muchos puntos de vista, también para los estudiantes de filosofía de la conciencia. Dicho sistema se llamaría **Fuerte IA** o  **[Artificial General Intelligence](https://en.wikipedia.org/wiki/Artificial_general_intelligence)** (AGI).

## La definición de inteligencia y el test de Turing

Uno de los problemas al abordar el término **[Intelligence](https://en.wikipedia.org/wiki/Intelligence)** es que no existe una definición clara de este término. Se puede argumentar que la inteligencia está relacionada con el **pensamiento abstracto** o con la **autoconciencia**, pero no podemos definirlo adecuadamente.

![Foto de un gato](images/photo-cat.jpg)

> [Photo](https://unsplash.com/photos/75715CVEJhI) by [Amber Kipp](https://unsplash.com/@sadmax) from Unsplash

Para ver la ambigüedad de un término *inteligencia*, intenta responder a una pregunta: "¿Es inteligente un gato?". Diferentes personas tienden a dar diferentes respuestas a esta pregunta, ya que no existe una prueba universalmente aceptada para demostrar que la afirmación es cierta o no. Y si crees que sí, prueba a someter a tu gato a una prueba de coeficiente intelectual...

✅ Piensa por un minuto en cómo defines la inteligencia. ¿Es inteligente un cuervo que puede resolver un laberinto y llegar a algo de comida? ¿Es inteligente un niño?

---

Cuando hablamos de AGI, necesitamos tener alguna forma de saber si hemos creado un sistema verdaderamente inteligente. [Alan Turing](https://en.wikipedia.org/wiki/Alan_Turing) propuso una forma llamada **[Turing Test](https://en.wikipedia.org/wiki/Turing_test)**, que también actúa como una definición de inteligencia. La prueba compara un sistema dado con algo inherentemente inteligente: un ser humano real, y debido a que cualquier comparación automática puede ser eludida por un programa de computadora, usamos un interrogador humano. Por lo tanto, si un ser humano es incapaz de distinguir entre una persona real y un sistema informático en un diálogo basado en texto, el sistema se considera inteligente.

> Un chat-bot llamado [Eugene Goostman](https://en.wikipedia.org/wiki/Eugene_Goostman), desarrollado en San Petersburgo, estuvo a punto de pasar el test de Turing en 2014 mediante el uso de un ingenioso truco de personalidad. Anunciaba por adelantado que se trataba de un niño ucraniano de 13 años, lo que explicaría la falta de conocimiento y algunas discrepancias en el texto. El bot convenció al 30% de los jueces de que era humano después de un diálogo de 5 minutos, una métrica que Turing creía que una máquina sería capaz de pasar en el año 2000. Sin embargo, hay que entender que esto no indica que hayamos creado un sistema inteligente, o que un sistema informático haya engañado al interrogador humano: ¡el sistema no engañó a los humanos, sino que lo hicieron los creadores de los bots!

✅ ¿Alguna vez has sido engañado por un bot de chat para que pienses que estás hablando con un humano? ¿Cómo te convenció?

## Diferentes enfoques de la IA

Si queremos que una computadora se comporte como un humano, necesitamos de alguna manera modelar dentro de una computadora nuestra forma de pensar. En consecuencia, tenemos que tratar de entender qué es lo que hace que un ser humano sea inteligente.

> Para poder programar la inteligencia en una máquina, necesitamos entender cómo funcionan nuestros propios procesos de toma de decisiones. Si haces un poco de introspección, te darás cuenta de que hay algunos procesos que ocurren inconscientemente, por ejemplo. Podemos distinguir a un gato de un perro sin pensar en ello, mientras que otros implican razonamiento.

Hay dos enfoques posibles para este problema:

Enfoque de arriba hacia abajo (razonamiento simbólico) | Enfoque ascendente (redes neuronales)
-------------------------------------------------------|-----------------------------------------------------
Un enfoque de arriba hacia abajo modela la forma en que una persona razona para resolver un problema. Consiste en extraer **conocimiento** de un ser humano y representarlo en una forma legible por computadora. También necesitamos desarrollar una forma de modelar el **razonamiento** dentro de una computadora. | Un enfoque ascendente modela la estructura de un cerebro humano, que consiste en un gran número de unidades simples llamadas **neuronas**. Cada neurona actúa como un promedio ponderado de sus entradas, y podemos entrenar una red de neuronas para resolver problemas útiles proporcionando **datos de entrenamiento**.

También hay otros enfoques posibles de la inteligencia:

* Un enfoque **Emergente**, **Sinérgico** o **multi-agente** se basa en el hecho de que se puede obtener un comportamiento inteligente complejo mediante la interacción de un gran número de agentes simples. Según [evolutionary cybernetics](https://en.wikipedia.org/wiki/Global_brain#Evolutionary_cybernetics), La inteligencia puede *emerger* de un comportamiento más simple y reactivo en el proceso de *transición del metasistema*.
  
* Un **enfoque evolutivo**, o **algoritmo genético** es un proceso de optimización basado en los principios de la evolución.
  
Consideraremos esos enfoques más adelante en el curso, pero en este momento nos centraremos en dos direcciones principales: de arriba hacia abajo y de abajo hacia arriba.

### El enfoque de arriba hacia abajo

En un **enfoque de arriba hacia abajo**, tratamos de modelar nuestro razonamiento.  Debido a que podemos seguir nuestros pensamientos cuando razonamos, podemos tratar de formalizar este proceso y programarlo dentro de la computadora. A esto se le llama **razonamiento simbólico**.

Las personas tienden a tener algunas reglas en su cabeza que guían sus procesos de toma de decisiones. Por ejemplo, cuando un médico está diagnosticando a un paciente, puede darse cuenta de que una persona tiene fiebre y, por lo tanto, puede haber algo de inflamación dentro del cuerpo. Al aplicar un gran conjunto de reglas a un problema específico, un médico puede llegar al diagnóstico final.

Este enfoque se basa en gran medida en la **representación del conocimiento** y el **razonamiento**. Extraer el conocimiento de un experto humano puede ser la parte más difícil, porque un médico en muchos casos no sabría exactamente por qué está llegando a un diagnóstico en particular. A veces, la solución simplemente surge en su cabeza sin pensar explícitamente. Algunas tareas, como determinar la edad de una persona a partir de una fotografía, no pueden reducirse en absoluto a manipular el conocimiento.

### Enfoque ascendente

Alternativamente, podemos intentar modelar los elementos más simples dentro de nuestro cerebro: una neurona. Podemos construir una llamada **red neuronal artificial** dentro de una computadora, y luego tratar de enseñarle a resolver problemas dándole ejemplos. Este proceso es similar a la forma en que un niño recién nacido aprende sobre su entorno haciendo observaciones.

✅ Investigue un poco sobre cómo aprenden los bebés. ¿Cuáles son los elementos básicos del cerebro de un bebé?

> | ¿Qué pasa con el aprendizaje automático?         |      |
> |--------------|-----------|
> | Parte de la Inteligencia Artificial que se basa en el aprendizaje informático para resolver un problema basado en unos datos se denomina **Machine Learning**. No consideraremos el aprendizaje automático clásico en este curso, lo remitimos a un [Machine Learning for Beginners](http://aka.ms/ml-beginners) currículo. |   ![ML for Beginners](images/ml-for-beginners.png)    |

## Breve historia de la IA

La Inteligencia Artificial se inició como campo a mediados del siglo XX. Inicialmente, el razonamiento simbólico era un enfoque prevalente, y condujo a una serie de éxitos importantes, como los sistemas expertos, programas informáticos que eran capaces de actuar como expertos en algunos dominios problemáticos limitados. Sin embargo, pronto quedó claro que este enfoque no se adapta bien.Extraer el conocimiento de un experto, representarlo en una computadora y mantener esa base de conocimiento precisa resulta ser una tarea muy compleja y demasiado costosa para ser práctica en muchos casos. Esto llevó a los llamados [AI Winter](https://en.wikipedia.org/wiki/AI_winter) en la década de 1970.

<img alt="Brief History of AI" src="images/history-of-ai.png" width="70%"/>

> Imagen de [Dmitry Soshnikov](http://soshnikov.com)

Con el paso del tiempo, los recursos informáticos se volvieron más baratos y se dispuso de más datos, por lo que los enfoques de redes neuronales comenzaron a demostrar un gran rendimiento para competir con los seres humanos en muchas áreas, como la visión por computadora o la comprensión del habla. En la última década, el término Inteligencia Artificial se ha utilizado principalmente como sinónimo de Redes Neuronales, porque la mayoría de los éxitos de la IA de los que oímos hablar se basan en ellas.

Podemos observar cómo cambiaron los enfoques, por ejemplo, en la creación de un programa informático para jugar al ajedrez:

* Los primeros programas de ajedrez se basaban en la búsqueda: un programa intentaba explícitamente estimar los posibles movimientos de un oponente para un número determinado de movimientos siguientes, y seleccionaba un movimiento óptimo basado en la posición óptima que se puede lograr en unos pocos movimientos. Condujo al desarrollo de la llamada [alpha-beta pruning](https://en.wikipedia.org/wiki/Alpha%E2%80%93beta_pruning) algoritmo de búsqueda.
* Las estrategias de búsqueda funcionan bien hacia el final del juego, donde el espacio de búsqueda está limitado por un pequeño número de movimientos posibles. Sin embargo, al comienzo del juego, el espacio de búsqueda es enorme y el algoritmo se puede mejorar aprendiendo de las coincidencias existentes entre jugadores humanos. En experimentos posteriores se emplearon los llamados [case-based reasoning](https://en.wikipedia.org/wiki/Case-based_reasoning), donde el programa buscaba casos en la base de conocimiento muy similares a la posición actual en el juego.
* Los programas modernos que conquistan a los jugadores humanos se basan en redes neuronales y [reinforcement learning](https://en.wikipedia.org/wiki/Reinforcement_learning), donde los programas aprenden a jugar únicamente jugando mucho tiempo contra sí mismos y aprendiendo de sus propios errores, al igual que lo hacen los seres humanos cuando aprenden a jugar al ajedrez. Sin embargo, un programa de computadora puede jugar muchos más juegos en mucho menos tiempo y, por lo tanto, puede aprender mucho más rápido.

✅ Investiga un poco sobre otros juegos que han sido jugados por IA.

Del mismo modo, podemos ver cómo cambió el enfoque hacia la creación de "programas parlantes" (que podrían pasar el test de Turing):

* Los primeros programas de este tipo, tales como [Eliza](https://en.wikipedia.org/wiki/ELIZA), se basaban en reglas gramaticales muy simples y en la reformulación de la oración introducida en una pregunta.
* Los asistentes modernos, como Cortana, Siri o Google Assistant son todos sistemas híbridos que utilizan redes neuronales para convertir el habla en texto y reconocer nuestra intención, y luego emplean algunos algoritmos de razonamiento o explícitos para realizar las acciones requeridas.
* En el futuro, podemos esperar un modelo completo basado en neuronas que maneje el diálogo por sí mismo. El reciente GPT y [Turing-NLG](https://turing.microsoft.com/) familia de redes neuronales muestran un gran éxito en esto.

<img alt="the Turing test's evolution" src="images/turing-test-evol.png" width="70%"/>

> Imagen de Dmitry Soshnikov, [photo](https://unsplash.com/photos/r8LmVbUKgns) by [Marina Abrosimova](https://unsplash.com/@abrosimova_marina_foto), Unsplash

## Investigación reciente sobre IA

El enorme crecimiento reciente en la investigación de redes neuronales comenzó alrededor de 2010, cuando grandes conjuntos de datos públicos comenzaron a estar disponibles. Una enorme colección de imágenes llamada [ImageNet](https://en.wikipedia.org/wiki/ImageNet), que contiene alrededor de 14 millones de imágenes anotadas, dio origen a la [ImageNet Large Scale Visual Recognition Challenge](https://image-net.org/challenges/LSVRC/).

![ILSVRC Accuracy](images/ilsvrc.gif)

> Imagen de [Dmitry Soshnikov](http://soshnikov.com)

En 2012, [Convolutional Neural Networks](../4-ComputerVision/07-ConvNets/README.md) se utilizaron por primera vez en la clasificación de imágenes, lo que condujo a una caída significativa en los errores de clasificación (de casi el 30% al 16,4%). En 2015, la arquitectura ResNet de Microsoft Research [achieved human-level accuracy](https://doi.org/10.1109/ICCV.2015.123).

Desde entonces, las Redes Neuronales han demostrado un comportamiento muy exitoso en muchas tareas:

---

Año  | Paridad Humana lograda
-----|--------
2015 | [Image Classification](https://doi.org/10.1109/ICCV.2015.123)
2016 | [Conversational Speech Recognition](https://arxiv.org/abs/1610.05256)
2018 | [Automatic Machine Translation](https://arxiv.org/abs/1803.05567) (Chinese-to-English)
2020 | [Image Captioning](https://arxiv.org/abs/2009.13682)

En los últimos años hemos sido testigos de grandes éxitos con grandes modelos de lenguaje, como BERT y GPT-3. Esto sucedió principalmente debido al hecho de que hay una gran cantidad de datos de texto general disponibles que nos permiten entrenar modelos para capturar la estructura y el significado de los textos, entrenarlos previamente en colecciones de texto generales y luego especializar esos modelos para tareas más específicas. Aprenderemos más sobre [Natural Language Processing](../5-NLP/README.md) más adelante en este curso.

## 🚀 Desafiar

Haga un recorrido por Internet para determinar dónde, en su opinión, se utiliza la IA de manera más efectiva. ¿Está en una aplicación de mapas, o en algún servicio de voz a texto o en un videojuego? Investiga cómo se construyó el sistema.

## [Post-lecture quiz](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/201)

## Repaso y autoestudio

Revise la historia de la IA y el ML leyendo [this lesson](https://github.com/microsoft/ML-For-Beginners/tree/main/1-Introduction/2-history-of-ML). Toma un elemento de la nota de boceto en la parte superior de esa lección o de esta otra e investiga con más profundidad para comprender el contexto cultural que informa su evolución.

**Assignment**: [Game Jam](assignment.md):
