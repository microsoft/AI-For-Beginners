# Einführung in KI

![Zusammenfassung der Einführung in KI in einer Skizze](../../../../translated_images/de/ai-intro.bf28d1ac4235881c.webp)

> Sketchnote von [Tomomi Imura](https://twitter.com/girlie_mac)

## [Quiz vor der Vorlesung](https://ff-quizzes.netlify.app/en/ai/quiz/1)

**Künstliche Intelligenz** ist eine spannende wissenschaftliche Disziplin, die untersucht, wie wir Computer dazu bringen können, intelligentes Verhalten zu zeigen, z. B. Dinge zu tun, die Menschen gut können.

Ursprünglich wurden Computer von [Charles Babbage](https://en.wikipedia.org/wiki/Charles_Babbage) erfunden, um Zahlen nach einem klar definierten Verfahren – einem Algorithmus – zu verarbeiten. Moderne Computer, obwohl sie wesentlich fortschrittlicher sind als das ursprüngliche Modell aus dem 19. Jahrhundert, folgen immer noch derselben Idee kontrollierter Berechnungen. Daher ist es möglich, einen Computer so zu programmieren, dass er etwas tut, wenn wir die genaue Abfolge der Schritte kennen, die wir ausführen müssen, um das Ziel zu erreichen.

![Foto einer Person](../../../../translated_images/de/dsh_age.d212a30d4e54fb5f.webp)

> Foto von [Vickie Soshnikova](http://twitter.com/vickievalerie)

> ✅ Das Alter einer Person anhand eines Fotos zu bestimmen, ist eine Aufgabe, die nicht explizit programmiert werden kann, da wir nicht wissen, wie wir die Zahl in unserem Kopf ermitteln, wenn wir es tun.

---

Es gibt jedoch Aufgaben, bei denen wir nicht genau wissen, wie wir sie lösen können. Überlegen Sie, wie man das Alter einer Person anhand eines Fotos bestimmt. Wir lernen es irgendwie, weil wir viele Beispiele von Menschen unterschiedlichen Alters gesehen haben, aber wir können nicht genau erklären, wie wir es tun, noch können wir den Computer so programmieren, dass er es tut. Genau solche Aufgaben interessieren die **Künstliche Intelligenz** (kurz KI).

✅ Überlegen Sie sich einige Aufgaben, die Sie an einen Computer auslagern könnten und die von KI profitieren würden. Denken Sie an die Bereiche Finanzen, Medizin und Kunst – wie profitieren diese Bereiche heute von KI?

## Schwache KI vs. Starke KI

Schwache KI | Starke KI
---------------------------------------|-------------------------------------
Schwache KI bezieht sich auf KI-Systeme, die für eine spezifische Aufgabe oder eine enge Aufgabenmenge entwickelt und trainiert wurden.|Starke KI, oder Allgemeine Künstliche Intelligenz (AGI), bezieht sich auf KI-Systeme mit menschlicher Intelligenz und Verständnis.
Diese KI-Systeme sind nicht allgemein intelligent; sie sind hervorragend darin, eine vordefinierte Aufgabe auszuführen, besitzen jedoch kein echtes Verständnis oder Bewusstsein.|Diese KI-Systeme können jede intellektuelle Aufgabe ausführen, die ein Mensch bewältigen kann, sich an verschiedene Bereiche anpassen und eine Form von Bewusstsein oder Selbstwahrnehmung besitzen.
Beispiele für schwache KI sind virtuelle Assistenten wie Siri oder Alexa, Empfehlungsalgorithmen von Streaming-Diensten und Chatbots, die für spezifische Kundenservice-Aufgaben entwickelt wurden.|Das Erreichen von Starker KI ist ein langfristiges Ziel der KI-Forschung und würde die Entwicklung von KI-Systemen erfordern, die in der Lage sind, zu argumentieren, zu lernen, zu verstehen und sich über eine Vielzahl von Aufgaben und Kontexten hinweg anzupassen.
Schwache KI ist hochspezialisiert und besitzt keine menschenähnlichen kognitiven Fähigkeiten oder allgemeine Problemlösungsfähigkeiten außerhalb ihres engen Bereichs.|Starke KI ist derzeit ein theoretisches Konzept, und kein KI-System hat dieses Niveau allgemeiner Intelligenz erreicht.

Weitere Informationen finden Sie unter **[Allgemeine Künstliche Intelligenz](https://en.wikipedia.org/wiki/Artificial_general_intelligence)** (AGI).

## Die Definition von Intelligenz und der Turing-Test

Eines der Probleme im Umgang mit dem Begriff **[Intelligenz](https://en.wikipedia.org/wiki/Intelligence)** ist, dass es keine klare Definition dieses Begriffs gibt. Man könnte argumentieren, dass Intelligenz mit **abstraktem Denken** oder **Selbstbewusstsein** verbunden ist, aber wir können sie nicht eindeutig definieren.

![Foto einer Katze](../../../../translated_images/de/photo-cat.8c8e8fb760ffe457.webp)

> [Foto](https://unsplash.com/photos/75715CVEJhI) von [Amber Kipp](https://unsplash.com/@sadmax) auf Unsplash

Um die Mehrdeutigkeit des Begriffs *Intelligenz* zu verdeutlichen, versuchen Sie, folgende Frage zu beantworten: "Ist eine Katze intelligent?". Verschiedene Menschen neigen dazu, unterschiedliche Antworten auf diese Frage zu geben, da es keinen allgemein anerkannten Test gibt, um die Behauptung zu beweisen oder zu widerlegen. Und wenn Sie denken, es gäbe einen – versuchen Sie, Ihre Katze durch einen IQ-Test zu schicken...

✅ Denken Sie eine Minute darüber nach, wie Sie Intelligenz definieren. Ist eine Krähe, die ein Labyrinth lösen kann, um an Futter zu gelangen, intelligent? Ist ein Kind intelligent?

---

Wenn wir über AGI sprechen, brauchen wir eine Möglichkeit, festzustellen, ob wir ein wirklich intelligentes System geschaffen haben. [Alan Turing](https://en.wikipedia.org/wiki/Alan_Turing) schlug eine Methode vor, die als **[Turing-Test](https://en.wikipedia.org/wiki/Turing_test)** bekannt ist und gleichzeitig als Definition von Intelligenz dient. Der Test vergleicht ein gegebenes System mit etwas inhärent Intelligenten – einem echten Menschen. Da jeder automatische Vergleich von einem Computerprogramm umgangen werden kann, verwenden wir einen menschlichen Befrager. Wenn ein Mensch nicht in der Lage ist, zwischen einer echten Person und einem Computersystem in einem textbasierten Dialog zu unterscheiden, wird das System als intelligent angesehen.

> Ein Chatbot namens [Eugene Goostman](https://en.wikipedia.org/wiki/Eugene_Goostman), entwickelt in St. Petersburg, kam 2014 dem Bestehen des Turing-Tests nahe, indem er einen cleveren Persönlichkeitstrick anwandte. Er gab von Anfang an an, ein 13-jähriger ukrainischer Junge zu sein, was das fehlende Wissen und einige Unstimmigkeiten im Text erklären würde. Der Bot überzeugte 30 % der Richter, dass er ein Mensch sei, nach einem 5-minütigen Dialog – eine Metrik, von der Turing glaubte, dass sie eine Maschine bis zum Jahr 2000 erreichen könnte. Man sollte jedoch verstehen, dass dies nicht bedeutet, dass wir ein intelligentes System geschaffen haben oder dass ein Computersystem den menschlichen Befrager getäuscht hat – das System hat die Menschen nicht getäuscht, sondern die Bot-Entwickler!

✅ Wurden Sie jemals von einem Chatbot getäuscht und dachten, Sie sprechen mit einem Menschen? Wie hat er Sie überzeugt?

## Verschiedene Ansätze zur KI

Wenn wir wollen, dass ein Computer sich wie ein Mensch verhält, müssen wir irgendwie unsere Denkweise im Computer modellieren. Folglich müssen wir versuchen zu verstehen, was einen Menschen intelligent macht.

> Um Intelligenz in eine Maschine programmieren zu können, müssen wir verstehen, wie unsere eigenen Entscheidungsprozesse funktionieren. Wenn Sie ein wenig Selbstreflexion betreiben, werden Sie feststellen, dass einige Prozesse unbewusst ablaufen – z. B. können wir eine Katze von einem Hund unterscheiden, ohne darüber nachzudenken – während andere Überlegungen erfordern.

Es gibt zwei mögliche Ansätze für dieses Problem:

Top-down-Ansatz (symbolisches Denken) | Bottom-up-Ansatz (Neuronale Netze)
---------------------------------------|-------------------------------------
Ein Top-down-Ansatz modelliert die Art und Weise, wie eine Person denkt, um ein Problem zu lösen. Es beinhaltet das Extrahieren von **Wissen** von einem Menschen und das Darstellen in einer computerlesbaren Form. Wir müssen auch eine Möglichkeit entwickeln, **Schlussfolgerungen** im Computer zu modellieren. | Ein Bottom-up-Ansatz modelliert die Struktur des menschlichen Gehirns, das aus einer großen Anzahl einfacher Einheiten besteht, die als **Neuronen** bezeichnet werden. Jedes Neuron agiert wie ein gewichteter Durchschnitt seiner Eingaben, und wir können ein Netzwerk von Neuronen trainieren, um nützliche Probleme zu lösen, indem wir **Trainingsdaten** bereitstellen.

Es gibt auch einige andere mögliche Ansätze zur Intelligenz:

* Ein **emergenter**, **synergetischer** oder **Multi-Agenten-Ansatz** basiert auf der Tatsache, dass komplexes intelligentes Verhalten durch die Interaktion einer großen Anzahl einfacher Agenten entstehen kann. Laut der [evolutionären Kybernetik](https://en.wikipedia.org/wiki/Global_brain#Evolutionary_cybernetics) kann Intelligenz im Prozess des *Metasystem-Übergangs* aus einfacheren, reaktiven Verhaltensweisen *entstehen*.

* Ein **evolutionärer Ansatz** oder **genetischer Algorithmus** ist ein Optimierungsprozess, der auf den Prinzipien der Evolution basiert.

Wir werden diese Ansätze später im Kurs betrachten, aber im Moment konzentrieren wir uns auf zwei Hauptansätze: Top-down und Bottom-up.

### Der Top-Down-Ansatz

Beim **Top-down-Ansatz** versuchen wir, unser Denken zu modellieren. Da wir unseren Gedanken folgen können, wenn wir nachdenken, können wir versuchen, diesen Prozess zu formalisieren und ihn im Computer zu programmieren. Dies wird als **symbolisches Denken** bezeichnet.

Menschen haben oft Regeln im Kopf, die ihre Entscheidungsprozesse leiten. Zum Beispiel kann ein Arzt bei der Diagnose eines Patienten feststellen, dass eine Person Fieber hat und daher möglicherweise eine Entzündung im Körper vorliegt. Durch die Anwendung einer großen Menge von Regeln auf ein spezifisches Problem kann ein Arzt möglicherweise die endgültige Diagnose stellen.

Dieser Ansatz stützt sich stark auf **Wissensrepräsentation** und **Schlussfolgerungen**. Wissen von einem menschlichen Experten zu extrahieren, könnte der schwierigste Teil sein, da ein Arzt in vielen Fällen nicht genau weiß, warum er oder sie zu einer bestimmten Diagnose kommt. Manchmal kommt die Lösung einfach in den Kopf, ohne explizites Nachdenken. Einige Aufgaben, wie das Bestimmen des Alters einer Person anhand eines Fotos, können überhaupt nicht auf die Manipulation von Wissen reduziert werden.

### Bottom-Up-Ansatz

Alternativ können wir versuchen, die einfachsten Elemente in unserem Gehirn zu modellieren – ein Neuron. Wir können ein sogenanntes **künstliches neuronales Netzwerk** im Computer konstruieren und dann versuchen, es durch Beispiele zu trainieren, um Probleme zu lösen. Dieser Prozess ähnelt dem, wie ein neugeborenes Kind seine Umgebung durch Beobachtungen kennenlernt.

✅ Recherchieren Sie ein wenig, wie Babys lernen. Was sind die grundlegenden Elemente des Gehirns eines Babys?

> | Was ist mit ML?         |      |
> |--------------|-----------|
> | Ein Teil der Künstlichen Intelligenz, der darauf basiert, dass Computer lernen, ein Problem anhand von Daten zu lösen, wird als **Maschinelles Lernen** bezeichnet. Wir werden klassisches maschinelles Lernen in diesem Kurs nicht behandeln – wir verweisen Sie auf den separaten [Maschinelles Lernen für Anfänger](http://aka.ms/ml-beginners)-Lehrplan. |   ![ML für Anfänger](../../../../translated_images/de/ml-for-beginners.9e4fed176fd5817d.webp)    |

## Ein kurzer Überblick über die Geschichte der KI

Künstliche Intelligenz wurde Mitte des 20. Jahrhunderts als Forschungsfeld begründet. Anfangs war symbolisches Denken der vorherrschende Ansatz, und es führte zu einer Reihe wichtiger Erfolge, wie z. B. Expertensysteme – Computerprogramme, die in der Lage waren, in begrenzten Problembereichen als Experte zu agieren. Es wurde jedoch bald klar, dass ein solcher Ansatz nicht gut skalierbar ist. Wissen von einem Experten zu extrahieren, es im Computer darzustellen und diese Wissensbasis aktuell zu halten, stellte sich als sehr komplexe Aufgabe heraus und war in vielen Fällen zu teuer, um praktikabel zu sein. Dies führte in den 1970er Jahren zum sogenannten [KI-Winter](https://en.wikipedia.org/wiki/AI_winter).

<img alt="Kurze Geschichte der KI" src="../../../../translated_images/de/history-of-ai.7e83efa70b537f5a.webp" width="70%"/>

> Bild von [Dmitry Soshnikov](http://soshnikov.com)

Mit der Zeit wurden Rechenressourcen günstiger, und es standen mehr Daten zur Verfügung, sodass neuronale Netzwerke in vielen Bereichen, wie z. B. der Computer Vision oder dem Sprachverständnis, großartige Leistungen zeigten. In den letzten zehn Jahren wurde der Begriff Künstliche Intelligenz meist als Synonym für Neuronale Netzwerke verwendet, da die meisten Erfolge der KI, von denen wir hören, auf ihnen basieren.

Wir können beobachten, wie sich die Ansätze geändert haben, z. B. bei der Entwicklung eines Schachprogramms:

* Frühe Schachprogramme basierten auf der Suche – ein Programm versuchte explizit, mögliche Züge eines Gegners für eine bestimmte Anzahl von Zügen vorauszuschätzen und wählte einen optimalen Zug basierend auf der besten Position, die in wenigen Zügen erreicht werden kann. Dies führte zur Entwicklung des sogenannten [Alpha-Beta-Suchalgorithmus](https://en.wikipedia.org/wiki/Alpha%E2%80%93beta_pruning).
* Suchstrategien funktionieren gut gegen Ende des Spiels, wenn der Suchraum durch eine geringe Anzahl möglicher Züge begrenzt ist. Zu Beginn des Spiels ist der Suchraum jedoch riesig, und der Algorithmus kann durch das Lernen aus bestehenden Partien zwischen menschlichen Spielern verbessert werden. Spätere Experimente verwendeten sogenanntes [Fallbasiertes Schließen](https://en.wikipedia.org/wiki/Case-based_reasoning), bei dem das Programm nach Fällen in der Wissensbasis suchte, die der aktuellen Spielsituation sehr ähnlich sind.
* Moderne Programme, die menschliche Spieler besiegen, basieren auf neuronalen Netzwerken und [Verstärkungslernen](https://en.wikipedia.org/wiki/Reinforcement_learning), bei dem die Programme allein durch das Spielen gegen sich selbst und das Lernen aus ihren eigenen Fehlern lernen – ähnlich wie Menschen, wenn sie Schach lernen. Ein Computerprogramm kann jedoch viel mehr Spiele in viel kürzerer Zeit spielen und somit viel schneller lernen.

✅ Recherchieren Sie ein wenig über andere Spiele, die von KI gespielt wurden.

Ähnlich können wir sehen, wie sich der Ansatz zur Erstellung von „sprechenden Programmen“ (die den Turing-Test bestehen könnten) verändert hat:

* Frühe Programme dieser Art, wie [Eliza](https://en.wikipedia.org/wiki/ELIZA), basierten auf sehr einfachen grammatikalischen Regeln und der Umformulierung des Eingabesatzes in eine Frage.
* Moderne Assistenten wie Cortana, Siri oder Google Assistant sind alle Hybridsysteme, die neuronale Netzwerke verwenden, um Sprache in Text umzuwandeln und unsere Absicht zu erkennen, und dann einige Schlussfolgerungen oder explizite Algorithmen anwenden, um die erforderlichen Aktionen auszuführen.
* In der Zukunft können wir erwarten, dass ein vollständiges neuronales Modell den Dialog eigenständig handhabt. Die jüngsten GPT- und [Turing-NLG](https://www.microsoft.com/research/blog/turing-nlg-a-17-billion-parameter-language-model-by-microsoft)-Familien von neuronalen Netzwerken zeigen große Erfolge in diesem Bereich.

<img alt="Die Entwicklung des Turing-Tests" src="../../../../translated_images/de/turing-test-evol.4184696701293ead.webp" width="70%"/>
> Bild von Dmitry Soshnikov, [Foto](https://unsplash.com/photos/r8LmVbUKgns) von [Marina Abrosimova](https://unsplash.com/@abrosimova_marina_foto), Unsplash

## Aktuelle KI-Forschung

Das enorme Wachstum der Forschung zu neuronalen Netzwerken begann etwa 2010, als große öffentliche Datensätze verfügbar wurden. Eine riesige Sammlung von Bildern namens [ImageNet](https://en.wikipedia.org/wiki/ImageNet), die etwa 14 Millionen annotierte Bilder enthält, führte zur Entstehung der [ImageNet Large Scale Visual Recognition Challenge](https://image-net.org/challenges/LSVRC/).

![ILSVRC Genauigkeit](../../../../lessons/1-Intro/images/ilsvrc.gif)

> Bild von [Dmitry Soshnikov](http://soshnikov.com)

Im Jahr 2012 wurden [Convolutional Neural Networks](../4-ComputerVision/07-ConvNets/README.md) erstmals für die Bildklassifikation eingesetzt, was zu einem signifikanten Rückgang der Klassifikationsfehler führte (von fast 30 % auf 16,4 %). Im Jahr 2015 erreichte die ResNet-Architektur von Microsoft Research [menschliche Genauigkeit](https://doi.org/10.1109/ICCV.2015.123).

Seitdem haben neuronale Netzwerke in vielen Aufgaben sehr erfolgreiche Ergebnisse gezeigt:

---

Jahr | Menschliche Gleichwertigkeit erreicht
-----|--------
2015 | [Bildklassifikation](https://doi.org/10.1109/ICCV.2015.123)
2016 | [Gesprächsbasierte Spracherkennung](https://arxiv.org/abs/1610.05256)
2018 | [Automatische maschinelle Übersetzung](https://arxiv.org/abs/1803.05567) (Chinesisch-Englisch)
2020 | [Bildbeschreibung](https://arxiv.org/abs/2009.13682)

In den letzten Jahren haben wir große Erfolge mit großen Sprachmodellen wie BERT und GPT-3 erlebt. Dies geschah vor allem, weil es eine große Menge an allgemeinen Textdaten gibt, die es uns ermöglichen, Modelle zu trainieren, um die Struktur und Bedeutung von Texten zu erfassen, sie auf allgemeinen Textsammlungen vorzutrainieren und diese Modelle dann für spezifischere Aufgaben zu spezialisieren. Wir werden später in diesem Kurs mehr über [Natural Language Processing](../5-NLP/README.md) lernen.

## 🚀 Herausforderung

Machen Sie eine Internet-Recherche, um herauszufinden, wo Ihrer Meinung nach KI am effektivsten eingesetzt wird. Ist es in einer Karten-App, einem Sprach-zu-Text-Dienst oder einem Videospiel? Recherchieren Sie, wie das System aufgebaut wurde.

## [Quiz nach der Vorlesung](https://ff-quizzes.netlify.app/en/ai/quiz/2)

## Rückblick & Selbststudium

Überblicken Sie die Geschichte der KI und des maschinellen Lernens, indem Sie [diese Lektion](https://github.com/microsoft/ML-For-Beginners/tree/main/1-Introduction/2-history-of-ML) durchlesen. Nehmen Sie ein Element aus der Sketchnote am Anfang dieser Lektion oder dieser hier und recherchieren Sie es genauer, um den kulturellen Kontext zu verstehen, der seine Entwicklung beeinflusst hat.

**Aufgabe**: [Game Jam](assignment.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Haftungsausschluss**:  
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner ursprünglichen Sprache sollte als maßgebliche Quelle betrachtet werden. Für kritische Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die sich aus der Nutzung dieser Übersetzung ergeben.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->