# Representación del Conocimiento y Sistemas Expertos

![Resumen del contenido de IA Simbólica](../../../../translated_images/ai-symbolic.715a30cb610411a6964d2e2f23f24364cb338a07cb4844c1f97084d366e586c3.es.png)

> Sketchnote de [Tomomi Imura](https://twitter.com/girlie_mac)

La búsqueda de inteligencia artificial se basa en la búsqueda de conocimiento, para entender el mundo de manera similar a como lo hacen los humanos. Pero, ¿cómo se puede llevar a cabo esto?

## [Cuestionario previo a la clase](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/102)

En los primeros días de la IA, el enfoque de arriba hacia abajo para crear sistemas inteligentes (discutido en la lección anterior) era popular. La idea era extraer el conocimiento de las personas en una forma legible por máquina y luego usarlo para resolver problemas automáticamente. Este enfoque se basaba en dos grandes ideas:

* Representación del Conocimiento
* Razonamiento

## Representación del Conocimiento

Uno de los conceptos importantes en la IA Simbólica es el **conocimiento**. Es importante diferenciar el conocimiento de la *información* o *datos*. Por ejemplo, se puede decir que los libros contienen conocimiento, porque uno puede estudiar libros y convertirse en un experto. Sin embargo, lo que contienen los libros se llama en realidad *datos*, y al leer libros e integrar estos datos en nuestro modelo del mundo, convertimos estos datos en conocimiento.

> ✅ **El conocimiento** es algo que está contenido en nuestra cabeza y representa nuestra comprensión del mundo. Se obtiene a través de un proceso activo de **aprendizaje**, que integra piezas de información que recibimos en nuestro modelo activo del mundo.

A menudo, no definimos estrictamente el conocimiento, sino que lo alineamos con otros conceptos relacionados utilizando la [Pirámide DIKW](https://en.wikipedia.org/wiki/DIKW_pyramid). Contiene los siguientes conceptos:

* **Datos** son algo representado en medios físicos, como texto escrito o palabras habladas. Los datos existen independientemente de los seres humanos y pueden ser transmitidos entre personas.
* **Información** es cómo interpretamos los datos en nuestra cabeza. Por ejemplo, cuando escuchamos la palabra *computadora*, tenemos alguna comprensión de lo que es.
* **Conocimiento** es la información que se integra en nuestro modelo del mundo. Por ejemplo, una vez que aprendemos lo que es una computadora, comenzamos a tener algunas ideas sobre cómo funciona, cuánto cuesta y para qué se puede usar. Esta red de conceptos interrelacionados forma nuestro conocimiento.
* **Sabiduría** es un nivel más de nuestra comprensión del mundo y representa *meta-conocimiento*, es decir, alguna noción sobre cómo y cuándo se debe usar el conocimiento.

<img src="images/DIKW_Pyramid.png" width="30%"/>

*Imagen [de Wikipedia](https://commons.wikimedia.org/w/index.php?curid=37705247), Por Longlivetheux - Trabajo propio, CC BY-SA 4.0*

Así, el problema de la **representación del conocimiento** es encontrar alguna manera efectiva de representar el conocimiento dentro de una computadora en forma de datos, para que sea automáticamente utilizable. Esto puede verse como un espectro:

![Espectro de representación del conocimiento](../../../../translated_images/knowledge-spectrum.b60df631852c0217e941485b79c9eee40ebd574f15f18609cec5758fcb384bf3.es.png)

> Imagen de [Dmitry Soshnikov](http://soshnikov.com)

* A la izquierda, hay tipos de representaciones de conocimiento muy simples que pueden ser utilizados efectivamente por las computadoras. La más simple es algorítmica, cuando el conocimiento es representado por un programa de computadora. Sin embargo, esta no es la mejor manera de representar el conocimiento, porque no es flexible. El conocimiento dentro de nuestra cabeza a menudo es no algorítmico.
* A la derecha, hay representaciones como el texto natural. Es la más poderosa, pero no puede ser utilizada para razonamiento automático.

> ✅ Piensa un momento en cómo representas el conocimiento en tu cabeza y lo conviertes en notas. ¿Hay un formato particular que funcione bien para ti para ayudar en la retención?

## Clasificación de Representaciones de Conocimiento Computacional

Podemos clasificar diferentes métodos de representación de conocimiento computacional en las siguientes categorías:

* **Representaciones en red** se basan en el hecho de que tenemos una red de conceptos interrelacionados dentro de nuestra cabeza. Podemos intentar reproducir las mismas redes como un gráfico dentro de una computadora - una llamada **red semántica**.

1. **Tripletas Objeto-Atributo-Valor** o **pares atributo-valor**. Dado que un gráfico puede ser representado dentro de una computadora como una lista de nodos y aristas, podemos representar una red semántica mediante una lista de tripletas, que contienen objetos, atributos y valores. Por ejemplo, construimos las siguientes tripletas sobre lenguajes de programación:

Objeto | Atributo | Valor
-------|-----------|------
Python | es | Lenguaje-Sin-Tipo
Python | inventado-por | Guido van Rossum
Python | sintaxis-de-bloque | indentación
Lenguaje-Sin-Tipo | no tiene | definiciones de tipo

> ✅ Piensa en cómo se pueden usar tripletas para representar otros tipos de conocimiento.

2. **Representaciones jerárquicas** enfatizan el hecho de que a menudo creamos una jerarquía de objetos dentro de nuestra cabeza. Por ejemplo, sabemos que un canario es un pájaro, y todos los pájaros tienen alas. También tenemos alguna idea sobre de qué color es un canario generalmente, y cuál es su velocidad de vuelo.

   - **Representación en marco** se basa en representar cada objeto o clase de objetos como un **marco** que contiene **slots**. Los slots tienen posibles valores predeterminados, restricciones de valor o procedimientos almacenados que pueden ser llamados para obtener el valor de un slot. Todos los marcos forman una jerarquía similar a una jerarquía de objetos en lenguajes de programación orientados a objetos.
   - **Escenarios** son un tipo especial de marcos que representan situaciones complejas que pueden desarrollarse en el tiempo.

**Python**

Slot | Valor | Valor predeterminado | Intervalo |
-----|-------|----------------------|----------|
Nombre | Python | | |
Es-Un | Lenguaje-Sin-Tipo | | |
Caso de Variable | | CamelCase | |
Longitud del Programa | | | 5-5000 líneas |
Sintaxis de Bloque | Indentación | | |

3. **Representaciones procedimentales** se basan en representar el conocimiento mediante una lista de acciones que pueden ser ejecutadas cuando ocurre una cierta condición.
   - Las reglas de producción son declaraciones si-entonces que nos permiten llegar a conclusiones. Por ejemplo, un médico puede tener una regla que diga que **SI** un paciente tiene fiebre alta **O** un alto nivel de proteína C-reactiva en el análisis de sangre **ENTONCES** tiene una inflamación. Una vez que encontramos una de las condiciones, podemos llegar a una conclusión sobre la inflamación, y luego usarla en un razonamiento posterior.
   - Los algoritmos pueden considerarse otra forma de representación procedimental, aunque casi nunca se utilizan directamente en sistemas basados en conocimiento.

4. **Lógica** fue propuesta originalmente por Aristóteles como una forma de representar el conocimiento humano universal.
   - La Lógica de Predicados como teoría matemática es demasiado rica para ser computable, por lo tanto, normalmente se utiliza algún subconjunto de ella, como las cláusulas de Horn utilizadas en Prolog.
   - La Lógica Descriptiva es una familia de sistemas lógicos utilizados para representar y razonar sobre jerarquías de objetos en representaciones de conocimiento distribuidas como la *web semántica*.

## Sistemas Expertos

Uno de los primeros éxitos de la IA simbólica fueron los llamados **sistemas expertos** - sistemas computacionales diseñados para actuar como un experto en un dominio de problema limitado. Se basaban en una **base de conocimiento** extraída de uno o más expertos humanos, y contenían un **motor de inferencia** que realizaba algún razonamiento sobre ella.

![Arquitectura Humana](../../../../translated_images/arch-human.5d4d35f1bba3ab1cdfda96af2f10b89574eb31e9796d0e3011cd9beda1c35112.es.png) | ![Sistema Basado en Conocimiento](../../../../translated_images/arch-kbs.3ec5c150b09fa8dadc2beb0931a4983c9e2b03913a89eebcc103b5bb841b0212.es.png)
---------------------------------------------|------------------------------------------------
Estructura simplificada de un sistema neural humano | Arquitectura de un sistema basado en conocimiento

Los sistemas expertos están construidos como el sistema de razonamiento humano, que contiene **memoria a corto plazo** y **memoria a largo plazo**. De manera similar, en los sistemas basados en conocimiento distinguimos los siguientes componentes:

* **Memoria del problema**: contiene el conocimiento sobre el problema que se está resolviendo actualmente, es decir, la temperatura o presión arterial de un paciente, si tiene inflamación o no, etc. Este conocimiento también se llama **conocimiento estático**, porque contiene una instantánea de lo que actualmente sabemos sobre el problema - el llamado *estado del problema*.
* **Base de conocimiento**: representa el conocimiento a largo plazo sobre un dominio de problema. Se extrae manualmente de expertos humanos y no cambia de consulta a consulta. Debido a que nos permite navegar de un estado de problema a otro, también se llama **conocimiento dinámico**.
* **Motor de inferencia**: orquesta todo el proceso de búsqueda en el espacio del estado del problema, haciendo preguntas al usuario cuando es necesario. También es responsable de encontrar las reglas adecuadas que se aplicarán a cada estado.

Como ejemplo, consideremos el siguiente sistema experto para determinar un animal basado en sus características físicas:

![Árbol AND-OR](../../../../translated_images/AND-OR-Tree.5592d2c70187f283703c8e9c0d69d6a786eb370f4ace67f9a7aae5ada3d260b0.es.png)

> Imagen de [Dmitry Soshnikov](http://soshnikov.com)

Este diagrama se llama un **árbol AND-OR**, y es una representación gráfica de un conjunto de reglas de producción. Dibujar un árbol es útil al principio para extraer conocimiento del experto. Para representar el conocimiento dentro de la computadora es más conveniente usar reglas:

```
IF the animal eats meat
OR (animal has sharp teeth
    AND animal has claws
    AND animal has forward-looking eyes
) 
THEN the animal is a carnivore
```

Puedes notar que cada condición en el lado izquierdo de la regla y la acción son esencialmente tripletas objeto-atributo-valor (OAV). **La memoria de trabajo** contiene el conjunto de tripletas OAV que corresponden al problema que se está resolviendo actualmente. Un **motor de reglas** busca reglas para las cuales se cumple una condición y las aplica, añadiendo otra tripleta a la memoria de trabajo.

> ✅ ¡Escribe tu propio árbol AND-OR sobre un tema que te guste!

### Inferencia hacia adelante vs. Inferencia hacia atrás

El proceso descrito anteriormente se llama **inferencia hacia adelante**. Comienza con algunos datos iniciales sobre el problema disponibles en la memoria de trabajo, y luego ejecuta el siguiente bucle de razonamiento:

1. Si el atributo objetivo está presente en la memoria de trabajo - detente y da el resultado
2. Busca todas las reglas cuya condición esté actualmente satisfecha - obtén el **conjunto de conflictos** de reglas.
3. Realiza **resolución de conflictos** - selecciona una regla que se ejecutará en este paso. Podría haber diferentes estrategias de resolución de conflictos:
   - Selecciona la primera regla aplicable en la base de conocimiento
   - Selecciona una regla aleatoria
   - Selecciona una regla *más específica*, es decir, aquella que cumple con más condiciones en el "lado izquierdo" (LHS)
4. Aplica la regla seleccionada e inserta un nuevo conocimiento en el estado del problema
5. Repite desde el paso 1.

Sin embargo, en algunos casos podemos querer comenzar con un conocimiento vacío sobre el problema y hacer preguntas que nos ayuden a llegar a la conclusión. Por ejemplo, al realizar un diagnóstico médico, generalmente no realizamos todos los análisis médicos por adelantado antes de comenzar a diagnosticar al paciente. Más bien, queremos realizar análisis cuando se necesita tomar una decisión.

Este proceso se puede modelar utilizando **inferencia hacia atrás**. Está impulsado por el **objetivo** - el valor del atributo que estamos buscando:

1. Selecciona todas las reglas que pueden darnos el valor de un objetivo (es decir, con el objetivo en el RHS ("lado derecho")) - un conjunto de conflictos
1. Si no hay reglas para este atributo, o hay una regla que dice que debemos preguntar el valor al usuario - pregúntalo, de lo contrario:
1. Usa una estrategia de resolución de conflictos para seleccionar una regla que usaremos como *hipótesis* - intentaremos probarla
1. Repetidamente repite el proceso para todos los atributos en el LHS de la regla, intentando probarlos como objetivos
1. Si en algún momento el proceso falla - usa otra regla en el paso 3.

> ✅ ¿En qué situaciones es más apropiada la inferencia hacia adelante? ¿Qué hay de la inferencia hacia atrás?

### Implementación de Sistemas Expertos

Los sistemas expertos pueden implementarse utilizando diferentes herramientas:

* Programándolos directamente en algún lenguaje de programación de alto nivel. Esta no es la mejor idea, porque la principal ventaja de un sistema basado en conocimiento es que el conocimiento está separado de la inferencia, y potencialmente un experto en el dominio del problema debería ser capaz de escribir reglas sin entender los detalles del proceso de inferencia.
* Usando **shell de sistemas expertos**, es decir, un sistema diseñado específicamente para ser poblado por conocimiento utilizando algún lenguaje de representación del conocimiento.

## ✍️ Ejercicio: Inferencia Animal

Consulta [Animals.ipynb](https://github.com/microsoft/AI-For-Beginners/blob/main/lessons/2-Symbolic/Animals.ipynb) para un ejemplo de implementación de un sistema experto de inferencia hacia adelante y hacia atrás.

> **Nota**: Este ejemplo es bastante simple y solo da una idea de cómo se ve un sistema experto. Una vez que comiences a crear tal sistema, solo notarás algún comportamiento *inteligente* de él una vez que alcances un cierto número de reglas, alrededor de 200+. En algún momento, las reglas se vuelven demasiado complejas para mantener todas en mente, y en este punto puedes comenzar a preguntarte por qué un sistema toma ciertas decisiones. Sin embargo, la característica importante de los sistemas basados en conocimiento es que siempre puedes *explicar* exactamente cómo se tomaron las decisiones.

## Ontologías y la Web Semántica

A finales del siglo XX, hubo una iniciativa para usar la representación del conocimiento para anotar recursos de Internet, de modo que fuera posible encontrar recursos que correspondieran a consultas muy específicas. Este movimiento se llamó **Web Semántica**, y se basó en varios conceptos:

- Una representación especial del conocimiento basada en **[lógicas de descripción](https://en.wikipedia.org/wiki/Description_logic)** (DL). Es similar a la representación de conocimiento en marcos, porque construye una jerarquía de objetos con propiedades, pero tiene semántica lógica formal e inferencia. Hay toda una familia de DLs que equilibran entre expresividad y complejidad algorítmica de la inferencia.
- Representación de conocimiento distribuido, donde todos los conceptos están representados por un identificador URI global, lo que hace posible crear jerarquías de conocimiento que abarcan Internet.
- Una familia de lenguajes basados en XML para la descripción del conocimiento: RDF (Marco de Descripción de Recursos), RDFS (Esquema RDF), OWL (Lenguaje de Ontología Web).

Un concepto central en la Web Semántica es el concepto de **Ontología**. Se refiere a una especificación explícita de un dominio de problema utilizando alguna representación formal del conocimiento. La ontología más simple puede ser solo una jerarquía de objetos en un dominio de problema, pero ontologías más complejas incluirán reglas que pueden ser utilizadas para inferencia.

En la web semántica, todas las representaciones se basan en tripletas. Cada objeto y cada relación están identificados de manera única por la URI. Por ejemplo, si queremos afirmar que este Currículo de IA ha sido desarrollado por Dmitry Soshnikov el 1 de enero de 2022, aquí están las tripletas que podemos usar:

<img src="images/triplet.png" width="30%"/>

```
http://github.com/microsoft/ai-for-beginners http://www.example.com/terms/creation-date “Jan 13, 2007”
http://github.com/microsoft/ai-for-beginners http://purl.org/dc/elements/1.1/creator http://soshnikov.com
```

> ✅ Aquí `http://www.example.com/terms/creation-date` and `http://purl.org/dc/elements/1.1/creator` son algunas URIs bien conocidas y universalmente aceptadas para expresar los conceptos de *creador* y *fecha de creación*.

En un caso más complejo, si queremos definir una lista de creadores, podemos usar algunas estructuras de datos definidas en RDF.

<img src="images/triplet-complex.png" width="40%"/>

> Diagramas arriba por [Dmitry Soshnikov](http://soshnikov.com)

El progreso en la construcción de la Web Semántica se vio algo ralentizado por el éxito de los motores de búsqueda y las técnicas de procesamiento de lenguaje natural, que permiten extraer datos estructurados de texto. Sin embargo, en algunas áreas aún hay esfuerzos significativos para mantener ontologías y bases de conocimiento. Algunos proyectos que vale la pena mencionar:

* [WikiData](https://wikidata.org/) es una colección de bases de conocimiento legibles por máquina asociadas con Wikipedia. La mayor parte de los datos se extraen de las *InfoBoxes* de Wikipedia, piezas de contenido estructurado dentro de las páginas de Wikipedia. Puedes [consultar](https://query.wikidata.org/) wikidata en SPARQL, un lenguaje de consulta especial para la Web Semántica. Aquí hay una consulta de muestra que muestra los colores de ojos más populares entre los humanos:

```sparql
#defaultView:BubbleChart
SELECT ?eyeColorLabel (COUNT(?human) AS ?count)
WHERE
{
  ?human wdt:P31 wd:Q5.       # human instance-of homo sapiens
  ?human wdt:P1340 ?eyeColor. # human eye-color ?eyeColor
  SERVICE wikibase:label { bd:serviceParam wikibase:language "en". }
}
GROUP BY ?eyeColorLabel
```

* [DBpedia](https://www.dbpedia.org/) es otro esfuerzo similar a WikiData.

> ✅ Si deseas experimentar con la construcción de tus propias ontologías, o abrir las existentes, hay un gran editor visual de ontologías llamado [Protégé](https://protege.stanford.edu/). Descárgalo o úsalo en línea.

<img src="images/protege.png" width="70%"/>

*Editor Web Protégé abierto con la ontología de la Familia Romanov. Captura de pantalla de Dmitry Soshnikov*

## ✍️ Ejercicio: Una Ontología Familiar

Consulta [FamilyOntology.ipynb](https://github.com/Ezana135/AI-For-Beginners/blob/main/lessons/2-Symbolic/FamilyOntology.ipynb) para un ejemplo de uso de técnicas de Web Semántica para razonar sobre relaciones familiares. Tomaremos un árbol genealógico representado en el formato GEDCOM común y una ontología de relaciones familiares y construiremos un gráfico de todas las relaciones familiares para un conjunto dado de individuos.

## Grafo de Conceptos de Microsoft

En la mayoría de los casos, las ontologías son creadas cuidadosamente a mano. Sin embargo, también es posible **extraer** ontologías de datos no estructurados, por ejemplo, de textos en lenguaje natural.

Un intento de este tipo fue realizado por Microsoft Research, y resultó en el [Grafo de Conceptos de Microsoft](https://blogs.microsoft.com/ai/microsoft-researchers-release-graph-that-helps-machines-conceptualize/?WT.mc_id=academic-77998-cacaste).

Es una gran colección de entidades agrupadas mediante la relación de herencia `is-a`. Permite responder preguntas como "¿Qué es Microsoft?"

**Descargo de responsabilidad**:  
Este documento ha sido traducido utilizando servicios de traducción automática basados en IA. Si bien nos esforzamos por lograr precisión, tenga en cuenta que las traducciones automáticas pueden contener errores o inexactitudes. El documento original en su idioma nativo debe considerarse la fuente autorizada. Para información crítica, se recomienda una traducción profesional realizada por humanos. No nos hacemos responsables de malentendidos o malas interpretaciones que surjan del uso de esta traducción.