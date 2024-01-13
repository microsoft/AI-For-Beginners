# Sistemas multiagente

Una de las posibles formas de lograr inteligencia es el llamado enfoque **emergente** (o **sinérgico**), que se basa en el hecho de que el comportamiento combinado de muchos agentes relativamente simples puede dar como resultado un conjunto más complejo ( o inteligente) del sistema en su conjunto. Teóricamente, esto se basa en los principios de [Inteligencia Colectiva](https://en.wikipedia.org/wiki/Collective_intelligence), [Emergentismo](https://en.wikipedia.org/wiki/Global_brain) y [Evolución Cibernética](https://en.wikipedia.org/wiki/Global_brain), que afirma que los sistemas de nivel superior obtienen algún tipo de valor agregado cuando se combinan adecuadamente con sistemas de nivel inferior (el llamado *principio de transición del metasistema* ).

## [Pre-lecture quiz](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/123)

La dirección de los **Sistemas Multi-Agente** surgió en la IA en la década de 1990 como respuesta al crecimiento de Internet y los sistemas distribuidos. Uno de los libros de texto clásicos sobre IA, [Inteligencia artificial: un enfoque moderno](https://en.wikipedia.org/wiki/Artificial_Intelligence:_A_Modern_Approach), se centra en la visión de la IA clásica desde el punto de vista de los sistemas multiagente. .

Un elemento central del enfoque de agentes múltiples es la noción de **Agente**: una entidad que vive en algún **entorno**, que puede percibir y sobre el cual puede actuar. Esta es una definición muy amplia y podrían existir muchos tipos y clasificaciones diferentes de agentes:

* Por su capacidad de razonar:
    - Los agentes **reactivos** suelen tener un tipo de comportamiento de solicitud-respuesta simple.
    - Los agentes **deliberativos** emplean algún tipo de razonamiento lógico y/o capacidades de planificación.
* Por el lugar donde el agente ejecuta su código:
    - Los agentes **estáticos** trabajan en un nodo de red dedicado
    - Los agentes **móviles** pueden mover su código entre nodos de red
* Por su comportamiento:
    - **Los agentes pasivos** no tienen objetivos específicos. Estos agentes pueden reaccionar a estímulos externos, pero no iniciarán ninguna acción por sí mismos.
    - **Los agentes activos** tienen algunos objetivos que persiguen
    - **Los agentes cognitivos** implican una planificación y un razonamiento complejos

Los sistemas multiagente se utilizan hoy en día en diversas aplicaciones:

* En los juegos, muchos personajes no jugadores emplean algún tipo de IA y pueden considerarse agentes inteligentes.
* En la producción de video, la representación de escenas 3D complejas que involucran multitudes generalmente se realiza mediante simulación de múltiples agentes.
* En el modelado de sistemas, se utiliza un enfoque de múltiples agentes para simular el comportamiento de un modelo complejo. Por ejemplo, se ha utilizado con éxito un enfoque de múltiples agentes para predecir la propagación de la enfermedad COVID-19 en todo el mundo. Se puede utilizar un enfoque similar para modelar el tráfico en la ciudad y ver cómo reacciona a los cambios en las normas de tráfico.
* En sistemas de automatización complejos, cada dispositivo puede actuar como un agente independiente, lo que hace que todo el sistema sea menos monolítico y más robusto.

No dedicaremos mucho tiempo a profundizar en los sistemas multiagente, pero consideremos un ejemplo de **Modelado multiagente**.

## Logotipo de red

[NetLogo](https://ccl.northwestern.edu/netlogo/) es un entorno de modelado multiagente basado en una versión modificada del [Logo](https://en.wikipedia.org/wiki/Logo_(programming_language)) lenguaje de programación. Este lenguaje fue desarrollado para enseñar conceptos de programación a niños y te permite controlar un agente llamado **tortuga**, que puede moverse dejando un rastro. Esto permite crear figuras geométricas complejas, lo cual es una forma muy visual de entender el comportamiento de un agente.

En NetLogo, podemos crear muchas tortugas usando el comando `create-turtles`. Luego podemos ordenar a todas las tortugas que realicen algunas acciones (en el siguiente ejemplo, más de 10 puntos hacia adelante):

```
crear-tortugas 10
pregúntale a las tortugas [
   adelante 10
]
```

Por supuesto, no es interesante cuando todas las tortugas hacen lo mismo, así que podemos "preguntar" a grupos de tortugas, por ejemplo. aquellos que se encuentran en las proximidades de un determinado punto. También podemos crear tortugas de diferentes *razas* usando el comando `breed [cats cat]`. Aquí "gato" es el nombre de una raza, y necesitamos especificar tanto la palabra singular como la plural, porque diferentes comandos usan diferentes formas para mayor claridad.

> ✅ No profundizaremos en el aprendizaje del lenguaje NetLogo en sí; puedes visitar el brillante [Beginner's Interactive NetLogo Dictionary](https://ccl.northwestern.edu/netlogo/bind/) recurso si está interesado en aprender más.
>
> Puede [download](https://ccl.northwestern.edu/netlogo/download.shtml) e instale NetLogo para probarlo.

### Biblioteca de modelos

Lo bueno de NetLogo es que contiene una biblioteca de modelos funcionales que puedes probar. Vaya a **Archivo &rightarrow; Biblioteca de modelos** y tienes muchas categorías de modelos para elegir.

<img alt="NetLogo Models Library" src="images/NetLogo-ModelLib.png" width="60%"/>

> Una captura de pantalla de la biblioteca de modelos por Dmitry Soshnikov

Puede abrir uno de los modelos, por ejemplo **Biología &rightarrow; Flocado**.

### Principios principales

Después de abrir el modelo, accederá a la pantalla principal de NetLogo. A continuación se muestra un modelo de muestra que describe la población de lobos y ovejas, dados recursos finitos (pasto).

![NetLogo Main Screen](images/NetLogo-Main.png)

> Captura de pantalla de Dmitry Soshnikov

En esta pantalla podrás ver:

* La sección **Interfaz** que contiene:
   - El campo principal, donde viven todos los agentes.
   - Diferentes controles: botones, sliders, etc.
   - Gráficos que puedes utilizar para mostrar los parámetros de la simulación.
* La pestaña **Código** que contiene el editor, donde puede escribir el programa NetLogo

En la mayoría de los casos, la interfaz tendría un botón **Configuración**, que inicializa el estado de simulación, y un botón **Ir** que inicia la ejecución. Estos son manejados por los controladores correspondientes en el código que se ve así:

```
ir [
...
]
```

El mundo de NetLogo consta de los siguientes objetos:

* **Agentes** (tortugas) que pueden moverse por el campo y hacer algo. Usted ordena a los agentes usando la sintaxis `preguntar a las tortugas [...]`, y todos los agentes ejecutan el código entre paréntesis en *modo tortuga*.
* **Parches** son áreas cuadradas del campo en las que viven los agentes. Puede consultar todos los agentes en el mismo parche o puede cambiar los colores del parche y algunas otras propiedades. También puedes "pedirle a los parches" que hagan algo.
* **Observador** es un agente único que controla el mundo. Todos los controladores de botones se ejecutan en *modo observador*.

> ✅ La belleza de un entorno multiagente es que el código que se ejecuta en modo tortuga o en modo parche es ejecutado al mismo tiempo por todos los agentes en paralelo. Por lo tanto, al escribir un pequeño código y programar el comportamiento de un agente individual, se puede crear un comportamiento complejo del sistema de simulación en su conjunto.

### Flocado

Como ejemplo de comportamiento multiagente, consideremos **[Flocking](https://en.wikipedia.org/wiki/Flocking_(behavior))**. La bandada es un patrón complejo que es muy similar a cómo vuelan las bandadas de pájaros. Al verlos volar se puede pensar que siguen algún tipo de algoritmo colectivo, o que poseen alguna forma de *inteligencia colectiva*. Sin embargo, este comportamiento complejo surge cuando cada agente individual (en este caso, un *pájaro*) sólo observa a otros agentes a corta distancia de él y sigue tres reglas simples:

* **Alineación** - se orienta hacia el rumbo promedio de los agentes vecinos
* **Cohesión** - intenta dirigirse hacia la posición promedio de los vecinos (*atracción de largo alcance*)
* **Separación** - cuando se acerca demasiado a otras aves, intenta alejarse (*repulsión de corto alcance*)

Puede ejecutar el ejemplo de flocado y observar el comportamiento. También puedes ajustar parámetros, como el *grado de separación* o el *rango de visión*, que define hasta dónde puede ver cada pájaro. Tenga en cuenta que si reduce el rango de visión a 0, todas las aves se vuelven ciegas y la bandada se detiene. Si reduce la separación a 0, todas las aves se juntan en línea recta.

> ✅ Cambie a la pestaña **Código** y vea dónde se implementan en el código tres reglas de flocado (alineación, cohesión y separación). Nótese cómo nos referimos sólo a aquellos agentes que están a la vista.

### Otros modelos para ver

Hay algunos modelos más interesantes con los que puedes experimentar:

* **Arte &rightarrow; Fuegos artificiales** muestra cómo un fuego artificial puede considerarse un comportamiento colectivo de corrientes de fuego individuales.
* **Ciencias Sociales &rightarrow; Tráfico Básico** y **Ciencias Sociales &rightarrow; Traffic Grid** muestra el modelo de tráfico de la ciudad en cuadrícula 1D y 2D con o sin semáforos. Cada coche de la simulación sigue las siguientes reglas:
    - Si el espacio frente a él está vacío, acelera (hasta una cierta velocidad máxima)
    - Si ve el obstáculo delante, frene (y puede ajustar hasta dónde puede ver el conductor)
* **Ciencias Sociales &rightarrow; Party** muestra cómo las personas se agrupan durante un cóctel. Puedes encontrar la combinación de parámetros que conducen al aumento más rápido de la felicidad del grupo.

Como puede ver en estos ejemplos, las simulaciones de múltiples agentes pueden ser una forma bastante útil de comprender el comportamiento de un sistema complejo formado por individuos que siguen la misma lógica o una similar. También se puede utilizar para controlar agentes virtuales, como [NPC](https://en.wikipedia.org/wiki/NPC) en juegos de computadora o agentes en mundos animados en 3D.

## Agentes deliberantes

Los agentes descritos anteriormente son muy simples y reaccionan a los cambios en el entorno utilizando algún tipo de algoritmo. Como tales, son **agentes reactivos**. Sin embargo, a veces los agentes pueden razonar y planificar su acción, en cuyo caso se les llama **deliberativos**.

Un ejemplo típico sería un agente personal que recibe instrucciones de un humano para reservar un viaje de vacaciones. Supongamos que hay muchos agentes que viven en Internet y que pueden ayudarle. Luego deberá contactar con otros agentes para ver qué vuelos hay disponibles, cuáles son los precios de los hoteles para las distintas fechas e intentar negociar el mejor precio. Cuando el plan de vacaciones esté completo y confirmado por el propietario, podrá proceder con la reserva.

Para hacerlo, los agentes deben **comunicarse**. Para una comunicación exitosa necesitan:

* Algunos **idiomas estándar para intercambiar conocimientos**, como [Knowledge Interchange Format](https://en.wikipedia.org/wiki/Knowledge_Interchange_Format) (KIF) y [Knowledge Query and Manipulation Language](https://en.wikipedia.org/wiki/Knowledge_Query_and_Manipulation_Language) (KQML). Esos lenguajes están diseñados en base a [Speech Act theory](https://en.wikipedia.org/wiki/Speech_act).
* Esos idiomas también deben incluir algunos **protocolos de negociación**, basados en diferentes **tipos de subasta**.
* Una **ontología** común a utilizar, para que se refieran a los mismos conceptos conociendo su semántica
* Una forma de **descubrir** qué pueden hacer diferentes agentes, también basada en algún tipo de ontología

Los agentes deliberativos son mucho más complejos que reactivos, porque no sólo reaccionan a los cambios en el entorno, sino que también deberían poder *iniciar* acciones. Una de las arquitecturas propuestas para los agentes deliberativos es el llamado agente Creencia-Deseo-Intención (BDI):

* **Las creencias** forman un conjunto de conocimientos sobre el entorno de un agente. Puede estructurarse como una base de conocimientos o un conjunto de reglas que un agente puede aplicar a una situación específica del entorno.
* **Los deseos** definen lo que un agente quiere hacer, es decir, sus objetivos. Por ejemplo, el objetivo del agente asistente personal anterior es reservar un recorrido y el objetivo de un agente hotelero es maximizar las ganancias.
* **Las intenciones** son acciones específicas que un agente planea para lograr sus objetivos. Las acciones suelen cambiar el entorno y provocar la comunicación con otros agentes.

Hay algunas plataformas disponibles para construir sistemas multiagente, como [JADE](https://jade.tilab.com/). [This paper](https://arxiv.org/ftp/arxiv/papers/2007/2007.08961.pdf) contiene una revisión de las plataformas multiagente, junto con una breve historia de los sistemas multiagente y sus diferentes escenarios de uso.

## Conclusión

Los sistemas multiagente pueden adoptar formas muy diferentes y utilizarse en muchas aplicaciones diferentes.
Todos tienden a centrarse en el comportamiento más simple de un agente individual y logran un comportamiento más complejo del sistema general debido al **efecto sinérgico**.

## 🚀 Desafío

Lleve esta lección al mundo real e intente conceptualizar un sistema multiagente que pueda resolver un problema. ¿Qué tendría que hacer, por ejemplo, un sistema multiagente para optimizar la ruta de un autobús escolar? ¿Cómo podría funcionar en una panadería?

## [Post-lecture quiz](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/223)

## Revisión y autoestudio

Revisar el uso de este tipo de sistemas en la industria. Elija un dominio como la fabricación o la industria de los videojuegos y descubra cómo se pueden utilizar los sistemas multiagente para resolver problemas únicos.

## [NetLogo Assignment](assignment.md)
