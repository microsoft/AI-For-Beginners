# Modellazione del Linguaggio

Gli embedding semantici, come Word2Vec e GloVe, rappresentano in realtà un primo passo verso la **modellazione del linguaggio** - la creazione di modelli che in qualche modo *comprendono* (o *rappresentano*) la natura del linguaggio.

## [Quiz pre-lezione](https://ff-quizzes.netlify.app/en/ai/quiz/29)

L'idea principale della modellazione del linguaggio è addestrare i modelli su dataset non etichettati in modo non supervisionato. Questo è importante perché abbiamo a disposizione enormi quantità di testo non etichettato, mentre la quantità di testo etichettato sarà sempre limitata dallo sforzo necessario per etichettarlo. Molto spesso, possiamo costruire modelli di linguaggio che siano in grado di **predire parole mancanti** nel testo, poiché è facile oscurare una parola casuale nel testo e usarla come campione di addestramento.

## Addestramento degli Embedding

Nei nostri esempi precedenti, abbiamo utilizzato embedding semantici pre-addestrati, ma è interessante vedere come questi embedding possano essere addestrati. Esistono diverse idee che possono essere utilizzate:

* **Modellazione del linguaggio con N-Gram**, in cui si predice un token osservando i N token precedenti (N-gram).
* **Continuous Bag-of-Words** (CBoW), in cui si predice il token centrale $W_0$ in una sequenza di token $W_{-N}$, ..., $W_N$.
* **Skip-gram**, in cui si predice un insieme di token vicini {$W_{-N},\dots, W_{-1}, W_1,\dots, W_N$} a partire dal token centrale $W_0$.

![immagine tratta da un articolo sulla conversione di parole in vettori](../../../../../translated_images/it/example-algorithms-for-converting-words-to-vectors.fbe9207a726922f6.webp)

> Immagine tratta da [questo articolo](https://arxiv.org/pdf/1301.3781.pdf)

## ✍️ Esempi di Notebook: Addestramento del modello CBoW

Continua il tuo apprendimento con i seguenti notebook:

* [Addestramento di CBoW Word2Vec con TensorFlow](CBoW-TF.ipynb)
* [Addestramento di CBoW Word2Vec con PyTorch](CBoW-PyTorch.ipynb)

## Conclusione

Nella lezione precedente abbiamo visto che gli embedding delle parole funzionano come per magia! Ora sappiamo che addestrare embedding delle parole non è un compito molto complesso, e dovremmo essere in grado di addestrare i nostri embedding per testi specifici di dominio, se necessario.

## [Quiz post-lezione](https://ff-quizzes.netlify.app/en/ai/quiz/30)

## Revisione e Studio Autonomo

* [Tutorial ufficiale di PyTorch sulla Modellazione del Linguaggio](https://pytorch.org/tutorials/beginner/nlp/word_embeddings_tutorial.html).
* [Tutorial ufficiale di TensorFlow sull'addestramento del modello Word2Vec](https://www.TensorFlow.org/tutorials/text/word2vec).
* L'utilizzo del framework **gensim** per addestrare gli embedding più comunemente usati in poche righe di codice è descritto [in questa documentazione](https://pytorch.org/tutorials/beginner/nlp/word_embeddings_tutorial.html).

## 🚀 [Compito: Addestra il Modello Skip-Gram](lab/README.md)

Nel laboratorio, ti sfidiamo a modificare il codice di questa lezione per addestrare un modello skip-gram invece di CBoW. [Leggi i dettagli](lab/README.md)

---

