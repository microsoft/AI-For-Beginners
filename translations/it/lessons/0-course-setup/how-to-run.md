# Come Eseguire il Codice

Questo programma contiene molti esempi eseguibili e laboratori che vorrai eseguire. Per farlo, è necessario poter eseguire codice Python nei Jupyter Notebook forniti come parte di questo programma. Hai diverse opzioni per eseguire il codice:

## Eseguire localmente sul tuo computer

Per eseguire il codice localmente sul tuo computer, è necessaria un'installazione di Python. Una raccomandazione è installare **[miniconda](https://conda.io/en/latest/miniconda.html)** - è un'installazione piuttosto leggera che supporta il gestore di pacchetti `conda` per diversi **ambienti virtuali** Python.

Dopo aver installato miniconda, clona il repository e crea un ambiente virtuale da usare per questo corso:

```bash
git clone http://github.com/microsoft/ai-for-beginners
cd ai-for-beginners
conda env create --name ai4beg --file .devcontainer/environment.yml
conda activate ai4beg
```

> **Nota per Windows**: Se la creazione dell'ambiente fallisce durante l'installazione di `gdk-pixbuf` con un `UnicodeDecodeError` che menziona il codec `gbk`, abilita la modalità UTF-8 di Python nel terminale e riprova. Usa la sintassi per il terminale che stai usando:
>
> **PowerShell:**
>
> ```powershell
> $env:PYTHONUTF8 = "1"
> conda env create --name ai4beg --file .devcontainer/environment.yml
> ```
>
> **Prompt dei comandi (`cmd.exe`) o Anaconda Prompt:**
>
> ```cmd
> set PYTHONUTF8=1
> conda env create --name ai4beg --file .devcontainer/environment.yml
> ```
>
> **Bash, incluso Git Bash:**
>
> ```bash
> export PYTHONUTF8=1
> conda env create --name ai4beg --file .devcontainer/environment.yml
> ```
>
> Se un tentativo fallito ha lasciato l'ambiente `ai4beg` attivo, disattivalo e rimuovi quell'ambiente prima di riprovare. Usa prima `conda deactivate` quando un ambiente è attivo:
>
> ```text
> conda deactivate
> conda env remove --name ai4beg
> ```

### Utilizzo di Visual Studio Code con estensione Python

Questo programma è meglio utilizzato aprendolo in [Visual Studio Code](http://code.visualstudio.com/?WT.mc_id=academic-77998-cacaste) con l'[estensione Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-77998-cacaste).

> **Nota**: Una volta che cloni e apri la directory in VS Code, ti suggerirà automaticamente di installare le estensioni Python. Dovrai inoltre installare miniconda come descritto sopra.

> **Nota**: Se VS Code ti suggerisce di riaprire il repository in un container, dovresti declinare per usare l'installazione Python locale.

### Uso di Jupyter nel browser

Puoi anche usare un ambiente Jupyter dal browser sul tuo computer. Sia Jupyter classico che JupyterHub offrono un ambiente di sviluppo comodo con completamento automatico, evidenziazione del codice, ecc.

Per avviare Jupyter localmente, vai nella directory del corso e esegui:

```bash
jupyter notebook
```
o
```bash
jupyterhub
```
Puoi quindi navigare verso uno qualsiasi dei file `.ipynb`, aprirli e iniziare a lavorare.

### Esecuzione in un container

Un'alternativa all'installazione di Python sarebbe eseguire il codice in un container. Poiché il nostro repository fornisce una speciale cartella `.devcontainer` che indica come costruire un container per questo repo, VS Code offre l'opportunità di riaprire il codice in un container. Questo richiederà l'installazione di Docker, ed è anche più complesso, quindi raccomandiamo questo agli utenti più esperti.

## Esecuzione nel Cloud

Se non vuoi installare Python localmente e hai accesso ad alcune risorse cloud, un'ottima alternativa sarebbe eseguire il codice nel cloud. Ci sono diversi modi per farlo:

* Usare **[GitHub Codespaces](https://github.com/features/codespaces)**, che è un ambiente virtuale creato per te su GitHub, accessibile tramite un'interfaccia browser di VS Code. Se hai accesso a Codespaces, puoi semplicemente cliccare il pulsante **Code** nel repo, avviare un codespace e iniziare a lavorare in poco tempo.
* Usare **[Binder](https://mybinder.org/v2/gh/microsoft/ai-for-beginners/HEAD)**. [Binder](https://mybinder.org) offre risorse di calcolo gratuite fornite nel cloud per persone come te per testare codice su GitHub. C'è un pulsante nella pagina principale per aprire il repository in Binder - questo ti porterà rapidamente al sito di Binder, che costruirà un container sottostante e avvierà un'interfaccia web Jupyter per te senza interruzioni.

> **Nota**: Per prevenire abusi, Binder blocca l'accesso ad alcune risorse web. Questo potrebbe impedire a parte del codice di funzionare, in particolare quello che scarica modelli e/o set di dati da Internet pubblico. Potrebbe essere necessario trovare qualche soluzione alternativa. Inoltre, le risorse di calcolo fornite da Binder sono abbastanza basiche, quindi l'addestramento sarà lento, specialmente nelle lezioni più complesse successive.

## Esecuzione nel Cloud con GPU

Alcune delle lezioni successive in questo programma trarrebbero grande beneficio dal supporto GPU. L'addestramento dei modelli, ad esempio, può essere dolorosamente lento altrimenti. Ci sono alcune opzioni che puoi seguire, specialmente se hai accesso al cloud tramite [Azure for Students](https://azure.microsoft.com/free/students/?WT.mc_id=academic-77998-cacaste), o tramite la tua istituzione:

* Crea una [Data Science Virtual Machine](https://docs.microsoft.com/learn/modules/intro-to-azure-data-science-virtual-machine/?WT.mc_id=academic-77998-cacaste) e connettiti ad essa tramite Jupyter. Puoi quindi clonare il repo direttamente sulla macchina e iniziare a imparare. Le VM della serie NC hanno supporto GPU.

> **Nota**: Alcuni abbonamenti, incluso Azure for Students, non forniscono supporto GPU di default. Potresti dover richiedere core GPU aggiuntivi tramite una richiesta di supporto tecnico.

* Crea un [Azure Machine Learning Workspace](https://azure.microsoft.com/services/machine-learning/?WT.mc_id=academic-77998-cacaste) e poi usa la funzione Notebook lì. [Questo video](https://azure-for-academics.github.io/quickstart/azureml-papers/) mostra come clonare un repository in un notebook Azure ML e iniziare a usarlo.

Puoi anche usare Google Colab, che offre un supporto GPU gratuito, e caricare lì i Jupyter Notebook per eseguirli uno per uno.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Questo documento è stato tradotto utilizzando il servizio di traduzione AI [Co-op Translator](https://github.com/Azure/co-op-translator). Sebbene ci impegniamo per garantire la precisione, si prega di notare che le traduzioni automatizzate possono contenere errori o imprecisioni. Il documento originale nella sua lingua nativa deve essere considerato la fonte autorevole. Per informazioni critiche, si raccomanda una traduzione professionale effettuata da un essere umano. Non siamo responsabili per eventuali malintesi o interpretazioni errate derivanti dall’uso di questa traduzione.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->