# Vnaprej naučeni veliki jezikovni modeli

Pri vseh naših prejšnjih nalogah smo trenirali nevronsko mrežo za izvajanje določene naloge z uporabo označenega nabora podatkov. Pri velikih transformacijskih modelih, kot je BERT, uporabljamo jezikovno modeliranje na samonadzorovan način za izdelavo jezikovnega modela, ki ga nato specializiramo za specifične naloge z dodatnim usposabljanjem na področju specifičnih podatkov. Vendar pa je bilo dokazano, da lahko veliki jezikovni modeli rešujejo številne naloge tudi brez KAKRŠNEGA KOLI specifičnega usposabljanja. Družina modelov, ki to zmore, se imenuje **GPT**: Generativni vnaprej naučeni transformator.

## [Pred-predavanjem kviz](https://ff-quizzes.netlify.app/en/ai/quiz/39)

## Generiranje besedila in zmedenost (Perplexity)

Ideja, da lahko nevronska mreža izvaja splošne naloge brez dodatnega usposabljanja, je predstavljena v članku [Language Models are Unsupervised Multitask Learners](https://cdn.openai.com/better-language-models/language_models_are_unsupervised_multitask_learners.pdf). Glavna ideja je, da je mogoče številne druge naloge modelirati z **generiranjem besedila**, saj razumevanje besedila v bistvu pomeni sposobnost njegovega ustvarjanja. Ker je model treniran na ogromni količini besedila, ki zajema človeško znanje, postane tudi seznanjen z različnimi temami.

> Razumevanje in sposobnost ustvarjanja besedila vključuje tudi poznavanje sveta okoli nas. Ljudje se v veliki meri učijo z branjem, GPT mreža pa je v tem pogledu podobna.

Mreže za generiranje besedila delujejo tako, da napovedujejo verjetnost naslednje besede $$P(w_N)$$. Vendar pa brezpogojna verjetnost naslednje besede ustreza pogostosti te besede v korpusu besedila. GPT nam omogoča **pogojno verjetnost** naslednje besede glede na prejšnje: $$P(w_N | w_{n-1}, ..., w_0)$$.

> Več o verjetnostih lahko preberete v našem [Učnem načrtu za začetnike v podatkovni znanosti](https://github.com/microsoft/Data-Science-For-Beginners/tree/main/1-Introduction/04-stats-and-probability).

Kakovost modela za generiranje besedila lahko opredelimo z **zmedenostjo** (perplexity). To je notranja metrika, ki nam omogoča merjenje kakovosti modela brez uporabe specifičnega nabora podatkov za nalogo. Temelji na konceptu *verjetnosti stavka* - model dodeli visoko verjetnost stavku, ki je verjetno resničen (tj. model ni **zmeden** zaradi njega), in nizko verjetnost stavkom, ki manj smiselni (npr. *Ali lahko to naredi kaj?*). Ko modelu podamo stavke iz resničnega korpusa besedila, pričakujemo, da bodo imeli visoko verjetnost in nizko **zmedenost**. Matematično je opredeljena kot normalizirana inverzna verjetnost testnega nabora:
$$
\mathrm{Perplexity}(W) = \sqrt[N]{1\over P(W_1,...,W_N)}
$$ 

**Lahko eksperimentirate z generiranjem besedila z uporabo [GPT-podprtega urejevalnika besedila iz Hugging Face](https://transformer.huggingface.co/doc/gpt2-large)**. V tem urejevalniku začnete pisati svoje besedilo, in s pritiskom na **[TAB]** vam bo ponujenih več možnosti za dokončanje. Če so prekratke ali z njimi niste zadovoljni - ponovno pritisnite [TAB], in dobili boste več možnosti, vključno z daljšimi deli besedila.

## GPT je družina

GPT ni en sam model, temveč zbirka modelov, ki jih je razvil in treniral [OpenAI](https://openai.com).

Pod GPT modeli imamo:

| [GPT-2](https://huggingface.co/docs/transformers/model_doc/gpt2#openai-gpt2) | [GPT 3](https://openai.com/research/language-models-are-few-shot-learners) | [GPT-4](https://openai.com/gpt-4) |
| -- | -- | -- |
| Jezikovni model z do 1,5 milijarde parametrov. | Jezikovni model z do 175 milijardami parametrov. | 100T parametrov, sprejema tako slikovne kot besedilne vnose in generira besedilo. |

Modela GPT-3 in GPT-4 sta na voljo [kot kognitivna storitev prek Microsoft Azure](https://azure.microsoft.com/en-us/services/cognitive-services/openai-service/#overview?WT.mc_id=academic-77998-cacaste) in kot [OpenAI API](https://openai.com/api/).

## Oblikovanje pozivov (Prompt Engineering)

Ker je GPT treniran na ogromnih količinah podatkov za razumevanje jezika in kode, ponuja rezultate kot odziv na vnose (pozive). Pozivi so vnosi ali poizvedbe za GPT, kjer uporabnik poda navodila modelom za naloge, ki jih nato izvedejo. Da bi dosegli želeni rezultat, potrebujete najučinkovitejši poziv, kar vključuje izbiro pravih besed, formatov, fraz ali celo simbolov. Ta pristop se imenuje [Oblikovanje pozivov](https://learn.microsoft.com/en-us/shows/ai-show/the-basics-of-prompt-engineering-with-azure-openai-service?WT.mc_id=academic-77998-bethanycheum).

[Ta dokumentacija](https://learn.microsoft.com/en-us/semantic-kernel/prompt-engineering/?WT.mc_id=academic-77998-bethanycheum) vam ponuja več informacij o oblikovanju pozivov.

## ✍️ Primer zvezka: [Igranje z OpenAI-GPT](GPT-PyTorch.ipynb)

Nadaljujte z učenjem v naslednjih zvezkih:

* [Generiranje besedila z OpenAI-GPT in Hugging Face Transformers](GPT-PyTorch.ipynb)

## Zaključek

Novi splošni vnaprej naučeni jezikovni modeli ne modelirajo le jezikovne strukture, temveč vsebujejo tudi ogromno naravnega jezika. Zato jih je mogoče učinkovito uporabiti za reševanje nekaterih nalog obdelave naravnega jezika v nastavitvah brez usposabljanja (zero-shot) ali z minimalnim usposabljanjem (few-shot).

## [Po-predavanju kviz](https://ff-quizzes.netlify.app/en/ai/quiz/40)

---

