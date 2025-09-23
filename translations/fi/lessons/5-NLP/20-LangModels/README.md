<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "2efbb183384a50f0fc0cde02534d912f",
  "translation_date": "2025-08-28T20:02:51+00:00",
  "source_file": "lessons/5-NLP/20-LangModels/README.md",
  "language_code": "fi"
}
-->
# Esikoulutetut suuret kielimallit

Kaikissa aiemmissa tehtävissämme olemme kouluttaneet neuroverkkoa suorittamaan tietyn tehtävän käyttäen merkittyä tietojoukkoa. Suurten transformer-mallien, kuten BERT, avulla käytämme kielen mallinnusta itseohjautuvassa muodossa rakentaaksemme kielimallin, joka sitten erikoistetaan tiettyyn jälkikäteen tehtävään lisäkoulutuksella, joka keskittyy tiettyyn alaan. On kuitenkin osoitettu, että suuret kielimallit voivat ratkaista monia tehtäviä ilman MITÄÄN alakohtaista koulutusta. Malliperhe, joka pystyy tähän, tunnetaan nimellä **GPT**: Generative Pre-Trained Transformer.

## [Ennakkokysely](https://ff-quizzes.netlify.app/en/ai/quiz/39)

## Tekstintuotanto ja hämmennys (perplexity)

