# Contribuisci traducendo le lezioni

Accogliamo con piacere traduzioni delle lezioni contenute in questo curriculum!

## Linee guida

In ogni cartella delle lezioni e nella cartella di introduzione alle lezioni ci sono delle sottocartelle che contengono i file Markdown tradotti.

> Nota: ti chiediamo di **non tradurre alcun codice** nei file di esempio. Gli unici contenuti da tradurre sono i file README, gli assignment e i quiz. Grazie!

I file tradotti devono seguire questa convenzione di denominazione:

**README._[lingua]_.md**

dove _[lingua]_ è un'abbreviazione di due lettere della lingua, secondo lo standard ISO 639-1 (es. `README.es.md` per lo spagnolo e `README.nl.md` per l’olandese).

**assignment._[lingua]_.md**

Allo stesso modo dei README, anche gli assignment devono essere tradotti.

**Quiz**

1. Aggiungi la tua traduzione al quiz-app creando un file qui: https://github.com/microsoft/AI-For-Beginners/tree/main/etc/quiz-app/src/assets/translations, utilizzando la convenzione di denominazione corretta (es. `en.json`, `fr.json`).  
   **Per favore, non localizzare le parole ‘true’ o ‘false’. Grazie!**

2. Aggiungi il codice della tua lingua al menu a discesa nel file `App.vue` del quiz-app.

3. Modifica il file [index.js delle traduzioni](https://github.com/microsoft/AI-For-Beginners/blob/main/etc/quiz-app/src/assets/translations/index.js) per includere la tua lingua.

4. Infine, modifica **tutti** i link ai quiz nei tuoi file README.md tradotti affinché puntino direttamente alla tua versione tradotta del quiz:  
   `https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/1` diventa  
   `https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/1?loc=id`

**GRAZIE**

Apprezziamo davvero tanto il tuo impegno!
