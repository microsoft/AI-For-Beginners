# Jazykové modelovanie

Sémantické vektory, ako Word2Vec a GloVe, sú v skutočnosti prvým krokom k **jazykovému modelovaniu** – vytváraniu modelov, ktoré nejako *rozumejú* (alebo *reprezentujú*) podstatu jazyka.

## [Kvíz pred prednáškou](https://ff-quizzes.netlify.app/en/ai/quiz/29)

Hlavnou myšlienkou jazykového modelovania je ich trénovanie na neoznačených dátach v nesupervidovanom režime. To je dôležité, pretože máme k dispozícii obrovské množstvo neoznačeného textu, zatiaľ čo množstvo označeného textu je vždy obmedzené úsilím, ktoré môžeme venovať jeho označovaniu. Najčastejšie môžeme vytvoriť jazykové modely, ktoré dokážu **predpovedať chýbajúce slová** v texte, pretože je jednoduché náhodne vynechať slovo v texte a použiť ho ako tréningový vzor.

## Trénovanie vektorov

V našich predchádzajúcich príkladoch sme používali predtrénované sémantické vektory, ale je zaujímavé vidieť, ako sa tieto vektory dajú trénovať. Existuje niekoľko možných prístupov, ktoré sa dajú použiť:

* **Jazykové modelovanie pomocou N-Gramov**, kde predpovedáme token na základe N predchádzajúcich tokenov (N-gram).
* **Continuous Bag-of-Words** (CBoW), kde predpovedáme stredný token $W_0$ v sekvencii tokenov $W_{-N}$, ..., $W_N$.
* **Skip-gram**, kde predpovedáme množinu susedných tokenov {$W_{-N},\dots, W_{-1}, W_1,\dots, W_N$} zo stredného tokenu $W_0$.

![obrázok z článku o konverzii slov na vektory](../../../../../translated_images/sk/example-algorithms-for-converting-words-to-vectors.fbe9207a726922f6.webp)

> Obrázok z [tohto článku](https://arxiv.org/pdf/1301.3781.pdf)

## ✍️ Príkladové notebooky: Trénovanie CBoW modelu

Pokračujte vo svojom učení v nasledujúcich notebookoch:

* [Trénovanie CBoW Word2Vec pomocou TensorFlow](CBoW-TF.ipynb)
* [Trénovanie CBoW Word2Vec pomocou PyTorch](CBoW-PyTorch.ipynb)

## Záver

V predchádzajúcej lekcii sme videli, že vektory slov fungujú ako kúzlo! Teraz vieme, že trénovanie vektorov slov nie je veľmi zložitá úloha, a mali by sme byť schopní trénovať vlastné vektory slov pre texty špecifické pre danú oblasť, ak to bude potrebné.

## [Kvíz po prednáške](https://ff-quizzes.netlify.app/en/ai/quiz/30)

## Prehľad a samostatné štúdium

* [Oficiálny PyTorch tutoriál o jazykovom modelovaní](https://pytorch.org/tutorials/beginner/nlp/word_embeddings_tutorial.html).
* [Oficiálny TensorFlow tutoriál o trénovaní Word2Vec modelu](https://www.TensorFlow.org/tutorials/text/word2vec).
* Použitie frameworku **gensim** na trénovanie najbežnejšie používaných vektorov v niekoľkých riadkoch kódu je popísané [v tejto dokumentácii](https://pytorch.org/tutorials/beginner/nlp/word_embeddings_tutorial.html).

## 🚀 [Úloha: Trénovanie Skip-Gram modelu](lab/README.md)

V laboratóriu vás vyzývame, aby ste upravili kód z tejto lekcie na trénovanie Skip-Gram modelu namiesto CBoW. [Prečítajte si podrobnosti](lab/README.md)

---

