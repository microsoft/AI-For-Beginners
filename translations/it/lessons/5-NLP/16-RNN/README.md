<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "58bf4adb210aab53e8f78c8082040e7c",
  "translation_date": "2025-08-26T06:55:35+00:00",
  "source_file": "lessons/5-NLP/16-RNN/README.md",
  "language_code": "it"
}
-->
# Reti Neurali Ricorrenti

## [Quiz pre-lezione](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/116)

Nelle sezioni precedenti, abbiamo utilizzato rappresentazioni semantiche ricche del testo e un semplice classificatore lineare sopra gli embeddings. Questa architettura cattura il significato aggregato delle parole in una frase, ma non tiene conto dell'**ordine** delle parole, poiché l'operazione di aggregazione sugli embeddings elimina questa informazione dal testo originale. Poiché questi modelli non sono in grado di modellare l'ordine delle parole, non possono risolvere compiti più complessi o ambigui come la generazione di testo o la risposta a domande.

Per catturare il significato di una sequenza di testo, dobbiamo utilizzare un'altra architettura di rete neurale, chiamata **rete neurale ricorrente**, o RNN. Nelle RNN, passiamo la nostra frase attraverso la rete un simbolo alla volta, e la rete produce uno **stato**, che poi passiamo nuovamente alla rete insieme al simbolo successivo.

![RNN](../../../../../translated_images/rnn.27f5c29c53d727b546ad3961637a267f0fe9ec5ab01f2a26a853c92fcefbb574.it.png)

> Immagine dell'autore

Data la sequenza di input di token X<sub>0</sub>,...,X<sub>n</sub>, l'RNN crea una sequenza di blocchi di rete neurale e allena questa sequenza end-to-end utilizzando la retropropagazione. Ogni blocco di rete prende come input una coppia (X<sub>i</sub>,S<sub>i</sub>) e produce S<sub>i+1</sub> come risultato. Lo stato finale S<sub>n</sub> (o l'output Y<sub>n</sub>) viene inviato a un classificatore lineare per produrre il risultato. Tutti i blocchi di rete condividono gli stessi pesi e vengono allenati end-to-end con un unico passaggio di retropropagazione.

Poiché i vettori di stato S<sub>0</sub>,...,S<sub>n</sub> vengono passati attraverso la rete, essa è in grado di apprendere le dipendenze sequenziali tra le parole. Ad esempio, quando la parola *non* appare da qualche parte nella sequenza, può imparare a negare determinati elementi all'interno del vettore di stato, risultando in una negazione.

> ✅ Poiché i pesi di tutti i blocchi RNN nell'immagine sopra sono condivisi, la stessa immagine può essere rappresentata come un unico blocco (a destra) con un ciclo di feedback ricorrente, che passa lo stato di output della rete nuovamente all'input.

## Anatomia di una cella RNN

Vediamo come è organizzata una semplice cella RNN. Accetta lo stato precedente S<sub>i-1</sub> e il simbolo corrente X<sub>i</sub> come input, e deve produrre lo stato di output S<sub>i</sub> (e, a volte, siamo anche interessati a un altro output Y<sub>i</sub>, come nel caso delle reti generative).

Una semplice cella RNN ha due matrici di peso al suo interno: una trasforma un simbolo di input (chiamiamola W) e un'altra trasforma uno stato di input (H). In questo caso, l'output della rete è calcolato come σ(W×X<sub>i</sub>+H×S<sub>i-1</sub>+b), dove σ è la funzione di attivazione e b è un bias aggiuntivo.

<img alt="Anatomia di una cella RNN" src="images/rnn-anatomy.png" width="50%"/>

> Immagine dell'autore

In molti casi, i token di input vengono passati attraverso il livello di embedding prima di entrare nell'RNN per ridurre la dimensionalità. In questo caso, se la dimensione dei vettori di input è *emb_size* e il vettore di stato è *hid_size*, la dimensione di W è *emb_size*×*hid_size* e la dimensione di H è *hid_size*×*hid_size*.

## Long Short Term Memory (LSTM)

Uno dei principali problemi delle RNN classiche è il cosiddetto problema dei **gradienti che svaniscono**. Poiché le RNN vengono allenate end-to-end in un unico passaggio di retropropagazione, hanno difficoltà a propagare l'errore ai primi strati della rete, e quindi la rete non riesce ad apprendere le relazioni tra token distanti. Uno dei modi per evitare questo problema è introdurre una **gestione esplicita dello stato** utilizzando i cosiddetti **gate**. Esistono due architetture ben note di questo tipo: **Long Short Term Memory** (LSTM) e **Gated Relay Unit** (GRU).

![Immagine che mostra un esempio di cella LSTM](../../../../../lessons/5-NLP/16-RNN/images/long-short-term-memory-cell.svg)

> Fonte immagine TBD

