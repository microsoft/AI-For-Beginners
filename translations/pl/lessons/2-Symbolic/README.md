<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "98c5222ff9556b55223fed2337145e18",
  "translation_date": "2025-08-24T10:47:17+00:00",
  "source_file": "lessons/2-Symbolic/README.md",
  "language_code": "pl"
}
-->
# Reprezentacja wiedzy i systemy ekspertowe

![Podsumowanie treści o Symbolic AI](../../../../lessons/sketchnotes/ai-symbolic.png)

> Sketchnotka autorstwa [Tomomi Imura](https://twitter.com/girlie_mac)

Dążenie do stworzenia sztucznej inteligencji opiera się na poszukiwaniu wiedzy, aby zrozumieć świat w sposób podobny do ludzi. Ale jak można to osiągnąć?

## [Quiz przed wykładem](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/102)

W początkowych dniach rozwoju AI popularne było podejście odgórne do tworzenia inteligentnych systemów (omówione w poprzedniej lekcji). Polegało ono na wydobywaniu wiedzy od ludzi w formie czytelnej dla maszyn, a następnie wykorzystywaniu jej do automatycznego rozwiązywania problemów. To podejście opierało się na dwóch kluczowych ideach:

* Reprezentacja wiedzy
* Wnioskowanie

## Reprezentacja wiedzy

Jednym z ważnych pojęć w Symbolic AI jest **wiedza**. Ważne jest, aby odróżnić wiedzę od *informacji* czy *danych*. Na przykład można powiedzieć, że książki zawierają wiedzę, ponieważ można je studiować i stać się ekspertem. Jednak to, co zawierają książki, to w rzeczywistości *dane*, a czytając książki i integrując te dane z naszym modelem świata, przekształcamy je w wiedzę.

> ✅ **Wiedza** to coś, co znajduje się w naszej głowie i reprezentuje nasze rozumienie świata. Jest zdobywana w wyniku aktywnego procesu **uczenia się**, który integruje otrzymywane informacje z naszym aktywnym modelem świata.

Najczęściej nie definiujemy wiedzy w sposób ścisły, ale porównujemy ją z innymi powiązanymi pojęciami za pomocą [Piramidy DIKW](https://en.wikipedia.org/wiki/DIKW_pyramid). Zawiera ona następujące poziomy:

* **Dane** to coś reprezentowanego na nośnikach fizycznych, takich jak tekst pisany czy słowa mówione. Dane istnieją niezależnie od ludzi i mogą być przekazywane między nimi.
* **Informacja** to sposób, w jaki interpretujemy dane w naszej głowie. Na przykład, gdy słyszymy słowo *komputer*, mamy pewne wyobrażenie, czym ono jest.
* **Wiedza** to informacja zintegrowana z naszym modelem świata. Na przykład, gdy nauczymy się, czym jest komputer, zaczynamy mieć pewne pojęcie o tym, jak działa, ile kosztuje i do czego można go używać. Ta sieć powiązanych pojęć tworzy naszą wiedzę.
* **Mądrość** to jeszcze wyższy poziom rozumienia świata, reprezentujący *meta-wiedzę*, np. wiedzę o tym, jak i kiedy używać posiadanej wiedzy.

*Obraz [z Wikipedii](https://commons.wikimedia.org/w/index.php?curid=37705247), autorstwa Longlivetheux - własna praca, CC BY-SA 4.0*

W związku z tym problem **reprezentacji wiedzy** polega na znalezieniu skutecznego sposobu reprezentowania wiedzy w komputerze w formie danych, aby mogła być automatycznie wykorzystywana. Można to zobrazować jako spektrum:

![Spektrum reprezentacji wiedzy](../../../../lessons/2-Symbolic/images/knowledge-spectrum.png)

> Obraz autorstwa [Dmitry Soshnikov](http://soshnikov.com)

* Po lewej stronie znajdują się bardzo proste typy reprezentacji wiedzy, które mogą być efektywnie wykorzystywane przez komputery. Najprostszą formą jest algorytmiczna, gdzie wiedza jest reprezentowana przez program komputerowy. Nie jest to jednak najlepszy sposób reprezentacji wiedzy, ponieważ nie jest elastyczny. Wiedza w naszej głowie często nie ma charakteru algorytmicznego.
* Po prawej stronie znajdują się reprezentacje takie jak tekst naturalny. Jest to najbardziej zaawansowana forma, ale nie nadaje się do automatycznego wnioskowania.

> ✅ Zastanów się przez chwilę, jak reprezentujesz wiedzę w swojej głowie i przekształcasz ją w notatki. Czy istnieje jakiś format, który szczególnie dobrze wspiera Twoją pamięć?

## Klasyfikacja reprezentacji wiedzy w komputerach

Różne metody reprezentacji wiedzy w komputerach można sklasyfikować w następujące kategorie:

* **Reprezentacje sieciowe** opierają się na fakcie, że w naszej głowie mamy sieć powiązanych pojęć. Możemy próbować odtworzyć te same sieci w formie grafu w komputerze - tzw. **sieć semantyczna**.

1. **Trójki Obiekt-Atrybut-Wartość** lub **pary atrybut-wartość**. Ponieważ graf można reprezentować w komputerze jako listę węzłów i krawędzi, sieć semantyczną można przedstawić jako listę trójek zawierających obiekty, atrybuty i wartości. Na przykład, możemy stworzyć następujące trójki o językach programowania:

Obiekt | Atrybut | Wartość
-------|---------|--------
Python | jest | Językiem nietypowanym
Python | wynaleziony przez | Guido van Rossum
Python | składnia blokowa | wcięcia
Język nietypowany | nie posiada | definicji typów

> ✅ Pomyśl, jak trójki mogą być używane do reprezentowania innych rodzajów wiedzy.

2. **Reprezentacje hierarchiczne** podkreślają fakt, że często tworzymy hierarchię obiektów w naszej głowie. Na przykład wiemy, że kanarek to ptak, a wszystkie ptaki mają skrzydła. Mamy też pewne wyobrażenie o kolorze kanarka i jego prędkości lotu.

   - **Reprezentacja ramowa** opiera się na reprezentowaniu każdego obiektu lub klasy obiektów jako **ramy**, która zawiera **sloty**. Sloty mogą mieć domyślne wartości, ograniczenia wartości lub procedury, które można wywołać, aby uzyskać wartość slotu. Wszystkie ramy tworzą hierarchię podobną do hierarchii obiektów w językach programowania obiektowego.
   - **Scenariusze** to specjalny rodzaj ram, które reprezentują złożone sytuacje rozwijające się w czasie.

**Python**

Slot | Wartość | Wartość domyślna | Przedział |
-----|---------|------------------|-----------|
Nazwa | Python | | |
Jest-A | Język nietypowany | | |
Wielkość zmiennych | | CamelCase | |
Długość programu | | | 5-5000 linii |
Składnia blokowa | Wcięcia | | |

3. **Reprezentacje proceduralne** opierają się na reprezentowaniu wiedzy jako listy działań, które można wykonać, gdy wystąpi określony warunek.
   - Reguły produkcji to instrukcje typu "jeśli-to", które pozwalają wyciągać wnioski. Na przykład lekarz może mieć regułę mówiącą, że **JEŚLI** pacjent ma wysoką gorączkę **LUB** wysoki poziom białka C-reaktywnego w badaniu krwi, **TO** ma stan zapalny. Gdy napotkamy jeden z warunków, możemy wyciągnąć wniosek o stanie zapalnym, a następnie użyć go w dalszym wnioskowaniu.
   - Algorytmy można uznać za inną formę reprezentacji proceduralnej, choć prawie nigdy nie są używane bezpośrednio w systemach opartych na wiedzy.

4. **Logika** została pierwotnie zaproponowana przez Arystotelesa jako sposób reprezentowania uniwersalnej wiedzy ludzkiej.
   - Logika predykatów jako teoria matematyczna jest zbyt bogata, aby była obliczalna, dlatego zwykle używa się jej podzbioru, takiego jak klauzule Horna używane w Prologu.
   - Logika deskrypcyjna to rodzina systemów logicznych używanych do reprezentowania i wnioskowania o hierarchiach obiektów w rozproszonych reprezentacjach wiedzy, takich jak *sieć semantyczna*.

## Systemy ekspertowe

Jednym z wczesnych sukcesów Symbolic AI były tzw. **systemy ekspertowe** - systemy komputerowe zaprojektowane do działania jako ekspert w ograniczonej dziedzinie problemowej. Opierały się na **bazie wiedzy** wydobytej od jednego lub więcej ludzkich ekspertów i zawierały **silnik wnioskowania**, który przeprowadzał pewne wnioskowanie na jej podstawie.

![Architektura człowieka](../../../../lessons/2-Symbolic/images/arch-human.png) | ![System oparty na wiedzy](../../../../lessons/2-Symbolic/images/arch-kbs.png)
---------------------------------------------|-----------------------------------------------
Uproszczona struktura ludzkiego układu nerwowego | Architektura systemu opartego na wiedzy

Systemy ekspertowe są zbudowane podobnie jak ludzki system wnioskowania, który zawiera **pamięć krótkotrwałą** i **pamięć długotrwałą**. Podobnie w systemach opartych na wiedzy wyróżniamy następujące komponenty:

* **Pamięć problemu**: zawiera wiedzę o aktualnie rozwiązywanym problemie, np. temperaturę lub ciśnienie krwi pacjenta, czy ma stan zapalny, itp. Ta wiedza nazywana jest również **wiedzą statyczną**, ponieważ zawiera migawkę tego, co obecnie wiemy o problemie - tzw. *stan problemu*.
* **Baza wiedzy**: reprezentuje wiedzę długoterminową o dziedzinie problemowej. Jest ręcznie wydobywana od ludzkich ekspertów i nie zmienia się między konsultacjami. Ponieważ pozwala nawigować między stanami problemu, nazywana jest również **wiedzą dynamiczną**.
* **Silnik wnioskowania**: koordynuje cały proces przeszukiwania przestrzeni stanów problemu, zadając pytania użytkownikowi, gdy jest to konieczne. Odpowiada również za znajdowanie odpowiednich reguł do zastosowania w każdym stanie.

Na przykład rozważmy następujący system ekspertowy do określania zwierzęcia na podstawie jego cech fizycznych:

![Drzewo AND-OR](../../../../lessons/2-Symbolic/images/AND-OR-Tree.png)

> Obraz autorstwa [Dmitry Soshnikov](http://soshnikov.com)

Ten diagram nazywa się **drzewem AND-OR** i jest graficzną reprezentacją zestawu reguł produkcji. Rysowanie drzewa jest przydatne na początku procesu wydobywania wiedzy od eksperta. Aby reprezentować wiedzę w komputerze, wygodniej jest używać reguł:

```
IF the animal eats meat
OR (animal has sharp teeth
    AND animal has claws
    AND animal has forward-looking eyes
) 
THEN the animal is a carnivore
```

Możesz zauważyć, że każdy warunek po lewej stronie reguły i akcja to w istocie trójki obiekt-atrybut-wartość (OAV). **Pamięć robocza** zawiera zestaw trójek OAV odpowiadających aktualnie rozwiązywanemu problemowi. **Silnik reguł** szuka reguł, dla których warunek jest spełniony, i stosuje je, dodając kolejną trójkę do pamięci roboczej.

> ✅ Narysuj własne drzewo AND-OR na temat, który Cię interesuje!

### Wnioskowanie w przód vs. wnioskowanie wstecz

Opisany powyżej proces nazywa się **wnioskowaniem w przód**. Zaczyna się od pewnych początkowych danych o problemie dostępnych w pamięci roboczej, a następnie wykonuje następującą pętlę wnioskowania:

1. Jeśli docelowy atrybut jest obecny w pamięci roboczej - zatrzymaj się i podaj wynik
2. Poszukaj wszystkich reguł, których warunek jest obecnie spełniony - uzyskaj **zestaw konfliktów** reguł.
3. Wykonaj **rozwiązanie konfliktu** - wybierz jedną regułę, która zostanie wykonana w tym kroku. Mogą istnieć różne strategie rozwiązywania konfliktów:
   - Wybierz pierwszą pasującą regułę w bazie wiedzy
   - Wybierz losową regułę
   - Wybierz *bardziej szczegółową* regułę, tj. taką, która spełnia najwięcej warunków po stronie "lewej" (LHS)
4. Zastosuj wybraną regułę i wprowadź nowy element wiedzy do stanu problemu
5. Powtórz od kroku 1.

Jednak w niektórych przypadkach możemy chcieć zacząć od braku wiedzy o problemie i zadawać pytania, które pomogą nam dojść do wniosku. Na przykład podczas diagnozy medycznej zwykle nie wykonujemy wszystkich analiz medycznych z góry przed rozpoczęciem diagnozowania pacjenta. Raczej chcemy przeprowadzać analizy, gdy trzeba podjąć decyzję.

Ten proces można modelować za pomocą **wnioskowania wstecz**. Jest on napędzany przez **cel** - wartość atrybutu, którą chcemy znaleźć:

1. Wybierz wszystkie reguły, które mogą dać nam wartość celu (tj. z celem po stronie prawej (RHS)) - zestaw konfliktów
1. Jeśli nie ma reguł dla tego atrybutu lub istnieje reguła mówiąca, że powinniśmy zapytać użytkownika o wartość - zapytaj o nią, w przeciwnym razie:
1. Użyj strategii rozwiązywania konfliktów, aby wybrać jedną regułę, którą będziemy traktować jako *hipotezę* - spróbujemy ją udowodnić
1. Rekurencyjnie powtórz proces dla wszystkich atrybutów po stronie lewej reguły, próbując je udowodnić jako cele
1. Jeśli w dowolnym momencie proces się nie powiedzie - użyj innej reguły w kroku 3.

> ✅ W jakich sytuacjach bardziej odpowiednie jest wnioskowanie w przód? A wnioskowanie wstecz?

### Implementacja systemów ekspertowych

Systemy ekspertowe można implementować za pomocą różnych narzędzi:

* Programowanie ich bezpośrednio w jakimś języku programowania wysokiego poziomu. Nie jest to najlepszy pomysł, ponieważ główną zaletą systemu opartego na wiedzy jest to, że wiedza jest oddzielona od wnioskowania, a potencjalnie ekspert dziedzinowy powinien być w stanie pisać reguły bez rozumienia szczegółów procesu wnioskowania.
* Używanie **powłoki systemu ekspertowego**, tj. systemu specjalnie zaprojektowanego do wypełniania wiedzą za pomocą jakiegoś języka reprezentacji wiedzy.

## ✍️ Ćwiczenie: Wnioskowanie o zwierzętach

Zobacz [Animals.ipynb](https://github.com/microsoft/AI-For-Beginners/blob/main/lessons/2-Symbolic/Animals.ipynb) jako przykład implementacji systemu ekspertowego z wnioskowaniem w przód i wstecz.
> **Uwaga**: Ten przykład jest dość prosty i jedynie daje ogólne pojęcie o tym, jak wygląda system ekspercki. Gdy zaczniesz tworzyć taki system, zauważysz *inteligentne* zachowanie dopiero po osiągnięciu pewnej liczby reguł, około 200+. W pewnym momencie reguły stają się zbyt skomplikowane, by wszystkie je zapamiętać, i wtedy możesz zacząć się zastanawiać, dlaczego system podejmuje określone decyzje. Jednak ważną cechą systemów opartych na wiedzy jest to, że zawsze można *wyjaśnić*, w jaki sposób podjęto każdą z decyzji.
## Ontologie i Sieć Semantyczna

Pod koniec XX wieku pojawiła się inicjatywa wykorzystania reprezentacji wiedzy do opisywania zasobów internetowych, aby możliwe było znajdowanie zasobów odpowiadających bardzo specyficznym zapytaniom. Ten ruch nazwano **Siecią Semantyczną** i opierał się na kilku koncepcjach:

- Specjalnej reprezentacji wiedzy opartej na **[logikach deskrypcyjnych](https://en.wikipedia.org/wiki/Description_logic)** (DL). Jest ona podobna do reprezentacji wiedzy w ramach, ponieważ buduje hierarchię obiektów z właściwościami, ale posiada formalną semantykę logiczną i wnioskowanie. Istnieje cała rodzina logik deskrypcyjnych, które balansują między ekspresywnością a algorytmiczną złożonością wnioskowania.
- Rozproszonej reprezentacji wiedzy, gdzie wszystkie pojęcia są reprezentowane przez globalny identyfikator URI, co umożliwia tworzenie hierarchii wiedzy obejmujących cały internet.
- Rodziny języków opartych na XML do opisu wiedzy: RDF (Resource Description Framework), RDFS (RDF Schema), OWL (Ontology Web Language).

Kluczowym pojęciem w Sieci Semantycznej jest pojęcie **Ontologii**. Odnosi się ono do jawnej specyfikacji dziedziny problemowej przy użyciu formalnej reprezentacji wiedzy. Najprostsza ontologia może być po prostu hierarchią obiektów w danej dziedzinie, ale bardziej złożone ontologie zawierają reguły, które mogą być używane do wnioskowania.

W Sieci Semantycznej wszystkie reprezentacje opierają się na trójkach. Każdy obiekt i każda relacja są jednoznacznie identyfikowane przez URI. Na przykład, jeśli chcemy stwierdzić, że ten program nauczania AI został opracowany przez Dmitrija Soshnikova 1 stycznia 2022 roku, oto trójki, których możemy użyć:

<img src="images/triplet.png" width="30%"/>

```
http://github.com/microsoft/ai-for-beginners http://www.example.com/terms/creation-date “Jan 13, 2007”
http://github.com/microsoft/ai-for-beginners http://purl.org/dc/elements/1.1/creator http://soshnikov.com
```

> ✅ Tutaj `http://www.example.com/terms/creation-date` i `http://purl.org/dc/elements/1.1/creator` to dobrze znane i powszechnie akceptowane URI wyrażające pojęcia *twórcy* i *daty utworzenia*.

W bardziej złożonym przypadku, jeśli chcemy zdefiniować listę twórców, możemy użyć struktur danych zdefiniowanych w RDF.

<img src="images/triplet-complex.png" width="40%"/>

> Diagramy powyżej autorstwa [Dmitrija Soshnikova](http://soshnikov.com)

Postęp w budowie Sieci Semantycznej został w pewnym stopniu spowolniony przez sukces wyszukiwarek i technik przetwarzania języka naturalnego, które pozwalają na wydobywanie danych strukturalnych z tekstu. Jednak w niektórych obszarach wciąż podejmowane są znaczące wysiłki na rzecz utrzymania ontologii i baz wiedzy. Kilka projektów wartych uwagi:

* [WikiData](https://wikidata.org/) to zbiór maszynowo czytelnych baz wiedzy powiązanych z Wikipedią. Większość danych pochodzi z *InfoBoxów* Wikipedii, czyli fragmentów strukturalnych treści na stronach Wikipedii. Możesz [przeszukiwać](https://query.wikidata.org/) WikiData za pomocą SPARQL, specjalnego języka zapytań dla Sieci Semantycznej. Oto przykładowe zapytanie, które wyświetla najpopularniejsze kolory oczu wśród ludzi:

```sparql
#defaultView:BubbleChart
SELECT ?eyeColorLabel (COUNT(?human) AS ?count)
WHERE
{
  ?human wdt:P31 wd:Q5.       # human instance-of homo sapiens
  ?human wdt:P1340 ?eyeColor. # human eye-color ?eyeColor
  SERVICE wikibase:label { bd:serviceParam wikibase:language "en". }
}
GROUP BY ?eyeColorLabel
```

* [DBpedia](https://www.dbpedia.org/) to inna inicjatywa podobna do WikiData.

> ✅ Jeśli chcesz eksperymentować z budowaniem własnych ontologii lub otwieraniem istniejących, istnieje świetny wizualny edytor ontologii o nazwie [Protégé](https://protege.stanford.edu/). Pobierz go lub użyj online.

<img src="images/protege.png" width="70%"/>

*Edytor Web Protégé otwarty z ontologią rodziny Romanowów. Zrzut ekranu autorstwa Dmitrija Soshnikova*

## ✍️ Ćwiczenie: Ontologia Rodzinna

Zobacz [FamilyOntology.ipynb](https://github.com/Ezana135/AI-For-Beginners/blob/main/lessons/2-Symbolic/FamilyOntology.ipynb) jako przykład wykorzystania technik Sieci Semantycznej do wnioskowania o relacjach rodzinnych. Weźmiemy drzewo genealogiczne zapisane w popularnym formacie GEDCOM oraz ontologię relacji rodzinnych i zbudujemy graf wszystkich relacji rodzinnych dla danego zestawu osób.

## Microsoft Concept Graph

W większości przypadków ontologie są starannie tworzone ręcznie. Jednak możliwe jest również **wydobywanie** ontologii z danych niestrukturalnych, na przykład z tekstów w języku naturalnym.

Jedną z takich prób podjęto w Microsoft Research, co zaowocowało [Microsoft Concept Graph](https://blogs.microsoft.com/ai/microsoft-researchers-release-graph-that-helps-machines-conceptualize/?WT.mc_id=academic-77998-cacaste).

Jest to duży zbiór jednostek pogrupowanych za pomocą relacji dziedziczenia `is-a`. Umożliwia odpowiadanie na pytania typu "Czym jest Microsoft?" - odpowiedź może brzmieć: "firmą z prawdopodobieństwem 0,87 i marką z prawdopodobieństwem 0,75".

Graf jest dostępny zarówno jako REST API, jak i w postaci dużego pliku tekstowego zawierającego wszystkie pary jednostek.

## ✍️ Ćwiczenie: Graf Konceptów

Wypróbuj notatnik [MSConceptGraph.ipynb](https://github.com/microsoft/AI-For-Beginners/blob/main/lessons/2-Symbolic/MSConceptGraph.ipynb), aby zobaczyć, jak można wykorzystać Microsoft Concept Graph do grupowania artykułów prasowych w kilka kategorii.

## Podsumowanie

Obecnie AI często jest utożsamiane z *uczeniem maszynowym* lub *sieciami neuronowymi*. Jednak człowiek wykazuje również zdolność do jawnego rozumowania, co jest czymś, czego obecnie nie obsługują sieci neuronowe. W rzeczywistych projektach jawne rozumowanie wciąż jest wykorzystywane do wykonywania zadań wymagających wyjaśnień lub możliwości kontrolowanej modyfikacji zachowania systemu.

## 🚀 Wyzwanie

W notatniku Family Ontology związanym z tą lekcją istnieje możliwość eksperymentowania z innymi relacjami rodzinnymi. Spróbuj odkryć nowe powiązania między osobami w drzewie genealogicznym.

## [Quiz po wykładzie](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/202)

## Przegląd i Samodzielna Nauka

Poszukaj w internecie informacji o obszarach, w których ludzie próbowali kwantyfikować i kodować wiedzę. Przyjrzyj się taksonomii Blooma i cofnij się w historii, aby dowiedzieć się, jak ludzie próbowali zrozumieć otaczający ich świat. Zbadaj pracę Linneusza nad tworzeniem taksonomii organizmów i zobacz, jak Dmitrij Mendelejew stworzył sposób opisu i grupowania pierwiastków chemicznych. Jakie inne interesujące przykłady możesz znaleźć?

**Zadanie domowe**: [Zbuduj Ontologię](assignment.md)

**Zastrzeżenie**:  
Ten dokument został przetłumaczony za pomocą usługi tłumaczenia AI [Co-op Translator](https://github.com/Azure/co-op-translator). Chociaż staramy się zapewnić dokładność, prosimy mieć na uwadze, że automatyczne tłumaczenia mogą zawierać błędy lub nieścisłości. Oryginalny dokument w jego rodzimym języku powinien być uznawany za wiarygodne źródło. W przypadku informacji krytycznych zaleca się skorzystanie z profesjonalnego tłumaczenia wykonanego przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z użycia tego tłumaczenia.