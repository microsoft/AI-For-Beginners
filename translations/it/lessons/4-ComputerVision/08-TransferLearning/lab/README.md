# Classificazione degli Oxford Pets utilizzando il Transfer Learning

Compito del laboratorio tratto dal [Curriculum AI for Beginners](https://github.com/microsoft/ai-for-beginners).

## Compito

Immagina di dover sviluppare un'applicazione per un asilo per animali domestici per catalogare tutti gli animali. Una delle funzionalità più utili di tale applicazione sarebbe quella di riconoscere automaticamente la razza da una fotografia. In questo compito, utilizzeremo il transfer learning per classificare immagini reali di animali domestici tratte dal dataset [Oxford-IIIT](https://www.robots.ox.ac.uk/~vgg/data/pets/).

## Il Dataset

Utilizzeremo il dataset originale [Oxford-IIIT](https://www.robots.ox.ac.uk/~vgg/data/pets/), che contiene 35 diverse razze di cani e gatti.

Per scaricare il dataset, utilizza questo frammento di codice:

```python
!wget https://www.robots.ox.ac.uk/~vgg/data/pets/data/images.tar.gz
!tar xfz images.tar.gz
!rm images.tar.gz
```

## Notebook di Partenza

Inizia il laboratorio aprendo [OxfordPets.ipynb](../../../../../../lessons/4-ComputerVision/08-TransferLearning/lab/OxfordPets.ipynb)

## Conclusione

Il transfer learning e le reti pre-addestrate ci permettono di risolvere problemi di classificazione delle immagini del mondo reale in modo relativamente semplice. Tuttavia, le reti pre-addestrate funzionano bene su immagini di tipo simile e, se iniziamo a classificare immagini molto diverse (ad esempio immagini mediche), è probabile che i risultati siano molto peggiori.

**Disclaimer**:  
Questo documento è stato tradotto utilizzando il servizio di traduzione automatica [Co-op Translator](https://github.com/Azure/co-op-translator). Sebbene ci impegniamo per garantire l'accuratezza, si prega di notare che le traduzioni automatiche possono contenere errori o imprecisioni. Il documento originale nella sua lingua nativa dovrebbe essere considerato la fonte autorevole. Per informazioni critiche, si raccomanda una traduzione professionale effettuata da un traduttore umano. Non siamo responsabili per eventuali incomprensioni o interpretazioni errate derivanti dall'uso di questa traduzione.