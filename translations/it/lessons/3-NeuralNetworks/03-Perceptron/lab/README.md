# Clasificación Multiclase con Perceptrón

Tarea del [Currículo de IA para Principiantes](https://github.com/microsoft/ai-for-beginners).

## Tarea

Usando el código que hemos desarrollado en esta lección para la clasificación binaria de dígitos manuscritos MNIST, crea un clasificador multiclase que sea capaz de reconocer cualquier dígito. Calcula la precisión de clasificación en el conjunto de datos de entrenamiento y prueba, y muestra la matriz de confusión.

## Sugerencias

1. Para cada dígito, crea un conjunto de datos para el clasificador binario de "este dígito vs. todos los demás dígitos".
1. Entrena 10 perceptrones diferentes para clasificación binaria (uno para cada dígito).
1. Define una función que clasifique un dígito de entrada.

> **Sugerencia**: Si combinamos los pesos de los 10 perceptrones en una sola matriz, deberíamos poder aplicar los 10 perceptrones a los dígitos de entrada mediante una multiplicación de matrices. El dígito más probable se puede encontrar simplemente aplicando la operación `argmax` sobre la salida.

## Notebook Inicial

Comienza el laboratorio abriendo [PerceptronMultiClass.ipynb](../../../../../../lessons/3-NeuralNetworks/03-Perceptron/lab/PerceptronMultiClass.ipynb).

**Disclaimer**: 
This document has been translated using machine-based AI translation services. While we strive for accuracy, please be aware that automated translations may contain errors or inaccuracies. The original document in its native language should be considered the authoritative source. For critical information, professional human translation is recommended. We are not liable for any misunderstandings or misinterpretations arising from the use of this translation.