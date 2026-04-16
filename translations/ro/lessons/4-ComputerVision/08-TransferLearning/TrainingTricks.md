# Trucuri pentru antrenarea rețelelor neuronale profunde

Pe măsură ce rețelele neuronale devin mai adânci, procesul de antrenare devine din ce în ce mai dificil. Una dintre principalele probleme este așa-numita [problemă a gradientului care dispare](https://en.wikipedia.org/wiki/Vanishing_gradient_problem) sau [gradientul exploziv](https://deepai.org/machine-learning-glossary-and-terms/exploding-gradient-problem#:~:text=Exploding%20gradients%20are%20a%20problem,updates%20are%20small%20and%20controlled.). [Acest articol](https://towardsdatascience.com/the-vanishing-exploding-gradient-problem-in-deep-neural-networks-191358470c11) oferă o introducere bună în aceste probleme.

Pentru a face antrenarea rețelelor profunde mai eficientă, există câteva tehnici care pot fi utilizate.

## Menținerea valorilor într-un interval rezonabil

Pentru a face calculele numerice mai stabile, dorim să ne asigurăm că toate valorile din rețeaua noastră neuronală sunt într-o scară rezonabilă, de obicei [-1..1] sau [0..1]. Nu este o cerință foarte strictă, dar natura calculelor cu punct flotant este astfel încât valorile de magnitudini diferite nu pot fi manipulate cu precizie împreună. De exemplu, dacă adunăm 10<sup>-10</sup> și 10<sup>10</sup>, este probabil să obținem 10<sup>10</sup>, deoarece valoarea mai mică ar fi „convertită” la același ordin ca cea mai mare, iar mantisa ar fi pierdută.

Majoritatea funcțiilor de activare au neliniarități în jurul intervalului [-1..1], așa că are sens să scalăm toate datele de intrare în intervalul [-1..1] sau [0..1].

## Inițializarea greutăților

Ideal, dorim ca valorile să fie în același interval după trecerea prin straturile rețelei. Prin urmare, este important să inițializăm greutățile astfel încât să păstrăm distribuția valorilor.

Distribuția normală **N(0,1)** nu este o idee bună, deoarece dacă avem *n* intrări, deviația standard a ieșirii ar fi *n*, iar valorile ar putea să iasă din intervalul [0..1].

Următoarele metode de inițializare sunt adesea utilizate:

 * Distribuție uniformă -- `uniform`
 * **N(0,1/n)** -- `gaussian`
 * **N(0,1/√n_in)** garantează că pentru intrări cu medie zero și deviație standard de 1, aceeași medie/deviație standard va rămâne
 * **N(0,√2/(n_in+n_out))** -- așa-numita **inițializare Xavier** (`glorot`), care ajută la menținerea semnalelor în interval în timpul propagării înainte și înapoi

## Normalizarea pe loturi (Batch Normalization)

Chiar și cu o inițializare corectă a greutăților, acestea pot deveni arbitrar de mari sau mici în timpul antrenării, ceea ce va scoate semnalele din intervalul potrivit. Putem readuce semnalele în interval folosind una dintre tehnicile de **normalizare**. Deși există mai multe (Normalizarea greutăților, Normalizarea pe strat), cea mai utilizată este Normalizarea pe loturi.

Ideea **normalizării pe loturi** este de a lua în considerare toate valorile din lotul de date și de a efectua normalizarea (adică scăderea mediei și împărțirea la deviația standard) pe baza acestor valori. Este implementată ca un strat al rețelei care face această normalizare după aplicarea greutăților, dar înainte de funcția de activare. Ca rezultat, este probabil să obținem o acuratețe finală mai mare și o antrenare mai rapidă.

Iată [lucrarea originală](https://arxiv.org/pdf/1502.03167.pdf) despre normalizarea pe loturi, [explicația de pe Wikipedia](https://en.wikipedia.org/wiki/Batch_normalization) și [un articol introductiv bun](https://towardsdatascience.com/batch-normalization-in-3-levels-of-understanding-14c2da90a338) (și unul [în rusă](https://habrahabr.ru/post/309302/)).

## Dropout

**Dropout** este o tehnică interesantă care elimină un anumit procent de neuroni aleatori în timpul antrenării. Este implementată ca un strat cu un parametru (procentul de neuroni de eliminat, de obicei 10%-50%), iar în timpul antrenării, elimină aleatoriu elemente din vectorul de intrare, înainte de a-l transmite stratului următor.

Deși poate suna ca o idee ciudată, puteți vedea efectul dropout-ului asupra antrenării unui clasificator de cifre MNIST în notebook-ul [`Dropout.ipynb`](../../../../../lessons/4-ComputerVision/08-TransferLearning/Dropout.ipynb). Aceasta accelerează antrenarea și ne permite să obținem o acuratețe mai mare în mai puține epoci de antrenare.

Acest efect poate fi explicat în mai multe moduri:

 * Poate fi considerat un factor de șoc aleatoriu pentru model, care scoate optimizarea dintr-un minim local
 * Poate fi considerat ca o *mediere implicită a modelului*, deoarece putem spune că în timpul dropout-ului antrenăm un model ușor diferit

> *Unii oameni spun că atunci când o persoană beată încearcă să învețe ceva, își va aminti mai bine a doua zi dimineață, comparativ cu o persoană trează, deoarece un creier cu câțiva neuroni disfuncționali încearcă să se adapteze mai bine pentru a înțelege sensul. Nu am testat noi înșine dacă acest lucru este adevărat sau nu.*

## Prevenirea supraînvățării (overfitting)

Unul dintre aspectele foarte importante ale învățării profunde este să putem preveni [supraînvățarea](../../3-NeuralNetworks/05-Frameworks/Overfitting.md). Deși poate fi tentant să folosim un model de rețea neuronală foarte puternic, ar trebui să echilibrăm întotdeauna numărul de parametri ai modelului cu numărul de mostre de antrenare.

> Asigurați-vă că înțelegeți conceptul de [supraînvățare](../../3-NeuralNetworks/05-Frameworks/Overfitting.md) pe care l-am introdus anterior!

Există mai multe modalități de a preveni supraînvățarea:

 * Oprirea timpurie -- monitorizarea continuă a erorii pe setul de validare și oprirea antrenării atunci când eroarea de validare începe să crească.
 * Penalizare explicită a greutăților / Regularizare -- adăugarea unei penalizări suplimentare la funcția de pierdere pentru valorile absolute mari ale greutăților, ceea ce previne obținerea unor rezultate foarte instabile
 * Medierea modelului -- antrenarea mai multor modele și apoi medierea rezultatului. Acest lucru ajută la minimizarea variației.
 * Dropout (Mediere implicită a modelului)

## Optimizatori / Algoritmi de antrenare

Un alt aspect important al antrenării este alegerea unui algoritm de antrenare bun. Deși **descendentul gradientului** clasic este o alegere rezonabilă, poate fi uneori prea lent sau poate duce la alte probleme.

În învățarea profundă, folosim **Descendentul Gradientului Stocastic** (SGD), care este un descendent al gradientului aplicat pe loturi mici, selectate aleatoriu din setul de antrenare. Greutățile sunt ajustate folosind această formulă:

w<sup>t+1</sup> = w<sup>t</sup> - η∇ℒ

### Momentum

În **SGD cu momentum**, păstrăm o parte din gradientul pașilor anteriori. Este similar cu situația în care ne deplasăm undeva cu inerție, iar dacă primim un impuls într-o direcție diferită, traiectoria noastră nu se schimbă imediat, ci păstrează o parte din mișcarea inițială. Aici introducem un alt vector v pentru a reprezenta *viteza*:

* v<sup>t+1</sup> = γ v<sup>t</sup> - η∇ℒ
* w<sup>t+1</sup> = w<sup>t</sup>+v<sup>t+1</sup>

Aici, parametrul γ indică măsura în care luăm în considerare inerția: γ=0 corespunde cu SGD clasic; γ=1 este o ecuație pură a mișcării.

### Adam, Adagrad, etc.

Deoarece în fiecare strat înmulțim semnalele cu o matrice W<sub>i</sub>, în funcție de ||W<sub>i</sub>||, gradientul poate fie să dispară și să fie aproape de 0, fie să crească la infinit. Aceasta este esența problemei Gradientelor Explozive/Disparente.

Una dintre soluțiile acestei probleme este să folosim doar direcția gradientului în ecuație și să ignorăm valoarea absolută, adică:

w<sup>t+1</sup> = w<sup>t</sup> - η(∇ℒ/||∇ℒ||), unde ||∇ℒ|| = √∑(∇ℒ)<sup>2</sup>

Acest algoritm se numește **Adagrad**. Alte algoritme care folosesc aceeași idee: **RMSProp**, **Adam**

> **Adam** este considerat a fi un algoritm foarte eficient pentru multe aplicații, așa că dacă nu sunteți sigur ce să folosiți - folosiți Adam.

### Gradient clipping

Gradient clipping este o extensie a ideii de mai sus. Când ||∇ℒ|| ≤ θ, considerăm gradientul original în optimizarea greutății, iar când ||∇ℒ|| > θ - împărțim gradientul la norma sa. Aici θ este un parametru, în majoritatea cazurilor putem lua θ=1 sau θ=10.

### Reducerea ratei de învățare

Succesul antrenării depinde adesea de parametrul ratei de învățare η. Este logic să presupunem că valorile mai mari ale lui η duc la o antrenare mai rapidă, ceea ce este ceva ce ne dorim de obicei la începutul antrenării, iar apoi valorile mai mici ale lui η ne permit să ajustăm fin rețeaua. Astfel, în majoritatea cazurilor dorim să reducem η pe parcursul antrenării.

Acest lucru poate fi realizat prin înmulțirea lui η cu un număr (de exemplu, 0.98) după fiecare epocă de antrenare sau prin utilizarea unui **program de reducere a ratei de învățare** mai complicat.

## Diferite arhitecturi de rețele

Selectarea arhitecturii potrivite pentru problema dvs. poate fi dificilă. De obicei, alegem o arhitectură care s-a dovedit a funcționa pentru sarcina noastră specifică (sau una similară). Iată o [prezentare generală bună](https://www.topbots.com/a-brief-history-of-neural-network-architectures/) a arhitecturilor de rețele neuronale pentru viziunea computerizată.

> Este important să selectați o arhitectură care să fie suficient de puternică pentru numărul de mostre de antrenare pe care le avem. Alegerea unui model prea puternic poate duce la [supraînvățare](../../3-NeuralNetworks/05-Frameworks/Overfitting.md).

O altă metodă bună ar fi utilizarea unei arhitecturi care se ajustează automat la complexitatea necesară. Într-o anumită măsură, arhitecturile **ResNet** și **Inception** sunt auto-ajustabile. [Mai multe despre arhitecturile pentru viziunea computerizată](../07-ConvNets/CNN_Architectures.md).

**Declinare de responsabilitate**:  
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). Deși ne străduim să asigurăm acuratețea, vă rugăm să fiți conștienți că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa natală ar trebui considerat sursa autoritară. Pentru informații critice, se recomandă traducerea profesională realizată de un specialist uman. Nu ne asumăm responsabilitatea pentru eventualele neînțelegeri sau interpretări greșite care pot apărea din utilizarea acestei traduceri.