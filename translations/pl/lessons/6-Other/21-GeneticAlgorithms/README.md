<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "893aa368cb485da704b466a0f3775587",
  "translation_date": "2025-08-24T10:35:33+00:00",
  "source_file": "lessons/6-Other/21-GeneticAlgorithms/README.md",
  "language_code": "pl"
}
-->
# Algorytmy Genetyczne

## [Quiz przed wykładem](https://ff-quizzes.netlify.app/en/ai/quiz/41)

**Algorytmy Genetyczne** (GA) opierają się na **ewolucyjnym podejściu** do sztucznej inteligencji, w którym wykorzystuje się metody ewolucji populacji do uzyskania optymalnego rozwiązania dla danego problemu. Zostały zaproponowane w 1975 roku przez [Johna Henry'ego Hollanda](https://wikipedia.org/wiki/John_Henry_Holland).

Algorytmy Genetyczne bazują na następujących założeniach:

* Prawidłowe rozwiązania problemu można przedstawić jako **geny**
* **Krzyżowanie** pozwala łączyć dwa rozwiązania, aby uzyskać nowe, prawidłowe rozwiązanie
* **Selekcja** służy do wybierania bardziej optymalnych rozwiązań za pomocą **funkcji dopasowania**
* **Mutacje** są wprowadzane, aby destabilizować optymalizację i wyprowadzać nas z lokalnego minimum

Aby zaimplementować Algorytm Genetyczny, potrzebujesz:

 * Metody kodowania rozwiązań problemu za pomocą **genów** g∈Γ
 * Na zbiorze genów Γ należy zdefiniować **funkcję dopasowania** fit: Γ→**R**. Mniejsze wartości funkcji odpowiadają lepszym rozwiązaniom.
 * Mechanizmu **krzyżowania**, który pozwala łączyć dwa geny w celu uzyskania nowego, prawidłowego rozwiązania crossover: Γ<sup>2</sub>→Γ.
 * Mechanizmu **mutacji** mutate: Γ→Γ.

W wielu przypadkach krzyżowanie i mutacja to dość proste algorytmy manipulujące genami jako sekwencjami liczbowymi lub wektorami bitowymi.

Konkretna implementacja algorytmu genetycznego może różnić się w zależności od przypadku, ale ogólna struktura wygląda następująco:

1. Wybierz początkową populację G⊂Γ
2. Losowo wybierz jedną z operacji, która zostanie wykonana na tym etapie: krzyżowanie lub mutacja
3. **Krzyżowanie**:
  * Losowo wybierz dwa geny g<sub>1</sub>, g<sub>2</sub> ∈ G
  * Oblicz krzyżowanie g=crossover(g<sub>1</sub>,g<sub>2</sub>)
  * Jeśli fit(g)<fit(g<sub>1</sub>) lub fit(g)<fit(g<sub>2</sub>) - zastąp odpowiedni gen w populacji przez g.
4. **Mutacja** - wybierz losowy gen g∈G i zastąp go przez mutate(g)
5. Powtarzaj od kroku 2, aż uzyskasz wystarczająco małą wartość fit lub do osiągnięcia limitu liczby kroków.

## Typowe Zadania

Zadania, które zazwyczaj rozwiązuje się za pomocą Algorytmów Genetycznych, obejmują:

1. Optymalizację harmonogramów
1. Optymalne pakowanie
1. Optymalne cięcie
1. Przyspieszanie wyczerpującego przeszukiwania

## ✍️ Ćwiczenia: Algorytmy Genetyczne

Kontynuuj naukę w poniższych notatnikach:

Przejdź do [tego notatnika](../../../../../lessons/6-Other/21-GeneticAlgorithms/Genetic.ipynb), aby zobaczyć dwa przykłady użycia Algorytmów Genetycznych:

1. Sprawiedliwy podział skarbu
1. Problem 8 hetmanów

## Podsumowanie

Algorytmy Genetyczne są wykorzystywane do rozwiązywania wielu problemów, w tym problemów logistycznych i wyszukiwania. Dziedzina ta jest inspirowana badaniami łączącymi tematy z zakresu psychologii i informatyki.

## 🚀 Wyzwanie

"Algorytmy genetyczne są proste w implementacji, ale ich zachowanie jest trudne do zrozumienia." [źródło](https://wikipedia.org/wiki/Genetic_algorithm) Przeprowadź badania, aby znaleźć implementację algorytmu genetycznego, na przykład rozwiązującego łamigłówkę Sudoku, i wyjaśnij, jak działa w formie szkicu lub schematu blokowego.

## [Quiz po wykładzie](https://ff-quizzes.netlify.app/en/ai/quiz/42)

## Przegląd i Samodzielna Nauka

Obejrzyj [ten świetny film](https://www.youtube.com/watch?v=qv6UVOQ0F44) opowiadający o tym, jak komputer może nauczyć się grać w Super Mario, wykorzystując sieci neuronowe trenowane przez algorytmy genetyczne. Dowiemy się więcej o tym, jak komputer uczy się grać w takie gry [w następnej sekcji](../22-DeepRL/README.md).

## [Zadanie: Równanie Diofantyczne](../../../../../lessons/6-Other/21-GeneticAlgorithms/Diophantine.ipynb)

Twoim celem jest rozwiązanie tzw. **równania diofantycznego** - równania z całkowitymi pierwiastkami. Na przykład rozważ równanie a+2b+3c+4d=30. Musisz znaleźć całkowite pierwiastki, które spełniają to równanie.

*To zadanie jest inspirowane [tym postem](https://habr.com/post/128704/).*

Wskazówki:

1. Możesz rozważyć pierwiastki w przedziale [0;30]
1. Jako gen rozważ użycie listy wartości pierwiastków

Użyj [Diophantine.ipynb](../../../../../lessons/6-Other/21-GeneticAlgorithms/Diophantine.ipynb) jako punktu wyjścia.

**Zastrzeżenie**:  
Ten dokument został przetłumaczony za pomocą usługi tłumaczenia AI [Co-op Translator](https://github.com/Azure/co-op-translator). Chociaż staramy się zapewnić dokładność, prosimy mieć na uwadze, że automatyczne tłumaczenia mogą zawierać błędy lub nieścisłości. Oryginalny dokument w jego rodzimym języku powinien być uznawany za wiarygodne źródło. W przypadku informacji krytycznych zaleca się skorzystanie z profesjonalnego tłumaczenia przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z użycia tego tłumaczenia.