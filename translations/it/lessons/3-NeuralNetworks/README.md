<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "1c6b8c7c1778a35fc1139b7f2aecb7b3",
  "translation_date": "2025-08-26T07:08:12+00:00",
  "source_file": "lessons/3-NeuralNetworks/README.md",
  "language_code": "it"
}
-->
# Introduzione alle Reti Neurali

![Riassunto del contenuto di Introduzione alle Reti Neurali in uno schizzo](../../../../translated_images/ai-neuralnetworks.1c687ae40bc86e834f497844866a26d3e0886650a67a4bbe29442e2f157d3b18.it.png)

Come discusso nell'introduzione, uno dei modi per raggiungere l'intelligenza è addestrare un **modello computazionale** o un **cervello artificiale**. Dalla metà del XX secolo, i ricercatori hanno provato diversi modelli matematici, fino a quando negli ultimi anni questa direzione si è dimostrata estremamente promettente. Questi modelli matematici del cervello sono chiamati **reti neurali**.

> A volte le reti neurali vengono chiamate *Reti Neurali Artificiali*, ANNs, per indicare che stiamo parlando di modelli, non di reti reali di neuroni.

## Apprendimento Automatico

Le reti neurali fanno parte di una disciplina più ampia chiamata **Apprendimento Automatico**, il cui obiettivo è utilizzare i dati per addestrare modelli computazionali in grado di risolvere problemi. L'apprendimento automatico costituisce una grande parte dell'Intelligenza Artificiale, tuttavia, non trattiamo l'apprendimento automatico classico in questo curriculum.

> Visita il nostro curriculum separato **[Machine Learning for Beginners](http://github.com/microsoft/ml-for-beginners)** per saperne di più sull'apprendimento automatico classico.

Nell'apprendimento automatico, assumiamo di avere un dataset di esempi **X** e i corrispondenti valori di output **Y**. Gli esempi sono spesso vettori N-dimensionali che consistono in **caratteristiche**, e gli output sono chiamati **etichette**.

Considereremo i due problemi più comuni dell'apprendimento automatico:

* **Classificazione**, dove dobbiamo classificare un oggetto di input in due o più classi.
* **Regressione**, dove dobbiamo prevedere un valore numerico per ciascun campione di input.

> Quando rappresentiamo gli input e gli output come tensori, il dataset di input è una matrice di dimensioni M×N, dove M è il numero di campioni e N è il numero di caratteristiche. Le etichette di output Y sono un vettore di dimensioni M.

In questo curriculum, ci concentreremo solo sui modelli di reti neurali.

## Un Modello di Neurone

Dalla biologia sappiamo che il nostro cervello è composto da cellule neuronali, ognuna delle quali ha molteplici "input" (assoni) e un output (dendrite). Gli assoni e i dendriti possono condurre segnali elettrici, e le connessioni tra assoni e dendriti possono mostrare diversi gradi di conduttività (controllati dai neuromediatori).

![Modello di un Neurone](../../../../translated_images/synapse-wikipedia.ed20a9e4726ea1c6a3ce8fec51c0b9bec6181946dca0fe4e829bc12fa3bacf01.it.jpg) | ![Modello di un Neurone](../../../../translated_images/artneuron.1a5daa88d20ebe6f5824ddb89fba0bdaaf49f67e8230c1afbec42909df1fc17e.it.png)
----|----
Neurone Reale *([Immagine](https://en.wikipedia.org/wiki/Synapse#/media/File:SynapseSchematic_lines.svg) da Wikipedia)* | Neurone Artificiale *(Immagine dell'Autore)*

Pertanto, il modello matematico più semplice di un neurone contiene diversi input X<sub>1</sub>, ..., X<sub>N</sub> e un output Y, e una serie di pesi W<sub>1</sub>, ..., W<sub>N</sub>. L'output viene calcolato come:

<img src="images/netout.png" alt="Y = f\left(\sum_{i=1}^N X_iW_i\right)" width="131" height="53" align="center"/>

dove f è una **funzione di attivazione** non lineare.

> I primi modelli di neurone sono stati descritti nel classico articolo [A logical calculus of the ideas immanent in nervous activity](https://www.cs.cmu.edu/~./epxing/Class/10715/reading/McCulloch.and.Pitts.pdf) di Warren McCullock e Walter Pitts nel 1943. Donald Hebb, nel suo libro "[The Organization of Behavior: A Neuropsychological Theory](https://books.google.com/books?id=VNetYrB8EBoC)", ha proposto il modo in cui queste reti possono essere addestrate.

## In questa Sezione

In questa sezione impareremo:
* [Perceptron](03-Perceptron/README.md), uno dei primi modelli di rete neurale per la classificazione a due classi
* [Reti multi-strato](04-OwnFramework/README.md) con un notebook associato [come costruire il nostro framework](../../../../lessons/3-NeuralNetworks/04-OwnFramework/OwnFramework.ipynb)
* [Framework per Reti Neurali](05-Frameworks/README.md), con questi notebook: [PyTorch](../../../../lessons/3-NeuralNetworks/05-Frameworks/IntroPyTorch.ipynb) e [Keras/Tensorflow](../../../../lessons/3-NeuralNetworks/05-Frameworks/IntroKerasTF.ipynb)
* [Overfitting](../../../../lessons/3-NeuralNetworks/05-Frameworks)

**Disclaimer**:  
Questo documento è stato tradotto utilizzando il servizio di traduzione automatica [Co-op Translator](https://github.com/Azure/co-op-translator). Sebbene ci impegniamo per garantire l'accuratezza, si prega di notare che le traduzioni automatiche possono contenere errori o imprecisioni. Il documento originale nella sua lingua nativa dovrebbe essere considerato la fonte autorevole. Per informazioni critiche, si raccomanda una traduzione professionale effettuata da un traduttore umano. Non siamo responsabili per eventuali incomprensioni o interpretazioni errate derivanti dall'uso di questa traduzione.