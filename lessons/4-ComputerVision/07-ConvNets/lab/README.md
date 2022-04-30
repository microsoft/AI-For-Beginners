# Classification of Pets Faces

Lab Assignment from [AI for Beginners Curriculum](https://github.com/microsoft/ai-for-beginners).

## Task

Imagine you need to develop and application for pet nursery to catalog all pets. One of the great features of such an application would be automatically discovering the breed from a photograph. This can be successfully done using neural networks.

You need to train a convolutional neural network to classify different breeds of cats and dogs using **Pet Faces** dataset.

## The Dataset

We will use the **Pet Faces** dataset, derived from [Oxford-IIIT](https://www.robots.ox.ac.uk/~vgg/data/pets/) pets dataset. It contains 35 different breeds of dogs and cats.

![Dataset we will deal with](images/data.png)

To download the dataset, use this code snippet:

```python
!wget https://mslearntensorflowlp.blob.core.windows.net/data/petfaces.tar.gz
!tar xfz petfaces.tar.gz
!rm petfaces.tar.gz
```

## Stating Notebook

Start the lab by opening [PetFaces.ipynb](PetFaces.ipynb)

## Takeaway

You have solved a relatively complex problem of image classification from scratch! There were quite a lot of classes, and you were still able to get reasonable accuracy! It also makes sense to measure top-k accuracy, because it is easy to confuse some of the classes which are not clearly different even to human beings.
