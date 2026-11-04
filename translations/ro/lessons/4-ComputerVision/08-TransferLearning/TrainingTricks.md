# Trucuri pentru Antrenamentul în Învățarea Profundă

Pe măsură ce rețelele neuronale devin mai adânci, procesul de antrenament devine din ce în ce mai dificil. O problemă majoră este așa-numitul [dispariția gradientului](https://en.wikipedia.org/wiki/Vanishing_gradient_problem) sau [explozia gradientului](https://deepai.org/machine-learning-glossary-and-terms/exploding-gradient-problem#:~:text=Exploding%20gradients%20are%20a%20problem,updates%20are%20small%20and%20controlled.). [Această postare](https://towardsdatascience.com/the-vanishing-exploding-gradient-problem-in-deep-neural-networks-191358470c11) oferă o bună introducere în aceste probleme.

Pentru a face antrenamentul rețelelor profunde mai eficient, există câteva tehnici care pot fi folosite.

## Menținerea valorilor în interval rezonabil

Pentru a face calculele numerice mai stabile, vrem să ne asigurăm că toate valorile din rețeaua noastră neuronală sunt în cadrul unei scale rezonabile, de obicei [-1..1] sau [0..1]. Nu este o cerință foarte strictă, dar natura calculelor în virgulă mobilă este astfel încât valorile de magnitudini diferite nu pot fi manipulate corect împreună. De exemplu, dacă adunăm 10<sup>-10</sup> și 10<sup>10</sup>, este probabil să obținem 10<sup>10</sup>, deoarece valoarea mai mică ar fi „convertită” la aceeași ordine ca cea mai mare, iar mantisa s-ar pierde.

Majoritatea funcțiilor de activare au neliniaritati în jurul intervalului [-1..1], așadar are sens să scalăm toate datele de intrare în intervalul [-1..1] sau [0..1].

## Inițializarea Greutăților

Ideal, vrem ca valorile să rămână în aceeași gamă după ce trec prin straturile rețelei. De aceea este important să inițializăm greutățile astfel încât să se păstreze distribuția valorilor.

Distribuția normală **N(0,1)** nu este o idee bună, pentru că dacă avem *n* intrări, deviația standard a ieșirii va fi *&radic;n*, iar valorile vor sări probabil din afara intervalului [0..1].

Următoarele inițializări sunt des folosite:

 * Distribuție uniformă -- `uniform`
 * **N(0,1/n)** -- `gaussian`
 * **N(0,1/&radic;n_in)** garantează că pentru intrări cu medie zero și deviație standard 1 va rămâne aceeași medie/deviație standard
 * **N(0,&radic;2/(n_in+n_out))** -- așa-numita **inițializare Xavier** (`glorot`), ajută să menținem semnalele în interval în timpul propagării înainte și înapoi

## Normalizarea Batch

Chiar și cu o inițializare corectă a greutăților, acestea pot deveni arbitrar mari sau mici în timpul antrenamentului, ducând semnalele în afara intervalului potrivit. Putem readuce semnalele în interval utilizând una dintre tehnicile de **normalizare**. Deși există mai multe dintre ele (Normalizarea greutăților, Normalizarea stratului), cea mai des folosită este Normalizarea Batch.

Ideea **normalizării batch** este să ținem cont de toate valorile din minibatch și să efectuăm normalizarea (adică scădem media și împărțim la deviația standard) pe baza acestor valori. Este implementată ca un strat în rețea care face această normalizare după aplicarea greutăților, dar înainte de funcția de activare. Ca rezultat, este probabil să obținem o acuratețe finală mai mare și un antrenament mai rapid.

Iată [lucrarea originală](https://arxiv.org/pdf/1502.03167.pdf) despre normalizarea batch, [explicația de pe Wikipedia](https://en.wikipedia.org/wiki/Batch_normalization), și [o bună postare introductivă pe blog](https://towardsdatascience.com/batch-normalization-in-3-levels-of-understanding-14c2da90a338) (și una [în limba rusă](https://habrahabr.ru/post/309302/)).

## Dropout

**Dropout** este o tehnică interesantă care elimină un procentaj aleator de neuroni în timpul antrenamentului. Este, de asemenea, implementată ca un strat cu un parametru (procentul de neuroni de eliminat, în mod tipic 10%-50%), și în timpul antrenamentului setă random elementele vectorului de intrare la zero, înainte de a le trece la stratul următor.

Deși poate părea o idee ciudată, poți vedea efectul dropout asupra antrenamentului unui clasificator de cifre MNIST în notebook-ul [`Dropout.ipynb`](Dropout.ipynb). Reduce timpul de antrenament și permite obținerea unei acurateți mai mari cu mai puține epoci de antrenament.

Acest efect poate fi explicat în mai multe moduri:

 * Poate fi considerat un factor aleatoriu de șoc pentru model, care scoate optimizarea dintr-un minim local
 * Poate fi considerat *media implicită a modelelor*, pentru că putem spune că în timpul dropout antrenăm modele ușor diferite

> *Unii spun că atunci când o persoană beată încearcă să învețe ceva, va reține mai bine dimineața următoare decât o persoană trează, pentru că creierul cu câțiva neuroni disfuncționali încearcă să se adapteze mai bine pentru a înțelege sensul. Nu am testat niciodată dacă acest lucru este adevărat sau nu*

## Prevenirea supraspecializării

Unul dintre aspectele foarte importante în învățarea profundă este să putem preveni [supraspecializarea](../../3-NeuralNetworks/05-Frameworks/Overfitting.md). Deși poate fi tentant să folosim un model de rețea neuronală foarte puternic, trebuie să echilibrăm întotdeauna numărul de parametri ai modelului cu numărul de eșantioane de antrenament.

> Asigură-te că înțelegi conceptul de [supraspecializare](../../3-NeuralNetworks/05-Frameworks/Overfitting.md) pe care l-am introdus anterior!

Există mai multe moduri de a preveni supraspecializarea:

 * Oprire timpurie -- monitorizează continuu eroarea pe setul de validare și oprește antrenamentul când eroarea pe validare începe să crească.
 * Decădere explicită a greutăților / Regularizare -- adăugarea unei penalități suplimentare funcției de pierdere pentru valorile absolute mari ale greutăților, ceea ce previne ca modelul să dea rezultate foarte instabile
 * Medierea modelului -- antrenarea mai multor modele și apoi media rezultatelor. Aceasta ajută la minimizarea variației.
 * Dropout (media implicită a modelelor)

## Optimizatori / Algoritmi de Antrenament

Un alt aspect important al antrenamentului este să alegem un algoritm de antrenament bun. Deși **gradientul descendent** clasic este o alegere rezonabilă, uneori poate fi prea lent sau poate duce la alte probleme.

În învățarea profundă, folosim **Gradientul Descendent Stocastic** (SGD), care este gradient descendent aplicat pe minibatch-uri, alese aleatoriu din setul de antrenament. Greutățile sunt ajustate folosind această formulă:

w<sup>t+1</sup> = w<sup>t</sup> - &eta;&nabla;&lagran;

### Momentum

În **momentum SGD**, păstrăm o parte din gradientul pașilor anteriori. Este similar cu situația când ne mișcăm undeva cu inerție și primim o lovitură în direcție diferită; traiectoria noastră nu se schimbă imediat, ci păstrează o parte din mișcarea inițială. Aici introducem un alt vector v pentru a reprezenta *viteza*:

* v<sup>t+1</sup> = &gamma; v<sup>t</sup> - &eta;&nabla;&lagran;
* w<sup>t+1</sup> = w<sup>t</sup>+v<sup>t+1</sup>

Parametrul &gamma; indică măsura în care ținem cont de inerție: &gamma;=0 corespunde SGD clasic; &gamma;=1 este o ecuație pură a mișcării.

### Adam, Adagrad, etc.

Deoarece în fiecare strat multiplicăm semnalele cu o matrice W<sub>i</sub>, în funcție de ||W<sub>i</sub>||, gradientul poate fie să scadă și să se apropie de 0, fie să crească la infinit. Aceasta este esența problemei Exploding/Vanishing Gradients.

Una dintre soluțiile acestei probleme este să folosim doar direcția gradientului în ecuație și să ignorăm valoarea absolută, adică

w<sup>t+1</sup> = w<sup>t</sup> - &eta;(&nabla;&lagran;/||&nabla;&lagran;||), unde ||&nabla;&lagran;|| = &radic;&sum;(&nabla;&lagran;)<sup>2</sup>

Acest algoritm se numește **Adagrad**. Alte algoritme care folosesc aceeași idee: **RMSProp**, **Adam**

> **Adam** este considerat a fi un algoritm foarte eficient pentru multe aplicații, deci dacă nu știi care să folosești - folosește Adam.

### Limitarea gradientului (Gradient clipping)

Limitarea gradientului este o extensie a ideii de mai sus. Când ||&nabla;&lagran;|| &le; &theta;, considerăm gradientul original în optimizarea greutăților, iar când ||&nabla;&lagran;|| > &theta; - împărțim gradientul la norma sa. Aici &theta; este un parametru, în cele mai multe cazuri putem lua &theta;=1 sau &theta;=10.

### Decăderea ratei de învățare

Succesul antrenamentului depinde adesea de parametrul ratei de învățare &eta;. Este logic să presupunem că valori mai mari ale lui &eta; duc la un antrenament mai rapid, ceea ce de obicei vrem la începutul antrenamentului, iar valorile mai mici ale &eta; ne permit să reglăm fin rețeaua. Astfel, în majoritatea cazurilor vrem să scădem &eta; pe parcursul antrenamentului.

Acest lucru se poate face prin înmulțirea lui &eta; cu un număr (de ex. 0.98) după fiecare epocă de antrenament, sau prin utilizarea unui **program mai complicat al ratei de învățare**.

## Diferite Arhitecturi de Rețele

Alegerea arhitecturii corecte a rețelei pentru problema ta poate fi dificilă. Normal, am alege o arhitectură care a demonstrat că funcționează pentru sarcina noastră specifică (sau una similară). Iată o [bună prezentare generală](https://www.topbots.com/a-brief-history-of-neural-network-architectures/) a arhitecturilor de rețele neuronale pentru viziune computerizată.

> Este important să alegi o arhitectură care va fi suficient de puternică pentru numărul de eșantioane de antrenament pe care le ai. Alegerea unui model prea puternic poate rezulta în [supraspecializare](../../3-NeuralNetworks/05-Frameworks/Overfitting.md)

Un alt mod bun ar fi să folosim o arhitectură care se ajustează automat la complexitatea necesară. În oarecare măsură, arhitectura **ResNet** și **Inception** sunt autoajustabile. [Mai multe despre arhitecturile pentru viziunea computerizată](../07-ConvNets/CNN_Architectures.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Declinare a responsabilității**:
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). În timp ce ne străduim pentru acuratețe, vă rugăm să rețineți că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa nativă trebuie considerat sursa autorizată. Pentru informații critice, se recomandă traducerea profesională realizată de un om. Nu ne asumăm responsabilitatea pentru eventualele neînțelegeri sau interpretări greșite care decurg din utilizarea acestei traduceri.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->