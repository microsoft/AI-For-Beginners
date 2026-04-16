# IA Ética y Responsable

Has casi terminado este curso, y espero que para ahora veas claramente que la IA se basa en una serie de métodos matemáticos formales que nos permiten encontrar relaciones en los datos y entrenar modelos para replicar algunos aspectos del comportamiento humano. En este momento de la historia, consideramos que la IA es una herramienta muy poderosa para extraer patrones de los datos y aplicar esos patrones para resolver nuevos problemas.

## [Cuestionario previo a la clase](https://white-water-09ec41f0f.azurestaticapps.net/quiz/5/)

Sin embargo, en la ciencia ficción a menudo vemos historias donde la IA representa un peligro para la humanidad. Por lo general, esas historias se centran en algún tipo de rebelión de la IA, cuando esta decide enfrentarse a los seres humanos. Esto implica que la IA tiene algún tipo de emoción o puede tomar decisiones imprevistas por sus desarrolladores.

El tipo de IA que hemos aprendido en este curso no es más que aritmética de matrices a gran escala. Es una herramienta muy poderosa para ayudarnos a resolver nuestros problemas, y como cualquier otra herramienta poderosa, puede ser utilizada para propósitos buenos o malos. Es importante destacar que puede ser *mal utilizada*.

## Principios de IA Responsable

Para evitar este uso accidental o intencionado de la IA, Microsoft establece los importantes [Principios de IA Responsable](https://www.microsoft.com/ai/responsible-ai?WT.mc_id=academic-77998-cacaste). Los siguientes conceptos sustentan estos principios:

* **Equidad** está relacionada con el importante problema de los *sesgos en los modelos*, que pueden ser causados por el uso de datos sesgados para el entrenamiento. Por ejemplo, cuando intentamos predecir la probabilidad de que una persona consiga un trabajo como desarrollador de software, el modelo probablemente dará mayor preferencia a los hombres, simplemente porque el conjunto de datos de entrenamiento probablemente estaba sesgado hacia una audiencia masculina. Necesitamos equilibrar cuidadosamente los datos de entrenamiento e investigar el modelo para evitar sesgos y asegurarnos de que el modelo tenga en cuenta características más relevantes.
* **Fiabilidad y Seguridad**. Por su naturaleza, los modelos de IA pueden cometer errores. Una red neuronal devuelve probabilidades, y debemos tenerlo en cuenta al tomar decisiones. Cada modelo tiene cierta precisión y exhaustividad, y necesitamos entender esto para prevenir el daño que un consejo erróneo puede causar.
* **Privacidad y Seguridad** tienen algunas implicaciones específicas de la IA. Por ejemplo, cuando usamos algunos datos para entrenar un modelo, estos datos se integran de alguna manera en el modelo. Por un lado, eso aumenta la seguridad y privacidad, pero por otro, debemos recordar qué datos se utilizaron para entrenar el modelo.
* **Inclusión** significa que no estamos construyendo IA para reemplazar a las personas, sino para complementarlas y hacer nuestro trabajo más creativo. También está relacionado con la equidad, porque al tratar con comunidades subrepresentadas, la mayoría de los conjuntos de datos que recopilamos probablemente estarán sesgados, y debemos asegurarnos de que esas comunidades estén incluidas y tratadas correctamente por la IA.
* **Transparencia**. Esto incluye asegurarnos de que siempre seamos claros sobre el uso de la IA. Además, siempre que sea posible, queremos utilizar sistemas de IA que sean *interpretables*.
* **Responsabilidad**. Cuando los modelos de IA toman decisiones, no siempre está claro quién es responsable de esas decisiones. Necesitamos asegurarnos de entender dónde recae la responsabilidad de las decisiones de la IA. En la mayoría de los casos, querríamos incluir a los seres humanos en el proceso de tomar decisiones importantes, para que las personas reales sean responsables.

## Herramientas para IA Responsable

Microsoft ha desarrollado el [Responsible AI Toolbox](https://github.com/microsoft/responsible-ai-toolbox), que contiene un conjunto de herramientas:

* Panel de Interpretabilidad (InterpretML)
* Panel de Equidad (FairLearn)
* Panel de Análisis de Errores
* Panel de IA Responsable que incluye:

   - EconML: herramienta para el Análisis Causal, que se centra en preguntas hipotéticas
   - DiCE: herramienta para el Análisis Contrafactual que permite ver qué características necesitan cambiarse para afectar la decisión del modelo

Para más información sobre Ética en IA, por favor visita [esta lección](https://github.com/microsoft/ML-For-Beginners/tree/main/1-Introduction/3-fairness?WT.mc_id=academic-77998-cacaste) en el currículo de Aprendizaje Automático, que incluye tareas.

## Revisión y Autoestudio

Toma este [Camino de Aprendizaje](https://docs.microsoft.com/learn/modules/responsible-ai-principles/?WT.mc_id=academic-77998-cacaste) para aprender más sobre IA responsable.

## [Cuestionario posterior a la clase](https://white-water-09ec41f0f.azurestaticapps.net/quiz/6/)

**Descargo de responsabilidad**:  
Este documento ha sido traducido utilizando el servicio de traducción automática [Co-op Translator](https://github.com/Azure/co-op-translator). Si bien nos esforzamos por lograr precisión, tenga en cuenta que las traducciones automáticas pueden contener errores o imprecisiones. El documento original en su idioma nativo debe considerarse como la fuente autorizada. Para información crítica, se recomienda una traducción profesional realizada por humanos. No nos hacemos responsables de malentendidos o interpretaciones erróneas que puedan surgir del uso de esta traducción.