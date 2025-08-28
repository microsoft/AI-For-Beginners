<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "2efbb183384a50f0fc0cde02534d912f",
  "translation_date": "2025-08-28T20:03:10+00:00",
  "source_file": "lessons/5-NLP/20-LangModels/README.md",
  "language_code": "nl"
}
-->
# Voorgetrainde Grote Taalmodellen

In al onze eerdere taken trainden we een neuraal netwerk om een bepaalde taak uit te voeren met behulp van een gelabelde dataset. Bij grote transformermodellen, zoals BERT, gebruiken we taalmodellering op een zelf-gestuurde manier om een taalmodel te bouwen, dat vervolgens wordt gespecialiseerd voor een specifieke downstream-taak met verdere domeinspecifieke training. Het is echter aangetoond dat grote taalmodellen ook veel taken kunnen oplossen zonder ENIGE domeinspecifieke training. Een familie van modellen die dat kan, wordt **GPT** genoemd: Generative Pre-Trained Transformer.

## [Pre-lecture quiz](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/120)

## Tekstgeneratie en Perplexiteit

Het idee dat een neuraal netwerk algemene taken kan uitvoeren zonder downstream-training wordt gepresenteerd in het artikel [Language Models are Unsupervised Multitask Learners](https://cdn.openai.com/better-language-models/language_models_are_unsupervised_multitask_learners.pdf). Het belangrijkste idee is dat veel andere taken kunnen worden gemodelleerd met behulp van **tekstgeneratie**, omdat tekst begrijpen in wezen betekent dat je het kunt produceren. Omdat het model is getraind op een enorme hoeveelheid tekst die menselijke kennis omvat, wordt het ook deskundig op een breed scala aan onderwerpen.

> Tekst begrijpen en kunnen produceren houdt ook in dat je iets weet over de wereld om ons heen. Mensen leren ook grotendeels door te lezen, en het GPT-netwerk is in dit opzicht vergelijkbaar.

Tekstgeneratienetwerken werken door de waarschijnlijkheid van het volgende woord te voorspellen $$P(w_N)$$. De onvoorwaardelijke waarschijnlijkheid van het volgende woord is echter gelijk aan de frequentie van dat woord in de tekstcorpus. GPT kan ons de **voorwaardelijke waarschijnlijkheid** van het volgende woord geven, gegeven de voorgaande woorden: $$P(w_N | w_{n-1}, ..., w_0)$$

> Je kunt meer lezen over waarschijnlijkheden in ons [Data Science for Beginners Curriculum](https://github.com/microsoft/Data-Science-For-Beginners/tree/main/1-Introduction/04-stats-and-probability).

De kwaliteit van een taalgenererend model kan worden gedefinieerd met behulp van **perplexiteit**. Dit is een intrinsieke metriek die ons in staat stelt de modelkwaliteit te meten zonder een taak-specifieke dataset. Het is gebaseerd op het idee van de *waarschijnlijkheid van een zin* - het model kent een hoge waarschijnlijkheid toe aan een zin die waarschijnlijk echt is (d.w.z. het model is er niet **verward** door), en een lage waarschijnlijkheid aan zinnen die minder logisch zijn (bijv. *Kan het doet wat?*). Wanneer we ons model zinnen uit een echte tekstcorpus geven, verwachten we dat ze een hoge waarschijnlijkheid en een lage **perplexiteit** hebben. Wiskundig wordt dit gedefinieerd als de genormaliseerde inverse waarschijnlijkheid van de testset:
$$
\mathrm{Perplexity}(W) = \sqrt[N]{1\over P(W_1,...,W_N)}
$$ 

**Je kunt experimenteren met tekstgeneratie met behulp van de [GPT-aangedreven teksteditor van Hugging Face](https://transformer.huggingface.co/doc/gpt2-large)**. In deze editor begin je met het schrijven van je tekst, en door op **[TAB]** te drukken krijg je verschillende voltooiingsopties. Als ze te kort zijn, of je bent er niet tevreden mee - druk opnieuw op [TAB], en je krijgt meer opties, inclusief langere stukken tekst.

## GPT is een Familie

GPT is niet één enkel model, maar eerder een verzameling modellen die zijn ontwikkeld en getraind door [OpenAI](https://openai.com). 

Binnen de GPT-modellen hebben we:

| [GPT-2](https://huggingface.co/docs/transformers/model_doc/gpt2#openai-gpt2) | [GPT-3](https://openai.com/research/language-models-are-few-shot-learners) | [GPT-4](https://openai.com/gpt-4) |
| -- | -- | -- |
| Taalmodel met tot 1,5 miljard parameters. | Taalmodel met tot 175 miljard parameters | 100T parameters en accepteert zowel beeld- als tekstinvoer en geeft tekst als output. |

De GPT-3- en GPT-4-modellen zijn beschikbaar [als een cognitieve service van Microsoft Azure](https://azure.microsoft.com/en-us/services/cognitive-services/openai-service/#overview?WT.mc_id=academic-77998-cacaste), en als [OpenAI API](https://openai.com/api/).

## Prompt Engineering

Omdat GPT is getraind op enorme hoeveelheden data om taal en code te begrijpen, geven ze output als reactie op input (prompts). Prompts zijn GPT-inputs of vragen waarbij je instructies geeft aan de modellen over de taken die ze vervolgens moeten uitvoeren. Om een gewenst resultaat te krijgen, heb je de meest effectieve prompt nodig, wat inhoudt dat je de juiste woorden, formats, zinnen of zelfs symbolen selecteert. Deze aanpak wordt [Prompt Engineering](https://learn.microsoft.com/en-us/shows/ai-show/the-basics-of-prompt-engineering-with-azure-openai-service?WT.mc_id=academic-77998-bethanycheum) genoemd.

[Deze documentatie](https://learn.microsoft.com/en-us/semantic-kernel/prompt-engineering/?WT.mc_id=academic-77998-bethanycheum) biedt meer informatie over prompt engineering.

## ✍️ Voorbeeldnotebook: [Spelen met OpenAI-GPT](GPT-PyTorch.ipynb)

Ga verder met leren in de volgende notebooks:

* [Tekst genereren met OpenAI-GPT en Hugging Face Transformers](GPT-PyTorch.ipynb)

## Conclusie

Nieuwe algemene voorgetrainde taalmodellen modelleren niet alleen de taalstructuur, maar bevatten ook een enorme hoeveelheid natuurlijke taal. Hierdoor kunnen ze effectief worden gebruikt om enkele NLP-taken op te lossen in zero-shot- of few-shot-instellingen.

## [Post-lecture quiz](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/220)

---

**Disclaimer**:  
Dit document is vertaald met behulp van de AI-vertalingsservice [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we streven naar nauwkeurigheid, dient u zich ervan bewust te zijn dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het originele document in zijn oorspronkelijke taal moet worden beschouwd als de gezaghebbende bron. Voor cruciale informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor eventuele misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.