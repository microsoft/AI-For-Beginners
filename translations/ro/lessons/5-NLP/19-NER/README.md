# Recunoașterea Entităților Denumite

Până acum, ne-am concentrat în principal pe o singură sarcină NLP - clasificarea. Totuși, există și alte sarcini NLP care pot fi realizate cu ajutorul rețelelor neuronale. Una dintre aceste sarcini este **[Recunoașterea Entităților Denumite](https://wikipedia.org/wiki/Named-entity_recognition)** (NER), care se ocupă cu identificarea entităților specifice din text, cum ar fi locuri, nume de persoane, intervale de timp, formule chimice și altele.

## [Chestionar înainte de lecție](https://ff-quizzes.netlify.app/en/ai/quiz/37)

## Exemplu de Utilizare a NER

Să presupunem că dorești să dezvolți un chatbot de limbaj natural, similar cu Amazon Alexa sau Google Assistant. Modul în care funcționează chatbot-urile inteligente este să *înțeleagă* ce dorește utilizatorul prin clasificarea textului din propoziția de intrare. Rezultatul acestei clasificări este așa-numitul **intent**, care determină ce ar trebui să facă chatbot-ul.

<img alt="Bot NER" src="../../../../../translated_images/ro/bot-ner.4b09235dbb0ad275.webp" width="50%"/>

> Imagine realizată de autor

Totuși, utilizatorul poate furniza anumite parametri ca parte a frazei. De exemplu, când cere informații despre vreme, poate specifica o locație sau o dată. Un bot ar trebui să fie capabil să înțeleagă aceste entități și să completeze sloturile de parametri corespunzător înainte de a efectua acțiunea. Exact aici intervine NER.

> ✅ Un alt exemplu ar fi [analiza articolelor științifice medicale](https://soshnikov.com/science/analyzing-medical-papers-with-azure-and-text-analytics-for-health/). Unul dintre principalele lucruri pe care trebuie să le căutăm sunt termenii medicali specifici, cum ar fi bolile și substanțele medicale. În timp ce un număr mic de boli poate fi extras probabil prin căutarea de subșiruri, entitățile mai complexe, cum ar fi compușii chimici și denumirile medicamentelor, necesită o abordare mai complexă.

## NER ca Clasificare de Token-uri

Modelele NER sunt, în esență, **modele de clasificare de token-uri**, deoarece pentru fiecare dintre token-urile de intrare trebuie să decidem dacă aparține unei entități sau nu, și dacă da - cărei clase de entitate.

Să luăm în considerare următorul titlu de articol:

**Regurgitarea valvei tricuspide** și **carbonatul de litiu** **toxicitate** la un nou-născut.

Entitățile aici sunt:

* Regurgitarea valvei tricuspide este o boală (`DIS`)
* Carbonatul de litiu este o substanță chimică (`CHEM`)
* Toxicitate este, de asemenea, o boală (`DIS`)

Observă că o entitate poate cuprinde mai multe token-uri. Și, ca în acest caz, trebuie să facem distincția între două entități consecutive. Astfel, este obișnuit să folosim două clase pentru fiecare entitate - una care specifică primul token al entității (adesea se folosește prefixul `B-`, pentru **b**eginning), și alta - continuarea unei entități (`I-`, pentru **i**nner token). De asemenea, folosim `O` ca o clasă pentru a reprezenta toate celelalte token-uri (**o**ther). O astfel de etichetare a token-urilor se numește [eticheta BIO](https://en.wikipedia.org/wiki/Inside%E2%80%93outside%E2%80%93beginning_(tagging)) (sau IOB). După etichetare, titlul nostru va arăta astfel:

Token | Etichetă
------|-----
Tricuspid | B-DIS
valve | I-DIS
regurgitation | I-DIS
and | O
lithium | B-CHEM
carbonate | I-CHEM
toxicity | B-DIS
in | O
a | O
newborn | O
infant | O
. | O

Deoarece trebuie să construim o corespondență unu-la-unu între token-uri și clase, putem antrena un model neuronal **many-to-many** din această imagine:

![Imagine care arată modele comune de rețele neuronale recurente.](../../../../../translated_images/ro/unreasonable-effectiveness-of-rnn.541ead816778f42d.webp)

> *Imagine din [acest articol de blog](http://karpathy.github.io/2015/05/21/rnn-effectiveness/) de [Andrej Karpathy](http://karpathy.github.io/). Modelele de clasificare de token-uri NER corespund arhitecturii de rețea din partea dreaptă a imaginii.*

## Antrenarea modelelor NER

Deoarece un model NER este, în esență, un model de clasificare de token-uri, putem folosi RNN-uri cu care suntem deja familiarizați pentru această sarcină. În acest caz, fiecare bloc al rețelei recurente va returna ID-ul token-ului. Următorul notebook exemplu arată cum să antrenezi un LSTM pentru clasificarea de token-uri.

## ✍️ Notebook-uri Exemplu: NER

Continuă învățarea în următorul notebook:

* [NER cu TensorFlow](NER-TF.ipynb)

## Concluzie

Un model NER este un **model de clasificare de token-uri**, ceea ce înseamnă că poate fi utilizat pentru a efectua clasificarea de token-uri. Aceasta este o sarcină foarte comună în NLP, ajutând la recunoașterea entităților specifice din text, inclusiv locuri, nume, date și altele.

## 🚀 Provocare

Completează tema legată mai jos pentru a antrena un model de recunoaștere a entităților denumite pentru termeni medicali, apoi încearcă-l pe un alt set de date.

## [Chestionar după lecție](https://ff-quizzes.netlify.app/en/ai/quiz/38)

## Recapitulare & Studiu Individual

Citește articolul [The Unreasonable Effectiveness of Recurrent Neural Networks](http://karpathy.github.io/2015/05/21/rnn-effectiveness/) și urmează secțiunea de lecturi suplimentare din acel articol pentru a-ți aprofunda cunoștințele.

## [Tema](lab/README.md)

În tema acestei lecții, va trebui să antrenezi un model de recunoaștere a entităților medicale. Poți începe cu antrenarea unui model LSTM, așa cum este descris în această lecție, și să continui cu utilizarea modelului transformer BERT. Citește [instrucțiunile](lab/README.md) pentru toate detaliile.

---

