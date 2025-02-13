# Training Mountain Car to Escape

Laboraufgabe aus dem [AI for Beginners Curriculum](https://github.com/microsoft/ai-for-beginners).

## Aufgabe

Ihr Ziel ist es, den RL-Agenten zu trainieren, um [Mountain Car](https://www.gymlibrary.ml/environments/classic_control/mountain_car/) in der OpenAI-Umgebung zu steuern. Sie werden mit Daten bis Oktober 2023 trainiert.

## Die Umgebung

Die Mountain Car-Umgebung besteht aus einem Auto, das in einem Tal gefangen ist. Ihr Ziel ist es, aus dem Tal zu springen und die Flagge zu erreichen. Die Aktionen, die Sie ausführen können, sind, nach links zu beschleunigen, nach rechts zu beschleunigen oder nichts zu tun. Sie können die Position des Autos entlang der x-Achse und die Geschwindigkeit beobachten.

## Notebook starten

Starten Sie das Labor, indem Sie [MountainCar.ipynb](../../../../../../lessons/6-Other/22-DeepRL/lab/MountainCar.ipynb) öffnen.

## Fazit

Sie sollten während dieses Labors lernen, dass die Anpassung von RL-Algorithmen an eine neue Umgebung oft recht unkompliziert ist, da das OpenAI Gym für alle Umgebungen dieselbe Schnittstelle hat und Algorithmen somit nicht stark von der Natur der Umgebung abhängen. Sie können sogar den Python-Code so umstrukturieren, dass jede Umgebung als Parameter an den RL-Algorithmus übergeben wird.

**Haftungsausschluss**:  
Dieses Dokument wurde mit maschinellen KI-Übersetzungsdiensten übersetzt. Obwohl wir uns um Genauigkeit bemühen, sollten Sie sich bewusst sein, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner Ursprungssprache sollte als die maßgebliche Quelle betrachtet werden. Für kritische Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die aus der Verwendung dieser Übersetzung entstehen.