# Jazykové modelování

Sémantické vektory, jako Word2Vec a GloVe, jsou ve skutečnosti prvním krokem k **jazykovému modelování** – vytváření modelů, které nějakým způsobem *rozumí* (nebo *reprezentují*) podstatu jazyka.

## [Kvíz před přednáškou](https://ff-quizzes.netlify.app/en/ai/quiz/29)

Hlavní myšlenkou jazykového modelování je jejich trénování na neoznačených datových sadách neřízeným způsobem. To je důležité, protože máme k dispozici obrovské množství neoznačeného textu, zatímco množství označeného textu bude vždy omezeno úsilím, které můžeme věnovat jeho označování. Nejčastěji můžeme vytvářet jazykové modely, které dokážou **předpovídat chybějící slova** v textu, protože je snadné náhodně zakrýt slovo v textu a použít ho jako trénovací vzorek.

## Trénování vektorů

V našich předchozích příkladech jsme používali předtrénované sémantické vektory, ale je zajímavé vidět, jak lze tyto vektory trénovat. Existuje několik možných přístupů, které lze použít:

* **Jazykové modelování pomocí N-Gramů**, kdy předpovídáme token na základě N předchozích tokenů (N-gram).
* **Continuous Bag-of-Words** (CBoW), kdy předpovídáme prostřední token $W_0$ v sekvenci tokenů $W_{-N}$, ..., $W_N$.
* **Skip-gram**, kde předpovídáme sadu sousedních tokenů {$W_{-N},\dots, W_{-1}, W_1,\dots, W_N$} na základě prostředního tokenu $W_0$.

![obrázek z článku o převodu slov na vektory](../../../../../translated_images/cs/example-algorithms-for-converting-words-to-vectors.fbe9207a726922f6.webp)

> Obrázek z [tohoto článku](https://arxiv.org/pdf/1301.3781.pdf)

## ✍️ Ukázkové notebooky: Trénování modelu CBoW

Pokračujte ve svém učení v následujících noteboocích:

* [Trénování CBoW Word2Vec pomocí TensorFlow](CBoW-TF.ipynb)
* [Trénování CBoW Word2Vec pomocí PyTorch](CBoW-PyTorch.ipynb)

## Závěr

V předchozí lekci jsme viděli, že vektory slov fungují jako kouzlo! Nyní víme, že trénování vektorů slov není příliš složitý úkol a měli bychom být schopni trénovat vlastní vektory slov pro texty specifické pro danou oblast, pokud to bude potřeba.

## [Kvíz po přednášce](https://ff-quizzes.netlify.app/en/ai/quiz/30)

## Přehled & Samostudium

* [Oficiální tutoriál PyTorch o jazykovém modelování](https://pytorch.org/tutorials/beginner/nlp/word_embeddings_tutorial.html).
* [Oficiální tutoriál TensorFlow o trénování modelu Word2Vec](https://www.TensorFlow.org/tutorials/text/word2vec).
* Použití frameworku **gensim** k trénování nejběžněji používaných vektorů v několika řádcích kódu je popsáno [v této dokumentaci](https://pytorch.org/tutorials/beginner/nlp/word_embeddings_tutorial.html).

## 🚀 [Úkol: Trénování modelu Skip-Gram](lab/README.md)

V laboratoři vás vyzýváme, abyste upravili kód z této lekce a trénovali model Skip-Gram místo CBoW. [Přečtěte si podrobnosti](lab/README.md)

---

