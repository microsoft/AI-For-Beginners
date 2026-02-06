# Předtrénované velké jazykové modely

Ve všech našich předchozích úlohách jsme trénovali neuronovou síť, aby vykonávala určitou úlohu pomocí označeného datového souboru. U velkých transformátorových modelů, jako je BERT, používáme jazykové modelování v samostatně řízeném režimu k vytvoření jazykového modelu, který je následně specializován na konkrétní úlohu pomocí dalšího tréninku zaměřeného na danou doménu. Bylo však prokázáno, že velké jazykové modely dokážou řešit mnoho úloh i bez jakéhokoliv tréninku zaměřeného na konkrétní doménu. Rodina modelů schopných tohoto výkonu se nazývá **GPT**: Generative Pre-Trained Transformer.

## [Kvíz před přednáškou](https://ff-quizzes.netlify.app/en/ai/quiz/39)

## Generování textu a perplexita

Myšlenka, že neuronová síť dokáže vykonávat obecné úlohy bez dalšího tréninku, je představena v článku [Language Models are Unsupervised Multitask Learners](https://cdn.openai.com/better-language-models/language_models_are_unsupervised_multitask_learners.pdf). Hlavní myšlenkou je, že mnoho dalších úloh lze modelovat pomocí **generování textu**, protože porozumění textu v podstatě znamená schopnost ho vytvářet. Díky tomu, že model je trénován na obrovském množství textu zahrnujícího lidské znalosti, stává se také znalým v široké škále témat.

> Porozumění textu a schopnost ho vytvářet zahrnuje také znalost světa kolem nás. Lidé se do značné míry učí čtením, a síť GPT je v tomto ohledu podobná.

Sítě pro generování textu fungují na principu předpovídání pravděpodobnosti dalšího slova $$P(w_N)$$. Nicméně, nepodmíněná pravděpodobnost dalšího slova odpovídá frekvenci tohoto slova v textovém korpusu. GPT nám dokáže poskytnout **podmíněnou pravděpodobnost** dalšího slova na základě předchozích slov: $$P(w_N | w_{n-1}, ..., w_0)$$.

> Více o pravděpodobnostech si můžete přečíst v našem [kurzu Data Science pro začátečníky](https://github.com/microsoft/Data-Science-For-Beginners/tree/main/1-Introduction/04-stats-and-probability).

Kvalitu modelu generujícího text lze definovat pomocí **perplexity**. Jedná se o vnitřní metriku, která nám umožňuje měřit kvalitu modelu bez jakéhokoliv datového souboru specifického pro danou úlohu. Je založena na konceptu *pravděpodobnosti věty* - model přiřazuje vysokou pravděpodobnost větám, které jsou pravděpodobně reálné (tj. model není **zmatený**), a nízkou pravděpodobnost větám, které dávají menší smysl (např. *Může to udělat co?*). Když modelu poskytneme věty z reálného textového korpusu, očekáváme, že budou mít vysokou pravděpodobnost a nízkou **perplexitu**. Matematicky je definována jako normalizovaná inverzní pravděpodobnost testovacího souboru:
$$
\mathrm{Perplexity}(W) = \sqrt[N]{1\over P(W_1,...,W_N)}
$$ 

**Můžete experimentovat s generováním textu pomocí [textového editoru poháněného GPT od Hugging Face](https://transformer.huggingface.co/doc/gpt2-large)**. V tomto editoru začnete psát svůj text a stisknutím **[TAB]** vám budou nabídnuty různé možnosti dokončení. Pokud jsou příliš krátké nebo s nimi nejste spokojeni, stiskněte [TAB] znovu a získáte další možnosti, včetně delších částí textu.

## GPT jako rodina

GPT není jediný model, ale spíše kolekce modelů vyvinutých a trénovaných společností [OpenAI](https://openai.com). 

Mezi modely GPT patří:

| [GPT-2](https://huggingface.co/docs/transformers/model_doc/gpt2#openai-gpt2) | [GPT 3](https://openai.com/research/language-models-are-few-shot-learners) | [GPT-4](https://openai.com/gpt-4) |
| -- | -- | -- |
|Jazykový model s až 1,5 miliardami parametrů. | Jazykový model s až 175 miliardami parametrů | 100T parametrů, přijímá jak obrazové, tak textové vstupy a generuje text. |

Modely GPT-3 a GPT-4 jsou dostupné [jako kognitivní služba od Microsoft Azure](https://azure.microsoft.com/en-us/services/cognitive-services/openai-service/#overview?WT.mc_id=academic-77998-cacaste) a také jako [OpenAI API](https://openai.com/api/).

## Prompt Engineering

Protože GPT bylo trénováno na obrovských objemech dat, aby porozumělo jazyku a kódu, poskytuje výstupy v reakci na vstupy (prompty). Prompty jsou vstupy nebo dotazy pro GPT, kdy uživatel poskytuje modelům instrukce k úlohám, které mají být dokončeny. Aby bylo dosaženo požadovaného výsledku, je potřeba co nejefektivnější prompt, což zahrnuje výběr správných slov, formátů, frází nebo dokonce symbolů. Tento přístup se nazývá [Prompt Engineering](https://learn.microsoft.com/en-us/shows/ai-show/the-basics-of-prompt-engineering-with-azure-openai-service?WT.mc_id=academic-77998-bethanycheum).

[Tato dokumentace](https://learn.microsoft.com/en-us/semantic-kernel/prompt-engineering/?WT.mc_id=academic-77998-bethanycheum) vám poskytne více informací o prompt engineeringu.

## ✍️ Ukázkový notebook: [Hraní s OpenAI-GPT](GPT-PyTorch.ipynb)

Pokračujte ve svém učení v následujících noteboocích:

* [Generování textu s OpenAI-GPT a Hugging Face Transformers](GPT-PyTorch.ipynb)

## Závěr

Nové obecné předtrénované jazykové modely nejen modelují strukturu jazyka, ale také obsahují obrovské množství přirozeného jazyka. Díky tomu mohou být efektivně využívány k řešení některých úloh z oblasti zpracování přirozeného jazyka v režimu zero-shot nebo few-shot.

## [Kvíz po přednášce](https://ff-quizzes.netlify.app/en/ai/quiz/40)

---

