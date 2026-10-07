# Perceptron ke saath Multi-Class Classification

[AI for Beginners Curriculum](https://github.com/microsoft/ai-for-beginners) se Lab Assignment.

## Task

Is lesson mein develop kiye gaye code ka use karke, jo MNIST handwritten digits ki binary classification ke liye hai, ek multi-class classifier banaiye jo kisi bhi digit ko recognize kar sake. Train aur test datasets par classification accuracy calculate kijiye, aur confusion matrix print kijiye.

## Hints

1. Har digit ke liye, "yeh digit vs baaki sabhi digits" ki binary classification ke liye ek dataset banaiye.
1. Binary classification ke liye 10 alag perceptrons train kijiye (har digit ke liye ek).
1. Ek function define kijiye jo input digit ko classify karega.

> **Hint**: Agar hum sabhi 10 perceptrons ke weights ko ek matrix mein combine kar dein, toh hum ek hi matrix multiplication se input digits par sabhi 10 perceptrons apply kar sakte hain. Sabse probable digit ko output par `argmax` operation apply karke aasaani se paaya ja sakta hai.

## Starting Notebook

Lab shuru karne ke liye [PerceptronMultiClass.ipynb](PerceptronMultiClass.ipynb) kholiye.

---

<!-- HINGLISH NOTE START -->
**Note**:
Yeh document Hindi translation ko Hinglish (Roman script) mein convert karke banaya gaya hai, taaki padhna aur samajhna aasaan ho.
Isme kuch galtiyan ya anuvaad ki kamiyan ho sakti hain. Sabse sahi jaankari ke liye original English document ko hi authoritative source maanein.
<!-- HINGLISH NOTE END -->
