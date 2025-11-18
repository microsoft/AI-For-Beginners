<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "1b8d9e1b3a6f1daa864b1ff3dfc3076d",
  "translation_date": "2025-11-18T18:21:02+00:00",
  "source_file": "lessons/4-ComputerVision/09-Autoencoders/README.md",
  "language_code": "pcm"
}
-->
# Autoencoders

Wen we dey train CNNs, one wahala wey dey be say we need plenty labeled data. For image classification, we go need separate images into different classes, and na manual work.

## [Pre-lecture quiz](https://ff-quizzes.netlify.app/en/ai/quiz/17)

But, we fit wan use raw (unlabeled) data to train CNN feature extractors, wey dem dey call **self-supervised learning**. Instead of labels, we go use training images as both network input and output. The main idea of **autoencoder** be say we go get **encoder network** wey go change input image into some **latent space** (normally na just vector wey small pass the original image), then **decoder network**, wey go try reconstruct the original image.

> ✅ An [autoencoder](https://wikipedia.org/wiki/Autoencoder) na "one type of artificial neural network wey dem dey use learn efficient codings of unlabeled data."

Since we dey train autoencoder to capture as much information from the original image as e fit for accurate reconstruction, the network go try find the best **embedding** of input images to capture the meaning.

![AutoEncoder Diagram](../../../../../translated_images/autoencoder_schema.5e6fc9ad98a5eb6197f3513cf3baf4dfbe1389a6ae74daebda64de9f1c99f142.pcm.jpg)

> Image from [Keras blog](https://blog.keras.io/building-autoencoders-in-keras.html)

## Scenarios wey Autoencoders dey useful

Even though reconstructing original images no dey useful on e own, some scenarios dey wey autoencoders dey make sense:

* **To reduce image dimension for visualization** or **to train image embeddings**. Autoencoders dey usually give better results than PCA, because e dey consider the spatial nature of images and hierarchical features.
* **Denoising**, wey mean to remove noise from image. Since noise dey carry plenty useless information, autoencoder no fit pack all the noise inside the small latent space, so e go only capture the important part of the image. For denoisers, we go start with original images, then use images wey we don add artificial noise as input for autoencoder.
* **Super-resolution**, wey mean to increase image resolution. We go start with high-resolution images, then use the image wey get lower resolution as autoencoder input.
* **Generative models**. Once we don train the autoencoder, the decoder part fit dey used to create new objects starting from random latent vectors.

## Variational Autoencoders (VAE)

Traditional autoencoders dey reduce the dimension of input data somehow, dey figure out the important features of input images. But, latent vectors no dey make much sense. For example, if we use MNIST dataset, e go hard to know which digits dey correspond to different latent vectors, because close latent vectors no go necessarily mean the same digits.

But, for *generative* models, e better make we understand the latent space. This idea na wetin lead us to **variational auto-encoder** (VAE).

VAE na autoencoder wey dey learn to predict *statistical distribution* of the latent parameters, wey dem dey call **latent distribution**. For example, we fit wan make latent vectors dey normally distributed with some mean z<sub>mean</sub> and standard deviation z<sub>sigma</sub> (both mean and standard deviation na vectors of some dimensionality d). Encoder for VAE go learn to predict those parameters, then decoder go take random vector from this distribution to reconstruct the object.

To summarize:

 * From input vector, we go predict `z_mean` and `z_log_sigma` (instead of predicting the standard deviation itself, we go predict e logarithm)
 * We go sample one vector `sample` from the distribution N(z<sub>mean</sub>,exp(z<sub>log\_sigma</sub>))
 * The decoder go try decode the original image using `sample` as input vector

 <img src="../../../../../translated_images/vae.464c465a5b6a9e253be65a8cb3be1724832cbde57ece3912ddc962b199472a89.pcm.png" width="50%">

> Image from [this blog post](https://ijdykeman.github.io/ml/2016/12/21/cvae.html) by Isaak Dykeman

Variational auto-encoders dey use one complex loss function wey get two parts:

* **Reconstruction loss** na the loss function wey dey show how close reconstructed image dey to the target (e fit be Mean Squared Error, or MSE). Na the same loss function wey normal autoencoders dey use.
* **KL loss**, wey dey make sure say latent variable distributions dey close to normal distribution. E dey based on the idea of [Kullback-Leibler divergence](https://www.countbayesie.com/blog/2017/5/9/kullback-leibler-divergence-explained) - one metric wey dey estimate how similar two statistical distributions be.

One big advantage of VAEs be say e dey allow us generate new images easily, because we sabi the distribution wey we go sample latent vectors from. For example, if we train VAE with 2D latent vector on MNIST, we fit vary components of the latent vector to get different digits:

<img alt="vaemnist" src="../../../../../translated_images/vaemnist.cab9e602dc08dc5066ce14e005889d6b53ca5bcaf16e35c28dbf8cd40c304de1.pcm.png" width="50%"/>

> Image by [Dmitry Soshnikov](http://soshnikov.com)

See as images dey blend into each other, as we dey get latent vectors from different parts of the latent parameter space. We fit also visualize this space for 2D:

<img alt="vaemnist cluster" src="../../../../../translated_images/vaemnist-diag.694315f775d5d666b02fb54f8fc7c64db65a9d126a16c2fdb8683cf9726f9ff5.pcm.png" width="50%"/> 

> Image by [Dmitry Soshnikov](http://soshnikov.com)

## ✍️ Exercises: Autoencoders

Learn more about autoencoders for these notebooks:

* [Autoencoders in TensorFlow](AutoencodersTF.ipynb)
* [Autoencoders in PyTorch](AutoEncodersPyTorch.ipynb)

## Properties of Autoencoders

* **Data Specific** - dem dey work well only with the type of images wey dem don train on. For example, if we train super-resolution network on flowers, e no go work well for portraits. This na because the network dey produce higher resolution image by using fine details from features wey e learn from the training dataset.
* **Lossy** - the reconstructed image no dey exactly the same as the original image. The type of loss dey depend on the *loss function* wey dem use during training.
* E dey work on **unlabeled data**

## [Post-lecture quiz](https://ff-quizzes.netlify.app/en/ai/quiz/18)

## Conclusion

For this lesson, you don learn about the different types of autoencoders wey AI scientists dey use. You don learn how to build them, and how to use them to reconstruct images. You don also learn about VAE and how to use am to generate new images.

## 🚀 Challenge

For this lesson, you don learn how to use autoencoders for images. But dem fit also dey used for music! Check out Magenta project [MusicVAE](https://magenta.tensorflow.org/music-vae) project, wey dey use autoencoders to learn how to reconstruct music. Try some [experiments](https://colab.research.google.com/github/magenta/magenta-demos/blob/master/colab-notebooks/Multitrack_MusicVAE.ipynb) with this library to see wetin you fit create.

## [Post-lecture quiz](https://ff-quizzes.netlify.app/en/ai/quiz/16)

## Review & Self Study

For reference, read more about autoencoders for these resources:

* [Building Autoencoders in Keras](https://blog.keras.io/building-autoencoders-in-keras.html)
* [Blog post on NeuroHive](https://neurohive.io/ru/osnovy-data-science/variacionnyj-avtojenkoder-vae/)
* [Variational Autoencoders Explained](https://kvfrans.com/variational-autoencoders-explained/)
* [Conditional Variational Autoencoders](https://ijdykeman.github.io/ml/2016/12/21/cvae.html)

## Assignment

For the end of [this notebook using TensorFlow](AutoencodersTF.ipynb), you go see one 'task' - use am as your assignment.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:  
Dis dokyument don use AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator) do di translation. Even as we dey try make am accurate, abeg sabi say automated translations fit get mistake or no dey correct well. Di original dokyument for im native language na di main source wey you go fit trust. For important information, e good make professional human translation dey use. We no go fit take blame for any misunderstanding or wrong interpretation wey fit happen because you use dis translation.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->