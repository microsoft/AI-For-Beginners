# Wissensdarstellung und Expertensysteme

![Zusammenfassung des Inhalts der symbolischen KI](../../../../translated_images/ai-symbolic.715a30cb610411a6964d2e2f23f24364cb338a07cb4844c1f97084d366e586c3.de.png)

> Sketchnote von [Tomomi Imura](https://twitter.com/girlie_mac)

Die Suche nach künstlicher Intelligenz basiert auf dem Streben nach Wissen, um die Welt ähnlich wie Menschen zu verstehen. Aber wie geht man dabei vor?

## [Vorlesungsquiz](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/102)

In den frühen Tagen der KI war der Top-Down-Ansatz zur Schaffung intelligenter Systeme (der im vorherigen Kapitel besprochen wurde) populär. Die Idee war, das Wissen von Menschen in eine maschinenlesbare Form zu extrahieren und es dann zur automatischen Problemlösung zu verwenden. Dieser Ansatz basierte auf zwei großen Ideen:

* Wissensdarstellung
* Schlussfolgerung

## Wissensdarstellung

Eines der wichtigen Konzepte in der symbolischen KI ist **Wissen**. Es ist wichtig, Wissen von *Information* oder *Daten* zu unterscheiden. Zum Beispiel kann man sagen, dass Bücher Wissen enthalten, weil man Bücher studieren und ein Experte werden kann. Was Bücher jedoch enthalten, wird tatsächlich als *Daten* bezeichnet, und durch das Lesen von Büchern und die Integration dieser Daten in unser Weltmodell wandeln wir diese Daten in Wissen um.

> ✅ **Wissen** ist etwas, das in unserem Kopf enthalten ist und unser Verständnis der Welt repräsentiert. Es wird durch einen aktiven **Lernprozess** erlangt, der die Informationen, die wir erhalten, in unser aktives Weltmodell integriert.

Meistens definieren wir Wissen nicht streng, sondern stellen es in Beziehung zu anderen verwandten Konzepten mithilfe der [DIKW-Pyramide](https://en.wikipedia.org/wiki/DIKW_pyramid). Sie enthält die folgenden Konzepte:

* **Daten** sind etwas, das in physischen Medien dargestellt wird, wie geschriebenem Text oder gesprochenen Worten. Daten existieren unabhängig von Menschen und können zwischen Personen ausgetauscht werden.
* **Information** ist, wie wir Daten in unserem Kopf interpretieren. Zum Beispiel, wenn wir das Wort *Computer* hören, haben wir ein gewisses Verständnis davon, was es ist.
* **Wissen** ist Information, die in unser Weltmodell integriert wird. Zum Beispiel, sobald wir lernen, was ein Computer ist, beginnen wir, einige Ideen darüber zu haben, wie er funktioniert, wie viel er kostet und wofür er verwendet werden kann. Dieses Netzwerk von miteinander verbundenen Konzepten bildet unser Wissen.
* **Weisheit** ist eine weitere Ebene unseres Verständnisses der Welt und repräsentiert *Meta-Wissen*, z.B. eine Vorstellung davon, wie und wann das Wissen verwendet werden sollte.

<img src="images/DIKW_Pyramid.png" width="30%"/>

*Bild [von Wikipedia](https://commons.wikimedia.org/w/index.php?curid=37705247), Von Longlivetheux - Eigenes Werk, CC BY-SA 4.0*

Das Problem der **Wissensdarstellung** besteht also darin, eine effektive Möglichkeit zu finden, Wissen in einem Computer in Form von Daten darzustellen, um es automatisch nutzbar zu machen. Dies kann als Spektrum betrachtet werden:

![Spektrum der Wissensdarstellung](../../../../translated_images/knowledge-spectrum.b60df631852c0217e941485b79c9eee40ebd574f15f18609cec5758fcb384bf3.de.png)

> Bild von [Dmitry Soshnikov](http://soshnikov.com)

* Links befinden sich sehr einfache Arten von Wissensdarstellungen, die effektiv von Computern genutzt werden können. Die einfachste ist algorithmisch, wenn Wissen durch ein Computerprogramm dargestellt wird. Dies ist jedoch nicht der beste Weg, Wissen darzustellen, da es nicht flexibel ist. Wissen in unserem Kopf ist oft nicht-algorithmisch.
* Rechts gibt es Darstellungen wie natürlichen Text. Es ist die mächtigste Form, kann jedoch nicht für automatisches Schließen verwendet werden.

> ✅ Denke einen Moment darüber nach, wie du Wissen in deinem Kopf darstellst und es in Notizen umwandelst. Gibt es ein bestimmtes Format, das dir hilft, es zu behalten?

## Klassifizierung von Computer-Wissensdarstellungen

Wir können verschiedene Methoden zur Wissensdarstellung im Computer in die folgenden Kategorien einteilen:

* **Netzwerkdarstellungen** basieren auf der Tatsache, dass wir ein Netzwerk von miteinander verbundenen Konzepten in unserem Kopf haben. Wir können versuchen, die gleichen Netzwerke als Graphen in einem Computer zu reproduzieren - ein sogenanntes **semantisches Netzwerk**.

1. **Objekt-Attribut-Wert-Triple** oder **Attribut-Wert-Paare**. Da ein Graph in einem Computer als Liste von Knoten und Kanten dargestellt werden kann, können wir ein semantisches Netzwerk durch eine Liste von Tripeln darstellen, die Objekte, Attribute und Werte enthalten. Zum Beispiel bauen wir die folgenden Tripel über Programmiersprachen:

Objekt | Attribut | Wert
-------|-----------|------
Python | ist | Ungetypte-Sprache
Python | erfunden-von | Guido van Rossum
Python | Block-Syntax | Einrückung
Ungetypte-Sprache | hat-keine | Typdefinitionen

> ✅ Überlege, wie Tripel verwendet werden können, um andere Arten von Wissen darzustellen.

2. **Hierarchische Darstellungen** betonen die Tatsache, dass wir oft eine Hierarchie von Objekten in unserem Kopf erstellen. Zum Beispiel wissen wir, dass ein Kanarienvogel ein Vogel ist und alle Vögel Flügel haben. Wir haben auch eine Vorstellung davon, welche Farbe ein Kanarienvogel normalerweise hat und wie schnell er fliegen kann.

   - **Frame-Darstellung** basiert darauf, jedes Objekt oder jede Klasse von Objekten als **Frame** darzustellen, der **Slots** enthält. Slots haben mögliche Standardwerte, Wertbeschränkungen oder gespeicherte Prozeduren, die aufgerufen werden können, um den Wert eines Slots zu erhalten. Alle Frames bilden eine Hierarchie, die einer Objekt-Hierarchie in objektorientierten Programmiersprachen ähnelt.
   - **Szenarien** sind spezielle Arten von Frames, die komplexe Situationen darstellen, die sich im Laufe der Zeit entfalten können.

**Python**

Slot | Wert | Standardwert | Intervall |
-----|-------|---------------|----------|
Name | Python | | |
Ist-Ein | Ungetypte-Sprache | | |
Variablenfall | | CamelCase | |
Programmlänge | | | 5-5000 Zeilen |
Blocksyntax | Einrückung | | |

3. **Prozedurale Darstellungen** basieren auf der Darstellung von Wissen durch eine Liste von Aktionen, die ausgeführt werden können, wenn eine bestimmte Bedingung eintritt.
   - Produktionsregeln sind Wenn-Dann-Aussagen, die es uns ermöglichen, Schlussfolgerungen zu ziehen. Zum Beispiel kann ein Arzt eine Regel haben, die besagt, dass **WENN** ein Patient Fieber hat **ODER** einen hohen Wert für C-reaktives Protein im Bluttest hat **DANN** hat er eine Entzündung. Sobald wir eine der Bedingungen treffen, können wir eine Schlussfolgerung über die Entzündung ziehen und diese dann in weiteren Überlegungen verwenden.
   - Algorithmen können als eine andere Form der prozeduralen Darstellung betrachtet werden, obwohl sie fast nie direkt in wissensbasierten Systemen verwendet werden.

4. **Logik** wurde ursprünglich von Aristoteles als eine Möglichkeit vorgeschlagen, universelles menschliches Wissen darzustellen.
   - Prädikatenlogik als mathematische Theorie ist zu reich, um berechenbar zu sein, daher wird normalerweise eine Teilmenge davon verwendet, wie Horn-Klauseln, die in Prolog verwendet werden.
   - Beschreibende Logik ist eine Familie von logischen Systemen, die verwendet werden, um Hierarchien von Objekten in verteilten Wissensdarstellungen wie dem *semantischen Web* darzustellen und darüber nachzudenken.

## Expertensysteme

Einer der frühen Erfolge der symbolischen KI waren die sogenannten **Expertensysteme** - Computersysteme, die dazu entworfen wurden, als Experte in einem bestimmten begrenzten Problembereich zu agieren. Sie basierten auf einer **Wissensbasis**, die aus einem oder mehreren menschlichen Experten extrahiert wurde, und sie enthielten eine **Schlussfolgerungsmaschine**, die darauf basierend einige Überlegungen anstellte.

![Menschliche Architektur](../../../../translated_images/arch-human.5d4d35f1bba3ab1cdfda96af2f10b89574eb31e9796d0e3011cd9beda1c35112.de.png) | ![Wissensbasiertes System](../../../../translated_images/arch-kbs.3ec5c150b09fa8dadc2beb0931a4983c9e2b03913a89eebcc103b5bb841b0212.de.png)
---------------------------------------------|------------------------------------------------
Vereinfachte Struktur eines menschlichen neuronalen Systems | Architektur eines wissensbasierten Systems

Expertensysteme sind aufgebaut wie das menschliche Denk-System, das **Kurzzeitgedächtnis** und **Langzeitgedächtnis** enthält. Ähnlich unterscheiden wir in wissensbasierten Systemen die folgenden Komponenten:

* **Problemerinnerung**: enthält das Wissen über das aktuell zu lösende Problem, z.B. die Temperatur oder den Blutdruck eines Patienten, ob er eine Entzündung hat oder nicht usw. Dieses Wissen wird auch als **statisches Wissen** bezeichnet, da es einen Schnappschuss dessen enthält, was wir derzeit über das Problem wissen - den sogenannten *Problemzustand*.
* **Wissensbasis**: repräsentiert langfristiges Wissen über ein Problembereich. Es wird manuell von menschlichen Experten extrahiert und ändert sich nicht von Konsultation zu Konsultation. Da es uns ermöglicht, von einem Problemzustand zu einem anderen zu navigieren, wird es auch als **dynamisches Wissen** bezeichnet.
* **Schlussfolgerungsmaschine**: orchestriert den gesamten Prozess der Suche im Problembereich und stellt dem Benutzer bei Bedarf Fragen. Sie ist auch dafür verantwortlich, die richtigen Regeln zu finden, die auf jeden Zustand angewendet werden sollen.

Als Beispiel betrachten wir folgendes Expertensystem zur Bestimmung eines Tieres basierend auf seinen physischen Eigenschaften:

![AND-OR-Baum](../../../../translated_images/AND-OR-Tree.5592d2c70187f283703c8e9c0d69d6a786eb370f4ace67f9a7aae5ada3d260b0.de.png)

> Bild von [Dmitry Soshnikov](http://soshnikov.com)

Dieses Diagramm wird als **AND-OR-Baum** bezeichnet und ist eine grafische Darstellung einer Menge von Produktionsregeln. Das Zeichnen eines Baumes ist zu Beginn der Wissensgewinnung von Nutzen. Um das Wissen im Computer darzustellen, ist es bequemer, Regeln zu verwenden:

```
IF the animal eats meat
OR (animal has sharp teeth
    AND animal has claws
    AND animal has forward-looking eyes
) 
THEN the animal is a carnivore
```

Du wirst feststellen, dass jede Bedingung auf der linken Seite der Regel und die Aktion im Wesentlichen Objekt-Attribut-Wert (OAV) Tripel sind. **Arbeitsgedächtnis** enthält die Menge der OAV-Triple, die dem aktuell zu lösenden Problem entsprechen. Eine **Regelmaschine** sucht nach Regeln, für die eine Bedingung erfüllt ist, und wendet sie an, indem sie ein weiteres Tripel zum Arbeitsgedächtnis hinzufügt.

> ✅ Schreibe deinen eigenen AND-OR-Baum zu einem Thema, das dir gefällt!

### Vorwärts- vs. Rückwärtsinferenz

Der oben beschriebene Prozess wird als **Vorwärtsinferenz** bezeichnet. Er beginnt mit einigen Anfangsdaten über das Problem, die im Arbeitsgedächtnis verfügbar sind, und führt dann die folgende Schlussfolgerungsschleife aus:

1. Wenn das Zielattribut im Arbeitsgedächtnis vorhanden ist - stoppe und gib das Ergebnis an
2. Suche nach allen Regeln, deren Bedingung derzeit erfüllt ist - erhalte die **Konfliktmenge** von Regeln.
3. Führe die **Konfliktlösung** durch - wähle eine Regel aus, die in diesem Schritt ausgeführt wird. Es könnte verschiedene Strategien zur Konfliktlösung geben:
   - Wähle die erste anwendbare Regel in der Wissensbasis
   - Wähle eine zufällige Regel
   - Wähle eine *spezifischere* Regel, d.h. diejenige, die die meisten Bedingungen auf der "linken Seite" (LHS) erfüllt
4. Wende die ausgewählte Regel an und füge neues Wissen in den Problemzustand ein
5. Wiederhole ab Schritt 1.

In einigen Fällen möchten wir jedoch vielleicht mit einem leeren Wissen über das Problem beginnen und Fragen stellen, die uns helfen, zu einer Schlussfolgerung zu gelangen. Zum Beispiel führen wir bei einer medizinischen Diagnose normalerweise nicht alle medizinischen Analysen im Voraus durch, bevor wir mit der Diagnose des Patienten beginnen. Wir möchten vielmehr Analysen durchführen, wenn eine Entscheidung getroffen werden muss.

Dieser Prozess kann mit **Rückwärtsinferenz** modelliert werden. Er wird durch das **Ziel** gesteuert - den Attributwert, den wir zu finden versuchen:

1. Wähle alle Regeln aus, die uns den Wert eines Ziels geben können (d.h. mit dem Ziel auf der RHS ("rechten Seite")) - eine Konfliktmenge
1. Wenn es keine Regeln für dieses Attribut gibt oder eine Regel besagt, dass wir den Wert vom Benutzer abfragen sollten - frage danach, andernfalls:
1. Verwende die Konfliktlösungsstrategie, um eine Regel auszuwählen, die wir als *Hypothese* verwenden werden - wir werden versuchen, sie zu beweisen
1. Wiederhole den Prozess rekursiv für alle Attribute auf der LHS der Regel und versuche, sie als Ziele zu beweisen
1. Wenn der Prozess an irgendeinem Punkt fehlschlägt - verwende eine andere Regel in Schritt 3.

> ✅ In welchen Situationen ist Vorwärtsinferenz geeigneter? Und Rückwärtsinferenz?

### Implementierung von Expertensystemen

Expertensysteme können mit verschiedenen Werkzeugen implementiert werden:

* Direkt in einer Hochsprache programmieren. Das ist nicht die beste Idee, da der Hauptvorteil eines wissensbasierten Systems darin besteht, dass Wissen von der Schlussfolgerung getrennt ist, und potenziell sollte ein Experte im Problembereich in der Lage sein, Regeln zu schreiben, ohne die Details des Schlussfolgerungsprozesses zu verstehen.
* Verwendung einer **Expertensystem-Schale**, d.h. eines Systems, das speziell dafür entworfen wurde, mit Wissen unter Verwendung einer bestimmten Wissensdarstellungssprache befüllt zu werden.

## ✍️ Übung: Tierinferenz

Siehe [Animals.ipynb](https://github.com/microsoft/AI-For-Beginners/blob/main/lessons/2-Symbolic/Animals.ipynb) für ein Beispiel zur Implementierung eines Expertensystems für Vorwärts- und Rückwärtsinferenz.

> **Hinweis**: Dieses Beispiel ist recht einfach und vermittelt nur eine Vorstellung davon, wie ein Expertensystem aussieht. Sobald du anfängst, ein solches System zu erstellen, wirst du erst dann einige *intelligente* Verhaltensweisen bemerken, wenn du eine bestimmte Anzahl von Regeln erreichst, etwa 200+. Irgendwann werden die Regeln zu komplex, um alle im Kopf zu behalten, und an diesem Punkt wirst du dich fragen, warum ein System bestimmte Entscheidungen trifft. Dennoch ist die wichtige Eigenschaft wissensbasierter Systeme, dass du immer genau *erklären* kannst, wie eine der Entscheidungen getroffen wurde.

## Ontologien und das semantische Web

Am Ende des 20. Jahrhunderts gab es eine Initiative, Wissensdarstellung zu verwenden, um Internetressourcen zu annotieren, sodass es möglich wäre, Ressourcen zu finden, die sehr spezifischen Anfragen entsprechen. Diese Bewegung wurde als **semantisches Web** bezeichnet und basierte auf mehreren Konzepten:

- Eine spezielle Wissensdarstellung, die auf **[Beschreibungslogiken](https://en.wikipedia.org/wiki/Description_logic)** (DL) basiert. Sie ähnelt der Frame-Wissensdarstellung, da sie eine Hierarchie von Objekten mit Eigenschaften aufbaut, jedoch formale logische Semantik und Schlussfolgerung hat. Es gibt eine ganze Familie von DLs, die zwischen Ausdruckskraft und algorithmischer Komplexität der Schlussfolgerung balancieren.
- Verteilte Wissensdarstellung, bei der alle Konzepte durch einen globalen URI-Identifikator dargestellt werden, was es ermöglicht, Wissenshierarchien zu erstellen, die sich über das Internet erstrecken.
- Eine Familie von XML-basierten Sprachen zur Wissensbeschreibung: RDF (Resource Description Framework), RDFS (RDF Schema), OWL (Ontology Web Language).

Ein zentrales Konzept im semantischen Web ist das Konzept der **Ontologie**. Es bezieht sich auf eine explizite Spezifikation eines Problembereichs unter Verwendung einer formalen Wissensdarstellung. Die einfachste Ontologie kann einfach eine Hierarchie von Objekten in einem Problembereich sein, aber komplexere Ontologien werden Regeln enthalten, die für Schlussfolgerungen verwendet werden können.

Im semantischen Web basieren alle Darstellungen auf Tripeln. Jedes Objekt und jede Relation sind eindeutig durch die URI identifiziert. Zum Beispiel, wenn wir den Fakt angeben wollen, dass dieser KI-Lehrplan von Dmitry Soshnikov am 1. Januar 2022 entwickelt wurde - hier sind die Tripel, die wir verwenden können:

<img src="images/triplet.png" width="30%"/>

```
http://github.com/microsoft/ai-for-beginners http://www.example.com/terms/creation-date “Jan 13, 2007”
http://github.com/microsoft/ai-for-beginners http://purl.org/dc/elements/1.1/creator http://soshnikov.com
```

> ✅ Hier `http://www.example.com/terms/creation-date` and `http://purl.org/dc/elements/1.1/creator` sind einige bekannte und allgemein akzeptierte URIs, um die Konzepte von *Schöpfer* und *Erstellungsdatum* auszudrücken.

In einem komplexeren Fall, wenn wir eine Liste von Schöpfern definieren möchten, können wir einige in RDF definierte Datenstrukturen verwenden.

<img src="images/triplet-complex.png" width="40%"/>

> Diagramme oben von [Dmitry Soshnikov](http://soshnikov.com)

Der Fortschritt beim Aufbau des semantischen Webs wurde durch den Erfolg von Suchmaschinen und Techniken der natürlichen Sprachverarbeitung, die es ermöglichen, strukturierte Daten aus Texten zu extrahieren, etwas verlangsamt. Dennoch gibt es in einigen Bereichen weiterhin erhebliche Bemühungen, Ontologien und Wissensbasen zu pflegen. Einige Projekte, die erwähnenswert sind:

* [WikiData](https://wikidata.org/) ist eine Sammlung von maschinenlesbaren Wissensbasen, die mit Wikipedia verbunden sind. Die meisten Daten stammen aus den Wikipedia *InfoBoxen*, Stücken strukturierten Inhalts innerhalb von Wikipedia-Seiten. Du kannst [abfragen](https://query.wikidata.org/) wikidata in SPARQL, einer speziellen Abfragesprache für das semantische Web. Hier ist eine Beispielabfrage, die die beliebtesten Augenfarben unter Menschen anzeigt:

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

* [DBpedia](https://www.dbpedia.org/) ist ein weiterer Versuch, ähnlich wie WikiData.

> ✅ Wenn du mit dem Erstellen deiner eigenen Ontologien oder dem Öffnen bestehender experimentieren möchtest, gibt es einen großartigen visuellen Ontologie-Editor namens [Protégé](https://protege.stanford.edu/). Lade ihn herunter oder benutze ihn online.

<img src="images/protege.png" width="70%"/>



**Haftungsausschluss**:  
Dieses Dokument wurde mit maschinellen KI-Übersetzungsdiensten übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner ursprünglichen Sprache sollte als die maßgebliche Quelle betrachtet werden. Für wichtige Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die aus der Verwendung dieser Übersetzung entstehen.