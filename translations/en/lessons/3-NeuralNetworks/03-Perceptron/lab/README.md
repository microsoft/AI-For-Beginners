<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "ba5d1eb353d20d3e7181066b3c424b99",
  "translation_date": "2025-08-31T17:50:44+00:00",
  "source_file": "lessons/3-NeuralNetworks/03-Perceptron/lab/README.md",
  "language_code": "en"
}
-->
# Multi-Class Classification with Perceptron

Lab Assignment from [AI for Beginners Curriculum](https://github.com/microsoft/ai-for-beginners).

## Task

Using the code developed in this lesson for binary classification of MNIST handwritten digits, create a multi-class classifier capable of recognizing any digit. Calculate the classification accuracy on the training and test datasets, and display the confusion matrix.

## Hints

1. For each digit, create a dataset for a binary classifier of "this digit vs. all other digits."
2. Train 10 different perceptrons for binary classification (one for each digit).
3. Define a function that classifies an input digit.

> **Hint**: If we combine the weights of all 10 perceptrons into one matrix, we can apply all 10 perceptrons to the input digits with a single matrix multiplication. The most probable digit can then be determined by simply applying the `argmax` operation on the output.

## Starting Notebook

Begin the lab by opening [PerceptronMultiClass.ipynb](PerceptronMultiClass.ipynb)

---

**Disclaimer**:  
This document has been translated using the AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). While we aim for accuracy, please note that automated translations may include errors or inaccuracies. The original document in its native language should be regarded as the authoritative source. For critical information, professional human translation is advised. We are not responsible for any misunderstandings or misinterpretations resulting from the use of this translation.