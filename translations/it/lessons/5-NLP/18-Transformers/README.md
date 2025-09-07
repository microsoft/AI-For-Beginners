<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "7e617f0b8de85a43957a853aba09bfeb",
  "translation_date": "2025-08-26T08:39:25+00:00",
  "source_file": "lessons/5-NLP/18-Transformers/README.md",
  "language_code": "it"
}
-->
# Meccanismi di Attenzione e Trasformatori

## [Quiz pre-lezione](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/118)

Uno dei problemi più importanti nel campo dell'elaborazione del linguaggio naturale (NLP) è la **traduzione automatica**, un compito essenziale alla base di strumenti come Google Translate. In questa sezione ci concentreremo sulla traduzione automatica o, più in generale, su qualsiasi compito di *sequence-to-sequence* (chiamato anche **trasduzione di frasi**).

Con le RNN, il sequence-to-sequence viene implementato da due reti ricorrenti, dove una rete, l'**encoder**, comprime una sequenza di input in uno stato nascosto, mentre un'altra rete, il **decoder**, espande questo stato nascosto in un risultato tradotto. Ci sono alcuni problemi con questo approccio:

* Lo stato finale della rete encoder ha difficoltà a ricordare l'inizio di una frase, causando una scarsa qualità del modello per frasi lunghe.
* Tutte le parole in una sequenza hanno lo stesso impatto sul risultato. In realtà, però, alcune parole nella sequenza di input hanno spesso un impatto maggiore sugli output sequenziali rispetto ad altre.

I **Meccanismi di Attenzione** forniscono un mezzo per pesare l'impatto contestuale di ciascun vettore di input su ciascuna previsione di output della RNN. Questo viene implementato creando collegamenti diretti tra gli stati intermedi della RNN di input e la RNN di output. In questo modo, quando si genera il simbolo di output y<sub>t</sub>, si tengono in considerazione tutti gli stati nascosti di input h<sub>i</sub>, con diversi coefficienti di peso α<sub>t,i</sub>.

![Immagine che mostra un modello encoder/decoder con uno strato di attenzione additiva](../../../../../translated_images/encoder-decoder-attention.7a726296894fb567aa2898c94b17b3289087f6705c11907df8301df9e5eeb3de.it.png)

