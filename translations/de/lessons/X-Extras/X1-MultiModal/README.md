# Multi-Modale Netzwerke

Nach dem Erfolg von Transformer-Modellen bei der Lösung von NLP-Aufgaben wurden ähnliche Architekturen auch auf Aufgaben der Computer Vision angewendet. Es gibt ein wachsendes Interesse daran, Modelle zu entwickeln, die Vision- und Sprachfähigkeiten *kombinieren*. Ein solcher Versuch wurde von OpenAI unternommen und nennt sich CLIP und DALL.E.

## Contrastive Image Pre-Training (CLIP)

Die Hauptidee von CLIP ist, Textaufforderungen mit einem Bild vergleichen zu können und zu bestimmen, wie gut das Bild zur Aufforderung passt.

![CLIP Architektur](../../../../../lessons/X-Extras/X1-MultiModal/images/clip-arch.png)

> *Bild aus [diesem Blogbeitrag](https://openai.com/blog/clip/)*

Das Modell wird mit Bildern aus dem Internet und deren Beschreibungen trainiert. Für jede Batch nehmen wir N Paare aus (Bild, Text) und konvertieren sie in Vektorrepräsentationen I, ..., I / T, ..., T. Diese Repräsentationen werden dann miteinander abgeglichen. Die Verlustfunktion ist so definiert, dass die Kosinusähnlichkeit zwischen den Vektoren eines Paares (z. B. I und T) maximiert und die Kosinusähnlichkeit zwischen allen anderen Paaren minimiert wird. Aus diesem Grund wird dieser Ansatz als **kontrastiv** bezeichnet.

Die CLIP-Bibliothek/Modell ist verfügbar auf [OpenAI GitHub](https://github.com/openai/CLIP). Der Ansatz wird in [diesem Blogbeitrag](https://openai.com/blog/clip/) beschrieben und ausführlicher in [diesem Paper](https://arxiv.org/pdf/2103.00020.pdf).

Sobald dieses Modell vortrainiert ist, können wir ihm eine Batch von Bildern und eine Batch von Textaufforderungen geben, und es wird einen Tensor mit Wahrscheinlichkeiten zurückgeben. CLIP kann für verschiedene Aufgaben verwendet werden:

**Bildklassifikation**

Angenommen, wir müssen Bilder zwischen Katzen, Hunden und Menschen klassifizieren. In diesem Fall können wir dem Modell ein Bild und eine Reihe von Textaufforderungen geben: "*ein Bild einer Katze*", "*ein Bild eines Hundes*", "*ein Bild eines Menschen*". Im resultierenden Vektor mit 3 Wahrscheinlichkeiten müssen wir nur den Index mit dem höchsten Wert auswählen.

![CLIP für Bildklassifikation](../../../../../lessons/X-Extras/X1-MultiModal/images/clip-class.png)

> *Bild aus [diesem Blogbeitrag](https://openai.com/blog/clip/)*

**Textbasierte Bildsuche**

Wir können auch das Gegenteil tun. Wenn wir eine Sammlung von Bildern haben, können wir diese Sammlung dem Modell übergeben und eine Textaufforderung - dies wird uns das Bild geben, das am ähnlichsten zur gegebenen Aufforderung ist.

## ✍️ Beispiel: [CLIP für Bildklassifikation und Bildsuche verwenden](../../../../../lessons/X-Extras/X1-MultiModal/Clip.ipynb)

Öffne das [Clip.ipynb](../../../../../lessons/X-Extras/X1-MultiModal/Clip.ipynb)-Notebook, um CLIP in Aktion zu sehen.

## Bildgenerierung mit VQGAN+CLIP

CLIP kann auch für die **Bildgenerierung** aus einer Textaufforderung verwendet werden. Dazu benötigen wir ein **Generator-Modell**, das Bilder basierend auf einer Vektoreingabe generieren kann. Eines dieser Modelle nennt sich [VQGAN](https://compvis.github.io/taming-transformers/) (Vector-Quantized GAN).

Die Hauptideen von VQGAN, die es von gewöhnlichen [GAN](../../4-ComputerVision/10-GANs/README.md) unterscheiden, sind folgende:
* Verwendung einer autoregressiven Transformer-Architektur, um eine Sequenz kontextreicher visueller Teile zu generieren, die das Bild zusammensetzen. Diese visuellen Teile werden wiederum von [CNN](../../4-ComputerVision/07-ConvNets/README.md) gelernt.
* Einsatz eines Sub-Bild-Diskriminators, der erkennt, ob Teile des Bildes "echt" oder "gefälscht" sind (im Gegensatz zum "Alles-oder-Nichts"-Ansatz bei traditionellen GANs).

Erfahre mehr über VQGAN auf der [Taming Transformers](https://compvis.github.io/taming-transformers/) Webseite.

Ein wichtiger Unterschied zwischen VQGAN und traditionellen GANs ist, dass letztere ein brauchbares Bild aus jedem Eingabevektor erzeugen können, während VQGAN wahrscheinlich ein Bild erzeugt, das nicht kohärent ist. Daher müssen wir den Bildgenerierungsprozess weiter steuern, und das kann mit CLIP erfolgen.

![VQGAN+CLIP Architektur](../../../../../lessons/X-Extras/X1-MultiModal/images/vqgan.png)

Um ein Bild zu erzeugen, das einer Textaufforderung entspricht, beginnen wir mit einem zufälligen Codierungsvektor, der durch VQGAN geleitet wird, um ein Bild zu erzeugen. Dann wird CLIP verwendet, um eine Verlustfunktion zu erzeugen, die zeigt, wie gut das Bild zur Textaufforderung passt. Ziel ist es, diesen Verlust zu minimieren, indem die Parameter des Eingabevektors mittels Backpropagation angepasst werden.

Eine großartige Bibliothek, die VQGAN+CLIP implementiert, ist [Pixray](http://github.com/pixray/pixray).

![Bild von Pixray erzeugt](../../../../../lessons/X-Extras/X1-MultiModal/images/a_closeup_watercolor_portrait_of_young_male_teacher_of_literature_with_a_book.png) |  ![Bild von Pixray erzeugt](../../../../../lessons/X-Extras/X1-MultiModal/images/a_closeup_oil_portrait_of_young_female_teacher_of_computer_science_with_a_computer.png) | ![Bild von Pixray erzeugt](../../../../../lessons/X-Extras/X1-MultiModal/images/a_closeup_oil_portrait_of_old_male_teacher_of_math.png)
----|----|----
Bild generiert aus der Aufforderung *ein Nahaufnahme-Aquarellporträt eines jungen männlichen Literaturlehrers mit einem Buch* | Bild generiert aus der Aufforderung *ein Nahaufnahme-Ölporträt einer jungen weiblichen Informatiklehrerin mit einem Computer* | Bild generiert aus der Aufforderung *ein Nahaufnahme-Ölporträt eines alten männlichen Mathematiklehrers vor einer Tafel*

> Bilder aus der **Artificial Teachers**-Sammlung von [Dmitry Soshnikov](http://soshnikov.com)

## DALL-E
### [DALL-E 1](https://openai.com/research/dall-e)
DALL-E ist eine Version von GPT-3, die darauf trainiert ist, Bilder aus Aufforderungen zu generieren. Es wurde mit 12 Milliarden Parametern trainiert.

Im Gegensatz zu CLIP erhält DALL-E sowohl Text als auch Bild als einen einzigen Strom von Tokens für Bilder und Text. Daher können aus mehreren Aufforderungen Bilder basierend auf dem Text generiert werden.

### [DALL-E 2](https://openai.com/dall-e-2)
Der Hauptunterschied zwischen DALL-E 1 und 2 besteht darin, dass es realistischere Bilder und Kunstwerke erzeugt.

Beispiele für Bildgenerierungen mit DALL-E:
![Bild von DALL-E erzeugt](../../../../../lessons/X-Extras/X1-MultiModal/images/DALL·E%202023-06-20%2015.56.56%20-%20a%20closeup%20watercolor%20portrait%20of%20young%20male%20teacher%20of%20literature%20with%20a%20book.png) |  ![Bild von DALL-E erzeugt](../../../../../lessons/X-Extras/X1-MultiModal/images/DALL·E%202023-06-20%2015.57.43%20-%20a%20closeup%20oil%20portrait%20of%20young%20female%20teacher%20of%20computer%20science%20with%20a%20computer.png) | ![Bild von DALL-E erzeugt](../../../../../lessons/X-Extras/X1-MultiModal/images/DALL·E%202023-06-20%2015.58.42%20-%20%20a%20closeup%20oil%20portrait%20of%20old%20male%20teacher%20of%20mathematics%20in%20front%20of%20blackboard.png)
----|----|----
Bild generiert aus der Aufforderung *ein Nahaufnahme-Aquarellporträt eines jungen männlichen Literaturlehrers mit einem Buch* | Bild generiert aus der Aufforderung *ein Nahaufnahme-Ölporträt einer jungen weiblichen Informatiklehrerin mit einem Computer* | Bild generiert aus der Aufforderung *ein Nahaufnahme-Ölporträt eines alten männlichen Mathematiklehrers vor einer Tafel*

## Referenzen

* VQGAN Paper: [Taming Transformers for High-Resolution Image Synthesis](https://compvis.github.io/taming-transformers/paper/paper.pdf)
* CLIP Paper: [Learning Transferable Visual Models From Natural Language Supervision](https://arxiv.org/pdf/2103.00020.pdf)

**Haftungsausschluss**:  
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner ursprünglichen Sprache sollte als maßgebliche Quelle betrachtet werden. Für kritische Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die sich aus der Nutzung dieser Übersetzung ergeben.