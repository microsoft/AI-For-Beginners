<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "7df19702b8d2d3f7c4238c51bec2c8fc",
  "translation_date": "2025-08-26T07:14:45+00:00",
  "source_file": "lessons/0-course-setup/how-to-run.md",
  "language_code": "it"
}
-->
# Come Eseguire il Codice

Questo curriculum contiene molti esempi eseguibili e laboratori che vorresti provare. Per farlo, hai bisogno della possibilità di eseguire codice Python nei Jupyter Notebook forniti come parte di questo curriculum. Hai diverse opzioni per eseguire il codice:

## Eseguire localmente sul tuo computer

Per eseguire il codice localmente sul tuo computer, devi avere una qualche versione di Python installata. Personalmente consiglio di installare **[miniconda](https://conda.io/en/latest/miniconda.html)** - è un'installazione piuttosto leggera che supporta il gestore di pacchetti `conda` per diversi **ambienti virtuali** Python.

Dopo aver installato miniconda, devi clonare il repository e creare un ambiente virtuale da utilizzare per questo corso:

```bash
git clone http://github.com/microsoft/ai-for-beginners
cd ai-for-beginners
conda env create --name ai4beg --file .devcontainer/environment.yml
conda activate ai4beg
```

### Utilizzare Visual Studio Code con l'Estensione Python

Probabilmente il modo migliore per utilizzare il curriculum è aprirlo in [Visual Studio Code](http://code.visualstudio.com/?WT.mc_id=academic-77998-cacaste) con l'[Estensione Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-77998-cacaste).

> **Note**: Una volta clonato e aperto il directory in VS Code, ti verrà automaticamente suggerito di installare le estensioni Python. Dovrai anche installare miniconda come descritto sopra.

> **Note**: Se VS Code ti suggerisce di riaprire il repository in un container, devi rifiutare per utilizzare l'installazione locale di Python.

### Utilizzare Jupyter nel Browser

Puoi anche utilizzare l'ambiente Jupyter direttamente dal browser sul tuo computer. In realtà, sia Jupyter classico che Jupyter Hub offrono un ambiente di sviluppo piuttosto comodo con completamento automatico, evidenziazione del codice, ecc.

Per avviare Jupyter localmente, vai nella directory del corso ed esegui:

```bash
jupyter notebook
```
oppure
```bash
jupyterhub
```
Puoi quindi navigare tra i file `.ipynb`, aprirli e iniziare a lavorare.

### Eseguire in un container

Un'alternativa all'installazione di Python sarebbe eseguire il codice in un container. Poiché il nostro repository contiene una cartella speciale `.devcontainer` che istruisce su come costruire un container per questo repo, VS Code ti offrirà di riaprire il codice in un container. Questo richiederà l'installazione di Docker e sarà anche più complesso, quindi lo consigliamo agli utenti più esperti.

## Eseguire nel Cloud

Se non vuoi installare Python localmente e hai accesso a risorse cloud, una buona alternativa sarebbe eseguire il codice nel cloud. Ci sono diversi modi per farlo:

* Utilizzando **[GitHub Codespaces](https://github.com/features/codespaces)**, che è un ambiente virtuale creato per te su GitHub, accessibile tramite l'interfaccia browser di VS Code. Se hai accesso a Codespaces, puoi semplicemente cliccare sul pulsante **Code** nel repository, avviare un codespace e iniziare rapidamente.

* Utilizzando **[Binder](https://mybinder.org/v2/gh/microsoft/ai-for-beginners/HEAD)**. [Binder](https://mybinder.org) offre risorse di calcolo gratuite nel cloud per persone come te che vogliono testare del codice su GitHub. C'è un pulsante nella pagina principale per aprire il repository in Binder - questo ti porterà rapidamente al sito di Binder, che costruirà il container sottostante e avvierà l'interfaccia web di Jupyter per te senza problemi.

> **Note**: Per prevenire abusi, Binder ha accesso a alcune risorse web bloccato. Questo potrebbe impedire il funzionamento di parte del codice che scarica modelli e/o dataset da Internet pubblico. Potresti dover trovare delle soluzioni alternative. Inoltre, le risorse di calcolo fornite da Binder sono piuttosto basilari, quindi l'addestramento sarà lento, specialmente nelle lezioni più complesse.

## Eseguire nel Cloud con GPU

Alcune delle lezioni più avanzate di questo curriculum trarrebbero grande beneficio dal supporto GPU, perché altrimenti l'addestramento sarebbe estremamente lento. Ci sono alcune opzioni che puoi seguire, specialmente se hai accesso al cloud tramite [Azure for Students](https://azure.microsoft.com/free/students/?WT.mc_id=academic-77998-cacaste) o tramite la tua istituzione:

* Crea una [Data Science Virtual Machine](https://docs.microsoft.com/learn/modules/intro-to-azure-data-science-virtual-machine/?WT.mc_id=academic-77998-cacaste) e connettiti ad essa tramite Jupyter. Puoi quindi clonare il repository direttamente sulla macchina e iniziare a imparare. Le VM della serie NC hanno supporto GPU.

> **Note**: Alcuni abbonamenti, inclusi Azure for Students, non forniscono supporto GPU di default. Potresti dover richiedere core GPU aggiuntivi tramite una richiesta di supporto tecnico.

* Crea un [Azure Machine Learning Workspace](https://azure.microsoft.com/services/machine-learning/?WT.mc_id=academic-77998-cacaste) e utilizza la funzione Notebook lì. [Questo video](https://azure-for-academics.github.io/quickstart/azureml-papers/) mostra come clonare un repository in un notebook di Azure ML e iniziare a usarlo.

Puoi anche utilizzare Google Colab, che offre un certo supporto GPU gratuito, e caricare i Jupyter Notebook lì per eseguirli uno per uno.

**Disclaimer**:  
Questo documento è stato tradotto utilizzando il servizio di traduzione automatica [Co-op Translator](https://github.com/Azure/co-op-translator). Sebbene ci impegniamo per garantire l'accuratezza, si prega di notare che le traduzioni automatiche possono contenere errori o imprecisioni. Il documento originale nella sua lingua nativa dovrebbe essere considerato la fonte autorevole. Per informazioni critiche, si raccomanda una traduzione professionale effettuata da un traduttore umano. Non siamo responsabili per eventuali fraintendimenti o interpretazioni errate derivanti dall'uso di questa traduzione.