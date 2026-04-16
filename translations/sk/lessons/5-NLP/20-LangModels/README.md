# Predtrénované veľké jazykové modely

Vo všetkých našich predchádzajúcich úlohách sme trénovali neurónovú sieť na vykonanie určitej úlohy pomocou označeného datasetu. Pri veľkých transformátorových modeloch, ako je BERT, používame jazykové modelovanie v samo-supervízovanom režime na vytvorenie jazykového modelu, ktorý je následne špecializovaný na konkrétnu úlohu pomocou ďalšieho tréningu v špecifickej doméne. Ukázalo sa však, že veľké jazykové modely dokážu riešiť mnohé úlohy aj bez akéhokoľvek tréningu v špecifickej doméne. Rodina modelov schopných to dosiahnuť sa nazýva **GPT**: Generatívny predtrénovaný transformátor.

## [Kvíz pred prednáškou](https://ff-quizzes.netlify.app/en/ai/quiz/39)

## Generovanie textu a perplexita

Myšlienka neurónovej siete schopnej vykonávať všeobecné úlohy bez ďalšieho tréningu je predstavená v článku [Language Models are Unsupervised Multitask Learners](https://cdn.openai.com/better-language-models/language_models_are_unsupervised_multitask_learners.pdf). Hlavná myšlienka je, že mnohé iné úlohy môžu byť modelované pomocou **generovania textu**, pretože porozumenie textu v podstate znamená schopnosť ho produkovať. Keďže model je trénovaný na obrovskom množstve textu, ktorý zahŕňa ľudské poznanie, stáva sa znalým v širokej škále tém.

> Porozumenie a schopnosť produkovať text zahŕňa aj poznanie niečoho o svete okolo nás. Ľudia sa do veľkej miery učia čítaním, a sieť GPT je v tomto ohľade podobná.

Siete na generovanie textu fungujú tak, že predpovedajú pravdepodobnosť nasledujúceho slova $$P(w_N)$$. Bezpodmienečná pravdepodobnosť nasledujúceho slova sa rovná frekvencii tohto slova v textovom korpuse. GPT nám dokáže poskytnúť **podmienenú pravdepodobnosť** nasledujúceho slova, vzhľadom na predchádzajúce: $$P(w_N | w_{n-1}, ..., w_0)$$.

> Viac o pravdepodobnostiach si môžete prečítať v našom [kurze Data Science pre začiatočníkov](https://github.com/microsoft/Data-Science-For-Beginners/tree/main/1-Introduction/04-stats-and-probability).

Kvalitu modelu na generovanie textu možno definovať pomocou **perplexity**. Je to vnútorná metrika, ktorá nám umožňuje merať kvalitu modelu bez akéhokoľvek datasetu špecifického pre úlohu. Je založená na pojme *pravdepodobnosti vety* - model priraďuje vysokú pravdepodobnosť vete, ktorá je pravdepodobne reálna (t.j. model nie je **zmätený**), a nízku pravdepodobnosť vetám, ktoré dávajú menší zmysel (napr. *Môže to robiť čo?*). Keď modelu poskytneme vety z reálneho textového korpusu, očakávame, že budú mať vysokú pravdepodobnosť a nízku **perplexitu**. Matematicky je definovaná ako normalizovaná inverzná pravdepodobnosť testovacej množiny:
$$
\mathrm{Perplexity}(W) = \sqrt[N]{1\over P(W_1,...,W_N)}
$$ 

**Môžete experimentovať s generovaním textu pomocou [textového editora poháňaného GPT od Hugging Face](https://transformer.huggingface.co/doc/gpt2-large)**. V tomto editore začnete písať svoj text a stlačením **[TAB]** vám editor ponúkne niekoľko možností dokončenia. Ak sú príliš krátke alebo s nimi nie ste spokojní - stlačte [TAB] znova a získate viac možností, vrátane dlhších častí textu.

## GPT je rodina

GPT nie je jediný model, ale skôr kolekcia modelov vyvinutých a trénovaných spoločnosťou [OpenAI](https://openai.com). 

Medzi modely GPT patria:

| [GPT-2](https://huggingface.co/docs/transformers/model_doc/gpt2#openai-gpt2) | [GPT 3](https://openai.com/research/language-models-are-few-shot-learners) | [GPT-4](https://openai.com/gpt-4) |
| -- | -- | -- |
| Jazykový model s až 1,5 miliardami parametrov. | Jazykový model s až 175 miliardami parametrov. | 100T parametrov, akceptuje vstupy vo forme obrázkov aj textu a produkuje text. |

Modely GPT-3 a GPT-4 sú dostupné [ako kognitívna služba od Microsoft Azure](https://azure.microsoft.com/en-us/services/cognitive-services/openai-service/#overview?WT.mc_id=academic-77998-cacaste) a ako [OpenAI API](https://openai.com/api/).

## Inžinierstvo promptov

Keďže GPT je trénovaný na obrovských objemoch dát na porozumenie jazyka a kódu, poskytuje výstupy ako odpovede na vstupy (prompty). Prompty sú vstupy alebo dotazy pre GPT, kde poskytujete modelom inštrukcie na úlohy, ktoré majú vykonať. Na dosiahnutie požadovaného výsledku potrebujete najefektívnejší prompt, čo zahŕňa výber správnych slov, formátov, fráz alebo dokonca symbolov. Tento prístup sa nazýva [inžinierstvo promptov](https://learn.microsoft.com/en-us/shows/ai-show/the-basics-of-prompt-engineering-with-azure-openai-service?WT.mc_id=academic-77998-bethanycheum).

[Táto dokumentácia](https://learn.microsoft.com/en-us/semantic-kernel/prompt-engineering/?WT.mc_id=academic-77998-bethanycheum) vám poskytne viac informácií o inžinierstve promptov.

## ✍️ Príkladový notebook: [Hranie sa s OpenAI-GPT](GPT-PyTorch.ipynb)

Pokračujte vo svojom učení v nasledujúcich notebookoch:

* [Generovanie textu s OpenAI-GPT a Hugging Face Transformers](GPT-PyTorch.ipynb)

## Záver

Nové všeobecné predtrénované jazykové modely nemodelujú len štruktúru jazyka, ale obsahujú aj obrovské množstvo prirodzeného jazyka. Preto ich možno efektívne použiť na riešenie niektorých úloh NLP v režime zero-shot alebo few-shot.

## [Kvíz po prednáške](https://ff-quizzes.netlify.app/en/ai/quiz/40)

---

