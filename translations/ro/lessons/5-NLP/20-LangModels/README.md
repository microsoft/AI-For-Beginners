<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "2efbb183384a50f0fc0cde02534d912f",
  "translation_date": "2025-08-25T22:07:24+00:00",
  "source_file": "lessons/5-NLP/20-LangModels/README.md",
  "language_code": "ro"
}
-->
# Modele Mari de Limbaj Pre-Antrenate

În toate sarcinile noastre anterioare, am antrenat o rețea neuronală pentru a îndeplini o anumită sarcină folosind un set de date etichetat. Cu modelele mari de tip transformer, precum BERT, folosim modelarea limbajului într-un mod auto-supervizat pentru a construi un model de limbaj, care este apoi specializat pentru o sarcină specifică printr-un antrenament suplimentar pe un domeniu specific. Totuși, s-a demonstrat că modelele mari de limbaj pot rezolva multe sarcini fără NICIUN antrenament specific pe domeniu. O familie de modele capabile să facă acest lucru se numește **GPT**: Transformer Generativ Pre-Antrenat.

## [Chestionar înainte de curs](https://ff-quizzes.netlify.app/en/ai/quiz/39)

## Generarea de Text și Perplexitatea

Ideea unei rețele neuronale capabile să îndeplinească sarcini generale fără antrenament suplimentar este prezentată în lucrarea [Language Models are Unsupervised Multitask Learners](https://cdn.openai.com/better-language-models/language_models_are_unsupervised_multitask_learners.pdf). Ideea principală este că multe alte sarcini pot fi modelate folosind **generarea de text**, deoarece înțelegerea textului înseamnă, în esență, a fi capabil să îl produci. Deoarece modelul este antrenat pe o cantitate uriașă de text care cuprinde cunoștințele umane, acesta devine, de asemenea, informat despre o mare varietate de subiecte.

> Înțelegerea și capacitatea de a produce text implică, de asemenea, cunoașterea lumii din jurul nostru. Oamenii învață, în mare măsură, citind, iar rețeaua GPT este similară în acest sens.

Rețelele de generare de text funcționează prin prezicerea probabilității următorului cuvânt $$P(w_N)$$. Totuși, probabilitatea necondiționată a următorului cuvânt este egală cu frecvența acestui cuvânt în corpusul de text. GPT este capabil să ne ofere **probabilitatea condiționată** a următorului cuvânt, având în vedere cuvintele anterioare: $$P(w_N | w_{n-1}, ..., w_0)$$

> Puteți citi mai multe despre probabilități în [Curriculum-ul nostru de Știința Datelor pentru Începători](https://github.com/microsoft/Data-Science-For-Beginners/tree/main/1-Introduction/04-stats-and-probability).

Calitatea unui model de generare a limbajului poate fi definită folosind **perplexitatea**. Este o metrică intrinsecă care ne permite să măsurăm calitatea modelului fără un set de date specific sarcinii. Aceasta se bazează pe noțiunea de *probabilitate a unei propoziții* - modelul atribuie o probabilitate mare unei propoziții care este probabil să fie reală (adică modelul nu este **perplex** de aceasta) și o probabilitate mică propozițiilor care au mai puțin sens (de exemplu, *Poate face ce?*). Când oferim modelului propoziții dintr-un corpus de text real, ne-am aștepta ca acestea să aibă o probabilitate mare și o **perplexitate** scăzută. Matematic, aceasta este definită ca probabilitatea inversă normalizată a setului de testare:
$$
\mathrm{Perplexity}(W) = \sqrt[N]{1\over P(W_1,...,W_N)}
$$ 

**Puteți experimenta cu generarea de text folosind [editorul de text bazat pe GPT de la Hugging Face](https://transformer.huggingface.co/doc/gpt2-large)**. În acest editor, începeți să scrieți textul, iar apăsarea tastei **[TAB]** vă va oferi mai multe opțiuni de completare. Dacă acestea sunt prea scurte sau nu sunteți mulțumit de ele - apăsați din nou [TAB], și veți avea mai multe opțiuni, inclusiv fragmente mai lungi de text.

## GPT este o Familie

GPT nu este un singur model, ci mai degrabă o colecție de modele dezvoltate și antrenate de [OpenAI](https://openai.com). 

Sub umbrela modelelor GPT, avem:

| [GPT-2](https://huggingface.co/docs/transformers/model_doc/gpt2#openai-gpt2) | [GPT-3](https://openai.com/research/language-models-are-few-shot-learners) | [GPT-4](https://openai.com/gpt-4) |
| -- | -- | -- |
| Model de limbaj cu până la 1,5 miliarde de parametri. | Model de limbaj cu până la 175 miliarde de parametri. | 100T parametri și acceptă atât intrări de tip imagine, cât și text, oferind ieșiri sub formă de text. |

Modelele GPT-3 și GPT-4 sunt disponibile [ca serviciu cognitiv de la Microsoft Azure](https://azure.microsoft.com/en-us/services/cognitive-services/openai-service/#overview?WT.mc_id=academic-77998-cacaste) și prin [API-ul OpenAI](https://openai.com/api/).

## Ingineria Prompturilor

Deoarece GPT a fost antrenat pe volume vaste de date pentru a înțelege limbajul și codul, acestea oferă răspunsuri la intrări (prompturi). Prompturile sunt intrările sau interogările pentru GPT, prin care se oferă instrucțiuni modelelor pentru sarcinile pe care urmează să le finalizeze. Pentru a obține un rezultat dorit, este necesar un prompt eficient, care implică selectarea cuvintelor, formatelor, frazelor sau chiar simbolurilor potrivite. Această abordare se numește [Ingineria Prompturilor](https://learn.microsoft.com/en-us/shows/ai-show/the-basics-of-prompt-engineering-with-azure-openai-service?WT.mc_id=academic-77998-bethanycheum).

[Această documentație](https://learn.microsoft.com/en-us/semantic-kernel/prompt-engineering/?WT.mc_id=academic-77998-bethanycheum) vă oferă mai multe informații despre ingineria prompturilor.

## ✍️ Notebook Exemplu: [Experimentând cu OpenAI-GPT](../../../../../lessons/5-NLP/20-LangModels/GPT-PyTorch.ipynb)

Continuați învățarea cu următoarele notebook-uri:

* [Generarea de text cu OpenAI-GPT și Hugging Face Transformers](../../../../../lessons/5-NLP/20-LangModels/GPT-PyTorch.ipynb)

## Concluzie

Noile modele generale de limbaj pre-antrenate nu doar modelează structura limbajului, ci conțin și o cantitate vastă de limbaj natural. Astfel, ele pot fi utilizate eficient pentru a rezolva unele sarcini NLP în setări zero-shot sau few-shot.

## [Chestionar după curs](https://ff-quizzes.netlify.app/en/ai/quiz/40)

**Declinare de responsabilitate**:  
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). Deși ne străduim să asigurăm acuratețea, vă rugăm să fiți conștienți că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa natală ar trebui considerat sursa autoritară. Pentru informații critice, se recomandă traducerea profesională realizată de un specialist uman. Nu ne asumăm responsabilitatea pentru eventualele neînțelegeri sau interpretări greșite care pot apărea din utilizarea acestei traduceri.