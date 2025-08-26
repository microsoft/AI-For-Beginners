<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "2efbb183384a50f0fc0cde02534d912f",
  "translation_date": "2025-08-25T22:06:15+00:00",
  "source_file": "lessons/5-NLP/20-LangModels/README.md",
  "language_code": "hu"
}
-->
# Előre Trénelt Nagy Nyelvi Modellek

Az eddigi feladataink során egy neurális hálót tanítottunk be egy adott feladat elvégzésére címkézett adathalmaz segítségével. Nagy transzformer modellek, mint például a BERT esetében, önfelügyelt nyelvi modellezést használunk egy nyelvi modell létrehozásához, amelyet aztán további, specifikus területekre irányuló képzéssel specializálunk konkrét feladatokra. Azonban bebizonyosodott, hogy a nagy nyelvi modellek számos feladatot képesek megoldani bármiféle területspecifikus képzés nélkül is. Az ilyen modellek családját **GPT**-nek, azaz Generatív Előre Trénelt Transzformernek nevezzük.

## [Előadás előtti kvíz](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/120)

## Szöveg Generálás és Perplexitás

Az a gondolat, hogy egy neurális háló képes általános feladatokat elvégezni utólagos képzés nélkül, a [Language Models are Unsupervised Multitask Learners](https://cdn.openai.com/better-language-models/language_models_are_unsupervised_multitask_learners.pdf) című tanulmányban kerül bemutatásra. A fő elképzelés az, hogy számos más feladat modellezhető **szöveg generálás** segítségével, mivel a szöveg megértése lényegében azt jelenti, hogy képesek vagyunk előállítani azt. Mivel a modell hatalmas mennyiségű szövegen van betanítva, amely az emberi tudást öleli fel, széles körű témákban ismereteket szerez.

> A szöveg megértése és előállítása magában foglalja a körülöttünk lévő világ ismeretét is. Az emberek nagy mértékben olvasás útján tanulnak, és a GPT hálózat ebben hasonló.

A szöveg generáló hálózatok úgy működnek, hogy megjósolják a következő szó valószínűségét $$P(w_N)$$. Azonban a következő szó feltétel nélküli valószínűsége megegyezik ennek a szónak a szövegkorpuszban való gyakoriságával. A GPT képes megadni a következő szó **feltételes valószínűségét**, figyelembe véve az előző szavakat: $$P(w_N | w_{n-1}, ..., w_0)$$.

> További információt a valószínűségekről a [Data Science for Beginners Curriculum](https://github.com/microsoft/Data-Science-For-Beginners/tree/main/1-Introduction/04-stats-and-probability) című anyagunkban találhatsz.

A nyelvi generáló modellek minőségét **perplexitás** segítségével lehet meghatározni. Ez egy belső metrika, amely lehetővé teszi a modell minőségének mérését bármiféle feladatspecifikus adathalmaz nélkül. Az *egy mondat valószínűségének* fogalmán alapul - a modell magas valószínűséget rendel egy olyan mondathoz, amely valószínűleg valódi (azaz a modell nem **zavarodott** meg tőle), és alacsony valószínűséget olyan mondatokhoz, amelyek kevésbé értelmesek (pl. *Can it does what?*). Ha a modellnek valódi szövegkorpusz mondatokat adunk, elvárjuk, hogy magas valószínűséget és alacsony **perplexitást** kapjunk. Matematikailag a perplexitás a teszthalmaz normalizált inverz valószínűségeként van definiálva:
$$
\mathrm{Perplexity}(W) = \sqrt[N]{1\over P(W_1,...,W_N)}
$$ 

**Kísérletezhetsz szöveg generálással a [GPT-alapú szövegszerkesztővel a Hugging Face-től](https://transformer.huggingface.co/doc/gpt2-large)**. Ebben a szerkesztőben elkezdheted írni a szövegedet, és a **[TAB]** megnyomásával több befejezési lehetőséget kapsz. Ha ezek túl rövidek, vagy nem vagy elégedett velük - nyomd meg újra a [TAB]-ot, és további lehetőségeket kapsz, beleértve hosszabb szövegrészeket is.

## A GPT egy Család

A GPT nem egyetlen modell, hanem a [OpenAI](https://openai.com) által fejlesztett és betanított modellek gyűjteménye.

A GPT modellek között található:

| [GPT-2](https://huggingface.co/docs/transformers/model_doc/gpt2#openai-gpt2) | [GPT 3](https://openai.com/research/language-models-are-few-shot-learners) | [GPT-4](https://openai.com/gpt-4) |
| -- | -- | -- |
|Nyelvi modell akár 1,5 milliárd paraméterrel. | Nyelvi modell akár 175 milliárd paraméterrel. | 100T paraméterrel, és képes képeket és szövegeket is bemenetként fogadni, valamint szöveget generálni kimenetként. |

A GPT-3 és GPT-4 modellek elérhetők [Microsoft Azure kognitív szolgáltatásként](https://azure.microsoft.com/en-us/services/cognitive-services/openai-service/#overview?WT.mc_id=academic-77998-cacaste), valamint [OpenAI API](https://openai.com/api) formájában.

## Prompt Engineering

Mivel a GPT hatalmas mennyiségű adat alapján van betanítva, hogy megértse a nyelvet és a kódot, válaszokat ad a bemenetekre (promptekre). A promtpek a GPT bemenetei vagy lekérdezései, amelyekben utasításokat adunk a modelleknek az elvégzendő feladatokról. Ahhoz, hogy a kívánt eredményt kapjuk, a leghatékonyabb promptot kell megalkotnunk, amely magában foglalja a megfelelő szavak, formátumok, kifejezések vagy akár szimbólumok kiválasztását. Ezt a megközelítést [Prompt Engineering](https://learn.microsoft.com/en-us/shows/ai-show/the-basics-of-prompt-engineering-with-azure-openai-service?WT.mc_id=academic-77998-bethanycheum) néven ismerjük.

[Ez a dokumentáció](https://learn.microsoft.com/en-us/semantic-kernel/prompt-engineering/?WT.mc_id=academic-77998-bethanycheum) további információt nyújt a prompt engineeringről.

## ✍️ Példa Notebook: [Játék az OpenAI-GPT-vel](../../../../../lessons/5-NLP/20-LangModels/GPT-PyTorch.ipynb)

Folytasd a tanulást az alábbi notebookokban:

* [Szöveg generálása OpenAI-GPT és Hugging Face Transformers segítségével](../../../../../lessons/5-NLP/20-LangModels/GPT-PyTorch.ipynb)

## Következtetés

Az új általános előre trénelt nyelvi modellek nemcsak a nyelvi struktúrát modellezik, hanem hatalmas mennyiségű természetes nyelvet is tartalmaznak. Ezért hatékonyan használhatók bizonyos NLP feladatok megoldására nulla vagy kevés tanítással.

## [Előadás utáni kvíz](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/220)

**Felelősség kizárása**:  
Ez a dokumentum az AI fordítási szolgáltatás [Co-op Translator](https://github.com/Azure/co-op-translator) segítségével lett lefordítva. Bár törekszünk a pontosságra, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az eredeti nyelvén tekintendő hiteles forrásnak. Fontos információk esetén javasolt professzionális emberi fordítást igénybe venni. Nem vállalunk felelősséget semmilyen félreértésért vagy téves értelmezésért, amely a fordítás használatából eredhet.