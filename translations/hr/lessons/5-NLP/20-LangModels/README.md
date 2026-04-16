# Pre-Trained Large Language Models

U svim našim prethodnim zadacima trenirali smo neuronsku mrežu da obavlja određeni zadatak koristeći označene skupove podataka. Kod velikih transformacijskih modela, poput BERT-a, koristimo jezično modeliranje u samonadziranom načinu rada kako bismo izgradili jezični model, koji se zatim specijalizira za specifične zadatke uz dodatnu obuku prilagođenu domeni. Međutim, pokazalo se da veliki jezični modeli mogu riješiti mnoge zadatke i bez IKAKVE obuke prilagođene domeni. Obitelj modela sposobnih za to naziva se **GPT**: Generativni unaprijed trenirani transformator.

## [Pre-lecture quiz](https://ff-quizzes.netlify.app/en/ai/quiz/39)

## Generiranje teksta i Perpleksnost

Ideja da neuronska mreža može obavljati opće zadatke bez dodatne obuke predstavljena je u radu [Language Models are Unsupervised Multitask Learners](https://cdn.openai.com/better-language-models/language_models_are_unsupervised_multitask_learners.pdf). Glavna ideja je da se mnogi drugi zadaci mogu modelirati pomoću **generiranja teksta**, jer razumijevanje teksta u osnovi znači sposobnost njegovog stvaranja. Budući da je model treniran na ogromnoj količini teksta koja obuhvaća ljudsko znanje, postaje sposoban za širok spektar tema.

> Razumijevanje i sposobnost stvaranja teksta također podrazumijeva poznavanje svijeta oko nas. Ljudi također u velikoj mjeri uče čitajući, a GPT mreža je u tom smislu slična.

Mreže za generiranje teksta rade predviđanjem vjerojatnosti sljedeće riječi $$P(w_N)$$ Međutim, bezuvjetna vjerojatnost sljedeće riječi jednaka je učestalosti te riječi u tekstualnom korpusu. GPT nam može pružiti **uvjetnu vjerojatnost** sljedeće riječi, s obzirom na prethodne: $$P(w_N | w_{n-1}, ..., w_0)$$

> Više o vjerojatnostima možete pročitati u našem [Data Science for Beginners Curriculum](https://github.com/microsoft/Data-Science-For-Beginners/tree/main/1-Introduction/04-stats-and-probability)

Kvaliteta modela za generiranje teksta može se definirati pomoću **perpleksnosti**. To je intrinzična metrika koja nam omogućuje mjerenje kvalitete modela bez korištenja skupa podataka specifičnog za zadatak. Temelji se na konceptu *vjerojatnosti rečenice* - model dodjeljuje visoku vjerojatnost rečenici koja je vjerojatno stvarna (tj. model nije **zbunjen** njome), i nisku vjerojatnost rečenicama koje manje imaju smisla (npr. *Može li to što?*). Kada modelu damo rečenice iz stvarnog tekstualnog korpusa, očekujemo da imaju visoku vjerojatnost i nisku **perpleksnost**. Matematički, definira se kao normalizirana inverzna vjerojatnost testnog skupa:
$$
\mathrm{Perplexity}(W) = \sqrt[N]{1\over P(W_1,...,W_N)}
$$ 

**Možete eksperimentirati s generiranjem teksta koristeći [GPT-pokretan tekstualni editor od Hugging Face](https://transformer.huggingface.co/doc/gpt2-large)**. U ovom editoru započinjete pisanje teksta, a pritiskom na **[TAB]** dobit ćete nekoliko opcija za dovršavanje. Ako su prekratke ili niste zadovoljni njima - pritisnite [TAB] ponovno, i dobit ćete više opcija, uključujući duže dijelove teksta.

## GPT je Obitelj

GPT nije jedan model, već zbirka modela koje je razvio i trenirao [OpenAI](https://openai.com). 

Unutar GPT modela imamo:

| [GPT-2](https://huggingface.co/docs/transformers/model_doc/gpt2#openai-gpt2) | [GPT 3](https://openai.com/research/language-models-are-few-shot-learners) | [GPT-4](https://openai.com/gpt-4) |
| -- | -- | -- |
| Jezični model s do 1,5 milijardi parametara. | Jezični model s do 175 milijardi parametara | 100T parametara, prihvaća i slike i tekst kao ulaz, a izlaz je tekst. |


Modeli GPT-3 i GPT-4 dostupni su [kao kognitivna usluga putem Microsoft Azure](https://azure.microsoft.com/en-us/services/cognitive-services/openai-service/#overview?WT.mc_id=academic-77998-cacaste), i kao [OpenAI API](https://openai.com/api/).

## Inženjering Upita (Prompt Engineering)

Budući da je GPT treniran na velikim količinama podataka za razumijevanje jezika i koda, pruža odgovore na temelju ulaza (upita). Upiti su GPT-ovi ulazi ili upiti gdje se modelima daju upute o zadacima koje trebaju izvršiti. Da biste dobili željeni rezultat, potrebno je osmisliti najučinkovitiji upit, što uključuje odabir pravih riječi, formata, fraza ili čak simbola. Ovaj pristup naziva se [Inženjering Upita](https://learn.microsoft.com/en-us/shows/ai-show/the-basics-of-prompt-engineering-with-azure-openai-service?WT.mc_id=academic-77998-bethanycheum)

[Ova dokumentacija](https://learn.microsoft.com/en-us/semantic-kernel/prompt-engineering/?WT.mc_id=academic-77998-bethanycheum) pruža više informacija o inženjeringu upita.

## ✍️ Primjer Notebooks: [Igranje s OpenAI-GPT](GPT-PyTorch.ipynb)

Nastavite učiti kroz sljedeće notebooks:

* [Generiranje teksta s OpenAI-GPT i Hugging Face Transformers](GPT-PyTorch.ipynb)

## Zaključak

Novi opći unaprijed trenirani jezični modeli ne samo da modeliraju strukturu jezika, već sadrže i ogromnu količinu prirodnog jezika. Stoga se mogu učinkovito koristiti za rješavanje nekih NLP zadataka u zero-shot ili few-shot postavkama.

## [Post-lecture quiz](https://ff-quizzes.netlify.app/en/ai/quiz/40)

---