Ajatus siitä, että neuroverkko pystyy suorittamaan yleisiä tehtäviä ilman jälkikoulutusta, esitetään [Language Models are Unsupervised Multitask Learners](https://cdn.openai.com/better-language-models/language_models_are_unsupervised_multitask_learners.pdf) -julkaisussa. Pääajatus on, että monet muut tehtävät voidaan mallintaa **tekstintuotannon** avulla, koska tekstin ymmärtäminen tarkoittaa olennaisesti sen tuottamista. Koska malli on koulutettu valtavalla määrällä tekstiä, joka kattaa ihmisen tiedon, siitä tulee myös tietoinen monista eri aiheista.

> Tekstin ymmärtäminen ja tuottaminen tarkoittaa myös jonkinlaista tietämystä ympäröivästä maailmasta. Ihmiset oppivat suurelta osin lukemalla, ja GPT-verkko on tässä suhteessa samanlainen.

Tekstintuotantoverkot toimivat ennustamalla seuraavan sanan todennäköisyyden $$P(w_N)$$. Kuitenkin seuraavan sanan ehdoton todennäköisyys vastaa tämän sanan esiintymistiheyttä tekstikorpuksessa. GPT pystyy antamaan meille **ehdollisen todennäköisyyden** seuraavalle sanalle, kun edelliset sanat ovat tiedossa: $$P(w_N | w_{n-1}, ..., w_0)$$.

> Voit lukea lisää todennäköisyyksistä [Data Science for Beginners Curriculum](https://github.com/microsoft/Data-Science-For-Beginners/tree/main/1-Introduction/04-stats-and-probability) -materiaalistamme.

Kielimallin laatua voidaan määritellä **hämmennyksen** avulla. Se on sisäinen mittari, joka mahdollistaa mallin laadun arvioinnin ilman tehtäväkohtaista tietojoukkoa. Se perustuu *lauseen todennäköisyyden* käsitteeseen - malli antaa korkean todennäköisyyden lauseelle, joka todennäköisesti on todellinen (eli malli ei ole **hämmästynyt** siitä), ja matalan todennäköisyyden lauseille, jotka ovat vähemmän järkeviä (esim. *Can it does what?*). Kun annamme mallille lauseita todellisesta tekstikorpuksesta, odotamme niiden olevan korkealla todennäköisyydellä ja matalalla **hämmennyksellä**. Matemaattisesti se määritellään testijoukon normalisoituna käänteisenä todennäköisyytenä:
$$
\mathrm{Perplexity}(W) = \sqrt[N]{1\over P(W_1,...,W_N)}
$$ 

**Voit kokeilla tekstintuotantoa [GPT-pohjaisella tekstieditorilla Hugging Facelta](https://transformer.huggingface.co/doc/gpt2-large)**. Tässä editorissa aloitat tekstin kirjoittamisen, ja painamalla **[TAB]** saat useita täydennysvaihtoehtoja. Jos ne ovat liian lyhyitä tai et ole tyytyväinen niihin - paina [TAB] uudelleen, ja saat lisää vaihtoehtoja, mukaan lukien pidempiä tekstipätkiä.

## GPT on perhe

GPT ei ole yksittäinen malli, vaan pikemminkin kokoelma malleja, jotka on kehitetty ja koulutettu [OpenAI:n](https://openai.com) toimesta.

GPT-mallien alla on:

| [GPT-2](https://huggingface.co/docs/transformers/model_doc/gpt2#openai-gpt2) | [GPT-3](https://openai.com/research/language-models-are-few-shot-learners) | [GPT-4](https://openai.com/gpt-4) |
| -- | -- | -- |
|Kielimalli, jossa jopa 1,5 miljardia parametria. | Kielimalli, jossa jopa 175 miljardia parametria. | 100T parametria, ja se hyväksyy sekä kuva- että tekstisyötteitä ja tuottaa tekstiä. |

GPT-3- ja GPT-4-mallit ovat saatavilla [Microsoft Azuren kognitiivisena palveluna](https://azure.microsoft.com/en-us/services/cognitive-services/openai-service/#overview?WT.mc_id=academic-77998-cacaste) sekä [OpenAI API:n](https://openai.com/api) kautta.

## Kehoteiden suunnittelu

Koska GPT on koulutettu valtavilla tietomäärillä ymmärtämään kieltä ja koodia, se tuottaa vastauksia syötteisiin (kehotteisiin). Kehotteet ovat GPT:n syötteitä tai kyselyitä, joissa annetaan malleille ohjeita seuraavaksi suoritettavista tehtävistä. Halutun lopputuloksen saavuttamiseksi tarvitaan tehokkain kehote, joka sisältää oikeiden sanojen, muotojen, fraasien tai jopa symbolien valinnan. Tätä lähestymistapaa kutsutaan [kehotteiden suunnitteluksi](https://learn.microsoft.com/en-us/shows/ai-show/the-basics-of-prompt-engineering-with-azure-openai-service?WT.mc_id=academic-77998-bethanycheum).

[Tämä dokumentaatio](https://learn.microsoft.com/en-us/semantic-kernel/prompt-engineering/?WT.mc_id=academic-77998-bethanycheum) tarjoaa lisätietoa kehotteiden suunnittelusta.

## ✍️ Esimerkkivihko: [Leikkiminen OpenAI-GPT:n kanssa](GPT-PyTorch.ipynb)

Jatka oppimista seuraavissa vihkoissa:

* [Tekstin tuottaminen OpenAI-GPT:llä ja Hugging Face Transformersilla](GPT-PyTorch.ipynb)

## Yhteenveto

Uudet yleiset esikoulutetut kielimallit eivät ainoastaan mallinna kielen rakennetta, vaan sisältävät myös valtavan määrän luonnollista kieltä. Näin ollen niitä voidaan tehokkaasti käyttää joidenkin NLP-tehtävien ratkaisemiseen nolla- tai vähäisellä koulutuksella.

## [Jälkikysely](https://ff-quizzes.netlify.app/en/ai/quiz/40)

---

**Vastuuvapauslauseke**:  
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, huomioithan, että automaattiset käännökset voivat sisältää virheitä tai epätarkkuuksia. Alkuperäinen asiakirja sen alkuperäisellä kielellä tulisi pitää ensisijaisena lähteenä. Kriittisen tiedon osalta suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa väärinkäsityksistä tai virhetulkinnoista, jotka johtuvat tämän käännöksen käytöstä.