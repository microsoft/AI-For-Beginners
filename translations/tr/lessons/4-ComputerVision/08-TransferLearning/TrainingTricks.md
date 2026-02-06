# Derin Öğrenme Eğitim İpuçları

Sinir ağları derinleştikçe, bu ağların eğitimi daha da zorlaşır. Ana sorunlardan biri, [kaybolan gradyanlar](https://en.wikipedia.org/wiki/Vanishing_gradient_problem) veya [patlayan gradyanlar](https://deepai.org/machine-learning-glossary-and-terms/exploding-gradient-problem#:~:text=Exploding%20gradients%20are%20a%20problem,updates%20are%20small%20and%20controlled.) olarak adlandırılan problemdir. [Bu yazı](https://towardsdatascience.com/the-vanishing-exploding-gradient-problem-in-deep-neural-networks-191358470c11), bu sorunlara iyi bir giriş sağlar.

Derin ağların eğitimini daha verimli hale getirmek için kullanılabilecek birkaç teknik vardır.

## Değerleri Makul Bir Aralıkta Tutmak

Sayısal hesaplamaları daha kararlı hale getirmek için, sinir ağımızdaki tüm değerlerin genellikle [-1..1] veya [0..1] gibi makul bir ölçekte olduğundan emin olmak isteriz. Bu çok katı bir gereklilik olmasa da, kayan nokta hesaplamalarının doğası gereği farklı büyüklükteki değerler birlikte doğru bir şekilde işlenemez. Örneğin, 10<sup>-10</sup> ve 10<sup>10</sup>'u toplarsak, büyük olasılıkla 10<sup>10</sup> elde ederiz, çünkü küçük değer daha büyük olanla aynı büyüklüğe "dönüştürülür" ve bu nedenle mantissa kaybolur.

Çoğu aktivasyon fonksiyonu [-1..1] aralığında doğrusal olmayan özelliklere sahiptir, bu nedenle tüm giriş verilerini [-1..1] veya [0..1] aralığına ölçeklendirmek mantıklıdır.

## Başlangıç Ağırlıklarının Başlatılması

İdeal olarak, ağ katmanlarından geçtikten sonra değerlerin aynı aralıkta olmasını isteriz. Bu nedenle, ağırlıkları değerlerin dağılımını koruyacak şekilde başlatmak önemlidir.

**N(0,1)** normal dağılımı iyi bir fikir değildir, çünkü *n* girişimiz varsa, çıktının standart sapması *n* olur ve değerler muhtemelen [0..1] aralığından çıkar.

Sıkça kullanılan başlangıç yöntemleri şunlardır:

- Uniform dağılım -- `uniform`
- **N(0,1/n)** -- `gaussian`
- **N(0,1/√n_in)**, sıfır ortalama ve standart sapması 1 olan girişler için aynı ortalama/standart sapmanın korunmasını garanti eder
- **N(0,√2/(n_in+n_out))** -- **Xavier başlatması** (`glorot`) olarak adlandırılır, bu yöntem sinyalleri hem ileri hem de geri yayılım sırasında aralıkta tutmaya yardımcı olur

## Batch Normalizasyonu

Doğru ağırlık başlatmasıyla bile, eğitim sırasında ağırlıklar keyfi olarak büyüyebilir veya küçülebilir ve bu da sinyalleri uygun aralıktan çıkarabilir. Sinyalleri geri getirmek için **normalizasyon** tekniklerinden biri kullanılabilir. Birkaç normalizasyon yöntemi (Ağırlık normalizasyonu, Katman Normalizasyonu) olmasına rağmen, en sık kullanılanı Batch Normalizasyonudur.

**Batch normalizasyonu** fikri, minibatch'teki tüm değerleri dikkate almak ve bu değerlere dayalı olarak normalizasyon (örneğin, ortalamayı çıkarmak ve standart sapmaya bölmek) yapmaktır. Bu, ağırlıklar uygulandıktan sonra ancak aktivasyon fonksiyonundan önce bu normalizasyonu gerçekleştiren bir ağ katmanı olarak uygulanır. Sonuç olarak, daha yüksek nihai doğruluk ve daha hızlı eğitim elde etme olasılığımız artar.

İşte batch normalizasyonu hakkında [orijinal makale](https://arxiv.org/pdf/1502.03167.pdf), [Wikipedia'daki açıklama](https://en.wikipedia.org/wiki/Batch_normalization) ve [iyi bir giriş blog yazısı](https://towardsdatascience.com/batch-normalization-in-3-levels-of-understanding-14c2da90a338) (ve [Rusça bir yazı](https://habrahabr.ru/post/309302/)).

## Dropout

**Dropout**, eğitim sırasında rastgele bir yüzde nöronu kaldıran ilginç bir tekniktir. Bu, bir parametreye (genellikle %10-%50 oranında nöron kaldırma) sahip bir katman olarak uygulanır ve eğitim sırasında giriş vektörünün rastgele elemanlarını sıfırlar, ardından bir sonraki katmana iletir.

Bu garip bir fikir gibi görünse de, dropout'un MNIST rakam sınıflandırıcısını eğitme üzerindeki etkisini [`Dropout.ipynb`](../../../../../lessons/4-ComputerVision/08-TransferLearning/Dropout.ipynb) defterinde görebilirsiniz. Eğitim sürecini hızlandırır ve daha az eğitim dönemiyle daha yüksek doğruluk elde etmemizi sağlar.

Bu etki birkaç şekilde açıklanabilir:

- Model için rastgele bir şok etkisi olarak düşünülebilir, bu da optimizasyonu yerel minimumdan çıkarır
- *Dolaylı model ortalaması* olarak düşünülebilir, çünkü dropout sırasında biraz farklı bir model eğitiyoruz diyebiliriz

> *Bazı insanlar, sarhoş bir kişinin bir şey öğrenmeye çalıştığında, ertesi sabah ayık bir kişiye kıyasla bunu daha iyi hatırlayacağını söyler, çünkü bazı işlevsiz nöronlara sahip bir beyin, anlamı daha iyi kavramak için daha iyi adapte olmaya çalışır. Bunun doğru olup olmadığını kendimiz hiç test etmedik.*

## Aşırı Öğrenmeyi Önleme

Derin öğrenmenin çok önemli bir yönü, [aşırı öğrenmeyi](../../3-NeuralNetworks/05-Frameworks/Overfitting.md) önleyebilmektir. Çok güçlü bir sinir ağı modeli kullanmak cazip gelse de, model parametrelerinin sayısını eğitim örneklerinin sayısıyla dengelemeliyiz.

> Daha önce tanıttığımız [aşırı öğrenme](../../3-NeuralNetworks/05-Frameworks/Overfitting.md) kavramını anladığınızdan emin olun!

Aşırı öğrenmeyi önlemenin birkaç yolu vardır:

- Erken durdurma -- doğrulama setindeki hatayı sürekli izlemek ve doğrulama hatası artmaya başladığında eğitimi durdurmak
- Açık Ağırlık Azalması / Düzenleme -- ağırlıkların yüksek mutlak değerleri için kayıp fonksiyonuna ekstra bir ceza eklemek, bu da modelin çok kararsız sonuçlar üretmesini önler
- Model Ortalaması -- birkaç model eğitmek ve ardından sonucu ortalamak. Bu, varyansı minimize etmeye yardımcı olur.
- Dropout (Dolaylı Model Ortalaması)

## Optimizasyon Yöntemleri / Eğitim Algoritmaları

Eğitimdeki bir diğer önemli yön, iyi bir eğitim algoritması seçmektir. Klasik **gradyan inişi** makul bir seçim olsa da, bazen çok yavaş olabilir veya başka sorunlara yol açabilir.

Derin öğrenmede, eğitim setinden rastgele seçilen minibatch'lere uygulanan bir gradyan inişi olan **Stokastik Gradyan İnişi** (SGD) kullanırız. Ağırlıklar şu formülle ayarlanır:

w<sup>t+1</sup> = w<sup>t</sup> - η∇ℒ

### Momentum

**Momentumlu SGD**'de, önceki adımlardan bir gradyan kısmını tutarız. Bu, bir yere ataletle hareket ederken farklı bir yönde bir darbe aldığımızda, yörüngemizin hemen değişmemesine, ancak orijinal hareketin bir kısmını korumasına benzer. Burada *hız*ı temsil eden başka bir vektör v tanıtırız:

- v<sup>t+1</sup> = γ v<sup>t</sup> - η∇ℒ
- w<sup>t+1</sup> = w<sup>t</sup>+v<sup>t+1</sup>

Burada γ parametresi, ataletin ne ölçüde dikkate alındığını gösterir: γ=0 klasik SGD'ye karşılık gelir; γ=1 saf bir hareket denklemidir.

### Adam, Adagrad, vb.

Her katmanda sinyalleri bir W<sub>i</sub> matrisiyle çarptığımız için, ||W<sub>i</sub>||'ye bağlı olarak gradyan ya küçülüp 0'a yaklaşabilir ya da sonsuza kadar artabilir. Bu, Patlayan/Kaybolan Gradyanlar probleminin özüdür.

Bu sorunun çözümlerinden biri, denklemde yalnızca gradyanın yönünü kullanmak ve mutlak değeri göz ardı etmektir, yani:

w<sup>t+1</sup> = w<sup>t</sup> - η(∇ℒ/||∇ℒ||), burada ||∇ℒ|| = √∑(∇ℒ)<sup>2</sup>

Bu algoritmaya **Adagrad** denir. Aynı fikri kullanan diğer algoritmalar: **RMSProp**, **Adam**

> **Adam**, birçok uygulama için çok verimli bir algoritma olarak kabul edilir, bu yüzden hangi algoritmayı kullanacağınızdan emin değilseniz - Adam'ı kullanın.

### Gradyan Kırpma

Gradyan kırpma, yukarıdaki fikrin bir uzantısıdır. ||∇ℒ|| ≤ θ olduğunda, ağırlık optimizasyonunda orijinal gradyanı dikkate alırız ve ||∇ℒ|| > θ olduğunda, gradyanı normuna böleriz. Burada θ bir parametredir, çoğu durumda θ=1 veya θ=10 alabiliriz.

### Öğrenme Oranı Azaltma

Eğitim başarısı genellikle öğrenme oranı parametresi η'ya bağlıdır. Daha büyük η değerlerinin daha hızlı eğitimle sonuçlanacağını varsaymak mantıklıdır, bu genellikle eğitimin başında istediğimiz bir şeydir ve ardından daha küçük η değerleri ağı ince ayar yapmamıza olanak tanır. Bu nedenle, çoğu durumda eğitim sürecinde η'yı azaltmak isteriz.

Bu, her eğitim döneminden sonra η'yı bir sayı (ör. 0.98) ile çarparak veya daha karmaşık bir **öğrenme oranı planı** kullanarak yapılabilir.

## Farklı Ağ Mimarileri

Sorununuz için doğru ağ mimarisini seçmek zor olabilir. Normalde, belirli görevimiz (veya benzeri bir görev) için işe yaradığı kanıtlanmış bir mimariyi alırız. İşte bilgisayarla görme için sinir ağı mimarilerinin [iyi bir özeti](https://www.topbots.com/a-brief-history-of-neural-network-architectures/).

> Sahip olduğumuz eğitim örneklerinin sayısı için yeterince güçlü bir mimari seçmek önemlidir. Çok güçlü bir model seçmek [aşırı öğrenme](../../3-NeuralNetworks/05-Frameworks/Overfitting.md) ile sonuçlanabilir.

Başka bir iyi yöntem, gerekli karmaşıklığa otomatik olarak uyum sağlayacak bir mimari kullanmaktır. Belirli bir ölçüde, **ResNet** mimarisi ve **Inception** kendini ayarlayabilir. [Bilgisayarla görme mimarileri hakkında daha fazla bilgi](../07-ConvNets/CNN_Architectures.md).

**Feragatname**:  
Bu belge, AI çeviri hizmeti [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba göstersek de, otomatik çevirilerin hata veya yanlışlık içerebileceğini lütfen unutmayın. Belgenin orijinal dili, yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımından kaynaklanan yanlış anlamalar veya yanlış yorumlamalar için sorumluluk kabul etmiyoruz.