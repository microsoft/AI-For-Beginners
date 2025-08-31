<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "2efbb183384a50f0fc0cde02534d912f",
  "translation_date": "2025-08-31T17:58:22+00:00",
  "source_file": "lessons/5-NLP/20-LangModels/README.md",
  "language_code": "lt"
}
-->
# Iš anksto apmokyti dideli kalbos modeliai

Visose ankstesnėse užduotyse mes treniravome neuroninį tinklą atlikti tam tikrą užduotį, naudodami pažymėtą duomenų rinkinį. Naudojant didelius transformatorių modelius, tokius kaip BERT, kalbos modeliavimas vykdomas savarankiškai prižiūrimu būdu, siekiant sukurti kalbos modelį, kuris vėliau specializuojamas konkrečiai užduočiai su papildomu domeno specifiniu mokymu. Tačiau buvo įrodyta, kad dideli kalbos modeliai gali išspręsti daugelį užduočių ir be JOKIO domeno specifinio mokymo. Modelių šeima, galinti tai padaryti, vadinama **GPT**: Generatyvus iš anksto apmokytas transformatorius.

## [Prieš paskaitą skirtas testas](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/120)

## Teksto generavimas ir sudėtingumas

Idėja, kad neuroninis tinklas gali atlikti bendras užduotis be papildomo mokymo, pristatoma straipsnyje [Language Models are Unsupervised Multitask Learners](https://cdn.openai.com/better-language-models/language_models_are_unsupervised_multitask_learners.pdf). Pagrindinė mintis yra ta, kad daugelį kitų užduočių galima modeliuoti naudojant **teksto generavimą**, nes teksto supratimas iš esmės reiškia gebėjimą jį kurti. Kadangi modelis yra apmokytas naudojant didžiulį tekstų kiekį, apimantį žmonių žinias, jis taip pat tampa išmanantis įvairias temas.

> Teksto supratimas ir gebėjimas jį kurti taip pat reiškia tam tikrą pasaulio supratimą. Žmonės taip pat daug mokosi skaitydami, ir GPT tinklas šiuo atžvilgiu yra panašus.

Teksto generavimo tinklai veikia prognozuodami kito žodžio tikimybę $$P(w_N)$$. Tačiau besąlyginė kito žodžio tikimybė yra lygi šio žodžio dažniui teksto korpuse. GPT gali pateikti **sąlyginę tikimybę** kito žodžio, atsižvelgiant į ankstesnius: $$P(w_N | w_{n-1}, ..., w_0)$$.

> Daugiau apie tikimybes galite sužinoti mūsų [Duomenų mokslo pradedantiesiems programoje](https://github.com/microsoft/Data-Science-For-Beginners/tree/main/1-Introduction/04-stats-and-probability).

Kalbos generavimo modelio kokybė gali būti apibrėžta naudojant **sudėtingumą**. Tai yra vidinis metrikos rodiklis, leidžiantis įvertinti modelio kokybę be jokio užduočiai specifinio duomenų rinkinio. Jis grindžiamas *sakinių tikimybės* sąvoka – modelis priskiria didelę tikimybę sakiniui, kuris greičiausiai yra realus (t. y. modelis nėra **suklaidintas**), ir mažą tikimybę sakiniams, kurie mažiau prasmingi (pvz., *Ar tai gali ką?*). Kai modelis gauna sakinius iš realaus teksto korpuso, tikimasi, kad jie turės didelę tikimybę ir mažą **sudėtingumą**. Matematiškai tai apibrėžiama kaip normalizuota atvirkštinė testų rinkinio tikimybė:
$$
\mathrm{Perplexity}(W) = \sqrt[N]{1\over P(W_1,...,W_N)}
$$ 

**Galite eksperimentuoti su teksto generavimu naudodami [GPT pagrindu veikiantį teksto redaktorių iš Hugging Face](https://transformer.huggingface.co/doc/gpt2-large)**. Šiame redaktoriuje pradėkite rašyti tekstą, o paspaudus **[TAB]** jums bus pasiūlytos kelios užbaigimo parinktys. Jei jos per trumpos arba jūsų netenkina – paspauskite [TAB] dar kartą, ir gausite daugiau parinkčių, įskaitant ilgesnius teksto fragmentus.

## GPT yra šeima

GPT nėra vienas modelis, o modelių rinkinys, sukurtas ir apmokytas [OpenAI](https://openai.com).

GPT modelių šeimoje yra:

| [GPT-2](https://huggingface.co/docs/transformers/model_doc/gpt2#openai-gpt2) | [GPT 3](https://openai.com/research/language-models-are-few-shot-learners) | [GPT-4](https://openai.com/gpt-4) |
| -- | -- | -- |
| Kalbos modelis su iki 1,5 milijardo parametrų. | Kalbos modelis su iki 175 milijardų parametrų. | 100T parametrai, priimantis tiek vaizdo, tiek teksto įvestis ir išvedantis tekstą. |

GPT-3 ir GPT-4 modeliai yra prieinami [kaip kognityvinė paslauga iš Microsoft Azure](https://azure.microsoft.com/en-us/services/cognitive-services/openai-service/#overview?WT.mc_id=academic-77998-cacaste) ir kaip [OpenAI API](https://openai.com/api/).

## Užklausų inžinerija

Kadangi GPT yra apmokytas naudoti didžiulius duomenų kiekius, kad suprastų kalbą ir kodą, jis pateikia atsakymus įvestims (užklausoms). Užklausos yra GPT įvestys arba užklausimai, kuriais pateikiamos instrukcijos modeliams apie užduotis, kurias jie turi atlikti. Norint gauti norimą rezultatą, reikia efektyviausios užklausos, kuri apima tinkamų žodžių, formatų, frazių ar net simbolių pasirinkimą. Šis metodas vadinamas [užklausų inžinerija](https://learn.microsoft.com/en-us/shows/ai-show/the-basics-of-prompt-engineering-with-azure-openai-service?WT.mc_id=academic-77998-bethanycheum).

[Daugiau informacijos apie užklausų inžineriją rasite šioje dokumentacijoje](https://learn.microsoft.com/en-us/semantic-kernel/prompt-engineering/?WT.mc_id=academic-77998-bethanycheum).

## ✍️ Pavyzdinė užrašų knygelė: [Žaidimas su OpenAI-GPT](GPT-PyTorch.ipynb)

Tęskite mokymąsi šiose užrašų knygelėse:

* [Teksto generavimas su OpenAI-GPT ir Hugging Face Transformers](GPT-PyTorch.ipynb)

## Išvada

Nauji bendrieji iš anksto apmokyti kalbos modeliai ne tik modeliuoja kalbos struktūrą, bet ir turi didžiulį natūralios kalbos žinių kiekį. Todėl jie gali būti efektyviai naudojami sprendžiant kai kurias NLP užduotis be mokymo arba su minimaliu mokymu.

## [Po paskaitos skirtas testas](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/220)

---

**Atsakomybės apribojimas**:  
Šis dokumentas buvo išverstas naudojant AI vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba turėtų būti laikomas autoritetingu šaltiniu. Kritinei informacijai rekomenduojama naudoti profesionalų žmogaus vertimą. Mes neprisiimame atsakomybės už nesusipratimus ar klaidingus interpretavimus, atsiradusius dėl šio vertimo naudojimo.