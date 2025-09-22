<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "2efbb183384a50f0fc0cde02534d912f",
  "translation_date": "2025-08-25T22:06:56+00:00",
  "source_file": "lessons/5-NLP/20-LangModels/README.md",
  "language_code": "sk"
}
-->
# Predtrénované veľké jazykové modely

Vo všetkých našich predchádzajúcich úlohách sme trénovali neurónovú sieť na vykonávanie určitej úlohy pomocou označených dátových súborov. Pri veľkých transformátorových modeloch, ako je BERT, používame modelovanie jazyka v samo-supervidovanom režime na vytvorenie jazykového modelu, ktorý je následne špecializovaný na konkrétnu úlohu pomocou ďalšieho tréningu v špecifickej doméne. Ukázalo sa však, že veľké jazykové modely dokážu riešiť mnohé úlohy aj bez akéhokoľvek tréningu v špecifickej doméne. Rodina modelov, ktoré to dokážu, sa nazýva **GPT**: Generative Pre-Trained Transformer.

## [Kvíz pred prednáškou](https://ff-quizzes.netlify.app/en/ai/quiz/39)

## Generovanie textu a perplexita

Myšlienka, že neurónová sieť dokáže vykonávať všeobecné úlohy bez ďalšieho tréningu, je predstavená v článku [Language Models are Unsupervised Multitask Learners](https://cdn.openai.com/better-language-models/language_models_are_unsupervised_multitask_learners.pdf). Hlavná myšlienka spočíva v tom, že mnohé iné úlohy môžu byť modelované pomocou **generovania textu**, pretože porozumenie textu v podstate znamená schopnosť ho vytvárať. Keďže model je trénovaný na obrovskom množstve textu, ktorý zahŕňa ľudské poznanie, stáva sa znalým v širokej škále tém.

> Porozumenie a schopnosť vytvárať text zahŕňa aj poznanie niečoho o svete okolo nás. Ľudia sa vo veľkej miere učia čítaním a sieť GPT je v tomto ohľade podobná.

Siete na generovanie textu fungujú predpovedaním pravdepodobnosti nasledujúceho slova $$P(w_N)$$. Bezpodmienečná pravdepodobnosť nasledujúceho slova sa rovná frekvencii tohto slova v textovom korpuse. GPT nám však dokáže poskytnúť **podmienenú pravdepodobnosť** nasledujúceho slova na základe predchádzajúcich: $$P(w_N | w_{n-1}, ..., w_0)$$.

> Viac o pravdepodobnostiach si môžete prečítať v našom [kurze Data Science pre začiatočníkov](https://github.com/microsoft/Data-Science-For-Beginners/tree/main/1-Introduction/04-stats-and-probability).

Kvalita modelu na generovanie textu môže byť definovaná pomocou **perplexity**. Ide o vnútornú metriku, ktorá nám umožňuje merať kvalitu modelu bez akéhokoľvek datasetu špecifického pre úlohu. Je založená na pojme *pravdepodobnosti vety* - model priraďuje vysokú pravdepodobnosť vete, ktorá je pravdepodobne reálna (t. j. model nie je z nej **zmätený**), a nízku pravdepodobnosť vetám, ktoré dávajú menší zmysel (napr. *Môže to robiť čo?*). Keď modelu poskytneme vety z reálneho textového korpusu, očakávame, že budú mať vysokú pravdepodobnosť a nízku **perplexitu**. Matematicky je definovaná ako normalizovaná inverzná pravdepodobnosť testovacej množiny:
$$
\mathrm{Perplexity}(W) = \sqrt[N]{1\over P(W_1,...,W_N)}
$$ 

**Môžete experimentovať s generovaním textu pomocou [textového editora poháňaného GPT od Hugging Face](https://transformer.huggingface.co/doc/gpt2-large)**. V tomto editore začnete písať svoj text a stlačením **[TAB]** vám editor ponúkne niekoľko možností dokončenia. Ak sú príliš krátke alebo s nimi nie ste spokojní, stlačte [TAB] znova a získate viac možností, vrátane dlhších častí textu.

## GPT je rodina

GPT nie je jeden model, ale skôr kolekcia modelov vyvinutých a trénovaných [OpenAI](https://openai.com). 

Medzi modely GPT patria:

| [GPT-2](https://huggingface.co/docs/transformers/model_doc/gpt2#openai-gpt2) | [GPT-3](https://openai.com/research/language-models-are-few-shot-learners) | [GPT-4](https://openai.com/gpt-4) |
| -- | -- | -- |
|Jazykový model s až 1,5 miliardami parametrov. | Jazykový model s až 175 miliardami parametrov. | 100T parametrov, akceptuje vstupy vo forme obrázkov aj textu a generuje text. |

Modely GPT-3 a GPT-4 sú dostupné [ako kognitívna služba od Microsoft Azure](https://azure.microsoft.com/en-us/services/cognitive-services/openai-service/#overview?WT.mc_id=academic-77998-cacaste) a ako [OpenAI API](https://openai.com/api/).

## Inžinierstvo výziev (Prompt Engineering)

Keďže GPT bolo trénované na obrovských objemoch dát na porozumenie jazyka a kódu, poskytuje výstupy ako odpovede na vstupy (výzvy). Výzvy sú vstupy alebo dotazy pre GPT, kde poskytujete modelu inštrukcie na úlohy, ktoré má vykonať. Na dosiahnutie požadovaného výsledku potrebujete najefektívnejšiu výzvu, čo zahŕňa výber správnych slov, formátov, fráz alebo dokonca symbolov. Tento prístup sa nazýva [inžinierstvo výziev](https://learn.microsoft.com/en-us/shows/ai-show/the-basics-of-prompt-engineering-with-azure-openai-service?WT.mc_id=academic-77998-bethanycheum).

[Táto dokumentácia](https://learn.microsoft.com/en-us/semantic-kernel/prompt-engineering/?WT.mc_id=academic-77998-bethanycheum) vám poskytne viac informácií o inžinierstve výziev.

## ✍️ Ukážkový notebook: [Hranie sa s OpenAI-GPT](../../../../../lessons/5-NLP/20-LangModels/GPT-PyTorch.ipynb)

Pokračujte vo svojom učení v nasledujúcich notebookoch:

* [Generovanie textu s OpenAI-GPT a Hugging Face Transformers](../../../../../lessons/5-NLP/20-LangModels/GPT-PyTorch.ipynb)

## Záver

Nové všeobecné predtrénované jazykové modely nemodelujú len štruktúru jazyka, ale obsahujú aj obrovské množstvo prirodzeného jazyka. Preto môžu byť efektívne použité na riešenie niektorých NLP úloh v režime zero-shot alebo few-shot.

## [Kvíz po prednáške](https://ff-quizzes.netlify.app/en/ai/quiz/40)

**Upozornenie**:  
Tento dokument bol preložený pomocou služby na automatický preklad [Co-op Translator](https://github.com/Azure/co-op-translator). Hoci sa snažíme o presnosť, upozorňujeme, že automatické preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho pôvodnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nenesieme zodpovednosť za akékoľvek nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.