> Modello encoder-decoder con meccanismo di attenzione additiva in [Bahdanau et al., 2015](https://arxiv.org/pdf/1409.0473.pdf), citato da [questo blog post](https://lilianweng.github.io/lil-log/2018/06/24/attention-attention.html)

La matrice di attenzione {α<sub>i,j</sub>} rappresenta il grado in cui determinate parole di input influenzano la generazione di una determinata parola nella sequenza di output. Di seguito è riportato un esempio di tale matrice:

![Immagine che mostra un allineamento campione trovato da RNNsearch-50, tratto da Bahdanau - arviz.org](../../../../../translated_images/bahdanau-fig3.09ba2d37f202a6af11de6c82d2d197830ba5f4528d9ea430eb65fd3a75065973.it.png)

> Figura da [Bahdanau et al., 2015](https://arxiv.org/pdf/1409.0473.pdf) (Fig.3)

I meccanismi di attenzione sono responsabili di gran parte dello stato dell'arte attuale o quasi attuale nell'NLP. Tuttavia, aggiungere l'attenzione aumenta notevolmente il numero di parametri del modello, il che ha portato a problemi di scalabilità con le RNN. Una delle principali limitazioni nello scalare le RNN è che la natura ricorrente dei modelli rende difficile il batch e la parallelizzazione dell'addestramento. In una RNN, ogni elemento di una sequenza deve essere elaborato in ordine sequenziale, il che significa che non può essere facilmente parallelizzato.

![Encoder Decoder con Attenzione](../../../../../lessons/5-NLP/18-Transformers/images/EncDecAttention.gif)

> Figura dal [Blog di Google](https://research.googleblog.com/2016/09/a-neural-network-for-machine.html)

L'adozione dei meccanismi di attenzione combinata con questa limitazione ha portato alla creazione dei modelli Transformer, ora lo stato dell'arte, che conosciamo e utilizziamo oggi, come BERT e Open-GPT3.

## Modelli Transformer

Una delle idee principali dietro i transformer è evitare la natura sequenziale delle RNN e creare un modello parallelizzabile durante l'addestramento. Questo viene ottenuto implementando due idee:

* codifica posizionale
* utilizzo del meccanismo di auto-attenzione per catturare i pattern invece delle RNN (o CNN) (ecco perché l'articolo che introduce i transformer si chiama *[Attention is all you need](https://arxiv.org/abs/1706.03762)*)

### Codifica/Embedding Posizionale

L'idea della codifica posizionale è la seguente.  
1. Quando si utilizzano le RNN, la posizione relativa dei token è rappresentata dal numero di passi, e quindi non deve essere rappresentata esplicitamente.  
2. Tuttavia, passando all'attenzione, è necessario conoscere le posizioni relative dei token all'interno di una sequenza.  
3. Per ottenere la codifica posizionale, si arricchisce la sequenza di token con una sequenza di posizioni dei token nella sequenza (cioè una sequenza di numeri 0,1, ...).  
4. Si mescola quindi la posizione del token con un vettore di embedding del token. Per trasformare la posizione (intero) in un vettore, si possono utilizzare diversi approcci:

* Embedding addestrabile, simile all'embedding dei token. Questo è l'approccio considerato qui. Si applicano livelli di embedding sia ai token che alle loro posizioni, ottenendo vettori di embedding delle stesse dimensioni, che vengono poi sommati.
* Funzione di codifica posizionale fissa, come proposto nell'articolo originale.

<img src="images/pos-embedding.png" width="50%"/>

> Immagine dell'autore

Il risultato ottenuto con l'embedding posizionale incorpora sia il token originale che la sua posizione all'interno di una sequenza.

### Auto-Attenzione Multi-Testa

Successivamente, è necessario catturare alcuni pattern all'interno della sequenza. Per fare ciò, i transformer utilizzano un meccanismo di **auto-attenzione**, che è essenzialmente l'attenzione applicata alla stessa sequenza sia come input che come output. Applicare l'auto-attenzione consente di tenere conto del **contesto** all'interno della frase e di vedere quali parole sono interconnesse. Ad esempio, permette di vedere a quali parole si riferiscono i coreferenti, come *esso*, e di considerare il contesto:

![](../../../../../translated_images/CoreferenceResolution.861924d6d384a7d68d8d0039d06a71a151f18a796b8b1330239d3590bd4947eb.it.png)

> Immagine dal [Blog di Google](https://research.googleblog.com/2017/08/transformer-novel-neural-network.html)

Nei transformer, si utilizza l'**attenzione multi-testa** per dare alla rete la capacità di catturare diversi tipi di dipendenze, ad esempio relazioni tra parole a lungo termine vs. breve termine, coreferenze vs. altro, ecc.

[Notebook TensorFlow](../../../../../lessons/5-NLP/18-Transformers/TransformersTF.ipynb) contiene maggiori dettagli sull'implementazione dei livelli transformer.

### Attenzione Encoder-Decoder

Nei transformer, l'attenzione viene utilizzata in due punti:

* Per catturare i pattern all'interno del testo di input utilizzando l'auto-attenzione.
* Per eseguire la traduzione di sequenze - è il livello di attenzione tra encoder e decoder.

L'attenzione encoder-decoder è molto simile al meccanismo di attenzione utilizzato nelle RNN, come descritto all'inizio di questa sezione. Questo diagramma animato spiega il ruolo dell'attenzione encoder-decoder.

![GIF animata che mostra come vengono eseguite le valutazioni nei modelli transformer.](../../../../../lessons/5-NLP/18-Transformers/images/transformer-animated-explanation.gif)

Poiché ogni posizione di input viene mappata indipendentemente a ciascuna posizione di output, i transformer possono parallelizzare meglio rispetto alle RNN, il che consente modelli linguistici molto più grandi ed espressivi. Ogni testa di attenzione può essere utilizzata per apprendere diverse relazioni tra parole, migliorando i compiti di elaborazione del linguaggio naturale a valle.

## BERT

**BERT** (Bidirectional Encoder Representations from Transformers) è una rete transformer multi-strato molto grande con 12 livelli per *BERT-base* e 24 per *BERT-large*. Il modello viene prima pre-addestrato su un ampio corpus di dati testuali (Wikipedia + libri) utilizzando un addestramento non supervisionato (predizione di parole mascherate in una frase). Durante il pre-addestramento, il modello acquisisce livelli significativi di comprensione del linguaggio che possono poi essere sfruttati con altri dataset tramite il fine tuning. Questo processo è chiamato **transfer learning**.

![immagine da http://jalammar.github.io/illustrated-bert/](../../../../../translated_images/jalammarBERT-language-modeling-masked-lm.34f113ea5fec4362e39ee4381aab7cad06b5465a0b5f053a0f2aa05fbe14e746.it.png)

> Immagine [fonte](http://jalammar.github.io/illustrated-bert/)

## ✍️ Esercizi: Transformer

Continua il tuo apprendimento nei seguenti notebook:

* [Transformer in PyTorch](../../../../../lessons/5-NLP/18-Transformers/TransformersPyTorch.ipynb)
* [Transformer in TensorFlow](../../../../../lessons/5-NLP/18-Transformers/TransformersTF.ipynb)

## Conclusione

In questa lezione hai appreso dei Transformer e dei Meccanismi di Attenzione, strumenti essenziali nella cassetta degli attrezzi dell'NLP. Esistono molte varianti delle architetture Transformer, tra cui BERT, DistilBERT, BigBird, OpenGPT3 e altre, che possono essere ottimizzate. Il pacchetto [HuggingFace](https://github.com/huggingface/) fornisce un repository per l'addestramento di molte di queste architetture sia con PyTorch che con TensorFlow.

## 🚀 Sfida

## [Quiz post-lezione](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/218)

## Revisione e Studio Autonomo

* [Blog post](https://mchromiak.github.io/articles/2017/Sep/12/Transformer-Attention-is-all-you-need/), che spiega il classico articolo [Attention is all you need](https://arxiv.org/abs/1706.03762) sui transformer.
* [Una serie di blog post](https://towardsdatascience.com/transformers-explained-visually-part-1-overview-of-functionality-95a6dd460452) sui transformer, che spiegano l'architettura in dettaglio.

## [Compito](assignment.md)

**Disclaimer**:  
Questo documento è stato tradotto utilizzando il servizio di traduzione AI [Co-op Translator](https://github.com/Azure/co-op-translator). Sebbene ci impegniamo per garantire l'accuratezza, si prega di notare che le traduzioni automatizzate potrebbero contenere errori o imprecisioni. Il documento originale nella sua lingua nativa dovrebbe essere considerato la fonte autorevole. Per informazioni critiche, si raccomanda una traduzione professionale effettuata da un esperto umano. Non siamo responsabili per eventuali incomprensioni o interpretazioni errate derivanti dall'uso di questa traduzione.