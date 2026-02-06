# Classificazione Multi-Classe con Perceptron

Compito del laboratorio dal [Curriculum AI for Beginners](https://github.com/microsoft/ai-for-beginners).

## Compito

Utilizzando il codice sviluppato in questa lezione per la classificazione binaria delle cifre scritte a mano del dataset MNIST, crea un classificatore multi-classe in grado di riconoscere qualsiasi cifra. Calcola l'accuratezza della classificazione sui dataset di addestramento e di test, e stampa la matrice di confusione.

## Suggerimenti

1. Per ogni cifra, crea un dataset per un classificatore binario del tipo "questa cifra vs. tutte le altre cifre".
1. Addestra 10 perceptroni diversi per la classificazione binaria (uno per ogni cifra).
1. Definisci una funzione che classifichi una cifra in input.

> **Suggerimento**: Se combiniamo i pesi di tutti e 10 i perceptroni in una matrice, dovremmo essere in grado di applicare tutti e 10 i perceptroni alle cifre in input con una sola moltiplicazione di matrici. La cifra più probabile può essere trovata semplicemente applicando l'operazione `argmax` sull'output.

## Notebook di Partenza

Inizia il laboratorio aprendo [PerceptronMultiClass.ipynb](PerceptronMultiClass.ipynb)

---

**Disclaimer**:  
Questo documento è stato tradotto utilizzando il servizio di traduzione automatica [Co-op Translator](https://github.com/Azure/co-op-translator). Sebbene ci impegniamo per garantire l'accuratezza, si prega di notare che le traduzioni automatiche possono contenere errori o imprecisioni. Il documento originale nella sua lingua nativa dovrebbe essere considerato la fonte autorevole. Per informazioni critiche, si consiglia una traduzione professionale eseguita da un traduttore umano. Non siamo responsabili per eventuali fraintendimenti o interpretazioni errate derivanti dall'uso di questa traduzione.