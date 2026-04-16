# Vooraf Getrainde Grote Taalmodellen

Bij al onze eerdere taken trainden we een neuraal netwerk om een bepaalde taak uit te voeren met behulp van een gelabelde dataset. Met grote transformator-modellen, zoals BERT, gebruiken we taalmodellering op een zelf-superviserende manier om een taalmodel te bouwen, dat vervolgens wordt gespecialiseerd voor specifieke downstream-taken met verdere domeinspecifieke training. Het is echter aangetoond dat grote taalmodellen ook veel taken kunnen oplossen zonder ENIGE domeinspecifieke training. Een familie van modellen die daartoe in staat is, wordt **GPT** genoemd: Generative Pre-Trained Transformer.

## [Pre-lecture quiz](https://ff-quizzes.netlify.app/en/ai/quiz/39)

## Tekstgeneratie en Perplexity

Het idee dat een neuraal netwerk algemene taken kan uitvoeren zonder downstream-training wordt gepresenteerd in het artikel [Language Models are Unsupervised Multitask Learners](https://cdn.openai.com/better-language-models/language_models_are_unsupervised_multitask_learners.pdf). Het belangrijkste idee is dat veel andere taken kunnen worden gemodelleerd met **tekstgeneratie**, omdat het begrijpen van tekst in wezen betekent dat je het kunt produceren. Omdat het model is getraind op een enorme hoeveelheid tekst die menselijke kennis omvat, wordt het ook deskundig op een breed scala aan onderwerpen.

> Tekst begrijpen en kunnen produceren houdt ook in dat je iets weet over de wereld om ons heen. Mensen leren ook in grote mate door te lezen, en het GPT-netwerk is in dit opzicht vergelijkbaar.

Netwerken voor tekstgeneratie werken door de waarschijnlijkheid van het volgende woord te voorspellen $$P(w_N)$$. De onvoorwaardelijke waarschijnlijkheid van het volgende woord is echter gelijk aan de frequentie van dat woord in de tekstcorpus. GPT kan ons de **voorwaardelijke waarschijnlijkheid** van het volgende woord geven, gegeven de voorgaande woorden: $$P(w_N | w_{n-1}, ..., w_0)$$.

> Je kunt meer lezen over waarschijnlijkheden in ons [Data Science for Beginners Curriculum](https://github.com/microsoft/Data-Science-For-Beginners/tree/main/1-Introduction/04-stats-and-probability).

De kwaliteit van een taalgenererend model kan worden gedefinieerd met behulp van **perplexity**. Dit is een intrinsieke maatstaf waarmee we de kwaliteit van het model kunnen meten zonder een taak-specifieke dataset. Het is gebaseerd op het idee van de *waarschijnlijkheid van een zin* - het model kent een hoge waarschijnlijkheid toe aan een zin die waarschijnlijk echt is (d.w.z. het model is niet **verward** door de zin), en een lage waarschijnlijkheid aan zinnen die minder logisch zijn (bijv. *Kan het wat doen?*). Wanneer we ons model zinnen uit een echte tekstcorpus geven, verwachten we dat ze een hoge waarschijnlijkheid en een lage **perplexity** hebben. Wiskundig wordt dit gedefinieerd als de genormaliseerde inverse waarschijnlijkheid van de testset:
$$
\mathrm{Perplexity}(W) = \sqrt[N]{1\over P(W_1,...,W_N)}
$$ 

**Je kunt experimenteren met tekstgeneratie met behulp van de [GPT-aangedreven teksteditor van Hugging Face](https://transformer.huggingface.co/doc/gpt2-large)**. In deze editor begin je met het schrijven van je tekst, en door op **[TAB]** te drukken krijg je verschillende opties voor voltooiing. Als ze te kort zijn, of je bent er niet tevreden mee - druk opnieuw op [TAB], en je krijgt meer opties, inclusief langere stukken tekst.

## GPT is een Familie

GPT is niet één enkel model, maar eerder een verzameling modellen die zijn ontwikkeld en getraind door [OpenAI](https://openai.com).

Onder de GPT-modellen hebben we:

| [GPT-2](https://huggingface.co/docs/transformers/model_doc/gpt2#openai-gpt2) | [GPT 3](https://openai.com/research/language-models-are-few-shot-learners) | [GPT-4](https://openai.com/gpt-4) |
| -- | -- | -- |
|Taalmodel met tot 1,5 miljard parameters. | Taalmodel met tot 175 miljard parameters | 100T parameters en accepteert zowel beeld- als tekstinvoer en geeft tekstuitvoer. |

De GPT-3 en GPT-4 modellen zijn beschikbaar [als een cognitieve dienst van Microsoft Azure](https://azure.microsoft.com/en-us/services/cognitive-services/openai-service/#overview?WT.mc_id=academic-77998-cacaste), en als [OpenAI API](https://openai.com/api/).

## Prompt Engineering

Omdat GPT is getraind op enorme hoeveelheden data om taal en code te begrijpen, geven ze outputs als reactie op inputs (prompts). Prompts zijn GPT-inputs of queries waarbij je instructies geeft aan modellen over taken die ze vervolgens voltooien. Om een gewenst resultaat te verkrijgen, heb je de meest effectieve prompt nodig, wat inhoudt dat je de juiste woorden, formats, zinnen of zelfs symbolen selecteert. Deze aanpak wordt [Prompt Engineering](https://learn.microsoft.com/en-us/shows/ai-show/the-basics-of-prompt-engineering-with-azure-openai-service?WT.mc_id=academic-77998-bethanycheum) genoemd.

[Deze documentatie](https://learn.microsoft.com/en-us/semantic-kernel/prompt-engineering/?WT.mc_id=academic-77998-bethanycheum) biedt je meer informatie over prompt engineering.

## ✍️ Voorbeeld Notebook: [Spelen met OpenAI-GPT](GPT-PyTorch.ipynb)

Ga verder met leren in de volgende notebooks:

* [Tekst genereren met OpenAI-GPT en Hugging Face Transformers](GPT-PyTorch.ipynb)

## Conclusie

Nieuwe algemene vooraf getrainde taalmodellen modelleren niet alleen de taalstructuur, maar bevatten ook een enorme hoeveelheid natuurlijke taal. Hierdoor kunnen ze effectief worden gebruikt om enkele NLP-taken op te lossen in zero-shot- of few-shot-instellingen.

## [Post-lecture quiz](https://ff-quizzes.netlify.app/en/ai/quiz/40)

---

