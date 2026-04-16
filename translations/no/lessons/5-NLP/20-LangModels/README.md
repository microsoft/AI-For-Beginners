# Forhåndstrente store språkmodeller

I alle våre tidligere oppgaver trente vi et nevralt nettverk for å utføre en bestemt oppgave ved hjelp av et merket datasett. Med store transformer-modeller, som BERT, bruker vi språklæring i en selv-supervisert tilnærming for å bygge en språkmodell, som deretter spesialiseres for spesifikke oppgaver gjennom videre domenespesifikk trening. Det har imidlertid blitt vist at store språkmodeller også kan løse mange oppgaver uten NOEN domenespesifikk trening. En familie av modeller som kan gjøre dette kalles **GPT**: Generative Pre-Trained Transformer.

## [Quiz før forelesning](https://ff-quizzes.netlify.app/en/ai/quiz/39)

## Tekstgenerering og forvirring (Perplexity)

Ideen om at et nevralt nettverk kan utføre generelle oppgaver uten videre trening presenteres i artikkelen [Language Models are Unsupervised Multitask Learners](https://cdn.openai.com/better-language-models/language_models_are_unsupervised_multitask_learners.pdf). Hovedideen er at mange andre oppgaver kan modelleres ved hjelp av **tekstgenerering**, fordi det å forstå tekst i bunn og grunn betyr å kunne produsere den. Siden modellen er trent på en enorm mengde tekst som omfatter menneskelig kunnskap, blir den også kunnskapsrik om et bredt spekter av emner.

> Å forstå og kunne produsere tekst innebærer også å vite noe om verden rundt oss. Mennesker lærer i stor grad ved å lese, og GPT-nettverket er likt på dette området.

Tekstgenereringsnettverk fungerer ved å forutsi sannsynligheten for neste ord $$P(w_N)$$. Den ubetingede sannsynligheten for neste ord tilsvarer imidlertid frekvensen av dette ordet i tekstkorpuset. GPT kan gi oss **betinget sannsynlighet** for neste ord, gitt de foregående: $$P(w_N | w_{n-1}, ..., w_0)$$

> Du kan lese mer om sannsynligheter i vårt [Data Science for Beginners Curriculum](https://github.com/microsoft/Data-Science-For-Beginners/tree/main/1-Introduction/04-stats-and-probability)

Kvaliteten på en språkmodell for tekstgenerering kan defineres ved hjelp av **forvirring (perplexity)**. Dette er en iboende metrikk som lar oss måle modellens kvalitet uten et oppgavespesifikt datasett. Den er basert på begrepet *sannsynlighet for en setning* – modellen tilordner høy sannsynlighet til en setning som sannsynligvis er ekte (dvs. modellen er ikke **forvirret** av den), og lav sannsynlighet til setninger som gir mindre mening (f.eks. *Kan det gjør hva?*). Når vi gir modellen vår setninger fra et ekte tekstkorpus, forventer vi at de har høy sannsynlighet og lav **forvirring**. Matematisk er det definert som normalisert invers sannsynlighet for testsettet:
$$
\mathrm{Perplexity}(W) = \sqrt[N]{1\over P(W_1,...,W_N)}
$$ 

**Du kan eksperimentere med tekstgenerering ved hjelp av [GPT-drevet teksteditor fra Hugging Face](https://transformer.huggingface.co/doc/gpt2-large)**. I denne editoren begynner du å skrive teksten din, og ved å trykke **[TAB]** vil du få flere fullføringsalternativer. Hvis de er for korte, eller du ikke er fornøyd med dem – trykk [TAB] igjen, og du vil få flere alternativer, inkludert lengre tekststykker.

## GPT er en familie

GPT er ikke en enkelt modell, men snarere en samling av modeller utviklet og trent av [OpenAI](https://openai.com). 

Blant GPT-modellene har vi:

| [GPT-2](https://huggingface.co/docs/transformers/model_doc/gpt2#openai-gpt2) | [GPT-3](https://openai.com/research/language-models-are-few-shot-learners) | [GPT-4](https://openai.com/gpt-4) |
| -- | -- | -- |
|Språkmodell med opptil 1,5 milliarder parametere. | Språkmodell med opptil 175 milliarder parametere | 100T parametere og aksepterer både bilde- og tekstinnganger og gir tekst som utdata. |

GPT-3 og GPT-4-modellene er tilgjengelige [som en kognitiv tjeneste fra Microsoft Azure](https://azure.microsoft.com/en-us/services/cognitive-services/openai-service/#overview?WT.mc_id=academic-77998-cacaste), og som [OpenAI API](https://openai.com/api/).

## Prompt Engineering

Siden GPT er trent på store mengder data for å forstå språk og kode, gir de svar basert på innganger (prompter). Prompter er GPT-forespørsler eller spørsmål der man gir instruksjoner til modellene om oppgavene de skal fullføre. For å oppnå ønsket resultat, trenger du den mest effektive prompten, som innebærer å velge riktige ord, formater, fraser eller til og med symboler. Denne tilnærmingen kalles [Prompt Engineering](https://learn.microsoft.com/en-us/shows/ai-show/the-basics-of-prompt-engineering-with-azure-openai-service?WT.mc_id=academic-77998-bethanycheum).

[Denne dokumentasjonen](https://learn.microsoft.com/en-us/semantic-kernel/prompt-engineering/?WT.mc_id=academic-77998-bethanycheum) gir deg mer informasjon om prompt engineering.

## ✍️ Eksempelnotatbok: [Leke med OpenAI-GPT](GPT-PyTorch.ipynb)

Fortsett læringen din i følgende notatbøker:

* [Generere tekst med OpenAI-GPT og Hugging Face Transformers](GPT-PyTorch.ipynb)

## Konklusjon

Nye generelle forhåndstrente språkmodeller modellerer ikke bare språkstrukturen, men inneholder også store mengder naturlig språk. Dermed kan de effektivt brukes til å løse noen NLP-oppgaver i zero-shot- eller few-shot-innstillinger.

## [Quiz etter forelesning](https://ff-quizzes.netlify.app/en/ai/quiz/40)

---

