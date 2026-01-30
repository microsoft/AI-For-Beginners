# Inteligență Artificială Etică și Responsabilă

Ai aproape terminat acest curs și sper că până acum ai înțeles clar că inteligența artificială (IA) se bazează pe o serie de metode matematice formale care ne permit să găsim relații în date și să antrenăm modele pentru a replica anumite aspecte ale comportamentului uman. În acest moment al istoriei, considerăm IA ca fiind un instrument foarte puternic pentru a extrage tipare din date și pentru a aplica aceste tipare în rezolvarea unor probleme noi.

## [Chestionar înainte de curs](https://white-water-09ec41f0f.azurestaticapps.net/quiz/5/)

Totuși, în science fiction vedem adesea povești în care IA reprezintă un pericol pentru omenire. De obicei, aceste povești se concentrează pe un fel de rebeliune a IA, când aceasta decide să se confrunte cu ființele umane. Acest lucru implică faptul că IA are un fel de emoție sau poate lua decizii neprevăzute de dezvoltatorii săi.

Tipul de IA despre care am învățat în acest curs nu este altceva decât aritmetică pe matrice mari. Este un instrument foarte puternic care ne ajută să ne rezolvăm problemele și, ca orice alt instrument puternic, poate fi folosit atât în scopuri bune, cât și rele. Important este că poate fi *folosit greșit*.

## Principiile unei IA Responsabile

Pentru a evita utilizarea greșită, accidentală sau intenționată, a IA, Microsoft enunță importantele [Principii ale unei IA Responsabile](https://www.microsoft.com/ai/responsible-ai?WT.mc_id=academic-77998-cacaste). Următoarele concepte stau la baza acestor principii:

* **Echitate** este legată de problema importantă a *prejudecăților modelului*, care pot fi cauzate de utilizarea unor date părtinitoare pentru antrenare. De exemplu, când încercăm să prezicem probabilitatea ca o persoană să obțină un loc de muncă ca dezvoltator software, modelul este probabil să acorde o preferință mai mare bărbaților - doar pentru că setul de date de antrenare a fost probabil părtinitor către un public masculin. Trebuie să echilibrăm cu atenție datele de antrenare și să investigăm modelul pentru a evita prejudecățile și să ne asigurăm că modelul ia în considerare caracteristici mai relevante.
* **Fiabilitate și Siguranță**. Prin natura lor, modelele IA pot face greșeli. O rețea neuronală returnează probabilități, iar noi trebuie să ținem cont de acest lucru atunci când luăm decizii. Fiecare model are o anumită precizie și un anumit recall, iar noi trebuie să înțelegem acest lucru pentru a preveni daunele pe care le pot provoca sfaturile greșite.
* **Confidențialitate și Securitate** au implicații specifice pentru IA. De exemplu, atunci când folosim anumite date pentru a antrena un model, aceste date devin cumva "integrate" în model. Pe de o parte, acest lucru crește securitatea și confidențialitatea, pe de altă parte - trebuie să ne amintim ce date au fost utilizate pentru antrenarea modelului.
* **Incluziune** înseamnă că nu construim IA pentru a înlocui oamenii, ci mai degrabă pentru a-i sprijini și pentru a face munca noastră mai creativă. Este, de asemenea, legată de echitate, deoarece atunci când lucrăm cu comunități subreprezentate, majoritatea seturilor de date pe care le colectăm sunt probabil părtinitoare, iar noi trebuie să ne asigurăm că aceste comunități sunt incluse și tratate corect de IA.
* **Transparență**. Aceasta include asigurarea faptului că suntem întotdeauna clari cu privire la utilizarea IA. De asemenea, acolo unde este posibil, dorim să folosim sisteme IA care sunt *interpretabile*.
* **Responsabilitate**. Când modelele IA iau anumite decizii, nu este întotdeauna clar cine este responsabil pentru acele decizii. Trebuie să ne asigurăm că înțelegem unde se află responsabilitatea pentru deciziile IA. În majoritatea cazurilor, ne-am dori să includem ființe umane în procesul de luare a deciziilor importante, astfel încât oamenii să fie cei care își asumă responsabilitatea.

## Instrumente pentru o IA Responsabilă

Microsoft a dezvoltat [Responsible AI Toolbox](https://github.com/microsoft/responsible-ai-toolbox), care conține un set de instrumente:

* Interpretability Dashboard (InterpretML)
* Fairness Dashboard (FairLearn)
* Error Analysis Dashboard
* Responsible AI Dashboard care include:

   - EconML - un instrument pentru Analiza Cauzală, care se concentrează pe întrebări de tip "ce-ar fi dacă"
   - DiCE - un instrument pentru Analiza Contrafactuală care îți permite să vezi ce caracteristici trebuie schimbate pentru a influența decizia modelului

Pentru mai multe informații despre Etica în IA, te rugăm să vizitezi [această lecție](https://github.com/microsoft/ML-For-Beginners/tree/main/1-Introduction/3-fairness?WT.mc_id=academic-77998-cacaste) din Curriculum-ul de Învățare Automată, care include teme.

## Recapitulare și Studiu Individual

Parcurge acest [Learn Path](https://docs.microsoft.com/learn/modules/responsible-ai-principles/?WT.mc_id=academic-77998-cacaste) pentru a afla mai multe despre IA responsabilă.

## [Chestionar după curs](https://white-water-09ec41f0f.azurestaticapps.net/quiz/6/)

**Declinare de responsabilitate**:  
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). Deși ne străduim să asigurăm acuratețea, vă rugăm să fiți conștienți că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa natală ar trebui considerat sursa autoritară. Pentru informații critice, se recomandă traducerea profesională realizată de un specialist uman. Nu ne asumăm responsabilitatea pentru eventualele neînțelegeri sau interpretări greșite care pot apărea din utilizarea acestei traduceri.