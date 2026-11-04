# Wie man den Code ausführt

Dieses Curriculum enthält viele ausführbare Beispiele und Laborübungen, die Sie ausführen möchten. Dafür benötigen Sie die Möglichkeit, Python-Code in Jupyter-Notebooks auszuführen, die als Teil dieses Curriculums bereitgestellt werden. Sie haben mehrere Optionen, um den Code auszuführen:

## Lokal auf Ihrem Computer ausführen

Um den Code lokal auf Ihrem Computer auszuführen, ist eine Python-Installation erforderlich. Eine Empfehlung ist die Installation von **[miniconda](https://conda.io/en/latest/miniconda.html)** – es ist eine eher leichte Installation, die den `conda` Paketmanager für verschiedene Python-**virtuelle Umgebungen** unterstützt.

Nachdem Sie miniconda installiert haben, klonen Sie das Repository und erstellen eine virtuelle Umgebung, die für diesen Kurs verwendet wird:

```bash
git clone http://github.com/microsoft/ai-for-beginners
cd ai-for-beginners
conda env create --name ai4beg --file .devcontainer/environment.yml
conda activate ai4beg
```

> **Hinweis für Windows**: Wenn die Erstellung der Umgebung beim Installieren von `gdk-pixbuf` mit einem `UnicodeDecodeError` fehlschlägt, der den `gbk` Codec erwähnt, aktivieren Sie den UTF-8-Modus von Python in Ihrem Terminal und versuchen Sie es erneut. Verwenden Sie die Syntax für das von Ihnen genutzte Terminal:
>
> **PowerShell:**
>
> ```powershell
> $env:PYTHONUTF8 = "1"
> conda env create --name ai4beg --file .devcontainer/environment.yml
> ```
>
> **Eingabeaufforderung (`cmd.exe`) oder Anaconda-Eingabeaufforderung:**
>
> ```cmd
> set PYTHONUTF8=1
> conda env create --name ai4beg --file .devcontainer/environment.yml
> ```
>
> **Bash, inklusive Git Bash:**
>
> ```bash
> export PYTHONUTF8=1
> conda env create --name ai4beg --file .devcontainer/environment.yml
> ```
>
> Wenn ein fehlgeschlagener Versuch die `ai4beg` Umgebung zurückgelassen hat, deaktivieren Sie sie und entfernen Sie diese Umgebung, bevor Sie es erneut versuchen. Verwenden Sie zuerst `conda deactivate`, wenn eine Umgebung aktiv ist:
>
> ```text
> conda deactivate
> conda env remove --name ai4beg
> ```

### Verwendung von Visual Studio Code mit Python-Erweiterung

Dieses Curriculum wird am besten verwendet, wenn es in [Visual Studio Code](http://code.visualstudio.com/?WT.mc_id=academic-77998-cacaste) mit der [Python-Erweiterung](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-77998-cacaste) geöffnet wird.

> **Hinweis**: Sobald Sie das Verzeichnis klonen und in VS Code öffnen, wird automatisch vorgeschlagen, Python-Erweiterungen zu installieren. Sie müssen auch miniconda wie oben beschrieben installieren.

> **Hinweis**: Wenn VS Code Ihnen anbietet, das Repository in einem Container neu zu öffnen, sollten Sie dies ablehnen, um die lokale Python-Installation zu verwenden.

### Verwendung von Jupyter im Browser

Sie können auch eine Jupyter-Umgebung aus dem Browser auf Ihrem eigenen Computer nutzen. Sowohl klassisches Jupyter als auch JupyterHub bieten eine bequeme Entwicklungsumgebung mit Autovervollständigung, Code-Hervorhebung usw.

Um Jupyter lokal zu starten, wechseln Sie in das Verzeichnis des Kurses und führen Sie aus:

```bash
jupyter notebook
```
oder
```bash
jupyterhub
```
Sie können dann zu einer der `.ipynb` Dateien navigieren, sie öffnen und mit der Arbeit beginnen.

### Ausführung im Container

Eine Alternative zur Python-Installation wäre die Ausführung des Codes in einem Container. Da unser Repository einen speziellen `.devcontainer` Ordner bereitstellt, der Anweisungen zum Erstellen eines Containers für dieses Repository enthält, bietet VS Code die Möglichkeit, den Code in einem Container neu zu öffnen. Dies erfordert eine Docker-Installation und ist auch komplexer, daher empfehlen wir dies eher erfahrenen Nutzern.

## Ausführung in der Cloud

Wenn Sie Python nicht lokal installieren möchten und Zugriff auf einige Cloud-Ressourcen haben, ist eine gute Alternative, den Code in der Cloud auszuführen. Es gibt verschiedene Möglichkeiten, dies zu tun:

* Verwendung von **[GitHub Codespaces](https://github.com/features/codespaces)**, einer virtuellen Umgebung, die für Sie auf GitHub erstellt wird und über eine VS Code-Browseroberfläche zugänglich ist. Wenn Sie Zugriff auf Codespaces haben, können Sie einfach auf die **Code**-Schaltfläche im Repository klicken, einen Codespace starten und sofort loslegen.
* Verwendung von **[Binder](https://mybinder.org/v2/gh/microsoft/ai-for-beginners/HEAD)**. [Binder](https://mybinder.org) bietet kostenlose Rechenressourcen in der Cloud für Nutzer wie Sie, um Code auf GitHub auszuprobieren. Es gibt auf der Startseite eine Schaltfläche, um das Repository in Binder zu öffnen – so gelangen Sie schnell auf die Binder-Seite, die einen zugrundeliegenden Container aufbaut und eine Jupyter-Weboberfläche nahtlos für Sie startet.

> **Hinweis**: Um Missbrauch zu verhindern, hat Binder den Zugriff auf einige Webressourcen gesperrt. Dies kann verhindern, dass Teile des Codes funktionieren, die Modelle und/oder Datensätze aus dem öffentlichen Internet beziehen. Möglicherweise müssen Sie Workarounds finden. Außerdem sind die von Binder bereitgestellten Rechenressourcen ziemlich einfach, daher wird das Training langsam sein, insbesondere in späteren, komplexeren Lektionen.

## Ausführung in der Cloud mit GPU

Einige der späteren Lektionen in diesem Curriculum profitieren stark von GPU-Unterstützung. Das Training von Modellen kann zum Beispiel ohne diese sehr langsam sein. Es gibt einige Optionen, denen Sie folgen können, insbesondere wenn Sie Zugang zur Cloud über [Azure for Students](https://azure.microsoft.com/free/students/?WT.mc_id=academic-77998-cacaste) oder Ihre Institution haben:

* Erstellen Sie eine [Data Science Virtual Machine](https://docs.microsoft.com/learn/modules/intro-to-azure-data-science-virtual-machine/?WT.mc_id=academic-77998-cacaste) und verbinden Sie sich über Jupyter damit. Sie können dann das Repository direkt auf die Maschine klonen und mit dem Lernen beginnen. NC-Serie VMs verfügen über GPU-Unterstützung.

> **Hinweis**: Einige Abonnements, einschließlich Azure for Students, bieten nicht von Haus aus GPU-Unterstützung. Möglicherweise müssen Sie weitere GPU-Kerne über eine technische Supportanfrage anfordern.

* Erstellen Sie einen [Azure Machine Learning Workspace](https://azure.microsoft.com/services/machine-learning/?WT.mc_id=academic-77998-cacaste) und nutzen Sie dort die Notebook-Funktion. [Dieses Video](https://azure-for-academics.github.io/quickstart/azureml-papers/) zeigt, wie man ein Repository in ein Azure ML Notebook klont und es nutzt.

Sie können auch Google Colab verwenden, das einige kostenlose GPU-Unterstützung bietet, und Jupyter-Notebooks dort hochladen, um sie einzeln auszuführen.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Haftungsausschluss**:
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner Ursprungssprache gilt als maßgebliche Quelle. Bei kritischen Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die aus der Verwendung dieser Übersetzung entstehen.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->