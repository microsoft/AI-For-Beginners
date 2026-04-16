# Algorytmy Genetyczne

## [Quiz przed wykładem](https://ff-quizzes.netlify.app/en/ai/quiz/41)

**Algorytmy Genetyczne** (GA) opierają się na **ewolucyjnym podejściu** do sztucznej inteligencji, w którym metody ewolucji populacji są wykorzystywane do uzyskania optymalnego rozwiązania dla danego problemu. Zostały zaproponowane w 1975 roku przez [Johna Henry'ego Hollanda](https://wikipedia.org/wiki/John_Henry_Holland).

Algorytmy Genetyczne bazują na następujących ideach:

* Poprawne rozwiązania problemu można reprezentować jako **geny**
* **Krzyżowanie** pozwala na połączenie dwóch rozwiązań w celu uzyskania nowego poprawnego rozwiązania
* **Selekcja** służy do wyboru bardziej optymalnych rozwiązań za pomocą **funkcji dopasowania**
* **Mutacje** są wprowadzane, aby destabilizować optymalizację i wyprowadzić nas z lokalnego minimum

Aby zaimplementować Algorytm Genetyczny, potrzebujesz:

 * Metody kodowania rozwiązań problemu za pomocą **genów** g&in;&Gamma;
 * Na zbiorze genów &Gamma; należy zdefiniować **funkcję dopasowania** fit: &Gamma;&rightarrow;**R**. Mniejsze wartości funkcji odpowiadają lepszym rozwiązaniom.
 * Mechanizmu **krzyżowania**, który pozwala na połączenie dwóch genów w celu uzyskania nowego poprawnego rozwiązania crossover: &Gamma;<sup>2</sub>&rightarrow;&Gamma;.
 * Mechanizmu **mutacji** mutate: &Gamma;&rightarrow;&Gamma;.

W wielu przypadkach krzyżowanie i mutacja są dość prostymi algorytmami manipulującymi genami jako sekwencjami liczbowymi lub wektorami bitowymi.

Konkretna implementacja algorytmu genetycznego może się różnić w zależności od przypadku, ale ogólna struktura wygląda następująco:

1. Wybierz początkową populację G&subset;&Gamma;
2. Losowo wybierz jedną z operacji, która zostanie wykonana na tym etapie: krzyżowanie lub mutacja
3. **Krzyżowanie**:
  * Losowo wybierz dwa geny g<sub>1</sub>, g<sub>2</sub> &in; G
  * Oblicz krzyżowanie g=crossover(g<sub>1</sub>,g<sub>2</sub>)
  * Jeśli fit(g)<fit(g<sub>1</sub>) lub fit(g)<fit(g<sub>2</sub>) - zastąp odpowiedni gen w populacji przez g.
4. **Mutacja** - wybierz losowy gen g&in;G i zastąp go przez mutate(g)
5. Powtarzaj od kroku 2, aż uzyskasz wystarczająco małą wartość fit lub do osiągnięcia limitu liczby kroków.

## Typowe Zadania

Zadania typowo rozwiązywane za pomocą Algorytmów Genetycznych obejmują:

1. Optymalizację harmonogramów
1. Optymalne pakowanie
1. Optymalne cięcie
1. Przyspieszenie wyczerpującego przeszukiwania

## ✍️ Ćwiczenia: Algorytmy Genetyczne

Kontynuuj naukę w poniższych notatnikach:

Przejdź do [tego notatnika](Genetic.ipynb), aby zobaczyć dwa przykłady użycia Algorytmów Genetycznych:

1. Sprawiedliwy podział skarbu
1. Problem 8 Hetmanów

## Podsumowanie

Algorytmy Genetyczne są wykorzystywane do rozwiązywania wielu problemów, w tym problemów logistycznych i wyszukiwania. Dziedzina ta jest inspirowana badaniami łączącymi tematy z psychologii i informatyki.

## 🚀 Wyzwanie

"Algorytmy genetyczne są proste w implementacji, ale ich zachowanie jest trudne do zrozumienia." [źródło](https://wikipedia.org/wiki/Genetic_algorithm) Przeprowadź badania, aby znaleźć implementację algorytmu genetycznego, na przykład rozwiązującego łamigłówkę Sudoku, i wyjaśnij, jak działa w formie szkicu lub diagramu przepływu.

## [Quiz po wykładzie](https://ff-quizzes.netlify.app/en/ai/quiz/42)

## Przegląd i Samodzielna Nauka

Obejrzyj [ten świetny film](https://www.youtube.com/watch?v=qv6UVOQ0F44) opowiadający o tym, jak komputer może nauczyć się grać w Super Mario za pomocą sieci neuronowych trenowanych przez algorytmy genetyczne. Dowiemy się więcej o nauce komputerów grających w takie gry [w następnej sekcji](../22-DeepRL/README.md).

## [Zadanie: Równanie Diofantyczne](Diophantine.ipynb)

Twoim celem jest rozwiązanie tzw. **równania Diofantycznego** - równania z całkowitymi pierwiastkami. Na przykład, rozważ równanie a+2b+3c+4d=30. Musisz znaleźć całkowite pierwiastki, które spełniają to równanie.

*To zadanie jest inspirowane [tym postem](https://habr.com/post/128704/).*

Wskazówki:

1. Możesz rozważyć pierwiastki w przedziale [0;30]
1. Jako gen, rozważ użycie listy wartości pierwiastków

Użyj [Diophantine.ipynb](Diophantine.ipynb) jako punktu wyjścia.

---

