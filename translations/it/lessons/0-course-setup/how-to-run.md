# Come eseguire il codice

Questo curriculum contiene molti esempi eseguibili e laboratori che potresti voler provare. Per farlo, hai bisogno della possibilità di eseguire codice Python nei Jupyter Notebook forniti come parte del curriculum. Hai diverse opzioni per eseguire il codice:

## Esecuzione in locale sul tuo computer

Per eseguire il codice in locale sul tuo computer, devi avere installata una versione di Python. Personalmente consiglio di installare **[miniconda](https://conda.io/en/latest/miniconda.html)** – si tratta di un’installazione leggera che supporta il gestore di pacchetti `conda` per diversi **ambienti virtuali** Python.

Dopo aver installato miniconda, devi clonare il repository e creare un ambiente virtuale da utilizzare per questo corso:

```bash
git clone http://github.com/microsoft/ai-for-beginners
cd ai-for-beginners
conda env create --name ai4beg --file .devcontainer/environment.yml
conda activate ai4beg
```

### Utilizzare Visual Studio Code con l’estensione Python

Probabilmente il modo migliore per utilizzare il curriculum è aprirlo in [Visual Studio Code](http://code.visualstudio.com/?WT.mc_id=academic-77998-cacaste) con l’[estensione Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-77998-cacaste).

> **Nota**: Una volta clonato e aperta la cartella in VS Code, ti verrà suggerito automaticamente di installare le estensioni Python. Dovrai anche installare miniconda come descritto sopra.

> **Nota**: Se VS Code ti suggerisce di riaprire il repository in un container, rifiuta per usare l’installazione Python locale.

### Utilizzare Jupyter nel browser

Puoi anche usare un ambiente Jupyter direttamente dal browser sul tuo computer. Sia il classico Jupyter sia Jupyter Hub offrono un ambiente di sviluppo molto comodo con autocompletamento, evidenziazione del codice, ecc.

Per avviare Jupyter in locale, vai nella cartella del corso ed esegui:

```bash
jupyter notebook
```
oppure
```bash
jupyterhub
```

Potrai quindi navigare tra i file `.ipynb`, aprirli e iniziare a lavorare.

### Esecuzione in container

Un’alternativa all’installazione di Python è l’esecuzione in un container. Poiché il nostro repository contiene una cartella `.devcontainer` che spiega come costruire un container per il progetto, VS Code ti proporrà di riaprire il codice in un container. Questo richiederà l’installazione di Docker e sarà leggermente più complesso, quindi lo consigliamo a utenti più esperti.

## Esecuzione nel Cloud

Se non vuoi installare Python localmente e hai accesso a risorse cloud, una buona alternativa è eseguire il codice nel cloud. Ci sono diversi modi per farlo:

* Utilizzando **[GitHub Codespaces](https://github.com/features/codespaces)**, un ambiente virtuale creato per te su GitHub, accessibile tramite l’interfaccia browser di VS Code. Se hai accesso a Codespaces, ti basta cliccare sul pulsante **Code** nel repository, avviare uno spazio, e iniziare a lavorare subito.
* Utilizzando **[Binder](https://mybinder.org/v2/gh/microsoft/ai-for-beginners/HEAD)**. [Binder](https://mybinder.org) fornisce gratuitamente risorse di calcolo nel cloud per testare codice da GitHub. C’è un pulsante nella homepage del repository per aprirlo in Binder – verrai reindirizzato al sito, che costruirà il container e avvierà automaticamente l’interfaccia web di Jupyter.

> **Nota**: Per evitare abusi, Binder blocca l’accesso a certe risorse web. Questo potrebbe impedire il funzionamento di alcuni script che scaricano modelli o dataset da Internet. Inoltre, le risorse di calcolo offerte da Binder sono abbastanza limitate, quindi l’addestramento sarà lento, soprattutto nelle lezioni più avanzate.

## Esecuzione nel Cloud con GPU

Alcune delle lezioni avanzate in questo curriculum traggono grande beneficio dal supporto GPU, altrimenti l’addestramento sarà molto lento. Hai alcune opzioni, specialmente se hai accesso al cloud tramite [Azure for Students](https://azure.microsoft.com/free/students/?WT.mc_id=academic-77998-cacaste), o tramite la tua istituzione:

* Crea una [Macchina Virtuale per Data Science](https://docs.microsoft.com/learn/modules/intro-to-azure-data-science-virtual-machine/?WT.mc_id=academic-77998-cacaste) e collegati tramite Jupyter. Puoi clonare il repository direttamente sulla macchina e iniziare a studiare. Le VM della serie NC offrono supporto GPU.

> **Nota**: Alcuni abbonamenti, incluso Azure for Students, non offrono il supporto GPU di default. Potresti dover richiedere core GPU aggiuntivi tramite una richiesta di supporto tecnico.

* Crea un [Workspace Azure Machine Learning](https://azure.microsoft.com/services/machine-learning/?WT.mc_id=academic-77998-cacaste) e usa la funzione Notebook integrata. [Questo video](https://azure-for-academics.github.io/quickstart/azureml-papers/) mostra come clonare un repository in un notebook Azure ML e iniziare a usarlo.

Puoi anche usare Google Colab, che offre un po’ di supporto GPU gratuito, e caricare lì i Jupyter Notebook per eseguirli uno per uno.
