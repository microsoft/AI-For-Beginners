<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "31b46ba1f3aa78578134d4829f88be53",
  "translation_date": "2025-08-31T17:56:25+00:00",
  "source_file": "lessons/5-NLP/15-LanguageModeling/README.md",
  "language_code": "lt"
}
-->
# Kalbos modeliavimas

Semantiniai įterpiniai, tokie kaip Word2Vec ir GloVe, iš tiesų yra pirmasis žingsnis link **kalbos modeliavimo** – modelių kūrimo, kurie kažkaip *supranta* (arba *atspindi*) kalbos prigimtį.

## [Prieš paskaitą vykdomas testas](https://ff-quizzes.netlify.app/en/ai/quiz/29)

Pagrindinė kalbos modeliavimo idėja yra jų mokymas su nepažymėtais duomenų rinkiniais nesupervizuotu būdu. Tai svarbu, nes turime didžiulius kiekius nepažymėto teksto, tuo tarpu pažymėto teksto kiekis visada bus ribotas dėl pastangų, reikalingų jį pažymėti. Dažniausiai galime kurti kalbos modelius, kurie gali **prognozuoti trūkstamus žodžius** tekste, nes lengva atsitiktinai užmaskuoti žodį tekste ir naudoti jį kaip mokymo pavyzdį.

## Įterpinių mokymas

Ankstesniuose pavyzdžiuose naudojome iš anksto apmokytus semantinius įterpinius, tačiau įdomu pamatyti, kaip šiuos įterpinius galima apmokyti. Yra keletas galimų idėjų, kurias galima naudoti:

* **N-Gram** kalbos modeliavimas, kai prognozuojame žodį, remdamiesi N ankstesniais žodžiais (N-grama).
* **Nuolatinis žodžių maišas** (CBoW), kai prognozuojame vidurinį žodį $W_0$ žodžių sekoje $W_{-N}$, ..., $W_N$.
* **Skip-gram**, kur prognozuojame kaimyninių žodžių rinkinį {$W_{-N},\dots, W_{-1}, W_1,\dots, W_N$} iš vidurinio žodžio $W_0$.

![vaizdas iš straipsnio apie žodžių konvertavimą į vektorius](../../../../../translated_images/example-algorithms-for-converting-words-to-vectors.fbe9207a726922f6f0f5de66427e8a6eda63809356114e28fb1fa5f4a83ebda7.lt.png)

> Vaizdas iš [šio straipsnio](https://arxiv.org/pdf/1301.3781.pdf)

## ✍️ Pavyzdiniai užrašai: CBoW modelio mokymas

Tęskite mokymąsi šiuose užrašuose:

* [CBoW Word2Vec mokymas naudojant TensorFlow](CBoW-TF.ipynb)
* [CBoW Word2Vec mokymas naudojant PyTorch](CBoW-PyTorch.ipynb)

## Išvada

Ankstesnėje pamokoje matėme, kad žodžių įterpiniai veikia kaip magija! Dabar žinome, kad žodžių įterpinių mokymas nėra labai sudėtinga užduotis, ir prireikus turėtume sugebėti apmokyti savo žodžių įterpinius specifiniam tekstui.

## [Po paskaitos vykdomas testas](https://ff-quizzes.netlify.app/en/ai/quiz/30)

## Apžvalga ir savarankiškas mokymasis

* [Oficialus PyTorch kalbos modeliavimo mokymo vadovas](https://pytorch.org/tutorials/beginner/nlp/word_embeddings_tutorial.html).
* [Oficialus TensorFlow vadovas apie Word2Vec modelio mokymą](https://www.TensorFlow.org/tutorials/text/word2vec).
* Naudojant **gensim** sistemą, dažniausiai naudojamų įterpinių mokymas keliose kodo eilutėse aprašytas [šioje dokumentacijoje](https://pytorch.org/tutorials/beginner/nlp/word_embeddings_tutorial.html).

## 🚀 [Užduotis: Skip-Gram modelio mokymas](lab/README.md)

Laboratorijoje kviečiame jus modifikuoti šios pamokos kodą, kad apmokytumėte Skip-Gram modelį vietoj CBoW. [Skaitykite detales](lab/README.md)

---

**Atsakomybės apribojimas**:  
Šis dokumentas buvo išverstas naudojant AI vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba turėtų būti laikomas autoritetingu šaltiniu. Kritinei informacijai rekomenduojama profesionali žmogaus vertimo paslauga. Mes neprisiimame atsakomybės už nesusipratimus ar klaidingus interpretavimus, atsiradusius naudojant šį vertimą.