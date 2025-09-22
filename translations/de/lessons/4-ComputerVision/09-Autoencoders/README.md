<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "0b306c04f5337b6e7430e5c0b16bb5c0",
  "translation_date": "2025-08-24T09:33:46+00:00",
  "source_file": "lessons/4-ComputerVision/09-Autoencoders/README.md",
  "language_code": "de"
}
-->
# Autoencoder

Beim Training von CNNs besteht eines der Probleme darin, dass wir viele gelabelte Daten benötigen. Im Fall der Bildklassifikation müssen wir Bilder in verschiedene Klassen unterteilen, was manuell erfolgen muss.

## [Quiz vor der Vorlesung](https://ff-quizzes.netlify.app/en/ai/quiz/17)

Wir möchten jedoch möglicherweise rohe (nicht gelabelte) Daten verwenden, um CNN-Feature-Extraktoren zu trainieren, was als **selbstüberwachtes Lernen** bezeichnet wird. Anstelle von Labels verwenden wir Trainingsbilder sowohl als Netzwerkeingabe als auch als -ausgabe. Die Hauptidee des **Autoencoders** besteht darin, dass wir ein **Encoder-Netzwerk** haben, das das Eingabebild in einen **latenten Raum** umwandelt (normalerweise ist dies einfach ein Vektor mit kleinerer Größe), und dann ein **Decoder-Netzwerk**, dessen Ziel es ist, das ursprüngliche Bild zu rekonstruieren.

