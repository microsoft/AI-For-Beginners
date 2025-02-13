# Vorgebildete große Sprachmodelle

In all unseren vorherigen Aufgaben haben wir ein neuronales Netzwerk trainiert, um eine bestimmte Aufgabe mit einem beschrifteten Datensatz auszuführen. Bei großen Transformermodellen wie BERT nutzen wir Sprachmodellierung in selbstüberwachter Weise, um ein Sprachmodell zu erstellen, das dann für spezifische nachgelagerte Aufgaben mit weiterem domänenspezifischem Training spezialisiert wird. Es wurde jedoch gezeigt, dass große Sprachmodelle viele Aufgaben auch ohne jegliches domänenspezifisches Training lösen können. Eine Familie von Modellen, die dazu in der Lage ist, wird als **GPT** bezeichnet: Generative Pre-Trained Transformer.

## [Vorlesungsquiz](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/120)

## Textgenerierung und Perplexität

Die Idee, dass ein neuronales Netzwerk in der Lage ist, allgemeine Aufgaben ohne nachgelagertes Training auszuführen, wird im Papier [Language Models are Unsupervised Multitask Learners](https://cdn.openai.com/better-language-models/language_models_are_unsupervised_multitask_learners.pdf) präsentiert. Die Hauptidee ist, dass viele andere Aufgaben mit **Textgenerierung** modelliert werden können, da das Verständnis von Text im Wesentlichen bedeutet, in der Lage zu sein, ihn zu produzieren. Da das Modell auf einer riesigen Menge an Text trainiert wurde, die menschliches Wissen umfasst, wird es auch über eine Vielzahl von Themen informiert.

> Das Verständnis und die Fähigkeit, Text zu produzieren, bedeutet auch, etwas über die Welt um uns herum zu wissen. Menschen lernen auch in großem Maße durch Lesen, und das GPT-Netzwerk ist in dieser Hinsicht ähnlich.

Textgenerierungsnetzwerke funktionieren, indem sie die Wahrscheinlichkeit des nächsten Wortes $$P(w_N)$$ vorhersagen. Die bedingungslose Wahrscheinlichkeit des nächsten Wortes entspricht jedoch der Häufigkeit dieses Wortes im Textkorpus. GPT kann uns die **bedingte Wahrscheinlichkeit** des nächsten Wortes geben, basierend auf den vorherigen: $$P(w_N | w_{n-1}, ..., w_0)$$

> Sie können mehr über Wahrscheinlichkeiten in unserem [Data Science for Beginners Curriculum](https://github.com/microsoft/Data-Science-For-Beginners/tree/main/1-Introduction/04-stats-and-probability) lesen.

Die Qualität des sprachgenerierenden Modells kann mit **Perplexität** definiert werden. Es ist eine intrinsische Metrik, die es uns ermöglicht, die Modellqualität ohne einen aufgaben-spezifischen Datensatz zu messen. Sie basiert auf dem Konzept der *Wahrscheinlichkeit eines Satzes* – das Modell weist einem Satz, der wahrscheinlich echt ist (d.h. das Modell ist nicht **verwirrt** von ihm), eine hohe Wahrscheinlichkeit zu, und einer niedrigen Wahrscheinlichkeit für Sätze, die weniger Sinn machen (z.B. *Kann es was tun?*). Wenn wir unserem Modell Sätze aus einem echten Textkorpus geben, erwarten wir, dass sie eine hohe Wahrscheinlichkeit und eine niedrige **Perplexität** haben. Mathematisch wird es als normalisierte inverse Wahrscheinlichkeit des Testdatensatzes definiert:
$$
\mathrm{Perplexity}(W) = \sqrt[N]{1\over P(W_1,...,W_N)}
$$ 

**Sie können mit der Textgenerierung den [GPT-gestützten Texteditor von Hugging Face](https://transformer.huggingface.co/doc/gpt2-large) ausprobieren.** In diesem Editor beginnen Sie, Ihren Text zu schreiben, und durch Drücken von **[TAB]** erhalten Sie mehrere Vervollständigungsoptionen. Wenn diese zu kurz sind oder Sie nicht zufrieden sind, drücken Sie erneut [TAB], und Sie erhalten weitere Optionen, einschließlich längerer Textabschnitte.

## GPT ist eine Familie

GPT ist kein einzelnes Modell, sondern eine Sammlung von Modellen, die von [OpenAI](https://openai.com) entwickelt und trainiert wurden. 

Unter den GPT-Modellen haben wir:

| [GPT-2](https://huggingface.co/docs/transformers/model_doc/gpt2#openai-gpt2) | [GPT 3](https://openai.com/research/language-models-are-few-shot-learners) | [GPT-4](https://openai.com/gpt-4) |
| -- | -- | -- |
| Sprachmodell mit bis zu 1,5 Milliarden Parametern. | Sprachmodell mit bis zu 175 Milliarden Parametern | 100T Parameter und akzeptiert sowohl Bild- als auch Texteingaben und gibt Text aus. |


Die Modelle GPT-3 und GPT-4 sind [als kognitiver Dienst von Microsoft Azure](https://azure.microsoft.com/en-us/services/cognitive-services/openai-service/#overview?WT.mc_id=academic-77998-cacaste) sowie als [OpenAI API](https://openai.com/api/) verfügbar.

## Prompt-Engineering

Da GPT auf riesigen Datenmengen trainiert wurde, um Sprache und Code zu verstehen, liefern sie Ausgaben als Antwort auf Eingaben (Prompts). Prompts sind die Eingaben oder Abfragen an GPT, bei denen man den Modellen Anweisungen zu den Aufgaben gibt, die sie als Nächstes ausführen sollen. Um ein gewünschtes Ergebnis zu erzielen, benötigen Sie den effektivsten Prompt, der die Auswahl der richtigen Wörter, Formate, Phrasen oder sogar Symbole umfasst. Dieser Ansatz wird als [Prompt Engineering](https://learn.microsoft.com/en-us/shows/ai-show/the-basics-of-prompt-engineering-with-azure-openai-service?WT.mc_id=academic-77998-bethanycheum) bezeichnet.

[Diese Dokumentation](https://learn.microsoft.com/en-us/semantic-kernel/prompt-engineering/?WT.mc_id=academic-77998-bethanycheum) bietet Ihnen weitere Informationen zum Prompt-Engineering.

## ✍️ Beispielnotizbuch: [Spielen mit OpenAI-GPT](../../../../../lessons/5-NLP/20-LangModels/GPT-PyTorch.ipynb)

Setzen Sie Ihr Lernen in den folgenden Notizbüchern fort:

* [Textgenerierung mit OpenAI-GPT und Hugging Face Transformers](../../../../../lessons/5-NLP/20-LangModels/GPT-PyTorch.ipynb)

## Fazit

Neue allgemeine vortrainierte Sprachmodelle modellieren nicht nur die Sprachstruktur, sondern enthalten auch eine riesige Menge an natürlicher Sprache. Daher können sie effektiv eingesetzt werden, um einige NLP-Aufgaben in Zero-Shot- oder Few-Shot-Einstellungen zu lösen.

## [Nachlesungsquiz](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/220)

**Haftungsausschluss**:  
Dieses Dokument wurde mit maschinellen KI-Übersetzungsdiensten übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner ursprünglichen Sprache sollte als die maßgebliche Quelle betrachtet werden. Für kritische Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die aus der Verwendung dieser Übersetzung entstehen.