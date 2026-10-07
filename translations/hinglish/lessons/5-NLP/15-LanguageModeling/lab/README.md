# Skip-Gram Model ki Training

[AI for Beginners Curriculum](https://github.com/microsoft/ai-for-beginners) se Lab Assignment.

## Task

Is lab mein, hum aapko challenge dete hain ki Skip-Gram technique use karke Word2Vec model ko train karein. Embeddings ke saath ek network train karein jo $N$-token-wide skip-gram window mein neighboring words ko predict kar sake. Aap [is lesson ka code](../../../../../../lessons/5-NLP/15-LanguageModeling/CBoW-TF.ipynb) use kar sakte hain aur ise thoda modify kar sakte hain.

## Dataset

Aap koi bhi book use kar sakte hain. [Project Gutenberg](https://www.gutenberg.org/) par aapko bahut saare free texts mil sakte hain. Jaise, yahan Lewis Carroll ki likhi hui [Alice's Adventures in Wonderland](https://www.gutenberg.org/files/11/11-0.txt) ka direct link hai. Ya, aap Shakespeare ke plays use kar sakte hain, jinhe aap neeche diye gaye code se le sakte hain:

```python
path_to_file = tf.keras.utils.get_file(
   'shakespeare.txt', 
   'https://storage.googleapis.com/download.tensorflow.org/data/shakespeare.txt')
text = open(path_to_file, 'rb').read().decode(encoding='utf-8')
```

## Explore karein!

Agar aapke paas time hai aur aap topic mein gehraai se jaana chahte hain, toh in cheezon ko explore karne ki koshish karein:

* Embedding size results ko kaise affect karta hai?
* Alag-alag text styles result ko kaise affect karte hain?
* Kuch bahut alag types ke words aur unke synonyms lein, unke vector representations nikaalein, PCA use karke dimensions ko 2 tak kam karein, aur unhe 2D space mein plot karein. Kya aapko koi pattern dikhta hai?

---

<!-- HINGLISH NOTE START -->
**Note**:
Yeh document Hindi translation ko Hinglish (Roman script) mein convert karke banaya gaya hai, taaki padhna aur samajhna aasaan ho.
Isme kuch galtiyan ya anuvaad ki kamiyan ho sakti hain. Sabse sahi jaankari ke liye original English document ko hi authoritative source maanein.
<!-- HINGLISH NOTE END -->
