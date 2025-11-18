<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "ba5d1eb353d20d3e7181066b3c424b99",
  "translation_date": "2025-11-18T18:28:30+00:00",
  "source_file": "lessons/3-NeuralNetworks/03-Perceptron/lab/README.md",
  "language_code": "pcm"
}
-->
# Multi-Class Classification wit Perceptron

Lab Assignment from [AI for Beginners Curriculum](https://github.com/microsoft/ai-for-beginners).

## Task

Use di code we don develop for dis lesson for binary classification of MNIST handwritten digits, create multi-class classifier wey go fit recognize any digit. Calculate di classification accuracy for di train and test dataset, and print di confusion matrix.

## Hints

1. For each digit, create dataset for binary classifier of "dis digit vs. all di oda digits"
1. Train 10 different perceptrons for binary classification (one for each digit)
1. Define function wey go classify one input digit

> **Hint**: If we join di weights of all 10 perceptrons inside one matrix, we fit apply all 10 perceptrons to di input digits by one matrix multiplication. Di digit wey get di highest probability fit be found just by using `argmax` operation for di output.

## Starting Notebook

Start di lab by opening [PerceptronMultiClass.ipynb](PerceptronMultiClass.ipynb)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:  
Dis docu don dey translate wit AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). Even though we dey try make am accurate, abeg sabi say automated translation fit get mistake or no correct well. Di original docu for im native language na di main correct source. For important information, e go beta make professional human translator check am. We no go dey responsible for any misunderstanding or wrong interpretation wey fit happen because you use dis translation.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->