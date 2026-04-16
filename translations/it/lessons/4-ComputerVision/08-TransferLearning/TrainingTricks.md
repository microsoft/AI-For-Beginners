# Trucchi per l'Addestramento del Deep Learning

Man mano che le reti neurali diventano più profonde, il processo di addestramento diventa sempre più complesso. Uno dei principali problemi è il cosiddetto [vanishing gradients](https://en.wikipedia.org/wiki/Vanishing_gradient_problem) o [exploding gradients](https://deepai.org/machine-learning-glossary-and-terms/exploding-gradient-problem#:~:text=Exploding%20gradients%20are%20a%20problem,updates%20are%20small%20and%20controlled.). [Questo post](https://towardsdatascience.com/the-vanishing-exploding-gradient-problem-in-deep-neural-networks-191358470c11) offre una buona introduzione a questi problemi.

Per rendere l'addestramento delle reti profonde più efficiente, ci sono alcune tecniche che possono essere utilizzate.

## Mantenere i valori in un intervallo ragionevole

Per rendere i calcoli numerici più stabili, è importante assicurarsi che tutti i valori all'interno della rete neurale siano in una scala ragionevole, tipicamente [-1..1] o [0..1]. Non è un requisito molto rigido, ma la natura dei calcoli in virgola mobile è tale che valori di magnitudini diverse non possono essere manipolati accuratamente insieme. Ad esempio, se sommiamo 10<sup>-10</sup> e 10<sup>10</sup>, è probabile che otteniamo 10<sup>10</sup>, poiché il valore più piccolo verrebbe "convertito" allo stesso ordine di grandezza del più grande, perdendo così la mantissa.

La maggior parte delle funzioni di attivazione presenta non-linearità intorno a [-1..1], e quindi ha senso scalare tutti i dati di input nell'intervallo [-1..1] o [0..1].

## Inizializzazione dei Pesi

Idealmente, vogliamo che i valori rimangano nello stesso intervallo dopo essere passati attraverso i livelli della rete. Pertanto, è importante inizializzare i pesi in modo da preservare la distribuzione dei valori.

La distribuzione normale **N(0,1)** non è una buona idea, perché se abbiamo *n* input, la deviazione standard dell'output sarebbe *n*, e i valori potrebbero uscire dall'intervallo [0..1].

Le seguenti inizializzazioni sono spesso utilizzate:

 * Distribuzione uniforme -- `uniform`
 * **N(0,1/n)** -- `gaussian`
 * **N(0,1/√n_in)** garantisce che per input con media zero e deviazione standard di 1, la stessa media/deviazione standard rimanga
 * **N(0,√2/(n_in+n_out))** -- la cosiddetta **Xavier initialization** (`glorot`), aiuta a mantenere i segnali nell'intervallo sia durante la propagazione in avanti che quella all'indietro

## Batch Normalization

Anche con una corretta inizializzazione dei pesi, questi possono diventare arbitrariamente grandi o piccoli durante l'addestramento, portando i segnali fuori dal range corretto. Possiamo riportare i segnali nel range corretto utilizzando una delle tecniche di **normalizzazione**. Sebbene ce ne siano diverse (Weight Normalization, Layer Normalization), la più utilizzata è la Batch Normalization.

L'idea della **batch normalization** è di considerare tutti i valori all'interno del minibatch e di eseguire la normalizzazione (cioè sottrarre la media e dividere per la deviazione standard) basandosi su quei valori. È implementata come un livello della rete che esegue questa normalizzazione dopo l'applicazione dei pesi, ma prima della funzione di attivazione. Il risultato è una maggiore accuratezza finale e un addestramento più veloce.

Ecco il [paper originale](https://arxiv.org/pdf/1502.03167.pdf) sulla batch normalization, la [spiegazione su Wikipedia](https://en.wikipedia.org/wiki/Batch_normalization), e [un buon post introduttivo](https://towardsdatascience.com/batch-normalization-in-3-levels-of-understanding-14c2da90a338) (e uno [in russo](https://habrahabr.ru/post/309302/)).

## Dropout

**Dropout** è una tecnica interessante che rimuove una certa percentuale di neuroni casuali durante l'addestramento. È implementata come un livello con un parametro (percentuale di neuroni da rimuovere, tipicamente 10%-50%), e durante l'addestramento azzera elementi casuali del vettore di input, prima di passarli al livello successivo.

Anche se può sembrare un'idea strana, puoi vedere l'effetto del dropout sull'addestramento di un classificatore di cifre MNIST nel notebook [`Dropout.ipynb`](../../../../../lessons/4-ComputerVision/08-TransferLearning/Dropout.ipynb). Accelera l'addestramento e consente di ottenere una maggiore accuratezza in meno epoche di addestramento.

Questo effetto può essere spiegato in diversi modi:

 * Può essere considerato come un fattore di shock casuale per il modello, che lo porta fuori da un minimo locale
 * Può essere considerato come *implicit model averaging*, perché durante il dropout stiamo addestrando un modello leggermente diverso

> *Alcune persone dicono che quando una persona ubriaca cerca di imparare qualcosa, la ricorderà meglio il giorno dopo rispetto a una persona sobria, perché un cervello con alcuni neuroni malfunzionanti cerca di adattarsi meglio per afferrare il significato. Non abbiamo mai testato personalmente se questo sia vero o meno.*

## Prevenire l'Overfitting

Uno degli aspetti molto importanti del deep learning è la capacità di prevenire l'[overfitting](../../3-NeuralNetworks/05-Frameworks/Overfitting.md). Anche se potrebbe essere allettante utilizzare un modello di rete neurale molto potente, dovremmo sempre bilanciare il numero di parametri del modello con il numero di campioni di addestramento.

> Assicurati di comprendere il concetto di [overfitting](../../3-NeuralNetworks/05-Frameworks/Overfitting.md) che abbiamo introdotto in precedenza!

Ci sono diversi modi per prevenire l'overfitting:

 * Early stopping -- monitorare continuamente l'errore sul set di validazione e interrompere l'addestramento quando l'errore di validazione inizia ad aumentare.
 * Decadimento esplicito dei pesi / Regularizzazione -- aggiungere una penalità extra alla funzione di perdita per valori assoluti elevati dei pesi, prevenendo risultati molto instabili
 * Media del modello -- addestrare diversi modelli e poi mediare il risultato. Questo aiuta a minimizzare la varianza.
 * Dropout (Implicit Model Averaging)

## Ottimizzatori / Algoritmi di Addestramento

Un altro aspetto importante dell'addestramento è scegliere un buon algoritmo di addestramento. Sebbene il classico **gradient descent** sia una scelta ragionevole, a volte può essere troppo lento o causare altri problemi.

Nel deep learning, utilizziamo **Stochastic Gradient Descent** (SGD), che è un gradient descent applicato a minibatch selezionati casualmente dal set di addestramento. I pesi vengono aggiornati utilizzando questa formula:

w<sup>t+1</sup> = w<sup>t</sup> - η∇ℒ

### Momentum

Nel **momentum SGD**, manteniamo una parte del gradiente dei passaggi precedenti. È simile a quando ci muoviamo con inerzia e riceviamo un colpo in una direzione diversa: la nostra traiettoria non cambia immediatamente, ma conserva una parte del movimento originale. Qui introduciamo un altro vettore v per rappresentare la *velocità*:

* v<sup>t+1</sup> = γ v<sup>t</sup> - η∇ℒ
* w<sup>t+1</sup> = w<sup>t</sup>+v<sup>t+1</sup>

Il parametro γ indica quanto teniamo conto dell'inerzia: γ=0 corrisponde al classico SGD; γ=1 è un'equazione di puro movimento.

### Adam, Adagrad, ecc.

Poiché in ogni livello moltiplichiamo i segnali per una matrice W<sub>i</sub>, a seconda di ||W<sub>i</sub>||, il gradiente può diminuire e avvicinarsi a 0, oppure crescere indefinitamente. Questo è il cuore del problema degli Exploding/Vanishing Gradients.

Una delle soluzioni a questo problema è utilizzare solo la direzione del gradiente nell'equazione, ignorando il valore assoluto, cioè:

w<sup>t+1</sup> = w<sup>t</sup> - η(∇ℒ/||∇ℒ||), dove ||∇ℒ|| = √∑(∇ℒ)<sup>2</sup>

Questo algoritmo è chiamato **Adagrad**. Altri algoritmi che utilizzano la stessa idea: **RMSProp**, **Adam**

> **Adam** è considerato un algoritmo molto efficiente per molte applicazioni, quindi se non sei sicuro di quale utilizzare, scegli Adam.

### Gradient clipping

Il gradient clipping è un'estensione dell'idea sopra. Quando ||∇ℒ|| ≤ θ, consideriamo il gradiente originale nell'ottimizzazione dei pesi, e quando ||∇ℒ|| > θ - dividiamo il gradiente per la sua norma. Qui θ è un parametro, nella maggior parte dei casi possiamo prendere θ=1 o θ=10.

### Decadimento del learning rate

Il successo dell'addestramento dipende spesso dal parametro learning rate η. È logico supporre che valori più grandi di η portino a un addestramento più veloce, che è qualcosa che tipicamente vogliamo all'inizio dell'addestramento, e poi valori più piccoli di η ci permettano di affinare la rete. Pertanto, nella maggior parte dei casi vogliamo diminuire η durante il processo di addestramento.

Questo può essere fatto moltiplicando η per un numero (es. 0.98) dopo ogni epoca di addestramento, o utilizzando un **learning rate schedule** più complicato.

## Diverse Architetture di Rete

Selezionare l'architettura di rete giusta per il tuo problema può essere complicato. Normalmente, sceglieremmo un'architettura che ha dimostrato di funzionare per il nostro compito specifico (o uno simile). Ecco una [buona panoramica](https://www.topbots.com/a-brief-history-of-neural-network-architectures/) delle architetture di reti neurali per la visione artificiale.

> È importante selezionare un'architettura che sia abbastanza potente per il numero di campioni di addestramento che abbiamo. Scegliere un modello troppo potente può portare all'[overfitting](../../3-NeuralNetworks/05-Frameworks/Overfitting.md).

Un altro buon approccio potrebbe essere utilizzare un'architettura che si adatti automaticamente alla complessità richiesta. In una certa misura, l'architettura **ResNet** e **Inception** sono auto-adattanti. [Maggiori informazioni sulle architetture per la visione artificiale](../07-ConvNets/CNN_Architectures.md).

**Disclaimer**:  
Questo documento è stato tradotto utilizzando il servizio di traduzione automatica [Co-op Translator](https://github.com/Azure/co-op-translator). Sebbene ci impegniamo per garantire l'accuratezza, si prega di notare che le traduzioni automatiche potrebbero contenere errori o imprecisioni. Il documento originale nella sua lingua nativa dovrebbe essere considerato la fonte autorevole. Per informazioni critiche, si raccomanda una traduzione professionale effettuata da un traduttore umano. Non siamo responsabili per eventuali incomprensioni o interpretazioni errate derivanti dall'uso di questa traduzione.