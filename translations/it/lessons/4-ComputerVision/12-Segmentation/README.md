<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "d7f8a25ff13cfe9f4cd671cc23351fad",
  "translation_date": "2025-08-26T07:00:33+00:00",
  "source_file": "lessons/4-ComputerVision/12-Segmentation/README.md",
  "language_code": "it"
}
-->
# Segmentazione

Abbiamo già imparato a conoscere il Rilevamento degli Oggetti, che ci permette di individuare gli oggetti in un'immagine prevedendo i loro *bounding box*. Tuttavia, per alcuni compiti non ci bastano solo i bounding box, ma abbiamo bisogno di una localizzazione più precisa degli oggetti. Questo compito si chiama **segmentazione**.

## [Quiz pre-lezione](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/112)

La segmentazione può essere vista come una **classificazione dei pixel**, in cui per **ogni** pixel dell'immagine dobbiamo prevedere la sua classe (*sfondo* essendo una delle classi). Esistono due principali algoritmi di segmentazione:

* La **segmentazione semantica** indica solo la classe del pixel, senza distinguere tra diversi oggetti della stessa classe.
* La **segmentazione per istanza** divide le classi in istanze diverse.

Ad esempio, nella segmentazione per istanza, queste pecore sono oggetti diversi, mentre nella segmentazione semantica tutte le pecore sono rappresentate da una sola classe.

<img src="images/instance_vs_semantic.jpeg" width="50%">

> Immagine tratta da [questo post sul blog](https://nirmalamurali.medium.com/image-classification-vs-semantic-segmentation-vs-instance-segmentation-625c33a08d50)

Esistono diverse architetture neurali per la segmentazione, ma tutte hanno la stessa struttura. In un certo senso, è simile all'autoencoder di cui hai già appreso, ma invece di decostruire l'immagine originale, il nostro obiettivo è decostruire una **maschera**. Pertanto, una rete di segmentazione ha le seguenti parti:

* **Encoder**: estrae le caratteristiche dall'immagine di input.
* **Decoder**: trasforma queste caratteristiche nell'**immagine maschera**, con la stessa dimensione e un numero di canali corrispondente al numero di classi.

<img src="images/segm.png" width="80%">

> Immagine tratta da [questa pubblicazione](https://arxiv.org/pdf/2001.05566.pdf)

Dobbiamo menzionare in particolare la funzione di perdita utilizzata per la segmentazione. Quando si utilizzano autoencoder classici, dobbiamo misurare la somiglianza tra due immagini, e possiamo utilizzare l'errore quadratico medio (MSE) per farlo. Nella segmentazione, ogni pixel nell'immagine maschera target rappresenta il numero della classe (one-hot-encoded lungo la terza dimensione), quindi dobbiamo utilizzare funzioni di perdita specifiche per la classificazione - la cross-entropy loss, mediata su tutti i pixel. Se la maschera è binaria, si utilizza la **binary cross-entropy loss** (BCE).

> ✅ La codifica one-hot è un modo per codificare un'etichetta di classe in un vettore di lunghezza pari al numero di classi. Dai un'occhiata a [questo articolo](https://datagy.io/sklearn-one-hot-encode/) su questa tecnica.

## Segmentazione per Immagini Mediche

In questa lezione, vedremo la segmentazione in azione addestrando una rete a riconoscere i nevi umani (noti anche come nei) nelle immagini mediche. Utilizzeremo il <a href="https://www.fc.up.pt/addi/ph2%20database.html">Database PH<sup>2</sup></a> di immagini dermoscopiche come fonte di immagini. Questo dataset contiene 200 immagini di tre classi: nevo tipico, nevo atipico e melanoma. Tutte le immagini contengono anche una corrispondente **maschera** che delinea il nevo.

> ✅ Questa tecnica è particolarmente adatta per questo tipo di immagini mediche, ma quali altre applicazioni nel mondo reale potresti immaginare?

<img alt="navi" src="images/navi.png"/>

> Immagine tratta dal Database PH<sup>2</sup>

Addestreremo un modello per segmentare qualsiasi nevo dal suo sfondo.

## ✍️ Esercizi: Segmentazione Semantica

Apri i notebook qui sotto per saperne di più sulle diverse architetture di segmentazione semantica, esercitarti a lavorare con esse e vederle in azione.

* [Segmentazione Semantica Pytorch](../../../../../lessons/4-ComputerVision/12-Segmentation/SemanticSegmentationPytorch.ipynb)
* [Segmentazione Semantica TensorFlow](../../../../../lessons/4-ComputerVision/12-Segmentation/SemanticSegmentationTF.ipynb)

## [Quiz post-lezione](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/212)

## Conclusione

La segmentazione è una tecnica molto potente per la classificazione delle immagini, andando oltre i bounding box fino alla classificazione a livello di pixel. È una tecnica utilizzata nell'imaging medico, tra le altre applicazioni.

## 🚀 Sfida

La segmentazione del corpo è solo uno dei compiti comuni che possiamo svolgere con le immagini delle persone. Altri compiti importanti includono il **rilevamento dello scheletro** e il **rilevamento della posa**. Prova la libreria [OpenPose](https://github.com/CMU-Perceptual-Computing-Lab/openpose) per vedere come può essere utilizzato il rilevamento della posa.

## Revisione e Studio Autonomo

Questo [articolo di Wikipedia](https://wikipedia.org/wiki/Image_segmentation) offre una buona panoramica delle varie applicazioni di questa tecnica. Approfondisci autonomamente i sottodomini della segmentazione per istanza e della segmentazione panottica in questo campo di studio.

## [Compito](lab/README.md)

In questo laboratorio, prova la **segmentazione del corpo umano** utilizzando il [Segmentation Full Body MADS Dataset](https://www.kaggle.com/datasets/tapakah68/segmentation-full-body-mads-dataset) da Kaggle.

**Disclaimer**:  
Questo documento è stato tradotto utilizzando il servizio di traduzione automatica [Co-op Translator](https://github.com/Azure/co-op-translator). Sebbene ci impegniamo per garantire l'accuratezza, si prega di notare che le traduzioni automatiche potrebbero contenere errori o imprecisioni. Il documento originale nella sua lingua nativa dovrebbe essere considerato la fonte autorevole. Per informazioni critiche, si raccomanda una traduzione professionale effettuata da un traduttore umano. Non siamo responsabili per eventuali incomprensioni o interpretazioni errate derivanti dall'uso di questa traduzione.