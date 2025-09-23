<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a560d5b845962cf33dc102266e409568",
  "translation_date": "2025-09-23T08:28:11+00:00",
  "source_file": "lessons/4-ComputerVision/07-ConvNets/README.md",
  "language_code": "it"
}
-->
# Reti Neurali Convoluzionali

Abbiamo visto in precedenza che le reti neurali sono piuttosto efficaci nel trattare le immagini, e persino un percettrone a un solo strato è in grado di riconoscere le cifre scritte a mano del dataset MNIST con una precisione ragionevole. Tuttavia, il dataset MNIST è molto particolare: tutte le cifre sono centrate all'interno dell'immagine, il che rende il compito più semplice.

## [Quiz pre-lezione](https://ff-quizzes.netlify.app/en/ai/quiz/13)

Nella vita reale, vogliamo essere in grado di riconoscere oggetti in un'immagine indipendentemente dalla loro posizione esatta. La visione artificiale è diversa dalla classificazione generica, perché quando cerchiamo un determinato oggetto in un'immagine, stiamo scansionando l'immagine alla ricerca di specifici **schemi** e delle loro combinazioni. Ad esempio, cercando un gatto, potremmo iniziare cercando linee orizzontali che possono formare i baffi, e poi una certa combinazione di baffi potrebbe indicarci che si tratta effettivamente di un gatto. La posizione relativa e la presenza di determinati schemi sono importanti, non la loro posizione esatta nell'immagine.

Per estrarre schemi, utilizzeremo il concetto di **filtri convoluzionali**. Come sapete, un'immagine è rappresentata da una matrice 2D o da un tensore 3D con profondità di colore. Applicare un filtro significa prendere una matrice relativamente piccola chiamata **kernel del filtro**, e per ogni pixel dell'immagine originale calcolare la media ponderata con i punti vicini. Possiamo immaginare questo processo come una piccola finestra che scorre su tutta l'immagine, mediando tutti i pixel secondo i pesi nella matrice del kernel del filtro.

![Filtro per bordi verticali](../../../../../translated_images/filter-vert.b7148390ca0bc356ddc7e55555d2481819c1e86ddde9dce4db5e71a69d6f887f.it.png) | ![Filtro per bordi orizzontali](../../../../../translated_images/filter-horiz.59b80ed4feb946efbe201a7fe3ca95abb3364e266e6fd90820cb893b4d3a6dda.it.png)
----|----

> Immagine di Dmitry Soshnikov

Ad esempio, se applichiamo filtri per bordi verticali e orizzontali 3x3 alle cifre del dataset MNIST, possiamo evidenziare (ad esempio, ottenere valori alti) dove ci sono bordi verticali e orizzontali nell'immagine originale. Questi due filtri possono quindi essere utilizzati per "cercare" bordi. Allo stesso modo, possiamo progettare filtri diversi per cercare altri schemi di basso livello:

<img src="images/lmfilters.jpg" width="500" align="center"/>

> Immagine del [Leung-Malik Filter Bank](https://www.robots.ox.ac.uk/~vgg/research/texclass/filters.html)

Tuttavia, mentre possiamo progettare manualmente i filtri per estrarre alcuni schemi, possiamo anche progettare la rete in modo tale che impari automaticamente gli schemi. Questa è una delle idee principali alla base delle CNN.

## Idee principali delle CNN

Il funzionamento delle CNN si basa sulle seguenti idee fondamentali:

* I filtri convoluzionali possono estrarre schemi
* Possiamo progettare la rete in modo che i filtri vengano addestrati automaticamente
* Possiamo utilizzare lo stesso approccio per trovare schemi in caratteristiche di alto livello, non solo nell'immagine originale. Pertanto, l'estrazione delle caratteristiche nelle CNN funziona su una gerarchia di caratteristiche, partendo da combinazioni di pixel di basso livello fino ad arrivare a combinazioni di alto livello di parti dell'immagine.

![Estrazione gerarchica delle caratteristiche](../../../../../translated_images/FeatureExtractionCNN.d9b456cbdae7cb643fde3032b81b2940e3cf8be842e29afac3f482725ba7f95c.it.png)

> Immagine tratta da [un articolo di Hislop-Lynch](https://www.semanticscholar.org/paper/Computer-vision-based-pedestrian-trajectory-Hislop-Lynch/26e6f74853fc9bbb7487b06dc2cf095d36c9021d), basato sulla [loro ricerca](https://dl.acm.org/doi/abs/10.1145/1553374.1553453)

## ✍️ Esercizi: Reti Neurali Convoluzionali

Continuiamo a esplorare come funzionano le reti neurali convoluzionali e come possiamo ottenere filtri addestrabili, lavorando sui notebook corrispondenti:

* [Reti Neurali Convoluzionali - PyTorch](ConvNetsPyTorch.ipynb)
* [Reti Neurali Convoluzionali - TensorFlow](ConvNetsTF.ipynb)

## Architettura a Piramide

La maggior parte delle CNN utilizzate per l'elaborazione delle immagini segue una cosiddetta architettura a piramide. Il primo strato convoluzionale applicato alle immagini originali ha tipicamente un numero relativamente basso di filtri (8-16), che corrispondono a diverse combinazioni di pixel, come linee orizzontali/verticali o tratti. Al livello successivo, riduciamo la dimensione spaziale della rete e aumentiamo il numero di filtri, che corrisponde a più possibili combinazioni di caratteristiche semplici. Con ogni strato, man mano che ci avviciniamo al classificatore finale, le dimensioni spaziali dell'immagine diminuiscono e il numero di filtri cresce.

Ad esempio, osserviamo l'architettura di VGG-16, una rete che ha raggiunto il 92,7% di accuratezza nella classificazione top-5 di ImageNet nel 2014:

![Strati di ImageNet](../../../../../translated_images/vgg-16-arch1.d901a5583b3a51baeaab3e768567d921e5d54befa46e1e642616c5458c934028.it.jpg)

![Piramide di ImageNet](../../../../../translated_images/vgg-16-arch.64ff2137f50dd49fdaa786e3f3a975b3f22615efd13efb19c5d22f12e01451a1.it.jpg)

> Immagine tratta da [Researchgate](https://www.researchgate.net/figure/Vgg16-model-structure-To-get-the-VGG-NIN-model-we-replace-the-2-nd-4-th-6-th-7-th_fig2_335194493)

## Architetture CNN più conosciute

[Continua il tuo studio sulle architetture CNN più conosciute](CNN_Architectures.md)

---

