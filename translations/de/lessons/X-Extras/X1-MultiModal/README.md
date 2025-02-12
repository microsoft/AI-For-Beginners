# Multi-Modal Netzwerke

Nach dem Erfolg von Transformermodellen zur Lösung von NLP-Aufgaben wurden dieselben oder ähnliche Architekturen auf Aufgaben der Computer Vision angewendet. Das Interesse wächst, Modelle zu entwickeln, die die Fähigkeiten von Vision und natürlicher Sprache *kombinieren*. Ein solcher Versuch wurde von OpenAI unternommen und trägt den Namen CLIP und DALL.E.

## Kontrastives Bildvortraining (CLIP)

Die Hauptidee von CLIP besteht darin, Textaufforderungen mit einem Bild zu vergleichen und zu bestimmen, wie gut das Bild zur Aufforderung passt.

![CLIP Architektur](../../../../../translated_images/clip-arch.b3dbf20b4e8ed8be1c38e2bc6100fd3cc257c33cda4692b301be91f791b13ea7.de.png)

> *Bild aus [diesem Blogbeitrag](https://openai.com/blog/clip/)*

Das Modell wird mit Bildern aus dem Internet und deren Beschreibungen trainiert. Für jede Batch nehmen wir N Paare von (Bild, Text) und wandeln sie in einige Vektorrepräsentationen um. Diese Repräsentationen werden dann zusammengeführt. Die Verlustfunktion ist so definiert, dass die Kosinusähnlichkeit zwischen Vektoren eines Paares (z.B. I und T) maximiert und die Kosinusähnlichkeit zwischen allen anderen Paaren minimiert wird. Das ist der Grund, warum dieser Ansatz als **kontrastiv** bezeichnet wird.

Das CLIP-Modell/bibliothek ist von [OpenAI GitHub](https://github.com/openai/CLIP) verfügbar. Der Ansatz wird in [diesem Blogbeitrag](https://openai.com/blog/clip/) beschrieben und detaillierter in [diesem Papier](https://arxiv.org/pdf/2103.00020.pdf).

Sobald dieses Modell vortrainiert ist, können wir ihm eine Batch von Bildern und eine Batch von Textaufforderungen geben, und es wird uns den Tensor mit Wahrscheinlichkeiten zurückgeben. CLIP kann für mehrere Aufgaben verwendet werden:

**Bildklassifikation**

Angenommen, wir müssen Bilder zwischen, sagen wir, Katzen, Hunden und Menschen klassifizieren. In diesem Fall können wir dem Modell ein Bild und eine Reihe von Textaufforderungen geben: "*ein Bild einer Katze*", "*ein Bild eines Hundes*", "*ein Bild eines Menschen*". In dem resultierenden Vektor von 3 Wahrscheinlichkeiten müssen wir nur den Index mit dem höchsten Wert auswählen.

![CLIP für Bildklassifikation](../../../../../translated_images/clip-class.3af42ef0b2b19369a633df5f20ddf4f5a01d6c8ffa181e9d3a0572c19f919f72.de.png)

> *Bild aus [diesem Blogbeitrag](https://openai.com/blog/clip/)*

**Textbasierte Bildsuche**

Wir können auch das Gegenteil tun. Wenn wir eine Sammlung von Bildern haben, können wir diese Sammlung dem Modell übergeben und eine Textaufforderung - das wird uns das Bild zurückgeben, das der gegebenen Aufforderung am ähnlichsten ist.

## ✍️ Beispiel: [CLIP für Bildklassifikation und Bildsuche verwenden](../../../../../lessons/X-Extras/X1-MultiModal/Clip.ipynb)

Öffnen Sie das [Clip.ipynb](../../../../../lessons/X-Extras/X1-MultiModal/Clip.ipynb) Notizbuch, um CLIP in Aktion zu sehen.

## Bildgenerierung mit VQGAN+ CLIP

CLIP kann auch für die **Bildgenerierung** aus einer Textaufforderung verwendet werden. Um dies zu tun, benötigen wir ein **Generator-Modell**, das in der Lage ist, Bilder basierend auf einem Vektor-Input zu erzeugen. Eines dieser Modelle wird [VQGAN](https://compvis.github.io/taming-transformers/) (Vektor-Quantisierter GAN) genannt.

Die Hauptideen von VQGAN, die es von gewöhnlichen [GAN](../../4-ComputerVision/10-GANs/README.md) unterscheiden, sind die folgenden:
* Verwendung einer autoregressiven Transformer-Architektur zur Generierung einer Sequenz von kontextreichen visuellen Teilen, die das Bild zusammensetzen. Diese visuellen Teile werden wiederum von [CNN](../../4-ComputerVision/07-ConvNets/README.md) gelernt.
* Verwendung eines Subbild-Discriminators, der erkennt, ob Teile des Bildes "echt" oder "falsch" sind (im Gegensatz zu dem "Alles-oder-Nichts"-Ansatz in traditionellen GANs).

Erfahren Sie mehr über VQGAN auf der Website [Taming Transformers](https://compvis.github.io/taming-transformers/).

Einer der wichtigen Unterschiede zwischen VQGAN und traditionellen GAN ist, dass letztere aus jedem Eingangsvektor ein annehmbares Bild erzeugen können, während VQGAN wahrscheinlich ein Bild erzeugt, das nicht kohärent wäre. Daher müssen wir den Bildschaffungsprozess weiter leiten, und das kann mit CLIP erfolgen.

![VQGAN+CLIP Architektur](../../../../../translated_images/vqgan.5027fe05051dfa3101950cfa930303f66e6478b9bd273e83766731796e462d9b.de.png)

Um ein Bild zu erzeugen, das einer Textaufforderung entspricht, beginnen wir mit einem zufälligen Kodierungsvektor, der durch VQGAN geleitet wird, um ein Bild zu erzeugen. Dann wird CLIP verwendet, um eine Verlustfunktion zu erzeugen, die zeigt, wie gut das Bild zur Textaufforderung passt. Das Ziel ist es dann, diesen Verlust zu minimieren, indem wir die Eingangsvektorparameter mittels Rückpropagation anpassen.

Eine großartige Bibliothek, die VQGAN+CLIP implementiert, ist [Pixray](http://github.com/pixray/pixray).

![Bild von Pixray erzeugt](../../../../../translated_images/a_closeup_watercolor_portrait_of_young_male_teacher_of_literature_with_a_book.2384968e9db8a0d09dc96de938b9f95bde8a7e1c721f48f286a7795bf16d56c7.de.png) |  ![Bild von Pixray erzeugt](../../../../../translated_images/a_closeup_oil_portrait_of_young_female_teacher_of_computer_science_with_a_computer.e0b6495f210a439077e1c32cc8afdf714e634fe24dc78dc5aa45fd2f560b0ed5.de.png) | ![Bild von Pixray erzeugt](../../../../../translated_images/a_closeup_oil_portrait_of_old_male_teacher_of_math.5362e67aa7fc2683b9d36a613b364deb7454760cd39205623fc1e3938fa133c0.de.png)
----|----|----
Bild erzeugt aus der Aufforderung *ein Nahaufnahme-Aquarell-Porträt eines jungen männlichen Lehrers für Literatur mit einem Buch* | Bild erzeugt aus der Aufforderung *ein Nahaufnahme-Öl-Porträt einer jungen weiblichen Lehrerin für Informatik mit einem Computer* | Bild erzeugt aus der Aufforderung *ein Nahaufnahme-Öl-Porträt eines alten männlichen Lehrers für Mathematik vor einer Tafel*

> Bilder aus der Sammlung **Künstliche Lehrer** von [Dmitry Soshnikov](http://soshnikov.com)

## DALL-E
### [DALL-E 1](https://openai.com/research/dall-e)
DALL-E ist eine Version von GPT-3, die darauf trainiert wurde, Bilder aus Aufforderungen zu generieren. Es wurde mit 12 Milliarden Parametern trainiert.

Im Gegensatz zu CLIP erhält DALL-E sowohl Text als auch Bild als einen einzigen Stream von Tokens für Bilder und Text. Daher können Sie aus mehreren Aufforderungen Bilder basierend auf dem Text generieren.

### [DALL-E 2](https://openai.com/dall-e-2)
Der Hauptunterschied zwischen DALL-E 1 und 2 besteht darin, dass es realistischere Bilder und Kunstwerke generiert.

Beispiele für Bildgenerierungen mit DALL-E:
![Bild von Pixray erzeugt](../../../../../translated_images/DALL·E%202023-06-20%2015.56.56%20-%20a%20closeup%20watercolor%20portrait%20of%20young%20male%20teacher%20of%20literature%20with%20a%20book.6c235e8271d9ed10ce985d86aeb241a58518958647973af136912116b9518fce.de.png) |  ![Bild von Pixray erzeugt](../../../../../translated_images/DALL·E%202023-06-20%2015.57.43%20-%20a%20closeup%20oil%20portrait%20of%20young%20female%20teacher%20of%20computer%20science%20with%20a%20computer.f21dc4166340b6c8b4d1cb57efd1e22127407f9b28c9ac7afe11344065369e64.de.png) | ![Bild von Pixray erzeugt](../../../../../translated_images/DALL·E%202023-06-20%2015.58.42%20-%20%20a%20closeup%20oil%20portrait%20of%20old%20male%20teacher%20of%20mathematics%20in%20front%20of%20blackboard.d331c2dfbdc3f7c46aa65c0809066f5e7ed4b49609cd259852e760df21051e4a.de.png)
----|----|----
Bild erzeugt aus der Aufforderung *ein Nahaufnahme-Aquarell-Porträt eines jungen männlichen Lehrers für Literatur mit einem Buch* | Bild erzeugt aus der Aufforderung *ein Nahaufnahme-Öl-Porträt einer jungen weiblichen Lehrerin für Informatik mit einem Computer* | Bild erzeugt aus der Aufforderung *ein Nahaufnahme-Öl-Porträt eines alten männlichen Lehrers für Mathematik vor einer Tafel*

## Referenzen

* VQGAN Papier: [Taming Transformers for High-Resolution Image Synthesis](https://compvis.github.io/taming-transformers/paper/paper.pdf)
* CLIP Papier: [Learning Transferable Visual Models From Natural Language Supervision](https://arxiv.org/pdf/2103.00020.pdf)

**Haftungsausschluss**:  
Dieses Dokument wurde mithilfe von maschinellen KI-Übersetzungsdiensten übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner ursprünglichen Sprache sollte als maßgebliche Quelle betrachtet werden. Für kritische Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die aus der Verwendung dieser Übersetzung entstehen.