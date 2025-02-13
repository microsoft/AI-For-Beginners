# Etik ve Sorumlu AI

Bu kursu neredeyse tamamladınız ve umarım artık AI'nın verilerdeki ilişkileri bulmamıza ve insan davranışının bazı yönlerini kopyalamak için modelleri eğitmemize olanak tanıyan bir dizi resmi matematiksel yönteme dayandığını net bir şekilde görüyorsunuzdur. Tarihsel olarak bu noktada, AI'yı verilerden desenler çıkarmak ve bu desenleri yeni problemleri çözmek için uygulamak için çok güçlü bir araç olarak değerlendiriyoruz.

## [Ön ders anketi](https://white-water-09ec41f0f.azurestaticapps.net/quiz/5/)

Ancak bilim kurgu eserlerinde, AI'nın insanlığa bir tehlike oluşturduğu hikayelere sıkça rastlıyoruz. Genellikle bu hikayeler, AI'nın insanlarla yüzleşmeye karar verdiği bir AI isyanı etrafında döner. Bu, AI'nın bir tür duygusunun olduğu veya geliştiricileri tarafından öngörülemeyen kararlar alabileceği anlamına gelir.

Bu kursta öğrendiğimiz AI türü, büyük matris aritmetiğinden başka bir şey değildir. Sorunlarımızı çözmemize yardımcı olmak için çok güçlü bir araçtır ve diğer güçlü araçlar gibi - iyi ve kötü amaçlar için kullanılabilir. Önemli olan, bunun *kötüye kullanılabileceğidir*.

## Sorumlu AI İlkeleri

AI'nın bu kazara veya kasıtlı kötüye kullanımını önlemek için Microsoft, önemli [Sorumlu AI İlkeleri](https://www.microsoft.com/ai/responsible-ai?WT.mc_id=academic-77998-cacaste) belirlemektedir. Bu ilkeleri destekleyen bazı kavramlar şunlardır:

* **Adalet**, *model önyargıları* ile ilgili önemli bir sorunla ilgilidir; bu önyargılar, eğitim için önyargılı verilerin kullanılmasıyla ortaya çıkabilir. Örneğin, bir kişinin yazılım geliştirici işine kabul edilme olasılığını tahmin etmeye çalıştığımızda, model muhtemelen erkeklere daha yüksek bir öncelik verecektir - çünkü eğitim veri seti muhtemelen erkek izleyicilere yönelik önyargılıydı. Eğitim verilerini dikkatlice dengelememiz ve modelin önyargılardan kaçınması için araştırmamız gerekiyor ve modelin daha ilgili özellikleri dikkate aldığından emin olmalıyız.
* **Güvenilirlik ve Güvenlik**. Doğası gereği, AI modelleri hata yapabilir. Bir sinir ağı olasılıkları döndürür ve kararlar alırken bunu dikkate almamız gerekir. Her modelin bir kesinliği ve geri çağırma oranı vardır ve yanlış tavsiyelerin neden olabileceği zararı önlemek için bunu anlamamız gerekir.
* **Gizlilik ve Güvenlik**, AI'ya özgü bazı sonuçlar taşır. Örneğin, bir modeli eğitmek için bazı verileri kullandığımızda, bu veriler bir şekilde modelin içine "entegrasyon" haline gelir. Bir yandan bu güvenliği ve gizliliği artırır, diğer yandan modelin hangi verilerle eğitildiğini hatırlamamız gerekir.
* **Kapsayıcılık**, AI'yı insanların yerini almak için değil, insanların yeteneklerini artırmak ve işimizi daha yaratıcı hale getirmek için inşa ettiğimiz anlamına gelir. Ayrıca adaletle de ilişkilidir, çünkü temsil edilmeyen topluluklarla ilgilendiğimizde, topladığımız veri setlerinin çoğu muhtemelen önyargılı olacaktır ve bu toplulukların AI tarafından dahil edilmesini ve doğru bir şekilde ele alınmasını sağlamalıyız.
* **Şeffaflık**. Bu, AI'nın kullanımında her zaman net olmamızı sağlamayı içerir. Ayrıca, mümkün olduğunca, *yorumlanabilir* AI sistemlerini kullanmak isteriz.
* **Hesap verebilirlik**. AI modelleri bazı kararlar aldığında, bu kararların kimin sorumluluğunda olduğu her zaman net değildir. AI kararlarının sorumluluğunun nerede olduğunu anlamamız gerekir. Çoğu durumda, önemli kararlar alma sürecine insanları dahil etmek isteriz, böylece gerçek insanlar sorumlu tutulabilir.

## Sorumlu AI Araçları

Microsoft, bir dizi araç içeren [Sorumlu AI Araç Kutusu](https://github.com/microsoft/responsible-ai-toolbox) geliştirmiştir:

* Yorumlanabilirlik Gösterge Tablosu (InterpretML)
* Adalet Gösterge Tablosu (FairLearn)
* Hata Analizi Gösterge Tablosu
* Sorumlu AI Gösterge Tablosu, şunları içerir:

   - EconML - Neden-sonuç analizi için bir araç, "ya ne olursa" sorularına odaklanır
   - DiCE - Karşıfaktüel Analiz için bir araç, modelin kararını etkilemek için hangi özelliklerin değiştirilmesi gerektiğini görmenizi sağlar

AI Etiği hakkında daha fazla bilgi için, [bu dersi](https://github.com/microsoft/ML-For-Beginners/tree/main/1-Introduction/3-fairness?WT.mc_id=academic-77998-cacaste) ziyaret edin; bu ders, ödevler içeren Makine Öğrenimi Müfredatına aittir.

## Gözden Geçirme ve Kendi Kendine Çalışma

Sorumlu AI hakkında daha fazla bilgi edinmek için bu [Öğrenme Yolu](https://docs.microsoft.com/learn/modules/responsible-ai-principles/?WT.mc_id=academic-77998-cacaste)nu takip edin.

## [Ders sonrası anket](https://white-water-09ec41f0f.azurestaticapps.net/quiz/6/)

**Açıklama**:  
Bu belge, makine tabanlı AI çeviri hizmetleri kullanılarak çevrilmiştir. Doğruluk için çaba göstersek de, otomatik çevirilerin hatalar veya yanlış anlamalar içerebileceğini lütfen dikkate alınız. Orijinal belge, kendi dilinde otorite kaynağı olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilmektedir. Bu çevirinin kullanımından kaynaklanan yanlış anlamalar veya yanlış yorumlamalardan dolayı sorumluluk kabul etmiyoruz.