# Transfer Learning use karke Oxford Pets ki Classification

[AI for Beginners Curriculum](https://github.com/microsoft/ai-for-beginners) se lab assignment.

## Task

Kalpana kijiye ki aapko ek pet nursery ke liye ek application develop karni hai jo saare pets ko catalog kar sake. Aisi application ka ek badhiya feature yeh hoga ki woh picture se hi automatically breed ko pehchan sake. Is assignment mein, hum transfer learning use karke [Oxford-IIIT](https://www.robots.ox.ac.uk/~vgg/data/pets/) pets dataset se real-life pet images ko classify karenge.

## Dataset

Hum original [Oxford-IIIT](https://www.robots.ox.ac.uk/~vgg/data/pets/) pets dataset use karenge, jisme kutton aur billiyon ki 35 alag-alag breeds shamil hain.

Dataset download karne ke liye, yeh code snippet use kijiye:

```python
!wget https://www.robots.ox.ac.uk/~vgg/data/pets/data/images.tar.gz
!tar xfz images.tar.gz
!rm images.tar.gz
```

## Notebook shuru karna

Lab shuru karne ke liye [OxfordPets.ipynb](../../../../../../lessons/4-ComputerVision/08-TransferLearning/lab/OxfordPets.ipynb) kholiye.

## Key Takeaway

Transfer learning aur pre-trained networks humein real-world image classification problems ko relatively aasaani se solve karne dete hain. Lekin, pre-trained networks similar type ki images par behtar kaam karte hain, aur agar hum bahut alag type ki images (jaise medical images) ko classify karna shuru karte hain, toh humein shayad bahut kharab results milenge.

---

<!-- HINGLISH NOTE START -->
**Note**:
Yeh document Hindi translation ko Hinglish (Roman script) mein convert karke banaya gaya hai, taaki padhna aur samajhna aasaan ho.
Isme kuch galtiyan ya anuvaad ki kamiyan ho sakti hain. Sabse sahi jaankari ke liye original English document ko hi authoritative source maanein.
<!-- HINGLISH NOTE END -->
