# Verarbeitung natürlicher Sprache

![Zusammenfassung der NLP-Aufgaben in einer Skizze](../../../../lessons/sketchnotes/ai-nlp.png)

In diesem Abschnitt konzentrieren wir uns darauf, neuronale Netzwerke für Aufgaben im Bereich der **Verarbeitung natürlicher Sprache (Natural Language Processing, NLP)** einzusetzen. Es gibt viele NLP-Probleme, die wir möchten, dass Computer lösen können:

* **Textklassifikation** ist ein typisches Klassifikationsproblem, das sich auf Textsequenzen bezieht. Beispiele sind das Klassifizieren von E-Mails als Spam oder Nicht-Spam oder das Kategorisieren von Artikeln in Sport, Wirtschaft, Politik usw. Auch bei der Entwicklung von Chatbots müssen wir oft verstehen, was ein Benutzer sagen wollte – in diesem Fall handelt es sich um **Intent-Klassifikation**. Häufig müssen wir bei der Intent-Klassifikation mit vielen Kategorien umgehen.
* **Sentiment-Analyse** ist ein typisches Regressionsproblem, bei dem wir einer Zahl (einem Sentiment) zuordnen müssen, wie positiv/negativ die Bedeutung eines Satzes ist. Eine fortgeschrittenere Version der Sentiment-Analyse ist die **aspektbasierte Sentiment-Analyse** (ABSA), bei der wir das Sentiment nicht dem gesamten Satz, sondern verschiedenen Teilen davon (Aspekten) zuordnen, z. B. *In diesem Restaurant mochte ich die Küche, aber die Atmosphäre war schrecklich*.
* **Erkennung benannter Entitäten** (Named Entity Recognition, NER) bezieht sich auf das Problem, bestimmte Entitäten aus Text zu extrahieren. Zum Beispiel müssen wir verstehen, dass in der Phrase *Ich muss morgen nach Paris fliegen* das Wort *morgen* ein DATUM und *Paris* ein ORT ist.  
* **Schlüsselwortextraktion** ist ähnlich wie NER, aber hier müssen wir automatisch Wörter extrahieren, die für die Bedeutung des Satzes wichtig sind, ohne vorheriges Training für spezifische Entitätstypen.
* **Text-Clustering** kann nützlich sein, wenn wir ähnliche Sätze gruppieren möchten, z. B. ähnliche Anfragen in technischen Supportgesprächen.
* **Fragebeantwortung** bezieht sich auf die Fähigkeit eines Modells, eine spezifische Frage zu beantworten. Das Modell erhält einen Textabschnitt und eine Frage als Eingaben und muss eine Stelle im Text angeben, an der die Antwort auf die Frage enthalten ist (oder manchmal die Antwort generieren).
* **Textgenerierung** ist die Fähigkeit eines Modells, neuen Text zu generieren. Dies kann als Klassifikationsaufgabe betrachtet werden, bei der der nächste Buchstabe/das nächste Wort basierend auf einem *Textprompt* vorhergesagt wird. Fortgeschrittene Textgenerierungsmodelle wie GPT-3 können andere NLP-Aufgaben wie Klassifikation mithilfe einer Technik namens [Prompt Programming](https://towardsdatascience.com/software-3-0-how-prompting-will-change-the-rules-of-the-game-a982fbfe1e0) oder [Prompt Engineering](https://medium.com/swlh/openai-gpt-3-and-prompt-engineering-dcdc2c5fcd29) lösen.
* **Textzusammenfassung** ist eine Technik, bei der wir möchten, dass ein Computer einen langen Text "liest" und ihn in wenigen Sätzen zusammenfasst.
* **Maschinelle Übersetzung** kann als Kombination aus Textverständnis in einer Sprache und Textgenerierung in einer anderen betrachtet werden.

Anfangs wurden die meisten NLP-Aufgaben mit traditionellen Methoden wie Grammatiken gelöst. Zum Beispiel wurden in der maschinellen Übersetzung Parser verwendet, um einen Ausgangssatz in einen Syntaxbaum zu transformieren, dann wurden semantische Strukturen höherer Ebene extrahiert, um die Bedeutung des Satzes darzustellen, und basierend auf dieser Bedeutung und der Grammatik der Zielsprache wurde das Ergebnis generiert. Heutzutage werden viele NLP-Aufgaben effektiver mit neuronalen Netzwerken gelöst.

> Viele klassische NLP-Methoden sind in der Python-Bibliothek [Natural Language Processing Toolkit (NLTK)](https://www.nltk.org) implementiert. Es gibt ein großartiges [NLTK-Buch](https://www.nltk.org/book/), das online verfügbar ist und zeigt, wie verschiedene NLP-Aufgaben mit NLTK gelöst werden können.

In unserem Kurs konzentrieren wir uns hauptsächlich auf die Verwendung neuronaler Netzwerke für NLP und verwenden NLTK, wo es erforderlich ist.

Wir haben bereits gelernt, wie neuronale Netzwerke für tabellarische Daten und Bilder verwendet werden können. Der Hauptunterschied zwischen diesen Datentypen und Text besteht darin, dass Text eine Sequenz variabler Länge ist, während die Eingabegröße bei Bildern im Voraus bekannt ist. Während konvolutionale Netzwerke Muster aus Eingabedaten extrahieren können, sind Muster in Texten komplexer. Zum Beispiel kann eine Verneinung vom Subjekt durch viele Wörter getrennt sein (z. B. *Ich mag keine Orangen* vs. *Ich mag diese großen bunten leckeren Orangen nicht*), und das sollte dennoch als ein Muster interpretiert werden. Daher müssen wir zur Verarbeitung von Sprache neue Arten von neuronalen Netzwerken einführen, wie z. B. *rekurrente Netzwerke* und *Transformers*.

## Bibliotheken installieren

Wenn Sie eine lokale Python-Installation verwenden, um diesen Kurs auszuführen, müssen Sie möglicherweise alle erforderlichen Bibliotheken für NLP mit den folgenden Befehlen installieren:

**Für PyTorch**  
```bash
pip install -r requirements-torch.txt
```  
**Für TensorFlow**  
```bash
pip install -r requirements-tf.txt
```  

> Sie können NLP mit TensorFlow auf [Microsoft Learn](https://docs.microsoft.com/learn/modules/intro-natural-language-processing-tensorflow/?WT.mc_id=academic-77998-cacaste) ausprobieren.

## GPU-Warnung

In diesem Abschnitt werden wir in einigen Beispielen recht große Modelle trainieren.  
* **Verwenden Sie einen Computer mit GPU-Unterstützung**: Es wird empfohlen, Ihre Notebooks auf einem Computer mit GPU-Unterstützung auszuführen, um die Wartezeiten beim Arbeiten mit großen Modellen zu reduzieren.  
* **GPU-Speicherbeschränkungen**: Das Ausführen auf einer GPU kann dazu führen, dass der GPU-Speicher ausgeht, insbesondere beim Training großer Modelle.  
* **GPU-Speicherverbrauch**: Die Menge des während des Trainings verbrauchten GPU-Speichers hängt von verschiedenen Faktoren ab, einschließlich der Minibatch-Größe.  
* **Minimieren Sie die Minibatch-Größe**: Wenn Sie auf GPU-Speicherprobleme stoßen, sollten Sie die Minibatch-Größe in Ihrem Code reduzieren.  
* **TensorFlow GPU-Speicherfreigabe**: Ältere Versionen von TensorFlow geben den GPU-Speicher möglicherweise nicht korrekt frei, wenn mehrere Modelle innerhalb eines Python-Kernels trainiert werden. Um den GPU-Speicher effektiv zu verwalten, können Sie TensorFlow so konfigurieren, dass GPU-Speicher nur bei Bedarf zugewiesen wird.  
* **Code-Einbindung**: Um TensorFlow so einzustellen, dass GPU-Speicher nur bei Bedarf wächst, fügen Sie den folgenden Code in Ihre Notebooks ein:

```python
physical_devices = tf.config.list_physical_devices('GPU') 
if len(physical_devices)>0:
    tf.config.experimental.set_memory_growth(physical_devices[0], True) 
```  

Wenn Sie daran interessiert sind, NLP aus der Perspektive des klassischen maschinellen Lernens zu lernen, besuchen Sie [diese Lektionenreihe](https://github.com/microsoft/ML-For-Beginners/tree/main/6-NLP).

## In diesem Abschnitt
In diesem Abschnitt werden wir lernen:

* [Text als Tensoren darstellen](13-TextRep/README.md)  
* [Wort-Embeddings](14-Emdeddings/README.md)  
* [Sprachmodellierung](15-LanguageModeling/README.md)  
* [Rekurrente neuronale Netzwerke](16-RNN/README.md)  
* [Generative Netzwerke](17-GenerativeNetworks/README.md)  
* [Transformers](18-Transformers/README.md)  

**Haftungsausschluss**:  
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, weisen wir darauf hin, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner ursprünglichen Sprache sollte als maßgebliche Quelle betrachtet werden. Für kritische Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die aus der Nutzung dieser Übersetzung entstehen.