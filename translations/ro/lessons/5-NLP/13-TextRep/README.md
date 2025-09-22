<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4522e22e150be0845e03aa41209a39d5",
  "translation_date": "2025-08-25T21:50:27+00:00",
  "source_file": "lessons/5-NLP/13-TextRep/README.md",
  "language_code": "ro"
}
-->
# Reprezentarea textului ca tensori

## [Chestionar înainte de curs](https://ff-quizzes.netlify.app/en/ai/quiz/25)

## Clasificarea textului

În prima parte a acestei secțiuni, ne vom concentra pe sarcina de **clasificare a textului**. Vom folosi setul de date [AG News](https://www.kaggle.com/amananandrai/ag-news-classification-dataset), care conține articole de știri precum următorul exemplu:

* Categorie: Știință/Tehnologie  
* Titlu: Compania Ky. câștigă un grant pentru a studia peptidele (AP)  
* Corp: AP - O companie fondată de un cercetător în chimie de la Universitatea din Louisville a câștigat un grant pentru a dezvolta...

Obiectivul nostru va fi să clasificăm articolul de știri într-una dintre categorii pe baza textului.

## Reprezentarea textului

Dacă dorim să rezolvăm sarcini de procesare a limbajului natural (NLP) cu rețele neuronale, avem nevoie de o metodă pentru a reprezenta textul ca tensori. Calculatoarele deja reprezintă caracterele textuale ca numere care corespund fonturilor de pe ecranul tău, folosind codificări precum ASCII sau UTF-8.

<img alt="Imagine care arată o diagramă ce mapează un caracter la o reprezentare ASCII și binară" src="images/ascii-character-map.png" width="50%"/>

> [Sursa imaginii](https://www.seobility.net/en/wiki/ASCII)

Ca oameni, înțelegem ce **reprezintă** fiecare literă și cum toate caracterele se unesc pentru a forma cuvintele unei propoziții. Totuși, calculatoarele, prin ele însele, nu au o astfel de înțelegere, iar rețeaua neuronală trebuie să învețe semnificația în timpul antrenării.

Prin urmare, putem folosi diferite abordări pentru a reprezenta textul:

* **Reprezentarea la nivel de caracter**, în care tratăm fiecare caracter ca un număr. Având *C* caractere diferite în corpusul nostru de text, cuvântul *Hello* ar fi reprezentat de un tensor de dimensiune 5x*C*. Fiecare literă ar corespunde unei coloane tensoriale în codificarea one-hot.  
* **Reprezentarea la nivel de cuvânt**, în care creăm un **vocabular** al tuturor cuvintelor din textul nostru și apoi reprezentăm cuvintele folosind codificarea one-hot. Această abordare este oarecum mai bună, deoarece fiecare literă, în sine, nu are prea multă semnificație, iar utilizând concepte semantice de nivel mai înalt - cuvintele - simplificăm sarcina pentru rețeaua neuronală. Totuși, având în vedere dimensiunea mare a dicționarului, trebuie să gestionăm tensori dispersați de dimensiuni mari.

Indiferent de reprezentare, mai întâi trebuie să convertim textul într-o secvență de **token-uri**, un token fiind fie un caracter, un cuvânt sau, uneori, chiar o parte a unui cuvânt. Apoi, convertim token-ul într-un număr, de obicei folosind un **vocabular**, iar acest număr poate fi introdus într-o rețea neuronală folosind codificarea one-hot.

## N-Grame

În limbajul natural, semnificația precisă a cuvintelor poate fi determinată doar în context. De exemplu, semnificațiile expresiilor *rețea neuronală* și *rețea de pescuit* sunt complet diferite. Una dintre modalitățile de a ține cont de acest lucru este să construim modelul nostru pe perechi de cuvinte, considerând perechile de cuvinte ca token-uri separate în vocabular. În acest fel, propoziția *Îmi place să merg la pescuit* va fi reprezentată de următoarea secvență de token-uri: *Îmi place*, *place să*, *să merg*, *merg la pescuit*. Problema cu această abordare este că dimensiunea dicționarului crește semnificativ, iar combinații precum *merg la pescuit* și *merg la cumpărături* sunt reprezentate de token-uri diferite, care nu împărtășesc nicio similaritate semantică, în ciuda aceluiași verb.

În unele cazuri, putem lua în considerare utilizarea tri-gramelor -- combinații de trei cuvinte -- de asemenea. Astfel, această abordare este adesea numită **n-grame**. De asemenea, are sens să folosim n-grame cu reprezentarea la nivel de caracter, caz în care n-gramele vor corespunde aproximativ diferitelor silabe.

## Bag-of-Words și TF/IDF

Când rezolvăm sarcini precum clasificarea textului, trebuie să putem reprezenta textul printr-un vector de dimensiune fixă, pe care îl vom folosi ca intrare pentru clasificatorul dens final. Una dintre cele mai simple metode de a face acest lucru este să combinăm toate reprezentările individuale ale cuvintelor, de exemplu, prin adunarea lor. Dacă adunăm codificările one-hot ale fiecărui cuvânt, vom obține un vector de frecvențe, care arată de câte ori apare fiecare cuvânt în text. O astfel de reprezentare a textului se numește **bag of words** (BoW).

<img src="images/bow.png" width="90%"/>

> Imagine realizată de autor

Un BoW reprezintă, în esență, ce cuvinte apar în text și în ce cantități, ceea ce poate fi într-adevăr un bun indicator al subiectului textului. De exemplu, un articol de știri despre politică este probabil să conțină cuvinte precum *președinte* și *țară*, în timp ce o publicație științifică ar avea termeni precum *colizor*, *descoperit*, etc. Astfel, frecvențele cuvintelor pot fi, în multe cazuri, un bun indicator al conținutului textului.

Problema cu BoW este că anumite cuvinte comune, precum *și*, *este*, etc., apar în majoritatea textelor și au frecvențe ridicate, mascând cuvintele care sunt cu adevărat importante. Putem reduce importanța acestor cuvinte luând în considerare frecvența cu care apar în întreaga colecție de documente. Aceasta este ideea principală din spatele abordării TF/IDF, care este acoperită în detaliu în caietele atașate acestei lecții.

Totuși, niciuna dintre aceste abordări nu poate lua în considerare pe deplin **semantica** textului. Avem nevoie de modele mai puternice de rețele neuronale pentru a face acest lucru, pe care le vom discuta mai târziu în această secțiune.

## ✍️ Exerciții: Reprezentarea textului

Continuă învățarea în următoarele caiete:

* [Reprezentarea textului cu PyTorch](../../../../../lessons/5-NLP/13-TextRep/TextRepresentationPyTorch.ipynb)  
* [Reprezentarea textului cu TensorFlow](../../../../../lessons/5-NLP/13-TextRep/TextRepresentationTF.ipynb)  

## Concluzie

Până acum, am studiat tehnici care pot adăuga greutate frecvenței diferitelor cuvinte. Totuși, acestea nu pot reprezenta semnificația sau ordinea. Așa cum a spus faimosul lingvist J. R. Firth în 1935, "Semnificația completă a unui cuvânt este întotdeauna contextuală, iar niciun studiu al semnificației în afara contextului nu poate fi luat în serios." Vom învăța mai târziu în curs cum să capturăm informații contextuale din text folosind modelarea limbajului.

## 🚀 Provocare

Încearcă alte exerciții folosind bag-of-words și diferite modele de date. Poți găsi inspirație în această [competiție pe Kaggle](https://www.kaggle.com/competitions/word2vec-nlp-tutorial/overview/part-1-for-beginners-bag-of-words).

## [Chestionar după curs](https://ff-quizzes.netlify.app/en/ai/quiz/26)

## Recapitulare și studiu individual

Exersează-ți abilitățile cu tehnicile de embedding și bag-of-words pe [Microsoft Learn](https://docs.microsoft.com/learn/modules/intro-natural-language-processing-pytorch/?WT.mc_id=academic-77998-cacaste).

## [Temă: Caiete](assignment.md)

**Declinare de responsabilitate**:  
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). Deși ne străduim să asigurăm acuratețea, vă rugăm să fiți conștienți că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa natală ar trebui considerat sursa autoritară. Pentru informații critice, se recomandă traducerea profesională realizată de un specialist uman. Nu ne asumăm responsabilitatea pentru eventualele neînțelegeri sau interpretări greșite care pot apărea din utilizarea acestei traduceri.