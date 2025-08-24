<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "5d1cbc67a9690adb5b33adf297794087",
  "translation_date": "2025-08-24T09:33:15+00:00",
  "source_file": "lessons/1-Intro/README.md",
  "language_code": "de"
}
-->
> Bild von [Dmitry Soshnikov](http://soshnikov.com)

Mit der Zeit wurden Rechenressourcen günstiger, und es standen mehr Daten zur Verfügung, sodass Ansätze mit neuronalen Netzwerken in vielen Bereichen, wie z. B. der Computer-Vision oder der Spracherkennung, große Fortschritte zeigten und mit Menschen konkurrieren konnten. In den letzten zehn Jahren wurde der Begriff Künstliche Intelligenz (KI) größtenteils als Synonym für neuronale Netzwerke verwendet, da die meisten Erfolge der KI, von denen wir hören, auf diesen basieren.

Wir können beobachten, wie sich die Ansätze verändert haben, zum Beispiel bei der Entwicklung eines Schachprogramms:

* Frühe Schachprogramme basierten auf Suchalgorithmen – ein Programm versuchte explizit, mögliche Züge eines Gegners für eine bestimmte Anzahl von Zügen im Voraus abzuschätzen und wählte den optimalen Zug basierend auf der besten Position, die in wenigen Zügen erreicht werden konnte. Dies führte zur Entwicklung des sogenannten [Alpha-Beta-Suchalgorithmus](https://de.wikipedia.org/wiki/Alpha-Beta-Suche).
* Suchstrategien funktionieren gut gegen Ende des Spiels, wenn der Suchraum durch eine geringe Anzahl möglicher Züge begrenzt ist. Zu Beginn des Spiels ist der Suchraum jedoch riesig, und der Algorithmus kann durch das Lernen aus bestehenden Partien zwischen menschlichen Spielern verbessert werden. Spätere Experimente nutzten das sogenannte [fallbasierte Schließen](https://de.wikipedia.org/wiki/Fallbasiertes_Schlie%C3%9Fen), bei dem das Programm in der Wissensdatenbank nach Fällen suchte, die der aktuellen Spielsituation sehr ähnlich sind.
* Moderne Programme, die menschliche Spieler besiegen, basieren auf neuronalen Netzwerken und [Reinforcement Learning](https://de.wikipedia.org/wiki/Best%C3%A4rkendes_Lernen), bei dem die Programme allein durch das Spielen gegen sich selbst über einen langen Zeitraum lernen und aus ihren eigenen Fehlern lernen – ähnlich wie Menschen, wenn sie Schach spielen lernen. Ein Computerprogramm kann jedoch viel mehr Partien in viel kürzerer Zeit spielen und somit viel schneller lernen.

✅ Recherchieren Sie ein wenig über andere Spiele, die von KI gespielt wurden.

Ähnlich können wir sehen, wie sich der Ansatz zur Entwicklung von „sprechenden Programmen“ (die den Turing-Test bestehen könnten) verändert hat:

* Frühe Programme dieser Art, wie [Eliza](https://de.wikipedia.org/wiki/ELIZA), basierten auf sehr einfachen grammatikalischen Regeln und der Umformulierung des Eingabesatzes in eine Frage.
* Moderne Assistenten wie Cortana, Siri oder Google Assistant sind hybride Systeme, die neuronale Netzwerke nutzen, um Sprache in Text umzuwandeln und unsere Absicht zu erkennen, und dann einige logische Schlussfolgerungen oder explizite Algorithmen anwenden, um die erforderlichen Aktionen auszuführen.
* In der Zukunft können wir erwarten, dass ein vollständig neuronales Modell den Dialog eigenständig bewältigt. Die neueren neuronalen Netzwerke der GPT- und [Turing-NLG](https://turing.microsoft.com/)-Familie zeigen in diesem Bereich große Erfolge.

> Bild von Dmitry Soshnikov, [Foto](https://unsplash.com/photos/r8LmVbUKgns) von [Marina Abrosimova](https://unsplash.com/@abrosimova_marina_foto), Unsplash

## Aktuelle KI-Forschung

Das enorme Wachstum der Forschung zu neuronalen Netzwerken begann um 2010, als große öffentliche Datensätze verfügbar wurden. Eine riesige Sammlung von Bildern namens [ImageNet](https://en.wikipedia.org/wiki/ImageNet), die etwa 14 Millionen annotierte Bilder enthält, führte zur [ImageNet Large Scale Visual Recognition Challenge](https://image-net.org/challenges/LSVRC/).

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

In den letzten Jahren haben wir große Erfolge mit großen Sprachmodellen wie BERT und GPT-3 erlebt. Dies geschah vor allem aufgrund der Tatsache, dass es eine große Menge an allgemeinen Textdaten gibt, die es uns ermöglichen, Modelle zu trainieren, um die Struktur und Bedeutung von Texten zu erfassen, sie auf allgemeinen Textsammlungen vorzutrainieren und diese Modelle dann für spezifischere Aufgaben zu spezialisieren. Wir werden später in diesem Kurs mehr über [Natural Language Processing](../5-NLP/README.md) lernen.

## 🚀 Herausforderung

Machen Sie eine Internetrecherche, um herauszufinden, wo KI Ihrer Meinung nach am effektivsten eingesetzt wird. Ist es in einer Karten-App, einem Sprach-zu-Text-Dienst oder einem Videospiel? Recherchieren Sie, wie das System aufgebaut wurde.

## [Quiz nach der Vorlesung](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/201)

## Rückblick & Selbststudium

Überblicken Sie die Geschichte der KI und des maschinellen Lernens, indem Sie [diese Lektion](https://github.com/microsoft/ML-For-Beginners/tree/main/1-Introduction/2-history-of-ML) durchlesen. Nehmen Sie ein Element aus der Sketchnote am Anfang dieser oder jener Lektion und recherchieren Sie es genauer, um den kulturellen Kontext zu verstehen, der seine Entwicklung beeinflusst hat.

**Aufgabe**: [Game Jam](assignment.md)

**Haftungsausschluss**:  
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, weisen wir darauf hin, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner ursprünglichen Sprache sollte als maßgebliche Quelle betrachtet werden. Für kritische Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die sich aus der Nutzung dieser Übersetzung ergeben.