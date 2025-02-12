# So führen Sie den Code aus

Dieser Lehrplan enthält viele ausführbare Beispiele und Laborübungen, die Sie ausführen möchten. Um dies zu tun, benötigen Sie die Möglichkeit, Python-Code in Jupyter-Notebooks auszuführen, die Teil dieses Lehrplans sind. Sie haben mehrere Optionen, um den Code auszuführen:

## Lokal auf Ihrem Computer ausführen

Um den Code lokal auf Ihrem Computer auszuführen, müssen Sie eine Version von Python installiert haben. Ich empfehle persönlich die Installation von **[miniconda](https://conda.io/en/latest/miniconda.html)** - es handelt sich um eine recht leichte Installation, die den `conda` Paketmanager für verschiedene Python **virtuelle Umgebungen** unterstützt.

Nachdem Sie miniconda installiert haben, müssen Sie das Repository klonen und eine virtuelle Umgebung erstellen, die für diesen Kurs verwendet wird:

```bash
git clone http://github.com/microsoft/ai-for-beginners
cd ai-for-beginners
conda env create --name ai4beg --file .devcontainer/environment.yml
conda activate ai4beg
```

### Verwendung von Visual Studio Code mit Python-Erweiterung

Wahrscheinlich ist der beste Weg, den Lehrplan zu nutzen, ihn in [Visual Studio Code](http://code.visualstudio.com/?WT.mc_id=academic-77998-cacaste) mit der [Python-Erweiterung](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-77998-cacaste) zu öffnen.

> **Hinweis**: Sobald Sie das Verzeichnis in VS Code klonen und öffnen, wird Ihnen automatisch vorgeschlagen, Python-Erweiterungen zu installieren. Sie müssen auch miniconda installieren, wie oben beschrieben.

> **Hinweis**: Wenn VS Code Ihnen vorschlägt, das Repository im Container erneut zu öffnen, müssen Sie dies ablehnen, um die lokale Python-Installation zu verwenden.

### Verwendung von Jupyter im Browser

Sie können auch die Jupyter-Umgebung direkt über den Browser auf Ihrem eigenen Computer verwenden. Tatsächlich bieten sowohl klassisches Jupyter als auch Jupyter Hub eine recht bequeme Entwicklungsumgebung mit Autovervollständigung, Code-Hervorhebung usw.

Um Jupyter lokal zu starten, gehen Sie in das Verzeichnis des Kurses und führen Sie aus:

```bash
jupyter notebook
```
oder
```bash
jupyterhub
```
Sie können dann zu einem der `.ipynb` files, open them and start working.

### Running in container

One alternative to Python installation would be to run the code in container. Since our repository contains special `.devcontainer`-Ordner navigieren, der Anweisungen gibt, wie ein Container für dieses Repo erstellt wird. VS Code würde Ihnen anbieten, den Code im Container erneut zu öffnen. Dies erfordert die Installation von Docker und wäre auch komplexer, daher empfehlen wir dies erfahrenen Benutzern.

## Ausführen in der Cloud

Wenn Sie Python nicht lokal installieren möchten und Zugang zu einigen Cloud-Ressourcen haben, wäre eine gute Alternative, den Code in der Cloud auszuführen. Es gibt mehrere Möglichkeiten, dies zu tun:

* Verwenden von **[GitHub Codespaces](https://github.com/features/codespaces)**, einem virtuellen Umfeld, das für Sie auf GitHub erstellt wird und über die VS Code-Browseroberfläche zugänglich ist. Wenn Sie Zugriff auf Codespaces haben, können Sie einfach auf die Schaltfläche **Code** im Repo klicken, einen Codespace starten und im Handumdrehen loslegen.
* Verwenden von **[Binder](https://mybinder.org/v2/gh/microsoft/ai-for-beginners/HEAD)**. [Binder](https://mybinder.org) ist eine kostenlose Rechenressource, die in der Cloud für Menschen wie Sie bereitgestellt wird, um etwas Code auf GitHub auszuprobieren. Es gibt eine Schaltfläche auf der Startseite, um das Repository in Binder zu öffnen - dies sollte Sie schnell zur Binder-Website bringen, die den zugrunde liegenden Container erstellt und die Jupyter-Weboberfläche nahtlos für Sie startet.

> **Hinweis**: Um Missbrauch zu verhindern, hat Binder den Zugriff auf einige Webressourcen blockiert. Dies kann verhindern, dass ein Teil des Codes funktioniert, der Modelle und/oder Datensätze aus dem öffentlichen Internet abruft. Möglicherweise müssen Sie einige Umgehungen finden. Außerdem sind die von Binder bereitgestellten Rechenressourcen ziemlich grundlegend, sodass das Training langsam sein wird, insbesondere in späteren, komplexeren Lektionen.

## Ausführen in der Cloud mit GPU

Einige der späteren Lektionen in diesem Lehrplan würden erheblich von GPU-Unterstützung profitieren, da das Training sonst schmerzhaft langsam sein wird. Es gibt einige Optionen, die Sie verfolgen können, insbesondere wenn Sie über [Azure for Students](https://azure.microsoft.com/free/students/?WT.mc_id=academic-77998-cacaste) oder über Ihre Institution Zugang zur Cloud haben:

* Erstellen Sie eine [Data Science Virtual Machine](https://docs.microsoft.com/learn/modules/intro-to-azure-data-science-virtual-machine/?WT.mc_id=academic-77998-cacaste) und verbinden Sie sich über Jupyter damit. Sie können das Repo dann direkt auf der Maschine klonen und mit dem Lernen beginnen. NC-Serie VMs haben GPU-Unterstützung.

> **Hinweis**: Einige Abonnements, einschließlich Azure for Students, bieten nicht standardmäßig GPU-Unterstützung. Möglicherweise müssen Sie zusätzliche GPU-Kerne über eine technische Supportanfrage anfordern.

* Erstellen Sie einen [Azure Machine Learning Workspace](https://azure.microsoft.com/services/machine-learning/?WT.mc_id=academic-77998-cacaste) und verwenden Sie dann die Notebook-Funktion dort. [Dieses Video](https://azure-for-academics.github.io/quickstart/azureml-papers/) zeigt, wie man ein Repository in ein Azure ML-Notebook klont und es zu verwenden beginnt.

Sie können auch Google Colab verwenden, das mit einer gewissen kostenlosen GPU-Unterstützung kommt, und dort Jupyter-Notebooks hochladen, um sie nacheinander auszuführen.

**Haftungsausschluss**:  
Dieses Dokument wurde mit maschinellen KI-Übersetzungsdiensten übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner Ursprungssprache sollte als die maßgebliche Quelle betrachtet werden. Für wichtige Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die aus der Verwendung dieser Übersetzung entstehen.