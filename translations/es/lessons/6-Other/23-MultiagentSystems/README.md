# Sistemas Multi-Agente

Una de las formas posibles de alcanzar la inteligencia es el llamado enfoque **emergente** (o **sinerético**), que se basa en el hecho de que el comportamiento combinado de muchos agentes relativamente simples puede resultar en un comportamiento general más complejo (o inteligente) del sistema en su conjunto. Teóricamente, esto se basa en los principios de la [Inteligencia Colectiva](https://en.wikipedia.org/wiki/Collective_intelligence), el [Emergentismo](https://en.wikipedia.org/wiki/Global_brain) y la [Cibernética Evolutiva](https://en.wikipedia.org/wiki/Global_brain), que afirman que los sistemas de nivel superior obtienen algún tipo de valor añadido cuando se combinan adecuadamente a partir de sistemas de nivel inferior (el llamado *principio de transición de metasistema*).

## [Cuestionario previo a la clase](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/123)

La dirección de los **Sistemas Multi-Agente** ha surgido en IA en la década de 1990 como respuesta al crecimiento de Internet y los sistemas distribuidos. Uno de los libros de texto clásicos de IA, [Inteligencia Artificial: Un Enfoque Moderno](https://en.wikipedia.org/wiki/Artificial_Intelligence:_A_Modern_Approach), se centra en la visión de la IA clásica desde el punto de vista de los sistemas multi-agente.

Central al enfoque multi-agente es la noción de **Agente** - una entidad que vive en algún **entorno**, que puede percibir y actuar sobre él. Esta es una definición muy amplia, y podría haber muchos tipos y clasificaciones diferentes de agentes:

* Por su capacidad de razonar:
   - Los agentes **reactivos** generalmente tienen un comportamiento simple de tipo solicitud-respuesta.
   - Los agentes **deliberativos** emplean algún tipo de razonamiento lógico y/o capacidades de planificación.
* Por el lugar donde el agente ejecuta su código:
   - Los agentes **estáticos** trabajan en un nodo de red dedicado.
   - Los agentes **móviles** pueden mover su código entre nodos de red.
* Por su comportamiento:
   - Los **agentes pasivos** no tienen objetivos específicos. Tales agentes pueden reaccionar a estímulos externos, pero no iniciarán acciones por sí mismos.
   - Los **agentes activos** tienen objetivos que persiguen.
   - Los **agentes cognitivos** involucran planificación y razonamiento complejos.

Los sistemas multi-agente se utilizan hoy en día en una serie de aplicaciones:

* En los juegos, muchos personajes no jugadores emplean algún tipo de IA y pueden considerarse agentes inteligentes.
* En la producción de video, renderizar escenas 3D complejas que involucran multitudes se realiza típicamente utilizando simulación multi-agente.
* En modelado de sistemas, el enfoque multi-agente se utiliza para simular el comportamiento de un modelo complejo. Por ejemplo, se ha utilizado con éxito el enfoque multi-agente para predecir la propagación de la enfermedad COVID-19 en todo el mundo. Un enfoque similar puede usarse para modelar el tráfico en la ciudad y ver cómo reacciona a los cambios en las normas de tráfico.
* En sistemas de automatización complejos, cada dispositivo puede actuar como un agente independiente, lo que hace que todo el sistema sea menos monolítico y más robusto.

No vamos a dedicar mucho tiempo a profundizar en los sistemas multi-agente, pero consideremos un ejemplo de **Modelado Multi-Agente**.

## NetLogo

[NetLogo](https://ccl.northwestern.edu/netlogo/) es un entorno de modelado multi-agente basado en una versión modificada del lenguaje de programación [Logo](https://en.wikipedia.org/wiki/Logo_(programming_language)). Este lenguaje fue desarrollado para enseñar conceptos de programación a niños, y permite controlar un agente llamado **tortuga**, que puede moverse, dejando un rastro detrás. Esto permite crear figuras geométricas complejas, lo que es una forma muy visual de entender el comportamiento de un agente.

En NetLogo, podemos crear muchas tortugas utilizando el comando `create-turtles`. Luego podemos ordenar a todas las tortugas que realicen algunas acciones (en el ejemplo a continuación - avanzar 10 puntos hacia adelante):

```
create-turtles 10
ask turtles [
  forward 10
]
```

Por supuesto, no es interesante cuando todas las tortugas hacen lo mismo, así que podemos `ask` groups of turtles, eg. those who are in the vicinity of a certain point. We can also create turtles of different *breeds* using `breed [cats cat]` command. Here `cat` es el nombre de una raza, y necesitamos especificar tanto la palabra en singular como en plural, porque diferentes comandos utilizan diferentes formas para mayor claridad.

> ✅ No vamos a entrar en aprender el lenguaje NetLogo en sí; puedes visitar el brillante [Diccionario Interactivo para Principiantes de NetLogo](https://ccl.northwestern.edu/netlogo/bind/) si estás interesado en aprender más.

Puedes [descargar](https://ccl.northwestern.edu/netlogo/download.shtml) e instalar NetLogo para probarlo.

### Biblioteca de Modelos

Una gran ventaja de NetLogo es que contiene una biblioteca de modelos funcionales que puedes probar. Ve a **Archivo → Biblioteca de Modelos**, y tienes muchas categorías de modelos para elegir.

<img alt="Biblioteca de Modelos de NetLogo" src="images/NetLogo-ModelLib.png" width="60%"/>

> Una captura de pantalla de la biblioteca de modelos por Dmitry Soshnikov

Puedes abrir uno de los modelos, por ejemplo **Biología → Rebaño**.

### Principios Principales

Después de abrir el modelo, se te lleva a la pantalla principal de NetLogo. Aquí hay un modelo de ejemplo que describe la población de lobos y ovejas, dados recursos finitos (hierba).

![Pantalla Principal de NetLogo](../../../../../translated_images/NetLogo-Main.32653711ec1a01b3cab22ec0b148e64193d0b979b055285bef329d5e3d6958c5.es.png)

> Captura de pantalla por Dmitry Soshnikov

En esta pantalla, puedes ver:

* La sección de **Interfaz** que contiene:
  - El campo principal, donde viven todos los agentes.
  - Diferentes controles: botones, deslizadores, etc.
  - Gráficos que puedes usar para mostrar parámetros de la simulación.
* La pestaña de **Código** que contiene el editor, donde puedes escribir el programa NetLogo.

En la mayoría de los casos, la interfaz tendría un botón de **Configuración**, que inicializa el estado de la simulación, y un botón de **Ejecutar** que inicia la ejecución. Estos son manejados por controladores correspondientes en el código que lucen así:

```
to go [
...
]
```

El mundo de NetLogo consiste en los siguientes objetos:

* **Agentes** (tortugas) que pueden moverse por el campo y hacer algo. Ordenas a los agentes usando `ask turtles [...]` syntax, and the code in brackets is executed by all agents in *turtle mode*.
* **Patches** are square areas of the field, on which agents live. You can refer to all agents on the same patch, or you can change patch colors and some other properties. You can also `ask patches` para hacer algo.
* **Observador** es un agente único que controla el mundo. Todos los controladores de botones se ejecutan en *modo observador*.

> ✅ La belleza de un entorno multi-agente es que el código que se ejecuta en modo tortuga o en modo parche se ejecuta al mismo tiempo por todos los agentes en paralelo. Así, al escribir un poco de código y programar el comportamiento de un agente individual, puedes crear un comportamiento complejo del sistema de simulación en su conjunto.

### Rebaño

Como ejemplo de comportamiento multi-agente, consideremos **[Rebaño](https://en.wikipedia.org/wiki/Flocking_(behavior))**. El rebaño es un patrón complejo que es muy similar a cómo vuelan los bandadas de aves. Al observarlas volar, puedes pensar que siguen algún tipo de algoritmo colectivo, o que poseen alguna forma de *inteligencia colectiva*. Sin embargo, este comportamiento complejo surge cuando cada agente individual (en este caso, un *pájaro*) solo observa a otros agentes a una corta distancia de él, y sigue tres reglas simples:

* **Alineación** - se dirige hacia la dirección promedio de los agentes vecinos.
* **Cohesión** - intenta dirigirse hacia la posición promedio de los vecinos (*atracción a largo alcance*).
* **Separación** - cuando se acerca demasiado a otros pájaros, intenta alejarse (*repulsión a corto alcance*).

Puedes ejecutar el ejemplo de rebaño y observar el comportamiento. También puedes ajustar parámetros, como el *grado de separación*, o el *rango de visión*, que define cuán lejos puede ver cada pájaro. Ten en cuenta que si reduces el rango de visión a 0, todos los pájaros se vuelven ciegos y el rebaño se detiene. Si reduces la separación a 0, todos los pájaros se agrupan en una línea recta.

> ✅ Cambia a la pestaña de **Código** y observa dónde se implementan las tres reglas del rebaño (alineación, cohesión y separación) en el código. Nota cómo nos referimos solo a aquellos agentes que están a la vista.

### Otros Modelos para Ver

Hay algunos modelos más interesantes con los que puedes experimentar:

* **Arte → Fuegos Artificiales** muestra cómo un fuego artificial puede considerarse un comportamiento colectivo de flujos individuales de fuego.
* **Ciencias Sociales → Tráfico Básico** y **Ciencias Sociales → Tráfico en Rejilla** muestran el modelo del tráfico de la ciudad en una rejilla 1D y 2D con o sin semáforos. Cada coche en la simulación sigue las siguientes reglas:
   - Si el espacio frente a él está vacío - acelera (hasta una cierta velocidad máxima).
   - Si ve un obstáculo frente a él - frena (y puedes ajustar cuán lejos puede ver un conductor).
* **Ciencias Sociales → Fiesta** muestra cómo las personas se agrupan durante una fiesta de cócteles. Puedes encontrar la combinación de parámetros que lleva al aumento más rápido de la felicidad del grupo.

Como puedes ver en estos ejemplos, las simulaciones multi-agente pueden ser una forma bastante útil de entender el comportamiento de un sistema complejo que consiste en individuos que siguen la misma lógica o lógica similar. También puede utilizarse para controlar agentes virtuales, como [NPCs](https://en.wikipedia.org/wiki/NPC) en videojuegos, o agentes en mundos animados en 3D.

## Agentes Deliberativos

Los agentes descritos anteriormente son muy simples, reaccionando a los cambios en el entorno utilizando algún tipo de algoritmo. Como tales, son **agentes reactivos**. Sin embargo, a veces los agentes pueden razonar y planificar sus acciones, en cuyo caso se les llama **deliberativos**.

Un ejemplo típico sería un agente personal que recibe instrucciones de un humano para reservar un tour de vacaciones. Supongamos que hay muchos agentes que viven en Internet, que pueden ayudarlo. Entonces debería contactar a otros agentes para ver qué vuelos están disponibles, cuáles son los precios de los hoteles para diferentes fechas y tratar de negociar el mejor precio. Cuando el plan de vacaciones esté completo y confirmado por el propietario, puede proceder con la reserva.

Para hacer eso, los agentes necesitan **comunicarse**. Para una comunicación exitosa, necesitan:

* Algunos **lenguajes estándar para intercambiar conocimiento**, como [Knowledge Interchange Format](https://en.wikipedia.org/wiki/Knowledge_Interchange_Format) (KIF) y [Knowledge Query and Manipulation Language](https://en.wikipedia.org/wiki/Knowledge_Query_and_Manipulation_Language) (KQML). Estos lenguajes están diseñados en base a la [teoría del acto de habla](https://en.wikipedia.org/wiki/Speech_act).
* Estos lenguajes también deben incluir algunos **protocolos para negociaciones**, basados en diferentes **tipos de subastas**.
* Una **ontología común** para usar, para que se refieran a los mismos conceptos conociendo su semántica.
* Una forma de **descubrir** qué pueden hacer los diferentes agentes, también basada en algún tipo de ontología.

Los agentes deliberativos son mucho más complejos que los reactivos, porque no solo reaccionan a los cambios en el entorno, sino que también deben ser capaces de *iniciar* acciones. Una de las arquitecturas propuestas para agentes deliberativos es el llamado agente de Creencias-Deseos-Intenciones (BDI):

* **Creencias** forman un conjunto de conocimientos sobre el entorno de un agente. Puede estructurarse como una base de conocimientos o un conjunto de reglas que un agente puede aplicar a una situación específica en el entorno.
* **Deseos** definen lo que un agente quiere hacer, es decir, sus objetivos. Por ejemplo, el objetivo del agente asistente personal mencionado anteriormente es reservar un tour, y el objetivo de un agente hotelero es maximizar las ganancias.
* **Intenciones** son acciones específicas que un agente planea realizar para alcanzar sus objetivos. Las acciones cambian típicamente el entorno y causan comunicación con otros agentes.

Hay algunas plataformas disponibles para construir sistemas multi-agente, como [JADE](https://jade.tilab.com/). [Este documento](https://arxiv.org/ftp/arxiv/papers/2007/2007.08961.pdf) contiene una revisión de plataformas multi-agente, junto con una breve historia de los sistemas multi-agente y sus diferentes escenarios de uso.

## Conclusión

Los sistemas multi-agente pueden adoptar formas muy diferentes y utilizarse en muchas aplicaciones distintas. 
Todos tienden a centrarse en el comportamiento más simple de un agente individual y lograr un comportamiento más complejo del sistema general debido al **efecto sinérgico**.

## 🚀 Desafío

Lleva esta lección al mundo real e intenta conceptualizar un sistema multi-agente que pueda resolver un problema. ¿Qué, por ejemplo, necesitaría hacer un sistema multi-agente para optimizar una ruta de autobús escolar? ¿Cómo podría funcionar en una panadería?

## [Cuestionario posterior a la clase](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/223)

## Revisión y Autoestudio

Revisa el uso de este tipo de sistema en la industria. Elige un dominio como la fabricación o la industria de los videojuegos y descubre cómo los sistemas multi-agente pueden utilizarse para resolver problemas únicos.

## [Tarea de NetLogo](assignment.md)

**Descargo de responsabilidad**:  
Este documento ha sido traducido utilizando servicios de traducción automática basados en inteligencia artificial. Si bien nos esforzamos por la precisión, tenga en cuenta que las traducciones automáticas pueden contener errores o inexactitudes. El documento original en su idioma nativo debe considerarse la fuente autorizada. Para información crítica, se recomienda una traducción profesional humana. No somos responsables de malentendidos o malas interpretaciones que surjan del uso de esta traducción.