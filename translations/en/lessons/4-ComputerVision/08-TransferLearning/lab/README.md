<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "7765935c35fcee69b9fe2d0cfd6963e2",
  "translation_date": "2025-08-31T17:38:44+00:00",
  "source_file": "lessons/4-ComputerVision/08-TransferLearning/lab/README.md",
  "language_code": "en"
}
-->
# Classification of Oxford Pets using Transfer Learning

Lab Assignment from [AI for Beginners Curriculum](https://github.com/microsoft/ai-for-beginners).

## Task

Imagine you need to develop an application for a pet nursery to catalog all pets. One of the great features of such an application would be the ability to automatically identify the breed from a photograph. In this assignment, we will use transfer learning to classify real-life pet images from the [Oxford-IIIT](https://www.robots.ox.ac.uk/~vgg/data/pets/) pets dataset.

## The Dataset

We will use the original [Oxford-IIIT](https://www.robots.ox.ac.uk/~vgg/data/pets/) pets dataset, which contains 35 different breeds of dogs and cats.

To download the dataset, use this code snippet:

```python
!wget https://www.robots.ox.ac.uk/~vgg/data/pets/data/images.tar.gz
!tar xfz images.tar.gz
!rm images.tar.gz
```

## Starting Notebook

Begin the lab by opening [OxfordPets.ipynb](OxfordPets.ipynb)

## Takeaway

Transfer learning and pre-trained networks make it relatively easy to solve real-world image classification problems. However, pre-trained networks perform well on images of a similar type, and if we attempt to classify very different images (e.g., medical images), the results are likely to be much less accurate.

---

**Disclaimer**:  
This document has been translated using the AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). While we aim for accuracy, please note that automated translations may include errors or inaccuracies. The original document in its native language should be regarded as the authoritative source. For critical information, professional human translation is advised. We are not responsible for any misunderstandings or misinterpretations resulting from the use of this translation.