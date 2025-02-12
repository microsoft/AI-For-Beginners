# Förtränade Stora Språkmodeller

I alla våra tidigare uppgifter har vi tränat ett neuralt nätverk för att utföra en viss uppgift med hjälp av en märkt dataset. Med stora transformer-modeller, såsom BERT, använder vi språkmodellering på ett självövervakat sätt för att bygga en språkmodell, som sedan specialiseras för specifika nedströmsuppgifter med ytterligare domänspecifik träning. Det har emellertid visat sig att stora språkmodeller också kan lösa många uppgifter utan NÅGON domänspecifik träning. En familj av modeller som kan göra detta kallas **GPT**: Generative Pre-Trained Transformer.

## [För-föreläsningsquiz](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/120)

## Textgenerering och Perplexitet

Idén om att ett neuralt nätverk kan utföra allmänna uppgifter utan nedströms träning presenteras i artikeln [Language Models are Unsupervised Multitask Learners](https://cdn.openai.com/better-language-models/language_models_are_unsupervised_multitask_learners.pdf). Huvudidén är att många andra uppgifter kan modelleras med hjälp av **textgenerering**, eftersom förståelse av text i grunden innebär att kunna producera den. Eftersom modellen tränas på en enorm mängd text som omfattar mänsklig kunskap, blir den också kunnig om en mängd olika ämnen.

> Att förstå och kunna producera text innebär också att veta något om världen omkring oss. Människor lär sig också i stor utsträckning genom att läsa, och GPT-nätverket är liknande i detta avseende.

Textgenereringsnätverk fungerar genom att förutsäga sannolikheten för nästa ord $$P(w_N)$$. Men den ovillkorliga sannolikheten för nästa ord är lika med frekvensen av detta ord i textkorpuset. GPT kan ge oss **villkorlig sannolikhet** för nästa ord, givet de föregående: $$P(w_N | w_{n-1}, ..., w_0)$$

> Du kan läsa mer om sannolikheter i vår [Data Science for Beginners Curriculum](https://github.com/microsoft/Data-Science-For-Beginners/tree/main/1-Introduction/04-stats-and-probability)

Kvaliteten på en språkgenererande modell kan definieras med hjälp av **perplexitet**. Det är en inneboende metrik som gör att vi kan mäta modellens kvalitet utan något uppgiftsspecifikt dataset. Den baseras på begreppet *sannolikheten för en mening* - modellen tilldelar hög sannolikhet till en mening som troligtvis är verklig (dvs. modellen är inte **förvirrad** av den), och låg sannolikhet till meningar som är mindre meningsfulla (t.ex. *Kan den göra vad?*). När vi ger vår modell meningar från ett verkligt textkorpus förväntar vi oss att de har hög sannolikhet och låg **perplexitet**. Matematisk definieras det som normaliserad invers sannolikhet för testuppsättningen:
$$
\mathrm{Perplexity}(W) = \sqrt[N]{1\over P(W_1,...,W_N)}
$$ 

**Du kan experimentera med textgenerering med hjälp av [GPT-drivet textredigerare från Hugging Face](https://transformer.huggingface.co/doc/gpt2-large)**. I denna redigerare börjar du skriva din text, och genom att trycka på **[TAB]** erbjuds du flera alternativ för avslutning. Om de är för korta, eller om du inte är nöjd med dem - tryck [TAB] igen, så får du fler alternativ, inklusive längre texter.

## GPT är en Familj

GPT är inte en enda modell, utan snarare en samling modeller som utvecklats och tränats av [OpenAI](https://openai.com). 

Under GPT-modellerna har vi:

| [GPT-2](https://huggingface.co/docs/transformers/model_doc/gpt2#openai-gpt2) | [GPT 3](https://openai.com/research/language-models-are-few-shot-learners) | [GPT-4](https://openai.com/gpt-4) |
| -- | -- | -- |
|Språkmodell med upp till 1,5 miljarder parametrar. | Språkmodell med upp till 175 miljarder parametrar | 100T parametrar och accepterar både bild- och textinmatningar och producerar text. |


GPT-3 och GPT-4-modellerna är tillgängliga [som en kognitiv tjänst från Microsoft Azure](https://azure.microsoft.com/en-us/services/cognitive-services/openai-service/#overview?WT.mc_id=academic-77998-cacaste), och som [OpenAI API](https://openai.com/api/).

## Prompt Engineering

Eftersom GPT har tränats på stora mängder data för att förstå språk och kod, ger de utdata som svar på indata (prompter). Prompter är GPT-inmatningar eller frågor där man ger instruktioner till modellerna om uppgifter de ska slutföra. För att framkalla ett önskat resultat behöver du den mest effektiva prompten, vilket innebär att välja rätt ord, format, fraser eller till och med symboler. Denna metod kallas [Prompt Engineering](https://learn.microsoft.com/en-us/shows/ai-show/the-basics-of-prompt-engineering-with-azure-openai-service?WT.mc_id=academic-77998-bethanycheum)

[Denna dokumentation](https://learn.microsoft.com/en-us/semantic-kernel/prompt-engineering/?WT.mc_id=academic-77998-bethanycheum) ger dig mer information om prompt engineering.

## ✍️ Exempel Notbok: [Leka med OpenAI-GPT](../../../../../lessons/5-NLP/20-LangModels/GPT-PyTorch.ipynb)

Fortsätt ditt lärande i följande notböcker:

* [Generera text med OpenAI-GPT och Hugging Face Transformers](../../../../../lessons/5-NLP/20-LangModels/GPT-PyTorch.ipynb)

## Slutsats

Nya allmänna förtränade språkmodeller modellerar inte bara språkstruktur, utan innehåller också stora mängder naturligt språk. Därför kan de effektivt användas för att lösa vissa NLP-uppgifter i zero-shot eller few-shot inställningar.

## [Efter-föreläsningsquiz](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/220)

**Ansvarsfriskrivning**:  
Detta dokument har översatts med hjälp av maskinbaserade AI-översättningstjänster. Även om vi strävar efter noggrannhet, vänligen var medveten om att automatiska översättningar kan innehålla fel eller brister. Det ursprungliga dokumentet på sitt modersmål bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för eventuella missförstånd eller feltolkningar som uppstår från användningen av denna översättning.