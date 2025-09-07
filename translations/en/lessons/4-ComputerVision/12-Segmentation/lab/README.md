<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "365f0decfe0f47b460bbde8227c5009d",
  "translation_date": "2025-08-31T17:42:56+00:00",
  "source_file": "lessons/4-ComputerVision/12-Segmentation/lab/README.md",
  "language_code": "en"
}
-->
# Human Body Segmentation

Lab Assignment from [AI for Beginners Curriculum](https://github.com/microsoft/ai-for-beginners).

## Task

In video production, such as weather forecasts, it's often necessary to extract a human image from the camera and overlay it onto other footage. This is usually achieved using **chroma key** techniques, where a person is filmed against a solid-colored background that is later removed. In this lab, we will train a neural network model to extract the human silhouette.

## The Dataset

We will use the [Segmentation Full Body MADS Dataset](https://www.kaggle.com/datasets/tapakah68/segmentation-full-body-mads-dataset) from Kaggle. Download the dataset manually from Kaggle.

## Starting Notebook

Begin the lab by opening [BodySegmentation.ipynb](BodySegmentation.ipynb)

## Takeaway

Body segmentation is just one of the many tasks that can be performed with images of people. Other important tasks include **skeleton detection** and **pose detection**. Check out the [OpenPose](https://github.com/CMU-Perceptual-Computing-Lab/openpose) library to explore how these tasks can be implemented.

---

**Disclaimer**:  
This document has been translated using the AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). While we aim for accuracy, please note that automated translations may include errors or inaccuracies. The original document in its native language should be regarded as the authoritative source. For critical information, professional human translation is advised. We are not responsible for any misunderstandings or misinterpretations resulting from the use of this translation.