# Contribuisci traducendo le lezioni

Accogliamo con piacere le traduzioni delle lezioni di questo curriculum!

## Linee guida

Ci sono cartelle in ogni cartella di lezione e nella cartella di introduzione alle lezioni che contengono i file markdown tradotti.

> Nota, per favore non tradurre alcun codice nei file di esempio di codice; le uniche cose da tradurre sono README, esercizi e quiz. Grazie!

I file tradotti devono seguire questa convenzione di denominazione:

**README._[lingua]_.md**

dove _[lingua]_ è un'abbreviazione di due lettere della lingua secondo lo standard ISO 639-1 (ad esempio `README.es.md` per lo spagnolo e `README.nl.md` per l'olandese).

**assignment._[lingua]_.md**

Simile ai README, traduci anche gli esercizi.

**Quiz**

1. Aggiungi la tua traduzione all'app del quiz aggiungendo un file qui: https://github.com/microsoft/AI-For-Beginners/tree/main/etc/quiz-app/src/assets/translations, seguendo la corretta convenzione di denominazione (en.json, fr.json). **Per favore, non localizzare le parole 'true' o 'false'. Grazie!**

2. Aggiungi il codice della tua lingua al menu a tendina nel file App.vue dell'app del quiz.

3. Modifica il [file index.js delle traduzioni](https://github.com/microsoft/AI-For-Beginners/blob/main/etc/quiz-app/src/assets/translations/index.js) dell'app del quiz per aggiungere la tua lingua.

4. Infine, modifica TUTTI i link ai quiz nei tuoi file README.md tradotti per puntare direttamente al tuo quiz tradotto: https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/1 diventa https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/1?loc=id

**GRAZIE**

Apprezziamo davvero i tuoi sforzi!

**Disclaimer**:  
Questo documento è stato tradotto utilizzando il servizio di traduzione automatica [Co-op Translator](https://github.com/Azure/co-op-translator). Sebbene ci impegniamo per garantire l'accuratezza, si prega di notare che le traduzioni automatiche possono contenere errori o imprecisioni. Il documento originale nella sua lingua nativa dovrebbe essere considerato la fonte autorevole. Per informazioni critiche, si raccomanda una traduzione professionale effettuata da un traduttore umano. Non siamo responsabili per eventuali incomprensioni o interpretazioni errate derivanti dall'uso di questa traduzione.