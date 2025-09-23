<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f07c85bbf05a1f67505da98f4ecc124c",
  "translation_date": "2025-08-26T07:01:04+00:00",
  "source_file": "lessons/4-ComputerVision/10-GANs/README.md",
  "language_code": "it"
}
-->
# Reti Generative Avversarie

Nella sezione precedente, abbiamo imparato a conoscere i **modelli generativi**: modelli in grado di generare nuove immagini simili a quelle presenti nel dataset di addestramento. Un esempio di modello generativo è il VAE.

## [Quiz pre-lezione](https://ff-quizzes.netlify.app/en/ai/quiz/19)

Tuttavia, se proviamo a generare qualcosa di veramente significativo, come un dipinto ad alta risoluzione, utilizzando un VAE, noteremo che l'addestramento non converge bene. Per questo caso d'uso, dobbiamo imparare un'altra architettura specificamente progettata per i modelli generativi: le **Reti Generative Avversarie**, o GAN.

L'idea principale di una GAN è avere due reti neurali che vengono addestrate l'una contro l'altra:

<img src="images/gan_architecture.png" width="70%"/>

> Immagine di [Dmitry Soshnikov](http://soshnikov.com)

> ✅ Un po' di vocabolario:
> * **Generatore**: una rete che prende un vettore casuale e produce un'immagine come risultato.
> * **Discriminatore**: una rete che prende un'immagine e deve determinare se è un'immagine reale (proveniente dal dataset di addestramento) o se è stata generata dal generatore. Essenzialmente, è un classificatore di immagini.

### Discriminatore

L'architettura del discriminatore non differisce da quella di una normale rete di classificazione delle immagini. Nel caso più semplice, può essere un classificatore completamente connesso, ma molto probabilmente sarà una [rete convoluzionale](../07-ConvNets/README.md).

> ✅ Una GAN basata su reti convoluzionali è chiamata [DCGAN](https://arxiv.org/pdf/1511.06434.pdf)

Un discriminatore CNN è composto dai seguenti strati: diverse convoluzioni+pooling (con dimensioni spaziali decrescenti) e uno o più strati completamente connessi per ottenere un "feature vector", seguito da un classificatore binario finale.

> ✅ Il 'pooling' in questo contesto è una tecnica che riduce la dimensione dell'immagine. "I livelli di pooling riducono le dimensioni dei dati combinando le uscite di cluster di neuroni in un livello in un singolo neurone nel livello successivo." - [fonte](https://wikipedia.org/wiki/Convolutional_neural_network#Pooling_layers)

### Generatore

Un generatore è leggermente più complesso. Può essere considerato come un discriminatore al contrario. Partendo da un vettore latente (al posto di un feature vector), ha uno strato completamente connesso per convertirlo nella dimensione/forma richiesta, seguito da deconvoluzioni+upscaling. Questo è simile alla parte di *decoder* di un [autoencoder](../09-Autoencoders/README.md).

> ✅ Poiché il livello di convoluzione è implementato come un filtro lineare che attraversa l'immagine, la deconvoluzione è essenzialmente simile alla convoluzione e può essere implementata utilizzando la stessa logica di livello.

<img src="images/gan_arch_detail.png" width="70%"/>

> Immagine di [Dmitry Soshnikov](http://soshnikov.com)

### Addestramento della GAN

Le GAN sono chiamate **avversarie** perché c'è una competizione costante tra il generatore e il discriminatore. Durante questa competizione, sia il generatore che il discriminatore migliorano, e la rete impara a produrre immagini sempre migliori.

L'addestramento avviene in due fasi:

* **Addestramento del discriminatore**. Questo compito è piuttosto semplice: generiamo un batch di immagini con il generatore, etichettandole come 0 (immagini false), e prendiamo un batch di immagini dal dataset di input (etichettate come 1, immagini reali). Otteniamo una *discriminator loss* e applichiamo il backpropagation.
* **Addestramento del generatore**. Questo è un po' più complesso, perché non conosciamo direttamente l'output atteso per il generatore. Prendiamo l'intera rete GAN composta da un generatore seguito da un discriminatore, la alimentiamo con vettori casuali e ci aspettiamo che il risultato sia 1 (corrispondente a immagini reali). Congeliamo quindi i parametri del discriminatore (non vogliamo che venga addestrato in questo passaggio) e applichiamo il backpropagation.

Durante questo processo, le perdite del generatore e del discriminatore non diminuiscono significativamente. Nella situazione ideale, dovrebbero oscillare, corrispondendo al miglioramento delle prestazioni di entrambe le reti.

## ✍️ Esercizi: GAN

* [Notebook GAN in TensorFlow/Keras](../../../../../lessons/4-ComputerVision/10-GANs/GANTF.ipynb)
* [Notebook GAN in PyTorch](../../../../../lessons/4-ComputerVision/10-GANs/GANPyTorch.ipynb)

### Problemi con l'addestramento delle GAN

Le GAN sono note per essere particolarmente difficili da addestrare. Ecco alcuni problemi:

* **Mode Collapse**. Con questo termine si intende che il generatore impara a produrre una sola immagine di successo che inganna il discriminatore, invece di una varietà di immagini diverse.
* **Sensibilità agli iperparametri**. Spesso si nota che una GAN non converge affatto, per poi improvvisamente convergere con una riduzione del tasso di apprendimento.
* Mantenere un **equilibrio** tra il generatore e il discriminatore. In molti casi, la perdita del discriminatore può scendere a zero relativamente in fretta, rendendo impossibile l'addestramento del generatore. Per superare questo problema, si possono provare tassi di apprendimento diversi per il generatore e il discriminatore, o saltare l'addestramento del discriminatore se la perdita è già troppo bassa.
* Addestramento per **alta risoluzione**. Riflettendo lo stesso problema degli autoencoder, questo problema si verifica perché ricostruire troppi livelli di rete convoluzionale porta ad artefatti. Questo problema viene tipicamente risolto con il cosiddetto **progressive growing**, in cui i primi livelli vengono addestrati su immagini a bassa risoluzione, e poi i livelli vengono "sbloccati" o aggiunti. Un'altra soluzione consiste nell'aggiungere connessioni extra tra i livelli e addestrare diverse risoluzioni contemporaneamente - vedi questo [articolo sulle Multi-Scale Gradient GANs](https://arxiv.org/abs/1903.06048) per i dettagli.

## Trasferimento di Stile

Le GAN sono un ottimo modo per generare immagini artistiche. Un'altra tecnica interessante è il cosiddetto **trasferimento di stile**, che prende un'immagine di **contenuto** e la ridisegna in uno stile diverso, applicando filtri da un'immagine di **stile**.

Il funzionamento è il seguente:
* Si parte da un'immagine casuale di rumore (o da un'immagine di contenuto, ma per semplicità è più facile partire da rumore casuale).
* L'obiettivo è creare un'immagine che sia vicina sia all'immagine di contenuto che a quella di stile. Questo viene determinato da due funzioni di perdita:
   - **Perdita di contenuto**, calcolata in base alle caratteristiche estratte dalla CNN a determinati livelli dall'immagine corrente e dall'immagine di contenuto.
   - **Perdita di stile**, calcolata tra l'immagine corrente e quella di stile in modo intelligente utilizzando le matrici di Gram (maggiori dettagli nel [notebook di esempio](../../../../../lessons/4-ComputerVision/10-GANs/StyleTransfer.ipynb)).
* Per rendere l'immagine più fluida e rimuovere il rumore, si introduce anche una **Perdita di variazione**, che calcola la distanza media tra pixel vicini.
* Il ciclo di ottimizzazione principale regola l'immagine corrente utilizzando la discesa del gradiente (o un altro algoritmo di ottimizzazione) per minimizzare la perdita totale, che è una somma ponderata di tutte e tre le perdite.

## ✍️ Esempio: [Trasferimento di Stile](../../../../../lessons/4-ComputerVision/10-GANs/StyleTransfer.ipynb)

## [Quiz post-lezione](https://ff-quizzes.netlify.app/en/ai/quiz/20)

## Conclusione

In questa lezione, hai imparato cosa sono le GAN e come addestrarle. Hai anche appreso le sfide specifiche che questo tipo di rete neurale può affrontare e alcune strategie per superarle.

## 🚀 Sfida

Esegui il [notebook sul Trasferimento di Stile](../../../../../lessons/4-ComputerVision/10-GANs/StyleTransfer.ipynb) utilizzando le tue immagini.

## Revisione e Studio Autonomo

Per approfondire, leggi di più sulle GAN in queste risorse:

* Marco Pasini, [10 lezioni che ho imparato addestrando GAN per un anno](https://towardsdatascience.com/10-lessons-i-learned-training-generative-adversarial-networks-gans-for-a-year-c9071159628)
* [StyleGAN](https://en.wikipedia.org/wiki/StyleGAN), un'architettura GAN *de facto* da considerare
* [Creare arte generativa usando GAN su Azure ML](https://soshnikov.com/scienceart/creating-generative-art-using-gan-on-azureml/)

## Compito

Rivedi uno dei due notebook associati a questa lezione e riaddestra la GAN utilizzando le tue immagini. Cosa riesci a creare?

**Disclaimer**:  
Questo documento è stato tradotto utilizzando il servizio di traduzione automatica [Co-op Translator](https://github.com/Azure/co-op-translator). Sebbene ci impegniamo per garantire l'accuratezza, si prega di notare che le traduzioni automatiche possono contenere errori o imprecisioni. Il documento originale nella sua lingua nativa dovrebbe essere considerato la fonte autorevole. Per informazioni critiche, si raccomanda una traduzione professionale effettuata da un esperto umano. Non siamo responsabili per eventuali incomprensioni o interpretazioni errate derivanti dall'uso di questa traduzione.