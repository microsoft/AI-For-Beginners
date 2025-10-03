<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f3d2cee9cb3c52160419e560c57a690e",
  "translation_date": "2025-08-26T07:03:23+00:00",
  "source_file": "lessons/4-ComputerVision/07-ConvNets/lab/README.md",
  "language_code": "it"
}
-->
# Classificazione dei Volti degli Animali Domestici

Compito del laboratorio tratto dal [Curriculum AI per Principianti](https://github.com/microsoft/ai-for-beginners).

## Compito

Immagina di dover sviluppare un'applicazione per un asilo per animali domestici per catalogare tutti gli animali. Una delle funzionalità più utili di tale applicazione sarebbe identificare automaticamente la razza da una fotografia. Questo può essere fatto con successo utilizzando le reti neurali.

Devi addestrare una rete neurale convoluzionale per classificare diverse razze di gatti e cani utilizzando il dataset **Pet Faces**.

## Il Dataset

Utilizzeremo il dataset **Pet Faces**, derivato dal dataset di animali domestici [Oxford-IIIT](https://www.robots.ox.ac.uk/~vgg/data/pets/). Contiene 35 diverse razze di cani e gatti.

![Dataset con cui lavoreremo](../../../../../../translated_images/data.50b2a9d5484bdbf0f52f5765b381cec9efe2bd296a98f007f90bedb6ac67f2a8.it.png)

Per scaricare il dataset, utilizza questo frammento di codice:

```python
!wget https://thor.robots.ox.ac.uk/~vgg/data/pets/images.tar.gz
!tar xfz images.tar.gz
!rm images.tar.gz
```

## Notebook di Partenza

Inizia il laboratorio aprendo [PetFaces.ipynb](../../../../../../lessons/4-ComputerVision/07-ConvNets/lab/PetFaces.ipynb)

## Conclusione

Hai risolto un problema relativamente complesso di classificazione delle immagini da zero! C'erano molte classi, e sei comunque riuscito a ottenere una precisione ragionevole! Ha anche senso misurare la top-k accuracy, perché è facile confondere alcune classi che non sono chiaramente distinguibili nemmeno per gli esseri umani.

**Disclaimer**:  
Questo documento è stato tradotto utilizzando il servizio di traduzione automatica [Co-op Translator](https://github.com/Azure/co-op-translator). Sebbene ci impegniamo per garantire l'accuratezza, si prega di notare che le traduzioni automatiche potrebbero contenere errori o imprecisioni. Il documento originale nella sua lingua nativa dovrebbe essere considerato la fonte autorevole. Per informazioni critiche, si raccomanda una traduzione professionale effettuata da un esperto umano. Non siamo responsabili per eventuali fraintendimenti o interpretazioni errate derivanti dall'uso di questa traduzione.