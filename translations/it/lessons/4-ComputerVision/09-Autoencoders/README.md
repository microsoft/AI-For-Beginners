<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "0b306c04f5337b6e7430e5c0b16bb5c0",
  "translation_date": "2025-08-26T07:00:05+00:00",
  "source_file": "lessons/4-ComputerVision/09-Autoencoders/README.md",
  "language_code": "it"
}
-->
# Autoencoder

Quando si addestrano le CNN, uno dei problemi è che abbiamo bisogno di molti dati etichettati. Nel caso della classificazione delle immagini, dobbiamo separare le immagini in diverse classi, il che richiede un lavoro manuale.

## [Quiz pre-lezione](https://ff-quizzes.netlify.app/en/ai/quiz/17)

Tuttavia, potremmo voler utilizzare dati grezzi (non etichettati) per addestrare gli estrattori di caratteristiche delle CNN, il che viene chiamato **apprendimento auto-supervisionato**. Invece delle etichette, utilizzeremo le immagini di addestramento sia come input che come output della rete. L'idea principale dell'**autoencoder** è che avremo una **rete encoder** che converte l'immagine di input in uno **spazio latente** (normalmente è solo un vettore di dimensioni ridotte), e poi una **rete decoder**, il cui obiettivo sarà ricostruire l'immagine originale.

