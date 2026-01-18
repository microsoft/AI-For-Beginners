<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "178c0b5ee5395733eb18aec51e71a0a9",
  "translation_date": "2025-09-23T11:44:41+00:00",
  "source_file": "lessons/4-ComputerVision/08-TransferLearning/README.md",
  "language_code": "en"
}
-->
# Pre-trained Networks and Transfer Learning

Training CNNs can be time-consuming and requires a significant amount of data. However, much of the training process involves learning the optimal low-level filters that a network uses to extract patterns from images. This raises an interesting question: can we use a neural network trained on one dataset and adapt it to classify different images without undergoing a full training process?

## [Pre-lecture quiz](https://ff-quizzes.netlify.app/en/ai/quiz/15)

This method is known as **transfer learning**, as it involves transferring knowledge from one neural network model to another. In transfer learning, we typically start with a pre-trained model that has been trained on a large image dataset, such as **ImageNet**. These models are already proficient at extracting features from generic images, and in many cases, simply building a classifier on top of these extracted features can yield excellent results.

> ✅ Transfer Learning is a term also used in other academic fields, such as Education. It refers to the process of applying knowledge from one domain to another.

## Pre-Trained Models as Feature Extractors

The convolutional networks discussed in the previous section consist of multiple layers, each designed to extract features from images. These range from low-level pixel combinations (e.g., horizontal/vertical lines or strokes) to higher-level feature combinations, such as the shape of an eye or flame. When trained on a sufficiently large and diverse dataset, the network learns to extract these common features.

Both Keras and PyTorch provide functions to easily load pre-trained neural network weights for popular architectures, most of which were trained on ImageNet images. Some commonly used architectures are described on the [CNN Architectures](../07-ConvNets/CNN_Architectures.md) page from the previous lesson. You might consider using one of the following:

* **VGG-16/VGG-19**: Relatively simple models that still deliver good accuracy. These are often a good starting point to test how transfer learning works.
* **ResNet**: A family of models introduced by Microsoft Research in 2015. They have more layers and require more computational resources.
* **MobileNet**: A family of models optimized for reduced size, making them suitable for mobile devices. Use these if you have limited resources and can tolerate a slight drop in accuracy.

Below are sample features extracted from a picture of a cat using the VGG-16 network:

![Features extracted by VGG-16](../../../../../translated_images/en/features.6291f9c7ba3a0b951af88fc9864632b9115365410765680680d30c927dd67354.png)

## Cats vs. Dogs Dataset

For this example, we will use a dataset of [Cats and Dogs](https://www.microsoft.com/download/details.aspx?id=54765&WT.mc_id=academic-77998-cacaste), which closely resembles a real-world image classification scenario.

## ✍️ Exercise: Transfer Learning

Explore transfer learning in action through the following notebooks:

* [Transfer Learning - PyTorch](TransferLearningPyTorch.ipynb)
* [Transfer Learning - TensorFlow](TransferLearningTF.ipynb)

## Visualizing Adversarial Cat

A pre-trained neural network contains various patterns within its *brain*, including representations of an **ideal cat** (as well as an ideal dog, zebra, etc.). It would be fascinating to **visualize these images**, but this is challenging because the patterns are distributed across the network's weights and organized hierarchically.

One approach is to start with a random image and use **gradient descent optimization** to adjust the image so that the network perceives it as a cat.

![Image Optimization Loop](../../../../../translated_images/en/ideal-cat-loop.999fbb8ff306e044f997032f4eef9152b453e6a990e449bbfb107de2493cc37e.png)

However, this process often results in images resembling random noise. This happens because *there are many ways to make the network think an input image is a cat*, including ways that are visually nonsensical. While these images contain patterns typical of a cat, they lack constraints to make them visually distinct.

To improve the result, we can add another term to the loss function called **variation loss**. This metric measures how similar neighboring pixels in the image are. Minimizing variation loss smooths the image and reduces noise, revealing more visually appealing patterns. Below are examples of "ideal" images classified as a cat and a zebra with high confidence:

![Ideal Cat](../../../../../translated_images/en/ideal-cat.203dd4597643d6b0bd73038b87f9c0464322725e3a06ab145d25d4a861c70592.png) | ![Ideal Zebra](../../../../../translated_images/en/ideal-zebra.7f70e8b54ee15a7a314000bb5df38a6cfe086ea04d60df4d3ef313d046b98a2b.png)
-----|-----
 *Ideal Cat* | *Ideal Zebra*

A similar approach can be used for **adversarial attacks** on a neural network. For instance, if we want to trick a neural network into classifying a dog as a cat, we can start with an image of a dog (recognized as a dog by the network) and tweak it slightly using gradient descent optimization until the network classifies it as a cat:

![Picture of a Dog](../../../../../translated_images/en/original-dog.8f68a67d2fe0911f33041c0f7fce8aa4ea919f9d3917ec4b468298522aeb6356.png) | ![Picture of a dog classified as a cat](../../../../../translated_images/en/adversarial-dog.d9fc7773b0142b89752539bfbf884118de845b3851c5162146ea0b8809fc820f.png)
-----|-----
*Original picture of a dog* | *Picture of a dog classified as a cat*

You can find the code to reproduce the above results in the following notebook:

* [Ideal and Adversarial Cat - TensorFlow](AdversarialCat_TF.ipynb)

## Conclusion

Transfer learning allows you to quickly create a classifier for custom object classification tasks and achieve high accuracy. As tasks become more complex, they require greater computational power and are not easily solved on a CPU. In the next unit, we will explore a more lightweight implementation to train the same model using fewer computational resources, with only a slight reduction in accuracy.

## 🚀 Challenge

In the accompanying notebooks, there are notes at the bottom discussing how transfer learning works best with somewhat similar training data (e.g., a new type of animal). Experiment with completely different types of images to evaluate how well or poorly your transfer learning models perform.

## [Post-lecture quiz](https://ff-quizzes.netlify.app/en/ai/quiz/16)

## Review & Self Study

Read through [TrainingTricks.md](TrainingTricks.md) to deepen your understanding of additional techniques for training models.

## [Assignment](lab/README.md)

In this lab, we will use the real-world [Oxford-IIIT](https://www.robots.ox.ac.uk/~vgg/data/pets/) pets dataset, which includes 35 breeds of cats and dogs, to build a transfer learning classifier.

---

