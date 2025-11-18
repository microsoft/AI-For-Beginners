<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "7765935c35fcee69b9fe2d0cfd6963e2",
  "translation_date": "2025-11-18T18:18:24+00:00",
  "source_file": "lessons/4-ComputerVision/08-TransferLearning/lab/README.md",
  "language_code": "pcm"
}
-->
# Classification of Oxford Pets using Transfer Learning

Lab Assignment from [AI for Beginners Curriculum](https://github.com/microsoft/ai-for-beginners).

## Task

Imagine say you wan develop one app for pet nursery wey go dey catalog all pets. One better feature for dat app na to fit sabi di breed from di photo. For dis assignment, we go use transfer learning to classify real-life pet images from [Oxford-IIIT](https://www.robots.ox.ac.uk/~vgg/data/pets/) pets dataset.

## The Dataset

We go use di original [Oxford-IIIT](https://www.robots.ox.ac.uk/~vgg/data/pets/) pets dataset, wey get 35 different breeds of dogs and cats.

To download di dataset, use dis code snippet:

```python
!wget https://www.robots.ox.ac.uk/~vgg/data/pets/data/images.tar.gz
!tar xfz images.tar.gz
!rm images.tar.gz
```

## Stating Notebook

Start di lab by opening [OxfordPets.ipynb](OxfordPets.ipynb)

## Takeaway

Transfer learning and pre-trained networks dey help us solve real-world image classification problems easy. But, pre-trained networks dey work well for images wey be di same kind, and if we start to classify images wey dey very different (like medical images), di result fit no too good.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:  
Dis docu don dey translate wit AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). Even though we dey try make am accurate, abeg sabi say automated translations fit get mistake or no dey 100% correct. Di original docu for di native language na di main correct source. For important information, e good make una use professional human translation. We no go fit take blame for any misunderstanding or wrong interpretation wey fit happen because of dis translation.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->