> ✅ Un [autoencoder](https://wikipedia.org/wiki/Autoencoder) è "un tipo di rete neurale artificiale utilizzata per apprendere codifiche efficienti di dati non etichettati."

Poiché stiamo addestrando un autoencoder per catturare quante più informazioni possibili dall'immagine originale per una ricostruzione accurata, la rete cerca di trovare il miglior **embedding** delle immagini di input per catturarne il significato.

![Diagramma AutoEncoder](../../../../../translated_images/autoencoder_schema.5e6fc9ad98a5eb6197f3513cf3baf4dfbe1389a6ae74daebda64de9f1c99f142.it.jpg)

> Immagine dal [blog di Keras](https://blog.keras.io/building-autoencoders-in-keras.html)

## Scenari di utilizzo degli Autoencoder

Sebbene la ricostruzione delle immagini originali possa non sembrare utile di per sé, ci sono alcuni scenari in cui gli autoencoder sono particolarmente utili:

* **Riduzione della dimensione delle immagini per la visualizzazione** o **addestramento degli embedding delle immagini**. Di solito gli autoencoder danno risultati migliori rispetto al PCA, perché tengono conto della natura spaziale delle immagini e delle caratteristiche gerarchiche.
* **Rimozione del rumore**, ovvero eliminare il rumore dall'immagine. Poiché il rumore trasporta molte informazioni inutili, l'autoencoder non può inserirle tutte nello spazio latente relativamente piccolo e quindi cattura solo la parte importante dell'immagine. Quando si addestrano denoiser, si parte dalle immagini originali e si utilizzano immagini con rumore artificiale aggiunto come input per l'autoencoder.
* **Super-risoluzione**, ovvero aumentare la risoluzione delle immagini. Si parte da immagini ad alta risoluzione e si utilizza l'immagine a risoluzione inferiore come input per l'autoencoder.
* **Modelli generativi**. Una volta addestrato l'autoencoder, la parte decoder può essere utilizzata per creare nuovi oggetti partendo da vettori latenti casuali.

## Autoencoder Variazionali (VAE)

Gli autoencoder tradizionali riducono la dimensione dei dati di input in qualche modo, individuando le caratteristiche importanti delle immagini di input. Tuttavia, i vettori latenti spesso non hanno molto senso. In altre parole, prendendo come esempio il dataset MNIST, capire quali cifre corrispondono ai diversi vettori latenti non è un compito facile, perché vettori latenti vicini non corrispondono necessariamente alle stesse cifre.

D'altra parte, per addestrare modelli *generativi* è meglio avere una certa comprensione dello spazio latente. Questa idea ci porta agli **autoencoder variazionali** (VAE).

Il VAE è un autoencoder che apprende a prevedere una *distribuzione statistica* dei parametri latenti, la cosiddetta **distribuzione latente**. Ad esempio, potremmo voler che i vettori latenti siano distribuiti normalmente con una certa media z<sub>mean</sub> e deviazione standard z<sub>sigma</sub> (sia la media che la deviazione standard sono vettori di una certa dimensionalità d). L'encoder nel VAE apprende a prevedere questi parametri, e poi il decoder prende un vettore casuale da questa distribuzione per ricostruire l'oggetto.

Per riassumere:

 * Dal vettore di input, prevediamo `z_mean` e `z_log_sigma` (invece di prevedere direttamente la deviazione standard, prevediamo il suo logaritmo)
 * Campioniamo un vettore `sample` dalla distribuzione N(z<sub>mean</sub>,exp(z<sub>log\_sigma</sub>))
 * Il decoder cerca di decodificare l'immagine originale utilizzando `sample` come vettore di input

 <img src="images/vae.png" width="50%">

> Immagine da [questo post sul blog](https://ijdykeman.github.io/ml/2016/12/21/cvae.html) di Isaak Dykeman

Gli autoencoder variazionali utilizzano una funzione di perdita complessa composta da due parti:

* **Perdita di ricostruzione**, ovvero la funzione di perdita che mostra quanto l'immagine ricostruita sia vicina al target (può essere l'Errore Quadratico Medio, o MSE). È la stessa funzione di perdita degli autoencoder normali.
* **Perdita KL**, che garantisce che le distribuzioni delle variabili latenti rimangano vicine alla distribuzione normale. Si basa sul concetto di [divergenza di Kullback-Leibler](https://www.countbayesie.com/blog/2017/5/9/kullback-leibler-divergence-explained) - una metrica per stimare quanto siano simili due distribuzioni statistiche.

Un vantaggio importante dei VAE è che ci permettono di generare nuove immagini relativamente facilmente, perché sappiamo da quale distribuzione campionare i vettori latenti. Ad esempio, se addestriamo un VAE con un vettore latente 2D su MNIST, possiamo poi variare i componenti del vettore latente per ottenere cifre diverse:

<img alt="vaemnist" src="images/vaemnist.png" width="50%"/>

> Immagine di [Dmitry Soshnikov](http://soshnikov.com)

Osserva come le immagini si fondono l'una nell'altra, mentre iniziamo a ottenere vettori latenti da diverse porzioni dello spazio dei parametri latenti. Possiamo anche visualizzare questo spazio in 2D:

<img alt="vaemnist cluster" src="images/vaemnist-diag.png" width="50%"/> 

> Immagine di [Dmitry Soshnikov](http://soshnikov.com)

## ✍️ Esercizi: Autoencoder

Scopri di più sugli autoencoder in questi notebook corrispondenti:

* [Autoencoder in TensorFlow](../../../../../lessons/4-ComputerVision/09-Autoencoders/AutoencodersTF.ipynb)
* [Autoencoder in PyTorch](../../../../../lessons/4-ComputerVision/09-Autoencoders/AutoEncodersPyTorch.ipynb)

## Proprietà degli Autoencoder

* **Specifici per i dati** - funzionano bene solo con il tipo di immagini su cui sono stati addestrati. Ad esempio, se addestriamo una rete di super-risoluzione sui fiori, non funzionerà bene sui ritratti. Questo perché la rete può produrre immagini ad alta risoluzione prendendo dettagli fini dalle caratteristiche apprese dal dataset di addestramento.
* **Con perdita** - l'immagine ricostruita non è identica all'immagine originale. La natura della perdita è definita dalla *funzione di perdita* utilizzata durante l'addestramento.
* Funziona su **dati non etichettati**

## [Quiz post-lezione](https://ff-quizzes.netlify.app/en/ai/quiz/18)

## Conclusione

In questa lezione, hai imparato i vari tipi di autoencoder disponibili per lo scienziato AI. Hai imparato come costruirli e come usarli per ricostruire immagini. Hai anche imparato il VAE e come usarlo per generare nuove immagini.

## 🚀 Sfida

In questa lezione, hai imparato a utilizzare gli autoencoder per le immagini. Ma possono essere utilizzati anche per la musica! Dai un'occhiata al progetto [MusicVAE](https://magenta.tensorflow.org/music-vae) del progetto Magenta, che utilizza gli autoencoder per imparare a ricostruire la musica. Fai alcuni [esperimenti](https://colab.research.google.com/github/magenta/magenta-demos/blob/master/colab-notebooks/Multitrack_MusicVAE.ipynb) con questa libreria per vedere cosa puoi creare.

## [Quiz post-lezione](https://ff-quizzes.netlify.app/en/ai/quiz/16)

## Revisione & Studio Autonomo

Per riferimento, leggi di più sugli autoencoder in queste risorse:

* [Costruire Autoencoder in Keras](https://blog.keras.io/building-autoencoders-in-keras.html)
* [Post sul blog di NeuroHive](https://neurohive.io/ru/osnovy-data-science/variacionnyj-avtojenkoder-vae/)
* [Autoencoder Variazionali Spiegati](https://kvfrans.com/variational-autoencoders-explained/)
* [Autoencoder Variazionali Condizionali](https://ijdykeman.github.io/ml/2016/12/21/cvae.html)

## Compito

Alla fine di [questo notebook usando TensorFlow](../../../../../lessons/4-ComputerVision/09-Autoencoders/AutoencodersTF.ipynb), troverai un 'task' - usalo come tuo compito.

**Disclaimer**:  
Questo documento è stato tradotto utilizzando il servizio di traduzione automatica [Co-op Translator](https://github.com/Azure/co-op-translator). Sebbene ci impegniamo per garantire l'accuratezza, si prega di tenere presente che le traduzioni automatiche possono contenere errori o imprecisioni. Il documento originale nella sua lingua nativa dovrebbe essere considerato la fonte autorevole. Per informazioni critiche, si raccomanda una traduzione professionale effettuata da un traduttore umano. Non siamo responsabili per eventuali incomprensioni o interpretazioni errate derivanti dall'uso di questa traduzione.