> ✅ Ein [Autoencoder](https://wikipedia.org/wiki/Autoencoder) ist "eine Art künstliches neuronales Netzwerk, das verwendet wird, um effiziente Kodierungen von nicht gelabelten Daten zu lernen."

Da wir einen Autoencoder trainieren, um so viele Informationen wie möglich aus dem ursprünglichen Bild für eine genaue Rekonstruktion zu erfassen, versucht das Netzwerk, die beste **Einbettung** der Eingabebilder zu finden, um die Bedeutung zu erfassen.

![AutoEncoder Diagramm](../../../../../lessons/4-ComputerVision/09-Autoencoders/images/autoencoder_schema.jpg)

> Bild von [Keras Blog](https://blog.keras.io/building-autoencoders-in-keras.html)

## Szenarien für die Verwendung von Autoencodern

Obwohl die Rekonstruktion ursprünglicher Bilder an sich nicht nützlich erscheint, gibt es einige Szenarien, in denen Autoencoder besonders hilfreich sind:

* **Reduzierung der Dimension von Bildern zur Visualisierung** oder **Training von Bild-Einbettungen**. Autoencoder liefern normalerweise bessere Ergebnisse als PCA, da sie die räumliche Natur von Bildern und hierarchische Merkmale berücksichtigen.
* **Rauschunterdrückung**, d.h. das Entfernen von Rauschen aus dem Bild. Da Rauschen viele unnütze Informationen enthält, kann der Autoencoder nicht alles in den relativ kleinen latenten Raum einpassen und erfasst daher nur den wichtigen Teil des Bildes. Beim Training von Rauschunterdrückern beginnen wir mit den ursprünglichen Bildern und verwenden Bilder mit künstlich hinzugefügtem Rauschen als Eingabe für den Autoencoder.
* **Superauflösung**, Erhöhung der Bildauflösung. Wir beginnen mit hochauflösenden Bildern und verwenden das Bild mit niedrigerer Auflösung als Eingabe für den Autoencoder.
* **Generative Modelle**. Sobald wir den Autoencoder trainiert haben, kann der Decoder-Teil verwendet werden, um neue Objekte aus zufälligen latenten Vektoren zu erstellen.

## Variationale Autoencoder (VAE)

Traditionelle Autoencoder reduzieren die Dimension der Eingabedaten auf irgendeine Weise und identifizieren die wichtigen Merkmale der Eingabebilder. Allerdings machen latente Vektoren oft wenig Sinn. Mit anderen Worten, wenn wir das MNIST-Dataset als Beispiel nehmen, ist es nicht einfach herauszufinden, welche Ziffern zu verschiedenen latenten Vektoren gehören, da nahe latente Vektoren nicht unbedingt denselben Ziffern entsprechen.

Um generative Modelle zu trainieren, ist es jedoch besser, ein Verständnis des latenten Raums zu haben. Diese Idee führt uns zu **variationalen Autoencodern** (VAE).

Ein VAE ist ein Autoencoder, der lernt, die *statistische Verteilung* der latenten Parameter vorherzusagen, die sogenannte **latente Verteilung**. Zum Beispiel möchten wir möglicherweise, dass latente Vektoren normal verteilt sind mit einem Mittelwert z<sub>mean</sub> und einer Standardabweichung z<sub>sigma</sub> (sowohl Mittelwert als auch Standardabweichung sind Vektoren einer bestimmten Dimensionalität d). Der Encoder im VAE lernt, diese Parameter vorherzusagen, und der Decoder nimmt dann einen zufälligen Vektor aus dieser Verteilung, um das Objekt zu rekonstruieren.

Zusammengefasst:

* Aus dem Eingabevektor sagen wir `z_mean` und `z_log_sigma` voraus (anstatt die Standardabweichung selbst vorherzusagen, sagen wir deren Logarithmus voraus).
* Wir entnehmen einen Vektor `sample` aus der Verteilung N(z<sub>mean</sub>,exp(z<sub>log\_sigma</sub>)).
* Der Decoder versucht, das ursprüngliche Bild mithilfe von `sample` als Eingabevektor zu dekodieren.

<img src="images/vae.png" width="50%">

> Bild aus [diesem Blogbeitrag](https://ijdykeman.github.io/ml/2016/12/21/cvae.html) von Isaak Dykeman

Variationale Autoencoder verwenden eine komplexe Verlustfunktion, die aus zwei Teilen besteht:

* **Rekonstruktionsverlust** ist die Verlustfunktion, die zeigt, wie nah ein rekonstruiertes Bild am Ziel ist (es kann Mean Squared Error oder MSE sein). Es ist dieselbe Verlustfunktion wie bei normalen Autoencodern.
* **KL-Verlust**, der sicherstellt, dass die Verteilung der latenten Variablen nahe an der Normalverteilung bleibt. Er basiert auf dem Konzept der [Kullback-Leibler-Divergenz](https://www.countbayesie.com/blog/2017/5/9/kullback-leibler-divergence-explained) - einem Maß zur Schätzung der Ähnlichkeit zweier statistischer Verteilungen.

Ein wichtiger Vorteil von VAEs ist, dass sie es uns ermöglichen, relativ einfach neue Bilder zu generieren, da wir wissen, aus welcher Verteilung wir latente Vektoren entnehmen müssen. Wenn wir beispielsweise einen VAE mit einem 2D-latenten Vektor auf MNIST trainieren, können wir dann die Komponenten des latenten Vektors variieren, um verschiedene Ziffern zu erhalten:

<img alt="vaemnist" src="images/vaemnist.png" width="50%"/>

> Bild von [Dmitry Soshnikov](http://soshnikov.com)

Beobachten Sie, wie Bilder ineinander übergehen, wenn wir beginnen, latente Vektoren aus verschiedenen Bereichen des latenten Parameterraums zu entnehmen. Wir können diesen Raum auch in 2D visualisieren:

<img alt="vaemnist cluster" src="images/vaemnist-diag.png" width="50%"/> 

> Bild von [Dmitry Soshnikov](http://soshnikov.com)

## ✍️ Übungen: Autoencoder

Erfahren Sie mehr über Autoencoder in den entsprechenden Notebooks:

* [Autoencoder in TensorFlow](../../../../../lessons/4-ComputerVision/09-Autoencoders/AutoencodersTF.ipynb)
* [Autoencoder in PyTorch](../../../../../lessons/4-ComputerVision/09-Autoencoders/AutoEncodersPyTorch.ipynb)

## Eigenschaften von Autoencodern

* **Daten-spezifisch** - sie funktionieren nur gut mit der Art von Bildern, auf denen sie trainiert wurden. Wenn wir beispielsweise ein Superauflösungsnetzwerk auf Blumen trainieren, wird es bei Porträts nicht gut funktionieren. Dies liegt daran, dass das Netzwerk ein hochauflösendes Bild erzeugen kann, indem es feine Details aus den Merkmalen des Trainingsdatensatzes entnimmt.
* **Verlustbehaftet** - das rekonstruierte Bild ist nicht identisch mit dem ursprünglichen Bild. Die Art des Verlusts wird durch die *Verlustfunktion* definiert, die während des Trainings verwendet wird.
* Funktioniert mit **nicht gelabelten Daten**

## [Quiz nach der Vorlesung](https://ff-quizzes.netlify.app/en/ai/quiz/18)

## Fazit

In dieser Lektion haben Sie die verschiedenen Arten von Autoencodern kennengelernt, die einem KI-Wissenschaftler zur Verfügung stehen. Sie haben gelernt, wie man sie erstellt und wie man sie verwendet, um Bilder zu rekonstruieren. Sie haben auch den VAE kennengelernt und erfahren, wie man ihn verwendet, um neue Bilder zu generieren.

## 🚀 Herausforderung

In dieser Lektion haben Sie gelernt, wie man Autoencoder für Bilder verwendet. Aber sie können auch für Musik verwendet werden! Schauen Sie sich das [MusicVAE](https://magenta.tensorflow.org/music-vae)-Projekt des Magenta-Projekts an, das Autoencoder verwendet, um Musik zu rekonstruieren. Machen Sie einige [Experimente](https://colab.research.google.com/github/magenta/magenta-demos/blob/master/colab-notebooks/Multitrack_MusicVAE.ipynb) mit dieser Bibliothek, um zu sehen, was Sie erstellen können.

## [Quiz nach der Vorlesung](https://ff-quizzes.netlify.app/en/ai/quiz/16)

## Überprüfung & Selbststudium

Lesen Sie zur Referenz mehr über Autoencoder in diesen Ressourcen:

* [Building Autoencoders in Keras](https://blog.keras.io/building-autoencoders-in-keras.html)
* [Blogbeitrag auf NeuroHive](https://neurohive.io/ru/osnovy-data-science/variacionnyj-avtojenkoder-vae/)
* [Variational Autoencoders Explained](https://kvfrans.com/variational-autoencoders-explained/)
* [Conditional Variational Autoencoders](https://ijdykeman.github.io/ml/2016/12/21/cvae.html)

## Aufgabe

Am Ende [dieses Notebooks mit TensorFlow](../../../../../lessons/4-ComputerVision/09-Autoencoders/AutoencodersTF.ipynb) finden Sie eine 'Aufgabe' - verwenden Sie diese als Ihre Aufgabe.

**Haftungsausschluss**:  
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner ursprünglichen Sprache sollte als maßgebliche Quelle betrachtet werden. Für kritische Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die sich aus der Nutzung dieser Übersetzung ergeben.