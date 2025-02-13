# Sinir Ağlarına Giriş

![Sinir Ağları içeriğinin özetini gösteren bir doodle](../../../../translated_images/ai-neuralnetworks.1c687ae40bc86e834f497844866a26d3e0886650a67a4bbe29442e2f157d3b18.tr.png)

Girişte tartıştığımız gibi, zeka elde etmenin yollarından biri bir **bilgisayar modeli** veya **yapay beyin** eğitmektir. 20. yüzyılın ortalarından beri araştırmacılar farklı matematiksel modeller denemiştir; son yıllarda bu yönün son derece başarılı olduğu kanıtlanmıştır. Beynin bu tür matematiksel modellerine **sinir ağları** denir.

> Bazen sinir ağlarına *Yapay Sinir Ağları* (Artificial Neural Networks), kısaca ANNs denir; bu, gerçek nöron ağlarından değil, modellerden bahsettiğimizi belirtmek içindir.

## Makine Öğrenimi

Sinir Ağları, **Makine Öğrenimi** adı verilen daha geniş bir disiplinin parçasıdır; bu disiplinin amacı verileri kullanarak sorunları çözebilen bilgisayar modelleri eğitmektir. Makine Öğrenimi, Yapay Zeka'nın büyük bir bölümünü oluşturur; ancak bu müfredatta klasik ML'yi ele almıyoruz.

> Klasik Makine Öğrenimi hakkında daha fazla bilgi edinmek için ayrı **[Makine Öğrenimi için Yeni Başlayanlar](http://github.com/microsoft/ml-for-beginners)** müfredatımıza göz atın.

Makine Öğrenimi'nde, elimizde bazı örneklerden oluşan bir veri seti **X** ve karşılık gelen çıktı değerleri **Y** olduğunu varsayıyoruz. Örnekler genellikle **özelliklerden** oluşan N-boyutlu vektörlerdir ve çıktılara **etiketler** denir.

İki en yaygın makine öğrenimi sorununu ele alacağız:

* **Sınıflandırma**, burada bir giriş nesnesini iki veya daha fazla sınıfa ayırmamız gerekir.
* **Regresyon**, burada her bir giriş örneği için bir sayısal değer tahmin etmemiz gerekir.

> Girişleri ve çıktıları tensörler olarak temsil ettiğimizde, giriş veri seti M×N boyutunda bir matristir; burada M örnek sayısını ve N özellik sayısını temsil eder. Çıktı etiketleri Y ise M boyutunda bir vektördür.

Bu müfredatta yalnızca sinir ağı modellerine odaklanacağız.

## Bir Nöron Modeli

Biyolojiden biliyoruz ki beynimiz, her biri birden fazla "giriş" (akson) ve bir çıkış (dendrit) olan sinir hücrelerinden oluşur. Aksonlar ve dendritler elektrik sinyallerini iletebilir ve aksonlar ile dendritler arasındaki bağlantılar farklı iletkenlik derecelerine sahip olabilir (nörotransmitterler tarafından kontrol edilir).

![Bir Nöron Modeli](../../../../translated_images/synapse-wikipedia.ed20a9e4726ea1c6a3ce8fec51c0b9bec6181946dca0fe4e829bc12fa3bacf01.tr.jpg) | ![Bir Nöron Modeli](../../../../translated_images/artneuron.1a5daa88d20ebe6f5824ddb89fba0bdaaf49f67e8230c1afbec42909df1fc17e.tr.png)
----|----
Gerçek Nöron *([Resim](https://en.wikipedia.org/wiki/Synapse#/media/File:SynapseSchematic_lines.svg) Wikipedia'dan)* | Yapay Nöron *(Yazarın Resmi)*

Böylece, bir nöronun en basit matematiksel modeli birkaç girişi X<sub>1</sub>, ..., X<sub>N</sub> ve bir çıkış Y ile birlikte bir dizi ağırlık W<sub>1</sub>, ..., W<sub>N</sub> içerir. Çıkış, şu şekilde hesaplanır:

<img src="images/netout.png" alt="Y = f\left(\sum_{i=1}^N X_iW_i\right)" width="131" height="53" align="center"/>

burada f bazı doğrusal olmayan **aktivasyon fonksiyonu**dur.

> Nöronun ilk modelleri, Warren McCullock ve Walter Pitts'in 1943'teki [A logical calculus of the ideas immanent in nervous activity](https://www.cs.cmu.edu/~./epxing/Class/10715/reading/McCulloch.and.Pitts.pdf) adlı klasik makalesinde tanımlanmıştır. Donald Hebb, "[The Organization of Behavior: A Neuropsychological Theory](https://books.google.com/books?id=VNetYrB8EBoC)" adlı kitabında bu ağların nasıl eğitileceğini önermiştir.

## Bu Bölümde

Bu bölümde şunları öğreneceğiz:
* [Perceptron](03-Perceptron/README.md), iki sınıflı sınıflandırma için en erken sinir ağı modellerinden biri
* [Çok katmanlı ağlar](04-OwnFramework/README.md) ve eşleşen not defteri [kendi çerçevemizi nasıl oluşturacağımız](../../../../lessons/3-NeuralNetworks/04-OwnFramework/OwnFramework.ipynb)
* [Sinir Ağı Çerçeveleri](05-Frameworks/README.md), bu not defterleri ile: [PyTorch](../../../../lessons/3-NeuralNetworks/05-Frameworks/IntroPyTorch.ipynb) ve [Keras/Tensorflow](../../../../lessons/3-NeuralNetworks/05-Frameworks/IntroKerasTF.ipynb)
* [Aşırı Uydurma](../../../../lessons/3-NeuralNetworks/05-Frameworks)

**Sorumluluk Reddi**:  
Bu belge, makine tabanlı yapay zeka çeviri hizmetleri kullanılarak çevrilmiştir. Doğruluk için çaba göstersek de, otomatik çevirilerin hatalar veya yanlışlıklar içerebileceğini lütfen unutmayın. Orijinal belge, kendi dilinde otorite kaynağı olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilmektedir. Bu çevirinin kullanılması sonucu ortaya çıkabilecek yanlış anlamalar veya yanlış yorumlamalardan sorumlu değiliz.