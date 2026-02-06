# Forudtrænede Store Sproglige Modeller

I alle vores tidligere opgaver har vi trænet et neuralt netværk til at udføre en bestemt opgave ved hjælp af et mærket datasæt. Med store transformer-modeller, såsom BERT, bruger vi sprogmodellering på en selv-superviseret måde til at bygge en sprogmodel, som derefter specialiseres til specifikke downstream-opgaver med yderligere domænespecifik træning. Det er dog blevet demonstreret, at store sproglige modeller også kan løse mange opgaver uden nogen form for domænespecifik træning. En familie af modeller, der kan gøre dette, kaldes **GPT**: Generative Pre-Trained Transformer.

## [Quiz før forelæsning](https://ff-quizzes.netlify.app/en/ai/quiz/39)

## Tekstgenerering og Perpleksitet

Ideen om, at et neuralt netværk kan udføre generelle opgaver uden downstream-træning, præsenteres i [Language Models are Unsupervised Multitask Learners](https://cdn.openai.com/better-language-models/language_models_are_unsupervised_multitask_learners.pdf)-artiklen. Hovedideen er, at mange andre opgaver kan modelleres ved hjælp af **tekstgenerering**, fordi forståelse af tekst i bund og grund betyder at kunne producere den. Fordi modellen er trænet på en enorm mængde tekst, der omfatter menneskelig viden, bliver den også vidende om en bred vifte af emner.

> At forstå og kunne producere tekst indebærer også at vide noget om verden omkring os. Mennesker lærer også i høj grad ved at læse, og GPT-netværket er på samme måde.

Tekstgenereringsnetværk fungerer ved at forudsige sandsynligheden for det næste ord $$P(w_N)$$. Den ubetingede sandsynlighed for det næste ord svarer dog til frekvensen af dette ord i tekstkorpusset. GPT kan give os **betinget sandsynlighed** for det næste ord, givet de foregående: $$P(w_N | w_{n-1}, ..., w_0)$$

> Du kan læse mere om sandsynligheder i vores [Data Science for Beginners Curriculum](https://github.com/microsoft/Data-Science-For-Beginners/tree/main/1-Introduction/04-stats-and-probability)

Kvaliteten af en sprogmodel kan defineres ved hjælp af **perpleksitet**. Det er en indre metrik, der giver os mulighed for at måle modellens kvalitet uden et opgavespecifikt datasæt. Det er baseret på begrebet *sandsynligheden for en sætning* - modellen tildeler høj sandsynlighed til en sætning, der sandsynligvis er ægte (dvs. modellen er ikke **forvirret** af den), og lav sandsynlighed til sætninger, der giver mindre mening (fx *Kan det gør hvad?*). Når vi giver vores model sætninger fra et ægte tekstkorpus, forventer vi, at de har høj sandsynlighed og lav **perpleksitet**. Matematisk defineres det som normaliseret invers sandsynlighed for testdatasættet:
$$
\mathrm{Perplexity}(W) = \sqrt[N]{1\over P(W_1,...,W_N)}
$$ 

**Du kan eksperimentere med tekstgenerering ved hjælp af [GPT-drevet teksteditor fra Hugging Face](https://transformer.huggingface.co/doc/gpt2-large)**. I denne editor begynder du at skrive din tekst, og ved at trykke på **[TAB]** får du flere forslag til fuldførelse. Hvis de er for korte, eller du ikke er tilfreds med dem - tryk på [TAB] igen, og du vil få flere muligheder, inklusive længere tekststykker.

## GPT er en Familie

GPT er ikke en enkelt model, men snarere en samling af modeller udviklet og trænet af [OpenAI](https://openai.com). 

Under GPT-modellerne har vi:

| [GPT-2](https://huggingface.co/docs/transformers/model_doc/gpt2#openai-gpt2) | [GPT 3](https://openai.com/research/language-models-are-few-shot-learners) | [GPT-4](https://openai.com/gpt-4) |
| -- | -- | -- |
|Sprogmodel med op til 1,5 milliarder parametre. | Sprogmodel med op til 175 milliarder parametre | 100T parametre og accepterer både billede- og tekstinput og genererer tekst som output. |

GPT-3 og GPT-4-modellerne er tilgængelige [som en kognitiv tjeneste fra Microsoft Azure](https://azure.microsoft.com/en-us/services/cognitive-services/openai-service/#overview?WT.mc_id=academic-77998-cacaste) og som [OpenAI API](https://openai.com/api/).

## Prompt Engineering

Fordi GPT er trænet på enorme mængder data til at forstå sprog og kode, giver de output som svar på input (prompter). Prompter er GPT-input eller forespørgsler, hvor man giver instruktioner til modellerne om opgaver, de skal udføre. For at opnå det ønskede resultat skal man bruge den mest effektive prompt, hvilket indebærer at vælge de rigtige ord, formater, sætninger eller endda symboler. Denne tilgang kaldes [Prompt Engineering](https://learn.microsoft.com/en-us/shows/ai-show/the-basics-of-prompt-engineering-with-azure-openai-service?WT.mc_id=academic-77998-bethanycheum).

[Denne dokumentation](https://learn.microsoft.com/en-us/semantic-kernel/prompt-engineering/?WT.mc_id=academic-77998-bethanycheum) giver dig mere information om prompt engineering.

## ✍️ Eksempel Notebook: [Leg med OpenAI-GPT](GPT-PyTorch.ipynb)

Fortsæt din læring i følgende notebooks:

* [Generering af tekst med OpenAI-GPT og Hugging Face Transformers](GPT-PyTorch.ipynb)

## Konklusion

Nye generelle forudtrænede sproglige modeller modellerer ikke kun sprogets struktur, men indeholder også en enorm mængde naturligt sprog. Derfor kan de effektivt bruges til at løse nogle NLP-opgaver i zero-shot eller few-shot indstillinger.

## [Quiz efter forelæsning](https://ff-quizzes.netlify.app/en/ai/quiz/40)

---

