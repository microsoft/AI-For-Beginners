<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "7d097f7fda9166ead615e4c34552381b",
  "translation_date": "2025-09-23T12:19:34+00:00",
  "source_file": "lessons/2-Symbolic/README.md",
  "language_code": "de"
}
-->
# Wissensrepräsentation und Expertensysteme

![Zusammenfassung des Symbolischen KI-Inhalts](../../../../translated_images/ai-symbolic.715a30cb610411a6964d2e2f23f24364cb338a07cb4844c1f97084d366e586c3.de.png)

> Sketchnote von [Tomomi Imura](https://twitter.com/girlie_mac)

Die Suche nach künstlicher Intelligenz basiert auf dem Streben nach Wissen, um die Welt ähnlich wie Menschen zu verstehen. Aber wie kann man das erreichen?

## [Quiz vor der Vorlesung](https://ff-quizzes.netlify.app/en/ai/quiz/3)

In den frühen Tagen der KI war der Top-Down-Ansatz zur Erstellung intelligenter Systeme (im vorherigen Kapitel besprochen) beliebt. Die Idee war, das Wissen von Menschen in eine maschinenlesbare Form zu extrahieren und es dann zu nutzen, um Probleme automatisch zu lösen. Dieser Ansatz basierte auf zwei großen Konzepten:

* Wissensrepräsentation
* Schlussfolgerung

## Wissensrepräsentation

Eines der wichtigen Konzepte in der symbolischen KI ist **Wissen**. Es ist wichtig, Wissen von *Information* oder *Daten* zu unterscheiden. Zum Beispiel könnte man sagen, dass Bücher Wissen enthalten, weil man durch das Studium von Büchern ein Experte werden kann. Tatsächlich enthalten Bücher jedoch *Daten*, und durch das Lesen und Integrieren dieser Daten in unser Weltmodell verwandeln wir diese Daten in Wissen.

> ✅ **Wissen** ist etwas, das in unserem Kopf enthalten ist und unsere Vorstellung von der Welt repräsentiert. Es wird durch einen aktiven **Lernprozess** gewonnen, der die erhaltenen Informationen in unser aktives Weltmodell integriert.

Meistens definieren wir Wissen nicht streng, sondern ordnen es anderen verwandten Konzepten zu, wie sie in der [DIKW-Pyramide](https://en.wikipedia.org/wiki/DIKW_pyramid) dargestellt sind. Sie enthält die folgenden Konzepte:

* **Daten** sind etwas, das in physischer Form dargestellt wird, wie geschriebener Text oder gesprochene Worte. Daten existieren unabhängig von Menschen und können zwischen ihnen weitergegeben werden.
* **Information** ist, wie wir Daten in unserem Kopf interpretieren. Zum Beispiel haben wir eine Vorstellung davon, was ein *Computer* ist, wenn wir das Wort hören.
* **Wissen** ist Information, die in unser Weltmodell integriert wird. Sobald wir lernen, was ein Computer ist, entwickeln wir Ideen darüber, wie er funktioniert, wie viel er kostet und wofür er verwendet werden kann. Dieses Netzwerk von miteinander verbundenen Konzepten bildet unser Wissen.
* **Weisheit** ist eine weitere Ebene unseres Weltverständnisses und repräsentiert *Meta-Wissen*, z. B. eine Vorstellung davon, wie und wann Wissen verwendet werden sollte.

<img src="images/DIKW_Pyramid.png" width="30%"/>

*Bild [von Wikipedia](https://commons.wikimedia.org/w/index.php?curid=37705247), By Longlivetheux - Eigenes Werk, CC BY-SA 4.0*

Das Problem der **Wissensrepräsentation** besteht also darin, eine effektive Methode zu finden, Wissen in Form von Daten in einem Computer darzustellen, um es automatisch nutzbar zu machen. Dies kann als Spektrum betrachtet werden:

![Spektrum der Wissensrepräsentation](../../../../translated_images/knowledge-spectrum.b60df631852c0217e941485b79c9eee40ebd574f15f18609cec5758fcb384bf3.de.png)

> Bild von [Dmitry Soshnikov](http://soshnikov.com)

* Links gibt es sehr einfache Arten der Wissensrepräsentation, die effektiv von Computern genutzt werden können. Die einfachste ist die algorithmische Darstellung, bei der Wissen durch ein Computerprogramm repräsentiert wird. Dies ist jedoch keine flexible Methode, da Wissen in unserem Kopf oft nicht algorithmisch ist.
* Rechts gibt es Darstellungen wie natürlichen Text. Diese sind am mächtigsten, können jedoch nicht für automatisches Schließen verwendet werden.

> ✅ Überlege einen Moment, wie du Wissen in deinem Kopf darstellst und in Notizen umwandelst. Gibt es ein bestimmtes Format, das dir hilft, Informationen besser zu behalten?

## Klassifizierung von Wissensrepräsentationen in Computern

Wir können verschiedene Methoden der Wissensrepräsentation in Computern in folgende Kategorien einteilen:

* **Netzwerkrepräsentationen** basieren auf der Tatsache, dass wir ein Netzwerk von miteinander verbundenen Konzepten in unserem Kopf haben. Wir können versuchen, dieselben Netzwerke als Graphen in einem Computer nachzubilden – ein sogenanntes **semantisches Netzwerk**.

1. **Objekt-Attribut-Wert-Tripel** oder **Attribut-Wert-Paare**. Da ein Graph in einem Computer als Liste von Knoten und Kanten dargestellt werden kann, können wir ein semantisches Netzwerk durch eine Liste von Tripeln repräsentieren, die Objekte, Attribute und Werte enthalten. Zum Beispiel erstellen wir die folgenden Tripel über Programmiersprachen:

Objekt | Attribut | Wert
-------|----------|-----
Python | ist | Untyped-Language
Python | erfunden-von | Guido van Rossum
Python | Block-Syntax | Einrückung
Untyped-Language | hat nicht | Typdefinitionen

> ✅ Überlege, wie Tripel verwendet werden können, um andere Arten von Wissen darzustellen.

2. **Hierarchische Repräsentationen** betonen die Tatsache, dass wir oft eine Hierarchie von Objekten in unserem Kopf erstellen. Zum Beispiel wissen wir, dass ein Kanarienvogel ein Vogel ist und alle Vögel Flügel haben. Wir haben auch eine Vorstellung davon, welche Farbe ein Kanarienvogel normalerweise hat und wie schnell er fliegen kann.

   - **Frame-Repräsentation** basiert darauf, jedes Objekt oder jede Klasse von Objekten als **Frame** darzustellen, der **Slots** enthält. Slots haben mögliche Standardwerte, Wertbeschränkungen oder gespeicherte Prozeduren, die aufgerufen werden können, um den Wert eines Slots zu erhalten. Alle Frames bilden eine Hierarchie, ähnlich wie eine Objekt-Hierarchie in objektorientierten Programmiersprachen.
   - **Szenarien** sind spezielle Arten von Frames, die komplexe Situationen darstellen, die sich im Laufe der Zeit entwickeln können.

**Python**

Slot | Wert | Standardwert | Intervall |
-----|------|--------------|----------|
Name | Python | | |
Ist-Ein | Untyped-Language | | |
Variablen-Schreibweise | | CamelCase | |
Programmlänge | | | 5-5000 Zeilen |
Block-Syntax | Einrückung | | |

3. **Prozedurale Repräsentationen** basieren darauf, Wissen durch eine Liste von Aktionen darzustellen, die ausgeführt werden können, wenn eine bestimmte Bedingung eintritt.
   - Produktionsregeln sind Wenn-Dann-Aussagen, die es uns ermöglichen, Schlussfolgerungen zu ziehen. Zum Beispiel könnte ein Arzt eine Regel haben, die besagt: **WENN** ein Patient hohes Fieber **ODER** einen hohen C-reaktiven Proteinspiegel im Bluttest hat, **DANN** hat er eine Entzündung. Sobald wir eine der Bedingungen feststellen, können wir eine Schlussfolgerung über die Entzündung ziehen und diese dann für weitere Überlegungen verwenden.
   - Algorithmen können als eine andere Form der prozeduralen Repräsentation betrachtet werden, obwohl sie fast nie direkt in wissensbasierten Systemen verwendet werden.

4. **Logik** wurde ursprünglich von Aristoteles als Methode vorgeschlagen, universelles menschliches Wissen darzustellen.
   - Prädikatenlogik als mathematische Theorie ist zu reichhaltig, um berechenbar zu sein, daher wird normalerweise ein Teil davon verwendet, wie Horn-Klauseln in Prolog.
   - Beschreibungslogik ist eine Familie von logischen Systemen, die verwendet werden, um Hierarchien von Objekten und verteilte Wissensrepräsentationen wie das *semantische Web* darzustellen und zu verarbeiten.

## Expertensysteme

Einer der frühen Erfolge der symbolischen KI waren sogenannte **Expertensysteme** – Computersysteme, die so konzipiert waren, dass sie in einem begrenzten Problembereich als Experte agieren. Sie basierten auf einer **Wissensbasis**, die von einem oder mehreren menschlichen Experten extrahiert wurde, und enthielten eine **Schlussfolgerungsmaschine**, die darauf basierende Überlegungen anstellte.

![Menschliche Architektur](../../../../translated_images/arch-human.5d4d35f1bba3ab1cdfda96af2f10b89574eb31e9796d0e3011cd9beda1c35112.de.png) | ![Wissensbasiertes System](../../../../translated_images/arch-kbs.3ec5c150b09fa8dadc2beb0931a4983c9e2b03913a89eebcc103b5bb841b0212.de.png)
--------------------------------------------------|-----------------------------------------------
Vereinfachte Struktur des menschlichen Nervensystems | Architektur eines wissensbasierten Systems

Expertensysteme sind ähnlich aufgebaut wie das menschliche Denksystem, das **Kurzzeitgedächtnis** und **Langzeitgedächtnis** enthält. Ebenso unterscheiden wir in wissensbasierten Systemen die folgenden Komponenten:

* **Problemspeicher**: enthält das Wissen über das aktuell zu lösende Problem, z. B. die Temperatur oder den Blutdruck eines Patienten, ob er eine Entzündung hat oder nicht usw. Dieses Wissen wird auch als **statisches Wissen** bezeichnet, da es eine Momentaufnahme dessen enthält, was wir derzeit über das Problem wissen – den sogenannten *Problemzustand*.
* **Wissensbasis**: repräsentiert langfristiges Wissen über einen Problembereich. Es wird manuell von menschlichen Experten extrahiert und ändert sich nicht von einer Konsultation zur nächsten. Da es uns ermöglicht, von einem Problemzustand zum anderen zu navigieren, wird es auch als **dynamisches Wissen** bezeichnet.
* **Schlussfolgerungsmaschine**: orchestriert den gesamten Prozess der Suche im Problemzustandsraum und stellt dem Benutzer bei Bedarf Fragen. Sie ist auch dafür verantwortlich, die richtigen Regeln für jeden Zustand zu finden.

Als Beispiel betrachten wir das folgende Expertensystem zur Bestimmung eines Tieres basierend auf seinen physischen Merkmalen:

![AND-OR-Baum](../../../../translated_images/AND-OR-Tree.5592d2c70187f283703c8e9c0d69d6a786eb370f4ace67f9a7aae5ada3d260b0.de.png)

> Bild von [Dmitry Soshnikov](http://soshnikov.com)

Dieses Diagramm wird als **AND-OR-Baum** bezeichnet und ist eine grafische Darstellung einer Reihe von Produktionsregeln. Das Zeichnen eines Baums ist nützlich zu Beginn der Wissensextraktion vom Experten. Um das Wissen im Computer darzustellen, ist es jedoch praktischer, Regeln zu verwenden:

```
IF the animal eats meat
OR (animal has sharp teeth
    AND animal has claws
    AND animal has forward-looking eyes
) 
THEN the animal is a carnivore
```

Man kann erkennen, dass jede Bedingung auf der linken Seite der Regel und die Aktion im Wesentlichen Objekt-Attribut-Wert (OAV)-Tripel sind. **Arbeitsgedächtnis** enthält die Menge von OAV-Tripeln, die dem aktuell zu lösenden Problem entsprechen. Eine **Regelmaschine** sucht nach Regeln, deren Bedingungen erfüllt sind, und wendet sie an, indem sie ein weiteres Tripel zum Arbeitsgedächtnis hinzufügt.

> ✅ Erstelle deinen eigenen AND-OR-Baum zu einem Thema, das dir gefällt!

### Vorwärts- vs. Rückwärts-Schlussfolgerung

Der oben beschriebene Prozess wird als **Vorwärts-Schlussfolgerung** bezeichnet. Er beginnt mit einigen Anfangsdaten über das Problem, die im Arbeitsgedächtnis verfügbar sind, und führt dann die folgende Schlussfolgerungsschleife aus:

1. Wenn das Zielattribut im Arbeitsgedächtnis vorhanden ist – stoppe und gib das Ergebnis aus.
2. Suche nach allen Regeln, deren Bedingungen derzeit erfüllt sind – erhalte den **Konfliktset** von Regeln.
3. Führe eine **Konfliktlösung** durch – wähle eine Regel aus, die in diesem Schritt ausgeführt wird. Es gibt verschiedene Strategien zur Konfliktlösung:
   - Wähle die erste anwendbare Regel in der Wissensbasis.
   - Wähle eine zufällige Regel.
   - Wähle eine *spezifischere* Regel, d. h. diejenige, die die meisten Bedingungen auf der "linken Seite" (LHS) erfüllt.
4. Wende die ausgewählte Regel an und füge ein neues Wissenselement zum Problemzustand hinzu.
5. Wiederhole ab Schritt 1.

In einigen Fällen möchten wir jedoch mit einem leeren Wissen über das Problem beginnen und Fragen stellen, die uns helfen, zu einer Schlussfolgerung zu gelangen. Zum Beispiel führen wir bei einer medizinischen Diagnose normalerweise nicht alle medizinischen Analysen im Voraus durch, bevor wir mit der Diagnose des Patienten beginnen. Stattdessen möchten wir Analysen durchführen, wenn eine Entscheidung getroffen werden muss.

Dieser Prozess kann mit **Rückwärts-Schlussfolgerung** modelliert werden. Er wird durch das **Ziel** gesteuert – den Attributwert, den wir finden möchten:

1. Wähle alle Regeln aus, die uns den Wert eines Ziels geben können (d. h. mit dem Ziel auf der RHS ("rechte Seite")) – ein Konfliktset.
1. Wenn es keine Regeln für dieses Attribut gibt oder eine Regel besagt, dass wir den Wert vom Benutzer erfragen sollen – frage danach, andernfalls:
1. Verwende eine Konfliktlösungsstrategie, um eine Regel auszuwählen, die wir als *Hypothese* verwenden – wir versuchen, sie zu beweisen.
1. Wiederhole den Prozess rekursiv für alle Attribute auf der LHS der Regel und versuche, sie als Ziele zu beweisen.
1. Wenn der Prozess zu irgendeinem Zeitpunkt fehlschlägt – verwende eine andere Regel in Schritt 3.

> ✅ In welchen Situationen ist die Vorwärts-Schlussfolgerung besser geeignet? Und wie sieht es mit der Rückwärts-Schlussfolgerung aus?

### Implementierung von Expertensystemen

Expertensysteme können mit verschiedenen Werkzeugen implementiert werden:

* Direkte Programmierung in einer Hochsprache. Dies ist keine optimale Lösung, da der Hauptvorteil eines wissensbasierten Systems darin besteht, dass Wissen von der Schlussfolgerung getrennt ist und ein Fachexperte potenziell in der Lage sein sollte, Regeln zu schreiben, ohne die Details des Schlussfolgerungsprozesses zu verstehen.
* Verwendung eines **Expertensystem-Shells**, d. h. eines Systems, das speziell dafür entwickelt wurde, mit Wissen in einer Wissensrepräsentationssprache gefüllt zu werden.

## ✍️ Übung: Tier-Schlussfolgerung

Siehe [Animals.ipynb](https://github.com/microsoft/AI-For-Beginners/blob/main/lessons/2-Symbolic/Animals.ipynb) für ein Beispiel zur Implementierung eines Expertensystems mit Vorwärts- und Rückwärts-Schlussfolgerung.

> **Hinweis**: Dieses Beispiel ist recht einfach und gibt nur eine Vorstellung davon, wie ein Expertensystem aussieht. Sobald du anfängst, ein solches System zu erstellen, wirst du erst ab einer bestimmten Anzahl von Regeln, etwa 200+, ein *intelligentes* Verhalten bemerken. Ab einem bestimmten Punkt werden die Regeln zu komplex, um alle im Kopf zu behalten, und du wirst dich möglicherweise fragen, warum das System bestimmte Entscheidungen trifft. Ein wichtiger Vorteil von wissensbasierten Systemen ist jedoch, dass du immer genau erklären kannst, wie jede Entscheidung getroffen wurde.

## Ontologien und das semantische Web

Ende des 20. Jahrhunderts gab es eine Initiative, Wissensrepräsentation zu nutzen, um Internetressourcen zu annotieren, sodass es möglich wäre, Ressourcen zu finden, die sehr spezifischen Anfragen entsprechen. Diese Bewegung wurde **Semantisches Web** genannt und basierte auf mehreren Konzepten:

- Eine spezielle Wissensrepräsentation basierend auf **[Beschreibungslogiken](https://en.wikipedia.org/wiki/Description_logic)** (DL). Sie ähnelt der Frame-Wissensrepräsentation, da sie eine Hierarchie von Objekten mit Eigenschaften aufbaut, aber sie hat formale logische Semantik und Schlussfolgerung. Es gibt eine ganze Familie von DLs, die zwischen Ausdruckskraft und algorithmischer Komplexität der Schlussfolgerung balancieren.
- Verteilte Wissensrepräsentation, bei der alle Konzepte durch einen globalen URI-Identifikator repräsentiert werden, was es ermöglicht, Wissenshierarchien zu erstellen, die das Internet umfassen.
- Eine Familie von XML-basierten Sprachen zur Wissensbeschreibung: RDF (Resource Description Framework), RDFS (RDF Schema), OWL (Ontology Web Language).

Ein Kernkonzept im Semantic Web ist das Konzept der **Ontologie**. Es bezeichnet eine explizite Spezifikation eines Problemfeldes mithilfe einer formalen Wissensrepräsentation. Die einfachste Ontologie kann einfach eine Hierarchie von Objekten in einem Problemfeld sein, aber komplexere Ontologien enthalten Regeln, die für Schlussfolgerungen verwendet werden können.

Im Semantic Web basieren alle Darstellungen auf Triplets. Jedes Objekt und jede Beziehung werden eindeutig durch eine URI identifiziert. Zum Beispiel, wenn wir die Tatsache ausdrücken möchten, dass dieses AI Curriculum von Dmitry Soshnikov am 1. Januar 2022 entwickelt wurde, könnten wir die folgenden Triplets verwenden:

<img src="images/triplet.png" width="30%"/>

```
http://github.com/microsoft/ai-for-beginners http://www.example.com/terms/creation-date “Jan 13, 2007”
http://github.com/microsoft/ai-for-beginners http://purl.org/dc/elements/1.1/creator http://soshnikov.com
```

> ✅ Hier sind `http://www.example.com/terms/creation-date` und `http://purl.org/dc/elements/1.1/creator` einige bekannte und allgemein akzeptierte URIs, um die Konzepte *Ersteller* und *Erstellungsdatum* auszudrücken.

In einem komplexeren Fall, wenn wir eine Liste von Erstellern definieren möchten, können wir einige in RDF definierte Datenstrukturen verwenden.

<img src="images/triplet-complex.png" width="40%"/>

> Diagramme oben von [Dmitry Soshnikov](http://soshnikov.com)

Der Fortschritt beim Aufbau des Semantic Web wurde durch den Erfolg von Suchmaschinen und Techniken der natürlichen Sprachverarbeitung etwas verlangsamt, die es ermöglichen, strukturierte Daten aus Text zu extrahieren. Dennoch gibt es in einigen Bereichen weiterhin bedeutende Bemühungen, Ontologien und Wissensbasen zu pflegen. Einige bemerkenswerte Projekte:

* [WikiData](https://wikidata.org/) ist eine Sammlung maschinenlesbarer Wissensbasen, die mit Wikipedia verbunden sind. Die meisten Daten werden aus den Wikipedia *InfoBoxes* extrahiert, strukturierten Inhalten innerhalb der Wikipedia-Seiten. Sie können [WikiData abfragen](https://query.wikidata.org/) mit SPARQL, einer speziellen Abfragesprache für das Semantic Web. Hier ist eine Beispielabfrage, die die beliebtesten Augenfarben unter Menschen anzeigt:

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

* [DBpedia](https://www.dbpedia.org/) ist ein weiteres Projekt, das ähnlich wie WikiData funktioniert.

> ✅ Wenn Sie mit dem Aufbau eigener Ontologien oder dem Öffnen bestehender experimentieren möchten, gibt es einen großartigen visuellen Ontologie-Editor namens [Protégé](https://protege.stanford.edu/). Laden Sie ihn herunter oder nutzen Sie ihn online.

<img src="images/protege.png" width="70%"/>

*Web Protégé Editor geöffnet mit der Romanov-Familienontologie. Screenshot von Dmitry Soshnikov*

## ✍️ Übung: Eine Familienontologie

Sehen Sie sich [FamilyOntology.ipynb](https://github.com/Ezana135/AI-For-Beginners/blob/main/lessons/2-Symbolic/FamilyOntology.ipynb) an, um ein Beispiel für die Verwendung von Semantic-Web-Techniken zur Analyse von Familienbeziehungen zu sehen. Wir werden einen Familienstammbaum im üblichen GEDCOM-Format und eine Ontologie von Familienbeziehungen verwenden, um einen Graphen aller Familienbeziehungen für eine gegebene Gruppe von Individuen zu erstellen.

## Microsoft Concept Graph

In den meisten Fällen werden Ontologien sorgfältig von Hand erstellt. Es ist jedoch auch möglich, Ontologien aus unstrukturierten Daten zu **extrahieren**, beispielsweise aus Texten in natürlicher Sprache.

Ein solcher Versuch wurde von Microsoft Research unternommen und führte zum [Microsoft Concept Graph](https://blogs.microsoft.com/ai/microsoft-researchers-release-graph-that-helps-machines-conceptualize/?WT.mc_id=academic-77998-cacaste).

Es handelt sich um eine große Sammlung von Entitäten, die mithilfe der `is-a`-Vererbungsbeziehung gruppiert sind. Damit können Fragen wie "Was ist Microsoft?" beantwortet werden – die Antwort könnte etwa lauten: "Ein Unternehmen mit einer Wahrscheinlichkeit von 0,87 und eine Marke mit einer Wahrscheinlichkeit von 0,75".

Der Graph ist entweder als REST-API oder als große herunterladbare Textdatei verfügbar, die alle Entitätspaare auflistet.

## ✍️ Übung: Ein Concept Graph

Probieren Sie das Notebook [MSConceptGraph.ipynb](https://github.com/microsoft/AI-For-Beginners/blob/main/lessons/2-Symbolic/MSConceptGraph.ipynb) aus, um zu sehen, wie wir den Microsoft Concept Graph verwenden können, um Nachrichtenartikel in verschiedene Kategorien zu gruppieren.

## Fazit

Heutzutage wird KI oft als Synonym für *Maschinelles Lernen* oder *Neuronale Netze* betrachtet. Ein Mensch zeigt jedoch auch explizites Denken, etwas, das derzeit von neuronalen Netzen nicht behandelt wird. In realen Projekten wird explizites Denken weiterhin verwendet, um Aufgaben zu erfüllen, die Erklärungen erfordern oder die Fähigkeit, das Verhalten des Systems kontrolliert zu ändern.

## 🚀 Herausforderung

Im Family Ontology Notebook, das mit dieser Lektion verbunden ist, gibt es die Möglichkeit, mit anderen Familienbeziehungen zu experimentieren. Versuchen Sie, neue Verbindungen zwischen Personen im Familienstammbaum zu entdecken.

## [Quiz nach der Vorlesung](https://ff-quizzes.netlify.app/en/ai/quiz/4)

## Überprüfung & Selbststudium

Recherchieren Sie im Internet, um Bereiche zu entdecken, in denen Menschen versucht haben, Wissen zu quantifizieren und zu kodifizieren. Schauen Sie sich Bloom's Taxonomy an und gehen Sie in der Geschichte zurück, um zu erfahren, wie Menschen versucht haben, ihre Welt zu verstehen. Erkunden Sie die Arbeit von Linnaeus zur Erstellung einer Taxonomie von Organismen und beobachten Sie, wie Dmitri Mendeleev eine Methode zur Beschreibung und Gruppierung chemischer Elemente entwickelt hat. Welche anderen interessanten Beispiele können Sie finden?

**Aufgabe**: [Erstellen Sie eine Ontologie](assignment.md)

---

