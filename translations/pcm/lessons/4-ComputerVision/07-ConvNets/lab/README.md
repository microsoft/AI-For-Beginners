# Classification of Pets Faces

Lab Assignment from [AI for Beginners Curriculum](https://github.com/microsoft/ai-for-beginners).

## Task

Imagine say you wan develop one app for pet nursery wey go dey catalog all di pets. One beta feature for dis kain app na to fit sabi di breed from di photo. Dis one fit work well if we use neural networks.

You go need train one convolutional neural network to classify di different breeds of cats and dogs using **Pet Faces** dataset.

## The Dataset

We go use di [Oxford-IIIT Pet Dataset](https://www.robots.ox.ac.uk/~vgg/data/pets/), wey get pictures of 37 different breeds of dogs and cats.

![Dataset we go use](../../../../../../translated_images/pcm/data.50b2a9d5484bdbf0.webp)

To download di dataset, use dis code snippet:

```python
!wget https://thor.robots.ox.ac.uk/~vgg/data/pets/images.tar.gz
!tar xfz images.tar.gz
!rm images.tar.gz
```

**Note:** Di Oxford-IIIT Pet Dataset pictures dey arranged by filename (e.g., `Abyssinian_1.jpg`, `Bengal_2.jpg`). Di notebook get code wey go help arrange di pictures into breed-specific subdirectories so classification go dey easier.

## Stating Notebook

Start di lab by opening [PetFaces.ipynb](PetFaces.ipynb)

## Takeaway

You don solve one kind complex problem of image classification from scratch! Di classes plenty well well, but you still fit get reasonable accuracy! E still make sense to measure top-k accuracy, because e easy to confuse some classes wey no too clear even for human beings.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:  
Dis dokyument don use AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator) take translate am. Even though we dey try make sure say e correct, abeg sabi say automatic translation fit get mistake or no dey accurate well. Di original dokyument for im native language na im you go take as di correct one. For important information, e good make you use professional human translation. We no go fit hold responsible for any misunderstanding or wrong interpretation wey fit happen because you use dis translation.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->