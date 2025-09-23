<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "7d097f7fda9166ead615e4c34552381b",
  "translation_date": "2025-09-23T13:54:28+00:00",
  "source_file": "lessons/2-Symbolic/README.md",
  "language_code": "pl"
}
-->
# Reprezentacja wiedzy i systemy ekspertowe

![Podsumowanie treści o Symbolicznym AI](../../../../translated_images/ai-symbolic.715a30cb610411a6964d2e2f23f24364cb338a07cb4844c1f97084d366e586c3.pl.png)

> Sketchnote autorstwa [Tomomi Imura](https://twitter.com/girlie_mac)

Dążenie do sztucznej inteligencji opiera się na poszukiwaniu wiedzy, aby zrozumieć świat w sposób podobny do ludzi. Ale jak można to osiągnąć?

## [Quiz przed wykładem](https://ff-quizzes.netlify.app/en/ai/quiz/3)

W początkowych dniach rozwoju AI popularne było podejście odgórne do tworzenia inteligentnych systemów (omówione w poprzedniej lekcji). Polegało ono na wydobywaniu wiedzy od ludzi w formie zrozumiałej dla maszyn, a następnie wykorzystywaniu jej do automatycznego rozwiązywania problemów. Podejście to opierało się na dwóch kluczowych ideach:

* Reprezentacja wiedzy
* Wnioskowanie

## Reprezentacja wiedzy

Jednym z ważnych pojęć w Symbolicznym AI jest **wiedza**. Ważne jest, aby odróżnić wiedzę od *informacji* czy *danych*. Na przykład można powiedzieć, że książki zawierają wiedzę, ponieważ można je studiować i stać się ekspertem. Jednak to, co zawierają książki, to właściwie *dane*, a czytając książki i integrując te dane z naszym modelem świata, przekształcamy je w wiedzę.

> ✅ **Wiedza** to coś, co znajduje się w naszej głowie i reprezentuje nasze rozumienie świata. Jest zdobywana poprzez aktywny proces **uczenia się**, który integruje otrzymywane informacje z naszym aktywnym modelem świata.

Najczęściej nie definiujemy wiedzy w sposób ścisły, ale zestawiamy ją z innymi powiązanymi pojęciami za pomocą [Piramidy DIKW](https://en.wikipedia.org/wiki/DIKW_pyramid). Zawiera ona następujące poziomy:

* **Dane** to coś reprezentowanego na nośnikach fizycznych, takich jak tekst pisany czy słowa mówione. Dane istnieją niezależnie od ludzi i mogą być przekazywane między nimi.
* **Informacja** to sposób, w jaki interpretujemy dane w naszej głowie. Na przykład, gdy słyszymy słowo *komputer*, mamy pewne wyobrażenie, czym ono jest.
* **Wiedza** to informacja zintegrowana z naszym modelem świata. Na przykład, gdy nauczymy się, czym jest komputer, zaczynamy mieć pewne pojęcie o tym, jak działa, ile kosztuje i do czego można go używać. Ta sieć powiązanych pojęć tworzy naszą wiedzę.
* **Mądrość** to jeszcze wyższy poziom rozumienia świata, reprezentujący *meta-wiedzę*, np. wiedzę o tym, jak i kiedy należy używać wiedzy.

<img src="images/DIKW_Pyramid.png" width="30%"/>

*Obraz [z Wikipedii](https://commons.wikimedia.org/w/index.php?curid=37705247), autorstwa Longlivetheux - własne dzieło, CC BY-SA 4.0*

Problem **reprezentacji wiedzy** polega więc na znalezieniu skutecznego sposobu reprezentowania wiedzy w komputerze w formie danych, aby była automatycznie użyteczna. Można to postrzegać jako spektrum:

![Spektrum reprezentacji wiedzy](../../../../translated_images/knowledge-spectrum.b60df631852c0217e941485b79c9eee40ebd574f15f18609cec5758fcb384bf3.pl.png)

> Obraz autorstwa [Dmitry Soshnikov](http://soshnikov.com)

* Po lewej stronie znajdują się bardzo proste typy reprezentacji wiedzy, które mogą być skutecznie wykorzystywane przez komputery. Najprostszą formą jest algorytmiczna, gdzie wiedza jest reprezentowana przez program komputerowy. Nie jest to jednak najlepszy sposób reprezentowania wiedzy, ponieważ jest mało elastyczny. Wiedza w naszej głowie często nie ma charakteru algorytmicznego.
* Po prawej stronie znajdują się reprezentacje takie jak naturalny tekst. Jest to najbardziej potężna forma, ale nie może być używana do automatycznego wnioskowania.

> ✅ Zastanów się przez chwilę, jak reprezentujesz wiedzę w swojej głowie i przekształcasz ją w notatki. Czy istnieje jakiś format, który dobrze wspomaga zapamiętywanie?

## Klasyfikacja reprezentacji wiedzy w komputerach

Możemy sklasyfikować różne metody reprezentacji wiedzy w komputerach w następujące kategorie:

* **Reprezentacje sieciowe** opierają się na fakcie, że w naszej głowie mamy sieć powiązanych pojęć. Możemy próbować odtworzyć te same sieci jako graf w komputerze - tzw. **sieć semantyczną**.

1. **Trójki obiekt-atrybut-wartość** lub **pary atrybut-wartość**. Ponieważ graf może być reprezentowany w komputerze jako lista węzłów i krawędzi, możemy reprezentować sieć semantyczną jako listę trójek zawierających obiekty, atrybuty i wartości. Na przykład, budujemy następujące trójki o językach programowania:

Obiekt | Atrybut | Wartość
-------|---------|--------
Python | jest | Językiem nietypowanym
Python | wynaleziony-przez | Guido van Rossum
Python | składnia-blokowa | wcięcia
Język nietypowany | nie ma | definicji typów

> ✅ Zastanów się, jak trójki mogą być używane do reprezentowania innych typów wiedzy.

2. **Reprezentacje hierarchiczne** podkreślają fakt, że często tworzymy hierarchię obiektów w naszej głowie. Na przykład, wiemy, że kanarek to ptak, a wszystkie ptaki mają skrzydła. Mamy też pewne wyobrażenie o tym, jaki kolor ma kanarek i jaka jest jego prędkość lotu.

   - **Reprezentacja ramowa** opiera się na reprezentowaniu każdego obiektu lub klasy obiektów jako **ramki**, która zawiera **sloty**. Sloty mają możliwe wartości domyślne, ograniczenia wartości lub procedury przechowywane, które można wywołać, aby uzyskać wartość slotu. Wszystkie ramki tworzą hierarchię podobną do hierarchii obiektów w językach programowania obiektowego.
   - **Scenariusze** to specjalny rodzaj ramek, które reprezentują złożone sytuacje rozwijające się w czasie.

**Python**

Slot | Wartość | Wartość domyślna | Przedział |
-----|---------|------------------|-----------|
Nazwa | Python | | |
Jest-A | Język nietypowany | | |
Styl zmiennych | | CamelCase | |
Długość programu | | | 5-5000 linii |
Składnia blokowa | Wcięcia | | |

3. **Reprezentacje proceduralne** opierają się na reprezentowaniu wiedzy jako listy działań, które można wykonać, gdy wystąpi określony warunek.
   - Reguły produkcji to instrukcje if-then, które pozwalają nam wyciągać wnioski. Na przykład, lekarz może mieć regułę mówiącą, że **JEŚLI** pacjent ma wysoką gorączkę **LUB** wysoki poziom białka C-reaktywnego w badaniu krwi **TO** ma stan zapalny. Gdy napotkamy jeden z warunków, możemy wyciągnąć wniosek o stanie zapalnym, a następnie użyć go w dalszym wnioskowaniu.
   - Algorytmy można uznać za inną formę reprezentacji proceduralnej, choć prawie nigdy nie są używane bezpośrednio w systemach opartych na wiedzy.

4. **Logika** została pierwotnie zaproponowana przez Arystotelesa jako sposób reprezentowania uniwersalnej ludzkiej wiedzy.
   - Logika predykatów jako teoria matematyczna jest zbyt bogata, aby była obliczalna, dlatego zwykle używa się jej podzbioru, takiego jak klauzule Horn używane w Prologu.
   - Logika deskryptywna to rodzina systemów logicznych używanych do reprezentowania i wnioskowania o hierarchiach obiektów w rozproszonych reprezentacjach wiedzy, takich jak *sieć semantyczna*.

## Systemy ekspertowe

Jednym z wczesnych sukcesów symbolicznego AI były tzw. **systemy ekspertowe** - systemy komputerowe zaprojektowane do działania jako ekspert w ograniczonej dziedzinie problemowej. Opierały się na **bazie wiedzy** wydobytej od jednego lub więcej ludzkich ekspertów i zawierały **silnik wnioskowania**, który wykonywał wnioskowanie na jej podstawie.

![Architektura człowieka](../../../../translated_images/arch-human.5d4d35f1bba3ab1cdfda96af2f10b89574eb31e9796d0e3011cd9beda1c35112.pl.png) | ![System oparty na wiedzy](../../../../translated_images/arch-kbs.3ec5c150b09fa8dadc2beb0931a4983c9e2b03913a89eebcc103b5bb841b0212.pl.png)
---------------------------------------------|------------------------------------------------
Uproszczona struktura ludzkiego układu nerwowego | Architektura systemu opartego na wiedzy

Systemy ekspertowe są zbudowane podobnie jak system wnioskowania człowieka, który zawiera **pamięć krótkotrwałą** i **pamięć długotrwałą**. Podobnie w systemach opartych na wiedzy wyróżniamy następujące komponenty:

* **Pamięć problemu**: zawiera wiedzę o aktualnie rozwiązywanym problemie, np. temperaturę czy ciśnienie krwi pacjenta, czy ma stan zapalny, itd. Ta wiedza nazywana jest również **wiedzą statyczną**, ponieważ zawiera migawkę tego, co obecnie wiemy o problemie - tzw. *stan problemu*.
* **Baza wiedzy**: reprezentuje długoterminową wiedzę o dziedzinie problemowej. Jest ręcznie wydobywana od ludzkich ekspertów i nie zmienia się od konsultacji do konsultacji. Ponieważ pozwala nawigować od jednego stanu problemu do drugiego, nazywana jest również **wiedzą dynamiczną**.
* **Silnik wnioskowania**: organizuje cały proces przeszukiwania przestrzeni stanów problemu, zadając pytania użytkownikowi, gdy jest to konieczne. Odpowiada również za znajdowanie odpowiednich reguł do zastosowania w każdym stanie.

Na przykład rozważmy następujący system ekspertowy do określania zwierzęcia na podstawie jego cech fizycznych:

![Drzewo AND-OR](../../../../translated_images/AND-OR-Tree.5592d2c70187f283703c8e9c0d69d6a786eb370f4ace67f9a7aae5ada3d260b0.pl.png)

> Obraz autorstwa [Dmitry Soshnikov](http://soshnikov.com)

Ten diagram nazywa się **drzewem AND-OR** i jest graficzną reprezentacją zestawu reguł produkcji. Rysowanie drzewa jest przydatne na początku wydobywania wiedzy od eksperta. Aby reprezentować wiedzę w komputerze, wygodniej jest używać reguł:

```
IF the animal eats meat
OR (animal has sharp teeth
    AND animal has claws
    AND animal has forward-looking eyes
) 
THEN the animal is a carnivore
```

Możesz zauważyć, że każdy warunek po lewej stronie reguły i akcja są w zasadzie trójkami obiekt-atrybut-wartość (OAV). **Pamięć robocza** zawiera zestaw trójek OAV odpowiadających aktualnie rozwiązywanemu problemowi. **Silnik reguł** szuka reguł, dla których warunek jest spełniony, i stosuje je, dodając kolejną trójkę do pamięci roboczej.

> ✅ Narysuj własne drzewo AND-OR na temat, który Cię interesuje!

### Wnioskowanie w przód vs. wnioskowanie wstecz

Proces opisany powyżej nazywa się **wnioskowaniem w przód**. Zaczyna się od pewnych początkowych danych o problemie dostępnych w pamięci roboczej, a następnie wykonuje następującą pętlę wnioskowania:

1. Jeśli docelowy atrybut jest obecny w pamięci roboczej - zatrzymaj się i podaj wynik
2. Poszukaj wszystkich reguł, których warunek jest obecnie spełniony - uzyskaj **zestaw konfliktów** reguł.
3. Wykonaj **rozwiązanie konfliktu** - wybierz jedną regułę, która zostanie wykonana w tym kroku. Mogą istnieć różne strategie rozwiązywania konfliktów:
   - Wybierz pierwszą pasującą regułę w bazie wiedzy
   - Wybierz losową regułę
   - Wybierz *bardziej szczegółową* regułę, tj. taką, która spełnia najwięcej warunków po stronie "lewej" (LHS)
4. Zastosuj wybraną regułę i wprowadź nowy element wiedzy do stanu problemu
5. Powtórz od kroku 1.

Jednak w niektórych przypadkach możemy chcieć zacząć od pustej wiedzy o problemie i zadawać pytania, które pomogą nam dojść do wniosku. Na przykład podczas diagnozowania medycznego zazwyczaj nie wykonujemy wszystkich analiz medycznych z góry przed rozpoczęciem diagnozowania pacjenta. Raczej chcemy przeprowadzać analizy, gdy trzeba podjąć decyzję.

Ten proces można modelować za pomocą **wnioskowania wstecznego**. Jest on napędzany przez **cel** - wartość atrybutu, którą chcemy znaleźć:

1. Wybierz wszystkie reguły, które mogą dać nam wartość celu (tj. z celem po stronie "prawej" (RHS)) - zestaw konfliktów
1. Jeśli nie ma reguł dla tego atrybutu lub istnieje reguła mówiąca, że powinniśmy zapytać użytkownika o wartość - zapytaj o nią, w przeciwnym razie:
1. Użyj strategii rozwiązywania konfliktów, aby wybrać jedną regułę, którą będziemy używać jako *hipotezę* - spróbujemy ją udowodnić
1. Rekurencyjnie powtórz proces dla wszystkich atrybutów w LHS reguły, próbując je udowodnić jako cele
1. Jeśli w dowolnym momencie proces się nie powiedzie - użyj innej reguły w kroku 3.

> ✅ W jakich sytuacjach wnioskowanie w przód jest bardziej odpowiednie? A wnioskowanie wstecz?

### Implementacja systemów ekspertowych

Systemy ekspertowe można implementować za pomocą różnych narzędzi:

* Programowanie ich bezpośrednio w jakimś języku programowania wysokiego poziomu. Nie jest to najlepszy pomysł, ponieważ główną zaletą systemu opartego na wiedzy jest to, że wiedza jest oddzielona od wnioskowania, a potencjalnie ekspert dziedzinowy powinien być w stanie pisać reguły bez rozumienia szczegółów procesu wnioskowania.
* Korzystanie z **powłoki systemów ekspertowych**, tj. systemu specjalnie zaprojektowanego do wypełniania wiedzą za pomocą jakiegoś języka reprezentacji wiedzy.

## ✍️ Ćwiczenie: Wnioskowanie o zwierzętach

Zobacz [Animals.ipynb](https://github.com/microsoft/AI-For-Beginners/blob/main/lessons/2-Symbolic/Animals.ipynb) jako przykład implementacji systemu ekspertowego z wnioskowaniem w przód i wstecz.

> **Note**: Ten przykład jest dość prosty i tylko daje wyobrażenie, jak wygląda system ekspertowy. Gdy zaczniesz tworzyć taki system, zauważysz pewne *inteligentne* zachowanie dopiero po osiągnięciu pewnej liczby reguł, około 200+. W pewnym momencie reguły stają się zbyt skomplikowane, aby wszystkie je zapamiętać, i wtedy możesz zacząć się zastanawiać, dlaczego system podejmuje określone decyzje. Jednak ważną cechą systemów opartych na wiedzy jest to, że zawsze można *wyjaśnić*, jak podjęto każdą decyzję.

## Ontologie i sieć semantyczna

Pod koniec XX wieku pojawiła się inicjatywa wykorzystania reprezentacji wiedzy do oznaczania zasobów internetowych, aby możliwe było znajdowanie zasobów odpowiadających bardzo specyficznym zapytaniom. Ten ruch nazwano **siecią semantyczną**, a opierał się na kilku koncepcjach:

- Specjalna reprezentacja wiedzy oparta na **[logikach deskryptywnych](https://en.wikipedia.org/wiki/Description_logic)** (DL). Jest podobna do reprezentacji wiedzy ramowej, ponieważ buduje hierarchię obiektów z właściwościami, ale ma formalną semantykę logiczną i wnioskowanie. Istnieje cała rodzina DL, które balansują między ekspresywnością a algorytmiczną złożonością wnioskowania.
- Rozproszona reprezentacja wiedzy, gdzie wszystkie pojęcia są reprezentowane przez globalny identyfikator URI, co umożliwia tworzenie hierarchii wiedzy obejmujących internet.
- Rodzina języków opartych na XML do opisu wiedzy: RDF (Resource Description Framework), RDFS (RDF Schema), OWL (Ontology Web Language).

Podstawowym pojęciem w Semantic Web jest **ontologia**. Odnosi się ona do jawnej specyfikacji dziedziny problemowej przy użyciu formalnej reprezentacji wiedzy. Najprostsza ontologia może być po prostu hierarchią obiektów w danej dziedzinie, ale bardziej złożone ontologie zawierają reguły, które mogą być używane do wnioskowania.

W Semantic Web wszystkie reprezentacje opierają się na trójkach. Każdy obiekt i każda relacja są jednoznacznie identyfikowane przez URI. Na przykład, jeśli chcemy stwierdzić fakt, że ten program AI Curriculum został opracowany przez Dmitry Soshnikova 1 stycznia 2022 roku, oto trójki, których możemy użyć:

<img src="images/triplet.png" width="30%"/>

```
http://github.com/microsoft/ai-for-beginners http://www.example.com/terms/creation-date “Jan 13, 2007”
http://github.com/microsoft/ai-for-beginners http://purl.org/dc/elements/1.1/creator http://soshnikov.com
```

> ✅ Tutaj `http://www.example.com/terms/creation-date` i `http://purl.org/dc/elements/1.1/creator` to dobrze znane i powszechnie akceptowane URI do wyrażania pojęć *twórca* i *data utworzenia*.

W bardziej złożonym przypadku, jeśli chcemy zdefiniować listę twórców, możemy użyć struktur danych zdefiniowanych w RDF.

<img src="images/triplet-complex.png" width="40%"/>

> Diagramy powyżej autorstwa [Dmitry Soshnikov](http://soshnikov.com)

Postęp w budowaniu Semantic Web został częściowo spowolniony przez sukces wyszukiwarek i technik przetwarzania języka naturalnego, które pozwalają na wydobywanie danych strukturalnych z tekstu. Jednak w niektórych obszarach wciąż podejmowane są znaczące wysiłki w celu utrzymania ontologii i baz wiedzy. Kilka projektów wartych uwagi:

* [WikiData](https://wikidata.org/) to zbiór maszynowo czytelnych baz wiedzy powiązanych z Wikipedią. Większość danych jest wydobywana z *InfoBoxów* Wikipedii, czyli fragmentów strukturalnych treści na stronach Wikipedii. Możesz [zapytania](https://query.wikidata.org/) do WikiData w SPARQL, specjalnym języku zapytań dla Semantic Web. Oto przykładowe zapytanie, które pokazuje najpopularniejsze kolory oczu wśród ludzi:

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

* [DBpedia](https://www.dbpedia.org/) to kolejna inicjatywa podobna do WikiData.

> ✅ Jeśli chcesz eksperymentować z budowaniem własnych ontologii lub otwieraniem istniejących, istnieje świetny wizualny edytor ontologii o nazwie [Protégé](https://protege.stanford.edu/). Pobierz go lub użyj online.

<img src="images/protege.png" width="70%"/>

*Edytor Web Protégé otwarty z ontologią rodziny Romanowów. Zrzut ekranu autorstwa Dmitry Soshnikov*

## ✍️ Ćwiczenie: Ontologia Rodziny

Zobacz [FamilyOntology.ipynb](https://github.com/Ezana135/AI-For-Beginners/blob/main/lessons/2-Symbolic/FamilyOntology.ipynb) jako przykład użycia technik Semantic Web do rozumowania o relacjach rodzinnych. Weźmiemy drzewo genealogiczne przedstawione w popularnym formacie GEDCOM oraz ontologię relacji rodzinnych i zbudujemy graf wszystkich relacji rodzinnych dla danego zestawu osób.

## Microsoft Concept Graph

W większości przypadków ontologie są starannie tworzone ręcznie. Jednak możliwe jest również **wydobywanie** ontologii z danych niestrukturalnych, na przykład z tekstów w języku naturalnym.

Jednym z takich prób było przedsięwzięcie Microsoft Research, które zaowocowało [Microsoft Concept Graph](https://blogs.microsoft.com/ai/microsoft-researchers-release-graph-that-helps-machines-conceptualize/?WT.mc_id=academic-77998-cacaste).

Jest to duży zbiór jednostek grupowanych za pomocą relacji dziedziczenia `is-a`. Pozwala odpowiadać na pytania typu "Czym jest Microsoft?" - odpowiedź może brzmieć "firmą z prawdopodobieństwem 0,87 oraz marką z prawdopodobieństwem 0,75".

Graf jest dostępny zarówno jako REST API, jak i jako duży plik tekstowy do pobrania, który zawiera wszystkie pary jednostek.

## ✍️ Ćwiczenie: Graf Konceptów

Wypróbuj notebook [MSConceptGraph.ipynb](https://github.com/microsoft/AI-For-Beginners/blob/main/lessons/2-Symbolic/MSConceptGraph.ipynb), aby zobaczyć, jak można użyć Microsoft Concept Graph do grupowania artykułów prasowych w kilka kategorii.

## Podsumowanie

Obecnie AI często jest uważane za synonim *uczenia maszynowego* lub *sieci neuronowych*. Jednak człowiek wykazuje również zdolność do jawnego rozumowania, co jest czymś, czego obecnie nie obsługują sieci neuronowe. W rzeczywistych projektach jawne rozumowanie wciąż jest używane do wykonywania zadań wymagających wyjaśnień lub możliwości kontrolowanej modyfikacji zachowania systemu.

## 🚀 Wyzwanie

W notebooku Ontologia Rodziny związanym z tą lekcją istnieje możliwość eksperymentowania z innymi relacjami rodzinnymi. Spróbuj odkryć nowe powiązania między osobami w drzewie genealogicznym.

## [Quiz po wykładzie](https://ff-quizzes.netlify.app/en/ai/quiz/4)

## Przegląd i Samodzielna Nauka

Przeprowadź badania w internecie, aby odkryć obszary, w których ludzie próbowali kwantyfikować i kodować wiedzę. Przyjrzyj się taksonomii Blooma i cofnij się w historii, aby dowiedzieć się, jak ludzie próbowali zrozumieć swój świat. Zbadaj pracę Linneusza nad stworzeniem taksonomii organizmów i zobacz, jak Dmitrij Mendelejew stworzył sposób opisu i grupowania pierwiastków chemicznych. Jakie inne interesujące przykłady możesz znaleźć?

**Zadanie**: [Zbuduj Ontologię](assignment.md)

---

