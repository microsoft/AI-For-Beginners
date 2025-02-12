# IA Ética y Responsable

Has casi terminado este curso, y espero que ahora veas claramente que la IA se basa en una serie de métodos matemáticos formales que nos permiten encontrar relaciones en los datos y entrenar modelos para replicar algunos aspectos del comportamiento humano. En este momento de la historia, consideramos que la IA es una herramienta muy poderosa para extraer patrones de los datos y aplicar esos patrones para resolver nuevos problemas.

## [Cuestionario previo a la clase](https://white-water-09ec41f0f.azurestaticapps.net/quiz/5/)

Sin embargo, en la ciencia ficción a menudo vemos historias donde la IA presenta un peligro para la humanidad. Generalmente, estas historias giran en torno a algún tipo de rebelión de la IA, cuando esta decide confrontar a los seres humanos. Esto implica que la IA tiene algún tipo de emoción o puede tomar decisiones imprevistas por sus desarrolladores.

El tipo de IA que hemos aprendido en este curso no es más que una aritmética de matrices grande. Es una herramienta muy poderosa que nos ayuda a resolver nuestros problemas, y como cualquier otra herramienta poderosa, puede ser utilizada para fines buenos y malos. Es importante destacar que puede ser *mal utilizada*.

## Principios de la IA Responsable

Para evitar este uso accidental o intencionado de la IA, Microsoft establece los importantes [Principios de la IA Responsable](https://www.microsoft.com/ai/responsible-ai?WT.mc_id=academic-77998-cacaste). Los siguientes conceptos sustentan estos principios:

* **Equidad** está relacionada con el importante problema de los *sesgos en los modelos*, que pueden ser causados por el uso de datos sesgados para el entrenamiento. Por ejemplo, cuando intentamos predecir la probabilidad de conseguir un trabajo como desarrollador de software para una persona, es probable que el modelo dé mayor preferencia a los hombres, simplemente porque el conjunto de datos de entrenamiento probablemente estaba sesgado hacia una audiencia masculina. Necesitamos equilibrar cuidadosamente los datos de entrenamiento e investigar el modelo para evitar sesgos, y asegurarnos de que el modelo tenga en cuenta características más relevantes.
* **Fiabilidad y Seguridad**. Por su naturaleza, los modelos de IA pueden cometer errores. Una red neuronal devuelve probabilidades, y debemos tenerlo en cuenta al tomar decisiones. Cada modelo tiene una cierta precisión y recuperación, y necesitamos entender eso para prevenir el daño que puede causar un consejo erróneo.
* **Privacidad y Seguridad** tienen algunas implicaciones específicas de la IA. Por ejemplo, cuando usamos algunos datos para entrenar un modelo, esos datos se integran de alguna manera en el modelo. Por un lado, eso aumenta la seguridad y la privacidad; por otro, debemos recordar sobre qué datos se entrenó el modelo.
* **Inclusividad** significa que no estamos construyendo IA para reemplazar a las personas, sino para aumentar a las personas y hacer nuestro trabajo más creativo. También está relacionado con la equidad, porque al tratar con comunidades subrepresentadas, la mayoría de los conjuntos de datos que recopilamos probablemente estén sesgados, y debemos asegurarnos de que esas comunidades estén incluidas y manejadas correctamente por la IA.
* **Transparencia**. Esto incluye asegurarnos de que siempre seamos claros sobre el uso de la IA. Además, siempre que sea posible, queremos utilizar sistemas de IA que sean *interpretables*.
* **Responsabilidad**. Cuando los modelos de IA toman decisiones, no siempre está claro quién es responsable de esas decisiones. Necesitamos asegurarnos de que entendemos dónde radica la responsabilidad de las decisiones de la IA. En la mayoría de los casos, querríamos incluir a seres humanos en el proceso de toma de decisiones importantes, para que las personas reales sean responsables.

## Herramientas para la IA Responsable

Microsoft ha desarrollado la [Caja de Herramientas de IA Responsable](https://github.com/microsoft/responsible-ai-toolbox) que contiene un conjunto de herramientas:

* Panel de Interpretabilidad (InterpretML)
* Panel de Equidad (FairLearn)
* Panel de Análisis de Errores
* Panel de IA Responsable que incluye

   - EconML - herramienta para Análisis Causal, que se centra en preguntas hipotéticas
   - DiCE - herramienta para Análisis Contrafactual que te permite ver qué características deben cambiarse para afectar la decisión del modelo

Para más información sobre Ética de la IA, visita [esta lección](https://github.com/microsoft/ML-For-Beginners/tree/main/1-Introduction/3-fairness?WT.mc_id=academic-77998-cacaste) en el Currículo de Aprendizaje Automático que incluye tareas.

## Revisión y Autoestudio

Realiza este [Ruta de Aprendizaje](https://docs.microsoft.com/learn/modules/responsible-ai-principles/?WT.mc_id=academic-77998-cacaste) para aprender más sobre la IA responsable.

## [Cuestionario posterior a la clase](https://white-water-09ec41f0f.azurestaticapps.net/quiz/6/)

**Disclaimer**:  
This document has been translated using machine-based AI translation services. While we strive for accuracy, please be aware that automated translations may contain errors or inaccuracies. The original document in its native language should be considered the authoritative source. For critical information, professional human translation is recommended. We are not liable for any misunderstandings or misinterpretations arising from the use of this translation.