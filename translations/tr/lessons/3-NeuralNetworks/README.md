<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "5abc5f7978919be90cd313f0c20e8228",
  "translation_date": "2025-09-07T14:32:22+00:00",
  "source_file": "lessons/3-NeuralNetworks/README.md",
  "language_code": "tr"
}
-->
# Sinir Ağlarına Giriş

![Sinir Ağları Giriş içeriğinin bir çizim özeti](../../../../translated_images/ai-neuralnetworks.1c687ae40bc86e834f497844866a26d3e0886650a67a4bbe29442e2f157d3b18.tr.png)

Giriş bölümünde tartıştığımız gibi, zekaya ulaşmanın yollarından biri bir **bilgisayar modeli** veya bir **yapay beyin** eğitmekten geçer. 20. yüzyılın ortalarından itibaren araştırmacılar farklı matematiksel modeller denediler ve son yıllarda bu yaklaşım büyük ölçüde başarılı oldu. Beynin bu tür matematiksel modellerine **sinir ağları** denir.

> Bazen sinir ağlarına *Yapay Sinir Ağları* (Artificial Neural Networks, ANNs) denir, böylece gerçek nöron ağlarından değil, modellerden bahsettiğimiz anlaşılır.

## Makine Öğrenimi

Sinir Ağları, **Makine Öğrenimi** adı verilen daha geniş bir disiplinin parçasıdır. Makine Öğrenimi'nin amacı, verileri kullanarak problemleri çözebilen bilgisayar modelleri eğitmektir. Makine Öğrenimi, Yapay Zeka'nın büyük bir bölümünü oluşturur, ancak bu müfredatta klasik Makine Öğrenimi'ni ele almıyoruz.

> Klasik Makine Öğrenimi hakkında daha fazla bilgi edinmek için ayrı **[Başlangıç Seviyesi için Makine Öğrenimi](http://github.com/microsoft/ml-for-beginners)** müfredatımıza göz atabilirsiniz.

Makine Öğrenimi'nde, elimizde bazı örneklerden oluşan bir veri seti **X** ve buna karşılık gelen çıktı değerleri **Y** olduğunu varsayarız. Örnekler genellikle **özelliklerden** oluşan N boyutlu vektörlerdir ve çıktılara **etiketler** denir.

En yaygın iki makine öğrenimi problemini ele alacağız:

* **Sınıflandırma**, burada bir giriş nesnesini iki veya daha fazla sınıfa ayırmamız gerekir.
* **Regresyon**, burada her bir giriş örneği için bir sayısal değer tahmin etmemiz gerekir.

> Giriş ve çıkışları tensörler olarak temsil ederken, giriş veri seti M×N boyutunda bir matristir; burada M örnek sayısını ve N özellik sayısını ifade eder. Çıkış etiketleri **Y**, M boyutunda bir vektördür.

Bu müfredatta yalnızca sinir ağı modellerine odaklanacağız.

## Bir Nöron Modeli

Biyolojiden biliyoruz ki beynimiz, her biri birden fazla "girişe" (akson) ve bir çıkışa (dendrit) sahip olan sinir hücrelerinden oluşur. Aksonlar ve dendritler elektrik sinyalleri iletebilir ve aksonlar ile dendritler arasındaki bağlantılar farklı iletkenlik dereceleri gösterebilir (nöromediyatörler tarafından kontrol edilir).

![Bir Nöron Modeli](../../../../translated_images/synapse-wikipedia.ed20a9e4726ea1c6a3ce8fec51c0b9bec6181946dca0fe4e829bc12fa3bacf01.tr.jpg) | ![Bir Nöron Modeli](../../../../translated_images/artneuron.1a5daa88d20ebe6f5824ddb89fba0bdaaf49f67e8230c1afbec42909df1fc17e.tr.png)
----|----
Gerçek Nöron *([Wikipedia'dan Görsel](https://en.wikipedia.org/wiki/Synapse#/media/File:SynapseSchematic_lines.svg))* | Yapay Nöron *(Yazarın Görseli)*

Dolayısıyla, bir nöronun en basit matematiksel modeli birkaç giriş **X<sub>1</sub>, ..., X<sub>N</sub>** ve bir çıkış **Y** ile bir dizi ağırlık **W<sub>1</sub>, ..., W<sub>N</sub>** içerir. Çıkış şu şekilde hesaplanır:

<img src="images/netout.png" alt="Y = f\left(\sum_{i=1}^N X_iW_i\right)" width="131" height="53" align="center"/>

burada **f**, bazı doğrusal olmayan **aktivasyon fonksiyonudur**.

> Nöronun erken modelleri, Warren McCullock ve Walter Pitts tarafından 1943 yılında yazılan klasik makale [Sinirsel Aktivitede İçkin Fikirlerin Mantıksal Hesaplaması](https://www.cs.cmu.edu/~./epxing/Class/10715/reading/McCulloch.and.Pitts.pdf) içinde tanımlanmıştır. Donald Hebb, "[Davranışın Organizasyonu: Bir Nöropsikolojik Teori](https://books.google.com/books?id=VNetYrB8EBoC)" adlı kitabında bu ağların nasıl eğitilebileceğini önermiştir.

## Bu Bölümde

Bu bölümde şunları öğreneceğiz:
* [Perceptron](03-Perceptron/README.md), iki sınıflı sınıflandırma için en erken sinir ağı modellerinden biri
* [Çok Katmanlı Ağlar](04-OwnFramework/README.md) ve eşlik eden not defteri [kendi çerçevemizi nasıl oluştururuz](04-OwnFramework/OwnFramework.ipynb)
* [Sinir Ağı Çerçeveleri](05-Frameworks/README.md), şu not defterleriyle: [PyTorch](05-Frameworks/IntroPyTorch.ipynb) ve [Keras/Tensorflow](05-Frameworks/IntroKerasTF.ipynb)
* [Aşırı Uyum](../../../../lessons/3-NeuralNetworks/05-Frameworks)

---

**Feragatname**:  
Bu belge, AI çeviri hizmeti [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba göstersek de, otomatik çevirilerin hata veya yanlışlıklar içerebileceğini lütfen unutmayın. Belgenin orijinal dili, yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımından kaynaklanan yanlış anlamalar veya yanlış yorumlamalar için sorumluluk kabul etmiyoruz.