# IA ética y responsable

Ya casi has terminado este curso y espero que ahora veas claramente que la IA se basa en una serie de métodos matemáticos formales que nos permiten encontrar relaciones en los datos y entrenar modelos para replicar algunos aspectos del comportamiento humano. En este momento de la historia, consideramos que la IA es una herramienta muy poderosa para extraer patrones de datos y aplicar esos patrones para resolver nuevos problemas.

## [Pre-lecture quiz](https://white-water-09ec41f0f.azurestaticapps.net/quiz/5/)

Sin embargo, en la ciencia ficción vemos a menudo historias en las que la IA representa un peligro para la humanidad. Por lo general, esas historias se centran en algún tipo de rebelión de la IA, cuando la IA decide enfrentarse a los seres humanos. Esto implica que la IA tiene algún tipo de emoción o puede tomar decisiones imprevistas por sus desarrolladores.

El tipo de IA que hemos aprendido en este curso no es más que aritmética de matrices grandes. Es una herramienta muy poderosa para ayudarnos a resolver nuestros problemas y, como cualquier otra herramienta poderosa, puede usarse para bien o para mal. Es importante destacar que se puede *usar mal*.

## Principios de una IA responsable

Para evitar este mal uso accidental o intencionado de la IA, Microsoft afirma la importante [Principles of Responsible AI](https://www.microsoft.com/ai/responsible-ai?WT.mc_id=academic-77998-cacaste). Los siguientes conceptos sustentan estos principios:

* **La equidad** está relacionada con el importante problema de los *sesgos del modelo*, que pueden deberse al uso de datos sesgados para el entrenamiento. Por ejemplo, cuando intentamos predecir la probabilidad de que una persona consiga un trabajo de desarrollador de software, es probable que el modelo dé mayor preferencia a los hombres, simplemente porque el conjunto de datos de entrenamiento probablemente estaba sesgado hacia una audiencia masculina. Necesitamos equilibrar cuidadosamente los datos de entrenamiento e investigar el modelo para evitar sesgos y asegurarnos de que el modelo tenga en cuenta características más relevantes.
* **Confiabilidad y Seguridad**. Por su naturaleza, los modelos de IA pueden cometer errores. Una red neuronal devuelve probabilidades y debemos tenerlas en cuenta a la hora de tomar decisiones. Cada modelo tiene cierta precisión y recuerdo, y debemos entenderlo para evitar el daño que pueden causar los consejos incorrectos.
* **Privacidad y seguridad** tienen algunas implicaciones específicas de la IA. Por ejemplo, cuando utilizamos algunos datos para entrenar un modelo, estos datos se "integran" de alguna manera en el modelo. Por un lado, esto aumenta la seguridad y la privacidad; por otro, debemos recordar con qué datos se entrenó el modelo.
* **Inclusividad** significa que no estamos creando IA para reemplazar a las personas, sino para aumentarlas y hacer que nuestro trabajo sea más creativo. También está relacionado con la equidad, porque cuando tratamos con comunidades subrepresentadas, es probable que la mayoría de los conjuntos de datos que recopilamos estén sesgados, y debemos asegurarnos de que esas comunidades estén incluidas y manejadas correctamente por la IA.
* **Transparencia**. Esto incluye asegurarnos de que siempre tengamos claro el uso de la IA. Además, siempre que sea posible, queremos utilizar sistemas de IA que sean *interpretables*.
* **Responsabilidad**. Cuando los modelos de IA toman algunas decisiones, no siempre está claro quién es responsable de esas decisiones. Necesitamos asegurarnos de comprender dónde reside la responsabilidad de las decisiones de la IA. En la mayoría de los casos, querríamos incluir a los seres humanos en el proceso de toma de decisiones importantes, de modo que personas reales rindan cuentas.

## Herramientas para una IA responsable

Microsoft ha desarrollado el [Responsible AI Toolbox](https://github.com/microsoft/responsible-ai-toolbox) que contiene un conjunto de herramientas:

* Panel de interpretabilidad (InterpretML)
* Panel de equidad (FairLearn)
* Panel de análisis de errores
* Panel de control de IA responsable que incluye

    - EconML: herramienta para análisis causal, que se centra en preguntas hipotéticas.
    - DiCE: herramienta para análisis contrafactual que le permite ver qué características deben cambiarse para afectar la decisión del modelo.

Para obtener más información sobre la ética de la IA, visite [this lesson](https://github.com/microsoft/ML-For-Beginners/tree/main/1-Introduction/3-fairness?WT.mc_id=academic-77998-cacaste) en el plan de estudios de aprendizaje automático que incluye tareas.

## Revisión y autoestudio

Toma esto [Learn Path](https://docs.microsoft.com/learn/modules/responsible-ai-principles/?WT.mc_id=academic-77998-cacaste) to learn more about responsible AI.

## [Post-lecture quiz](https://white-water-09ec41f0f.azurestaticapps.net/quiz/6/)

