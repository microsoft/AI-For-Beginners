<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "893aa368cb485da704b466a0f3775587",
  "translation_date": "2025-08-25T23:18:35+00:00",
  "source_file": "lessons/6-Other/21-GeneticAlgorithms/README.md",
  "language_code": "ro"
}
-->
# Algoritmi Genetici

## [Chestionar înainte de curs](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/121)

**Algoritmii Genetici** (AG) se bazează pe o **abordare evolutivă** a inteligenței artificiale, în care metodele de evoluție a unei populații sunt utilizate pentru a obține o soluție optimă pentru o problemă dată. Aceștia au fost propuși în 1975 de [John Henry Holland](https://wikipedia.org/wiki/John_Henry_Holland).

Algoritmii Genetici se bazează pe următoarele idei:

* Soluțiile valide ale problemei pot fi reprezentate ca **gene**
* **Încrucișarea** ne permite să combinăm două soluții pentru a obține o nouă soluție validă
* **Selecția** este utilizată pentru a alege soluții mai optime folosind o **funcție de fitness**
* **Mutațiile** sunt introduse pentru a destabiliza optimizarea și a ne scoate dintr-un minim local

Dacă dorești să implementezi un Algoritm Genetic, ai nevoie de următoarele:

* Să găsești o metodă de codificare a soluțiilor problemei folosind **gene** g∈Γ
* Pe setul de gene Γ trebuie să definești o **funcție de fitness** fit: Γ→**R**. Valorile mai mici ale funcției corespund soluțiilor mai bune.
* Să definești un mecanism de **încrucișare** pentru a combina două gene și a obține o nouă soluție validă crossover: Γ<sup>2</sup>→Γ.
* Să definești un mecanism de **mutație** mutate: Γ→Γ.

În multe cazuri, încrucișarea și mutația sunt algoritmi destul de simpli pentru a manipula genele ca secvențe numerice sau vectori de biți.

Implementarea specifică a unui algoritm genetic poate varia de la caz la caz, dar structura generală este următoarea:

1. Selectează o populație inițială G⊂Γ
2. Selectează aleatoriu una dintre operațiile care vor fi efectuate în acest pas: încrucișare sau mutație
3. **Încrucișare**:
   * Selectează aleatoriu două gene g<sub>1</sub>, g<sub>2</sub> ∈ G
   * Calculează încrucișarea g=crossover(g<sub>1</sub>,g<sub>2</sub>)
   * Dacă fit(g)<fit(g<sub>1</sub>) sau fit(g)<fit(g<sub>2</sub>) - înlocuiește gena corespunzătoare din populație cu g.
4. **Mutație** - selectează o genă aleatorie g∈G și înlocuiește-o cu mutate(g)
5. Repetă de la pasul 2, până când obții o valoare suficient de mică a funcției fit sau până când se atinge limita numărului de pași.

## Sarcini Tipice

Sarcinile rezolvate în mod obișnuit de Algoritmii Genetici includ:

1. Optimizarea programărilor
1. Împachetarea optimă
1. Tăierea optimă
1. Accelerarea căutării exhaustive

## ✍️ Exerciții: Algoritmi Genetici

Continuă învățarea în următoarele notebook-uri:

Accesează [acest notebook](../../../../../lessons/6-Other/21-GeneticAlgorithms/Genetic.ipynb) pentru a vedea două exemple de utilizare a Algoritmilor Genetici:

1. Împărțirea echitabilă a unei comori
1. Problema celor 8 regine

## Concluzie

Algoritmii Genetici sunt utilizați pentru a rezolva multe probleme, inclusiv probleme de logistică și căutare. Domeniul este inspirat de cercetări care au îmbinat subiecte din Psihologie și Știința Calculatoarelor.

## 🚀 Provocare

"Algoritmii genetici sunt simpli de implementat, dar comportamentul lor este dificil de înțeles." [sursa](https://wikipedia.org/wiki/Genetic_algorithm) Fă câteva cercetări pentru a găsi o implementare a unui algoritm genetic, cum ar fi rezolvarea unui puzzle Sudoku, și explică cum funcționează sub forma unei schițe sau a unui diagram de flux.

## [Chestionar după curs](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/221)

## Recapitulare și Studiu Individual

Urmărește [acest videoclip excelent](https://www.youtube.com/watch?v=qv6UVOQ0F44) care vorbește despre cum un calculator poate învăța să joace Super Mario folosind rețele neuronale antrenate de algoritmi genetici. Vom învăța mai multe despre cum calculatoarele învață să joace astfel de jocuri [în secțiunea următoare](../22-DeepRL/README.md).

## [Temă: Ecuația Diofantică](../../../../../lessons/6-Other/21-GeneticAlgorithms/Diophantine.ipynb)

Scopul tău este să rezolvi așa-numita **ecuație diofantică** - o ecuație cu rădăcini întregi. De exemplu, consideră ecuația a+2b+3c+4d=30. Trebuie să găsești rădăcinile întregi care satisfac această ecuație.

*Această temă este inspirată de [acest articol](https://habr.com/post/128704/).*

Sugestii:

1. Poți considera rădăcinile în intervalul [0;30]
1. Ca genă, poți utiliza lista valorilor rădăcinilor

Folosește [Diophantine.ipynb](../../../../../lessons/6-Other/21-GeneticAlgorithms/Diophantine.ipynb) ca punct de plecare.

**Declinare de responsabilitate**:  
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). Deși ne străduim să asigurăm acuratețea, vă rugăm să aveți în vedere că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa natală ar trebui considerat sursa autoritară. Pentru informații critice, se recomandă traducerea profesională realizată de un specialist uman. Nu ne asumăm responsabilitatea pentru eventualele neînțelegeri sau interpretări greșite care pot apărea din utilizarea acestei traduceri.