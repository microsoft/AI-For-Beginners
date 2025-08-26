<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "e40b47ac3fd48f71304ede1474e66293",
  "translation_date": "2025-08-26T06:56:09+00:00",
  "source_file": "lessons/5-NLP/14-Embeddings/README.md",
  "language_code": "it"
}
-->
# Incorporazioni

## [Quiz pre-lezione](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/114)

Quando si addestrano classificatori basati su BoW o TF/IDF, lavoravamo su vettori sparsi ad alta dimensionalità con lunghezza `vocab_size`, convertendo esplicitamente da vettori di rappresentazione posizionale a bassa dimensionalità a rappresentazioni one-hot sparse. Tuttavia, questa rappresentazione one-hot non è efficiente in termini di memoria. Inoltre, ogni parola viene trattata in modo indipendente dalle altre, cioè i vettori one-hot codificati non esprimono alcuna somiglianza semantica tra le parole.

L'idea delle **incorporazioni** è rappresentare le parole con vettori densi a bassa dimensionalità, che in qualche modo riflettano il significato semantico di una parola. Più avanti discuteremo come costruire incorporazioni di parole significative, ma per ora pensiamo alle incorporazioni come un modo per ridurre la dimensionalità di un vettore di parole.

Quindi, il livello di incorporazione prenderebbe una parola come input e produrrebbe un vettore di output di dimensione specificata `embedding_size`. In un certo senso, è molto simile a un livello `Linear`, ma invece di prendere un vettore one-hot codificato, sarà in grado di prendere un numero di parola come input, permettendoci di evitare di creare grandi vettori one-hot codificati.

Utilizzando un livello di incorporazione come primo livello nella nostra rete di classificazione, possiamo passare da un modello bag-of-words a un modello **embedding bag**, dove prima convertiamo ogni parola nel nostro testo nella corrispondente incorporazione, e poi calcoliamo una funzione aggregata su tutte queste incorporazioni, come `sum`, `average` o `max`.

![Immagine che mostra un classificatore con incorporazioni per cinque parole in sequenza.](../../../../../translated_images/embedding-classifier-example.b77f021a7ee67eeec8e68bfe11636c5b97d6eaa067515a129bfb1d0034b1ac5b.it.png)

> Immagine dell'autore

## ✍️ Esercizi: Incorporazioni

Continua il tuo apprendimento nei seguenti notebook:
* [Incorporazioni con PyTorch](../../../../../lessons/5-NLP/14-Embeddings/EmbeddingsPyTorch.ipynb)
* [Incorporazioni con TensorFlow](../../../../../lessons/5-NLP/14-Embeddings/EmbeddingsTF.ipynb)

## Incorporazioni Semantiche: Word2Vec

Mentre il livello di incorporazione ha imparato a mappare le parole in rappresentazioni vettoriali, questa rappresentazione non aveva necessariamente un significato semantico rilevante. Sarebbe utile imparare una rappresentazione vettoriale tale che parole simili o sinonimi corrispondano a vettori vicini tra loro in termini di una certa distanza vettoriale (ad esempio, distanza euclidea).

