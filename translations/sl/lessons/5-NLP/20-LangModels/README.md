<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "2efbb183384a50f0fc0cde02534d912f",
  "translation_date": "2025-08-25T22:08:53+00:00",
  "source_file": "lessons/5-NLP/20-LangModels/README.md",
  "language_code": "sl"
}
-->
# Vnaprej naučeni veliki jezikovni modeli

Pri vseh naših prejšnjih nalogah smo učili nevronsko mrežo za izvajanje določene naloge z uporabo označenega nabora podatkov. Pri velikih transformacijskih modelih, kot je BERT, uporabljamo jezikovno modeliranje na samonadzorovan način za gradnjo jezikovnega modela, ki ga nato s specifičnim usposabljanjem za določeno področje prilagodimo za specifične naloge. Vendar pa je bilo dokazano, da lahko veliki jezikovni modeli rešujejo številne naloge tudi brez kakršnega koli usposabljanja za določeno področje. Družina modelov, ki to omogoča, se imenuje **GPT**: Generativni vnaprej naučeni transformator.

## [Pred-predavanjski kviz](https://ff-quizzes.netlify.app/en/ai/quiz/39)

## Generiranje besedila in zapletenost

Ideja, da lahko nevronska mreža izvaja splošne naloge brez dodatnega usposabljanja, je predstavljena v članku [Language Models are Unsupervised Multitask Learners](https://cdn.openai.com/better-language-models/language_models_are_unsupervised_multitask_learners.pdf). Glavna ideja je, da je mogoče številne druge naloge modelirati z uporabo **generiranja besedila**, saj razumevanje besedila v bistvu pomeni sposobnost njegovega ustvarjanja. Ker je model usposobljen na ogromni količini besedil, ki zajemajo človeško znanje, postane tudi sam "znalec" širokega spektra tem.

> Razumevanje in sposobnost ustvarjanja besedila vključuje tudi poznavanje sveta okoli nas. Ljudje se v veliki meri učijo z branjem, in GPT mreža je v tem pogledu podobna.

Mreže za generiranje besedila delujejo tako, da napovedujejo verjetnost naslednje besede $$P(w_N)$$. Vendar pa je brezpogojna verjetnost naslednje besede enaka pogostosti te besede v korpusu besedil. GPT nam omogoča izračun **pogojne verjetnosti** naslednje besede glede na prejšnje: $$P(w_N | w_{n-1}, ..., w_0)$$

> Več o verjetnostih si lahko preberete v našem [učnem načrtu za začetnike v podatkovni znanosti](https://github.com/microsoft/Data-Science-For-Beginners/tree/main/1-Introduction/04-stats-and-probability).

Kakovost modela za generiranje besedila lahko določimo z uporabo **zapletenosti** (perplexity). To je notranja metrika, ki nam omogoča merjenje kakovosti modela brez uporabe nabora podatkov za specifične naloge. Temelji na konceptu *verjetnosti stavka* - model dodeli visoko verjetnost stavkom, ki so verjetno resnični (tj. model jih ne "zmede"), in nizko verjetnost stavkom, ki so manj smiselni (npr. *Ali lahko to kaj naredi?*). Ko modelu podamo stavke iz resničnega korpusa besedil, pričakujemo, da bodo imeli visoko verjetnost in nizko **zapletenost**. Matematično je zapletenost definirana kot normirana inverzna verjetnost testnega nabora:
$$
\mathrm{Perplexity}(W) = \sqrt[N]{1\over P(W_1,...,W_N)}
$$ 

**Z generiranjem besedila lahko eksperimentirate z uporabo [GPT-poganjanega urejevalnika besedil iz Hugging Face](https://transformer.huggingface.co/doc/gpt2-large)**. V tem urejevalniku začnete pisati svoje besedilo, in s pritiskom na **[TAB]** vam bo ponujenih več možnosti za dokončanje. Če so prekratke ali z njimi niste zadovoljni, ponovno pritisnite [TAB], da dobite več možnosti, vključno z daljšimi deli besedila.

## GPT je družina

GPT ni en sam model, temveč zbirka modelov, ki jih je razvilo in usposobilo [OpenAI](https://openai.com). 

Pod modele GPT spadajo:

| [GPT-2](https://huggingface.co/docs/transformers/model_doc/gpt2#openai-gpt2) | [GPT-3](https://openai.com/research/language-models-are-few-shot-learners) | [GPT-4](https://openai.com/gpt-4) |
| -- | -- | -- |
| Jezikovni model z do 1,5 milijarde parametrov. | Jezikovni model z do 175 milijardami parametrov. | 100T parametrov, sprejema tako slikovne kot besedilne vnose in vrača besedilne izhode. |

Modela GPT-3 in GPT-4 sta na voljo [kot kognitivna storitev prek Microsoft Azure](https://azure.microsoft.com/en-us/services/cognitive-services/openai-service/#overview?WT.mc_id=academic-77998-cacaste) in kot [OpenAI API](https://openai.com/api/).

## Oblikovanje pozivov (Prompt Engineering)

Ker je GPT usposobljen na ogromnih količinah podatkov za razumevanje jezika in kode, ponuja izhode kot odziv na vnose (pozive). Pozivi so vnosi ali poizvedbe za GPT, kjer modelu podate navodila za naloge, ki jih mora opraviti. Da bi dosegli želeni rezultat, potrebujete najučinkovitejši poziv, kar vključuje izbiro pravih besed, formatov, fraz ali celo simbolov. Ta pristop se imenuje [oblikovanje pozivov](https://learn.microsoft.com/en-us/shows/ai-show/the-basics-of-prompt-engineering-with-azure-openai-service?WT.mc_id=academic-77998-bethanycheum).

[Ta dokumentacija](https://learn.microsoft.com/en-us/semantic-kernel/prompt-engineering/?WT.mc_id=academic-77998-bethanycheum) vam ponuja več informacij o oblikovanju pozivov.

## ✍️ Primer beležnice: [Igranje z OpenAI-GPT](../../../../../lessons/5-NLP/20-LangModels/GPT-PyTorch.ipynb)

Nadaljujte z učenjem v naslednjih beležnicah:

* [Generiranje besedila z OpenAI-GPT in Hugging Face Transformers](../../../../../lessons/5-NLP/20-LangModels/GPT-PyTorch.ipynb)

## Zaključek

Novi splošni vnaprej naučeni jezikovni modeli ne modelirajo le jezikovne strukture, temveč vsebujejo tudi ogromno naravnega jezika. Zato jih je mogoče učinkovito uporabiti za reševanje nekaterih nalog obdelave naravnega jezika v nastavitvah brez primerov (zero-shot) ali z malo primeri (few-shot).

## [Po-predavanjski kviz](https://ff-quizzes.netlify.app/en/ai/quiz/40)

**Omejitev odgovornosti**:  
Ta dokument je bil preveden z uporabo storitve AI za prevajanje [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas prosimo, da upoštevate, da lahko avtomatizirani prevodi vsebujejo napake ali netočnosti. Izvirni dokument v njegovem maternem jeziku je treba obravnavati kot avtoritativni vir. Za ključne informacije priporočamo profesionalni človeški prevod. Ne prevzemamo odgovornosti za morebitna nesporazumevanja ali napačne razlage, ki izhajajo iz uporabe tega prevoda.