<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "1c6b8c7c1778a35fc1139b7f2aecb7b3",
  "translation_date": "2025-08-26T07:34:01+00:00",
  "source_file": "lessons/3-NeuralNetworks/README.md",
  "language_code": "tr"
}
-->
# Sinir Ağlarına Giriş

![Sinir Ağlarına Giriş içeriğinin bir çizim özeti](../../../../translated_images/ai-neuralnetworks.1c687ae40bc86e834f497844866a26d3e0886650a67a4bbe29442e2f157d3b18.tr.png)

Giriş bölümünde tartıştığımız gibi, zekaya ulaşmanın yollarından biri bir **bilgisayar modeli** veya bir **yapay beyin** eğitmektir. 20. yüzyılın ortalarından itibaren, araştırmacılar farklı matematiksel modeller denediler ve son yıllarda bu yaklaşımın büyük ölçüde başarılı olduğu kanıtlandı. Beynin bu tür matematiksel modellerine **sinir ağları** denir.

> Bazen sinir ağlarına *Yapay Sinir Ağları* (Artificial Neural Networks, ANNs) denir, bu şekilde gerçek nöron ağlarından değil, modellerden bahsedildiği belirtilir.

## Makine Öğrenimi

Sinir Ağları, **Makine Öğrenimi** adı verilen daha geniş bir disiplinin parçasıdır. Bu disiplinin amacı, problemleri çözebilen bilgisayar modellerini eğitmek için verileri kullanmaktır. Makine Öğrenimi, Yapay Zekanın büyük bir bölümünü oluşturur, ancak bu müfredatta klasik Makine Öğrenimi konularını ele almıyoruz.

> Klasik Makine Öğrenimi hakkında daha fazla bilgi edinmek için ayrı **[Makine Öğrenimi Başlangıç Rehberi](http://github.com/microsoft/ml-for-beginners)** müfredatımıza göz atabilirsiniz.

Makine Öğreniminde, elimizde bazı örneklerden oluşan bir veri kümesi **X** ve buna karşılık gelen çıktı değerleri **Y** olduğunu varsayarız. Örnekler genellikle **özelliklerden** oluşan N boyutlu vektörlerdir ve çıktılara **etiketler** denir.

En yaygın iki makine öğrenimi problemini ele alacağız:

* **Sınıflandırma**, burada bir giriş nesnesini iki veya daha fazla sınıfa ayırmamız gerekir.
* **Regresyon**, burada her bir giriş örneği için sayısal bir değer tahmin etmemiz gerekir.

> Giriş ve çıkışları tensörler olarak temsil ederken, giriş veri kümesi M×N boyutunda bir matristir; burada M örnek sayısını, N ise özellik sayısını ifade eder. Çıktı etiketleri **Y**, M boyutunda bir vektördür.

Bu müfredatta yalnızca sinir ağı modellerine odaklanacağız.

## Bir Nöron Modeli

Biyolojiden biliyoruz ki beynimiz, her biri birden fazla "girişe" (akson) ve bir "çıkışa" (dendrit) sahip nöral hücrelerden oluşur. Aksonlar ve dendritler elektrik sinyalleri iletebilir ve aksonlar ile dendritler arasındaki bağlantılar, farklı iletkenlik dereceleri gösterebilir (nöromediyatörler tarafından kontrol edilir).

![Bir Nöron Modeli](../../../../translated_images/synapse-wikipedia.ed20a9e4726ea1c6a3ce8fec51c0b9bec6181946dca0fe4e829bc12fa3bacf01.tr.jpg) | ![Bir Nöron Modeli](../../../../translated_images/artneuron.1a5daa88d20ebe6f5824ddb89fba0bdaaf49f67e8230c1afbec42909df1fc17e.tr.png)
----|----
Gerçek Nöron *([Görsel](https://en.wikipedia.org/wiki/Synapse#/media/File:SynapseSchematic_lines.svg) Wikipedia'dan)* | Yapay Nöron *(Yazarın Görseli)*

Dolayısıyla, bir nöronun en basit matematiksel modeli, birkaç giriş **X<sub>1</sub>, ..., X<sub>N</sub>** ve bir çıkış **Y**, ayrıca bir dizi ağırlık **W<sub>1</sub>, ..., W<sub>N</sub>** içerir. Çıkış şu şekilde hesaplanır:

<img src="images/netout.png" alt="Y = f\left(\sum_{i=1}^N X_iW_i\right)" width="131" height="53" align="center"/>

burada **f**, bazı doğrusal olmayan **aktivasyon fonksiyonudur**.

> Nöronun erken modelleri, Warren McCullock ve Walter Pitts tarafından 1943'te yazılan klasik makale [A logical calculus of the ideas immanent in nervous activity](https://www.cs.cmu.edu/~./epxing/Class/10715/reading/McCulloch.and.Pitts.pdf)'de tanımlanmıştır. Donald Hebb, "[The Organization of Behavior: A Neuropsychological Theory](https://books.google.com/books?id=VNetYrB8EBoC)" adlı kitabında bu ağların nasıl eğitilebileceğini önermiştir.

## Bu Bölümde

Bu bölümde şunları öğreneceğiz:
* [Perceptron](03-Perceptron/README.md), iki sınıflı sınıflandırma için en erken sinir ağı modellerinden biri
* [Çok katmanlı ağlar](04-OwnFramework/README.md) ve eşlik eden defter [kendi çerçevemizi nasıl oluştururuz](../../../../lessons/3-NeuralNetworks/04-OwnFramework/OwnFramework.ipynb)
* [Sinir Ağı Çerçeveleri](05-Frameworks/README.md), şu defterlerle: [PyTorch](../../../../lessons/3-NeuralNetworks/05-Frameworks/IntroPyTorch.ipynb) ve [Keras/Tensorflow](../../../../lessons/3-NeuralNetworks/05-Frameworks/IntroKerasTF.ipynb)
* [Aşırı Uyum](../../../../lessons/3-NeuralNetworks/05-Frameworks)

**Feragatname**:  
Bu belge, AI çeviri hizmeti [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba göstersek de, otomatik çevirilerin hata veya yanlışlık içerebileceğini lütfen unutmayın. Belgenin orijinal dili, yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımından kaynaklanan yanlış anlamalar veya yanlış yorumlamalar için sorumluluk kabul etmiyoruz.