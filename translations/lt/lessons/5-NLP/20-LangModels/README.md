# Iš anksto apmokyti dideli kalbos modeliai

Visose ankstesnėse užduotyse mes treniravome neuroninius tinklus atlikti tam tikras užduotis, naudodami pažymėtus duomenų rinkinius. Naudojant didelius transformatorių modelius, tokius kaip BERT, kalbos modeliavimas vykdomas savarankiškai mokantis, siekiant sukurti kalbos modelį, kuris vėliau specializuojamas konkrečiai užduočiai, atliekant papildomą mokymą konkrečioje srityje. Tačiau buvo įrodyta, kad dideli kalbos modeliai gali spręsti daugelį užduočių be JOKIO specifinio mokymo. Modelių šeima, galinti tai atlikti, vadinama **GPT**: Generatyvus iš anksto apmokytas transformatorius.

## [Prieš paskaitą vykdomas testas](https://ff-quizzes.netlify.app/en/ai/quiz/39)

## Teksto generavimas ir sudėtingumas

Idėja, kad neuroninis tinklas gali atlikti bendras užduotis be papildomo mokymo, pristatyta straipsnyje [Language Models are Unsupervised Multitask Learners](https://cdn.openai.com/better-language-models/language_models_are_unsupervised_multitask_learners.pdf). Pagrindinė mintis yra ta, kad daugelį kitų užduočių galima modeliuoti naudojant **teksto generavimą**, nes teksto supratimas iš esmės reiškia gebėjimą jį kurti. Kadangi modelis yra apmokytas naudojant didžiulį tekstų kiekį, apimantį žmonių žinias, jis taip pat tampa išmanantis įvairias temas.

> Teksto supratimas ir gebėjimas jį kurti taip pat reiškia tam tikrą pasaulio supratimą. Žmonės taip pat daug mokosi skaitydami, ir GPT tinklas yra panašus šiuo atžvilgiu.

Teksto generavimo tinklai veikia prognozuodami kito žodžio tikimybę $$P(w_N)$$. Tačiau besąlyginė kito žodžio tikimybė lygi šio žodžio dažniui teksto korpuse. GPT gali pateikti **sąlyginę tikimybę** kito žodžio, atsižvelgiant į ankstesnius: $$P(w_N | w_{n-1}, ..., w_0)$$.

> Daugiau apie tikimybes galite perskaityti mūsų [Duomenų mokslas pradedantiesiems mokymo programoje](https://github.com/microsoft/Data-Science-For-Beginners/tree/main/1-Introduction/04-stats-and-probability).

Kalbos generavimo modelio kokybė gali būti apibrėžta naudojant **sudėtingumą**. Tai yra vidinis matas, leidžiantis įvertinti modelio kokybę be jokio užduočiai specifinio duomenų rinkinio. Jis grindžiamas *sakinių tikimybės* sąvoka – modelis priskiria aukštą tikimybę sakiniui, kuris greičiausiai yra realus (t. y. modelis nėra **sutrikęs** dėl jo), ir žemą tikimybę sakiniams, kurie mažiau prasmingi (pvz., *Ar tai gali ką?*). Kai modelis gauna sakinius iš realaus teksto korpuso, tikimasi, kad jie turės aukštą tikimybę ir žemą **sudėtingumą**. Matematiškai tai apibrėžiama kaip normalizuota atvirkštinė testų rinkinio tikimybė:
$$
\mathrm{Perplexity}(W) = \sqrt[N]{1\over P(W_1,...,W_N)}
$$ 

**Galite eksperimentuoti su teksto generavimu naudodami [GPT pagrįstą teksto redaktorių iš Hugging Face](https://transformer.huggingface.co/doc/gpt2-large)**. Šiame redaktoriuje pradėkite rašyti tekstą, o paspaudus **[TAB]** jums bus pasiūlytos kelios užbaigimo parinktys. Jei jos per trumpos arba nesate patenkinti – paspauskite [TAB] dar kartą, ir gausite daugiau parinkčių, įskaitant ilgesnius teksto fragmentus.

## GPT yra šeima

GPT nėra vienas modelis, o modelių kolekcija, sukurta ir apmokyta [OpenAI](https://openai.com).

GPT modelių šeimą sudaro:

| [GPT-2](https://huggingface.co/docs/transformers/model_doc/gpt2#openai-gpt2) | [GPT 3](https://openai.com/research/language-models-are-few-shot-learners) | [GPT-4](https://openai.com/gpt-4) |
| -- | -- | -- |
| Kalbos modelis su iki 1,5 milijardo parametrų. | Kalbos modelis su iki 175 milijardų parametrų. | 100T parametrai, priima tiek vaizdo, tiek teksto įvestis ir pateikia teksto išvestis. |

GPT-3 ir GPT-4 modeliai yra prieinami [kaip kognityvinė paslauga iš Microsoft Azure](https://azure.microsoft.com/en-us/services/cognitive-services/openai-service/#overview?WT.mc_id=academic-77998-cacaste) ir kaip [OpenAI API](https://openai.com/api/).

## Užklausų kūrimas (Prompt Engineering)

Kadangi GPT buvo apmokytas didžiuliais duomenų kiekiais, kad suprastų kalbą ir kodą, jis pateikia atsakymus įvestims (užklausoms). Užklausos yra GPT įvestys arba užklausimai, kuriais pateikiamos instrukcijos modeliams apie užduotis, kurias jie turi atlikti. Norint gauti norimą rezultatą, reikia efektyviausios užklausos, kuri apima tinkamų žodžių, formatų, frazių ar net simbolių pasirinkimą. Šis metodas vadinamas [užklausų kūrimu](https://learn.microsoft.com/en-us/shows/ai-show/the-basics-of-prompt-engineering-with-azure-openai-service?WT.mc_id=academic-77998-bethanycheum).

[Dokumentacija](https://learn.microsoft.com/en-us/semantic-kernel/prompt-engineering/?WT.mc_id=academic-77998-bethanycheum) suteikia daugiau informacijos apie užklausų kūrimą.

## ✍️ Pavyzdinė užrašų knygelė: [Darbas su OpenAI-GPT](GPT-PyTorch.ipynb)

Tęskite mokymąsi šiose užrašų knygelėse:

* [Teksto generavimas su OpenAI-GPT ir Hugging Face Transformers](GPT-PyTorch.ipynb)

## Išvada

Nauji bendrieji iš anksto apmokyti kalbos modeliai ne tik modeliuoja kalbos struktūrą, bet ir apima didžiulį kiekį natūralios kalbos. Todėl jie gali būti efektyviai naudojami kai kurioms NLP užduotims spręsti be mokymo arba su minimaliais mokymo duomenimis.

## [Po paskaitos vykdomas testas](https://ff-quizzes.netlify.app/en/ai/quiz/40)

---

