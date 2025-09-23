<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "0c84b280e654e05ed658023021a6a975",
  "translation_date": "2025-09-23T12:20:36+00:00",
  "source_file": "lessons/1-Intro/README.md",
  "language_code": "de"
}
-->
# Einführung in KI

![Zusammenfassung des Inhalts der Einführung in KI in einer Skizze](../../../../translated_images/ai-intro.bf28d1ac4235881c096f0ffdb320ba4102940eafcca4e9d7a55a03914361f8f3.de.png)

> Skizze von [Tomomi Imura](https://twitter.com/girlie_mac)

## [Quiz vor der Vorlesung](https://ff-quizzes.netlify.app/en/ai/quiz/1)

**Künstliche Intelligenz** ist eine faszinierende wissenschaftliche Disziplin, die untersucht, wie wir Computer dazu bringen können, intelligentes Verhalten zu zeigen, z. B. Dinge zu tun, die Menschen gut können.

Ursprünglich wurden Computer von [Charles Babbage](https://en.wikipedia.org/wiki/Charles_Babbage) erfunden, um Zahlen nach einem klar definierten Verfahren – einem Algorithmus – zu verarbeiten. Moderne Computer, obwohl sie erheblich fortschrittlicher sind als das ursprüngliche Modell aus dem 19. Jahrhundert, folgen immer noch derselben Idee kontrollierter Berechnungen. Daher ist es möglich, einen Computer so zu programmieren, dass er etwas tut, wenn wir die genaue Abfolge der Schritte kennen, die erforderlich sind, um das Ziel zu erreichen.

![Foto einer Person](../../../../translated_images/dsh_age.d212a30d4e54fb5f68b94a624aad64bc086124bcbbec9561ae5bd5da661e22d8.de.png)

> Foto von [Vickie Soshnikova](http://twitter.com/vickievalerie)

> ✅ Das Alter einer Person anhand ihres Fotos zu bestimmen, ist eine Aufgabe, die nicht explizit programmiert werden kann, da wir nicht wissen, wie wir die Zahl in unserem Kopf ermitteln, wenn wir dies tun.

---

Es gibt jedoch einige Aufgaben, bei denen wir nicht genau wissen, wie wir sie lösen können. Betrachten Sie das Bestimmen des Alters einer Person anhand ihres Fotos. Wir lernen es irgendwie, weil wir viele Beispiele von Menschen unterschiedlichen Alters gesehen haben, aber wir können nicht genau erklären, wie wir es tun, noch können wir den Computer dazu programmieren. Genau solche Aufgaben sind für die **Künstliche Intelligenz** (kurz KI) von Interesse.

✅ Überlegen Sie sich einige Aufgaben, die Sie einem Computer überlassen könnten und die von KI profitieren würden. Denken Sie an die Bereiche Finanzen, Medizin und Kunst – wie profitieren diese Bereiche heute von KI?

## Schwache KI vs. Starke KI

Schwache KI | Starke KI
---------------------------------------|-------------------------------------
Schwache KI bezieht sich auf KI-Systeme, die für eine bestimmte Aufgabe oder eine begrenzte Anzahl von Aufgaben entwickelt und trainiert wurden.|Starke KI, oder Allgemeine Künstliche Intelligenz (AGI), bezieht sich auf KI-Systeme mit menschlicher Intelligenz und Verständnis.
Diese KI-Systeme sind nicht allgemein intelligent; sie sind darauf spezialisiert, eine vordefinierte Aufgabe auszuführen, besitzen jedoch kein echtes Verständnis oder Bewusstsein.|Diese KI-Systeme können jede intellektuelle Aufgabe ausführen, die ein Mensch bewältigen kann, sich an verschiedene Bereiche anpassen und eine Form von Bewusstsein oder Selbstwahrnehmung besitzen.
Beispiele für schwache KI sind virtuelle Assistenten wie Siri oder Alexa, Empfehlungsalgorithmen von Streaming-Diensten und Chatbots, die für spezifische Kundenservice-Aufgaben entwickelt wurden.|Das Erreichen von starker KI ist ein langfristiges Ziel der KI-Forschung und würde die Entwicklung von KI-Systemen erfordern, die in der Lage sind, zu argumentieren, zu lernen, zu verstehen und sich über eine Vielzahl von Aufgaben und Kontexten anzupassen.
Schwache KI ist hochspezialisiert und besitzt keine menschlichen kognitiven Fähigkeiten oder allgemeine Problemlösungsfähigkeiten außerhalb ihres begrenzten Bereichs.|Starke KI ist derzeit ein theoretisches Konzept, und kein KI-System hat dieses Niveau allgemeiner Intelligenz erreicht.

Weitere Informationen finden Sie unter **[Artificial General Intelligence](https://en.wikipedia.org/wiki/Artificial_general_intelligence)** (AGI).

## Die Definition von Intelligenz und der Turing-Test

Eines der Probleme bei der Auseinandersetzung mit dem Begriff **[Intelligenz](https://en.wikipedia.org/wiki/Intelligence)** ist, dass es keine klare Definition dieses Begriffs gibt. Man könnte argumentieren, dass Intelligenz mit **abstraktem Denken** oder **Selbstbewusstsein** verbunden ist, aber wir können sie nicht richtig definieren.

![Foto einer Katze](../../../../translated_images/photo-cat.8c8e8fb760ffe45725c5b9f6b0d954e9bf114475c01c55adf0303982851b7eae.de.jpg)

> [Foto](https://unsplash.com/photos/75715CVEJhI) von [Amber Kipp](https://unsplash.com/@sadmax) von Unsplash

Um die Mehrdeutigkeit des Begriffs *Intelligenz* zu verdeutlichen, versuchen Sie, die Frage zu beantworten: "Ist eine Katze intelligent?". Verschiedene Menschen neigen dazu, unterschiedliche Antworten auf diese Frage zu geben, da es keinen allgemein akzeptierten Test gibt, um die Behauptung zu beweisen oder zu widerlegen. Und wenn Sie denken, es gäbe einen – versuchen Sie, Ihre Katze einem IQ-Test zu unterziehen...

✅ Denken Sie eine Minute darüber nach, wie Sie Intelligenz definieren. Ist eine Krähe, die ein Labyrinth lösen kann, um an Nahrung zu gelangen, intelligent? Ist ein Kind intelligent?

---

Wenn wir über AGI sprechen, müssen wir eine Möglichkeit haben, festzustellen, ob wir ein wirklich intelligentes System geschaffen haben. [Alan Turing](https://en.wikipedia.org/wiki/Alan_Turing) schlug eine Methode vor, die als **[Turing-Test](https://en.wikipedia.org/wiki/Turing_test)** bekannt ist und gleichzeitig als Definition von Intelligenz dient. Der Test vergleicht ein gegebenes System mit etwas inhärent Intelligenten – einem echten Menschen. Da jeder automatische Vergleich von einem Computerprogramm umgangen werden kann, verwenden wir einen menschlichen Fragesteller. Wenn ein Mensch nicht in der Lage ist, zwischen einer echten Person und einem Computersystem in einem textbasierten Dialog zu unterscheiden, wird das System als intelligent angesehen.

> Ein Chatbot namens [Eugene Goostman](https://en.wikipedia.org/wiki/Eugene_Goostman), entwickelt in St. Petersburg, kam 2014 dem Bestehen des Turing-Tests nahe, indem er einen cleveren Persönlichkeitstrick anwandte. Er gab von Anfang an an, ein 13-jähriger ukrainischer Junge zu sein, was das mangelnde Wissen und einige Unstimmigkeiten im Text erklären würde. Der Bot überzeugte 30 % der Richter, dass er ein Mensch sei, nach einem fünfminütigen Dialog – eine Metrik, die Turing glaubte, dass eine Maschine bis 2000 erreichen könnte. Man sollte jedoch verstehen, dass dies nicht bedeutet, dass wir ein intelligentes System geschaffen haben oder dass ein Computersystem den menschlichen Fragesteller getäuscht hat – die Menschen wurden nicht vom System getäuscht, sondern von den Bot-Entwicklern!

✅ Wurden Sie jemals von einem Chatbot getäuscht und dachten, Sie sprechen mit einem Menschen? Wie hat er Sie überzeugt?

## Verschiedene Ansätze für KI

Wenn wir möchten, dass ein Computer sich wie ein Mensch verhält, müssen wir irgendwie unsere Denkweise im Computer modellieren. Folglich müssen wir versuchen zu verstehen, was einen Menschen intelligent macht.

> Um Intelligenz in eine Maschine programmieren zu können, müssen wir verstehen, wie unsere eigenen Entscheidungsprozesse funktionieren. Wenn Sie ein wenig Selbstreflexion betreiben, werden Sie feststellen, dass einige Prozesse unbewusst ablaufen – z. B. können wir eine Katze von einem Hund unterscheiden, ohne darüber nachzudenken – während andere Überlegungen erfordern.

Es gibt zwei mögliche Ansätze für dieses Problem:

Top-down-Ansatz (symbolisches Denken) | Bottom-up-Ansatz (Neuronale Netze)
---------------------------------------|-------------------------------------
Ein Top-down-Ansatz modelliert die Art und Weise, wie eine Person denkt, um ein Problem zu lösen. Es beinhaltet das Extrahieren von **Wissen** von einem Menschen und das Darstellen in einer computerlesbaren Form. Außerdem müssen wir eine Möglichkeit entwickeln, **Denken** im Computer zu modellieren. | Ein Bottom-up-Ansatz modelliert die Struktur des menschlichen Gehirns, bestehend aus einer großen Anzahl einfacher Einheiten, den **Neuronen**. Jedes Neuron agiert wie ein gewichteter Durchschnitt seiner Eingaben, und wir können ein Netzwerk von Neuronen trainieren, um nützliche Probleme zu lösen, indem wir **Trainingsdaten** bereitstellen.

Es gibt auch einige andere mögliche Ansätze zur Intelligenz:

* Ein **Emergenter**, **Synergetischer** oder **Multi-Agenten-Ansatz** basiert auf der Tatsache, dass komplexes intelligentes Verhalten durch die Interaktion einer großen Anzahl einfacher Agenten entstehen kann. Laut [evolutionärer Kybernetik](https://en.wikipedia.org/wiki/Global_brain#Evolutionary_cybernetics) kann Intelligenz im Prozess des *Metasystem-Übergangs* aus einfacheren, reaktiven Verhaltensweisen *entstehen*.

* Ein **Evolutionärer Ansatz** oder **genetischer Algorithmus** ist ein Optimierungsprozess, der auf den Prinzipien der Evolution basiert.

Wir werden diese Ansätze später im Kurs betrachten, aber jetzt konzentrieren wir uns auf zwei Hauptrichtungen: Top-down und Bottom-up.

### Der Top-Down-Ansatz

Beim **Top-down-Ansatz** versuchen wir, unser Denken zu modellieren. Da wir unseren Gedanken folgen können, wenn wir denken, können wir versuchen, diesen Prozess zu formalisieren und ihn im Computer zu programmieren. Dies wird als **symbolisches Denken** bezeichnet.

Menschen neigen dazu, einige Regeln im Kopf zu haben, die ihre Entscheidungsprozesse leiten. Zum Beispiel kann ein Arzt bei der Diagnose eines Patienten feststellen, dass eine Person Fieber hat und daher möglicherweise eine Entzündung im Körper vorliegt. Durch die Anwendung einer großen Anzahl von Regeln auf ein spezifisches Problem kann ein Arzt möglicherweise die endgültige Diagnose stellen.

Dieser Ansatz stützt sich stark auf **Wissensrepräsentation** und **Denken**. Wissen von einem menschlichen Experten zu extrahieren, könnte der schwierigste Teil sein, da ein Arzt in vielen Fällen nicht genau weiß, warum er oder sie zu einer bestimmten Diagnose kommt. Manchmal kommt die Lösung einfach in seinem oder ihrem Kopf auf, ohne explizites Denken. Einige Aufgaben, wie das Bestimmen des Alters einer Person anhand eines Fotos, können überhaupt nicht auf die Manipulation von Wissen reduziert werden.

### Bottom-Up-Ansatz

Alternativ können wir versuchen, die einfachsten Elemente in unserem Gehirn – ein Neuron – zu modellieren. Wir können ein sogenanntes **künstliches neuronales Netzwerk** im Computer konstruieren und dann versuchen, es durch Beispiele zu trainieren, um Probleme zu lösen. Dieser Prozess ähnelt dem, wie ein neugeborenes Kind seine Umgebung durch Beobachtungen kennenlernt.

✅ Recherchieren Sie ein wenig, wie Babys lernen. Was sind die grundlegenden Elemente des Gehirns eines Babys?

> | Was ist mit ML?         |      |
> |--------------|-----------|
> | Ein Teil der Künstlichen Intelligenz, der darauf basiert, dass ein Computer lernt, ein Problem anhand von Daten zu lösen, wird als **Maschinelles Lernen** bezeichnet. Wir werden klassisches maschinelles Lernen in diesem Kurs nicht behandeln – wir verweisen Sie auf den separaten Lehrplan [Machine Learning for Beginners](http://aka.ms/ml-beginners). |   ![ML für Anfänger](../../../../translated_images/ml-for-beginners.9e4fed176fd5817d7d1f7d358302515186579cbf09b2a6c5bd8092b345da7f22.de.png)    |

## Eine kurze Geschichte der KI

Künstliche Intelligenz wurde Mitte des zwanzigsten Jahrhunderts als Forschungsfeld ins Leben gerufen. Ursprünglich war symbolisches Denken der vorherrschende Ansatz, und es führte zu einer Reihe wichtiger Erfolge, wie Expertensystemen – Computerprogrammen, die in begrenzten Problembereichen als Experten agieren konnten. Es wurde jedoch bald klar, dass dieser Ansatz nicht gut skalierbar ist. Wissen von einem Experten zu extrahieren, es im Computer darzustellen und die Wissensbasis aktuell zu halten, erwies sich als sehr komplexe und in vielen Fällen zu teure Aufgabe. Dies führte in den 1970er Jahren zum sogenannten [KI-Winter](https://en.wikipedia.org/wiki/AI_winter).

<img alt="Kurze Geschichte der KI" src="images/history-of-ai.png" width="70%"/>

> Bild von [Dmitry Soshnikov](http://soshnikov.com)

Mit der Zeit wurden Computerressourcen günstiger, und es standen mehr Daten zur Verfügung, sodass neuronale Netzwerkansätze in vielen Bereichen wie Computer Vision oder Sprachverständnis große Leistungen zeigten. Im letzten Jahrzehnt wurde der Begriff Künstliche Intelligenz meist als Synonym für neuronale Netzwerke verwendet, da die meisten Erfolge der KI, von denen wir hören, auf ihnen basieren.

Wir können beobachten, wie sich die Ansätze geändert haben, beispielsweise bei der Entwicklung eines Schachspiel-Computerprogramms:

* Frühe Schachprogramme basierten auf der Suche – ein Programm versuchte explizit, mögliche Züge eines Gegners für eine bestimmte Anzahl von nächsten Zügen abzuschätzen und wählte einen optimalen Zug basierend auf der optimalen Position, die in wenigen Zügen erreicht werden kann. Dies führte zur Entwicklung des sogenannten [Alpha-Beta-Suchalgorithmus](https://en.wikipedia.org/wiki/Alpha%E2%80%93beta_pruning).
* Suchstrategien funktionieren gut gegen Ende des Spiels, wo der Suchraum durch eine geringe Anzahl möglicher Züge begrenzt ist. Am Anfang des Spiels ist der Suchraum jedoch riesig, und der Algorithmus kann durch Lernen aus bestehenden Partien zwischen menschlichen Spielern verbessert werden. Nachfolgende Experimente verwendeten sogenanntes [Fallbasiertes Denken](https://en.wikipedia.org/wiki/Case-based_reasoning), bei dem das Programm nach Fällen in der Wissensbasis suchte, die der aktuellen Position im Spiel sehr ähnlich sind.
* Moderne Programme, die menschliche Spieler besiegen, basieren auf neuronalen Netzwerken und [Verstärkungslernen](https://en.wikipedia.org/wiki/Reinforcement_learning), bei dem die Programme ausschließlich durch langes Spielen gegen sich selbst lernen und aus ihren eigenen Fehlern lernen – ähnlich wie Menschen, wenn sie Schach lernen. Ein Computerprogramm kann jedoch viel mehr Spiele in viel kürzerer Zeit spielen und somit viel schneller lernen.

✅ Recherchieren Sie ein wenig über andere Spiele, die von KI gespielt wurden.

Ähnlich können wir sehen, wie sich der Ansatz zur Erstellung von „sprechenden Programmen“ (die den Turing-Test bestehen könnten) geändert hat:

* Frühe Programme dieser Art, wie [Eliza](https://en.wikipedia.org/wiki/ELIZA), basierten auf sehr einfachen grammatikalischen Regeln und der Umformulierung des Eingabesatzes in eine Frage.
* Moderne Assistenten wie Cortana, Siri oder Google Assistant sind alle hybride Systeme, die neuronale Netzwerke verwenden, um Sprache in Text umzuwandeln und unsere Absicht zu erkennen, und dann einige Denkprozesse oder explizite Algorithmen anwenden, um die erforderlichen Aktionen auszuführen.
* In Zukunft können wir erwarten, dass ein vollständiges neuronales Modell den Dialog selbstständig handhabt. Die jüngsten GPT- und [Turing-NLG](https://turing.microsoft.com/)-Familien von neuronalen Netzwerken zeigen große Erfolge in diesem Bereich.

<img alt="Die Entwicklung des Turing-Tests" src="images/turing-test-evol.png" width="70%"/>
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

In den letzten Jahren haben wir große Erfolge mit großen Sprachmodellen wie BERT und GPT-3 erlebt. Dies geschah vor allem aufgrund der Tatsache, dass es eine große Menge an allgemeinen Textdaten gibt, die es uns ermöglichen, Modelle zu trainieren, um die Struktur und Bedeutung von Texten zu erfassen, sie auf allgemeinen Textsammlungen vorzutrainieren und diese Modelle dann für spezifischere Aufgaben zu spezialisieren. Mehr über [Natural Language Processing](../5-NLP/README.md) werden wir später in diesem Kurs lernen.

## 🚀 Herausforderung

Machen Sie eine Internet-Recherche, um herauszufinden, wo KI Ihrer Meinung nach am effektivsten eingesetzt wird. Ist es in einer Karten-App, einem Sprach-zu-Text-Dienst oder einem Videospiel? Recherchieren Sie, wie das System aufgebaut wurde.

## [Quiz nach der Vorlesung](https://ff-quizzes.netlify.app/en/ai/quiz/2)

## Rückblick & Selbststudium

Überblicken Sie die Geschichte der KI und des maschinellen Lernens, indem Sie [diese Lektion](https://github.com/microsoft/ML-For-Beginners/tree/main/1-Introduction/2-history-of-ML) durchlesen. Nehmen Sie ein Element aus der Sketchnote am Anfang dieser Lektion oder dieser hier und recherchieren Sie es genauer, um den kulturellen Kontext zu verstehen, der seine Entwicklung beeinflusst hat.

**Aufgabe**: [Game Jam](assignment.md)

---

