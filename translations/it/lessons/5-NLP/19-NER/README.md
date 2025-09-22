<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "bd10f434e444bce61b7f97eeb1ff6a55",
  "translation_date": "2025-08-26T06:58:16+00:00",
  "source_file": "lessons/5-NLP/19-NER/README.md",
  "language_code": "it"
}
-->
# Riconoscimento delle Entità Nominate

Fino ad ora, ci siamo concentrati principalmente su un compito di elaborazione del linguaggio naturale (NLP) - la classificazione. Tuttavia, ci sono anche altri compiti NLP che possono essere affrontati con le reti neurali. Uno di questi compiti è il **[Riconoscimento delle Entità Nominate](https://wikipedia.org/wiki/Named-entity_recognition)** (NER), che si occupa di riconoscere entità specifiche all'interno di un testo, come luoghi, nomi di persone, intervalli di date e orari, formule chimiche e così via.

## [Quiz pre-lezione](https://ff-quizzes.netlify.app/en/ai/quiz/37)

## Esempio di utilizzo del NER

Supponiamo che tu voglia sviluppare un chatbot di linguaggio naturale, simile ad Amazon Alexa o Google Assistant. Il modo in cui funzionano i chatbot intelligenti è *comprendere* ciò che l'utente desidera facendo una classificazione del testo sulla frase di input. Il risultato di questa classificazione è il cosiddetto **intent**, che determina cosa dovrebbe fare il chatbot.

<img alt="Bot NER" src="images/bot-ner.png" width="50%"/>

> Immagine dell'autore

Tuttavia, un utente potrebbe fornire alcuni parametri come parte della frase. Ad esempio, quando chiede informazioni sul meteo, potrebbe specificare una località o una data. Un bot dovrebbe essere in grado di comprendere queste entità e riempire di conseguenza gli spazi dei parametri prima di eseguire l'azione. Ed è proprio qui che entra in gioco il NER.

> ✅ Un altro esempio potrebbe essere [l'analisi di articoli scientifici medici](https://soshnikov.com/science/analyzing-medical-papers-with-azure-and-text-analytics-for-health/). Una delle principali cose da cercare sono termini medici specifici, come malattie e sostanze mediche. Mentre un piccolo numero di malattie può probabilmente essere estratto utilizzando una ricerca per sottostringhe, entità più complesse, come composti chimici e nomi di farmaci, richiedono un approccio più sofisticato.

## NER come classificazione dei token

I modelli NER sono essenzialmente **modelli di classificazione dei token**, perché per ciascuno dei token di input dobbiamo decidere se appartiene a un'entità o meno, e se sì - a quale classe di entità.

Consideriamo il seguente titolo di un articolo:

**Rigurgito della valvola tricuspide** e **carbonato di litio** **tossicità** in un neonato.

Le entità qui sono:

* Rigurgito della valvola tricuspide è una malattia (`DIS`)
* Carbonato di litio è una sostanza chimica (`CHEM`)
* Tossicità è anch'essa una malattia (`DIS`)

Nota che un'entità può estendersi su più token. E, come in questo caso, dobbiamo distinguere tra due entità consecutive. Pertanto, è comune utilizzare due classi per ciascuna entità - una che specifica il primo token dell'entità (spesso si utilizza il prefisso `B-`, per **b**eginning), e un'altra per la continuazione di un'entità (`I-`, per **i**nner token). Usiamo anche `O` come classe per rappresentare tutti gli altri token (**o**ther). Questo tipo di etichettatura dei token è chiamato [etichettatura BIO](https://en.wikipedia.org/wiki/Inside%E2%80%93outside%E2%80%93beginning_(tagging)) (o IOB). Quando etichettato, il nostro titolo apparirà così:

Token | Tag
------|-----
Rigurgito | B-DIS
della | I-DIS
valvola | I-DIS
tricuspide | I-DIS
e | O
carbonato | B-CHEM
di | I-CHEM
litio | I-CHEM
tossicità | B-DIS
in | O
un | O
neonato | O
. | O

Poiché dobbiamo costruire una corrispondenza uno-a-uno tra token e classi, possiamo addestrare un modello neurale **many-to-many** come mostrato in questa immagine:

![Immagine che mostra i modelli comuni di reti neurali ricorrenti.](../../../../../translated_images/unreasonable-effectiveness-of-rnn.541ead816778f42dce6c42d8a56c184729aa2378d059b851be4ce12b993033df.it.jpg)

> *Immagine tratta da [questo post sul blog](http://karpathy.github.io/2015/05/21/rnn-effectiveness/) di [Andrej Karpathy](http://karpathy.github.io/). I modelli di classificazione dei token NER corrispondono all'architettura di rete più a destra in questa immagine.*

## Addestramento dei modelli NER

Poiché un modello NER è essenzialmente un modello di classificazione dei token, possiamo utilizzare le RNN che già conosciamo per questo compito. In questo caso, ogni blocco della rete ricorrente restituirà l'ID del token. Il seguente notebook di esempio mostra come addestrare un LSTM per la classificazione dei token.

## ✍️ Notebook di esempio: NER

Continua il tuo apprendimento con il seguente notebook:

* [NER con TensorFlow](../../../../../lessons/5-NLP/19-NER/NER-TF.ipynb)

## Conclusione

Un modello NER è un **modello di classificazione dei token**, il che significa che può essere utilizzato per eseguire la classificazione dei token. Questo è un compito molto comune nell'NLP, utile per riconoscere entità specifiche all'interno di un testo, inclusi luoghi, nomi, date e altro.

## 🚀 Sfida

Completa l'esercizio collegato qui sotto per addestrare un modello di riconoscimento delle entità nominate per termini medici, quindi provalo su un dataset diverso.

## [Quiz post-lezione](https://ff-quizzes.netlify.app/en/ai/quiz/38)

## Revisione e studio autonomo

Leggi il blog [The Unreasonable Effectiveness of Recurrent Neural Networks](http://karpathy.github.io/2015/05/21/rnn-effectiveness/) e segui la sezione di letture aggiuntive in quell'articolo per approfondire le tue conoscenze.

## [Esercizio](lab/README.md)

Nell'esercizio di questa lezione, dovrai addestrare un modello di riconoscimento delle entità mediche. Puoi iniziare con l'addestramento di un modello LSTM come descritto in questa lezione, e poi passare all'utilizzo del modello transformer BERT. Leggi [le istruzioni](lab/README.md) per ottenere tutti i dettagli.

**Disclaimer**:  
Questo documento è stato tradotto utilizzando il servizio di traduzione automatica [Co-op Translator](https://github.com/Azure/co-op-translator). Sebbene ci impegniamo per garantire l'accuratezza, si prega di notare che le traduzioni automatiche possono contenere errori o imprecisioni. Il documento originale nella sua lingua nativa dovrebbe essere considerato la fonte autorevole. Per informazioni critiche, si raccomanda una traduzione professionale effettuata da un traduttore umano. Non siamo responsabili per eventuali fraintendimenti o interpretazioni errate derivanti dall'uso di questa traduzione.