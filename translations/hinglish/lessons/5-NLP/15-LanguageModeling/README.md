# Language Modeling

Semantic embeddings, jaise Word2Vec aur GloVe, asal mein **language modeling** ki taraf pehla kadam hain - aise models banana jo kisi tarah language ki nature ko *samajhte* (ya *represent karte*) hain.

## [Pre-lecture quiz](https://ff-quizzes.netlify.app/en/ai/quiz/29)

Language modeling ka main idea yeh hai ki unhe unlabeled datasets par unsupervised tareeke se train kiya jaye. Yeh important hai kyunki humare paas unlabeled text badi quantity mein available hai, jabki labeled text ki quantity hamesha limited hogi kyunki labeling mein time aur effort lagta hai. Aksar, hum aise language models bana sakte hain jo **missing words predict** kar sakein, kyunki text mein ek random word ko mask karna aur use training sample ke roop mein use karna aasaan hai.

## Embeddings ki Training

Pichhle examples mein, humne pre-trained semantic embeddings use kiye the, lekin yeh dekhna dilchasp hai ki in embeddings ko kaise train kiya ja sakta hai. Iske liye kai possible ideas hain:

* **N-Gram** language modeling, jisme hum N pichhle tokens dekhkar ek token predict karte hain (N-gram).
* **Continuous Bag-of-Words** (CBoW), jisme hum token sequence $W_{-N}$, ..., $W_N$ mein beech ka token $W_0$ predict karte hain.
* **Skip-gram**, jisme hum beech ke token $W_0$ se neighboring tokens {$W_{-N},\dots, W_{-1}, W_1,\dots, W_N$} ka set predict karte hain.

![Words ko vectors mein convert karne ke algorithms ke paper se image](../../../../../translated_images/hi/example-algorithms-for-converting-words-to-vectors.fbe9207a726922f6.webp)

> Image [is paper](https://arxiv.org/pdf/1301.3781.pdf) se

## ✍️ Example Notebooks: CBoW Model ko Train karna

Neeche diye gaye notebooks mein apni learning jaari rakhiye:

* [TensorFlow ke saath CBoW Word2Vec ki Training](CBoW-TF.ipynb)
* [PyTorch ke saath CBoW Word2Vec ki Training](CBoW-PyTorch.ipynb)

## Conclusion

Pichhle lesson mein humne dekha ki word embeddings jaadu ki tarah kaam karte hain! Ab hum jaante hain ki word embeddings ki training koi bahut complex task nahi hai, aur agar zaroorat ho toh hum domain-specific text ke liye apne khud ke word embeddings train kar sakte hain.

## [Post-lecture quiz](https://ff-quizzes.netlify.app/en/ai/quiz/30)

## Review & Self Study

* [PyTorch par language modeling ke liye official tutorial](https://pytorch.org/tutorials/beginner/nlp/word_embeddings_tutorial.html).
* [Word2Vec model ki training par TensorFlow ka official tutorial](https://www.TensorFlow.org/tutorials/text/word2vec).
* **gensim** framework use karke kuch lines ke code mein sabse common embeddings ko train karne ka description [is documentation mein](https://pytorch.org/tutorials/beginner/nlp/word_embeddings_tutorial.html) diya gaya hai.

## 🚀 [Assignment: Skip-Gram Model ki Training](lab/README.md)

Lab mein, hum aapko challenge dete hain ki is lesson ke code ko modify karke skip-gram model train kijiye. [Details padhiye](lab/README.md)

---