La rete LSTM è organizzata in modo simile all'RNN, ma ci sono due stati che vengono passati da uno strato all'altro: lo stato effettivo C e il vettore nascosto H. In ogni unità, il vettore nascosto H<sub>i</sub> viene concatenato con l'input X<sub>i</sub>, e insieme controllano cosa accade allo stato C tramite i **gate**. Ogni gate è una rete neurale con attivazione sigmoide (output nell'intervallo [0,1]), che può essere considerata come una maschera bitwise quando moltiplicata per il vettore di stato. I gate sono i seguenti (da sinistra a destra nell'immagine sopra):

* Il **forget gate** prende un vettore nascosto e determina quali componenti del vettore C dobbiamo dimenticare e quali passare.
* L'**input gate** prende alcune informazioni dai vettori di input e nascosti e le inserisce nello stato.
* L'**output gate** trasforma lo stato tramite un livello lineare con attivazione *tanh*, quindi seleziona alcune delle sue componenti utilizzando un vettore nascosto H<sub>i</sub> per produrre un nuovo stato C<sub>i+1</sub>.

Le componenti dello stato C possono essere considerate come flag che possono essere attivati o disattivati. Ad esempio, quando incontriamo un nome *Alice* nella sequenza, potremmo voler assumere che si riferisca a un personaggio femminile e attivare il flag nello stato che indica un sostantivo femminile nella frase. Quando successivamente incontriamo la frase *e Tom*, attiveremo il flag che indica un sostantivo plurale. Così, manipolando lo stato, possiamo teoricamente tenere traccia delle proprietà grammaticali delle parti della frase.

> ✅ Una risorsa eccellente per comprendere i dettagli interni delle LSTM è questo ottimo articolo [Understanding LSTM Networks](https://colah.github.io/posts/2015-08-Understanding-LSTMs/) di Christopher Olah.

## RNN Bidirezionali e Multistrato

Abbiamo discusso di reti ricorrenti che operano in una direzione, dall'inizio di una sequenza alla fine. Sembra naturale, poiché ricorda il modo in cui leggiamo e ascoltiamo il discorso. Tuttavia, poiché in molti casi pratici abbiamo accesso casuale alla sequenza di input, potrebbe avere senso eseguire il calcolo ricorrente in entrambe le direzioni. Tali reti sono chiamate **RNN bidirezionali**. Quando si lavora con una rete bidirezionale, avremo bisogno di due vettori di stato nascosto, uno per ciascuna direzione.

Una rete ricorrente, sia unidirezionale che bidirezionale, cattura determinati schemi all'interno di una sequenza e può memorizzarli in un vettore di stato o passarli all'output. Come con le reti convoluzionali, possiamo costruire un altro livello ricorrente sopra il primo per catturare schemi di livello superiore e costruire a partire dagli schemi di basso livello estratti dal primo livello. Questo ci porta al concetto di **RNN multistrato**, che consiste in due o più reti ricorrenti, dove l'output del livello precedente viene passato al livello successivo come input.

![Immagine che mostra un RNN LSTM multistrato](../../../../../translated_images/multi-layer-lstm.dd975e29bb2a59fe58b429db833932d734c81f211cad2783797a9608984acb8c.it.jpg)

*Immagine tratta da [questo fantastico post](https://towardsdatascience.com/from-a-lstm-cell-to-a-multilayer-lstm-network-with-pytorch-2899eb5696f3) di Fernando López*

## ✍️ Esercizi: Embeddings

Continua il tuo apprendimento nei seguenti notebook:

* [RNNs con PyTorch](../../../../../lessons/5-NLP/16-RNN/RNNPyTorch.ipynb)
* [RNNs con TensorFlow](../../../../../lessons/5-NLP/16-RNN/RNNTF.ipynb)

## Conclusione

In questa unità, abbiamo visto che le RNN possono essere utilizzate per la classificazione di sequenze, ma in realtà possono gestire molti altri compiti, come la generazione di testo, la traduzione automatica e altro. Considereremo questi compiti nell'unità successiva.

## 🚀 Sfida

Leggi alcune pubblicazioni sulle LSTM e considera le loro applicazioni:

- [Grid Long Short-Term Memory](https://arxiv.org/pdf/1507.01526v1.pdf)
- [Show, Attend and Tell: Neural Image Caption
Generation with Visual Attention](https://arxiv.org/pdf/1502.03044v2.pdf)

## [Quiz post-lezione](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/216)

## Revisione e Studio Autonomo

- [Understanding LSTM Networks](https://colah.github.io/posts/2015-08-Understanding-LSTMs/) di Christopher Olah.

## [Compito: Notebook](assignment.md)

**Disclaimer (Avvertenza)**:  
Questo documento è stato tradotto utilizzando il servizio di traduzione automatica [Co-op Translator](https://github.com/Azure/co-op-translator). Sebbene ci impegniamo per garantire l'accuratezza, si prega di tenere presente che le traduzioni automatiche possono contenere errori o imprecisioni. Il documento originale nella sua lingua nativa dovrebbe essere considerato la fonte autorevole. Per informazioni critiche, si raccomanda una traduzione professionale effettuata da un traduttore umano. Non siamo responsabili per eventuali incomprensioni o interpretazioni errate derivanti dall'uso di questa traduzione.