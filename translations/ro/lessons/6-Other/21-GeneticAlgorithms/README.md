# Algoritmi Genetici

## [Chestionar înainte de curs](https://ff-quizzes.netlify.app/en/ai/quiz/41)

**Algoritmii Genetici** (GA) se bazează pe o **abordare evolutivă** a inteligenței artificiale, în care metodele de evoluție ale unei populații sunt utilizate pentru a obține o soluție optimă pentru o problemă dată. Aceștia au fost propuși în 1975 de [John Henry Holland](https://wikipedia.org/wiki/John_Henry_Holland).

Algoritmii Genetici se bazează pe următoarele idei:

* Soluțiile valide ale problemei pot fi reprezentate ca **gene**
* **Recombinarea** permite combinarea a două soluții pentru a obține o nouă soluție validă
* **Selecția** este utilizată pentru a alege soluții mai optime folosind o **funcție de fitness**
* **Mutările** sunt introduse pentru a destabiliza optimizarea și a ieși din minimul local

Dacă dorești să implementezi un Algoritm Genetic, ai nevoie de următoarele:

 * Să găsești o metodă de codificare a soluțiilor problemei folosind **gene** g&in;&Gamma;
 * Pe setul de gene &Gamma; trebuie să definești o **funcție de fitness** fit: &Gamma;&rightarrow;**R**. Valorile mai mici ale funcției corespund soluțiilor mai bune.
 * Să definești un mecanism de **recombinare** pentru a combina două gene și a obține o nouă soluție validă crossover: &Gamma;<sup>2</sub>&rightarrow;&Gamma;.
 * Să definești un mecanism de **mutare** mutate: &Gamma;&rightarrow;&Gamma;.

În multe cazuri, recombinarea și mutarea sunt algoritmi destul de simpli pentru manipularea genelor ca secvențe numerice sau vectori de biți.

Implementarea specifică a unui algoritm genetic poate varia de la caz la caz, dar structura generală este următoarea:

1. Selectează o populație inițială G&subset;&Gamma;
2. Selectează aleatoriu una dintre operațiile care vor fi efectuate în acest pas: recombinare sau mutare
3. **Recombinare**:
  * Selectează aleatoriu două gene g<sub>1</sub>, g<sub>2</sub> &in; G
  * Calculează recombinarea g=crossover(g<sub>1</sub>,g<sub>2</sub>)
  * Dacă fit(g)<fit(g<sub>1</sub>) sau fit(g)<fit(g<sub>2</sub>) - înlocuiește gena corespunzătoare din populație cu g.
4. **Mutare** - selectează o genă aleatorie g&in;G și înlocuiește-o cu mutate(g)
5. Repetă de la pasul 2, până obții o valoare suficient de mică a funcției fit sau până se atinge limita numărului de pași.

## Sarcini Tipice

Sarcinile rezolvate de obicei prin Algoritmi Genetici includ:

1. Optimizarea programării
1. Împachetarea optimă
1. Tăierea optimă
1. Accelerarea căutării exhaustive

## ✍️ Exerciții: Algoritmi Genetici

Continuă învățarea în următoarele notebook-uri:

Accesează [acest notebook](Genetic.ipynb) pentru a vedea două exemple de utilizare a Algoritmilor Genetici:

1. Împărțirea echitabilă a comorii
1. Problema celor 8 regine

## Concluzie

Algoritmii Genetici sunt utilizați pentru a rezolva multe probleme, inclusiv probleme de logistică și căutare. Domeniul este inspirat de cercetări care au îmbinat subiecte din Psihologie și Informatică.

## 🚀 Provocare

"Algoritmii genetici sunt ușor de implementat, dar comportamentul lor este dificil de înțeles." [sursa](https://wikipedia.org/wiki/Genetic_algorithm) Fă cercetări pentru a găsi o implementare a unui algoritm genetic, cum ar fi rezolvarea unui puzzle Sudoku, și explică cum funcționează sub formă de schiță sau diagramă de flux.

## [Chestionar după curs](https://ff-quizzes.netlify.app/en/ai/quiz/42)

## Recapitulare & Studiu Individual

Urmărește [acest video excelent](https://www.youtube.com/watch?v=qv6UVOQ0F44) despre cum un computer poate învăța să joace Super Mario folosind rețele neuronale antrenate prin algoritmi genetici. Vom învăța mai multe despre cum computerele învață să joace astfel de jocuri [în secțiunea următoare](../22-DeepRL/README.md).

## [Temă: Ecuația Diofantină](Diophantine.ipynb)

Scopul tău este să rezolvi așa-numita **ecuație Diofantină** - o ecuație cu rădăcini întregi. De exemplu, consideră ecuația a+2b+3c+4d=30. Trebuie să găsești rădăcinile întregi care satisfac această ecuație.

*Această temă este inspirată de [acest articol](https://habr.com/post/128704/).*

Sugestii:

1. Poți considera rădăcinile în intervalul [0;30]
1. Ca genă, ia în considerare utilizarea listei de valori ale rădăcinilor

Folosește [Diophantine.ipynb](Diophantine.ipynb) ca punct de plecare.

---

