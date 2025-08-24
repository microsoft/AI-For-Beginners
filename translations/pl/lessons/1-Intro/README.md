<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "5d1cbc67a9690adb5b33adf297794087",
  "translation_date": "2025-08-24T10:24:17+00:00",
  "source_file": "lessons/1-Intro/README.md",
  "language_code": "pl"
}
-->
> Zdjęcie autorstwa [Dmitry Soshnikov](http://soshnikov.com)

Z biegiem czasu zasoby obliczeniowe stały się tańsze, a dostęp do większej ilości danych umożliwił podejściom opartym na sieciach neuronowych osiąganie znakomitych wyników w rywalizacji z ludźmi w wielu dziedzinach, takich jak rozpoznawanie obrazów czy rozumienie mowy. W ostatniej dekadzie termin Sztuczna Inteligencja był często używany jako synonim sieci neuronowych, ponieważ większość sukcesów AI, o których słyszymy, opiera się właśnie na nich.

Możemy zaobserwować, jak zmieniały się podejścia, na przykład w tworzeniu programu komputerowego grającego w szachy:

* Wczesne programy szachowe opierały się na wyszukiwaniu – program próbował oszacować możliwe ruchy przeciwnika na określoną liczbę kolejnych ruchów i wybierał optymalny ruch na podstawie najlepszej pozycji, którą można osiągnąć w kilku ruchach. Doprowadziło to do opracowania tzw. algorytmu wyszukiwania [alpha-beta pruning](https://en.wikipedia.org/wiki/Alpha%E2%80%93beta_pruning).
* Strategie wyszukiwania dobrze sprawdzają się pod koniec gry, gdy przestrzeń wyszukiwania jest ograniczona przez niewielką liczbę możliwych ruchów. Jednak na początku gry przestrzeń wyszukiwania jest ogromna, a algorytm można ulepszyć, ucząc się na podstawie istniejących partii rozegranych przez ludzi. Kolejne eksperymenty wykorzystywały tzw. [rozumowanie oparte na przypadkach](https://en.wikipedia.org/wiki/Case-based_reasoning), gdzie program szukał przypadków w bazie wiedzy bardzo podobnych do obecnej pozycji w grze.
* Nowoczesne programy, które pokonują ludzkich graczy, opierają się na sieciach neuronowych i [uczeniu przez wzmacnianie](https://en.wikipedia.org/wiki/Reinforcement_learning), gdzie programy uczą się grać wyłącznie poprzez wielokrotne rozgrywanie partii przeciwko sobie i uczenie się na własnych błędach – podobnie jak ludzie uczą się grać w szachy. Jednak program komputerowy może rozegrać znacznie więcej partii w znacznie krótszym czasie, dzięki czemu uczy się szybciej.

✅ Zrób małe badanie na temat innych gier, w które grały systemy AI.

Podobnie możemy zaobserwować, jak zmieniało się podejście do tworzenia „programów rozmawiających” (które mogłyby przejść test Turinga):

* Wczesne programy tego typu, takie jak [Eliza](https://en.wikipedia.org/wiki/ELIZA), opierały się na bardzo prostych regułach gramatycznych i przekształcaniu zdania wejściowego w pytanie.
* Nowoczesne asystenty, takie jak Cortana, Siri czy Google Assistant, to systemy hybrydowe, które wykorzystują sieci neuronowe do konwersji mowy na tekst i rozpoznawania naszych intencji, a następnie stosują pewne rozumowanie lub algorytmy do wykonania wymaganych działań.
* W przyszłości możemy spodziewać się pełnego modelu opartego na sieciach neuronowych, który samodzielnie będzie obsługiwał dialog. Ostatnie sieci neuronowe z rodziny GPT i [Turing-NLG](https://turing.microsoft.com/) pokazują w tym zakresie duże sukcesy.

> Zdjęcie autorstwa Dmitry Soshnikov, [zdjęcie](https://unsplash.com/photos/r8LmVbUKgns) autorstwa [Mariny Abrosimovej](https://unsplash.com/@abrosimova_marina_foto), Unsplash

## Najnowsze badania nad sztuczną inteligencją

Ogromny wzrost badań nad sieciami neuronowymi rozpoczął się około 2010 roku, kiedy zaczęły być dostępne duże publiczne zbiory danych. Ogromna kolekcja obrazów o nazwie [ImageNet](https://en.wikipedia.org/wiki/ImageNet), zawierająca około 14 milionów oznaczonych obrazów, dała początek [ImageNet Large Scale Visual Recognition Challenge](https://image-net.org/challenges/LSVRC/).

![Dokładność ILSVRC](../../../../lessons/1-Intro/images/ilsvrc.gif)

> Zdjęcie autorstwa [Dmitry Soshnikov](http://soshnikov.com)

W 2012 roku [konwolucyjne sieci neuronowe](../4-ComputerVision/07-ConvNets/README.md) zostały po raz pierwszy zastosowane w klasyfikacji obrazów, co doprowadziło do znacznego spadku błędów klasyfikacji (z prawie 30% do 16,4%). W 2015 roku architektura ResNet opracowana przez Microsoft Research [osiągnęła dokładność na poziomie ludzkim](https://doi.org/10.1109/ICCV.2015.123).

Od tego czasu sieci neuronowe wykazały bardzo wysoką skuteczność w wielu zadaniach:

---

Rok | Osiągnięcie parytetu z człowiekiem
-----|--------
2015 | [Klasyfikacja obrazów](https://doi.org/10.1109/ICCV.2015.123)
2016 | [Rozpoznawanie mowy konwersacyjnej](https://arxiv.org/abs/1610.05256)
2018 | [Automatyczne tłumaczenie maszynowe](https://arxiv.org/abs/1803.05567) (z chińskiego na angielski)
2020 | [Opisywanie obrazów](https://arxiv.org/abs/2009.13682)

W ostatnich latach byliśmy świadkami ogromnych sukcesów dużych modeli językowych, takich jak BERT i GPT-3. Stało się to głównie dzięki temu, że dostępnych jest wiele ogólnych danych tekstowych, które pozwalają trenować modele w celu uchwycenia struktury i znaczenia tekstów, wstępnie trenować je na ogólnych zbiorach tekstów, a następnie specjalizować te modele do bardziej specyficznych zadań. Więcej o [przetwarzaniu języka naturalnego](../5-NLP/README.md) dowiemy się później w tym kursie.

## 🚀 Wyzwanie

Przeprowadź badanie w internecie, aby określić, gdzie Twoim zdaniem sztuczna inteligencja jest najskuteczniej wykorzystywana. Czy jest to aplikacja mapowa, usługa zamiany mowy na tekst, czy może gra wideo? Zbadaj, jak został zbudowany ten system.

## [Quiz po wykładzie](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/201)

## Przegląd i samodzielna nauka

Przejrzyj historię AI i ML, czytając [tę lekcję](https://github.com/microsoft/ML-For-Beginners/tree/main/1-Introduction/2-history-of-ML). Wybierz element z notatki wizualnej na początku tej lekcji lub tej i zbadaj go bardziej szczegółowo, aby zrozumieć kontekst kulturowy, który wpłynął na jego rozwój.

**Zadanie domowe**: [Game Jam](assignment.md)

**Zastrzeżenie**:  
Ten dokument został przetłumaczony za pomocą usługi tłumaczenia AI [Co-op Translator](https://github.com/Azure/co-op-translator). Chociaż dokładamy wszelkich starań, aby tłumaczenie było precyzyjne, prosimy pamiętać, że automatyczne tłumaczenia mogą zawierać błędy lub nieścisłości. Oryginalny dokument w jego rodzimym języku powinien być uznawany za wiarygodne źródło. W przypadku informacji o kluczowym znaczeniu zaleca się skorzystanie z profesjonalnego tłumaczenia przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z użycia tego tłumaczenia.