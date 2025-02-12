# Derin Öğrenme Eğitim İpuçları

Sinir ağları daha derin hale geldikçe, bunların eğitimi süreci giderek daha zor hale geliyor. Ana sorunlardan biri, sözde [kaybolan gradyanlar](https://en.wikipedia.org/wiki/Vanishing_gradient_problem) veya [patlayan gradyanlar](https://deepai.org/machine-learning-glossary-and-terms/exploding-gradient-problem#:~:text=Exploding%20gradients%20are%20a%20problem,updates%20are%20small%20and%20controlled.). [Bu yazı](https://towardsdatascience.com/the-vanishing-exploding-gradient-problem-in-deep-neural-networks-191358470c11) bu sorunlara iyi bir giriş yapmaktadır.

Derin ağların eğitimini daha verimli hale getirmek için kullanılabilecek birkaç teknik bulunmaktadır.

## Değerleri makul bir aralıkta tutmak

Sayısal hesaplamaların daha kararlı olmasını sağlamak için, sinir ağımız içindeki tüm değerlerin genellikle [-1..1] veya [0..1] aralığında olmasını sağlamak istiyoruz. Bu çok katı bir gereklilik değildir, ancak kayan nokta hesaplamalarının doğası gereği farklı büyüklükteki değerlerin birlikte doğru bir şekilde işlenememesi gibi bir durum söz konusudur. Örneğin, 10<sup>-10</sup> ile 10<sup>10</sup>'i toplarsak, muhtemelen 10<sup>10</sup>'i alırız çünkü daha küçük değer, daha büyük olanla aynı düzeye "dönüştürülür" ve böylece mantissa kaybolur.

Çoğu aktivasyon fonksiyonu [-1..1] etrafında doğrusal olmayanlıklar taşır, bu nedenle tüm giriş verilerini [-1..1] veya [0..1] aralığına ölçeklendirmek mantıklıdır.

## İlk Ağırlık Başlatma

İdeal olarak, değerlerin ağ katmanlarından geçtikten sonra aynı aralıkta olmasını istiyoruz. Bu nedenle, değerlerin dağılımını koruyacak şekilde ağırlıkları başlatmak önemlidir.

Normal dağılım **N(0,1)** iyi bir fikir değildir, çünkü *n* girişi olduğunda, çıkışın standart sapması *n* olur ve değerler [0..1] aralığının dışına çıkma olasılığı yüksektir.

Aşağıdaki başlatma yöntemleri sıklıkla kullanılır:

 * Üniform dağılım -- `uniform`
 * **N(0,1/n)** -- `gaussian`
 * **N(0,1/√n_in)**, sıfır ortalamaya ve standart sapması 1 olan girişler için aynı ortalama/standart sapmanın kalmasını garanti eder
 * **N(0,√2/(n_in+n_out))** -- sözde **Xavier başlatması** (`glorot`), bu, hem ileri hem de geri yayılım sırasında sinyalleri aralıkta tutmaya yardımcı olur

## Batch Normalizasyonu

Doğru ağırlık başlatmasına rağmen, ağırlıklar eğitim sırasında rastgele büyük veya küçük hale gelebilir ve bu durum sinyalleri doğru aralığın dışına çıkarabilir. Sinyalleri geri getirmek için **normalizasyon** tekniklerinden birini kullanabiliriz. Birkaç tane vardır (Ağırlık normalizasyonu, Katman Normalizasyonu), ancak en sık kullanılanı Batch Normalizasyonudur.

**Batch normalizasyonu** fikri, minibatch içindeki tüm değerleri dikkate almak ve bu değerlere dayalı olarak normalizasyon (yani ortalamayı çıkarmak ve standart sapmaya bölmek) yapmaktır. Bu, ağırlıkların uygulanmasından sonra, ancak aktivasyon fonksiyonundan önce bu normalizasyonu yapan bir ağ katmanı olarak uygulanır. Sonuç olarak, daha yüksek nihai doğruluk ve daha hızlı eğitim görme olasılığımız vardır.

Batch normalizasyonu ile ilgili [orijinal makale](https://arxiv.org/pdf/1502.03167.pdf), [Vikipedi'deki açıklama](https://en.wikipedia.org/wiki/Batch_normalization) ve [iyi bir tanıtım blog yazısı](https://towardsdatascience.com/batch-normalization-in-3-levels-of-understanding-14c2da90a338) (ve [Rusça](https://habrahabr.ru/post/309302/) olanı) bulunmaktadır.

## Dropout

**Dropout**, eğitim sırasında rastgele nöronların belirli bir yüzdesini kaldıran ilginç bir tekniktir. Aynı zamanda bir parametre (kaldırılacak nöron yüzdesi, genellikle %10-%50) ile bir katman olarak uygulanır ve eğitim sırasında, bir sonraki katmana geçmeden önce giriş vektörünün rastgele elemanlarını sıfırlar.

Bu garip bir fikir gibi görünse de, dropout'un MNIST rakam sınıflandırıcısını eğitme üzerindeki etkisini [`Dropout.ipynb`](../../../../../lessons/4-ComputerVision/08-TransferLearning/Dropout.ipynb) defterinde görebilirsiniz. Bu, eğitimi hızlandırır ve daha az eğitim döngüsünde daha yüksek doğruluk elde etmemizi sağlar.

Bu etki birkaç şekilde açıklanabilir:

 * Model için rastgele bir şok faktörü olarak düşünülebilir, bu da optimizasyonu yerel minimumdan çıkarır
 * *İçsel model ortalaması* olarak düşünülebilir, çünkü dropout sırasında biraz farklı bir modeli eğittiğimizi söyleyebiliriz

> *Bazı insanlar, sarhoş bir kişinin bir şey öğrenmeye çalıştığında, bunun sabah daha iyi hatırlanacağını, bunun da bir sarhoş kişinin bazı işlev bozukluğu olan nöronları ile anlamı kavramaya daha iyi uyum sağlamaya çalışmasından kaynaklandığını söyler. Bunun doğru olup olmadığını kendimiz hiç test etmedik.*

## Aşırı Uydurmayı Önleme

Derin öğrenmenin çok önemli bir yönü, [aşırı uydurmayı](../../3-NeuralNetworks/05-Frameworks/Overfitting.md) önleyebilme yeteneğidir. Çok güçlü bir sinir ağı modeli kullanmak cazip olabilir, ancak her zaman model parametrelerinin sayısını eğitim örneklerinin sayısıyla dengelemeliyiz.

> Daha önce tanıttığımız [aşırı uydurma](../../3-NeuralNetworks/05-Frameworks/Overfitting.md) kavramını anladığınızdan emin olun!

Aşırı uydurmayı önlemek için birkaç yol vardır:

 * Erken durdurma -- doğrulama setindeki hatayı sürekli izleyerek, doğrulama hatası artmaya başladığında eğitimi durdurma.
 * Açık Ağırlık Çürütme / Düzenleme -- yüksek mutlak ağırlık değerleri için kayıp fonksiyonuna ekstra bir ceza ekleyerek, modelin çok dengesiz sonuçlar almasını önler
 * Model Ortalaması -- birkaç modeli eğitip ardından sonucu ortalamak. Bu, varyansı minimize etmeye yardımcı olur.
 * Dropout (İçsel Model Ortalaması)

## Optimizatörler / Eğitim Algoritmaları

Eğitimin bir diğer önemli yönü, iyi bir eğitim algoritması seçmektir. Klasik **gradyan inişi** makul bir seçimdir, ancak bazen çok yavaş olabilir veya başka sorunlara yol açabilir.

Derin öğrenmede, **Stokastik Gradyan İnişi** (SGD) kullanıyoruz; bu, eğitim setinden rastgele seçilen minibatch'lere uygulanan bir gradyan inişidir. Ağırlıklar bu formül ile ayarlanır:

w<sup>t+1</sup> = w<sup>t</sup> - η∇ℒ

### Momentum

**Momentum SGD**'de, önceki adımlardan bir gradyan kısmını saklıyoruz. Bu, bir yere ataletle hareket ederken farklı bir yönde bir darbe aldığımızda, yolculuğumuzun hemen değişmediği, ancak orijinal hareketin bir kısmını koruduğu durumla benzerdir. Burada *hız*ı temsil etmek için başka bir vektör v tanıtıyoruz:

* v<sup>t+1</sup> = γ v<sup>t</sup> - η∇ℒ
* w<sup>t+1</sup> = w<sup>t</sup>+v<sup>t+1</sup>

Burada γ parametresi, ataletin ne kadar dikkate alındığını gösterir: γ=0, klasik SGD'ye karşılık gelir; γ=1, saf hareket denklemi anlamına gelir.

### Adam, Adagrad, vb.

Her katmanda sinyalleri bazı matrislerle çarptığımız için W<sub>i</sub>, ||W<sub>i</sub>||'ya bağlı olarak, gradyan ya azalabilir ve 0'a yakın olabilir ya da sonsuz bir şekilde yükselebilir. Bu, Patlayan/Kaybolan Gradyanlar sorununu oluşturmaktadır.

Bu sorunun çözümlerinden biri, denklemin içinde yalnızca gradyanın yönünü kullanmak ve mutlak değeri görmezden gelmektir, yani

w<sup>t+1</sup> = w<sup>t</sup> - η(∇ℒ/||∇ℒ||), burada ||∇ℒ|| = √∑(∇ℒ)<sup>2</sup>

Bu algoritmaya **Adagrad** denir. Aynı fikri kullanan diğer algoritmalar: **RMSProp**, **Adam**

> **Adam**, birçok uygulama için çok etkili bir algoritma olarak kabul edilir, bu nedenle hangi algoritmayı kullanacağınızdan emin değilseniz - Adam'ı kullanın.

### Gradyan kesme

Gradyan kesme, yukarıdaki fikrin bir uzantısıdır. ||∇ℒ|| ≤ θ olduğunda, ağırlık optimizasyonunda orijinal gradyanı dikkate alıyoruz ve ||∇ℒ|| > θ olduğunda - gradyanı normu ile bölüyoruz. Burada θ bir parametredir; çoğu durumda θ=1 veya θ=10 alabiliriz.

### Öğrenme oranı azaltma

Eğitim başarısı genellikle öğrenme oranı parametresi η'ye bağlıdır. Daha büyük η değerlerinin daha hızlı bir eğitim sağladığını varsaymak mantıklıdır; bu, genellikle eğitim sürecinin başında istediğimiz bir şeydir ve ardından daha küçük η değerleri, ağın ince ayarını yapmamıza olanak tanır. Bu nedenle, çoğu durumda η'yi eğitim sürecinde azaltmak isteriz.

Bu, her eğitim döngüsünden sonra η'yi bazı sayılarla (örneğin 0.98) çarparak veya daha karmaşık bir **öğrenme oranı takvimi** kullanarak yapılabilir.

## Farklı Ağ Mimarileri

Probleminiz için doğru ağ mimarisini seçmek zor olabilir. Normalde, belirli görevimiz (veya benzer bir görev) için işe yaradığını kanıtlamış bir mimari seçeriz. İşte bilgisayarla görme için sinir ağı mimarileri hakkında [iyi bir genel bakış](https://www.topbots.com/a-brief-history-of-neural-network-architectures/) bulunmaktadır.

> Eğitim örneklerimizin sayısı için yeterince güçlü bir mimari seçmek önemlidir. Çok güçlü bir model seçmek [aşırı uydurma](../../3-NeuralNetworks/05-Frameworks/Overfitting.md) ile sonuçlanabilir.

Bir diğer iyi yol, gerekli karmaşıklığa otomatik olarak uyum sağlayacak bir mimari kullanmaktır. Belirli bir ölçüde, **ResNet** mimarisi ve **Inception** kendiliğinden ayarlanan mimarilerdir. [Bilgisayarla görme mimarileri hakkında daha fazla bilgi](../07-ConvNets/CNN_Architectures.md) bulunmaktadır.

**Açıklama**:  
Bu belge, makine tabanlı AI çeviri hizmetleri kullanılarak çevrilmiştir. Doğruluğa özen göstersek de, otomatik çevirilerin hatalar veya yanlışlıklar içerebileceğini lütfen dikkate alınız. Orijinal belge, kendi dilinde yetkili kaynak olarak değerlendirilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilmektedir. Bu çevirinin kullanılması sonucunda oluşabilecek yanlış anlamalardan veya yanlış yorumlamalardan sorumlu değiliz.