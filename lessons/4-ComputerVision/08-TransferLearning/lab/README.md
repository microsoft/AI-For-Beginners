# Classification of Oxford Pets using Transfer Learning

Lab Assignment from [AI for Beginners Curriculum](https://github.com/microsoft/ai-for-beginners).

## Task

Imagine you need to develop and application for pet nursery to catalog all pets. One of the great features of such an application would be automatically discovering the breed from a photograph. In this assignment, we will use transfer learning to classify real-life pet images from [Oxford-IIIT](https://www.robots.ox.ac.uk/~vgg/data/pets/) pets dataset.

## The Dataset

We will use the original [Oxford-IIIT](https://www.robots.ox.ac.uk/~vgg/data/pets/) pets dataset, which contains 35 different breeds of dogs and cats.

To download the dataset, use this code snippet:

```python
!wget https://www.robots.ox.ac.uk/~vgg/data/pets/data/images.tar.gz
!tar xfz images.tar.gz
!rm images.tar.gz
```

## Stating Notebook

Start the lab by opening [OxfordPets.ipynb](OxfordPets.ipynb)

## Takeaway

Transfer learning and pre-trained networks allow us to solve real-world image classification problems relatively easily. However, pre-trained networks work well on images of similar kind, and if we start classifying very different images (eg. medical images), we are likely to get much worse results.
