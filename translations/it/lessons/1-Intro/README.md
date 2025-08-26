<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "5d1cbc67a9690adb5b33adf297794087",
  "translation_date": "2025-08-26T06:59:29+00:00",
  "source_file": "lessons/1-Intro/README.md",
  "language_code": "it"
}
-->
> Immagine di [Dmitry Soshnikov](http://soshnikov.com)

Con il passare del tempo, le risorse informatiche sono diventate più economiche e sono stati resi disponibili più dati, permettendo agli approcci basati su reti neurali di dimostrare grandi prestazioni nel competere con gli esseri umani in molti ambiti, come la visione artificiale o la comprensione del linguaggio parlato. Nell'ultimo decennio, il termine Intelligenza Artificiale è stato spesso usato come sinonimo di Reti Neurali, poiché la maggior parte dei successi dell'IA di cui sentiamo parlare si basa su di esse.

Possiamo osservare come gli approcci siano cambiati, ad esempio, nella creazione di un programma per giocare a scacchi:

* I primi programmi di scacchi si basavano sulla ricerca: un programma cercava di stimare esplicitamente le possibili mosse dell'avversario per un certo numero di mosse successive e selezionava la mossa ottimale basandosi sulla posizione migliore che poteva essere raggiunta in poche mosse. Questo ha portato allo sviluppo del cosiddetto algoritmo di ricerca [alpha-beta pruning](https://en.wikipedia.org/wiki/Alpha%E2%80%93beta_pruning).
* Le strategie di ricerca funzionano bene verso la fine della partita, dove lo spazio di ricerca è limitato da un numero ridotto di mosse possibili. Tuttavia, all'inizio della partita, lo spazio di ricerca è enorme e l'algoritmo può essere migliorato imparando dalle partite esistenti tra giocatori umani. Esperimenti successivi hanno impiegato il cosiddetto [case-based reasoning](https://en.wikipedia.org/wiki/Case-based_reasoning), in cui il programma cercava casi nella base di conoscenza molto simili alla posizione attuale nel gioco.
* I programmi moderni che vincono contro i giocatori umani si basano su reti neurali e [apprendimento per rinforzo](https://en.wikipedia.org/wiki/Reinforcement_learning), dove i programmi imparano a giocare semplicemente giocando a lungo contro sé stessi e apprendendo dai propri errori, proprio come fanno gli esseri umani quando imparano a giocare a scacchi. Tuttavia, un programma informatico può giocare molte più partite in molto meno tempo e quindi può imparare molto più velocemente.

✅ Fai una piccola ricerca su altri giochi che sono stati giocati dall'IA.

Allo stesso modo, possiamo osservare come l'approccio alla creazione di "programmi parlanti" (che potrebbero superare il test di Turing) sia cambiato:

* I primi programmi di questo tipo, come [Eliza](https://en.wikipedia.org/wiki/ELIZA), si basavano su regole grammaticali molto semplici e sulla riformulazione della frase di input in una domanda.
* Gli assistenti moderni, come Cortana, Siri o Google Assistant, sono tutti sistemi ibridi che utilizzano reti neurali per convertire il parlato in testo e riconoscere l'intento dell'utente, per poi impiegare un po' di ragionamento o algoritmi espliciti per eseguire le azioni richieste.
* In futuro, possiamo aspettarci un modello completamente basato su reti neurali per gestire il dialogo autonomamente. Le recenti famiglie di reti neurali GPT e [Turing-NLG](https://turing.microsoft.com/) mostrano grandi successi in questo ambito.

> Immagine di Dmitry Soshnikov, [foto](https://unsplash.com/photos/r8LmVbUKgns) di [Marina Abrosimova](https://unsplash.com/@abrosimova_marina_foto), Unsplash

## Recenti Ricerche sull'AI

Il grande sviluppo recente nella ricerca sulle reti neurali è iniziato intorno al 2010, quando sono diventati disponibili grandi dataset pubblici. Una vasta collezione di immagini chiamata [ImageNet](https://en.wikipedia.org/wiki/ImageNet), che contiene circa 14 milioni di immagini annotate, ha dato vita alla [ImageNet Large Scale Visual Recognition Challenge](https://image-net.org/challenges/LSVRC/).

![Precisione ILSVRC](../../../../lessons/1-Intro/images/ilsvrc.gif)

> Immagine di [Dmitry Soshnikov](http://soshnikov.com)

Nel 2012, le [Reti Neurali Convoluzionali](../4-ComputerVision/07-ConvNets/README.md) sono state utilizzate per la prima volta nella classificazione delle immagini, portando a una significativa riduzione degli errori di classificazione (dal quasi 30% al 16,4%). Nel 2015, l'architettura ResNet di Microsoft Research [raggiunse una precisione a livello umano](https://doi.org/10.1109/ICCV.2015.123).

Da allora, le Reti Neurali hanno dimostrato un comportamento molto efficace in molti compiti:

---

Anno | Parità con l'Umano raggiunta
-----|-----------------------------
2015 | [Classificazione delle Immagini](https://doi.org/10.1109/ICCV.2015.123)
2016 | [Riconoscimento del Parlato Conversazionale](https://arxiv.org/abs/1610.05256)
2018 | [Traduzione Automatica](https://arxiv.org/abs/1803.05567) (Cinese-Inglese)
2020 | [Descrizione delle Immagini](https://arxiv.org/abs/2009.13682)

Negli ultimi anni abbiamo assistito a enormi successi con i modelli linguistici di grandi dimensioni, come BERT e GPT-3. Questo è avvenuto principalmente grazie alla grande quantità di dati testuali generali disponibili, che permettono di addestrare i modelli a catturare la struttura e il significato dei testi, pre-addestrarli su collezioni di testi generali e poi specializzarli per compiti più specifici. Impareremo di più sull'[Elaborazione del Linguaggio Naturale](../5-NLP/README.md) più avanti in questo corso.

## 🚀 Sfida

Fai un giro su internet per determinare dove, secondo te, l'AI viene utilizzata in modo più efficace. È in un'app di mappatura, in un servizio di riconoscimento vocale o in un videogioco? Ricerca come è stato costruito il sistema.

## [Quiz post-lezione](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/201)

## Revisione e Studio Autonomo

Rivedi la storia dell'AI e del ML leggendo [questa lezione](https://github.com/microsoft/ML-For-Beginners/tree/main/1-Introduction/2-history-of-ML). Prendi un elemento dallo sketchnote all'inizio di quella lezione o di questa e approfondiscilo per comprendere il contesto culturale che ha influenzato la sua evoluzione.

**Compito**: [Game Jam](assignment.md)

**Disclaimer**:  
Questo documento è stato tradotto utilizzando il servizio di traduzione automatica [Co-op Translator](https://github.com/Azure/co-op-translator). Sebbene ci impegniamo per garantire l'accuratezza, si prega di notare che le traduzioni automatiche potrebbero contenere errori o imprecisioni. Il documento originale nella sua lingua nativa dovrebbe essere considerato la fonte autorevole. Per informazioni critiche, si raccomanda una traduzione professionale effettuata da un traduttore umano. Non siamo responsabili per eventuali incomprensioni o interpretazioni errate derivanti dall'uso di questa traduzione.