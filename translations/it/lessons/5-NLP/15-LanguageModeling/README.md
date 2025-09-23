<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "31b46ba1f3aa78578134d4829f88be53",
  "translation_date": "2025-08-26T06:57:46+00:00",
  "source_file": "lessons/5-NLP/15-LanguageModeling/README.md",
  "language_code": "it"
}
-->
# Modellazione del linguaggio

Gli embedding semantici, come Word2Vec e GloVe, rappresentano in realtà un primo passo verso la **modellazione del linguaggio** - la creazione di modelli che in qualche modo *comprendono* (o *rappresentano*) la natura del linguaggio.

## [Quiz pre-lezione](https://ff-quizzes.netlify.app/en/ai/quiz/29)

L'idea principale della modellazione del linguaggio è allenare i modelli su dataset non etichettati in modo non supervisionato. Questo è importante perché abbiamo a disposizione enormi quantità di testo non etichettato, mentre la quantità di testo etichettato sarà sempre limitata dall'impegno necessario per etichettarlo. Molto spesso, possiamo costruire modelli di linguaggio che possono **predire parole mancanti** nel testo, poiché è facile oscurare una parola casuale nel testo e usarla come campione di allenamento.

## Allenamento degli embedding

Nei nostri esempi precedenti, abbiamo utilizzato embedding semantici pre-addestrati, ma è interessante vedere come questi embedding possano essere allenati. Ci sono diverse idee che possono essere utilizzate:

* **Modellazione del linguaggio N-Gram**, in cui si predice un token osservando i N token precedenti (N-gram).
* **Continuous Bag-of-Words** (CBoW), in cui si predice il token centrale $W_0$ in una sequenza di token $W_{-N}$, ..., $W_N$.
* **Skip-gram**, dove si predice un insieme di token vicini {$W_{-N},\dots, W_{-1}, W_1,\dots, W_N$} a partire dal token centrale $W_0$.

![immagine tratta da un articolo sulla conversione di parole in vettori](../../../../../translated_images/example-algorithms-for-converting-words-to-vectors.fbe9207a726922f6f0f5de66427e8a6eda63809356114e28fb1fa5f4a83ebda7.it.png)

> Immagine tratta da [questo articolo](https://arxiv.org/pdf/1301.3781.pdf)

## ✍️ Notebook di esempio: Allenamento del modello CBoW

Continua il tuo apprendimento nei seguenti notebook:

* [Allenamento di CBoW Word2Vec con TensorFlow](../../../../../lessons/5-NLP/15-LanguageModeling/CBoW-TF.ipynb)
* [Allenamento di CBoW Word2Vec con PyTorch](../../../../../lessons/5-NLP/15-LanguageModeling/CBoW-PyTorch.ipynb)

## Conclusione

Nella lezione precedente abbiamo visto che gli embedding delle parole funzionano come per magia! Ora sappiamo che allenare gli embedding delle parole non è un compito molto complesso e dovremmo essere in grado di allenare i nostri embedding per testi specifici di dominio, se necessario.

## [Quiz post-lezione](https://ff-quizzes.netlify.app/en/ai/quiz/30)

## Revisione e studio autonomo

* [Tutorial ufficiale di PyTorch sulla modellazione del linguaggio](https://pytorch.org/tutorials/beginner/nlp/word_embeddings_tutorial.html).
* [Tutorial ufficiale di TensorFlow sull'allenamento del modello Word2Vec](https://www.TensorFlow.org/tutorials/text/word2vec).
* Utilizzare il framework **gensim** per allenare gli embedding più comunemente usati in poche righe di codice è descritto [in questa documentazione](https://pytorch.org/tutorials/beginner/nlp/word_embeddings_tutorial.html).

## 🚀 [Compito: Allenare il modello Skip-Gram](lab/README.md)

Nel laboratorio, ti sfidiamo a modificare il codice di questa lezione per allenare un modello Skip-Gram invece di CBoW. [Leggi i dettagli](lab/README.md)

**Disclaimer**:  
Questo documento è stato tradotto utilizzando il servizio di traduzione automatica [Co-op Translator](https://github.com/Azure/co-op-translator). Sebbene ci impegniamo per garantire l'accuratezza, si prega di notare che le traduzioni automatiche possono contenere errori o imprecisioni. Il documento originale nella sua lingua nativa dovrebbe essere considerato la fonte autorevole. Per informazioni critiche, si raccomanda una traduzione professionale effettuata da un traduttore umano. Non siamo responsabili per eventuali incomprensioni o interpretazioni errate derivanti dall'uso di questa traduzione.