# Representación del Conocimiento y Sistemas Expertos

![Summary of Symbolic AI content](../sketchnotes/ai-symbolic.png)

> Sketchnote by [Tomomi Imura](https://twitter.com/girlie_mac)

La búsqueda de la inteligencia artificial se basa en una búsqueda de conocimiento, para dar sentido al mundo de forma similar a como lo hacen los humanos. Pero, ¿cómo se puede hacer esto?

## [Pre-lecture quiz](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/102)

En los primeros días de la IA, el enfoque de arriba hacia abajo para crear sistemas inteligentes (discutido en la lección anterior) era popular. La idea era extraer el conocimiento de las personas en una forma legible por máquina y luego usarlo para resolver problemas automáticamente. Este enfoque se basó en dos grandes ideas:

* Representación del conocimiento
*Razonamiento

## Representación del conocimiento

Uno de los conceptos importantes en la IA simbólica es el **conocimiento**. Es importante diferenciar el conocimiento de la *información* o los *datos*. Por ejemplo, se puede decir que los libros contienen conocimiento, porque uno puede estudiar libros y convertirse en un experto. Sin embargo, lo que contienen los libros en realidad se llama *datos*, y al leer libros e integrar estos datos en nuestro modelo de mundo, convertimos estos datos en conocimiento.

> ✅ **El conocimiento** es algo que está contenido en nuestra cabeza y representa nuestra comprensión del mundo. Se obtiene mediante un proceso activo de **aprendizaje**, que integra piezas de información que recibimos en nuestro modelo activo del mundo.

La mayoría de las veces, no definimos estrictamente el conocimiento, sino que lo alineamos con otros conceptos relacionados utilizando [DIKW Pyramid](https://en.wikipedia.org/wiki/DIKW_pyramid).Contiene los siguientes conceptos:

* **Datos** es algo representado en medios físicos, como texto escrito o palabras habladas. Los datos existen independientemente de los seres humanos y pueden transmitirse entre personas.
* **Información** es la forma en que interpretamos los datos en nuestra cabeza. Por ejemplo, cuando escuchamos la palabra *computadora*, tenemos cierta comprensión de lo que es.
* **Conocimiento** es información que se integra en nuestro modelo de mundo. Por ejemplo, una vez que aprendemos lo que es una computadora, empezamos a tener algunas ideas sobre cómo funciona, cuánto cuesta y para qué se puede utilizar. Esta red de conceptos interrelacionados forma nuestro conocimiento.
* **Sabiduría** es un nivel más de nuestra comprensión del mundo, y representa *meta-conocimiento*, por ejemplo. alguna noción sobre cómo y cuándo se debe utilizar el conocimiento.

  <img src="images/DIKW_Pyramid.png" width="30%"/>

*Image [from Wikipedia](https://commons.wikimedia.org/w/index.php?curid=37705247), By Longlivetheux - Own work, CC BY-SA 4.0*

Por lo tanto, el problema de la **representación del conocimiento** es encontrar alguna forma efectiva de representar el conocimiento dentro de una computadora en forma de datos, para que sea utilizable automáticamente. Esto se puede ver como un espectro:

![Knowledge representation spectrum](images/knowledge-spectrum.png)

> Image by [Dmitry Soshnikov](http://soshnikov.com)

* A la izquierda, hay tipos muy simples de representaciones de conocimiento que pueden ser utilizadas de manera efectiva por las computadoras. La más simple es la algorítmica, cuando el conocimiento está representado por un programa informático. Esta, sin embargo, no es la mejor manera de representar el conocimiento, porque no es flexible. El conocimiento dentro de nuestra cabeza a menudo no es algorítmico.
* A la derecha, hay representaciones como texto natural. Es el más poderoso, pero no se puede usar para el razonamiento automático.

> ✅ Piensa por un minuto en cómo representas el conocimiento en tu cabeza y conviértelo en notas. ¿Hay algún formato en particular que funcione bien para ayudar en la retención?

## Clasificación de representaciones de conocimiento informático
