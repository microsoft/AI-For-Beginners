# Vorgefertigte große Sprachmodelle

In all unseren bisherigen Aufgaben haben wir ein neuronales Netzwerk darauf trainiert, eine bestimmte Aufgabe mithilfe eines beschrifteten Datensatzes auszuführen. Bei großen Transformermodellen wie BERT verwenden wir Sprachmodellierung in selbstüberwachter Weise, um ein Sprachmodell zu erstellen, das anschließend durch weitere domänenspezifische Trainings für spezifische Downstream-Aufgaben spezialisiert wird. Es wurde jedoch gezeigt, dass große Sprachmodelle viele Aufgaben auch ohne jegliches domänenspezifisches Training lösen können. Eine Familie von Modellen, die dazu in der Lage ist, wird als **GPT** bezeichnet: Generative Pre-Trained Transformer.

## [Quiz vor der Vorlesung](https://ff-quizzes.netlify.app/en/ai/quiz/39)

## Textgenerierung und Perplexität

Die Idee, dass ein neuronales Netzwerk allgemeine Aufgaben ohne Downstream-Training ausführen kann, wird im Paper [Language Models are Unsupervised Multitask Learners](https://cdn.openai.com/better-language-models/language_models_are_unsupervised_multitask_learners.pdf) vorgestellt. Der Hauptgedanke ist, dass viele andere Aufgaben mithilfe der **Textgenerierung** modelliert werden können, da das Verstehen von Text im Wesentlichen bedeutet, in der Lage zu sein, ihn zu produzieren. Da das Modell auf einer riesigen Menge an Text trainiert wird, die menschliches Wissen umfasst, wird es auch über eine Vielzahl von Themen informiert.

> Text zu verstehen und zu produzieren bedeutet auch, etwas über die Welt um uns herum zu wissen. Menschen lernen ebenfalls in großem Maße durch Lesen, und das GPT-Netzwerk ist in dieser Hinsicht ähnlich.

Textgenerierungsnetzwerke arbeiten, indem sie die Wahrscheinlichkeit des nächsten Wortes $$P(w_N)$$ vorhersagen. Die unbedingte Wahrscheinlichkeit des nächsten Wortes entspricht jedoch der Häufigkeit dieses Wortes im Textkorpus. GPT ist in der Lage, uns die **bedingte Wahrscheinlichkeit** des nächsten Wortes zu geben, basierend auf den vorherigen Wörtern: $$P(w_N | w_{n-1}, ..., w_0)$$

> Mehr über Wahrscheinlichkeiten kannst du in unserem [Data Science for Beginners Curriculum](https://github.com/microsoft/Data-Science-For-Beginners/tree/main/1-Introduction/04-stats-and-probability) nachlesen.

Die Qualität eines sprachgenerierenden Modells kann durch die **Perplexität** definiert werden. Dies ist eine intrinsische Metrik, die es uns ermöglicht, die Modellqualität ohne einen aufgabenspezifischen Datensatz zu messen. Sie basiert auf dem Konzept der *Wahrscheinlichkeit eines Satzes* – das Modell weist einem Satz, der wahrscheinlich real ist (d. h. das Modell ist nicht **verwirrt** davon), eine hohe Wahrscheinlichkeit zu und Sätzen, die weniger Sinn ergeben (z. B. *Kann es was tun?*), eine niedrige Wahrscheinlichkeit. Wenn wir unserem Modell Sätze aus einem echten Textkorpus geben, erwarten wir, dass diese eine hohe Wahrscheinlichkeit und eine niedrige **Perplexität** haben. Mathematisch wird sie als normalisierte inverse Wahrscheinlichkeit des Testdatensatzes definiert:
$$
\mathrm{Perplexity}(W) = \sqrt[N]{1\over P(W_1,...,W_N)}
$$ 

**Du kannst mit der Textgenerierung experimentieren, indem du den [GPT-basierten Texteditor von Hugging Face](https://transformer.huggingface.co/doc/gpt2-large) verwendest.** In diesem Editor beginnst du mit dem Schreiben deines Textes, und durch Drücken von **[TAB]** werden dir mehrere Vervollständigungsoptionen angeboten. Wenn diese zu kurz sind oder du nicht zufrieden bist, drücke erneut [TAB], und du erhältst weitere Optionen, einschließlich längerer Textstücke.

## GPT ist eine Familie

GPT ist kein einzelnes Modell, sondern eine Sammlung von Modellen, die von [OpenAI](https://openai.com) entwickelt und trainiert wurden.

Zu den GPT-Modellen gehören:

| [GPT-2](https://huggingface.co/docs/transformers/model_doc/gpt2#openai-gpt2) | [GPT-3](https://openai.com/research/language-models-are-few-shot-learners) | [GPT-4](https://openai.com/gpt-4) |
| -- | -- | -- |
| Sprachmodell mit bis zu 1,5 Milliarden Parametern. | Sprachmodell mit bis zu 175 Milliarden Parametern. | 100T Parameter, akzeptiert sowohl Bild- als auch Texteingaben und gibt Text aus. |

Die Modelle GPT-3 und GPT-4 sind verfügbar [als kognitive Dienste von Microsoft Azure](https://azure.microsoft.com/en-us/services/cognitive-services/openai-service/#overview?WT.mc_id=academic-77998-cacaste) und als [OpenAI API](https://openai.com/api/).

## Prompt Engineering

Da GPT auf großen Datenmengen trainiert wurde, um Sprache und Code zu verstehen, liefert es Ausgaben als Reaktion auf Eingaben (Prompts). Prompts sind Eingaben oder Abfragen für GPT, bei denen man den Modellen Anweisungen zu den Aufgaben gibt, die sie als Nächstes ausführen sollen. Um ein gewünschtes Ergebnis zu erzielen, benötigt man den effektivsten Prompt, was die Auswahl der richtigen Wörter, Formate, Phrasen oder sogar Symbole umfasst. Dieser Ansatz wird als [Prompt Engineering](https://learn.microsoft.com/en-us/shows/ai-show/the-basics-of-prompt-engineering-with-azure-openai-service?WT.mc_id=academic-77998-bethanycheum) bezeichnet.

[Diese Dokumentation](https://learn.microsoft.com/en-us/semantic-kernel/prompt-engineering/?WT.mc_id=academic-77998-bethanycheum) bietet dir weitere Informationen zum Prompt Engineering.

## ✍️ Beispiel-Notebook: [Spielen mit OpenAI-GPT](GPT-PyTorch.ipynb)

Setze dein Lernen in den folgenden Notebooks fort:

* [Textgenerierung mit OpenAI-GPT und Hugging Face Transformers](GPT-PyTorch.ipynb)

## Fazit

Neue vortrainierte allgemeine Sprachmodelle modellieren nicht nur die Sprachstruktur, sondern enthalten auch eine enorme Menge an natürlicher Sprache. Daher können sie effektiv eingesetzt werden, um einige NLP-Aufgaben in Zero-Shot- oder Few-Shot-Szenarien zu lösen.

## [Quiz nach der Vorlesung](https://ff-quizzes.netlify.app/en/ai/quiz/40)

---