Per fare ciò, dobbiamo pre-addestrare il nostro modello di incorporazione su una grande collezione di testi in un modo specifico. Un metodo per addestrare incorporazioni semantiche è chiamato [Word2Vec](https://en.wikipedia.org/wiki/Word2vec). Si basa su due principali architetture utilizzate per produrre una rappresentazione distribuita delle parole:

 - **Continuous bag-of-words** (CBoW) — in questa architettura, addestriamo il modello a prevedere una parola dal contesto circostante. Dato l'ngram $(W_{-2},W_{-1},W_0,W_1,W_2)$, l'obiettivo del modello è prevedere $W_0$ da $(W_{-2},W_{-1},W_1,W_2)$.
 - **Continuous skip-gram** è l'opposto del CBoW. Il modello utilizza la finestra di parole di contesto circostanti per prevedere la parola corrente.

CBoW è più veloce, mentre skip-gram è più lento, ma rappresenta meglio le parole meno frequenti.

![Immagine che mostra gli algoritmi CBoW e Skip-Gram per convertire parole in vettori.](../../../../../translated_images/example-algorithms-for-converting-words-to-vectors.fbe9207a726922f6f0f5de66427e8a6eda63809356114e28fb1fa5f4a83ebda7.it.png)

> Immagine tratta da [questo articolo](https://arxiv.org/pdf/1301.3781.pdf)

Le incorporazioni pre-addestrate di Word2Vec (così come altri modelli simili, come GloVe) possono anche essere utilizzate al posto del livello di incorporazione nelle reti neurali. Tuttavia, dobbiamo gestire i vocabolari, poiché il vocabolario utilizzato per pre-addestrare Word2Vec/GloVe probabilmente differisce dal vocabolario nel nostro corpus di testo. Dai un'occhiata ai notebook sopra per vedere come risolvere questo problema.

## Incorporazioni Contestuali

Una limitazione chiave delle rappresentazioni tradizionali di incorporazioni pre-addestrate come Word2Vec è il problema della disambiguazione del significato delle parole. Sebbene le incorporazioni pre-addestrate possano catturare parte del significato delle parole nel contesto, ogni possibile significato di una parola è codificato nella stessa incorporazione. Questo può causare problemi nei modelli a valle, poiché molte parole, come la parola 'play', hanno significati diversi a seconda del contesto in cui vengono utilizzate.

Ad esempio, la parola 'play' in queste due frasi ha significati piuttosto diversi:

- Sono andato a vedere una **commedia** a teatro.
- John vuole **giocare** con i suoi amici.

Le incorporazioni pre-addestrate sopra rappresentano entrambi i significati della parola 'play' nella stessa incorporazione. Per superare questa limitazione, dobbiamo costruire incorporazioni basate sul **modello linguistico**, che è addestrato su un ampio corpus di testi e *sa* come le parole possono essere messe insieme in diversi contesti. Discutere le incorporazioni contestuali è fuori dal campo di questa lezione, ma ne parleremo quando affronteremo i modelli linguistici più avanti nel corso.

## Conclusione

In questa lezione, hai scoperto come costruire e utilizzare i livelli di incorporazione in TensorFlow e PyTorch per riflettere meglio i significati semantici delle parole.

## 🚀 Sfida

Word2Vec è stato utilizzato per alcune applicazioni interessanti, tra cui la generazione di testi poetici e di canzoni. Dai un'occhiata a [questo articolo](https://www.politetype.com/blog/word2vec-color-poems) che spiega come l'autore ha utilizzato Word2Vec per generare poesie. Guarda anche [questo video di Dan Shiffmann](https://www.youtube.com/watch?v=LSS_bos_TPI&ab_channel=TheCodingTrain) per scoprire un'altra spiegazione di questa tecnica. Poi prova ad applicare queste tecniche al tuo corpus di testo, magari preso da Kaggle.

## [Quiz post-lezione](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/214)

## Revisione e Studio Autonomo

Leggi questo articolo su Word2Vec: [Efficient Estimation of Word Representations in Vector Space](https://arxiv.org/pdf/1301.3781.pdf)

## [Compito: Notebook](assignment.md)

**Disclaimer**:  
Questo documento è stato tradotto utilizzando il servizio di traduzione automatica [Co-op Translator](https://github.com/Azure/co-op-translator). Sebbene ci impegniamo per garantire l'accuratezza, si prega di notare che le traduzioni automatiche potrebbero contenere errori o imprecisioni. Il documento originale nella sua lingua nativa dovrebbe essere considerato la fonte autorevole. Per informazioni critiche, si raccomanda una traduzione professionale effettuata da un traduttore umano. Non siamo responsabili per eventuali fraintendimenti o interpretazioni errate derivanti dall'uso di questa traduzione.