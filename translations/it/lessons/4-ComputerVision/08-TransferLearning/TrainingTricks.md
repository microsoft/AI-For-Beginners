# Trucchi per l'addestramento del Deep Learning

Man mano che le reti neurali diventano più profonde, il processo del loro addestramento diventa sempre più impegnativo. Un problema principale sono i cosiddetti [gradienti che scompaiono](https://en.wikipedia.org/wiki/Vanishing_gradient_problem) o [gradienti che esplodono](https://deepai.org/machine-learning-glossary-and-terms/exploding-gradient-problem#:~:text=Exploding%20gradients%20are%20a%20problem,updates%20are%20small%20and%20controlled.). [Questo post](https://towardsdatascience.com/the-vanishing-exploding-gradient-problem-in-deep-neural-networks-191358470c11) fornisce una buona introduzione a questi problemi.

Per rendere l'addestramento delle reti profonde più efficiente, ci sono alcune tecniche che possono essere utilizzate.

## Mantenere i valori in un intervallo ragionevole

Per rendere i calcoli numerici più stabili, vogliamo assicurarci che tutti i valori all'interno della nostra rete neurale siano in una scala ragionevole, tipicamente [-1..1] o [0..1]. Non è un requisito molto rigido, ma la natura dei calcoli in virgola mobile è tale che valori di magnitudini diverse non possono essere manipolati accuratamente insieme. Ad esempio, se sommiamo 10<sup>-10</sup> e 10<sup>10</sup>, probabilmente otteniamo 10<sup>10</sup>, perché il valore più piccolo verrebbe "convertito" allo stesso ordine di grandezza di quello più grande, e quindi la mantissa andrebbe persa.

La maggior parte delle funzioni di attivazione ha non linearità attorno a [-1..1], quindi ha senso scalare tutti i dati di input nell'intervallo [-1..1] o [0..1].

## Inizializzazione dei pesi

Idealmente, vogliamo che i valori siano nello stesso intervallo dopo essere passati attraverso gli strati della rete. Pertanto è importante inizializzare i pesi in modo da preservare la distribuzione dei valori.

La distribuzione normale **N(0,1)** non è una buona idea, perché se abbiamo *n* input, la deviazione standard dell'output sarebbe *&radic;n*, e i valori probabilmente usciranno dall'intervallo [0..1].

Le seguenti inizializzazioni sono spesso utilizzate:

 * Distribuzione uniforme -- `uniform`
 * **N(0,1/n)** -- `gaussian`
 * **N(0,1/&radic;n_in)** garantisce che per input con media zero e deviazione standard 1 rimangano la stessa media e deviazione standard
 * **N(0,&radic;2/(n_in+n_out))** -- cosiddetta **inizializzazione Xavier** (`glorot`), aiuta a mantenere i segnali nell'intervallo sia durante la propagazione in avanti che in quella all'indietro

## Batch Normalization

Anche con una corretta inizializzazione dei pesi, i pesi possono diventare arbitrariamente grandi o piccoli durante l'addestramento, e spingeranno i segnali fuori dal corretto intervallo. Possiamo riportare i segnali nell'intervallo usando una delle tecniche di **normalizzazione**. Sebbene ne esistano diverse (normalizzazione dei pesi, normalizzazione dei livelli), quella più usata è la Batch Normalization.

L'idea della **batch normalization** è di prendere in considerazione tutti i valori nel minibatch e di effettuare la normalizzazione (cioè sottrarre la media e dividere per la deviazione standard) basandosi su quei valori. Viene implementata come uno strato di rete che esegue questa normalizzazione dopo aver applicato i pesi, ma prima della funzione di attivazione. Di conseguenza, è probabile vedere una maggiore accuratezza finale e un addestramento più veloce.

Ecco il [documento originale](https://arxiv.org/pdf/1502.03167.pdf) sulla batch normalization, la [spiegazione su Wikipedia](https://en.wikipedia.org/wiki/Batch_normalization) e [un buon post introduttivo su un blog](https://towardsdatascience.com/batch-normalization-in-3-levels-of-understanding-14c2da90a338) (e uno [in russo](https://habrahabr.ru/post/309302/)).

## Dropout

Il **dropout** è una tecnica interessante che rimuove una certa percentuale di neuroni casuali durante l'addestramento. Anch'esso è implementato come uno strato con un parametro (percentuale dei neuroni da rimuovere, tipicamente 10%-50%), e durante l'addestramento azzera elementi casuali del vettore di input, prima di passarli allo strato successivo.

Sebbene possa sembrare un'idea strana, puoi osservare l'effetto del dropout nell'addestramento di un classificatore di cifre MNIST nel notebook [`Dropout.ipynb`](Dropout.ipynb). Velocizza l'addestramento e ci permette di ottenere maggiore accuratezza in meno epoche.

Questo effetto può essere spiegato in diversi modi:

 * Può essere considerato un fattore casuale di shock per il modello, che lo porta fuori da minimi locali
 * Può essere considerato un *averaging implicito del modello*, perché durante il dropout si sta addestrando un modello leggermente diverso

> *Alcune persone dicono che quando una persona ubriaca cerca di imparare qualcosa, se lo ricorderà meglio la mattina dopo rispetto a una persona sobria, perché un cervello con alcuni neuroni malfunzionanti tenta di adattarsi meglio a cogliere il significato. Noi stessi non abbiamo mai testato se questo sia vero o meno*

## Prevenire l'overfitting

Uno degli aspetti molto importanti del deep learning è riuscire a prevenire l'[overfitting](../../3-NeuralNetworks/05-Frameworks/Overfitting.md). Sebbene possa risultare allettante usare un modello di rete neurale molto potente, dovremmo sempre bilanciare il numero di parametri del modello con il numero di campioni di addestramento.

> Assicurati di comprendere il concetto di [overfitting](../../3-NeuralNetworks/05-Frameworks/Overfitting.md) che abbiamo introdotto prima!

Ci sono diversi modi per prevenire l'overfitting:

 * Early stopping -- monitorare continuamente l'errore sul set di validazione e interrompere l'addestramento quando l'errore di validazione inizia ad aumentare.
 * Decadimento esplicito dei pesi / regolarizzazione -- aggiungere una penalità extra alla funzione di perdita per i valori assoluti elevati dei pesi, che impedisce al modello di generare risultati molto instabili
 * Media del modello -- addestrare diversi modelli e poi fare la media dei risultati. Questo aiuta a minimizzare la varianza.
 * Dropout (media implicita del modello)

## Ottimizzatori / Algoritmi di addestramento

Un altro aspetto importante dell'addestramento è scegliere un buon algoritmo di addestramento. Sebbene la classica **discesa del gradiente** sia una scelta ragionevole, a volte può essere troppo lenta o causare altri problemi.

Nel deep learning, utilizziamo la **discesa del gradiente stocastica** (SGD), che è una discesa del gradiente applicata ai minibatch, selezionati casualmente dal set di addestramento. I pesi vengono aggiornati usando questa formula:

w<sup>t+1</sup> = w<sup>t</sup> - &eta;&nabla;&lagran;

### Momentum

Nella **momentum SGD**, manteniamo una porzione del gradiente dei passi precedenti. È simile a quando ci muoviamo con inerzia, e riceviamo un colpo in una direzione diversa, la nostra traiettoria non cambia immediatamente, ma mantiene parte del movimento originale. Qui introduciamo un altro vettore v per rappresentare la *velocità*:

* v<sup>t+1</sup> = &gamma; v<sup>t</sup> - &eta;&nabla;&lagran;
* w<sup>t+1</sup> = w<sup>t</sup>+v<sup>t+1</sup>

Qui il parametro &gamma; indica in quale misura teniamo conto dell'inerzia: &gamma;=0 corrisponde alla classica SGD; &gamma;=1 è una pura equazione di moto.

### Adam, Adagrad, ecc.

Poiché in ogni livello moltiplichiamo i segnali per una matrice W<sub>i</sub>, a seconda di ||W<sub>i</sub>||, il gradiente può diminuire fino a essere vicino a zero, o crescere indefinitamente. Questa è l'essenza del problema dei gradienti che esplodono/scompaiono.

Una delle soluzioni a questo problema è utilizzare solo la direzione del gradiente nell'equazione, ignorando il valore assoluto, cioè

w<sup>t+1</sup> = w<sup>t</sup> - &eta;(&nabla;&lagran;/||&nabla;&lagran;||), dove ||&nabla;&lagran;|| = &radic;&sum;(&nabla;&lagran;)<sup>2</sup>

Questo algoritmo si chiama **Adagrad**. Altri algoritmi che usano la stessa idea sono: **RMSProp**, **Adam**

> **Adam** è considerato un algoritmo molto efficiente per molte applicazioni, quindi se non sei sicuro quale usare - usa Adam.

### Clipping del gradiente

Il clipping del gradiente è un'estensione dell'idea di cui sopra. Quando ||&nabla;&lagran;|| &le; &theta;, consideriamo il gradiente originale nell'ottimizzazione del peso, e quando ||&nabla;&lagran;|| > &theta; - dividiamo il gradiente per la sua norma. Qui &theta; è un parametro, nella maggior parte dei casi possiamo prendere &theta;=1 o &theta;=10.

### Decadimento del tasso di apprendimento

Il successo dell'addestramento spesso dipende dal parametro del tasso di apprendimento &eta;. È logico assumere che valori più grandi di &eta; risultino in un addestramento più veloce, cosa che di solito vogliamo all'inizio dell'addestramento, e poi valori più piccoli di &eta; ci permettono di perfezionare la rete. Quindi, nella maggior parte dei casi vogliamo ridurre &eta; durante il processo di addestramento.

Questo può essere fatto moltiplicando &eta; per qualche numero (ad es. 0.98) dopo ogni epoca di addestramento, o usando un **programma di decay del tasso di apprendimento** più complesso.

## Diverse architetture di rete

Selezionare l'architettura di rete giusta per il tuo problema può essere complicato. Normalmente, prenderemmo un'architettura che ha dimostrato di funzionare per il nostro specifico compito (o uno simile). Ecco una [buona panoramica](https://www.topbots.com/a-brief-history-of-neural-network-architectures/) delle architetture di reti neurali per la visione artificiale.

> È importante selezionare un'architettura che sia sufficientemente potente per il numero di campioni di addestramento che abbiamo. Scegliere un modello troppo potente può portare a [overfitting](../../3-NeuralNetworks/05-Frameworks/Overfitting.md)

Un altro buon modo è usare un'architettura che si adatti automaticamente alla complessità richiesta. In qualche misura, le architetture **ResNet** e **Inception** sono auto-regolanti. [Ulteriori dettagli sulle architetture per la visione artificiale](../07-ConvNets/CNN_Architectures.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Questo documento è stato tradotto utilizzando il servizio di traduzione AI [Co-op Translator](https://github.com/Azure/co-op-translator). Sebbene ci impegniamo per garantire la precisione, si prega di notare che le traduzioni automatizzate possono contenere errori o imprecisioni. Il documento originale nella sua lingua nativa deve essere considerato la fonte autorevole. Per informazioni critiche, si raccomanda una traduzione professionale effettuata da un essere umano. Non siamo responsabili per eventuali malintesi o interpretazioni errate derivanti dall’uso di questa traduzione.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->