<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "2efbb183384a50f0fc0cde02534d912f",
  "translation_date": "2025-08-25T22:08:32+00:00",
  "source_file": "lessons/5-NLP/20-LangModels/README.md",
  "language_code": "hr"
}
-->
# Pre-Trained Large Language Models

U svim našim prethodnim zadacima trenirali smo neuronsku mrežu da obavlja određeni zadatak koristeći označeni skup podataka. Kod velikih transformacijskih modela, poput BERT-a, koristimo modeliranje jezika u samonadziranom načinu kako bismo izgradili jezični model, koji se zatim specijalizira za specifične zadatke uz dodatnu obuku specifičnu za domenu. Međutim, pokazalo se da veliki jezični modeli mogu riješiti mnoge zadatke i bez ikakve obuke specifične za domenu. Obitelj modela sposobnih za to naziva se **GPT**: Generativni unaprijed trenirani transformator.

## [Pre-lecture quiz](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/120)

## Generiranje teksta i Perpleksnost

Ideja da neuronska mreža može obavljati opće zadatke bez dodatne obuke predstavljena je u radu [Language Models are Unsupervised Multitask Learners](https://cdn.openai.com/better-language-models/language_models_are_unsupervised_multitask_learners.pdf). Glavna ideja je da se mnogi drugi zadaci mogu modelirati pomoću **generiranja teksta**, jer razumijevanje teksta u suštini znači sposobnost njegovog stvaranja. Budući da je model treniran na ogromnoj količini teksta koji obuhvaća ljudsko znanje, on također postaje informiran o širokom spektru tema.

> Razumijevanje i sposobnost stvaranja teksta također podrazumijeva poznavanje svijeta oko nas. Ljudi također u velikoj mjeri uče čitajući, a GPT mreža je u tom pogledu slična.

Mreže za generiranje teksta rade predviđanjem vjerojatnosti sljedeće riječi $$P(w_N)$$. Međutim, bezuvjetna vjerojatnost sljedeće riječi jednaka je učestalosti te riječi u korpusu teksta. GPT nam može dati **uvjetnu vjerojatnost** sljedeće riječi, s obzirom na prethodne: $$P(w_N | w_{n-1}, ..., w_0)$$

> Više o vjerojatnostima možete pročitati u našem [kurikulumu za početnike u znanosti o podacima](https://github.com/microsoft/Data-Science-For-Beginners/tree/main/1-Introduction/04-stats-and-probability).

Kvaliteta modela za generiranje jezika može se definirati pomoću **perpleksnosti**. To je intrinzična metrika koja nam omogućuje mjerenje kvalitete modela bez ikakvog skupa podataka specifičnog za zadatak. Temelji se na konceptu *vjerojatnosti rečenice* - model dodjeljuje visoku vjerojatnost rečenici koja je vjerojatno stvarna (tj. model nije **zbunjen** njome) i nisku vjerojatnost rečenicama koje manje imaju smisla (npr. *Može li to što?*). Kada modelu damo rečenice iz stvarnog korpusa teksta, očekujemo da će imati visoku vjerojatnost i nisku **perpleksnost**. Matematički, ona se definira kao normalizirana inverzna vjerojatnost testnog skupa:
$$
\mathrm{Perplexity}(W) = \sqrt[N]{1\over P(W_1,...,W_N)}
$$ 

**Možete eksperimentirati s generiranjem teksta koristeći [GPT-pokretan uređivač teksta od Hugging Face](https://transformer.huggingface.co/doc/gpt2-large)**. U ovom uređivaču započinjete pisanje svog teksta, a pritiskom na **[TAB]** dobit ćete nekoliko opcija za nastavak. Ako su prekratke ili niste zadovoljni njima - ponovno pritisnite [TAB], i dobit ćete više opcija, uključujući dulje dijelove teksta.

## GPT je Obitelj

GPT nije jedan model, već zbirka modela koje je razvio i trenirao [OpenAI](https://openai.com). 

Unutar GPT modela nalazimo:

| [GPT-2](https://huggingface.co/docs/transformers/model_doc/gpt2#openai-gpt2) | [GPT 3](https://openai.com/research/language-models-are-few-shot-learners) | [GPT-4](https://openai.com/gpt-4) |
| -- | -- | -- |
| Jezični model s do 1,5 milijardi parametara. | Jezični model s do 175 milijardi parametara. | 100T parametara, prihvaća i slike i tekst kao ulaz, a daje tekst kao izlaz. |

Modeli GPT-3 i GPT-4 dostupni su [kao kognitivna usluga putem Microsoft Azure](https://azure.microsoft.com/en-us/services/cognitive-services/openai-service/#overview?WT.mc_id=academic-77998-cacaste) i kao [OpenAI API](https://openai.com/api/).

## Inženjering Upita (Prompt Engineering)

Budući da je GPT treniran na ogromnim količinama podataka kako bi razumio jezik i kod, daje odgovore na temelju ulaza (upita). Upiti su ulazi ili upiti za GPT gdje se modelima daju upute o zadacima koje trebaju izvršiti. Kako biste dobili željeni rezultat, potrebno je osmisliti najučinkovitiji upit, što uključuje odabir pravih riječi, formata, fraza ili čak simbola. Ovaj pristup naziva se [Inženjering upita](https://learn.microsoft.com/en-us/shows/ai-show/the-basics-of-prompt-engineering-with-azure-openai-service?WT.mc_id=academic-77998-bethanycheum).

[Ova dokumentacija](https://learn.microsoft.com/en-us/semantic-kernel/prompt-engineering/?WT.mc_id=academic-77998-bethanycheum) pruža više informacija o inženjeringu upita.

## ✍️ Primjer Bilježnice: [Igranje s OpenAI-GPT](../../../../../lessons/5-NLP/20-LangModels/GPT-PyTorch.ipynb)

Nastavite učiti kroz sljedeće bilježnice:

* [Generiranje teksta s OpenAI-GPT i Hugging Face Transformers](../../../../../lessons/5-NLP/20-LangModels/GPT-PyTorch.ipynb)

## Zaključak

Novi opći unaprijed trenirani jezični modeli ne modeliraju samo strukturu jezika, već sadrže i ogromnu količinu prirodnog jezika. Stoga se mogu učinkovito koristiti za rješavanje nekih NLP zadataka u zero-shot ili few-shot postavkama.

## [Post-lecture quiz](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/220)

**Odricanje od odgovornosti**:  
Ovaj dokument je preveden pomoću AI usluge za prevođenje [Co-op Translator](https://github.com/Azure/co-op-translator). Iako nastojimo osigurati točnost, imajte na umu da automatski prijevodi mogu sadržavati pogreške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati autoritativnim izvorom. Za ključne informacije preporučuje se profesionalni prijevod od strane čovjeka. Ne preuzimamo odgovornost za nesporazume ili pogrešna tumačenja koja mogu proizaći iz korištenja ovog prijevoda.