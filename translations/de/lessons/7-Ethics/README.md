# Ethische und Verantwortungsvolle KI

Sie haben diesen Kurs fast abgeschlossen, und ich hoffe, dass Sie inzwischen klar erkennen, dass KI auf einer Reihe von formalen mathematischen Methoden basiert, die es uns ermöglichen, Beziehungen in Daten zu finden und Modelle zu trainieren, um einige Aspekte menschlichen Verhaltens zu replizieren. An diesem Punkt in der Geschichte betrachten wir KI als ein sehr mächtiges Werkzeug, um Muster aus Daten zu extrahieren und diese Muster anzuwenden, um neue Probleme zu lösen.

## [Vorlesungsquiz](https://white-water-09ec41f0f.azurestaticapps.net/quiz/5/)

In der Science-Fiction sehen wir jedoch oft Geschichten, in denen KI eine Gefahr für die Menschheit darstellt. In der Regel konzentrieren sich diese Geschichten auf eine Art von KI-Rebellion, wenn KI beschließt, sich den Menschen zu widersetzen. Das impliziert, dass KI eine Art von Emotion hat oder Entscheidungen trifft, die von ihren Entwicklern nicht vorhergesehen wurden.

Die Art von KI, die wir in diesem Kurs kennengelernt haben, ist nichts weiter als große Matrizenarithmetik. Es ist ein sehr mächtiges Werkzeug, das uns hilft, unsere Probleme zu lösen, und wie jedes andere mächtige Werkzeug kann es sowohl für gute als auch für schlechte Zwecke eingesetzt werden. Wichtig ist, dass es *missbraucht* werden kann.

## Prinzipien der Verantwortungsvolle KI

Um diesen unbeabsichtigten oder absichtlichen Missbrauch von KI zu vermeiden, gibt Microsoft die wichtigen [Prinzipien der Verantwortungsvolle KI](https://www.microsoft.com/ai/responsible-ai?WT.mc_id=academic-77998-cacaste) an. Die folgenden Konzepte bilden die Grundlage für diese Prinzipien:

* **Fairness** hängt mit dem wichtigen Problem der *Modellverzerrungen* zusammen, die durch die Verwendung von voreingenommenen Daten für das Training verursacht werden können. Zum Beispiel, wenn wir die Wahrscheinlichkeit vorhersagen wollen, dass eine Person einen Job als Softwareentwickler erhält, wird das Modell wahrscheinlich Männern eine höhere Präferenz einräumen – nur weil der Trainingsdatensatz wahrscheinlich auf ein männliches Publikum ausgerichtet war. Wir müssen die Trainingsdaten sorgfältig ausbalancieren und das Modell untersuchen, um Verzerrungen zu vermeiden und sicherzustellen, dass das Modell relevantere Merkmale berücksichtigt.
* **Zuverlässigkeit und Sicherheit**. Aufgrund ihrer Natur können KI-Modelle Fehler machen. Ein neuronales Netzwerk gibt Wahrscheinlichkeiten zurück, und wir müssen dies bei Entscheidungen berücksichtigen. Jedes Modell hat eine gewisse Präzision und Rückrufquote, und wir müssen verstehen, dass wir Schäden, die falsche Ratschläge verursachen können, verhindern müssen.
* **Datenschutz und Sicherheit** haben einige KI-spezifische Implikationen. Zum Beispiel, wenn wir einige Daten zum Trainieren eines Modells verwenden, werden diese Daten irgendwie "integriert" in das Modell. Einerseits erhöht das die Sicherheit und den Datenschutz, andererseits müssen wir uns daran erinnern, auf welchen Daten das Modell trainiert wurde.
* **Inklusivität** bedeutet, dass wir KI nicht entwickeln, um Menschen zu ersetzen, sondern um Menschen zu unterstützen und unsere Arbeit kreativer zu gestalten. Es hängt auch mit Fairness zusammen, denn im Umgang mit unterrepräsentierten Gemeinschaften sind die meisten Datensätze, die wir sammeln, wahrscheinlich voreingenommen, und wir müssen sicherstellen, dass diese Gemeinschaften einbezogen und korrekt von der KI behandelt werden.
* **Transparenz**. Dazu gehört, dass wir immer klar kommunizieren, dass KI verwendet wird. Auch wo immer möglich, möchten wir KI-Systeme nutzen, die *interpretierbar* sind.
* **Rechenschaftspflicht**. Wenn KI-Modelle Entscheidungen treffen, ist nicht immer klar, wer für diese Entscheidungen verantwortlich ist. Wir müssen sicherstellen, dass wir verstehen, wo die Verantwortung für KI-Entscheidungen liegt. In den meisten Fällen möchten wir Menschen in den Entscheidungsprozess einbeziehen, damit tatsächliche Personen zur Rechenschaft gezogen werden.

## Werkzeuge für Verantwortungsvolle KI

Microsoft hat die [Responsible AI Toolbox](https://github.com/microsoft/responsible-ai-toolbox) entwickelt, die eine Reihe von Werkzeugen enthält:

* Interpretierbarkeit-Dashboard (InterpretML)
* Fairness-Dashboard (FairLearn)
* Fehleranalyse-Dashboard
* Verantwortungsvolles KI-Dashboard, das Folgendes umfasst

   - EconML - ein Werkzeug für Kausalanalyse, das sich auf Was-wäre-wenn-Fragen konzentriert
   - DiCE - ein Werkzeug für kontrafaktische Analysen, mit dem Sie sehen können, welche Merkmale geändert werden müssen, um die Entscheidung des Modells zu beeinflussen

Für weitere Informationen über KI-Ethische Grundsätze besuchen Sie bitte [diese Lektion](https://github.com/microsoft/ML-For-Beginners/tree/main/1-Introduction/3-fairness?WT.mc_id=academic-77998-cacaste) im Lehrplan für maschinelles Lernen, der Aufgaben enthält.

## Überprüfung & Selbststudium

Nehmen Sie diesen [Lernpfad](https://docs.microsoft.com/learn/modules/responsible-ai-principles/?WT.mc_id=academic-77998-cacaste), um mehr über verantwortungsvolle KI zu erfahren.

## [Nachlesungsquiz](https://white-water-09ec41f0f.azurestaticapps.net/quiz/6/)

**Haftungsausschluss**:  
Dieses Dokument wurde mit maschinellen KI-Übersetzungsdiensten übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner ursprünglichen Sprache sollte als maßgebliche Quelle betrachtet werden. Für kritische Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die aus der Verwendung dieser Übersetzung resultieren.