# Ethische und verantwortungsvolle KI

Sie haben diesen Kurs fast abgeschlossen, und ich hoffe, dass Sie mittlerweile klar erkennen, dass KI auf einer Reihe formaler mathematischer Methoden basiert, die es uns ermöglichen, Beziehungen in Daten zu finden und Modelle zu trainieren, um bestimmte Aspekte menschlichen Verhaltens nachzubilden. Zu diesem Zeitpunkt in der Geschichte betrachten wir KI als ein sehr mächtiges Werkzeug, um Muster aus Daten zu extrahieren und diese Muster anzuwenden, um neue Probleme zu lösen.

## [Quiz vor der Vorlesung](https://white-water-09ec41f0f.azurestaticapps.net/quiz/5/)

In der Science-Fiction sehen wir jedoch oft Geschichten, in denen KI eine Gefahr für die Menschheit darstellt. Diese Geschichten drehen sich meist um eine Art KI-Rebellion, bei der die KI beschließt, sich gegen die Menschen zu stellen. Dies impliziert, dass KI eine Art Emotion besitzt oder Entscheidungen treffen kann, die von ihren Entwicklern nicht vorhergesehen wurden.

Die Art von KI, die wir in diesem Kurs kennengelernt haben, ist nichts anderes als umfangreiche Matrizenarithmetik. Es ist ein sehr mächtiges Werkzeug, das uns hilft, unsere Probleme zu lösen, und wie jedes andere mächtige Werkzeug kann es sowohl für gute als auch für schlechte Zwecke eingesetzt werden. Wichtig ist, dass es *missbraucht* werden kann.

## Prinzipien der verantwortungsvollen KI

Um einen zufälligen oder absichtlichen Missbrauch von KI zu vermeiden, hat Microsoft die wichtigen [Prinzipien der verantwortungsvollen KI](https://www.microsoft.com/ai/responsible-ai?WT.mc_id=academic-77998-cacaste) definiert. Die folgenden Konzepte bilden die Grundlage dieser Prinzipien:

* **Fairness** bezieht sich auf das wichtige Problem der *Modellverzerrungen*, die durch die Verwendung von voreingenommenen Trainingsdaten verursacht werden können. Zum Beispiel, wenn wir versuchen, die Wahrscheinlichkeit vorherzusagen, dass eine Person einen Job als Softwareentwickler bekommt, wird das Modell wahrscheinlich Männern den Vorzug geben – einfach weil der Trainingsdatensatz wahrscheinlich auf eine männliche Zielgruppe ausgerichtet war. Wir müssen die Trainingsdaten sorgfältig ausbalancieren und das Modell untersuchen, um Verzerrungen zu vermeiden und sicherzustellen, dass das Modell relevantere Merkmale berücksichtigt.
* **Zuverlässigkeit und Sicherheit**. KI-Modelle können von Natur aus Fehler machen. Ein neuronales Netzwerk liefert Wahrscheinlichkeiten, und das müssen wir bei Entscheidungen berücksichtigen. Jedes Modell hat eine bestimmte Präzision und einen bestimmten Rückrufwert, und wir müssen das verstehen, um Schäden zu vermeiden, die durch falsche Ratschläge entstehen können.
* **Privatsphäre und Sicherheit** haben einige KI-spezifische Implikationen. Zum Beispiel wird die verwendete Trainingsdaten irgendwie in das Modell "integriert". Einerseits erhöht das die Sicherheit und Privatsphäre, andererseits müssen wir uns daran erinnern, welche Daten für das Training des Modells verwendet wurden.
* **Inklusivität** bedeutet, dass wir KI nicht entwickeln, um Menschen zu ersetzen, sondern um sie zu unterstützen und unsere Arbeit kreativer zu gestalten. Es steht auch in Zusammenhang mit Fairness, denn wenn wir mit unterrepräsentierten Gemeinschaften arbeiten, sind die meisten der gesammelten Datensätze wahrscheinlich voreingenommen. Wir müssen sicherstellen, dass diese Gemeinschaften einbezogen und korrekt von der KI behandelt werden.
* **Transparenz**. Dazu gehört, dass wir immer klarstellen, wenn KI verwendet wird. Außerdem möchten wir, wo immer möglich, KI-Systeme verwenden, die *interpretierbar* sind.
* **Verantwortlichkeit**. Wenn KI-Modelle Entscheidungen treffen, ist nicht immer klar, wer für diese Entscheidungen verantwortlich ist. Wir müssen sicherstellen, dass wir verstehen, wo die Verantwortung für KI-Entscheidungen liegt. In den meisten Fällen möchten wir Menschen in den Entscheidungsprozess einbeziehen, damit tatsächliche Personen zur Verantwortung gezogen werden können.

## Werkzeuge für verantwortungsvolle KI

Microsoft hat das [Responsible AI Toolbox](https://github.com/microsoft/responsible-ai-toolbox) entwickelt, das eine Reihe von Werkzeugen enthält:

* Interpretability Dashboard (InterpretML)
* Fairness Dashboard (FairLearn)
* Error Analysis Dashboard
* Responsible AI Dashboard, das Folgendes umfasst:

   - EconML – ein Tool für Kausalanalysen, das sich auf Was-wäre-wenn-Fragen konzentriert
   - DiCE – ein Tool für kontrafaktische Analysen, mit dem Sie sehen können, welche Merkmale geändert werden müssen, um die Entscheidung des Modells zu beeinflussen

Weitere Informationen zur KI-Ethik finden Sie in [dieser Lektion](https://github.com/microsoft/ML-For-Beginners/tree/main/1-Introduction/3-fairness?WT.mc_id=academic-77998-cacaste) im Machine Learning Curriculum, das auch Aufgaben enthält.

## Überprüfung & Selbststudium

Nehmen Sie an diesem [Lernpfad](https://docs.microsoft.com/learn/modules/responsible-ai-principles/?WT.mc_id=academic-77998-cacaste) teil, um mehr über verantwortungsvolle KI zu erfahren.

## [Quiz nach der Vorlesung](https://white-water-09ec41f0f.azurestaticapps.net/quiz/6/)

**Haftungsausschluss**:  
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner ursprünglichen Sprache sollte als maßgebliche Quelle betrachtet werden. Für kritische Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die sich aus der Nutzung dieser Übersetzung ergeben.