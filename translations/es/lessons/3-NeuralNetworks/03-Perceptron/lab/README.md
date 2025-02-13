# Clasificación Multiclase con Perceptrón

Tarea del [Currículo de IA para Principiantes](https://github.com/microsoft/ai-for-beginners).

## Tarea

Usando el código que hemos desarrollado en esta lección para la clasificación binaria de dígitos manuscritos MNIST, crea un clasificador multiclase que sea capaz de reconocer cualquier dígito. Calcula la precisión de clasificación en el conjunto de datos de entrenamiento y prueba, y muestra la matriz de confusión.

## Consejos

1. Para cada dígito, crea un conjunto de datos para el clasificador binario de "este dígito vs. todos los demás dígitos".
2. Entrena 10 perceptrones diferentes para clasificación binaria (uno para cada dígito).
3. Define una función que clasifique un dígito de entrada.

> **Consejo**: Si combinamos los pesos de los 10 perceptrones en una sola matriz, deberíamos poder aplicar los 10 perceptrones a los dígitos de entrada mediante una multiplicación de matrices. El dígito más probable se puede encontrar simplemente aplicando la operación `argmax` en la salida.

## Notebook de Inicio

Comienza el laboratorio abriendo [PerceptronMultiClass.ipynb](../../../../../../lessons/3-NeuralNetworks/03-Perceptron/lab/PerceptronMultiClass.ipynb).

**Descargo de responsabilidad**:  
Este documento ha sido traducido utilizando servicios de traducción automática basados en inteligencia artificial. Aunque nos esforzamos por la precisión, tenga en cuenta que las traducciones automáticas pueden contener errores o inexactitudes. El documento original en su idioma nativo debe considerarse la fuente autorizada. Para información crítica, se recomienda una traducción profesional humana. No somos responsables de malentendidos o malas interpretaciones que surjan del uso de esta traducción.