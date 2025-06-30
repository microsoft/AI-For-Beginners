# Introduzione all'Intelligenza Artificiale

![Riepilogo dell'introduzione all'IA in uno schizzo](../sketchnotes/ai-intro.png)

> Sketchnote di [Tomomi Imura](https://twitter.com/girlie_mac)

## [Quiz preliminare](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/101)

**L'intelligenza artificiale** è una disciplina scientifica entusiasmante che studia come possiamo far sì che i computer mostrino un comportamento intelligente, ad esempio facendo cose in cui gli esseri umani sono bravi.

Originariamente, i computer furono inventati da [Charles Babbage](https://en.wikipedia.org/wiki/Charles_Babbage) per operare sui numeri seguendo una procedura ben definita – un algoritmo. I computer moderni, sebbene significativamente più avanzati rispetto al modello originale proposto nel XIX secolo, seguono ancora la stessa idea di calcoli controllati. È quindi possibile programmare un computer per fare qualcosa se conosciamo esattamente la sequenza di passaggi necessaria per raggiungere l'obiettivo.

![Foto di una persona](images/dsh_age.png)

> Foto di [Vickie Soshnikova](http://twitter.com/vickievalerie)

> ✅ Determinare l’età di una persona da una sua fotografia è un compito che non può essere esplicitamente programmato, perché non sappiamo esattamente come nella nostra mente arriviamo a quel numero.

---

Ci sono però alcuni compiti per i quali non sappiamo esplicitamente come trovare una soluzione. Considera il compito di determinare l'età di una persona da una sua fotografia. Impariamo a farlo perché abbiamo visto molti esempi di persone di età diversa, ma non sappiamo spiegare esattamente come lo facciamo, né possiamo programmare un computer per farlo. Questo è esattamente il tipo di compito che interessa all’**Intelligenza Artificiale** (IA).

✅ Pensa ad alcuni compiti che potresti delegare a un computer e che trarrebbero beneficio dall’uso dell’IA. Considera i campi della finanza, della medicina e dell’arte: come stanno beneficiando oggi di queste tecnologie?

## IA Debole vs. IA Forte

IA Debole | IA Forte
---------------------------------------|-------------------------------------
L'IA debole si riferisce a sistemi progettati e addestrati per svolgere un compito specifico o un insieme ristretto di compiti.|L'IA forte, o Intelligenza Artificiale Generale (AGI), si riferisce a sistemi con intelligenza e comprensione a livello umano.
Questi sistemi non sono generalmente intelligenti; eccellono in un compito predefinito ma mancano di vera comprensione o coscienza.|Questi sistemi sono in grado di svolgere qualsiasi compito intellettuale che un essere umano può fare, adattarsi a diversi ambiti e possedere una forma di coscienza o autoconsapevolezza.
Esempi di IA debole includono assistenti virtuali come Siri o Alexa, algoritmi di raccomandazione usati nei servizi di streaming e chatbot progettati per compiti specifici di assistenza clienti.|Raggiungere l’IA forte è un obiettivo a lungo termine della ricerca sull’intelligenza artificiale e richiederebbe sistemi in grado di ragionare, apprendere, comprendere e adattarsi a una vasta gamma di compiti e contesti.
L’IA debole è altamente specializzata e non possiede capacità cognitive simili a quelle umane né capacità di risoluzione dei problemi generali.|L’IA forte è attualmente un concetto teorico e nessun sistema ha ancora raggiunto questo livello di intelligenza generale.

Per maggiori informazioni, vedi **[Intelligenza Artificiale Generale](https://en.wikipedia.org/wiki/Artificial_general_intelligence)** (AGI).

## La Definizione di Intelligenza e il Test di Turing

Uno dei problemi nel trattare il termine **[Intelligenza](https://en.wikipedia.org/wiki/Intelligence)** è che non esiste una definizione chiara di questo concetto. Si può sostenere che l’intelligenza sia legata al **pensiero astratto** o alla **consapevolezza di sé**, ma non possiamo definirla in modo preciso.

![Foto di un gatto](images/photo-cat.jpg)

> [Foto](https://unsplash.com/photos/75715CVEJhI) di [Amber Kipp](https://unsplash.com/@sadmax) da Unsplash

Per capire l’ambiguità del termine *intelligenza*, prova a rispondere a questa domanda: "Un gatto è intelligente?". Persone diverse tendono a dare risposte diverse, poiché non esiste un test universalmente accettato per dimostrare se l’affermazione sia vera o meno. E se pensi che esista, prova a far fare al tuo gatto un test del QI...

✅ Rifletti per un momento su come definisci l’intelligenza. Un corvo che riesce a risolvere un labirinto per raggiungere del cibo è intelligente? E un bambino?

---

Quando si parla di AGI, è necessario avere un modo per capire se abbiamo davvero creato un sistema intelligente. [Alan Turing](https://en.wikipedia.org/wiki/Alan_Turing) ha proposto un metodo chiamato **[Test di Turing](https://en.wikipedia.org/wiki/Turing_test)**, che funge anche da definizione di intelligenza. Il test confronta un sistema con qualcosa di intrinsecamente intelligente – un essere umano. Poiché qualsiasi confronto automatico può essere aggirato da un programma, si utilizza un interrogatore umano. Se un essere umano non riesce a distinguere tra una persona reale e un sistema informatico in un dialogo testuale, allora il sistema viene considerato intelligente.

> Un chatbot chiamato [Eugene Goostman](https://en.wikipedia.org/wiki/Eugene_Goostman), sviluppato a San Pietroburgo, si è avvicinato al superamento del test di Turing nel 2014 grazie a un espediente ingegnoso: dichiarava fin da subito di essere un ragazzo ucraino di 13 anni, giustificando così eventuali mancanze di conoscenza o discrepanze nel testo. Il bot riuscì a convincere il 30% dei giudici di essere umano dopo un dialogo di 5 minuti, una soglia che Turing riteneva raggiungibile da una macchina entro il 2000. Tuttavia, questo non significa che abbiamo creato un sistema intelligente, né che il computer abbia ingannato l’interrogatore umano – è stato l’ingegno dei creatori del bot a farlo!

✅ Sei mai stato ingannato da un chatbot, credendo di parlare con una persona reale? Come ti ha convinto?

## Approcci Diversi all’IA

Se vogliamo che un computer si comporti come un essere umano, dobbiamo in qualche modo modellare nel computer il nostro modo di pensare. Di conseguenza, dobbiamo cercare di capire cosa rende intelligente un essere umano.

> Per poter programmare l’intelligenza in una macchina, dobbiamo capire come funzionano i nostri stessi processi decisionali. Se fai un po’ di introspezione, ti accorgerai che alcuni processi avvengono inconsciamente – ad esempio possiamo distinguere un gatto da un cane senza pensarci – mentre altri richiedono ragionamento.

Esistono due approcci principali a questo problema:

Approccio Top-Down (Ragionamento Simbolico) | Approccio Bottom-Up (Reti Neurali)
-------------------------------------------|------------------------------------------
Un approccio top-down modella il modo in cui una persona ragiona per risolvere un problema. Comporta l’estrazione della **conoscenza** da un essere umano e la sua rappresentazione in un formato leggibile da un computer. Occorre anche sviluppare un modo per modellare il **ragionamento** all'interno del computer. | Un approccio bottom-up modella la struttura del cervello umano, costituita da un numero enorme di unità semplici chiamate **neuroni**. Ogni neurone agisce come una media ponderata dei suoi input e possiamo addestrare una rete di neuroni a risolvere problemi utili fornendo dei **dati di addestramento**.

Esistono anche altri approcci all’intelligenza:

* Un approccio **emergente**, **sinergico** o **multi-agente** si basa sul fatto che un comportamento intelligente complesso può emergere dall’interazione di un gran numero di agenti semplici. Secondo la [cibernetica evolutiva](https://en.wikipedia.org/wiki/Global_brain#Evolutionary_cybernetics), l’intelligenza può *emergere* da comportamenti semplici e reattivi attraverso un processo di *transizione metasistemica*.

* Un **approccio evolutivo**, o **algoritmo genetico**, è un processo di ottimizzazione basato sui principi dell’evoluzione.

Esamineremo questi approcci più avanti nel corso, ma per ora ci concentreremo su due direzioni principali: top-down e bottom-up.

### L’Approccio Top-Down

Nell’**approccio top-down**, cerchiamo di modellare il nostro ragionamento. Poiché possiamo seguire i nostri pensieri mentre ragioniamo, possiamo cercare di formalizzare questo processo e programmarlo all’interno del computer. Questo è chiamato **ragionamento simbolico**.

Le persone tendono ad avere delle regole mentali che guidano i loro processi decisionali. Ad esempio, quando un medico fa una diagnosi, può rilevare che un paziente ha la febbre e quindi dedurre che ci sia un’infiammazione. Applicando un ampio insieme di regole a un problema specifico, il medico può arrivare a una diagnosi finale.

Questo approccio si basa molto sulla **rappresentazione della conoscenza** e sul **ragionamento**. Estrarre conoscenza da un esperto umano è spesso la parte più difficile, perché un medico, in molti casi, non sa esattamente perché arriva a una certa diagnosi – a volte la soluzione gli viene in mente senza pensarci esplicitamente. Alcuni compiti, come determinare l’età di una persona da una foto, non possono essere ridotti alla semplice manipolazione della conoscenza.

### L’Approccio Bottom-Up

In alternativa, possiamo cercare di modellare gli elementi più semplici del nostro cervello – i neuroni. Possiamo costruire una cosiddetta **rete neurale artificiale** all’interno di un computer e cercare di insegnarle a risolvere problemi fornendole esempi. Questo processo è simile a come un neonato impara a conoscere l’ambiente circostante tramite l’osservazione.

✅ Fai una piccola ricerca su come imparano i bambini. Quali sono gli elementi di base del cervello di un neonato?

> | E il Machine Learning? |      |
> |------------------------|------|
> | Una parte dell’Intelligenza Artificiale basata sull’apprendimento del computer per risolvere un problema a partire da alcuni dati si chiama **Machine Learning**. Non tratteremo il machine learning classico in questo corso – ti rimandiamo al curriculum separato [Machine Learning for Beginners](http://aka.ms/ml-beginners). | ![ML for Beginners](images/ml-for-beginners.png) |

---

## Una breve storia dell’Intelligenza Artificiale

L’Intelligenza Artificiale è nata come disciplina a metà del ventesimo secolo. Inizialmente, l’approccio predominante era quello del **ragionamento simbolico**, che portò a diversi successi importanti, come i sistemi esperti – programmi informatici in grado di agire come esperti in domini di problemi specifici. Tuttavia, presto si capì che questo approccio non era facilmente scalabile. Estrarre la conoscenza da un esperto, rappresentarla in un computer e mantenerla aggiornata si rivelò un compito molto complesso e troppo costoso per essere pratico in molti casi. Questo portò al cosiddetto [inverno dell’IA](https://it.wikipedia.org/wiki/Inverno_dell%27intelligenza_artificiale) negli anni ’70.

<img alt="Brief History of AI" src="images/history-of-ai.png" width="70%"/>

> Immagine di [Dmitry Soshnikov](http://soshnikov.com)

Col passare del tempo, le risorse computazionali sono diventate più economiche e si è resa disponibile una maggiore quantità di dati. Di conseguenza, gli approcci basati su **reti neurali** hanno iniziato a mostrare ottime prestazioni, riuscendo a competere con gli esseri umani in molti ambiti, come la visione artificiale o il riconoscimento vocale. Nell’ultimo decennio, il termine *Intelligenza Artificiale* è stato usato quasi come sinonimo di *reti neurali*, dato che la maggior parte dei successi dell’IA di cui si sente parlare oggi sono basati su di esse.

Possiamo osservare come gli approcci siano cambiati nel tempo, ad esempio nella creazione di un programma per giocare a scacchi:

- I primi programmi per gli scacchi erano basati sulla ricerca – il programma stimava esplicitamente le possibili mosse dell’avversario per un certo numero di turni successivi, e selezionava la mossa ottimale in base alla posizione migliore che si poteva raggiungere. Questo portò allo sviluppo del cosiddetto algoritmo di [potatura alfa-beta](https://it.wikipedia.org/wiki/Potatura_alfa-beta).
- Le strategie di ricerca funzionano bene nella fase finale della partita, dove il numero di mosse possibili è limitato. Tuttavia, all’inizio del gioco, lo spazio di ricerca è enorme e l’algoritmo può essere migliorato imparando dalle partite giocate dagli esseri umani. Esperimenti successivi hanno impiegato il cosiddetto [ragionamento basato sui casi](https://en.wikipedia.org/wiki/Case-based_reasoning), dove il programma cercava situazioni simili nel proprio archivio di conoscenza.
- I programmi moderni che riescono a battere i giocatori umani sono basati su **reti neurali** e **apprendimento per rinforzo** ([reinforcement learning](https://en.wikipedia.org/wiki/Reinforcement_learning)), dove il programma impara a giocare sfidando sé stesso e apprendendo dai propri errori – un processo molto simile a quello degli esseri umani quando imparano a giocare. Tuttavia, un programma può giocare molte più partite in meno tempo e quindi imparare molto più velocemente.

✅ Fai una ricerca su altri giochi in cui l’IA è stata utilizzata con successo.

Allo stesso modo, possiamo vedere come si sia evoluto l’approccio alla creazione di “programmi parlanti” (quelli che potrebbero superare il Test di Turing):

- I primi programmi di questo tipo, come [Eliza](https://en.wikipedia.org/wiki/ELIZA), si basavano su regole grammaticali molto semplici e sulla riformulazione delle frasi in forma di domanda.
- Gli assistenti moderni, come Cortana, Siri o Google Assistant, sono sistemi ibridi che usano **reti neurali** per convertire la voce in testo e riconoscere l’intento, e poi impiegano del ragionamento o algoritmi espliciti per svolgere le azioni richieste.
- In futuro, potremmo aspettarci che l’intero modello di dialogo venga gestito da una rete neurale. Le recenti famiglie di reti neurali come GPT e [Turing-NLG](https://turing.microsoft.com/) hanno dimostrato grandi successi in questo campo.

<img alt="Evoluzione del Test di Turing" src="images/turing-test-evol.png" width="70%"/>

> Immagine di Dmitry Soshnikov, [foto](https://unsplash.com/photos/r8LmVbUKgns) di [Marina Abrosimova](https://unsplash.com/@abrosimova_marina_foto), Unsplash

---

## Ricerche recenti sull’IA

La grande crescita recente nella ricerca sulle reti neurali è iniziata intorno al 2010, quando sono diventati disponibili grandi dataset pubblici. Una vasta collezione di immagini chiamata [ImageNet](https://en.wikipedia.org/wiki/ImageNet), contenente circa 14 milioni di immagini annotate, ha dato il via alla [ImageNet Large Scale Visual Recognition Challenge](https://image-net.org/challenges/LSVRC/).

![Accuratezza ILSVRC](images/ilsvrc.gif)

> Immagine di [Dmitry Soshnikov](http://soshnikov.com)

Nel 2012, le **Reti Neurali Convoluzionali** ([Convolutional Neural Networks](../4-ComputerVision/07-ConvNets/README.md)) furono utilizzate per la prima volta nella classificazione delle immagini, portando a una riduzione significativa degli errori (dal quasi 30% al 16,4%). Nel 2015, l’architettura **ResNet** di Microsoft Research [raggiunse una precisione pari a quella umana](https://doi.org/10.1109/ICCV.2015.123).

Da allora, le reti neurali hanno dimostrato prestazioni molto positive in molti compiti:

---

Anno | Parità con l'essere umano raggiunta
-----|------------------------------------
2015 | [Classificazione di immagini](https://doi.org/10.1109/ICCV.2015.123)  
2016 | [Riconoscimento vocale conversazionale](https://arxiv.org/abs/1610.05256)  
2018 | [Traduzione automatica](https://arxiv.org/abs/1803.05567) (Cinese-Inglese)  
2020 | [Descrizione automatica di immagini](https://arxiv.org/abs/2009.13682)  

---

Negli ultimi anni abbiamo assistito a enormi successi con i **modelli linguistici di grandi dimensioni**, come **BERT** e **GPT-3**. Questo è stato possibile soprattutto grazie alla disponibilità di grandi quantità di dati testuali generali, che hanno permesso di allenare modelli in grado di catturare la struttura e il significato dei testi, pre-addestrarli su grandi collezioni e poi specializzarli per compiti specifici. Parleremo più avanti nel corso di **[Elaborazione del Linguaggio Naturale](../5-NLP/README.md)**.

---

## 🚀 Sfida

Fai un giro su internet per determinare, secondo te, dove l’IA viene utilizzata in modo più efficace. È in un’app di mappatura? In un servizio di conversione vocale? In un videogioco? Fai una ricerca su come è stato costruito quel sistema.

---

## [Quiz post lezione](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/201)

---

## Ripasso e Studio Individuale

Ripassa la storia dell’IA e del Machine Learning leggendo [questa lezione](https://github.com/microsoft/ML-For-Beginners/tree/main/1-Introduction/2-history-of-ML). Scegli un elemento dal disegno riassuntivo in alto a questa lezione (o all’altra) e approfondisci la sua storia e il contesto culturale in cui si è evoluto.

**Compito**: [Game Jam](assignment.md)
