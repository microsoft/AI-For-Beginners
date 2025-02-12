# Multi-Agent-Systeme

Eine der möglichen Wege, Intelligenz zu erreichen, ist der sogenannte **emergente** (oder **synergetische**) Ansatz, der darauf basiert, dass das kombinierte Verhalten vieler relativ einfacher Agenten zu einem insgesamt komplexeren (oder intelligenten) Verhalten des Systems als Ganzes führen kann. Theoretisch beruht dies auf den Prinzipien der [kollektiven Intelligenz](https://de.wikipedia.org/wiki/Kollektive_Intelligenz), [Emergentismus](https://de.wikipedia.org/wiki/Emergentismus) und [evolutionären Kybernetik](https://de.wikipedia.org/wiki/Evolution%C3%A4re_Kybernetik), die besagen, dass höherstufige Systeme einen gewissen Mehrwert gewinnen, wenn sie richtig aus niederstufigen Systemen kombiniert werden (sogenanntes *Prinzip des Metasystemübergangs*).

## [Vorlesungsquiz](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/123)

Der Bereich der **Multi-Agent-Systeme** hat sich in den 1990er Jahren als Reaktion auf das Wachstum des Internets und verteilter Systeme in der KI entwickelt. Eines der klassischen KI-Lehrbücher, [Künstliche Intelligenz: Ein moderner Ansatz](https://de.wikipedia.org/wiki/K%C3%BCnstliche_Intelligenz:_Ein_moderner_Ansatz), konzentriert sich auf die Sichtweise der klassischen KI aus der Perspektive von Multi-Agent-Systemen.

Zentral für den Multi-Agenten-Ansatz ist der Begriff des **Agenten** - eine Entität, die in einer bestimmten **Umgebung** lebt, die sie wahrnehmen und beeinflussen kann. Dies ist eine sehr breite Definition, und es könnte viele verschiedene Arten und Klassifikationen von Agenten geben:

* Nach ihrer Fähigkeit zu schlussfolgern:
   - **Reaktive** Agenten haben in der Regel ein einfaches Anfrage-Antwort-Verhalten
   - **Deliberative** Agenten verwenden eine Art logisches Denken und/oder Planungsfähigkeiten
* Nach dem Ort, an dem der Agent seinen Code ausführt:
   - **Statische** Agenten arbeiten auf einem dedizierten Netzwerk-Knoten
   - **Mobile** Agenten können ihren Code zwischen Netzwerk-Knoten bewegen
* Nach ihrem Verhalten:
   - **Passive Agenten** haben keine spezifischen Ziele. Solche Agenten können auf externe Reize reagieren, initiieren jedoch selbst keine Aktionen.
   - **Aktive Agenten** verfolgen bestimmte Ziele
   - **Kognitive Agenten** beinhalten komplexe Planung und Schlussfolgerungen

Multi-Agent-Systeme werden heutzutage in einer Vielzahl von Anwendungen eingesetzt:

* In Spielen verwenden viele Nicht-Spieler-Charaktere eine Art von KI und können als intelligente Agenten betrachtet werden.
* In der Videoproduktion wird das Rendern komplexer 3D-Szenen, die Menschenmengen beinhalten, typischerweise durch Multi-Agenten-Simulationen durchgeführt.
* In der Systemmodellierung wird der Multi-Agenten-Ansatz verwendet, um das Verhalten eines komplexen Modells zu simulieren. Zum Beispiel wurde der Multi-Agenten-Ansatz erfolgreich genutzt, um die Ausbreitung der COVID-19-Krankheit weltweit vorherzusagen. Ein ähnlicher Ansatz kann verwendet werden, um den Verkehr in der Stadt zu modellieren und zu sehen, wie er auf Änderungen der Verkehrsregeln reagiert.
* In komplexen Automatisierungssystemen kann jedes Gerät als unabhängiger Agent fungieren, was das gesamte System weniger monolithisch und robuster macht.

Wir werden nicht viel Zeit damit verbringen, tief in Multi-Agent-Systeme einzutauchen, sondern ein Beispiel für **Multi-Agenten-Modellierung** betrachten.

## NetLogo

[NetLogo](https://ccl.northwestern.edu/netlogo/) ist eine Multi-Agenten-Modellierungsumgebung, die auf einer modifizierten Version der [Logo](https://de.wikipedia.org/wiki/Logo_(Programmiersprache))-Programmiersprache basiert. Diese Sprache wurde entwickelt, um Programmierkonzepte Kindern beizubringen, und ermöglicht es Ihnen, einen Agenten namens **Schildkröte** zu steuern, der sich bewegen und dabei eine Spur hinterlassen kann. Dies ermöglicht die Erstellung komplexer geometrischer Figuren, was eine sehr visuelle Art ist, das Verhalten eines Agenten zu verstehen.

In NetLogo können wir viele Schildkröten erstellen, indem wir den `create-turtles`-Befehl verwenden. Wir können dann alle Schildkröten anweisen, einige Aktionen auszuführen (im folgenden Beispiel - 10 Punkte nach vorne):

```
create-turtles 10
ask turtles [
  forward 10
]
```

Natürlich ist es nicht interessant, wenn alle Schildkröten dasselbe tun, also können wir `ask` groups of turtles, eg. those who are in the vicinity of a certain point. We can also create turtles of different *breeds* using `breed [cats cat]` command. Here `cat` ist der Name einer Rasse, und wir müssen sowohl das Singular- als auch das Pluralwort angeben, da verschiedene Befehle unterschiedliche Formen zur Klarheit verwenden.

> ✅ Wir werden nicht in die Sprache NetLogo selbst eintauchen - Sie können die brillante [Interaktive NetLogo-Wörterbuch für Anfänger](https://ccl.northwestern.edu/netlogo/bind/) Ressource besuchen, wenn Sie mehr lernen möchten.

Sie können [NetLogo herunterladen](https://ccl.northwestern.edu/netlogo/download.shtml) und installieren, um es auszuprobieren.

### Modelle-Bibliothek

Eine großartige Sache an NetLogo ist, dass es eine Bibliothek von funktionierenden Modellen enthält, die Sie ausprobieren können. Gehen Sie zu **Datei → Modelle-Bibliothek**, und Sie haben viele Kategorien von Modellen zur Auswahl.

<img alt="NetLogo Modelle-Bibliothek" src="images/NetLogo-ModelLib.png" width="60%"/>

> Ein Screenshot der Modelle-Bibliothek von Dmitry Soshnikov

Sie können eines der Modelle öffnen, zum Beispiel **Biologie → Vogelschwarm**.

### Hauptprinzipien

Nach dem Öffnen des Modells gelangen Sie zum Hauptbildschirm von NetLogo. Hier ist ein Beispielmodell, das die Population von Wölfen und Schafen beschreibt, bei begrenzten Ressourcen (Gras).

![NetLogo Hauptbildschirm](../../../../../translated_images/NetLogo-Main.32653711ec1a01b3cab22ec0b148e64193d0b979b055285bef329d5e3d6958c5.de.png)

> Screenshot von Dmitry Soshnikov

Auf diesem Bildschirm sehen Sie:

* Den Abschnitt **Schnittstelle**, der enthält:
  - Das Hauptfeld, in dem alle Agenten leben
  - Verschiedene Steuerungen: Tasten, Schieberegler usw.
  - Grafiken, die Sie verwenden können, um Parameter der Simulation anzuzeigen
* Den **Code**-Tab, der den Editor enthält, in dem Sie NetLogo-Programme eingeben können

In den meisten Fällen hätte die Schnittstelle eine **Setup**-Taste, die den Simulationszustand initialisiert, und eine **Go**-Taste, die die Ausführung startet. Diese werden von den entsprechenden Handlern im Code behandelt, die so aussehen:

```
to go [
...
]
```

Die Welt von NetLogo besteht aus den folgenden Objekten:

* **Agenten** (Schildkröten), die sich über das Feld bewegen und etwas tun können. Sie befehlen Agenten mit `ask turtles [...]` syntax, and the code in brackets is executed by all agents in *turtle mode*.
* **Patches** are square areas of the field, on which agents live. You can refer to all agents on the same patch, or you can change patch colors and some other properties. You can also `ask patches`, um etwas zu tun.
* **Beobachter** ist ein einzigartiger Agent, der die Welt kontrolliert. Alle Button-Handler werden im *Beobachtungsmodus* ausgeführt.

> ✅ Die Schönheit einer Multi-Agenten-Umgebung besteht darin, dass der Code, der im Schildkrötenmodus oder im Patchmodus ausgeführt wird, gleichzeitig von allen Agenten parallel ausgeführt wird. Durch das Schreiben eines kleinen Codes und das Programmieren des Verhaltens des einzelnen Agenten können Sie komplexes Verhalten des Simulationssystems als Ganzes erzeugen.

### Vogelschwarm

Als Beispiel für multi-agenten Verhalten betrachten wir **[Vogelschwarm](https://de.wikipedia.org/wiki/Vogelschwarm_(Verhalten))**. Vogelschwarm ist ein komplexes Muster, das dem ähnelt, wie Vogelschwärme fliegen. Wenn man ihnen beim Fliegen zusieht, könnte man denken, dass sie einem kollektiven Algorithmus folgen oder dass sie eine Form von *kollektiver Intelligenz* besitzen. Dieses komplexe Verhalten entsteht jedoch, wenn jeder einzelne Agent (in diesem Fall ein *Vogel*) nur einige andere Agenten in kurzer Distanz von sich beobachtet und drei einfache Regeln befolgt:

* **Ausrichtung** - er steuert in Richtung des durchschnittlichen Kurs der benachbarten Agenten
* **Kohäsion** - er versucht, in Richtung der durchschnittlichen Position der Nachbarn zu steuern (*langfristige Anziehung*)
* **Trennung** - wenn er zu nah an anderen Vögeln ist, versucht er, sich zu entfernen (*kurzfristige Abstoßung*)

Sie können das Vogelschwarm-Beispiel ausführen und das Verhalten beobachten. Sie können auch Parameter anpassen, wie den *Grad der Trennung* oder den *Sichtbereich*, der definiert, wie weit jeder Vogel sehen kann. Beachten Sie, dass, wenn Sie den Sichtbereich auf 0 reduzieren, alle Vögel blind werden und der Vogelschwarm stoppt. Wenn Sie die Trennung auf 0 reduzieren, versammeln sich alle Vögel in einer geraden Linie.

> ✅ Wechseln Sie zum **Code**-Tab und sehen Sie, wo die drei Regeln des Vogelschwarmes (Ausrichtung, Kohäsion und Trennung) im Code implementiert sind. Beachten Sie, wie wir uns nur auf die Agenten beziehen, die in Sichtweite sind.

### Weitere Modelle zum Ausprobieren

Es gibt noch einige weitere interessante Modelle, mit denen Sie experimentieren können:

* **Kunst → Feuerwerk** zeigt, wie ein Feuerwerk als kollektives Verhalten individueller Feuerströme betrachtet werden kann.
* **Sozialwissenschaft → Verkehr Grundlegend** und **Sozialwissenschaft → Verkehr Raster** zeigen das Modell des Stadtverkehrs in 1D und 2D Rastern mit oder ohne Ampeln. Jedes Auto in der Simulation folgt den folgenden Regeln:
   - Wenn der Raum vor ihm leer ist - beschleunigen (bis zu einer bestimmten Höchstgeschwindigkeit)
   - Wenn es ein Hindernis vor sich sieht - bremsen (und Sie können anpassen, wie weit ein Fahrer sehen kann)
* **Sozialwissenschaft → Party** zeigt, wie Menschen sich während einer Cocktailparty gruppieren. Sie können die Kombination von Parametern finden, die zu einer schnellsten Steigerung des Glücks der Gruppe führen.

Wie Sie an diesen Beispielen sehen können, können Multi-Agenten-Simulationen eine nützliche Möglichkeit sein, das Verhalten eines komplexen Systems zu verstehen, das aus Individuen besteht, die der gleichen oder ähnlichen Logik folgen. Sie können auch verwendet werden, um virtuelle Agenten zu steuern, wie [NPCs](https://de.wikipedia.org/wiki/NPC) in Computerspielen oder Agenten in 3D-animierten Welten.

## Deliberative Agenten

Die oben beschriebenen Agenten sind sehr einfach und reagieren auf Veränderungen in der Umgebung mithilfe einer Art Algorithmus. Daher sind sie **reaktive Agenten**. Manchmal können Agenten jedoch auch schlussfolgern und ihre Aktionen planen, in diesem Fall werden sie als **deliberative** bezeichnet.

Ein typisches Beispiel wäre ein persönlicher Agent, der eine Anweisung von einem Menschen erhält, um eine Urlaubsreise zu buchen. Angenommen, es gibt viele Agenten, die im Internet leben und ihm helfen können. Er sollte dann andere Agenten kontaktieren, um zu sehen, welche Flüge verfügbar sind, wie die Hotelpreise an verschiedenen Daten sind, und versuchen, den besten Preis auszuhandeln. Wenn der Urlaubsplan abgeschlossen und vom Besitzer bestätigt ist, kann er mit der Buchung fortfahren.

Um dies zu tun, müssen Agenten **kommunizieren**. Für eine erfolgreiche Kommunikation benötigen sie:

* Einige **Standardsprachen zum Austausch von Wissen**, wie [Knowledge Interchange Format](https://de.wikipedia.org/wiki/Knowledge_Interchange_Format) (KIF) und [Knowledge Query and Manipulation Language](https://de.wikipedia.org/wiki/Knowledge_Query_and_Manipulation_Language) (KQML). Diese Sprachen sind auf der Grundlage der [Sprechakt-Theorie](https://de.wikipedia.org/wiki/Sprechakt) entworfen.
* Diese Sprachen sollten auch einige **Protokolle für Verhandlungen** beinhalten, basierend auf verschiedenen **Auktionsarten**.
* Eine **gemeinsame Ontologie**, die verwendet wird, damit sie sich auf die gleichen Konzepte beziehen und deren Semantik kennen.
* Eine Möglichkeit, um zu **entdecken**, was verschiedene Agenten tun können, ebenfalls basierend auf einer Art Ontologie.

Deliberative Agenten sind viel komplexer als reaktive, da sie nicht nur auf Veränderungen in der Umgebung reagieren, sondern auch in der Lage sein sollten, Aktionen *zu initiieren*. Eine der vorgeschlagenen Architekturen für deliberative Agenten ist der sogenannte Belief-Desire-Intention (BDI) Agent:

* **Überzeugungen** bilden ein Set von Wissen über die Umgebung eines Agenten. Es kann als Wissensbasis oder Regelset strukturiert sein, das ein Agent auf eine spezifische Situation in der Umgebung anwenden kann.
* **Wünsche** definieren, was ein Agent tun möchte, d.h. seine Ziele. Zum Beispiel ist das Ziel des oben genannten persönlichen Assistenten, eine Reise zu buchen, und das Ziel eines Hotelagenten ist es, den Gewinn zu maximieren.
* **Absichten** sind spezifische Aktionen, die ein Agent plant, um seine Ziele zu erreichen. Aktionen verändern typischerweise die Umgebung und verursachen Kommunikation mit anderen Agenten.

Es gibt einige Plattformen, die für den Aufbau von Multi-Agenten-Systemen verfügbar sind, wie [JADE](https://jade.tilab.com/). [Dieses Papier](https://arxiv.org/ftp/arxiv/papers/2007/2007.08961.pdf) enthält eine Übersicht über Multi-Agenten-Plattformen, zusammen mit einer kurzen Geschichte der Multi-Agenten-Systeme und ihren verschiedenen Anwendungsszenarien.

## Fazit

Multi-Agent-Systeme können sehr unterschiedliche Formen annehmen und in vielen verschiedenen Anwendungen eingesetzt werden. Sie konzentrieren sich alle auf das einfachere Verhalten eines einzelnen Agenten und erreichen komplexeres Verhalten des Gesamtsystems aufgrund des **synergetischen Effekts**.

## 🚀 Herausforderung

Bringen Sie diese Lektion in die reale Welt und versuchen Sie, ein Multi-Agenten-System zu konzipieren, das ein Problem lösen kann. Was müsste ein Multi-Agenten-System beispielsweise tun, um eine Schulbusroute zu optimieren? Wie könnte es in einer Bäckerei funktionieren?

## [Nachvorlesungsquiz](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/223)

## Überprüfung & Selbststudium

Überprüfen Sie die Verwendung dieses Typs von Systemen in der Industrie. Wählen Sie ein Gebiet wie die Fertigung oder die Videospielindustrie aus und entdecken Sie, wie Multi-Agenten-Systeme verwendet werden können, um einzigartige Probleme zu lösen.

## [NetLogo Aufgabe](assignment.md)

**Haftungsausschluss**:  
Dieses Dokument wurde mit maschinellen KI-Übersetzungsdiensten übersetzt. Obwohl wir uns um Genauigkeit bemühen, sollten Sie sich bewusst sein, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner ursprünglichen Sprache sollte als autoritative Quelle betrachtet werden. Für kritische Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die aus der Verwendung dieser Übersetzung entstehen.