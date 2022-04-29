# Multi-Class Classification with Perceptron

Lab Assignment from [AI for Beginners Curriculum](https://github.com/microsoft/ai-for-beginners).

## Task

Using the code we have developed in this lesson for binary classification of MNIST handwritten digits, create a multi-class classified that would be able to recognize any digit. Compute the classification accuracy on the train and test dataset, and print out the confusion matrix.

## Hints

1. For each digit, create a dataset for binary classifier of "this digit vs. all other digits"
1. Train 10 different perceptrons for binary classification (one for each digit)
1. Define a function that will classify an input digit

> **Hint**: If we combine weights of all 10 perceptrons into one matrix, we should be able to apply all 10 perceptrons to the input digits by one matrix multiplication. Most probable digit can then be found just by applying `argmax` operation on the output.

## Stating Notebook

Start the lab by opening [PerceptronMultiClass.ipynb](PerceptronMultiClass.ipynb)
