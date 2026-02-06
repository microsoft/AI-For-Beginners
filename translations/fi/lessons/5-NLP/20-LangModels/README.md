# Esikoulutetut Suuret Kielenmallit

Kaikissa aiemmissa tehtävissämme olemme kouluttaneet neuroverkkoa suorittamaan tietyn tehtävän käyttäen merkittyä aineistoa. Suurten transformer-mallien, kuten BERT:n, kohdalla käytämme kielenmallinnusta itseohjautuvassa muodossa rakentaaksemme kielenmallin, joka sitten erikoistetaan tiettyyn jatkotehtävään lisäkoulutuksella, joka keskittyy tiettyyn alaan. On kuitenkin osoitettu, että suuret kielenmallit voivat ratkaista monia tehtäviä myös ilman mitään alakohtaista koulutusta. Malliperhe, joka pystyy tähän, tunnetaan nimellä **GPT**: Generative Pre-Trained Transformer.

## [Ennakkokysely](https://ff-quizzes.netlify.app/en/ai/quiz/39)

## Tekstintuotanto ja Perpleksisyys

Ajatus siitä, että neuroverkko pystyy suorittamaan yleisiä tehtäviä ilman jatkokoulutusta, esitetään [Language Models are Unsupervised Multitask Learners](https://cdn.openai.com/better-language-models/language_models_are_unsupervised_multitask_learners.pdf) -julkaisussa. Pääidea on, että monet muut tehtävät voidaan mallintaa **tekstintuotannon** avulla, koska tekstin ymmärtäminen tarkoittaa olennaisesti sen tuottamista. Koska malli on koulutettu valtavalla määrällä tekstiä, joka kattaa ihmisen tietämyksen, siitä tulee myös tietoinen monista eri aiheista.

> Tekstin ymmärtäminen ja tuottaminen tarkoittaa myös jonkinlaista tietämystä ympäröivästä maailmasta. Ihmiset oppivat myös suurelta osin lukemalla, ja GPT-verkko on tässä suhteessa samanlainen.

Tekstintuotantoverkot toimivat ennustamalla seuraavan sanan todennäköisyyden $$P(w_N)$$. Kuitenkin seuraavan sanan ehdoton todennäköisyys vastaa tämän sanan esiintymistiheyttä tekstikorpuksessa. GPT pystyy antamaan meille **ehdollisen todennäköisyyden** seuraavalle sanalle, kun edelliset sanat ovat tiedossa: $$P(w_N | w_{n-1}, ..., w_0)$$.

> Voit lukea lisää todennäköisyyksistä [Data Science for Beginners Curriculum](https://github.com/microsoft/Data-Science-For-Beginners/tree/main/1-Introduction/04-stats-and-probability) -materiaalista.

Kielen tuottamisen mallin laatua voidaan määritellä **perpleksisyyden** avulla. Se on sisäinen mittari, joka mahdollistaa mallin laadun arvioinnin ilman mitään tehtäväkohtaista aineistoa. Se perustuu *lauseen todennäköisyyden* käsitteeseen - malli antaa korkeaa todennäköisyyttä lauseelle, joka todennäköisesti on oikea (eli malli ei ole **hämmästynyt** siitä), ja matalaa todennäköisyyttä lauseille, jotka ovat vähemmän järkeviä (esim. *Voiko se tehdä mitä?*). Kun annamme mallille lauseita oikeasta tekstikorpuksesta, odotamme niiden olevan korkealla todennäköisyydellä ja matalalla **perpleksisyydellä**. Matemaattisesti se määritellään testijoukon normalisoituna käänteisenä todennäköisyytenä:
$$
\mathrm{Perplexity}(W) = \sqrt[N]{1\over P(W_1,...,W_N)}
$$ 

**Voit kokeilla tekstintuotantoa [GPT-pohjaisella tekstieditorilla Hugging Facelta](https://transformer.huggingface.co/doc/gpt2-large)**. Tässä editorissa aloitat tekstin kirjoittamisen, ja painamalla **[TAB]** saat useita täydennysvaihtoehtoja. Jos ne ovat liian lyhyitä tai et ole tyytyväinen niihin - paina [TAB] uudelleen, ja saat lisää vaihtoehtoja, mukaan lukien pidempiä tekstikappaleita.

## GPT on Malliperhe

GPT ei ole yksittäinen malli, vaan pikemminkin kokoelma malleja, jotka on kehitetty ja koulutettu [OpenAI:n](https://openai.com) toimesta.

GPT-mallien alla meillä on:

| [GPT-2](https://huggingface.co/docs/transformers/model_doc/gpt2#openai-gpt2) | [GPT-3](https://openai.com/research/language-models-are-few-shot-learners) | [GPT-4](https://openai.com/gpt-4) |
| -- | -- | -- |
|Kielenmalli, jossa jopa 1,5 miljardia parametria. | Kielenmalli, jossa jopa 175 miljardia parametria. | 100T parametria, ja se hyväksyy sekä kuvia että tekstiä syötteenä ja tuottaa tekstiä. |

GPT-3- ja GPT-4-mallit ovat saatavilla [Microsoft Azuren kognitiivisena palveluna](https://azure.microsoft.com/en-us/services/cognitive-services/openai-service/#overview?WT.mc_id=academic-77998-cacaste) ja [OpenAI API:n](https://openai.com/api/) kautta.

## Prompt-suunnittelu

Koska GPT on koulutettu valtavilla datamäärillä ymmärtämään kieltä ja koodia, se tuottaa vastauksia syötteisiin (prompteihin). Promptit ovat GPT:n syötteitä tai kyselyitä, joissa annetaan malleille ohjeita tehtävistä, jotka niiden tulee suorittaa. Halutun lopputuloksen saavuttamiseksi tarvitaan tehokkain prompti, joka sisältää oikeiden sanojen, muotojen, fraasien tai jopa symbolien valinnan. Tätä lähestymistapaa kutsutaan [Prompt-suunnitteluksi](https://learn.microsoft.com/en-us/shows/ai-show/the-basics-of-prompt-engineering-with-azure-openai-service?WT.mc_id=academic-77998-bethanycheum).

[Tämä dokumentaatio](https://learn.microsoft.com/en-us/semantic-kernel/prompt-engineering/?WT.mc_id=academic-77998-bethanycheum) tarjoaa lisätietoa prompt-suunnittelusta.

## ✍️ Esimerkkivihko: [Leikkiminen OpenAI-GPT:n kanssa](GPT-PyTorch.ipynb)

Jatka oppimista seuraavissa vihkoissa:

* [Tekstin tuottaminen OpenAI-GPT:llä ja Hugging Face Transformersilla](GPT-PyTorch.ipynb)

## Yhteenveto

Uudet yleiset esikoulutetut kielenmallit eivät ainoastaan mallinna kielen rakennetta, vaan sisältävät myös valtavan määrän luonnollista kieltä. Näin ollen niitä voidaan tehokkaasti käyttää joidenkin NLP-tehtävien ratkaisemiseen nolla-shot- tai vähä-shot-asetuksissa.

## [Jälkikysely](https://ff-quizzes.netlify.app/en/ai/quiz/40)

---

