# Modeliranje jezika

Semantičke ugrađene reprezentacije, poput Word2Vec i GloVe, zapravo su prvi korak prema **modeliranju jezika** - stvaranju modela koji na neki način *razumiju* (ili *predstavljaju*) prirodu jezika.

## [Kviz prije predavanja](https://ff-quizzes.netlify.app/en/ai/quiz/29)

Glavna ideja modeliranja jezika je treniranje na nepodacima bez oznaka na nesuperviziran način. Ovo je važno jer imamo ogromne količine teksta bez oznaka, dok je količina teksta s oznakama uvijek ograničena trudom koji možemo uložiti u označavanje. Najčešće možemo izgraditi modele jezika koji mogu **predvidjeti nedostajuće riječi** u tekstu, jer je lako sakriti nasumičnu riječ u tekstu i koristiti je kao uzorak za treniranje.

## Treniranje ugrađenih reprezentacija

U našim prethodnim primjerima koristili smo unaprijed trenirane semantičke ugrađene reprezentacije, ali zanimljivo je vidjeti kako se te reprezentacije mogu trenirati. Postoji nekoliko mogućih ideja koje se mogu koristiti:

* **N-Gram** modeliranje jezika, gdje predviđamo token gledajući N prethodnih tokena (N-gram)
* **Kontinuirana vreća riječi** (CBoW), gdje predviđamo srednji token $W_0$ u nizu tokena $W_{-N}$, ..., $W_N$.
* **Skip-gram**, gdje predviđamo skup susjednih tokena {$W_{-N},\dots, W_{-1}, W_1,\dots, W_N$} iz srednjeg tokena $W_0$.

![slika iz rada o pretvaranju riječi u vektore](../../../../../translated_images/hr/example-algorithms-for-converting-words-to-vectors.fbe9207a726922f6.webp)

> Slika iz [ovog rada](https://arxiv.org/pdf/1301.3781.pdf)

## ✍️ Primjeri bilježnica: Treniranje CBoW modela

Nastavite učiti kroz sljedeće bilježnice:

* [Treniranje CBoW Word2Vec s TensorFlowom](CBoW-TF.ipynb)
* [Treniranje CBoW Word2Vec s PyTorchom](CBoW-PyTorch.ipynb)

## Zaključak

U prethodnoj lekciji vidjeli smo da ugrađene reprezentacije riječi djeluju kao čarolija! Sada znamo da treniranje ugrađenih reprezentacija riječi nije vrlo složen zadatak, i trebali bismo biti u mogućnosti trenirati vlastite ugrađene reprezentacije za tekst specifičan za određeno područje ako je potrebno.

## [Kviz nakon predavanja](https://ff-quizzes.netlify.app/en/ai/quiz/30)

## Pregled i samostalno učenje

* [Službeni PyTorch vodič o modeliranju jezika](https://pytorch.org/tutorials/beginner/nlp/word_embeddings_tutorial.html).
* [Službeni TensorFlow vodič o treniranju Word2Vec modela](https://www.TensorFlow.org/tutorials/text/word2vec).
* Korištenje okvira **gensim** za treniranje najčešće korištenih ugrađenih reprezentacija u nekoliko linija koda opisano je [u ovoj dokumentaciji](https://pytorch.org/tutorials/beginner/nlp/word_embeddings_tutorial.html).

## 🚀 [Zadatak: Trenirajte Skip-Gram model](lab/README.md)

U laboratorijskom zadatku izazivamo vas da izmijenite kod iz ove lekcije kako biste trenirali Skip-Gram model umjesto CBoW. [Pročitajte detalje](lab/README.md)

---

