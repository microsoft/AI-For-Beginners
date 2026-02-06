# Come eseguire il codice

Questo curriculum contiene molti esempi eseguibili e laboratori che vorresti eseguire. Per farlo, hai bisogno della capacità di eseguire codice Python nei Jupyter Notebook forniti come parte di questo curriculum. Hai diverse opzioni per eseguire il codice:

## Esegui localmente sul tuo computer

Per eseguire il codice localmente sul tuo computer, è necessaria un'installazione di Python. Una raccomandazione è installare **[miniconda](https://conda.io/en/latest/miniconda.html)** - si tratta di un'installazione piuttosto leggera che supporta il gestore di pacchetti `conda` per diversi **ambienti virtuali** Python.

Dopo aver installato miniconda, clona il repository e crea un ambiente virtuale da utilizzare per questo corso:

```bash
git clone http://github.com/microsoft/ai-for-beginners
cd ai-for-beginners
conda env create --name ai4beg --file .devcontainer/environment.yml
conda activate ai4beg
```

### Usare Visual Studio Code con l'estensione Python

Questo curriculum è meglio utilizzato aprendolo in [Visual Studio Code](http://code.visualstudio.com/?WT.mc_id=academic-77998-cacaste) con l'[estensione Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-77998-cacaste).

> **Nota**: Una volta che cloni e apri la directory in VS Code, ti suggerirà automaticamente di installare le estensioni Python. Dovrai anche installare miniconda come descritto sopra.

> **Nota**: Se VS Code ti suggerisce di riaprire il repository in un container, dovresti rifiutare per usare l'installazione Python locale.

### Usare Jupyter nel browser

Puoi anche usare un ambiente Jupyter dal browser sul tuo computer. Sia il classico Jupyter che JupyterHub offrono un ambiente di sviluppo comodo con completamento automatico, evidenziazione del codice, ecc.

Per iniziare Jupyter localmente, vai nella directory del corso ed esegui:

```bash
jupyter notebook
```
o
```bash
jupyterhub
```
Puoi quindi navigare in uno qualsiasi dei file `.ipynb`, aprirli e iniziare a lavorare.

### Esecuzione in contenitore

Un'alternativa all'installazione di Python sarebbe eseguire il codice in un contenitore. Poiché il nostro repository fornisce una cartella speciale `.devcontainer` che spiega come costruire un contenitore per questo repo, VS Code offre l'opportunità di riaprire il codice in un contenitore. Questo richiederà l'installazione di Docker e sarà anche più complesso, quindi lo consigliamo a utenti più esperti.

## Esecuzione nel cloud

Se non vuoi installare Python localmente e hai accesso ad alcune risorse cloud, una buona alternativa è eseguire il codice nel cloud. Ci sono diversi modi per farlo:

* Usare **[GitHub Codespaces](https://github.com/features/codespaces)**, che è un ambiente virtuale creato per te su GitHub, accessibile tramite un'interfaccia browser di VS Code. Se hai accesso a Codespaces, puoi semplicemente cliccare sul pulsante **Code** nel repo, avviare un codespace e iniziare rapidamente.
* Usare **[Binder](https://mybinder.org/v2/gh/microsoft/ai-for-beginners/HEAD)**. [Binder](https://mybinder.org) offre risorse di calcolo gratuite fornite nel cloud per persone come te per testare del codice su GitHub. C'è un pulsante nella pagina principale per aprire il repository in Binder - questo ti porterà rapidamente al sito di binder, che costruirà un contenitore sottostante e avvierà un'interfaccia web Jupyter per te senza interruzioni.

> **Nota**: Per prevenire abusi, Binder ha accesso bloccato ad alcune risorse web. Questo potrebbe impedire che parte del codice funzioni, specialmente quello che cerca di scaricare modelli e/o dataset da Internet pubblico. Potresti dover trovare alcune soluzioni alternative. Inoltre, le risorse di calcolo fornite da Binder sono piuttosto basilari, quindi l'addestramento sarà lento, specialmente nelle lezioni successive, più complesse.

## Esecuzione nel cloud con GPU

Alcune lezioni successive di questo curriculum trarrebbero grande beneficio dal supporto GPU. L'addestramento dei modelli, per esempio, può essere dolorosamente lento altrimenti. Ci sono alcune opzioni che puoi seguire, specialmente se hai accesso al cloud tramite [Azure for Students](https://azure.microsoft.com/free/students/?WT.mc_id=academic-77998-cacaste), o tramite la tua istituzione:

* Crea una [Data Science Virtual Machine](https://docs.microsoft.com/learn/modules/intro-to-azure-data-science-virtual-machine/?WT.mc_id=academic-77998-cacaste) e connettiti tramite Jupyter. Puoi quindi clonare il repo direttamente sulla macchina e iniziare a imparare. Le VM della serie NC hanno supporto GPU.

> **Nota**: Alcuni abbonamenti, inclusi Azure for Students, non forniscono supporto GPU di default. Potresti dover richiedere core GPU aggiuntivi tramite richiesta di supporto tecnico.

* Crea un [Azure Machine Learning Workspace](https://azure.microsoft.com/services/machine-learning/?WT.mc_id=academic-77998-cacaste) e quindi usa la funzione Notebook lì. [Questo video](https://azure-for-academics.github.io/quickstart/azureml-papers/) mostra come clonare un repository in un notebook Azure ML e iniziare a usarlo.

Puoi anche usare Google Colab, che viene fornito con un certo supporto GPU gratuito, e caricare lì i Jupyter Notebook per eseguirli uno alla volta.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Questo documento è stato tradotto utilizzando il servizio di traduzione AI [Co-op Translator](https://github.com/Azure/co-op-translator). Pur impegnandoci per garantire accuratezza, si prega di considerare che le traduzioni automatiche possono contenere errori o inesattezze. Il documento originale nella sua lingua madre deve essere considerato la fonte autorevole. Per informazioni importanti, si consiglia una traduzione professionale effettuata da un esperto umano. Non ci assumiamo responsabilità per eventuali malintesi o interpretazioni errate derivanti dall’uso di questa traduzione.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->