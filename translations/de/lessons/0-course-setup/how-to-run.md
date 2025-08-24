<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "7df19702b8d2d3f7c4238c51bec2c8fc",
  "translation_date": "2025-08-24T09:43:53+00:00",
  "source_file": "lessons/0-course-setup/how-to-run.md",
  "language_code": "de"
}
-->
# So führen Sie den Code aus

Dieses Curriculum enthält viele ausführbare Beispiele und Übungen, die Sie ausprobieren möchten. Um dies zu tun, benötigen Sie die Möglichkeit, Python-Code in den Jupyter-Notebooks auszuführen, die Teil dieses Curriculums sind. Es gibt mehrere Möglichkeiten, den Code auszuführen:

## Lokal auf Ihrem Computer ausführen

Um den Code lokal auf Ihrem Computer auszuführen, benötigen Sie eine installierte Python-Version. Ich empfehle persönlich die Installation von **[miniconda](https://conda.io/en/latest/miniconda.html)** – eine schlanke Installation, die den `conda`-Paketmanager für verschiedene Python-**virtuelle Umgebungen** unterstützt.

Nachdem Sie Miniconda installiert haben, müssen Sie das Repository klonen und eine virtuelle Umgebung für diesen Kurs erstellen:

```bash
git clone http://github.com/microsoft/ai-for-beginners
cd ai-for-beginners
conda env create --name ai4beg --file .devcontainer/environment.yml
conda activate ai4beg
```

### Verwendung von Visual Studio Code mit Python-Erweiterung

Die wahrscheinlich beste Möglichkeit, das Curriculum zu nutzen, besteht darin, es in [Visual Studio Code](http://code.visualstudio.com/?WT.mc_id=academic-77998-cacaste) mit der [Python-Erweiterung](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-77998-cacaste) zu öffnen.

> **Hinweis**: Sobald Sie das Verzeichnis in VS Code klonen und öffnen, wird Ihnen automatisch vorgeschlagen, die Python-Erweiterungen zu installieren. Sie müssen auch Miniconda wie oben beschrieben installieren.

> **Hinweis**: Wenn VS Code Ihnen vorschlägt, das Repository in einem Container zu öffnen, sollten Sie dies ablehnen, um die lokale Python-Installation zu verwenden.

### Verwendung von Jupyter im Browser

Sie können die Jupyter-Umgebung auch direkt im Browser auf Ihrem eigenen Computer nutzen. Tatsächlich bieten sowohl das klassische Jupyter als auch Jupyter Hub eine recht komfortable Entwicklungsumgebung mit Autovervollständigung, Syntaxhervorhebung usw.

Um Jupyter lokal zu starten, gehen Sie in das Verzeichnis des Kurses und führen Sie aus:

```bash
jupyter notebook
```  
oder  
```bash
jupyterhub
```  
Anschließend können Sie zu einer der `.ipynb`-Dateien navigieren, diese öffnen und mit der Arbeit beginnen.

### Ausführung in einem Container

Eine Alternative zur Python-Installation besteht darin, den Code in einem Container auszuführen. Da unser Repository einen speziellen `.devcontainer`-Ordner enthält, der Anweisungen zum Erstellen eines Containers für dieses Repository bereitstellt, wird Ihnen VS Code anbieten, den Code in einem Container zu öffnen. Dies erfordert die Installation von Docker und ist auch etwas komplexer, daher empfehlen wir dies eher erfahrenen Nutzern.

## Ausführung in der Cloud

Wenn Sie Python nicht lokal installieren möchten und Zugriff auf Cloud-Ressourcen haben, ist eine gute Alternative, den Code in der Cloud auszuführen. Es gibt mehrere Möglichkeiten, dies zu tun:

* Verwendung von **[GitHub Codespaces](https://github.com/features/codespaces)**, einer virtuellen Umgebung, die für Sie auf GitHub erstellt wird und über die Browseroberfläche von VS Code zugänglich ist. Wenn Sie Zugriff auf Codespaces haben, können Sie einfach auf die Schaltfläche **Code** im Repository klicken, einen Codespace starten und sofort loslegen.
* Verwendung von **[Binder](https://mybinder.org/v2/gh/microsoft/ai-for-beginners/HEAD)**. [Binder](https://mybinder.org) bietet kostenlose Rechenressourcen in der Cloud, mit denen Sie Code auf GitHub testen können. Auf der Startseite gibt es eine Schaltfläche, um das Repository in Binder zu öffnen – dies sollte Sie schnell zur Binder-Seite führen, die den zugrunde liegenden Container erstellt und nahtlos die Jupyter-Weboberfläche startet.

> **Hinweis**: Um Missbrauch zu verhindern, hat Binder den Zugriff auf einige Webressourcen blockiert. Dies kann dazu führen, dass bestimmter Code, der Modelle und/oder Datensätze aus dem öffentlichen Internet abruft, nicht funktioniert. Sie müssen möglicherweise Workarounds finden. Außerdem sind die von Binder bereitgestellten Rechenressourcen recht begrenzt, sodass das Training, insbesondere in späteren komplexeren Lektionen, langsam sein wird.

## Ausführung in der Cloud mit GPU

Einige der späteren Lektionen in diesem Curriculum profitieren stark von GPU-Unterstützung, da das Training sonst extrem langsam wäre. Es gibt einige Optionen, die Sie nutzen können, insbesondere wenn Sie über [Azure for Students](https://azure.microsoft.com/free/students/?WT.mc_id=academic-77998-cacaste) oder Ihre Institution Zugang zur Cloud haben:

* Erstellen Sie eine [Data Science Virtual Machine](https://docs.microsoft.com/learn/modules/intro-to-azure-data-science-virtual-machine/?WT.mc_id=academic-77998-cacaste) und verbinden Sie sich über Jupyter mit ihr. Sie können das Repository dann direkt auf die Maschine klonen und mit dem Lernen beginnen. NC-Serien-VMs unterstützen GPUs.

> **Hinweis**: Einige Abonnements, einschließlich Azure for Students, bieten standardmäßig keine GPU-Unterstützung. Sie müssen möglicherweise zusätzliche GPU-Kerne über eine technische Supportanfrage anfordern.

* Erstellen Sie einen [Azure Machine Learning Workspace](https://azure.microsoft.com/services/machine-learning/?WT.mc_id=academic-77998-cacaste) und nutzen Sie dort die Notebook-Funktion. [Dieses Video](https://azure-for-academics.github.io/quickstart/azureml-papers/) zeigt, wie Sie ein Repository in ein Azure ML-Notebook klonen und es verwenden können.

Sie können auch Google Colab verwenden, das einige kostenlose GPU-Ressourcen bietet, und Jupyter-Notebooks hochladen, um sie dort Schritt für Schritt auszuführen.

**Haftungsausschluss**:  
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner ursprünglichen Sprache sollte als maßgebliche Quelle betrachtet werden. Für kritische Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die sich aus der Nutzung dieser Übersetzung ergeben.