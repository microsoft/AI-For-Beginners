# Modelarea Limbajului

Încorporările semantice, precum Word2Vec și GloVe, reprezintă de fapt un prim pas către **modelarea limbajului** - crearea de modele care într-un fel *înțeleg* (sau *reprezintă*) natura limbajului.

## [Chestionar înainte de lecție](https://ff-quizzes.netlify.app/en/ai/quiz/29)

Ideea principală din spatele modelării limbajului este antrenarea acestora pe seturi de date neetichetate într-un mod nesupravegheat. Acest lucru este important deoarece avem la dispoziție cantități uriașe de text neetichetat, în timp ce cantitatea de text etichetat va fi întotdeauna limitată de efortul pe care îl putem depune pentru etichetare. Cel mai adesea, putem construi modele de limbaj care pot **prezice cuvintele lipsă** din text, deoarece este ușor să mascăm un cuvânt aleator din text și să-l folosim ca exemplu de antrenament.

## Antrenarea Încorporărilor

În exemplele anterioare, am folosit încorporări semantice pre-antrenate, dar este interesant să vedem cum pot fi antrenate aceste încorporări. Există mai multe idei posibile care pot fi utilizate:

* **Modelarea limbajului N-Gram**, când prezicem un token analizând N tokeni anteriori (N-gram).
* **Continuous Bag-of-Words** (CBoW), când prezicem tokenul din mijloc $W_0$ într-o secvență de tokeni $W_{-N}$, ..., $W_N$.
* **Skip-gram**, unde prezicem un set de tokeni vecini {$W_{-N},\dots, W_{-1}, W_1,\dots, W_N$} pornind de la tokenul din mijloc $W_0$.

![imagine dintr-un articol despre convertirea cuvintelor în vectori](../../../../../translated_images/ro/example-algorithms-for-converting-words-to-vectors.fbe9207a726922f6.webp)

> Imagine din [acest articol](https://arxiv.org/pdf/1301.3781.pdf)

## ✍️ Exemple de Notebook-uri: Antrenarea modelului CBoW

Continuă învățarea în următoarele notebook-uri:

* [Antrenarea CBoW Word2Vec cu TensorFlow](CBoW-TF.ipynb)
* [Antrenarea CBoW Word2Vec cu PyTorch](CBoW-PyTorch.ipynb)

## Concluzie

În lecția anterioară am văzut că încorporările de cuvinte funcționează ca prin magie! Acum știm că antrenarea încorporărilor de cuvinte nu este o sarcină foarte complexă și ar trebui să fim capabili să ne antrenăm propriile încorporări de cuvinte pentru texte specifice unui domeniu, dacă este necesar.

## [Chestionar după lecție](https://ff-quizzes.netlify.app/en/ai/quiz/30)

## Recapitulare & Studiu Individual

* [Tutorial oficial PyTorch despre Modelarea Limbajului](https://pytorch.org/tutorials/beginner/nlp/word_embeddings_tutorial.html).
* [Tutorial oficial TensorFlow despre antrenarea modelului Word2Vec](https://www.TensorFlow.org/tutorials/text/word2vec).
* Utilizarea framework-ului **gensim** pentru a antrena cele mai utilizate încorporări în câteva linii de cod este descrisă [în această documentație](https://pytorch.org/tutorials/beginner/nlp/word_embeddings_tutorial.html).

## 🚀 [Temă: Antrenează Modelul Skip-Gram](lab/README.md)

În laborator, te provocăm să modifici codul din această lecție pentru a antrena un model skip-gram în loc de CBoW. [Citește detaliile](lab/README.md)

---

