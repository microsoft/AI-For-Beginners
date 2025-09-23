<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "2efbb183384a50f0fc0cde02534d912f",
  "translation_date": "2025-08-24T10:20:36+00:00",
  "source_file": "lessons/5-NLP/20-LangModels/README.md",
  "language_code": "de"
}
-->
# Vorgefertigte große Sprachmodelle

In all unseren bisherigen Aufgaben haben wir ein neuronales Netzwerk trainiert, um eine bestimmte Aufgabe mithilfe eines beschrifteten Datensatzes auszuführen. Mit großen Transformermodellen wie BERT verwenden wir Sprachmodellierung in selbstüberwachter Weise, um ein Sprachmodell zu erstellen, das anschließend durch weitere domänenspezifische Trainings für spezifische nachgelagerte Aufgaben spezialisiert wird. Es wurde jedoch gezeigt, dass große Sprachmodelle viele Aufgaben auch ohne jegliches domänenspezifisches Training lösen können. Eine Familie von Modellen, die dazu in der Lage ist, wird **GPT** genannt: Generative Pre-Trained Transformer.

## [Quiz vor der Vorlesung](https://ff-quizzes.netlify.app/en/ai/quiz/39)

## Textgenerierung und Perplexität

Die Idee, dass ein neuronales Netzwerk allgemeine Aufgaben ohne nachgelagertes Training ausführen kann, wird im Papier [Language Models are Unsupervised Multitask Learners](https://cdn.openai.com/better-language-models/language_models_are_unsupervised_multitask_learners.pdf) vorgestellt. Der Hauptgedanke ist, dass viele andere Aufgaben mithilfe der **Textgenerierung** modelliert werden können, da das Verstehen von Text im Wesentlichen bedeutet, ihn produzieren zu können. Da das Modell auf einer riesigen Menge an Text trainiert wird, die menschliches Wissen umfasst, wird es auch über eine Vielzahl von Themen informiert.

> Text zu verstehen und produzieren zu können, bedeutet auch, etwas über die Welt um uns herum zu wissen. Menschen lernen ebenfalls in großem Maße durch Lesen, und das GPT-Netzwerk ist in dieser Hinsicht ähnlich.

Textgenerierungsnetzwerke arbeiten, indem sie die Wahrscheinlichkeit des nächsten Wortes $$P(w_N)$$ vorhersagen. Die bedingungslose Wahrscheinlichkeit des nächsten Wortes entspricht jedoch der Häufigkeit dieses Wortes im Textkorpus. GPT ist in der Lage, uns die **bedingte Wahrscheinlichkeit** des nächsten Wortes zu geben, basierend auf den vorherigen: $$P(w_N | w_{n-1}, ..., w_0)$$

> Mehr über Wahrscheinlichkeiten können Sie in unserem [Data Science für Anfänger Curriculum](https://github.com/microsoft/Data-Science-For-Beginners/tree/main/1-Introduction/04-stats-and-probability) lesen.

Die Qualität eines sprachgenerierenden Modells kann mithilfe der **Perplexität** definiert werden. Es handelt sich um eine intrinsische Metrik, die es uns ermöglicht, die Modellqualität ohne einen aufgabenspezifischen Datensatz zu messen. Sie basiert auf dem Konzept der *Wahrscheinlichkeit eines Satzes* – das Modell weist einem Satz, der wahrscheinlich real ist (d.h. das Modell ist nicht **verwirrt** davon), eine hohe Wahrscheinlichkeit zu und Sätzen, die weniger Sinn ergeben (z.B. *Kann es was tun?*), eine niedrige Wahrscheinlichkeit. Wenn wir unserem Modell Sätze aus einem echten Textkorpus geben, erwarten wir, dass sie eine hohe Wahrscheinlichkeit und eine niedrige **Perplexität** haben. Mathematisch wird sie als normalisierte inverse Wahrscheinlichkeit des Testsets definiert:
$$
\mathrm{Perplexity}(W) = \sqrt[N]{1\over P(W_1,...,W_N)}
$$ 

**Sie können mit der Textgenerierung experimentieren, indem Sie den [GPT-gestützten Texteditor von Hugging Face](https://transformer.huggingface.co/doc/gpt2-large) verwenden.** In diesem Editor beginnen Sie, Ihren Text zu schreiben, und durch Drücken von **[TAB]** werden Ihnen mehrere Abschlussoptionen angeboten. Wenn diese zu kurz sind oder Sie nicht zufrieden sind, drücken Sie erneut [TAB], und Sie erhalten weitere Optionen, einschließlich längerer Textstücke.

## GPT ist eine Familie

GPT ist kein einzelnes Modell, sondern vielmehr eine Sammlung von Modellen, die von [OpenAI](https://openai.com) entwickelt und trainiert wurden.

Innerhalb der GPT-Modelle haben wir:

| [GPT-2](https://huggingface.co/docs/transformers/model_doc/gpt2#openai-gpt2) | [GPT 3](https://openai.com/research/language-models-are-few-shot-learners) | [GPT-4](https://openai.com/gpt-4) |
| -- | -- | -- |
|Sprachmodell mit bis zu 1,5 Milliarden Parametern. | Sprachmodell mit bis zu 175 Milliarden Parametern | 100T Parameter und akzeptiert sowohl Bild- als auch Texteingaben und gibt Text aus. |

Die GPT-3- und GPT-4-Modelle sind verfügbar [als kognitiver Dienst von Microsoft Azure](https://azure.microsoft.com/en-us/services/cognitive-services/openai-service/#overview?WT.mc_id=academic-77998-cacaste) und als [OpenAI API](https://openai.com/api/).

## Prompt Engineering

Da GPT auf großen Datenmengen trainiert wurde, um Sprache und Code zu verstehen, liefert es Ausgaben als Reaktion auf Eingaben (Prompts). Prompts sind GPT-Eingaben oder Abfragen, bei denen man den Modellen Anweisungen zu den Aufgaben gibt, die sie als Nächstes ausführen sollen. Um ein gewünschtes Ergebnis zu erzielen, benötigt man den effektivsten Prompt, der die Auswahl der richtigen Wörter, Formate, Phrasen oder sogar Symbole umfasst. Dieser Ansatz wird [Prompt Engineering](https://learn.microsoft.com/en-us/shows/ai-show/the-basics-of-prompt-engineering-with-azure-openai-service?WT.mc_id=academic-77998-bethanycheum) genannt.

[Diese Dokumentation](https://learn.microsoft.com/en-us/semantic-kernel/prompt-engineering/?WT.mc_id=academic-77998-bethanycheum) bietet Ihnen weitere Informationen zum Prompt Engineering.

## ✍️ Beispiel-Notebook: [Spielen mit OpenAI-GPT](../../../../../lessons/5-NLP/20-LangModels/GPT-PyTorch.ipynb)

Setzen Sie Ihr Lernen in den folgenden Notebooks fort:

* [Textgenerierung mit OpenAI-GPT und Hugging Face Transformers](../../../../../lessons/5-NLP/20-LangModels/GPT-PyTorch.ipynb)

## Fazit

Neue allgemeine vortrainierte Sprachmodelle modellieren nicht nur die Sprachstruktur, sondern enthalten auch eine große Menge an natürlicher Sprache. Daher können sie effektiv verwendet werden, um einige NLP-Aufgaben in Zero-Shot- oder Few-Shot-Szenarien zu lösen.

## [Quiz nach der Vorlesung](https://ff-quizzes.netlify.app/en/ai/quiz/40)

**Haftungsausschluss**:  
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, weisen wir darauf hin, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner ursprünglichen Sprache sollte als maßgebliche Quelle betrachtet werden. Für kritische Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die aus der Nutzung dieser Übersetzung entstehen.