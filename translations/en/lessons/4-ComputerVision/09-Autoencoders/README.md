<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "1b8d9e1b3a6f1daa864b1ff3dfc3076d",
  "translation_date": "2025-09-23T11:45:57+00:00",
  "source_file": "lessons/4-ComputerVision/09-Autoencoders/README.md",
  "language_code": "en"
}
-->
# Autoencoders

When training CNNs, one of the challenges is the need for a large amount of labeled data. For example, in image classification, we must manually categorize images into different classes.

## [Pre-lecture quiz](https://ff-quizzes.netlify.app/en/ai/quiz/17)

However, we might want to use raw (unlabeled) data to train CNN feature extractors, a process known as **self-supervised learning**. Instead of labels, we use the training images as both the input and output of the network. The main idea behind an **autoencoder** is to have an **encoder network** that transforms the input image into a **latent space** (usually a smaller-sized vector) and a **decoder network** that reconstructs the original image.

> ✅ An [autoencoder](https://wikipedia.org/wiki/Autoencoder) is "a type of artificial neural network used to learn efficient codings of unlabeled data."

By training an autoencoder to capture as much information as possible from the original image for accurate reconstruction, the network attempts to find the best **embedding** of the input images to represent their meaning.

![AutoEncoder Diagram](../../../../../translated_images/en/autoencoder_schema.5e6fc9ad98a5eb6197f3513cf3baf4dfbe1389a6ae74daebda64de9f1c99f142.jpg)

> Image from [Keras blog](https://blog.keras.io/building-autoencoders-in-keras.html)

## Scenarios for using Autoencoders

While reconstructing original images may not seem useful on its own, there are several scenarios where autoencoders are particularly valuable:

* **Reducing image dimensions for visualization** or **training image embeddings**. Autoencoders often outperform PCA because they account for the spatial nature of images and hierarchical features.
* **Denoising**, or removing noise from images. Since noise contains a lot of irrelevant information, the autoencoder cannot fit all of it into the relatively small latent space, focusing instead on the essential parts of the image. When training denoisers, we start with original images and use artificially noise-added images as the autoencoder input.
* **Super-resolution**, or increasing image resolution. We start with high-resolution images and use their lower-resolution versions as the autoencoder input.
* **Generative models**. Once the autoencoder is trained, the decoder can generate new objects by starting with random latent vectors.

## Variational Autoencoders (VAE)

Traditional autoencoders reduce the input data's dimensionality, identifying the key features of input images. However, the latent vectors often lack interpretability. For instance, in the MNIST dataset, it’s not straightforward to determine which digits correspond to specific latent vectors, as nearby latent vectors may not represent the same digit.

For generative models, it’s beneficial to have a more structured understanding of the latent space. This leads to the concept of **variational autoencoders** (VAE).

A VAE is an autoencoder that learns to predict the *statistical distribution* of latent parameters, known as the **latent distribution**. For example, we might want latent vectors to follow a normal distribution with a mean z<sub>mean</sub> and standard deviation z<sub>sigma</sub> (both are vectors of some dimensionality d). The encoder in a VAE predicts these parameters, and the decoder reconstructs the object using a random vector sampled from this distribution.

To summarize:

 * From the input vector, we predict `z_mean` and `z_log_sigma` (instead of predicting the standard deviation directly, we predict its logarithm).
 * We sample a vector `sample` from the distribution N(z<sub>mean</sub>, exp(z<sub>log_sigma</sub>)).
 * The decoder reconstructs the original image using `sample` as the input vector.

 <img src="images/vae.png" width="50%">

> Image from [this blog post](https://ijdykeman.github.io/ml/2016/12/21/cvae.html) by Isaak Dykeman

Variational autoencoders use a complex loss function with two components:

* **Reconstruction loss**, which measures how closely the reconstructed image matches the target (e.g., Mean Squared Error or MSE). This is the same loss function used in standard autoencoders.
* **KL loss**, which ensures that the latent variable distribution remains close to a normal distribution. This is based on the concept of [Kullback-Leibler divergence](https://www.countbayesie.com/blog/2017/5/9/kullback-leibler-divergence-explained), a metric for comparing two statistical distributions.

One key advantage of VAEs is their ability to generate new images easily, as the latent vector distribution is well-defined. For example, if we train a VAE with a 2D latent vector on MNIST, we can vary the components of the latent vector to generate different digits:

<img alt="vaemnist" src="images/vaemnist.png" width="50%"/>

> Image by [Dmitry Soshnikov](http://soshnikov.com)

Notice how the images transition smoothly, as latent vectors are sampled from different regions of the latent parameter space. We can also visualize this space in 2D:

<img alt="vaemnist cluster" src="images/vaemnist-diag.png" width="50%"/> 

> Image by [Dmitry Soshnikov](http://soshnikov.com)

## ✍️ Exercises: Autoencoders

Learn more about autoencoders in these corresponding notebooks:

* [Autoencoders in TensorFlow](AutoencodersTF.ipynb)
* [Autoencoders in PyTorch](AutoEncodersPyTorch.ipynb)

## Properties of Autoencoders

* **Data Specific** - Autoencoders perform well only on the type of images they were trained on. For instance, a super-resolution network trained on flowers will not work well on portraits. This is because the network uses fine details learned from the training dataset to enhance resolution.
* **Lossy** - The reconstructed image is not identical to the original image. The nature of the loss depends on the *loss function* used during training.
* Works on **unlabeled data**.

## [Post-lecture quiz](https://ff-quizzes.netlify.app/en/ai/quiz/18)

## Conclusion

In this lesson, you learned about the different types of autoencoders available to AI practitioners. You explored how to build them and use them to reconstruct images. Additionally, you learned about VAEs and how they can be used to generate new images.

## 🚀 Challenge

In this lesson, you learned about using autoencoders for images. But they can also be applied to music! Check out the Magenta project's [MusicVAE](https://magenta.tensorflow.org/music-vae), which uses autoencoders to reconstruct music. Try some [experiments](https://colab.research.google.com/github/magenta/magenta-demos/blob/master/colab-notebooks/Multitrack_MusicVAE.ipynb) with this library to see what you can create.

## [Post-lecture quiz](https://ff-quizzes.netlify.app/en/ai/quiz/16)

## Review & Self Study

For further reading, explore these resources on autoencoders:

* [Building Autoencoders in Keras](https://blog.keras.io/building-autoencoders-in-keras.html)
* [Blog post on NeuroHive](https://neurohive.io/ru/osnovy-data-science/variacionnyj-avtojenkoder-vae/)
* [Variational Autoencoders Explained](https://kvfrans.com/variational-autoencoders-explained/)
* [Conditional Variational Autoencoders](https://ijdykeman.github.io/ml/2016/12/21/cvae.html)

## Assignment

At the end of [this notebook using TensorFlow](AutoencodersTF.ipynb), you will find a 'task' - use this as your assignment.

---

