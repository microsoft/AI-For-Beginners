# Autoencoder

Beim Training von CNNs besteht eines der Probleme darin, dass wir eine große Menge an beschrifteten Daten benötigen. Im Falle der Bildklassifikation müssen wir Bilder in verschiedene Klassen unterteilen, was einen manuellen Aufwand erfordert.

## [Vorlesungsquiz](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/109)

Wir möchten jedoch möglicherweise rohe (unbeschriftete) Daten für das Training von CNN-Feature-Extraktoren verwenden, was als **selbstüberwachtes Lernen** bezeichnet wird. Anstelle von Beschriftungen verwenden wir Trainingsbilder sowohl als Eingabe als auch als Ausgabe des Netzwerks. Die Hauptidee des **Autoencoders** ist, dass wir ein **Encoder-Netzwerk** haben, das das Eingangsbild in einen **latent space** (normalerweise ein Vektor einer kleineren Größe) umwandelt, und dann das **Decoder-Netzwerk**, dessen Ziel es ist, das ursprüngliche Bild wiederherzustellen.

> ✅ Ein [Autoencoder](https://wikipedia.org/wiki/Autoencoder) ist "eine Art künstliches neuronales Netzwerk, das verwendet wird, um effiziente Kodierungen von unbeschrifteten Daten zu lernen."

Da wir einen Autoencoder trainieren, um so viele Informationen wie möglich aus dem ursprünglichen Bild für eine genaue Rekonstruktion zu erfassen, versucht das Netzwerk, die beste **Einbettung** der Eingabebilder zu finden, um die Bedeutung zu erfassen.

![AutoEncoder Diagramm](../../../../../translated_images/autoencoder_schema.5e6fc9ad98a5eb6197f3513cf3baf4dfbe1389a6ae74daebda64de9f1c99f142.de.jpg)

> Bild von [Keras Blog](https://blog.keras.io/building-autoencoders-in-keras.html)

## Szenarien für die Verwendung von Autoencodern

Obwohl die Rekonstruktion ursprünglicher Bilder an sich nicht nützlich erscheint, gibt es einige Szenarien, in denen Autoencoder besonders nützlich sind:

* **Reduzierung der Dimension von Bildern zur Visualisierung** oder **Training von Bild-Einbettungen**. In der Regel liefern Autoencoder bessere Ergebnisse als PCA, da sie die räumliche Natur von Bildern und hierarchische Merkmale berücksichtigen.
* **Rauschunterdrückung**, d.h. das Entfernen von Rauschen aus dem Bild. Da Rauschen viele nutzlose Informationen enthält, kann der Autoencoder diese nicht alle in den relativ kleinen latenten Raum einfügen und erfasst daher nur den wichtigen Teil des Bildes. Beim Training von Rauschunterdrückern beginnen wir mit den Originalbildern und verwenden Bilder mit künstlich hinzugefügtem Rauschen als Eingabe für den Autoencoder.
* **Superauflösung**, d.h. Erhöhung der Bildauflösung. Wir beginnen mit hochauflösenden Bildern und verwenden das Bild mit niedrigerer Auflösung als Eingabe für den Autoencoder.
* **Generative Modelle**. Sobald wir den Autoencoder trainiert haben, kann der Decoder-Teil verwendet werden, um neue Objekte aus zufälligen latenten Vektoren zu erstellen.

## Variationale Autoencoder (VAE)

Traditionelle Autoencoder reduzieren die Dimension der Eingabedaten auf irgendeine Weise, indem sie die wichtigen Merkmale der Eingabebilder herausfinden. Allerdings machen latente Vektoren oft nicht viel Sinn. Mit anderen Worten, wenn wir das MNIST-Dataset als Beispiel nehmen, ist es keine einfache Aufgabe herauszufinden, welche Ziffern verschiedenen latenten Vektoren entsprechen, da nahe latente Vektoren nicht unbedingt den gleichen Ziffern entsprechen.

Andererseits ist es besser, um *generative* Modelle zu trainieren, ein gewisses Verständnis des latenten Raums zu haben. Diese Idee führt uns zu **variational auto-encoder** (VAE).

VAE ist der Autoencoder, der lernt, die *statistische Verteilung* der latenten Parameter, die sogenannte **latente Verteilung**, vorherzusagen. Zum Beispiel möchten wir, dass latente Vektoren normal verteilt sind mit einem Mittelwert z<sub>mean</sub> und einer Standardabweichung z<sub>sigma</sub> (sowohl Mittelwert als auch Standardabweichung sind Vektoren einer bestimmten Dimension d). Der Encoder in VAE lernt, diese Parameter vorherzusagen, und dann nimmt der Decoder einen zufälligen Vektor aus dieser Verteilung, um das Objekt zu rekonstruieren.

Zusammenfassend:

 * Vom Eingangsvektor sagen wir `z_mean` und `z_log_sigma` voraus (anstatt die Standardabweichung selbst vorherzusagen, sagen wir ihren Logarithmus voraus)
 * Wir ziehen einen Vektor `sample` aus der Verteilung N(z<sub>mean</sub>,exp(z<sub>log\_sigma</sub>))
 * Der Decoder versucht, das ursprüngliche Bild unter Verwendung von `sample` als Eingangsvektor zu decodieren

 <img src="images/vae.png" width="50%">

> Bild von [diesem Blogbeitrag](https://ijdykeman.github.io/ml/2016/12/21/cvae.html) von Isaak Dykeman

Variationale Autoencoder verwenden eine komplexe Verlustfunktion, die aus zwei Teilen besteht:

* **Rekonstruktionsverlust** ist die Verlustfunktion, die zeigt, wie nah ein rekonstruiertes Bild am Zielbild ist (es kann der Mittlere Quadratische Fehler, oder MSE, sein). Es ist dieselbe Verlustfunktion wie bei normalen Autoencodern.
* **KL-Verlust**, der sicherstellt, dass die Verteilungen der latenten Variablen nahe an der Normalverteilung bleiben. Er basiert auf dem Konzept der [Kullback-Leibler-Divergenz](https://www.countbayesie.com/blog/2017/5/9/kullback-leibler-divergence-explained) - eine Metrik zur Schätzung, wie ähnlich zwei statistische Verteilungen sind.

Ein wichtiger Vorteil von VAEs ist, dass sie es uns ermöglichen, relativ einfach neue Bilder zu generieren, da wir wissen, aus welcher Verteilung wir latente Vektoren ziehen können. Wenn wir beispielsweise VAE mit einem 2D-latenten Vektor auf MNIST trainieren, können wir dann die Komponenten des latenten Vektors variieren, um verschiedene Ziffern zu erhalten:

<img alt="vaemnist" src="images/vaemnist.png" width="50%"/>

> Bild von [Dmitry Soshnikov](http://soshnikov.com)

Beobachten Sie, wie die Bilder ineinander übergehen, während wir latente Vektoren aus verschiedenen Bereichen des latenten Parameterraums erhalten. Wir können diesen Raum auch in 2D visualisieren:

<img alt="vaemnist cluster" src="images/vaemnist-diag.png" width="50%"/> 

> Bild von [Dmitry Soshnikov](http://soshnikov.com)

## ✍️ Übungen: Autoencoder

Erfahren Sie mehr über Autoencoder in diesen entsprechenden Notizbüchern:

* [Autoencoders in TensorFlow](../../../../../lessons/4-ComputerVision/09-Autoencoders/AutoencodersTF.ipynb)
* [Autoencoders in PyTorch](../../../../../lessons/4-ComputerVision/09-Autoencoders/AutoEncodersPyTorch.ipynb)

## Eigenschaften von Autoencodern

* **Daten-spezifisch** - sie funktionieren nur gut mit der Art von Bildern, auf denen sie trainiert wurden. Wenn wir beispielsweise ein Superauflösungsnetzwerk auf Blumen trainieren, wird es bei Porträts nicht gut abschneiden. Das liegt daran, dass das Netzwerk ein hochauflösendes Bild erzeugen kann, indem es feine Details aus den im Trainingsdatensatz gelernten Merkmalen entnimmt.
* **Verlustbehaftet** - das rekonstruierte Bild ist nicht dasselbe wie das ursprüngliche Bild. Die Art des Verlusts wird durch die *Verlustfunktion* definiert, die während des Trainings verwendet wird.
* Funktioniert mit **unbeschrifteten Daten**.

## [Nachlese-Quiz](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/209)

## Fazit

In dieser Lektion haben Sie die verschiedenen Arten von Autoencodern kennengelernt, die für den KI-Wissenschaftler verfügbar sind. Sie haben gelernt, wie man sie baut und wie man sie zur Rekonstruktion von Bildern verwendet. Sie haben auch über den VAE gelernt und wie man ihn verwendet, um neue Bilder zu generieren.

## 🚀 Herausforderung

In dieser Lektion haben Sie gelernt, wie man Autoencoder für Bilder verwendet. Aber sie können auch für Musik verwendet werden! Schauen Sie sich das Projekt [MusicVAE](https://magenta.tensorflow.org/music-vae) des Magenta-Projekts an, das Autoencoder verwendet, um zu lernen, Musik zu rekonstruieren. Machen Sie einige [Experimente](https://colab.research.google.com/github/magenta/magenta-demos/blob/master/colab-notebooks/Multitrack_MusicVAE.ipynb) mit dieser Bibliothek, um zu sehen, was Sie erstellen können.

## [Nachlese-Quiz](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/208)

## Überprüfung & Selbststudium

Zur Referenz lesen Sie mehr über Autoencoder in diesen Ressourcen:

* [Autoencoder in Keras erstellen](https://blog.keras.io/building-autoencoders-in-keras.html)
* [Blogbeitrag auf NeuroHive](https://neurohive.io/ru/osnovy-data-science/variacionnyj-avtojenkoder-vae/)
* [Variationale Autoencoder erklärt](https://kvfrans.com/variational-autoencoders-explained/)
* [Bedingte Variationale Autoencoder](https://ijdykeman.github.io/ml/2016/12/21/cvae.html)

## Aufgabe

Am Ende von [diesem Notizbuch mit TensorFlow](../../../../../lessons/4-ComputerVision/09-Autoencoders/AutoencodersTF.ipynb) finden Sie eine 'Aufgabe' - verwenden Sie dies als Ihre Aufgabe.

**Haftungsausschluss**:  
Dieses Dokument wurde mit maschinellen KI-Übersetzungsdiensten übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner ursprünglichen Sprache sollte als autoritative Quelle betrachtet werden. Für kritische Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Verantwortung für Missverständnisse oder Fehlinterpretationen, die aus der Verwendung dieser Übersetzung entstehen.