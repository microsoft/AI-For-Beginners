# Modelli di Linguaggio di Grandi Dimensioni Pre-Addestrati

In tutti i nostri compiti precedenti, abbiamo addestrato una rete neurale per svolgere un determinato compito utilizzando un dataset etichettato. Con i grandi modelli transformer, come BERT, utilizziamo il modellamento del linguaggio in modalità auto-supervisionata per costruire un modello linguistico, che viene poi specializzato per compiti specifici con ulteriore addestramento specifico per il dominio. Tuttavia, è stato dimostrato che i grandi modelli di linguaggio possono anche risolvere molti compiti senza ALCUN addestramento specifico per il dominio. Una famiglia di modelli in grado di fare ciò è chiamata **GPT**: Generative Pre-Trained Transformer.

## [Quiz pre-lezione](https://ff-quizzes.netlify.app/en/ai/quiz/39)

## Generazione di Testo e Perplessità

L'idea di una rete neurale in grado di svolgere compiti generali senza addestramento specifico è presentata nel documento [Language Models are Unsupervised Multitask Learners](https://cdn.openai.com/better-language-models/language_models_are_unsupervised_multitask_learners.pdf). L'idea principale è che molti altri compiti possono essere modellati utilizzando la **generazione di testo**, poiché comprendere il testo significa essenzialmente essere in grado di produrlo. Poiché il modello è addestrato su una quantità enorme di testo che racchiude la conoscenza umana, diventa anche esperto su una vasta gamma di argomenti.

> Comprendere e essere in grado di produrre testo implica anche sapere qualcosa sul mondo che ci circonda. Anche le persone imparano in gran parte leggendo, e la rete GPT è simile in questo senso.

Le reti di generazione di testo funzionano prevedendo la probabilità della parola successiva $$P(w_N)$$. Tuttavia, la probabilità incondizionata della parola successiva equivale alla frequenza di questa parola nel corpus di testo. GPT è in grado di fornire la **probabilità condizionale** della parola successiva, date le precedenti: $$P(w_N | w_{n-1}, ..., w_0)$$.

> Puoi leggere di più sulle probabilità nel nostro [Curriculum di Data Science per Principianti](https://github.com/microsoft/Data-Science-For-Beginners/tree/main/1-Introduction/04-stats-and-probability).

La qualità di un modello di generazione di linguaggio può essere definita utilizzando la **perplessità**. È una metrica intrinseca che ci permette di misurare la qualità del modello senza alcun dataset specifico per il compito. Si basa sulla nozione di *probabilità di una frase* - il modello assegna alta probabilità a una frase che è probabile che sia reale (cioè il modello non è **perplesso** da essa), e bassa probabilità a frasi che hanno meno senso (es. *Può fare cosa?*). Quando forniamo al nostro modello frasi da un corpus di testo reale, ci aspettiamo che abbiano alta probabilità e bassa **perplessità**. Matematicamente, è definita come la probabilità inversa normalizzata del set di test:
$$
\mathrm{Perplexity}(W) = \sqrt[N]{1\over P(W_1,...,W_N)}
$$ 

**Puoi sperimentare la generazione di testo utilizzando [l'editor di testo basato su GPT di Hugging Face](https://transformer.huggingface.co/doc/gpt2-large)**. In questo editor, inizi a scrivere il tuo testo e premendo **[TAB]** ti verranno offerte diverse opzioni di completamento. Se sono troppo brevi o non ti soddisfano, premi [TAB] di nuovo e avrai più opzioni, inclusi pezzi di testo più lunghi.

## GPT è una Famiglia

GPT non è un singolo modello, ma piuttosto una collezione di modelli sviluppati e addestrati da [OpenAI](https://openai.com).

Tra i modelli GPT, abbiamo:

| [GPT-2](https://huggingface.co/docs/transformers/model_doc/gpt2#openai-gpt2) | [GPT 3](https://openai.com/research/language-models-are-few-shot-learners) | [GPT-4](https://openai.com/gpt-4) |
| -- | -- | -- |
| Modello linguistico con fino a 1,5 miliardi di parametri. | Modello linguistico con fino a 175 miliardi di parametri. | 100T parametri e accetta sia input di immagini che di testo, producendo output testuali. |

I modelli GPT-3 e GPT-4 sono disponibili [come servizio cognitivo da Microsoft Azure](https://azure.microsoft.com/en-us/services/cognitive-services/openai-service/#overview?WT.mc_id=academic-77998-cacaste) e come [API di OpenAI](https://openai.com/api/).

## Prompt Engineering

Poiché GPT è stato addestrato su vasti volumi di dati per comprendere il linguaggio e il codice, fornisce output in risposta agli input (prompt). I prompt sono input o query per GPT, in cui si forniscono istruzioni ai modelli sui compiti da completare. Per ottenere un risultato desiderato, è necessario il prompt più efficace, che implica la selezione delle parole, dei formati, delle frasi o persino dei simboli giusti. Questo approccio è chiamato [Prompt Engineering](https://learn.microsoft.com/en-us/shows/ai-show/the-basics-of-prompt-engineering-with-azure-openai-service?WT.mc_id=academic-77998-bethanycheum).

[Questa documentazione](https://learn.microsoft.com/en-us/semantic-kernel/prompt-engineering/?WT.mc_id=academic-77998-bethanycheum) ti fornisce ulteriori informazioni sul prompt engineering.

## ✍️ Notebook di Esempio: [Giocare con OpenAI-GPT](GPT-PyTorch.ipynb)

Continua il tuo apprendimento nei seguenti notebook:

* [Generazione di testo con OpenAI-GPT e Hugging Face Transformers](GPT-PyTorch.ipynb)

## Conclusione

I nuovi modelli linguistici generali pre-addestrati non solo modellano la struttura del linguaggio, ma contengono anche una vasta quantità di linguaggio naturale. Pertanto, possono essere utilizzati efficacemente per risolvere alcuni compiti di NLP in modalità zero-shot o few-shot.

## [Quiz post-lezione](https://ff-quizzes.netlify.app/en/ai/quiz/40)

---

