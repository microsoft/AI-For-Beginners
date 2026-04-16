# Wie man den Code ausführt

Dieses Curriculum enthält viele ausführbare Beispiele und Labs, die Sie ausführen möchten. Um dies zu tun, benötigen Sie die Möglichkeit, Python-Code in Jupyter Notebooks auszuführen, die als Teil dieses Curriculums bereitgestellt werden. Sie haben mehrere Optionen, um den Code auszuführen:

## Lokal auf Ihrem Computer ausführen

Um den Code lokal auf Ihrem Computer auszuführen, ist eine Python-Installation erforderlich. Eine Empfehlung ist die Installation von **[miniconda](https://conda.io/en/latest/miniconda.html)** – es ist eine eher leichtgewichtige Installation, die den `conda` Paketmanager für verschiedene Python-**virtuelle Umgebungen** unterstützt.

Nachdem Sie miniconda installiert haben, klonen Sie das Repository und erstellen eine virtuelle Umgebung, die für diesen Kurs verwendet wird:

```bash
git clone http://github.com/microsoft/ai-for-beginners
cd ai-for-beginners
conda env create --name ai4beg --file .devcontainer/environment.yml
conda activate ai4beg
```

### Verwendung von Visual Studio Code mit Python-Erweiterung

Dieses Curriculum wird am besten verwendet, wenn es in [Visual Studio Code](http://code.visualstudio.com/?WT.mc_id=academic-77998-cacaste) mit der [Python-Erweiterung](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-77998-cacaste) geöffnet wird.

> **Hinweis**: Sobald Sie das Verzeichnis klonen und in VS Code öffnen, wird automatisch vorgeschlagen, Python-Erweiterungen zu installieren. Sie müssen auch miniconda wie oben beschrieben installieren.

> **Hinweis**: Wenn VS Code vorschlägt, das Repository in einem Container erneut zu öffnen, sollten Sie dies ablehnen, um die lokale Python-Installation zu verwenden.

### Verwendung von Jupyter im Browser

Sie können auch eine Jupyter-Umgebung aus dem Browser auf Ihrem eigenen Computer verwenden. Sowohl klassisches Jupyter als auch JupyterHub bieten eine bequeme Entwicklungsumgebung mit Autovervollständigung, Code-Hervorhebung usw.

Um Jupyter lokal zu starten, wechseln Sie in das Verzeichnis des Kurses und führen aus:

```bash
jupyter notebook
```
oder
```bash
jupyterhub
```
Sie können dann zu einer beliebigen `.ipynb`-Datei navigieren, sie öffnen und mit der Arbeit beginnen.

### Ausführen in einem Container

Eine Alternative zur Python-Installation wäre das Ausführen des Codes in einem Container. Da unser Repository einen speziellen `.devcontainer`-Ordner bereitstellt, der beschreibt, wie ein Container für dieses Repo gebaut wird, bietet VS Code die Möglichkeit, den Code in einem Container erneut zu öffnen. Dies erfordert die Installation von Docker und wäre auch komplexer, daher empfehlen wir dies eher erfahrenen Nutzern.

## Ausführung in der Cloud

Wenn Sie Python nicht lokal installieren möchten und Zugriff auf Cloud-Ressourcen haben – eine gute Alternative ist es, den Code in der Cloud auszuführen. Es gibt mehrere Möglichkeiten, dies zu tun:

* Verwendung von **[GitHub Codespaces](https://github.com/features/codespaces)**, einer virtuellen Umgebung, die für Sie auf GitHub erstellt wird und über eine VS Code-Browseroberfläche zugänglich ist. Wenn Sie Zugriff auf Codespaces haben, können Sie einfach auf die **Code**-Schaltfläche im Repo klicken, einen Codespace starten und sofort loslegen.
* Verwendung von **[Binder](https://mybinder.org/v2/gh/microsoft/ai-for-beginners/HEAD)**. [Binder](https://mybinder.org) bietet kostenfreie Cloud-Computing-Ressourcen für Personen wie Sie, um Code auf GitHub auszuprobieren. Es gibt eine Schaltfläche auf der Startseite, um das Repository in Binder zu öffnen – dies sollte Sie schnell auf die Binder-Seite bringen, die einen zugrundeliegenden Container baut und nahtlos eine Jupyter-Weboberfläche für Sie startet.

> **Hinweis**: Zur Vermeidung von Missbrauch hat Binder den Zugriff auf einige Webressourcen blockiert. Dies kann verhindern, dass ein Teil des Codes funktioniert, der Modelle und/oder Datensätze aus dem öffentlichen Internet lädt. Sie müssen möglicherweise einige Umgehungen finden. Außerdem sind die von Binder bereitgestellten Rechenressourcen eher grundlegend, sodass das Training langsam sein wird, besonders in späteren, komplexeren Lektionen.

## Ausführung in der Cloud mit GPU

Einige der späteren Lektionen in diesem Curriculum würden erheblich von GPU-Unterstützung profitieren. Das Modelltraining kann sonst sehr langsam sein. Es gibt einige Möglichkeiten, die Sie nutzen können, besonders wenn Sie über [Azure for Students](https://azure.microsoft.com/free/students/?WT.mc_id=academic-77998-cacaste) oder über Ihre Institution Zugang zur Cloud haben:

* Erstellen Sie eine [Data Science Virtual Machine](https://docs.microsoft.com/learn/modules/intro-to-azure-data-science-virtual-machine/?WT.mc_id=academic-77998-cacaste) und verbinden Sie sich über Jupyter mit ihr. Sie können dann das Repo direkt auf die Maschine klonen und mit dem Lernen beginnen. NC-Serien VMs unterstützen GPU.

> **Hinweis**: Einige Abonnements, einschließlich Azure for Students, bieten nicht standardmäßig GPU-Unterstützung. Möglicherweise müssen Sie zusätzliche GPU-Kerne per technischem Supportantrag anfordern.

* Erstellen Sie einen [Azure Machine Learning Workspace](https://azure.microsoft.com/services/machine-learning/?WT.mc_id=academic-77998-cacaste) und verwenden Sie dort die Notizbuchfunktion. [Dieses Video](https://azure-for-academics.github.io/quickstart/azureml-papers/) zeigt, wie man ein Repository in ein Azure ML-Notizbuch klont und es verwendet.

Sie können auch Google Colab verwenden, das über eine kostenlose GPU-Unterstützung verfügt, und Jupyter Notebooks dort hochladen, um sie einzeln auszuführen.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Haftungsausschluss**:  
Dieses Dokument wurde mithilfe des KI-Übersetzungsdienstes [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir bemüht sind, eine genaue Übersetzung zu gewährleisten, sollten Sie beachten, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner Ursprungssprache gilt als verbindliche Quelle. Für wichtige Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die aus der Nutzung dieser Übersetzung entstehen.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->