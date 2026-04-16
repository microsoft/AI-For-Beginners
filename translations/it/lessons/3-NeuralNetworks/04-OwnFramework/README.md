# Introduzione alle Reti Neurali. Perceptron Multistrato

Nella sezione precedente, hai imparato il modello di rete neurale più semplice: il perceptron a uno strato, un modello lineare per la classificazione a due classi.

In questa sezione estenderemo questo modello in un framework più flessibile, che ci permetterà di:

* eseguire la **classificazione multi-classe** oltre alla classificazione a due classi
* risolvere problemi di **regressione** oltre alla classificazione
* separare classi che non sono linearmente separabili

Svilupperemo inoltre un framework modulare in Python che ci consentirà di costruire diverse architetture di reti neurali.

## [Quiz pre-lezione](https://ff-quizzes.netlify.app/en/ai/quiz/7)

## Formalizzazione del Machine Learning

Iniziamo formalizzando il problema del Machine Learning. Supponiamo di avere un dataset di addestramento **X** con etichette **Y**, e dobbiamo costruire un modello *f* che produca previsioni il più accurate possibile. La qualità delle previsioni viene misurata tramite la **funzione di perdita** &lagran;. Le seguenti funzioni di perdita sono spesso utilizzate:

* Per problemi di regressione, quando dobbiamo prevedere un numero, possiamo usare l'**errore assoluto** &sum;<sub>i</sub>|f(x<sup>(i)</sup>)-y<sup>(i)</sup>|, o l'**errore quadratico** &sum;<sub>i</sub>(f(x<sup>(i)</sup>)-y<sup>(i)</sup>)<sup>2</sup>
* Per la classificazione, utilizziamo la **perdita 0-1** (che è essenzialmente la stessa cosa dell'**accuratezza** del modello), o la **perdita logistica**.

Per il perceptron a uno strato, la funzione *f* era definita come una funzione lineare *f(x)=wx+b* (qui *w* è la matrice dei pesi, *x* è il vettore delle caratteristiche di input, e *b* è il vettore di bias). Per diverse architetture di reti neurali, questa funzione può assumere una forma più complessa.

> Nel caso della classificazione, spesso è desiderabile ottenere le probabilità delle classi corrispondenti come output della rete. Per convertire numeri arbitrari in probabilità (ad esempio per normalizzare l'output), utilizziamo spesso la funzione **softmax** &sigma;, e la funzione *f* diventa *f(x)=&sigma;(wx+b)*

Nella definizione di *f* sopra, *w* e *b* sono chiamati **parametri** &theta;=⟨*w,b*⟩. Dato il dataset ⟨**X**,**Y**⟩, possiamo calcolare un errore complessivo sull'intero dataset come funzione dei parametri &theta;.

> ✅ **L'obiettivo dell'addestramento della rete neurale è minimizzare l'errore variando i parametri &theta;**

## Ottimizzazione con Discesa del Gradiente

Esiste un metodo noto per l'ottimizzazione delle funzioni chiamato **discesa del gradiente**. L'idea è che possiamo calcolare una derivata (nel caso multidimensionale chiamata **gradiente**) della funzione di perdita rispetto ai parametri, e variare i parametri in modo tale che l'errore diminuisca. Questo può essere formalizzato come segue:

* Inizializzare i parametri con alcuni valori casuali w<sup>(0)</sup>, b<sup>(0)</sup>
* Ripetere il seguente passo molte volte:
    - w<sup>(i+1)</sup> = w<sup>(i)</sup>-&eta;&part;&lagran;/&part;w
    - b<sup>(i+1)</sup> = b<sup>(i)</sup>-&eta;&part;&lagran;/&part;b

Durante l'addestramento, i passi di ottimizzazione dovrebbero essere calcolati considerando l'intero dataset (ricorda che la perdita viene calcolata come somma su tutti i campioni di addestramento). Tuttavia, nella pratica prendiamo piccole porzioni del dataset chiamate **minibatch**, e calcoliamo i gradienti basandoci su un sottoinsieme di dati. Poiché il sottoinsieme viene scelto casualmente ogni volta, tale metodo è chiamato **discesa del gradiente stocastica** (SGD).

## Perceptron Multistrato e Backpropagation

La rete a uno strato, come abbiamo visto sopra, è in grado di classificare classi linearmente separabili. Per costruire un modello più ricco, possiamo combinare diversi strati della rete. Matematicamente ciò significherebbe che la funzione *f* avrebbe una forma più complessa e verrebbe calcolata in diversi passaggi:
* z<sub>1</sub>=w<sub>1</sub>x+b<sub>1</sub>
* z<sub>2</sub>=w<sub>2</sub>&alpha;(z<sub>1</sub>)+b<sub>2</sub>
* f = &sigma;(z<sub>2</sub>)

Qui, &alpha; è una **funzione di attivazione non lineare**, &sigma; è una funzione softmax, e i parametri &theta;=<*w<sub>1</sub>,b<sub>1</sub>,w<sub>2</sub>,b<sub>2</sub>*>.

L'algoritmo di discesa del gradiente rimarrebbe lo stesso, ma sarebbe più difficile calcolare i gradienti. Dato il principio della derivazione a catena, possiamo calcolare le derivate come:

* &part;&lagran;/&part;w<sub>2</sub> = (&part;&lagran;/&part;&sigma;)(&part;&sigma;/&part;z<sub>2</sub>)(&part;z<sub>2</sub>/&part;w<sub>2</sub>)
* &part;&lagran;/&part;w<sub>1</sub> = (&part;&lagran;/&part;&sigma;)(&part;&sigma;/&part;z<sub>2</sub>)(&part;z<sub>2</sub>/&part;&alpha;)(&part;&alpha;/&part;z<sub>1</sub>)(&part;z<sub>1</sub>/&part;w<sub>1</sub>)

> ✅ Il principio della derivazione a catena viene utilizzato per calcolare le derivate della funzione di perdita rispetto ai parametri.

Nota che la parte più a sinistra di tutte queste espressioni è la stessa, e quindi possiamo calcolare efficacemente le derivate partendo dalla funzione di perdita e andando "indietro" attraverso il grafo computazionale. Pertanto, il metodo di addestramento di un perceptron multistrato è chiamato **backpropagation**, o 'backprop'.

<img alt="compute graph" src="../../../../../translated_images/it/ComputeGraphGrad.4626252c0de03507.webp"/>

> TODO: citazione immagine

> ✅ Approfondiremo il backpropagation in modo molto più dettagliato nel nostro esempio nel notebook.  

## Conclusione

In questa lezione, abbiamo costruito la nostra libreria di reti neurali e l'abbiamo utilizzata per un semplice compito di classificazione bidimensionale.

## 🚀 Sfida

Nel notebook allegato, implementerai il tuo framework per costruire e addestrare perceptron multistrato. Potrai vedere in dettaglio come operano le reti neurali moderne.

Procedi al notebook [OwnFramework](OwnFramework.ipynb) e segui le istruzioni.

## [Quiz post-lezione](https://ff-quizzes.netlify.app/en/ai/quiz/8)

## Revisione e Studio Autonomo

Il backpropagation è un algoritmo comune utilizzato in AI e ML, vale la pena studiarlo [in modo più approfondito](https://wikipedia.org/wiki/Backpropagation)

## [Compito](lab/README.md)

In questo laboratorio, ti viene chiesto di utilizzare il framework che hai costruito in questa lezione per risolvere la classificazione delle cifre scritte a mano del dataset MNIST.

* [Istruzioni](lab/README.md)
* [Notebook](lab/MyFW_MNIST.ipynb)

---

