# Eeltreenitud suured keelemudelid

Kõikides meie varasemates ülesannetes treenisime närvivõrku, et see täidaks teatud ülesannet, kasutades märgistatud andmestikku. Suurte transformer-mudelite, nagu BERT, puhul kasutame keelemodelleerimist isejuhitud viisil, et luua keelemudel, mida seejärel spetsialiseeritakse konkreetsele ülesandele täiendava valdkonnapõhise treeninguga. Siiski on näidatud, et suured keelemudelid suudavad lahendada paljusid ülesandeid ka ILMA valdkonnapõhise treeninguta. Mudelite perekonda, mis seda suudavad, nimetatakse **GPT**: Generatiivne Eeltreenitud Transformer.

## [Eelloengu viktoriin](https://ff-quizzes.netlify.app/en/ai/quiz/39)

## Teksti genereerimine ja hämmeldus

Idee, et närvivõrk suudab täita üldisi ülesandeid ilma täiendava treeninguta, on esitatud artiklis [Language Models are Unsupervised Multitask Learners](https://cdn.openai.com/better-language-models/language_models_are_unsupervised_multitask_learners.pdf). Peamine idee on, et paljusid teisi ülesandeid saab modelleerida **teksti genereerimise** abil, sest teksti mõistmine tähendab sisuliselt ka selle loomise oskust. Kuna mudel on treenitud tohutul hulgal tekstil, mis hõlmab inimteadmisi, muutub see teadlikuks ka väga erinevatest teemadest.

> Teksti mõistmine ja selle loomise oskus tähendab ka midagi teadmist meid ümbritseva maailma kohta. Inimesed õpivad samuti suurel määral lugemise kaudu ning GPT-võrk on selles osas sarnane.

Teksti genereerivad võrgud töötavad järgmise sõna tõenäosuse ennustamise kaudu $$P(w_N)$$. Kuid järgmise sõna tingimusteta tõenäosus võrdub selle sõna sagedusega tekstikorpuses. GPT suudab anda meile järgmise sõna **tingimusliku tõenäosuse**, arvestades eelnevaid sõnu: $$P(w_N | w_{n-1}, ..., w_0)$$

> Lisateavet tõenäosuste kohta leiate meie [Andmeteaduse algajatele mõeldud õppekavast](https://github.com/microsoft/Data-Science-For-Beginners/tree/main/1-Introduction/04-stats-and-probability).

Keele genereerimise mudeli kvaliteeti saab määratleda **hämmelduse** abil. See on sisemine mõõdik, mis võimaldab meil hinnata mudeli kvaliteeti ilma ülesandespetsiifilise andmestikuta. See põhineb *lause tõenäosuse* mõistel - mudel omistab suure tõenäosuse lausele, mis tõenäoliselt on tõeline (st mudel ei ole selle üle **hämmeldunud**) ja madala tõenäosuse lausele, mis tundub vähem loogiline (nt *Kas see saab mida?*). Kui anname oma mudelile lauseid reaalsest tekstikorpusest, ootame, et neil oleks kõrge tõenäosus ja madal **hämmeldus**. Matemaatiliselt on see määratletud testikomplekti normaliseeritud pöördtõenäosusena:
$$
\mathrm{Perplexity}(W) = \sqrt[N]{1\over P(W_1,...,W_N)}
$$ 

**Saate katsetada teksti genereerimist [GPT-põhise Hugging Face'i tekstiredaktoriga](https://transformer.huggingface.co/doc/gpt2-large)**. Selles redaktoris alustate oma teksti kirjutamist ja vajutades **[TAB]** pakutakse teile mitmeid lõpetamisvõimalusi. Kui need on liiga lühikesed või te pole nendega rahul, vajutage [TAB] uuesti ja saate rohkem valikuid, sealhulgas pikemaid tekstiosi.

## GPT on perekond

GPT ei ole üksik mudel, vaid pigem [OpenAI](https://openai.com) poolt välja töötatud ja treenitud mudelite kogum.

GPT mudelite hulka kuuluvad:

| [GPT-2](https://huggingface.co/docs/transformers/model_doc/gpt2#openai-gpt2) | [GPT-3](https://openai.com/research/language-models-are-few-shot-learners) | [GPT-4](https://openai.com/gpt-4) |
| -- | -- | -- |
| Keelemudel kuni 1,5 miljardi parameetriga. | Keelemudel kuni 175 miljardi parameetriga. | 100T parameetrit, mis aktsepteerib nii pildi- kui tekstisisendeid ja väljastab teksti. |

GPT-3 ja GPT-4 mudelid on saadaval [Microsoft Azure'i kognitiivse teenusena](https://azure.microsoft.com/en-us/services/cognitive-services/openai-service/#overview?WT.mc_id=academic-77998-cacaste) ja [OpenAI API-na](https://openai.com/api/).

## Promptide inseneeria

Kuna GPT on treenitud tohutul hulgal andmetel, et mõista keelt ja koodi, annavad need mudelid väljundeid vastuseks sisenditele (promptidele). Promptid on GPT sisendid või päringud, mille kaudu antakse mudelitele juhiseid ülesannete täitmiseks. Soovitud tulemuse saavutamiseks on vaja kõige tõhusamat prompti, mis hõlmab õigete sõnade, vormingute, fraaside või isegi sümbolite valimist. Seda lähenemist nimetatakse [Promptide inseneeriaks](https://learn.microsoft.com/en-us/shows/ai-show/the-basics-of-prompt-engineering-with-azure-openai-service?WT.mc_id=academic-77998-bethanycheum).

[See dokumentatsioon](https://learn.microsoft.com/en-us/semantic-kernel/prompt-engineering/?WT.mc_id=academic-77998-bethanycheum) annab teile rohkem teavet promptide inseneeria kohta.

## ✍️ Näide märkmikust: [Mängimine OpenAI-GPT-ga](GPT-PyTorch.ipynb)

Jätkake õppimist järgmistes märkmikes:

* [Teksti genereerimine OpenAI-GPT ja Hugging Face Transformersiga](GPT-PyTorch.ipynb)

## Kokkuvõte

Uued üldised eeltreenitud keelemudelid ei modelleeri mitte ainult keele struktuuri, vaid sisaldavad ka tohutul hulgal loomulikku keelt. Seega saab neid tõhusalt kasutada mõnede loomuliku keele töötlemise ülesannete lahendamiseks null- või vähese treeninguga.

## [Järelloengu viktoriin](https://ff-quizzes.netlify.app/en/ai/quiz/40)

---

**Lahtiütlus**:  
See dokument on tõlgitud AI tõlketeenuse [Co-op Translator](https://github.com/Azure/co-op-translator) abil. Kuigi püüame tagada täpsust, palume arvestada, et automaatsed tõlked võivad sisaldada vigu või ebatäpsusi. Algne dokument selle algses keeles tuleks pidada autoriteetseks allikaks. Olulise teabe puhul soovitame kasutada professionaalset inimtõlget. Me ei vastuta selle tõlke kasutamisest tulenevate arusaamatuste või valesti tõlgenduste eest.