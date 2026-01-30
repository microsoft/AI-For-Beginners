# AI Etica e Responsabile

Hai quasi terminato questo corso e spero che ormai tu abbia chiaramente compreso che l'AI si basa su una serie di metodi matematici formali che ci permettono di trovare relazioni nei dati e di addestrare modelli per replicare alcuni aspetti del comportamento umano. In questo momento storico, consideriamo l'AI uno strumento molto potente per estrarre schemi dai dati e applicarli per risolvere nuovi problemi.

## [Quiz pre-lezione](https://white-water-09ec41f0f.azurestaticapps.net/quiz/5/)

Tuttavia, nella fantascienza spesso vediamo storie in cui l'AI rappresenta un pericolo per l'umanità. Di solito queste storie ruotano attorno a una sorta di ribellione dell'AI, quando l'AI decide di confrontarsi con gli esseri umani. Questo implica che l'AI abbia una sorta di emozione o possa prendere decisioni impreviste dai suoi sviluppatori.

Il tipo di AI che abbiamo studiato in questo corso non è altro che una grande aritmetica matriciale. È uno strumento molto potente per aiutarci a risolvere i nostri problemi e, come qualsiasi altro strumento potente, può essere usato per scopi buoni o cattivi. È importante sottolineare che può essere *mal utilizzato*.

## Principi di AI Responsabile

Per evitare questo uso improprio, accidentale o intenzionale, Microsoft stabilisce i [Principi di AI Responsabile](https://www.microsoft.com/ai/responsible-ai?WT.mc_id=academic-77998-cacaste). I seguenti concetti sono alla base di questi principi:

* **Equità** è legata al problema importante dei *bias nei modelli*, che possono essere causati dall'uso di dati di addestramento distorti. Ad esempio, quando cerchiamo di prevedere la probabilità che una persona ottenga un lavoro come sviluppatore software, il modello potrebbe dare una preferenza maggiore ai maschi, semplicemente perché il dataset di addestramento era probabilmente orientato verso un pubblico maschile. Dobbiamo bilanciare attentamente i dati di addestramento e investigare il modello per evitare bias e assicurarci che il modello prenda in considerazione caratteristiche più rilevanti.
* **Affidabilità e Sicurezza**. Per loro natura, i modelli di AI possono commettere errori. Una rete neurale restituisce probabilità, e dobbiamo tenerne conto quando prendiamo decisioni. Ogni modello ha una certa precisione e richiamo, e dobbiamo comprenderlo per prevenire i danni che un consiglio errato può causare.
* **Privacy e Sicurezza** hanno alcune implicazioni specifiche per l'AI. Ad esempio, quando utilizziamo alcuni dati per addestrare un modello, questi dati diventano in qualche modo "integrati" nel modello. Da un lato, ciò aumenta la sicurezza e la privacy, dall'altro dobbiamo ricordare quali dati sono stati utilizzati per l'addestramento del modello.
* **Inclusività** significa che non stiamo costruendo AI per sostituire le persone, ma piuttosto per potenziarle e rendere il nostro lavoro più creativo. È anche legata all'equità, perché quando si tratta di comunità sottorappresentate, la maggior parte dei dataset che raccogliamo tende ad essere distorta, e dobbiamo assicurarci che queste comunità siano incluse e gestite correttamente dall'AI.
* **Trasparenza**. Questo include assicurarsi che sia sempre chiaro quando viene utilizzata l'AI. Inoltre, ove possibile, vogliamo utilizzare sistemi di AI che siano *interpretabili*.
* **Responsabilità**. Quando i modelli di AI prendono delle decisioni, non è sempre chiaro chi sia responsabile di quelle decisioni. Dobbiamo assicurarci di comprendere dove risiede la responsabilità delle decisioni dell'AI. Nella maggior parte dei casi, vorremmo includere esseri umani nel processo decisionale per le decisioni importanti, in modo che siano le persone a essere ritenute responsabili.

## Strumenti per AI Responsabile

Microsoft ha sviluppato il [Responsible AI Toolbox](https://github.com/microsoft/responsible-ai-toolbox) che contiene una serie di strumenti:

* Interpretability Dashboard (InterpretML)
* Fairness Dashboard (FairLearn)
* Error Analysis Dashboard
* Responsible AI Dashboard che include:

   - EconML - uno strumento per l'Analisi Causale, che si concentra sulle domande "cosa succederebbe se"
   - DiCE - uno strumento per l'Analisi Controfattuale che ti permette di vedere quali caratteristiche devono essere modificate per influenzare la decisione del modello

Per ulteriori informazioni sull'etica dell'AI, visita [questa lezione](https://github.com/microsoft/ML-For-Beginners/tree/main/1-Introduction/3-fairness?WT.mc_id=academic-77998-cacaste) nel curriculum di Machine Learning che include esercizi.

## Revisione e Studio Autonomo

Segui questo [Percorso di Apprendimento](https://docs.microsoft.com/learn/modules/responsible-ai-principles/?WT.mc_id=academic-77998-cacaste) per approfondire i principi di AI responsabile.

## [Quiz post-lezione](https://white-water-09ec41f0f.azurestaticapps.net/quiz/6/)

**Disclaimer**:  
Questo documento è stato tradotto utilizzando il servizio di traduzione automatica [Co-op Translator](https://github.com/Azure/co-op-translator). Sebbene ci impegniamo per garantire l'accuratezza, si prega di notare che le traduzioni automatiche potrebbero contenere errori o imprecisioni. Il documento originale nella sua lingua nativa dovrebbe essere considerato la fonte autorevole. Per informazioni critiche, si raccomanda una traduzione professionale effettuata da un esperto umano. Non siamo responsabili per eventuali incomprensioni o interpretazioni errate derivanti dall'uso di questa traduzione.